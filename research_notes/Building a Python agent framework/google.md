# Google's Agent-Building Guidance (ADK, Gemini, Vertex AI, A2A)

## What is Google's Agent Development Kit (ADK)? Core abstractions and the agent loop

### Takeaway
ADK is Google's open-source, code-first agent framework (Python, TS, Go, Java, Kotlin) built around an event-loop runtime where a `Runner` orchestrates `Agent`/`LlmAgent` execution, `Session`/`SessionService` manage conversation state, and tools/callbacks/plugins extend behavior; it is model-agnostic but optimized for Gemini.

### Cited Findings
- ADK is "an open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control"; available in Python, TypeScript, Go, Java, Kotlin — [GitHub google/adk-python](https://github.com/google/adk-python); [ADK docs](https://google.github.io/adk-docs/).
- Core classes: `Agent`/`LlmAgent` (identity `name`, `description`, `model`, `instruction`, `tools`, `generate_content_config`, `input_schema`/`output_schema`, `output_key`, `include_contents`, `planner`, `code_executor`), `Runner`, `Session`/`SessionService`, `MemoryService`, `BaseTool`/`FunctionTool`, `SequentialAgent`/`ParallelAgent`/`LoopAgent` — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/); [ADK agents index](https://google.github.io/adk-docs/agents/).
- `LlmAgent` uses an LLM for non-deterministic reasoning; `name` is required, `model` required (string id like `"gemini-flash-latest"`), `description` recommended for multi-agent routing — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).
- Instructions support dynamic state templating `{var}`, `{artifact.var}`, optional `?` for missing vars — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).
- `output_key` auto-saves final response text into `session.state[output_key]`; `output_schema` enforces JSON (Pydantic in Python); warning: `output_schema` with tools only reliably supported by Gemini 3.0+ else ADK falls back to `set_model_response` tool — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).
- `include_contents` default `'default'` (history sent) or `'none'` (stateless) — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).
- Planners: `BuiltInPlanner` (Gemini thinking, `thinking_config` with `include_thoughts`, `thinking_budget`) and `PlanReActPlanner` (structured `/*PLANNING*/` `/*ACTION*/` `/*REASONING*/` `/*FINAL_ANSWER*/`) — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).
- Code execution via `code_executor=BuiltInCodeExecutor()` (Gemini code execution) — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).
- Default model can be set globally: `LlmAgent.set_default_model("gemini-flash-latest")` (v1.22.0+) — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).
- `Session` object: `id`, `app_name`, `user_id`, `events` (history), `state` (scratchpad), `last_update_time`; lifecycle: create/resume → Runner provides context → agent processes → Runner packages `Event` → `sessionService.append_event` commits state + history — [ADK Session docs](https://google.github.io/adk-docs/sessions/session/).
- `SessionService` impls: `InMemorySessionService`, `VertexAiSessionService` (Agent Runtime, requires `google-adk[gcp]`), `DatabaseSessionService` (SQL via async driver, row-level locking, `AutoMigrate`) — [ADK Session docs](https://google.github.io/adk-docs/sessions/session/).
- `MemoryService`/`BaseMemoryService`: `add_session_to_memory`, `add_events_to_memory`, `add_memory`, `search_memory`; impls `InMemoryMemoryService` (keyword), `VertexAiMemoryBankService` (LLM-extracted consolidated memories), `VertexAiRagMemoryService` (vector search over Knowledge Engine) — [ADK Memory docs](https://google.github.io/adk-docs/sessions/memory/).
- Memory tools: `load_memory`, `preload_memory`; auto-save pattern via `after_agent_callback` calling `callback_context.add_session_to_memory()` — [ADK Memory docs](https://google.github.io/adk-docs/sessions/memory/).
- Runtime event loop: `Runner` orchestrates; agent/tool/callback yields `Event`, pauses; Runner commits via services then resumes; state changes only persisted after yielded event processed; "dirty reads" possible within same invocation — [ADK Event Loop docs](https://google.github.io/adk-docs/runtime/event-loop/).
- Async is primary: `runner.run_async(...)`; sync `runner.run(...)` wraps it — [ADK Event Loop docs](https://google.github.io/adk-docs/runtime/event-loop/).
- Runner signature (Python): `Runner(agent=..., app_name=..., session_service=..., memory_service=..., artifact_service=...)`; methods `run(user_id, session_id, new_message)` / `run_async(...)` yielding events; `event.is_final_response()` — [ADK docs examples](https://google.github.io/adk-docs/agents/llm-agents/).
- Callbacks: `before_agent`/`after_agent`, `before_model`/`after_model`, `before_tool`/`after_tool`; return `None` to continue or specific object to override (e.g. `Content`, `LlmResponse`, `dict`); context objects `CallbackContext`/`ToolContext` — [ADK Callbacks docs](https://google.github.io/adk-docs/callbacks/).
- Plugins recommended over callbacks for cross-cutting policies; `GlobalInstructionPlugin` for shared instructions — [ADK Callbacks docs](https://google.github.io/adk-docs/callbacks/); [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).
- Artifacts, Skills, App management, context compression, model context caching also listed as agent features — [ADK agents index](https://google.github.io/adk-docs/agents/).

### Inferences
- ADK's design mirrors a classic agent runtime: separation of "execution logic" (agents/tools/callbacks) from "orchestration + persistence" (Runner + services), with cooperative yield/pause/resume to guarantee state consistency.
- Treating tools as ordinary Python functions auto-wrapped into `FunctionTool` lowers boilerplate, but schema/type hints become the contract.

### Gaps
- Exact internal class hierarchy (`BaseAgent._run_async_impl`) details beyond docs not captured; ADK 2.0 graph workflows (`Node`, `Edge`) only referenced, not deep-dived.

## Google's agentic patterns in Vertex AI / Gemini docs (function calling, code execution, grounding, extensions, MCP)

### Takeaway
Gemini provides native agentic primitives—function calling, code execution, Google Search grounding, URL context, and managed extensions—while ADK wraps them; MCP is the standard tool-interop layer (`McpToolset`) and ADK can itself be exposed as an MCP server.

### Cited Findings
- MCP is an open standard for connecting models to external data/tools/systems; ADK uses `McpToolset` as the client interface and supports exposing an ADK agent as an MCP server via `to_mcp_server` — [ADK MCP tools docs](https://google.github.io/adk-docs/tools-custom/mcp-tools/).
- Transport options: `StdioConnectionParams` (local subprocess, `npx`), `StreamableHTTPConnectionParams`/`SseConnectionParams` (remote), with auth headers or `auth_scheme`/`auth_credential` (Bearer/Basic/APIKey/OAuth2, token refresh) — [ADK MCP tools docs](https://google.github.io/adk-docs/tools-custom/mcp-tools/).
- MCP resources accessible via `list_resources()`/`read_resource()` or `use_mcp_resources=True` enabling `LoadMcpResourceTool` — [ADK MCP tools docs](https://google.github.io/adk-docs/tools-custom/mcp-tools/).
- Context-bloat tradeoff table: Direct MCP tool integration (high context bloat, low latency/cost) vs Agent-as-MCP-server (isolated) vs Specialized Sub-Agent Delegation (`AgentTool`, zero context bloat, model tiering) — [ADK MCP tools docs](https://google.github.io/adk-docs/tools-custom/mcp-tools/).
- Google Search grounding available as built-in tool `google_search` (used in ParallelAgent research example) — [ADK Parallel agent docs](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/).
- Code execution: `BuiltInCodeExecutor()` uses Gemini's code execution capability; Vertex Code Interpreter Extension and sandboxed execution recommended for data analysis — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/); [ADK Safety docs](https://google.github.io/adk-docs/safety/).
- Structured output: `output_schema` with tools only fully supported by Gemini 3.0+; otherwise ADK injects `set_model_response` tool — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).
- Function calling: native Python functions auto-wrapped as `FunctionTool`; docstrings + type hints drive schema; tools return dict/Map; `ToolContext` provides state, auth, memory search — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/); [ADK Safety docs](https://google.github.io/adk-docs/safety/).
- Gemini safety: configurable content filters (hate/harassment/sexually explicit/dangerous thresholds), non-configurable filters (CSAM/PII), system instructions for safety; set via `generate_content_config.safety_settings` — [ADK Safety docs](https://google.github.io/adk-docs/safety/).
- Agent Platform (Vertex) provides Model Garden (200+ models), grounding in Google Search, managed connectors, VPC-SC, Agent Engine runtime — [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/build-and-manage-multi-system-agents-with-vertex-ai); [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform).

### Inferences
- Google's stack is layered: Gemini supplies model-native capabilities (function calling, code exec, grounding, safety filters); ADK supplies orchestration, state, and tooling; Vertex supplies managed runtime, memory bank, RAG, evaluation, and enterprise controls.

### Gaps
- Detailed Vertex AI function-calling API request/response shapes beyond ADK abstraction not captured (would require ai.google.dev docs fetch).

## A2A (Agent2Agent) protocol: inter-agent communication, agent cards, task lifecycle, relation to MCP

### Takeaway
A2A is Google's open protocol for peer-to-peer agent communication over HTTP: agents discover each other via Agent Cards at `/.well-known/agent.json`, exchange stateful `Task`s with a defined lifecycle, stream `TaskStatusUpdateEvent`/`TaskArtifactUpdateEvent`, and complement MCP (A2A = horizontal agent-to-agent, MCP = vertical tool/context).

### Cited Findings
- A2A announced by Google as open protocol; complements Anthropic's MCP: MCP gives tools/context to agents, A2A connects agents to agents — [Google Developers Blog A2A](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability).
- Client agent formulates/communicates tasks; remote agent acts on them; interaction capabilities: capability discovery, task management, collaboration, UX negotiation — [Google Developers Blog A2A](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability).
- Task lifecycle states: `submitted`, `working`, `input-required`, `completed`, `canceled`, `failed`, `unknown`; tasks created by client, state managed by remote agent; artifacts are outputs; multiple tasks per session via `sessionId` — [agent2agent.info Task docs](https://agent2agent.info/docs/concepts/task); [Google Dev Forum A2A](https://discuss.google.dev/t/understanding-a2a-the-protocol-for-agent-collaboration/189103).
- Protocol methods: `message/send`, `message/stream`, `tasks/get`, `tasks/cancel`, `tasks/pushNotification/set`; streaming emits `TaskStatusUpdateEvent`, `TaskArtifactUpdateEvent`; resubscribe replays full snapshot — [Google Dev Forum A2A](https://discuss.google.dev/t/understanding-a2a-the-protocol-for-agent-collaboration/189103); [Mastra A2A blog](https://mastra.ai/blog/what-is-agent-to-agent-protocol).
- Discovery: client fetches Agent Card at `/.well-known/agent.json`; card describes capabilities/skills/auth — [Stackademic A2A](https://blog.stackademic.com/agent2agent-protocol-in-google-agent-development-kit-a-comprehensive-guide-to-building-real-time-72b9671fb374); [A2A codelab](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge).
- Content units: `Part` types `TextPart`, `DataPart`, `FilePart` — [WWT A2A deep dive](https://www.wwt.com/blog/agent-2-agent-protocol-a2a-a-deep-dive).
- A2A SDKs: Python, Go, JavaScript, Java, .NET; servers typically run alongside the agent — [CodiLime A2A](https://codilime.com/blog/a2a-protocol-explained).
- Push notifications: best-effort webhooks on terminal states (`completed`, `failed`, `canceled`, `input-required`); fall back to polling — [Mastra A2A blog](https://mastra.ai/blog/what-is-agent-to-agent-protocol).
- Agent cards support signatures; verify before sending work — [Mastra A2A blog](https://mastra.ai/blog/what-is-agent-to-agent-protocol).
- Auth: OAuth2/OIDC on behalf of user with redirect/consent; `Authorization: Bearer` — [CodiLime A2A](https://codilime.com/blog/a2a-protocol-explained).
- A2A vs MCP: "A2A provides the horizontal integration layer for peer-to-peer, multi-agent workflows, while MCP delivers vertical integration by connecting agents to specialized external services and tools" — [WWT A2A deep dive](https://www.wwt.com/blog/agent-2-agent-protocol-a2a-a-deep-dive).
- ADK integration: expose an agent as `A2AServer` (turns agent into network service) and consume via `RemoteA2aAgent` (client proxy); ADK preserves reasoning traces, long-running tools, and artifacts across A2A — [ADK A2A intro](https://google.github.io/adk-docs/a2a/intro/).
- Use A2A when agents are separate services, different teams/orgs, different languages/frameworks, or need formal contracts; prefer local sub-agents for internal code organization, performance-critical ops, shared memory — [ADK A2A intro](https://google.github.io/adk-docs/a2a/intro/).

### Inferences
- A2A's task-centric model (stateful tasks with artifacts) is designed for long-running, possibly human-in-the-loop agent work, unlike simple RPC.

### Gaps
- Full A2A spec JSON schemas (AgentCard fields, Message/Part exact schema) not fetched from a2a-protocol.org; only secondary summaries captured.

## How Google structures multi-agent systems (hierarchical/orchestrator patterns, handoffs)

### Takeaway
ADK structures multi-agent systems as a tree of agents with three families—LLM agents (brains), Workflow agents (Sequential/Parallel/Loop managers), and Custom agents (specialists)—coordinating via shared session state, LLM-driven delegation (`description`/`AgentTool`), and explicit invocation; ADK 2.0 adds graph-based workflows.

### Cited Findings
- Three agent categories: LLM (brains), Workflow (managers), Custom (specialists); hierarchy is parent-child tree (root = CEO analogy) — [Google Cloud Blog multi-agent ADK](https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk).
- Workflow agents: `SequentialAgent` (runs sub-agents in order, shared `InvocationContext` incl. `temp:` namespace), `ParallelAgent` (concurrent, independent branches, no auto state sharing), `LoopAgent` (repeats until `max_iterations` or sub-agent calls `exit_loop` setting `tool_context.actions.escalate=True`) — [ADK Sequential docs](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/); [ADK Parallel docs](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/); [ADK Loop docs](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/).
- Coordination mechanisms: (1) Shared Session State (key templating `{key?}` in instructions, `output_key` writes), (2) LLM-Driven Delegation (auto transfer via `description`), (3) Explicit Invocation (`AgentTool` wrapping sub-agent as tool) — [arjunprabhulal ADK multi-agent](https://arjunprabhulal.com/adk-multi-agent-systems); [ADK codelab](https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/3-developing-agents/build-a-multi-agent-system-with-adk).
- `CustomAgent`/`BaseAgent` allows arbitrary Python control flow between sub-agents (e.g., critic→refine with `parse_verdict`) — [aipractitioner substack](https://aipractitioner.substack.com/p/google-adk-multi-agent-orchestration); [ADK codelab](https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/3-developing-agents/build-a-multi-agent-system-with-adk).
- `SequentialAgent` example pipeline: CodeWriter → CodeReviewer → CodeRefactorer, each writing to `output_key` and next reading via `{generated_code}` templating — [ADK Sequential docs](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/).
- `ParallelAgent` example: 3 researchers in parallel then a `SynthesisAgent` merger in an outer `SequentialAgent`; branches independent, state sharing must be explicit (shared `InvocationContext` with locks or post-processing) — [ADK Parallel docs](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/).
- `LoopAgent` termination: `max_iterations` or sub-agent calls `exit_loop` tool setting `tool_context.actions.escalate = True` + `skip_summarization=True` — [ADK Loop docs](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/).
- Multi-agent patterns catalog (Google Developers Blog): Sequential Pipeline, Coordinator/Dispatcher, Parallel Fan-Out/Gather, Hierarchical Task Decomposition, Review/Critique, Iterative Refinement, Human-in-the-Loop, Composite (mix-and-match) — [Google Developers Blog multi-agent patterns](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk).
- ADK 2.0 introduces graph-based workflows (nodes, routes, data handling, human input, dynamic workflows) and task API for structured agent-to-agent delegation (multi-turn task mode, single-turn controlled output, human-in-the-loop, task agents as workflow nodes) — [GitHub adk-python](https://github.com/google/adk-python).
- Agent-as-tool (`AgentTool`) enables model tiering (e.g., Pro orchestrator, Flash sub-agent) and zero context bloat — [ADK MCP tools docs](https://google.github.io/adk-docs/tools-custom/mcp-tools/).
- ADK 2.0 Go introduces explicit `Mode` field: `ModeChat`, `ModeSingleTurn`, `ModeTask` — [ADK LlmAgent docs](https://google.github.io/adk-docs/agents/llm-agents/).

### Inferences
- Google's philosophy favors deterministic workflow agents (Sequential/Parallel/Loop) for predictable pipelines and LLM-driven routing only when adaptive decisions are needed; mixing is encouraged via composite patterns.

### Gaps
- ADK 2.0 graph workflow API exact node/edge classes not captured (docs exist under /graphs/).

## Agent evaluation, safety, guardrails, tracing/observability (Agent Engine, Cloud Trace)

### Takeaway
ADK provides an evaluation framework (criteria, user/environment simulation, custom metrics, optimization), OTel-based tracing (invoke_agent/execute_tool/generate_content spans) exportable to Cloud Trace, and layered safety (identity/auth, in-tool guardrails, Gemini safety filters, callbacks/plugins, sandboxed code execution, VPC-SC).

### Cited Findings
- Evaluation docs: Criteria, User Simulation, Environment Simulation, Custom Metrics, Optimization — [ADK eval docs](https://google.github.io/adk-docs/evaluate/criteria/) (via nav).
- Safety risks: ambiguous instructions, prompt injection/jailbreak, indirect injection via tools; risk categories: misalignment/goal corruption, harmful content/brand safety, unsafe actions (data exfiltration, unauthorized transactions, PII leak) — [ADK Safety docs](https://google.github.io/adk-docs/safety/).
- Identity/auth: Agent-Auth (service account, read-only scopes) vs User Auth (OAuth delegation) — [ADK Safety docs](https://google.github.io/adk-docs/safety/).
- In-tool guardrails: tools receive deterministic `ToolContext` (state) to enforce policies (e.g., allowed tables, SELECT-only) independent of model args — [ADK Safety docs](https://google.github.io/adk-docs/safety/).
- Gemini built-in safety: configurable content filters (hate/harassment/sexually explicit/dangerous thresholds), non-configurable filters (CSAM/PII), system instructions for safety — [ADK Safety docs](https://google.github.io/adk-docs/safety/).
- Callbacks vs plugins: callbacks for agent-specific pre-validation (`before_tool_callback` returning dict to block); plugins recommended for reusable cross-agent policies (Gemini-as-Judge plugin, Model Armor plugin, PII Redaction plugin) — [ADK Safety docs](https://google.github.io/adk-docs/safety/); [ADK Callbacks docs](https://google.github.io/adk-docs/callbacks/).
- Sandboxed code execution: use Vertex code execution / Code Interpreter extension; hermetic env (no network, cleanup) recommended — [ADK Safety docs](https://google.github.io/adk-docs/safety/).
- Network controls: VPC-SC perimeters; escape model-generated content in UIs to prevent XSS/data exfil — [ADK Safety docs](https://google.github.io/adk-docs/safety/).
- Tracing: OTel semantic conventions for GenAI; spans `invoke_agent {agent.name}`, `invoke_workflow {workflow.name}`, `execute_tool {tool.name}`, `generate_content {model.name}` with attributes (`gen_ai.usage.input_tokens`, etc.); OTLP wire format; hierarchical waterfall; context propagation across processes — [ADK Traces docs](https://google.github.io/adk-docs/observability/traces/).
- Export: env vars `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`, `OTEL_SERVICE_NAME`; `adk web --otel_to_cloud` for Cloud Trace; programmatic `maybe_set_otel_providers()` / `get_gcp_exporters(enable_cloud_tracing=True)` — [ADK Traces docs](https://google.github.io/adk-docs/observability/traces/).
- Cloud Trace integration via Agent Engine; Agent Engine handles "context, infrastructure management, scaling, security, evaluation, and monitoring" with Cloud Logging/Monitoring/Tracing — [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/build-and-manage-multi-system-agents-with-vertex-ai); [YouTube Agent Engine](https://www.youtube.com/watch?v=jstvZ2M9PiE).

### Inferences
- Google positions observability as OTel-first so ADK traces plug into any backend, not just GCP, while offering first-party Cloud Trace convenience.

### Gaps
- ADK evaluation metric names/thresholds and user-simulation APIs not captured in detail (only nav-level).

## Relationship between ADK, Vertex AI Agent Engine, and Gemini

### Takeaway
Gemini is the model layer (native function calling, code exec, grounding, safety filters); ADK is the open-source framework for building agents (model-agnostic, Gemini-optimized); Vertex AI Agent Engine is the managed runtime/deployment/ops layer for ADK (or other framework) agents, providing sessions, memory bank, RAG memory, scaling, evaluation, and monitoring.

### Cited Findings
- ADK "works with any AI model but is deeply integrated with Google's ecosystem including Gemini and Vertex AI"; optimized for Gemini — [GeeksforGeeks ADK](https://www.geeksforgeeks.org/artificial-intelligence/what-is-google-adk-agent-development-kit); [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/build-and-manage-multi-system-agents-with-vertex-ai).
- Vertex AI Agent Engine = "fully managed runtime that makes it easy to deploy AI agents to production... handles agent context, infrastructure management, scaling complexities, security, evaluation, and monitoring"; integrates with ADK or preferred framework — [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/build-and-manage-multi-system-agents-with-vertex-ai).
- Agent Engine provides `VertexAiSessionService` and `VertexAiMemoryBankService`/`VertexAiRagMemoryService` (managed memory) — [ADK Session docs](https://google.github.io/adk-docs/sessions/session/); [ADK Memory docs](https://google.github.io/adk-docs/sessions/memory/).
- Agent Platform renamed/rebranded: docs now at cloud.google.com/gemini-enterprise-agent-platform; ADK available in Python/TS/Go/Java/Kotlin — [ADK docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk).
- Gemini platform is the "advanced platform where you can build, customize, and fine-tune sophisticated agents using frameworks like ADK"; Model Garden has 200+ models — [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform).
- ADK agents deploy to Agent Engine via `provisionedReasoningEngine` resource; `VertexAiSessionService` uses Reasoning Engine ID as app_name — [Google Dev Forum](https://discuss.google.dev/t/how-to-integrate-an-agent-built-using-the-agent-development-kit-adk-and-deployed-to-vertex-agent-engine-with-gemini-enterprise/279804); [ADK Session docs](https://google.github.io/adk-docs/sessions/session/).
- Agent identity: ADK agents on Agent Engine can use Agent Identity principal (preview) — [alphasecio repo](https://github.com/alphasecio/google-adk).
- Pydantic compliance required for Agent Engine deployment (explicit class fields) — [Medium infra agent](https://medium.com/google-cloud/building-an-autonomous-infra-agent-using-vertex-ai-adk-and-google-managed-remote-mcp-e80e657ac67e).
- ADK natively supports A2A and MCP; Vertex inherits via ADK integration plus managed connectors, Google Search grounding, Workspace integrations — [metavert comparison](https://metavert.io/compare/vertex-ai-vs-google-adk).
- Features relying on Gemini-specific capabilities (Interactions API, thinking, code execution) may not work with non-Google models — [metavert comparison](https://metavert.io/compare/vertex-ai-vs-google-adk).

### Inferences
- The intended stack: develop with ADK locally (InMemory services), then swap to Vertex-backed services (VertexAiSessionService/MemoryBank) for production without changing agent code—ADK's service abstraction enables this.

### Gaps
- Exact Agent Engine pricing, SLAs, and region availability not captured.