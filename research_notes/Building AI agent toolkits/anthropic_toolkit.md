# Anthropic agent toolkit design research

## Anthropic's tool use API (tool_use blocks, tool_result blocks, stop_reason)

### Takeaway
Anthropic's Messages API implements tool use as a structured round-trip: Claude returns `stop_reason: "tool_use"` with `tool_use` blocks, the host executes them, and results come back as `tool_result` blocks in a `user` message; the API integrates tools into the user/assistant message structure rather than a separate tool role.

### Cited Findings
- Tools differ primarily by where code executes: client tools run in your application (Claude returns `tool_use` blocks and `stop_reason: "tool_use"`); server tools run on Anthropic's infrastructure and return results directly — [Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).
- A `tool_use` block contains `id` (unique identifier used to match results), `name`, and `input` (object conforming to `input_schema`); computer/browser use member blocks also carry `toolset_name` — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
- Tool results are returned in a `user` message as `tool_result` blocks with `tool_use_id`, optional `content` (string, nested content blocks of text/image/document/search_result, or document blocks), and optional `is_error` — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
- Formatting requirements: tool result blocks must immediately follow the assistant's tool use message; in the user message all `tool_result` blocks must come before any text; if a server tool has no result block yet, the user message must contain only `tool_result` blocks — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
- `tool_choice` options: `auto` (default), `any` (must use one tool), `tool` (force a named tool), `none`; `disable_parallel_tool_use` lives inside `tool_choice` — [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#forcing-tool-use).
- Unlike APIs that use special `tool`/`function` roles, Claude integrates tools into the `user`/`assistant` message structure — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
- The `tools` parameter adds a tool-use system prompt (e.g. 286–675 tokens depending on model and tool_choice) plus per-tool tokens — [Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).

### Inferences
- Keeping tool results inside `tool_result` blocks (not system prompts) is an explicit prompt-injection hardening requirement, since tool output is untrusted — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).

### Gaps
- Exact SDK-level retry/backoff behavior for HTTP-level failures (429/5xx) is not documented in the fetched pages; not verified here.

## Tool definitions: name, description, input_schema, strict mode

### Takeaway
A client tool is defined by `name` (regex `^[a-zA-Z0-9_-]{1,128}$`), a detailed `description`, a JSON Schema `input_schema`, optional `input_examples`, and optional `strict`, `defer_loading`, `cache_control`, `allowed_callers`, `eager_input_streaming`; `strict: true` uses grammar-constrained sampling to guarantee schema-conformant inputs.

### Cited Findings
- Tool definition fields: `name`, `description`, `input_schema` (JSON Schema), optional `input_examples` (array of example input objects) — [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools).
- Optional properties on any tool: `cache_control`, `strict`, `defer_loading`, `allowed_callers`, `input_examples`, `eager_input_streaming` (user-defined only) — [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#tool-definition-properties).
- Best practices: extremely detailed descriptions (3–4+ sentences); consolidate related ops into fewer tools with an `action` parameter; meaningful namespacing prefixes (`github_list_prs`); return only high-signal fields; ask for explanation not reasoning — [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#best-practices-for-tool-definitions).
- `strict: true` guarantees Claude's tool inputs match the schema via grammar-constrained sampling; requires `additionalProperties: false` in practice; not supported on computer/browser toolsets — [Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use).
- `input_examples` are schema-validated, add ~20–50 tokens (simple) / ~100–200 tokens (complex), not supported on server tools/toolsets — [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#providing-tool-use-examples).
- Forcing tool use: `tool_choice` of `auto`/`any`/`tool`/`none`; on Opus 5.5/Sonnet 5.5/Fable 5.1/Mythos 5.1, `any`/`tool` return 400 — use `auto` + strict or structured outputs — [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#forcing-tool-use).
- `allowed_callers` controls who may call a tool: `"direct"` (default) and/or `"code_execution_20260120"` for programmatic tool calling — [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#allowed_callers-values).

### Inferences
- Strict mode is the recommended pairing with `tool_choice: any` to guarantee both a call and schema-valid inputs; omitting strict risks type mismatches like `"2"` vs `2` — [Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use).

### Gaps
- JSON Schema subset supported under strict mode is referenced but not fully enumerated in the fetched pages (links to structured-outputs limitations) — not reproduced here.

## Model Context Protocol (MCP): tools, resources, prompts

### Takeaway
MCP is a JSON-RPC 2.0 protocol where servers declare capabilities and expose tools (model-controlled, `tools/list`, `tools/call`), resources (application-driven, URI-addressed, readable/subscribable), and prompts (user-controlled templates, `prompts/get`), with pagination, list-changed notifications, and structured/unstructured content.

### Cited Findings
- MCP tools are model-controlled; servers declare `tools` capability with optional `listChanged`; discovery via `tools/list` (paginated), invocation via `tools/call` with `name`+`arguments`; results carry `content` array (text/image/audio/resource_link/embedded resource) plus optional `structuredContent` and `isError` — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).
- Tool definitions include `name`, optional `title`, `description`, `inputSchema`, optional `outputSchema`, optional `annotations`; output schema enables structured results — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).
- Errors: protocol errors (JSON-RPC, e.g. -32602 unknown tool) vs tool execution errors (`isError: true` in result) — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).
- Resources are application-driven, identified by URI; capability supports optional `subscribe` and `listChanged`; `resources/list`, `resources/read`, `resources/templates/list` (RFC 6570 URI templates), `resources/subscribe`/`notifications/resources/updated` — [MCP resources spec](https://modelcontextprotocol.io/specification/2025-06-18/server/resources).
- Resource contents are text or base64 blob; annotations: `audience`, `priority` (0.0–1.0), `lastModified` — [MCP resources spec](https://modelcontextprotocol.io/specification/2025-06-18/server/resources).
- Prompts are user-controlled templates; capability optional `listChanged`; `prompts/list`, `prompts/get` with arguments; messages contain text/image/audio/embedded resources with roles user/assistant — [MCP prompts spec](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts).
- Security: servers must validate inputs, implement access controls, rate limit, sanitize outputs; clients should prompt for confirmation on sensitive ops, validate results — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).

### Inferences
- MCP's three interaction models (model-controlled tools, application-driven resources, user-controlled prompts) map cleanly onto how context is injected into an agent: tools as actions, resources as data, prompts as slash commands.

### Gaps
- Transport details (stdio/HTTP/SSE/streamable HTTP) are referenced but not fully covered in the fetched spec pages; the Agent SDK MCP page covers them at a higher level.

## Claude Agent SDK tool system: built-in tools, custom tools, MCP clients, hooks

### Takeaway
The Claude Agent SDK exposes Claude Code's agent loop as a library with built-in tools, MCP server integration (stdio/HTTP/SSE/SDK servers), custom in-process SDK MCP tools, permission modes, hooks, subagents, sessions, compaction, and tool search for deferred loading.

### Cited Findings
- SDK runs the same agentic loop as Claude Code: receive prompt → evaluate/respond → execute tools → repeat → return result; messages include System/Assistant/User/StreamEvent/Result — [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop).
- Built-in tools: file (Read/Edit/Write), search (Glob/Grep), execution (Bash), web (WebSearch/WebFetch), discovery (ToolSearch), orchestration (Agent, Skill, AskUserQuestion, TaskCreate/Update) — [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop).
- Tool permissions: `allowed_tools` auto-approves, `disallowed_tools` blocks, `permission_mode` (default/acceptEdits/plan/dontAsk/auto/bypassPermissions); tool calls denied feed a rejection message back to Claude — [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop).
- Parallel execution: read-only tools (Read/Glob/Grep/MCP read-only) run concurrently; state-modifying tools (Edit/Write/Bash) run sequentially; custom tools default sequential unless `readOnlyHint` set — [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop).
- MCP: servers registered via `mcpServers` (stdio/HTTP/SSE/SDK in-process); tool naming `mcp__<server>__<tool>`; allow via `allowedTools` wildcards; connection timing depends on type and cached tool lists — [MCP in SDK](https://platform.claude.com/docs/en/agent-sdk/mcp).
- Hooks: PreToolUse/PostToolUse/UserPromptSubmit/Stop/SubagentStart/Stop/PreCompact run in the host process (not context), can short-circuit tool calls — [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop).
- Context management: automatic compaction near limit emits `compact_boundary`; subagents get fresh context; tool definitions consume context; MCP tool search defers schemas by default — [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop).
- Effort levels (`low`/`medium`/`high`/`xhigh`/`max`) and budget caps (`max_turns`, `max_budget_usd`) control the loop — [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop).

### Inferences
- The SDK's read-only-vs-stateful parallelism rule mirrors the general advice to run independent read-only operations in parallel and stateful ones sequentially.

### Gaps
- Full hook event list and per-SDK availability differences (TS has more) are referenced but not enumerated here.

## Tool errors, retries, and result formatting

### Takeaway
Anthropic distinguishes tool execution errors (`is_error: true` with instructive messages) from invalid tool names (Claude retries 2–3 times), server tool errors (handled transparently by Claude), and recommends instructive error messages; invalid tool calls can be eliminated with strict mode.

### Cited Findings
- Tool execution error: return error text in `content` with `is_error: true`; Claude incorporates it and may suggest retry; write instructive messages (what went wrong + what to try next) — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
- Invalid tool name/missing params: continue with a `tool_result` indicating the error; Claude retries 2–3 times with corrections before apologizing; eliminate with strict tool use — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
- Server tool errors: Claude handles transparently; web search error codes include `too_many_requests`, `invalid_input`, `max_uses_exceeded`, `query_too_long`, `unavailable` — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
- Tool result `content` supports text, image, document, search_result blocks; computer/browser use member results narrower (text+image, plus optional browser_state for browser) — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
- Empty tool result allowed (omit `content`) — [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
- MCP: protocol errors (JSON-RPC standard) vs tool execution errors (`isError: true`); servers must validate inputs, rate limit, sanitize outputs — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).

### Inferences
- The retry policy (2–3 attempts) is a model-side behavior, not an SDK guarantee; production systems should still implement their own retry/backoff for transient failures.

### Gaps
- No documented exponential backoff or max-retry defaults in the API; SDK retry behavior not verified here.

## Context engineering and tool design

### Takeaway
Context engineering treats the context window as a finite attention budget: curate the smallest high-signal token set; tools must be token-efficient, self-contained, and minimally overlapping; long-horizon tasks need compaction, structured note-taking, and sub-agent architectures.

### Cited Findings
- Context rot: as tokens increase, recall decreases; LLM attention budget is finite; n² pairwise relationships in transformers — [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- System prompts should sit at the "right altitude" between brittle hardcoded logic and vague guidance; organize into sections with XML/Markdown; aim for minimal but sufficient info — [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Tools should promote efficiency: token-efficient returns, encourage efficient agent behavior; minimal viable tool set; avoid overlapping tools; metadata (file paths, naming, timestamps) guides just-in-time retrieval — [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Just-in-time retrieval: maintain lightweight identifiers and load data at runtime via tools (Claude Code uses glob/grep/head/tail); progressive disclosure — [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Long-horizon techniques: compaction (summarize and reinit context), structured note-taking (NOTES.md/todos), sub-agent architectures (clean context windows, return condensed summaries) — [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Tool Search Tool reduces context bloat by deferring tool definitions and loading on demand (85%+ reduction possible) — [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use) and [Tool search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool).
- Prompt caching: deferred tools are stripped from the cached prefix; cache breakpoints can be set on tool definitions — [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#defer_loading-and-prompt-caching).

### Inferences
- For a custom CAD toolkit, the "minimal viable tool set" principle suggests consolidating operations (e.g. a single `create_part` with an `action`/`code` parameter) rather than many micro-tools, and returning only high-signal geometry metadata.

### Gaps
- Optimal compaction prompt tuning is task-specific; no universal recipe provided.

## Agent-computer interface (ACI) concept from SWE-bench

### Takeaway
Anthropic frames tool design as an "agent-computer interface" (ACI) requiring as much effort as HCI: put yourself in the model's shoes, write great docstrings, poka-yoke tools (e.g. require absolute file paths), and invest more in tool optimization than in the overall prompt.

### Cited Findings
- Agents are LLMs using tools based on environmental feedback in a loop; crucial to design toolsets and documentation clearly — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- ACI: "think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good agent-computer interfaces (ACI)" — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- Tool format choices matter: writing diffs vs whole files, JSON vs markdown; keep formats close to what the model has seen in internet text; avoid formatting overhead (accurate line counts, string escaping) — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- SWE-bench example: relative filepaths caused errors after the agent moved out of root; switching to absolute filepaths fixed it — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- Tool design heuristics: give the model enough tokens to think before committing; test in workbench with many examples; iterate on mistakes — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).

### Inferences
- For CAD code generation, requiring absolute output paths and returning structured validation errors (not prose) aligns directly with the ACI poka-yoke principle.

### Gaps
- No quantitative ACI benchmarks beyond SWE-bench task resolution cited.

## Tool discovery and registration (MCP servers)

### Takeaway
Discovery is dynamic: MCP servers expose `tools/list` (paginated, with `listChanged` notifications), Claude Code/SDK defers schemas via tool search, and the Messages API MCP connector fetches server tool lists (with pinning in newer betas); registration requires explicit allowlisting.

### Cited Findings
- MCP discovery: clients send `tools/list` (paginated via cursor); servers notify `notifications/tools/list_changed` when capabilities change; `listChanged` declared in capability — [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools).
- Agent SDK: MCP servers registered via `mcpServers`; tool names namespaced `mcp__<server>__<tool>`; `allowedTools` wildcards auto-approve; connection timing varies (stdio/HTTP/SSE may delay first turn; cached tool lists enable deferred connect) — [MCP in SDK](https://platform.claude.com/docs/en/agent-sdk/mcp).
- Tool search: defer loading with `defer_loading: true`; search variants regex/BM25; server-side `tool_search_tool_*`; at least one non-deferred tool required; up to 10,000 deferred tools — [Tool search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool).
- MCP connector (Messages API): `mcp_servers` array + `mcp_toolset` in `tools`; allowlist/denylist via `enabled`; `defer_loading` per tool; `mcp-client-2026-09-15` beta pins tool lists via `mcp_tool_listing` blocks — [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector).
- Claude Code/SDK MCP tool search is on by default; schemas deferred unless `alwaysLoad: true` — [MCP in SDK](https://platform.claude.com/docs/en/agent-sdk/mcp).

### Inferences
- For a toolkit with many tools, namespacing (`thinktocad_create_part`, `thinktocad_validate_code`) plus deferred loading keeps the context prefix cacheable and improves selection accuracy.

### Gaps
- Exact `listChanged` propagation latency and client re-list behavior in the SDK not specified in fetched docs.

## Patterns for tool design ("Writing tools for agents")

### Takeaway
Anthropic's tool-design principles: choose fewer high-impact tools over API wrappers; namespace by service/resource; return meaningful, token-efficient context; support concise/detailed response formats; optimize error messages; prompt-engineer descriptions; iterate via evaluations with agents.

### Cited Findings
- Choose the right tools: don't just wrap API endpoints; build tools matching high-impact workflows; consolidate operations (`schedule_event` instead of list/create); agents have limited context, so avoid returning all records — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).
- Namespacing: prefix by service/resource (`asana_search`, `asana_projects_search`); prefix vs suffix affects evals — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).
- Return meaningful context: prefer semantic identifiers (names, slugs) over UUIDs; support `response_format` enum (`concise`/`detailed`) to control verbosity; structure (JSON/XML/Markdown) affects performance — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).
- Token efficiency: pagination, range selection, filtering, truncation; default limits (Claude Code restricts tool responses to 25,000 tokens); truncation messages should steer toward efficient strategies — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).
- Prompt-engineer descriptions: treat like docstrings for a junior dev; examples, edge cases, boundaries; precise refinements to SWE-bench tool descriptions dramatically reduced errors — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).
- Evaluation-driven iteration: generate dozens of realistic tasks; run agentic loops; analyze transcripts and metrics (redundant calls, errors); let Claude Code refactor tools; use held-out test sets to avoid overfit — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).
- Tool annotations (MCP) disclose open-world/destructive behavior — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).

### Inferences
- These principles map directly to the ThinkToCad MCP servers: `create_part` should return only artifact paths/ids and validation status, not full code; error results should include the traceback and a suggested fix.

### Gaps
- No published rubric for evaluating tool descriptions; relies on empirical evals.

## Parallel tool calls and streaming

### Takeaway
Claude may emit multiple `tool_use` blocks in one turn; the host chooses concurrency (read-only safe in parallel, stateful sequential), must return all results in a single user message with tool_results first; streaming delivers tool-use blocks incrementally; parallelism can be disabled via `tool_choice.disable_parallel_tool_use`.

### Cited Findings
- Execution semantics: API doesn't prescribe order; host may run concurrently or sequentially; return one `tool_result` per `tool_use`, all in the next user message, matched by `tool_use_id`; put tool_results before text; for skipped calls return `is_error: true` with explanation — [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).
- Computer use/browser use batches are stricter: run sequentially in order, stop at first failure, with specified skip text — [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).
- Claude 4+ makes parallel calls by default when beneficial; maximize via system prompt (`<use_parallel_tool_calls>` block) or user phrasing — [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).
- Disable: `tool_choice: {type: "auto"|"any"|"tool", disable_parallel_tool_use: true}` (not a top-level param); `auto` → at most one call; `any`/`tool` → exactly one call — [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).
- Troubleshooting: separate user messages per result "teach" Claude to avoid parallelism; weak prompting; measure avg tools per message — [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).
- Streaming: `StreamEvent` messages carry raw API deltas; fine-grained input streaming via `eager_input_streaming` on user-defined tools; tool results can include images/documents — [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop) and [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference).
- SDK: read-only tools run concurrently, state-modifying sequentially; custom tools default sequential unless `readOnlyHint` — [Agent loop](https://platform.claude.com/docs/en/agent-sdk/agent-loop).

### Inferences
- For a CAD toolkit, file reads/validations can run in parallel, but code execution/write steps should be sequential to avoid conflicting output directories.

### Gaps
- Streaming protocol specifics (SSE event types, partial JSON deltas) are referenced but the full streaming page was not fetched in this research.
