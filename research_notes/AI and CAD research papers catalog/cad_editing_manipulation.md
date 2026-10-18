# AI-Assisted CAD Editing, Manipulation, and Modification of Existing CAD Models

## Major papers on CAD editing with AI (2024–2026)

### Takeaway
Text-based/LLM-driven editing of existing CAD models emerged as a distinct task around 2024–2025 (CAD-Editor, FlexCAD) and by 2026 has split into several families: sketch-and-extrude sequence editing, B-rep latent-space editing, geometry-driven parametric editing, and multimodal/stateful agentic editing, with a wave of expert-collected benchmarks (neuralCAD-Edit, RealCADBench, CADEngBench, HistCAD).

### Cited Findings
- CAD-Editor: A Locate-then-Infill Framework with Automated Training Data Synthesis for Text-Based CAD Editing — Yu Yuan, Shizhao Sun, Qi Liu, Jiang Bian; arXiv:2502.03997 (v2 2025-07-03); ICML 2025 (PMLR 267); first framework for text-based CAD editing on sketch-and-extrude sequences; locate-then-infill; https://arxiv.org/abs/2502.03997
- FlexCAD: Unified and Versatile Controllable CAD Generation with Fine-tuned Large Language Models — Zhanwei Zhang, Shizhao Sun, Wenxiao Wang, Deng Cai, Jiang Bian; arXiv:2411.05823 (v2 2025-02-17); ICLR 2025; hierarchy-aware masking for editing at sketch/extrusion/face/loop/curve levels; https://arxiv.org/abs/2411.05823
- CADMorph: Geometry-Driven Parametric CAD Editing via a Plan-Generate-Verify Loop — Weijian Ma, Shizhao Sun, Ruiyu Wang, Jiang Bian; arXiv:2512.11480 (v2 2026-01-05); NeurIPS 2025; edits parametric sequence to match a target shape using P2S diffusion + MPP infilling, no triplet data; https://arxiv.org/abs/2512.11480
- B-repLer: Language-guided Editing of CAD Models — Yilin Liu, Niladri Shekhar Dutt, Changjian Li, Niloy J. Mitra; arXiv:2508.10201 (v4); SIGGRAPH 2026 (ACM DOI 10.1145/3799902.3811166); first text-driven B-rep editing in latent space without construction history; dataset BrepEDIT-240K; https://arxiv.org/html/2508.10201v4
- B-repLer (earlier preprint variant) — same authors; arXiv:2508.10201v1 (2025-08-13); supports delete/add operations; dataset BrepEDIT-10K; https://arxiv.org/html/2508.10201v1
- BrepDiff: Single-stage B-rep Diffusion Model — Mingi Lee, Dongsu Zhang, Clément Jambon, Young Min Kim; SIGGRAPH 2025; diffusion over masked UV grids enabling shape completion, merging, interpolation edits; https://brepdiff.github.io/
- BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry — Xiang Xu et al.; arXiv:2401.15563; supports CAD autocomplete and design interpolation; https://arxiv.org/html/2401.15563v3
- Semantic Direct Modeling — arXiv:2504.13893; LLM + conditional context-sensitive feature recognition mapping natural-language intent to direct B-rep modifications; https://arxiv.org/html/2504.13893v1
- PR-CAD: Progressive Refinement for Unified Controllable and Faithful Text-to-CAD Generation — Jiyuan An et al.; arXiv:2604.19773 (2026-03-27); unifies generation and editing with defined edit operation types (addition/modification/deletion) and qualitative+quantitative instructions; https://arxiv.org/html/2604.19773
- ReliCAD: From Uncertain LLM Generation to Reliable Parametric CAD Modeling — arXiv:2609.22325 (2026-09-16); evidence-driven validation and closed-loop repair for editing; beats CAD-Editor on multi-granularity editing dataset; https://arxiv.org/abs/2609.22325
- LLM4CAD-Editor: An Intent-Aware LLM Framework for Multi-Level CAD Editing — Yuewan Sun, Zhenghui Sha; arXiv:2606.20607 (2026-05-21); IDETC/CIE 2026; DSL-based editing with feature-level entity selection, functional/operation/parameter-level intents; https://sidilab.net/... (preprint)
- TraceCAD: Trace-Guided Repair for Agentic CAD Generation — arXiv:2608.03062 (2026-08-04); localized repair + preservation checks + skill memory; https://arxiv.org/html/2608.03062
- AgenticCADedit: A Stateful, Tool-Mediated Agentic Approach to Multimodal 3D CAD Editing — Saptarshi Neil Sinha et al.; arXiv:2609.29621 (2026-08-28); Fraunhofer IGD/TU Darmstadt/TU Delft; stateful incremental editing via MCP; https://arxiv.org/abs/2609.29621
- neuralCAD-Edit: An Expert Benchmark for Multimodal-Instructed 3D CAD Model Editing — Toby Perrett, Matthew Bouchard, William McCarthy; arXiv:2604.16170 (2026-04-17); Autodesk Research; first expert-collected multimodal editing benchmark; https://autodeskailab.github.io/neuralCAD-Edit/
- eCAD-Net: Editable Parametric CAD Models from dumb B-Rep — Computer-Aided Design journal (2025); deep learning reconstruction of editable parametric models from B-Rep (reverse engineering into editable form); https://www.sciencedirect.com/science/article/abs/pii/S0010448524001337
- HistCAD: Constraint-Aware Parametric History-Based CAD Representation/Dataset/Benchmark — arXiv:2602.19171 (2026-05-29); dimensional edits with preservation; https://arxiv.org/html/2602.19171
- RealCADBench: Benchmarking Parametric CAD Modeling from Industrial Design Intents — arXiv:2609.03773 (2026-09-03); JoyIndustrial; includes assembly track; https://arxiv.org/abs/2609.03773
- CADEngBench: Parametric Design, Assembly Reasoning, Physics Simulation — arXiv:2608.09296 (2026-08-10); 12 edit types, preservation checks, FEA; https://arxiv.org/html/2608.09296
- Nova3D: Code-Native Generation of Programmable 3D Assets — arXiv:2607.22738 (2026-07-22); local edits with locality 18/18 preserved (Blender code-native, not strictly CAD); https://arxiv.org/abs/2607.22738
- CADTalk (mentioned in B-repLer related work) — Yuan et al. 2024; semantic labels for part-wise CAD editing; unverified full citation (flagged).

### Inferences
- The field's center of gravity moved from "controllable generation" (FlexCAD, 2024) to "editing existing models" (CAD-Editor, 2025) to "multimodal expert editing + stateful agents" (neuralCAD-Edit, AgenticCADedit, 2026).
- Construction-history dependence is the main fault line: history-based methods (CAD-Editor) are limited to simple prismatic shapes; B-rep latent methods (B-repLer) target history-free editing of freeform surfaces.

### Gaps
- No single paper I found reports style transfer on CAD (texture/material style) as a primary edit type; most "style" work is in mesh/3D generation, not parametric CAD. Flagged as gap.
- GNN-on-B-rep editing specifically (as opposed to generation/diffusion) is sparsely represented; most B-rep editing uses latent transformers or diffusion, not explicit GNNs. Flagged.

## Edit types (dimension change, feature add/remove, topology edit, style transfer)

### Takeaway
Edit types cluster into: (1) parametric/dimensional changes, (2) feature add/remove/replace, (3) topology/structural edits, (4) geometry-driven shape matching, (5) constraint preservation under edits; "style transfer" is essentially absent from parametric CAD editing literature.

### Cited Findings
- Dimensional/parametric edits: HistCAD defines target dimensional edits (length/radius/diameter/angle/distance) with modification vs. addition of a dimension; cPCSR measures preservation; https://arxiv.org/html/2602.19171
- ReliCAD multi-granularity editing dataset covers "fine-grained dimensional edits, structural-unit edits, and global geometric edits"; https://arxiv.org/abs/2609.22325
- LLM4CAD-Editor covers functional-, operation-, and parameter-level editing intents; https://www.alphaxiv.org/abs/2606.20607
- Feature add/remove: CAD-Editor examples include "Drill four smaller holes", "Remove the cylinder", "Add smaller prisms"; PR-CAD defines Addition/Modification/Deletion of S-E operations or loops; https://arxiv.org/html/2604.19773
- Topology/structural edits: TraceCAD repair families include "topology" and "operation order"; CADEngBench L2-E functional edits include booleans/holes; https://arxiv.org/html/2608.09296
- Geometry-driven edits (shape matching): CADMorph edits parametric sequence to match a target geometric shape while preserving structure; https://arxiv.org/abs/2512.11480
- B-rep edits: B-repLer supports delete/add (and high-level semantic/functional descriptions) on freeform B-Spline surfaces; BrepDiff supports completion, merging, interpolation; https://arxiv.org/html/2508.10201v4
- neuralCAD-Edit captures easy/medium/hard edits expected to take 2/5/10 min by experts; multimodal requests; https://autodeskailab.github.io/neuralCAD-Edit/
- Style transfer: no verified paper in this set treats style transfer as a parametric CAD edit; flagged as gap (likely lives in mesh/texture generation, not CAD).

### Inferences
- "Preservation of non-target geometry" is the implicit edit type that benchmarks (CADEngBench L2-E, HistCAD cPCSR, TraceCAD shape-delta) treat as a first-class requirement, distinct from the requested change.

### Gaps
- Quantitative prevalence of each edit type across datasets not reported in a comparable way; PR-CAD notes editing data is "dominated by add and delete operations, with only a small proportion of quantitative edits" (pre-PR-CAD methods). 

## Methods (LLM code editing, diffusion on CAD, GNN on B-rep)

### Takeaway
Dominant methods: (a) LLMs editing sketch-and-extrude sequences or CadQuery/FreeCAD Python code (locate-then-infill, masking, agentic tool use); (b) diffusion/autoregressive models in B-rep latent space for completion/merging/interpolation; (c) constraint solvers + deterministic kernels for reliable edits; GNN-on-B-rep is mainly a generation/understanding primitive, not a mainstream editing method in these papers.

### Cited Findings
- LLM code/sequence editing: CAD-Editor (LLaMA-3-8B, locate-then-infill), FlexCAD (Llama-3-8B, hierarchy-aware masking), LLM4CAD-Editor (32B model on LLM4CAD-DSL), ReliCAD (LLM + CAD kernel API + verification-feedback repair); https://arxiv.org/abs/2502.03997
- Agentic/stateful: AgenticCADedit runs an LLM inside a persistent CadQuery session via MCP, incremental commits + inspect/revert; TraceCAD wraps an executable CAD agent with persistent recovery state, localized repair, skill memory; https://arxiv.org/abs/2609.29621
- Diffusion on CAD: BrepDiff (single-stage diffusion transformer over masked UV grids, SIGGRAPH 2025) for completion/merging/interpolation; BrepGen (hierarchical tree diffusion); CADMorph orchestrates a P2S latent diffusion model + MPP model in a plan-generate-verify loop; https://brepdiff.github.io/
- B-rep latent editing: B-repLer uses a variational autoregressive transformer directly in HoLa-BRep latent space, no construction history; https://arxiv.org/html/2508.10201v4
- Constraint/kernel-based: HistCAD evaluates constraint sets for dimensional editability; ReliCAD uses geometric constraint solver + Agent-ready API; https://arxiv.org/html/2602.19171
- GNN on B-rep: B-repLer cites entity-level correspondence work (Jones et al. 2023) on B-rep topology; eCAD-Net uses UV-graph encoder-decoder to reconstruct parametric sequences; I did not find a paper whose primary editing method is a GNN on B-rep. Flagged as gap/unverified.

### Inferences
- "Kernel is the referee" pattern (ReliCAD, TraceCAD, CADEngBench) is converging: LLM proposes, CAD kernel executes/validates, preservation checks gate acceptance.

### Gaps
- Whether any editing method uses graph neural networks as the primary editor (vs. generation) — not found in this search; treat as unverified.

## Benchmarks (CAD-Edit, Nova3D, RealCADBench)

### Takeaway
Benchmark landscape for CAD editing expanded rapidly in 2026: neuralCAD-Edit (expert multimodal editing), RealCADBench (industrial intents incl. assemblies), CADEngBench (parametric editing + FEA + assembly joints), HistCAD (constraint-preserving dimensional edits), plus CAD-Editor's own evaluation and FlexCAD's controllability metrics.

### Cited Findings
- neuralCAD-Edit: 192 multimodal requests + 384 edits from 10 expert designers; Fusion Gallery inputs; metrics Chamfer-dist, Voxel-IoU, DINO-sim, validity, human/VLM eval; GPT 5.2 acceptance 0.25 vs human 0.78; https://arxiv.org/abs/2604.16170
- RealCADBench: 12,632 tasks, 19 factory-automation categories, 4 input regimes, Part + Assembly tracks; 1,770-task slice (1,745 Part + RCB-Assm25 25 assemblies); FreeCAD Python; metrics executability, Solid IoU, Surface IoU, visual-semantic Judge; https://arxiv.org/abs/2609.03773
- CADEngBench: 300 parts (gen + edit each = 600 tasks), 12 edit types, hidden preservation checks, L2-E functional edits, L3 FEA; Assembly track 150 body pairs, 7 joint types, face/edge grounding; https://arxiv.org/abs/2608.09296
- HistCAD: 170,236/180,495 parametric histories (Academic+Industrial); metrics ER, cPCSR, OES for dimensional edits with preservation; https://arxiv.org/abs/2602.19171
- CAD-Editor evaluation: generation validity, text-CAD alignment, overall quality on DeepCAD-derived data; https://arxiv.org/abs/2502.03997
- FlexCAD controllability: PV up to 93.4% sketch-level; COV/MMD/JSD; https://arxiv.org/abs/2411.05823
- Nova3D-Bench: 54 items, 6 domains, 3 difficulty levels; 18 local edits with locality preserved 18/18; code-native Blender (not parametric CAD); https://arxiv.org/abs/2607.22738
- "CAD-Edit" as a named benchmark: I did not find a standalone benchmark literally called "CAD-Edit" distinct from CAD-Editor/neuralCAD-Edit; neuralCAD-Edit and CAD-Editor are the closest. Flagged as possibly conflated in the prompt.

### Inferences
- Editing benchmarks now explicitly separate "reachability" (did it execute and hit target) from "preservation" (did non-target geometry/constraints survive), which generation-only benchmarks cannot measure.

### Gaps
- Cross-benchmark comparability is low (different CAD kernels: CadQuery, FreeCAD, Fusion 360, sketch-and-extrude sequences); no common leaderboard.

## "Localized repair" (TraceCAD) and "preservation checks"

### Takeaway
TraceCAD reframes CAD correction as local, evidence-backed edits: diagnose the likely faulty step, restrict edits to a bounded dependency region upstream of it, and promote a patch only when execution, semantic, preservation, and locality evidence all agree. "Preservation checks" verify that previously-correct features/salient unrelated geometry are not damaged (shape-delta), complementing execution and visual checks.

### Cited Findings
- TraceCAD: persistent recovery layer linking requested features, modeling steps, failure evidence, candidate outcomes; arXiv:2608.03062; https://arxiv.org/html/2608.03062
- Localized repair search: dependency graph from variables defined/used per step; repair region R_h(s) = {s} ∪ Upstream(s,h) with small hop budget h; downstream consumers checked after patching, not auto-included, to avoid global edits; https://arxiv.org/html/2608.03062
- Repair families diagnosed: API misuse, invalid parameter, missing feature, operation order, topology, export, visual mismatch; https://arxiv.org/html/2608.03062
- Candidates evaluated as complete programs; execution + required export are hard constraints; feature state and visual feedback test semantics; shape-delta evidence detects damage to salient unrelated geometry; selector favors fewer changed CAD step scopes; promotes only when execution, semantic, preservation, and locality evidence agree; https://arxiv.org/html/2608.03062
- Preservation checks in CADEngBench L2-E: hidden preservation checks R_i^E for geometry that should not change; T_i hidden B-Rep measurement verifies requested outcome; https://arxiv.org/html/2608.09296
- HistCAD preservation: cPCSR measures whether all constraints in C_preserve remain satisfied among reachable edits; https://arxiv.org/html/2602.19171
- neuralCAD-Edit human eval uses instruction-following + model-quality with acceptance threshold; automatic metrics (Chamfer, Voxel-IoU, DINO) are weaker proxies; https://arxiv.org/abs/2604.16170

### Inferences
- "Preservation" is implemented three ways in this literature: (i) shape-delta/geometry checks (TraceCAD), (ii) hidden B-Rep measurement checks (CADEngBench), (iii) constraint-satisfaction checks (HistCAD). Conflating them would overstate agreement.

### Gaps
- Formal geometric equivalence testing (exact) is explicitly noted as not performed by TraceCAD ("shape-delta inspection ... does not constitute exact geometric equivalence testing").

## Papers on editing assemblies

### Takeaway
Assembly editing is the least mature sub-area: RealCADBench and CADEngBench include assembly tracks (placement, joint prediction), neuralCAD-Edit includes single-body and assembly models, and Embodied CAD/ReliCAD touch assemblies, but end-to-end AI editing of multi-part assemblies with joints remains largely unsolved (RealCADBench reports "incorrect assembly placement" as a recurring failure).

### Cited Findings
- RealCADBench Assembly Track: 167 real-picture assembly tasks; RCB-Assm25 25-task study; evaluates components, placement, system structure via Judge; recurring failure "incorrect assembly placement"; https://arxiv.org/abs/2609.03773
- CADEngBench-A: 150 body pairs from Fusion 360 assembly-joint data (Jones et al. 2021); rigid/revolute/slider/cylindrical/pin-slot/planar/ball joints; ranked joint retrieval, exact face-and-edge grounding, joint-frame prediction, kinematic verification; "Assembly predictions often locate the relevant region but fail to recover the recorded joint or mating entities"; https://arxiv.org/abs/2608.09296
- neuralCAD-Edit: input CAD models include "single-body and assembly models, with and without parametric design histories"; edits by experts may include assembly edits; https://autodeskailab.github.io/neuralCAD-Edit/
- Nova3D: parent-child assembly tree, 59 joints across 12 assets, joint pivots; edits preserve non-target content; https://arxiv.org/abs/2607.22738
- AgenticCADedit notes prior "Embodied CAD constructs assemblies from structured specifications through a fixed skill library" but does not study general multimodal assembly editing; https://arxiv.org/abs/2609.29621
- Semantic Direct Modeling and Zookeeper (commercial) mention assembly/feature trees but no verified assembly-editing benchmark; https://arxiv.org/html/2504.13893v1

### Inferences
- Assembly editing lags part editing because joint/mating semantics, placement, and multi-body preservation are harder to verify than single-body geometry; benchmarks are only beginning to formalize these (CADEngBench-A, RealCADBench assembly track).

### Gaps
- No dedicated "assembly editing" benchmark with paired before/after assemblies and edits comparable to neuralCAD-Edit's single-body focus; RealCADBench's assembly slice is only 25 tasks. Flagged as thin evidence.