# AI Agent Toolkit Guide

A comprehensive guide for building an AI agent toolkit, synthesized from OpenAI, Anthropic, Google, and open-source frameworks (LangChain, LlamaIndex, CrewAI, AutoGen, Pydantic AI, smolagents), plus cross-cutting design patterns. Written for toolkit authors who ship tools to an LLM and want predictable, debuggable, safe behavior.

Source research notes: `research_notes/Building AI agent toolkits/{openai,anthropic,google,opensource}_toolkits.md` and `toolkit_design_patterns.md`.

---

## 1. Purpose and how to use this guide

### What this guide is

A design reference, not an implementation. It captures convergent patterns across providers so you can build a toolkit once and port it across models. Where providers disagree, it states the convergence and flags the divergence.

### How to read it

- Sections 2-11 are provider-neutral patterns. Read these first; they define the contract.
- Section 12 is lab-specific deep dives; read when targeting one provider.
- Section 13 maps patterns onto the ThinkToCad CAD toolkit (this repo).
- Section 14 is a quick reference index ("I want to do X").
- Section 15 lists sources.

### Core thesis

A tool is a contract. Its name, description, and JSON Schema are the entire interface the model sees; there is no other documentation. Therefore:

1. The schema is both validation and generation constraint (strict mode).
2. The description is the primary accuracy lever.
3. Tools return structured errors and never raise into the loop.
4. The kernel (executor) is the referee, not the LLM.

### Invariants (ThinkToCad "kernel is the referee")

- The LLM never declares pass/fail. Tools execute; the kernel verifies.
- Every tool returns a structured dict `{"ok", "data"/..., "error"}`. Validation feedback is JSON, not prose.
- Units are mm internally; params are snake_case with a unit suffix (`length_mm`, `mass_kg`).
- One source of truth per dimension: contract -> spec -> code. Never hard-code a dimension in CAD code.
- Tools never raise into the loop. Catch everything; return an error payload.

### Pattern summary table

| # | Pattern | When to use | Key rule |
|---|---------|-------------|----------|
| 1 | Strict schema | Always (where supported) | `additionalProperties: false`, all fields required, optionals as `type: ["x","null"]` |
| 2 | Structured error envelope | Always | `{"ok": bool, "data": ..., "error": {code, message, retryable, suggested_fix}}` |
| 3 | Never raise into loop | Always | Catch exceptions; return error payload |
| 4 | Retryability in payload | Always | Invalid-args (model retries 2-3x) vs transient (silent backoff) vs permanent (do not retry) |
| 5 | Hide raw exceptions | Default | Expose only app-approved details via formatter |
| 6 | Tool as contract | Always | Name + schema + description self-sufficient ("intern test") |
| 7 | Minimal viable tool set | Always | Consolidate micro-ops into fewer high-impact tools with an `action` param |
| 8 | Namespacing | >1 service | Prefix by service/resource (`thinktocad_create_part`) |
| 9 | Read-only vs stateful concurrency | Execution | Parallel reads, sequential writes |
| 10 | Per-tool timeout | Execution | Never let one hung tool block the turn |
| 11 | Cooperative cancellation | Execution | Check at safe points; propagate parent cancel |
| 12 | Preserve call order in outputs | Execution | Results appended in requested order, not completion order |
| 13 | Sibling failure isolation | Execution | A failed call must not discard successful siblings |
| 14 | Token-efficient results | Result formatting | Return paths/ids + status, not full payloads |
| 15 | Concise/detailed verbosity | Result formatting | `response_format` enum |
| 16 | Truncation with steering | Result formatting | Truncation message points to efficient strategy |
| 17 | Tool search / deferred loading | >20 tools | Defer schemas; load on demand |
| 18 | Per-agent scoping | >20 tools | `tool_filter` / namespaces |
| 19 | Agent-as-tool | Specialist delegation | In-process by default; escalate to MCP/A2A |
| 20 | Programmatic tool calling | Multi-step coordination | Model writes code orchestrating tools |
| 21 | Deny-wins policy | Security | Deny > Ask > Allow; critical paths never auto-approved |
| 22 | OS sandbox for exec | Security | Policy alone is insufficient for untrusted code |
| 23 | GenAI semantic conventions | Observability | `gen_ai.tool.name`, `gen_ai.tool.call.id`, ... |
| 24 | No raw args in spans | Observability | PII/secrets safety; opt in with redaction |
| 25 | Layered testing pyramid | Testing | Unit (50%) / integration (30%) / e2e (15%) / adversarial (5%) |
| 26 | Eval harness with trials | Testing | task + trial + grader + transcript + outcome + suite |
| 27 | Tool simulator | Testing | LLM-powered, stateful, schema-enforced |
| 28 | Trust tiers on write-back | Knowledge | Never overwrite higher-trust with lower-trust |

---

## 2. AI pointer rules (how to design tools)

Drawn from OpenAI's "pass the intern test", Anthropic's ACI, and Google's ADK best practices.

### Rule 1: The intern test

Write the description and schema so an intern with no other context could call the tool correctly. The model has no access to your source code, README, or docstrings beyond the tool definition.

### Rule 2: Self-sufficient definitions

- Name: clear, specific, verb-first or noun-qualified (`create_part`, `validate_code`).
- Description: 3-4+ sentences covering purpose, when to use, when NOT to use, side effects.
- Every parameter: description, type, constraints, example if non-obvious.
- Enums over free text wherever the valid set is closed.
- Object structure over boolean flags (avoid `toggle_light(on, off)`; use `set_light(state)`).

### Rule 3: Minimal viable tool set

- Prefer fewer, higher-impact tools over API wrappers.
- Consolidate operations with an `action` parameter (`manage_event(action="create"|"update"|"delete")`).
- Avoid overlapping tools; overlap causes wrong selection.
- Keep initially exposed tools small (<20 soft; hard problems start around 10 overlapping).

### Rule 4: Token efficiency

- Return only high-signal fields (paths, ids, status, counts), not full payloads.
- Prefer semantic identifiers (names, slugs) over UUIDs where the model must reason.
- Support `response_format: "concise" | "detailed"`.
- Paginate, filter, range-select; default limits; truncation messages steer toward efficient strategies.
- Claude Code caps tool responses at ~25,000 tokens; treat as a reference ceiling.

### Rule 5: Poka-yoke (mistake-proofing)

- Require absolute paths, not relative (SWE-bench: relative paths broke after the agent moved out of root).
- Require units in param names (`length_mm`, not `length`).
- Validate arguments against format before sending (strict mode catches `"2"` vs `2`).
- Use enums to prevent invalid states.
- Return structured validation errors, not prose, so the model self-corrects.

### Rule 6: Naming and namespacing

- Regex: `^[a-zA-Z0-9_-]{1,64}$` (OpenAI max 64; Anthropic allows 128; stay within 64 for portability).
- Namespace by service/resource: `asana_search`, `thinktocad_create_part`.
- Pick prefix vs suffix convention and stick to it (prefix is more common).
- MCP tool names are server-prefixed automatically in some SDKs (`mcp__server__tool`).

### Rule 7: Side-effect classification

Every tool declares a side-effect class: `read` (no state change; parallel-safe, cacheable, retryable), `write` (mutates state; sequential, consider idempotency, may need approval), `exec` (runs code/shell; sandboxed, approval-gated), `orchestrate` (delegates to another agent; context-isolation rules). This drives concurrency, caching, approval, sandboxing.

### Rule 8: Description quality is the biggest lever

- 50-200 characters per parameter is the sweet spot.
- Treat descriptions like docstrings for a junior dev: examples, edge cases, boundaries.
- Precise refinements to SWE-bench tool descriptions dramatically reduced errors.
- Iterate via evals with held-out test sets to avoid overfitting.

### Rule 9: One source of truth per dimension

Contract -> spec -> code. Never hard-code a dimension in CAD code. If a number appears in two places, one is wrong.

### Rule 10: Tools are published APIs

Version them, test them, make them self-sufficient. Changing a tool's schema is a breaking change for the model's learned behavior.

---

## 3. Canonical tool schema contract (cross-provider)

### The durable unit

Every provider and MCP converge on the same three-part contract per tool:

```
ToolDefinition { name, description, inputSchema (JSON Schema), sideEffect (read|write|exec|orchestrate),
                 outputSchema?, annotations? }
```

Wrapped in a provider-specific envelope at the boundary.

### Provider envelopes

OpenAI:

```json
{ "type": "function", "name": "create_part", "description": "...",
  "parameters": { "type": "object", "properties": {...}, "required": [...], "additionalProperties": false },
  "strict": true }
```

Anthropic:

```json
{ "name": "create_part", "description": "...", "input_schema": { "type": "object", "properties": {...}, "required": [...] },
  "strict": true, "defer_loading": false, "input_examples": [...] }
```

Gemini/ADK: `{ "name", "description", "parameters": { "type": "OBJECT", "properties", "required" } }`.

MCP: `{ "name", "title", "description", "inputSchema", "outputSchema", "annotations": { "readOnlyHint", "destructiveHint" } }`.

### Canonical internal contract (provider-neutral)

Define ONE contract in your codebase and adapt at the boundary:

```python
@dataclass
class ToolDefinition:
    name: str; description: str; input_schema: dict; side_effect: str
    output_schema: dict | None = None
    handler: Callable          # async (ctx, args) -> ToolResult
    timeout_s: float = 30.0; retryable: bool = True; max_retries: int = 2
```

Normalized call/result: `ToolCall = {provider, provider_call_id, name, arguments}`; `ToolResult = {provider_call_id, ok, content, evidence, metadata}`. Correlation keys differ by provider: OpenAI `call_id`, Anthropic `tool_use_id`, Gemini `call_id` (plus `previous_interaction_id`). Normalize to `provider_call_id`.

### Strict mode

Strict mode turns the schema into a generation constraint. Requirements (OpenAI; Anthropic similar):

1. `additionalProperties: false` on every object.
2. Every property in `properties` listed in `required`.
3. Optionals expressed as `type: ["string", "null"]` (nullable union), not omitted from required.

Provider schema dialect differences (normalize at boundary): OpenAI strict rejects `allOf`/`not`/`if-then-else`. Gemini does not understand `$ref`/`oneOf`/`allOf`/`additionalProperties`; uses `nullable: true`. Anthropic and MCP are the most permissive. Write canonical schema to the most permissive dialect (JSON Schema draft 2020-12) and convert at the adapter.

Anthropic optional properties: `cache_control`, `strict`, `defer_loading`, `allowed_callers`, `input_examples`, `eager_input_streaming`. `allowed_callers`: `"direct"` (default) and/or `"code_execution_20260120"` for programmatic tool calling. `input_examples` schema-validated, add ~20-50 tokens (simple) / ~100-200 tokens (complex); not supported on server tools/toolsets.

### Anti-patterns

- Authoring per-provider schemas by hand (drift, bugs).
- Omitting `additionalProperties: false` (model invents extra fields).
- Using `oneOf`/`allOf`/`$ref` in strict mode (rejected or ignored).
- Putting prose constraints in the description instead of schema (`enum`, `minimum`, `pattern`).

---

## 4. Tool registration and discovery patterns

### Three mechanisms

1. In-code decorators (`@tool`, `@function_tool`) - ergonomic, static.
2. Plugin entry points (Python entry points, manifests) - extensible, hot-loadable.
3. Dynamic MCP `tools/list` - interoperable, runtime discovery.

Combine: canonical in-code registry (dict of ToolDefinition) + decorator registration + optional entry-point plugin discovery + deferred loading.

### Registry pattern

A queryable catalogue of tools with capability, cost, latency, quality metadata. The agent selects at task time. Uniform entries allow implementations to change without touching the agent. Last-write-wins for duplicate names (AgentsKit). "Thin core, fat plugins": every capability is a record (ToolDefinition); side effects go through gates.

### Decorator pattern (OpenAI Agents SDK)

```python
@function_tool
def create_part(code: str, timeout: int = 120) -> dict: ...
```

Auto-generates name from function name, description from docstring, schema from type hints via inspect + griffe + pydantic. Supports sync/async, optional `RunContextWrapper` first arg. Overrides: `name_override`, `description_override`, `defer_loading`, `needs_approval`, `tool_input_guardrails`, `tool_output_guardrails`, `failure_error_function`.

### ADK auto-wrap

Assigning a function to an agent's `tools` list auto-wraps it as `FunctionTool`. Explicit `FunctionTool(func=...)` also supported. Parameters required if typed without default; optional if default given. `*args`/`**kwargs` ignored. Docstrings become the description. Preferred return is a dict with a "status" key.

### Plugin system (NeMo / Soothe RFC-600)

`Plugin` protocol, decorator API (`@plugin`, `@tool`, `@subagent`), manifest schema, lifecycle hooks (`on_load`/`on_unload`/`health_check`), trust levels, multiple discovery mechanisms (entry points, config, filesystem), graceful degradation. Filesystem-as-registry (Claude Code skills): directory tree of manifests + scripts; suited to single-host.

### MCP discovery

Client sends `tools/list` (paginated via cursor); server notifies `notifications/tools/list_changed` when capabilities change; capability declares `listChanged`. `list_tools()` per run; cache with `cacheToolsList: true`; invalidate via `invalidateToolsCache()`. Filtering: static (`create_static_tool_filter`) / dynamic callable; ADK `tool_filter` (list or predicate).

### Deferred / lazy loading

- OpenAI tool search: add `tool_search` tool; mark functions/MCP with `defer_loading: true`; namespaces group related tools (<10 functions per namespace); hosted or client-executed search; only `gpt-5.4+`. Discovered tools injected at end of context to preserve cache.
- Anthropic: `defer_loading: true` on tool definition; up to 10,000 deferred tools; regex/BM25 search variants; at least one non-deferred tool required; deferred tools stripped from cached prefix; cache breakpoints on tool definitions.
- Claude Code/SDK: defers schemas by default; `alwaysLoad: true` to force.

### Scoping as cognitive control

Per-agent `tools` lists, `tool_filter`, namespaces. Primary defense against tool overload. ADK: no global registry; scoping per agent.

### Static vs dynamic trade-off

Static: simpler, faster, debuggable. Dynamic: flexible, hot-reload, smaller idle footprint. Hybrid recommended for long-running services.

### Registration best practices

- Decorator for ergonomics; registry dict as source of truth.
- Validate on registration: name uniqueness, schema validity, handler signature.
- Version tool definitions; breaking schema change = major version.
- Trust levels for plugins; graceful degradation if a plugin fails to load.

---

## 5. Tool execution patterns (sync/async, parallel/sequential, timeout)

### Concurrency rule

Run independent read-only calls in parallel (often capped); stateful calls sequentially. Convergent across Claude SDK, ADK, OpenAI, Strands.

- Claude Agent SDK: read-only tools run concurrently; state-modifying run sequentially; custom tools default sequential unless `readOnlyHint`.
- ADK v1.10.0+: parallel execution requires `async def`; sync tools block others.
- OpenAI SDK: `RunConfig.tool_execution.max_function_tool_concurrency` controls local handlers; sync functions run via `asyncio.to_thread()`; async handlers are the only ones supporting SDK timeouts.

### Execution invariants (OpenAI tool execution lifecycle)

- Preserve model order in emitted outputs even when handlers complete out of order.
- Isolate sibling results: a cancelled/failed call must not discard successful siblings' outputs.
- Distinguish tool-local cancellation from parent-run cancellation.
- Select/raise failures deterministically when several tasks fail.
- Transcript order is call order (results appended in requested order, not completion order).
- Events start in call order; first approval-needed call stops the batch.
- Propagating errors stop new calls, wait for running to settle, then reject.
- Cancellation resolves (not rejects) with `finishReason: 'aborted'`.

### Timeout enforcement

Per-tool via `ToolMetadata.timeout`. Thread backend: `Future.result(timeout)`; async: `asyncio.wait_for`. On timeout: abandon (daemon thread) and return typed `timeout` result. Never let one hung tool block the turn. No universal default; pick per tool (CAD: 60-120s for build, 30s for validate).

### Cancellation

Cooperative tokens checked at safe points (before model call, before tool execution). `AbortSignal` passed to tools. Parent cancellation propagates promptly; tool-local cancellation follows configured failure policy.

### Parallelism knobs

`toolConcurrency`: positive integer or `'unbounded'` (default); `1` for strictly sequential. `sequential=True` forces serial; batch with both runs parallel group first then sequential (Definable). Concurrency cap: `max_function_tool_concurrency`.

### Async patterns (ADK)

`async with` for HTTP/DB; `await asyncio.sleep(0)` yield points in long loops; thread pools for CPU-bound work; chunking + yielding.

### Strands tool executors

Per-tool event order preserved; concurrent mode interleaves across tools; cancellation identical in both modes.

### Programmatic tool calling (OpenAI)

Model writes/runs JavaScript coordinating tools; supported tool types: function, custom, mcp, apply_patch, local/hosted shell, code_interpreter. Available on gpt-5.4+. Use when the model needs to orchestrate many calls with logic.

### Practical defaults

Default parallel for read-only; sequential for writes/exec. Global cap configurable (default unbounded for reads, 1 for writes). Per-tool timeout mandatory. Cooperative cancellation mandatory. Preserve call order. Isolate sibling failures.

---

## 6. Error handling patterns (structured errors, retry, fallback, circuit breaker)

### The invariant

Tools return structured errors and never raise into the loop. Catch exceptions; return an error payload. #1 invariant across ThinkToCad, OpenAI, Anthropic, Google, and MCP.

### Structured error envelope

```json
{ "ok": false, "data": null,
  "error": { "code": "INVALID_DIMENSION", "message": "length_mm must be > 0, got -5",
             "retryable": false, "suggested_fix": "Pass a positive length_mm.",
             "details": { "param": "length_mm", "value": -5 } } }
```

Success: `{ "ok": true, "data": { "artifacts": [...], "workdir": "..." }, "error": null }`.

### Error categories (encode retryability)

1. Invalid arguments (bad input): model corrects and retries 2-3 times. `retryable: true` but only with corrected input. Eliminate with strict mode where possible.
2. Transient failure (timeout, 429, 5xx, network): silent backoff with retries; surface to model only when different input needed.
3. Permanent failure (not found, permission denied, invalid state): `retryable: false`, "do not retry".

### Provider patterns

OpenAI: `on_invoke_tool` may raise (fails run) or return a string error message (sent to LLM). Default `failure_error_function` returns generic `"An error occurred while running the tool. Please try again."` hiding the exception. Custom formatter can return app-approved details; `None` re-raises. Agents API: `success` flag + output/error; result size <4 MiB; retry same `turn_id`/`call_id` while pending. `tool_error_formatter` in `RunConfig` overrides. Recommend: specific cause + fix/next step + explicit retryability ("temporary"/"try again"/"do not retry"/"permanent"); short plain text; don't leak secrets.

Anthropic: tool execution error returned in `content` with `is_error: true`; Claude incorporates and may suggest retry; write instructive messages. Invalid tool name/missing params: continue with `tool_result` indicating error; Claude retries 2-3 times with corrections before apologizing; eliminate with strict tool use. Server tool errors handled transparently; web search error codes: `too_many_requests`, `invalid_input`, `max_uses_exceeded`, `query_too_long`, `unavailable`. Empty result allowed (omit `content`).

MCP: distinguish protocol errors (JSON-RPC, e.g. -32602 unknown tool) from tool execution errors (`isError: true` in result). Servers must validate inputs, rate limit, sanitize outputs.

Google/ADK: tools return dicts with "status" key ("success"/"error"/"pending") and human-readable `error_message`. Non-dict returns auto-wrapped into `{"result": ...}`. `on_tool_error_callback` returning a dict suppresses the exception and uses it as result. Before-tool-callback returning a dict skips execution (cache/override); `None` lets it run. Empty dict `{}` counts as override, not "let run".

### Retry policy

Retry transient failures silently with exponential backoff + jitter. Surface to model only when different input needed. Bound total iterations (8-10) and repeated failures per tool; repeated failures become permanent-style "do not retry". No provider specifies default backoff numbers; implement your own. ADK/Gemini automatic retry policies not found in docs (unverified).

### Fallback

If a tool fails permanently, the model should try an alternative tool or ask the user. Encode alternatives in the error's `suggested_fix`. Tool-level fallback belongs in the orchestrator, not the tool.

### Circuit breaker

States: closed (normal) -> open (failing, reject fast) -> half-open (probe) -> closed. Track transitions as a metric (`photon.circuit_breaker.transitions` counter with from/to states). Per-tool or per-dependency; reset after cooldown. State-machine details beyond metric names not captured in research.

### Guardrails (OpenAI)

Risk ratings: low/medium/high by read-only vs write, reversibility, permissions, financial impact. Tool guardrails: input can skip call, replace output with message, or raise tripwire; output can replace output or raise tripwire. Tripwires: `ToolInputGuardrailTripwireTriggered`, `ToolOutputGuardrailTripwireTriggered` halt execution. Human-in-the-loop: `needs_approval=True` pauses the run, returns `interruptions` + resumable state; approve/reject then resume. Applies even nested. Hosted/built-in execution tools and `Agent.as_tool()` do NOT use the function-tool guardrail pipeline (rely on approval policies). Input guardrails can run in parallel with main model or block before.

### Prompt-injection hardening (Anthropic)

Tool output is untrusted. Keep tool results inside `tool_result` blocks, not system prompts. Never interpolate tool output into the system prompt. Sanitize outputs server-side (MCP guidance).

### Security: never leak secrets

Default error formatter hides raw exceptions (OpenAI default stance). Expose only app-approved, non-secret details via configurable formatter. Distinguish bad input vs transient vs permanent without revealing internals.

---

## 7. Tool result formatting (text, structured, binary, artifacts)

### Core rule

Return only high-signal, token-efficient content. Keep full artifacts on disk; return paths/ids + status.

### Content types by provider

OpenAI: typically a string (JSON, error codes, plain text); images/files can be passed as arrays; no-return functions should return a success/failure string.

Anthropic: `tool_result.content` supports text, image, document, search_result blocks. Empty result allowed (omit `content`). Computer/browser use member results narrower (text+image, plus optional browser_state for browser).

MCP: results carry `content` array (text/image/audio/resource_link/embedded resource) plus optional `structuredContent` and `isError`. `outputSchema` enables structured results.

### Formatting best practices (Anthropic)

Token-efficient returns; minimal viable tool set; avoid overlapping tools. Prefer semantic identifiers (names, slugs) over UUIDs. Support `response_format` enum (`concise`/`detailed`). Pagination, range selection, filtering, truncation. Default limits (Claude Code restricts tool responses to 25,000 tokens). Truncation messages should steer toward efficient strategies.

### Structure choices

JSON vs XML vs Markdown affects performance; keep formats close to what the model has seen in internet text. Avoid formatting overhead (accurate line counts, string escaping). For CAD: return artifact paths, validation status, counts, bounding boxes - not full geometry dumps.

### Binary and artifacts

Write artifacts to disk (e.g., `output/run_*/out.step`). Return paths/ids in the result; let the model reference them. OpenAI Agents API result size limit <4 MiB; keep payloads under that. For images: pass as content blocks/arrays, not base64 in text.

### Verbosity pattern

```python
def get_part_info(part_id, response_format="concise"):
    if response_format == "concise":
        return {"id": part_id, "status": "ok", "bbox_mm": [...]}
    return {"id": part_id, "status": "ok", "bbox_mm": [...], "mass_kg": ..., "volume_mm3": ..., "mesh_stats": {...}}
```

### Empty results

Allowed; omit `content` (Anthropic) or return `{"ok": true, "data": null}`. Don't fabricate "no results found" prose; let the model handle absence.

### Truncation contract

When truncating, include a message pointing to the efficient strategy:

```json
{ "ok": true, "data": { "items": [...], "truncated": true, "total": 500, "hint": "use filter='name' or range to narrow" } }
```

---

## 8. Tool composition patterns (pipelines, chains, tool-as-agent, agent-as-tool)

### Three levels

1. Tool-level: sequential/parallel/conditional pipelines of tool calls.
2. Agent-level: agents exposed as tools or as sub-agents with isolated context.
3. Model-level: programmatic tool calling (model writes code coordinating tools).

### Tool-level composition

Sequential pipelines: output of tool A feeds tool B. Implement in orchestrator or as a composite tool. Parallel fan-out: independent calls in one turn. Conditional: tool B only if tool A succeeds. OpenAI `tool_use_behavior` controls whether tool results loop back to model or end run; `reset_tool_choice` resets after a tool call (default True) to avoid loops.

### Namespaces (OpenAI)

Group related tools under a name+description (`tool_namespace(name, description, tools)`). Recommended <10 functions per namespace. Mix deferred/immediate. Use namespaces/MCP over individually deferred functions.

### Agent-as-tool

Expose an entire agent as a callable tool; manager retains control of user-facing reply.

- OpenAI: `agent.as_tool(tool_name=..., tool_description=...)`.
- ADK: `AgentTool` wraps an `LlmAgent` as a native tool for in-process hierarchical delegation; isolates intermediate reasoning/tool calls (zero context bloat in parent); supports model tiering.
- Categories: Data (retrieve context), Action (interact with systems), Orchestration (agents as tools).

### Delegation tiers (ADK)

| Tier | Latency | Context bloat | Isolation | Use when |
|------|---------|---------------|-----------|----------|
| In-process AgentTool | higher | zero | medium | specialist delegation, model tiering |
| MCP sub-agent | medium | isolated | high | isolation matters, separate lifecycle |
| Networked A2A | highest | isolated | highest | cross-org, formal contract, cross-language |
| Direct MCP | lowest | high | low | simple, same-process, latency-critical |

Default to in-process agent-as-tool; escalate to MCP sub-agent when isolation matters; use A2A only for cross-boundary/cross-org.

### A2A (Agent2Agent)

Open protocol for networked agent-to-agent communication. Agents run as separate services. Use when target is a separate standalone service, different team/org, cross-language/framework, or formal contract needed. Use local sub-agents for internal organization, performance-critical ops, shared memory. ADK preserves reasoning traces, long-running tools, artifacts across A2A.

### Workflow agents (ADK)

`SequentialAgent`, `ParallelAgent`, `LoopAgent` orchestrate multiple agents.

### MCP primitives beyond tools

Resources (application-driven, URI-addressed, subscribable) and prompts (user-controlled templates) compose with tools for context injection. Resources: `resources/list`, `resources/read`, `resources/templates/list` (RFC 6570 URI templates), `resources/subscribe`/`notifications/resources/updated`. Prompts: `prompts/list`, `prompts/get` with arguments.

### Programmatic tool calling (OpenAI)

Model writes/runs JavaScript coordinating tools; available tool types: function, custom, mcp, apply_patch, local/hosted shell, code_interpreter. Use when the model needs to coordinate many calls with logic.

### Composition best practices

- Expose high-level orchestration tools (`create_part`) rather than many micro-tools.
- Keep specialist agents behind an agent-as-tool interface; don't leak their internal tools.
- Isolate context: sub-agent intermediate reasoning should not bloat parent context.
- Use model tiering: cheaper model for the specialist, stronger model for orchestration.

---

## 9. Security patterns (sandboxing, permission scoping, allow/deny lists)

### Layered defenses

1. Deny-wins policy engine with scoped patterns.
2. Permission modes (default/acceptEdits/plan/dontAsk/auto/bypassPermissions).
3. Hooks that can short-circuit tool calls.
4. OS-level sandboxing with filesystem/network boundaries.
5. Path scoping.
6. Elevation escape hatches requiring approval.
7. Human-in-the-loop for high-risk actions.

### Permission evaluation order (Claude Code)

Hooks -> Deny rules -> Ask rules -> Permission mode -> Allow rules -> `canUseTool` callback. Deny rules match even in `bypassPermissions`. Bare-name deny removes tool from context. Scoped patterns like `Bash(rm *)`. Tool-name globs in deny (`*`, `mcp__*`). Critical-path `rm`/`rmdir` never auto-approved.

### Policy engines (OpenClaw / Antigravity / agents.cli)

- Global `tools.allow`/`tools.deny` (deny wins, case-insensitive, `*` wildcards). `allow` and `alsoAllow` mutually exclusive in same scope.
- Unified permission engine with Deny/Ask/Allow lists; precedence Deny > Ask > Allow.
- Permission presets: Default/Request Review/Turbo.
- Real-world tiers: reads/tests/formatters allowed; installs/pushes asked; `rm -rf`/secrets writes denied.
- Per-agent profiles: plan (read-only), build (full access).
- Org-wide policy via managed config.
- Workspace rules can only tighten, never loosen (Doable).

### OS sandboxing

- Antigravity: namespaces on Linux, `sandbox-exec`/Seatbelt on macOS; filesystem/network boundaries derived from permissions; `unsandboxed` escape hatches always require approval unless matched by allow rule.
- Doable: eight layers - policy allow-lists, permission handler gating every call with audit entry, process isolator (Nsjail/Systemd/JobObject/Direct), per-project Linux UID, bubblewrap runtime jail, seccomp + capability drop, egress firewall (nftables + Squid allowlist), OS containment.
- Windows: noted as using a previous permission system in Antigravity (unverified beyond that).

### OpenAI risk ratings and guardrails

Risk ratings: low/medium/high by read-only vs write, reversibility, permissions, financial impact. Guardrails: input/output/tool with tripwires; human-in-the-loop approvals (`needs_approval=True`) that pause and resume; plan mode prevents auto-approval of writes. Input guardrails can run in parallel with main model or block before.

### MCP security guidance

Servers must validate inputs, implement access controls, rate limit, sanitize outputs. Clients should prompt for confirmation on sensitive ops, validate results.

### Plugin sandboxing (Agent Governance Toolkit)

Ed25519 signatures, declarative manifests, capability declarations, `PluginSandbox` restricted subprocess blocking dangerous modules at import time.

### Practical defaults

Default new tools to "ask" for side effects. Require explicit allow for automation. Protect critical paths regardless of mode (deny wins). Separate OS sandbox for shell/exec tools; never rely on policy alone for untrusted code. Workspace rules can only tighten, never loosen. Audit every tool call (who, what, when, args, result).

---

## 10. Observability patterns (tracing, logging, metrics)

### Core rule

Instrument every tool call as a first-class span with GenAI semantic-convention attributes. Keep arguments/results out of spans by default for PII safety.

### Span hierarchy (Claude Code/SDK)

Three OTel signals: metrics, logs, traces. Span names: `claude_code.interaction`, `claude_code.llm_request`, `claude_code.tool` (with child spans `claude_code.tool.blocked_on_user`, `claude_code.tool.execution`), `claude_code.hook`. Subagent spans nest under parent tool span. `session.id` attribute. Tracing beta requires `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`.

### GenAI semantic conventions

`gen_ai.operation.name`, `gen_ai.tool.name`, `gen_ai.tool.call.id`, `gen_ai.agent.name`, `gen_ai.conversation.id`. Bind every span with conversation/agent/operation attributes; distinct names per agent/sub-agent. Nested tool spans keep multi-hop workflows connected.

### Per-tool metrics (ADK / Photon / Atlas / mcp-audit)

- ADK: `gen_ai.execute_tool.duration` histogram (agent, tool name, tool type, error type); `gen_ai.invoke_agent.tool_calls` histogram; token usage histograms. ADK-TS: counters `adk.tool.executions`; histograms `adk.tool.duration`.
- Photon: span `gen_ai.tool.call {photon}.{tool}` with attributes; metrics `photon.tool.duration` (histogram), `photon.tool.calls`/`photon.tool.errors` (counters), `photon.circuit_breaker.transitions`, `photon.rate_limit.rejections`, `photon.bulkhead.rejections`. Logs auto-attach context; W3C traceparent propagation with validation; baggage is context only (never expanded into metric labels).
- Atlas: every server-executed tool emits `atlas.tool.<name>` span with call_id, error, streaming, aborted; tool args/results not recorded; MCP dispatch spans include transport/deploy mode; metrics `atlas.mcp.tool.calls`/`atlas.mcp.tool.latency` with outcome dimension.
- mcp-audit: records every tool invocation with timing, cost, tokens, result; aggregates (error rate, p50/p95/p99 latency, total cost, top tools); alert rules; Prometheus exposition; OTLP export.
- AgentOS: spans `agentos.tool_result`, `agentos.gmi.handle_tool_result`; metrics `agentos.tool_results` counter, `agentos.tool_result.duration_ms` histogram; trace IDs attached to streamed chunks.

### Practical defaults

Standardize on GenAI semantic-convention attribute names for portability. Add toolkit-specific prefix only for non-standard metrics. Never record raw tool arguments/results in spans by default (PII/secrets); opt in explicitly with redaction. Propagate W3C traceparent across sub-agents and MCP. Attach trace IDs to streamed chunks and logs. Track per-tool: call count, error count, duration (p50/p95/p99), timeout count, circuit-breaker transitions.

### Gaps

Tool-level cost attribution (per-tool USD) not standardized; mcp-audit implements it but no convention. Trace sampling strategies for high-volume tool calls not covered.

---

## 11. Testing patterns (unit, integration, eval harnesses)

### Testing pyramid for agents

Tool Unit Tests (50%), Agent Integration Tests (30%), E2E Scenario Tests (15%), Adversarial Tests (5%).

### Layer 1: Tool unit tests

Test handlers as pure functions with fixed inputs/outputs. Validate error handling (bad args, timeouts, exceptions). NeMo `ToolTestRunner`: test tools in complete isolation without spinning up workflows/agents/external services. Mock dependencies; assert structured envelope.

### Layer 2: Integration tests

Full agent loop with real tools and mock/stub LLM. 10xGraph: `TestAgent` (drop-in replacement returning predefined responses, records LLM calls, tracks tool names), `MockToolRegistry` (tracks invocations by name/args), `MockMCPClient`. Microsoft Foundry: unit (agent logic, tool handlers, prompt formatting), local integration (full agent vs real models), deployed integration. Purista: test without external providers by injecting fake providers/stores/fixtures; contract tests; coverage gates.

### Layer 3: Eval harnesses (Anthropic framework)

- Task: a single test case with inputs and expected outcome.
- Trial: multiple runs for consistency (models are non-deterministic).
- Grader: logic scoring aspects, multiple assertions.
- Transcript/trace: full messages array.
- Outcome: final environment state.
- Eval harness: runs end-to-end, records steps, grades, aggregates.
- Eval suite: collection of tasks.

Unit-style evals: take a transcript and assert next tool calls/args (cheap, verify prompt-following). Integration evals: run full agentic loop with tool calling and fakes (validate output shape, assumptions).

### Layer 4: Tool simulators

ToolSimulator (Strands Evals): LLM-powered tool simulation with adaptive response generation, stateful shared state across calls, Pydantic schema enforcement; avoids live API calls/PII. Use LLM-powered simulators for multi-turn stateful workflows instead of static mocks that break across turns.

### Layer 5: Adversarial tests

Prompt injection via tool output. Malformed arguments. Timeout/exception paths. Held-out test sets to avoid overfitting tool descriptions.

### CI gating

Regression thresholds (e.g., block merge if score regresses >2%). Microsoft Foundry: structured eval (`azd ai agent eval` with dataset + adaptive evaluator, CI quality gate). 10xGraph: eval reports (HTML/JSON/JUnit).

### Evaluation-driven iteration (Anthropic)

Generate dozens of realistic tasks. Run agentic loops. Analyze transcripts and metrics (redundant calls, errors). Let Claude Code refactor tools. Use held-out test sets to avoid overfit.

### Grading guidance

No single standardized eval metric set or grader rubric is mandated; grading remains task-specific. Measure: tool selection accuracy, argument correctness, trajectory efficiency, final outcome, safety.

---

## 12. Lab-specific deep dives

### 12.1 OpenAI

API: legacy Chat Completions `tools` (non-strict by default) and newer Responses API (recommended; agentic loop by default, built-in/hosted tools, stateful context, encrypted reasoning; preserves reasoning across turns). Tool def: `type: "function"`, `name` (a-z, A-Z, 0-9, underscores/dashes, max 64), `description`, `parameters` (JSON Schema), `strict`. Strict requires `additionalProperties: false` + all fields required. Structured Outputs incompatible with parallel function calls; set `parallel_tool_calls: false`.

Tool types: hosted (web_search, file_search, code_interpreter, image_generation, tool_search, programmatic_tool_calling, MCP); built-in execution (computer use, apply_patch, shell); function tools; agents-as-tools (`agent.as_tool(...)`); MCP servers (stdio/SSE/streamable HTTP or hosted); sandbox capabilities; experimental Codex tool.

Agents SDK: `FunctionTool` dataclass (`name`, `description`, `params_json_schema`, `on_invoke_tool(ctx, args_json)`, `strict_json_schema` default True, `is_enabled`). Created via `@function_tool`/`@tool` (auto-schema from type hints + docstrings; sync/async; optional `RunContextWrapper` first arg). Overrides: `name_override`, `description_override`, `defer_loading`, `needs_approval`, `tool_input_guardrails`, `tool_output_guardrails`, `failure_error_function`. Custom: provide `name`, `description`, `params_json_schema`, `on_invoke_tool` (async). MCP: `MCPServerStdio`/`Sse`/`StreamableHttp`, `HostedMCPTool`, `list_tools()` per run, filtering, caching (`cacheToolsList`), server-prefixed names, `convert_schemas_to_strict`.

Agent loop (SDK): (1) call model, (2) inspect output, (3) if tool calls execute and continue, (4) if handoff switch agents, (5) if final answer return. Exit: final-output tool invoked, or no tool calls; max turns enforced. Partial failures in parallel: return all results (successes normal, failures flagged) each matched to its own id; don't abort batch.

Errors: never crash the loop; catch and return model-visible error message (default generic). Custom `failure_error_function` or `None` to re-raise. Agents API: `success` flag + output/error; result size <4 MiB; retry same `turn_id`/`call_id` while pending. `tool_error_formatter` in `RunConfig`.

Design philosophy: standardized, reusable definitions; "pass the intern test"; principle of least surprise; reduce tool count exposed at once (<20 soft); split agents when tool overload; categorize as Data/Action/Orchestration. Risk ratings low/medium/high. Guardrails: input/output/tool guardrails, tripwires; human-in-the-loop approvals.

Discovery: eager loading default; hosted tool search defers definitions (namespaces/MCP recommended, <10 functions per namespace); client-executed search; MCP `list_tools()` with caching/filtering. Only `gpt-5.4+` supports `tool_search`.

Responses loop: server-managed for hosted tools (shell, code interpreter, MCP, web/file search) with preserved reasoning state and streaming; custom function tools yield control to client. Spectrum: pure client loop, server-orchestrated hosted tools, fully managed (Agents API/SDK).

### 12.2 Anthropic

Messages API: client tools run in your app (Claude returns `tool_use` blocks, `stop_reason: "tool_use"`); server tools run on Anthropic's infra and return results directly. `tool_use` block: `id`, `name`, `input`. Results in a `user` message as `tool_result` blocks with `tool_use_id`, optional `content` (string, nested content blocks of text/image/document/search_result, or document blocks), optional `is_error`. Formatting: tool result blocks must immediately follow the assistant's tool use message; in the user message all `tool_result` blocks before any text; if a server tool has no result block yet, the user message must contain only `tool_result` blocks. Tools integrate into user/assistant message structure (no separate tool role). `tools` param adds tool-use system prompt (286-675 tokens depending on model and tool_choice) plus per-tool tokens.

Tool defs: `name` regex `^[a-zA-Z0-9_-]{1,128}$`, detailed `description`, JSON Schema `input_schema`, optional `input_examples`, `strict`, `defer_loading`, `cache_control`, `allowed_callers`, `eager_input_streaming`. `strict: true` uses grammar-constrained sampling; requires `additionalProperties: false` in practice; not supported on computer/browser toolsets. `input_examples` schema-validated, add ~20-50 tokens (simple) / ~100-200 tokens (complex); not supported on server tools/toolsets. `tool_choice`: `auto` (default), `any` (must use one tool), `tool` (force named), `none`; `disable_parallel_tool_use` lives inside `tool_choice`. On Opus 5.5/Sonnet 5.5/Fable 5.1/Mythos 5.1, `any`/`tool` return 400 - use `auto` + strict or structured outputs. `allowed_callers`: `"direct"` (default) and/or `"code_execution_20260120"` for programmatic tool calling.

MCP: JSON-RPC 2.0; servers declare capabilities; tools (model-controlled, `tools/list`, `tools/call`), resources (application-driven, URI-addressed, readable/subscribable), prompts (user-controlled templates, `prompts/get`). Pagination, list-changed notifications, structured/unstructured content. Tool defs: `name`, optional `title`, `description`, `inputSchema`, optional `outputSchema`, optional `annotations`. Results: `content` array (text/image/audio/resource_link/embedded resource) plus optional `structuredContent` and `isError`. Errors: protocol errors (JSON-RPC) vs tool execution errors (`isError: true`). Security: servers validate inputs, access controls, rate limit, sanitize outputs; clients prompt for confirmation on sensitive ops, validate results.

Claude Agent SDK: runs the same agentic loop as Claude Code. Built-in tools: file (Read/Edit/Write), search (Glob/Grep), execution (Bash), web (WebSearch/WebFetch), discovery (ToolSearch), orchestration (Agent, Skill, AskUserQuestion, TaskCreate/Update). Permissions: `allowed_tools` auto-approves, `disallowed_tools` blocks, `permission_mode` (default/acceptEdits/plan/dontAsk/auto/bypassPermissions); denied calls feed a rejection message back. Parallel: read-only run concurrently; state-modifying run sequentially; custom tools default sequential unless `readOnlyHint`. MCP: servers registered via `mcpServers` (stdio/HTTP/SSE/SDK in-process); tool naming `mcp__<server>__<tool>`; allow via `allowedTools` wildcards; connection timing varies. Hooks: PreToolUse/PostToolUse/UserPromptSubmit/Stop/SubagentStart/Stop/PreCompact run in host process, can short-circuit. Context management: automatic compaction near limit emits `compact_boundary`; subagents get fresh context; MCP tool search defers schemas by default. Effort levels and budget caps (`max_turns`, `max_budget_usd`).

Tool errors: tool execution error returned in `content` with `is_error: true`; Claude incorporates and may suggest retry; write instructive messages. Invalid tool name/missing params: continue with `tool_result` indicating error; Claude retries 2-3 times with corrections before apologizing; eliminate with strict tool use. Server tool errors handled transparently. Empty result allowed. MCP: protocol vs execution errors.

Context engineering: context rot (as tokens increase, recall decreases; n^2 pairwise relationships). System prompts at "right altitude". Tools token-efficient, self-contained, minimally overlapping. Just-in-time retrieval: maintain lightweight identifiers, load data at runtime via tools (Claude Code uses glob/grep/head/tail). Long-horizon: compaction, structured note-taking, sub-agent architectures. Tool Search Tool reduces context bloat (85%+ reduction possible). Prompt caching: deferred tools stripped from cached prefix; cache breakpoints on tool definitions.

ACI: invest as much effort in ACI as HCI. Tool format choices matter (diffs vs whole files, JSON vs markdown); keep formats close to internet text; avoid formatting overhead. SWE-bench: relative filepaths caused errors after agent moved out of root; switching to absolute filepaths fixed it. Give model enough tokens to think before committing; test in workbench with many examples; iterate on mistakes.

Tool design ("Writing tools for agents"): choose fewer high-impact tools over API wrappers; consolidate operations (`schedule_event` instead of list/create); agents have limited context, avoid returning all records. Namespace by service/resource (`asana_search`, `asana_projects_search`); prefix vs suffix affects evals. Return meaningful context: prefer semantic identifiers (names, slugs) over UUIDs; support `response_format` enum (`concise`/`detailed`); structure affects performance. Token efficiency: pagination, range selection, filtering, truncation; default limits (Claude Code 25,000 tokens); truncation messages steer toward efficient strategies. Prompt-engineer descriptions: treat like docstrings for a junior dev; examples, edge cases, boundaries; precise refinements to SWE-bench tool descriptions dramatically reduced errors. Evaluation-driven iteration: generate dozens of realistic tasks; run agentic loops; analyze transcripts and metrics (redundant calls, errors); let Claude Code refactor tools; held-out test sets. Tool annotations (MCP) disclose open-world/destructive behavior.

Parallel tool calls and streaming: Claude may emit multiple `tool_use` blocks in one turn; host chooses concurrency (read-only safe in parallel, stateful sequential), must return all results in a single user message with tool_results first; streaming delivers tool-use blocks incrementally; parallelism disabled via `tool_choice.disable_parallel_tool_use`. Execution semantics: API doesn't prescribe order; host may run concurrently or sequentially; return one `tool_result` per `tool_use`, all in next user message, matched by `tool_use_id`; put tool_results before text; for skipped calls return `is_error: true` with explanation. Computer use/browser use batches stricter: run sequentially in order, stop at first failure. Claude 4+ makes parallel calls by default when beneficial; maximize via system prompt (`<use_parallel_tool_calls>` block) or user phrasing. Disable: `tool_choice: {type: "auto"|"any"|"tool", disable_parallel_tool_use: true}`. Streaming: `StreamEvent` messages carry raw API deltas; fine-grained input streaming via `eager_input_streaming` on user-defined tools.

Discovery and registration: dynamic. MCP servers expose `tools/list` (paginated, with `listChanged` notifications). Claude Code/SDK defers schemas via tool search. Messages API MCP connector fetches server tool lists (with pinning in newer betas). Registration requires explicit allowlisting. MCP discovery: clients send `tools/list` (paginated via cursor); servers notify `notifications/tools/list_changed`; `listChanged` declared in capability. Agent SDK: MCP servers registered via `mcpServers`; tool names namespaced `mcp__<server>__<tool>`; `allowedTools` wildcards auto-approve; connection timing varies (stdio/HTTP/SSE may delay first turn; cached tool lists enable deferred connect). Tool search: defer loading with `defer_loading: true`; search variants regex/BM25; server-side `tool_search_tool_*`; at least one non-deferred tool required; up to 10,000 deferred tools. MCP connector (Messages API): `mcp_servers` array + `mcp_toolset` in `tools`; allowlist/denylist via `enabled`; `defer_loading` per tool; `mcp-client-2026-09-15` beta pins tool lists via `mcp_tool_listing` blocks. Claude Code/SDK MCP tool search on by default; schemas deferred unless `alwaysLoad: true`.

### 12.3 Google

Function calling API: four-step protocol where the model returns a structured `function_call` step (name + arguments) and the application executes the function and returns a `function_result` step. Tools declared inline as JSON schemas in the request's `tools` array; the model never executes code itself. Interactions API is current surface; chaining via `previous_interaction_id`. Supports parallel and compositional/sequential function calling.

Tool defs: `name`, `description`, `parameters` (JSON Schema object with properties/required). ADK generates schema automatically from Python function signature (name, docstring, type hints, defaults) when wrapping with `FunctionTool`. Parameters required if type hint without default; optional if default given or `typing.Optional`/`| None`. `*args`/`**kwargs` ignored. Preferred return is a dict/map; non-dict auto-wrapped into `{"result": <value>}`. Best practice: include a "status" key ("success"/"error"/"pending") and human-readable error messages. Docstrings become tool description. JSON schema tool declarations (`JSON_SCHEMA_FOR_FUNC_DECL`) enabled by default in ADK Python via Pydantic, toggle by env var or `override_feature_enabled`. ADK supports `ToolContext` injection (typed parameter) for session state/actions/artifacts; detected by type, not name.

ADK tool system: `FunctionTool`/`LongRunningFunctionTool` for Python functions; `AgentTool` for in-process sub-agent delegation; `McpToolset` for external MCP servers; OpenAPI tools; auth; built-in grounding tools. All implement common `BaseTool`/`Toolset` interface. `LongRunningFunctionTool` for tasks managed outside the agent workflow (human-in-the-loop, approvals); agent run pauses and client can send intermediate/final responses. `McpToolset` is the ADK<->MCP server interface: handshake + `list_tools` discovery, adapts external schemas into ADK `BaseTool` instances, proxies `call_tool`. ADK supports exposing an agent as an MCP server via `to_mcp_server`, and sub-agent delegation via `AgentTool`. `tool_filter` (list or predicate) restricts which tools from a toolset are exposed. Built-in grounding tools: Google Search grounding, Google Maps grounding, code execution, URL context, file search, computer use.

Execution: ADK runs function tools in parallel when defined as `async def` (asyncio event loop) since v1.10.0; synchronous tools block others. Before Tool Callback runs before `run_async`; can modify args; returning a dict skips execution and uses that dict as result (cache/override); `None` lets tool run. After Tool Callback runs after successful execution; can replace result by returning a new dict; `None` keeps original. Non-dict results wrapped into `{"result": ...}` only after callback runs. `on_tool_error_callback` (Python) / `OnToolErrorCallbacks` (Go): runs on tool exception; returning a dict suppresses exception and uses it as result. Before/After Model Callbacks can skip the LLM call (return `LlmResponse`) or post-process responses; `on_model_error_callback` handles model exceptions. Agent lifecycle callbacks (`before_agent`/`after_agent`) gate or append output. Long-running tools pause the agent run; client sends intermediate/final `FunctionResponse` to resume; invocation ID must match for Resume feature. Sequential/parallel/loop workflow agents (`SequentialAgent`, `ParallelAgent`, `LoopAgent`) orchestrate multiple agents.

MCP support (ADK): `McpToolset` client adapter discovers tools from MCP server over stdio or HTTP/SSE, adapts schemas to ADK tools, proxies calls, handles auth (headers, bearer, OAuth2 with token refresh). ADK can also expose an agent as an MCP server. Transports: `StdioConnectionParams` (local subprocess via npx/python) and `StreamableHTTPConnectionParams`/`SseConnectionParams` (remote HTTP/SSE with headers, timeout, sse_read_timeout). Auth: `auth_scheme` (Bearer/Basic/APIKey/OAuth2) + `auth_credential`; ADK builds Authorization headers and manages OAuth2 refresh. Manual header injection also. Resources: `list_resources()` / `read_resource(name)`; `use_mcp_resources=True` equips the LLM with `LoadMcpResourceTool`. Tool filtering via `tool_filter=[...]`. Timeouts; explicit `close()`/context managers in custom runtimes. Production rule: `McpToolset` must be instantiated synchronously in `agent.py` (no async factory) for deployed agents. Environment-aware connection selection (K_SERVICE env var -> HTTP; else stdio) recommended.

A2A: open protocol for networked agent-to-agent communication. Use A2A when target is a separate standalone service, different team/org, cross-language/framework, or formal contract needed; use local sub-agents for internal organization, performance-critical ops, shared memory. ADK workflow: expose agent as `A2AServer`; consume via `RemoteA2aAgent` (client proxy). ADK preserves reasoning traces, long-running tools, artifacts across A2A. `AgentTool` wraps an `LlmAgent` as a native tool for in-process hierarchical delegation, isolating intermediate reasoning/tool calls (zero context bloat). Comparison: Direct MCP (low latency, high context bloat), Agent-exposed MCP server (isolated), AgentTool sub-agent (zero context bloat, model tiering, higher cost/latency).

Tool errors: no auto-retry appears; structured error handling via callbacks. Tools return descriptive dicts with "status" key. Validation feedback is structured (JSON), not prose. Invariants: tools return structured dicts (`{"ok", ...}`) and never raise into the loop. Gemini API returns function calls as structured steps; errors in execution reported back via `function_result` content blocks.

Tool design: grounding tools (Google Search, Google Maps, URL context, file search), code execution, computer use as first-party tools, combined with function calling via "tool combination". Design guidance: fewer parameters, simple types (str/int), meaningful names, async/parallel-ready, descriptive docstrings. Agent Skills (agentskills.io) extend capabilities efficiently within context window limits.

Discovery and registration: static via agent's `tools` list (functions, toolsets, MCP adapters); MCP toolsets discover tools dynamically via `list_tools` at init; no global tool registry - scoping per-agent via `tool_filter`; skills and plugins extend capabilities separately. OpenAPI tools generate tools from an OpenAPI spec. Authentication configured per-toolset via `auth_scheme`/`auth_credential`. Whether ADK supports dynamic tool registration at runtime not documented; unverified.

### 12.4 Open-source frameworks

LangChain: tools are callable objects with name, description, Pydantic args_schema; plain functions/callables auto-converted; ToolNode handles execution in LangGraph. `@tool` decorator; type hints define input schema, docstring becomes description. `create_agent` accepts `tools: Sequence[BaseTool | Callable | dict]`. ToolNode supports parallel execution, error handling, state injection, Command-based state updates. Constructor: `tools`, `handle_tool_errors` (bool/str/callable/type/tuple, default catches invocation errors), `messages_key`, `wrap_tool_call`/`awrap_tool_call`. `StructuredTool` represents an action wrapping any function; defined by `name`, `description`, `args_schema` (Pydantic BaseModel), `_run`/`_arun`. Older string-input `Tool` shares same BaseTool base. `create_agent` splits tools into built-in provider tools (dicts) and regular tools; ToolNode created from available_tools + middleware tools; `tools_by_name` becomes default tool set.

LlamaIndex: `AsyncBaseTool` with metadata; `FunctionTool` wraps arbitrary sync/async functions with auto-inferred schemas and optional context injection; `QueryEngineTool` wraps a query engine and supports `return_direct`. `FunctionTool.from_defaults(fn, name=..., description=...)`; type hints and docstrings drive schema; `Annotated` types specify arg descriptions; async via `async_fn`. Inspects signature to detect context parameter (`requires_context`, `ctx_param_name`); supports callbacks (`callback`/`async_callback`) and `partial_params`. Both subclass `AsyncBaseTool` and expose `call`/`acall` returning `ToolOutput` (content, tool_name, raw_input, raw_output). `QueryEngineTool.from_defaults` takes `query_engine`, `name`, `description`, `return_direct`, `resolve_input_errors`; `return_direct=True` ends the agent loop and returns the tool result directly. Tool retrieval at query time via `ObjectIndex`/`ObjectRetriever` passed as `tool_retriever` to agents, for large tool catalogs.

CrewAI: two construction paths (BaseTool subclass with `_run`/`_arun` and `@tool` decorator) built on Pydantic args schemas, plus tool-level controls (`result_as_answer`, `max_usage_count`, caching) and agent-level delegation hooks. `@tool` supports `result_as_answer` (tool result becomes final answer) and `max_usage_count` (usage cap). Typed outputs: infers output schema when BaseTool has Pydantic return annotation; agent receives JSON based on output model. Custom caching via `cache_function` per tool; async tools supported; framework handles sync/async automatically. Tool delegation: agents can delegate work to coworkers via injected `Delegate work to coworker` / `Ask question to coworker` tools; hooks (`before_tool_call`/`after_tool_call`) gate execution; authority can narrow monotonically across delegation. `to_langchain` converts CrewAI tools to `CrewStructuredTool` for LangChain interop.

AutoGen/AG2: wraps any function in `FunctionTool`, auto-generates JSON schema from type annotations/descriptions; tools subclass `BaseTool` and passed directly to model clients; execution explicit via `run_json` with cancellation tokens. `FunctionTool(func, description=...)`; type annotations with `Annotated` descriptions generate schema; every tool subclasses `BaseTool` exposing `.schema`, `.run_json(args, cancellation_token)`, `.return_value_as_string(result)`. Tools passed to `model_client.create(messages=..., tools=[...])`; client returns `FunctionCall` objects; caller executes tools (example uses `asyncio.gather` for parallel) and feeds `FunctionExecutionResult` back. Built-in tools: code execution, GraphRAG search, MCP server tools, HTTP tool, LangChain adapter. Tool-equipped agents implement their own loop; AgentChat provides pre-built agents.

Pydantic AI: registers tools via decorators or `tools` list; `RunContext` injects dependencies; schemas auto-generated from signatures + Pydantic, with rich docstring extraction and advanced toolsets. Registration: `@agent.tool` (needs context), `@agent.tool_plain` (no context), or `tools=[fn, Tool(fn, takes_ctx=...)]`. `RunContext` provides `ctx.deps` and `ctx.enqueue` for injecting follow-up messages; tools can return any Pydantic-serializable value. Schema: function parameters (except RunContext) build JSON schema; docstrings (google/numpy/sphinx styles) parsed via griffe for parameter descriptions; `require_parameter_descriptions=True` enforces docs. Toolsets manage collections of tools and can be combined; supports MCP servers and third-party tools. Native tools, common tools, deferred tools (approval/external execution), advanced features (custom schemas, dynamic tools, retries).

smolagents: tool as class wrapping `forward` method with explicit `name`, `description`, `inputs` (JSON-schema-ish types), `output_type`; `@tool` decorator for simple functions; CodeAgent executes tools by generating Python code. A tool subclasses `Tool` and defines `name`, `description`, `inputs` (dict with type/description), `output_type`, and `forward(...)`. Types are Pydantic JSON-schema formats. `@tool` decorator recommended for simple tools; subclassing `Tool` for complex/multi-method. Tools shared/loaded from Hub (`push_to_hub`, `load_tool`, `from_hub`), imported from MCP servers (`MCPClient`, `ToolCollection.from_mcp`), LangChain (`Tool.from_langchain`), Gradio Spaces (`Tool.from_space`). `structured_output=True` on MCPClient enables JSON-schema-aware tool outputs; toolbox is standard dict (`agent.tools[name] = tool`). CodeAgent writes actions as Python code (function nesting, loops, conditionals) to invoke tools; ToolCallingAgent uses JSON/text tool-calling.

Common patterns across frameworks: (1) Tool = name + description + JSON-schema args + callable implementation. (2) Results are string/structured payloads returned to the model. (3) An executor runs calls and feeds results back. (4) Context/dependency injection and async support increasingly standard. Schema derived from type annotations/Pydantic models/docstrings across all. Result types: LangChain ToolMessage; LlamaIndex ToolOutput; AutoGen FunctionExecutionResult; Pydantic AI ToolReturnPart; CrewAI typed output; smolagents forward return. Executors: LangChain ToolNode; LlamaIndex agent loop; AutoGen explicit orchestration; CrewAI framework-managed; Pydantic AI agent run loop; smolagents CodeAgent/ToolCallingAgent. Context injection: LlamaIndex `requires_context`; Pydantic AI `RunContext`; LangChain ToolNode state injection; CrewAI delegation hooks. Async: LlamaIndex acall; CrewAI `_arun`; AutoGen async functions; Pydantic AI async tools; LangChain `_arun`. Interop: LangChain<->CrewAI (`to_langchain`), LangChain<->smolagents (`from_langchain`), LangChain<->AutoGen adapter, Pydantic AI third-party/MCP toolsets. Convergence: Pydantic/JSON-schema-driven tool definitions, async-first execution, MCP as universal tool transport.

---

## 13. ThinkToCad toolkit implementation guide

How to apply these patterns to the ThinkToCad CAD toolkit (this repo).

### Current state

- `thinktocad/mcp/build123d_server.py`: works - `create_part` (subprocess execution, artifacts in `output/run_*/`), `validate_code`.
- `thinktocad/mcp/freecad_server.py` and `matlab_server.py`: stubs - return `{"ok": False, "error": "... not implemented"}`.
- `thinktocad/runtime/design_agent.py`: ReAct loop with 5 termination conditions; `_tool_validate` and `_tool_simulate` are TODOs; `step_fn` not wired.
- No tests, CI, or lint config. Not a git repo.

### Recommended architecture

Adopt the canonical contract from Section 3. Define one `ToolDefinition` dataclass in a shared module (e.g., `thinktocad/tools/registry.py`) and adapt to FastMCP/MCP at the server boundary. All three MCP servers (build123d, freecad, matlab) should expose tools through the same registry.

Suggested tool set (minimal viable, consolidated):

| Tool | Side effect | Purpose |
|------|-------------|---------|
| `thinktocad_validate_code` | read | Static compile check (exists as `validate_code`) |
| `thinktocad_create_part` | exec | Run build123d code in subprocess (exists as `create_part`) |
| `thinktocad_verify_part` | read (freecad) | Mass, interference, clearance checks (stub -> implement) |
| `thinktocad_simulate` | read (matlab) | Dynamics/kinematics simulation (stub -> implement) |
| `thinktocad_retrieve_knowledge` | read | Fetch mechanism/constraint/lesson files |
| `thinktocad_save_attempt` | write | Persist attempt_N.yaml |

Consolidate micro-operations. Use `action` params where natural (e.g., `verify_part(checks=["mass","interference","clearance"])`).

### Apply the invariants

- `_execute_tool` in `design_agent.py` already never raises - keep it that way. Wrap every new tool the same way.
- Return structured envelopes: `{"ok": bool, "data": ..., "error": {code, message, retryable, suggested_fix}}`. The build123d server currently returns `{ok, stdout, stderr, artifacts, workdir, error}` - normalize to the envelope (put stdout/stderr/artifacts under `data`).
- Units: mm internally, params snake_case with suffix. `create_part` takes `code` (string) - the code itself must use mm; document this in the tool description.
- One source of truth: contract YAML -> spec -> code. The design agent loads `contracts/<name>.yaml`; geometry dimensions must come from the contract, not be hard-coded in generated code.

### Implement the stubs

1. `freecad_server.py`: implement `verify_part` (mass, interference, clearance) as subprocess or FreeCAD RPC. Return structured envelope. Handle timeout (120s). Never raise.
2. `matlab_server.py`: implement `simulate` similarly.
3. `design_agent._tool_validate`: call freecad MCP (or in-process). `_tool_simulate`: call matlab MCP.

### Concurrency and timeouts

- `create_part` runs in subprocess with timeout (already). Add per-tool timeout to registry metadata.
- Read-only tools (`validate_code`, `retrieve_knowledge`) can run in parallel; `create_part`/`verify_part`/`simulate` are exec/stateful - sequential.
- Preserve call order in outputs; isolate sibling failures (already in `_execute_tool` loop, but make explicit).

### Error handling

- Normalize all errors to the envelope. Build123d subprocess failures: put stderr + suggested fix ("check imports; ensure export_step called") in `error.suggested_fix`.
- Timeout: `{"ok": false, "error": {"code": "TIMEOUT", "message": "timeout (120s)", "retryable": true, "suggested_fix": "simplify geometry or increase timeout"}}`.
- Freecad/matlab stubs currently return `{"ok": False, "error": "... not implemented"}` - replace with real impls or keep as structured "NOT_IMPLEMENTED" errors until done.

### Knowledge write-back (trust tiers T1-T4)

- `save_memory` writes `memory/designs/<name>/attempt_N.yaml`. Add trust tier field. Never silently overwrite a higher-trust entry with a lower-trust one. Implement a check: if existing entry has tier >= new tier, skip or require explicit override.

### Observability

- Add OTel spans per tool call: `thinktocad.tool.<name>` with `gen_ai.tool.name`, `gen_ai.tool.call.id`. Log call count, error count, duration. Keep args/results out of spans by default (they may contain file paths / code).
- Track circuit-breaker transitions if you add breakers around FreeCAD/MATLAB (external processes).

### Testing

- There are no tests. Add:
  - Unit tests for `_run_code_sandboxed`, `_tool_build`, `_execute_tool` (mock subprocess).
  - Unit tests for contract loading, knowledge retrieval.
  - Integration test for the ReAct loop with a mock `step_fn`.
  - Eval harness: realistic CAD tasks (e.g., "create a bracket with 4 holes") with graders checking artifact existence + dimensions.
- Use a tool simulator for multi-turn stateful workflows (geometry depends on prior steps).

### Security

- `create_part` executes arbitrary Python in a subprocess - already sandboxed by subprocess + timeout + cwd isolation. Add: deny dangerous imports (os.system, subprocess) via AST pre-check in `validate_code` or a pre-execution filter. Consider a restricted Python environment (no network, limited filesystem).
- Freecad/MATLAB: same subprocess isolation.
- Path scoping: artifacts only under `output/run_*/`. Validate no path traversal in generated code (static check).
- Human-in-the-loop: high-risk ops (overwriting a verified part, publishing) require approval. The loop already supports `interrupt` termination - use it.

### Discovery and registration

- FastMCP `@mcp.tool()` is the current registration. Add a central registry dict so tools can be enumerated for deferred loading / tool search later.
- Names: prefix with `thinktocad_` when exposed alongside other toolkits; keep short names internally.
- Descriptions: pass the intern test. `create_part` description should state: code must be Python using build123d, must export at least one artifact (step/stl), units are mm, timeout 120s, returns artifact paths.

### Quick wins (apply now)

1. Normalize build123d server output to the structured envelope.
2. Implement `freecad_server.py` verify_part (or a credible stub with structured "NOT_IMPLEMENTED").
3. Add `thinktocad_` prefix to tool names for namespace safety.
4. Add OTel spans + per-tool metrics.
5. Add a test directory with unit tests for the build sandbox.
6. Document the tool contract in each server's module docstring.

---

## 14. Quick reference: "I want to do X"

| I want to... | Pattern / section | Key rule |
|--------------|-------------------|----------|
| Define a new tool | Canonical contract (S3) + AI pointer rules (S2) | Name + schema + description self-sufficient; strict mode |
| Make schema strict | S3 strict mode | `additionalProperties: false`, all required, optionals nullable |
| Handle a tool error | S6 | Return structured envelope; never raise; encode retryability |
| Retry a transient failure | S6 retry policy | Silent backoff; surface only if different input needed; bound attempts |
| Time out a hung tool | S5 timeout | Per-tool timeout; abandon and return typed timeout result |
| Run tools in parallel | S5 concurrency | Parallel reads, sequential writes; preserve call order |
| Cancel a run | S5 cancellation | Cooperative tokens at safe points |
| Format a tool result | S7 | High-signal, token-efficient; paths/ids not full payloads |
| Truncate a large result | S7 truncation | Steering message pointing to efficient strategy |
| Return binary/artifact | S7 binary | Write to disk; return path |
| Compose tools into a pipeline | S8 | Sequential/parallel/conditional in orchestrator |
| Delegate to a specialist agent | S8 agent-as-tool | In-process by default; escalate to MCP/A2A |
| Let model orchestrate tools | S8 programmatic | Model writes code coordinating tools |
| Reduce context bloat | S4 deferred loading + S7 token efficiency | Defer schemas; minimal viable tool set |
| Scope tools per agent | S4 scoping | `tool_filter` / namespaces |
| Add a plugin | S4 plugin system | Entry points + manifest + lifecycle hooks + trust levels |
| Discover tools at runtime | S4 MCP discovery | `tools/list` paginated + `listChanged` |
| Sandbox untrusted code | S9 | OS sandbox + policy; never policy alone |
| Set up permissions | S9 | Deny-wins; Deny > Ask > Allow; critical paths never auto-approved |
| Approve a sensitive action | S9 human-in-the-loop | `needs_approval=True`; pause + resume |
| Trace tool calls | S10 | GenAI semantic conventions; spans per call |
| Measure tool performance | S10 metrics | Per-tool count/error/duration; no raw args in spans |
| Unit-test a tool | S11 | Pure function with fixed I/O; mock deps |
| Integration-test the loop | S11 | Mock LLM + real tools |
| Run an eval suite | S11 | task + trial + grader + transcript + outcome + suite |
| Simulate tools in tests | S11 | LLM-powered, stateful, schema-enforced |
| Gate CI on quality | S11 | Regression threshold (e.g., >2% blocks merge) |
| Write knowledge back | S13 trust tiers | Never overwrite higher-trust with lower-trust |
| Port to OpenAI | S12.1 | Responses API; strict mode; tool search |
| Port to Anthropic | S12.2 | Messages API; `tool_result` blocks; ACI design |
| Port to Google | S12.3 | ADK; status key; async parallel; A2A |
| Port to open-source framework | S12.4 | Pydantic/JSON-schema; MCP transport |

---

## 15. References

Research notes (this repo):
- `research_notes/Building AI agent toolkits/openai_toolkit.md`
- `research_notes/Building AI agent toolkits/anthropic_toolkit.md`
- `research_notes/Building AI agent toolkits/google_toolkit.md`
- `research_notes/Building AI agent toolkits/opensource_toolkits.md`
- `research_notes/Building AI agent toolkits/toolkit_design_patterns.md`

Repo context:
- `AGENTS.md` (invariants, conventions, gotchas)
- `WORKFLOW.md` (end-to-end process)
- `thinktocad/mcp/build123d_server.py`, `freecad_server.py`, `matlab_server.py`
- `thinktocad/runtime/design_agent.py`

Provider docs (cited in research notes):
- OpenAI: Function calling, Responses API, Agents SDK, Agents API, tool search, guardrails, programmatic tool calling.
- Anthropic: Tool use overview, define tools, handle tool calls, strict tool use, MCP, Claude Agent SDK, context engineering, building effective agents, writing effective tools for agents, parallel tool use, tool search tool, MCP connector.
- Google: Gemini function calling, ADK tools (function, MCP, agent-managed), callbacks, performance, A2A, grounding.
- MCP specification: tools, resources, prompts (2025-06-18).
- Open-source: LangChain/LangGraph, LlamaIndex, CrewAI, AutoGen, Pydantic AI, smolagents.

Cross-cutting sources (cited in research notes):
- CSIRO Tool/Agent Registry; NeMo Agent Toolkit plugin system; Soothe RFC-600; AgentsKit architecture; Zylos plugin architecture.
- OpenTelemetry GenAI semantic conventions; Claude Code observability; ADK metrics; Photon; Atlas; mcp-audit; AgentOS.
- Anthropic evals framework; NeMo ToolTestRunner; 10xGraph testing; Strands ToolSimulator; Microsoft Foundry.
- Claude Code permissions; OpenClaw tool policy; Antigravity permissions/sandbox; agents.cli; Doable sandboxing; OpenAI guardrails; Agent Governance Toolkit plugin marketplace.

---

*End of guide.*