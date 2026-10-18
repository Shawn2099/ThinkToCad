# Anthropic agent-building guidance (research notes)

## 1. What does Anthropic's "Building effective agents" recommend (workflow vs agent, simplicity-first, five workflow patterns)?

### Takeaway
Anthropic's Dec 2024 post argues the most successful production agentic systems use simple, composable patterns rather than complex frameworks: start with the simplest solution, prefer workflows (predefined code paths) for predictability, use agents only when flexibility and model-driven decisions are needed, and invest heavily in the agent-computer interface (tool docs/tests).

### Cited Findings
- Published Dec 19, 2024 by Erik S. and Barry Zhang; draws on work with dozens of teams. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- "Agent" covers fully autonomous systems and more prescriptive predefined workflows; Anthropic categorizes both as agentic systems but distinguishes **workflows** (LLMs/tools orchestrated through predefined code paths) from **agents** (LLMs dynamically direct their own processes and tool usage). — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- Recommendation: "find the simplest solution possible, and only increasing complexity when needed"; agentic systems trade latency and cost for performance; for many apps, optimizing a single LLM call with retrieval and in-context examples is enough. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- Frameworks (Claude Agent SDK, Strands, Rivet, Vellum) simplify low-level tasks but add abstraction that obscures prompts/responses and tempts over-complexity; start with LLM APIs directly and understand underlying code. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- Foundational building block is the **augmented LLM** (retrieval, tools, memory); Anthropic's Model Context Protocol (MCP) is one way to integrate third-party tools via a client implementation. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- **Prompt chaining**: sequence of LLM calls where each processes the previous output; add programmatic gates; use when task decomposes into fixed subtasks; trades latency for accuracy. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- **Routing**: classify input and direct to a specialized followup task/prompt/model; use for distinct categories; example: easy questions to Claude Haiku 4.5, hard to Claude Sonnet 4.5. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- **Parallelization**: sectioning (independent subtasks in parallel) or voting (same task multiple times); use for speed or higher confidence. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- **Orchestrator-workers**: central LLM dynamically breaks down tasks, delegates to workers, synthesizes; use when subtasks can't be predicted (e.g., multi-file code changes, multi-source search). — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- **Evaluator-optimizer**: one LLM generates, another evaluates/feedback in a loop; use when clear evaluation criteria and iterative refinement help (e.g., literary translation, complex search). — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- **Agents**: LLMs using tools based on environmental feedback in a loop; gain ground truth each step; can pause for human feedback; include stopping conditions; autonomous nature means higher cost and compounding errors; test in sandboxes with guardrails. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- Core principles: (1) maintain simplicity, (2) prioritize transparency by showing planning steps, (3) carefully craft the agent-computer interface (ACI) through tool documentation and testing. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- Appendix 2 (tool prompt engineering): choose formats the model writes easily (close to natural internet text, no formatting overhead); give tokens to think; poka-yoke arguments; require absolute filepaths example fixed SWE-bench errors. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- Agents in practice: customer support (conversation + tools + measurable resolution) and coding agents (verifiable via tests). — [Source](https://www.anthropic.com/engineering/building-effective-agents)

### Inferences
- The post treats "agent" as an architectural extreme (model-driven loop), not a binary; most real systems are workflows with selective autonomy.
- Tool design is positioned as equal-or-greater effort than prompt design for agent reliability.

### Gaps
- The post is dated Dec 2024 and notes tooling landscape has changed; current approach references Claude Managed Agents docs, which I did not fetch in depth. — [Source](https://www.anthropic.com/engineering/building-effective-agents)

## 2. What is the Claude Agent SDK (Python/TypeScript)? Core abstractions and how it works?

### Takeaway
The Claude Agent SDK is "Claude Code as a library": Python (`claude-agent-sdk`, Py 3.10+) and TypeScript (`@anthropic-ai/claude-agent-sdk`) packages that run a bundled Claude Code CLI over stdio and expose the same agent loop, built-in tools, context management, permissions, sessions, hooks, subagents, skills, and MCP support.

### Cited Findings
- Renamed from "Claude Code SDK" in Sept 2025; available as `claude-agent-sdk` (Python) and `@anthropic-ai/claude-agent-sdk` (TypeScript). — [Source](https://www.ksred.com/the-claude-agent-sdk-what-it-is-and-why-its-worth-understanding)
- Python install: `pip install claude-agent-sdk`; requires Python 3.10+; CLI bundled in wheel, no separate install. — [Source](https://github.com/anthropics/claude-agent-sdk-python)
- Core entry point `query()` is an async function returning an `AsyncIterator` of response messages (`AssistantMessage`, `UserMessage`, `SystemMessage`, `ResultMessage`) with content blocks `TextBlock`, `ToolUseBlock`, `ToolResultBlock`. — [Source](https://github.com/anthropics/claude-agent-sdk-python)
- `ClaudeSDKClient` supports bidirectional interactive conversations and additionally enables custom tools and hooks. — [Source](https://github.com/anthropics/claude-agent-sdk-python)
- Configuration via `ClaudeAgentOptions`: `system_prompt`, `max_turns`, `allowed_tools` (permission allowlist auto-approving; does not remove tools), `disallowed_tools`, `permission_mode`, `cwd`, `mcp_servers`, `hooks`. — [Source](https://github.com/anthropics/claude-agent-sdk-python)
- Built-in tools are the Claude Code toolset (Read, Write, Edit, Bash, etc.); `allowed_tools` auto-approves listed tools, unlisted fall through to permission mode/`can_use_tool`. — [Source](https://github.com/anthropics/claude-agent-sdk-python)
- Custom tools are Python functions decorated with `@tool(name, description, schema)` and registered via `create_sdk_mcp_server(name, version, tools=[...])`, running as in-process MCP servers (no subprocess, lower overhead, easier debugging). — [Source](https://github.com/anthropics/claude-agent-sdk-python)
- Hooks are Python functions the Claude Code application (not Claude) invokes at lifecycle points; configured via `HookMatcher(matcher=..., hooks=[...])` under `hooks={"PreToolUse": [...]}`; used for deterministic processing/feedback (e.g., deny Bash commands). — [Source](https://github.com/anthropics/claude-agent-sdk-python)
- Capabilities listed by docs: built-in tools, hooks, subagents, MCP, permissions, sessions, skills/commands/memory, plugins. — [Source](https://platform.claude.com/docs/en/agent-sdk/overview)
- System prompt default builds on first request and is reused (including after resume); set `snapshot=False` in `{"type":"custom","prompt":...}` or `{"type":"preset",...}` to rebuild each request (requires CLI 2.1.257+). — [Source](https://github.com/anthropics/claude-agent-sdk-python)
- Error types: `ClaudeSDKError`, `CLINotFoundError`, `CLIConnectionError`, `ProcessError`, `ResultError` (terminal error result), `CLIJSONDecodeError`. — [Source](https://github.com/anthropics/claude-agent-sdk-python)
- Auth note: Anthropic does not allow third-party devs to offer claude.ai login/rate limits for SDK-built products; use API key auth. — [Source](https://platform.claude.com/docs/en/agent-sdk/overview)
- Distinction: Client SDKs (`anthropic`) call the Messages API directly and you write the tool loop; Agent SDK runs Claude Code binary with built-in loop/tools/context. — [Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)

### Inferences
- The SDK is optimized for coding-style agents (file/bash/search) but extensible to any tool via MCP; in-process MCP servers are the recommended path for custom Python tools.

### Gaps
- I did not fetch the full Python/TS API reference pages or subagents/sessions/hooks deep-dive docs; details beyond README/docs overview (e.g., exact session resume/fork APIs) are not captured. — [Source](https://platform.claude.com/docs/en/agent-sdk/python)

## 3. What are Claude's agentic primitives (tool use, extended thinking, context editing, memory tool, bash/file tools, computer use)?

### Takeaway
Claude's primitives split into client tools (your app executes: user-defined tools, Memory, Bash, Text editor, Computer use, Browser use) and server tools (Anthropic executes: web search, web fetch, code execution, advisor, tool search, MCP connector), plus model-level extended thinking and context-management features (compaction, tool-result clearing, memory tool).

### Cited Findings
- Tool use (function calling): Claude decides when to call based on request and tool description; returns `tool_use` blocks; client tools yield `stop_reason: "tool_use"` and you return `tool_result`; server tools run on Anthropic infra. Default `tool_choice` `{"type":"auto"}`; can force with `any`/`tool`; `strict: true` guarantees schema conformance. — [Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- Anthropic-schema client tools: **Memory tool** (store/retrieve info across conversations in files you control), **Bash tool** (shell commands in persistent session), **Text editor tool** (view/modify text files), **Computer use tool** (screenshots + mouse/keyboard control), **Browser use tool** (navigate/read/interact with webpages). — [Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- Server tools: web search, web fetch, code execution (sandboxed Python/bash + file generation), advisor (fast executor consults higher-intelligence advisor), tool search (discover/load tools on demand), MCP connector. — [Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- Tool Runner (SDK) executes your tools and sends results back automatically, avoiding manual round trips. — [Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- Tool use adds system prompt tokens (e.g., ~286-675 tokens depending on model and tool_choice) plus tokens from tool definitions/calls/results. — [Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- Extended thinking: Claude outputs additional visible thinking tokens; in multi-agent research, lead agent uses thinking to plan and subagents use interleaved thinking after tool results to evaluate quality/gaps; improved instruction-following, reasoning, efficiency. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)
- Context editing / management: compaction (summarize nearing-limit history and restart with summary), tool result clearing (remove raw tool results deep in history), structured note-taking/agentic memory, sub-agent architectures; "context management" launched as Claude Developer Platform feature. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Memory tool: file-based system to store/consult info outside context window; lets agents build knowledge bases over time and maintain project state across sessions. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### Inferences
- Anthropic increasingly ships "server tools" (Anthropic executes) to reduce client boilerplate, while client tools remain for environment-specific actions (files, bash, desktop).

### Gaps
- I did not fetch dedicated docs for extended thinking API params (budget_tokens, interleaved thinking beta headers) or context editing endpoints; exact request shapes are not captured here. — [Source](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)

## 4. How does Anthropic think about multi-agent architectures ("How we built our multi-agent research system")?

### Takeaway
Anthropic's research system uses an orchestrator-worker pattern: a lead agent (Claude Opus 4) plans and saves its plan to memory, spawns parallel subagents (Claude Sonnet 4) that search with interleaved thinking, synthesizes results, optionally iterates, then hands off to a CitationAgent; it beat single-agent Opus 4 by 90.2% on internal research eval but burns ~15x chat tokens.

### Cited Findings
- Multi-agent systems excel for breadth-first queries pursuing multiple independent directions; multi-agent (Opus 4 lead + Sonnet 4 subagents) outperformed single-agent Opus 4 by 90.2% on internal research eval. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)
- Token usage explains 80% of BrowseComp performance variance; multi-agent ~15x tokens vs chats, single agents ~4x. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)
- Architecture: LeadResearcher analyzes query, develops strategy, saves plan to Memory (because context >200k tokens gets truncated), creates specialized Subagents; each subagent performs web searches, evaluates results via interleaved thinking, returns findings; LeadResearcher synthesizes and decides whether more research needed; final pass to CitationAgent for source attribution. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)
- Prompting principles: (1) think like your agents (simulate in Console), (2) teach orchestrator to delegate with objective/output format/tools/boundaries, (3) scale effort to query complexity (simple: 1 agent 3-10 calls; complex: >10 subagents), (4) tool design/selection critical, (5) let agents improve themselves (tool-testing agent rewrote descriptions, 40% faster), (6) start wide then narrow, (7) guide thinking process (extended/interleaved thinking), (8) parallel tool calling cuts research time up to 90%. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)
- Evaluation: start with ~20 real queries; LLM-as-judge with rubric (factual accuracy, citation accuracy, completeness, source quality, tool efficiency) scoring 0.0-1.0 with pass/fail; human evaluation catches edge cases (e.g., SEO content farms vs authoritative sources). — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)
- Production challenges: agents stateful and errors compound; durable execution + resume from checkpoints; combine AI adaptability with deterministic safeguards (retries/checkpoints); full production tracing; rainbow deployments to avoid breaking running agents; synchronous execution creates bottlenecks; observability without reading individual conversations. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)
- Appendix tips: end-state evaluation for state-mutating agents; long-horizon conversation management via summarization + external memory + fresh subagents with handoffs; subagent outputs to filesystem to minimize "telephone" game. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)

### Inferences
- Anthropic's stance (vs Cognition's "don't build multi-agents") is that multi-agent pays off for high-value, parallelizable, breadth-first research, not for tightly coupled coding tasks.

### Gaps
- Costs/latency figures are internal and model-specific (Opus 4/Sonnet 4 era); newer model economics may differ. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)

## 5. What is "context engineering" and why does Anthropic emphasize it over prompt engineering? How should one manage context in an agent loop?

### Takeaway
Context engineering is the iterative curation of the optimal set of tokens (system instructions, tools, MCP, external data, message history) at each inference step; Anthropic frames it as the successor to prompt engineering because agents run long loops where context, not a single prompt, determines behavior, and LLM attention degrades as context grows (context rot).

### Cited Findings
- Published Sep 29, 2025 by Anthropic Applied AI team. Prompt engineering = writing/organizing LLM instructions; context engineering = curating/maintaining optimal tokens during inference, including everything outside prompts. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Context is finite with diminishing returns; transformer attention is n² pairwise; longer contexts reduce recall (context rot). — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- System prompts should hit the "right altitude" between brittle hardcoded logic and vague guidance; organize into sections (XML/Markdown); minimal but sufficient. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Tools must be token-efficient and self-contained; avoid bloated/overlapping tool sets; curate minimal viable tool set. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Few-shot: use diverse canonical examples, not laundry lists of edge cases. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Just-in-time retrieval: agents keep lightweight identifiers (paths, queries, links) and load data at runtime via tools; progressive disclosure; hybrid (some up-front + autonomous exploration). Claude Code uses CLAUDE.md up front + glob/grep just-in-time. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Long-horizon techniques: **Compaction** (summarize nearing-limit history, restart with summary; Claude Code keeps 5 most recently accessed files), **structured note-taking/agentic memory** (NOTES.md/TODOs; Claude Pokémon example), **sub-agent architectures** (isolated context windows, return 1k-2k token summaries). — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Memory tool (public beta): file-based storage/consultation outside context window; build knowledge bases over time, maintain project state across sessions. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Choice depends on task: compaction for back-and-forth, note-taking for iterative milestones, multi-agent for parallel research. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### Inferences
- Anthropic's practical rule: "do the simplest thing that works"; smarter models need less prescriptive engineering, but context remains a precious resource.

### Gaps
- Compaction prompt tuning guidance is high-level (maximize recall then precision); exact compaction APIs/params not detailed in the post. — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## 6. What is the Model Context Protocol (MCP)? Design and promotion? Server/client?

### Takeaway
MCP is an open standard (JSON-RPC 2.0) for connecting AI apps to external systems, promoted by Anthropic as "USB-C for AI": a host creates one client per server; servers expose tools/resources/prompts; clients may expose elicitation; transports are stdio (local) and streamable HTTP (remote, OAuth recommended).

### Cited Findings
- MCP is an open-source standard for connecting AI applications to external systems (data sources, tools, workflows); supported across clients (Claude, ChatGPT, VS Code, Cursor, etc.). — [Source](https://modelcontextprotocol.io/introduction)
- Participants: **MCP Host** (AI app coordinating clients), **MCP Client** (maintains connection, obtains context), **MCP Server** (provides context). One client per server; local stdio servers typically serve one client, remote streamable HTTP servers serve many. — [Source](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- Layers: data layer (JSON-RPC 2.0, discovery, primitives, notifications) and transport layer (stdio, streamable HTTP). — [Source](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- Server primitives: **Tools** (executable functions), **Resources** (context data), **Prompts** (reusable templates). Client primitives: **Elicitation** (request user input); **Sampling** and **Logging** are deprecated as of 2026-07-28. — [Source](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- Protocol is stateless: every request carries protocol version + capabilities in `_meta`; clients may call `server/discover`; tools discovered via `tools/list`, executed via `tools/call`; change notifications via `subscriptions/listen` (opt-in). — [Source](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- Scope includes spec, SDKs (multiple languages), MCP Inspector, reference server implementations. — [Source](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- Anthropic's "Building effective agents" recommends MCP for integrating with a growing ecosystem of third-party tools via a simple client implementation. — [Source](https://www.anthropic.com/engineering/building-effective-agents)
- Anthropic's multi-agent research post notes MCP servers can give models access to external tools, and bad tool descriptions can send agents down wrong paths; gave agents heuristics to examine all tools first. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)

### Inferences
- MCP is positioned as the protocol layer of Anthropic's three-layer stack (MCP protocol, Agent Skills, Agent SDK runtime); Claude Agent SDK has MCP support built in (in-process SDK servers + external servers).

### Gaps
- I fetched the 2026-07-28 doc version; protocol details may differ in earlier versions. OAuth/security specifics and SDK APIs not deeply captured. — [Source](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)

## 7. What guidance exists on evaluation, prompt caching, and reducing latency/cost in agent systems?

### Takeaway
Anthropic's guidance emphasizes starting evals small and early, using LLM-as-judge with rubrics plus human eval, and optimizing latency/cost via parallel tool calling, prompt caching (5-min default / 1-hour option, ~0.1x read cost), context compaction, token-efficient tool design, and scaling effort to query complexity.

### Cited Findings
- Evaluation (multi-agent research): start immediately with ~20 real queries; LLM-as-judge single call scoring 0.0-1.0 with pass/fail across factual accuracy, citation accuracy, completeness, source quality, tool efficiency; human eval catches edge cases. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)
- Tool evals (writing tools post): generate dozens of realistic multi-step tasks; run simple agentic while-loops; collect metrics (runtime, tool calls, tokens, errors); analyze transcripts; let Claude Code refactor tools; held-out test sets to avoid overfitting; tool description tweaks yielded big gains (e.g., SWE-bench). — [Source](https://www.anthropic.com/engineering/writing-tools-for-agents)
- Prompt caching: two modes—automatic (top-level `cache_control`) and explicit breakpoints (up to 4); cache prefix order tools → system → messages; default 5-min TTL (refreshed free on use), optional 1-hour at 2x base; cache writes 1.25x (5m) / 2x (1h); cache reads 0.1x base (model-specific exceptions); minimum cacheable prompt length varies by model (e.g., 1024-4096 tokens). — [Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- Caching lookback window is 20 blocks per breakpoint; place `cache_control` on last block whose prefix is identical across requests; tool definitions/system/messages changes invalidate downstream caches. — [Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- Automatic caching moves breakpoint forward as conversations grow; compatible with explicit breakpoints (uses one slot). — [Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- Latency/cost reductions: parallel tool calling (lead spins 3-5 subagents; subagents use 3+ tools in parallel) cut research time up to 90%; scale effort to query complexity; tool result clearing and compaction reduce context; token-efficient tool responses (pagination/truncation/filters, concise vs detailed formats). — [Source](https://www.anthropic.com/engineering/multi-agent-research-system) — [Source](https://www.anthropic.com/engineering/writing-tools-for-agents) — [Source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Multi-agent token economics: agents ~4x chat tokens, multi-agent ~15x; use only when task value justifies cost. — [Source](https://www.anthropic.com/engineering/multi-agent-research-system)

### Inferences
- Anthropic's eval philosophy favors outcome-based, flexible evaluation over rigid step matching because agents can take different valid paths.

### Gaps
- I did not fetch dedicated latency/cost tuning docs (e.g., batching, streaming, fast mode details) beyond prompt caching and parallelization; those specifics are not captured. — [Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)