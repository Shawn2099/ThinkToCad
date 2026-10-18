# Benchmarks and the Novelty Gap in Agentic CAD

Scope note: this note covers how agentic/text-to-CAD systems are evaluated (2024–2026), the
headline numbers each named benchmark reports, which metrics dominate, what parts of a real
design workflow remain unbenchmarked, and what that implies for a knowledge-guided agentic-CAD
framework aimed at small-scale agricultural machinery in India. Every factual claim carries an
inline source. Vendor/aggregate numbers are flagged. Search was done via the arXiv API and
project/GitHub pages (web-search authentication and DuckDuckGo were unavailable/rate-limited
during this run); where a specific number could not be retrieved it is recorded in Gaps.

---

## Key Question 1: What does each named benchmark measure, and what are its headline numbers?

### Takeaway
The named artifacts split into (a) execution/validity-first text-to-CAD benchmarks
(Text2CAD-Bench, BenchCAD, RealCADBench, MUSE), (b) engineering-behavior benchmarks that add
DFM/assembly/FEA gates (CADEngBench, MUSE, BenchCAD), and (c) agent/method papers that
report their own custom metrics and ablations (CADSmith, TraceCAD, MIRAGE-CAD, CAD-MLLM/Omni-CAD,
CAD-IR). "AgentCAD" is an open-source CAD CLI/MCP tool, not a benchmark; it runs an external
benchmark called **CADGenBench**, and its published numbers are vendor-reported. Headline
numbers are dominated by executability/validity plus solid/surface IoU and Chamfer distance;
even frontier models sit well below the levels needed for engineering use.

### Cited Findings

**CADEngBench** — arXiv:2608.09296 (10 Aug 2026), "It Looks Like CAD, but Does It Work?"
- Two tracks. CADEngBench-P evaluates **300 parametric parts**, each used for one
  zero-to-CAD task and one functional-editing task (**600 tasks total**), through B-Rep
  validity, engineering and DFM checks, parameter-family perturbations, functional editing, and
  matched linear-static FEA in CalculiX. CADEngBench-A evaluates **150 body pairs** through
  ranked joint retrieval, exact face-and-edge grounding, joint-frame prediction, and
  kinematic verification. — [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)
- Across eight multimodal, code-capable models: editing supplied CAD is substantially easier
  than generating it; complex edits and matched FEA remain difficult. Assembly predictions
  often locate the relevant region but fail to recover the recorded joint or mating entities. —
  [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)

**RealCADBench** — arXiv:2609.03773v2 (3 Sep 2026), "Benchmarking Parametric CAD Modeling from
Industrial Design Intents".
- Contains **12,632 tasks from 19 factory-automation categories**; input regimes: text
  descriptions, 2D engineering drawings, real product pictures, rendered images; both Part and
  Assembly modeling. Reports on a **1,770-task evaluation slice**: 1,745 Part tasks across four
  input regimes plus **RCB-Assm25**, a 25-task assembly study used in every reported assembly
  comparison. Each method generates **FreeCAD API Python** executed by a shared runtime. —
  [arXiv:2609.03773](https://arxiv.org/abs/2609.03773)
- Metrics: **executability, Solid IoU, Surface IoU, and a rubric-based visual-semantic identity
  Judge**. Among nine standalone frontier LLMs, **no model leads all four metrics**. Across six
  frontier-scale models: executability **0.565–0.812**, Solid IoU **0.2841–0.5379**, Surface IoU
  **0.112–0.217** across the four Part regimes. The highest regime-balanced composite comes from
  a *different* model than the leaders on the four component metrics. On RCB-Assm25, Codex with
  GPT-5.5 improves executability and both IoUs over standalone GPT-5.5 but lowers the Judge score
  by **6.98 percentage points**, leaving GPT-5.5 as the Judge leader. Recurring failure modes:
  missing fine structures, loss of part identity, incorrect assembly placement. —
  [arXiv:2609.03773](https://arxiv.org/abs/2609.03773)
- Follow-on VisCAD-M1 (27B) reports the highest average part-level score on PubCADBench and
  RealCADBench, **0.5540 vs 0.5496** for the strongest frontier model, and **0.5797 (~5% relative
  improvement)** when reused as a test-time verifier. — [arXiv:2609.03811](https://arxiv.org/abs/2609.03811)

**Text2CAD-Bench** — arXiv:2605.18430 (18 May 2026).
- **600 human-curated examples** across four levels: L1–L2 fundamental geometry with standard
  features; L3 complex topology and freeform surfaces; L4 real-world domains beyond mechanical
  parts. Each example pairs dual-style prompts: geometric descriptions (non-expert style) and
  procedural sequences (expert style). — [arXiv:2605.18430](https://arxiv.org/abs/2605.18430)
- Headline finding (qualitative, no exact numbers in the abstract): models perform reasonably on
  basic geometry but **degrade substantially on complex topology and advanced features**. —
  [arXiv:2605.18430](https://arxiv.org/abs/2605.18430)
- **Naming-collision warning.** A separate repo, `prashantkul366/textcad-bench`
  ("TextCAD-Bench", INCECT 2026, under review), uses a different design: three frozen test sets
  (T1 = 2,000 DeepCAD/Text2CAD samples stratified by complexity; T2 = 1,725 Fusion360/CADmium
  real engineering parts GPT-4.1-annotated; T3 = 200 human-authored CadQuery-style prompts), and
  reports Chamfer Distance ×10² where **model rankings reverse across test sets** (e.g., T1 best
  CD 17.30 for Text-to-CadQuery, T2 best 16.75 for CADmium-7B, T3 best 26.82 for Qwen-7B). It is
  unclear from available material whether this is the same work as arXiv:2605.18430; treat the two
  as possibly distinct. — [github.com/prashantkul366/textcad-bench](https://github.com/prashantkul366/textcad-bench)
- Dataset: [huggingface.co/datasets/AICAD/Text2CAD-Bench](https://huggingface.co/datasets/AICAD/Text2CAD-Bench)

**MUSE** — arXiv:2605.28579v2 (27 May 2026), "Benchmarking Manufacturable, Functional, and
Assemblable Text-to-CAD Generation". Project page [dong7313.github.io/muse-benchmark](https://dong7313.github.io/muse-benchmark/).
- Text-to-CAD benchmark focused on **complex, editable B-Rep assemblies**, pairing practical
  design instances with structured **Design Specifications**. Three-stage funnel, one failure zeroes
  downstream: (1) **Code Check** = sandbox success (binary); (2) **Geometry Check** = four binary
  OCCT checks — watertight, manifold, self-intersection free, overlap free; (3) **Design-Intent
  Alignment** = rubric-based VLM judge (Gemini-3.1-Pro) scoring **Functionality, Manufacturability,
  Assemblability**; "Final" is the mean of the three pillars. VLM-judge reliability validated via
  human annotation. — [arXiv:2605.28579](https://arxiv.org/abs/2605.28579);
  [project page](https://dong7313.github.io/muse-benchmark/)
- Headline finding: a clear **failure cascade** from executable code to valid geometry to
  engineering-ready design, with even the strongest models achieving limited success on
  fine-grained engineering criteria. The public leaderboard lists **15+ models across 10 metrics**
  (Sandbox, Geom. Valid, Function, Manuf., Assembl., Final), but the top-5 values are loaded by
  JavaScript and were **not captured** — exact leaderboard scores are a gap. —
  [project page](https://dong7313.github.io/muse-benchmark/)
- Dataset: [huggingface.co/datasets/dongxiaoyu/MUSE](https://huggingface.co/datasets/dongxiaoyu/MUSE);
  code: [github.com/dong7313/muse](https://github.com/dong7313/muse)

**BenchCAD** — arXiv:2605.10865v2 (11 May 2026), "A Comprehensive, Industry-Standard Benchmark
for Programmatic CAD". Site [benchcad.com](https://benchcad.com/).
- **17,900 execution-verified CadQuery programs across 106 industrial part families**, including
  bevel gears, compression springs, twist drills. Four tasks: **visual question answering, code
  question answering, image-to-code generation, and instruction-guided code editing**, enabling
  fine-grained analysis across perception, parametric abstraction, and executable program
  synthesis. — [arXiv:2605.10865](https://arxiv.org/abs/2605.10865)
- Across 10+ frontier models: systems often recover coarse outer geometry but **fail to produce
  faithful parametric CAD programs**. Common failures: missing fine 3D structure, misinterpreting
  industrial design parameters, and **replacing sweeps, lofts, and twist-extrudes with simpler
  sketch-and-extrude patterns**. Fine-tuning and RL improve in-distribution performance, but
  generalization to unseen part families remains limited. — [arXiv:2605.10865](https://arxiv.org/abs/2605.10865)
- Leaderboard scoring is "execution-grounded" across four matched tasks (Vision2Code, Vision QA,
  Code QA, Code Edit); exact per-model scores were not retrieved. —
  [benchcad.com/leaderboard](https://benchcad.com/leaderboard)

**AgentCAD's benchmark** — AgentCAD (`jdilla1277/agentcad`) is an **open-source CAD CLI/MCP server**
(build123d default, CadQuery compat mode), not a benchmark. It *runs* an external benchmark called
**CADGenBench**. — [github.com/jdilla1277/agentcad](https://github.com/jdilla1277/agentcad);
  [agentcad.dev](https://agentcad.dev/)
- **Vendor/marketing-sourced numbers (flagged, not peer-reviewed):** the README claims "On
  CADGenBench: **48% higher CAD Score and 21.8% lower model cost**" in a GPT-5 Nano comparison,
  and that "the agent using agentcad also produced **2.5 times as many valid outputs**." It also
  reports one Candidate L run where GPT-5 Nano scored **.245 overall (.175 generation, .353
  editing) with 80 of 81 valid outputs**, while explicitly noting "That is a single run, not a
  new matched direct-build123d comparison." —
  [github.com/jdilla1277/agentcad](https://github.com/jdilla1277/agentcad)
- The agentcad.dev "Spec & measure" page uses a CADGenBench part (220×120×45 mm, ten Ø12 holes,
  four Ø36 bosses) to argue that a part is only correct if every feature is correct. —
  [agentcad.dev/measure-and-spec](https://agentcad.dev/measure-and-spec)
- Separately, the CUAWright paper (arXiv:2610.04116) reports that on **CADGenBench and BenchCAD**
  its unified terminal harness yields **8.1%–41.6% relative improvements** over other CLI-based
  harnesses with GPT-5.5 — evidence that harness/tooling alone shifts CADGenBench and BenchCAD
  scores substantially. — [arXiv:2610.04116](https://arxiv.org/abs/2610.04116)

**CADSmith's metrics** — arXiv:2603.26512 (27 Mar 2026), "Multi-Agent CAD Generation with
Programmatic Geometric Validation".
- Multi-agent pipeline: generates CadQuery code from NL, then two nested correction loops — an
  inner loop resolving execution errors, an outer loop grounded in **programmatic geometric
  validation** (exact OpenCASCADE measurements: bounding-box dimensions, volume, solid validity)
  plus an independent VLM Judge; RAG over API documentation instead of fine-tuning. —
  [arXiv:2603.26512](https://arxiv.org/abs/2603.26512)
- Evaluated on a **custom benchmark of 100 prompts** in three difficulty tiers (T1–T3) with three
  ablation configurations. Against a zero-shot baseline: **100% execution rate (up from 95%)**,
  median **F1 0.9707 → 0.9846**, median **IoU 0.8085 → 0.9629**, mean **Chamfer distance 28.37 →
  0.74**. These are **self-reported on a small, self-defined benchmark** — flag for weak external
  validity. — [arXiv:2603.26512](https://arxiv.org/abs/2603.26512)

**MIRAGE-CAD's metrics** — arXiv:2608.28669 (24 Aug 2026), "Construction-Mediated Multimodal
Generation of Executable CAD Programs".
- Recovers executable parametric CAD programs from four input types (natural language, rendered
  images, point clouds, STEP/B-Rep) by mapping each to a shared construction representation mediated
  through an explicit **construction-plan interface**; code executed by an OpenCASCADE kernel and
  exported as STEP. — [arXiv:2608.28669](https://arxiv.org/abs/2608.28669)
- On **2,500 held-out queries per modality**, **55.4–70.0% build success** and **52.3–66.2% STEP
  export success** without retrieval at inference. Reports that **executable validity, geometric
  fidelity, and parametric responsiveness can diverge substantially and should be evaluated
  separately**; also that a continuous (non-text) construction representation reconstructs strongly,
  so the explicit plan's value is readability/measurability rather than geometry. —
  [arXiv:2608.28669](https://arxiv.org/abs/2608.28669); code/eval:
  [github.com/Cad-Kernel/MIRAGE-CAD](https://github.com/Cad-Kernel/MIRAGE-CAD)

**TraceCAD's ablations** — arXiv:2608.03062 (4 Aug 2026), "Trace-Guided Repair for Agentic CAD
Generation".
- A recovery layer linking requested features, modeling steps, failure evidence, and candidate
  outcomes as persistent state; it diagnoses likely faulty operations, searches bounded edits in
  their dependency regions, validates candidates through execution and preservation checks, and
  retains successful/failed repair outcomes in reusable **skill memory**. —
  [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- Evaluated on DeepCAD-derived benchmarks with **200-model ablations** and a **1K-model
  comparison**, reporting IoU, Chamfer distance, and Hausdorff distance. Ablations: **removing
  persistent state nearly halves recovery score**; **removing localized search more than doubles
  geometric regression and doubles code-agent invocations**; initializing the skill store on
  disjoint training models further reduces retries, token cost, and latency. —
  [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)

**CAD-MLLM / Omni-CAD** — arXiv:2411.04954v3 (Nov 2024; v3 Aug 2025).
- Omni-CAD: the first multimodal CAD dataset with text, multi-view images, points, and command
  sequence per model; **~450K instances (453,220 after augmentation)**. —
  [arXiv:2411.04954](https://arxiv.org/abs/2411.04954);
  [project page](https://cad-mllm.github.io/)
- Introduces four topology/enclosure metrics: **SegE (Segment Error), DangEL (Dangling Edge Length),
  SIR (Self-Intersection Ratio), FluxEE (Flux Enclosure Error)**, plus standard Chamfer,
  F-score, and Normal Consistency. — [arXiv:2411.04954](https://arxiv.org/abs/2411.04954)
- Point-conditioned results (×100): Ours vs baselines — Chamfer **1.85** vs ParSeNet 4.59,
  ComplexGen 1.65, Point2CAD 1.25, NVDNet 0.82, DeepCAD(Point) 4.51; F-score **90.88**; SegE
  **1.66**; DangEL **0.46**; SIR **1.31**; FluxEE **0.044**. Trained on 16×H800, Vicuna-7B,
  20 epochs, ~47 h. — [arXiv:2411.04954](https://arxiv.org/abs/2411.04954)

**Adjacent benchmarks worth knowing** (found while mapping the landscape):
- **CADWorld**: GUI-based benchmark of **200 mechanical CAD tasks across 11 FreeCAD workflow
  categories** for computer-use agents. — [cad-world.github.io](https://cad-world.github.io/)
- **CAD Bench V3** (cadbench.ai): **100 complex FreeCAD tasks** — 30 creation-from-text, 30
  create-and-edit-from-text, 40 creation-from-engineering-drawings. —
  [cadbench.ai](https://cadbench.ai/)
- **CAD Arena**: "first open benchmark comparing text-to-CAD models," **20 curated prompts across 4
  difficulty tiers**. — [cadarena.dev/models/text2cad](https://cadarena.dev/models/text2cad)
- **UniCAD**: unified multi-modal/multi-task benchmark (point-to-CAD reconstruction,
  text/image-to-CAD generation, CAD QA) plus UniCAD-MLLM. —
  [arXiv:2606.05058](https://arxiv.org/abs/2606.05058)
- **CADReview / ReCAD**: dataset of **20K+ program-image pairs** for error detection and
  correction (ACL 2025). — [arXiv:2505.22304](https://arxiv.org/abs/2505.22304)
- **CADFather**: autonomous agentic reconstruction evaluated on DeepCAD, Fusion360, MCB test sets,
  **CADENA-Bench, CADBench, and BenchCAD**. — [arXiv:2610.09127](https://arxiv.org/abs/2610.09127)
- **Text-to-CadQuery**: best model **top-1 exact match 69.3% (up from 58.8%)** and **48.6%
  Chamfer reduction**. — [arXiv:2505.06507](https://arxiv.org/abs/2505.06507)
- **CADmium**: 170k CAD models with geometric/topological metrics based on sphericity, mean
  curvature, and Euler characteristic. — [arXiv:2507.09792](https://arxiv.org/abs/2507.09792)
- **ArtisanCAD**: skill-guided industrial CAD agent with CATIA-MCP backend; on Text2CAD,
  CAD-IR reduces mean Chamfer Distance **14.83 → 9.88** for intermediate prompts. —
  [arXiv:2607.05750](https://arxiv.org/abs/2607.05750)
- **Survey**: "Large Language Models for Computer-Aided Design: A Survey" (six-area taxonomy). —
  [arXiv:2505.08137](https://arxiv.org/abs/2505.08137)

### Inferences
- The field is converging on a **funnel** model: sandbox/executability → geometric validity →
  engineering/design-intent checks. MUSE, RealCADBench, and BenchCAD all instantiate it, with
  increasing fidelity at each later stage.
- Even the strongest frontier/agent systems produce **executability roughly 0.57–0.81 and solid
  IoU roughly 0.28–0.54** on RealCADBench — i.e., the headline numbers are far from "correct
  engineering part," and IoU/Surface IoU are not monotone with engineering acceptability
  (RealCADBench explicitly shows no model leads all four metrics; MUSE shows a code→geometry→design
  cascade).
- **Editing supplied CAD is consistently easier than generating it** (CADEngBench), which supports
  positioning around iterative edit/recovery loops (TraceCAD, BenchCAD code-editing) rather than
  one-shot generation.
- Benchmark definitions are **moving fast and partly unstable**: five of the eight named
  artifacts were posted in 2026, MUSE/Text2CAD-Bench leaderboards are JavaScript-rendered, and
  there is a name collision between two "Text2CAD-Bench" works. Claims must be re-verified at
  citation time.

### Gaps
- **CADGenBench's own metric definition and task set** could not be retrieved (the AgentCAD repo's
  `benchmarks/cadgenbench/` directory contains only run outputs; its README 404s). Only
  second-hand descriptions were obtained. — [github.com/jdilla1277/agentcad](https://github.com/jdilla1277/agentcad)
- **MUSE leaderboard values** (Sandbox/Geom. Valid/Function/Manuf./Assembl./Final per model) were
  not captured because they load via JavaScript. —
  [dong7313.github.io/muse-benchmark](https://dong7313.github.io/muse-benchmark/)
- **BenchCAD per-model leaderboard scores** were not retrieved. —
  [benchcad.com/leaderboard](https://benchcad.com/leaderboard)
- Whether **arXiv:2605.18430 Text2CAD-Bench** and the `textcad-bench` repo (INCECT 2026) are the
  same work is unresolved. — [arXiv:2605.18430](https://arxiv.org/abs/2605.18430);
  [github.com/prashantkul366/textcad-bench](https://github.com/prashantkul366/textcad-bench)
- Exact per-model numbers for **CADEngBench, MIRAGE-CAD per-modality, and TraceCAD** are stated in
  prose in the abstracts; full tables live in the PDFs/HTML, which were not fully parsed here.

---

## Key Question 2: Which metrics dominate?

### Takeaway
Executability/validity (sandbox success, code validity, B-Rep validity) is the universal first
gate, followed by **solid/surface IoU** and **Chamfer distance**, with **F-score**, **Hausdorff
distance**, and **visual-semantic/VLM-judge** scores as secondary. Constraint satisfaction and
design-intent alignment (rubric judges) are the newest differentiator, and **edit success /
iteration count / token cost / latency** are emerging as agent-specific metrics. Simulation
(infrequent) and topology (growing) metrics are niche but rising.

### Cited Findings
- **Executability/validity**: RealCADBench's primary metric is executability (0.565–0.812 across
  models) and MUSE's stage-1 gate is pure sandbox success. —
  [arXiv:2609.03773](https://arxiv.org/abs/2609.03773);
  [dong7313.github.io/muse-benchmark](https://dong7313.github.io/muse-benchmark/)
- **Solid IoU / Surface IoU**: RealCADBench reports Solid IoU 0.2841–0.5379 and Surface IoU
  0.112–0.217; the `textcad-bench` repo uses IoU on 64³ voxelisation (watertight meshes only).
  — [arXiv:2609.03773](https://arxiv.org/abs/2609.03773);
  [github.com/prashantkul366/textcad-bench](https://github.com/prashantkul366/textcad-bench)
- **Chamfer distance**: dominant in method papers — CADSmith (28.37 → 0.74), ArtisanCAD
  (14.83 → 9.88), Text-to-CadQuery (−48.6%), and the `textcad-bench` CD metric. —
  [arXiv:2603.26512](https://arxiv.org/abs/2603.26512);
  [arXiv:2607.05750](https://arxiv.org/abs/2607.05750);
  [arXiv:2505.06507](https://arxiv.org/abs/2505.06507);
  [github.com/prashantkul366/textcad-bench](https://github.com/prashantkul366/textcad-bench)
- **F-score / Hausdorff distance**: used by CAD-MLLM (point-conditioned F-score 90.88) and
  TraceCAD (IoU, Chamfer, Hausdorff). — [arXiv:2411.04954](https://arxiv.org/abs/2411.04954);
  [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- **Constraint satisfaction / design-intent alignment**: MUSE's stage-3 rubric judge scores
  Functionality, Manufacturability, Assemblability against per-case rubrics; CADEngBench adds
  engineering and DFM checks and functional-editing success. —
  [arXiv:2605.28579](https://arxiv.org/abs/2605.28579);
  [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)
- **Visual-semantic / VLM judge**: RealCADBench uses a "rubric-based visual-semantic identity
  Judge"; CADSmith uses an independent VLM Judge; MUSE uses Gemini-3.1-Pro as judge. —
  [arXiv:2609.03773](https://arxiv.org/abs/2609.03773);
  [arXiv:2603.26512](https://arxiv.org/abs/2603.26512);
  [arXiv:2605.28579](https://arxiv.org/abs/2605.28579)
- **Topology metrics**: CAD-MLLM's SegE/DangEL/SIR/FluxEE; CADmium's sphericity, mean curvature,
  and Euler characteristic; Pointer-CAD v2's vertex/edge/face hierarchical accuracy. —
  [arXiv:2411.04954](https://arxiv.org/abs/2411.04954);
  [arXiv:2507.09792](https://arxiv.org/abs/2507.09792);
  [arXiv:2606.29301](https://arxiv.org/abs/2606.29301)
- **Edit success / iteration / cost / latency**: CADEngBench separates zero-to-CAD from
  functional editing; BenchCAD has instruction-guided code editing; TraceCAD reports code-agent
  invocations, token cost, latency, and retries; AgentCAD markets "lower model cost" and valid-output
  counts. — [arXiv:2608.09296](https://arxiv.org/abs/2608.09296);
  [arXiv:2605.10865](https://arxiv.org/abs/2605.10865);
  [arXiv:2608.03062](https://arxiv.org/abs/2608.03062);
  [github.com/jdilla1277/agentcad](https://github.com/jdilla1277/agentcad)
- **Simulation gates**: CADEngBench runs matched linear-static FEA in CalculiX and kinematic
  verification; MIRAGE-CAD reports build success and STEP export success as separate gates. —
  [arXiv:2608.09296](https://arxiv.org/abs/2608.09296);
  [arXiv:2608.28669](https://arxiv.org/abs/2608.28669)

### Inferences
- **IoU and Chamfer reward "looks like" over "works as"**: RealCADBench's finding that no model
  leads all four metrics, and MIRAGE-CAD's finding that validity, fidelity, and parametric
  responsiveness diverge, together argue that any single geometric number is insufficient. —
  [arXiv:2609.03773](https://arxiv.org/abs/2609.03773);
  [arXiv:2608.28669](https://arxiv.org/abs/2608.28669)
- **Rubric/VLM judges are becoming the differentiator but are also a reliability risk**: MUSE
  validates its VLM judge with human annotation; CAD-Judge explicitly warns that VLM-based
  review "can be expensive and may introduce reward hacking." —
  [arXiv:2605.28579](https://arxiv.org/abs/2605.28579);
  [arXiv:2508.04002](https://arxiv.org/abs/2508.04002)
- **Cost/efficiency is a real, reportable axis**: TraceCAD's ablations and AgentCAD's marketing
  both treat token cost, latency, retries, and valid-output counts as first-class, suggesting a
  frugality metric is legitimate and comparable. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062);
  [github.com/jdilla1277/agentcad](https://github.com/jdilla1277/agentcad)
- The dominance of **execution-grounded** scoring aligns with the "kernel is the referee"
  principle: CAD engines, not the LLM, declare validity.

### Gaps
- No benchmark found that reports **DFM/tolerance/cost as a scored, calibrated metric with a
  published reference scale** — MUSE's manufacturability is rubric-judged, not a numeric
  manufacturability index.
- **Inter-rater reliability numbers** for the VLM judges (RealCADBench, MUSE, CADSmith) beyond
  MUSE's human-validation claim were not retrieved.

---

## Key Question 3: Which parts of a real design workflow are NOT benchmarked?

### Takeaway
Even the newest 2026 benchmarks stop at geometry/validity, generic manufacturability/assemblability
rubrics, or generic linear-static FEA. **Tolerance stack-up and GD&T reasoning, assembly *intent*
beyond mating-entity prediction, process-aware DFM for specific local processes, closed-loop
delivery to shop artifacts (2D drawings with GD&T, BOM, process plans), cost/frugality tradeoffs,
and domain-specific load cases (soil-engaging tools, PTO/linkage kinematics)** are essentially
unbenchmarked in the LLM/agentic-CAD literature. Tolerance stack-up and CAD-agent assembly
benchmarks returned zero arXiv hits, which is suggestive (not conclusive) evidence of the gap.

### Cited Findings
- **Tolerance stack-up**: a targeted arXiv search for `"tolerance stack" AND CAD AND LLM` returned
  **0 results**. — [arXiv API query](http://export.arxiv.org/api/query?search_query=all:%22tolerance+stack%22+AND+all:CAD+AND+all:LLM)
- **Assembly-intent benchmarking**: a targeted search for `"CAD agent" AND benchmark AND assembly`
  returned **0 results**. (CADEngBench-A covers joint retrieval/grounding/kinematic verification,
  and MUSE covers assemblability by rubric, but neither is framed as an "assembly intent" benchmark.) —
  [arXiv API query](http://export.arxiv.org/api/query?search_query=all:%22CAD+agent%22+AND+all:%22benchmark%22+AND+all:%22assembly%22);
  [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)
- **Assembly predictions remain shallow**: CADEngBench reports predictions "often locate the
  relevant region but fail to recover the recorded joint or mating entities." —
  [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)
- **Manufacturability is generic, not process-aware**: MUSE scores Manufacturability via a
  rubric-based VLM judge rather than process-specific rules; the one DFM-specific agent paper
  (LLM-Aided DFM Redesign) is a **preliminary report** with a **46-part benchmark scored by
  Chamfer distance**, and states that "evaluation of the full review-and-redesign loop, including
  manufacturability gain and an operational measure of intent preservation, is ongoing." —
  [arXiv:2605.28579](https://arxiv.org/abs/2605.28579);
  [arXiv:2609.05559](https://arxiv.org/abs/2609.05559)
- **Shop artifacts / process planning exist but are not closed-loop with generation**:
  Design-to-Plan turns 3D CAD + 2D drawings into process plans (300 cases; Tool F1
  95.9–97.6%; 100% downstream success; 60–68% token reduction), but is a separate downstream
  task, not a generation-time gate. — [arXiv:2608.24039](https://arxiv.org/abs/2608.24039)
- **2D drawing ↔ 3D feature binding is addressed in isolation**: a context-aware framework maps
  2D drawing annotations to 3D CAD features on **20 real CAD-drawing pairs** (precision 83.67%,
  recall 90.46%, F1 86.29%). — [arXiv:2602.18296](https://arxiv.org/abs/2602.18296)
- **Precision/tolerance is treated as a metric problem, not a reasoning problem**: Pointer-CAD v2
  motivates metric-scale prediction because "small numerical deviations … may still violate
  industrial tolerance requirements," and introduces vertex/edge/face hierarchical accuracy. —
  [arXiv:2606.29301](https://arxiv.org/abs/2606.29301)
- **Manufacturability intent for manufacturing** is acknowledged as missing: STEP-LLM notes
  CadQuery/command-sequence formats are "kernel-dependent and lack universality for manufacturing,"
  motivating neutral STEP generation. — [arXiv:2601.12641](https://arxiv.org/abs/2601.12641)
- **Agricultural domain**: the only LLM-agriculture-machinery work surfaced is **CIAMM**
  (arXiv:2407.20588), which uses GPT-4 + multi-round prompting for *machinery management/
  consultation*, not CAD design. — [arXiv:2407.20588](https://arxiv.org/abs/2407.20588)

### Inferences
- There is a **clear, citable gap between "valid solid" and "manufacturable, assemblable,
  inspectable product"**: no benchmark found scores a generated CAD model on tolerance stack-up,
  GD&T callout correctness, BOM completeness, or a drawing set. MUSE is closest (assemblability +
  manufacturability rubrics) but does not score stacks or shop artifacts. —
  [arXiv:2605.28579](https://arxiv.org/abs/2605.28579)
- **Simulation gates are nascent**: only CADEngBench (CalculiX linear-static FEA, kinematic
  verification) and MUSE's geometric checks touch engineering behavior; domain-specific loads
  (soil reaction on tools, PTO/linkage kinematics, fatigue of cyclic soil loads) appear
  unbenchmarked. — [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)
- **Frugality/cost is unreported as a design-quality metric** in any benchmark surveyed; the only
  cost numbers are agent-efficiency claims (TraceCAD, AgentCAD), not design-cost-per-unit or
  cost-per-hectare tradeoffs. — [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- **The closed loop to the shop is unbuilt as an evaluated artifact**: generation → validation →
  drawings/BOM/process plan is split across separate papers (RealCADBench/MUSE → Design-to-Plan),
  with no benchmark requiring an end-to-end deliverable. —
  [arXiv:2608.24039](https://arxiv.org/abs/2608.24039)
- **Data scarcity is domain-specific**: Omni-CAD, DeepCAD, Fusion360, and CADmium are
  general/industrial mechanical; no India- or agriculture-specific CAD corpus was found. —
  [arXiv:2411.04954](https://arxiv.org/abs/2411.04954);
  [arXiv:2507.09792](https://arxiv.org/abs/2507.09792)

### Gaps
- Absence of results in the two targeted searches is **suggestive, not proof** — arXiv API
  coverage is incomplete and web search/DDG were unavailable this run. A systematic survey-level
  search is needed to assert "no benchmark exists."
- Whether **CADEngBench's DFM checks** include tolerance/stack-up or are limited to feature-level
  manufacturability rules could not be determined from the abstract alone. —
  [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)
- No source found that quantifies **design cost, material utilization, or local stock-size
  availability** as an evaluation axis for generated CAD. — (no reliable source found)
- No source found evaluating **farmer/manufacturer-in-the-loop acceptance** of AI-generated
  agricultural machinery designs. — (no reliable source found)

---

## Key Question 4: What would constitute a genuinely novel contribution for a knowledge-guided agentic CAD framework targeting small-scale agricultural machinery in India?

### Takeaway
Given the published landscape, the defensible novelty is not "another text-to-CAD generator" but a
**knowledge-guided, trust-tiered agentic loop that closes the loop from intent → validated
parametric model → manufacturability/tolerance reasoning → shop deliverables**, evaluated on a
**domain corpus of small-scale Indian agricultural machinery** with **frugality and
manufacturability metrics** that no current benchmark scores. The strongest positioning combines
(a) an executable, constraint-grounded knowledge base, (b) process-aware DFM + tolerance
stack-up reasoning, (c) closed-loop delivery to 2D drawings/BOM/process plan, and (d) a
domain-specific benchmark with frugality metrics.

### Cited Findings
- **Edits beat generation**: CADEngBench shows editing supplied CAD is substantially easier than
  generating it, and BenchCAD/TraceCAD treat editing as a first-class task — supporting an
  iterative, knowledge-guided edit loop as the core contribution rather than one-shot generation. —
  [arXiv:2608.09296](https://arxiv.org/abs/2608.09296);
  [arXiv:2605.10865](https://arxiv.org/abs/2605.10865);
  [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- **Knowledge/RAG is already used but shallow**: CADSmith uses RAG over API documentation and
  reports big gains (execution 95%→100%; Chamfer 28.37→0.74) on its own 100-prompt benchmark;
  ArtisanCAD distills expert CATIA recordings into reusable parameterized skills (CAD-IR) and cuts
  mean Chamfer 14.83→9.88 on intermediate prompts. This shows **expert-procedure retrieval is a
  real lever** — and also that it is the obvious next thing for others to do. —
  [arXiv:2603.26512](https://arxiv.org/abs/2603.26512);
  [arXiv:2607.05750](https://arxiv.org/abs/2607.05750)
- **Persistent state and localized search matter**: TraceCAD's ablations show removing persistent
  state nearly halves recovery score and removing localized search more than doubles geometric
  regression — a knowledge/trace layer is a measurable contribution, not cosmetic. —
  [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- **Engineering behavior, not appearance, is the frontier**: CADEngBench's thesis is that "CAD
  evaluation must test engineering behavior rather than appearance alone," and its FEA/DFM/kinematic
  tracks show matched FEA and complex edits remain hard. —
  [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)
- **Manufacturability/assemblability are now benchmarked generically** (MUSE) but not
  process- or region-specific; the DFM agent paper is preliminary and scores by Chamfer only. —
  [arXiv:2605.28579](https://arxiv.org/abs/2605.28579);
  [arXiv:2609.05559](https://arxiv.org/abs/2609.05559)
- **Tolerance/GD&T is a recognized pain point but unbenched**: Pointer-CAD v2 (ECCV 2026) targets
  metric-scale/tolerance precision; the 2D-drawing-to-3D-feature work handles GD&T callouts but on
  only 20 pairs; no tolerance-stack benchmark exists. —
  [arXiv:2606.29301](https://arxiv.org/abs/2606.29301);
  [arXiv:2602.18296](https://arxiv.org/abs/2602.18296)
- **No agriculture-specific CAD benchmark or corpus exists**: the only LLM-agri-machinery paper
  found is about machinery management, not design. —
  [arXiv:2407.20588](https://arxiv.org/abs/2407.20588)
- **Agent/tooling alone shifts scores**: CUAWright reports 8.1%–41.6% relative gains on
  CADGenBench/BenchCAD from a better harness — so a framework must report harness-controlled
  comparisons, not just raw scores. — [arXiv:2610.04116](https://arxiv.org/abs/2610.04116)

### Inferences
- **Novelty claim 1 — domain knowledge as a first-class, executable artifact.** Position the
  contribution as a *knowledge-guided* agent whose retrieved constraints (mechanism catalog, DFM
  rules, local stock sizes, fit/standard tables) are executable and unit-consistent, rather than
  prose RAG. This is distinct from CADSmith's API-doc RAG and ArtisanCAD's expert-skill
  distillation, and directly targets the gap that no agriculture-machinery corpus exists. —
  [arXiv:2603.26512](https://arxiv.org/abs/2603.26512);
  [arXiv:2607.05750](https://arxiv.org/abs/2607.05750)
- **Novelty claim 2 — manufacturability + tolerance stack-up as scored gates.** Build
  process-aware DFM checks (welding, sheet metal, casting, machining, manual) plus a
  tolerance-stack reasoner, and score them numerically. This addresses the two zero-result gaps
  (tolerance stack; CAD-agent assembly) and goes beyond MUSE's generic rubric and the preliminary
  DFM-redesign work. —
  [arXiv API query: tolerance stack](http://export.arxiv.org/api/query?search_query=all:%22tolerance+stack%22+AND+all:CAD+AND+all:LLM);
  [arXiv:2609.05559](https://arxiv.org/abs/2609.05559)
- **Novelty claim 3 — closed-loop delivery to shop artifacts.** Evaluate end-to-end deliverables
  (GD&T-annotated 2D drawings, BOM, process plan) generated from the model, not just the solid.
  Design-to-Plan shows the downstream reasoning exists, but no benchmark requires it as part of
  generation. — [arXiv:2608.24039](https://arxiv.org/abs/2608.24039);
  [arXiv:2602.18296](https://arxiv.org/abs/2602.18296)
- **Novelty claim 4 — a frugality/cost metric and a domain benchmark.** Report cost per
  part/implement, material utilization, and agent token/cost, alongside validity and IoU. No
  benchmark surveyed reports design cost or frugality; AgentCAD only markets agent-side cost. —
  [github.com/jdilla1277/agentcad](https://github.com/jdilla1277/agentcad);
  [arXiv:2608.03062](https://arxiv.org/abs/2608.03062)
- **Novelty claim 5 — simulation gates for agricultural loads.** Add domain-specific kinematics
  (hitches, PTO, linkages) and load cases (soil reaction, cyclic fatigue) as verification gates,
  extending CADEngBench's generic FEA/kinematic tracks to agronomic machinery. —
  [arXiv:2608.09296](https://arxiv.org/abs/2608.09296)
- **Positioning caution:** because harness choice alone moves CADGenBench/BenchCAD scores by
  8–42%, any headline must be a **matched, harness-controlled** comparison, and because
  benchmark scores reverse across test sets (`textcad-bench`), the domain benchmark should
  report per-tier and per-regime results rather than a single number. —
  [arXiv:2610.04116](https://arxiv.org/abs/2610.04116);
  [github.com/prashantkul366/textcad-bench](https://github.com/prashantkul366/textcad-bench)

### Gaps
- **No source found** that defines or validates a *frugality* metric (cost/material/token per
  accepted design) for CAD generation; this would need to be operationalized and defended by the
  project itself. — (no reliable source found)
- **No agriculture-machinery CAD dataset** was found to anchor a domain benchmark; sourcing or
  constructing one (e.g., from manufacturers, NPTEL "Design of Farm Machinery" material, or public
  implement catalogs) is an open task. —
  [onlinecourses.nptel.ac.in/noc25_ag03](https://onlinecourses.nptel.ac.in/noc25_ag03/preview)
- **No source found** on Indian small-scale manufacturer DFM constraints (available stock sizes,
  process capabilities, welding vs machining preferences) in machine-readable form; this would
  need primary fieldwork. — (no reliable source found)
- Whether **CADEngBench's DFM checks** or **MUSE's manufacturability rubric** already cover any of
  the proposed process-aware checks is unresolved from abstracts; full PDF review is needed before
  claiming novelty over them. — [arXiv:2608.09296](https://arxiv.org/abs/2608.09296);
  [arXiv:2605.28579](https://arxiv.org/abs/2605.28579)
