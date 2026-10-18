# Production-Grade Concerns, Interoperability Protocols, and Evaluation for a Custom Python Agent Framework

## 1. Interoperability Protocols: MCP, A2A, and an OpenAI-Compatible Surface

### Takeaway
A production Python agent framework should treat MCP as its tool/resource/prompt plane (JSON-RPC over stdio or Streamable HTTP, with a Python SDK on both client and server), A2A as its agent-to-agent delegation plane (HTTP(S) JSON-RPC 2.0 with SSE streaming and a task lifecycle), and expose an OpenAI-compatible `/v1/chat/completions` (and optionally Responses) HTTP front door so existing clients, SDKs, and routers work unchanged.

### Cited Findings
- MCP messages MUST follow JSON-RPC 2.0, are UTF-8 encoded, and the protocol defines two standard transports: stdio (client launches server as subprocess, newline-delimited messages on stdin/stdout, server may write logs to stderr) and Streamable HTTP (single MCP endpoint supporting POST and GET, optional SSE streaming, session id via `Mcp-Session-Id` header). — [MCP Transports spec 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)
- Streamable HTTP was introduced in protocol version 2025-03-26 replacing HTTP+SSE; revision 2026-07-28 removed the GET stream endpoint, so clients must handle backwards compatibility. — [MCP Streamable HTTP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- MCP's base protocol defines Requests (with non-null string/integer id), Responses (result xor error), and Notifications (no id); all implementations MUST support base protocol and lifecycle management, while Resources/Prompts/Tools are optional server features. — [MCP base protocol overview](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
- MCP authorization applies to HTTP transports (SHOULD conform); stdio transports SHOULD NOT follow it and instead retrieve credentials from the environment. — [MCP base protocol overview](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
- The MCP Python SDK exposes `stdio_server`, SSE, and `streamable_http`/`streamable_http_manager` transports, plus `TransportContext` carrying `kind`, `can_send_request`, and request `headers` for each inbound message. — [MCP Python SDK stdio](https://py.sdk.modelcontextprotocol.io/api/mcp/server/stdio); [MCP Python SDK transport_context](https://py.sdk.modelcontextprotocol.io/api/mcp/shared/transport_context)
- The Python SDK's Streamable HTTP server supports `EventStore` for resumability via event storage, `Mcp-Session-Id`, `security_settings`, and `idle_timeout`. — [python-sdk streamable_http.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/streamable_http.py)
- A2A communication MUST occur over HTTP(S), with the server at a URL in its AgentCard; it uses JSON-RPC 2.0 payloads (Content-Type `application/json`) and SSE for streaming methods (`message/stream`, `tasks/resubscribe`). — [A2A spec v0.2.6](https://a2a-protocol.org/v0.2.6/specification/)
- An AgentCard is a JSON document at `https://{domain}/.well-known/agent.json` (RFC 8615) declaring `protocolVersion`, `name`, `description`, `url`, `capabilities` (streaming, pushNotifications, stateTransitionHistory), `securitySchemes`/`security`, `defaultInputModes`/`defaultOutputModes`, and `skills` (id, name, description, tags, examples, input/output modes); cards with sensitive data must be access-controlled. — [A2A spec v0.2.6 §5](https://a2a-protocol.org/v0.2.6/specification/)
- A2A Task lifecycle states: `submitted`, `working`, `input-required`, `completed`, `canceled`, `failed`, `rejected`, `auth-required`, `unknown`; tasks in terminal states cannot be restarted; multiple tasks can share a `contextId`; artifacts carry `Part` (TextPart/FilePart/DataPart). — [A2A spec v0.2.6 §6.1–6.3](https://a2a-protocol.org/v0.2.6/specification/); [agent2agent.info task concept](https://agent2agent.info/docs/concepts/task/)
- A2A RPC methods: `message/send` (returns Task or Message), `message/stream` (SSE), `tasks/get`, `tasks/cancel`, `tasks/pushNotificationConfig/set|get|list|delete`, `tasks/resubscribe`, `agent/authenticatedExtendedCard`; push notifications deliver async updates to client webhooks. — [A2A spec v0.2.6 §7](https://a2a-protocol.org/v0.2.6/specification/)
- A2A treats agents as standard enterprise apps: identity at HTTP layer (TLS 1.3+ recommended), credentials out-of-band, least privilege, `auth-required` task state for secondary credentials, and OAuth/OpenID Connect security schemes mirroring OpenAPI. — [A2A spec v0.2.6 §4](https://a2a-protocol.org/v0.2.6/specification/)
- A2A's appendix explicitly documents its relationship to MCP: MCP gives agents tools/data; A2A gives agents to agents. — [A2A spec v0.2.6 §10.1](https://a2a-protocol.org/v0.2.6/specification/) (per TOC; content not fully extracted)

### Inferences
- A custom framework should keep three planes separate: (a) MCP client for consuming tools/resources/prompts from any MCP server and MCP server for exposing its own tools; (b) A2A server/client for delegating to remote agents and receiving delegated tasks; (c) an OpenAI-compatible HTTP API for end users and for interoperability with gateways (LiteLLM, OpenRouter, vLLM).
- AgentCard `skills` map naturally to a framework's registered "agent capabilities," and `contextId`/`taskId` map to a framework's thread/run identifiers, so an A2A adapter can be a thin shim over the internal run model.
- MCP's optional `EventStore` and session id give a ready-made resumability hook for long-running tool calls; a framework can reuse it rather than inventing its own replay log.
- Providing `/v1/chat/completions` with `tools`/`tool_choice`, streaming SSE, and JSON mode lets the framework plug into OpenAI SDKs, eval harnesses, and routers with no client changes.

### Gaps
- The exact OpenAI Responses API schema and current function-calling JSON schema details were not fetched from primary docs in this pass; treat OpenAI platform docs as the authority for `/v1/responses` and tool schema.
- I did not verify the current A2A Python SDK package name/API; the spec's gRPC/REST variants suggest multiple transports, but Python SDK maturity should be checked before committing.
- MCP auth spec details (OAuth 2.1 flow) were referenced but not fully extracted; consult the MCP authorization page for scopes/PKCE specifics.

## 2. Observability and Tracing

### Takeaway
Trace every agent run as an OpenTelemetry trace tree: a top-level `invoke_agent` span with child `chat`/inference spans for each LLM call and `execute_tool` spans for each tool invocation, carrying `gen_ai.*` attributes (model, token usage, finish reasons) and opt-in prompt/completion content, exported to any OTLP backend (Langfuse, Braintrust, LangSmith, Jaeger).

### Cited Findings
- OpenTelemetry GenAI semantic conventions define agent spans with operations `create_agent`, `invoke_agent`, `invoke_workflow`, and `plan`, plus `execute_tool`; inference spans use `{gen_ai.operation.name} {gen_ai.request.model}` naming. — [OTel GenAI agent spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md); [OTel GenAI spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/63f8200eee093730ce845d26ce2aafb621b0807e/docs/gen-ai/gen-ai-spans.md)
- GenAI span attributes include `gen_ai.request.model`, `gen_ai.response.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.response.finish_reasons`, `gen_ai.conversation.id`, `gen_ai.tool.name`, `gen_ai.tool.type`, `gen_ai.tool.definitions`, and cache token counts `gen_ai.usage.cache_read.input_tokens` / `gen_ai.usage.cache_creation.input_tokens`. — [OTel GenAI attributes registry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
- Content capture (prompts, completions, tool args/results) is opt-in because it may contain sensitive data; default captures only metadata (model, tokens, duration); content is recorded as `gen_ai.system_instructions`, `gen_ai.input.messages`, `gen_ai.output.messages`. — [OTel blog: GenAI observability](https://opentelemetry.io/blog/2026/genai-observability/)
- The span tree shape in practice: top-level `invoke_agent` span with child `chat` spans per LLM call and `execute_tool` spans per tool invocation; OTel GenAI visualizers render these as a chat-style view. — [OTel blog: GenAI observability](https://opentelemetry.io/blog/2026/genai-observability/)
- Frameworks publish to vendor backends: LangSmith provides tracing + trajectory evals; Langfuse provides tracing/monitoring; Braintrust and Arize/Galileo/Patronus are cited as eval/observability platforms in the agent eval survey. — [Survey on Evaluation of LLM-based Agents](https://arxiv.org/html/2503.16416v1)
- OpenTelemetry GenAI conventions are Status: Development and have moved out of the core semconv repo into `open-telemetry/semantic-conventions-genai`; attribute stability is not yet final. — [OTel GenAI spans (moved)](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/?ref=blog.aibox.today)

### Inferences
- A custom tracer should record at minimum: run/trace id, agent name/version, conversation id, model + provider, per-call token usage (input/output/reasoning/cache read-write), latency, finish reason, tool name + args + result + duration, errors/exceptions, and (opt-in, redacted) message content.
- Because conventions are still "Development," pin to a specific semconv version and make attribute names configurable so backend dashboards don't break on upgrades.
- Recording tool calls as first-class spans (not just log lines) is what enables trajectory evaluation and failure attribution later.
- Cost should be computed from token usage × price table in the tracer itself, not delegated to a backend, so spend caps can be enforced inline.

### Gaps
- Exact Braintrust/Langfuse SDK ingestion APIs and pricing were not fetched; OTLP export is the safest common denominator.
- No primary source in this pass specified a standard for recording "agent turn" vs "LLM call" nesting beyond the GenAI semconv; frameworks differ (LangGraph uses task/checkpoint events).

## 3. Evaluation of Agents

### Takeaway
Evaluate agents at three levels — final task success, trajectory (tool selection/order/efficiency), and stepwise/LLM-as-judge — using deterministic task-success metrics where possible and LLM-as-judge (preferably agent-as-judge with trajectory access) for nuanced quality, run offline in CI as regression tests and online in production with sampling.

### Cited Findings
- Eval platforms: LangSmith (stepwise + trajectory + HITL + A/B), Langfuse (stepwise, no trajectory match in the survey's table), Google Vertex AI (trajectory), Arize, Galileo, Patronus, AgentEvals, Databricks Mosaic AI, AutoGen. — [Survey on Evaluation of LLM-based Agents](https://arxiv.org/html/2503.16416v1)
- LangSmith AgentEvals supports trajectory match (exact/unordered/subset/superset) and LLM-as-judge over the trajectory, with or without a reference trajectory. — [LangSmith trajectory evals docs](https://docs.langchain.com/langsmith/trajectory-evals)
- τ-bench compares final DB state; AgentBench/WebArena score task success; AgentBoard tracks subgoal progress; newer work scores reasoning trajectories directly. — [trajectory-judge paper](https://arxiv.org/abs/2609.00038)
- Outcome-only LLM judges are structurally blind to agents that reach the right answer the wrong way; paired discrimination against clean parent trajectories and splitting by outcome survival are recommended reporting. — [trajectory-judge paper](https://arxiv.org/abs/2609.00038)
- Agent-as-a-Judge evaluates the whole trajectory and outperformed output-only LLM-as-judge on code tasks, reaching parity with human evaluators; cost is high (tens of minutes per task). — [When AIs Judge AIs](https://arxiv.org/html/2508.02994v1)
- Auto-Eval Judge decomposes tasks into sub-tasks and validates each step, achieving 4.76% and 10.52% higher alignment with human judgments than GPT-4o LLM-as-a-judge on GAIA/BigCodeBench. — [Auto-Eval Judge](https://arxiv.org/pdf/2508.05508)
- A practical eval harness scores four metrics: task success, tool-call accuracy (precision/recall/F1 over the multiset vs reference trace), step efficiency (optimal/actual steps), and cost per task. — [agent-eval-harness](https://github.com/tkarim45/agent-eval-harness)
- Unified evaluation frameworks persist structured trajectories, intermediate states, and artifacts so custom metrics can be added without re-running the agent; they report task completion score via deterministic rule matching or LLM judge, plus environment-state comparison via hash matching of terminal state. — [Unified Framework for Evaluating LLM Agentic Capabilities](https://arxiv.org/html/2605.27898v2)

### Inferences
- A custom framework should ship an eval harness with: a dataset format (task input + expected final answer + reference tool trace + optimal step count), deterministic scorers (success, tool F1, step efficiency, cost), and pluggable LLM/agent judges.
- Trajectory capture must be a first-class artifact of every run (the same spans from §2), so offline eval can replay/re-score without re-running the agent.
- Regression testing = pinned datasets + thresholds on success rate/tool F1/cost, gated in CI; online eval = sampled production traces scored by a judge with human review queues.
- Prefer deterministic environment-state checks (hash of terminal state) over output string matching when tools mutate state.

### Gaps
- No single standard eval dataset schema exists; AgentBench/τ-bench/BFCL are benchmarks, not a framework schema — the framework must define its own.
- Human-in-the-loop eval calibration (LLM-human agreement) was reported in the unified framework paper but methodology details not extracted.

## 4. Guardrails and Safety

### Takeaway
Layer guardrails: validate/sanitize inputs and outputs, defend against direct and indirect prompt injection (knowing all such defenses are probabilistic), enforce tool allow/deny lists and least privilege, redact PII, require human approval for high-risk actions, and sandbox tool execution; treat prompt injection as a property to manage, not a bug to fix.

### Cited Findings
- OWASP Top 10 for LLM Applications 2025 ranks Prompt Injection (LLM01) #1 for the second consecutive year; other risks include Sensitive Information Disclosure (LLM02), Supply Chain (LLM03), Data/Model Poisoning (LLM04), Improper Output Handling (LLM05), Excessive Agency (LLM06), System Prompt Leakage (LLM07), Vector/Embedding Weaknesses (LLM08), Misinformation (LLM09), Unbounded Consumption (LLM10). — [OWASP Top 10 for LLMs 2025](https://genai.owasp.org/llm-top-10/); [OWASP PDF](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)
- Direct prompt injection: user input alters model behavior; indirect injection: malicious instructions embedded in external content (retrieved docs, tool results) alter behavior; multimodal injection possible via images. — [OWASP Top 10 for LLMs 2025 PDF](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)
- OWASP recommends: identify untrusted content from every channel (retrieved docs, tool results, history) and keep it separate from trusted instructions; apply semantic filters and string checks; evaluate responses with the RAG Triad (context relevance, groundedness, Q/A relevance); enforce least privilege; human-in-the-loop for high-risk actions. — [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html); [OWASP PDF](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)
- Guardrails are probabilistic: researchers consistently find bypasses within weeks of new guardrails; Cisco argues prompt injection cannot be parameterized like SQL, so defenses reduce attack surface but must be paired with containment (least privilege, sandboxing, audit). — [Cisco blog 2026-03-09](https://blogs.cisco.com/ai/prompt-injection-is-the-new-sql-injection-and-guardrails-arent-enough)
- Empirical study bypassed six prominent guardrail systems (Azure Prompt Shield, Meta Prompt Guard) with up to 100% evasion using character injection and adversarial ML. — [Hackett et al. LLMSEC 2025](https://aclanthology.org/2025.llmsec-1.8/)
- Simon Willison's "Dual LLM Pattern" is cited by OWASP as a mitigation for prompt injection. — [OWASP PDF](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)

### Inferences
- A framework should expose guardrail hooks as a pipeline: pre-model input filters, tool-call policy (allow/deny lists, argument schema validation), post-model output filters (PII redaction, toxicity, format), and human-approval gates before destructive tools.
- Keep untrusted content (tool results, retrieved docs) in separate message roles/sections and never concatenate into the system prompt; mark provenance.
- Treat guardrail bypass as expected: enforce least privilege on tool scopes, sandbox execution, and log everything for forensics (ties to §2 tracing).
- PII redaction should run on both inputs (before logging) and outputs (before returning to user), with configurable entity types.

### Gaps
- No primary source in this pass provided a concrete, framework-agnostic guardrail API/schema; OWASP gives principles, not interfaces. Vendor SDKs (NeMo Guardrails, Llama Guard) would need separate evaluation.
- Quantified guardrail efficacy numbers beyond the bypass study were not found.

## 5. Security

### Takeaway
Apply standard web security to agent endpoints (TLS, auth at HTTP layer, least privilege), scope tool permissions per agent/run, sandbox filesystem/network access (SSRF and path traversal defenses), manage secrets via environment/secret stores (never in AgentCards or prompts), enforce rate limits and token/spend caps, and cache safely.

### Cited Findings
- A2A: production MUST use HTTPS, TLS 1.3+ recommended; auth at HTTP layer; credentials out-of-band; least privilege by skill; `auth-required` for secondary creds; cards with sensitive data must be access-controlled; avoid plaintext secrets in cards. — [A2A spec v0.2.6 §4–5](https://a2a-protocol.org/v0.2.6/specification/)
- MCP: stdio transports retrieve credentials from environment; HTTP transports SHOULD conform to MCP authorization; tool descriptions containing internal details (e.g., DB type) can enable targeted attacks. — [MCP base protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic/index); [OWASP PDF](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)
- OWASP LLM06 Excessive Agency and LLM05 Improper Output Handling: insufficient validation/sanitization of LLM outputs can lead to downstream exploits including SSRF, privilege escalation, RCE in backend systems. — [OWASP Top 10 for LLMs 2025](https://genai.owasp.org/llm-top-10/)
- OWASP LLM10 Unbounded Consumption: resource-heavy operations can cause service disruption and cost blowup; mitigation includes rate limiting, token budgets, timeouts. — [OWASP Top 10 for LLMs 2025](https://genai.owasp.org/llm-top-10/)
- Prompt caching can cut token cost 41–80% but requires stable prefixes; dynamic content (timestamps, user info) in system prompts busts cache. — [Don't Break the Cache paper](https://arxiv.org/html/2601.06007); [OpenAI prompt caching docs](https://developers.openai.com/api/docs/guides/prompt-caching?model=gpt-6-astra)

### Inferences
- A framework should support a per-run budget object: max tokens, max tool calls, max wall-clock time, max spend USD; enforced in the agent loop and in the tracer.
- Tool execution should run in a sandbox with an allowlist of network hosts, filesystem paths, and environment variables; SSRF defenses (block private IPs, metadata endpoints) and path canonicalization are mandatory for any tool that fetches URLs or reads files.
- Secrets should be injected at tool-runtime via a secret resolver, never serialized into prompts, traces (redact), or AgentCards.
- Rate limiting should be per-tenant and per-tool, with backpressure surfaced to the agent as a retryable error rather than a crash.

### Gaps
- No primary source in this pass quantified recommended rate-limit thresholds or sandbox implementation details; these are deployment-specific.
- Secret-management integration patterns (Vault, cloud KMS) were not covered by the sources gathered.

## 6. Reliability

### Takeaway
Design the agent loop as a durable, resumable workflow: persist checkpoints per step, make side effects idempotent with idempotency keys, retry transient failures with backoff and timeouts, support human-in-the-loop interrupts, and use a task queue to decouple request handling from execution.

### Cited Findings
- LangGraph durable execution: requires a checkpointer (state persisted per super-step) and a thread id; resume does not restart from the same line but from an appropriate starting point; non-deterministic/side-effecting ops must be wrapped in tasks/nodes; durability modes `exit`/`async`/`sync`. — [LangGraph durable execution docs](https://docs.langchain.com/oss/python/langgraph/durable-execution)
- LangGraph: idempotent operations are critical; use idempotency keys or verify existing results to avoid duplication on retry. — [LangGraph durable execution docs](https://docs.langchain.com/oss/python/langgraph/durable-execution)
- LangGraph design rationale lists the production features an agent runtime needs: parallelization, streaming, task queue, checkpointing, human-in-the-loop, tracing. — [Building LangGraph](https://www.langchain.com/blog/building-langgraph)
- Temporal + LangGraph plugin: runs the graph as a Temporal Workflow; Activity nodes get configurable timeouts/retries/heartbeating; Workflow nodes run inline and must be deterministic; InMemorySaver checkpointer (Temporal handles durability); supports `interrupt()` in Activity nodes. — [Temporal LangGraph integration docs](https://docs.temporal.io/develop/python/integrations/langgraph)
- Temporal blog: LangGraph checkpoints are data, not execution — a crashed process means a dead run unless an orchestration layer detects failure and re-enters; human-in-the-loop becomes a coordination problem; long-running agents strain checkpointing. — [Temporal blog](https://temporal.io/blog/temporal-langgraph-plugin-durable-execution)
- Streaming has at-least-once delivery per Activity attempt; subscribers must dedupe on sequence ids or rely on final result. — [Temporal LangGraph integration docs](https://docs.temporal.io/develop/python/integrations/langgraph)
- Durability modes trade performance vs consistency: `exit` (persist only on exit/interrupt, best perf, no mid-run recovery), `async` (persist async, small crash risk), `sync` (persist before next step, highest durability). — [LangGraph durable execution docs](https://docs.langchain.com/oss/python/langgraph/durable-execution)

### Inferences
- A custom framework should make checkpointing pluggable (in-memory for dev, SQLite/Postgres/Redis for prod) and require a run/thread id for any resumable run.
- Separate "pure" agent steps (deterministic, no I/O) from "effect" steps (LLM calls, tool calls, I/O) so only effects are retried and replay stays deterministic.
- Human-in-the-loop should be modeled as a first-class interrupt state (like A2A's `input-required`/`auth-required`) with a durable pending-approval record and a resume entrypoint.
- For long-running agents, prefer an external durable executor (Temporal/Cadence) or a task queue + checkpoint store rather than in-process only.

### Gaps
- Specific retry/backoff defaults and timeout values are framework/deployment choices not specified by sources; LangGraph/Temporal expose them as config, not defaults.
- Exactly-once tool execution is not achievable in general; idempotency keys are the documented mitigation.

## 7. Cost and Latency Optimization

### Takeaway
Optimize cost/latency by (1) enabling provider prompt caching with stable prefixes (41–80% savings), (2) routing simple sub-tasks to cheaper models, (3) trimming/compressing context with awareness of cache invalidation break-even, (4) parallelizing independent tool calls, and (5) pre-warming caches; measure KV-cache hit rate as the key metric.

### Cited Findings
- Prompt caching cuts token cost 41–80% across providers (GPT-5.2 79.6%, Claude Sonnet 4.5 78.5%, Gemini 2.5 Pro 41.4%, GPT-4o 45.9%) and TTFT 6–31% on realistic agentic workloads; OpenAI/Google cache automatically, Anthropic requires explicit breakpoints. — [Don't Break the Cache paper](https://arxiv.org/html/2601.06007)
- System prompt caching drives most savings; all three cache strategies (full context, system-prompt-only, exclude tool results) are within 2–4 percentage points of each other. — [Don't Break the Cache paper](https://arxiv.org/html/2601.06007)
- Anthropic explicit breakpoints + Deep Agents cut token cost 49–80% on real trajectories; Manus AI cites KV-cache hit rate as the single most important production metric. — [LangChain deep-agents prompt caching](https://www.langchain.com/blog/deep-agents-prompt-caching)
- Anthropic optimizing guide: turn on prompt caching + trim unneeded tokens (free levers); a 25-token status line at the front of a system prompt made a small agent cost more than caching off; input trimming cut 21–26% further on top of caching. — [Claude optimizing for cost and intelligence](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)
- Context trimming (drop older turns, keep last N) vs compression (summarize): trimming is deterministic, zero added latency, weak long-range recall; compression retains memory compactly but adds latency/cost and risks context poisoning. — [OpenAI Agents SDK session memory cookbook](https://developers.openai.com/cookbook/examples/agents_sdk/session_memory)
- Trimming invalidates the prompt cache (cold-cache penalty); a case study (76 sessions, Opus 4.6, h=0.9) showed median 12% token reduction, median $0.32 cache-miss penalty, break-even at median 38 turns (1–60 range); DAG-based snapshot branching avoids the penalty by loading full prior context once. — [Contextual Memory Virtualisation paper](https://arxiv.org/html/2602.22402)
- OpenAI prompt caching: prefix must match exactly; min cacheable length 1,024 tokens (GPT-5.6+); cache writes 1.25× input rate, reads 0.1× (0.05× on GPT-6.1 Sol); explicit breakpoints give control over what is cached. — [OpenAI prompt caching docs](https://developers.openai.com/api/docs/guides/prompt-caching?model=gpt-6-astra)
- A cost-optimizing proxy pattern: exact response cache (100% on hits), prompt caching, model routing by token threshold (Haiku/Sonnet vs Opus, 5–15× cheaper), context trimming (keep first + recent turns), optional batch API (50% discount). — [claude-proxy repo](https://github.com/arunjora1992/claude-proxy)

### Inferences
- Keep the static prefix (system prompt, tool schemas, skills) byte-stable and put volatile content (timestamps, per-request user info) at the end or in user messages to maximize cache hits; avoid mid-prompt mutations that bust the whole prefix.
- Model routing should be configurable by token count/complexity with per-task overrides; measure quality regression on the eval suite (§3) before enabling.
- Context strategy should be chosen per workload: trimming for deterministic/short tasks, compression for long-horizon planning; always log summaries for auditability and eval.
- Combine caching + trimming + routing + parallel tool calls; track cost-per-task and KV-cache hit rate as first-class metrics in the tracer (§2).

### Gaps
- Exact break-even thresholds are model/pricing specific and must be recomputed per provider; the cited 38-turn median is one user's Opus 4.6 data, not a universal default.
- No source in this pass provided a definitive "context compression" algorithm or summarizer prompt; treat compression as an eval-gated feature.
