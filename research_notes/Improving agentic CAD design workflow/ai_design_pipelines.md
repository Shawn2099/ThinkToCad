# AI-Assisted Mechanical/CAD Design Pipelines: Workflow Structure and Feedback Loops

## Q1: What stages do AI CAD design systems use (ideation, retrieval, specification, generation, validation, review, delivery)?

### Takeaway
Recent AI CAD systems converge on a common skeleton — requirement capture → (retrieval/knowledge) → parametric code generation → execution validation → (simulation) → human review → artifact delivery — but vary in where they place feedback loops and whether they add "publish/curate", "change-proposal", or "knowledge write-back" stages.

### Cited Findings
- Zero-to-CAD frames synthesis as an "agentic search problem": an LLM embedded in a feedback-driven CAD environment iteratively generates, executes, and validates code using tools and documentation lookup to promote geometric validity and operation diversity — stages: generate → execute → validate, repeated. — [arXiv:2604.24479](https://arxiv.org/abs/2604.24479)
- CADSmith uses a multi-agent pipeline with two nested correction loops: an inner loop resolving execution errors and an outer loop grounded in programmatic geometric validation (exact OpenCASCADE measurements + VLM Judge). — [arXiv:2603.26512](https://arxiv.org/abs/2603.26512)
- TraceCAD adds a recovery layer on top of generation: diagnoses likely faulty operations, searches bounded edits in dependency regions, validates candidates through execution and preservation checks, and retains successful/failed repair outcomes in reusable skill memory. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- CADIR structures generation around an explicit construction graph recording operations, parameter dependencies, constraints, and topology selections, enabling cross-backend reconstruction and construction-graph retrieval for text/image queries (full-graph and subgraph). — [arXiv:2608.00891](https://arxiv.org/abs/2608.00891)
- AgentCAD (n3r/AgentCAD) treats the project as a git repo with branching, semantic merges revalidated by the kernel, and "change proposals" (CAD pull requests) with a governed lifecycle (draft → open → approved/changes-requested → merged/closed), auto-generated review packets, and a publish gate that builds every part at each declared parameter range. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- CAD/CAE Copilot (aieng) pipeline: engineering spec → agent (plan/reason) → MCP tool layer → CAD modeling/editing → CAE setup & simulation → result evaluation → closed-loop optimization, with a human-in-the-loop trust/approval layer and a self-describing `.aieng` package; includes a "Design Study" stage (adjustable dimensions → compare → adopt) that validates/executes/compares candidates without overwriting baseline. — [GitHub: armpro24-blip/cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot)
- MecAgent exposes two modes: live "CAD Agent" (in-session) and "Background CAD Tasks" (longer jobs: drawings from CAD, CAD from drawings/text/STEP) — effectively splitting interactive generation from batch delivery. — [mecagent.com](https://mecagent.com)
- Cosmon PartLab agent loop: clarify → confidence gate → tool loop → reflect (re-fix when safety factor < 2.0), with phase ordering, workflow rules, manufacturing constraints, retry+call budget, trace logging. — [GitHub: supmo668/cosmon-partlab-agent](https://github.com/supmo668/cosmon-partlab-agent)
- CAD-Judge introduces a Compiler-as-a-Judge Module (fast grammatical/validity reward) and a Compiler-as-a-Review Module for test-time verification/refinement, plus an agentic generation approach. — [arXiv:2508.04002](https://arxiv.org/abs/2508.04002)
- Pointer-CAD v2 uses a "Plan-Then-Construct" paradigm: first a structured design plan with explicit metric scale parameters, then sequence generation referencing them via a pointer mechanism. — [arXiv:2606.29301](https://arxiv.org/abs/2606.29301)
- Seek-CAD self-refinement: render the generated parametric model into step-wise perspective images, process with a VLM + CoT feedback, then refine the next round. — [arXiv:2505.17702](https://arxiv.org/abs/2505.17702)
- MIRAGE-CAD mediates generation through an explicit construction-plan interface shared across modalities (text/image/point cloud/STEP), with construction-plan agreement measured separately from execution success. — [arXiv:2608.28669](https://arxiv.org/abs/2608.28669)

### Inferences
- The dominant "new" stages beyond a basic build-validate loop are: (a) a planning/plan-first stage (Pointer-CAD, MIRAGE-CAD), (b) a recovery/repair stage with persistent state (TraceCAD), (c) a design-study/comparison stage (aieng), (d) a publish/curate gate (AgentCAD), and (e) a knowledge write-back stage (ThinkToCad Stage 2/7 and Corpus2Skill-style compiled knowledge).
- Human review is consistently retained as a gate; full automation is explicitly disclaimed (ThinkToCad, aieng, MecAgent approval modes).

### Gaps
- No single paper benchmarks a full 7-stage end-to-end pipeline against ThinkToCad's exact flow; comparisons are partial (geometry validity, not DFM/manufacturability).
- Industry tools (MecAgent, Onshape/PTC AI, Autodesk AI) do not publish stage definitions publicly beyond marketing pages.

## Q2: How do they handle requirement elicitation from non-expert users (sketches, natural language, constraints)?

### Takeaway
Elicitation is moving from free-form text to multimodal (text + image + sketch + point cloud + STEP) inputs plus structured "spec sheets", with explicit dimensions/parameters preferred over vague prompts; several systems add clarification/confidence gates before acting.

### Cited Findings
- CAD-MLLM is the first system generating parametric CAD conditioned on multimodal input: textual description, images, point clouds, or combinations; trained on the Omni-CAD dataset (~450K instances with command sequences). — [arXiv:2411.04954](https://arxiv.org/abs/2411.04954)
- MIRAGE-CAD recovers executable CAD programs from four input types: natural-language descriptions, rendered images, point clouds, and STEP/B-Rep geometry, mapping each to a shared construction representation. — [arXiv:2608.28669](https://arxiv.org/abs/2608.28669)
- MecAgent supports "SPEC-to-CAD" (spec sheet → CAD), "Sketch-to-CAD", "Drawing-to-CAD", "STEP-to-CAD", and "Text-to-CAD" demos; emphasizes explicit dimensions and constraints. — [mecagent.com](https://mecagent.com)
- CADSmith generates CadQuery from natural language with RAG over API docs; targets 100 prompts across 3 difficulty tiers. — [arXiv:2603.26512](https://arxiv.org/abs/2603.26512)
- Cosmon PartLab agent uses a clarify step and a ConfidenceGate (5 subscores → mean ≥ 0.8 to run; aborts after max cycles) before starting the tool loop. — [GitHub: supmo668/cosmon-partlab-agent](https://github.com/supmo668/cosmon-partlab-agent)
- Seek-CAD uses visual + Chain-of-Thought feedback to self-refine, improving alignment with the intended model. — [arXiv:2505.17702](https://arxiv.org/abs/2505.17702)
- CAD/CAE Copilot insists on explicit mechanical specs, dimensions, constraints, and follow-up edits; "the agent executes and verifies the spec; it does not silently fill in the engineering." — [GitHub: armpro24-blip/cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot)
- ThinkToCad Stage 1 captures idea, usage context, sketches/photos, candidate mechanisms, manufacturing context (tools, materials, tolerances, batch size), and standards; outputs a brief.md + open questions + manufacturing profile. — [WORKFLOW.md (ThinkToCad)](https://github.com) (local file: C:\Users\malliath\Desktop\CADResearch\WORKFLOW.md)

### Inferences
- Non-expert elicitation benefits from (a) multimodal inputs, (b) explicit spec sheets over vague prose, (c) clarification/confidence gating, and (d) manufacturing context captured up front (ThinkToCad's DFM-from-day-one principle).

### Gaps
- Limited published detail on how industry tools elicit constraints from non-experts; mostly demo videos.
- No comparative study of elicitation quality across these systems.

## Q3: What is "text-to-code-to-CAD" and how do recent systems (Zero-to-CAD, AgentCAD, MecAgent, Cosmon, Argus) structure the loop?

### Takeaway
"Text-to-code-to-CAD" means generating executable parametric CAD programs (Python/build123d/CadQuery) from natural language, then executing them in a real kernel; recent systems structure this as a generate→execute→validate→repair loop, with some adding plan-first, retrieval, or persistent repair state.

### Cited Findings
- Zero-to-CAD: LLM embedded in a feedback-driven CAD environment iteratively generates, executes, and validates code using tools and documentation lookup; produces ~1M executable sequences; also fine-tunes a VLM for image→CAD program reconstruction. — [arXiv:2604.24479](https://arxiv.org/abs/2604.24479)
- ToolCAD proposes an agentic framework deploying LLMs as tool-using agents for text-to-CAD, with an interactive CAD modeling gym, hybrid feedback, human supervision, and online curriculum RL to evolve CAD-CoT. — [arXiv:2604.07960](https://arxiv.org/abs/2604.07960)
- CADSmith: generates CadQuery from NL, then two nested correction loops — inner resolves execution errors; outer grounded in programmatic geometric validation (exact measurements + VLM Judge); uses RAG over API docs. — [arXiv:2603.26512](https://arxiv.org/abs/2603.26512)
- TraceCAD: recovery layer linking requested features, modeling steps, failure evidence, candidate outcomes as persistent state; diagnoses faulty operations, searches bounded edits, validates via execution + preservation checks, retains outcomes in skill memory. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- AgentCAD: "the model is code" — every part is a parametric Python script; kernel is referee; 109 MCP tools; change proposals with kernel revalidation; publish gate builds every part at each parameter range. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- MecAgent: live CAD Agent + background tasks; works in SolidWorks/Inventor/CATIA/etc.; spec-to-CAD, sketch-to-CAD, drawing-to-CAD, STEP-to-CAD. — [mecagent.com](https://mecagent.com)
- Cosmon PartLab agent: OpenAI-client FEA agent driving PartLab SDK; 7-layer guard pipeline (unknown → retry → budget → phase → schema → workflow_rule → constraint → dispatch); state-threading on success; hard gates (no_save_below_safety_threshold, manufacturing constraints); tenacity retry; confidence gate; trace logging; reflect/re-fix when SF<2.0. — [GitHub: supmo668/cosmon-partlab-agent](https://github.com/supmo668/cosmon-partlab-agent)
- Argus: not located as a public repository or primary source in this research; mentioned as an industry tool in the assignment but no reliable citable details found. — Gap
- MIRAGE-CAD: maps each input to a shared construction representation and mediates program generation through an explicit construction-plan interface; Python CAD code executed by OpenCASCADE to build solid and export STEP. — [arXiv:2608.28669](https://arxiv.org/abs/2608.28669)
- CADIR: agent-friendly executable intermediate representation (OCCT/OCP) with explicit compositional ops and construction graph; cross-backend reconstruction (FreeCAD/SolidWorks/Fusion) via Geometric Signature Matching; construction-graph retrieval. — [arXiv:2608.00891](https://arxiv.org/abs/2608.00891)

### Inferences
- The shift from "single-pass generation" to "generate→execute→validate→repair" is the consensus; the differentiators are (a) whether repair is stateful/persistent (TraceCAD), (b) whether a plan precedes code (Pointer-CAD, MIRAGE-CAD), (c) whether retrieval augments generation (CADSmith RAG, CADIR construction-graph retrieval, ThinkToCad retrieve_knowledge).

### Gaps
- Argus details could not be verified from public sources.
- No benchmark directly compares these loops end-to-end on identical prompts.

## Q4: How do they integrate simulation (FEA, kinematics) into the loop?

### Takeaway
Simulation integration ranges from "optional extra gated by approval" to "inner-loop design variable" (safety factor drives re-fix), with credibility tiering and mesh-accuracy measurement emerging as trust patterns.

### Cited Findings
- CAD/CAE Copilot: CAD → CAE path with material, loads, constraints, mesh, solver artifacts, evidence beside the model; approval-gated actions; V&V-40 credibility tiers (critique_finding < surrogate_prediction < proxy_assembly_result < executed_solver_result); mesh accuracy measured (reliable/marginal/unreliable) with optional GCI/Richardson convergence; NAFEMS-style benchmarks in CI. — [GitHub: armpro24-blip/cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot)
- Cosmon PartLab: agent fixes safety factor under manufacturing constraints; reflects/re-fixes when SF<2.0; manufacturing constraints (thickness ≤ 5.0, hole_diameter ≥ 4.0) enforced as hard gates; tenacity retry on get_safety_factor. — [GitHub: supmo668/cosmon-partlab-agent](https://github.com/supmo668/cosmon-partlab-agent)
- CADEngBench: benchmark evaluating parametric parts through matched linear-static FEA in CalculiX, plus assembly joint retrieval and kinematic verification; stresses that CAD must satisfy design requirements and structural response, not just look right. — [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)
- AgentCAD: linear-static FEM is an optional extra (`agentcad[fem]`); fem_static/modal/thermal tools appear only when installed; geometry CI rebuilds every part and runs interference. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- ThinkToCad Stage 3/5: MATLAB sim gates (torque, stability, traction) must print PASS before build; Validate stage runs FreeCAD interference/clash/clearance/mass/CG/watertight + sim gates; on failure feed structured feedback to LLM and rebuild. — [WORKFLOW.md (ThinkToCad)](C:\Users\malliath\Desktop\CADResearch\WORKFLOW.md)
- Analog Design Bench: long-horizon agentic benchmark where agents design to electrical specification using a simulator; verifier evaluates submitted circuit with specification-based tests; electrical closure is the dominant endpoint challenge. — [arXiv:2609.33356](https://arxiv.org/abs/2609.33356)

### Inferences
- Simulation is most effective when (a) gated by explicit thresholds (SF≥2.0, PASS gates), (b) results are tiered by credibility, and (c) mesh/numerical uncertainty is measured rather than assumed.

### Gaps
- Kinematics integration in AI CAD loops is less documented than FEA; CADEngBench touches joint/kinematic verification but full kinematic optimization loops are sparse in sources.

## Q5: What are "contract-driven" or "spec-driven" design patterns?

### Takeaway
"Contract/spec-driven" design means capturing design intent as executable, measurable constraints (YAML contracts, SPECS lists, design-rule assertions) that the kernel evaluates on every rebuild, so the spec — not the model — is the source of truth.

### Cited Findings
- ThinkToCad Stage 3 "Specify (contract)": contract YAML from template with `name`, `function`, `constraints` (numbers/stock sizes only, no prose), `mechanisms`, `validation` (tool + thresholds), `deliverables`; cross-check against knowledge/constraints; sim gates must PASS. — [WORKFLOW.md (ThinkToCad)](C:\Users\malliath\Desktop\CADResearch\WORKFLOW.md)
- AgentCAD: "Executable design specs" — a `SPECS` list in a part script (`check_wall(min_mm=...)`, `check_mass(max_g=...)`, arbitrary predicates) and project `specs.py` for assembly intent (clearances, interference, tolerance stack-ups); every rebuild evaluates them and reports pass/fail/skip; a proposal whose specs are red (or never evaluated) cannot be merged. Described as "TDD for hardware." — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- CAD/CAE Copilot: "Design-rule assertions" — `require(WALL >= 3, ...)` or bare `assert` in build123d code; violation fails the build deterministically with structured `design_rule_violation`. — [GitHub: armpro24-blip/cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot)
- Pointer-CAD v2: "Plan-Then-Construct" — first a structured design plan with explicit metric scale parameters organized into a dictionary, referenced during sequence generation via a pointer mechanism, eliminating discretization errors. — [arXiv:2606.29301](https://arxiv.org/abs/2606.29301)
- CADIR: construction graph records operations, parameter dependencies, constraints, and topology selections as first-class state; retrieval over full/subgraphs. — [arXiv:2608.00891](https://arxiv.org/abs/2608.00891)
- Corpus2Skill / Knowledge-as-Skill: knowledge organized as navigable skill directories (SKILL.md + index.md + YAML frontmatter) — a "spec" for what the agent may know/load. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572); [arXiv:2609.25991](https://arxiv.org/abs/2609.25991)

### Inferences
- Contract-driven patterns share: (1) machine-checkable constraints, (2) evaluation on every change, (3) blocking merge/delivery on failure, (4) separation of intent (spec) from implementation (model/code).

### Gaps
- The term "contract-driven" is used more in software (API contracts) than in CAD literature; CAD-side equivalents are "spec-driven" or "design-rule assertions." No standardized contract schema across tools.

## Q6: Any novel stages or gates not in a typical Inspect-Specify-Build-Validate-Deliver flow?

### Takeaway
Novel additions include: persistent repair state / skill memory (TraceCAD), design-study candidate comparison (aieng), publish/curate gate (AgentCAD), change proposals with kernel revalidation (AgentCAD), confidence/clarification gating (Cosmon), credibility tiering (aieng), knowledge write-back (ThinkToCad, Corpus2Skill), and Plan-Then-Construct (Pointer-CAD).

### Cited Findings
- TraceCAD: persistent state linking requested features, modeling steps, failure evidence, candidate outcomes; reusable skill memory of successful/failed repairs. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- aieng Design Study: validates/executes/compares/adopts parameterized candidates without overwriting baseline; ranking advisory. — [GitHub: armpro24-blip/cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot)
- AgentCAD publish gate: nine-stage gate building every part at each parameter range and config, running specs, mating connectors; "the gate is the curation." — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- AgentCAD change proposals: governed lifecycle, auto review packet (script/PARAMS diffs, metric deltas, before/after renders, kernel geometric diff), one non-author approval + kernel validation, override recorded. — [GitHub: n3r/AgentCAD](https://github.com/n3r/AgentCAD)
- Cosmon: ConfidenceGate (5 subscores, threshold 0.8, max cycles) before tool loop; phase ordering; workflow rules; manufacturing constraints; call budget. — [GitHub: supmo668/cosmon-partlab-agent](https://github.com/supmo668/cosmon-partlab-agent)
- aieng credibility tiers: every result stamped with ordered tier; production_ready never assumed; mesh accuracy measured. — [GitHub: armpro24-blip/cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot)
- ThinkToCad knowledge growth policy: trusted research + every design (pass/fail) written back to knowledge/ and memory/; graph.yaml updated. — [WORKFLOW.md (ThinkToCad)](C:\Users\malliath\Desktop\CADResearch\WORKFLOW.md)
- CAD-Judge: Compiler-as-a-Judge (fast reward) + Compiler-as-a-Review (test-time verification/refinement). — [arXiv:2508.04002](https://arxiv.org/abs/2508.04002)
- Seek-CAD: visual self-refinement loop (render → VLM+CoT feedback → refine). — [arXiv:2505.17702](https://arxiv.org/abs/2505.17702)
- HERA (harness-environment co-evolution): controlled mutations create feasible/infeasible task pairs for abstention training; co-evolution drives harness adaptation. — [arXiv:2610.06563](https://arxiv.org/abs/2610.06563)

### Inferences
- The most transferable novel gates for ThinkToCad are: (1) persistent repair state (TraceCAD), (2) confidence/clarification gate (Cosmon), (3) design-rule assertions blocking merge (AgentCAD/aieng), (4) credibility tiering on simulation results (aieng), (5) knowledge write-back (already in ThinkToCad, reinforce).

### Gaps
- No evidence that these novel gates compose well together; integration cost unknown.
- Abstention/co-evolution (HERA) not yet applied to CAD design tasks.