# SKILLS.md - Knowledge-Guided Agentic CAD Design

Loaded by the AI agent before any design task. Read this first. This skill packages
research-backed engineering knowledge + an agentic loop so an LLM can do real
mechanical design instead of drawing plausible garbage.

> The AI reasons. The tools judge. The memory learns.

## 1. Role and paradigm

You are a mechanical design assistant. You do **not** design directly. You:

1. **Retrieve** relevant mechanisms/constraints/lessons from `knowledge/`.
2. **Plan** a design approach against the contract.
3. **Execute** through tools (build123d, FreeCAD, MATLAB).
4. **Evaluate** against constraints; the tools decide PASS/FAIL.
5. **Learn** - save the outcome to `memory/`.

Paradigm (2026): **text-to-code-to-CAD**, not text-to-CAD. The LLM writes
parametric Python (build123d); the kernel executes it. LLMs alone hit ~88%
validity; with a knowledge base + validation loop, ~99% (AgentCAD benchmark).

Consult `guides/DESIGN_TEXTBOOKS.md` for the pointer guide: which book/standard owns each
topic, plus the 0-to-professional roadmap. Cite book + edition + chapter when
answering any sizing/standards question.

Consult `guides/SENIOR_CAD_KNOWLEDGE.md` for senior-level design knowledge: GD&T,
FEA, materials, assembly, drawing, surface finish, fasteners, power transmission,
vibration, reliability, cost. Route by topic to `knowledge/constraints/*.md`.

Consult `guides/CAD_PARTS_SOURCES.md` for pre-made CAD models, mechanisms, and parts
(standards parts, open-source STEP, community repos, manufacturer libraries,
3D printing, academic datasets). Check license before use.

Consult `guides/AI_CAD_RESEARCH_CATALOG.md` for the master index of ~170+ AI+CAD research
papers (2024-2026): text-to-CAD, text-to-code, agentic, editing, assembly,
manufacturing, benchmarks, surveys. Use for research-backed design decisions.

Consult `guides/MECHANISM_CATALOG.md` for the master index of ~228 mechanisms with
selection guidance. Route to `knowledge/mechanisms/*.md` for details.

Consult `guides/AI_AGENT_TOOLKIT_GUIDE.md` for how to build AI agent toolkits
from OpenAI/Anthropic/Google patterns (tool schema, execution, errors, security,
observability, testing). Use when designing ThinkToCad's MCP tool layer.

## 2. The kernel is the referee

- You never decide if a part works. build123d executes; FreeCAD verifies; MATLAB simulates.
- On failure, read the structured error, repair, and retry. Do not argue with the tool.
- If a tool says interference > 0, the design is invalid. Full stop.
- Errors are returned to you as tool results for retry, never raised into the loop.

## 3. The agent loop (ReAct-shaped)

Canonical loop, used by every major framework (OpenAI Agents SDK, Claude Agent SDK,
Google ADK, LangGraph, Pydantic AI, smolagents):

```
assemble model input from state
  -> call LLM
  -> if no tool calls: return final output
  -> else execute tool calls (parallel where independent)
  -> append tool results to history
  -> repeat, bounded by max_turns / termination condition
```

**Five termination conditions to implement:**
1. No tool calls / final output (text or structured).
2. `max_turns` exceeded (raise `MaxTurnsExceeded`; allow disabling).
3. Handoff to another agent (`transfer_to_<agent>` tool call).
4. HITL interrupt/pause (save state, wait for human).
5. Guardrail tripwire or explicit exit signal (`final_answer`, `exit_loop`, `StopEvent`).

**Design rules from research:**
- Start with a **single agent** maximized for capability. Add multi-agent only for
  high-value, parallelizable, breadth-first work - multi-agent burns ~15x the tokens
  of a chat (Anthropic orchestrator-worker: +90.2% quality, 15x tokens).
- Async-first with sync wrappers; hook points `before_model` / `before_tools` / `after_turn`.
- Represent the turn as typed **items** (message, function_call, function_call_output,
  reasoning), not flat messages, so client- and server-managed state both work.
- Single-agent-first consensus (OpenAI + Anthropic): split only when tool confusion or
  instruction non-compliance is *measured*, not speculated.

## 4. Tool design (the product)

Tools are Python functions whose signatures + docstrings become JSON schemas. The
framework validates args, executes (async, parallel where safe), and returns a
`ToolResult(call_id, content, is_error, metadata)`. **Never raise into the loop.**

Cross-provider schema contract: `{name, description, parameters}` where parameters
is JSON Schema (`type: "object"`, `properties`, `required`). OpenAI strict mode
requires all params in `required` and `additionalProperties: false`; Anthropic uses
`input_schema`; MCP uses `inputSchema`.

**Design rules (from Anthropic "Writing tools for agents" + OpenAI function calling):**
- Descriptions state **when to invoke** and **how to build arguments**; developer
  instructions disambiguate similar tools and preferred ordering.
- **Similarity and overlap matter more than raw count**: >15 distinct tools can work;
  <10 overlapping tools can fail.
- Choose formats the model writes easily (close to natural internet text, no
  formatting overhead). Give tokens to think. Poka-yoke arguments (e.g. require
  absolute filepaths) - this alone fixed SWE-bench errors.
- Return structured errors so the model can retry ("reflection and self-correction").
- Run read-only / `concurrency_safe` tools via `asyncio.gather`; stateful tools
  sequentially in call order to avoid corruption.
- Wrap tools with input/output validators; tripwires raise terminal exceptions for
  catastrophic violations.
- **Iterate on tool descriptions with held-out tasks**: generate realistic
  multi-step tasks, run simple agentic loops, collect metrics (runtime, tool calls,
  tokens, errors), analyze transcripts, hold out test sets to avoid overfitting.

## 5. Context engineering (not prompt engineering)

Context is finite with diminishing returns (transformer attention is n^2; longer
contexts reduce recall - "context rot"). Anthropic frames context engineering as
the successor to prompt engineering because agents run long loops.

**Represent history as typed messages/items; budget tokens per request.**
- On overflow: compact (summarize) older turns or clear stale tool results; keep a
  per-run scratchpad; use just-in-time retrieval for long-term memory.
- Place prompt-cache breakpoints on stable prefixes (tools -> system -> messages).
- System prompts at the "right altitude" between brittle hardcoded logic and vague
  guidance; organize into sections (Identity, Instructions, Examples, Context).
- Few-shot examples: diverse and canonical, not laundry lists.
- Agents keep lightweight identifiers (paths, queries, links) and load data at
  runtime via tools (progressive disclosure). Claude Code uses `CLAUDE.md` up front
  plus glob/grep just-in-time.
- Keep intermediate values (plans, retrieved doc IDs, tool outputs) in a per-run
  state dict and inject a compact summary into messages, not the full data.

**Long-horizon techniques (Anthropic):**
1. **Compaction** - summarize nearing-limit history and restart with the summary;
   keep the 5 most recently accessed files. Run when estimated tokens exceed ~80%
   of budget: keep system + tools (cached) + last K turns verbatim; summarize the
   middle; clear raw tool results beyond a window, keeping only summaries.
2. **Structured note-taking / agentic memory** - `NOTES.md` / TODOs persisted
   outside the context window.
3. **Sub-agent architectures** - isolated context windows returning 1k-2k token
   summaries.

**Prompt caching order:** stable prefixes first, volatile content last. Anthropic
cache prefix order is tools -> system -> messages (5-min TTL default, refreshed free
on use; 1-hour at 2x base; writes 1.25x/2x; reads 0.1x; 20-block lookback window).
Never put volatile content (timestamps, user-specific data) in the cached prefix.
Version and test tool descriptions with held-out tasks. Use templating (`{var}`) for
dynamic state injection. "Smarter models need less prescriptive engineering"
(Anthropic) - calibrate to the model.

## 6. Multi-agent (earn it with measurement)

Multi-agent excels for breadth-first queries pursuing multiple independent
directions. Anthropic's orchestrator-worker (Opus 4 lead + Sonnet 4 subagents)
outperformed single-agent Opus 4 by 90.2% on research eval but burns ~15x tokens;
token usage explains 80% of BrowseComp variance.

**Patterns to implement:** prompt chaining, routing, parallelization
(sectioning/voting), orchestrator-workers, evaluator-optimizer (Anthropic's five);
manager (agents as tools, central control) vs decentralized (handoffs, peers
transfer control) (OpenAI); deterministic workflow agents (Sequential/Parallel/Loop
in ADK); Swarm speaker selection by most recent HandoffMessage (AutoGen);
sequential/hierarchical process (CrewAI); managed_agents (smolagents).

**Handoffs as ordinary tool calls** (`transfer_to_<agent>`), so any tool-calling
model can drive routing without a separate orchestrator. OpenAI's `handoff()`
supports `tool_name_override`, `input_type`, `input_filter`, `is_enabled`,
`nest_handoff_history` (compacts transcripts into summary segments); agents-as-tools
via `as_tool()` keeps a manager in control.

**Shared state vs message passing:** shared state (session state, state dict) is fast
and enables templating but couples agents; message passing (thread, A2A tasks) is
decoupled and auditable. Recommendation: shared scratchpad for in-process subagents
(summaries only, 1-2k tokens); message passing (A2A) for cross-service agents;
write large subagent outputs to the filesystem and pass paths, not content.

**Avoid infinite loops:** `max_turns`/`max_iterations`, termination conditions,
`exit_loop` escalation, final-answer tools, HITL breakpoints, state-based
convergence checks (no new information in N turns).

## 7. Production hardening (layered stack)

**Interoperability - three planes:**
- MCP client/server for tools (JSON-RPC 2.0, stdio local + Streamable HTTP remote).
- A2A server/client for agent delegation (Agent Cards at `/.well-known/agent.json`,
  task lifecycle, JSON-RPC over HTTP).
- OpenAI-compatible HTTP front door (`/v1/chat/completions`, `/v1/responses`).

MCP is the standard for tools (Anthropic: "USB-C for AI"); A2A complements it
(vertical tools vs horizontal agent-to-agent). Keep the three planes separate.

**Observability:** trace every run as an OpenTelemetry trace tree - top-level
`invoke_agent` span with child `chat`/inference spans per LLM call and
`execute_tool` spans per tool call - carrying `gen_ai.*` attributes (model, input/
output tokens, finish reasons, conversation id, tool name, cache token counts).
Content capture (prompts, completions, tool args/results) is opt-in (sensitive).
Conventions are still "Development" status - pin to a specific semconv version.
Record tool calls as first-class spans for trajectory evaluation. Compute cost from
token usage x price table in the tracer so spend caps enforce inline.

**Evaluation:** three levels - final task success, trajectory (tool selection/order/
efficiency), stepwise LLM-as-judge. Deterministic task-success where possible;
LLM-as-judge (preferably agent-as-judge with trajectory access) for nuanced quality;
offline in CI as regression tests, online in production with sampling. Score four
metrics: task success, tool-call accuracy (precision/recall/F1 vs reference trace),
step efficiency (optimal/actual steps), cost per task. Persist structured
trajectories, intermediate states, artifacts. Outcome-only judges are blind to
agents that reach the right answer the wrong way - pair discrimination against
clean parent trajectories.

**Guardrails & safety:** OWASP ranks Prompt Injection (LLM01) #1. Defenses are
probabilistic - treat as a property to manage, not a bug to fix. Layer: validate/
sanitize inputs and outputs; defend direct + indirect injection by keeping untrusted
content (tool results, retrieved docs) in separate message roles/sections with
provenance, never concatenated into the system prompt; tool allow/deny lists and
least privilege; PII redaction on inputs (before logging) and outputs (before
returning); human approval for high-risk actions; sandbox tool execution. Apply
standard web security (TLS, auth at HTTP layer, least privilege), scope tool
permissions per agent/run, defend SSRF (block private IPs/metadata endpoints) and
path traversal (canonicalize paths), inject secrets via a resolver at tool runtime
(never in prompts/traces/AgentCards), per-tenant and per-tool rate limits with
backpressure as retryable errors. Per-run budget: max tokens, max tool calls, max
wall-clock, max spend USD - enforced in the loop and tracer.

**Reliability:** design the loop as a durable, resumable workflow - persist
checkpoints per step, make side effects idempotent with idempotency keys, retry
transient failures with backoff + timeouts, support HITL interrupts as first-class
state with a durable pending-approval record and resume entrypoint, use a task
queue to decouple request handling from execution. Separate "pure" agent steps
(deterministic, no I/O) from "effect" steps (LLM calls, tool calls, I/O) so only
effects are retried and replay stays deterministic. For long-running agents, prefer
an external durable executor (Temporal) or task queue + checkpoint store. Exactly-
once tool execution is not achievable in general; idempotency keys are the
mitigation.

**Cost & latency:**
1. Enable provider prompt caching with stable prefixes (41-80% savings; OpenAI/Google
   cache automatically, Anthropic requires explicit breakpoints). Turn on caching +
   trim unneeded tokens as free levers.
2. Route simple sub-tasks to cheaper models (5-15x cheaper), configurable by token
   count/complexity, quality-gated on the eval suite.
3. Trim or compress context with awareness of cache invalidation (trimming is
   deterministic, zero added latency, weak long-range recall, invalidates cache -
   case study: 12% token reduction, $0.32 cache-miss penalty, break-even at 38 turns;
   compression retains memory compactly but adds latency/cost and risks poisoning).
4. Parallelize independent tool calls.
5. Pre-warm caches. Track KV-cache hit rate as the #1 production metric (Manus AI).

## 8. Design rules (general mechanical)

- Prefer standard stock sizes and off-the-shelf fasteners (M3/M4/M5/M6, 608 bearings).
- Minimum wall thickness: 2 mm (plastic/printed), 1.5 mm (sheet metal), 3 mm (cast).
- Fillet all internal corners (min r = 1 mm) to reduce stress concentration.
- Holes for fasteners: clearance +0.2 mm over nominal; tapped holes at nominal.
- Keep parts single-piece where possible; split only for assembly or manufacturing.
- Avoid magic numbers: every dimension traces to a contract constraint or stock size.

## 9. Parametric conventions

- All dimensions in mm internally; convert to m only at sim boundaries.
- Name parameters in snake_case with unit suffix where ambiguous (`length_mm`, `mass_kg`).
- One source of truth per dimension: contract -> spec -> code. Never hard-code in CAD.
- Expose adjustable dims as top-level variables, not buried in expressions.

## 10. Workflow (five stages)

`Inspect -> Specify -> Build -> Validate -> Deliver`

- **Inspect**: read contract + knowledge + CAD output. State the task in one sentence.
- **Specify**: convert every constraint to a number or stock size.
- **Build**: sim in MATLAB, model in build123d. Gates print PASS.
- **Validate**: FreeCAD interference + mass + clearance. Every check PASS.
- **Deliver**: TechDraw + BOM + git commit + close the item.

Runtime loop: `Spec -> Build -> Validate -> Learn -> Improve -> Repeat`

## 11. Error recovery recipes

- Boolean fails -> check for coincident faces; add 0.01 mm tolerance or rebuild.
- Mesh non-watertight -> re-tessellate with finer linear deflection.
- Interference > 0 -> identify clashing faces; offset or redesign.
- Mass off by >5% -> check material density assignment and shell thickness.
- Clearance < min -> increase gap or reduce moving part envelope.

## 12. Memory

After every design, save to `memory/designs/<name>/attempt_N.yaml`:
mechanism, status, verification (interference, clearance, mass), timestamp.
Failed attempts are as valuable as successes. Persist lessons to `knowledge/lessons/`.

## 13. What to NOT build

No new LLM, no new CAD kernel, no generic agent framework, no text-to-CAD generator,
no commercial product. The value is in the **knowledge packaging**, not the agent.
The kernel is the referee; the AI reasons; the memory learns.