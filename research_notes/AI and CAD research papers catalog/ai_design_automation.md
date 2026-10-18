# AI-Assisted Design Automation, Generative Design, and Design Optimization — Research Paper Catalog

## Scope and Method
This catalog compiles research papers (2018–2026) on AI-assisted mechanical/CAD design automation, generative design, topology optimization, design space exploration, and multi-objective optimization. Sources: arXiv, ASME (J. Mech. Des., J. Comput. Inf. Sci. Eng.), IEEE, ACM, Springer, Elsevier, Nature, ScienceDirect, Cambridge (Proc. Design Society), MDPI, and vendor research notes (Autodesk, nTop). Items flagged **[unverified]** where only snippets/abstracts were available or details could not be confirmed. URLs are provided for traceability.

---

## 1. Major Papers on AI-Assisted Mechanical/CAD Design Automation (2023–2026)

### Takeaway
The 2023–2026 wave is dominated by LLM/VLLM-driven CAD automation (text-to-CAD, tool-augmented agents, fine-tuned models) plus agent-based multidisciplinary design optimization (MDO) pipelines that orchestrate parametric CAD + FEA.

### Cited Findings
- **Sun, Li, Sha (2025)**, "Large Language Models for Computer-Aided Design Fine Tuned: Dataset and Experiments," *ASME J. Mech. Des.* 147(4): 041710, DOI 10.1115/1.4067713. Fine-tuned GPT-3.5 on a mechanical-component CAD dataset (gears, shafts, springs) with natural-language descriptions collected via AMT; CAD programs as bridge to 3D designs. — [ASME](https://asmedigitalcollection.asme.org/mechanicaldesign/article/147/4/041710/1212251/Large-Language-Models-for-Computer-Aided-Design)
- **Li, Sun, Sha (2024)**, "LLM4CAD: Multi-modal Large Language Models for 3D Computer-Aided Design Generation," *ASME J. Comput. Inf. Sci. Eng.* 25(2): 021005. Multimodal LLMs for text-to-CAD. — [cited in Sun et al.]
- **CAD-Assistant (2024/2025)**, "CAD-Assistant: Tool-Augmented VLLMs as Generic CAD Task Solvers," arXiv:2412.13810. VLLM planner + CAD-specific tools executed in FreeCAD Python API; handles 3D reverse engineering, CAD QA, text-guided editing. — [arXiv](https://arxiv.org/pdf/2412.13810v2)
- **Kumar, Kapoor, Vardhan, Zhao (2025)**, "Generative AI for CAD Automation: Leveraging Large Language Models for 3D Modelling," arXiv:2508.00843. FreeCAD + LLM scripts with iterative error-feedback refinement; good for simple/moderate designs, struggles with highly constrained models. — [arXiv](https://arxiv.org/abs/2508.00843)
- **Automated CAD Modeling Sequence Generation (2025)**, "Automated CAD Modeling Sequence Generation from Text Descriptions via Transformer-Based Large Language Models," arXiv:2505.19490 (CAutoD framework: TCADGen Transformer + CADLLM). — [arXiv](https://arxiv.org/pdf/2505.19490)
- **Query2CAD (Badagabettu et al., 2024)**, "Query2cad: Generating cad models using natural language queries," arXiv:2406.00144. — [cited in Kumar et al.]
- **Jadhav & Farimani (2024)**, "Large language model agent as a mechanical designer," arXiv:2404.17525. LLM autonomously generates optimized truss structures with FEM feedback; explores discrete/multi-faceted design spaces. — [arXiv](https://arxiv.org/pdf/2404.17525)
- **Etesam, Cheong, Ataei, Jayaraman (2024/2025)**, "Deep Generative Model for Mechanical System Configuration Design," arXiv:2409.06016, accepted AAAI-25. GearFormer Transformer for gear-train configuration synthesis; outperforms EA/MCTS; hybrid methods further improve. — [arXiv](https://arxiv.org/abs/2409.06016v3)
- **MDO Agent (Guo et al., 2025)**, "A Multidisciplinary Design and Optimization (MDO) Agent Driven by Large Language Models," arXiv:2511.17511. Natural-language parametric modeling + RAG + tool orchestration (FEA); validated on gas-turbine blade, machine-tool column, fractal heat sink. — [arXiv](https://arxiv.org/abs/2511.17511v1)
- **Kim et al. (2026)**, "A Novel LLM-Assisted Approach for Automated Mechanical Design," IEEE (PDF 11404166). Template-based parametric design automation in FreeCAD via LLM + CAD APIs (KBE rules). — [IEEE](https://ieeexplore.ieee.org/iel8/6287639/11323511/11404166.pdf)
- **Rosnitschek (2026)**, "From dialogue to design: GenAI-Based automation of parametric modeling and sizing tasks in CAD workflows," *Computer-Aided Design* (ACM/Elsevier). Compact fine-tuned LLMs for bolted connections in FreeCAD. — [ACM](https://dl.acm.org/doi/10.1016/j.cad.2026.104065)
- **LLMs in mechanical design of mechatronic systems (2026)**, *Advanced Engineering Informatics* 104807. PRISMA review of 58 studies (2020–2025). — [ACM](https://dl.acm.org/doi/10.1016/j.aei.2026.104807)
- **Fusion AI-AD system (2025)**, "LLMs driven fusion AI-AD system for mechanical design," *Advanced Engineering Informatics* 103745. — [ACM](https://dl.acm.org/doi/10.1016/j.aei.2025.103745)
- **Embodied CAD (2026)**, "Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling," arXiv:2606.31252. LLM agents with exact geometric kernel feedback for parametric B-Rep assembly. — [arXiv](https://arxiv.org/abs/2606.31252)
- **Nelson, Goenner, Gale (2023)**, "Utilizing Chatgpt to Assist CAD Design for Microfluidic Devices," *Lab Chip* 23(17): 3778–3784. — [cited in Sun et al.]

### Inferences
- LLM-based CAD automation has moved from research prototypes to agent architectures with tool use and solver feedback (CAD-Assistant, MDO Agent, Embodied CAD), reflecting the "kernel is the referee" invariant.
- FreeCAD is the dominant open-source CAD target for LLM automation studies.

### Gaps
- No independent replication/benchmark of most LLM-CAD frameworks; evaluation is author-reported on small task sets.
- Long-horizon, multi-part assembly automation remains largely unsolved (Embodied CAD is recent).

---

## 2. Surveys on AI in Engineering Design / CAD

### Takeaway
Multiple surveys now cover LLMs-for-CAD (Zhang et al. 2025/2026) and AI-method-to-design-stage mapping (Cambridge 2023), plus an EDA-focused LLM survey; a 2025 manufacturing-industry study catalogs AI design activities.

### Cited Findings
- **Zhang et al. (2025/2026)**, "Large Language Models for Computer-Aided Design: A Survey," arXiv:2505.08137, *ACM Comput. Surv.* 58(9), DOI 10.1145/3787499. First systematic survey of LLM–CAD intersection; taxonomy of tasks (parametric generation, coding, image synthesis, evaluation). — [arXiv](https://arxiv.org/pdf/2505.08137) · [ACM](https://dl.acm.org/doi/abs/10.1145/3787499)
- **Mapping AI-based methods to engineering design stages (2023)**, focused literature review of 108 papers (ASME/AI EDAM/IDETC), *AI EDAM*. Maps 7 AI methods (agent-based, DL, ML, NLP, network theory, probabilistic, optimization) to 5 design stages; notes detailed-design stage relies on ML/DL optimization. — [Cambridge PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/706442DFC0F1213F01997072DFD71A3C/S0890060423000203a.pdf/...)
- **Opportunities and challenges of AI in design (2025)**, Proc. Design Society. Reviews 2023–24 AI-in-design papers; 7 design activities (Planning, Customising, Defining, Discovering, Generating, Maintaining, Validating); 4–7 future research directions. — [Cambridge](https://www.cambridge.org/core/journals/proceedings-of-the-design-society/article/opportunities-and-challenges-of-ai-in-design-a-practical-study-from-the-manufacturing-industry/446D1D00C36A7D15635DD9E38B09A6B0)
- **Special Issue: Artificial Intelligence and Engineering Design (2022)**, *J. Mech. Des.* editorial. Four themes; AI methods as tools vs. design methods. — [NSF PAR](https://par.nsf.gov/servlets/purl/10470485)
- **Review of AI applications in engineering design (2022)**, *Eng. Appl. Artif. Intell.* (Elsevier). Categorizes AI-powered design studies by stage: inspiration, idea/concept generation, evaluation, optimization, decision-making, modelling. — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S095219762200687X)
- **LLM survey for EDA (2025)**, "A Survey of Research in Large Language Models for Electronic Design Automation," arXiv:2501.09655 (2022–2024, 58+ papers). — [arXiv](https://arxiv.org/pdf/2501.09655)
- **GNN survey for EDA (2023)**, "A Comprehensive Survey on Electronic Design Automation and Graph Neural Networks," *ACM TODAES* 28(2):15. — [ACM](https://dl.acm.org/doi/10.1145/3543853)
- **Topology Optimization via ML/DL: A Review (2022)**, arXiv:2210.10782. Reviews MLTO: supervised/unsupervised/RL for acceleration, non-iterative optimization, metamodeling, dimensionality reduction, generative design, postprocessing. — [arXiv](https://arxiv.org/pdf/2210.10782v1)
- **Topology optimization methods and applications in aerospace: a review (2025)**, *Struct. Multidiscip. Optim.* 68(5). — [ACM](https://dl.acm.org/doi/10.1007/s00158-025-04030-x)

### Inferences
- LLM-for-CAD is the fastest-growing subfield (2024–2026); surveys are now annual.
- Mechanical-design AI surveys lag behind EDA surveys in maturity.

### Gaps
- No single comprehensive survey spanning mechanical CAD + generative design + TO + MDO + DSE together; this catalog is a partial patch.

---

## 3. Generative Design

### Takeaway
Generative design = AI-driven exploration of a design space against objectives/constraints; distinct from topology optimization (which yields a single mesh). Autodesk Fusion and nTop are the dominant commercial platforms; research spans RL/diversity, cGAN+TO, and human-in-the-loop DSE.

### Cited Findings
- **Deep Generative Design (Oh et al., 2019)**, "Deep Generative Design: Integration of Topology Optimization and Generative Models," arXiv:1903.01548, *J. Mech. Des.* 141(11): 111405, DOI 10.1115/1.4044229. GAN + TO iterative framework for aesthetic + performant 2D wheel designs; anomaly detection for novelty. — [arXiv](https://arxiv.org/abs/1903.01548)
- **Generative Design by embedding TO into cGAN (2023)**, *J. Mech. Des.* 145(11): 111702, DOI 10.1115/1.4062691 (approx). cGAN + TO one-step scheme; tests loss terms and TO params. — [ASME](https://asmedigitalcollection.asme.org/mechanicaldesign/article/145/11/111702/1164479/Generative-Design-by-Embedding-Topology)
- **Generative Design by Reinforcement Learning (2021)**, arXiv:2008.07119. RL-based GD maximizing diversity of topology designs; references Autodesk Generative Design (level-set TO, cloud). — [arXiv](https://arxiv.org/pdf/2008.07119)
- **Generative Design Exploration by Integrating Deep Generative Models and Topology Optimization** (same as Oh et al. above).
- **TopoGAN (Bernhard et al., ETH Zurich)**, "Topology Optimization with Generative Adversarial Networks." GAN trained on TO solutions; real-time 8 fps feedback for conceptual structural design. — [PDF](https://psl.design.upenn.edu/wp-content/uploads/2023/01/AAG2020_11_Bernhard.pdf)
- **Intelligent Generation of Innovative Structures (2021)**, PMC8706216. BEGAN + TO; evaluation on innovation, aesthetics, machinability, mechanical performance. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8706216)
- **Generative design of space frames for additive manufacturing (2023)**, *Int. J. Adv. Manuf. Technol.* DOI 10.1007/s00170-023-11691-9. TO-based GD for aerospace bracket; 14 solutions; AM-oriented. — [Springer](https://link.springer.com/article/10.1007/s00170-023-11691-9)
- **AI-based design and TO of a coupled system (2025)**, TUM mediatum 1833881. AI predicts TO geometry from boundary conditions; stiffness-matrix training. — [TUM](https://mediatum.ub.tum.de/doc/1833881/1833881.pdf)
- **Generative AI–driven topology optimization for mass reduction in aerospace drones (2026)**, ScienceDirect 259012302600784X. SIMP TO + ML post-optimization analysis; 70% mass reduction, 83.94% compliance reduction. — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S259012302600784X)
- **Generative AI-driven design optimization: eight key application scenarios (2025)**, *JMST Advances* DOI 10.1007/s42791-025-00097-1. Conceptual framework: 3D/2D/1D prediction/generation/optimization scenarios. — [Springer](https://link.springer.com/article/10.1007/s42791-025-00097-1)
- **Autodesk generative design (platform)**, Fusion generative design uses cloud level-set TO + ML; Autodesk University class "Design Like a Rocket Scientist" compares GD vs TO. — [Autodesk](https://www.autodesk.com/autodesk-university/fr/class/Design-Like-a-Rocket-Scientist-Generative-Design-Versus-Topology-Optimization-in-Autodesk-Fusion-2025)
- **nTop (platform)**, field-driven generative design; TO as one function within broader workflow; explores 100–1000x more configurations. — [nTop](https://www.ntop.com/software/capabilities/generative-design)

### Inferences
- Industry framing (PTC, Autodesk) distinguishes generative design (physics-driven, multi-option) from generative AI (interaction/automation); combined, they compound.
- Diversity of generated designs is a recurring research target (RL rewards, PaDGAN, GenTO).

### Gaps
- Limited head-to-head benchmarks between Autodesk/nTop/Fusion generative design and open research methods.

---

## 4. Topology Optimization (incl. ML-Accelerated)

### Takeaway
TO research splits into (a) ML acceleration/surrogates (one-shot generators, neural reps) and (b) generative/diverse TO (GenTO, RL-based) that yields multiple near-optimal designs instead of one.

### Cited Findings
- **One-Shot Optimal Topology Generation (2018/2019)**, arXiv:1807.10787. Theory-driven meta-learning generator producing TO solutions in one shot; kick-starts iterative solvers. — [arXiv](https://arxiv.org/html/1807.10787v2)
- **NTopo (Zehnder et al., 2021)**, "NTopo: Mesh-free Topology Optimization using Implicit Neural Representations," arXiv:2102.10782. MLP-parameterized density/displacement fields; self-supervised learning of continuous solution spaces. — [arXiv](https://arxiv.org/abs/2102.10782v2)
- **GenTO (Radler et al., 2025)**, "Generative Topology Optimization: Exploring Diverse Solutions in Structural Design," arXiv:2502.13174. Data-free neural network with explicit diversity constraint; solver-in-the-loop; 2D/3D; faster due to parallelism. — [arXiv](https://arxiv.org/abs/2502.13174v1)
- **Topology Optimization via ML/DL Review (2022)**, arXiv:2210.10782. — [arXiv](https://arxiv.org/pdf/2210.10782v1)
- **Topology Optimization and its Applications in Aerospace: A Review (2025)**, *Struct. Multidiscip. Optim.* 68(5). — [ACM](https://dl.acm.org/doi/10.1007/s00158-025-04030-x)
- **A Study on Topology Optimization of Aerospace and Automobile Components (2020)**, SAE 2020-28-0388. TO for aerospace bracket and auto gear; FDM prototypes. — [SAE](https://legacy.sae.org/publications/technical-papers/content/2020-28-0388/)
- **An AI-Assisted Design Method for Topology Optimization without Pre-Optimized Training Data (Halle, 2021)**, MDPI Appl. Sci. 11(19):9041. — [MDPI](https://www.mdpi.com/2076-3417/11/19/9041)

### Inferences
- Shift from "single optimum" TO to "diverse near-optimal sets" (GenTO, RL-based GD) aligns with designer need for alternatives.

### Gaps
- Most ML-TO methods validated on 2D compliance problems; 3D, multi-physics, manufacturing constraints remain hard.

---

## 5. Design Space Exploration (DSE) and "Design Studies"

### Takeaway
DSE papers examine how designers/AI explore generative design spaces; recent work targets interactive DSE, agency in human-AI collaboration, and MBSE-based generative DSE for spacecraft.

### Cited Findings
- **Feature space exploration as alternative for DSE (2023)**, arXiv:2301.11416. Compares parametric design space vs. DL feature space; feature space captures complex parameter relationships. — [arXiv](https://arxiv.org/abs/2301.11416)
- **Evaluating Designer Learning and Performance in Interactive Deep Generative Design (2023)**, *J. Mech. Des.* 145(5): 051403, DOI 10.1115/1.4056374. Human-subject study (N=42) on mechanical metamaterials with C-VAE; designer learning & cognitive load. — [ASME](https://asmedigitalcollection.asme.org/mechanicaldesign/article/145/5/051403/1152164/Evaluating-Designer-Learning-and-Performance-in) · [NSF PAR](https://par.nsf.gov/servlets/purl/10394336)
- **How does agency impact human-AI collaborative DSE? (Khan et al., 2023)**, arXiv:2305.10451. Ship-hull generative design space; compares exploration approaches. — [arXiv](https://arxiv.org/pdf/2305.10451)
- **Towards Improving the DSE Process Using Generative Design with MBSE (Timperley et al., 2023)**, IEEE. SysML profile + GD + optimization for LEO satellite trade-offs; 38–96% exploration time reduction. — [IEEE](https://ieeexplore.ieee.org/document/10116019/)
- **Generative Design Exploration by Integrating Deep Generative Models and Topology Optimization (Oh et al., 2019)** — see §3.
- **Engineering Design Thinking in the Age of Generative AI (2024)**, NSF PAR 10545416. Compares parametric vs. generative design workflows; AI agent explores beyond human cognition. — [NSF PAR](https://par.nsf.gov/servlets/purl/10545416)
- **gem5 Co-Pilot: AI Assistant Agent for Architectural DSE (2025)**, arXiv:2510.19577. LLM-driven DSE for computer architecture with DSDB/RAG. — [arXiv](https://arxiv.org/html/2510.19577v1)
- **Simplification of DSE (2025, CAADRIA)**, DesignSense DSE tool; set-based operations to reduce cognitive overload. — [CumInCAD PDF](https://papers.cumincad.org/data/works/att/caadria2025_564.pdf)
- **A Study on Generative Design Reasoning and Students' Divergent/Convergent Thinking (2024)**, *J. Mech. Des.* 146(3): 031405. GD software and designer reasoning. — [ASME](https://asmedigitalcollection.asme.org/mechanicaldesign/article/146/3/031405/1194687/A-Study-on-Generative-Design-Reasoning-and)
- **From geometry to function: context-aware generative AI for engineering design (2026)**, Proc. Design Society. Reorients generative CAD from geometry to function/manufacturability/sustainability. — [Cambridge](https://www.cambridge.org/core/journals/proceedings-of-the-design-society/article/from-geometry-to-function-towards-contextaware-generative-ai-for-engineering-design/90272687EE5F9335AC57310A303618C6)

### Inferences
- "Design studies" in Autodesk terminology = a generative design run (study) with constraints/goals; research analog = DSE experiment with human subjects.
- DSE is shifting from parametric sweeps to generative (latent) spaces requiring new exploration/visualization tools.

### Gaps
- Few standardized benchmarks for DSE quality; most studies are case-specific or human-subject experiments with small N.

---

## 6. Multi-Objective Optimization (MOO) with Generative/AI Methods

### Takeaway
Recent MOO work uses generative models (GANs, diffusion, flow matching) to sample Pareto fronts directly from data, plus amortized multi-task optimization; preference-guided diffusion improves diversity.

### Cited Findings
- **MO-PaDGAN (2020/2021)**, arXiv:2009.07110. Performance-augmented GAN for multi-objective design; >180% hypervolume improvement on airfoil example. — [arXiv](https://arxiv.org/html/2009.07110v3)
- **ParetoFlow (2025)**, "PARETOFLOW: GUIDED FLOWS IN MULTI-OBJECTIVE OPTIMIZATION," arXiv:2412.03718, ICLR 2025. Flow matching with multi-objective predictor guidance + local filtering for non-convex fronts. — [arXiv](https://arxiv.org/pdf/2412.03718)
- **Preference-Guided Diffusion for MOO (2025)**, NeurIPS 2025 (Annadani et al.). Classifier-based preference guidance; diversity-aware. — [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2025/hash/175fa4fc8f275f877ec85340131c5d7a-Abstract-Conference.html)
- **Amortized Multi-Objective Optimization Across Tasks with Generative Solution Modeling (2025)**, arXiv:2511.09598. Parametric multi-objective Bayesian optimizer with conditional generative model. — [arXiv](https://arxiv.org/pdf/2511.09598v5)
- **Learning Where to Steer: Noise-Space Geometry for Efficient Offline MOO (2026)**, arXiv:2609.38920. Acts on initial noise of diffusion models. — [arXiv](https://arxiv.org/pdf/2609.38920)
- **Surrogate-assisted multi-objective design of complex multibody systems (2024/2025)**, arXiv:2412.14851. Surrogate + MOEA for expensive MBS simulations. — [arXiv](https://arxiv.org/html/2412.14854v1)
- **Machine learning-enabled constrained multi-objective design (2023)**, *Nature Communications* (PDF). Active learning + generative model + simulation. — [Nature](https://www.nature.com/articles/s41467-023-42415-y.pdf)
- **NSGAN: Multi-objective Optimization-Oriented Generative Adversarial Design for Multi-principal Element Alloys (2024)**, *Integrating Materials and Manufacturing Innovation* DOI 10.1007/s40192-024-00354-6. GAN + NSGA-II. — [Springer](https://link.springer.com/article/10.1007/s40192-024-00354-6)
- **Pareto front generation using design generative models (2026)**, US Patent 20260228396A1. Perturbed-requirement generator for Pareto fronts. — [USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/20260228396)

### Inferences
- Generative-model-based MOO is transitioning from single-objective to multi-objective Pareto-front sampling; diversity-aware guidance is the current frontier.

### Gaps
- Most MOO-generative methods tested on continuous low-dim benchmarks, not real CAD/FEA pipelines.

---

## 7. AI for Parametric/Configurational Design & Conceptual Design

### Takeaway
Beyond geometry, AI assists configuration design (component selection) and conceptual design; LLMs support requirements elicitation and knowledge reuse.

### Cited Findings
- **GearFormer (Etesam et al., 2024/2025)** — see §1.
- **LLM agent as mechanical designer (Jadhav & Farimani, 2024)** — see §1.
- **Conversational AI-Powered Design: ChatGPT as Designer, User, and Product (Filippi, 2023)**, *Electronics* 12(16): 3535. — [cited in Sun et al.]
- **Exploring the Role of Text-to-Image AI in Concept Generation (Li, Wang, Sha, 2023)**, *Proc. Design Soc.* 3: 1835–1844. — [cited in Sun et al.]
- **Measuring the Impact of ChatGPT on Fostering Concept Generation in Innovative Product Design (Filippi, 2023)** — [cited in Sun et al.]
- **Utilizing ChatGPT to Assist CAD Design for Microfluidic Devices (Nelson et al., 2023)**, *Lab Chip* 23(17): 3778–3784. — [cited in Sun et al.]
- **From Concept to Manufacturing: Evaluating Vision-Language Models for Engineering Design (2023/2024)**, arXiv:2311.12668. — [cited in Sun et al.]

### Gaps
- Conceptual-design AI studies often lack quantitative performance validation; mostly human-subject or case studies.

---

## 8. Platforms and Tools

### Takeaway
Autodesk Generative Design/Fusion and nTop are the two most cited commercial platforms; research references them as baselines. Siemens NX/PTC Creo appear in industry commentary (PTC blog) but fewer peer-reviewed studies.

### Cited Findings
- **Autodesk Generative Design**: cloud level-set TO + ML; Fusion 360 integration; Airbus bionic partition case study (2019). — [Autodesk News](https://adsknews.autodesk.com/en/news/autodesk-airbus-generative-design-aerospace-factory) · [Fusion Blog](https://www.autodesk.com/products/fusion-360/blog/topology-optimization-and-autodesk-fusion)
- **nTop (formerly nTopology)**: field-driven generative design; TO as one function; 100–1000x config evaluation; implicit geometry. — [nTop](https://www.ntop.com/software/capabilities/generative-design) · [nTop blog](https://www.ntop.com/resources/blog/generative-design-tools-that-put-you-in-control)
- **PTC Creo**: industry perspective on AI in CAD; distinguishes generative design vs. generative AI; rules-based intelligent automation. — [PTC Blog](https://www.ptc.com/en/blogs/cad/ai-cad-next-era-engineering)
- **Siemens NX**: mentioned in industry AI-CAD discussions; limited peer-reviewed research cited here [unverified].

### Gaps
- Peer-reviewed comparative studies across commercial platforms are scarce; most platform claims are vendor-authored.

---

## 9. Cross-Cutting: AI Methods Mapped to Design Stages

### Takeaway
AI methods span the full design process: NLP/LLMs for requirements and concept, generative models for shape/config, surrogate+MOO for detailed design, RL for exploration.

### Cited Findings
- **Mapping AI-based methods to engineering design stages (2023)** — see §2. — [Cambridge PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/706442DFC0F1213F01997072DFD71A3C/S0890060423000203a.pdf/...)
- **A Conceptual Framework for Combining AI and Optimization in Engineering Design (Cagan, Grossmann, Hooker, 1997)**, *Res. Eng. Des.* 9:20–34. Foundational AI+OR integration framework. — [CMU PDF](https://www.contrib.andrew.cmu.edu/org/IDIG/A%20Conceptual%20Framework%20for%20Combining%20Artificial%20Intelligence%20&%20Optimization%20in%20Engineering%20Design.pdf)
- **AI in engineering design: industry perspective (2025?)**, Proc. Design Society. — [Cambridge](https://www.cambridge.org/core/journals/proceedings-of-the-design-society/article/artificial-intelligence-in-engineering-design-an-industry-perspective/B009F2953E0DFD67476EA0F22D2DE744)

---

## 10. Unverified / Flagged Items
- Siemens NX peer-reviewed AI-CAD studies: not found; flagged unverified.
- Specific DOIs for some ASME papers (e.g., cGAN+TO JMD 145(11)) approximated from page numbers; verify before citation.
- arXiv IDs and URLs above taken from search snippets; spot-check recommended for exact versions.
- Some 2026-dated papers (Embodied CAD 2606.31252, LLM mechanical design 104807, mass-reduction drone paper) are very recent; details from snippets only.

---

## Quick Index (arXiv IDs)
1903.01548, 1807.10787, 2008.07119, 2009.07110, 2102.10782, 2210.10782, 2301.11416, 2305.10451, 2404.17525, 2406.00144, 2409.06016, 2412.03718, 2412.13810, 2412.14851, 2502.13174, 2505.08137, 2505.19490, 2508.00843, 2510.19577, 2511.09598, 2511.17511, 2606.31252, 2609.38920, 2501.09655.