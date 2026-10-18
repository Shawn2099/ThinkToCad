# Text-to-CAD and Text-to-3D Generation Papers Catalog

## Major Text-to-CAD Papers (2023–2026)

### Takeaway
Text-to-CAD research (2024–2026) has converged on LLM/code-based generation of parametric CAD (command sequences, CadQuery scripts, STEP B-rep files), with Text2CAD (NeurIPS 2024 Spotlight) as the foundational text-to-parametric benchmark and a wave of 2025–2026 papers targeting code representations, NURBS, STEP, and evaluation.

### Cited Findings
- Text2CAD: Generating Sequential CAD Models from Beginner-to-Expert Level Text Prompts — Mohammad Sadil Khan, Sankalp Sinha, Talha Uddin Sheikh, Didier Stricker, Sk Aziz Ali, Muhammad Zeshan Afzal; arXiv:2409.17106 (cs.CV, cs.GR); NeurIPS 2024 Spotlight. First AI framework generating parametric CAD (sketch-and-extrude sequences) from text; ~170K models / ~660K text annotations over DeepCAD. — [arXiv](https://arxiv.org/abs/2409.17106)
- Text2CAD: Text to 3D CAD Generation via Technical Drawings — Mohsen Yavartanoo, Sangmin Hong, Reyhaneh Neshatavar, Kyoung Mu Lee; arXiv:2411.06206 (cs.CV); 2024. Diffusion pipeline: text → isometric image → orthographic views → 3D B-rep. — [arXiv](https://arxiv.org/abs/2411.06206)
- Query2CAD: Generating CAD models using natural language queries — Akshay Badagabettu, Sai Sravan Yarlagadda, Amir Barati Farimani; arXiv:2406.00144 (cs.LG); 2024. Zero-shot LLM (GPT-4 Turbo) generates FreeCAD Python macros with self-refinement loops; 53.6% first-attempt success, +23.1% after refinement. — [arXiv](https://arxiv.org/abs/2406.00144)
- Text-to-CadQuery: A New Paradigm for CAD Generation with Scalable Large Model Capabilities — Haoyang Xie, Feng Ju; arXiv:2505.06507 (cs.AI); 2025. Fine-tunes 6 LLMs (124M–7B) on Text2CAD-augmented DeepCAD with CadQuery annotations; top-1 exact match 69.3%, Chamfer Distance −48.6%. — [arXiv](https://arxiv.org/abs/2505.06507)
- CAD-Coder: Text-to-CAD Generation with Chain-of-Thought and Geometric Reward — Yandong Guan, Xilin Wang, Ximing Xing, Jing Zhang, Dong Xu, Qian Yu; arXiv:2505.19713 (cs.GR); NeurIPS 2025. CadQuery generation via SFT + GRPO with geometric (Chamfer Distance) + format reward; 110K verified triplets + 1.5K CoT samples. — [arXiv](https://arxiv.org/abs/2505.19713)
- CAD-Llama: Leveraging Large Language Models for Computer-Aided Design Parametric 3D Model Generation — Jiahao Li, Weijian Ma, Xueyang Li, Yunzhong Lou, Guichun Zhou, Xiangdong Zhou; arXiv:2505.04481 (cs.CV); CVPR 2025. SPCC format + hierarchical annotation + adaptive pretraining; text-to-CAD among downstream tasks. — [arXiv](https://arxiv.org/abs/2505.04481)
- FlexCAD: Unified and Versatile Controllable CAD Generation with Fine-tuned Large Language Models — Zhanwei Zhang, Shizhao Sun, Wenxiao Wang, Deng Cai, Jiang Bian; arXiv:2411.05823 (cs.CV); ICLR 2025. Mask-and-infill over structured CAD text across all hierarchies (sketch-extrusion … curve). — [arXiv](https://arxiv.org/abs/2411.05823)
- GeoCAD: Local Geometry-Controllable CAD Generation with Large Language Models — Zhanwei Zhang, Kaiyuan Liu, Junjie Liu, Wenxiao Wang, Binbin Lin, Liang Xie, Chen Shen, Deng Cai; arXiv:2506.10337 (cs.CV); NeurIPS 2025. Local part editing guided by geometric instructions; ~221K annotated local parts. — [arXiv](https://arxiv.org/abs/2506.10337)
- CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM — Jingwei Xu, Zibo Zhao, Chenyu Wang, Wen Liu, Yi Ma, Shenghua Gao; arXiv:2411.04954 (cs.CV); 2024. First MLLM for parametric CAD conditioned on text/images/point clouds; Omni-CAD dataset (~450K). — [arXiv](https://arxiv.org/abs/2411.04954)
- CAD-Assistant: Tool-Augmented VLLMs as Generic CAD Task Solvers — Dimitrios Mallis, Ahmet Serdar Karadeniz, Sebastian Cavada, Danila Rukhovich, Niki Foteinopoulou, Kseniya Cherenkova, Anis Kacem, Djamila Aouada; arXiv:2412.13810 (cs.CV); ICCV 2025. Zero-shot tool-augmented VLLM planner executing FreeCAD Python API; includes text-to-CAD workflows. — [arXiv](https://arxiv.org/abs/2412.13810)
- CAD-Recode: Reverse Engineering CAD Code from Point Clouds — Danila Rukhovich, Elona Dupont, Dimitrios Mallis, Kseniya Cherenkova, Anis Kacem, Djamila Aouada; arXiv:2412.14042 (cs.CV); ICCV 2025. Point cloud → CadQuery code (Qwen2-1.5B + projector); 1M generated programs. (Point-cloud-conditioned, included as code-representation reference.) — [arXiv](https://arxiv.org/abs/2412.14042)
- Generating CAD Code with Vision-Language Models for 3D Designs (CADCodeVerify) — Kamel Alrashedy, Pradyumna Tambwekar, Zulfiqar Zaidi, Megan Langwasser, Wei Xu, Matthew Gombolay; arXiv:2410.05340 (cs.LG); ICLR 2025. Iterative VLM verification/refinement of CadQuery code; introduces CADPrompt benchmark (200 objects). — [arXiv](https://arxiv.org/abs/2410.05340)
- Text-to-CAD Generation Through Infusing Visual Feedback in Large Language Models (CADFusion) — Ruiyu Wang, Yu Yuan, Shizhao Sun, Jiang Bian; arXiv:2501.19054 (cs.CV); ICML 2025. Alternates sequential learning and visual-feedback (rendered image preference) stages. — [arXiv](https://arxiv.org/abs/2501.19054)
- CADmium: Fine-Tuning Code Language Models for Text-Driven Sequential CAD Design — Prashant Govindarajan, Davide Baldelli, Jay Pathak, Quentin Fournier, Sarath Chandar; arXiv:2507.09792 (cs.GR); TMLR 2026. Code-LLMs fine-tuned on 170K CAD models with GPT-4.1 descriptions; JSON-based CAD sequences; geometric/topological metrics (sphericity, curvature, Euler characteristic). — [arXiv](https://arxiv.org/abs/2507.09792)
- CAD-Tokenizer: Towards Text-based CAD Prototyping via Modality-Specific Tokenization — Ruiyu Wang, Shizhao Sun, Weijian Ma, Jiang Bian; arXiv:2509.21150 (cs.LG); ICLR 2026. VQ-VAE primitive-level tokenization for unified text-to-CAD generation + editing. — [arXiv](https://arxiv.org/abs/2509.21150)
- CADSmith: Multi-Agent CAD Generation with Programmatic Geometric Validation — Jesse Barkley, Rumi Loghmani, Amir Barati Farimani; arXiv:2603.26512 (cs.AI); 2026. Multi-agent CadQuery pipeline with inner (execution) and outer (OpenCASCADE measurement + VLM judge) correction loops; F1 0.9707→0.9846, IoU 0.8085→0.9629, CD 28.37→0.74. — [arXiv](https://arxiv.org/abs/2603.26512)
- CAD-Judge: Toward Efficient Morphological Grading and Verification for Text-to-CAD Generation — Zheyuan Zhou, Jiayi Han, Liang Du, Naiyu Fang, Lemiao Qiu, Shuyou Zhang; arXiv:2508.04002 (cs.CV); 2025. Compiler-as-a-Judge / Compiler-as-a-Review modules as fast reward/verification signals. — [arXiv](https://arxiv.org/abs/2508.04002)
- STEP-LLM: Generating CAD STEP Models from Natural Language with Large Language Models — Xiangyu Shi, Junyang Ding, Xu Zhao, Sinong Zhan, Payal Mohapatra, Daniel Quispe, Kojo Welbeck, Jian Cao, Wei Chen, Ping Guo, Qi Zhu; arXiv:2601.12641 (cs.AI); DATE 2026. First direct STEP/B-rep generation; DFS reserialization + RAG + RL with CD reward; ~40K caption–STEP pairs; MSCD 3.99→0.53 vs Text2CAD. — [arXiv](https://arxiv.org/abs/2601.12641)
- NURBGen: High-Fidelity Text-to-CAD Generation through LLM-Driven NURBS Modeling — Muhammad Usama, Mohammad Sadil Khan, Didier Stricker, Muhammad Zeshan Afzal; arXiv:2511.06194 (cs.CV); AAAI 2026. LLM (Qwen3-4B) maps text → NURBS params (control points, knots, degrees, weights) → B-Rep; partABC dataset (~300K components from ABC). — [arXiv](https://arxiv.org/abs/2511.06194)
- Text-to-CAD Evaluation with CADTests (CADTestBench) — Dimitrios Mallis, Marco Wang, Ahmet Serdar Karadeniz, Elisa Ricci, Anis Kacem, Djamila Aouada; arXiv:2605.07807 (cs.CV); 2026. Test-based evaluation: executable CADTests over B-rep; 5,937 tests over 200 CADPrompt programs. — [arXiv](https://arxiv.org/abs/2605.07807)
- Text2CAD-Bench: A Benchmark for LLM-based Text-to-Parametric CAD Generation — Liang Wang, Heng Meng, Zekai Xiang, Jin Liu, Pingyi Zhou, Litao Chen, Yongqiang Tang; arXiv:2605.18430 (cs.LG); 2026. 600 human-curated examples across 4 complexity levels; dual-style prompts (geometric vs. procedural). — [arXiv](https://arxiv.org/abs/2605.18430)
- MUSE: Benchmarking Manufacturable, Functional, and Assemblable Text-to-CAD Generation — Xiaoyu Dong, Zhi Li, Xiao-Ming Wu; arXiv:2605.28579 (cs.AI); 2026. B-Rep assembly benchmark with design-intent rubrics (functionality, manufacturability, assemblability). — [arXiv](https://arxiv.org/abs/2605.28579)
- SldprtNet: A Large-Scale Multimodal Dataset for CAD Generation in Language-Driven 3D Design — (authors per arXiv 2603.13098); arXiv:2603.13098 (cs.RO); ICRA 2026. 242K SolidWorks .sldprt parts with 13 CAD feature types, rendered views, natural-language descriptions. — [arXiv](https://arxiv.org/abs/2603.13098)
- Text-to-CAD Retrieval: a Strong Baseline — (arXiv 2605.05572); 2026. Retrieval baseline over text–CAD (DeepCAD/Text2CAD) embedding spaces. — [arXiv](https://arxiv.org/html/2605.05572v1)
- LLM4CAD: Multimodal Large Language Models for Three-Dimensional Computer-Aided Design Generation — Yuewan Sun, Xingang Li, Zhenghui Sha; Journal of Mechanical Design, 2025 (NSF PAR). Text+image mechanical components (gears, shafts, springs); IoU evaluation; fine-tuned GPT-3.5 pipeline. — [NSF PAR](https://par.nsf.gov/biblio/10661922-llm4cad-multimodal-large-language-models-three-dimensional-computer-aided-design-generation)
- CAD-Translator (Li et al.) — cited in CAD-Judge/CADFusion as encoder-decoder transformer for text→CAD sequences (ACM MM 2024 era); arXiv ID not located in this search (low-confidence citation). — [ACM DL](https://dl.acm.org/doi/10.1145/3664647.3681549)

### Inferences
- The field's center of gravity shifted from transformer seq2seq over DeepCAD command tokens (2024) to LLM code generation (CadQuery/STEP/NURBS) in 2025–2026, leveraging pretrained code priors.
- CadQuery has become the dominant intermediate representation for LLM-based text-to-CAD; STEP and NURBS are emerging for manufacturing fidelity.
- Evaluation is moving from pure geometric similarity (CD/IoU) toward validity/editability and test-based (CADTests) and engineering-intent (MUSE) benchmarks.

### Gaps
- Several papers (CAD-Translator, CADFusion's full arXiv provenance, UniCAD) could not be fully verified via arXiv search in this pass; treated as lower-confidence citations.
- No comprehensive survey dedicated solely to text-to-CAD evaluation standards exists beyond the LLM-for-CAD surveys cited below.

## Methods Used (diffusion, autoregressive, transformer, LLM-based)

### Takeaway
Methods span (a) autoregressive transformers over quantized CAD command tokens, (b) LLM fine-tuning/code generation (CadQuery, STEP, NURBS/JSON), (c) diffusion over technical drawings, and (d) tool-augmented/multi-agent VLLM loops with geometric feedback.

### Cited Findings
- Autoregressive transformer over CAD command tokens conditioned on text: Text2CAD (arXiv:2409.17106) — [arXiv](https://arxiv.org/abs/2409.17106)
- Diffusion (Stable Diffusion) text→isometric→orthographic drawings→B-rep: Text2CAD technical-drawings paper (arXiv:2411.06206) — [arXiv](https://arxiv.org/abs/2411.06206)
- LLM code generation (CadQuery) with SFT+RL (GRPO) and geometric reward: CAD-Coder (arXiv:2505.19713); Text-to-CadQuery (arXiv:2505.06507) — [arXiv](https://arxiv.org/abs/2505.19713)
- Mask-and-infill controllable generation via LLMs: FlexCAD (arXiv:2411.05823), GeoCAD (arXiv:2506.10337) — [arXiv](https://arxiv.org/abs/2411.05823)
- MLLM multimodal conditioning (text/image/point cloud): CAD-MLLM (arXiv:2411.04954) — [arXiv](https://arxiv.org/abs/2411.04954)
- Tool-augmented VLLM agent with FreeCAD API: CAD-Assistant (arXiv:2412.13810); CADSmith (arXiv:2603.26512) — [arXiv](https://arxiv.org/abs/2412.13810)
- Zero-shot LLM macros + self-refinement: Query2CAD (arXiv:2406.00144) — [arXiv](https://arxiv.org/abs/2406.00144)
- Visual-feedback RL (sequential learning ↔ rendered-image preference): CADFusion (arXiv:2501.19054) — [arXiv](https://arxiv.org/abs/2501.19054)
- LLM→STEP with DFS reserialization + RAG + RL: STEP-LLM (arXiv:2601.12641) — [arXiv](https://arxiv.org/abs/2601.12641)
- LLM→NURBS params: NURBGen (arXiv:2511.06194) — [arXiv](https://arxiv.org/abs/2511.06194)
- Primitive-aware tokenization (VQ-VAE) feeding LLMs: CAD-Tokenizer (arXiv:2509.21150) — [arXiv](https://arxiv.org/abs/2509.21150)
- VLM iterative verification of generated code: CADCodeVerify (arXiv:2410.05340) — [arXiv](https://arxiv.org/abs/2410.05340)

### Inferences
- The dominant paradigm moved from "train a transformer from scratch on CAD tokens" to "fine-tune/pretrain LLMs on code-like CAD representations," leveraging code priors.
- RL with geometric rewards (Chamfer Distance) is increasingly used to close the gap between syntactic validity and geometric fidelity.

### Gaps
- No head-to-head comparison across all methods on a single unified benchmark yet; CADTestBench/Text2CAD-Bench/MUSE are emerging but not universally adopted.

## Datasets (DeepCAD, Fusion 360 Gallery, ABC, Text2CAD, etc.)

### Takeaway
Foundational datasets are DeepCAD (command sequences), ABC (B-rep/NURBS), Fusion 360 Gallery (sketches/extrusions); text-aligned derivatives include Text2CAD (~170K models/~660K prompts), Omni-CAD (~450K multimodal), partABC (~300K), SldprtNet (242K SolidWorks parts), and STEP caption–STEP pairs (~40K).

### Cited Findings
- DeepCAD: 178,238 CAD models as sketch-and-extrude command sequences; base for Text2CAD annotations — [Text2CAD paper](https://arxiv.org/abs/2409.17106)
- Text2CAD dataset: ~170K models, ~660K text annotations (L0–L3 abstraction levels) over DeepCAD — [arXiv:2409.17106](https://arxiv.org/abs/2409.17106)
- ABC dataset: B-rep/NURBS CAD models; source for NURBGen's partABC (~300K components) and NURBS captions — [arXiv:2511.06194](https://arxiv.org/abs/2511.06194)
- Fusion 360 Gallery: sketch/extrusion design history; used by CAD-Recode evaluation — [arXiv:2412.14042](https://arxiv.org/abs/2412.14042)
- Omni-CAD: ~450K instances with text, multi-view images, point clouds, command sequences (CAD-MLLM) — [arXiv:2411.04954](https://arxiv.org/abs/2411.04954)
- SldprtNet: 242K SolidWorks .sldprt parts, 13 feature types, rendered views + descriptions — [arXiv:2603.13098](https://arxiv.org/abs/2603.13098)
- STEP caption–STEP pairs: ~40K (STEP-LLM) — [arXiv:2601.12641](https://arxiv.org/abs/2601.12641)
- CADPrompt: 200 objects with natural-language prompts + ground-truth code (CADCodeVerify/CADTestBench) — [arXiv:2410.05340](https://arxiv.org/abs/2410.05340)
- LLM4CAD dataset: synthetic mechanical components (gears, shafts, springs) with AMT descriptions — [NSF PAR](https://par.nsf.gov/biblio/10661922-llm4cad-multimodal-large-language-models-three-dimensional-computer-aided-design-generation)
- CADmium dataset: 170K CAD models with GPT-4.1-generated human-like descriptions — [arXiv:2507.09792](https://arxiv.org/abs/2507.09792)

### Inferences
- Text-aligned CAD data is mostly auto-annotated (LLM/VLM pipelines), creating a dependency on annotation quality; human-verified subsets (CADPrompt, Text2CAD-Bench) are emerging.

### Gaps
- Fusion 360 Gallery and ABC are not natively text-annotated; text labels are synthesized, which may bias language coverage.

## Representations (B-rep, mesh, point cloud, SDF, voxel, parametric)

### Takeaway
Text-to-CAD targets parametric command sequences and code (CadQuery, Python macros, JSON, STEP B-rep, NURBS); meshes/point clouds appear mainly as inputs or evaluation geometry, not as primary generation targets.

### Cited Findings
- Parametric command sequences (sketch + extrude, quantized coords): Text2CAD (arXiv:2409.17106), CAD-MLLM (arXiv:2411.04954) — [arXiv](https://arxiv.org/abs/2409.17106)
- CadQuery Python code: Text-to-CadQuery (arXiv:2505.06507), CAD-Coder (arXiv:2505.19713), CADSmith (arXiv:2603.26512), Query2CAD (FreeCAD macros, arXiv:2406.00144) — [arXiv](https://arxiv.org/abs/2505.06507)
- STEP / B-rep files: STEP-LLM (arXiv:2601.12641), MUSE (arXiv:2605.28579) — [arXiv](https://arxiv.org/abs/2601.12641)
- NURBS surfaces → B-Rep: NURBGen (arXiv:2511.06194) — [arXiv](https://arxiv.org/abs/2511.06194)
- JSON-based CAD sequences: CADmium (arXiv:2507.09792) — [arXiv](https://arxiv.org/abs/2507.09792)
- SPCC (Structured Parametric CAD Code): CAD-Llama (arXiv:2505.04481) — [arXiv](https://arxiv.org/abs/2505.04481)
- Mesh/point cloud as input modality (not generation target): CAD-Recode (point cloud→code), CAD-MLLM (point clouds), CAD-Assistant (3D scans) — [arXiv](https://arxiv.org/abs/2412.14042)
- Technical drawings (images) as intermediate: Text2CAD diffusion (arXiv:2411.06206) — [arXiv](https://arxiv.org/abs/2411.06206)

### Inferences
- Parametric/code representations dominate because they preserve editability and design history, which meshes/point clouds/SDFs do not.

### Gaps
- Direct generation of meshes/SDFs/voxels from text is largely the domain of general text-to-3D (not CAD-specific) and is out of scope here; CAD research favors B-rep/parametric outputs.

## Evaluation Metrics (IoU, Chamfer distance, F1, validity, editability)

### Takeaway
Metrics include geometric similarity (Chamfer Distance, IoU), validity/renderability, exact-match/command accuracy, and newer test-based (CADTests pass rate/requirement score) and engineering-intent (MUSE rubrics) measures.

### Cited Findings
- Chamfer Distance (CD) and IoU: standard geometric similarity vs. ground-truth — CAD-Coder (arXiv:2505.19713), STEP-LLM (MSCD, arXiv:2601.12641), Text-to-CadQuery (arXiv:2505.06507) — [arXiv](https://arxiv.org/abs/2505.19713)
- Invalid Rate (IR) / Renderability Ratio (RR): code execution success — Text-to-CadQuery (IR), STEP-LLM (RR 95.18%) — [arXiv](https://arxiv.org/abs/2505.06507)
- Top-1 exact match of command sequences: Text-to-CadQuery (69.3%) — [arXiv](https://arxiv.org/abs/2505.06507)
- F1 / IoU on generated vs. ground-truth: CADSmith (F1 0.9846, IoU 0.9629) — [arXiv](https://arxiv.org/abs/2603.26512)
- Command/parameter accuracy (Acc_command, Acc_parameter): CAD-Recode — [arXiv](https://arxiv.org/abs/2412.14042)
- Coverage (COV), Minimum Matching Distance (MMD), Jensen-Shannon Divergence (JSD): unconditional generation — CAD-Llama (arXiv:2505.04481) — [arXiv](https://arxiv.org/abs/2505.04481)
- Geometric/topological metrics (sphericity, mean curvature, Euler characteristic): CADmium (arXiv:2507.09792) — [arXiv](https://arxiv.org/abs/2507.09792)
- CADTests pass rate, requirement score, invalidity rate over B-rep: CADTestBench (arXiv:2605.07807) — [arXiv](https://arxiv.org/abs/2605.07807)
- Gemini 2.0 Flash / GPT-4 / human evaluation of rendered images: Text-to-CadQuery, Text2CAD diffusion MOS 8.375/10 — [arXiv](https://arxiv.org/abs/2411.06206)
- Feature-presence accuracy: Text2CAD diffusion (~90%+) — [arXiv](https://arxiv.org/abs/2411.06206)
- Entity count alignment (STEP): STEP-LLM (avg 240.99 vs GT 265.64) — [arXiv](https://arxiv.org/abs/2601.12641)
- MUSE three-stage protocol: code check → geometric check → design-intent rubrics (functionality, manufacturability, assemblability) via VLM judge — [arXiv](https://arxiv.org/abs/2605.28579)

### Inferences
- Geometric similarity (CD/IoU) is increasingly criticized as insufficient because it penalizes valid design variations; test-based and intent-based evaluation is emerging to address this (CADTests, MUSE).

### Gaps
- No single standardized evaluation protocol exists; papers use heterogeneous metric suites, hindering comparison.

## Surveys and Benchmarks

### Takeaway
Three surveys cover LLMs-for-CAD and AI-driven CAD generation; benchmarks include Text2CAD (dataset), CADPrompt, CADTestBench, Text2CAD-Bench, MUSE, and Omni-CAD.

### Cited Findings
- Large Language Models for Computer-Aided Design: A Survey — (arXiv:2505.08137, Zhang et al., ACM manuscript, 2025/2026); comprehensive LLM-for-CAD survey (data generation, code generation, parametric generation, evaluation). — [arXiv](https://arxiv.org/abs/2505.08137)
- AI-Driven Generation of 3D CAD Models: A Survey — Wu et al.; IEEE 2026 (cited by 2–3); covers representations, datasets, machine learning methods, LLMs. — [IEEE](https://ieeexplore.ieee.org/document/11503120)
- A Survey on Generative AI for 3-D CAD in Engineering — Klein, Mueller-Roemer, Stork; IEEE CG&A, May–Jun 2026. — [IEEE](https://www.computer.org/csdl/magazine/cg/2026/03/11397452/2e9R0ceuB68)
- UniCAD: A Unified Benchmark and Universal Model for Multi-Modal Multi-Task CAD — mentioned via Semantic Scholar as related to CAD-MLLM (arXiv:2411.04954 references); specific arXiv ID not verified here (low confidence). — [Semantic Scholar](https://www.semanticscholar.org/paper/CAD-MLLM%3A-Unifying-Multimodality-Conditioned-CAD-Xu-Wang/1b111d932d4bfb7b1112a550f04e25d9cf472e0d)

### Inferences
- The LLM-for-CAD survey (arXiv:2505.08137) is the most directly relevant synthesis for text-to-CAD; the IEEE surveys broaden to generative-AI-for-CAD generally.

### Gaps
- No dedicated, widely-adopted text-to-CAD benchmark existed before 2025; standardization is still in progress (CADTestBench, Text2CAD-Bench, MUSE all 2026).