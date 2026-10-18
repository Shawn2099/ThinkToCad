# OpenAI agent toolkit design

## What is OpenAI's function calling / tool calling API? (chat.completions tools vs Responses API tools)

### Takeaway
OpenAI exposes tool calling in two API primitives: the legacy Chat Completions `tools` array (non-strict by default) and the newer Responses API, which is recommended for all new projects and runs an agentic loop by default with built-in/hosted tools, stateful context, and encrypted reasoning.

### Cited Findings
- Function calling (tool calling) lets models interface with external systems; functions are declared in the `tools` parameter of each API request, each with `type: "function"`, `name`, `description`, `parameters` (JSON Schema), and `strict`. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- Chat Completions requests remain non-strict by default; Responses requests attempt to normalize schemas into strict mode when possible and fall back to non-strict if incompatible. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- The Responses API is a unified interface with built-in tools (web search, file search, computer use, code interpreter, remote MCP), seamless multi-turn interactions, native multimodal support, and an agentic loop by default where the model can call multiple tools within one API request. — [Migrate to the Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses)
- Responses benefits: better performance with reasoning models, lower costs via cache utilization (40–80% improvement in internal tests), stateful context (`store: true`), flexible inputs, encrypted reasoning, future-proofing. — [Migrate to the Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses)
- `/v1/responses` is an agentic loop: it preserves reasoning state across turns (Chat Completions drops reasoning between calls), emits multiple output items (tool calls, structured outputs, intermediate steps), and hosted tool execution happens server-side. — [Why we built the Responses API](https://developers.openai.com/blog/responses-api)
- In Responses, custom tools yield control back to the client (client-managed loop); hosted tools (code interpreter, MCP, shell, web search, file search) execute server-side with the API orchestrating the loop. — [From model to agent: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- Chat Completions function calling is multi-step: define functions → model decides → client executes → append results → model responds; with built-in tools execution is automatic server-side. — [Building agents](https://developers.openai.com/tracks/building-agents)

### Inferences
- OpenAI's direction is to push tool execution server-side (hosted tools, shell containers, MCP) to reduce client round-trips and preserve reasoning state; client-managed loops remain for custom functions needing app-side secrets/logic.

### Gaps
- No independent benchmark numbers beyond OpenAI's internal claims (e.g., 3% SWE-bench, 40–80% cache improvement) were verified externally.

## How are tools defined (JSON Schema, strict mode, parameters, descriptions)?

### Takeaway
Tools are defined as JSON Schema objects with `type`, `name`, `description`, `parameters`, and `strict`; strict mode (recommended always on) enforces schema adherence via Structured Outputs, requiring `additionalProperties: false` and all fields `required` (optionals expressed as `type: ["string","null"]`).

### Cited Findings
- A function definition has fields `type` (always `"function"`), `name` (a-z, A-Z, 0-9, underscores/dashes, max 64 chars), `description`, `parameters` (JSON Schema), `strict` (boolean). — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling); [openai-python FunctionDefinition](https://github.com/openai/openai-python/blob/main/src/openai/types/shared_params/function_definition.py)
- Strict mode ensures function calls adhere to the schema; requirements: (1) `additionalProperties: false` for each object; (2) all fields in `properties` marked `required`; optional fields use `null` type union. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- If `strict: true` sent with non-conforming schema, request rejected; if `strict` omitted, Responses normalizes when possible (fallback to non-strict shown as `strict: false`), Chat Completions stays non-strict by default; to opt out in Responses set `strict: false`. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- Strict mode limitations: subset of JSON Schema only; fine-tuned models incur first-request schema processing/caching latency; schemas not ZDR-eligible. — [Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/)
- Structured Outputs via function calling available on all models supporting tools (gpt-4-0613 and later, gpt-3.5-turbo-0613 and later); response-format structured outputs only on newer snapshots. — [Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/)
- Structured Outputs is not compatible with parallel function calls (may not match schemas); set `parallel_tool_calls: false` to disable. — [Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/)
- OpenAI best practices for defining functions: clear/detailed names, param descriptions, instructions; use enums/object structure to prevent invalid states; "pass the intern test"; offload known args and combine sequential functions; keep initially available functions small (<20 soft suggestion); leverage Playground and fine-tuning. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- For deferred tools, put detailed guidance in function description and keep namespace description concise. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)

### Inferences
- OpenAI treats schema strictness as a contract between model and tool: the schema is both validation and generation constraint, shifting burden from runtime validation to API-level structured outputs.

### Gaps
- The exact supported JSON Schema subset for strict mode is documented but not reproduced here; consult the "supported schemas" reference. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)

## What tool types exist (function, code_interpreter, file_search, web_search, computer_use, MCP)?

### Takeaway
OpenAI supports hosted tools (web_search, file_search, code_interpreter, image_generation, tool_search, programmatic_tool_calling, MCP), local/built-in execution tools (computer use, apply_patch, shell), custom function tools, agents-as-tools, and sandbox capabilities.

### Cited Findings
- Hosted OpenAI tools run alongside the model on OpenAI servers: Web search, File/retrieval search, Code Interpreter, Image generation, Tool search, Programmatic Tool Calling. — [Tools | OpenAI Agents SDK (JS)](https://openai.github.io/openai-agents-js/guides/tools/); [Using tools | OpenAI API](https://developers.openai.com/api/docs/guides/tools)
- Built-in execution tools: ComputerTool and ApplyPatchTool always run in your environment; ShellTool can run locally or in a hosted container. — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/)
- Function tools wrap any local function with a JSON schema so the LLM can call it. — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/)
- Agents as tools: expose an entire Agent as a callable tool (manager retains control of user-facing reply). — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/)
- MCP servers: attach a Model Context Protocol server (local or remote); hosted MCP tools push the whole round-trip into OpenAI infra. — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/); [MCP connections | OpenAI API](https://developers.openai.com/api/docs/guides/agents-api/tools/mcp)
- Sandbox capabilities: workspace-scoped shell, filesystem, skills, memory, compaction tools for SandboxAgent. — [Tools | OpenAI Agents SDK (JS)](https://openai.github.io/openai-agents-js/guides/tools/)
- Experimental: Codex tool wraps the Codex SDK as a function tool. — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/)
- Programmatic Tool Calling: model writes/runs JavaScript coordinating tools; available tool types supporting `allowed_callers: ["programmatic"]`: function, custom, mcp, apply_patch, local/hosted shell, code_interpreter. — [Programmatic Tool Calling | OpenAI API](https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling)
- Only `gpt-5.4` and later models support `tool_search`. — [Using tools | OpenAI API](https://developers.openai.com/api/docs/guides/tools)

### Inferences
- OpenAI's taxonomy splits capabilities by where execution happens (hosted vs. local) and by whether the model composes them (programmatic JS), reflecting a layered toolkit rather than a flat tool list.

### Gaps
- The full set of connector-backed hosted MCP tools and their approval semantics beyond `require_approval` were not fully enumerated in fetched sources.

## How does parallel tool calling work? How does the agent loop handle tool results?

### Takeaway
The model may emit zero/one/multiple function calls per turn; clients must execute all and return each result matched to its `call_id`; the SDK/Responses API loops until a final answer or exit condition; parallel calls can be disabled for strict-mode compatibility.

### Cited Findings
- "Since model responses can include zero, one, or multiple calls, it is best practice to assume there are several." — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- Each function call output entry has `call_id`, `name`, JSON-encoded `arguments`; results returned via `function_call_output` with the same `call_id`. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- Result formatting: typically a string (JSON, error codes, plain text); images/files can be passed as arrays; no-return functions should return a success/failure string. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- Agent loop (SDK): (1) call model, (2) inspect output, (3) if tool calls execute and continue, (4) if handoff switch agents and continue, (5) if final answer return result. — [Running agents | OpenAI API](https://developers.openai.com/api/docs/guides/agents/running-agents)
- Exit conditions: final-output tool invoked (defined by output type), or model returns response without tool calls; max turns enforced. — [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Partial failures in parallel calls: return all results (successes normal, failures flagged) each matched to its own id; don't abort the batch. — [Returning Tool Errors to an LLM for Graceful Recovery](https://ai-tldr.dev/learn/llm-apis/function-calling/handling-tool-errors/) (third-party; treat as guidance, not OpenAI primary source)
- Shell command output can be executed concurrently using separate container sessions, multiplexed back into structured tool outputs. — [From model to agent: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- `parallel_tool_calls` parameter controls parallel calling; disable when using Structured Outputs with function calling. — [Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/)

### Inferences
- OpenAI's loop is model-driven: the client/SDK executes whatever calls the model emits and feeds all results back; the model decides retries/next steps, not a hard-coded orchestration.

### Gaps
- Exact default value and model-specific support matrix for `parallel_tool_calls` in Responses vs Chat Completions were not fully verified from primary sources.

## What is the OpenAI Agents SDK's tool system (Tool, FunctionTool, AgentTool, MCP tools)?

### Takeaway
The Agents SDK centers on `FunctionTool` (dataclass) with `name`, `description`, `params_json_schema`, `on_invoke_tool`, `strict_json_schema`; created via `@function_tool`/`@tool` with auto-schema from Python type hints + docstrings, or hand-built; plus hosted tools, execution tools, agents-as-tools, MCP servers, and sandbox capabilities.

### Cited Findings
- `FunctionTool` fields: `name`, `description`, `params_json_schema` (JSON schema), `on_invoke_tool(ctx, args_json) -> output`, `strict_json_schema` (default True), `is_enabled`, etc. — [openai-agents-python src/agents/tool.py](https://raw.githubusercontent.com/openai/openai-agents-python/main/src/agents/tool.py)
- `@function_tool`/`@tool` auto-generates name from function name, description from docstring, schema from type hints via `inspect` + `griffe` + `pydantic`; functions may be sync/async and optionally take `RunContextWrapper` as first arg. — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/)
- Decorator overrides: `name_override`, `description_override`, docstring style, `defer_loading`, `needs_approval`, `tool_input_guardrails`, `tool_output_guardrails`, `failure_error_function`. — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/); [Guardrails | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/)
- Custom `FunctionTool`: provide `name`, `description`, `params_json_schema`, `on_invoke_tool` (async). — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/)
- Agents as tools: `agent.as_tool(tool_name=..., tool_description=...)` exposes a specialist; manager stays in control. — [Agents | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/agents/)
- MCP: local servers (`MCPServerStdio`, `MCPServerSse`, `MCPServerStreamableHttp`) discovered via `list_tools()` per run; hosted MCP via `HostedMCPTool`; tool filtering (static/dynamic), caching (`cacheToolsList`), server-prefixed names. — [MCP | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/mcp/)
- MCP config: `convert_schemas_to_strict`, `failure_error_function`, `include_server_in_tool_names`. — [MCP | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/mcp/)
- Tool search in SDK: `@function_tool(defer_loading=True)`, `tool_namespace(name, description, tools)`, `HostedMCPTool(tool_config={..., "defer_loading": True})`, exactly one `ToolSearchTool()`. — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/)
- `tool_use_behavior` controls whether tool results loop back to model or end run; `reset_tool_choice` resets after a tool call (default True) to avoid loops. — [Agents | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/agents/)

### Inferences
- The SDK's tool system mirrors the API's JSON-schema contract but adds Pythonic ergonomics (type hints, docstrings) and runtime policy (approvals, guardrails, timeouts) around invocation.

### Gaps
- The JS SDK's exact `Tool` base class hierarchy and Zod-schema generation details were not fetched in depth; only Python SDK internals were inspected.

## How does OpenAI handle tool errors, retries, and result formatting?

### Takeaway
OpenAI's pattern: never crash the loop—catch exceptions and return a model-visible error message (default generic "An error occurred while running the tool. Please try again."); SDK supports custom `failure_error_function` or `None` to re-raise; Agents API distinguishes success/error via `success` flag; retries are bounded in client code.

### Cited Findings
- `FunctionTool.on_invoke_tool` doc: "In case of errors, you can either raise an Exception (which will cause the run to fail) or return a string error message (which will be sent back to the LLM)." — [openai-agents-python src/agents/tool.py](https://raw.githubusercontent.com/openai/openai-agents-python/main/src/agents/tool.py)
- Default `failure_error_function` returns fixed `"An error occurred while running the tool. Please try again."` without exposing exception; custom formatter can return app-approved details; `None` re-raises. — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/)
- `default_tool_error_function` deliberately avoids exposing exception to model; custom `failure_error_function` for details. — [openai-agents-python src/agents/tool.py](https://raw.githubusercontent.com/openai/openai-agents-python/main/src/agents/tool.py)
- Agents API function result: set `success: true` + `output` string, or `success: false` + `error` message; result size limit <4 MiB; retry same `turn_id`/`call_id` while pending. — [Functions | OpenAI API (Agents)](https://developers.openai.com/api/docs/guides/agents-api/tools/functions)
- Tool result should typically be a string (JSON, error codes, plain text); images/files as arrays; no-return → success/failure string. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- Recommended error-message design: specific cause, fix/next step, explicit retryability ("temporary"/"try again"/"do not retry"/"permanent"); short plain text; don't leak secrets; distinguish bad input vs transient vs permanent. — [Returning Tool Errors to an LLM for Graceful Recovery](https://ai-tldr.dev/learn/llm-apis/function-calling/handling-tool-errors/) (third-party guidance)
- Retries inside code vs. model-visible: retry transient failures silently with backoff; surface to model only when different input needed. — [Returning Tool Errors to an LLM for Graceful Recovery](https://ai-tldr.dev/learn/llm-apis/function-calling/handling-tool-errors/) (third-party guidance)
- Bounded loops: cap total iterations (e.g., 8–10) and repeated failures per tool; repeated failures become permanent-style "do not retry". — [Returning Tool Errors to an LLM for Graceful Recovery](https://ai-tldr.dev/learn/llm-apis/function-calling/handling-tool-errors/) (third-party guidance)
- `tool_error_formatter` in `RunConfig` allows overriding message formatting; MCP `failure_error_function` controls MCP failure surfacing. — [MCP | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/mcp/); [openai-agents-python src/agents/tool.py](https://raw.githubusercontent.com/openai/openai-agents-python/main/src/agents/tool.py)
- OpenAI o-series prompting guide: set `strict: true` to catch bad arguments; validate arguments against format before sending. — [o3/o4-mini Function Calling Guide](https://developers.openai.com/cookbook/examples/o-series/o3o4-mini_prompting_guide)

### Inferences
- OpenAI's default stance is to hide raw exceptions from the model (security + noise) and let developers opt into richer, app-approved error text; this aligns with "tools return structured errors, never raise into loop" invariant.

### Gaps
- No OpenAI-primary source specifies a recommended max-turn default in the SDK beyond configurable `max_turns`; exact default not verified.

## What is the "tool as a contract" philosophy? How do they recommend designing tools?

### Takeaway
OpenAI frames tools as standardized, reusable definitions with clear names/params/descriptions; "pass the intern test"; principle of least surprise; reduce tool count exposed at once; split agents when tool overload; categorize tools as Data/Action/Orchestration.

### Cited Findings
- "Each tool should have a standardized definition, enabling flexible, many-to-many relationships between tools and agents. Well-documented, thoroughly tested, and reusable tools improve discoverability, simplify version management, and prevent redundant definitions." — [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Tool categories: Data (retrieve context), Action (interact with systems), Orchestration (agents as tools). — [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Best practices for defining functions (OpenAI): clear/detailed names/params/instructions; use enums/object structure to prevent invalid states (e.g., avoid `toggle_light(on, off)`); pass the intern test; offload known args; combine sequential functions; keep initially available functions small (<20 soft); evaluate with different counts; use tool search to defer. — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- "Make the functions predictable and intuitive. (principle of least surprise)" — [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- Tool overload guidance: issue isn't number but similarity/overlap; some manage >15 distinct tools, others struggle with <10 overlapping; split agents if clarity improvements don't help. — [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Risk ratings for tools (low/medium/high) by read-only vs write, reversibility, permissions, financial impact; trigger guardrail checks or human escalation for high-risk. — [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Guardrails: input/output/tool guardrails, tripwires; human-in-the-loop approvals for sensitive actions. — [Guardrails and human review | OpenAI API](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals); [Guardrails | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/)

### Inferences
- "Tool as a contract" in OpenAI's framing means the tool definition (name + schema + description) is the sole interface the model sees; therefore descriptions and schemas must be self-sufficient ("intern test").

### Gaps
- No single OpenAI doc uses the exact phrase "tool as a contract"; the philosophy is inferred from the standardized-definition and intern-test guidance.

## What is the Responses API agentic loop (server-managed vs client-managed)?

### Takeaway
Responses API can manage the loop server-side for hosted tools (shell, code interpreter, MCP, web/file search) with preserved reasoning state and streaming output; for custom function tools control returns to the client, which must execute and feed results back (or use the Agents SDK/Agents API to orchestrate).

### Cited Findings
- Responses API orchestrates between model and hosted tools out of the box: assembles context, model decides next action, forwards shell commands to container runtime, streams output back, repeats until completion without additional commands. — [From model to agent: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- When used with custom tools, Responses yields control back to the client and the client requires its own harness. — [From model to agent: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- Agents API runs the agent loop for you: configure tools in `agent.tools`, handle function calls in your app, connect sandbox when needed; Programmatic Tool Calling enabled by default. — [Using tools | OpenAI API](https://developers.openai.com/api/docs/guides/tools)
- Agents SDK `Runner.run` loops until exit condition; supports server-managed state via `conversationId`/`previousResponseId` or local replay via `result.history`/`to_input_list()`, plus sessions. — [Running agents | OpenAI API](https://developers.openai.com/api/docs/guides/agents/running-agents)
- Stateful context: `store: true` maintains state turn-to-turn preserving reasoning/tool context. — [Migrate to the Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses)
- Shell command output streamed near real-time; multiple commands can run concurrently via separate container sessions. — [From model to agent: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)

### Inferences
- OpenAI offers a spectrum: pure client loop (Chat Completions/custom functions), server-orchestrated hosted tools (Responses), fully managed (Agents API/SDK); choice depends on where execution must live.

### Gaps
- Detailed server-side retry/timeout policies for hosted shell containers were not documented in fetched sources.

## How does OpenAI handle tool discovery and registration?

### Takeaway
Discovery ranges from eager loading of all tool schemas, to hosted tool search that defers definitions until needed (namespaces/MCP servers recommended, <10 functions per namespace), to client-executed search; MCP tools discovered via `list_tools()` with optional caching and filtering.

### Cited Findings
- Tool search: model dynamically searches/loads tools; avoids loading all definitions up front; saves tokens; preserves cache by injecting discovered tools at end of context. — [Tool search | OpenAI API](https://developers.openai.com/api/docs/guides/tools-tool-search)
- Activation: add `tool_search` tool; mark functions/MCP with `defer_loading: true`. Only `gpt-5.4`+ supports. — [Tool search | OpenAI API](https://developers.openai.com/api/docs/guides/tools-tool-search)
- Namespaces: group related tools under a name+description; `defer_loading` applies to functions inside; mix deferred/immediate; recommended <10 functions per namespace; use namespaces/MCP over individually deferred functions. — [Tool search | OpenAI API](https://developers.openai.com/api/docs/guides/tools-tool-search)
- Two search types: hosted (OpenAI searches declared deferred tools) and client-executed (app performs lookup, returns `tool_search_output`). — [Tool search | OpenAI API](https://developers.openai.com/api/docs/guides/tools-tool-search)
- Agents API: loads eagerly by default; defer selected functions with `defer_loading: true` + `tool_search`; MCP tools use automatic discovery and deferral when supported. — [Tool search | OpenAI API](https://developers.openai.com/api/docs/guides/tools-tool-search)
- SDK: `ToolSearchTool()`, `tool_namespace()`, `@function_tool(defer_loading=True)`, `HostedMCPTool(tool_config={..., "defer_loading": True})`; add exactly one `ToolSearchTool()`. — [Tools | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/tools/)
- MCP discovery: each run may call `list_tools()`; cache with `cacheToolsList: true`; invalidate via `invalidateToolsCache()`; filter with `create_static_tool_filter`/dynamic callable. — [MCP | OpenAI Agents SDK (JS)](https://openai.github.io/openai-agents-js/guides/mcp/); [MCP | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/mcp/)
- Local MCP tools can be server-prefixed to avoid name collisions; tool schemas can be converted to strict mode best-effort. — [MCP | OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/mcp/)

### Inferences
- OpenAI's discovery model is "declare everything, load lazily": full definitions supplied up front but only surfaced to the model on demand, balancing catalog size with context cost.

### Gaps
- Performance/latency impact of `list_tools()` caching and invalidation strategies beyond docs was not measured.

## What are OpenAI's guardrails for tools (input/output/tool guardrails, tripwires)?

### Takeaway
OpenAI implements layered guardrails: agent-level input/output guardrails (run only first agent / final-output agent), tool-level guardrails around every guarded function-tool invocation, tripwire exceptions that halt execution, and human-in-the-loop approvals for sensitive actions.

### Cited Findings
- Two kinds of guardrails: input (initial user input) and output (final agent output); plus tool guardrails. — [Guardrails | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/)
- Workflow boundaries: input guardrails run only for first agent in chain; output guardrails only for agent producing final output; tool guardrails run on every guarded function-tool invocation including local MCP (input before execution, output after). — [Guardrails | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/)
- Tool guardrails: input can skip call, replace output with message, or raise tripwire; output can replace output or raise tripwire; approval ordering configurable via `RunConfig.tool_execution`. — [Guardrails | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/)
- Tripwires: `InputGuardrailTripwireTriggered`, `OutputGuardrailTripwireTriggered`, `ToolInputGuardrailTripwireTriggered`, `ToolOutputGuardrailTripwireTriggered`; `guardrail_result` identifies trigger; accumulated results in `run_data`. — [Guardrails | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/)
- Hosted/built-in execution tools (WebSearch, FileSearch, HostedMCP, CodeInterpreter, ImageGeneration, Computer, Shell, ApplyPatch, LocalShell) and `Agent.as_tool()` do not use the function-tool guardrail pipeline. — [Guardrails | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/)
- Human-in-the-loop: `needs_approval=True` on function tools; run pauses, returns `interruptions` + resumable `state`; approve/reject then resume same run; applies even nested. — [Guardrails and human review | OpenAI API](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)
- Practical guardrail patterns: relevance classifier, safety classifier, PII filter, moderation, tool safeguards (risk ratings), rules-based protections, output validation. — [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Tool safeguards: assign risk rating low/medium/high by read-only vs write, reversibility, permissions, financial impact; pause for guardrail checks before high-risk. — [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Input guardrails can run in parallel with main model (faster) or block before (guaranteed no main-model start); output guardrails validate final output. — [Guardrails | OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/); [A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

### Inferences
- OpenAI's guardrail architecture is intentionally scoped: agent-level checks at boundaries, tool-level checks at side-effect points, with tripwires as fail-fast halts; hosted tools bypass client guardrails (must rely on approval policies).

### Gaps
- Whether OpenAI provides built-in moderation/PII classifiers as ready-made guardrails or expects developers to implement them was not confirmed from primary sources (guide describes patterns, not shipped implementations).
