# CAD Benchmarks, Evaluation Metrics, and Testing Frameworks for AI-Generated CAD

Research notes compiled from arXiv (2024-2026). Findings are drawn from paper abstracts; full-text verification was not performed. Entries marked (unverified) where details could not be confirmed.

## Key Question 1: Major CAD Benchmarks (2024-2026)

### Takeaway
The 2024-2026 period saw a rapid proliferation of CAD benchmarks spanning text-to-CAD, image-to-CAD, mesh/point-cloud-to-CAD, and multimodal CAD program generation, with a shift from purely geometric metrics (IoU/Chamfer) toward execution validity, design-intent rubrics, and VLM-based judges. Unified multimodal benchmarks (CADBench, BenchCAD) and industrial-intent benchmarks (RealCADBench, MUSE) are the newest trend.

### Cited Findings
- **CADBench** (arXiv 2605.10873) — unified multimodal benchmark for CAD program generation: 18,000 eval samples across six benchmark families derived from DeepCAD, Fusion 360, ABC, MCB, Objaverse; five input modalities (clean meshes, noisy meshes, single-view renders, photorealistic renders, multi-view renders); six metrics covering geometric fidelity, executability, program compactness. Benchmarks 11 VLM systems; >1.4M programs generated. Repo: https://github.com/anniedoris/CADBench — [arXiv](https://arxiv.org/abs/2605.10873)
- **BenchCAD** (arXiv 2605.10865) — industry-standard benchmark: 17,900 execution-verified CadQuery programs across 106 industrial part families (bevel gears, compression springs, twist drills, etc.); tasks: VQA, code QA, image-to-code, instruction-guided code editing; evaluates 10+ frontier models. — [arXiv](https://arxiv.org/abs/2605.10865)
- **RealCADBench** (arXiv 2609.03773) — intent-to-program CAD from real industrial design intents: 12,632 tasks from 19 factory-automation categories; text, 2D engineering drawings, real product pictures, rendered images; Part + Assembly modeling; 1,770-task eval slice (1,745 Part + RCB-Assm25 25-task assembly study); outputs FreeCAD API Python executed by shared runtime; metrics: executability, Solid IoU, Surface IoU, rubric-based visual-semantic identity Judge. — [arXiv](https://arxiv.org/abs/2609.03773)
- **MUSE** (arXiv 2605.28579) — Text-to-CAD benchmark for complex editable B-Rep assemblies: three-stage protocol (code check, geometric check, design-intent alignment); final stage uses design-specific rubrics for functionality, manufacturability, assemblability; VLM-based judge validated by human annotation. Website: https://dong7313.github.io/muse-benchmark/ — [arXiv](https://arxiv.org/abs/2605.28579)
- **Text2CAD-Bench** (arXiv 2605.18430) — LLM-based text-to-parametric CAD: 600 human-curated examples across four levels (L1-L2 fundamental geometry, L3 complex topology/freeform surfaces, L4 real-world domains beyond mechanical parts); dual-style prompts (geometric descriptions for non-experts + procedural sequences for experts). — [arXiv](https://arxiv.org/abs/2605.18430)
- **CADENA-Bench** (arXiv 2608.00799) — benchmark for reverse-engineering methods on mechanical parts; measures performance across categories of mechanical parts; HuggingFace: https://huggingface.co/datasets/kulibinai/cadena-bench — [arXiv](https://arxiv.org/abs/2608.00799)
- **ComCADBench** (arXiv 2606.13239) — first benchmark for agents operating real industrial CAD software via COM-as-Action paradigm. — [arXiv](https://arxiv.org/abs/2606.13239)
- **CADENA-Bench / CADBench / BenchCAD** used as evaluation targets in CADFather (arXiv 2610.09127), which also evaluates on full DeepCAD, Fusion360, MCB test sets. — [arXiv](https://arxiv.org/abs/2610.09127)
- **CADGenBench** (mentioned in arXiv 2610.04116) — CAD generation benchmark used to evaluate harnesses. — [arXiv](https://arxiv.org/abs/2610.04116)
- **GERD / GERD-EVL** (arXiv 2609.22688) — Geometry Explicit Reference Dataset: aligned commands, geometry states and IDs at every modeling step; used to evaluate Vision2CAD. — [arXiv](https://arxiv.org/abs/2609.22688)
- **OpenRealCAD** (arXiv 2608.30617) — four-view photographs of 392 3D-printed objects paired with ground-truth command sequences; real-domain image-to-CAD. — [arXiv](https://arxiv.org/abs/2608.30617)
- **DeepCAD-240** (arXiv 2603.21978) — extended benchmark increasing sequence length from 40 to 240 commands, preserving sketch-extrusion semantics from ABC dataset. — [arXiv](https://arxiv.org/abs/2603.21978)
- **Text2CAD dataset** (arXiv 2409.17106) — ~170K models, ~660K text annotations; beginner-to-expert prompts; used as base for Text-to-CadQuery (170K CadQuery annotations added). — [arXiv](https://arxiv.org/abs/2409.17106)
- **BlenderLLM / CADBench (Blender)** (arXiv 2412.14203) — evaluation suite for LLM CAD script generation in Blender. — [arXiv](https://arxiv.org/abs/2412.14203)
- **BIM-Edit** (arXiv 2606.20146) — 324 editing tasks spanning 11 building models + 36 synthetic scenes for IFC-based BIM editing; three instruction categories (direct, spatial, topological); metrics: geometric accuracy, semantic validity, topological consistency. Best model only 49.5% avg, <3.4% fully solved. — [arXiv](https://arxiv.org/abs/2606.20146)
- **CADFusion / Text2CAD** used as eval targets in RA-CAD (arXiv 2608.05714). — [arXiv](https://arxiv.org/abs/2608.05714)

### Inferences
- Benchmark design is moving from "single metric on synthetic data" to multi-metric, multi-modality, real-industrial-intent evaluation; execution validity is now treated as a hard gate before geometric scoring.
- Assembly-level and manufacturability evaluation (MUSE, RealCADBench) is emerging as the frontier beyond single-part shape matching.

### Gaps
- No central registry of CAD benchmarks; naming overlap (CADBench vs BenchCAD vs CAD-GEN) creates confusion. Sizes/eval slices for some benchmarks (BenchCAD 17,900; CADBench 18,000) are similar but disjoint — direct comparability unverified.
- Whether any benchmark has a held-out test set with public leaderboard beyond MUSE's website is not confirmed.

## Key Question 2: Datasets

### Takeaway
Core datasets are DeepCAD (procedural sketch-extrude, ~170K-1M models), Fusion 360 Gallery (human-designed, richer operations), ABC (B-rep, large-scale), CC3D (real scanned 3D), MCB (mechanical parts), Objaverse (general 3D), plus newer curated sets (CADEvolve 8K complex parts, CADEvolve 1.3M scripts, STEP-caption ~40K, Text2CAD ~170K annotated, OpenRealCAD 392 objects, CADENA-Bench). HuggingFace hosts several (cadena-bench, RealCAD).

### Cited Findings
- **DeepCAD** — procedural sketch-and-extrude sequences derived from ABC; widely used base dataset (~170K models in Text2CAD annotation; ~180K DeepCAD subset of ABC in STEP-Parts). Used by CAD-Recode, CADFit, PrimitiveCAD, ConCAD, TraceCAD, RA-CAD, etc. — [arXiv refs: 2412.14042, 2605.01171, 2609.34494, 2608.03062, 2608.05714]
- **Fusion 360 Gallery** — Autodesk dataset of human-designed parametric CAD (sketch/extrude/revolve/etc.); used as benchmark target in CADFather, CADReasoner, SightCAD, PrimitiveCAD, cadrille. — [arXiv refs: 2610.09127, 2603.29847, 2610.11954, 2610.08698, 2505.22914]
- **ABC** — large-scale B-rep dataset; source for DeepCAD; used in STEP-Parts (~180K models), TG-Diff, CADBench, GeoFusion-CAD (DeepCAD-240 from ABC). — [arXiv refs: 2604.14927, 2607.21928, 2605.10873, 2603.21978]
- **CC3D** — real scanned 3D shapes; used by CAD-Recode for real-world evaluation. — [arXiv 2412.14042]
- **MCB** (Mechanical Components Benchmark) — mechanical parts; used in CADFather, CADReasoner, SightCAD, CADBench, CADFit, CADEvolve. — [arXiv refs: 2610.09127, 2603.29847, 2610.11954, 2605.10873, 2605.01171, 2602.16317]
- **Objaverse** — general 3D objects; family in CADBench. — [arXiv 2605.10873]
- **Text2CAD** — ~170K models with ~660K text annotations (beginner-to-expert); base for Text-to-CadQuery (170K CadQuery annotations). — [arXiv 2409.17106, 2505.06507]
- **CADEvolve** — 8k complex parts as executable CadQuery parametric generators; after augmentation 1.3M scripts with rendered geometry. — [arXiv 2602.16317]
- **STEP-caption** — ~40K STEP-caption pairs for text-to-STEP. — [arXiv 2601.12641]
- **OpenRealCAD** — 392 3D-printed objects, four-view photos + ground-truth command sequences. — [arXiv 2608.30617]
- **CADENA-Bench** — HuggingFace dataset for reverse-engineering eval. — [arXiv 2608.00799, https://huggingface.co/datasets/kulibinai/cadena-bench]
- **RealCAD (dataset)** — ModelScope: https://www.modelscope.cn/datasets/yeguomao/RealCAD — [arXiv 2608.30617]
- **BlendNet** — BlenderLLM training dataset for Blender CAD scripts. — [arXiv 2412.14203]
- **T-LESS, MP6D** — industrial metal-parts benchmarks used in SightCAD (real images). — [arXiv 2610.11954]

### Inferences
- DeepCAD remains the de facto standard evaluation substrate; most reported numbers are on DeepCAD-derived splits, which may inflate comparability but limit industrial realism (noted by RealCAD, RealCADBench, MUSE).
- A parameter-frequency prior in DeepCAD (local normalization concentrating params) can make parameter accuracy misleading — flagged by RealCAD (arXiv 2608.30617).

### Gaps
- Exact sizes/versions of Fusion 360 Gallery and ABC (model counts) not verified from abstracts.
- License/terms and download locations for several datasets (e.g., Fusion 360 Gallery) not stated in these papers.

## Key Question 3: Metrics

### Takeaway
Metrics cluster into (a) execution validity, (b) geometric fidelity (IoU variants, Chamfer distance, Hausdorff), (c) sequence/structural fidelity (ECD, mAP of CAD sequence, edit success), (d) design-intent/constraint metrics (G-CSR), and (e) judge-based scores (VLM judge, visual-semantic identity). No single metric dominates; RealCADBench explicitly shows leaders differ across metrics.

### Cited Findings
- **Execution rate / code validity / executability** — whether generated program runs; reported by RealCADBench, MUSE (code check), CADFather, SightCAD (invalid-code rate ≤1.5%), cadrille, ConCAD, PrimitiveCAD, CADFit (Invalid Ratio), GACO-CAD, etc. — [arXiv 2609.03773, 2605.28579, 2610.09127, 2610.11954, 2505.22914, 2609.34494, 2610.08698, 2605.01171, 2510.17157]
- **Solid IoU / Surface IoU** — volumetric/surface overlap; RealCADBench reports Solid IoU 0.2841-0.5379, Surface IoU 0.112-0.217 across models. — [arXiv 2609.03773]
- **Chamfer Distance (CD)** — point-cloud distance between generated and GT geometry; used almost universally (ArtisanCAD: CD 14.83→9.88; ConCAD best CD; CADFit volumetric IoU + CD; TraceCAD; RA-CAD terminal reward). — [arXiv 2607.05750, 2609.34494, 2605.01171, 2608.03062, 2608.05714]
- **Hausdorff Distance (HD)** — used in TraceCAD, PS-CAD (geometry errors). — [arXiv 2608.03062, 2405.15188]
- **F1** — DeciCAD reports F1 + IoU; RA-CAD terminal F1 + Chamfer reward. — [arXiv 2610.21755, 2608.05714]
- **IoU (general)** — widely reported (DeciCAD best F1 & IoU; SightCAD +6.4 IoU; UniBRep valid B-reps 80.49%). — [arXiv 2610.21755, 2610.11954, 2610.04092]
- **G-CSR (B-rep geometric constraint satisfaction rate)** — ConCAD introduces: analytically extracts and evaluates geometric constraints from B-reps; measures design intent beyond volume. — [arXiv 2609.34494]
- **ECD (structural error metric)** — PS-CAD reports ~15% structural error reduction (ECD). — [arXiv 2405.15188]
- **mAP of CAD Sequence** — TransCAD proposes mean Average Precision of CAD sequence to address limitations of existing metrics. — [arXiv 2407.12702]
- **Edit success / parameter-editing** — Vision2CAD parameter-editing experiments; RealCADBench judge. — [arXiv 2609.22688, 2609.03773]
- **Judge (visual-semantic identity)** — RealCADBench rubric-based visual-semantic identity Judge; MUSE design-intent rubrics; CAD-Judge morphological grading. — [arXiv 2609.03773, 2605.28579, 2508.04002]
- **COV / MMD / JSD** — distribution metrics for B-rep generation (TG-Diff on DeepCAD/ABC). — [arXiv 2607.21928]
- **Face Chamfer distance** — UniBRep reduces face CD 0.1096→0.0345. — [arXiv 2610.04092]
- **Program compactness** — CADBench metric. — [arXiv 2605.10873]

### Inferences
- Metric choice materially changes model rankings (CADBench, RealCADBench both note rankings change across metrics); reporting only IoU is insufficient.
- Geometric metrics alone can be gamed by parameter-frequency priors (RealCAD) and by volumetrically-similar-but-structurally-different shapes (ConCAD/G-CSR).

### Gaps
- Standardized definitions/thresholds for "validity" (e.g., kernel execution success vs. watertightness vs. manifoldness) vary across papers; not harmonized.
- No consensus on assembly-level metrics beyond MUSE's rubric judge.

## Key Question 4: Evaluation Frameworks

### Takeaway
Three judge paradigms dominate: (1) compiler-as-judge (execution-based validity + geometric computation), (2) VLM-as-judge (visual-semantic/design-intent rubrics), and (3) hybrid (CAD-Judge combines Compiler-as-a-Judge Module + agentic Compiler-as-a-Review Module). CAD-Judge (arXiv 2508.04002) is the canonical named framework; MUSE and RealCADBench implement VLM-judge variants.

### Cited Findings
- **CAD-Judge** (arXiv 2508.04002) — verifiable reward system for Text-to-CAD preference grading + grammatical validation; **Compiler-as-a-Judge Module (CJM)** as fast direct reward signal optimizing alignment via prospect theory; **Compiler-as-a-Review Module (CRM)** for efficient verification and refinement in testing; agentic CAD generation approach. — [arXiv](https://arxiv.org/abs/2508.04002)
- **Compiler-as-judge** (general) — execution of generated code in CAD kernel (FreeCAD/CadQuery/build123d) to check validity and compute geometry; used by RealCADBench (shared FreeCAD runtime), CADBench, BenchCAD, MUSE (code check). — [arXiv 2609.03773, 2605.10873, 2605.10865, 2605.28579]
- **VLM-as-judge** — MUSE uses rubric-based VLM judge validated by human annotation for design-intent alignment; RealCADBench uses visual-semantic identity Judge; SightCAD scores by geometric fidelity of executed solid via VLM-generated code. — [arXiv 2605.28579, 2609.03773, 2610.11954]
- **Agentic evaluation loops** — CADFather, TraceCAD, RA-CAD, CADReasoner, DeciCAD use generate-execute-critique-rewrite loops with execution feedback; RA-CAD makes critique a learnable policy decision. — [arXiv 2610.09127, 2608.03062, 2608.05714, 2603.29847, 2610.21755]
- **RL with geometric rewards** — ConCAD (GRPO with code-level constraint + execution-level geometric rewards), cadrille (GRPO), RA-CAD (trajectory-level GRPO with terminal F1/CD rewards). — [arXiv 2609.34494, 2505.22914, 2608.05714]
- **3DVerifierBench** (arXiv 2610.22360) — adjacent: benchmark for verification of 3D content (decisions, rejection explanations, responses to controlled spec changes); 10 tasks, 14,126 training examples; human-model gap 21.6 pts. Not CAD-specific but relevant to CAD verification. — [arXiv](https://arxiv.org/abs/2610.22360)

### Inferences
- The kernel-as-referee invariant (execution never raises into the loop; tools return structured errors) is echoed across frameworks; compiler-as-judge is the dominant validity gate.
- VLM judges are used for semantic/design-intent scoring where geometry metrics are insufficient, but reliability (reward hacking, cost) is an acknowledged concern (CAD-Judge).

### Gaps
- No standardized, shared evaluation harness across benchmarks; each paper implements its own execution sandbox — cross-benchmark comparability unverified.
- Cost/latency of VLM-as-judge at scale not quantified in most papers.

## Key Question 5: Surveys on CAD Evaluation

### Takeaway
No survey dedicated solely to CAD evaluation/benchmarks was found. The closest are: "Geometric Deep Learning for Computer-Aided Design: A Survey" (arXiv 2402.17695, 2024) covering datasets/benchmarks across CAD tasks; "A Survey of AI Methods for Geometry Preparation and Mesh Generation" (arXiv 2512.23719); "A Survey of Methods for Converting Unstructured Data to CSG Models" (arXiv 2305.01220); and a recent position paper on AI+CAD data representation (arXiv 2606.16797). Survey coverage of evaluation methodology specifically is thin.

### Cited Findings
- **Geometric Deep Learning for CAD: A Survey** (arXiv 2402.17695) — overview of learning-based CAD methods across similarity/retrieval, 2D/3D CAD synthesis, CAD from point clouds/images; includes complete list of benchmark datasets and characteristics + open-source codes. 28 pages. — [arXiv](https://arxiv.org/abs/2402.17695)
- **AI Methods for Geometry Preparation and Mesh Generation** (arXiv 2512.23719) — survey of AI in CAD-to-mesh pipeline; touches benchmarks/data challenges. — [arXiv](https://arxiv.org/abs/2512.23719)
- **Survey: Converting Unstructured Data to CSG Models** (arXiv 2305.01220) — covers CSG recovery methods, segmentation, fitting; not evaluation-focused. — [arXiv](https://arxiv.org/abs/2305.01220)
- **AI+CAD Data Representation Architecture** (arXiv 2606.16797) — position paper analyzing gaps between DeepCAD and industrial parametric feature modeling (WHUCAD); discusses data representation rather than eval. — [arXiv](https://arxiv.org/abs/2606.16797)
- **CAD-Judge** (arXiv 2508.04002) — contains comparative discussion of evaluation efficiency/reward hacking in Text-to-CAD. — [arXiv](https://arxiv.org/abs/2508.04002)

### Inferences
- The field lacks a dedicated survey on CAD evaluation/benchmarks; the 2024 GDL survey is the closest but predates most 2025-2026 benchmarks (MUSE, RealCADBench, CADBench, BenchCAD, CADENA-Bench, etc.).
- A new survey is warranted given the benchmark explosion in 2025-2026.

### Gaps
- No survey found covering evaluation metrics standardization, VLM-judge reliability, or cross-benchmark comparability for AI-generated CAD.
- Whether any of these surveys has a 2026 update is unverified.

---

## Appendix: Quick Reference Table

| Benchmark | Year | Size | Source/Domain | Key Metrics | arXiv |
|---|---|---|---|---|---|
| DeepCAD (dataset) | 2021 | ~170K-1M | ABC-derived sketch-extrude | CD, IoU, validity | 2409.17106 (Text2CAD) |
| Fusion 360 Gallery | — | human-designed | Autodesk parametric | CD, IoU, validity | multiple |
| ABC | — | large-scale B-rep | analytic B-reps | CD, IoU | multiple |
| CC3D | — | real scans | scanned 3D | CD, IoU | 2412.14042 |
| MCB | — | mechanical parts | mechanical | CD, IoU, validity | multiple |
| Text2CAD | 2024 | ~170K models / ~660K prompts | DeepCAD-derived | CD, IoU, validity | 2409.17106 |
| CADBench | 2026 | 18,000 samples | DeepCAD/Fusion360/ABC/MCB/Objaverse | geom fidelity, executability, compactness | 2605.10873 |
| BenchCAD | 2026 | 17,900 programs | 106 industrial families | VQA, code QA, image-to-code, edit | 2605.10865 |
| RealCADBench | 2026 | 12,632 tasks (1,770 eval) | factory-automation | executability, Solid/Surface IoU, Judge | 2609.03773 |
| MUSE | 2026 | — | B-Rep assemblies | code/geometric/design-intent | 2605.28579 |
| Text2CAD-Bench | 2026 | 600 examples | 4 complexity levels | geom precision, accuracy | 2605.18430 |
| CADENA-Bench | 2026 | — | mechanical parts | reverse-engineering | 2608.00799 |
| ComCADBench | 2026 | — | real CAD software | success rate | 2606.13239 |
| GERD/GERD-EVL | 2026 | — | stepwise CAD | mIoU, CD | 2609.22688 |
| OpenRealCAD | 2026 | 392 objects | 3D-printed + 4 views | command/param accuracy | 2608.30617 |
| DeepCAD-240 | 2026 | long sequences 40-240 | ABC-derived | geom fidelity, topology | 2603.21978 |
| CADENA (dataset) | 2026 | — | mechanical | reverse-eng | 2608.00799 |
| CADEvolve | 2026 | 8K parts / 1.3M scripts | complex CadQuery | CD, IoU, validity | 2602.16317 |
| STEP-caption | 2026 | ~40K pairs | STEP models | CD, renderability | 2601.12641 |
| BIM-Edit | 2026 | 324 tasks | IFC buildings | geom/semantic/topological | 2606.20146 |
| BlenderLLM/CADBench | 2024 | — | Blender scripts | functionality, accuracy | 2412.14203 |

Flag: sizes for several benchmarks (MUSE, CADENA-Bench, ComCADBench, GERD) not stated in abstracts — marked unverified/unknown. All entries derived from arXiv abstracts; full-paper verification not performed.
