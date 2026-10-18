# AI + CAD Research Catalog (Master Index)

## 1. Purpose and how to use

This master catalog indexes research on AI for computer-aided design (CAD), synthesized from the 9 research notes in `research_notes/AI and CAD research papers catalog/`. It is an index, not a paper. Use it to:

- Find relevant papers by category (Text-to-CAD, editing, assemblies, etc.).
- Get a one-line method and key result per paper before reading the source.
- Jump to the underlying research note for full citations, inferences, and gaps.
- Cross-check arXiv IDs against the cited links in the notes before citing in your own work.

Counts and metrics are taken from paper abstracts as captured in the notes; full-text verification was not performed. Items flagged "unverified" or "low confidence" in the notes are either omitted or marked.

## 2. AI pointer rules

- Treat arXiv IDs as lookup keys, not as proof. Verify title, authors, and numbers in the primary source before citation.
- Do not invent paper details. If an ID is missing (journal-only or DOI-only work), the "arXiv ID" cell shows the DOI/ID that is available.
- Low-confidence items (e.g., CAD-Translator, UniCAD, AgentCAD, "CADAssembly" benchmark) are deliberately excluded or flagged; search the notes for "unverified" before relying on them.
- A paper may appear in more than one category when it spans tasks (e.g., MUSE is both Text-to-CAD and Assembly). Category placement reflects primary focus.
- Counts in the summary are row counts in this catalog; unique-ID counts are reported separately. Overlaps are expected.
- Do not modify the research notes or other repository files based on this catalog; it is a derived index.

## 3. Categories with paper tables

Counts below are rows in each table.

### 3.1 Text-to-CAD (25 rows)

| Title | arXiv ID | Year | Method | Key result |
|---|---|---|---|---|
| Text2CAD: Generating Sequential CAD Models from Text Prompts | 2409.17106 | 2024 | Autoregressive transformer over DeepCAD command tokens | First text-to-parametric CAD; ~170K models / ~660K prompts |
| Text2CAD: Text to 3D CAD via Technical Drawings | 2411.06206 | 2024 | Diffusion: text -> isometric -> orthographic -> B-rep | MOS 8.375/10; ~90%+ feature presence |
| Query2CAD | 2406.00144 | 2024 | Zero-shot LLM (GPT-4 Turbo) FreeCAD macros + self-refinement | 53.6% first-attempt; +23.1% after refinement |
| Text-to-CadQuery | 2505.06507 | 2025 | LLM fine-tuning (124M-7B) on CadQuery annotations | Top-1 exact match 69.3%; CD -48.6% |
| CAD-Coder (Guan et al.) | 2505.19713 | 2025 | CadQuery generation via SFT + GRPO geometric reward | 110K verified triplets; NeurIPS 2025 |
| CAD-Llama | 2505.04481 | 2025 | SPCC format + hierarchical annotation + adaptive pretraining | CVPR 2025; text-to-CAD downstream |
| FlexCAD | 2411.05823 | 2025 | Mask-and-infill over structured CAD text (all hierarchies) | ICLR 2025; controllable generation/editing |
| GeoCAD | 2506.10337 | 2025 | Local part editing guided by geometric instructions | ~221K annotated local parts; NeurIPS 2025 |
| CAD-MLLM | 2411.04954 | 2024 | First MLLM for parametric CAD (text/image/point cloud) | Omni-CAD ~450K instances |
| CAD-Assistant | 2412.13810 | 2024/25 | Tool-augmented VLLM planner executing FreeCAD Python API | ICCV 2025; includes text-to-CAD workflows |
| CAD-Recode | 2412.14042 | 2024/25 | Point cloud -> CadQuery code (Qwen2-1.5B + projector) | 1M generated programs; ICCV 2025 |
| CADCodeVerify | 2410.05340 | 2025 | Iterative VLM verification/refinement of CadQuery code | CADPrompt benchmark (200 objects); ICLR 2025 |
| CADFusion | 2501.19054 | 2025 | Alternating sequential learning + visual-feedback preference | ICML 2025 |
| CADmium | 2507.09792 | 2026 | Code-LLMs on 170K CAD models; JSON-based sequences | Geometric/topological metrics (sphericity, curvature, Euler) |
| CAD-Tokenizer | 2509.21150 | 2026 | VQ-VAE primitive-level tokenization feeding LLMs | Unified generation + editing; ICLR 2026 |
| CADSmith | 2603.26512 | 2026 | Multi-agent CadQuery pipeline with inner/outer correction loops | F1 0.9707->0.9846; IoU 0.8085->0.9629; CD 28.37->0.74 |
| CAD-Judge | 2508.04002 | 2025 | Compiler-as-a-Judge / Compiler-as-a-Review reward signals | Fast verification for text-to-CAD grading |
| STEP-LLM | 2601.12641 | 2026 | LLM -> STEP/B-rep (DFS reserialization + RAG + RL) | ~40K caption-STEP pairs; MSCD 3.99->0.53 |
| NURBGen | 2511.06194 | 2026 | LLM (Qwen3-4B) -> NURBS params -> B-Rep | partABC ~300K components; AAAI 2026 |
| CADTestBench | 2605.07807 | 2026 | Test-based evaluation over B-rep (executable CADTests) | 5,937 tests over 200 CADPrompt programs |
| Text2CAD-Bench | 2605.18430 | 2026 | Human-curated benchmark, 4 complexity levels | 600 examples; dual-style prompts |
| MUSE | 2605.28579 | 2026 | B-Rep assembly benchmark with design-intent rubrics | Functionality, manufacturability, assemblability |
| SldprtNet | 2603.13098 | 2026 | 242K SolidWorks .sldprt parts + rendered views + descriptions | 13 CAD feature types; ICRA 2026 |
| Text-to-CAD Retrieval | 2605.05572 | 2026 | Retrieval baseline over text-CAD embedding spaces | DeepCAD/Text2CAD embedding spaces |
| LLM4CAD (Sun, Li, Sha) | n/a (NSF PAR 10661922) | 2025 | Fine-tuned GPT-3.5 on mechanical components (gears/shafts/springs) | ASME J. Mech. Des. 147(4); text+image -> CAD programs |

### 3.2 Text-to-Code-to-CAD (18 rows)

| Title | arXiv ID | Year | Method | Key result |
|---|---|---|---|---|
| Text2CAD (seq baseline) | 2409.17106 | 2024 | DeepCAD command sequences (contrast baseline for code methods) | Foundational text-to-parametric benchmark |
| Generative AI for CAD Automation | 2508.00843 | 2025 | FreeCAD + LLM scripts with iterative error-feedback refinement | Good on simple/moderate designs |
| Automated CAD Modeling Sequence Generation | 2505.19490 | 2025 | CAutoD framework: TCADGen Transformer + CADLLM | Text -> modeling sequence generation |
| CAD-Coder (Doris et al., MIT) | 2505.14646 | 2025 | VLM (LLaVA 1.5) for CAD code generation | Open-source; GitHub available |
| Learning From Design Procedure | 2603.06894 | 2026 | CadQuery/Build123d code generation via design procedures (OpenAI o3) | Data augmentation for CAD programs |
| FutureCAD | 2603.11831 | 2026 | CadQuery + BRepGround primitive grounding; SFT then RL | ICML 2026 Spotlight |
| Foundation Models for Automatic CAD Generation | 2607.05573 | 2026 | LLMForge: 7 models, up to 3 refinement rounds (IterTracer/IterVision) | 97 problems, 4 geometry families |
| Generative AI meets CAD (OpenSCAD) | 10.1007/s00170-025-15830-2 | 2025 | GPT-4o OpenSCAD generation with closed feedback loop | Springer Int. J. Adv. Manuf. Technol. |
| Seek-CAD | 2505.17702 | 2025/26 | Training-free local DeepSeek-R1 CAD generation + visual/CoT self-refinement | ICLR 2026 |
| Zero-to-CAD | 2604.24479 | 2026 | Agentic search synthesizes ~1M executable CAD sequences; VLM reconstructs code | Beats GPT-5.2 on multi-view reconstruction |
| CAD-Assistant | 2412.13810 | 2024/25 | FreeCAD Python API tool use (also listed 3.1) | Generic CAD task solver |
| CAD-Recode | 2412.14042 | 2024/25 | Point cloud -> CadQuery code (also listed 3.1) | 1M programs |
| CADCodeVerify | 2410.05340 | 2025 | VLM iterative verification of CadQuery code (also listed 3.1) | CADPrompt benchmark |
| ConCAD | 2609.34494 | 2026 | GRPO with dual-granularity rewards (constraint + IoU) | G-CSR design-intent metric |
| LLM4CAD-Editor | 2606.20607 | 2026 | Intent-aware editing via LLM4CAD-DSL; 1.4x robustness over Python | IDETC/CIE 2026 |
| CADMorph | 2512.11480 | 2026 | Plan-generate-verify loop: P2S diffusion + MPP infilling for shape matching | No triplet data needed |
| BenchCAD | 2605.10865 | 2026 | 17,900 verified CadQuery programs; VQA/code QA/image-to-code/edit tasks | 106 industrial families; 47 standards |
| CADBench | 2605.10873 | 2026 | 18,000 samples, 6 families, 5 modalities, 6 metrics | 11 VLMs; >1.4M programs |

### 3.3 Agentic / Knowledge-Guided CAD (26 rows)

| Title | arXiv ID | Year | Method | Key result |
|---|---|---|---|---|
| DeciCAD | 2610.21755 | 2026 | Harness-grounded action policies; SFT + geometry-grounded online RL | Best F1/IoU on 4 CAD benchmarks; 45-88% fewer tokens |
| AgenticCADedit | 2609.29621 | 2026 | Stateful tool-mediated multimodal editing via persistent CAD state + revert | Validity 51.0%->94.8% (qwen3.6-27b) |
| ReliCAD | 2609.22325 | 2026 | Design-intent -> constraint-aware instructions -> agent-ready kernel API + repair | 99.8% validity; 0.8753 IoU |
| DFM-Redesign (Welbeck et al.) | 2609.05559 | 2026 | Multi-agent DFM Reviewer + CAD Modifier with compile+visual verification | 46-part benchmark |
| RA-CAD | 2608.05714 | 2026 | Generate-Execute-Critique-Rewrite loop with learnable critique (CCB+FAO, GRPO) | SOTA validity/geometry |
| CADIR | 2608.00891 | 2026 | Cross-backend editable IR on OCCT with construction graph | Reconstructs to FreeCAD/SolidWorks/Fusion 360 |
| CAD-Assistant | 2412.13810 | 2024/25 | VLLM planner + tool augmentation over FreeCAD Python API | ICCV 2025 |
| Idea-to-CAD (Ocker et al.) | 2503.04417 | 2025 | VLM multi-agent (requirements/CAD/vision-QA) from sketches/text | Iterative validation |
| Mechanical Design Agent (Lu et al.) | 2408.02087 | 2024 | Method for building a comprehensive Mechanical Design Agent | Guides LLM learning |
| AGENT (aircraft) | 2504.08981 | 2025 | CodeT5+ over AircraftVerse; conditional generation + surrogate simulation | Aircraft design tool |
| Luban | 2405.15414 | 2024 | Creative building agent with two-level embodied verification | CAD modeling programs + functional verification |
| DropMicroFluidAgents | 2501.14772 | 2025 | Agents generate ML models + code-based CAD scripts for microfluidics | Autonomous research framework |
| Knowledge-Guided Multi-Agent (Karniadakis) | 2511.03179 | 2025 | Multi-agent (Graph Ontologist/Design/Systems Engineer) + domain KGs | NACA airfoil aerodynamic optimization |
| Automotive AEI (Son et al.) | 2604.07784 | 2026 | Agentic Engineering Intelligence: constrained history-aware decision processes | Offline workflow memory + online retrieval |
| IndustryForge-27B | 2607.28050 | 2026 | Domain-enhanced multimodal foundation model for industrial CAD | CAD-focused foundation model |
| RealCADBench | 2609.03773 | 2026 | 12,632 industrial intent tasks; FreeCAD API Python | Executability, IoU, visual-semantic judge |
| CADWorld | 2609.16251 | 2026 | Computer-use benchmark: 200 tasks / 11 workflow categories in FreeCAD GUI | Best agent 17.5% vs 87% expert |
| EngiWorld | 2609.37686 | 2026 | 1,301 tasks across 6 domains and 26 apps | Best agent 44.7/100 |
| LMBuild | 2610.04292 | 2026 | Benchmark for buildable/functional assembled structures | LLM agents retrieve/create/place components |
| OmniMech | 2608.05539 | 2026 | Million-scale multimodal mechanical benchmark | Includes tool-augmented agentic reasoning task |
| On Evaluation of eAGI | 2505.10653 | 2025 | Framework for evaluating engineering AGI agents | CAD/SysML artifacts as structured outputs |
| Design-to-Plan | 2608.24039 | 2026 | Orchestrator over specialized agents (3D/2D/fusion/knowledge/sequencing) | Knowledge retrieval agent + manufacturing rules |
| Diekmann VCM | 2606.03255 | 2026 | Virtual commissioning VCMs: system understanding/component gen/signal mapping | Siemens TIA Portal + NX MCD |
| Corpus2Skill | 2604.14572 | 2026 | Offline compiler distills corpus into hierarchical skill directory | Improves RAG grounding; EMNLP 2026 Findings |
| Knowledge-as-Skill | 2609.25991 | 2026 | Higher Factuality/Context Recall than Corpus2Skill | Related knowledge-compilation approach |
| HERA (multi-agent RAG) | 2604.00901 | 2026 | Hierarchical framework evolving orchestration topologies + prompt evolution | +38.69% avg on 6 knowledge-intensive benchmarks |

### 3.4 CAD Editing & Manipulation (18 rows)

| Title | arXiv ID | Year | Method | Key result |
|---|---|---|---|---|
| CAD-Editor | 2502.03997 | 2025 | Locate-then-infill over sketch-and-extrude sequences | First text-based CAD editing; ICML 2025 |
| FlexCAD | 2411.05823 | 2025 | Hierarchy-aware masking for editing at sketch/extrusion/face/loop/curve | PV up to 93.4% sketch-level |
| CADMorph | 2512.11480 | 2026 | Geometry-driven editing: P2S diffusion + MPP infilling to match target shape | NeurIPS 2025; no triplet data |
| B-repLer | 2508.10201 | 2025/26 | Language-guided B-rep editing in latent space (HoLa-BRep) | SIGGRAPH 2026; BrepEDIT-240K |
| BrepGen | 2401.15563 | 2024 | B-rep generative diffusion; autocomplete and interpolation edits | Hierarchical tree diffusion |
| Semantic Direct Modeling | 2504.13893 | 2025 | LLM + conditional feature recognition -> direct B-rep modifications | Natural-language intent to B-rep edits |
| PR-CAD | 2604.19773 | 2026 | Progressive refinement unifying generation and editing (add/mod/delete) | Qualitative + quantitative instructions |
| ReliCAD | 2609.22325 | 2026 | Verification-feedback repair for editing (see 3.3) | Beats CAD-Editor on multi-granularity editing |
| LLM4CAD-Editor | 2606.20607 | 2026 | DSL-based editing with functional/operation/parameter intents | 1.4x robustness over Python scripting |
| TraceCAD | 2608.03062 | 2026 | Trace-guided localized repair with preservation checks + skill memory | Promotes patch only when all evidence agrees |
| AgenticCADedit | 2609.29621 | 2026 | Stateful agentic multimodal editing (see 3.3) | Validity 51.0%->94.8% |
| neuralCAD-Edit | 2604.16170 | 2026 | Expert multimodal editing benchmark (Autodesk Research) | 192 requests + 384 edits; 10 designers |
| eCAD-Net | n/a (CAD journal 2025) | 2025 | Deep learning reconstruction of editable parametric models from B-Rep | Reverse engineering into editable form |
| HistCAD | 2602.19171 | 2026 | Constraint-aware parametric history representation/dataset/benchmark | 170K/180K histories; cPCSR preservation |
| RealCADBench | 2609.03773 | 2026 | Industrial intent editing incl. assembly (see 3.3) | 12,632 tasks |
| CADEngBench | 2608.09296 | 2026 | 12 edit types + hidden preservation checks + FEA | 300 parts, 600 tasks; assembly track |
| Nova3D | 2607.22738 | 2026 | Code-native generation with local edits preserving locality | 18/18 local edits preserved |
| BrepDiff | n/a (SIGGRAPH 2025) | 2025 | Single-stage B-rep diffusion over masked UV grids | Completion, merging, interpolation edits |

### 3.5 Assembly & Multi-Part CAD (22 rows)

| Title | arXiv ID | Year | Method | Key result |
|---|---|---|---|---|
| ArtiCAD | 2604.10992 | 2026 | Multi-agent code gen with Connector-first joints before geometry | Training-free articulated assemblies; URDF export |
| AssemCAD | 2607.05123 | 2026 | Typed parts, geometry-backed ports, executable mates, axioms | Port/mate-first assembly generation |
| MUSE | 2605.28579 | 2026 | B-Rep assembly benchmark with design-intent rubrics (see 3.1) | Manufacturability/assemblability |
| ComAct / ComCADBench | 2606.13239 | 2026 | Agents in real industrial CAD software via COM-as-Action | Frontier models near-zero under GUI |
| CADWorld | 2609.16251 | 2026 | Computer-use CAD benchmark (see 3.3) | Best agent 17.5% vs 87% expert |
| CADEngBench | 2608.09296 | 2026 | Assembly track: joint retrieval, face/edge grounding, kinematics | 150 body pairs; 7 joint types |
| RealCADBench | 2609.03773 | 2026 | Assembly slice (RCB-Assm25) with placement/structure judge | Recurring "incorrect assembly placement" |
| VisCAD | 2609.03811 | 2026 | Multimodal industrial CAD foundation model suite | CAD-focused foundation model |
| Embodied CAD | 2606.31252 | 2026 | Solver-grounded LLM agents for parametric B-Rep assembly | Parametric B-Rep assembly modeling |
| Linkify | 2607.01205 | 2026 | Assembly graphs with part nodes + interface-geometry edges (GATv2) | Masked part prediction |
| IndustryForge-27B | 2607.28050 | 2026 | Domain-enhanced multimodal foundation model for industrial CAD | (abstract truncated) |
| Self-Improving CAD Agents | 2605.17448 | 2026 | FEA feedback for assembled multi-part STEP | Self-improvement via simulation |
| LMBuild | 2610.04292 | 2026 | Benchmark for buildable/functional assembled structures | Joints/materials/sequences |
| Nova3D | 2607.22738 | 2026 | Code-native generation; 59 joints across 12 assets | 98.3% geometric validity |
| CAD-Based Relation Learning | 2609.17263 | 2026 | Neural relation prediction from point clouds -> symbolic assembly graph | 85.83% planning success; >50x speedup |
| End-to-End Human Assembly Plans | 2610.09781 | 2026 | Physics-simulator disassembly + DfA cost + MLLM manuals | 35% reduction in simulated assembly time |
| Engineering as Code (ADL) | 2609.04216 | 2026 | ADL: PDL/PML/PLL sub-languages for parts, mating, layout | Declarative assembly mating |
| CIT-CAD | 2609.07434 | 2026 | Constraint Intent Tree guides code gen and verification | G-CSR constraint metric |
| Hierarchical Geometry-Aware Graphs | 2604.10075 | 2026 | Text -> structure/constraints -> action sequencing -> code | 12K dataset; ICLR 2026 |
| Material Prediction (GNN) | 2209.12793 | 2022 | Node-level material prediction over assembly graph (Fusion 360 Gallery) | GNN on assembly graph |
| Component Function Classification (GNN) | 2107.07042 | 2021 | Assembly-flow graphs + GNN for component function | Early assembly GNN |
| Automated Assembly Instruction Gen | 2610.11896 | 2026 | STEP assembly -> ProductGraph -> topological sort -> LLM steps | Withdrawal requested; human-in-the-loop |

### 3.6 AI Design Automation & Generative Design (52 rows)

| Title | arXiv ID | Year | Method | Key result |
|---|---|---|---|---|
| LLM Fine-Tuned for CAD (Sun et al.) | n/a (ASME J. Mech. Des. 2025) | 2025 | Fine-tuned GPT-3.5 on mechanical components with AMT descriptions | DOI 10.1115/1.4067713 |
| LLM4CAD (Li, Sun, Sha) | n/a (ASME JCISE 2025) | 2024/25 | Multimodal LLMs for text-to-CAD | NSF PAR 10661832 |
| CAD-Assistant | 2412.13810 | 2024/25 | Tool-augmented VLLM (see 3.1/3.3) | Generic CAD task solver |
| Generative AI for CAD Automation | 2508.00843 | 2025 | FreeCAD + LLM scripts (see 3.2) | Simple/moderate designs |
| Automated CAD Modeling Sequence Gen | 2505.19490 | 2025 | CAutoD (see 3.2) | Transformer-based sequence gen |
| Query2CAD | 2406.00144 | 2024 | Zero-shot LLM macros (see 3.1) | +23.1% after refinement |
| LLM Agent as Mechanical Designer | 2404.17525 | 2024 | LLM autonomously generates optimized truss structures with FEM feedback | Discrete/multi-faceted design spaces |
| Deep Generative Model for Mech. Config. | 2409.06016 | 2024/25 | GearFormer Transformer for gear-train configuration synthesis | Outperforms EA/MCTS; AAAI-25 |
| MDO Agent (Guo et al.) | 2511.17511 | 2025 | Natural-language parametric modeling + RAG + tool orchestration (FEA) | Gas-turbine blade, column, heat sink |
| Novel LLM-Assisted Mechanical Design | n/a (IEEE 11404166) | 2026 | Template-based parametric design in FreeCAD via LLM + KBE rules | FreeCAD API automation |
| Rosnitschek: GenAI Parametric Modeling | n/a (CAD journal 2026) | 2026 | Compact fine-tuned LLMs for bolted connections in FreeCAD | Computer-Aided Design 2026 |
| LLMs in Mechanical Design (Mechatronics) | n/a (Adv. Eng. Informatics 2026) | 2026 | PRISMA review of 58 studies (2020-2025) | AI in mechanical design |
| Fusion AI-AD System | n/a (Adv. Eng. Informatics 2025) | 2025 | LLMs-driven fusion AI-AD system for mechanical design | DOI 10.1016/j.aei.2025.103745 |
| Embodied CAD | 2606.31252 | 2026 | Solver-grounded LLM agents for parametric B-Rep assembly (see 3.5) | Assembly modeling |
| Deep Generative Design (Oh et al.) | 1903.01548 | 2019 | GAN + TO iterative framework for aesthetic + performant designs | J. Mech. Des. 141(11) |
| cGAN + Topology Optimization | n/a (JMD 2023) | 2023 | cGAN + TO one-step scheme | J. Mech. Des. 145(11) |
| Gen Design by RL | 2008.07119 | 2021 | RL maximizing diversity of topology designs | Autodesk GD reference |
| TopoGAN (Bernhard et al.) | n/a (AAG 2020) | 2020 | GAN trained on TO solutions; real-time 8 fps feedback | Conceptual structural design |
| Intelligent Generation of Innovative Structures | n/a (PMC8706216) | 2021 | BEGAN + TO; innovation/aesthetics/machinability/performance | PMC8706216 |
| Generative Design of Space Frames | n/a (IJAMT 2023) | 2023 | TO-based GD for aerospace bracket; AM-oriented | 14 solutions |
| AI-Based Design and TO (TUM) | n/a (mediatum 1833881) | 2025 | AI predicts TO geometry from boundary conditions | Stiffness-matrix training |
| GenAI-Driven TO Mass Reduction | n/a (ScienceDirect 2026) | 2026 | SIMP TO + ML post-optimization analysis | 70% mass reduction; 83.94% compliance reduction |
| One-Shot Optimal Topology Generation | 1807.10787 | 2018/19 | Theory-driven meta-learning generator for TO solutions | Kick-starts iterative solvers |
| NTopo (Zehnder et al.) | 2102.10782 | 2021 | MLP-parameterized density/displacement fields; self-supervised | Mesh-free TO with implicit neural reps |
| GenTO (Radler et al.) | 2502.13174 | 2025 | Data-free neural network with explicit diversity constraint | 2D/3D; solver-in-the-loop |
| MO-PaDGAN | 2009.07110 | 2020/21 | Performance-augmented GAN for multi-objective design | >180% hypervolume improvement (airfoil) |
| ParetoFlow | 2412.03718 | 2025 | Flow matching with multi-objective predictor guidance | ICLR 2025; non-convex fronts |
| Preference-Guided Diffusion (MOO) | n/a (NeurIPS 2025) | 2025 | Classifier-based preference guidance; diversity-aware | NeurIPS 2025 |
| Amortized Multi-Objective Optimization | 2511.09598 | 2025 | Parametric multi-objective Bayesian optimizer with conditional generative model | Amortized across tasks |
| Feature Space Exploration | 2301.11416 | 2023 | Compares parametric design space vs. DL feature space | Feature space captures complex relationships |
| Evaluating Designer Learning (IDGD) | n/a (JMD 2023) | 2023 | Human-subject study (N=42) on mechanical metamaterials with C-VAE | Designer learning & cognitive load |
| Agency in Human-AI Collaborative DSE | 2305.10451 | 2023 | Ship-hull generative design space exploration | Compares exploration approaches |
| MBSE-Based DSE (Timperley et al.) | n/a (IEEE 2023) | 2023 | SysML profile + GD + optimization for LEO satellite trade-offs | 38-96% exploration time reduction |
| Engineering Design Thinking Age of GenAI | n/a (NSF PAR 10545416) | 2024 | Compares parametric vs. generative design workflows | AI agent explores beyond human cognition |
| gem5 Co-Pilot | 2510.19577 | 2025 | LLM-driven DSE for computer architecture with DSDB/RAG | Architecture DSE |
| From Geometry to Function | n/a (Proc. Design Society 2026) | 2026 | Reorients generative CAD from geometry to function/manufacturability | Context-aware generative AI |
| GearFormer | 2409.06016 | 2024/25 | Gear-train configuration synthesis (see 3.6 above) | AAAI-25 |
| Jadhav & Farimani (LLM mech. designer) | 2404.17525 | 2024 | LLM autonomously generates optimized truss structures (see 3.6) | FEM feedback |
| Conversational AI-Powered Design | n/a (Electronics 2023) | 2023 | ChatGPT as designer/user/product | Filippi 2023 |
| Text-to-Image AI in Concept Generation | n/a (Proc. Design Soc. 2023) | 2023 | Li, Wang, Sha on text-to-image for concept generation | Concept generation |
| Impact of ChatGPT on Concept Generation | n/a (2023) | 2023 | Filippi on ChatGPT fostering concept generation | Human-subject study |
| ChatGPT for Microfluidic CAD | n/a (Lab Chip 2023) | 2023 | Nelson et al. ChatGPT assisting CAD for microfluidic devices | Lab Chip 23(17) |
| From Concept to Manufacturing (VLM) | 2311.12668 | 2023/24 | Vision-language models for engineering design | Concept-to-manufacturing eval |
| AI+OR Framework (Cagan et al.) | n/a (Res. Eng. Des. 1997) | 1997 | Foundational AI+OR integration framework | Cagan, Grossmann, Hooker |
| Mapping AI Methods to Design Stages | n/a (AI EDAM 2023) | 2023 | 108 papers; 7 AI methods x 5 design stages | Detailed design relies on ML/DL optimization |
| Opportunities/Challenges AI in Design | n/a (Proc. Design Society 2025) | 2025 | 7 design activities; 4-7 future directions | Manufacturing industry study |
| Special Issue AI Engineering Design | n/a (J. Mech. Des. 2022) | 2022 | Four themes; AI as tools vs design methods | Editorial |
| Review AI Applications Engineering Design | n/a (Eng. Appl. AI 2022) | 2022 | Categorizes AI-powered design studies by stage | Elsevier |
| LLM Survey for EDA | 2501.09655 | 2025 | 58+ papers 2022-2024 on LLMs for electronic design automation | EDA analog of DFM |
| GNN Survey for EDA | n/a (ACM TODAES 2023) | 2023 | Graph neural networks in EDA | ACM TODAES 28(2) |
| TO via ML/DL Review | 2210.10782 | 2022 | Reviews MLTO: supervised/unsupervised/RL acceleration | arXiv review |
| TO Aerospace Review | n/a (Struct. Multidiscip. Optim. 2025) | 2025 | Topology optimization methods and applications in aerospace | 68(5) |

### 3.7 AI for Manufacturing / DFM / CAE (27 rows)

| Title | arXiv ID | Year | Method | Key result |
|---|---|---|---|---|
| LLM-Aided DFM (Welbeck et al.) | 2609.05559 | 2026 | Multi-agent DFM Reviewer + CAD Modifier with compile+visual verification | 46-part benchmark |
| AgentsCAD | 2607.02448 | 2026 | Multi-agent LLM FDM DFAM with STEP parsing + overhang detection | GraphSAGE features (MFCAD++) |
| KAN Manufacturability Assessment | 2601.06334 | 2026 | KAN vs 14 ML/DL models on drilling/milling/combined | IEEE Access vol.14 |
| Physics-Informed GenAI (Semiconductor) | 2606.11247 | 2026 | Enforcing hard physical constraints in generative models | Perspective |
| Yield-Optimized Inverse-Designed EPICs | 2604.15493 | 2026 | DFM/yield-aware inverse design for photonic ICs | Accepted DAC 2026 |
| Knowledge-Guided AI Inverse Design | 2506.00056 | 2025 | Perspective: domain/physics/human-AI synergy; injection molding example | 34 pp. |
| AI for Better UX in CAE | 2507.16586 | 2025 | Multivocal literature review (academic vs industry) | CAE UX gap |
| Automotive Aerodynamics Benchmark | 2507.10747 | 2025 | DrivAerML dataset + DoMINO/X-MeshGraphNet/FIGConvNet | NVIDIA benchmark |
| DL in CAD/CAE (3D Wheel) | 2006.02138 | 2021 | Deep learning CAD/CAE generative design of conceptual wheel | Struct. Multidiscip. Optim. |
| CADCodeVerify | 2410.05340 | 2025 | VLM verification of CAD code (see 3.1) | CADPrompt benchmark |
| Speech to Reality | 2409.18390 | 2025 | Natural language -> 3D gen AI -> discrete robotic assembly | SCF 2025 |
| Industry 6.0 | 2409.10106 | 2024 | Generative AI + swarm of heterogeneous robots | Industry vision |
| Intelligent OPC Engineer Assistant | 2408.12775 | 2024 | RL-based OPC recipe search + multimodal agent | Semiconductor manufacturing |
| Human-AI Teaming for AM Info Extraction | 2407.18827 | 2024 | LLM-assisted scientific info extraction from AM research | IDETC-CIE 2024 |
| AI-Powered Hemodynamics Meshing | 2407.00535 | 2024 | Automated meshing 100x faster than existing | Aortic stenosis |
| Automated Process Planning (Semantic Capability) | 2312.08801 | 2024 | Semantic capability model + SMT solver | AAAI CAIPI Workshop |
| Automated Process Planning (Turning, Feature-Free) | 1905.09434 | 2019 | Configuration space + AI search for turning | J. Prod. Manuf. Res. |
| Situation Calculus for Manufacturing Controllers | 1807.04561 | 2018 | Situation calculus controller synthesis | cs.AI preprint |
| Towards Automated Process Planning and Mining | 2208.08943 | 2022 | PMAI Workshop @ IJCAI-ECAI | Process planning/mining |
| LLMs for EDA | 2508.20030 | 2025 | Comprehensive LLM integration into EDA workflows | IEEE SoCC |
| NSF AI-for-EDA Workshop Report | 2601.14541 | 2026 | AI for physical synthesis and DFM theme | IEEE Circuits and Systems Magazine |
| X-DFS | 2411.07308 | 2024 | Explainable AI guided design-for-security exploration | cs.CR/cs.AI |
| AI for Materials Science Survey | 2506.20743 | 2025 | Foundation models, LLM agents, datasets, tools (incl. planning) | cs.LG/cs.CE |
| Neuro-Symbolic AI for PdM | 2602.00731 | 2026 | Neuro-symbolic predictive maintenance review | cs.AI/cs.LO |
| Survey Diffusion Models for Anomaly Detection | 2501.11430 | 2025 | Diffusion models for manufacturing anomaly detection | cs.LG/cs.AI |
| Ontologies + Knowledge-Augmented LLMs (Industry) | 2505.18553 | 2025 | Ontologies + LLMs for industrial automation | Industry 5.0 |
| Generative Retrieval-Augmented Ontologic Graph | 2310.19998 | 2023 | Multi-agent strategies for LLM-based materials design | cs.CL |

### 3.8 Benchmarks & Datasets (36 rows)

| Title | arXiv ID | Year | Method | Key result |
|---|---|---|---|---|
| CADBench | 2605.10873 | 2026 | Unified multimodal: 18,000 samples, 6 families, 5 modalities, 6 metrics | 11 VLMs; >1.4M programs |
| BenchCAD | 2605.10865 | 2026 | 17,900 verified CadQuery programs; 106 industrial families | VQA, code QA, image-to-code, edit |
| RealCADBench | 2609.03773 | 2026 | 12,632 industrial intent tasks; FreeCAD Python | 1,770-task eval slice |
| MUSE | 2605.28579 | 2026 | B-Rep assembly benchmark with design-intent rubrics | Code/geometric/design-intent stages |
| Text2CAD-Bench | 2605.18430 | 2026 | 600 human-curated examples, 4 levels | Dual-style prompts |
| CADENA-Bench | 2608.00799 | 2026 | Reverse-engineering benchmark on mechanical parts | HuggingFace dataset |
| ComCADBench | 2606.13239 | 2026 | Agents in real industrial CAD software via COM | Frontier models near-zero GUI |
| GERD / GERD-EVL | 2609.22688 | 2026 | Aligned commands, geometry states, IDs at every step | Vision2CAD evaluation |
| OpenRealCAD | 2608.30617 | 2026 | Four-view photos of 392 3D-printed objects + command sequences | Real-domain image-to-CAD |
| DeepCAD-240 | 2603.21978 | 2026 | Sequence length 40 -> 240 commands | ABC-derived; longer histories |
| Text2CAD dataset | 2409.17106 | 2024 | ~170K models / ~660K text annotations | Beginner-to-expert prompts |
| BlenderLLM / CADBench (Blender) | 2412.14203 | 2024 | Evaluation suite for LLM CAD scripts in Blender | Functionality, accuracy |
| BIM-Edit | 2606.20146 | 2026 | 324 editing tasks, 11 building models + 36 scenes | IFC-based BIM editing |
| CADTestBench | 2605.07807 | 2026 | Test-based evaluation over B-rep | 5,937 tests / 200 programs |
| CADWorld | 2609.16251 | 2026 | 200 tasks / 11 mechanical-CAD workflow categories | FreeCAD GUI; 17.5% vs 87% expert |
| EngiWorld | 2609.37686 | 2026 | 1,301 tasks across 6 domains and 26 apps | 44.7/100 best |
| LMBuild | 2610.04292 | 2026 | Buildable/functional assembled structures | LLM agents retrieve/create/place |
| OmniMech | 2608.05539 | 2026 | Million-scale multimodal mechanical benchmark | Tool-augmented agentic task |
| neuralCAD-Edit | 2604.16170 | 2026 | Expert multimodal editing benchmark | 192 requests + 384 edits; 10 designers |
| HistCAD | 2602.19171 | 2026 | Constraint-preserving dimensional edit benchmark | 170K/180K histories |
| CADEngBench | 2608.09296 | 2026 | 600 tasks + 150 body pairs; FEA (CalculiX) | 12 edit types; joint retrieval |
| CADPrompt | 2410.05340 | 2025 | 200 NL prompts + expert CAD code | From CADCodeVerify |
| CAD-Judge | 2508.04002 | 2025 | Compiler-as-a-Judge + Compiler-as-a-Review framework | Efficient verification/refinement |
| 3DVerifierBench | 2610.22360 | 2026 | Verification of 3D content (decisions, explanations) | 10 tasks; 14,126 training examples |
| DeepCAD (dataset) | n/a (2409.17106) | 2021 | Procedural sketch-and-extrude sequences from ABC | ~170K-1M models |
| Fusion 360 Gallery | n/a (multiple) | - | Human-designed parametric CAD | Autodesk dataset |
| ABC (dataset) | n/a (multiple) | - | Large-scale B-rep | Analytic B-reps |
| CC3D (dataset) | n/a (2412.14042) | - | Real scanned 3D shapes | Used by CAD-Recode |
| MCB (dataset) | n/a (multiple) | - | Mechanical components | Mechanical parts |
| Objaverse (dataset) | n/a (2605.10873) | - | General 3D objects | CADBench family |
| CADEvolve (dataset) | 2602.16317 | 2026 | 8K complex parts -> 1.3M CadQuery scripts | Complex part generation |
| STEP-caption (dataset) | 2601.12641 | 2026 | ~40K STEP-caption pairs | Text-to-STEP training |
| CADENA (dataset) | 2608.00799 | 2026 | Mechanical reverse-engineering dataset | HuggingFace |
| RealCAD (dataset) | n/a (ModelScope) | - | Real industrial CAD intents | ModelScope: yeguomao/RealCAD |
| BlendNet (dataset) | 2412.14203 | 2024 | Blender CAD script training data | BlenderLLM |
| T-LESS / MP6D | n/a (2610.11954) | - | Industrial metal-parts benchmarks | Used by SightCAD |

### 3.9 Surveys & Overviews (32 rows)

| Title | arXiv ID | Year | Method | Key result |
|---|---|---|---|---|
| LLMs for CAD: A Survey | 2505.08137 | 2025/26 | First systematic LLM+CAD survey; 6 application areas | ACM CSUR 58(9) |
| Geometric Deep Learning for CAD: A Survey | 2402.17695 | 2024/25 | Similarity/retrieval, 2D/3D synthesis, point cloud/image CAD | 28 pages; datasets/codes |
| AI-Driven 3D CAD Generation: A Survey | n/a (CVM 2026) | 2025/26 | ML->LLM 3D CAD generation across representations/conditions | DOI 10.26599/CVM.2025.9450521 |
| LLMs in Mechanics/Product Design/Manufacturing | n/a (AEI 2024) | 2024 | Survey of LLM applications in mechanics/design/manufacturing | 88 citations |
| MLLMs in Parametric CAD | n/a (ESWA 2025) | 2025 | Status/evolution/challenges of MLLMs in parametric CAD | 132 references |
| Challenges/Opportunities GenAI + CAD | n/a (ICED25) | 2025 | Barriers: small datasets, mixed types, proprietary formats | Proc. Design Society |
| LLMs for Design and Manufacturing | n/a (MIT 2024) | 2024 | MIT tech report; design gen, DfM, inverse design | DOI 10.21428/e4baedd9.745b62fa |
| Data-Driven Intelligent CAD Review | n/a (JCAD 2025) | 2025 | Chinese review: datasets, representation, forward/reverse eng, LLM | DOI 10.3724/SP.J.1089.2025-00241 |
| Generative AI for 3D CAD in Engineering | n/a (IEEE CG&A 2026) | 2026 | Design process, design theory, human cognition | DOI 10.1109/mcg.2026.3665334 |
| AI in Generative Design: Structured Review | n/a (MDPI Designs 2025) | 2025 | 88 of 14,355 publications; GANs, surrogates, structural/aero | DOI 10.3390/designs9040079 |
| AI for Engineering-Grade Parametric CAD: Critical Review | n/a (MDPI Machines 2026) | 2026 | EG-CAD 7-criteria framework; 107 sources | DOI 10.3390/machines14101206 |
| Intelligent CAD 2.0 | 2410.03759 | 2024 | Vision paper: ICAD 1.0 vs 2.0; intensional vs extensional | J. Visual Informatics |
| GenAI + LLMs for CAD Assembly Design and MFR | n/a (CANA 2025) | 2025 | LLMs for assembly + MFR/CAPP | DOI 10.52783/cana.v32.7270 |
| GenAI meets CAD (engineering design to manufacturing) | n/a (IJAMT 2025) | 2025 | GPT-4o text/image/voice -> CAD code with closed feedback loop | DOI 10.1007/s00170-025-15830-2 |
| Quality of CAD Generation with LLMs: Critical Overview | n/a (DFX 2026) | 2026 | 6-level maturity model (VDI 2209); most at level 3 | DOI 10.35199/dfx2026.8 |
| Enhancing CAD with Deep Learning Frameworks | n/a (ICED25?) | 2025 | Literature review of DL frameworks for CAD | DOI 10.1017/pds.2025.10165 (verify) |
| LLMs for Manufacturing | 2410.21418 | 2024 | Broader manufacturing LLM survey; engineering design/CAD subsection | arXiv HTML |
| Mapping AI Methods to Engineering Design Stages | n/a (AI EDAM 2023) | 2023 | 108 papers; 7 AI methods x 5 design stages | NSF PAR 10394336? |
| Opportunities/Challenges AI in Design | n/a (Proc. Design Society 2025) | 2025 | 7 design activities; 4-7 future directions | Manufacturing industry study |
| Special Issue: AI and Engineering Design | n/a (J. Mech. Des. 2022) | 2022 | Four themes; AI as tools vs design methods | NSF PAR 10470485 |
| Review of AI Applications in Engineering Design | n/a (Eng. Appl. AI 2022) | 2022 | Categorizes AI-powered design studies by stage | ScienceDirect |
| LLM Survey for EDA | 2501.09655 | 2025 | 58+ papers 2022-2024 on LLMs for EDA | arXiv PDF |
| GNN Survey for EDA | n/a (ACM TODAES 2023) | 2023 | Graph neural networks in EDA | ACM TODAES 28(2) |
| TO via ML/DL Review | 2210.10782 | 2022 | Reviews MLTO: supervised/unsupervised/RL acceleration | arXiv PDF |
| TO Aerospace Review | n/a (Struct. Multidiscip. Optim. 2025) | 2025 | Topology optimization methods and applications in aerospace | 68(5) |
| AI Methods for Geometry Prep and Mesh Gen | 2512.23719 | 2025 | Survey of AI in CAD-to-mesh pipeline | arXiv |
| Converting Unstructured Data to CSG Models | 2305.01220 | 2023 | CSG recovery methods, segmentation, fitting | arXiv |
| AI+CAD Data Representation Architecture | 2606.16797 | 2026 | Position paper: DeepCAD vs industrial parametric feature modeling (WHUCAD) | arXiv |
| AI for Materials Science Survey | 2506.20743 | 2025 | Foundation models, LLM agents, datasets, tools (incl. planning) | arXiv |
| AI for Better UX in CAE | 2507.16586 | 2025 | Multivocal review mapping academic vs industry | arXiv |
| NSF AI-for-EDA Workshop Report | 2601.14541 | 2026 | AI for physical synthesis and DFM theme | IEEE Circuits and Systems Magazine |
| LLMs for EDA (Xu et al.) | 2508.20030 | 2025 | Comprehensive LLM integration into EDA workflows | IEEE SoCC |

## 4. Key trends (2024-2026)

- Shift from transformer seq2seq over DeepCAD command tokens (2024) to LLM code generation (CadQuery/STEP/NURBS) in 2025-2026, leveraging pretrained code priors.
- CadQuery is the dominant intermediate representation; STEP and NURBS emerge for manufacturing fidelity.
- Agentic, tool-mediated, iterative loops (generate-execute-critique-repair) replace single-shot generation; multi-agent teams mirror engineering orgs.
- Benchmarks proliferate: from single-part geometric similarity (IoU/CD) to editability, preservation, assembly, manufacturability, and design-intent rubrics (CADTests, MUSE, CADEngBench, RealCADBench).
- Evaluation moves from geometric similarity toward validity (execution) as a hard gate, then intent/preservation; VLM-as-judge and compiler-as-judge become standard.
- Knowledge enters via ontologies/knowledge graphs, RAG, workflow memory, and navigable skill structures (Corpus2Skill), not just passive chunks.
- Connector/port/mate-first designs fix joint semantics before geometry in assembly generation.
- DFM work splits into LLM multi-agent CAD redesign loops and parametric-feature ML classifiers; CAE AI concentrates on surrogates and automated meshing.

## 5. Open challenges

- No standardized, widely-adopted benchmark or evaluation protocol; heterogeneous metric suites hinder comparison.
- Geometric similarity (CD/IoU) is insufficient; test-based and intent-based evaluation is still emerging and not universal.
- Long-horizon, multi-part assembly automation and assembly editing remain largely unsolved (RealCADBench reports "incorrect assembly placement" as recurring failure).
- Simulation-in-the-loop (FEA/CFD) is rarely integrated into agent loops; most verify geometry only.
- Text-aligned CAD data is mostly auto-annotated (LLM/VLM), creating dependency on annotation quality; human-verified subsets are small.
- Fusion 360 Gallery and ABC are not natively text-annotated; synthesized labels may bias language coverage.
- Direct head-to-head benchmarks of AI DFM vs. incumbent tools (aPriori, DFMPro, Fusion 360, Siemens NX) are scarce.
- No comprehensive survey spanning mechanical CAD + generative design + topology optimization + MDO + DSE together.
- AgentCAD and "CADAssembly" named benchmarks could not be located; names may be conflated.
- Siemens affiliation of the AEI paper and some 2026 preprint details are not confirmed from abstracts.

## 6. Quick lookup

By arXiv ID (selected high-impact entries):

- 2409.17106 Text2CAD (foundational text-to-parametric) - 3.1
- 2406.00144 Query2CAD (zero-shot LLM macros) - 3.1 / 3.6
- 2505.19713 CAD-Coder (SFT+GRPO) - 3.1
- 2603.26512 CADSmith (multi-agent CadQuery) - 3.1
- 2601.12641 STEP-LLM (direct STEP/B-rep) - 3.1
- 2511.06194 NURBGen (LLM -> NURBS) - 3.1
- 2605.28579 MUSE (assembly intent rubrics) - 3.1 / 3.5 / 3.8
- 2412.13810 CAD-Assistant (tool-augmented VLLM) - 3.1 / 3.3 / 3.6
- 2502.03997 CAD-Editor (locate-then-infill) - 3.4
- 2508.10201 B-repLer (B-rep latent editing) - 3.4
- 2608.03062 TraceCAD (localized repair + preservation) - 3.4
- 2604.16170 neuralCAD-Edit (expert editing benchmark) - 3.4 / 3.8
- 2604.10992 ArtiCAD (connector-first assembly) - 3.5
- 2607.05123 AssemCAD (port/mate-first) - 3.5
- 2609.03773 RealCADBench (industrial intents) - 3.3 / 3.4 / 3.5 / 3.8
- 2609.16251 CADWorld (GUI computer-use) - 3.3 / 3.5 / 3.8
- 2511.03179 Knowledge-Guided Multi-Agent (Karniadakis) - 3.3
- 2604.07784 Agentic Engineering Intelligence (AEI) - 3.3
- 2604.14572 Corpus2Skill (knowledge compilation) - 3.3
- 2604.24479 Zero-to-CAD (agentic synthesis) - 3.2 / 3.3
- 2609.05559 DFM-Redesign (multi-agent DFM) - 3.3 / 3.5 / 3.7
- 2505.08137 LLMs for CAD: A Survey - 3.9
- 2402.17695 Geometric Deep Learning for CAD: A Survey - 3.9
- 2605.10873 CADBench - 3.2 / 3.8
- 2605.10865 BenchCAD - 3.2 / 3.8

By topic:

- Text-to-CAD generation: 3.1
- Code generation (CadQuery/FreeCAD/build123d): 3.2
- Agents and knowledge-guided systems: 3.3
- Editing existing CAD models: 3.4
- Assemblies and multi-part design: 3.5
- Design automation, generative design, optimization: 3.6
- Manufacturing, DFM, CAE, process planning: 3.7
- Benchmarks and datasets: 3.8
- Surveys and overviews: 3.9

## 7. References to research notes

All content derived from these 9 notes (do not modify them):

- `research_notes/AI and CAD research papers catalog/text_to_cad.md`
- `research_notes/AI and CAD research papers catalog/text_to_code_cad.md`
- `research_notes/AI and CAD research papers catalog/ai_design_automation.md`
- `research_notes/AI and CAD research papers catalog/agentic_knowledge_guided_cad.md`
- `research_notes/AI and CAD research papers catalog/cad_editing_manipulation.md`
- `research_notes/AI and CAD research papers catalog/assembly_cad_ai.md`
- `research_notes/AI and CAD research papers catalog/ai_manufacturing_dfm_cae.md`
- `research_notes/AI and CAD research papers catalog/cad_benchmarks_evaluation.md`
- `research_notes/AI and CAD research papers catalog/cad_llm_surveys.md`

## Appendix A: Low-confidence or unverified items deliberately omitted

The following items appear in the research notes but could not be verified (no stable arXiv ID or conflicting details). They are excluded from the tables above; consult the notes before citing.

- CAD-Translator (Li et al.) - cited in CAD-Judge/CADFusion as encoder-decoder text->CAD sequences; arXiv ID not located (low confidence).
- UniCAD - unified benchmark/model for multi-modal multi-task CAD; specific arXiv ID not verified.
- AgentCAD - no arXiv paper found under that exact name; may be a project/tool.
- "CADAssembly" benchmark - not found as a standalone arXiv benchmark; may be an internal dataset name.
- "CAD-Edit" standalone benchmark - not found distinct from CAD-Editor/neuralCAD-Edit.
- CADFusion full arXiv provenance - partially verified.
- Siemens NX peer-reviewed AI-CAD studies - not found; flagged unverified.
- Some ASME paper DOIs approximated from page numbers; verify before citation.
- IndustryForge-27B abstract truncated in listing; details incomplete.
- AgentCAD, CADAssembly, CAD-Edit may be conflated names in prompts; flagged.

## Appendix B: Additional cross-cutting papers captured in the notes

These entries are referenced in the research notes but are secondary to the category tables above (method/evaluation/motion papers). IDs are as recorded in the notes.

| Title | arXiv ID | Year | Note |
|---|---|---|---|
| CADFather | 2610.09127 | 2026 | Evaluates on CADBench/BenchCAD/DeepCAD/Fusion360/MCB |
| SightCAD | 2610.11954 | 2026 | Real-image CAD code generation; VLM-generated code scoring |
| cadrille | 2505.22914 | 2025 | GRPO-based CAD generation |
| PrimitiveCAD | 2610.08698 | 2026 | Primitive-aware CAD generation |
| CADFit | 2605.01171 | 2026 | Volumetric IoU + Chamfer Distance |
| TransCAD | 2407.12702 | 2024 | mAP of CAD sequence metric proposal |
| PS-CAD | 2405.15188 | 2024 | ECD structural error metric |
| TG-Diff | 2607.21928 | 2026 | B-rep generation on DeepCAD/ABC (COV/MMD/JSD) |
| UniBRep | 2610.04092 | 2026 | Valid B-reps 80.49%; face CD reduction |
| CADReasoner | 2603.29847 | 2026 | CAD generation reasoning |
| GACO-CAD | 2510.17157 | 2026 | Agentic CAD generation |
| CAD-Coder VLM (Doris et al.) | 2505.14646 | 2025 | LLaVA-based CAD code VLM (also 3.2) |
| CAD-Recode | 2412.14042 | 2024/25 | Point cloud -> code (also 3.1/3.2) |
| Zero-to-CAD | 2604.24479 | 2026 | Agentic synthesis (also 3.2/3.3) |
| ReliCAD | 2609.22325 | 2026 | Repair for editing (also 3.3/3.4) |
| AgenticCADedit | 2609.29621 | 2026 | Stateful editing (also 3.3/3.4) |
| CADWorld | 2609.16251 | 2026 | GUI computer-use benchmark (also 3.3/3.5/3.8) |
| RealCADBench | 2609.03773 | 2026 | Industrial intents (also multiple) |
| MUSE | 2605.28579 | 2026 | Assembly intent benchmark (also multiple) |
| ConCAD | 2609.34494 | 2026 | GRPO constraint+IoU rewards; G-CSR metric |
| ConCAD (metric) | 2609.34494 | 2026 | G-CSR design-intent metric |
| FutureCAD | 2603.11831 | 2026 | CadQuery + BRepGround (also 3.2) |
| Seek-CAD | 2505.17702 | 2025/26 | Local DeepSeek-R1 generation (also 3.2) |
| CADMorph | 2512.11480 | 2026 | Shape-matching editing (also 3.2/3.4) |
| CAD-Assistant | 2412.13810 | 2024/25 | Tool-augmented VLLM (also 3.1/3.3/3.6) |

## Appendix C: How this catalog was built

- Source: the 9 research notes listed in section 7 (AI and CAD research papers catalog).
- Extraction: major papers, methods, and key results were taken from the "Cited Findings" and "Takeaway" blocks of each note.
- De-duplication: papers spanning multiple tasks (e.g., MUSE, RealCADBench, CAD-Assistant) appear in multiple category tables; counts in section 7 are row counts, not unique papers.
- Verification level: abstract-level only. Full-text verification was not performed; items flagged "unverified" or "low confidence" in the notes are listed in Appendix A rather than in the main tables.
- ArXiv ID format: 4-digit year prefix + 4-5 digit number (e.g., 2409.17106). Non-arXiv items show a DOI, journal, or "n/a" placeholder.
- Scope limits: general text-to-3D (mesh/SDF/voxel) work is mostly out of scope; CAD research here favors B-rep/parametric outputs. Electronic design automation (EDA) papers are included only where they inform mechanical DFM/CAE.
- Maintenance: when a new research note is added, append its papers to the relevant category table and update the counts in section 7 and Appendix A/B.

## Appendix D: Frequently used acronyms

- B-rep: boundary representation (solid geometry).
- CD: Chamfer Distance (geometric similarity metric).
- DFM: Design for Manufacturing.
- DSE: Design Space Exploration.
- EDA: Electronic Design Automation.
- FEA: Finite Element Analysis.
- G-CSR: B-rep Geometric Constraint Satisfaction Rate.
- IoU: Intersection over Union.
- KAN: Kolmogorov-Arnold Network.
- MDO: Multidisciplinary Design Optimization.
- MLLM: Multimodal Large Language Model.
- MOO: Multi-Objective Optimization.
- NURBS: Non-Uniform Rational B-Spline.
- RL: Reinforcement Learning.
- SFT: Supervised Fine-Tuning.
- STEP: Standard for the Exchange of Product model data.
- TO: Topology Optimization.
- VLLM: Vision-Language Large Model.
- VLM: Vision-Language Model.

Paper count summary (rows in category tables above):

- Text-to-CAD: 25
- Text-to-Code-to-CAD: 18
- Agentic / Knowledge-Guided CAD: 26
- CAD Editing & Manipulation: 18
- Assembly & Multi-Part CAD: 22
- AI Design Automation & Generative Design: 52
- AI for Manufacturing / DFM / CAE: 27
- Benchmarks & Datasets: 36
- Surveys & Overviews: 32

Total rows: 256 (papers appear in multiple categories; unique arXiv IDs across tables: 144).

---

End of catalog.
