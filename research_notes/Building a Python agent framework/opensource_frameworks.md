# Open-Source Python Agent Frameworks: Comparative Architectural Survey

## LangGraph: state-graph model, nodes, edges, state, checkpointers, streaming, HITL

### Takeaway
LangGraph models an agent as a directed graph (`StateGraph`) over a typed state object: nodes are Python functions that return partial state updates, edges (including conditional edges) route control flow, and a compiled `Pregel` runtime executes it with built-in checkpointing, streaming, and dynamic interrupts. Persistence is split into thread-scoped checkpointers (short-term) and cross-thread Stores (long-term).

### Cited Findings
- A graph is built with `StateGraph(State)`; nodes added via `add_node`, edges via `add_edge(START, ...)` / `add_edge(..., END)` and `add_conditional_edges`; compiled with `.compile()`. Example uses `MessagesState` and `START`/`END` sentinels — [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview).
- Inspired by Pregel and Apache Beam; public interface draws from NetworkX; uses a `Pregel` runtime exposing `.stream()`/`.astream()`/`.invoke()` — [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview).
- State can be a `TypedDict`, Pydantic `BaseModel`, or dataclass; with v2 streaming, `values` mode coerces output back to the model type — [Streaming doc](https://docs.langchain.com/oss/python/langgraph/streaming).
- Persistence has two systems: **Checkpointers** (thread-scoped graph state snapshots, short-term memory) and **Stores** (cross-thread key-value data, long-term memory); compiled via `builder.compile(checkpointer=..., store=...)` with `thread_id` in config — [Persistence doc](https://docs.langchain.com/oss/python/langgraph/persistence).
- Checkpointer implementations: `InMemorySaver`/`MemorySaver`, `SqliteSaver`, `PostgresSaver` (async variants exist); thread_id stored with length limits (keep under 255 chars for Postgres) — [Persistence doc](https://docs.langchain.com/oss/python/langgraph/persistence).
- Human-in-the-loop via `interrupt(value)` inside a node; pauses by raising a special exception caught by runtime, saves state via checkpointer, waits indefinitely; resumed with `Command(resume=...)` under the same `thread_id`; node re-runs from its start on resume — [Interrupts doc](https://docs.langchain.com/oss/python/langgraph/interrupts).
- Static breakpoints: `interrupt_before`/`interrupt_after` at compile or run time — [Interrupts doc](https://docs.langchain.com/oss/python/langgraph/interrupts).
- Interrupt response schemas: `interrupt(value, response_schema=PydanticModel)` validates resume payload — [Interrupts doc](https://docs.langchain.com/oss/python/langgraph/interrupts).
- Streaming modes: `values`, `updates`, `messages` (LLM tokens), `custom` (via `get_stream_writer`), `checkpoints`, `tasks`, `debug`; v2 unified `StreamPart` dict `{type, ns, data}`; subgraph streaming via `subgraphs=True`; event streaming via `graph.stream_events(..., version="v3")` with `stream.messages/values/interrupts/output` — [Streaming doc](https://docs.langchain.com/oss/python/langgraph/streaming).
- `Command` object supports `goto` (routing), `update` (state), `resume` (interrupt), `graph` (subgraph) — [Interrupts doc](https://docs.langchain.com/oss/python/langgraph/interrupts).
- Durable execution: checkpoints keep exact state including error states; pending writes tracked; durability modes mentioned — [Persistence doc](https://docs.langchain.com/oss/python/langgraph/persistence).

### Inferences
- LangGraph's core abstraction is a state machine over a shared state dict; the "agent loop" (LLM → tool calls → LLM) is just one common graph shape, not a framework-imposed loop. This is why LangChain's `create_agent` is built on top of LangGraph.
- The interrupt mechanism's node-restart semantics impose idempotency requirements on pre-interrupt side effects — a notable constraint when modeling custom frameworks.
- v1→v2 streaming migration (unified `StreamPart`, `GraphOutput` with `.value`/`.interrupts`) shows the API churn cost of streaming design decisions.

### Gaps
- Exact internal `Pregel` channel/worker mechanics and `Send`/`Command` dispatch details not fully captured here; reference docs would be needed for a from-scratch reimplementation.

## Microsoft AutoGen / AG2: conversation-based multi-agent patterns

### Takeaway
AutoGen 0.4 (and its community fork AG2) split into `autogen-core` (event-driven runtime) and `autogen-agentchat` (high-level API). The agent model is conversation-centric: `AssistantAgent`s broadcast `TextMessage`/`ToolCallRequestEvent`/`HandoffMessage` into a shared thread; teams (`RoundRobinGroupChat`, `SelectorGroupChat`, `Swarm`, `GraphFlow`) define turn-taking and termination conditions. Swarm uses tool-call-based `HandoffMessage` to transfer control between agents sharing one context.

### Cited Findings
- AgentChat is the high-level API built on `autogen-core`; 0.2→0.4 migration guide exists — [AutoGen AgentChat index](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html).
- `AssistantAgent` configured with `model_client`, `tools`, `handoffs` (list of agent names or `"user"`), `system_message`; supports `Handoff` customization — [Swarm doc](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html).
- `Swarm` team: speaker selected by most recent `HandoffMessage`; agents share message context; handoff implemented via model tool-calling (`transfer_to_<agent>` functions auto-generated) — [Swarm doc](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html).
- Termination conditions: `TextMentionTermination`, `HandoffTermination`, `MaxMessageTermination`, composable with `|` — [Swarm doc](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html).
- `GraphFlow` + `DiGraphBuilder`: deterministic directed graph of agents; supports sequential, parallel fan-out/fan-in, conditional edges with lambda conditions, loops; `MessageFilterAgent`/`MessageFilterConfig`/`PerSourceFilter` for per-agent message filtering; experimental — [GraphFlow doc](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/graph-flow.html).
- Message types: `TextMessage`, `ToolCallRequestEvent`, `ToolCallExecutionEvent`, `HandoffMessage`, `StopMessage`; `TaskResult` aggregates messages + `stop_reason` — [Swarm doc](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html).
- Memory/RAG and state management covered in tutorial; `Console` UI helper for streaming — [AgentChat index](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html).
- `SelectorGroupChat` (centralized LLM selector) and `RoundRobinGroupChat` also available — [Swarm doc](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html).

### Inferences
- AutoGen's distinctive idea is treating handoffs as ordinary tool calls (`transfer_to_X`), so any tool-calling model can drive multi-agent routing without a separate orchestrator.
- The 0.2→0.4 split (core vs agentchat) is a useful template: keep a thin event-driven runtime and a higher-level conversational API on top.

### Gaps
- AG2-specific divergence from AutoGen 0.4 not researched in depth; AG2 docs would need separate verification. Core runtime internals (event bus, `AgentRuntime`) only referenced, not detailed.

## CrewAI: crews, agents, tasks, flows, sequential/hierarchical process

### Takeaway
CrewAI has two layers: `Crew` (a group of `Agent`s executing `Task`s under a `Process.sequential` or `Process.hierarchical` strategy, with optional manager LLM/agent, memory, cache, checkpointing, streaming) and `Flow` (an event-driven workflow class with `@start`/`@listen`/`@router`/`or_`/`and_` decorators, Pydantic or dict state, `@persist` for SQLite-backed state, and built-in memory). Crews can be embedded as steps inside Flows.

### Cited Findings
- `Crew` attributes: `tasks`, `agents`, `process` (default sequential), `manager_llm` (required for hierarchical), `memory`, `cache`, `max_rpm`, `planning`, `checkpoint`, `stream`, `step_callback`, `task_callback`, `knowledge_sources`, `security_config`, `skills` — [Crews doc](https://docs.crewai.com/en/concepts/crews).
- `Process.sequential`: tasks run in order; `Process.hierarchical`: a manager agent coordinates/delegates/validates — [Crews doc](https://docs.crewai.com/en/concepts/crews).
- Kickoff variants: `kickoff`, `kickoff_for_each`, `akickoff` (native async), `kickoff_async` (thread-based), `akickoff_for_each`; streaming returns `CrewStreamingOutput` iterable with `.result` — [Crews doc](https://docs.crewai.com/en/concepts/crews).
- Checkpointing: `checkpoint=True` or `CheckpointConfig(location, on_events, provider JsonProvider/SqliteProvider, max_checkpoints)`; resume via `Crew.from_checkpoint(path)` — [Crews doc](https://docs.crewai.com/en/concepts/crews).
- Memory: short-term, long-term, entity memory via `memory=True` and `embedder` config — [Crews doc](https://docs.crewai.com/en/concepts/crews).
- Flows: `Flow` base class, `@start()`, `@listen(...)`, `@router()`, `or_()`, `and_()`, `@human_feedback`; structured state via `Flow[PydanticModel]` or unstructured dict; state auto-gets UUID `id` — [Flows doc](https://docs.crewai.com/en/concepts/flows).
- `@persist` decorator (class or method level) saves state to SQLite by default; resume via `kickoff(inputs={"id": uuid})`, fork via `kickoff(restore_from_state_id=uuid)` — [Flows doc](https://docs.crewai.com/en/concepts/flows).
- Flows have built-in memory methods: `self.remember`, `self.recall`, `self.extract_memories` (LanceDB-backed, persists across runs) — [Flows doc](https://docs.crewai.com/en/concepts/flows).
- Usage metrics aggregated across all LLM calls in a flow via `flow.usage_metrics` — [Flows doc](https://docs.crewai.com/en/concepts/flows).
- Flows can embed crews (`PoemCrew().crew().kickoff(...)`) and agents (`Agent(...).kickoff_async(...)`) — [Flows doc](https://docs.crewai.com/en/concepts/flows).

### Inferences
- CrewAI's split between Crew (team execution) and Flow (orchestration/state) mirrors AutoGen's agentchat/core split but with a more declarative, decorator-driven style.
- Checkpointing + fork semantics make CrewAI flows suitable for long-running, resumable pipelines with branching.

### Gaps
- Exact internal task execution loop and manager agent prompting not detailed in these docs; deeper source inspection needed for faithful reimplementation.

## Pydantic AI: typed agent loop, dependencies, tools, structured outputs

### Takeaway
Pydantic AI is a typed agent SDK where an `Agent[deps_type, output_type]` wraps a pydantic-graph state machine. Tools are functions whose signatures (including `RunContext[deps_type]`) become JSON schemas with pydantic validation; structured outputs are validated and retried on failure; dependencies are injected type-safely. Runs expose `agent.iter()` for node-by-node traversal (`UserPromptNode`, `ModelRequestNode`, `CallToolsNode`, `End`), and streaming/HITL/cancellation are first-class.

### Cited Findings
- `Agent` components: instructions, function tools/toolsets, structured output type, dependency type, default model, model settings, capabilities — [Agents doc](https://pydantic.dev/docs/ai/core-concepts/agent/).
- Run methods: `run`, `run_sync`, `run_stream`, `run_stream_sync`, `run_stream_events`, `iter` (async context manager yielding `AgentRun`) — [Agents doc](https://pydantic.dev/docs/ai/core-concepts/agent/).
- `agent.iter()` yields nodes: `UserPromptNode`, `ModelRequestNode`, `CallToolsNode`, `End(data=FinalResult(...))`; manual driving via `agent_run.next(node)`; usage via `agent_run.usage`, final via `agent_run.result` — [Agents doc](https://pydantic.dev/docs/ai/core-concepts/agent/).
- Tools registered with `@agent.tool`/`@agent.tool_plain`; receive `RunContext[deps_type]`; docstrings become descriptions; arguments validated by pydantic; errors returned to model for retry — [Agents doc](https://pydantic.dev/docs/ai/core-concepts/agent/) and overview.
- Structured output via `output_type=PydanticModel`; validation failures prompt retry ("reflection and self-correction") — [Agents doc](https://pydantic.dev/docs/ai/core-concepts/agent/).
- Dependency injection: `deps_type` dataclass passed at run time via `deps=`; tools/instructions receive it via `RunContext` — [overview](https://pydantic.dev/docs/ai/).
- Capabilities bundle tools/instructions/hooks/model settings; on-demand capabilities (`defer_loading=True`) collapse to catalog entries loaded via `load_capability` — [overview](https://pydantic.dev/docs/ai/).
- Streaming events: `PartStartEvent`, `PartDeltaEvent`, `FunctionToolCallEvent`, `FunctionToolResultEvent`, `FinalResultEvent`; custom events via `CustomEvent`/`CapabilityEvent` with `ctx.emit()`; `ui=False` opt-out — [Agents doc](https://pydantic.dev/docs/ai/core-concepts/agent/).
- Cancellation via `CancellationToken` → `RunCancelled` with `all_messages()` for resume — [Agents doc](https://pydantic.dev/docs/ai/core-concepts/agent/).
- Durable execution on 9 engines (Temporal, DBOS, Prefect, Restate, AWS Lambda, Kitaru, Airflow, Absurd, pgtask) via capability attach; human-in-the-loop via deferred tools — [overview](https://pydantic.dev/docs/ai/).
- Interfaces: CLI, web chat, realtime voice (OpenAI Realtime/Gemini Live/Azure/xAI), AG-UI/Vercel AI adapters, ACP, GitHub Agentic Workflows — [overview](https://pydantic.dev/docs/ai/).

### Inferences
- Pydantic AI's distinctive contribution is making the agent graph (pydantic-graph) an explicit, traversable, typed artifact rather than a hidden loop — useful for debugging and custom control flow.
- The `deps_type` generic + `RunContext` pattern is the cleanest dependency-injection model among the surveyed frameworks.

### Gaps
- Exact pydantic-graph `GraphBuilder`/node transition internals and how `CallToolsNode` dispatches concurrent tool calls not captured beyond high-level node names.

## OpenAI Agents SDK, smolagents, LlamaIndex Workflows

### OpenAI Agents SDK
#### Takeaway
The OpenAI Agents SDK exposes a minimal primitive set — `Agent` (instructions + tools), `Runner` (loop), handoffs/agents-as-tools, guardrails, sessions, tracing — with a built-in loop that runs until a final output or `max_turns`. Handoffs are implemented as tool calls (`transfer_to_<agent>`), similar to AutoGen Swarm.

#### Cited Findings
- Primitives: Agents, handoffs/agents-as-tools, guardrails; built-in tracing — [OpenAI Agents SDK intro](https://openai.github.io/openai-agents-python/).
- Agent loop: call LLM → if final output, end; if handoff, switch agent+input and re-run; if tool calls, execute and re-run; `max_turns` (None disables) raises `MaxTurnsExceeded` — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Runner methods: `run` (async), `run_sync`, `run_streamed` (streaming events); `RunResult`/`RunResultStreaming` — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Sessions: `SQLiteSession`, SQLAlchemy/Redis/Mongo/Dapr/encrypted variants; server-managed via `conversation_id`/`previous_response_id`/`auto_previous_response_id` — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- RunConfig: model/provider/settings overrides, guardrails, handoff filters, `call_model_input_filter`, tracing, tool execution concurrency (`ToolExecutionConfig.max_function_tool_concurrency`), tool-not-found behavior, tool error formatter, reasoning item ID policy — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Error handlers: `error_handlers` dict for `"max_turns"`, `"model_refusal"`, `"invalid_final_output"` returning `RunErrorHandlerResult` — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Human-in-the-loop: tool approval pause/resume; durable integrations: Dapr, Temporal, Restate, DBOS — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- `nest_handoff_history` opt-in compacts transcript into summary segments — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).

### smolagents (HuggingFace)
#### Takeaway
smolagents is a minimal (~1000 lines) library with two agent classes: `CodeAgent` (generates Python code snippets, executed in a sandbox/interpreter) and `ToolCallingAgent` (JSON tool calls). Tools are Python functions with type hints + docstrings. Multi-agent via `managed_agents` where sub-agents have `name`/`description`. Emphasizes code-as-action for expressiveness.

#### Cited Findings
- `CodeAgent` generates Python code; `ToolCallingAgent` generates JSON tool calls; both extend a base `Agent` — [smolagents index](https://huggingface.co/docs/smolagents/index).
- Model-agnostic: `InferenceClientModel`, `LiteLLMModel`, `TransformersModel`, `AzureOpenAIModel`, `AmazonBedrockModel`, `MLXModel` — [guided tour](https://huggingface.co/docs/smolagents/guided_tour).
- Tools: `@tool` decorator on typed functions with docstrings, or `Tool` subclass with `name`/`description`/`inputs`/`output_type`/`forward`; default toolbox via `add_base_tools=True` — [guided tour](https://huggingface.co/docs/smolagents/guided_tour).
- Code execution: local interpreter with import allowlist (`additional_authorized_imports`), or sandboxed via E2B/Blaxel/Docker — [guided tour](https://huggingface.co/docs/smolagents/guided_tour).
- Termination: agent runs until `final_answer` tool call or `max_steps`; `final_answer_checks` list of validator functions — [guided tour](https://huggingface.co/docs/smolagents/guided_tour).
- Multi-agent: sub-agents passed as `managed_agents` with `name`/`description` embedded in manager prompt; `reset=False` for conversation continuity; `agent.interrupt()` — [guided tour](https://huggingface.co/docs/smolagents/guided_tour).
- CLI: `smolagent` command; Hub push/load; Gradio UI via `GradioUI` — [guided tour](https://huggingface.co/docs/smolagents/guided_tour).

### LlamaIndex Workflows / AgentWorkflow
#### Takeaway
LlamaIndex `Workflow` is an event-driven, step-based orchestration model: steps are async methods decorated with `@step` whose type annotations (input event → output event) define the graph edges. Special `StartEvent`/`StopEvent` mark entry/exit. Supports branching via different return types, loops, fan-out (`list[Event]`), fan-in (`list[Event]` param), shared per-run state via `Context`/`ctx.store`, and resource injection via `Resource(...)`. Validated before run.

#### Cited Findings
- Steps declared with `@step` decorator; input/output inferred from type annotations; graph validated before run — [Workflows intro](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
- Events are user-defined Pydantic models; `StartEvent`/`StopEvent` provided; `StopEvent(result=...)` terminates — [Workflows intro](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
- Async-first; `await w.run(topic=...)` returns `WorkflowHandler` (awaitable, or `.stream_events()` for streaming) — [Workflows intro](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
- Dynamic fan-out via `ctx.send_event`, fan-in via `ctx.collect_events`; shared state via `ctx.store`; resources via `Resource(...)` — [Workflows intro](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
- Branches/loops/concurrency documented in separate pages; human-in-the-loop, durable workflows, DBOS integration, error handling/retry, drawing, testing — [Workflows intro](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
- Agents defined separately; `AgentWorkflow` orchestrates agents as tools — [High-Level Concepts](https://docs.llamaindex.ai/en/stable/getting_started/concepts/).

### Inferences
- LlamaIndex Workflows' type-annotation-driven graph definition is the most "Pythonic"/declarative of the surveyed; edges are inferred, not manually wired, reducing boilerplate but requiring static type discipline.
- smolagents' code-action paradigm (CodeAgent) is the most radical departure from JSON tool-calling and suits tasks requiring composability.

### Gaps
- LlamaIndex `AgentWorkflow`/agent loop mechanics (ReAct-style) only referenced, not detailed; would need the agent module docs for tool-dispatch loop internals.

## Cross-cutting patterns: ReAct, planner/executor, reflection, ToT, plan-and-execute

### Takeaway
None of the frameworks hard-code a single "agent loop"; instead they expose primitives (graph nodes, steps, events, handoffs) onto which patterns are layered. ReAct is the default shape of most "agent" abstractions (LangChain's `create_agent`, Pydantic AI's `CallToolsNode` loop, OpenAI Agents SDK loop, smolagents). Planner/executor, reflection, and plan-and-execute appear as higher-level constructs: CrewAI's `planning=True` (AgentPlanner plans tasks before iteration), LangGraph's Deep Agents harness (planning + subagents + filesystem), Pydantic AI's capabilities/harness, and LlamaIndex's planning workflow example.

### Cited Findings
- LangGraph docs note LangChain's `create_agent` provides prebuilt LLM+tool-calling loops on top of LangGraph; LangGraph itself is lower-level orchestration — [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview).
- CrewAI `planning=True` activates an `AgentPlanner` that plans tasks and injects the plan into each task description before each crew iteration — [Crews doc](https://docs.crewai.com/en/concepts/crews).
- LangGraph ecosystem lists "Deep Agents" harness: planning, subagents, filesystem tools, context management on top of LangGraph — [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview).
- Pydantic AI Harness provides planning, sub-agents, context management/compaction, guardrails, persistence as composable capabilities — [overview](https://pydantic.dev/docs/ai/).
- LlamaIndex docs list a "Query Planning with Workflows" example (plan → execute sub-queries → synthesize) and "Reliable Structured Generation" (reflection loop) — [Workflows intro](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
- OpenAI Agents SDK loop is explicitly ReAct-shaped: LLM → tool calls → LLM until final output — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- smolagents `CodeAgent` loop runs until `final_answer` tool call or `max_steps`; `final_answer_checks` enable self-validation — [guided tour](https://huggingface.co/docs/smolagents/guided_tour).
- AutoGen termination conditions (`TextMentionTermination`, `MaxMessageTermination`) bound reflection loops — [Swarm doc](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html).

### Inferences
- "Tree-of-thoughts" and explicit "reflection/self-critique" as named patterns are not first-class in any of these frameworks' core APIs; they are implemented as graph/loop constructs (conditional edges, retry nodes) or via planning capabilities. The frameworks provide the orchestration substrate, not the reasoning strategy.
- Plan-and-execute appears most concretely in CrewAI (planning flag) and LlamaIndex (planning example); others leave it to user code.

### Gaps
- No primary-source benchmarks or comparative evaluations of these patterns found; claims about relative performance are not supported by these docs.

## Memory, checkpoints, retries, rate limits, streaming

### Takeaway
Short-term/thread memory is handled by checkpointers (LangGraph), session stores (OpenAI Agents SDK), flow state + `@persist` (CrewAI), and in-memory message history. Long-term/cross-thread memory by Stores (LangGraph), CrewAI memory (short/long/entity), LlamaIndex memory, and Pydantic AI durable execution. Retries/rate limits: CrewAI `max_rpm`; LangGraph pruning; OpenAI SDK retry on conversation-locked; Pydantic AI cancellation tokens. Streaming is a major differentiator: LangGraph has the richest mode set (values/updates/messages/custom/checkpoints/tasks/debug + event streaming v3); CrewAI/OpenAI SDK/smolagents support token streaming; Pydantic AI supports events + custom events.

### Cited Findings
- LangGraph: checkpointers (InMemory/Sqlite/Postgres) for short-term thread memory; Stores for long-term cross-thread; checkpoint pruning recommended for unbounded growth; durability modes — [Persistence doc](https://docs.langchain.com/oss/python/langgraph/persistence).
- CrewAI: `max_rpm` (crew-level, overrides agents); memory (short/long/entity) via `memory=True`; checkpointing via `CheckpointConfig` with Json/Sqlite providers and `from_checkpoint` resume; flow `@persist` (SQLite) with resume/fork; streaming via `stream=True` returning iterable with `.result` — [Crews doc](https://docs.crewai.com/en/concepts/crews), [Flows doc](https://docs.crewai.com/en/concepts/flows).
- OpenAI Agents SDK: sessions (SQLite/SQLAlchemy/Redis/Mongo/Dapr/encrypted) for persistent memory; server-managed conversations via `conversation_id`/`previous_response_id`; `MaxTurnsExceeded`; retry on conversation-locked; streaming via `run_streamed`/`stream_events`; durable integrations (Dapr/Temporal/Restate/DBOS) — [running_agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Pydantic AI: `agent.iter()`/streaming events; `CancellationToken` for cancellation with `RunCancelled.all_messages()` resume; durable execution on 9 engines; realtime voice streaming — [Agents doc](https://pydantic.dev/docs/ai/core-concepts/agent/).
- smolagents: in-memory agent logs; `reset=False` conversation continuity; interrupt support — [guided tour](https://huggingface.co/docs/smolagents/guided_tour).
- LlamaIndex: workflows support streaming events (`.stream_events()`), durable workflows, DBOS; state via `ctx.store` — [Workflows intro](https://docs.llamaindex.ai/en/stable/understanding/workflows/).
- AutoGen: memory/RAG in tutorial; state management tutorial; streaming via `run_stream`/`Console` — [AgentChat index](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html).

### Inferences
- Checkpoint/resume is now table stakes (LangGraph, CrewAI, Pydantic AI durable, OpenAI SDK sessions); the main design choice is whether state is a single graph state object (LangGraph) vs. an event-sourced message log (AutoGen) vs. a Pydantic flow state (CrewAI).
- Rate limiting is mostly left to user/provider config except CrewAI's built-in `max_rpm`.

### Gaps
- Detailed retry/backoff policies, circuit breakers, and token-bucket rate limiting internals are not documented in these sources; would require source-code inspection.
- LangGraph "durability modes" and pending-writes semantics referenced but not fully detailed here.
