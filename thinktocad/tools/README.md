# Tool layer

The canonical, provider-neutral tool contract for ThinkToCad. Implements
`guides/AI_AGENT_TOOLKIT_GUIDE.md`. Every tool returns a structured envelope and never
raises into the agent loop.

## Modules

| Module | Responsibility |
|---|---|
| `errors.py` | Error codes + `ToolError` with retryability (guide §6) |
| `registry.py` | `ToolDefinition`, `ToolRegistry`, `@safe_tool`, JSON-schema from signature (guide §3–4) |
| `execution.py` | Single-call pipeline + `ExecutionContext`, `RetryPolicy`, `CircuitBreaker` (guide §5–6) |
| `policy.py` | Deny-wins allow/ask/deny rules; `ASK` is the human-in-the-loop hook (guide §9) |
| `guardrails.py` | Input/output guardrail pipeline + `Tripwire` (guide §6, §9) |
| `security.py` | Static code screen (AST deny-list) + `PathScope` (guide §9) |
| `observability.py` | GenAI-semconv spans + per-tool counters/histograms (guide §10) |
| `adapters.py` | OpenAI / Anthropic / Gemini / MCP schema envelopes + strict mode (guide §3, §12) |
| `formatting.py` | `paginate`, `truncate_text`, `artifact` — token-efficient results (guide §7) |
| `knowledge.py`, `contracts.py`, `verification.py` | The domain tools |

## Pipeline

```
policy -> cancellation -> input guardrails -> span
       -> circuit breaker -> retry + timeout -> fn
       -> output guardrails -> metrics -> envelope
```

## Envelope

```json
{"ok": true,  "data": {...}, "error": null}
{"ok": false, "data": null,
 "error": {"code": "...", "message": "...", "retryable": false,
           "suggested_fix": "...", "details": {}}}
```

## Tests

`tests/` — unit (registry, tools), governance (policy, guardrails), security, execution
(retry, breaker, batch), adapters/formatting. Run `pytest -q`.
