# SENIOR CAD KNOWLEDGE: Pointer Guide for an AI Design Assistant

Purpose: route any senior-level mechanical design question to the right constraint
file, research note, or textbook. This is a pointer/guide only - it does not
reproduce equations or standard values; it routes you to the source that owns them.

Sources: 12 research notes in `research_notes/Senior CAD engineer knowledge/`
(listed in Section 7). Facts below are synthesized from those notes.

---

## 1. Purpose and how to use this guide

### 1.1 What this guide is
- A routing layer between a design question and the constraint file / research note
  that owns the answer.
- A level map: which knowledge files belong at which stage of a designer's
  development.
- A citation discipline: every answer should name the constraint file, research
  note, book, or standard it came from.

### 1.2 AI pointer rules (follow in order)
1. Classify the question by topic using Section 2 (Quick lookup) or Section 3
   (Knowledge map).
2. Read the corresponding constraint file in `knowledge/constraints/`.
3. If the constraint file references a research note or book, cite it.
4. Never invent equations. Use only equation families named in the research notes
   or constraint files. If an equation is not verified, point to the source.
5. Prefer standards (ASME/ISO/AGMA/AWS) over textbooks for production decisions.
6. State assumptions: jurisdiction, unit system, material, process, load type.
7. For safety-critical parts, require FEA + hand calc + test. Never trust a
   single source.

### 1.3 When NOT to use a constraint file
- Do not use a constraint file to set a safety-critical limit. Use the governing
  code (ASME/ISO/AWS/AGMA).
- Do not use a constraint file's property table as a design allowable. Cross-check
  against supplier datasheets and standards.
- Do not use outdated or unverified research notes without cross-checking.

---

## 2. Quick lookup (topic -> constraint file -> key rule)

| Topic | Constraint file | Key rule |
|---|---|---|
| GD&T symbols, datums, fits | gdt_tolerancing.md | Declare governing standard in title block; default hole-basis H7 |
| Tolerance stack-up | gdt_tolerancing.md | Worst-case for safety-critical; RSS for high-volume |
| FEA setup, mesh, BCs | fea_cae.md | Require convergence check; report element type and mesh size |
| Material selection | materials_selection.md | Ashby method; never use textbook tables as allowables |
| Failure analysis (fatigue, yield) | materials_selection.md | Goodman for fatigue; von Mises for ductile yield |
| Assembly design, mates, DFA | assembly_design.md | Minimize part count; top-down preferred; run interference check |
| Engineering drawings | drawing_standards.md | Baseline dimensioning; title block with standard declaration |
| Surface finish | surface_finish.md | Specify only where function requires; default 3.2 Ra |
| Bolts, welds, pins, keys | fastener_joint_design.md | Size for preload + external + fatigue; weld size = 0.7*thinner |
| Shafts, bearings, gears | power_transmission.md | Shaft diameter is master variable; check critical speed |
| Belts, chains, clutches | power_transmission.md | V-belt wrap >= 120 deg; chain min 17 teeth |
| Vibration, resonance | vibration_dynamics.md | Avoid operating within +/-20% of natural frequency |
| Reliability, safety factors | reliability_safety.md | SF 1.5-4.0 by consequence; FMEA for new designs |
| Cost estimation | cost_estimation.md | Bottom-up most accurate; flag cost drivers early |
| Manufacturing/DFM | manufacturing.md | Capture tools/materials/tolerances in Stage 1 |
| Failure analysis | failure_analysis.md | Start macro then micro; never declare from one feature |
| Machining/shop-floor | machining_shop_floor.md | Use standard drill sizes; +/-0.1mm default tolerance |
| Metrology/inspection | metrology_gdt_inspection.md | Measure on correct datum; check temperature effects |
| Trade-off decisions | tradeoff_case_studies.md | Pugh matrix for concepts; weighted matrix for final |
| Regulatory compliance | regulatory_compliance.md | ISO 12100 risk assessment first; declare standards |
| Prototyping | prototyping_methods.md | Fail fast; lowest-cost prototype first |
| Tool design (AI) | tool_design.md | Descriptions state when to invoke + how to build args |
| Context management (AI) | context_management.md | Compact at 80% budget; cache stable prefixes |
| Guardrails (AI) | guardrails_and_production.md | OWASP LLM01 #1; kernel is referee |
| Cost/latency (AI) | cost_and_reliability.md | Prompt caching 41-80% savings; track KV-cache hit rate |

---

## 3. Knowledge map (domain -> constraint files)

### 3.1 Mechanical design (senior-level)
- GD&T & tolerancing -> `knowledge/constraints/gdt_tolerancing.md`
- FEA/CAE -> `knowledge/constraints/fea_cae.md`
- Materials selection & failure -> `knowledge/constraints/materials_selection.md`
- Assembly design -> `knowledge/constraints/assembly_design.md`
- Drawing standards -> `knowledge/constraints/drawing_standards.md`
- Surface finish -> `knowledge/constraints/surface_finish.md`
- Fastener & joint design -> `knowledge/constraints/fastener_joint_design.md`
- Power transmission -> `knowledge/constraints/power_transmission.md`
- Vibration & dynamics -> `knowledge/constraints/vibration_dynamics.md`
- Reliability & safety -> `knowledge/constraints/reliability_safety.md`
- Cost estimation -> `knowledge/constraints/cost_estimation.md`
- Manufacturing & DFM -> `knowledge/constraints/manufacturing.md`
- Failure analysis -> `knowledge/constraints/failure_analysis.md`
- Machining/shop-floor -> `knowledge/constraints/machining_shop_floor.md`
- Metrology/inspection -> `knowledge/constraints/metrology_gdt_inspection.md`
- Trade-off decisions -> `knowledge/constraints/tradeoff_case_studies.md`
- Regulatory compliance -> `knowledge/constraints/regulatory_compliance.md`
- Prototyping -> `knowledge/constraints/prototyping_methods.md`

### 3.2 AI agent design (from agent framework research)
- Tool design -> `knowledge/constraints/tool_design.md`
- Context management -> `knowledge/constraints/context_management.md`
- Guardrails & production -> `knowledge/constraints/guardrails_and_production.md`
- Cost & reliability (AI) -> `knowledge/constraints/cost_and_reliability.md`

### 3.3 Mechanisms (65 files)
- `knowledge/mechanisms/*.md` - one file per mechanism (four_bar_linkage, spur_gear,
  deep_groove_ball, helical_compression_spring, etc.)

### 3.4 Textbooks and standards
- `guides/DESIGN_TEXTBOOKS.md` - pointer guide: which book/standard owns each topic,
  plus 0-to-professional roadmap.

---

## 4. Senior CAD engineer competency checklist

A senior CAD engineer should be able to:

### 4.1 Design
- [ ] Size shafts for fatigue (modified Goodman) and check critical speed.
- [ ] Select bearings by load type, speed, and L10 life.
- [ ] Design gear trains (spur, helical, bevel, worm, planetary) with AGMA/ISO.
- [ ] Size bolted joints for preload, external load, and fatigue.
- [ ] Design welds (fillet/butt) per AWS/ASME.
- [ ] Select fits (ISO 286) by function (clearance/transition/interference).
- [ ] Apply GD&T correctly (datums, position, profile, runout).
- [ ] Create standards-compliant drawings (views, dimensions, title block).

### 4.2 Analysis
- [ ] Set up FEA (mesh, BCs, materials, contact) and verify convergence.
- [ ] Interpret results (von Mises, displacement, safety factor).
- [ ] Run tolerance stack-up (worst-case, RSS, Monte Carlo).
- [ ] Perform vibration analysis (natural frequency, resonance avoidance).
- [ ] Estimate fatigue life (S-N, Goodman, Marin factors).

### 4.3 Manufacturing
- [ ] Select manufacturing process by quantity, material, tolerance, cost.
- [ ] Apply DFM rules (wall thickness, draft, fillets, tool access).
- [ ] Estimate cost (bottom-up, parametric, should-cost).
- [ ] Design for assembly (minimize part count, standardize fasteners).

### 4.4 Materials
- [ ] Select materials using Ashby method and performance indices.
- [ ] Choose heat treatment for required properties.
- [ ] Analyze failure modes (yield, fatigue, creep, wear, corrosion).

### 4.5 Standards
- [ ] Know ASME Y14.5, Y14.100, B1.1, B18, VIII, B31.
- [ ] Know ISO 286, 128, 129, 2768, 8015, 1101, 1302.
- [ ] Know AGMA gear standards, AWS D1.1, ASTM/SAE material specs.

### 4.6 Reliability
- [ ] Apply safety factors with stated basis.
- [ ] Run FMEA and target high RPN items.
- [ ] Design fail-safe or fail-operational systems.

---

## 5. Design process (pointer to WORKFLOW.md)

See `WORKFLOW.md` for the full end-to-end process:
Ideate -> Elicitate -> Research -> Specify -> Explore -> Build -> Validate ->
Review -> Publish -> Deliver -> Write-back.

Each stage maps to components: SKILLS.md (knowledge), contracts/ (specs),
runtime/ (loop), mcp/ (tools), tools/ (validators), memory/ (history).

---

## 6. Gaps and cautions

- Research notes are synthesized from web sources (Wikipedia, textbooks, standards
  bodies). Some equation details and edition-specific data are flagged as
  unverified in the research notes. Cross-check against the governing standard or
  textbook before production use.
- Constraint files are distilled summaries, not full derivations. For exact
  formulas, consult the cited book/standard.
- Standards (ASME/ISO/AWS/AGMA) are normative; textbooks are pedagogical.
  For production decisions, the standard wins.
- Property tables in textbooks are not design allowables; use supplier datasheets.
- Regional texts (Bhandari, Khurmi) use IS standards; verify against current IS
  editions.

---

## 7. References

### Research notes (local)
- `research_notes/Senior CAD engineer knowledge/gdt_tolerancing.md`
- `research_notes/Senior CAD engineer knowledge/fea_cae.md`
- `research_notes/Senior CAD engineer knowledge/manufacturing_dfm.md`
- `research_notes/Senior CAD engineer knowledge/materials_selection_failure.md`
- `research_notes/Senior CAD engineer knowledge/assembly_design.md`
- `research_notes/Senior CAD engineer knowledge/drawing_standards.md`
- `research_notes/Senior CAD engineer knowledge/surface_finish.md`
- `research_notes/Senior CAD engineer knowledge/fastener_joint_design.md`
- `research_notes/Senior CAD engineer knowledge/power_transmission.md`
- `research_notes/Senior CAD engineer knowledge/vibration_dynamics.md`
- `research_notes/Senior CAD engineer knowledge/reliability_safety.md`
- `research_notes/Senior CAD engineer knowledge/cost_estimation_optimization.md`

### Textbook guide
- `DESIGN_TEXTBOOKS.md` - which book/standard owns each topic, 0-to-professional roadmap.

### Mechanism catalog
- `knowledge/mechanisms/*.md` (228 files) - one per mechanism.

### Agent framework research
- `research_notes/Building a Python agent framework/` (6 notes) - OpenAI, Anthropic,
  Google, open-source, core architecture, production.

### Workflow
- `WORKFLOW.md` - end-to-end design process.