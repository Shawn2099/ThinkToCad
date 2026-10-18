# Guardrails and production constraints (from research)

- OWASP LLM01 Prompt Injection is #1; defenses are probabilistic - manage, don't fix.
- Keep untrusted content (tool results, retrieved docs) in separate message roles
  with provenance; never concatenate into the system prompt.
- Tool allow/deny lists + least privilege per agent/run.
- PII redaction on inputs (before logging) and outputs (before returning).
- Human approval for high-risk actions; sandbox tool execution.
- Defend SSRF (block private IPs/metadata endpoints) and path traversal (canonicalize).
- Inject secrets via resolver at tool runtime - never in prompts, traces, AgentCards.
- Per-run budget: max tokens, max tool calls, max wall-clock, max spend USD.
- Trace every run (OTel): invoke_agent -> chat/execute_tool spans; gen_ai.* attrs.
- Content capture opt-in (sensitive). Pin to a specific semconv version.
- Evaluate at 3 levels: task success, trajectory, stepwise LLM-as-judge.
- Score 4 metrics: task success, tool-call accuracy (P/R/F1), step efficiency, cost/task.