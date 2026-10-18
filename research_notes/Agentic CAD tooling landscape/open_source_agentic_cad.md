# Open-Source Agentic-CAD Projects & Frameworks

## Project-by-Project Comparison

### Takeaway
The open-source agentic-CAD landscape splits into two tiers: (1) **runnable systems** with public code — dominated by build123d/CadQuery-based agent loops with OCCT kernel verification (AgentCAD, CADSmith, agentcad, cad-cae-copilot, Pointer-CAD, Seek-CAD, MIRAGE-CAD, CAD-Judge, Zero-to-CAD); and (2) **paper-only systems** (CAD-MLLM, RA-CAD, TOOLCAD, TraceCAD, CADIR) with arXiv papers but no discoverable public code. The dominant architecture pattern is "LLM writes parametric Python CAD code → sandboxed execution → kernel geometry validation → VLM or compiler judge → repair loop."

### Cited Findings

#### Code-Available Projects

**n3r/AgentCAD** — https://github.com/n3r/AgentCAD
- **What**: Agentic-first parametric CAD system for complex parts/systems (rocketry, construction, prototyping). Real B-rep solid modeling via OpenCascade/build123d, browser UI, AI agents as first-class users. — [GitHub](https://github.com/n3r/AgentCAD)
- **License**: Apache-2.0 — [GitHub](https://github.com/n3r/AgentCAD)
- **Maturity**: 6 stars, last updated 2026-10-16. macOS-only today; architecture is Windows/Linux-ready. — [GitHub](https://github.com/n3r/AgentCAD)
- **Architecture**: "The model is code" — every part is a small parametric Python script. "The kernel is the referee" — every change validated by real geometry (B-rep validity, volume, mass, bounding box, interference). Tool surface defined once, exposed twice: as MCP server (Claude Code, Claude Desktop) and built-in chat agent in UI. — [GitHub](https://github.com/n3r/AgentCAD)
- **Verification**: Kernel-based validation (B-rep validity, volume, mass, bbox, interference). Structured errors returned to agent (traceback, failing line, hints) for self-correction. — [GitHub](https://github.com/n3r/AgentCAD)
- **Memory/Repair**: Branching version control (git-based), semantic merges with kernel revalidation, change proposals ("CAD pull requests") with review packets and geometric diffs. Parts library/registry ("pip for parts") with nine-stage publish gate. 30 curated materials. Error Doctor rewrites OCCT errors into plain-language fixes. — [GitHub](https://github.com/n3r/AgentCAD)
- **What it produces**: Parametric Python scripts, validated assemblies, STEP/BREP/STL, 2D engineering drawings (SVG/DXF), geometric analysis (cross-section, wall thickness, inertia tensor), optional linear-static FEM. — [GitHub](https://github.com/n3r/AgentCAD)
- **Reusable**: MCP server, parts library/registry, materials system, Error Doctor, safe_fillet/safe_shell/safe_bool toolkit, constraint solver, change-proposal system. Apache-2.0 license is permissive. — [GitHub](https://github.com/n3r/AgentCAD)

**jabarkle/CADSmith** — https://github.com/jabarkle/CADSmith
- **What**: Multi-agent system generating manufacturing-ready CAD from natural language. Combines LLM code generation with programmatic geometric validation from OpenCASCADE kernel and visual inspection from VLM. — [GitHub](https://github.com/jabarkle/CADSmith)
- **License**: No license specified (null on GitHub) — [GitHub](https://github.com/jabarkle/CADSmith)
- **Maturity**: 37 stars, last updated 2026-10-11. — [GitHub](https://github.com/jabarkle/CADSmith)
- **Architecture**: Five agents: Planner → Coder → Executor → Validator → Refiner. Two nested correction loops: inner loop (execution errors, up to 3 retries), outer loop (geometric errors, up to 5 iterations). — [GitHub](https://github.com/jabarkle/CADSmith)
- **Verification**: Dual approach — (1) exact geometric measurements from OCCT kernel (bounding box, volume, face counts, solid validity); (2) VLM Judge (Claude Opus) cross-references prompt, code, kernel metrics, and three-view render. — [GitHub](https://github.com/jabarkle/CADSmith)
- **Memory/Repair**: RAG knowledge base with 155 CadQuery API entries + 28 worked examples, plus 25 error-solution patterns for common failures. Retrieval over API documentation during code generation. — [GitHub](https://github.com/jabarkle/CADSmith)
- **What it produces**: CadQuery Python code, STEP/STL exports. Benchmark on 100 hand-written prompts across 3 difficulty tiers (primitives, engineering parts, complex parts). 38× reduction in mean Chamfer Distance vs zero-shot. — [GitHub](https://github.com/jabarkle/CADSmith)
- **Reusable**: Multi-agent pipeline architecture, dual kernel+VLM validation approach, RAG knowledge bases, 3-tier benchmark dataset (100 prompts with reference code). Note: no license may restrict reuse. — [GitHub](https://github.com/jabarkle/CADSmith)

**Snitro/Pointer-CAD** — https://github.com/Snitro/Pointer-CAD
- **What**: CVPR 2026 paper. Autoregressive parametric CAD generation from natural language. At each step, takes full text prompt + current intermediate B-Rep solid, predicts next CAD operation (extrude, fillet, chamfer) while directly pointing to faces/edges on existing geometry. — [GitHub](https://github.com/Snitro/Pointer-CAD), [arXiv 2603.04337](https://arxiv.org/abs/2603.04337)
- **License**: No license specified (null on GitHub) — [GitHub](https://github.com/Snitro/Pointer-CAD)
- **Maturity**: 314 stars, last updated 2026-10-12. — [GitHub](https://github.com/Snitro/Pointer-CAD)
- **Architecture**: Language backbone: Qwen2.5-Instruct fine-tuned with LoRA (rank 8). B-Rep encoder: UV-Net (1D/2D convolutions on UV-grid samples of edges/faces, then GNN over face-adjacency graph). Output heads: value head (command token/8-bit quantized numeric), pointer head (128-dim embedding matched to B-Rep faces/edges via cosine similarity), scale head. — [GitHub](https://github.com/Snitro/Pointer-CAD)
- **Verification**: OCC solid construction. Evaluation metrics: IoU, Chamfer, F1, watertightness. — [GitHub](https://github.com/Snitro/Pointer-CAD)
- **What it produces**: Step-by-step CAD models. Dataset: Recap-OmniCAD on HuggingFace. — [GitHub](https://github.com/Snitro/Pointer-CAD), [HF Dataset](https://huggingface.co/datasets/Snitro/Recap-OmniCAD)
- **Reusable**: Pre-trained model, dataset, training/evaluation pipeline. Requires Linux + NVIDIA GPU + CUDA. Note: no license may restrict reuse. — [GitHub](https://github.com/Snitro/Pointer-CAD)

**Sunny-Hack/Seek-CAD** — https://github.com/Sunny-Hack/Seek-CAD
- **What**: ICLR 2026 paper. Self-refined generative modeling for 3D parametric CAD using local inference via DeepSeek. — [GitHub](https://github.com/Sunny-Hack/Seek-CAD)
- **License**: MIT — [GitHub](https://github.com/Sunny-Hack/Seek-CAD)
- **Maturity**: 24 stars, last updated 2026-10-05. — [GitHub](https://github.com/Sunny-Hack/Seek-CAD)
- **Architecture**: Self-refinement loop with local DeepSeek inference. Dataset of ~40K CAD models in JSON format supporting sketch, extrude, revolve, fillet, chamfer, shell operations. ~70% contain advanced operations. — [GitHub](https://github.com/Sunny-Hack/Seek-CAD)
- **Verification**: Execution-based (OpenCascade API execution, STEP export). — [GitHub](https://github.com/Sunny-Hack/Seek-CAD)
- **Memory/Repair**: RAG corpus of 10,000 Text-SSR (Sketch, Sketch-based feature, Refinements) pairs. 23,313 pre-processed Text-SSR pairs provided. — [GitHub](https://github.com/Sunny-Hack/Seek-CAD)
- **What it produces**: JSON-format CAD models, code-based representation convertible to DeepCAD format. — [GitHub](https://github.com/Sunny-Hack/Seek-CAD)
- **Reusable**: Dataset (~40K models), RAG corpus, pre-processing scripts. MIT license. — [GitHub](https://github.com/Sunny-Hack/Seek-CAD)

**Cad-Kernel/MIRAGE-CAD** — https://github.com/Cad-Kernel/MIRAGE-CAD
- **What**: Multimodal system generating executable parametric CAD programs. Routes text, rendered image, point cloud, or STEP/B-Rep geometry through shared construction representation and explicit construction plan. — [GitHub](https://github.com/Cad-Kernel/MIRAGE-CAD)
- **License**: 0BSD (no conditions, no attribution required) — [GitHub](https://github.com/Cad-Kernel/MIRAGE-CAD)
- **Maturity**: 0 stars, last updated 2026-08-24. — [GitHub](https://github.com/Cad-Kernel/MIRAGE-CAD)
- **Architecture**: Modality encoders → latent priors → soft-prefix adapter → construction plan → Python CAD code → OpenCASCADE kernel execution → STEP export. Qwen2.5-Coder-1.5B in 4-bit NF4 with LoRA adapters. — [GitHub](https://github.com/Cad-Kernel/MIRAGE-CAD)
- **Verification**: Five gates: syntax, execution, build, kernel validity, STEP export. Deterministic repair rules. — [GitHub](https://github.com/Cad-Kernel/MIRAGE-CAD)
- **Memory/Repair**: Construction graph recording modeling operations, parameter dependencies, constraints, topology selections. Retrieval index for similar parts. — [GitHub](https://github.com/Cad-Kernel/MIRAGE-CAD)
- **What it produces**: Python CAD code, STEP files. External comparison against CAD-Recode. — [GitHub](https://github.com/Cad-Kernel/MIRAGE-CAD)
- **Reusable**: 0BSD license is maximally permissive. Library under `miragecad/` is free of absolute paths. Note: pipeline scripts have machine-specific absolute paths (87 of 165 files carry hard-coded paths) — not turnkey. — [GitHub](https://github.com/Cad-Kernel/MIRAGE-CAD)

**zhouzheyuan/cad-judge** — https://github.com/zhouzheyuan/cad-judge
- **What**: ICASSP 2026 Oral. Replaces VLM judge with CAD compiler for text-to-CAD alignment. Two modes: CJM (Compiler-as-a-Judge) for training-time KTO-style alignment loss; CRM (Compiler-as-a-Review) for inference-time generate→compile-review→refine loop. — [GitHub](https://github.com/zhouzheyuan/cad-judge), [arXiv 2508.04002](https://arxiv.org/abs/2508.04002)
- **License**: NOASSERTION (non-standard, custom license) — [GitHub](https://github.com/zhouzheyuan/cad-judge)
- **Maturity**: 3 stars, last updated 2026-07-22. — [GitHub](https://github.com/zhouzheyuan/cad-judge)
- **Architecture**: CJM compiles predicted SE sequence, computes Chamfer Distance against GT, emits binary preference label for KTO loss. CRM classifies failures (format/geometry/extrusion/boolean) and feeds diagnostics back into prompt. — [GitHub](https://github.com/zhouzheyuan/cad-judge)
- **Verification**: Compiler-based (pythonOCC). Built on Text2CAD, CADPrompt, Fusion360 Reconstruction datasets. — [GitHub](https://github.com/zhouzheyuan/cad-judge)
- **What it produces**: Training-time alignment scores, inference-time self-correcting agentic loop. — [GitHub](https://github.com/zhouzheyuan/cad-judge)
- **Reusable**: CJM/CRM approach is directly applicable to any text-to-CAD system. Note: built partly on CC BY-NC-SA 4.0 code (Text2CAD's CadSeqProc). Custom license may restrict reuse. — [GitHub](https://github.com/zhouzheyuan/cad-judge)

**xuebadi/Zero-to-CAD** — https://github.com/xuebadi/Zero-to-CAD
- **What**: Desktop application (Electron + Python) for AI-driven CAD code generation from multi-view images. Based on Autodesk AI Lab's Zero-to-CAD project. Uses fine-tuned Qwen3-VL-2B VLM. — [GitHub](https://github.com/xuebadi/Zero-to-CAD), [arXiv 2604.24479](https://arxiv.org/abs/2604.24479)
- **License**: Apache-2.0 — [GitHub](https://github.com/xuebadi/Zero-to-CAD)
- **Maturity**: 10 stars, last updated 2026-10-18. macOS-focused. — [GitHub](https://github.com/xuebadi/Zero-to-CAD)
- **Architecture**: Electron frontend → Python inference server (port 18765) → Qwen3-VL-2B + Transformers. Multi-view input (up to 8 rendered views) → CadQuery Python code output. — [GitHub](https://github.com/xuebadi/Zero-to-CAD)
- **Verification**: Execution-based (CadQuery). Benchmark: 82.1% success rate, 0.747 Mean IoU on Zero-to-CAD test set. — [GitHub](https://github.com/xuebadi/Zero-to-CAD)
- **What it produces**: CadQuery Python code. Model: ADSKAILab/Zero-To-CAD-Qwen3-VL-2B on HuggingFace. Dataset: Zero-To-CAD-1m. — [GitHub](https://github.com/xuebadi/Zero-to-CAD), [HF Model](https://huggingface.co/ADSKAILab/Zero-To-CAD-Qwen3-VL-2B)
- **Reusable**: Fine-tuned Qwen3-VL-2B model (Apache-2.0), dataset, inference pipeline. — [GitHub](https://github.com/xuebadi/Zero-to-CAD)

**armpro24-blip/cad-cae-copilot** — https://github.com/armpro24-blip/cad-cae-copilot
- **What**: AI-native CAD/CAE/CAX workbench. MCP-capable agent writes real build123d/OpenCASCADE geometry, exports STEP/STL/GLB, names parts, exposes stable topology pointers, runs deterministic critique, continues into CAE. — [GitHub](https://github.com/armpro24-blip/cad-cae-copilot)
- **License**: MIT — [GitHub](https://github.com/armpro24-blip/cad-cae-copilot)
- **Maturity**: 74 stars, last updated 2026-10-17. — [GitHub](https://github.com/armpro24-blip/cad-cae-copilot)
- **Architecture**: User requirement → MCP agent (plan/reason) → MCP tool layer → CAD modeling → CAE setup & simulation → result evaluation → closed-loop optimization. Human-in-the-loop trust/approval layer gates mutations. Credibility tier stamped on results. All artifacts in self-describing `.aieng` package. — [GitHub](https://github.com/armpro24-blip/cad-cae-copilot)
- **Verification**: Deterministic critique, geometry checks, design-rule assertions, diff-aware edits. CAE path with CalculiX FEA. Analytical FEA benchmark corpus with closed-form references. — [GitHub](https://github.com/armpro24-blip/cad-cae-copilot)
- **What it produces**: STEP, STL, GLB, generated source, thumbnails, topology maps, `.aieng` packages, FEA solver artifacts. — [GitHub](https://github.com/armpro24-blip/cad-cae-copilot)
- **Reusable**: MCP server, `.aieng` package format, topology pointer system, deterministic critique approach, FEA benchmark harness. MIT license. Docker/Codespaces support. — [GitHub](https://github.com/armpro24-blip/cad-cae-copilot)

**jdilla1277/agentcad** — https://github.com/jdilla1277/agentcad
- **What**: CAD CLI and MCP server for AI agents. Agent writes build123d Python scripts by default; agentcad handles execution, STEP export, PNG rendering, mesh export (STL/GLB/OBJ), geometric metrics, validation, diffing, browser preview. CadQuery compatibility mode. — [GitHub](https://github.com/jdilla1277/agentcad)
- **License**: Apache-2.0 — [GitHub](https://github.com/jdilla1277/agentcad)
- **Maturity**: 166 stars, last updated 2026-10-16. Featured on Product Hunt. — [GitHub](https://github.com/jdilla1277/agentcad)
- **Architecture**: Five-stage workflow: Inspect → Specify → Build → Validate → Deliver. Structured JSON on stdout, progress on stderr. Agent skill available via `npx skills add`. — [GitHub](https://github.com/jdilla1277/agentcad)
- **Verification**: Geometric metrics, visual evidence (renders), dimensional checks, structural evidence, difference checking. — [GitHub](https://github.com/jdilla1277/agentcad)
- **What it produces**: Versioned STEP files, PNG renders, mesh exports, spec.json contracts, browser preview. — [GitHub](https://github.com/jdilla1277/agentcad)
- **Reusable**: CLI/MCP server, agent skill, five-stage workflow guide. CADGenBench benchmark results: 48% higher CAD Score, 21.8% lower model cost vs baseline. Apache-2.0. — [GitHub](https://github.com/jdilla1277/agentcad)

#### Additional Code-Available Projects Discovered

**jeremylongshore/cad-ai-agent** — https://github.com/jeremylongshore/cad-ai-agent
- Drawing intelligence for AEC: analyze and safely edit DXF or vector PDF. Model-agnostic, typed, deterministic. Apache-2.0, 45 stars, updated 2026-10-17. — [GitHub](https://github.com/jeremylongshore/cad-ai-agent)

**gchen19/AnkusDrive** — https://github.com/gchen19/AnkusDrive
- CLI + MCP server turning FreeCAD into mechanical-design workbench for LLM agents. Parametric CAD, drawings, FEM/CFD simulation, manufacturing checks. Apache-2.0, 11 stars, updated 2026-10-18. — [GitHub](https://github.com/gchen19/AnkusDrive)

**SmartAI/Chamfer** — https://github.com/SmartAI/Chamfer
- Text/image to CAD agent harness supporting different MCPs and LLMs. NOASSERTION license, 10 stars, updated 2026-09-25. — [GitHub](https://github.com/SmartAI/Chamfer)

**pouyabagheri2005/sudo/CATIA-mcp-ai-automation** — https://github.com/pouyabagheri2005/sudo/CATIA-mcp-ai-automation
- AI-powered CATIA V5 automation using MCP. Connect Claude Desktop to CATIA, generate 3D CAD from natural language. MIT, 8 stars, updated 2026-09-30. — [GitHub](https://github.com/pouyabagheri2005/sudo/CATIA-mcp-ai-automation)

**R-SMP/text-to-design** — https://github.com/R-SMP/text-to-design
- Function calling and agent workflows for automating CAD geometry generation. No license, 7 stars, updated 2026-10-10. — [GitHub](https://github.com/R-SMP/text-to-design)

**bcllcc/modulor** — https://github.com/bcllcc/modulor
- Agent-native 2D drafting + 3D modeling kernel. JSON in, geometry out. MIT, 2 stars, updated 2026-10-12. — [GitHub](https://github.com/bcllcc/modulor)

#### Paper-Only Projects (No Public Code Found)

**CAD-MLLM** — [arXiv 2411.04954](https://arxiv.org/abs/2411.04954)
- **What**: First system capable of generating parametric CAD models conditioned on multimodal input (text, images, point clouds, or combinations). Uses command sequences of CAD models, employs LLMs to align feature space across multimodalities and CAD vectorized representations. — [arXiv](https://arxiv.org/abs/2411.04954)
- **License**: N/A (paper-only)
- **Maturity**: Published 2024 (v3). No public GitHub repo discovered. — [arXiv](https://arxiv.org/abs/2411.04954)
- **Architecture**: LLM aligns multimodal input with CAD command sequences. Omni-CAD dataset (~450K instances with text, multi-view images, points, command sequences). — [arXiv](https://arxiv.org/abs/2411.04954)
- **Reusable**: Omni-CAD dataset concept, multimodal alignment approach. No code available. — [arXiv](https://arxiv.org/abs/2411.04954)

**RA-CAD** — [arXiv 2608.05714](https://arxiv.org/abs/2608.05714)
- **What**: ReAct Agent for CAD. State-aware agent interacting with CAD environment through Generate–Execute–Critique–Rewrite loop. Generates explicit post-execution critique as intermediate policy action. CAD Code Bootstrapping (CCB) establishes fundamental parametric CAD coding capabilities through supervised learning. — [arXiv](https://arxiv.org/abs/2608.05714)
- **License**: N/A (paper-only)
- **Maturity**: Published 2026 (v4). No public GitHub repo discovered. — [arXiv](https://arxiv.org/abs/2608.05714)
- **Architecture**: Generate → Execute → Critique → Rewrite loop with post-execution critique. CCB for bootstrapping coding capabilities. — [arXiv](https://arxiv.org/abs/2608.05714)
- **Reusable**: CCB training approach, critique-then-rewrite pattern. No code available. — [arXiv](https://arxiv.org/abs/2608.05714)

**TOOLCAD** — [arXiv 2604.07960](https://arxiv.org/abs/2604.07960)
- **What**: Agentic CAD framework deploying LLMs as tool-using agents. Interactive CAD modeling gym for rollout reasoning and tool-augmented interaction trajectories. Hybrid feedback and human supervision. End-to-end post-training with online curriculum reinforcement learning for CAD Modeling Chain of Thought (CAD-CoT). — [arXiv](https://arxiv.org/abs/2604.07960)
- **License**: N/A (paper-only)
- **Maturity**: Published 2026 (v2). No public GitHub repo discovered. — [arXiv](https://arxiv.org/abs/2604.07960)
- **Architecture**: Tool-using LLM agent + CAD modeling gym + hybrid feedback + online curriculum RL. Demonstrates open-source LLMs can perform comparably to proprietary models. — [arXiv](https://arxiv.org/abs/2604.07960)
- **Reusable**: CAD-CoT concept, CAD modeling gym design, online curriculum RL approach. No code available. — [arXiv](https://arxiv.org/abs/2604.07960)

**TraceCAD** — [arXiv 2608.03062](https://arxiv.org/abs/2608.03062)
- **What**: Recovery layer for agentic CAD generation. Links requested features, modeling steps, failure evidence, and candidate outcomes as persistent state. Diagnoses faulty operations, searches bounded edits in dependency regions, validates through execution and preservation checks, retains repair outcomes in reusable skill memory. — [arXiv](https://arxiv.org/abs/2608.03062)
- **License**: N/A (paper-only)
- **Maturity**: Published 2026. No public GitHub repo discovered. — [arXiv](https://arxiv.org/abs/2608.03062)
- **Architecture**: Persistent state → fault diagnosis → bounded edit search → execution validation → skill memory. Removing persistent state nearly halves recovery score. — [arXiv](https://arxiv.org/abs/2608.03062)
- **Reusable**: Skill memory concept, localized search approach, persistent state design. No code available. — [arXiv](https://arxiv.org/abs/2608.03062)

**CADIR** — [arXiv 2608.00891](https://arxiv.org/abs/2608.00891)
- **What**: Cross-backend editable intermediate representation for agentic CAD. Built on OCCT geometry kernel via OCP. Records modeling operations, parameter dependencies, constraints, topology selections in construction graph. Geometric Signature Matching for cross-backend reconstruction (FreeCAD, SolidWorks, Fusion 360). — [arXiv](https://arxiv.org/abs/2608.00891)
- **License**: N/A (paper-only)
- **Maturity**: Published 2026. No public GitHub repo discovered. — [arXiv](https://arxiv.org/abs/2608.00891)
- **Architecture**: Construction graph with explicit compositional modeling operations, fine-grained execution diagnostics, Geometric Signature Matching for cross-backend adapters. — [arXiv](https://arxiv.org/abs/2608.00891)
- **Reusable**: Cross-backend IR concept, Geometric Signature Matching, construction graph design. No code available. — [arXiv](https://arxiv.org/abs/2608.00891)

### Inferences

- **Dominant pattern**: The "LLM writes parametric Python → sandboxed execution → OCCT kernel validation → VLM/compiler judge → repair loop" architecture is shared by AgentCAD, CADSmith, agentcad, cad-cae-copilot, and MIRAGE-CAD. This is the de facto standard for text-to-code-to-CAD.
- **License gap**: Several high-profile projects (CADSmith, Pointer-CAD) have no specified license, which creates legal uncertainty for reuse. Projects with clear permissive licenses (Apache-2.0: n3r/AgentCAD, jdilla1277/agentcad, Zero-to-CAD; MIT: Seek-CAD, cad-cae-copilot, CATIA-mcp; 0BSD: MIRAGE-CAD) are safer for adoption.
- **Verification spectrum**: Three verification tiers exist — (1) kernel geometry checks only (agentcad, MIRAGE-CAD), (2) kernel + VLM judge (CADSmith), (3) compiler-as-judge replacing VLM (CAD-Judge). CAD-Judge explicitly argues VLM judges are slow and hackable.
- **Memory/repair is differentiating**: Projects invest differently in persistence — CADSmith uses RAG over API docs, Seek-CAD uses RAG corpus, TraceCAD proposes skill memory, MIRAGE-CAD uses retrieval indexes, n3r/AgentCAD uses git-based VCS with semantic merges.
- **MCP is converging as the tool surface**: n3r/AgentCAD, jdilla1277/agentcad, cad-cae-copilot, AnkusDrive, CATIA-mcp, and Chamfer all expose MCP servers, making MCP the standard agent-to-CAD interface.
- **Paper-only projects (CAD-MLLM, RA-CAD, TOOLCAD, TraceCAD, CADIR) represent the research frontier** — they propose concepts (critique-then-rewrite, skill memory, cross-backend IR, CAD-CoT) that have not yet been released as code but could inform next-generation systems.
- **Maturity varies wildly**: Pointer-CAD (314 stars, CVPR 2026) and agentcad (166 stars, Product Hunt featured) are the most visible; MIRAGE-CAD (0 stars, 0BSD) is research code with hard-coded paths; CAD-Judge (3 stars) is a paper artifact.

### Gaps

- **CAD-MLLM, RA-CAD, TOOLCAD, TraceCAD, CADIR**: No public code repos found despite active 2026 arXiv papers. May have unreleased/private code, or code may appear at future dates. The arXiv abstracts are the only source.
- **CADSmith and Pointer-CAD licenses**: Both show `null` on GitHub. Need to check for LICENSE files in-repo or contact authors. This significantly impacts reusability.
- **CAD-Judge license**: Shows "NOASSERTION" (non-standard). The custom license terms are not clear from the README. Also built partly on CC BY-NC-SA 4.0 code (Text2CAD), which may impose share-alike obligations.
- **No "awesome agentic CAD" curated list found**: Web search returned no results for awesome lists. The closest is the GitHub topic search which surfaced the projects listed above.
- **TraceCAD and CADIR**: Both are August 2026 papers — very recent. Code may be forthcoming but is not yet available.
- **Zero-to-CAD (Autodesk AI Lab)**: The original Autodesk project (arXiv 2604.24479, model + dataset on HuggingFace) is separate from the xuebadi/Zero-to-CAD repo which is a desktop app wrapper. The Autodesk repo itself was not found in GitHub search — only the HuggingFace model and dataset are confirmed.
