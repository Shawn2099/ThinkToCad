# Toolkit design patterns (cross-cutting synthesis)

Synthesis of cross-cutting design patterns for building a well-structured agent toolkit, drawing from OpenAI, Anthropic, and Google provider APIs/SDKs, MCP, and software-engineering patterns. Companion notes: `openai_toolkit.md`, `anthropic_toolkit.md`, `google_toolkit.md`.

## Canonical tool schema contract across providers

### Takeaway
Every major provider and MCP converge on the same three-part contract per tool — a short `name`, a `description`, and a JSON Schema for parameters — wrapped in a provider-specific envelope; strict mode turns the schema into a generation constraint, not just validation.

### Cited Findings
- The durable unit is a provider-neutral definition: `name`, `description`, `inputSchema`, plus a side-effect class (`read`/`write`); a normalized `ToolCall` (provider, providerCallId, name, arguments) and a normalized `ToolResult` (providerCallId, ok, content, evidence). — [Qveris function-calling guide](https://qveris.ai/guides/function-calling/)
- Shared mental model across providers: name + description + JSON Schema parameters; the differences are only in the envelope (OpenAI `type:"function"` + `function.parameters`; Anthropic flat `{name, description, input_schema}`; Gemini `functionDeclarations` + `parameters`). — [Jsonic JSON Schema for function calling](https://jsonic.io/guides/json-schema-function-calling); [Craig Trim](https://craigtrim.com/articles/function-calling-across-providers/)
- OpenAI function definition fields: `type` ("function"), `name` (a-z, A-Z, 0-9, underscores/dashes, max 64 chars), `description`, `parameters` (JSON Schema), `strict`. — [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling)
- Anthropic client tool: `name` regex `^[a-zA-Z0-9_-]{1,128}$`, `description`, `input_schema` (JSON Schema), optional `input_examples`, `strict`, `defer_loading`, `cache_control`, `allowed_callers`, `eager_input_streaming`. — [Anthropic define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools); [tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
- Gemini/ADK: `FunctionTool` auto-generates schema from Python signature + docstring; parameters required if typed without default; `*args`/`**kwargs` ignored; preferred return is a dict with a "status" key. — [ADK function tools](https://google.github.io/adk-docs/tools-custom/function-tools/)
- MCP tool definition: `name`, optional `title`, `description`, `inputSchema`, optional `outputSchema`, optional `annotations`; results carry `content` array plus optional `structuredContent` and `isError`. — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- Strict mode: OpenAI requires `additionalProperties: false` on every object and every property in `required` (optionals as `type: ["string","null"]`); Anthropic strict uses grammar-constrained sampling with `additionalProperties: false` in practice; Gemini strict schema subset varies by API/model. — [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling); [Anthropic strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)
- Provider schema dialect differences: OpenAI strict rejects `allOf`/`not`/`if-then-else`; Gemini does not understand `$ref`, `oneOf`, `allOf`, `additionalProperties` and uses `nullable: true`; Anthropic/MCP are most permissive. Normalization libraries (tool-schema, toolerance) exist for cross-provider conversion. — [tool-schema](https://github.com/slegarraga/tool-schema); [toolerance](https://github.com/ishaand0314/toolerance)
- Correlation keys differ: OpenAI `call_id`, Anthropic `tool_use_id`, Gemini `call_id` (plus `previous_interaction_id` for chaining). — [Qveris function-calling guide](https://qveris.ai/guides/function-calling/)
- Schema is the contract the model reads: descriptions on root and per-property, `enum` constraints, `required`; OpenAI recommends "pass the intern test" and keeping initially available functions small (<20 soft). — [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling)

### Inferences
- A custom toolkit should define one canonical, provider-neutral tool contract (name, description, JSON Schema, side-effect class, result envelope) and adapt to provider envelopes at the boundary, rather than authoring per-provider schemas.
- Strict mode is the recommended default where supported: it moves validation from runtime to the sampler and prevents type mismatches (e.g., `"2"` vs `2`).

### Gaps
- The exact supported JSON Schema subset per provider under strict mode is documented but not reproduced here; consult each provider's "supported schemas" reference. Flagged as unverified for Gemini's strict subset.

## Registration and discovery

### Takeaway
Registration spans three mechanisms — in-code decorators, plugin entry points, and dynamic MCP `tools/list` discovery — with scoping (per-agent tool lists, `tool_filter`, namespaces) as the main defense against tool overload; deferred/lazy loading keeps context cost bounded.

### Cited Findings
- Registry pattern: a queryable catalogue of tools/agents with capability, cost, latency, quality metadata; the agent selects at task time; uniform entries allow implementations to change without touching the agent. — [CSIRO Tool/Agent Registry](https://research.csiro.au/ss/science/projects/agent-design-pattern-catalogue/tool-agent-registry/); [agentpatternscatalog](https://agentpatternscatalog.github.io/patterns/patterns/tool-agent-registry.html)
- Decorator pattern: `@function_tool`/`@tool` (OpenAI Agents SDK) auto-generates name/description/schema from function + docstring; supports sync/async, `RunContextWrapper` first arg, overrides (`name_override`, `description_override`, `defer_loading`, `needs_approval`, guardrails). — [OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/)
- ADK auto-wraps a function assigned to an agent's `tools` list as `FunctionTool`; explicit `FunctionTool(func=...)` also supported. — [ADK function tools](https://google.github.io/adk-docs/tools-custom/function-tools/)
- Plugin system: Python entry points + decorators for discovery; NeMo Agent Toolkit registers functions/agents/workflows/evaluators via `@nat.plugin_api.register_*`; plugins treated identically to first-party. — [NeMo plugin system](https://docs.nvidia.com/nemo/agent-toolkit/latest/extend/plugins.html)
- Soothe RFC plugin model: `Plugin` protocol, decorator API (`@plugin`, `@tool`, `@subagent`), manifest schema, lifecycle hooks (`on_load`/`on_unload`/`health_check`), trust levels, multiple discovery mechanisms (entry points, config, filesystem), graceful degradation. — [RFC-600](https://github.com/mirasoth/soothe/blob/36339822/docs/specs/RFC-600-plugin-extension-system.md)
- AgentsKit principles: "thin core, fat plugins"; every capability is a record (ToolDefinition); registry last-write-wins; side effects go through gates. — [AgentsKit ARCHITECTURE](https://github.com/AgentsKit-io/agentskit/blob/HEAD/packages/cli/ARCHITECTURE.md)
- Filesystem-as-registry (Claude Code skills): directory tree of manifests + scripts; no infrastructure beyond shared directory; suited to single-host. — [Zylos plugin architecture](https://zylos.ai/research/2026-02-21-ai-agent-plugin-extension-architecture/)
- MCP discovery: `tools/list` (paginated via cursor), `notifications/tools/list_changed`, capability declares `listChanged`; clients re-list; servers validate inputs/rate-limit/sanitize outputs. — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- Deferred/lazy loading: OpenAI tool search (`tool_search`, `defer_loading`, namespaces with <10 functions per namespace, hosted or client-executed search); Anthropic `defer_loading: true` (up to 10,000 deferred tools, regex/BM25 search variants, at least one non-deferred tool required); Claude Code/SDK defers schemas by default. — [OpenAI tool search](https://developers.openai.com/api/docs/guides/tools-tool-search); [Anthropic tool search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)
- Scoping: ADK `tool_filter` (list or predicate) restricts which discovered tools reach the LLM; per-agent `tools` lists; OpenAI MCP static/dynamic tool filters. — [ADK MCP tools](https://google.github.io/adk-docs/tools-custom/mcp-tools/); [OpenAI MCP](https://openai.github.io/openai-agents-python/mcp/)
- Static vs dynamic loading trade-off: static = simpler, faster, debuggable; dynamic = flexible, hot-reload, smaller idle footprint; hybrid recommended for long-running services. — [Zylos plugin architecture](https://zylos.ai/research/2026-02-21-ai-agent-plugin-extension-architecture/)

### Inferences
- For a toolkit with many tools, combine: a canonical in-code registry (dict of ToolDefinition), decorator-based registration for ergonomics, optional entry-point plugin discovery, and deferred loading for context efficiency.
- Per-agent scoping (`tool_filter`/namespaces) is the primary cognitive-load control, not just a performance optimization.

### Gaps
- Whether ADK supports dynamic tool registration mid-run was not documented; unverified. Runtime registration semantics (thread safety, invalidation) are not specified in fetched sources.

## Tool execution (sync/async, parallel/sequential, timeout, cancellation)

### Takeaway
Execution is async-first with a read-only-vs-stateful concurrency rule: run independent read-only calls in parallel (often capped), stateful calls sequentially, enforce per-tool timeouts, and propagate cancellation cooperatively; preserve request order in outputs and isolate sibling failures.

### Cited Findings
- Claude Agent SDK: read-only tools (Read/Glob/Grep/MCP read-only) run concurrently; state-modifying (Edit/Write/Bash) run sequentially; custom tools default sequential unless `readOnlyHint` set. — [Claude Agent SDK agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop)
- ADK v1.10.0+: attempts parallel execution of function tools; requires `async def`; sync tools block others; async patterns (`async with`, `asyncio.sleep(0)` yields, thread pools for CPU-bound). — [ADK performance](https://google.github.io/adk-docs/tools-custom/performance/)
- OpenAI SDK: provider controls how many calls appear per response; `RunConfig.tool_execution.max_function_tool_concurrency` controls local handlers; decorated sync functions run via `asyncio.to_thread()`; async handlers are the only ones supporting SDK timeouts. — [OpenAI tool execution lifecycle](https://github.com/openai/openai-agents-python/blob/main/.agents/references/tool-execution-lifecycle.md)
- Definable: parallel via `asyncio.gather` by default; `sequential=True` forces serial; batch with both runs parallel group first then sequential. — [Definable agentic loop](https://docs.definable.ai/agents/agentic-loop)
- Strands: per-tool event order preserved; concurrent mode interleaves across tools; cancellation identical in both modes. — [Strands tool executors](https://strandsagents.com/docs/user-guide/sdk/tools/executors/)
- Timeout enforcement: toolregistry uses `Future.result(timeout)` (thread backend) and `asyncio.wait_for` (async); per-tool via `ToolMetadata.timeout`. PraisonAI abandons timed-out worker on a daemon thread and returns typed `timeout` result. — [toolregistry concurrency](https://toolregistry.readthedocs.io/en/latest/usage/concurrency_modes/); [PraisonAI tool timeout](https://praison.ai/docs/features/tool-timeout)
- Cancellation: cooperative tokens checked at safe points (before model call, before tool execution); `AbortSignal` passed to tools (lousho, LiveKit); LiveKit async tools opt into `CANCELLABLE` flag exposing `get_running_tasks`/`cancel_task`. — [lousho runs](https://lousho.com/runs); [LiveKit async tools](https://docs.livekit.io/agents/logic/tools/async/)
- async-toolformer-orchestrator: per-tool rate limiting (token bucket), hard timeouts, branch cancellation for speculative execution. — [async-toolformer-orchestrator](https://github.com/danieleschmidt/async-toolformer-orchestrator)
- Ordering/failure isolation invariants: preserve model order in emitted outputs even when handlers complete out of order; isolate sibling results (a cancelled/failed call must not discard successful siblings' outputs); distinguish tool-local cancellation from parent-run cancellation; select/raise failures deterministically when several tasks fail. — [OpenAI tool execution lifecycle](https://github.com/openai/openai-agents-python/blob/main/.agents/references/tool-execution-lifecycle.md)
- lousho guarantees: transcript order is call order (results appended in requested order, not completion order); events start in call order; first approval-needed call stops the batch; propagating errors stop new calls, wait for running to settle, then reject; cancellation resolves (not rejects) with `finishReason: 'aborted'`. — [lousho runs](https://lousho.com/runs)
- Concurrency cap example: `toolConcurrency` positive integer or `'unbounded'` (default); `1` for strictly sequential. — [lousho runs](https://lousho.com/runs)

### Inferences
- Default to parallel execution for read-only tools and sequential for stateful ones, with a configurable global cap; never let a single hung tool block the turn (timeout + daemon/abandon).
- Cancellation should be cooperative and checked at safe points; parent cancellation must propagate promptly, while tool-local cancellation follows the configured failure policy.

### Gaps
- No universal default timeout values are specified by providers; teams must pick. SDK-specific retry/backoff defaults for HTTP failures were not documented in fetched sources.

## Tool error handling (structured errors, retry, fallback, circuit breaker)

### Takeaway
The invariant is "tools return structured errors, never raise into the loop": catch exceptions, return a model-visible error payload with cause + suggested next step + retryability; retry transient failures silently with backoff, surface to the model only when different input is needed; bound total attempts.

### Cited Findings
- OpenAI: `on_invoke_tool` may raise (fails run) or return a string error message (sent to LLM); default `failure_error_function` returns generic `"An error occurred while running the tool. Please try again."` hiding the exception; custom formatter can return app-approved details; `None` re-raises. — [OpenAI Agents SDK tool.py](https://raw.githubusercontent.com/openai/openai-agents-python/main/src/agents/tool.py); [tools docs](https://openai.github.io/openai-agents-python/tools/)
- OpenAI Agents API: function result uses `success: true` + `output` string, or `success: false` + `error` message; result size limit <4 MiB; retry same `turn_id`/`call_id` while pending. — [OpenAI Agents functions](https://developers.openai.com/api/docs/guides/agents-api/tools/functions)
- Anthropic: tool execution error returned in `content` with `is_error: true`; Claude incorporates and may suggest retry; invalid tool name/missing params → Claude retries 2–3 times with corrections; server tool errors handled transparently (web search codes: `too_many_requests`, `invalid_input`, `max_uses_exceeded`, `query_too_long`, `unavailable`). — [Anthropic handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)
- MCP: distinguishes protocol errors (JSON-RPC, e.g. -32602 unknown tool) from tool execution errors (`isError: true` in result); servers must validate inputs, rate limit, sanitize outputs. — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- Google/ADK: tools return dicts with a "status" key ("success"/"error"/"pending") and human-readable `error_message`; non-dict returns auto-wrapped into `{"result": ...}`; `on_tool_error_callback` returning a dict suppresses the exception and uses it as result; before-tool-callback returning a dict skips execution (cache/override). — [ADK function tools](https://google.github.io/adk-docs/tools-custom/function-tools/); [ADK callbacks](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- Error-message design guidance (third-party): specific cause + fix/next step + explicit retryability ("temporary"/"try again"/"do not retry"/"permanent"); short plain text; don't leak secrets; distinguish bad input vs transient vs permanent. Retry transient failures silently with backoff; surface to model only when different input needed; bound total iterations (8–10) and repeated failures per tool. — [Returning Tool Errors to an LLM](https://ai-tldr.dev/learn/llm-apis/function-calling/handling-tool-errors/)
- OpenAI guardrails tripwires: `ToolInputGuardrailTripwireTriggered`/`ToolOutputGuardrailTripwireTriggered` halt execution; risk ratings (low/medium/high) by read-only vs write, reversibility, permissions, financial impact; human-in-the-loop approvals for sensitive actions. — [OpenAI guardrails](https://openai.github.io/openai-agents-python/guardrails/); [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Circuit breaker transitions tracked as a metric (Photon: `photon.circuit_breaker.transitions` counter with from/to states). — [Photon observability](https://github.com/portel-dev/photon/blob/main/docs/guides/observability.md)
- Anthropic prompting guide: treat tool output as untrusted; keep tool results inside `tool_result` blocks (prompt-injection hardening). — [Anthropic handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)

### Inferences
- Adopt a single structured result envelope `{"ok": bool, "data": ..., "error": {code, message, retryable, suggested_fix}}` across all tools; never raise into the agent loop.
- Separate "invalid arguments" (model should correct and retry 2–3 times) from "transient failure" (silent backoff) from "permanent failure" (do not retry); encode retryability in the payload.
- Hide raw exceptions by default; expose only app-approved, non-secret details via a configurable formatter.

### Gaps
- No provider-primary source specifies exponential backoff defaults or max-retry numbers for tool calls; ADK/Gemini automatic retry policies were not found. Flagged as unverified. Circuit-breaker state-machine details beyond metric names were not captured.

## Tool result formatting (text, structured, binary, artifacts)

### Takeaway
Return only high-signal, token-efficient content: structured JSON with semantic identifiers, optional concise/detailed verbosity, binary via content blocks/arrays, empty results allowed, and truncation messages that steer toward efficient strategies; keep full artifacts on disk and return paths/ids.

### Cited Findings
- OpenAI: result should typically be a string (JSON, error codes, plain text); images/files can be passed as arrays; no-return functions should return success/failure string. — [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling)
- Anthropic: `tool_result.content` supports text, image, document, search_result blocks; empty result allowed (omit `content`); computer/browser use member results narrower (text+image, plus optional browser_state). — [Anthropic handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)
- MCP: results carry `content` array (text/image/audio/resource_link/embedded resource) plus optional `structuredContent` and `isError`; `outputSchema` enables structured results. — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- Anthropic context engineering: token-efficient returns, minimal viable tool set, avoid overlapping tools, prefer semantic identifiers (names, slugs) over UUIDs, support `response_format` enum (`concise`/`detailed`), pagination/range/filtering/truncation, default limits (Claude Code restricts tool responses to 25,000 tokens), truncation messages steer toward efficient strategies. — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents); [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Anthropic ACI: poka-yoke tools (e.g., require absolute file paths); invest more in tool optimization than overall prompt; keep formats close to internet text; avoid formatting overhead (accurate line counts, string escaping). — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- OpenAI guidance: combine sequential functions; offload known args; return only high-signal fields; categorize tools as Data/Action/Orchestration. — [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Tool result size limit <4 MiB (OpenAI Agents API). — [OpenAI Agents functions](https://developers.openai.com/api/docs/guides/agents-api/tools/functions)

### Inferences
- For CAD/code-generation toolkits, return only artifact paths/ids and validation status, not full generated code; include the traceback and a suggested fix in error results.
- Prefer structured JSON over prose for validation feedback; let the model parse, not read.

### Gaps
- No universal token budget or truncation threshold is mandated; Claude Code's 25,000-token default is a reference point, not a standard. Binary streaming/chunking specifics were not fully covered.

## Tool composition (pipelines, chains, tool-as-agent, agent-as-tool)

### Takeaway
Composition happens at three levels — tool-level (sequential/parallel/conditional pipelines), agent-level (agents exposed as tools or as sub-agents with isolated context), and model-level (programmatic tool calling where the model writes code that coordinates tools); choose by trading latency vs. context isolation vs. cross-boundary interoperability.

### Cited Findings
- OpenAI: agents as tools via `agent.as_tool(tool_name, tool_description)` (manager retains control of user-facing reply); tool categories Data/Action/Orchestration. Programmatic Tool Calling: model writes/runs JavaScript coordinating tools; supported tool types include function, custom, mcp, apply_patch, shell, code_interpreter. — [OpenAI Agents tools](https://openai.github.io/openai-agents-python/tools/); [OpenAI programmatic tool calling](https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling)
- ADK: `AgentTool` wraps an `LlmAgent` as a native tool for in-process hierarchical delegation, isolating intermediate reasoning/tool calls (zero context bloat in parent); supports model tiering. `SequentialAgent`, `ParallelAgent`, `LoopAgent` orchestrate multiple agents. — [ADK agent-managed MCP](https://google.github.io/adk-docs/tools-custom/mcp-tools/agent-managed/); [ADK agents nav](https://google.github.io/adk-docs/agents/)
- Delegation tiers: in-process `AgentTool` (zero context bloat, higher cost/latency), MCP sub-agent (isolated), networked A2A (cross-org/formal contract). Direct MCP has low latency but high context bloat. — [ADK A2A intro](https://google.github.io/adk-docs/a2a/intro/); [ADK MCP tools](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- A2A (Agent2Agent): open protocol for networked agent-to-agent communication; preserve reasoning traces, long-running tools, artifacts across A2A. — [ADK A2A intro](https://google.github.io/adk-docs/a2a/intro/)
- Tool namespaces: group related tools under a name+description (`tool_namespace`); recommended <10 functions per namespace; mix deferred/immediate. — [OpenAI tool search](https://developers.openai.com/api/docs/guides/tools-tool-search)
- OpenAI `tool_use_behavior` controls whether tool results loop back to model or end run; `reset_tool_choice` resets after a tool call (default True) to avoid loops. — [OpenAI Agents agents](https://openai.github.io/openai-agents-python/agents/)
- MCP primitives beyond tools: resources (application-driven, URI-addressed, subscribable) and prompts (user-controlled templates) compose with tools for context injection. — [MCP resources spec](https://modelcontextprotocol.io/specification/2025-06-18/server/resources); [MCP prompts spec](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts)

### Inferences
- Default to in-process agent-as-tool for specialist delegation; escalate to MCP sub-agent when isolation matters; use A2A only for cross-boundary/cross-org.
- Expose high-level orchestration tools (e.g., `create_part`) rather than many micro-tools, aligning with "minimal viable tool set."

### Gaps
- A2A protocol spec details (task lifecycle, streaming, auth) were not fetched; unverified. Programmatic tool calling support matrix beyond listed tool types not enumerated.

## Testing (unit, integration, eval harnesses)

### Takeaway
Use a layered testing pyramid: fast, free unit tests for tool logic and routing with mocks; integration tests for the agent loop with real tools and mock/stub LLM; eval harnesses with tasks, trials, graders, transcripts, and outcomes for end-to-end quality, gated in CI with regression thresholds.

### Cited Findings
- Testing pyramid for agents: Tool Unit Tests (50%), Agent Integration Tests (30%), E2E Scenario Tests (15%), Adversarial Tests (5%). — [Agentic AI testing pyramid](https://callsphere.ai/blog/agentic-ai-testing-pyramid-unit-integration-e2e.md)
- Anthropic evals framework: task, trial (multiple runs for consistency), grader (logic scoring aspects, multiple assertions), transcript/trace (full messages array), outcome (final environment state), eval harness (runs end-to-end, records steps, grades, aggregates), eval suite (collection of tasks). — [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- NeMo `ToolTestRunner`: test tools in complete isolation without spinning up workflows/agents/external services; validate error handling. — [NeMo add unit tests for tools](https://github.com/nvidia/nemo-agent-toolkit/blob/develop/docs/source/extend/testing/add-unit-tests-for-tools.md)
- 10xGraph: `TestAgent` (drop-in replacement returning predefined responses, records LLM calls, tracks tool names), `MockToolRegistry` (tracks invocations by name/args), `MockMCPClient`; eval layer with `EvalSet`, `EvalPresets`, criteria (tool accuracy, response quality, trajectory, safety, hallucination), `AgentEvaluator` (sequential/parallel), reports (HTML/JSON/JUnit). — [10xGraph testing](https://10xgraph.com/docs/testing)
- ToolSimulator (Strands Evals): LLM-powered tool simulation with adaptive response generation, stateful shared state across calls, Pydantic schema enforcement; avoids live API calls/PII. — [AWS ToolSimulator](https://aws.amazon.com/blogs/machine-learning/toolsimulator-scalable-tool-testing-for-ai-agents/)
- Microsoft Foundry: unit (agent logic, tool handlers, prompt formatting), local integration (full agent vs real models), deployed integration, structured eval (`azd ai agent eval` with dataset + adaptive evaluator, CI quality gate). — [Test hosted agent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/test-hosted-agent)
- Unit vs integration evals: unit-style evals take a transcript and assert next tool calls/args (cheap, verify prompt-following); integration evals run full agentic loop with tool calling and fakes (validate output shape, assumptions). — [Unit Testing's Eval Twin](https://volary.ai/articles/unit-testings-eval-twin)
- Purista harness: test without external providers by injecting fake providers/stores/fixtures; contract tests for state/sandbox/model providers; coverage gates. — [Purista testing guide](https://github.com/puristajs/harness/blob/main/docs/guides/testing.md)

### Inferences
- Test tool handlers as pure functions with fixed inputs/outputs first; then test routing with a mock LLM; then run eval suites with real models and regression thresholds (e.g., block merge if score regresses >2%).
- Use LLM-powered tool simulators for multi-turn stateful workflows instead of static mocks that break across turns.

### Gaps
- No single standardized eval metric set or grader rubric is mandated; grading remains task-specific. Adversarial/prompt-injection test suites were referenced but not detailed in fetched sources.

## Security patterns (sandboxing, permission scoping, allow/deny lists)

### Takeaway
Layer defenses: deny-wins allow/deny/ask policy rules scoped to tools and arguments, permission modes, hooks that can short-circuit, OS-level sandboxing with filesystem/network boundaries, path scoping, elevation escape hatches requiring approval, and human-in-the-loop for high-risk actions.

### Cited Findings
- Claude Code permission evaluation order: Hooks → Deny rules → Ask rules → Permission mode → Allow rules → `canUseTool` callback; deny rules match even in `bypassPermissions`; bare-name deny removes tool from context; scoped patterns like `Bash(rm *)`; tool-name globs in deny (`*`, `mcp__*`); critical-path `rm`/`rmdir` never auto-approved. — [Claude Code permissions](https://code.claude.com/docs/en/agent-sdk/permissions)
- OpenClaw: global `tools.allow`/`tools.deny` (deny wins, case-insensitive, `*` wildcards); `allow` and `alsoAllow` mutually exclusive in same scope; sandbox vs tool policy vs elevated are separate controls. — [OpenClaw tool policy](https://docs.openclaw.ai/gateway/config-tools/tool-policy); [sandbox vs tool policy](https://docs.openaeon.ai/gateway/sandbox-vs-tool-policy-vs-elevated)
- Antigravity: unified permission engine with Deny/Ask/Allow lists; precedence Deny > Ask > Allow; permission presets (Default/Request Review/Turbo); OS sandbox (namespaces on Linux, `sandbox-exec`/Seatbelt on macOS) with filesystem/network boundaries derived from permissions; `unsandboxed` escape hatches always require approval unless matched by allow rule. — [Antigravity permissions](https://antigravity.google/docs/permissions/); [Antigravity sandbox](https://antigravity.google/docs/cli/sandbox/)
- agents.cli: real-world allow/ask/deny tiers (reads/tests/formatters allowed; installs/pushes asked; `rm -rf`/secrets writes denied); per-agent profiles (plan read-only, build full access); org-wide policy via managed config. — [agents.cli permissions](https://www.agentscli.com/foundations/permissions/)
- Doable: defense-in-depth eight layers — policy allow-lists, permission handler gating every call with audit entry, process isolator (Nsjail/Systemd/JobObject/Direct), per-project Linux UID, bubblewrap runtime jail, seccomp + capability drop, egress firewall (nftables + Squid allowlist), OS containment; workspace rules can only tighten, never loosen. — [Doable sandboxing](https://docs.doable.me/security/sandboxing/)
- OpenAI: risk ratings (low/medium/high) by read-only vs write, reversibility, permissions, financial impact; guardrails (input/output/tool) with tripwires; human-in-the-loop approvals (`needs_approval=True`) that pause and resume; plan mode prevents auto-approval of writes. — [OpenAI guardrails](https://openai.github.io/openai-agents-python/guardrails/); [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- MCP security guidance: servers must validate inputs, implement access controls, rate limit, sanitize outputs; clients should prompt for confirmation on sensitive ops, validate results. — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- Plugin marketplace (Agent Governance Toolkit): Ed25519 signatures, declarative manifests, capability declarations, `PluginSandbox` restricted subprocess blocking dangerous modules at import time. — [plugin marketplace tutorial](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/tutorials/10-plugin-marketplace.md)

### Inferences
- Implement a deny-wins policy engine with scoped patterns (`Tool(action)`, `Tool(arg pattern)`), plus a separate OS sandbox for shell/exec tools; never rely on policy alone for untrusted code.
- Default new tools to "ask" for side effects; require explicit allow for automation; protect critical paths regardless of mode.

### Gaps
- Formal verification/guarantees of sandbox escape resistance were not assessed; container/VM overhead trade-offs not benchmarked. Windows sandbox specifics were noted as using a previous permission system in Antigravity (unverified beyond that).

## Observability (tracing, logging, metrics per tool)

### Takeaway
Instrument every tool call as a first-class span with GenAI semantic-convention attributes, emit per-tool duration/error/token metrics, correlate logs via trace IDs, and propagate context across sub-agents/MCP; keep arguments/results out of spans by default for PII safety.

### Cited Findings
- Claude Code/SDK: three OTel signals (metrics, logs, traces); span names `claude_code.interaction`, `claude_code.llm_request`, `claude_code.tool` (with child spans `claude_code.tool.blocked_on_user`, `claude_code.tool.execution`), `claude_code.hook`; subagent spans nest under parent tool span; `session.id` attribute. Tracing beta requires `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`. — [Claude Code observability](https://code.claude.com/docs/en/agent-sdk/observability)
- GenAI semantic conventions: `gen_ai.operation.name`, `gen_ai.tool.name`, `gen_ai.tool.call.id`, `gen_ai.agent.name`, `gen_ai.conversation.id`; bind every span with conversation/agent/operation attributes; distinct names per agent/sub-agent. — [base14 Scout agent observability](https://docs.base14.io/guides/ai-observability/agent-observability/)
- ADK metrics: `gen_ai.execute_tool.duration` histogram (agent, tool name, tool type, error type), `gen_ai.invoke_agent.tool_calls` histogram, token usage histograms. ADK-TS adds counters `adk.tool.executions` and histograms `adk.tool.duration`. — [ADK metrics](https://adk.dev/observability/metrics/); [ADK-TS metrics](https://adk.iqai.com/docs/framework/observability/metrics)
- Photon: span `gen_ai.tool.call {photon}.{tool}` with attributes; metrics `photon.tool.duration` (histogram), `photon.tool.calls`/`photon.tool.errors` (counters), `photon.circuit_breaker.transitions`, `photon.rate_limit.rejections`, `photon.bulkhead.rejections`; logs auto-attach context; W3C traceparent propagation with validation; baggage is context only (never expanded into metric labels). — [Photon observability](https://github.com/portel-dev/photon/blob/main/docs/guides/observability.md)
- Atlas: every server-executed tool emits `atlas.tool.<name>` span with call_id, error, streaming, aborted; tool args/results not recorded; MCP dispatch spans include transport/deploy mode; metrics `atlas.mcp.tool.calls`/`atlas.mcp.tool.latency` with outcome dimension. — [Atlas observability](https://docs.useatlas.dev/platform-ops/observability/)
- mcp-audit: records every tool invocation with timing, cost, tokens, result; aggregates (error rate, p50/p95/p99 latency, total cost, top tools); alert rules; Prometheus exposition (`mcp_audit_tool_calls_total`, `mcp_audit_tool_duration_ms`, etc.); OTLP export. — [mcp-audit](https://github.com/nyx-builds/mcp-audit)
- AgentOS: spans `agentos.tool_result`, `agentos.gmi.handle_tool_result`; metrics `agentos.tool_results` counter, `agentos.tool_result.duration_ms` histogram; trace IDs attached to streamed chunks. — [AgentOS observability](https://docs.agentos.sh/architecture/observability)
- OpenTelemetry GenAI conventions are the emerging standard; error spans auto-set sampling priority; nested tool spans keep multi-hop workflows connected. — [base14 Scout](https://docs.base14.io/guides/ai-observability/agent-observability/)

### Inferences
- Standardize on GenAI semantic-convention attribute names so traces are portable across backends; add a toolkit-specific prefix only for non-standard metrics (e.g., `base14.` pattern).
- Never record raw tool arguments/results in spans by default (PII/secrets); opt in explicitly with redaction.

### Gaps
- Tool-level cost attribution (per-tool USD) is not standardized; mcp-audit implements it but no convention exists. Trace sampling strategies for high-volume tool calls were not covered.

## "Tool as a contract" philosophy

### Takeaway
A tool is a contract: its name + schema + description are the entire interface the model sees, so they must be self-sufficient, standardized, reusable, and minimal; optimize tool definitions and descriptions at least as much as prompts, and validate them through evals.

### Cited Findings
- OpenAI: "Each tool should have a standardized definition, enabling flexible, many-to-many relationships between tools and agents. Well-documented, thoroughly tested, and reusable tools improve discoverability, simplify version management, and prevent redundant definitions." — [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- OpenAI "pass the intern test": clear/detailed names/params/instructions; use enums/object structure to prevent invalid states; offload known args; combine sequential functions; keep initially available functions small (<20 soft); principle of least surprise. — [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling)
- OpenAI tool categories: Data (retrieve context), Action (interact with systems), Orchestration (agents as tools). Tool overload: issue is similarity/overlap, not count; split agents when clarity improvements don't help. — [OpenAI practical guide](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- Anthropic ACI: invest as much effort in ACI as HCI; poka-yoke tools (absolute paths); SWE-bench example where relative paths caused errors; test in workbench with many examples; iterate on mistakes. — [Anthropic building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- Anthropic tool design: choose fewer high-impact tools over API wrappers; namespace by service/resource; return meaningful, token-efficient context; support concise/detailed response formats; prompt-engineer descriptions (3–4+ sentences); evaluation-driven iteration with held-out test sets. — [Anthropic writing effective tools](https://www.anthropic.com/engineering/writing-tools-for-agents)
- Google/ADK best practices: fewer parameters, simple data types (str/int), meaningful names, build for parallel execution, descriptive docstrings; ADK prefers "status" key in result dict. — [ADK function tools](https://google.github.io/adk-docs/tools-custom/function-tools/)
- Context engineering: minimal viable tool set; avoid overlapping tools; tools must be token-efficient and self-contained; context window is a finite attention budget (context rot). — [Anthropic effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Description-quality guidance: 50–200 characters per parameter is the sweet spot; descriptions are the single biggest accuracy lever. — [Jsonic JSON Schema for function calling](https://jsonic.io/guides/json-schema-function-calling)

### Inferences
- Treat tool definitions as published APIs: version them, test them, and make them self-sufficient (the model has no other documentation).
- Consolidate micro-operations into fewer high-impact tools with an `action` parameter; namespace by service/resource; keep the exposed set small and non-overlapping.

### Gaps
- No single source uses the exact phrase "tool as a contract"; the philosophy is inferred from standardized-definition, intern-test, and ACI guidance. No published rubric for evaluating tool descriptions; relies on empirical evals.
<|im_end|><|end|><|start|> assistant<|channel|>final<|message|>The file has been written to `C:\Users\malliath\Desktop\CADResearch\research_notes\Building AI agent toolkits\toolkit_design_patterns.md`.

I synthesized cross-cutting patterns across the canonical schema contract, registration/discovery, execution, error handling, result formatting, composition, testing, security, observability, and the "tool as a contract" philosophy, with inline URL citations and explicit gaps/unverified items. Sources included the three provider notes already in the folder plus web research on registries/plugins, schema normalization, execution/cancellation, testing pyramids, sandboxing/permissions, and OpenTelemetry observability. Done.<|end|><|start|>tool_calls_section_begin|><|tool_call_begin|>![xml<|message|><rfl:parameter name="path">
C:\Users\malliath\Desktop\CADResearch\research_notes\Building AI agent toolkits\toolkit_design_patterns.md