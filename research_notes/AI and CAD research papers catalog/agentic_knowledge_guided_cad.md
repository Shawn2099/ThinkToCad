# Agentic, Knowledge-Guided, and Multi-Agent CAD Design Systems: Research Catalog

Scope: research papers (primarily 2024–2026) on AI agents that design, edit, or reason about CAD, including knowledge-guided frameworks, multi-agent systems, and agentic engineering intelligence. Sources are arXiv abstracts (primary). Where an item could not be verified on arXiv it is flagged.

## Major papers on agentic CAD design (2024–2026)

### Takeaway
There is a fast-growing 2024–2026 literature on LLM/VLM agents for CAD, ranging from tool-augmented single agents to multi-agent team mirrors of engineering orgs; most are arXiv preprints, several accepted to venues (ICLR 2026, EMNLP 2026 Findings, ICLAD 2026, MLCAD 2026, FPL 2024, AAAI symposium). Benchmark papers (CADWorld, EngiWorld, LMBuild, RealCADBench, OmniMech) are a major parallel thread.

### Cited Findings
- DeciCAD: Harness-Grounded Learning of Action Policies for CAD Agents — Yufeng Peng et al. — arXiv:2610.21755 (Oct 2026). Domain-native harness exposing semantic CAD actions; SFT+geometry-grounded online RL; best F1/IoU on four CAD benchmarks, 45–88% fewer tokens. — [arXiv:2610.21755](https://arxiv.org/abs/2610.21755)
- AgenticCADedit: A Stateful, Tool-Mediated Agentic Approach to Multimodal 3D CAD Editing — Saptarshi Neil Sinha et al. — arXiv:2609.29621 (Sep 2026). Incremental committed actions on persistent CAD state with face/edge inspection and revert; validity 51.0%→94.8% for qwen3.6-27b. — [arXiv:2609.29621](https://arxiv.org/abs/2609.29621)
- ReliCAD: From Uncertain LLM Generation to Reliable Parametric CAD Modeling — Peng Zheng et al. — arXiv:2609.22325 (Sep 2026). Design-intent modeling → constraint-aware parametric instructions → Agent-ready CAD-kernel API with verification-feedback repair; 99.8% validity, 0.8753 IoU. — [arXiv:2609.22325](https://arxiv.org/abs/2609.22325)
- LLM-Aided Design for Manufacturing: A Multi-Agent System for Intent-Preserving Redesign of CAD for Improved Manufacturability — Kojo Welbeck et al. — arXiv:2609.05559 (Sep 2026). DFM-Redesign: DFM Reviewer + CAD Modifier with compile+visual verification loop; 46-part benchmark. — [arXiv:2609.05559](https://arxiv.org/abs/2609.05559)
- RA-CAD (ReAct Agent for CAD): Learning Post-Execution Critique for State-Aware Text-to-CAD Generation — Shuhao Yan et al. — arXiv:2608.05714 (Aug 2026). Generate–Execute–Critique–Rewrite loop with learnable critique via CCB+FAO (GRPO); SOTA validity/geometry. — [arXiv:2608.05714](https://arxiv.org/abs/2608.05714)
- CADIR: A Cross-Backend Editable Intermediate Representation for Agentic CAD Generation — Yu Liu et al. — arXiv:2608.00891 (Aug 2026). Agent-friendly executable IR on OCCT with construction graph; cross-backend reconstruction to FreeCAD/SolidWorks/Fusion 360. — [arXiv:2608.00891](https://arxiv.org/abs/2608.00891)
- CAD-Assistant: Tool-Augmented VLLMs as Generic CAD Task Solvers — Dimitrios Mallis et al. — arXiv:2412.13810 (Dec 2024, rev Aug 2025). VLLM planner + tool augmentation over FreeCAD Python API; sketch parameterizer, rendering, cross-section tools. — [arXiv:2412.13810](https://arxiv.org/abs/2412.13810)
- From Idea to CAD: A Language Model-Driven Multi-Agent System for Collaborative Design — Felix Ocker et al. — arXiv:2503.04417 (Mar 2025). VLM-based multi-agent (requirements/CAD/vision-QA) from sketches/text; iterative validation. — [arXiv:2503.04417](https://arxiv.org/abs/2503.04417)
- Constructing Mechanical Design Agent Based on Large Language Models — Jiaxing Lu et al. — arXiv:2408.02087 (Aug 2024). Method for building a comprehensive Mechanical Design Agent (MDA) guiding LLM learning. — [arXiv:2408.02087](https://arxiv.org/abs/2408.02087)
- Seek-CAD: Self-refined Generative Modeling for 3D Parametric CAD Using Local Inference via DeepSeek — Xueyang Li et al. — arXiv:2505.17702 (May 2025, rev Feb 2026; accepted ICLR 2026). Training-free local open-source (DeepSeek-R1) CAD generation with visual+CoT self-refinement. — [arXiv:2505.17702](https://arxiv.org/abs/2505.17702)
- AGENT (Aircraft GENeraTor): Aerial Vehicle Generation/Design Tool Using LLMs — Colin Samplawski et al. — arXiv:2504.08981 (Apr 2025). CodeT5+ over AircraftVerse; conditional generation + surrogate simulation. — [arXiv:2504.08981](https://arxiv.org/abs/2504.08981)
- Zero-to-CAD: Agentic Synthesis of Interpretable CAD Programs at Million-Scale Without Real Data — Mohammadmehdi Ataei et al. — arXiv:2604.24479 (Apr 2026). Agentic search (LLM in feedback-driven CAD env) synthesizes ~1M executable CAD sequences; fine-tuned VLM reconstructs CAD programs from multi-view images, beating GPT-5.2. — [arXiv:2604.24479](https://arxiv.org/abs/2604.24479)
- Luban: Building Open-Ended Creative Agents via Autonomous Embodied Verification — Yuxuan Guo et al. — arXiv:2405.15414 (May 2024). Creative building agent in Minecraft with two-level embodied verification; CAD modeling programs + functional verification. — [arXiv:2405.15414](https://arxiv.org/abs/2405.15414)
- DropMicroFluidAgents (DMFAs): Autonomous Droplet Microfluidic Research Framework Through LLM Agents — Dinh-Nguyen Nguyen et al. — arXiv:2501.14772 (Jan 2025). Agents generate ML models and code-based CAD scripts for droplet microfluidic devices. — [arXiv:2501.14772](https://arxiv.org/abs/2501.14772)
- Toward Autonomous Engineering Design: A Knowledge-Guided Multi-Agent Framework — Varun Kumar, George Em Karniadakis — arXiv:2511.03179 (Nov 2025). Multi-agent (Graph Ontologist, Design Engineer, Systems Engineer) with domain knowledge graphs; exemplar aerodynamic optimization of NACA airfoils. — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179)
- Automotive Engineering-Centric Agentic AI Workflow Framework — Tong Duy Son et al. — arXiv:2604.07784 (Apr 2026). Presents "Agentic Engineering Intelligence (AEI)" vision: engineering workflows as constrained, history-aware sequential decision processes; offline workflow-memory + online retrieval/decision support. — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- IndustryForge-27B: A Domain-Enhanced Multimodal Foundation Model for Industrial CAD — (authors in listing) — arXiv:2607.28050 (Jul 2026). (Abstract truncated in listing; CAD-focused foundation model.) — [arXiv:2607.28050](https://arxiv.org/abs/2607.28050)
- RealCADBench: Benchmarking Parametric CAD Modeling from Industrial Design Intents — Guanlin Li et al. — arXiv:2609.03773 (Sep 2026). 12,632 tasks / 19 factory-automation categories; FreeCAD API Python; executability/IoU/visual-semantic judge. — [arXiv:2609.03773](https://arxiv.org/abs/2609.03773)
- CADWorld: Computer-Use Benchmark for Long-Horizon CAD — Zihan Dong et al. — arXiv:2609.16251 (Sep 2026). 200 tasks / 11 workflow categories in FreeCAD via GUI actions; strongest agent 17.5% vs 87% expert. — [arXiv:2609.16251](https://arxiv.org/abs/2609.16251)
- EngiWorld: What Can Frontier Agents Deliver in Professional Engineering Environments? — Hongcheng Gao et al. — arXiv:2609.37686 (Sep 2026). 1,301 tasks across 6 domains (CAD, CAE, CAM, BIM, EDA, DCC) and 26 apps; strongest 44.7/100. — [arXiv:2609.37686](https://arxiv.org/abs/2609.37686)
- LMBuild: Evaluating LLM Agents for Generating Buildable and Functional Structures — Jiateng Liu et al. — arXiv:2610.04292 (Oct 2026). Benchmark for buildable/functional assembled structures. — [arXiv:2610.04292](https://arxiv.org/abs/2610.04292)
- OmniMech: All-in-one Multimodal Mechanical Benchmark for 3D Reconstruction — Taiting Lu et al. — arXiv:2608.05539 (Aug 2026). Million-scale; includes tool-augmented agentic reasoning task. — [arXiv:2608.05539](https://arxiv.org/abs/2608.05539)
- On the Evaluation of Engineering Artificial General Intelligence — Sandeep Neema et al. — arXiv:2505.10653 (May 2025). Framework for evaluating eAGI agents; CAD/SysML artifacts as structured outputs. — [arXiv:2505.10653](https://arxiv.org/abs/2505.10653)

### Inferences
- The field has moved from single-shot text-to-CAD generation (2023–2024) to stateful, tool-mediated, iterative agents (2025–2026), mirroring software-engineering agent patterns.
- Multi-agent designs split into (a) role-mirroring engineering teams (Ocker et al., Kumar/Karniadakis, Welbeck et al.) and (b) orchestrator + specialized subagents (Design-to-Plan, Diekmann VCM).
- Benchmarks are becoming first-class artifacts; GUI/computer-use CAD (CADWorld) exposes a large gap vs. code-API agents.

### Gaps
- AgentCAD: no arXiv paper found under that exact name in searched queries; may be a GitHub/project/tool rather than a paper — unverified. Flagged.
- Some abstracts truncated in listing (IndustryForge-27B); details not fully captured.

## Agent architectures observed

### Takeaway
Architectures span single tool-using agents, ReAct-style generate-execute-critique loops, orchestrator-worker multi-agent teams, and vision-based quality-assurance loops; knowledge graphs and harnesses are recurring.

### Cited Findings
- Single tool-using agent: CAD-Assistant (VLLM planner + FreeCAD Python tools) — [arXiv:2412.13810](https://arxiv.org/abs/2412.13810); DeciCAD harness-grounded policy — [arXiv:2610.21755](https://arxiv.org/abs/2610.21755).
- ReAct/state-aware loop: RA-CAD Generate–Execute–Critique–Rewrite — [arXiv:2608.05714](https://arxiv.org/abs/2608.05714); ReliCAD verification-feedback repair — [arXiv:2609.22325](https://arxiv.org/abs/2609.22325).
- Stateful incremental editing: AgenticCADedit persistent session with revert — [arXiv:2609.29621](https://arxiv.org/abs/2609.29621).
- Multi-agent team (orchestrator + specialists): Ocker et al. requirements/CAD/vision-QA — [arXiv:2503.04417](https://arxiv.org/abs/2503.04417); Kumar/Karniadakis Graph Ontologist + Design Engineer + Systems Engineer — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179); Welbeck DFM Reviewer + CAD Modifier — [arXiv:2609.05559](https://arxiv.org/abs/2609.05559).
- Orchestrator over specialized agents: Design-to-Plan (3D feature, 2D drawing, fusion, knowledge retrieval, sequencing, tool selection, report) — [arXiv:2608.24039](https://arxiv.org/abs/2608.24039); Diekmann VCM (system understanding / component generation / signal mapping) — [arXiv:2606.03255](https://arxiv.org/abs/2606.03255).
- Embedded-verification/creative agent: Luban two-level verification — [arXiv:2405.15414](https://arxiv.org/abs/2405.15414).

### Inferences
- Harness design (DeciCAD) and intermediate representations (CADIR) are emerging as first-class architectural components, not just model choices.

### Gaps
- No standard agent protocol/benchmark yet; evaluation fragmented across IoU, validity, chamfer, task success.

## Knowledge sources

### Takeaway
Knowledge enters via domain ontologies/knowledge graphs, RAG over literature/databases, workflow memory, and structured design intent; several frameworks explicitly build KGs from text.

### Cited Findings
- Knowledge graphs from literature: Kumar/Karniadakis Graph Ontologist builds two domain-specific KGs from airfoil literature — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179).
- Knowledge retrieval agent + manufacturing rules: Design-to-Plan — [arXiv:2608.24039](https://arxiv.org/abs/2608.24039).
- Workflow memory + offline knowledge processing: AEI — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784).
- RAG over molecular/literature DBs: Chemist-X (reaction condition optimization, uses CAD tool) — [arXiv:2311.10776](https://arxiv.org/abs/2311.10776).
- Design-intent modeling (structured specs, geometric relations, topology, feature order): ReliCAD — [arXiv:2609.22325](https://arxiv.org/abs/2609.22325).
- Corpus2Skill: offline compiler distills a corpus into hierarchical skill directory; agent navigates summaries to docs; improves QA/RAG grounding — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572) (accepted EMNLP 2026 Findings). Related "Knowledge-as-Skill" (arXiv:2609.25991) reports higher Factuality/Context Recall than reported Corpus2Skill values. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572); [arXiv:2609.25991](https://arxiv.org/abs/2609.25991)
- HERA (multi-agent RAG): hierarchical framework evolving orchestration topologies + role-aware prompt evolution; +38.69% avg over baselines on 6 knowledge-intensive benchmarks — [arXiv:2604.00901](https://arxiv.org/abs/2604.00901).

### Inferences
- Knowledge is shifting from passive RAG chunks to navigable, self-descriptive skill structures (Corpus2Skill/Knowledge-as-Skill), directly relevant to knowledge-guided CAD agents.

### Gaps
- Few CAD-specific ontologies evaluated; most KGs are domain-exemplar (airfoils, manufacturing).

## Tools (CAD kernels, simulators, validators)

### Takeaway
Code-API CAD (FreeCAD Python API, CadQuery, OCCT/OCP) dominates agent tools; verification uses execution validity, IoU/chamfer, visual rendering, physics simulators, and domain verifiers.

### Cited Findings
- FreeCAD Python API: CAD-Assistant, CADWorld, RealCADBench — [arXiv:2412.13810](https://arxiv.org/abs/2412.13810); [arXiv:2609.16251](https://arxiv.org/abs/2609.16251); [arXiv:2609.03773](https://arxiv.org/abs/2609.03773).
- CadQuery program edits: Welbeck DFM-Redesign — [arXiv:2609.05559](https://arxiv.org/abs/2609.05559).
- OCCT kernel / OCP intermediate rep: CADIR — [arXiv:2608.00891](https://arxiv.org/abs/2608.00891).
- Agent-ready CAD kernel API: ReliCAD — [arXiv:2609.22325](https://arxiv.org/abs/2609.22325).
- Physics simulators: Airfoil evaluation in Karniadakis framework (performance metrics); surface inspection RL on CAD-based sim (Roos-Hoefgeest) — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179); [arXiv:2409.03429](https://arxiv.org/abs/2409.03429).
- Siemens toolchains: PTI PSSE via MCP for power-system studies (skill-based agents) — [arXiv:2609.40272](https://arxiv.org/abs/2609.40272); TIA Portal + NX MCD for virtual commissioning VCMs — [arXiv:2606.03255](https://arxiv.org/abs/2606.03255).
- Verification metrics: execution validity, Solid/Surface IoU, Chamfer distance, visual-semantic judge, artifact-centric domain verifiers (EngiWorld) — [arXiv:2609.37686](https://arxiv.org/abs/2609.37686).

### Inferences
- Tool use is converging on "execute code in a real kernel + observe + repair," matching the kernel-as-referee invariant.

### Gaps
- Simulation-in-the-loop for mechanical CAD (FEA/CFD) rarely integrated into agent loops; most verify geometry only.

## Named concepts requested

### Agentic Engineering Intelligence (AEI)
- Defined in arXiv:2604.07784 (Son et al., Apr 2026) as an industrial vision framework modeling engineering workflows as constrained, history-aware sequential decision processes with AI agents supporting engineer-supervised interventions over toolchains; offline workflow-memory construction + online state estimation/retrieval/decision support; control-theoretic interpretation. Representative automotive use cases (suspension design, RL tuning, aero exploration, MBSE). Siemens mentioned in question; the paper's author affiliations not confirmed as Siemens in the abstract — flagged unverified. — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)

### Knowledge-Guided Multi-Agent (Karniadakis)
- "Toward Autonomous Engineering Design: A Knowledge-Guided Multi-Agent Framework" (Kumar & Karniadakis, arXiv:2511.03179, Nov 2025): formalizes engineering design via multi-agent AI with structured design/review loops; Graph Ontologist builds two domain KGs from literature; Systems Engineer sets requirements; Design Engineer proposes candidates; iterative feedback; exemplar NACA 4-digit airfoil aerodynamic optimization. — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179)

### Agentic Synthesis of CAD Programs (Zero-to-CAD)
- Zero-to-CAD (Ataei et al., arXiv:2604.24479, Apr 2026): frames synthesis as agentic search — LLM embedded in feedback-driven CAD env iteratively generates/executes/validates code with tools + doc lookup; ~1M executable editable sequences; fine-tuned VLM reconstructs CAD programs from multi-view images, outperforming GPT-5.2. — [arXiv:2604.24479](https://arxiv.org/abs/2604.24479)

### Corpus2Skill
- Corpus2Skill (Sun, Wei, Hsieh, arXiv:2604.14572, Apr 2026; EMNLP 2026 Findings): system-level retrieval architecture; offline compiler distills corpus into hierarchical skill directory; agent navigates bird's-eye → finer summaries → docs with backtracking; wins on 5/11 datasets, ties 3, loses 3; scope guideline for knowledge-grounded systems. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)

### HERA
- Multiple distinct "HERA" papers:
  - Multi-agent RAG with evolving orchestration + role-aware prompt evolution (Li & Ramakrishnan, arXiv:2604.00901, Apr 2026): +38.69% avg on 6 knowledge-intensive benchmarks. — [arXiv:2604.00901](https://arxiv.org/abs/2604.00901)
  - Hypothesis- and Evidence-guided Research Agent for high-dim Bayesian optimization (Gao et al., arXiv:2609.34281, Sep 2026). — [arXiv:2609.34281](https://arxiv.org/abs/2609.34281)
  - Harness-Environment Co-Evolution for agentic abstention (Luo et al., arXiv:2610.06563, Oct 2026). — [arXiv:2610.06563](https://arxiv.org/abs/2610.06563)
  - Device-cloud collaborative LLM agent coordinator (Zhang et al., arXiv:2605.24598, May 2026). — [arXiv:2605.24598](https://arxiv.org/abs/2605.24598)
  - Hybrid edge-cloud resource allocation (Liu et al., arXiv:2504.00434, Apr 2025). — [arXiv:2504.00434](https://arxiv.org/abs/2504.00434)
- For knowledge-guided agentic CAD context, the most relevant HERA is the multi-agent RAG one (arXiv:2604.00901); others are different domains — flag.

### AgentCAD
- No arXiv paper found under "AgentCAD" in searched queries. Possibly a project/tool name (e.g., CAD agent frameworks) rather than a paper. Flagged unverified; recommend targeted search. — Gap.

### Inferences
- The named concepts cluster around (a) harness/environment co-evolution, (b) knowledge compilation into navigable skills, (c) multi-agent orchestration evolution — all directly applicable to a ThinkToCad-style knowledge-guided CAD agent.

### Gaps
- Siemens affiliation of AEI paper not confirmed from abstract.
- AgentCAD paper not located.