# Google's Agent Toolkit Design

Research notes on Google's approach to agent toolkits: Gemini function calling API, ADK tool system, MCP, A2A, tool errors/retries, design patterns, discovery/registration.

## What is Google's function calling API? (Gemini function declarations, tool config)

### Takeaway
Gemini function calling is a four-step protocol where the model returns a structured `function_call` step (name + arguments) and the application executes the function and returns a `function_result` step; tools are declared inline as JSON schemas in the request's `tools` array, and the model never executes code itself.

### Cited Findings
- Function calling involves a structured interaction: (1) define function declaration, (2) call LLM with declarations, (3) execute function code (your responsibility), (4) send result back to the model. — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- Tools are passed in the `tools` array of the request; each tool is `{"type": "function", "name": ..., "description": ..., "parameters": {...}}` (JSON Schema object). — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- The model returns a `function_call` step containing `type`, `name`, and `arguments`. — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- Result is returned via a `function_result` step with `name`, `call_id` (matching the call's `id`), and `result` (content blocks). The follow-up request uses `previous_interaction_id` to chain. — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- The model supports parallel function calling (multiple functions in a single turn) and compositional/sequential function calling. — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- Interactions API is the current surface (model "gemini-3.8-flash" in docs; `client.interactions.create`). — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)

### Inferences
- Google's design keeps execution client-side; the model is a planner that emits structured calls, consistent with "kernel is the referee" invariant-style separation of concerns.
- The `call_id`/`previous_interaction_id` chaining implies stateful interaction management on Google's side rather than a stateless chat completions loop.

### Gaps
- Exact REST endpoint versioning and older `generateContent` function-calling shape (FunctionDeclaration proto) were not captured; the fetched page focused on the newer Interactions API. Unverified whether both APIs remain supported.

## How are tools defined (FunctionDeclaration, name, description, parameters, response)?

### Takeaway
A tool is a JSON-schema-backed function declaration with `name`, `description`, `parameters` (JSON Schema object with properties/required), and the function itself returns a dictionary/map result; ADK prefers a "status" key in the result dict to signal outcome to the LLM.

### Cited Findings
- Function declaration fields: `name`, `description`, `parameters` (type object with `properties` and `required`). — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)
- ADK generates the schema automatically from the Python function signature (name, docstring, type hints, defaults) when wrapping with `FunctionTool`. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- Parameters are required if they have a type hint but no default value; optional if a default value is given (or `typing.Optional`/`| None`). — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- `*args` and `**kwargs` are ignored by ADK when generating the tool schema; only explicitly defined parameters are exposed to the LLM. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- Preferred return type is a dict/map/object; non-dict returns are auto-wrapped into `{"result": <value>}`. Best practice: include a "status" key ("success"/"error"/"pending") and human-readable error messages. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- Docstrings become the tool description sent to the LLM. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- JSON schema tool declarations (`JSON_SCHEMA_FOR_FUNC_DECL`) are enabled by default in ADK Python, generated via Pydantic, and can be toggled by env var or `override_feature_enabled`. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- ADK supports `ToolContext` injection (typed parameter) for session state/actions/artifacts; ADK detects it by type, not name. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)

### Inferences
- Google relies heavily on type hints + docstrings as the single source of truth for schemas, reducing boilerplate and keeping code/docs aligned.
- The "status key" convention is a soft contract: the LLM interprets outcome via content rather than structured error codes.

### Gaps
- Whether `FunctionDeclaration` (protobuf) in the older `generateContent` API exposes a separate `response` schema field was not captured; unverified.

## What is the Agent Development Kit (ADK) tool system (FunctionTool, AgentTool, McpToolset, etc.)?

### Takeaway
ADK provides a layered tool taxonomy: `FunctionTool`/`LongRunningFunctionTool` for Python functions, `AgentTool` for in-process sub-agent delegation, `McpToolset` for external MCP servers, plus OpenAPI tools, auth, and built-in grounding tools; all implement a common `BaseTool`/`Toolset` interface.

### Cited Findings
- Transforming a Python function into a tool: assigning a function to an agent's `tools` list auto-wraps it as `FunctionTool`; explicit `FunctionTool(func=...)` is also supported. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- `LongRunningFunctionTool` subclass for tasks managed outside the agent workflow (human-in-the-loop, approvals); agent run pauses and client can send intermediate/final responses. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- `AgentTool` wraps an `LlmAgent` to expose it as a native tool to a parent orchestrator (in-process sub-agent delegation). — [google.github.io/adk-docs/tools-custom/mcp-tools/agent-managed/](https://google.github.io/adk-docs/tools-custom/mcp-tools/agent-managed/)
- `McpToolset` is the ADK↔MCP server interface: handshake + `list_tools` discovery, adapts external schemas into ADK `BaseTool` instances, proxies `call_tool`. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- ADK supports exposing an agent as an MCP server via `to_mcp_server`, and sub-agent delegation via `AgentTool`. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- `tool_filter` (list or predicate) restricts which tools from a toolset are exposed to the LLM. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/), [agent-managed](https://google.github.io/adk-docs/tools-custom/mcp-tools/agent-managed/)
- Built-in grounding tools: Google Search grounding, Google Maps grounding, code execution, URL context, file search, computer use. — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling) (nav), [adk-docs grounding](https://google.github.io/adk-docs/grounding/)

### Inferences
- ADK's tool abstraction is backend-agnostic: the same agent `tools` list can mix native functions, MCP servers, and sub-agents, giving a unified delegation surface.
- `tool_filter` is the primary cognitive-scoping mechanism, preventing schema bloat.

### Gaps
- Full enumeration of built-in ADK tool classes (e.g., `GoogleSearchTool`, `CodeExecutionTool`) and their exact import paths were not captured from docs; unverified.

## How does ADK handle tool execution (parallel, sequential, callbacks)?

### Takeaway
ADK runs function tools in parallel when they are defined as `async def` (asyncio event loop) since v1.10.0; synchronous tools block others; execution is bracketed by before/after tool callbacks that can skip or override results; long-running tools pause the run.

### Cited Findings
- Starting v1.10.0, ADK attempts to run agent-requested function tools in parallel; requires async functions; synchronous tools block others even if others are async. — [google.github.io/adk-docs/tools-custom/performance/](https://google.github.io/adk-docs/tools-custom/performance/)
- Parallel-ready patterns: `async with` for HTTP/DB, `await asyncio.sleep(0)` yield points in long loops, thread pools for CPU-bound work, chunking + yielding. — [google.github.io/adk-docs/tools-custom/performance/](https://google.github.io/adk-docs/tools-custom/performance/)
- Prompt/tool-description hints can encourage the model to emit parallel calls. — [google.github.io/adk-docs/tools-custom/performance/](https://google.github.io/adk-docs/tools-custom/performance/)
- Before Tool Callback: runs before `run_async`; can modify args; returning a dict skips execution and uses that dict as result (cache/override). Returning `None` lets tool run. — [google.github.io/adk-docs/callbacks/types-of-callbacks/](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- After Tool Callback: runs after successful execution; can replace result by returning a new dict; `None` keeps original. Non-dict results are wrapped into `{"result": ...}` only after callback runs. — [google.github.io/adk-docs/callbacks/types-of-callbacks/](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- `on_tool_error_callback` (Python) / `OnToolErrorCallbacks` (Go): runs on tool exception; returning a dict suppresses the exception and uses it as result. — [google.github.io/adk-docs/callbacks/types-of-callbacks/](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- Before/After Model Callbacks can skip the LLM call (return `LlmResponse`) or post-process responses; `on_model_error_callback` handles model exceptions. — [google.github.io/adk-docs/callbacks/types-of-callbacks/](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- Agent lifecycle callbacks (`before_agent`/`after_agent`) gate or append output. — [google.github.io/adk-docs/callbacks/types-of-callbacks/](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- Long-running tools pause the agent run; client sends intermediate/final `FunctionResponse` to resume; invocation ID must match for Resume feature. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- Sequential/parallel/loop workflow agents (`SequentialAgent`, `ParallelAgent`, `LoopAgent`) orchestrate multiple agents. — [google.github.io/adk-docs/agents/](https://google.github.io/adk-docs/agents/) (nav)

### Inferences
- ADK's execution model is async-first with explicit blocking semantics, pushing developers toward cooperative concurrency.
- Callbacks are the primary extension point for cross-cutting concerns (logging, auth, caching, guardrails) without modifying tool code.

### Gaps
- Whether ADK retries failed tool calls automatically was not documented in fetched pages; appears to be left to `on_tool_error_callback` / app logic. Unverified.

## What is Google's MCP support (McpToolset, transports, auth)?

### Takeaway
ADK's `McpToolset` is a client adapter that discovers tools from an MCP server over stdio or HTTP/SSE, adapts schemas to ADK tools, proxies calls, and handles auth (headers, bearer, OAuth2 with token refresh); ADK can also expose an agent as an MCP server.

### Cited Findings
- MCP is an open standard client-server protocol for connecting models to external data/tools/systems. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- `McpToolset` manages connection lifecycle, handshake, `list_tools` discovery, and graceful shutdown; connections are re-initialized on restore (not auto-reestablished). — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- Transports: `StdioConnectionParams` (local subprocess via npx/python) and `StreamableHTTPConnectionParams`/`SseConnectionParams` (remote HTTP/SSE with headers, timeout, sse_read_timeout). — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- Auth: `auth_scheme` (Bearer/Basic/APIKey/OAuth2) + `auth_credential`; ADK builds Authorization headers and manages OAuth2 refresh. Manual header injection also shown. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- Resources: `list_resources()` / `read_resource(name)`; `use_mcp_resources=True` equips the LLM with `LoadMcpResourceTool`. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- Tool filtering via `tool_filter=[...]` for security/scoping; timeouts; explicit `close()`/context managers in custom runtimes. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- Production rule: `McpToolset` must be instantiated synchronously in `agent.py` (no async factory) for deployed agents. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- Environment-aware connection selection (K_SERVICE env var → HTTP; else stdio) is recommended. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)

### Inferences
- Google treats MCP as the interoperability layer rather than a proprietary protocol, aligning ADK with the broader ecosystem.
- Synchronous instantiation requirement for production reflects deployment constraints (Cloud Run/GKE).

### Gaps
- MCP sampling/elicitation and advanced server features support in ADK was not covered; unverified.

## What is A2A and how does it relate to tool delegation?

### Takeaway
A2A (Agent2Agent) is an open protocol for networked agent-to-agent communication; in ADK an agent can be exposed as an A2A server and consumed via `RemoteA2aAgent`, which feels like a tool to the parent; ADK also supports in-process delegation via `AgentTool` and context-isolated MCP sub-agents.

### Cited Findings
- A2A is the standard for agent-to-agent communication over a network; agents run as separate services. — [google.github.io/adk-docs/a2a/intro/](https://google.github.io/adk-docs/a2a/intro/)
- Use A2A when the target is a separate standalone service, different team/org, cross-language/framework, or when a formal contract is needed; use local sub-agents for internal organization, performance-critical ops, shared memory. — [google.github.io/adk-docs/a2a/intro/](https://google.github.io/adk-docs/a2a/intro/)
- ADK workflow: expose agent as `A2AServer`; consume via `RemoteA2aAgent` (client proxy). ADK preserves reasoning traces, long-running tools, and artifacts across A2A. — [google.github.io/adk-docs/a2a/intro/](https://google.github.io/adk-docs/a2a/intro/)
- `AgentTool` wraps an `LlmAgent` as a native tool for in-process hierarchical delegation, isolating intermediate reasoning/tool calls in the sub-agent loop (zero context bloat in parent). — [google.github.io/adk-docs/tools-custom/mcp-tools/agent-managed/](https://google.github.io/adk-docs/tools-custom/mcp-tools/agent-managed/)
- Comparison table: Direct MCP (low latency, high context bloat), Agent-exposed MCP server (isolated), AgentTool sub-agent (zero context bloat, model tiering, higher cost/latency). — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)

### Inferences
- Google provides three delegation tiers (in-process AgentTool, MCP sub-agent, networked A2A) letting developers trade latency vs. isolation vs. cross-org interoperability.
- A2A is positioned as the cross-boundary standard, while `AgentTool`/`McpToolset` cover intra-process and intra-team cases.

### Gaps
- A2A protocol spec details (task lifecycle, streaming, auth) at a2a-protocol.org were not fetched; unverified.

## How does Google handle tool errors, retries, and result formatting?

### Takeaway
Google's toolkit does not appear to auto-retry tool calls; instead it exposes structured error handling via `on_tool_error_callback`/`on_model_error_callback`, requires tools to return descriptive dicts with a "status" key, and wraps non-dict results; validation feedback is structured (JSON), not prose.

### Cited Findings
- Tool functions should return dicts with a "status" key and human-readable "error_message" rather than numeric codes; LLM interprets the result. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- Non-dict tool returns are auto-wrapped into `{"result": <value>}`. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- `on_tool_error_callback` (Python) / `OnToolErrorCallbacks` (Go): runs on tool exception; returning a dict suppresses the exception and uses it as the tool result; returning an error replaces the original. — [google.github.io/adk-docs/callbacks/types-of-callbacks/](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- `on_model_error_callback` / `OnModelErrorCallbacks`: same pattern for model call failures. — [google.github.io/adk-docs/callbacks/types-of-callbacks/](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- Before Tool Callback returning a dict skips execution (caching/override); returning `None` lets it run. Empty dict `{}` counts as override, not "let run". — [google.github.io/adk-docs/callbacks/types-of-callbacks/](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- Invariants: tools return structured dicts (`{"ok", ...}` style) and never raise into the loop; validation feedback is JSON. — ThinkToCad `AGENTS.md` (local repo context)
- Gemini API returns function calls as structured steps; errors in execution are reported back via `function_result` content blocks. — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling)

### Inferences
- Error handling is delegated to callbacks and to the tool's own return dict, keeping the LLM in the loop for recovery rather than silently retrying.
- The "never raise into the loop" invariant aligns with Google's pattern of returning structured errors as tool results.

### Gaps
- Automatic retry/backoff policies (if any) in ADK or Gemini were not found in fetched docs; unverified. Flagged as unverified.

## What are Google's patterns for tool design (grounding, code execution, Google Search)?

### Takeaway
Google's toolkit emphasizes grounding tools (Google Search, Google Maps, URL context, file search), code execution, and computer use as first-party tools, combined with function calling via "tool combination"; design guidance stresses fewer parameters, simple types, meaningful names, async/parallel-ready, and descriptive docstrings.

### Cited Findings
- Gemini API Tools overview lists: Google Search, Google Maps, Code execution, URL context, Computer use, File search, and "Combine tools and function calling". — [ai.google.dev/gemini-api/docs/function-calling](https://ai.google.dev/gemini-api/docs/function-calling) (nav)
- ADK grounding docs: Google Search Grounding, Grounding with Search. — [google.github.io/adk-docs/grounding/](https://google.github.io/adk-docs/grounding/)
- ADK best practices for function tools: fewer parameters, simple data types (str/int), meaningful names, build for parallel execution, descriptive docstrings. — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- Managed agents (first-party) come with built-in server-side tools like web search and code execution. — [google.github.io/adk-docs/agents/](https://google.github.io/adk-docs/agents/) (nav)
- Agent Skills (agentskills.io) extend capabilities efficiently within context window limits. — [google.github.io/adk-docs/agents/](https://google.github.io/adk-docs/agents/) (nav)

### Inferences
- Google treats grounding as a first-class tool category, not an afterthought, reflecting a RAG/grounding-first philosophy for factual accuracy.
- Tool-combination support (built-in + function calling in one request) is a key differentiator.

### Gaps
- Detailed API shape for code execution / Google Search tools (parameters, result format) was not fetched; unverified.

## How does ADK handle tool discovery and registration?

### Takeaway
ADK registers tools statically via the agent's `tools` list (functions, toolsets, MCP adapters); MCP toolsets discover tools dynamically via `list_tools` at init; there is no global tool registry—scoping happens per-agent via `tool_filter`; skills and plugins extend capabilities separately.

### Cited Findings
- Tools are provided per-agent in the `tools` list (functions, `FunctionTool`, `AgentTool`, `McpToolset`, built-ins). — [google.github.io/adk-docs/tools-custom/function-tools/](https://google.github.io/adk-docs/tools-custom/function-tools/)
- `McpToolset` performs protocol handshake + `list_tools` discovery at initialization and adapts schemas into ADK tools. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- `tool_filter` (list of names or predicate) scopes which discovered tools reach the LLM. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/), [agent-managed](https://google.github.io/adk-docs/tools-custom/mcp-tools/agent-managed/)
- OpenAPI tools generate tools from an OpenAPI spec (implied by nav entry "OpenAPI tools"). — [google.github.io/adk-docs/tools-custom/](https://google.github.io/adk-docs/tools-custom/) (nav)
- Authentication is configured per-toolset via `auth_scheme`/`auth_credential`. — [google.github.io/adk-docs/tools-custom/mcp-tools/](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- Skills for Agents (agentskills.io) and Plugins extend capabilities. — [google.github.io/adk-docs/agents/](https://google.github.io/adk-docs/agents/) (nav)

### Inferences
- Discovery is pull-based (MCP list_tools) at init time, not a runtime registry lookup; this favors deterministic, auditable tool sets.
- Per-agent scoping via `tool_filter` is Google's answer to "too many tools" cognitive overload.

### Gaps
- Whether ADK supports dynamic tool registration at runtime (adding tools mid-run) was not documented in fetched pages; unverified.
