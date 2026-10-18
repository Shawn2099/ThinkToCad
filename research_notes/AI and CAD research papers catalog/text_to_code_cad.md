# Text-to-Code-to-CAD: LLM Generating CAD Code/Programs

## Major text-to-code-to-CAD papers (2024–2026)

### Takeaway
The field shifted from generating task-specific command sequences (DeepCAD-style) to generating executable Python CAD code (CadQuery/FreeCAD/build123d), letting pretrained LLMs' code ability carry over; 2024–2026 saw a wave of text-to-CAD-code papers plus many new execution-grounded benchmarks.

### Cited Findings
- Text2CAD: Generating Sequential CAD Models from Beginner-to-Expert Level Text Prompts — Mohammad Sadil Khan, Sankalp Sinha, Talha Uddin Sheikh, Didier Stricker, Sk Aziz Ali, Muhammad Zeshan Afzal; arXiv:2409.17106; NeurIPS 2024 (Spotlight) — [arXiv](https://arxiv.org/abs/2409.17106); [project](https://sadilkhan.github.io/text2cad-project/).
- Query2CAD: Generating CAD models using natural language queries — Akshay Badagabettu, Sai Sravan Yarlagadda, Amir Barati Farimani; arXiv:2406.00144; 2024 — [arXiv](https://arxiv.org/abs/2406.00144).
- LLM4CAD: Multi-Modal Large Language Models for Three-Dimensional Computer-Aided Design Generation — Xingang Li, Yuewan Sun, Zhenghui Sha; Journal of Computing and Information Science in Engineering, 2025 (Feb 2025); NSF PAR 10661832 — [NSF](https://par.nsf.gov/biblio/10661832-llm4cad-multi-modal-large-language-models-computer-aided-design-generation).
- CADCodeVerify: Generating CAD Code with Vision-Language Models (ICLR 2025) — introduced CADPrompt benchmark (200 prompts + expert code); arXiv:2410.05340 — [arXiv](https://arxiv.org/abs/2410.05340); [ICLR PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf).
- CAD-Llama: Leveraging Large Language Models for Computer-Aided Design Parametric 3D Model Generation — arXiv:2505.04481; CVPR 2025 — [arXiv](https://arxiv.org/abs/2505.04481); [CVPR](https://cvpr.thecvf.com/virtual/2025/poster/33676).
- Text-to-CadQuery: A New Paradigm for CAD Generation with Scalable Large Model Capabilities — arXiv:2505.06507; 2025 (authors per alphaXiv) — [arXiv](https://arxiv.org/abs/2505.06507).
- CAD-Coder: Text-to-CAD Generation with Chain-of-Thought and Geometric Reward — Yandong Guan, Xilin Wang, Ximing Xing, Jing Zhang, Dong Xu, Qian Yu; arXiv:2505.19713; NeurIPS 2025 — [arXiv](https://arxiv.org/abs/2505.19713); [NeurIPS PDF](https://papers.neurips.cc/paper_files/paper/2025/file/564a224e88f2490f3c1deaae877d37e3-Paper-Conference.pdf).
- CAD-Coder: An Open-Source Vision-Language Model for Computer-Aided Design Code Generation — Anna C. Doris, Md Ferdous Alam, Amin Heyrani Nobari, Faez Ahmed; arXiv:2505.14646; 2025 (MIT) — [arXiv](https://arxiv.org/abs/2505.14646); [GitHub](https://github.com/anniedoris/CAD-Coder).
- CAD-Assistant: Tool-Augmented VLLMs as Generic CAD Task Solvers — Dimitrios Mallis et al.; arXiv:2412.13810; ICCV 2025 — [arXiv](https://arxiv.org/abs/2412.13810).
- CAD-Recode: Reverse Engineering CAD Code from Point Clouds — arXiv:2412.14042; ICCV 2025 — [arXiv](https://arxiv.org/abs/2412.14042); [GitHub](https://github.com/filaPro/cad-recode).
- Generative AI for CAD Automation: Leveraging LLMs for 3D Modelling (FreeCAD scripts, GPT-4 + LangChain) — arXiv:2508.00843; 2025 — [arXiv PDF](https://arxiv.org/pdf/2508.00843v1).
- Learning From Design Procedure To Generate CAD Programs for Data Augmentation (uses CadQuery/Build123d, OpenAI o3) — arXiv:2603.06894; 2026 — [arXiv PDF](https://arxiv.org/pdf/2603.06894v1).
- FutureCAD: LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding (CadQuery + BRepGround) — Jiahao Li et al.; arXiv:2603.11831; ICML 2026 Spotlight — [arXiv](https://arxiv.org/abs/2603.11831); [GitHub](https://github.com/JohanStackk/FutureCAD).
- Foundation Models for Automatic CAD Generation (LLMForge, 7 models, iterative refinement) — J. de Curtò et al.; arXiv:2607.05573; Springer chapter 2026 — [arXiv](https://arxiv.org/abs/2607.05573).
- Generative AI meets CAD: LLM-driven design (OpenSCAD, GPT-4o, closed feedback loop) — Springer Int J Adv Manuf Technol, 2025 — [Springer](https://link.springer.com/article/10.1007/s00170-025-15830-2).
- OpenSCAD text-to-code tools: cadgenerator (Llama/Ollama → OpenSCAD) — [GitHub](https://github.com/Im-Harshith/cadgenerator).
- Industrial/agentic pipelines: CadCore (build123d/FreeCAD, self-healing loop, Gemini/OpenAI/Anthropic/Ollama) — [PyPI](https://pypi.org/project/cadcore-ai/); cad-agent (build123d) — [GitHub](https://github.com/Youssef-RAPCorp/cad-agent).

### Inferences
- CadQuery dominates as the code target (text-to-CadQuery, CAD-Coder, FutureCAD, BenchCAD, CADPrompt, MUSE); FreeCAD Python appears where agents need a full CAD kernel (CAD-Assistant, RealCADBench, CADGenBench baseline, tim-odonnell benchmark); build123d is the newer target in agentic pipelines (CadCore, cad-agent, cadgenbench baseline).
- Validation/repair loops are the differentiator: zero-shot text-to-code papers (Query2CAD, Text-to-CadQuery) vs. execution-feedback refinement (CADCodeVerify, Query2CAD's 3-iteration VQA loop, LLMForge's 3-round critique, CadCore self-healing).

### Gaps
- I did not find a peer-reviewed SolidPython-specific text-to-code paper; SolidPython/OpenSCAD generation appears mostly in hobbyist repos and the Springer GAD paper.
- Author lists for some arXiv entries (e.g., Text-to-CadQuery 2505.06507, FutureCAD) were not fully captured; verify before citing.

## Code representations used

### Takeaway
CadQuery is the dominant representation; FreeCAD Python API and build123d are used for agentic/kernel-grounded workflows; OpenSCAD appears in hobbyist/early systems; command-sequence (DeepCAD) DSLs are being replaced by Python code.

### Cited Findings
- CadQuery: Python-based parametric CAD scripting language, chosen because it is Python (LLM-friendly), chainable, executable headless, supports fillets/chamfers/sweeps/lofts — [CAD-Coder arXiv:2505.19713](https://arxiv.org/abs/2505.19713); [Text-to-CadQuery arXiv:2505.06507](https://arxiv.org/abs/2505.06507); [CAD-Coder VLM arXiv:2505.14646](https://arxiv.org/abs/2505.14646).
- FreeCAD Python API: CAD-Assistant generates FreeCAD code executed in FreeCAD; Generative AI for CAD Automation uses FreeCAD + GPT-4; RealCADBench tasks generate FreeCAD API Python; LLM CAD benchmark (tim-odonnell) includes FreeCAD track — [CAD-Assistant arXiv:2412.13810](https://arxiv.org/abs/2412.13810); [RealCADBench arXiv:2609.03773](https://arxiv.org/abs/2609.03773).
- build123d: modern OpenCASCADE Pythonic BREP framework; CadCore default backend; cad-agent output; cadgenbench baseline supports build123d & CadQuery — [build123d GitHub](https://github.com/gumyr/build123d); [CadCore PyPI](https://pypi.org/project/cadcore-ai/).
- OpenSCAD: used in GAD (Springer) and cadgenerator (Ollama/Llama) — [Springer](https://link.springer.com/article/10.1007/s00170-025-15830-2); [GitHub](https://github.com/Im-Harshith/cadgenerator).
- Command-sequence DSLs (DeepCAD/SkexGen style) are contrasted with code: CAD-Llama uses SPCC; CAD-Coder text-to-CadQuery replaces command sequences — [CAD-Llama arXiv:2505.04481](https://arxiv.org/abs/2505.04481); [Text2CAD arXiv:2409.17106](https://arxiv.org/abs/2409.17106).

### Inferences
- Representation choice tracks validation needs: CadQuery for fast headless execution/validation; FreeCAD when tool-augmented agents need a full kernel (sketching, constraints, rendering); build123d for newer agentic pipelines needing BREP + STEP export.

### Gaps
- No comprehensive comparison study of representation impact on LLM accuracy was found; most papers pick one representation.

## LLMs used

### Takeaway
GPT-4/GPT-4V and GPT-4o dominate early work; recent fine-tuned open models (Qwen2.5-7B, Qwen3-VL, LLaVA-derived) and frontier models (GPT-5.x, Claude 4.5, Gemini 3, DeepSeek) are benchmarked; DeepSeek-V3 is commonly used as a data-annotation/code-generation teacher.

### Cited Findings
- GPT-4 / GPT-4V / GPT-4o / GPT-4 Turbo: LLM4CAD, Query2CAD, CADCodeVerify, IdeaToCAD, CAD-Assistant planner, Springer GAD — [LLM4CAD NSF](https://par.nsf.gov/biblio/10661832-llm4cad-multi-modal-large-language-models-computer-aided-design-generation); [Query2CAD arXiv:2406.00144](https://arxiv.org/abs/2406.00144); [CADCodeVerify ICLR](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf).
- Claude (Sonnet/Opus) and Gemini (Pro/Flash): benchmarked in BenchCAD, CADEngBench, RealCADBench, LLMForge (Gemma), MUSE; Claude Sonnet 4.5 struggled in neuralCAD-Edit — [BenchCAD arXiv:2605.10865](https://arxiv.org/abs/2605.10865); [neuralCAD-Edit arXiv:2604.16170](https://arxiv.org/abs/2604.16170).
- DeepSeek (V3, V3.2, Coder): used as annotation teacher (CAD-Coder uses DeepSeek-V3) and evaluated model (LLMForge) — [CAD-Coder arXiv:2505.19713](https://arxiv.org/abs/2505.19713); [Foundation Models arXiv:2607.05573](https://arxiv.org/abs/2607.05573).
- Qwen family (Qwen2.5-7B-Instruct base for CAD-Coder; Qwen3-VL-2B, Qwen3-235B): [CAD-Coder arXiv:2505.19713](https://arxiv.org/abs/2505.19713); [ConCAD arXiv:2609.34494](https://arxiv.org/html/2609.34494); [LLMForge arXiv:2607.05573](https://arxiv.org/abs/2607.05573).
- Llama 3/3.3, Gemma 3, GLM-4.5, MiniMax, INTELLECT evaluated in LLMForge; CodeLlama in CADCodeVerify — [LLMForge arXiv:2607.05573](https://arxiv.org/abs/2607.05573); [CADCodeVerify ICLR](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf).
- LLaVA-derived VLMs fine-tuned for CAD code: CAD-Coder (LLaVA 1.5), CAD-Coder VLM (LLaVA 1.5) — [CAD-Coder VLM arXiv:2505.14646](https://arxiv.org/abs/2505.14646).

### Inferences
- Trend: shift from zero-shot prompting of closed models (2024) to SFT/RL fine-tuning of open 7B-class models (2025), then to large frontier-model benchmarking and agentic loops (2026).

### Gaps
- Exact model versions and hyperparameters are often not fully reported; verify in each paper.

## Validation and repair loops

### Takeaway
Loops range from simple retry-on-execution-error to multi-round critique: VLM visual question-answering (CADCodeVerify), VQA-score refinement (Query2CAD), tool-augmented agent inspection (CAD-Assistant), analytic + VLM critique (LLMForge IterTracer/IterVision), self-healing tracebacks (CadCore), and RL with geometric rewards (CAD-Coder GRPO).

### Cited Findings
- CADCodeVerify: VLM generates/answers validation questions on rendered object; feedback refines code; reduced Point Cloud distance 7.30% — [ICLR 2025 PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf).
- Query2CAD: self-refinement loops up to 3 iterations using BLIP2 captions + VQA score; +23.1% success after refinements; human-in-the-loop for false negatives — [arXiv:2406.00144](https://arxiv.org/abs/2406.00144).
- LLM4CAD: debugger corrects syntax errors iteratively — [NSF](https://par.nsf.gov/biblio/10661832-llm4cad-multi-modal-large-language-models-computer-aided-design-generation).
- CAD-Assistant: tool-augmented VLLM planner executes FreeCAD code, inspects evolving geometry, refines/corrects actions — [arXiv:2412.13810](https://arxiv.org/abs/2412.13810).
- LLMForge: up to R=3 refinement rounds with structural feedback (schema errors, missing features, edge clearance), visual feedback (silhouette IoU, hole visibility, edge clearance, aspect ratio), and VLM semantic feedback (Qwen2.5-VL-72B) in IterVision — [arXiv:2607.05573](https://arxiv.org/abs/2607.05573).
- CadCore: self-healing loop captures runtime errors/invalid topology and sends tracebacks back to LLM, up to max_retries — [PyPI](https://pypi.org/project/cadcore-ai/).
- CAD-Coder: GRPO RL with CAD-specific reward (Chamfer Distance geometric reward + format reward) after SFT — [arXiv:2505.19713](https://arxiv.org/abs/2505.19713).
- ConCAD: GRPO with dual-granularity rewards (code-level constraint reward + execution-level IoU reward); execution validity gate — [arXiv:2609.34494](https://arxiv.org/html/2609.34494).
- FutureCAD: SFT then RL for generalization, plus BRepGround for primitive grounding — [arXiv:2603.11831](https://arxiv.org/abs/2603.11831).
- neuralCAD-Edit: foundation models allowed up to 10 refinement iterations; human CAD experts baseline — [arXiv:2604.16170](https://arxiv.org/abs/2604.16170).

### Inferences
- Execution feedback is necessary but not sufficient: many pipelines add visual/semantic critique because syntactically valid code can produce wrong geometry.

### Gaps
- No standardized comparison of loop strategies (rounds, feedback type) across papers was found.

## Benchmarks

### Takeaway
A crowded 2025–2026 benchmark landscape: CADPrompt (200), Text2CAD-Bench (600), CAD-Edit/neuralCAD-Edit (multimodal expert edits), CADBench (18k), BenchCAD (17.9k parts, 748 edits), MUSE (assemblies, manufacturability), CADEngBench (engineering + FEA + assembly), RealCADBench (12.6k industrial), Text2CAD-Bench, CADGenBench, tim-odonnell LLM CAD benchmark.

### Cited Findings
- CADPrompt: first benchmark for CAD code generation, 200 NL prompts + expert-annotated scripting code — [ICLR 2025 PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf).
- Text2CAD-Bench: 600 human-curated examples, 4 levels, dual-style NL descriptions, CadQuery target — [arXiv:2605.18430](https://arxiv.org/abs/2605.18430).
- neuralCAD-Edit: first expert CAD-editing benchmark, multimodal video/speech/drawing requests, 10 designers; GPT 5.2 53% below human acceptance — [arXiv:2604.16170](https://arxiv.org/abs/2604.16170).
- LLM4CAD-Editor: intent-aware CAD editing via LLM4CAD-DSL (not Python), editing robustness 1.4x over Python scripting — [arXiv:2606.20607](https://arxiv.org/abs/2606.20607).
- CADBench: 18,000 samples, 6 families (DeepCAD, Fusion 360, ABC, MCB, Objaverse), 5 modalities, 6 metrics; arXiv:2605.10873 — [arXiv](https://arxiv.org/abs/2605.10873); [GitHub](https://github.com/anniedoris/CADBench).
- BenchCAD: 17,900 verified CadQuery programs, 106 industrial families, 47 standards; tasks: Vision2Code, CodeEdit (748), Vision-QA, Code-QA (2,400); voxel IoU scoring — [arXiv:2605.10865](https://arxiv.org/abs/2605.10865); [GitHub](https://github.com/BenchCAD/BenchCAD-main); [site](https://benchcad.com/).
- MUSE: manufacturable/functional/assemblable text-to-CAD, complex B-Rep assemblies, 3-stage eval (code check, geometric check, design-intent rubrics via VLM judge) — [arXiv:2605.28579](https://arxiv.org/abs/2605.28579); [GitHub](https://github.com/dong7313/muse).
- CADEngBench: 2 tracks — P: 600 zero-to-CAD + functional-edit tasks, A: 150 assembly pairs; layered checks incl. FEA (CalculiX); 8 models — [arXiv:2608.09296](https://arxiv.org/abs/2608.09296).
- RealCADBench: 12,632 tasks, 19 factory-automation categories, 4 input regimes (text, 2D drawings, real pictures, rendered images), Part + Assembly; FreeCAD API Python output; executability, Solid/Surface IoU, VLM Judge — [arXiv:2609.03773](https://arxiv.org/abs/2609.03773).
- CADGenBench: tool-agnostic, STEP/BREP submission, generation + editing, build123d/CadQuery baselines — [GitHub](https://github.com/yntianyu/cadgenbench); [GitHub fleet-ai](https://github.com/fleet-ai/cadgenbench).
- tim-odonnell LLM CAD/Engineering Capability Benchmark: 35 tasks across 7 CAD ecosystems (Blender, Rhino, Grasshopper, FreeCAD, Alias, NX, capstones) — [GitHub](https://github.com/tim-odonnell/llm-cad-benchmark).
- LLM CAD benchmark (eaglejosh9): 77 prompts, qwen2.5-coder:14b, CadQuery, baseline vs LLM4CAD prompting — [GitHub](https://github.com/eaglejosh9/llm-cad-benchmark).
- LLMForge (Foundation Models chapter): 97 problems, 4 geometry families, 7 models, iterative critique — [arXiv:2607.05573](https://arxiv.org/abs/2607.05573).

### Inferences
- Benchmark focus moved from single-part geometric similarity (IoU) to editability, parametric validity, assembly, manufacturability, and design intent.

### Gaps
- "CAD-Edit" as a standalone named benchmark beyond BenchCAD-Edit and neuralCAD-Edit was not found; names overlap. Flag unverified.

## Metrics

### Takeaway
Metrics span code validity (execution rate, syntax validity, IR), geometric fidelity (IoU, Chamfer Distance, CD), semantic/design intent (G-CSR, CSR, GCS, VLM Judge), and edit/assembly success (normalized IoU, edit success, pair pass).

### Cited Findings
- Execution/validity: Invalidity Ratio (IR) % unexecutable/empty; Valid Shape Rate; syntax error rate (Esyntax); mesh success/watertight rate — [ConCAD arXiv:2609.34494](https://arxiv.org/html/2609.34494); [BenchCAD arXiv:2605.10865](https://arxiv.org/abs/2605.10865); [LLMForge arXiv:2607.05573](https://arxiv.org/abs/2607.05573).
- Geometric: Voxel IoU (64³), Solid IoU, Surface IoU, Chamfer Distance (CD), Point Cloud distance, silhouette IoU, hole visibility, edge clearance — [BenchCAD](https://github.com/BenchCAD/BenchCAD-main); [RealCADBench arXiv:2609.03773](https://arxiv.org/abs/2609.03773); [CADCodeVerify ICLR](https://proceedings.iclr.cc/paper_files/paper/2025/file/81a934cd364e18ea6fdeaf57a93c17d4-Paper-Conference.pdf).
- Design intent: G-CSR (B-rep Geometric Constraint Satisfaction Rate) macro-averaged over constraint categories; CSR (Constraint Satisfaction Rate) construction-level; GCS (Geometric Constraint Satisfaction); VLM rubric Judge — [ConCAD arXiv:2609.34494](https://arxiv.org/html/2609.34494); [CIT-CAD arXiv:2609.07434](http://arxiv.org/abs/2609.07434v1); [RealCADBench arXiv:2609.03773](https://arxiv.org/abs/2609.03773).
- Edit success: normalized IoU = clip((model_iou - baseline_iou)/(1 - baseline_iou),0,1); BenchCAD-Edit 748 edit pairs across T1–T5; neuralCAD-Edit human acceptance (GPT 5.2 53% below experts) — [BenchCAD CodeEdit](https://github.com/BenchCAD/BenchCAD-main/blob/main/CodeEdit/README.md); [neuralCAD-Edit arXiv:2604.16170](https://arxiv.org/abs/2604.16170).
- QA: symmetric ratio accuracy on numeric answers — [BenchCAD](https://github.com/BenchCAD/BenchCAD-main).
- Program compactness: token count, operation count — [CADBench arXiv:2605.10873](https://arxiv.org/abs/2605.10873).
- Assembly: pair pass rate, joint retrieval mAP/F1, kinematic verification — [CADEngBench arXiv:2608.09296](https://arxiv.org/abs/2608.09296); [FutureCAD arXiv:2603.11831](https://arxiv.org/abs/2603.11831).

### Inferences
- Execution rate alone overestimates quality; benchmarks increasingly report layered metrics (executability → geometry → intent → manufacturability).

### Gaps
- Metric implementations differ across papers (e.g., IoU voxel vs exact boolean); cross-paper comparison is not standardized.

## Surveys

### Takeaway
One comprehensive survey (ACM Computing Surveys, Zhang et al. 2025/2026) covers LLM applications in CAD including CAD code generation; no survey yet dedicated solely to text-to-code-to-CAD.

### Cited Findings
- Large Language Models for Computer-Aided Design: A Survey — Licheng Zhang, Bach Le, Naveed Akhtar, Siew-Kei Lam, Tuan Ngo; arXiv:2505.08137; ACM Comput. Surv. 2026 (accepted Dec 2025) — [arXiv](https://arxiv.org/abs/2505.08137); [ACM](https://dl.acm.org/doi/full/10.1145/3787499).
- Survey on LLM-based Code Generation for Low-Resource and Domain-Specific Programming Languages (ACM TOSEM, 2025) — tangentially relevant for DSLs — [ACM](https://dl.acm.org/doi/10.1145/3770084).

### Inferences
- A dedicated text-to-code-to-CAD survey would be timely given the 2025–2026 benchmark explosion.

### Gaps
- I found no survey specifically on text-to-code-to-CAD; the general LLM-for-CAD survey is the closest.