# Automated Verification & Validation (V&V) in AI-Assisted CAD Design

> **Note (2026-10-19):** This note was written against an earlier in-repo architecture.
> The `thinktocad/mcp/freecad_server.py` / `matlab_server.py` stubs and the
> `check_watertight` / `_tool_validate` tools described below were removed. Verification
> and simulation are now delivered by the external `freecad-mcp` and `matlab-mcp` servers;
> ThinkToCad's domain tools (`check_gate`, `dfm_check`, `save_attempt`) orchestrate them.
> The kernel analysis (OCCT / build123d / FreeCAD) remains accurate.

## Q1: What automated geometry checks exist (watertight, manifold, self-intersection, degenerate faces)?

### Takeaway
Geometry validity is best treated as a layered, kernel-backed gate: cheap topological checks (manifold/watertight, closed shells, non-degenerate edges) plus geometric checks (self-intersecting wires, curve-on-surface deviation, invalid tolerances) exposed by OpenCASCADE's `BRepCheck_Analyzer`, surfaced in build123d as `Shape.is_valid`/`Shape.is_manifold` and in FreeCAD as `Shape.isValid()`/`Shape.check()` and `Mesh.hasNonManifolds`/`hasInvalidPoints`. These are deterministic and should run before any LLM judgement.

### Cited Findings
- OpenCASCADE `BRepCheck_Analyzer::IsValid()` returns true only if the topology is correct and edge parameterization is correct: edges have ≥2 vertices unless degenerate and stay within tolerance; wires defining a face must not self-intersect and must be closed; one wire contains all others; faces correctly oriented (especially w.r.t. adjacent faces in a solid); shells defining a solid must be closed with one enclosing shell; edges in a face must have `SameParameter`/`SameRange` true and satisfy ‖C(t) − S(P(t))‖ ≤ tolerance. — [OCCT 8.0.1 BRepCheck_Analyzer](https://dev.opencascade.org/doc/refman/html/class_b_rep_check___analyzer.html)
- build123d exposes `Shape.is_valid` (wraps `BRepCheck_Analyzer`, `SetParallel(True)`) and `Shape.is_manifold` (each non-degenerate edge shared by exactly two faces; degenerate edges skipped) — effectively the watertight/manifold test for B-Rep solids. — local source: `build123d/topology/shape_core.py` (installed package) and [build123d docs](https://build123d.readthedocs.io/en/latest/)
- FreeCAD `Part.Shape.isValid()` and `Shape.check(runBopCheck=False)` perform the detailed structural check (more detailed than `isValid()`; `runBopCheck=True` adds a BOP check); `Part.ShapeFix` (Edge/Face/Solid/Shell/Wire/Root) provides automatic healing. — local FreeCAD 1.1 (`Part.pyd`) inspection
- FreeCAD `Mesh` exposes `hasNonManifolds`, `hasInvalidPoints`, `hasInvalidNeighbourhood` as mesh-level watertight/manifold checks, plus `removeNonManifolds`/`removeInvalidPoints`. — local FreeCAD 1.1 inspection
- CADSmith enforces a hard kernel check: "if the solid is not valid (not watertight), the iteration fails regardless of the Judge's assessment," alongside kernel metrics (volume, bounding box, face/edge/vertex counts). — [arXiv:2603.26512](https://arxiv.org/abs/2603.26512) (CADSmith paper)
- build123d docs call out "Self Intersection" as a known failure mode requiring care (offset/shell operations), confirming self-intersection is a first-class validity concern. — [build123d tips](https://build123d.readthedocs.io/en/latest/tips.html)
- OpenCASCADE `ShapeFix`/`ShapeUpgrade`/`ShapeAnalysis` packages are the standard healing toolkit invoked after a failed `BRepCheck`. — [OCCT 8.0.1 BRepCheck_Analyzer](https://dev.opencascade.org/doc/refman/html/class_b_rep_check___analyzer.html)

### Inferences
- ThinkToCad's `check_watertight` stub should be implemented two ways: (a) B-Rep path via `shape.is_valid` + `is_manifold` for STEP, and (b) mesh path via FreeCAD `Mesh.hasNonManifolds`/`hasInvalidPoints` for STL exports. Returning both avoids false confidence when an STL is generated from a valid B-Rep but tessellated poorly.
- Degenerate faces/edges are implicitly caught by `BRepCheck` (wires must be closed, edges need vertices); but a fast pre-check of zero-area faces and zero-length edges is cheap and localizes errors before invoking the analyzer.
- Self-healing should be an explicit, logged step (ShapeFix) rather than silent: log which subshape was healed so the LLM can decide whether to trust the result.

### Gaps
- I found no single published checklist of "all geometry checks" for build123d/OCCT beyond the BRepCheck criteria above; some checks (e.g., minimum wall thickness, undercut) are application-specific and not in the kernel.
- FreeCAD's `Shape.check()` return semantics (None when OK vs. list of error strings) were inferred from local probing; exact error-string taxonomy not verified from docs.

## Q2: How do systems do automated interference/clash detection and clearance checks?

### Takeaway
Clash detection reduces to (a) boolean intersection volume (0 = no clash) and (b) minimum distance between bodies; both are exposed by OCCT via build123d (`shape.intersect`/`common`, `shape.distance_to`) and FreeCAD (`Shape.common`, `Shape.distToShape`). A robust pipeline also adds bounding-box pre-filters, clearance thresholds from the contract, and assembly-level aggregate checks.

### Cited Findings
- build123d `Shape.distance_to(other)` returns the minimal distance between two shapes via `BRepExtrema_DistShapeShape`; `Shape.intersect`/`common` compute boolean intersection; `volume` gives intersection volume. — local build123d source (`topology/shape_core.py`)
- FreeCAD `Part.Shape.common(other)` yields the intersection solid (volume = clash volume); `Shape.distToShape(other)` returns `(min_distance, closest_points, ...)` for clearance. — local FreeCAD 1.1 inspection
- AgentCAD exposes interference and clearance as first-class metrics: "interference between assembly components" is part of kernel validation; `specs.py` supports assembly intent checks (clearances, interference, tolerance stack-ups) evaluated on every rebuild, and a proposal whose specs are red cannot be merged. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- CAD/CAE Copilot uses explicit assembly-level geometric checks (interference, clearance) inside design-rule assertions and credibility-tiered results. — [GitHub: armpro24-blip/cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot) (cited in prior notes)
- ThinkToCad's FreeCAD MCP stubs already define `interference(a_path, b_path)` ("Boolean intersection volume; 0 = no clash") and `min_clearance(a_path, b_path)` ("Minimum distance between two bodies (mm)"). — local `thinktocad/mcp/freecad_server.py`
- AgentCAD `agentcad check` runs interference across the whole assembly headlessly and emits a versioned JSON report + exit code (0 green / 1 model wrong / 2 no verdict). — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)

### Inferences
- Implement `interference` as `common_volume = (a.common(b)).volume` (with try/except; OCCT can fail on bad geometry) and report both the volume and a boolean `clash = volume > epsilon`. Use a tolerance epsilon (e.g., 1e-3 mm³) to ignore numerical slivers.
- Implement `min_clearance` via `a.distToShape(b)[0]` (FreeCAD) or `a.distance_to(b)` (build123d); compare against contract thresholds (e.g., `min_clearance_mm`).
- Add a bounding-box pre-filter (`_bounding_boxes_overlap`) to skip expensive boolean ops when parts are far apart — build123d already uses this internally in `brep_from_stl`.
- Feed failures back as structured records: `{check: "interference", parts: [a,b], measured_mm3, threshold_mm3, pass: bool, suggested_action}` so the LLM can localize to the offending parts/instances.

### Gaps
- No source documents how industry tools handle large-assembly clash detection (spatial hashing, broad-phase) beyond OCCT's exact methods; scaling to 1000+ parts may need a broad-phase layer not covered here.

## Q3: How do they handle tolerance analysis (worst-case, RSS, Monte Carlo) automatically?

### Takeaway
Automated tolerance analysis is still largely a CAD-adjacent discipline: worst-case (linear stackup of limits) and statistical (RSS or Monte Carlo over distributions) are well-defined methods, but in AI-CAD loops they are best implemented as executable assertions in the model/spec (AgentCAD `specs.py` tolerance stack-ups) evaluated on every rebuild, rather than as opaque post-hoc checks. Monte Carlo requires re-running the parametric model at sampled dimensions.

### Cited Findings
- Worst-case: place each variable at its tolerance limit to maximize/minimize the measurement; guarantees 100% assembly success but forces tight (expensive) tolerances. — [Wikipedia: Tolerance analysis](https://en.wikipedia.org/wiki/Tolerance_analysis)
- Statistical: model each variation as a distribution and sum them; RSS combines variances (σ_assembly² = Σ σ_i²) for independent variables; Monte Carlo samples distributions, rebuilds/assembles, and records measurements to estimate yield. — [Wikipedia: Tolerance analysis](https://en.wikipedia.org/wiki/Tolerance_analysis)
- Two statistical approaches: (1) sensitivity/delta method (small deltas to nominals → geometric multipliers, smooth output but assumes parallel surfaces stay parallel) and (2) Monte Carlo (random geometry within tolerances, assembled, measured; captures real imperfect geometry and can ingest factory inspection data, but run-to-run variation). — [Wikipedia: Tolerance analysis](https://en.wikipedia.org/wiki/Tolerance_analysis)
- AgentCAD supports "tolerance stack-ups" inside project `specs.py` (assembly intent), evaluated on every rebuild with pass/fail/skip; a proposal whose specs are red cannot be merged — i.e., tolerance checks are treated like unit tests. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- ASME Y14.5 (GD&T), ASME Y14.41 (digital product definition), and relevant ISO dimensioning/tolerancing standards are the referenced basis for tolerance concepts; no single standard covers the tolerance-analysis process itself. — [Wikipedia: Tolerance analysis](https://en.wikipedia.org/wiki/Tolerance_analysis)
- For automated Monte Carlo in a parametric code stack: re-execute the build script at sampled `PARAMS` (AgentCAD declares `PARAMS` with min/max bounds and units) and measure critical gaps/clearances; AgentCAD's publish gate already "builds every part at each parameter's declared range" — a natural hook for worst-case/Monte Carlo sampling. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)

### Inferences
- ThinkToCad should add a `tolerance_stackup` check type to contract `validation`: worst-case (min/max) and RSS over named dimensions, computed from the parametric variables. For Monte Carlo, sample N (e.g., 1000) parameter sets within tolerances, rebuild via the build123d sandbox, measure the critical clearance, and report yield (fraction passing) plus 95th-percentile clearance.
- Because MATLAB is in the stack, tolerance propagation of nonlinear performance (stress, deflection) can be pushed into the sim gates: sample dimensions → rebuild geometry → compute mass/CG/volume → run MATLAB gate; this matches the "variation engine outputs to a stress program" pattern.
- Treat tolerance results as credibility-tiered (executed solver result > surrogate) per CAD/CAE Copilot's V&V-40-style tiers, and stamp each result with its tier.

### Gaps
- I found no open-source, build123d-native tolerance-analysis library in the sources; implementing Monte Carlo over STEP rebuilds is feasible but cost-heavy (N kernel runs). No published benchmarks for AI-CAD tolerance loops were located.

## Q4: How do they feed structured errors back to an LLM for repair (error localization, minimal edits)?

### Takeaway
The highest-leverage pattern is "persistent, localized, evidence-backed repair": keep a structured record linking requirements ↔ modeling steps ↔ failures ↔ candidate outcomes; diagnose the faulty step; restrict edits to a small dependency region (bounded hops); evaluate candidates with execution + preservation + locality checks; and retain successful/failed repairs as reusable skills. This is TraceCAD's core contribution and is directly transferable to ThinkToCad.

### Cited Findings
- TraceCAD persistent recovery state: feature state `F` (lifecycle, evidence, related steps) + `StepTrace` (ordered scopes with identity, intent, status, timing, exception). Tracebacks identify modeling operations, not just source lines. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- TraceCAD localized repair: build a dependency graph from variables defined/used per step; repair region `R_h(s) = {s} ∪ Upstream(s,h)` with small hop budget h; downstream consumers checked after patching (not auto-included) to keep edits local. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- TraceCAD candidates are evaluated as complete programs; execution + export are hard constraints; feature state and visual feedback test semantics; shape-delta detects damage to unrelated geometry; selector favors fewer changed scopes and promotes only when execution, semantic, preservation, and locality evidence agree. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- TraceCAD repair-skill memory: promoted trajectory → skill `k=(σ,d,π,τ,ε,u)` (signature, diagnosis, policy, template, evidence, reuse stats); reuse counts as success only if it contributes to a promoted repair; failures retained as negative evidence. Removing persistent state nearly halves recovery score; removing localized search more than doubles geometric regression and doubles code-agent invocations. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- CADSmith feedback: Validator Judge (stronger model than coder) receives prompt + code + exact kernel metrics + three-view render; outputs `{passed, feedback}` with exact numeric discrepancies; escalation guidance at iteration ≥3; Refiner receives full history of attempts to prevent oscillation. — [arXiv:2603.26512](https://arxiv.org/abs/2603.26512)
- AgentCAD: errors return as structured data ("traceback, failing line, hints"); design specs report pass/fail/skip; `run_specs` groups by requirement id; Error Doctor rewrites raw OCCT errors into plain-language fixes. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- CAD/CAE Copilot: design-rule violations fail deterministically with structured `design_rule_violation`; credibility tiers stamped on results. — [GitHub: armpro24-blip/cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot) (cited in prior notes)
- Self-Refine (Madaan et al.) establishes that refinement helps only when feedback is informative enough to guide correction. — cited via [arXiv:2603.26512](https://arxiv.org/abs/2603.26512) references

### Inferences
- ThinkToCad's `_tool_validate` stub should return a structured JSON failure, not a string: `{pass, checks:[{name, measured, threshold, pass, localization:{step/feature/part}, severity}], feedback_text, suggested_edits}`. This is the single biggest improvement over the current "validate: not implemented" stub.
- Add step instrumentation to generated code (`with cad_step("mounting_holes", intent=..., step_type=...)`) so failures localize to a named operation, as in TraceCAD. Even without full persistence, logging step names in stdout makes tracebacks actionable.
- Adopt "minimal edit" discipline: prefer exact text edits / single-step replacements over full-program rewrites; use full rewrites only when a local expression is impossible (TraceCAD's candidate-generation rule).
- Add preservation checks: after a repair, re-run geometry checks and compare salient metrics (volume, bbox) to ensure the repair didn't destroy previously-correct features; reject candidates that regress.
- Add an escalation rule: if the same check fails twice, instruct the Refiner to change construction strategy, not tweak parameters (CADSmith's Judge escalation).

### Gaps
- TraceCAD's numbers are on DeepCAD-derived single-part benchmarks, not on ThinkToCad's mechanism/assembly flow; transfer cost and effectiveness for multi-part assemblies are unverified.
- I found no study comparing structured-JSON feedback vs. free-text feedback for CAD repair; the benefit is inferred from CADSmith/TraceCAD ablations, not isolated.

## Q5: What is "self-healing" CAD and how does it work (Zero-to-CAD repair loop, AgentCAD validation)?

### Takeaway
"Self-healing" CAD spans three layers: (1) kernel-level geometric healing (ShapeFix/ShapeUpgrade fixing invalid B-Reps), (2) authoring-level safe operations and error translation (AgentCAD's `safe_fillet`/`safe_shell`/`safe_bool`, Error Doctor), and (3) agentic repair loops (Zero-to-CAD's generate→execute→validate search; TraceCAD's persistent localized repair; AgentCAD's kernel-as-referee revalidation). The unifying idea: the kernel is the referee and every failure returns as structured data that drives the next edit.

### Cited Findings
- Zero-to-CAD frames synthesis as an "agentic search problem": an LLM embedded in a feedback-driven CAD environment iteratively generates, executes, and validates code using tools and documentation lookup to promote geometric validity and operation diversity. — [arXiv:2604.24479](https://arxiv.org/abs/2604.24479)
- AgentCAD's core bet: "the model is code" and "the kernel is the referee" — every change is validated by real geometry (B-rep validity, volume, mass, bbox, interference) and failures return as structured data (traceback, failing line, hints) for self-correction. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- AgentCAD ships `safe_fillet`/`safe_shell`/`safe_bool` that "survive the common OCCT failures", a scipy constraint solver, and an "Error Doctor" that "rewrites raw OCCT errors into plain-language fixes". — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- FreeCAD `Part.ShapeFix` (Edge/Face/Solid/Shell/Wire/Root) and OpenCASCADE `ShapeFix`/`ShapeUpgrade`/`ShapeAnalysis` provide automatic geometric healing of invalid shapes. — local FreeCAD 1.1; [OCCT docs](https://dev.opencascade.org/doc/refman/html/class_b_rep_check___analyzer.html)
- AgentCAD semantic merges are revalidated by the kernel: a merge that breaks a build, strands an instance, or introduces interference is blocked unless landed deliberately. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- AgentCAD change proposals carry a review packet with kernel-computed geometric diff (added/removed mm³ + overlay solids); merging requires one non-author approval + kernel validation, with overrides recorded. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)

### Inferences
- ThinkToCad already embodies "kernel as referee" in `create_part` ("The kernel is the referee"), but the referee is only invoked at build time, not at validate time. Close the loop: every `validate` call must re-run kernel checks on the exported STEP, not trust the build's success.
- Add a `heal_geometry` step (ShapeFix) as an explicit, logged repair action before declaring a build failed — but record that healing occurred so downstream checks and the LLM know the geometry was modified.
- Adopt AgentCAD's "safe operation" wrappers pattern for common OCCT failures (fillet radius violations, boolean errors) as a first line of defense, with the Error Doctor translating residual errors.
- Add a publish/curate gate analogous to AgentCAD's nine-stage gate for ThinkToCad's Deliver stage: rebuild every part at each declared parameter range, run specs, mate connectors.

### Gaps
- "Self-healing CAD" is not a standardized term; sources use it loosely. I found no benchmark isolating the healing layer's contribution independent of generation quality.
- Zero-to-CAD's actual repair heuristic details (how it decides to retry vs. abandon) are not specified in the abstract; the full PDF would be needed for implementation-level guidance.

## Q6: How do systems validate against standards (GD&T, ISO/ASME drawing standards)?

### Takeaway
Standards validation in AI-CAD is emerging, not mature: the concrete, citable pattern is AgentCAD's PMI/GD&T with tolerance stack-ups plus 2D drawings with projected views and hole callouts detected from geometry, combined with assembly-level spec checks. Broader GD&T rule-checking (feature control frames, datum reference frames, tolerance zones) remains largely manual or tool-specific (FreeCAD drawing workbench, commercial GD&T software).

### Cited Findings
- AgentCAD v3 includes "PMI/GD&T with tolerance stack-ups" and "2D engineering drawings: projected front/top/right/iso views with overall dimensions and hole callouts detected from the geometry, as SVG or DXF." — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- AgentCAD COTS packages follow ISO standards (ISO 4762/4014/7380 screws, DIN 625 bearings, ISO 286 fits via skills). — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- AgentCAD skills include "ISO 286 fits" and "FDM rules" as craft-knowledge guides. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- ASME Y14.5 (GD&T), ASME Y14.41 (digital product definition), ISO 128 (technical drawings), and relevant ISO dimensioning/tolerancing standards are the referenced basis; "no official engineering standard covers the process or format of tolerance analysis and stackups." — [Wikipedia: Tolerance analysis](https://en.wikipedia.org/wiki/Tolerance_analysis)
- ThinkToCad Stage 3 contract captures `constraints` (numbers/stock sizes only, no prose) and `validation` (tool + thresholds); cross-checks against `knowledge/constraints` including manufacturing and standards constraints. — local `WORKFLOW.md`

### Inferences
- For ThinkToCad, "standards compliance" is best scoped as (a) drawing-level checks (views present, dimensions/callouts populated, title block) via FreeCAD's drawing workbench, and (b) fit/tolerance checks via ISO 286 fit tables (hole/shaft tolerance classes) implemented as a lookup in `knowledge/constraints`. Full GD&T rule verification (per ASME Y14.5) is out of scope for an automated kernel and should be a human-review gate.
- Add a `standards` field to the contract listing applicable standards (e.g., ISO 286, ASME Y14.5) and a corresponding check that validates fit classes and dimension callouts exist in the drawing exports.

### Gaps
- I found no open-source, automated GD&T verifier for STEP/B-Rep in the sources; commercial tools (Sigmetrix, 3DCS) handle this but are not citable here. Full ASME Y14.5 compliance checking remains a gap for ThinkToCad.

## Q7: Any patterns for "verification as a service" or "kernel as referee"?

### Takeaway
The dominant pattern is "kernel as referee + verification as a service": geometry is validated by a real kernel (OCCT) exposed through a service boundary (MCP tools, headless CLI, or sandboxed workers), with deterministic pass/fail, structured JSON reports, exit codes, and CI integration. This keeps the LLM honest and makes validation reproducible and auditable.

### Cited Findings
- AgentCAD: "the kernel is the referee" — every agent change validated by real geometry; full tool surface exposed as an MCP server (109 tools) and a built-in chat agent; `agentcad check` is a headless Geometry CI producing a versioned JSON report, markdown summary, and exit code (0 green / 1 model wrong / 2 no verdict), with `--ref` and `--verify-determinism`; a GitHub Action ships in the box. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- ThinkToCad: `create_part` runs code in a sandboxed subprocess and returns `{ok, stdout, stderr, artifacts, ...}`; docstring states "The kernel is the referee." FreeCAD MCP exposes validation as tools (mass, interference, clearance, render, watertight). — local `thinktocad/mcp/build123d_server.py`, `freecad_server.py`
- CAD/CAE Copilot: credibility tiers (critique_finding < surrogate_prediction < proxy_assembly_result < executed_solver_result) stamp every result; mesh accuracy measured (reliable/marginal/unreliable) with optional GCI/Richardson; NAFEMS-style benchmarks in CI. — [GitHub: armpro24-blip/cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot) (cited in prior notes)
- CADSmith: Executor is deterministic with no LLM calls; extracts volume, bbox, COM, face/edge/vertex counts, solid validity directly from OCCT. — [arXiv:2603.26512](https://arxiv.org/abs/2603.26512)
- TraceCAD: validation is mandatory (execution + export + visual) before success; rejected candidates retained as negative evidence; promotion requires agreement of execution, semantic, preservation, and locality evidence. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- AgentCAD sandboxed kernel workers: on macOS scripts run under a deny-by-default `sandbox-exec` profile (write only in project folders + tmp, no network); server binds 127.0.0.1; kernel requests time out and workers auto-respawn. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)

### Inferences
- ThinkToCad should formalize "verification as a service": a single `validate` entry point that (1) runs all geometry checks, (2) runs interference/clearance against other parts, (3) runs sim gates, (4) runs contract specs, and (5) returns one structured report with an overall pass/fail plus per-check details and a repair hint. This mirrors `agentcad check`'s JSON report and exit-code semantics.
- Add determinism verification (`--verify-determinism` equivalent): run the build twice and compare mesh bytes; catches nondeterministic geometry (e.g., unordered set iteration) before delivery.
- Keep the kernel in a separate process (as ThinkToCad already does for build123d) so a segfaulting OCCT call (e.g., boolean on a mesh) cannot kill the agent; add timeouts and auto-respawn (AgentCAD pattern).
- Stamp every verification result with a credibility tier and the kernel version, so downstream consumers (and the LLM) know how much to trust it.

### Gaps
- "Verification as a service" as a hosted/SaaS product is not documented in the cited sources; the pattern here is local service boundaries (MCP/CLI), not cloud-hosted validation. No pricing or multi-tenant model was found.
- I found no source measuring the latency/throughput trade-offs of kernel-as-referee validation in an LLM loop beyond TraceCAD's token/latency tables.