# Commercial and Industry Agentic/AI CAD Tools — Landscape Notes

Scope: commercial products that use AI to design or verify mechanical CAD, current as of October 2026.
Method note: vendor/marketing pages are the primary sources for product positioning; claims that are
vendor-reported are flagged as such. Web search was unreliable during this session (repeated HTTP 401),
so several findings come from direct vendor-page fetches and search-engine result pages that were
successfully retrieved. Conflicts are noted inline.

---

## Key Question 1 — Product-by-product: what each tool does, who it targets, its pipeline stage, verification, and openness

### Takeaway
Commercial agentic CAD splits into three camps: (1) in-CAD copilots that drive an existing CAD session
(MecAgent, Argus/Cosmon, Adam, SOLIDWORKS Aura, Autodesk Assistant), (2) standalone generative /
computational CAD platforms (nTop, Zoo/Zookeeper, Autodesk generative design), and (3) engineering
knowledge agents that stop at retrieval, calculation and part reuse rather than geometry (Leo AI,
Onshape AI Advisor). Almost all are aimed at enterprise engineering teams; very few are priced or
designed for a single person doing small-scale machine design.

### Cited Findings

**MecAgent** (mecagent.com)
- Positioning: "AI copilot that generates parts, assemblies and drawings from text or a spec sheet,
  right in SolidWorks," with a live "CAD Agent" mode and a background "CAD Tasks" mode (drawings from
  CAD, CAD from drawings/text/STEP). — [Source](https://www.mecagent.com)
- Two modes: CAD Agent acts live in the open session (models parts, adds parts to assemblies, applies
  materials/equations, renames, exports, writes macros); Background CAD Tasks run longer jobs
  (drawing generation, drawing-to-CAD) while the user keeps working. — [Source](https://www.mecagent.com)
- Supported CAD: SolidWorks (2024/2025/2026), Inventor, CATIA V5, 3DEXPERIENCE, Fusion 360, NX, Solid
  Edge, Onshape, Creo (several marked "soon"). MecAgent is a separate desktop app that connects to the
  open CAD session. — [Source](https://www.mecagent.com)
- Named customers include NASA, Apple, McLaren, Ford, ZF, Dyson, Caterpillar, Safran; backers include
  Founders Inc., NVIDIA Inception, Autodesk Authorized Developer, Station F. — [Source](https://www.mecagent.com)
- Verification posture: it executes natively inside the CAD kernel (feature tree, mates, equations are
  real SolidWorks features), which is a form of kernel-level validity rather than a separate verifier.
  — [Source](https://www.mecagent.com)

**Onshape (PTC) AI**
- AI Advisor is an in-product LLM help/assist feature grounded in Onshape's own training materials,
  available in the Learning Center, help docs and design environment. — [Source](https://www.onshape.com/en/blog/ai-artificial-intelligence-cloud-native-cad-pdm-platform)
- 2026 roadmap features: LLM-powered FeatureScript autocomplete/generation, AI-powered search by
  AI-generated model descriptions, AI Quick Render (text-to-render), and Replicate Annotations (ML
  matching to copy dimensions/tolerances between drawing views). — [Source](https://www.onshape.com/en/blog/ai-artificial-intelligence-cloud-native-cad-pdm-platform)
- Onshape Labs is an early-access program (announced July 14 2026) for emerging AI features, opt-in via
  Preferences. — [Source](https://www.ptc.com/en/news/2026/onshapelabs)
- Openness: Onshape is explicitly building an MCP (Model Context Protocol) server as "a stable, open
  interface" for teams to build custom agents; PTC announced a FeatureScript MCP server on Aug 13 2026
  for natural-language custom CAD features. — [Source](https://www.onshape.com/en/blog/ai-artificial-intelligence-cloud-native-cad-pdm-platform);
  [Source](https://www.ptc.com/en/news/2026/onshape-launches-featurescript-mcp-server)
- Target: enterprise/team CAD+PDM (cloud-native, database-driven; the whole selling point is the data
  trail for AI). — [Source](https://www.onshape.com/en/blog/ai-artificial-intelligence-cloud-native-cad-pdm-platform)

**Autodesk — generative design + Fusion AI**
- At AU 2026 (Sept 15 2026), Autodesk previewed next-generation agentic AI across Forma, Fusion and
  Flow. Autodesk Assistant is generally available today across many products including Fusion; the
  expanded cross-product agentic experience is "not yet generally available" and begins rolling out
  in 2027. — [Source](https://adsknews.autodesk.com/en/pressrelease/autodesk-advances-agentic-ai-in-its-three-industry-clouds/)
- Next-gen Assistant components: Personal Pulse (prioritized issues), Assistant Spaces (shared agent
  workspace), Assistant Builder (customers connect their own AI agents/tools and third-party agents
  from the Design & Make Marketplace), and an Autodesk AI Orchestrator that selects models per task. — [Source](https://adsknews.autodesk.com/en/pressrelease/autodesk-advances-agentic-ai-in-its-three-industry-clouds/)
- Fusion-specific: "an agentic PLM experience brings AI into product lifecycle workflows, using Autodesk
  Assistant to extract actionable information, identify product impacts, evaluate alternatives, and help
  coordinate changes." — [Source](https://aps.autodesk.com/blog/au-2026-autodesk-building-ai-design-and-make)
- Openness: Assistant Builder explicitly supports third-party agents/tools, so integration is by
  design; but the primary path is Autodesk's own cloud data. — [Source](https://adsknews.autodesk.com/en/pressrelease/autodesk-advances-agentic-ai-in-its-three-industry-clouds/)
- Verification posture: grounded in "geometry, constraints, physics, processes, and project history";
  evaluated for data integrity/privacy/risk; human oversight retained; AI Transparency Cards published.
  — [Source](https://adsknews.autodesk.com/en/pressrelease/autodesk-advances-agentic-ai-in-its-three-industry-clouds/)
- Generative design is the legacy Autodesk optimization feature (topology/lightweighting), distinct from
  the new Assistant; both are part of the Fusion/PD&M stack. — [Source](https://www.autodesk.com/solutions/generative-design) (page 403-blocked; positioning corroborated by nTop/Fusion blog reference)

**nTop**
- Explicitly NOT an AI design tool: "nTop isn't an AI design tool itself — it's built to be the geometry
  infrastructure that AI tools run on." Parametric implicit models are machine-readable and plug into
  Physics AI pipelines, surrogate training and AI agents. — [Source](https://www.ntop.com/platform/)
- Pipeline: implicit modeling → scalable design exploration (thousands of variants) → accelerated physics
  (embedded FEA/CFD, voxel CFD, GPU/ML) → export STEP/Parasolid/STL/3MF downstream. — [Source](https://www.ntop.com/platform/)
- Open architecture: "connects to existing CAD, simulation, and PLM tools"; imports/exports standard
  formats; "doesn't replace your existing CAD or CAE tools." — [Source](https://www.ntop.com/platform/)
- Verification posture: simulation-in-the-loop; a Lockheed Martin case study reports 400+ design variants
  simulated in 6–8 hours with zero mesh failures, and a Fourier Neural Operator (FNO) surrogate giving
  1-second inference vs 3600-second simulation. — [Source](https://www.ntop.com/resources/case-studies/lockheed-martin-accelerates-design-with-ai-and-embedded-simulation)
- Third-party meshfree FEA (Intact.Simulation for nTop) runs directly on implicit geometry, with
  Bayesian optimization as the "AI" layer. — [Source](https://intact-solutions.com/ai-guided-design-exploration-with-intact-simulation-for-ntop)
- Target: aerospace, propulsion, energy, motorsports; "450+ leading engineering teams"; enterprise. — [Source](https://www.ntop.com)

**Argus (Cosmon)**
- Positioning: "AI agent for CAD, CAE and PLM" that "models parts, reviews designs, drafts drawings,
  sets up simulations" inside existing tools, with no scripting/macros. — [Source](https://www.cosmon.com)
- Claims (vendor-reported, unverified): 52% average engineering speedup, 72% higher success rate vs
  other engineering AI tools, 2x more design iterations, <4 weeks to adoption. — [Source](https://www.cosmon.com)
- Integrations named in case studies: SolidWorks (parametric edits) and Ansys Fluent (compressible CFD,
  external aerodynamics). — [Source](https://www.cosmon.com)
- Deployment: cloud or fully on-premise with BYOK; SOC 2, zero data retention, never trained on
  customer data. — [Source](https://www.cosmon.com)
- Target: enterprise ("hundreds of companies including 6 of the Fortune 500"); free trial offered. — [Source](https://www.cosmon.com)
- Note on "PartLab": the task references "Cosmon PartLab agent." My sources describe Cosmon's agent as
  "Argus" and reference "Cosmon AI Agent Nexus"; I did not find a distinct commercial product page for
  "PartLab" in this session. See Gaps.

**CAD/CAE Copilot (aieng)**
- Important correction: CAD/CAE Copilot is an open-source (MIT-licensed) GitHub project
  (`armpro24-blip/cad-cae-copilot`), not a commercial product. It is a "CAD/CAE/CAX workbench for AI
  agents" using real build123d/OpenCASCADE geometry. — [Source](https://github.com/armpro24-blip/cad-cae-copilot)
- It is MCP-based and agent-independent: "bring your own MCP client (Claude Code, Codex, Copilot,
  Cursor), which carries its own model access. The aieng backend itself needs no API key." — [Source](https://github.com/armpro24-blip/cad-cae-copilot)
- Pipeline: spec → MCP agent → build123d/OpenCASCADE CAD → named parts + stable `@face:*` topology
  pointers → deterministic critique → CAE setup/solver → reproducible `.aieng` package. — [Source](https://github.com/armpro24-blip/cad-cae-copilot)
- Verification is unusually explicit: deterministic critique, design-rule assertions that fail the
  build, diff on every edit, V&V-40 credibility tiering, measured mesh accuracy (reliable/marginal/
  unreliable), GCI/Richardson mesh-convergence, NAFEMS-style analytical FEA benchmarks in CI. — [Source](https://github.com/armpro24-blip/cad-cae-copilot)
- Explicit limitations: not production-certified; no fatigue/durability; assembly contact and bolt
  preload are proxy-only; 3D SIMP experimental; mesh-to-CAD best for plane/cylinder geometry. — [Source](https://github.com/armpro24-blip/cad-cae-copilot)
- Target: AI-agent/MCP developers, mechanical engineers exploring AI CAD, makers, researchers. Free. — [Source](https://github.com/armpro24-blip/cad-cae-copilot)

**Zoo / KittyCAD (Text-to-CAD + ML-ephant)**
- Zoo Design Studio is "AI-native CAD" combining sketching, prompting and coding; Zookeeper is a
  conversational CAD agent that "researches, reasons, plans, proposes constraints" and generates
  editable B-rep geometry (not meshes). — [Source](https://zoo.dev)
- Underlying stack: KittyCAD Design API (GPU-native geometry engine) plus ML-ephant ML API; KCL
  (KittyCAD Language) is the design language. Text-to-CAD is described as open-source. — [Source](https://3dprintingindustry.com/news/open-source-ai-text-to-cad-software-by-zoo-unlocks-accessible-3d-design-236964)
- Verification/manufacturability: Zookeeper "evaluates manufacturability as you design"; roadmap stages
  are Design → Analyze → Manufacture (Analyze and Manufacture described as "next"). — [Source](https://zoo.dev)
- Openness: APIs and MCP are the core product; "Zoo MCP has no separate fee, but hosted Zoo operations
  count as external API usage." Usage-based API pricing, no charge for failed calls. — [Source](https://zoo.dev/api-pricing)
- Target: hardware teams, developers, enterprise (enterprise tier: fine-tune on proprietary data, SSO,
  unlimited credits); SOC 2 Type 2, ITAR-compliant US region. — [Source](https://zoo.dev/zookeeper)

**Leo AI**
- A "CAD-aware" engineering AI with a proprietary Large Mechanical Model (LMM) trained on 1M+ engineering
  sources; vendor claims 96% accuracy (vs GPT 46%) and 5+ hours/week saved. — [Source](https://www.machinedesign.com/automation-iiot/article/55330891/leo-ai-leo-ai-how-cad-aware-ai-is-changing-mechanical-design-and-engineering-workflows)
- Primary value: part search and reuse (120M+ vendor parts), organizational knowledge retrieval across
  PLM/PDM/ERP, and calculations with citations to ASME/ISO clauses and transparent Python code. — [Source](https://www.getleo.ai)
- Integrations: SOLIDWORKS, SOLIDWORKS PDM, Autodesk Inventor, Fusion, NX, Teamcenter, SAP PLM. — [Source](https://www.getleo.ai)
- Founded May 2023 (Cambridge, MA); 60,000+ users; $9.7M seed; customers include Scania, HP, Mobileye;
  340+ updates/year. — [Source](https://www.machinedesign.com/automation-iiot/article/55330891/leo-ai-leo-ai-how-cad-aware-ai-is-changing-mechanical-design-and-engineering-workflows)
- Target: enterprise engineering organizations (security: SOC 2, GDPR, zero training on data). — [Source](https://www.getleo.ai)

**Adam (CAD Copilot)**
- AI CAD copilot that works natively inside Onshape and Autodesk Fusion: prompt-driven part editing,
  selection-aware commands, feature-tree optimization, parametric cleanup, keeping geometry editable. — [Source](https://adam.new/copilot)
- Listed on the Autodesk marketplace as "Adam AI CAD Copilot" for Fusion; launched on Product Hunt
  July 1 2026 (#5 daily, 314 upvotes). — [Source](https://marketplace.autodesk.com/apps/ada81435-7335-4dcc-913f-30936f9ae0a1);
  [Source](https://www.altis.vc/research/companies/adam)
- Backed by a $4.1M seed led by TQ Ventures after a viral text-to-3D launch. — [Source](https://www.altis.vc/research/companies/adam)
- Target: mechanical engineers and hardware teams; appears positioned between consumer and enterprise
  (Autodesk marketplace listing, Product Hunt launch). — [Source](https://www.producthunt.com/products/adam-cad-copilot)
- Note: there is a separate, earlier "Adam" text-to-CAD approach by Datagrok described as
  script-generation. The current "Adam CAD Copilot" is the adam.new product. — [Source](https://www.getleo.ai/blog/text-to-cad-tools-comparison-guide)

**Spline AI**
- Text-to-3D and image-to-3D generation producing mesh models with PBR maps, GLB export, and
  web/Apple/Android publishing. It is a graphics/design tool, not mechanical CAD (no B-rep, no
  feature tree, no engineering verification). — [Source](https://spline.design/ai-generate)
- Target: 3D designers/artists and web/AR content, not mechanical engineers. — [Source](https://spline.design/ai-generate)

**SOLIDWORKS 2026 (Dassault Systèmes)**
- SOLIDWORKS 2026 includes 400+ enhancements with AI-powered drawings, Selective Loading, AI fastener
  assembly, and natural-language macro generation; an "Aura copilot" plus "Leo and Marie agents" were
  reported as coming mid-to-late 2026. — [Source](https://www.solidworks.com/media/introducing-solidworks-2026);
  [Source](https://morphos3d.com/blog/solidworks-ai-for-machine-shops)
- Target: the existing SOLIDWORKS user base (enterprise + SME), with AI features bundled into the
  platform/marketplace. — [Source](https://morphos3d.com/blog/solidworks-ai-for-machine-shops)

**Other tools observed**
- `agentcad` is an open-source CAD tool for AI agents with an MCP server (`agentcad[mcp]`), aimed at
  turning prompts into printable parts. — [Source](https://agentcad.dev)
- Spectral Labs' SGS-1 is described as a neural B-rep text-to-CAD model (research/experiment tier). — [Source](https://www.getleo.ai/blog/text-to-cad-tools-comparison-guide)
- MIT researchers built an AI UI agent that drives CAD programs click-by-click from 2D sketches (research,
  not product). — [Source](https://news.mit.edu/2025/new-ai-agent-learns-use-cad-create-3d-objects-sketches-1119)

### Inferences
- The commercial frontier in 2026 is "agent drives the CAD session" (MecAgent, Argus, Adam, Aura,
  Assistant) rather than "AI replaces CAD." The strongest verification story belongs to the open-source
  aieng project, not to any commercial vendor I found.
- Enterprise data (PLM/PDM/feature history) is the recurring moat argument: Onshape, Autodesk, Leo AI,
  Zoo enterprise, and Argus all sell on grounding AI in the customer's existing engineering data.
- The cheapest, most openly integrable option is the open-source aieng/CAD-CAE-Copilot (MIT, MCP, bring
  your own model). Commercial tools are almost uniformly gated behind seats/usage and enterprise sales.

### Gaps
- Cosmon "PartLab": I could not confirm a distinct PartLab product/agent from primary sources this
  session; the Cosmon agent is consistently named Argus. PartLab may be a rebranded or sub-product name
  not documented in the pages I reached.
- Autodesk's Fusion AI page and generative-design page returned HTTP 403 to direct fetch, so some
  Fusion-specific AI details come from the AU 2026 press release rather than product docs.
- No primary sources found for pricing/roadmap of several vendors (see Key Question 2).

---

## Key Question 2 — Pricing and model posture (open vs closed, API/MCP, enterprise vs small-scale)

### Takeaway
Pricing ranges from genuinely free/open-source (aieng, agentcad, Zoo Text-to-CAD) through per-seat SaaS
(MecAgent $84–$417/mo; Leo AI ~$15–$39/mo) to enterprise-negotiated (nTop, Argus/Cosmon, Onshape,
Autodesk, SOLIDWORKS). Openness to API/MCP is widespread at the platform layer (Zoo, Onshape, Autodesk,
aieng) but the AI logic itself is usually proprietary and cloud-hosted.

### Cited Findings
- MecAgent published tiers: Free ($0), Starter ($84/mo, 40 agentic runs, 15,000 tokens/mo), Advanced+
  ($417/mo/seat, 202 agentic runs, 90,000 tokens/mo); Enterprise with shared usage budget, SOC 2, optional
  fine-tuning on customer data. — [Source](https://www.mecagent.com)
- Leo AI pricing is inconsistent across sources: one comparison article states Pro at $39/month and
  Business/Enterprise at $1,800/year with PLM integration; a software-listing page shows a $15/month
  starting price. Treat exact Leo pricing as unconfirmed. — [Source](https://thecadhub.com/blog/ai-cad-software);
  [Source](https://www.softwareadvice.com/product/531017-Leo-AI)
- Zoo: consumption pricing reported at ~$0.0083/second with a free tier; API pricing is usage-based
  (only successful billable operations count, failed calls are free); Zoo MCP has no separate fee but
  hosted operations count as API usage. — [Source](https://thecadhub.com/blog/ai-cad-software);
  [Source](https://zoo.dev/api-pricing)
- Adam CAD Copilot: described as freemium by one comparison site; no official public price found. — [Source](https://thecadhub.com/blog/ai-cad-software)
- nTop: no public price; "Request a Demo" / "Talk to an engineer"; enterprise licensing. — [Source](https://www.ntop.com)
- Argus/Cosmon: no public price; "Start a free trial" / "Book a demo"; enterprise with on-prem BYOK. — [Source](https://www.cosmon.com)
- Autodesk: Assistant is included with Autodesk subscriptions (bundled), next-gen capabilities roll out
  in 2027; pricing for new capabilities "will be announced in 2027." — [Source](https://adsknews.autodesk.com/en/pressrelease/autodesk-advances-agentic-ai-in-its-three-industry-clouds/)
- Onshape: AI Advisor available "for most plans"; broader availability via Onshape Labs opt-in; Onshape
  pricing is plan-based (Standard/Pro/Enterprise) but specific AI pricing not published on the pages
  reached. — [Source](https://www.onshape.com/en/blog/ai-artificial-intelligence-cloud-native-cad-pdm-platform)
- CAD/CAE Copilot (aieng): MIT-licensed open source, free, no backend API key required. — [Source](https://github.com/armpro24-blip/cad-cae-copilot)
- agentcad: open-source with `agentcad[mcp]` install; free. — [Source](https://agentcad.dev)
- Spline AI: pricing not found in the pages reached; product is a freemium-style web app. — [Source](https://spline.design/ai-generate)

### Inferences
- The only tools with fully transparent, low-cost, open integration are the open-source projects
  (aieng, agentcad) and Zoo's API-first model. Everything else requires either a seat subscription or a
  sales conversation.
- Enterprise posture correlates with data-residency claims: Argus (BYOK, zero retention), Leo AI (SOC 2,
  zero training), Zoo (ITAR region), MecAgent (SOC 2, optional fine-tuning), Onshape (government/
  enterprise plans).

### Gaps
- No primary pricing found for: nTop, Argus/Cosmon, Adam, Spline AI, Onshape AI add-ons. Marked "not
  public."
- Exact Leo AI pricing is contradictory across secondary sources; not resolvable from primary pages
  reached this session.

---

## Key Question 3 — Where these products stop (concept CAD? FEA? manufacturing/drawings? shop handoff?)

### Takeaway
Most tools stop at concept/parametric CAD plus documentation (drawings, BOM). Genuine CAE (FEA/CFD)
is served mainly by nTop (embedded/voxel + meshfree FEA), the open-source aieng workbench (CalculiX),
and enterprise simulation tools (Argus drives Ansys Fluent). Manufacturing/CAM/shop handoff is mostly
"next" or partially available, and no tool I found offers an end-to-end design-to-shop-floor agent for
small-scale agricultural machinery.

### Cited Findings
- MecAgent: covers parts, assemblies, drawings, STEP-to-CAD, macros, materials, equations, exploded
  views, motion, configurations, and manufacturing-process change demos — i.e., design + documentation,
  with CAD-native output but no in-tool FEA. — [Source](https://www.mecagent.com)
- Onshape: AI features are help, FeatureScript generation, search, render, and annotation replication —
  all design/documentation. Simulation, CAM and MBD are separate Onshape products, not AI-agent outputs.
  — [Source](https://www.onshape.com/en/blog/ai-artificial-intelligence-cloud-native-cad-pdm-platform)
- Autodesk: Fusion connects "design and manufacturing" and the agentic PLM experience covers change
  coordination; but the AU 2026 next-gen Assistant was explicitly not yet generally available. — [Source](https://adsknews.autodesk.com/en/pressrelease/autodesk-advances-agentic-ai-in-its-three-industry-clouds/)
- nTop: strongest on the analysis side — embedded FEA/CFD, voxel CFD, meshfree FEA, surrogate/Physics
  AI, topology optimization; exports to CAD/CAE/PLM downstream. It stops at early-stage design +
  analysis, not shop-floor manufacturing. — [Source](https://www.ntop.com/platform/)
- Argus/Cosmon: explicitly spans CAD, CAE (Ansys Fluent CFD case studies) and PLM; "drafts drawings,"
  "sets up simulations"; enterprise workflows. — [Source](https://www.cosmon.com)
- aieng: full CAD → CAE path (linear static, modal, linear buckling, steady-state thermal, one-way
  thermal-stress) with CalculiX; explicitly no fatigue/durability, proxy-only assembly contact. — [Source](https://github.com/armpro24-blip/cad-cae-copilot)
- Zoo: roadmap is Design → Analyze → Manufacture, with Analyze and Manufacture described as "next";
  today it is design with manufacturability checks. — [Source](https://zoo.dev)
- Leo AI: knowledge retrieval, part search/reuse, calculations and concept generation; does not produce
  FEA or manufacturing output as its core. — [Source](https://www.getleo.ai)
- Adam: in-CAD part editing and feature-tree cleanup only; no CAE or manufacturing claims found. — [Source](https://adam.new/copilot)
- Spline AI: concept/graphics only; mesh output, no engineering verification. — [Source](https://spline.design/ai-generate)

### Inferences
- The gap between "AI CAD" and "AI engineering" is the simulation/verification layer: only nTop, aieng,
  and (via Ansys integration) Argus run real solvers. Most copilots stop at geometry + drawings.
- Shop handoff (CAM, work instructions, drawings for production) is advertised by MecAgent (drawings,
  DXF export macros) and Autodesk (Fusion manufacturing cloud), but no vendor I found offers a
  fully autonomous design-to-manufacturing agent with verified output.

### Gaps
- I did not find any commercial tool that publicly documents an end-to-end pipeline from concept
  through verified FEA/CFD to CAM/shop-floor instructions in one agentic flow. If it exists, it is not
  in the public pages I reached.

---

## Key Question 4 — What is explicitly NOT served (frugal, single-person, small-scale agricultural machinery)

### Takeaway
Every tool I found is either enterprise-priced/enterprise-positioned or a research/open-source project.
None is marketed for a frugal, single-person shop doing small-scale agricultural machinery. The practical
barriers are cost, data prerequisites (PLM/PDM/CAD data trails), and the fact that verification-heavy
engineering CAE is concentrated in expensive enterprise platforms.

### Cited Findings
- Enterprise/price posture: nTop (demo/enterprise), Argus (Fortune 500, on-prem, enterprise), Onshape
  (enterprise/team), Autodesk (subscription + 2027 rollout), Leo AI (enterprise, $1,800/yr tier),
  MecAgent (enterprise tier with admin controls), SOLIDWORKS (platform subscription). — [Source](https://www.ntop.com);
  [Source](https://www.cosmon.com); [Source](https://adsknews.autodesk.com/en/pressrelease/autodesk-advances-agentic-ai-in-its-three-industry-clouds/);
  [Source](https://www.getleo.ai); [Source](https://www.mecagent.com)
- The data prerequisite: Onshape's AI argument is that AI "is only as effective as the data behind it"
  and requires a database-driven CAD/PDM history; Leo AI and Argus similarly require the customer's
  engineering data. A solo shop with no PLM history gets less value. — [Source](https://www.onshape.com/en/blog/ai-artificial-intelligence-cloud-native-cad-pdm-platform);
  [Source](https://www.getleo.ai); [Source](https://www.cosmon.com)
- Low-cost options exist but are developer/enthusiast tools, not turnkey agricultural-machinery design
  suites: aieng (MIT, bring your own MCP model), agentcad (open-source MCP), Zoo Text-to-CAD
  (open-source, consumption API). — [Source](https://github.com/armpro24-blip/cad-cae-copilot);
  [Source](https://agentcad.dev); [Source](https://3dprintingindustry.com/news/open-source-ai-text-to-cad-software-by-zoo-unlocks-accessible-3d-design-236964)
- Agricultural/farm-machinery-specific AI CAD: I found no commercial product marketed for small-scale
  agricultural machinery design. Industry solution pages I saw target aerospace, automotive, medical,
  energy, robotics and machine design. — [Source](https://www.onshape.com/en/solutions/machine-design);
  [Source](https://www.ntop.com/industries/aerospace/)

### Inferences
- The "frugal single-person" niche is structurally underserved: enterprise tools assume PLM/PDM and
  seat economics; open-source tools assume an agent-savvy user who brings their own model and does
  their own verification.
- For a one-person agricultural-machinery designer, the realistic 2026 stack is open-source CAD kernels
  (build123d/OpenCASCADE via aieng or agentcad) plus a general LLM agent, rather than any commercial
  agentic CAD product.

### Gaps
- I found no vendor that publishes pricing or a target market for "small-scale agricultural machinery."
  This absence is itself the finding, but it is based on the subset of vendor sites I reached, not an
  exhaustive market scan.
- I could not confirm whether any vendor offers an offline/on-prem single-user license suitable for a
  frugal solo shop; enterprise pages emphasize cloud, BYOK and seat licensing.

---

## Appendix — Source reliability notes
- Vendor pages (mecagent.com, cosmon.com, ntop.com, zoo.dev, getleo.ai, autodesk.com, onshape.com,
  solidworks.com) are primary for product claims but are marketing sources; performance numbers
  (e.g., 52% speedup, 96% accuracy, 72% success rate) are vendor-reported and unverified.
- The open-source CAD/CAE Copilot README is the most detailed source on verification methodology and
  limitations found; it is community-maintained (74 stars, MIT license) and self-declares
  "not production-certified."
- Web search (both the integrated search tool and DuckDuckGo HTML) was unreliable this session; several
  queries returned HTTP 401 or CAPTCHA. Findings marked with secondary sources should be re-checked
  before publication.
