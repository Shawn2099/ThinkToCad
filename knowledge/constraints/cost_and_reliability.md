# Cost and reliability constraints (from research)

- Prompt caching: 41-80% savings. OpenAI/Google cache automatically; Anthropic
  needs explicit breakpoints. Turn on caching + trim unneeded tokens as free levers.
- Route simple sub-tasks to cheaper models (5-15x cheaper), quality-gated on evals.
- Trim context: deterministic, zero added latency, weak long-range recall, invalidates
  cache (break-even ~38 turns in case study). Compression: retains memory, adds
  latency/cost, risks poisoning.
- Parallelize independent tool calls; pre-warm caches.
- Track KV-cache hit rate as the #1 production metric.
- Durable execution: checkpoints per step, idempotency keys, backoff + timeouts,
  HITL interrupts as first-class state, task queue decoupling.
- Separate pure steps (deterministic, no I/O) from effect steps (LLM/tool calls, I/O)
  so only effects retry and replay stays deterministic.
- Exactly-once tool execution is impossible in general; use idempotency keys.