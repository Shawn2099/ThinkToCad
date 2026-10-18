# WORKFLOW.md - ThinkToCad End-to-End Design Process

The complete process from a user's idea to a manufactured part. Operating manual
for the ThinkToCad agentic design toolkit. Every stage maps to existing components
(`SKILLS.md`, `knowledge/`, `contracts/`, `runtime/`, `mcp/`, `tools/`, `memory/`).

> The AI reasons. The tools judge. The memory learns. The user decides.

---

## 0. Guiding principles

1. **Kernel is the referee** - build123d executes, FreeCAD verifies, MATLAB
   simulates. The LLM never declares "this works."
2. **Single-agent-first** - one agent, many tools. Multi-agent only when measured.
3. **DFM from day one** - manufacturing constraints and available tools are
   captured during ideation, not bolted on at the end.
4. **Knowledge grows** - every trusted research finding and every design lesson
   is written back into `knowledge/` so the next design is smarter.
5. **Human in the loop** - the user visualizes and approves; the agent builds
   and verifies. Full automation is never the goal.
6. **Plan before code** - emit a structured design plan (mechanism, joints,
   params) before any CAD code (Pointer-CAD / MIRAGE-CAD).
7. **Credibility is explicit** - every result carries a tier (critique ->
   surrogate -> proxy -> executed); `production_ready` is never assumed.

---

## Stage map

```
0. Guiding principles
1. Ideation            (human-led, agent-assisted)
1.5 Requirement elicitation & confidence gate   (NEW)
2. Research            (web-guided + knowledge base)
3. Specify (contract)
3.5 Design space exploration (NEW, optional)
4. Build (CAD)         + visual self-refinement loop (NEW)
5. Validate (FreeCAD + MATLAB)  + credibility tiering
6. Review (human in the loop)
6.5 Publish gate      (NEW)
7. Deliver
8. Knowledge write-back (NEW, with trust levels)
```

Runtime loop: `Spec -> Build -> Validate -> Learn -> Improve -> Repeat`
(`runtime/design_agent.py` implements this with termination conditions and hooks.)

---

## Stage 1 - Ideation (human-led, agent-assisted)

**Goal:** Turn a vague idea into a stated problem with constraints.

Inputs captured from the user:
- The idea in their own words (what it should do).
- Usage context (load, environment, frequency, operator).
- Sketches / photos / reference parts (any format - multimodal inputs improve
  elicitation: CAD-MLLM, MIRAGE-CAD).
- Candidate mechanisms they have in mind (optional).
- **Manufacturing context (ask explicitly):**
  - What tools are available? (drill press, angle grinder, welder, lathe, mill,
    3D printer, hand tools only)
  - What materials are on hand / locally purchasable?
  - What tolerances can be held?
  - Single-piece or assembly? Repairability needs?
  - Budget and batch size (one-off vs repeated).
- Standards to follow (if any): ISO/ASME drawing, fastener standard, safety.

Outputs:
- `brief.md` (one paragraph: what, for whom, under what constraints).
- A list of open questions for the user.
- Manufacturing profile saved to `constraints/manufacturing_profile.md` (per user).

Exit condition: user confirms the brief and manufacturing profile.

---

## Stage 1.5 - Requirement elicitation & confidence gate (NEW)

**Goal:** No silent engineering. The agent must not fill in missing engineering
decisions; it must ask or abort.

Pattern from Cosmon PartLab (clarify -> confidence gate -> tool loop) and
CAD/CAE Copilot ("the agent executes and verifies the spec; it does not silently
fill in the engineering").

Steps:
1. Convert the brief + manufacturing profile into a structured spec sheet:
   explicit dimensions, loads, tolerances, materials, standards. Prefer numbers
   over prose; prefer a spec sheet over vague prompts (MecAgent SPEC-to-CAD).
2. Run a **clarify pass**: for every missing or ambiguous engineering quantity,
   emit a question with a default + the consequence of each option.
3. Compute a **ConfidenceGate** score over 5 subscores (Cosmon):
   - `mechanism_fit` (does a known mechanism satisfy the function?)
   - `constraint_completeness` (are all constraints numeric?)
   - `manufacturability` (does the shop profile cover it?)
   - `physics_coverage` (are sim gates defined?)
   - `standards_coverage` (are applicable standards named?)
4. **Gate:** mean subscore >= 0.80 to proceed. Otherwise loop clarification
   (max 3 cycles); on exhaustion, abort and surface open questions to the user.
   Never start the tool loop below threshold.
5. Lock approved elements (Neural CAD pattern): once the user approves a
   dimension/mechanism, mark it `locked: true` in the contract so later edits
   regenerate only the unlocked subset.

Output: `spec_sheet.yaml` with `confidence` block and `locked` flags.

Exit condition: confidence >= 0.80 AND user confirms the spec sheet.

---

## Stage 2 - Research (web-guided + knowledge base)

**Goal:** Find the right mechanism(s) and fill knowledge gaps.

Steps:
1. Search `knowledge/` (mechanisms, constraints, lessons, graph.yaml) for
   relevant entries - use Corpus2Skill-style hierarchical navigation where the
   corpus is large; flat retrieval is fine for ~100 mechanisms.
2. If gaps exist, run **web-guided research** (textbooks, patents, standards,
   trusted engineering sources). Sources must be trusted; cite them.
3. For each promising mechanism, extract: principle, key dimensions/equations,
   constraints, failure modes, DFM, when to use.
4. **Write back** new findings to `knowledge/mechanisms/` and `knowledge/lessons/`
   (and update `graph.yaml`) so the knowledge base grows with each design.
   Tag entries with source + date + trust level (see Stage 8).
5. Produce a shortlist of 2-4 candidate mechanisms with pros/cons vs the
   manufacturing profile.

Outputs:
- Updated `knowledge/` (new mechanism/constraint/lesson files).
- `research_summary.md` in the design folder: candidates, trade-offs,
  recommendation.
- Recommended mechanism + rationale for user approval.

Exit condition: user approves the chosen mechanism(s).

---

## Stage 3 - Specify (contract)

**Goal:** Convert the idea into measurable numbers. The spec is the source of
truth, not the model.

Steps:
1. Create a contract YAML from `contracts/_template.yaml` (see **Contract
   schema** below). Every constraint is a number or stock size (no prose).
2. Cross-check constraints against `knowledge/constraints/` (manufacturing,
   tool_design, context, etc.).
3. Add `standards:` field listing applicable standards (e.g., ISO 286, ASME
   Y14.5); add fit/tolerance checks.
4. Add design-rule assertions in the build script where useful
   (`require(WALL >= 3, ...)` / bare `assert`) - violations fail the build
   deterministically with `design_rule_violation` (CAD/CAE Copilot).
5. Run MATLAB sim if physics is involved (torque, stability, traction) - gates
   must print PASS.

Outputs:
- `contracts/<name>.yaml`
- Sim results (PASS/FAIL gates).

Exit condition: all constraints are numbers; sim gates PASS.

---

## Stage 3.5 - Design space exploration (NEW, optional)

**Goal:** When multiple valid designs exist, explore rather than commit to the
first.

Pattern from Autodesk Generative Design, Schulz et al. (interactive DSE), and
TraceDSE (trace-informed proposer-critic, 6-9x fewer evaluations than BO).

Steps:
1. Define the design space: base parametric program + sampled parameter vector
   + constraint-solver feasibility check (Z3 / OCCT constraints).
2. Precompute a sample set where feasible (Schulz) and interpolate for
   real-time visual exploration; display physical properties (mass, surface
   area, CG) alongside geometry.
3. Preference learning: collect **pairwise** preferences ("which of these two
   do you prefer?") - never numeric scores (Cheng et al.); use uncertainty-aware
   Bayesian optimization (Astudillo) to propose the next pair.
4. Emit a small menu (3-6) of candidates for final selection; keep ranking
   advisory (aieng Design Study: validates/executes/compares/adopts without
   overwriting baseline).
5. Stop when: user selects, or plateau (no change in approved elements across
   2 rounds), or budget exhausted (~5 iterations, ~3 review rounds default).

Output: `design_space.yaml` (parameters, ranges, sampled candidates, chosen).

Exit condition: user selects a candidate OR exploration budget exhausted.

---

## Stage 4 - Build (CAD)

**Goal:** Generate parametric CAD from the contract. Plan first, then code.

Steps:
1. **Plan-Then-Construct** (Pointer-CAD, MIRAGE-CAD): emit a structured design
   plan first - mechanism, joints/connectors (ArtiCAD Connector-first: attachment
   points + joint params before geometry), parameter dictionary with units -
   then generate code referencing those params via pointers (no discretization).
2. Retrieve relevant knowledge (`retrieve_knowledge`).
3. Generate build123d code (LLM) under the contract constraints. Use safe
   operation wrappers (`safe_fillet`, `safe_shell`, `safe_bool`) as first line
   of defense; add step instrumentation:
   `with cad_step("mounting_holes", intent=..., step_type=...)` so failures
   localize to a named operation (TraceCAD).
4. Execute via `build123d-mcp` (`create_part`) - sandboxed subprocess.
   - On error: read structured error, repair, retry (self-healing).
   - Prefer **minimal edits** (exact text edits / single-step replacements) over
     full-program rewrites; full rewrite only when a local expression is
     impossible (TraceCAD). Preserve previously-correct features (re-run
     geometry checks; reject candidates that regress).
5. **Visual self-refinement loop** (Seek-CAD, CADSmith): render the generated
   model (isometric + orthographic + step-wise perspectives), critique with
   VLM + CoT, refine next round. Combine exact OCCT measurements (bbox, volume,
   solid validity) as primary signal; VLM holistic judgment secondary. Make
   critique an optimized policy step (RA-CAD) where feasible.
6. Escalation rule: if the same check fails twice, change construction strategy,
   not just tweak parameters (CADSmith Judge).
7. On success: STEP/STL artifacts persist in `output/run_*/`.

Outputs:
- Validated build123d script + construction graph (operations, params,
  topology IDs) for localized edits and cross-backend portability (CADIR).
- STEP/STL artifacts.

Exit condition: build runs clean (returncode 0, valid geometry).

---

## Stage 5 - Validate (FreeCAD + MATLAB)

**Goal:** Independent verification. The kernel is the referee. Verification is
a service: one `validate` entry point returning one structured report.

Checks (via `freecad-mcp` + `matlab-mcp`):
- Geometry validity: `shape.is_valid` + `is_manifold` (B-Rep path for STEP);
  mesh path `Mesh.hasNonManifolds`/`hasInvalidPoints` for STL. Self-heal via
  `ShapeFix` as an explicit, logged step before declaring failure.
- Interference volume = 0 (clash check) with epsilon tolerance (e.g., 1e-3 mm^3).
- Clearance >= min (mm).
- Mass within budget; CG / mass properties.
- Watertight mesh (if STL).
- Sim gates: torque, stability, traction (if applicable).
- Tolerance stack-up (worst-case default; RSS/Monte Carlo on request) over named
  dimensions; report yield + 95th-percentile clearance.
- Design-rule assertions (`design_rule_violation` blocks).
- Standards fit checks (ISO 286 fit classes etc.).
- Determinism check: build twice, compare mesh bytes.

On failure: feed structured feedback to the LLM (see **Repair feedback format**),
adjust, rebuild (Stage 4).

**Credibility tiering** (CAD/CAE Copilot V&V-40 style): every result stamped
with one of:
`critique_finding < surrogate_prediction < proxy_assembly_result <
executed_solver_result`. Mesh accuracy measured (reliable/marginal/unreliable)
with optional GCI/Richardson. `production_ready` is never assumed; NAFEMS-style
benchmarks in CI for sim gates.

Outputs:
- Verification report (see **Verification report JSON**).
- Rendered preview PNGs (isometric + orthographic) for vision critique.

Exit condition: every check prints PASS with credibility tier recorded.

---

## Stage 6 - Review (human in the loop)

**Goal:** User approves the design.

Steps:
1. Launch the result in FreeCAD for the user to inspect.
2. Show a **curated gallery** of 3-6 rendered 3D previews (not raw parameter
   tables - Neural CAD / MIT Schulz pattern) + parameter table + BOM draft.
3. Feedback modalities (Apple CHI 2026 findings): prefer a hybrid -
   - approve/reject on a small curated set,
   - sketch/region annotation ("make this wall taller") for partial changes
     (highest quality/quantity balance, Elo 1054),
   - natural-language edits for global changes,
   - avoid pure ranking (noisy, degraded models).
   Support **lock controls** (freeze approved elements, regenerate unlocked subset)
   and "agree to disagree" (each distinct fix becomes a separate data point).
4. Partial edits: translate NL partial edit into a parameter change + re-render
   rather than expose the parameter directly.
5. If changes: update contract/constraints, loop back to Stage 4 (Build).
6. Cap at ~5 iterations; stop early on approval or if two consecutive rounds
   yield no change in approved elements; escalate only on ambiguity. Reserve
   human review for high-risk/ambiguous decisions to avoid approval fatigue.

Outputs:
- User approval (or change requests).

Exit condition: user explicitly approves.

---

## Stage 6.5 - Publish gate (NEW)

**Goal:** Curation before delivery. "The gate is the curation" (AgentCAD).

Steps:
1. Rebuild every part at each declared parameter range (`PARAMS` min/max).
2. Run all specs (interference, clearance, mass, tolerance) at each extreme.
3. Mate connectors / assembly checks.
4. Determinism verification (mesh-byte equality across two builds).
5. If any red spec or non-deterministic result: block; feed back to Stage 4.
6. Record overrides (with reason) if a gate is deliberately bypassed.

Exit condition: all gate checks green OR an explicit, recorded override.

---

## Stage 7 - Deliver

**Goal:** Final artifacts and closure.

Steps:
1. Generate TechDraw (2D drawing) from the model (projected views, dimensions,
   hole callouts; standards compliance check on drawing completeness).
2. Generate BOM entry (part, qty, material, source).
3. Export final DXF/STEP/STL as needed.
4. Git commit with message referencing the contract.
5. Save final design to `memory/designs/<name>/final.yaml`.
6. Write lessons to `knowledge/lessons/` (successes and failures).
7. Close the open item in the project tracker.

Outputs:
- `*.step`, `*.dxf`, `*.pdf` (TechDraw), BOM.
- Git commit.
- Memory + lessons updated.

Exit condition: commit exists, item closed.

---

## Stage 8 - Knowledge write-back with trust levels (NEW)

**Goal:** The knowledge base grows, but never silently. Consolidate with
trust tiers and utility scoring.

Trust tiers (store as `trust:` in frontmatter):
- **T1 - verified by tool** (FreeCAD/MATLAB pass on this design).
- **T2 - cited standard/textbook** (with source URI + date).
- **T3 - heuristic / workshop note** (empirical, single source).
- **T4 - LLM-inferred (unverified)** (must be confirmed before promotion).

Provenance fields on every knowledge file: `source:`, `version:`, `date:`,
`trust:`, `last_verified:`. Git history provides file versioning; `verified_by`
edge type in `graph.yaml` encodes which tool validated an entity.

Consolidation (HERA ADD/MERGE/PRUNE/KEEP, with utility score u = empirical
success rate):
1. After each validated design: append `memory/designs/<name>/attempt_N.yaml`.
2. On failure: append a lesson markdown with root cause + rule going forward.
3. ADD distinct new insights; MERGE similar/complementary; PRUNE contradicted
   or low-utility; KEEP unchanged.
4. Never silently overwrite a higher-trust entry with a lower-trust one; require
   explicit promotion with evidence.

---

## Concrete data structures

### Contract schema (`contracts/<name>.yaml`)

```yaml
name: cut_height_adjust
function: "Adjust cutter height from 25mm to 60mm"
version: 1
locked: []                       # list of locked param names
standards: [ISO 286, ASME Y14.5]

constraints:
  motor_rise_mm: 0
  deck_clearance_mm: 1.0
  shaft_length_mm: 17
  mass_budget_kg: 0.5
  min_wall_mm: 2.0

mechanisms:                      # tried in order
  - spacer_sleeve
  - slotted_bracket
  - cam_pin

design_space:                    # optional (Stage 3.5)
  parameters:
    slot_length_mm: {min: 10, max: 30, unit: mm}
  samples: 12

validation:
  - type: interference
    tool: freecad
    max_mm3: 0
  - type: clearance
    tool: freecad
    min_mm: 1.0
  - type: mass
    tool: freecad
    max_kg: 0.5
  - type: watertight
    tool: freecad
  - type: sim
    tool: matlab
    checks: [torque, stability, traction]
  - type: tolerance_stackup
    method: worst_case            # worst_case | rss | monte_carlo
    dims: [slot_length_mm, pin_dia_mm]
  - type: design_rule
    rules: [wall_min, fillet_min]
  - type: standards_fit
    standard: ISO 286

deliverables:
  - step_file
  - techdraw_pdf
  - bom_entry
  - git_commit
```

### Verification report JSON

```json
{
  "design": "cut_height_adjust",
  "run_id": "run_2026-10-19T10:00Z",
  "overall": "PASS",
  "credibility": "executed_solver_result",
  "checks": [
    {"name": "interference", "parts": ["deck", "bracket"],
     "measured_mm3": 0.0, "threshold_mm3": 0.0, "pass": true,
     "localization": {"step": "mounting_holes"}, "severity": "blocker"},
    {"name": "clearance", "parts": ["pin", "slot"],
     "measured_mm": 1.2, "threshold_mm": 1.0, "pass": true},
    {"name": "mass", "measured_kg": 0.42, "threshold_kg": 0.5, "pass": true},
    {"name": "watertight", "pass": true},
    {"name": "sim_torque", "measured_nm": 12.4, "threshold_nm": 10.0, "pass": true},
    {"name": "tolerance_stackup", "method": "worst_case",
     "min_clearance_mm": 0.9, "pass": true}
  ],
  "feedback_text": "All checks PASS.",
  "suggested_edits": [],
  "healing_applied": false,
  "kernel_version": "OCCT 7.7",
  "determinism_ok": true
}
```

### Repair feedback format (structured, not free text)

```json
{
  "pass": false,
  "failing_check": "interference",
  "parts": ["deck", "bracket"],
  "measured": 4.2,
  "threshold": 0.0,
  "unit": "mm3",
  "localization": {
    "step": "mounting_holes",
    "feature": "hole_pattern",
    "line": 47
  },
  "severity": "blocker",
  "suggested_action": "offset bracket +2mm along Z or reduce hole count",
  "escalate_if_repeated": true,
  "preservation": {"volume_mm3_before": 1200.0, "volume_mm3_after": 1198.5}
}
```

Rule: `_tool_validate` must return this JSON, never a string. On repeated
failure of the same check, instruct the Refiner to change construction strategy.

### Memory attempt schema (`memory/designs/<name>/attempt_N.yaml`)

```yaml
design: cut_height_adjust
attempt: 2
mechanism: slotted_bracket
status: passed            # passed | failed | partial
contract_version: 1
verification:
  interference_mm3: 0.0
  clearance_mm: 1.2
  mass_kg: 0.42
  watertight: true
  sim_gates: {torque: PASS, stability: PASS}
  credibility: executed_solver_result
failure_mode: null        # e.g. "interference_at_mounting_holes"
root_cause: null
fix_applied: "offset bracket +2mm Z"
reasoning_consulted: [knowledge/mechanisms/slotted_bracket.md]
utility_score: 0.85       # empirical success rate for this mechanism+context
timestamp: 2026-10-19T10:00Z
```

Failed attempts are as valuable as successes.

---

## Metrics & benchmarks

Track these per design run (ThinkToCad evaluation suite, multi-metric per
MIRAGE-CAD/RealCADBench findings that metrics diverge):

| Metric | Target | Source |
|---|---|---|
| Execution/validity rate | >= 99% | AgentCAD benchmark (83% -> 99%) |
| Solid IoU vs reference | >= 0.95 | CADSmith (0.9629) |
| Chamfer Distance | <= 1.0 | CADSmith (0.74) |
| Constraint satisfaction (G-CSR) | 100% | contract specs |
| Edit success (localized) | >= 80% | Nova3D (14/18) |
| Iterations to approval | <= 5 (median ~3) | NN/g plateau data |
| Interference volume | 0 mm^3 | kernel |
| Clearance | >= contract min | kernel |
| Mass error | <= 5% | contract |
| Sim gate pass | 100% | MATLAB |
| Determinism (mesh-byte equality) | pass | AgentCAD |
| Confidence gate score | >= 0.80 | Cosmon |
| Knowledge write-back count | >= 1 lesson/design | ThinkToCad policy |

Benchmarks to align with: CADEngBench (FEA + kinematics), RealCADBench
(executability + IoU + VLM judge), Text2CAD-Bench (4 complexity levels),
MUSE (assembly intent), BenchCAD (industrial families).

---

## DFM rules applied throughout

- Manufacturing profile captured in Stage 1 (tools, materials, tolerances).
- All constraints checked against `knowledge/constraints/manufacturing.md`
  and the user's manufacturing profile.
- Rule packs (declarative JSON/TOML, vcad-style) reference profile parameters
  (`min_tool_dia_mm`, envelope, stock thicknesses); per-process, per-machine.
- Standard stock sizes and off-the-shelf fasteners preferred (M3/M4/M5/M6,
  608 bearings).
- Min wall thickness, fillet radii, hole clearances per `skills/SKILLS.md`.
- No magic numbers: every dimension traces to a contract constraint or stock size.
- Repairability and local sourcing considered (frugal design, OSE principles).
- Buy-out flag for anything beyond machine capability (threads/gears finer than
  cutter, etc.).
- Tolerance default: worst-case (guaranteed fit) for small shops; RSS/Monte
  Carlo for high-volume.

---

## Knowledge growth policy

- Trusted research (textbooks, standards, patents, verified experiments) is
  written to `knowledge/` with source + date + trust level (T1-T4).
- Every design (pass or fail) writes to `memory/` and `knowledge/lessons/`.
- Failed attempts are as valuable as successes.
- `graph.yaml` updated when new entities/relationships appear; `verified_by`
  edge populated consistently.
- Consolidate with HERA ADD/MERGE/PRUNE/KEEP + utility scoring; never silently
  overwrite a higher-trust entry.

---

## The runtime loop (summary)

```
Ideate -> Elicitate -> Research -> Specify -> Explore -> Build -> Validate -> Review -> Publish -> Deliver -> Write-back
               ^                                                                                          |
               |________________________ feedback / errors _________________________________________________|
```

Underneath: `Spec -> Build -> Validate -> Learn -> Improve -> Repeat`
(`runtime/design_agent.py` implements this with termination conditions and hooks.)

Termination conditions (SKILLS.md sec.3): no tool calls/final output; max_turns
exceeded; handoff; HITL interrupt; guardrail tripwire/exit signal.

---

## What ThinkToCad is NOT

- Not a new LLM. Not a new CAD kernel. Not a generic agent framework.
- Not a "text-to-CAD" generator (dead end, ~88% validity).
- Not a commercial product.
- Not fully automated: the user decides.

The value is in the **knowledge packaging + feedback loop + memory** around
the AI and tools you already have.

---

## References

### Research notes (local)
- `research_notes/Improving agentic CAD design workflow/ai_design_pipelines.md`
- `research_notes/Improving agentic CAD design workflow/hitl_feedback.md`
- `research_notes/Improving agentic CAD design workflow/dfm_automation.md`
- `research_notes/Improving agentic CAD design workflow/knowledge_management.md`
- `research_notes/Improving agentic CAD design workflow/verification_validation.md`
- `research_notes/Improving agentic CAD design workflow/generative_cad_llms.md`

### Key papers / projects
- AgentCAD (n3r/AgentCAD) - contract-driven CAD, kernel as referee, publish gate, change proposals.
- Zero-to-CAD (arXiv:2604.24479) - agentic search, feedback-driven synthesis.
- TraceCAD (arXiv:2608.03062) - persistent localized repair, skill memory.
- CADSmith (arXiv:2603.26512) - nested correction loops, VLM Judge, exact metrics.
- Pointer-CAD v2 (arXiv:2606.29301) - Plan-Then-Construct.
- MIRAGE-CAD (arXiv:2608.28669) - shared construction representation.
- CADIR (arXiv:2608.00891) - construction graph, cross-backend reconstruction.
- Cosmon PartLab agent - clarify + ConfidenceGate + guard pipeline.
- CAD/CAE Copilot (aieng) - credibility tiers, design-rule assertions, Design Study.
- Seek-CAD (arXiv:2505.17702) - visual self-refinement.
- RA-CAD (arXiv:2608.05714) - learnable critique.
- TraceDSE (arXiv:2610.07191) - trace-informed design space exploration.
- ArtiCAD (arXiv:2604.10992) - Connector-first assemblies.
- Karniadakis et al. (arXiv:2511.03179) - knowledge-guided multi-agent.
- Siemens AEI (arXiv:2604.07784) - agentic engineering intelligence.
- Corpus2Skill (arXiv:2604.14572) - compile-then-navigate knowledge.
- HERA (arXiv:2604.00901) - hierarchical evolving RAG, experience library.
- Apple CHI 2026 (arXiv:2509.16779) - feedback modalities, sketching.
- CAD/CAE Copilot credibility tiers; V&V-40.
- Schulz et al. (2017) - interactive design space exploration.
- Astudillo (2020), Cheng et al. - preference-based Bayesian optimization.
- OSE Design for Fabrication - frugal design principles.
- vcad-kernel-dfm - hobby 3-axis mill rule pack.
- CADCLAW - automated STEP-assembly gates, confidence budgets.
- build123d, FreeCAD, MATLAB (tools).