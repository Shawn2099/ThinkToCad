# OpenAI — Agent-Building Philosophy, APIs, SDKs, and Architectural Patterns (research notes)

## Q1: What does OpenAI's "A practical guide to building agents" recommend (workflow vs agent, when to use agents, single vs multi, tool design)?

### Takeaway
OpenAI defines agents as LLM-driven systems that independently accomplish tasks on a user's behalf, distinct from LLM-augmented apps where the LLM does not control workflow execution; the guide recommends starting with a single agent maximized for capability, evolving to multi-agent (Manager vs Decentralized) only when needed, and designing tools as well-documented, reusable data/action/orchestration primitives with explicit guardrails and human-in-the-loop for high-risk actions.

### Cited Findings
- Agent definition: "systems that independently accomplish tasks on your behalf"; apps that integrate LLMs but don't use them to control workflow execution (simple chatbots, single-turn LLMs, sentiment classifiers) are not agents — [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/); [PDF](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).
- Core characteristics: (1) LLM manages workflow execution/decisions, recognizes completion, self-corrects, can halt and hand back to user; (2) access to tools to gather context and take actions, dynamically selected, within guardrails — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Agent = three components: Model, Tools, Instructions — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Use cases where agents beat deterministic automation: complex decision-making, difficult-to-maintain rules, heavy reliance on unstructured data; otherwise deterministic may suffice — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Tool types: Data (retrieve context), Action (mutate external systems), Orchestration (agents as tools) — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Tool design: standardized definition enabling flexible many-to-many tool/agent relationships; well-documented, tested, reusable tools improve discoverability and versioning; for legacy systems without APIs, use computer-use models — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Instructions best practices: use existing operating procedures/policy docs, break tasks into smaller steps, define clear actions, capture edge cases with conditional branches — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Orchestration split: single-agent (one model + tools in a loop) vs multi-agent (distributed). Recommend maximizing a single agent first — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Single-agent loop exit conditions: tool calls, structured output, errors, max turns. In Agents SDK, `Runner.run()` loops until a final-output tool is invoked or model returns text with no tool calls — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- When to split agents: complex logic with many if-then-else branches; tool overload (similarity/overlap, not raw count — >15 distinct tools can work, <10 overlapping can fail) — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Multi-agent patterns: Manager (agents as tools, central control) vs Decentralized (handoffs, peers transfer control); modeled as graphs — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Handoffs are one-way transfers that pass latest conversation state to the new agent — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).
- Human intervention triggers: exceeding failure thresholds (retries); high-risk actions (cancel orders, large refunds, payments) — [OpenAI guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).

### Inferences
- OpenAI's philosophy is incremental: prefer deterministic solutions where possible, then single agent, then multi-agent; complexity should be justified by measured failure modes (tool confusion, instruction non-compliance).
- "Agent" is a behavior/role, not a framework primitive; the same primitive (Agent) can represent a whole workflow, a step, or a task.

### Gaps
- The guide's PDF full text on model selection, evals, and guardrail internals was not fully fetched; some details (e.g., recommended model families per agent role) may be in the PDF but not captured here.

## Q2: What is the OpenAI Agents SDK (Python)? Core abstractions and how the agent loop works?

### Takeaway
The OpenAI Agents SDK is an open-source, production-ready Python framework (successor to Swarm) built on three primitives — Agents, Handoffs/agents-as-tools, Guardrails — plus Runner, Sessions, Tracing, MCP, and structured outputs; its core `Runner` loop repeatedly calls the current agent's model, executes tool calls, handles handoffs, and stops on final text/structured output or `max_turns`.

### Cited Findings
- SDK overview: "lightweight, easy-to-use package with very few abstractions", production-ready upgrade of Swarm; primitives: Agents, Agents as tools/Handoffs, Guardrails; built-in tracing; works with Responses API by default and Chat Completions; supports other providers via Chat Completions-style endpoints — [Agents SDK docs](https://openai.github.io/openai-agents-python/).
- Features: Sandbox agents, Realtime/voice agents, Python-first, function tools with auto schema + Pydantic validation, MCP server tool calling, Sessions, Human-in-the-loop, Tracing — [Agents SDK docs](https://openai.github.io/openai-agents-python/).
- Agent fields: `name` (required), `instructions`, `prompt`, `handoff_description`, `handoffs`, `model`, `model_settings`, `tools`, `mcp_servers`, `mcp_config`, `input_guardrails`, `output_guardrails`, `output_type`, `hooks`, `tool_use_behavior` — [Agents doc](https://openai.github.io/openai-agents-python/agents/).
- `Agent` vs `SandboxAgent`: base Agent for prompt/tool/state work; SandboxAgent for isolated workspaces with manifest files — [Agents doc](https://openai.github.io/openai-agents-python/agents/).
- Runner methods: `Runner.run()` (async), `Runner.run_sync()`, `Runner.run_streamed()` (returns `RunResultStreaming`) — [Running agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Agent loop steps: (1) call LLM for current agent with current input; (2) inspect output; (3a) final output -> end; (3b) handoff -> switch agent and re-run; (3c) tool calls -> execute, append results, re-run; (4) exceed `max_turns` -> `MaxTurnsExceeded` (`max_turns=None` disables) — [Running agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Final output rule: model produces text output of desired type with no tool calls — [Running agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- RunConfig: `model`, `model_provider`, `model_settings`, `session_settings`, `session_input_callback`, `input_guardrails`, `output_guardrails`, `handoff_input_filter`, `nest_handoff_history`, `handoff_history_mapper`, `call_model_input_filter`, `reasoning_item_id_policy`, `tracing_disabled`, `tool_execution` — [Running agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Run results: `RunResult`/`RunResultStreaming` inherit `RunResultBase` with `final_output`, `new_items`, `last_agent`, `raw_responses`, `to_state()`, `to_input_list()`, `last_response_id`, `interruptions` — [Results doc](https://openai.github.io/openai-agents-python/results/).
- `RunState` supports resuming paused runs (approvals) and `cancel(mode="after_turn")` — [Running agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Input to Runner can be string, list of OpenAI Responses items, or `RunState` — [Running agents doc](https://openai.github.io/openai-agents-python/running_agents/).
- Quickstart example: `result = await Runner.run(agent, "When did the Roman Empire fall?")`; multi-turn via `result.to_input_list()`, sessions, or `conversation_id`/`previous_response_id` — [Quickstart](https://openai.github.io/openai-agents-python/quickstart/).

### Inferences
- The SDK is intentionally minimal: orchestration lives in Python control flow + LLM decisions rather than a graph DSL; state management is pluggable (client-side sessions vs server-side continuation).

### Gaps
- Exact `max_turns` default value and full `RunConfig` dataclass fields (beyond those documented) were not captured; check `ref/run_config`.

## Q3: Responses API vs Chat Completions API for agents; agentic primitives

### Takeaway
OpenAI recommends the Responses API for all new agent projects: it is stateful-by-default, returns typed Items, supports an agentic loop within a single request (multiple tool calls), built-in tools (web search, file search, code interpreter, computer use, image gen, remote MCP), and better reasoning-model performance/caching; Chat Completions remains stateless, message-based, and is recommended only when you need full manual control or maximum speed.

### Cited Findings
- Responses API described as "unified interface for building powerful, agent-like applications" with built-in tools (web search, file search, computer use, code interpreter, remote MCPs) and seamless multi-turn via previous responses — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- Responses benefits: better performance with reasoning models (+3% SWE-bench), agentic loop by default (model can call multiple tools in one request), lower costs (40-80% cache improvement), stateful context (`store: true`), flexible inputs, encrypted reasoning, future-proof — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- Chat Completions vs Responses capability table: both support text/vision/structured outputs/function calling; Responses additionally supports web search, file search, computer use, code interpreter, MCP, image generation, reasoning summaries — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- Messages vs Items: Chat Completions uses `messages` (input+output); Responses uses `input`/`output` arrays of typed Items (`message`, `function_call`, `function_call_output`, `reasoning`); Chat supports `n` parallel generations, Responses returns one — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- State: Responses stored by default; Chat stateless (full history each call); Responses supports Conversations API or `previous_response_id` chaining; instructions from previous response not carried over automatically — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- Structured Outputs shape differs: Chat uses `response_format`; Responses uses `text.format` — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses); [Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs).
- Function-calling shape differs both in config and returned calls — [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- Chat Completions not going away; Responses is a superset with same performance; Assistants API to be deprecated (sunset mid-2026) in favor of Responses — [New tools for building agents](https://openai.com/index/new-tools-for-building-agents/).
- Responses preserves reasoning state across turns (Chat drops it), boosting TAUBench +5% with GPT-5 — [Why we built Responses API](https://developers.openai.com/blog/responses-api).
- Built-in tools: web search, file search, computer use, code interpreter, image generation, MCP, remote MCPs — [New tools](https://openai.com/index/new-tools-for-building-agents/); [Migrate](https://developers.openai.com/api/docs/guides/migrate-to-responses).
- Function calling: model emits `function_call` items with `call_id`; app executes and returns `function_call_output` linked by `call_id`; `parallel_tool_calls` true by default; `max_tool_calls` caps built-in tool calls per response — [Responses API ref](https://platform.openai.com/docs/api-reference/responses/create).
- Structured Outputs: guarantees schema adherence via `strict: true`; two forms — function calling (tools) and `text.format`/`response_format` with `json_schema`; uses subset of JSON Schema; first request with new schema incurs latency (cached after); supports refusals; incompatible with parallel function calls unless `parallel_tool_calls: false` — [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs); [Introducing Structured Outputs](https://openai.com/index/introducing-structured-outputs-in-the-api/).
- Computer use model: can interact with UIs for legacy systems without APIs — [Practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/).

### Inferences
- For agent frameworks, the key design implication: model the internal turn as a sequence of typed "items" (not messages), support both client-managed and server-managed state, and treat tool calls as first-class items with correlation IDs.
- Strict structured outputs on every turn can suppress tool calls on non-OpenAI backends (vLLM); OpenAI relies on server special-casing; portable frameworks may need two-stage orchestration.

### Gaps
- Exact function-calling JSON shapes for Responses (tool definition `type: function` with `name`/`parameters`/`strict`) and the `tool_choice` enum values beyond "auto" were not fully captured from official docs in this pass.

## Q4: Published patterns for tool design, prompt engineering, guardrails, tracing/observability, and multi-agent handoffs

### Takeaway
OpenAI publishes concrete patterns: tool descriptions as durable interface contracts with usage criteria and argument rules; prompts structured with Identity/Instructions/Examples/Context plus persistence/tool-calling/planning reminders for GPT-4.1; guardrails as input/output/tool tripwires with parallel vs blocking execution; tracing as traces/spans with custom processors; handoffs as tools (`transfer_to_*`) with input filters, nested history, and agents-as-tools for manager control.

### Cited Findings
- Tool design: use the `tools` field (not manual prompt injection); descriptions should state when to invoke and how to build arguments; usage criteria can refine proactiveness; developer instructions disambiguate similar tools and preferred ordering — [o3/o4-mini function calling guide](https://d2a346aex646576656c6f70657273x6f70656e6169x636f6d.gateway.web.tr/https/cookbook/examples/o-series/o3o4-mini_prompting_guide).
- Guard against hallucinations: explicit "do not promise future calls", `strict: true`, validate arguments, discard irrelevant history/summarize — [o3/o4-mini guide](https://d2a346aex646576656c6f70657273x6f70656e6169x636f6d.gateway.web.tr/https/cookbook/examples/o-series/o3o4-mini_prompting_guide).
- Prompt engineering: message roles (developer/user/assistant); `instructions` parameter high priority; structure developer messages as Identity, Instructions, Examples, Context using Markdown/XML; GPT-4.1 agent reminders for PERSISTENCE, TOOL CALLING, PLANNING; pin model snapshots; build evals — [GPT-4.1 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide) (note: source is GPT-5 prompting guide URL but content covers GPT-4.1 reminders).
- Guardrails: input (first agent only) and output (final agent only) guardrails as `@input_guardrail`/`@output_guardrail` returning `GuardrailFunctionOutput(tripwire_triggered=...)`; execution modes parallel (default) vs blocking (`run_in_parallel=False`); tool guardrails wrap `FunctionTool` with input/output validation and can reject/replace content; tripwires raise exceptions; guardrail results accumulated in `run_data` — [Guardrails doc](https://openai.github.io/openai-agents-python/guardrails/).
- Tool guardrails: `@tool_input_guardrail`, `@tool_output_guardrail`, `ToolGuardrailFunctionOutput.allow()/reject_content()`; local MCP servers can attach guardrails; hosted/built-in tools do not use this pipeline — [Guardrails doc](https://openai.github.io/openai-agents-python/guardrails/); [Tools doc](https://openai.github.io/openai-agents-python/tools/).
- Tracing: traces (workflow-level) composed of spans; default spans for run, task, turn, agent, generation, function, guardrail, handoff, audio; `trace()` context manager; `custom_span()`; `TracingProcessor` interface (`on_trace_start/end`, `on_span_start/end`, `shutdown`, `force_flush`); `add_trace_processor`/`set_trace_processors`; export to OpenAI ingest endpoint with retries; disable via env/`set_tracing_disabled`/`RunConfig.tracing_disabled`; redaction guidance — [Tracing doc](https://openai.github.io/openai-agents-python/tracing/).
- Multi-agent handoffs: handoffs represented as tools named `transfer_to_<agent>`; `handoff()` customization (`tool_name_override`, `tool_description_override`, `on_handoff`, `input_type`, `input_filter`, `is_enabled`, `nest_handoff_history`); `handoff_description` for routing hints; input filters can reshape history; `remove_all_tools` filter; nested handoff history (opt-in beta) compacts history into assistant summary segments; agents-as-tools via `as_tool()` keeps manager in control; approval gates via `needs_approval` — [Handoffs doc](https://openai.github.io/openai-agents-python/handoffs/); [Tools doc](https://openai.github.io/openai-agents-python/tools/).
- MCP integration: `HostedMCPTool` (remote via Responses) vs local `MCPServerStdio/Sse/StreamableHttp` with tool filtering (`create_static_tool_filter`, dynamic filters), tool guardrails, and tracing of tool listing/calls — [MCP doc](https://github.com/openai/openai-agents-python/blob/main/docs/mcp.md); [Integrations/observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability).

### Inferences
- OpenAI's recommended control model: use guardrails at boundaries (input/output/tool) rather than only in prompts; treat tool descriptions as the contract and instructions as orchestration policy.
- Observability is first-class: default tracing covers all primitive events; custom processors allow export to any backend, but redaction must be co-located with export to be reliable.

### Gaps
- The exact `HandoffInputData` fields and `agents.extensions.handoff_filters` full list were only partially captured; full handoff filter helpers beyond `remove_all_tools` not enumerated here.

## Q5: Published open-source code, reference implementations, and cookbook examples

### Takeaway
OpenAI's open-source references are `openai/openai-agents-python` (current production SDK), `openai/swarm` (deprecated educational predecessor), and `openai/openai-cookbook` (extensive notebooks/MDX); the cookbook contains agent patterns, orchestration, parallel agents, guardrails, memory/compaction, MCP, evals, and migration guides.

### Cited Findings
- `openai/openai-agents-python`: main SDK repo; docs, examples (agent_patterns, memory, mcp, etc.), source under `src/agents/`; published on GitHub and PyPI — [GitHub](https://github.com/openai/openai-agents-python).
- `openai/swarm`: marked deprecated/educational; replaced by Agents SDK; stateless, Chat Completions-based; primitives Agent + handoffs via function returning Agent; `Result` object for value/agent/context_variables; function schemas from docstrings/type hints; errors surface as chat messages — [GitHub](https://github.com/openai/swarm/).
- `openai/openai-cookbook`: examples including `Orchestrating_agents.ipynb` (routines + handoffs), `agents_sdk/parallel_agents.ipynb`, `agents_sdk/agent_improvement_loop.ipynb`, deep research API, node SDK agent guide, structured outputs intro, function calling guides, GPT-4.1/5 prompting guides — [GitHub](https://github.com/openai/openai-cookbook/); [Cookbook site](https://developers.openai.com/cookbook).
- Cookbook agent topics (recent): Agents SDK Deployment Manager, AML analysis, Slack bot, data analyst, prior auth review, SRE agent, computer use agents, iterative repair loops with Codex, memory/compaction, context engineering/personalization, long-term memory, MCP plugin evals, migration from Claude Agent SDK, sandbox agents — [Cookbook](https://developers.openai.com/cookbook).
- OpenAI platform docs: "A practical guide to building agents" PDF, developer docs for agents (running, orchestration, tools, guardrails, tracing, MCP, sessions, human-in-the-loop), Responses/Chat Completions, function calling, structured outputs — [platform.openai.com](https://platform.openai.com/); [developers.openai.com](https://developers.openai.com/).

### Inferences
- For building your own framework, the highest-value references are: SDK's `Runner` loop + `Agent` dataclass, `handoff()` and `as_tool()`, guardrail decorators, session protocol, tracing processor interface, and MCP server wrappers; plus cookbook notebooks for end-to-end patterns.

### Gaps
- I did not clone or inspect the SDK source beyond docs/tracing files; concrete internal class hierarchies (e.g., `Model` interface, `Converter`) would need source-level review for reimplementation.<|end|><|start|> assistant to=shell<|channel|>analysis <|constrain|>xml<|message|><rfl:parameter name="command">
ls -la "C:\Users\malliath\Desktop\matlab\research_notes\Building a Python agent framework\"