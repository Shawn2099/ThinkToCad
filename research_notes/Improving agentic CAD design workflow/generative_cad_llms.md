# Generative / Parametric CAD with LLMs (2025-2026): Techniques for Improving ThinkToCad's Build Stage

## Latest text-to-code-to-CAD systems and reported validity/editing scores

### Takeaway
2025-2026 text-to-CAD has converged on "code-as-CAD" (CadQuery/FreeCAD Python/OpenCASCADE) with closed-loop execution+geometry feedback; the best systems report ~100% execution, IoU ~0.96, and Chamfer Distance ~0.7-9.9 depending on prompt difficulty, while agentic critique loops (RA-CAD, CADSmith, TraceCAD) now beat single-pass and proprietary models on execution validity and geometric fidelity.

### Cited Findings
- CADSmith (arXiv:2603.26512): multi-agent CadQuery pipeline with nested loops — inner loop fixes execution errors, outer loop uses OpenCASCADE exact measurements (bbox, volume, solid validity) plus a VLM Judge. On 100 prompts (T1-T3): 100% execution (up from 95%), median F1 0.9846 (from 0.9707), median IoU 0.9629 (from 0.8085), mean Chamfer Distance 0.74 (from 28.37) — [Source](https://arxiv.org/abs/2603.26512).
- RA-CAD (arXiv:2608.05714): ReAct-style Generate-Execute-Critique-Rewrite agent with learnable post-execution critique (trajectory-level GRPO over code+critique), reports SOTA execution validity and geometric quality on CADFusion and Text2CAD vs. strong proprietary LLMs — [Source](https://arxiv.org/abs/2608.05714).
- Seek-CAD (arXiv:2505.17702): first local open-source (DeepSeek-R1) training-free CAD generation with visual+CoT self-refinement; renders step-wise perspective images reviewed by a VLM, accepted at ICLR 2026 — [Source](https://arxiv.org/abs/2505.17702).
- ArtisanCAD (arXiv:2607.05750): industrial agent with CAD-IR intermediate representation + expert skill distillation + CATIA-MCP backend + multi-view visual feedback; on Text2CAD, CAD-IR reduces mean Chamfer Distance from 14.83 to 9.88 on intermediate prompts — [Source](https://arxiv.org/abs/2607.05750).
- MIRAGE-CAD (arXiv:2608.28669): maps text/image/point-cloud/STEP to a shared construction representation then Python/OpenCASCADE code; 55.4-70.0% build success and 52.3-66.2% STEP export success on 2,500 queries/modality without retrieval — [Source](https://arxiv.org/abs/2608.28669).
- Zero-to-CAD (arXiv:2604.24479): agentic synthesis of ~1M executable CAD sequences (rich op vocabulary beyond sketch-extrude) via LLM-in-CAD-environment with tool/doc lookup; VLM fine-tuned on synthetic data outperforms GPT-5.2 on image→CAD reconstruction — [Source](https://arxiv.org/abs/2604.24479).
- Pointer-CAD v2 (arXiv:2606.29301): plan-then-construct paradigm predicting continuous metric-scale params via pointer mechanism, eliminating quantization errors; accepted ECCV 2026 — [Source](https://arxiv.org/abs/2606.29301).
- CAD-MLLM (arXiv:2411.04954): first unified multimodal (text/image/point-cloud) CAD generation via command sequences — [Source](https://arxiv.org/abs/2411.04954).
- Text2CAD (arXiv:2409.17106): first text-to-parametric-CAD for all skill levels, ~170K models / ~660K text annotations on DeepCAD — [Source](https://arxiv.org/abs/2409.17106).
- Text-to-CadQuery (arXiv:2505.06507): direct CadQuery code generation; best model 69.3% top-1 exact match (up from 58.8%), Chamfer Distance reduced 48.6% — [Source](https://arxiv.org/abs/2505.06507).
- STEP-LLM (arXiv:2601.12641): generates STEP (ISO 10303) directly via DFS reserialization + RAG + RL with Chamfer-Distance reward; accepted DATE 2026 — [Source](https://arxiv.org/abs/2601.12641).
- Embodied CAD (arXiv:2606.31252): solver-grounded LLM agents for parametric B-Rep assembly with L0-L4 skill library, action grammar constraints, solver-derived rewards — [Source](https://arxiv.org/abs/2606.31252).
- ConCAD (arXiv:2609.34494): constraint-aware image-to-CAD via GRPO with code-level constraint reward + execution-level geometric reward; best IoU/Chamfer on DeepCAD and Zero2CAD — [Source](https://arxiv.org/abs/2609.34494).
- GACO-CAD (arXiv:2510.17157): two-stage SFT+RL for image-to-CAD using depth/normal priors and a group-length reward for conciseness — [Source](https://arxiv.org/abs/2510.17157).
- Test-time consensus selection (arXiv:2608.09706): verifier-free candidate selection by geometric/topological agreement; geometric consensus improves all three geometric metrics over the method's verifier — [Source](https://arxiv.org/abs/2608.09706).

### Inferences
- For a build123d+FreeCAD stack, the transferable pattern is: generate code → execute in kernel → compute exact metrics (bbox/volume/IoU/CD) → feed back to LLM, matching CADSmith/TraceCAD rather than VLM-only critique.
- Direct code generation (CadQuery/FreeCAD Python) dominates command-sequence representations because it reuses pretrained LLM Python skill and enables tool-use/repair.

### Gaps
- No single paper reports a unified validity+editing score across all systems; numbers come from custom benchmarks (CADSmith's 100-prompt set, Text2CAD, DeepCAD), so cross-system comparison is approximate.

## Parametric editability and design-intent preservation

### Takeaway
Design intent is being tackled at two levels: (a) sketch-level constraint satisfaction (solvers) and (b) construction-graph / IR representations that keep feature history and stable topological references; aligning generated constraints with solver feedback raised fully-constrained sketches from 8.9% to 93%.

### Cited Findings
- "Aligning Constraint Generation with Design Intent in Parametric CAD" (arXiv:2504.13178): adapts LLM alignment (RL with solver feedback) to sketch constraint generation; fully-constrains 93% of sketches vs. 34% SFT and 8.9% no-SFT — [Source](https://arxiv.org/abs/2504.13178).
- CADIR (arXiv:2608.00891): agent-friendly executable IR built on OCCT/OCP recording operations, parameter deps, constraints, topology selections in a construction graph; "Geometric Signature Matching" recovers corresponding edges/faces across parameter changes and backends (FreeCAD, SolidWorks, Fusion 360) — [Source](https://arxiv.org/abs/2608.00891).
- ArtisanCAD CAD-IR (arXiv:2607.05750): encodes parameters, ordered operations, tool bindings, dependencies, generated entities, verification rules; distills expert procedures into reusable skills — [Source](https://arxiv.org/abs/2607.05750).
- B-repLer (arXiv:2508.10201): language-guided editing directly on B-reps in a learned latent space, no construction history needed; BrepEDIT-240K dataset — [Source](https://arxiv.org/abs/2508.10201).
- Pointer-CAD (arXiv:2603.04337): pointer-based entity selection (faces/edges) enabling complex edits (chamfer/fillet) that command sequences cannot express; ~575K annotated models — [Source](https://arxiv.org/abs/2603.04337).
- Zero-shot CAD re-parameterization (arXiv:2306.03217): uses LLM+image models to infer meaningful variation axes and re-parameterize constrained CAD programs for design-space exploration — [Source](https://arxiv.org/abs/2306.03217).
- MIRAGE-CAD (arXiv:2608.28669): notes executable validity, geometric fidelity, and parametric responsiveness can diverge substantially and should be evaluated separately — [Source](https://arxiv.org/abs/2608.28669).

### Inferences
- For ThinkToCad, preserve a construction graph (operations + params + topology IDs) rather than only final code; this enables localized edits and cross-backend portability (FreeCAD import) as in CADIR.
- Add a constraint-solver feedback reward (fully-constrained sketch target) to the Build stage, mirroring arXiv:2504.13178.

### Gaps
- "Design intent" remains loosely defined; only sketch-constraint and construction-graph approaches are operationalized; no metric yet for edit-predictability under parameter perturbation beyond CAD-Edit/CADEngBench (see below).

## Constraint solvers and design-space exploration methods

### Takeaway
Constraint solving is used both as a validator/reward (sketch fully-constrained targets, geometric signature matching) and as the backbone of design-space exploration; LLMs increasingly drive DSE via trace-informed proposer-critic loops, and Z3/Cassowary-style solvers are the standard for sketch constraints, while OCCT kernels provide exact geometric validation.

### Cited Findings
- SketchGen (arXiv:2106.02711): generative CAD sketches as primitive+constraint graphs, with final regularization by a constraint solver — [Source](https://arxiv.org/abs/2106.02711).
- Engineering Sketch Generation (arXiv:2104.09621): CurveGen/TurtleGen generate curve primitives without a sketch constraint solver, explicitly considering topology — [Source](https://arxiv.org/abs/2104.09621).
- Aligning Constraint Generation (arXiv:2504.13178): uses a constraint solver as feedback (reward) to train LLMs to produce fully-constrained sketches — [Source](https://arxiv.org/abs/2504.13178).
- TraceDSE (arXiv:2610.07191): agentic DSE with LLM proposer+critic loop using execution traces; improves hypervolume up to 35% over NSGA-II and 68% over Bayesian optimization with 6-9x fewer evaluations — [Source](https://arxiv.org/abs/2610.07191).
- Zero-shot re-parameterization (arXiv:2306.03217): LLM+image models infer design axes and re-parameterize CAD programs for interactive design-space exploration — [Source](https://arxiv.org/abs/2306.03217).
- Embodied CAD (arXiv:2606.31252): deterministic parameter resolution + solver-derived rewards for GRPO refinement of CAD agents — [Source](https://arxiv.org/abs/2606.31252).

### Inferences
- For ThinkToCad's MATLAB-adjacent stack, expose a constraint solver (e.g., Z3 or OCCT's built-in constraints) as a tool the LLM can query; use solver feasibility as a hard gate before geometry execution.
- Adopt trace-based DSE (TraceDSE-style) for design exploration: richer feedback than aggregate metrics yields better Pareto frontiers with fewer evaluations.

### Gaps
- No paper in this set explicitly couples a numerical optimization (e.g., MATLAB) with LLM CAD generation; the LLM-driven DSE work targets hardware SoCs, not mechanical design spaces.

## Multi-part assemblies and joints

### Takeaway
Assembly generation is emerging as a distinct track: predict joint/connectors before geometry (ArtiCAD), use ranked joint retrieval + kinematic verification (CADEngBench-A), and generate articulated assemblies via multi-agent pipelines (ArtiCAD); joint grounding remains the weakest link.

### Cited Findings
- ArtiCAD (arXiv:2604.10992): first training-free multi-agent system for editable articulated CAD assemblies from text/image; key insight — predict assembly relationships via a "Connector" (attachment points + joint params) during design stage, before geometry generation, bypassing LLM spatial-reasoning limits; includes cross-stage rollback and self-evolving experience store; exports URDF — [Source](https://arxiv.org/abs/2604.10992).
- CADEngBench (arXiv:2608.09296): CADEngBench-A evaluates 150 body pairs via ranked joint retrieval, exact face-and-edge grounding, joint-frame prediction, kinematic verification; models often locate the relevant region but fail to recover the recorded joint/mating entities — [Source](https://arxiv.org/abs/2608.09296).
- MUSE (arXiv:2605.28579): benchmark focused on complex editable B-Rep assemblies with three-stage protocol (code check, geometric check, design-intent alignment including assemblability) — [Source](https://arxiv.org/abs/2605.28579).
- RealCADBench (arXiv:2609.03773): includes Part and Assembly modeling across text/2D drawings/images/rendered images; recurring failures include incorrect assembly placement — [Source](https://arxiv.org/abs/2609.03773).
- "End-to-End Autonomous Generation of Human Assembly Plans" (arXiv:2610.09781): generates assembly plans from mesh assemblies using physics-simulator disassembly + DfA cost function + MLLM manuals; DfA-aware sequence planning reduces simulated assembly time 35% on 136 assemblies (5-30 parts) — [Source](https://arxiv.org/abs/2610.09781).
- Embodied CAD (arXiv:2606.31252): parametric B-Rep assembly modeling with solver-grounded agents — [Source](https://arxiv.org/abs/2606.31252).
- Engineering as Code (arXiv:2609.04216): ADL with Part atom + PDL/PML/PLL sub-languages and ESA static analysis on semantic categories (Family types, Mate relations) rather than geometry; 69 rules checked in <200ms, 100% detection, zero false positives — [Source](https://arxiv.org/abs/2609.04216).

### Inferences
- For ThinkToCad, adopt ArtiCAD's "Connector-first" approach: have the LLM emit explicit joint/attachment parameters before generating geometry, then verify kinematics.
- Use ADL-style mate relations as a machine-checkable intermediate for assemblies, enabling static analysis at design time.

### Gaps
- No open-source assembly benchmark matches Fusion 360 Gallery assembly corpus quality; CADEngBench-A is small (150 pairs) and recent.

## "Design studies" / "design spaces" / "design families" generation

### Takeaway
"Design family" generation appears mainly as parametric families/variants (parameter perturbations, design variants) rather than explicit "design studies"; the closest concepts are parametric families (CADEngBench parameter-family perturbations), design-space exploration (TraceDSE), and design-study generation via expert skill distillation (ArtisanCAD).

### Cited Findings
- CADEngBench (arXiv:2608.09296): evaluates "parameter-family perturbations" — models must respond predictably to parameter changes — [Source](https://arxiv.org/abs/2608.09296).
- Zero-shot re-parameterization (arXiv:2306.03217): turns a single CAD program into a constrained family along meaningful design axes — [Source](https://arxiv.org/abs/2306.03217).
- ArtisanCAD (arXiv:2607.05750): distills expert CATIA recordings into reusable parameterized skills, enabling generation of editable variants for new requests — [Source](https://arxiv.org/abs/2607.05750).
- Foundation Models for Automatic CAD Generation (arXiv:2607.05573): iterative refinement over "four canonical geometry families" with analytic visual metrics; 98.97% mesh success — [Source](https://arxiv.org/abs/2607.05573).
- DesignQA (arXiv:2404.07917): evaluates MLLMs on engineering-document-grounded design rules (comprehension/compliance/extraction) — [Source](https://arxiv.org/abs/2404.07917).
- Nova3D (arXiv:2607.22738): code-native generation exposing named parts in parent-child assembly tree, 51/52 numeric constraints satisfied, 14/18 local edits pass — [Source](https://arxiv.org/abs/2607.22738).

### Inferences
- ThinkToCad can implement "design families" as: one base parametric program + sampled parameter vector + constraint-solver feasibility check + rendered variants, which directly supports design studies/exploration.
- Skill distillation (ArtisanCAD) is transferable: log expert build123d scripts as reusable parameterized skills.

### Gaps
- I found no paper explicitly titled "design studies" generation for CAD; the concept is distributed across parametric families, DSE, and skill distillation. (No reliable source on a standardized "design study" artifact.)

## Visual feedback loops (render → critique → revise)

### Takeaway
Visual feedback has matured from single VLM critique to structured, multi-modal, and analytic feedback: best results combine exact kernel measurements (CADSmith) with VLM holistic judgment, and learnable critique policies (RA-CAD) outperform fixed critics.

### Cited Findings
- CADSmith (arXiv:2603.26512): outer loop combines exact OpenCASCADE measurements (bbox/volume/solid validity) with independent VLM Judge holistic assessment — [Source](https://arxiv.org/abs/2603.26512).
- Seek-CAD (arXiv:2505.17702): renders step-wise perspective images; VLM + CoT from DeepSeek-R1 assess generation; first to combine visual + CoT feedback in self-refinement — [Source](https://arxiv.org/abs/2505.17702).
- RA-CAD (arXiv:2608.05714): Generate-Execute-Critique-Rewrite with critique as a learnable policy action (GRPO), not unoptimized auxiliary output — [Source](https://arxiv.org/abs/2608.05714).
- ArtisanCAD (arXiv:2607.05750): multi-view visual feedback for iterative refinement — [Source](https://arxiv.org/abs/2607.05750).
- CADReview/ReCAD (arXiv:2505.22304): MLLM-based CAD program review with error detection and correction vs. reference images — [Source](https://arxiv.org/abs/2505.22304).
- Foundation Models for CAD (arXiv:2607.05573): IterTracer analytic renderer (silhouette IoU, hole visibility, edge clearance, aspect ratio) vs. IterVision VLM semantic critic (Qwen2.5-VL-72B); VLM critique achieved 100% watertight meshes — [Source](https://arxiv.org/abs/2607.05573).
- GReFEM (arXiv:2607.08798): MLLM as zero-shot semantic assistant for FEM mesh refinement from rendered views (orthoViews) — [Source](https://arxiv.org/abs/2607.08798).
- GACO-CAD (arXiv:2510.17157): depth/normal maps as dense geometric priors for image-to-CAD — [Source](https://arxiv.org/abs/2510.17157).
- CAD-Judge (arXiv:2508.04002): Compiler-as-a-Judge (fast, no rendering) + Compiler-as-a-Review for efficient verification; avoids expensive VLM rendering/reward hacking — [Source](https://arxiv.org/abs/2508.04002).

### Inferences
- For ThinkToCad, combine (a) exact OCCT/build123d measurements as primary reward, (b) optional VLM critique for holistic shape, (c) make critique a learned/optimized policy step rather than fixed prompt, as in RA-CAD.

### Gaps
- No paper benchmarks render→critique→revise iteration counts or convergence rates; mostly final-quality metrics reported.

## Benchmarks and metrics (CAD-Edit, CAD-Coder, Fusion 360 Gallery, DeepCAD, etc.)

### Takeaway
The benchmark landscape exploded in 2025-2026: beyond DeepCAD/Fusion 360 Gallery/ABC/CC3D, new benchmarks (CADEngBench, RealCADBench, Text2CAD-Bench, MUSE, BenchCAD, ComCADBench, UniCAD, CADReview dataset) add editing, assembly, physics (FEA), and industrial-readiness evaluation; CAD-Edit/CAD-Coder as named benchmarks were not found in this search.

### Cited Findings
- DeepCAD (canonical): command-sequence dataset; basis for Text2CAD annotations and many evaluations — referenced by Text2CAD (arXiv:2409.17106) and ConCAD (arXiv:2609.34494).
- Fusion 360 Gallery (canonical): used by UniCAD (arXiv:2606.05058) as benchmark — [Source](https://arxiv.org/abs/2606.05058).
- ABC / CC3D: standard B-Rep/geometry datasets (referenced broadly; e.g., BRepCLIP (arXiv:2606.05515) on ABC) — [Source](https://arxiv.org/abs/2606.05515).
- CADEngBench (arXiv:2608.09296): 300 parts × 2 tasks (zero-to-CAD + functional editing) = 600 tasks; B-Rep validity, engineering/DFM checks, parameter-family perturbations, functional editing, matched linear-static FEA (CalculiX); 150 body pairs for joint retrieval/grounding/kinematics — [Source](https://arxiv.org/abs/2608.09296).
- RealCADBench (arXiv:2609.03773): 12,632 tasks / 19 factory-automation categories; text/2D drawings/images/rendered images; Part+Assembly; metrics: executability, Solid IoU, Surface IoU, rubric-based VLM Judge; 1,770-task eval slice — [Source](https://arxiv.org/abs/2609.03773).
- Text2CAD-Bench (arXiv:2605.18430): 600 human-curated examples across 4 complexity levels (L1-L4) with dual-style prompts (geometric vs procedural) — [Source](https://arxiv.org/abs/2605.18430).
- MUSE (arXiv:2605.28579): B-Rep assemblies; three-stage protocol (code check, geometric check, design-intent alignment via rubrics for functionality/manufacturability/assemblability); rubric-based VLM judge validated by human annotation — [Source](https://arxiv.org/abs/2605.28579).
- BenchCAD (arXiv:2605.10865): 17,900 execution-verified CadQuery programs across 106 industrial part families; VQA, code QA, image-to-code, instruction-guided editing — [Source](https://arxiv.org/abs/2605.10865).
- ComCADBench (arXiv:2606.13239): benchmark for agents operating real industrial CAD software via COM; frontier models near-zero under GUI, large gains under COM execution — [Source](https://arxiv.org/abs/2606.13239).
- UniCAD (arXiv:2606.05058): unified multi-modal multi-task benchmark (point-to-CAD, text/image-to-CAD, CAD QA) — [Source](https://arxiv.org/abs/2606.05058).
- CADReview dataset (arXiv:2505.22304): >20K program-image pairs with diverse errors for review/correction — [Source](https://arxiv.org/abs/2505.22304).
- Nova3D-Bench (arXiv:2607.22738): 54 items × 6 domains × 3 difficulty levels; metrics: executable+valid artifact, numeric/count constraints (51/52), local edits (14/18), joints (59 at 98.3% validity) — [Source](https://arxiv.org/abs/2607.22738).
- Common metrics across these: execution/validity rate, Solid IoU, Surface IoU, Chamfer Distance, Hausdorff distance, F1, G-CSR (geometric constraint satisfaction rate), Judge/VLM scores, parametric responsiveness, FEA match, edit success.

### Inferences
- For ThinkToCad evaluation, adopt a multi-metric suite (execution, Solid/Surface IoU, Chamfer, constraint-satisfaction, edit success, FEA) rather than IoU alone, per MIRAGE-CAD/RealCADBench findings that these diverge.

### Gaps
- "CAD-Edit" and "CAD-Coder" named benchmarks were not located in this search; if they exist they may be subsets/aliases of Text2CAD/CADFusion. No reliable source found — flagged as a gap. Fusion 360 Gallery and DeepCAD remain the canonical geometry corpora but lack construction-history labels (motivating Zero-to-CAD).