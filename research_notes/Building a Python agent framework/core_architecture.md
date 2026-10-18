# Core Architecture of a Custom Python Agent Framework

## The Agent Loop

### Takeaway
The canonical agent loop is a ReAct-shaped cycle: assemble model input from state → call the LLM → if there are no tool calls, return a final output; otherwise execute the tool calls (in parallel where independent) → append tool results to history → repeat, bounded by `max_turns`/termination. Frameworks differ in control-flow substrate (implicit loop vs. graph vs. event-driven state machine), but all reduce to this shape.

### Cited Findings
- OpenAI defines an agent as Model + Tools + Instructions; the single-agent loop exits on tool calls, structured output, errors, or `max_turns`; `Runner.run()` loops until a final-output tool is invoked or the model returns text with no tool calls — [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/); [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- OpenAI Agents SDK loop steps: (1) call LLM for current agent with current input; (2) inspect output; (3a) final output → end; (3b) handoff → switch agent and re-run; (3c) tool calls → execute and append results, re-run; (4) exceed `max_turns` → `MaxTurnsExceeded` (`max_turns=None` disables) — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Anthropic: agents are LLMs using tools based on environmental feedback in a loop; they gain ground truth each step, can pause for human feedback, and require explicit stopping conditions; test in sandboxes with guardrails — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- ReAct is the default shape of most "agent" abstractions (LangChain's `create_agent`, Pydantic AI's `CallToolsNode` loop, OpenAI Agents SDK, smolagents); frameworks expose primitives (graph nodes, steps, events, handoffs) onto which patterns are layered rather than hard-coding one loop — [opensource survey §cross-cutting](https://docs.langchain.com/oss/python/langgraph/overview).
- LangGraph models an agent as a directed `StateGraph` over a typed state object executed by a Pregel runtime (`.stream()`/`.invoke()`); HITL via `interrupt()` which pauses and saves state via a checkpointer — [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview); [interrupts doc](https://docs.langchain.com/oss/python/langgraph/interrupts).
- Pydantic AI wraps a pydantic-graph state machine; `agent.iter()` yields `UserPromptNode`, `ModelRequestNode`, `CallToolsNode`, `End`; manual driving via `agent_run.next(node)` — [Pydantic AI agents](https://pydantic.dev/docs/ai/core-concepts/agent/).
- ADK: `Runner` orchestrates; agent/tool/callback yields `Event` and pauses; `Runner` commits via services then resumes; async is primary (`run_async`) — [ADK event loop](https://google.github.io/adk-docs/runtime/event-loop/).
- AutoGen: conversation-centric; `AssistantAgent`s broadcast `TextMessage`/`ToolCallRequestEvent`/`HandoffMessage` into a shared thread; teams (`RoundRobinGroupChat`, `SelectorGroupChat`, `Swarm`, `GraphFlow`) define turn-taking and termination — [AutoGen Swarm](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html).
- CrewAI: `Crew` executes `Task`s under `Process.sequential` or `Process.hierarchical` (manager agent coordinates/delegates/validates); kickoff variants and checkpointing — [Crews doc](https://docs.crewai.com/en/concepts/crews).
- LlamaIndex Workflows: event-driven, step-based; `@step` methods whose type annotations (input event → output event) define graph edges; `StartEvent`/`StopEvent` mark entry/exit; fan-out via `list[Event]`, fan-in via `list[Event]` param — [Workflows intro](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
- smolagents: `CodeAgent`/`ToolCallingAgent` loop runs until a `final_answer` tool call or `max_steps`; `final_answer_checks` validators enable self-validation — [smolagents guided tour](https://huggingface.co/docs/smolagents/guided_tour).

**Termination conditions** (from sources): no tool calls / final output (text or structured); `max_turns` exceeded; handoff transferring control; HITL interrupt/pause; guardrail tripwire; `final_answer` tool call (smolagents); `exit_loop` setting `escalate=True` (ADK `LoopAgent`); `StopEvent` (LlamaIndex); `MaxMessageTermination` (AutoGen).

### Inferences
Minimal, buildable loop skeleton (start here; add hooks/checkpointing later):

```python
class AgentLoop:
    async def run(self, state: AgentState) -> RunResult:
        for turn in range(self.max_turns):
            await self.hooks.before_model(state)
            resp = await self.model.chat(state.messages, tools=self.tools.schemas(),
                                        response_format=self.output_schema)
            state.messages.append(resp.assistant_message)
            if not resp.tool_calls:
                return RunResult(final=resp.parsed or resp.text, state=state,
                                 usage=state.usage)
            await self.hooks.before_tools(resp.tool_calls)
            results = await self.tools.execute_all(resp.tool_calls)  # parallel where safe
            state.messages.extend(results)
            await self.hooks.after_turn(state)
        raise MaxTurnsExceeded(self.max_turns)
```

**Substrate trade-offs:** an implicit async loop (smolagents / OpenAI SDK style) is simplest and easiest to debug but hard to make durable or resumable; a graph (LangGraph) is flexible and checkpointable but carries boilerplate and v1→v2 API churn; an event-driven state machine (LlamaIndex / ADK) is composable and resumable but complex. Recommendation: start with an implicit async loop with `before_model`/`before_tools`/`after_turn` hook points so it can be migrated to a graph later without rewriting tool/model code.

**Sync vs. async:** ADK, Pydantic AI, and OpenAI SDK treat async as primary with sync wrappers; prefer async end-to-end and offer `run_sync` wrappers, since tool I/O and streaming are inherently async.

### Gaps
- Exact Pregel channel/worker mechanics and `Command` dispatch internals (LangGraph) are not captured beyond docs; source inspection needed for a faithful reimplementation.
- The OpenAI Agents SDK's internal `Runner` concurrency and tool-execution scheduling details (`ToolExecutionConfig.max_function_tool_concurrency`) are referenced but not deeply documented.

---

## Model Abstraction

### Takeaway
Build a provider-agnostic client around a small interface: `chat(messages, tools, response_format) → ModelResponse`, `stream(...) → AsyncIterator[StreamEvent]`, `count_tokens(...) → int`, with usage/cost tracked on every response. Normalize provider payloads (OpenAI Responses/Chat Completions, Anthropic Messages, Gemini `generateContent`) to an internal message/item representation. Retries, rate limits, and token counting are cross-cutting concerns that most frameworks leave to user configuration.

### Cited Findings
- OpenAI recommends the Responses API for new agent projects (stateful-by-default, typed Items, multi-tool agentic loop in one request, built-in tools, preserved reasoning state, 40–80% cache improvement); Chat Completions remains stateless and message-based — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- OpenAI Agents SDK is model-agnostic via Chat Completions-style endpoints and supports other providers; `Agent.model`/`model_settings` and `RunConfig` overrides — [Agents SDK](https://openai.github.io/openai-agents-python/); [running_agents](https://openai.github.io/openai-agents-python/running_agents/).
- Anthropic tool use: Claude emits `tool_use` blocks; client tools yield `stop_reason: "tool_use"` and the client returns `tool_result`; `strict: true` guarantees schema conformance; tool use adds system-prompt tokens — [Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).
- ADK: `LlmAgent.model` is a required string id (e.g. `"gemini-flash-latest"`); `generate_content_config`, `thinking_config` (`include_thoughts`, `thinking_budget`); global default via `LlmAgent.set_default_model()` — [ADK LlmAgent](https://google.github.io/adk-docs/agents/llm-agents/).
- smolagents is model-agnostic via `InferenceClientModel`, `LiteLLMModel`, `TransformersModel`, etc. — [smolagents guided tour](https://huggingface.co/docs/smolagents/guided_tour).
- Gemini native capabilities: function calling, code execution, Google Search grounding, URL context, safety filters via `generate_content_config.safety_settings` — [ADK safety](https://google.github.io/adk-docs/safety/); [ADK LlmAgent](https://google.github.io/adk-docs/agents/llm-agents/).
- Responses API preserves reasoning state across turns (Chat drops it), boosting TAUBench +5% with GPT-5 — [Why we built Responses API](https://developers.openai.com/blog/responses-api).
- Anthropic prompt caching: cache prefix order tools → system → messages; default 5-min TTL (refreshed free on use), optional 1-hour at 2× base; writes 1.25×/2×, reads 0.1×; min cacheable length varies (1024–4096 tokens) — [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).

### Inferences
Provider-agnostic interface sketch:

```python
class ModelClient(Protocol):
    async def chat(self, messages: list[Message], *, tools: list[dict] | None = None,
                   response_format: type[BaseModel] | None = None,
                   settings: ModelSettings | None = None) -> ModelResponse: ...
    def stream(self, messages, *, tools=None, response_format=None,
               settings=None) -> AsyncIterator[StreamEvent]: ...
    def count_tokens(self, messages: list[Message]) -> int: ...

@dataclass
class ModelResponse:
    text: str | None
    tool_calls: list[ToolCall]          # id, name, arguments (parsed dict)
    reasoning: str | None
    usage: Usage                       # input/output/cached tokens, cost_usd
    raw: Any                           # provider payload for debugging
    finish_reason: str
```

**Normalization note:** model the internal turn as a sequence of typed "items" (message, function_call, function_call_output, reasoning) rather than flat messages, so both client-managed and server-managed (Responses `previous_response_id`) state work — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).

**Retries/rate limits:** exponential backoff on 429/5xx with jitter; per-provider token bucket; circuit breaker. Only CrewAI ships a built-in `max_rpm`; otherwise these are user config — [opensource survey §memory](https://docs.crewai.com/en/concepts/crews).

**Trade-offs:** Responses API is richer but provider-specific; Chat Completions is the portable lowest common denominator. A framework targeting multiple providers should implement against Chat Completions semantics and add Responses-specific optimizations (reasoning state, built-in tools) as optional capabilities.

### Gaps
- Exact Responses API function-calling JSON shapes (tool definition `type: function` with `name`/`parameters`/`strict`, `tool_choice` enum values) were not fully captured from official docs.
- Provider-specific retry/backoff policies and token-bucket implementations are not documented in these sources; would require source inspection.

---

## Tool System

### Takeaway
Tools are Python functions whose signatures and docstrings become JSON schemas (via `inspect`/Pydantic). The framework validates arguments, executes (async, in parallel where safe), and returns structured results; errors are returned to the model as tool results for retry rather than raised. MCP standardizes discovery/invocation across processes. Tool descriptions are the durable interface contract.

### Cited Findings
- OpenAI function calling: model emits `function_call` items with `call_id`; app executes and returns `function_call_output` linked by `call_id`; `parallel_tool_calls` true by default; `max_tool_calls` caps built-in tool calls per response — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- Anthropic tool use: Claude decides when to call based on request + tool description; returns `tool_use` blocks; client tools yield `stop_reason: "tool_use"`; `strict: true` guarantees schema conformance — [Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).
- OpenAI practical guide: tool types Data (retrieve context), Action (mutate external systems), Orchestration (agents as tools); standardized definitions enabling flexible many-to-many tool/agent relationships; well-documented, tested, reusable tools improve discoverability/versioning — [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- OpenAI o3/o4-mini guide: use the `tools` field (not manual prompt injection); descriptions should state when to invoke and how to build arguments; usage criteria refine proactiveness; developer instructions disambiguate similar tools and preferred ordering; guard against hallucinations via explicit "do not promise future calls", `strict: true`, arg validation, history summarization — [o3/o4-mini prompting guide](https://d2a346aex646576656c6f70657273x6f70656e6169x636f6d.gateway.web.tr/https/cookbook/examples/o-series/o3o4-mini_prompting_guide).
- Anthropic on tool design: invest in the agent-computer interface; choose formats the model writes easily (close to natural internet text, no formatting overhead); give tokens to think; poka-yoke arguments; require absolute filepaths (fixed SWE-bench errors) — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- Anthropic "writing tools for agents": generate dozens of realistic multi-step tasks; run simple agentic while-loops; collect metrics (runtime, tool calls, tokens, errors); analyze transcripts; held-out test sets to avoid overfitting; tool description tweaks yielded large gains — [writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).
- Pydantic AI: tools registered via `@agent.tool`/`@agent.tool_plain`; receive `RunContext[deps_type]`; docstrings become descriptions; arguments validated by Pydantic; errors returned to model for retry — [Pydantic AI agents](https://pydantic.dev/docs/ai/core-concepts/agent/).
- smolagents: `@tool` decorator on typed functions with docstrings, or `Tool` subclass with `name`/`description`/`inputs`/`output_type`/`forward` — [smolagents guided tour](https://huggingface.co/docs/smolagents/guided_tour).
- ADK: native Python functions auto-wrapped as `FunctionTool`; docstrings + type hints drive schema; tools return dict/Map; `ToolContext` provides state, auth, memory search — [ADK LlmAgent](https://google.github.io/adk-docs/agents/llm-agents/).
- OpenAI Agents SDK: function tools with auto schema + Pydantic validation; MCP server tool calling; tool guardrails wrap `FunctionTool` with input/output validation and can reject/replace content — [Agents SDK](https://openai.github.io/openai-agents-python/); [guardrails doc](https://openai.github.io/openai-agents-python/guardrails/).
- MCP: tools discovered via `tools/list`, executed via `tools/call` over JSON-RPC 2.0; stateless with protocol version/capabilities in `_meta` — [MCP intro](https://modelcontextprotocol.io/introduction); [MCP architecture](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture).
- OpenAI on tool overload: similarity/overlap matters more than raw count (>15 distinct tools can work, <10 overlapping can fail) — [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).

**Tool schema contract (cross-provider):** an object with `name`, `description`, and `parameters` (JSON Schema: `type: "object"`, `properties`, `required`). OpenAI strict mode requires all params in `required` and `additionalProperties: false`. Anthropic uses `input_schema`. MCP's `tools/list` returns `name`/`description`/`inputSchema`.

### Inferences
Design sketch:

```python
def tool(func=None, *, name=None, description=None, concurrency_safe=False):
    # introspect signature -> pydantic model via TypeAdapter
    ...

class ToolRegistry:
    def schemas(self) -> list[dict]: ...          # provider-formatted
    async def execute(self, call: ToolCall) -> ToolResult: ...
    async def execute_all(self, calls: list[ToolCall]) -> list[ToolResult]:
        # read-only/concurrency_safe tools run via asyncio.gather;
        # stateful tools run sequentially in call order
        ...

@dataclass
class ToolResult:
    call_id: str
    content: str | list[ContentPart]   # text or structured
    is_error: bool = False
    metadata: dict = field(default_factory=dict)
```

**Execution policy:** validate args with Pydantic; on `ValidationError` or exception, return `ToolResult(is_error=True, content=str(exc))` so the model can retry ("reflection and self-correction" — Pydantic AI). Never raise into the loop. Support parallel calls via `asyncio.gather` only when tools declare `concurrency_safe=True` or are read-only; otherwise sequential to avoid state corruption.

**Guardrails:** wrap tools with input/output validators that can reject or replace content (OpenAI tool guardrails pattern); tripwires raise terminal exceptions for catastrophic violations.

**Trade-offs:** JSON tool-calling is portable and model-native; code-as-action (smolagents `CodeAgent`) is more expressive for composability but requires a sandboxed interpreter and import allowlists. Start with JSON tool-calling; add code execution as a single sandboxed tool.

### Gaps
- Exact Pydantic extraction of JSON Schema from arbitrary function signatures (nested types, generics, `Annotated` metadata) is library-dependent; `pydantic.TypeAdapter(func_signature)` patterns vary by version.
- No standardized heuristic for detecting concurrency safety; frameworks leave it to tool authors.

---

## Context / Memory Management

### Takeaway
Represent history as typed messages/items; budget tokens per request; on overflow, compact (summarize) older turns or clear stale tool results; keep a per-run scratchpad; use just-in-time retrieval for long-term memory; place prompt-cache breakpoints on stable prefixes. Anthropic frames this as "context engineering": curate the optimal token set each step because LLM attention degrades as context grows (context rot).

### Cited Findings
- Anthropic context engineering (Sep 29, 2025): context is finite with diminishing returns; transformer attention is n² pairwise; longer contexts reduce recall (context rot). System prompts at the "right altitude" between brittle hardcoded logic and vague guidance; organize into sections (XML/Markdown); minimal but sufficient. Tools must be token-efficient and self-contained; avoid bloated/overlapping tool sets. Few-shot: diverse canonical examples, not laundry lists of edge cases. Just-in-time retrieval: keep lightweight identifiers (paths, queries, links) and load data at runtime via tools; progressive disclosure; hybrid (some up-front + autonomous exploration). Claude Code uses `CLAUDE.md` up front + glob/grep just-in-time — [effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Long-horizon techniques: **Compaction** (summarize nearing-limit history, restart with summary; Claude Code keeps 5 most recently accessed files); **structured note-taking/agentic memory** (`NOTES.md`/TODOs); **sub-agent architectures** (isolated context windows, return 1k–2k token summaries) — [effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Memory tool: file-based system to store/consult info outside the context window; build knowledge bases over time; maintain project state across sessions — [effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Anthropic multi-agent research: lead agent saves plan to Memory because context >200k tokens gets truncated; subagent outputs written to filesystem to minimize the "telephone" game — [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system).
- LangGraph: two persistence systems — **Checkpointers** (thread-scoped graph state snapshots, short-term) and **Stores** (cross-thread key-value, long-term); `InMemorySaver`/`SqliteSaver`/`PostgresSaver` (async variants); pruning recommended for unbounded growth — [persistence doc](https://docs.langchain.com/oss/python/langgraph/persistence).
- ADK: `Session` (`id`, `app_name`, `user_id`, `events`, `state`, `last_update_time`); `SessionService` impls `InMemorySessionService`, `VertexAiSessionService`, `DatabaseSessionService` (SQL, row-level locking, `AutoMigrate`); `MemoryService`/`BaseMemoryService` with `add_session_to_memory`, `search_memory`; impls `InMemoryMemoryService` (keyword), `VertexAiMemoryBankService` (LLM-extracted), `VertexAiRagMemoryService` (vector); memory tools `load_memory`/`preload_memory`; auto-save via `after_agent_callback` — [ADK session](https://google.github.io/adk-docs/sessions/session/); [ADK memory](https://google.github.io/adk-docs/sessions/memory/).
- OpenAI Agents SDK: sessions (`SQLiteSession`, SQLAlchemy/Redis/Mongo/Dapr/encrypted); server-managed via `conversation_id`/`previous_response_id`/`auto_previous_response_id`; `nest_handoff_history` compacts transcript into summary segments — [running_agents](https://openai.github.io/openai-agents-python/running_agents/).
- CrewAI: short/long/entity memory via `memory=True` + `embedder`; checkpointing via `CheckpointConfig` (Json/Sqlite providers, `from_checkpoint` resume); flow `@persist` (SQLite) with resume/fork; LanceDB-backed `remember`/`recall`/`extract_memories` — [Crews doc](https://docs.crewai.com/en/concepts/crews); [Flows doc](https://docs.crewai.com/en/concepts/flows).
- OpenAI Responses: stateful context (`store: true`); chaining via `previous_response_id`; instructions from previous response not carried over automatically — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- Prompt caching: Anthropic cache prefix order tools → system → messages; default 5-min TTL (refreshed free), optional 1-hour at 2×; writes 1.25×/2×, reads 0.1×; lookback window 20 blocks per breakpoint; tool/system/message changes invalidate downstream caches — [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).

### Inferences
Message model and budgeting sketch:

```python
@dataclass
class Message:
    role: Literal["system", "user", "assistant", "tool"]
    content: list[ContentPart]   # text, image, tool_call, tool_result
    metadata: dict = field(default_factory=dict)  # tokens, cached, turn_id

class ContextManager:
    def __init__(self, budget_tokens: int, reserve_for_output: int = 4096):
        ...
    def build(self, state: AgentState) -> list[Message]:
        # 1. system + tools (stable, cached) first
        # 2. scratchpad summary if present
        # 3. recent turns verbatim up to budget
        # 4. if overflow: compact middle turns into a summary message
        # 5. just-in-time retrieve top-k from long-term store into context
    async def compact(self, messages, keep_last: int = 6) -> list[Message]: ...
```

**Compaction policy:** keep system + tools (cached) + last K turns verbatim; summarize the middle into a single "summary" message; clear raw tool results beyond a window (keep only their summaries); retain the 5 most recently accessed files (Claude Code heuristic). Run compaction when estimated tokens exceed ~80% of budget.

**Scratchpad vs. messages:** keep intermediate values (plans, retrieved doc IDs, tool outputs) in a per-run state dict (`session.state` in ADK terms) and inject a compact summary into messages, not the full data — reduces token bloat and enables just-in-time loading.

**Long-term memory interface:** `add(text, metadata)`, `search(query, k) → list[Memory]`; implementations: in-memory keyword, SQLite+FTS, or vector store (pgvector/Qdrant). Retrieve top-k into context only when relevant (just-in-time), not always.

**Trade-offs:** in-memory state is fast and simple but lost on restart; checkpointed/persistent state enables resume and multi-process but adds latency and serialization constraints. Summarization loses fidelity and can drop critical details; raw retention hits context limits. Vector retrieval adds latency/cost and retrieval errors.

### Gaps
- Exact compaction prompt tuning guidance is high-level ("maximize recall then precision"); exact compaction APIs/params are not detailed in the post.
- Vector DB selection benchmarks and embedding model comparisons are not covered in these sources.

---

## Prompt Construction

### Takeaway
System prompts should sit at the "right altitude" (not brittle hardcoded logic, not vague guidance), organized into sections (Identity, Instructions, Examples, Context), with tool descriptions as durable contracts and few-shot examples that are diverse and canonical. Stable prefixes come first to maximize prompt-cache hits; dynamic content last.

### Cited Findings
- Anthropic: system prompts at the "right altitude" between brittle hardcoded logic and vague guidance; organize into sections (XML/Markdown); minimal but sufficient — [effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Anthropic: few-shot examples should be diverse and canonical, not laundry lists of edge cases — [effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- OpenAI: developer instructions are high-priority; structure developer messages as Identity, Instructions, Examples, Context using Markdown/XML; GPT-4.1 agent reminders for PERSISTENCE, TOOL CALLING, PLANNING; pin model snapshots; build evals — [GPT-4.1 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide).
- OpenAI: tool descriptions should state when to invoke and how to build arguments; usage criteria refine proactiveness; developer instructions disambiguate similar tools and preferred ordering — [o3/o4-mini prompting guide](https://d2a346aex646576656c6f70657273x6f70656e6169x636f6d.gateway.web.tr/https/cookbook/examples/o-series/o3o4-mini_prompting_guide).
- OpenAI: guard against hallucinations — explicit "do not promise future calls", `strict: true`, validate arguments, discard irrelevant history/summarize — [o3/o4-mini prompting guide](https://d2a346aex646576656c6f70657273x6f70656e6169x636f6d.gateway.web.tr/https/cookbook/examples/o-series/o3o4-mini_prompting_guide).
- Anthropic: tool formats should be close to natural internet text with no formatting overhead; give tokens to think; poka-yoke arguments; require absolute filepaths — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- ADK: instructions support dynamic state templating `{var}`, `{artifact.var}`, optional `?` for missing vars; `include_contents` default `'default'` (history sent) or `'none'` (stateless) — [ADK LlmAgent](https://google.github.io/adk-docs/agents/llm-agents/).
- Anthropic prompt caching: cache prefix order tools → system → messages; place `cache_control` on the last block whose prefix is identical across requests; automatic caching moves the breakpoint forward as conversations grow — [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).

### Inferences
Prompt builder sketch:

```python
class PromptBuilder:
    def build(self, agent, state) -> PromptBundle:
        # Order matters for caching: stable first, volatile last
        system = [
            Section("identity", agent.identity),          # stable
            Section("instructions", agent.instructions), # stable
            Section("examples", agent.few_shot),          # stable
            Section("context", state.dynamic_context),    # volatile
        ]
        tools = agent.tools.schemas()                    # stable
        messages = state.messages                        # volatile
        cache_breakpoints = [after_tools, after_system]  # provider-specific
        return PromptBundle(system=system, tools=tools, messages=messages,
                            cache_breakpoints=cache_breakpoints)
```

**Design rules:** (1) never put volatile content (timestamps, user-specific data) in the cached prefix; (2) tool descriptions are part of the contract — version them and test them with held-out tasks; (3) use templating (`{var}`) for dynamic state injection rather than string concatenation; (4) include persistence/tool-calling/planning reminders for models that need them (GPT-4.1 family).

**Trade-offs:** richly structured prompts improve reliability but consume tokens; prompt caching (5-min/1-hour TTL) amortizes the cost of stable prefixes across turns. Over-specified prompts can hurt with stronger models ("smarter models need less prescriptive engineering" — Anthropic).

### Gaps
- Exact token overhead of tool definitions per model is not specified; caching minimum lengths vary by model (1024–4096 tokens).
- No consensus on optimal few-shot count; Anthropic recommends diverse canonical examples but gives no number.

---

## Structured Outputs

### Takeaway
Two forms: (a) `response_format`/`json_schema` mode where the model returns JSON matching a schema, and (b) tool-based structured output where a "submit_result" tool's arguments are the schema. Validate with Pydantic; on failure, return the validation error to the model for retry ("reflection"). OpenAI `strict: true` requires all fields in `required` and `additionalProperties: false`; Anthropic `strict: true` guarantees conformance. Strict structured outputs can suppress tool calls on some backends (vLLM), so portable frameworks may need two-stage orchestration.

### Cited Findings
- OpenAI structured outputs: guarantees schema adherence via `strict: true`; two forms — function calling (tools) and `text.format`/`response_format` with `json_schema`; uses a subset of JSON Schema; first request with a new schema incurs latency (cached after); supports refusals; incompatible with parallel function calls unless `parallel_tool_calls: false` — [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs); [Introducing Structured Outputs](https://openai.com/index/introducing-structured-outputs-in-the-api/).
- OpenAI Responses uses `text.format`; Chat Completions uses `response_format` — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- OpenAI Agents SDK: `Agent.output_type` for structured outputs; output guardrails — [Agents doc](https://openai.github.io/openai-agents-python/agents/).
- Pydantic AI: `output_type=PydanticModel`; validation failures prompt retry ("reflection and self-correction") — [Pydantic AI agents](https://pydantic.dev/docs/ai/core-concepts/agent/).
- ADK: `output_schema` enforces JSON (Pydantic in Python); warning: `output_schema` with tools only reliably supported by Gemini 3.0+, otherwise ADK falls back to a `set_model_response` tool — [ADK LlmAgent](https://google.github.io/adk-docs/agents/llm-agents/).
- Anthropic: `strict: true` guarantees schema conformance for tool use — [Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).
- OpenAI Agents SDK inference: strict structured outputs on every turn can suppress tool calls on non-OpenAI backends (vLLM); OpenAI relies on server special-casing; portable frameworks may need two-stage orchestration — [opensource survey](https://openai.github.io/openai-agents-python/running_agents/).

### Inferences
Implementation sketch:

```python
class StructuredOutputRunner:
    async def run(self, model, messages, schema: type[BaseModel], max_retries=3):
        for attempt in range(max_retries):
            resp = await model.chat(messages, response_format=schema)
            try:
                return schema.model_validate_json(resp.text)
            except ValidationError as e:
                # feed error back for reflection
                messages.append(resp.assistant_message)
                messages.append(Message(role="user",
                    content=f"Validation failed: {e}. Return valid JSON."))
        raise StructuredOutputError("exhausted retries")
```

**Tool-based alternative:** define a `submit_result` tool whose `parameters` == the schema and force `tool_choice="submit_result"`; parse the tool call's arguments. More robust when the model also needs to use other tools first (two-stage: tool-using turn, then structured finalization).

**Validation/repair:** use Pydantic `model_validate` + `model_validate_json`; on failure, include the error message in the retry prompt; optionally use a repair model or `json_repair` library for malformed JSON. Held-out eval sets recommended to measure schema adherence (OpenAI).

**Trade-offs:** `json_schema` mode is simplest and guarantees adherence on OpenAI/Anthropic but can conflict with tool use on some providers; tool-based is portable but consumes a tool slot and a turn. Two-stage (gather with tools, then finalize structured) is most robust for portable frameworks.

### Gaps
- The exact subset of JSON Schema supported per provider (e.g., `anyOf`, `$ref`, enums) is not fully enumerated in these sources.
- Auto-repair strategies (best-effort JSON fixing) are not standardized; would require empirical evaluation.

---

## Multi-Agent Orchestration

### Takeaway
Patterns: orchestrator-worker (lead delegates to subagents and synthesizes), manager (agents-as-tools, central control), decentralized (handoffs transfer control), sequential/parallel pipelines, loops/refinement, hierarchical. Avoid infinite loops with `max_turns`/`max_iterations`, termination conditions, escalation flags, and final-answer tools. Shared state (fast, coupled) vs. message passing (decoupled, auditable) is the central design choice.

### Cited Findings
- Anthropic multi-agent research: orchestrator-worker; lead agent (Claude Opus 4) plans, saves plan to Memory, spawns parallel subagents (Claude Sonnet 4) that search with interleaved thinking; synthesizes; optional iteration; CitationAgent for attribution; outperformed single-agent Opus 4 by 90.2% on internal research eval; ~15× tokens vs. chats. Prompting principles: delegate with objective/output format/tools/boundaries; scale effort to query complexity (simple: 1 agent, 3–10 calls; complex: >10 subagents); tool design critical; let agents improve themselves (tool-testing agent rewrote descriptions, 40% faster); start wide then narrow; guide thinking; parallel tool calling cuts research time up to 90% — [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system).
- Anthropic building effective agents: five workflow patterns — prompt chaining, routing, parallelization (sectioning/voting), orchestrator-workers, evaluator-optimizer — plus agents; recommend maximizing a single agent first — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- OpenAI: Manager (agents as tools, central control) vs. Decentralized (handoffs, peers transfer control); modeled as graphs; handoffs are one-way transfers passing latest conversation state; `handoff()` customization (`tool_name_override`, `input_type`, `input_filter`, `is_enabled`, `nest_handoff_history`); agents-as-tools via `as_tool()` keeps manager in control; `nest_handoff_history` compacts transcript into summary segments — [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/); [handoffs doc](https://openai.github.io/openai-agents-python/handoffs/).
- ADK: tree of agents (LLM/workflow/custom); `SequentialAgent` (ordered, shared `InvocationContext`), `ParallelAgent` (concurrent, independent branches), `LoopAgent` (repeats until `max_iterations` or sub-agent calls `exit_loop` setting `tool_context.actions.escalate=True`); coordination via shared session state templating `{key?}`, LLM-driven delegation via `description`, explicit invocation via `AgentTool` (model tiering, zero context bloat) — [ADK workflow agents](https://google.github.io/adk-docs/agents/workflow-agents/); [Google Cloud blog](https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk).
- AutoGen: `Swarm` speaker selected by most recent `HandoffMessage`; agents share message context; handoff via auto-generated `transfer_to_<agent>` tool calls; termination conditions `TextMentionTermination`, `HandoffTermination`, `MaxMessageTermination`, composable with `|` — [AutoGen Swarm](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html).
- CrewAI: `Process.sequential` (tasks in order) vs. `Process.hierarchical` (manager agent coordinates/delegates/validates); crews embeddable in flows — [Crews doc](https://docs.crewai.com/en/concepts/crews).
- A2A: Google's open protocol for peer-to-peer agent communication over HTTP; agents discover via Agent Cards at `/.well-known/agent.json`; stateful `Task`s with lifecycle (`submitted`, `working`, `input-required`, `completed`, `canceled`, `failed`, `unknown`); streams `TaskStatusUpdateEvent`/`TaskArtifactUpdateEvent`; complements MCP (A2A = horizontal agent-to-agent, MCP = vertical tool/context) — [A2A blog](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability).
- smolagents: sub-agents passed as `managed_agents` with `name`/`description` embedded in manager prompt; `reset=False` for conversation continuity — [smolagents guided tour](https://huggingface.co/docs/smolagents/guided_tour).

**Avoiding infinite loops:** `max_turns`/`max_iterations`; termination conditions; `exit_loop` escalation; final-answer tools; HITL breakpoints; state-based convergence checks (e.g., no new information in N turns).

### Inferences
Orchestrator sketch:

```python
class Orchestrator:
    async def run(self, task: str) -> str:
        plan = await self.lead.plan(task)          # saved to scratchpad/memory
        for step in plan.steps:
            sub = self.registry.get(step.agent)
            result = await sub.run(step.instruction, context=step.context,
                                  max_turns=step.budget)
            self.scratchpad.record(step.id, result.summary)  # 1-2k tokens
            if self.should_stop(result):
                break
        return await self.lead.synthesize(self.scratchpad)
```

**Shared state vs. message passing:** shared state (ADK session state, LangGraph state dict) is fast and enables templating but couples agents and complicates concurrency; message passing (AutoGen thread, A2A tasks) is decoupled and auditable but adds serialization. Recommendation: use shared scratchpad for in-process subagents (summaries only) and message passing (A2A) for cross-service agents. Write large subagent outputs to the filesystem and pass paths, not content, to avoid the telephone game (Anthropic).

**Trade-offs:** multi-agent (15× tokens) pays off only for high-value, parallelizable, breadth-first work; for tightly coupled tasks prefer a single agent with better tools. Single-agent-first is the consensus recommendation (OpenAI, Anthropic).

### Gaps
- A2A exact JSON schemas (AgentCard fields, Message/Part) were only captured from secondary summaries, not the spec.
- Cost/latency economics are model-specific (Opus 4/Sonnet 4 era) and may not generalize to newer models.

---

## Streaming

### Takeaway
Stream three granularities to a UI: token deltas (text), partial tool calls (incremental JSON), and agent events (turn/node boundaries). Frameworks offer multiple modes (values/updates/messages/custom/checkpoints/tasks/debug). Design as an async generator of typed events with cancellation and resume support; backpressure falls out of async iteration.

### Cited Findings
- LangGraph: streaming modes `values`, `updates`, `messages` (LLM tokens), `custom` (via `get_stream_writer`), `checkpoints`, `tasks`, `debug`; v2 unified `StreamPart` dict `{type, ns, data}`; subgraph streaming via `subgraphs=True`; event streaming via `graph.stream_events(..., version="v3")` — [streaming doc](https://docs.langchain.com/oss/python/langgraph/streaming).
- OpenAI Agents SDK: `Runner.run_streamed()` returns `RunResultStreaming`; streaming events; durable integrations (Dapr/Temporal/Restate/DBOS) — [running_agents](https://openai.github.io/openai-agents-python/running_agents/).
- Pydantic AI: events `PartStartEvent`, `PartDeltaEvent`, `FunctionToolCallEvent`, `FunctionToolResultEvent`, `FinalResultEvent`; custom events via `CustomEvent`/`CapabilityEvent` with `ctx.emit()`; `ui=False` opt-out; cancellation via `CancellationToken` → `RunCancelled` with `all_messages()` for resume — [Pydantic AI agents](https://pydantic.dev/docs/ai/core-concepts/agent/).
- CrewAI: streaming returns `CrewStreamingOutput` iterable with `.result` — [Crews doc](https://docs.crewai.com/en/concepts/crews).
- ADK: `Runner.run_async(...)` yields events; `event.is_final_response()`; async is primary — [ADK event loop](https://google.github.io/adk-docs/runtime/event-loop/).
- LlamaIndex: `WorkflowHandler` is awaitable or `.stream_events()` for streaming — [Workflows intro](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
- OpenAI Responses: agentic loop within a single request can call multiple tools; built-in tools (web search, file search, code interpreter, computer use, image gen, MCP) — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- Anthropic: parallel tool calling cuts research time up to 90%; multi-agent ~15× tokens vs. chats — [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system).

### Inferences
Event model sketch:

```python
class AgentEvent(BaseModel):
    type: Literal["text_delta", "tool_call_start", "tool_call_delta",
                  "tool_result", "turn_start", "turn_end", "final", "error"]
    data: Any
    turn_id: int
    timestamp: float

async def run_streamed(self, state) -> AsyncIterator[AgentEvent]:
    yield AgentEvent(type="turn_start", ...)
    async for chunk in self.model.stream(state.messages, tools=...):
        if chunk.text_delta:
            yield AgentEvent(type="text_delta", data=chunk.text_delta)
        if chunk.tool_call_delta:
            yield AgentEvent(type="tool_call_delta", data=chunk.tool_call_delta)
    # after full tool calls parsed:
    for call in parsed_calls:
        yield AgentEvent(type="tool_call_start", data=call)
        result = await self.tools.execute(call)
        yield AgentEvent(type="tool_result", data=result)
    ...
```

**Tool-call streaming:** emit `tool_call_start` when the function name is known, then `tool_call_delta` with incremental argument JSON, then parse on completion; emit `tool_result` after execution. For UIs, show a "calling X…" indicator during execution.

**Cancellation/resume:** wrap the run in an `asyncio.Task`; on cancel, checkpoint state (messages + partial tool results) and allow resume via `RunCancelled.all_messages()`-style replay (Pydantic AI pattern). Streaming complicates checkpointing because partial state must be persisted; LangGraph's checkpointers handle this at node boundaries.

**Trade-offs:** token-level streaming maximizes perceived responsiveness but complicates backpressure and checkpointing; event-level streaming (turn boundaries) is simpler and sufficient for many UIs. LangGraph's v1→v2 streaming migration (unified `StreamPart`, `GraphOutput` with `.value`/`.interrupts`) shows the API churn cost of streaming design decisions — prefer a stable event schema from the start.

### Gaps
- Backpressure/buffering specifics and resumable streaming after client disconnect are not deeply documented in these sources.
- Optimal chunk size / flush cadence for tool-argument streaming is not specified.