# Engineering Standards, Handbooks, and Reference Manuals for Mechanical Design

Pointer/guide catalog for an AI design assistant. Each entry: what it covers, level, when to consult, and AI usage guidance. Sources cited inline.

## Q1: What are the indispensable general engineering handbooks?

### Takeaway
Machinery's Handbook is the universal desk reference for machine design/manufacturing data; Shigley's is the canonical teaching text for component design; Roark's and Marks' are the go-to formula/data handbooks; Perry's and Crane TP-410 cover chemical/process and fluid flow respectively.

### Cited Findings
- *Machinery's Handbook* (Industrial Press, New York): continuous publication since 1914; 32nd edition announced; "for machine shop and drafting-room; a reference book on machine design and shop practice for the mechanical engineer, draftsman, toolmaker, and machinist" — [Wikipedia](https://en.wikipedia.org/wiki/Machinery%27s_Handbook); [Industrial Press history](https://books.industrialpress.com/history-of-machinerys-handbook). Table of contents spans Mathematics, Mechanics and Strength of Materials, Properties/Treatment/Testing of Materials, Dimensioning/Gaging/Measuring, Tooling, Machining, Manufacturing Processes, Fasteners, etc. — [31st ed. PDF TOC](https://dl.icdst.org/pdfs/files4/80364b03673ba30eb5ccf1e27e119ffc.pdf). A companion *Machinery's Handbook Guide* (32nd ed.) teaches table/formula use — [Industrial Press](https://books.industrialpress.com/9780831150327/machinerys-handbook-guide).
- *Shigley's Mechanical Engineering Design* (Budynas & Nisbett, McGraw-Hill): intended for students beginning design; covers materials, load/stress analysis, deflection, failure (static + fatigue), shafts, fasteners/nonpermanent joints, welding/permanent joints, springs, bearings, lubrication, gears, clutches/brakes/couplings/flywheels, flexible elements, power transmission case study — [Missouri S&T ScholarsMine](https://scholarsmine.mst.edu/mec_aereng_facwork/2395); [McGraw-Hill](https://www.mheducation.com/highered/product/shigleys-mechanical-engineering-design-nisbett.html).
- *Roark's Formulas for Stress and Strain* (Roark, Young, now Budynas & Sadegh, McGraw-Hill): first published 1938; 9th edition March 2020; analytical formulas for stresses, strains, deflections; tables organized chapter/table/case/subcase; covers bearing/shear stress, stress concentrations, material behavior, stress/strain measurement; includes fatigue & fracture mechanics, stresses in fasteners/joints, composites — [Wikipedia](https://en.wikipedia.org/wiki/Roark%27s_Formulas_for_Stress_and_Strain); [Amazon 8th ed.](https://www.amazon.com/Roarks-Formulas-Stress-Strain-8th/dp/0071742476).
- *Marks' Standard Handbook for Mechanical Engineers* (McGraw-Hill): first published 1916 by Lionel S. Marks (Harvard/MIT); 12th edition 2017 (100th anniversary); contributions from 160+ global experts; broad coverage (math tables, units, mechanics of solids, material properties, applied mechanics, ethics, digital control, sensors/actuators, vehicle electrification new in 12th) — [Wikipedia](https://en.wikipedia.org/wiki/Marks%27_Standard_Handbook_for_Mechanical_Engineers); [McGraw-Hill](https://www.mheducation.com/highered/mhp/product/marks-standard-handbook-mechanical-engineers-12th-edition.html).
- *Perry's Chemical Engineers' Handbook* (McGraw-Hill): first published 1934; 9th edition 2018; ~2,700 pages, 1,900 illustrations; comprehensive chemical engineering reference (mass/energy balance, heat transfer, fluid flow, thermodynamics, distillation, reactors); relevant for process/mechanical interface, heat exchangers, pressure vessels — [Wikipedia](https://en.wikipedia.org/wiki/Perry%27s_Chemical_Engineers%27_Handbook); [Cornell Engineering Library](https://engineering.library.cornell.edu/database/perrys-chemical-engineers-handbook).
- *Crane Technical Paper No. 410 — Flow of Fluids Through Valves, Pipes, Pumps and Fittings*: introduced 1942; "quintessential guide" to fluid flow through valves/pipes/fittings; includes K-factors, friction losses, pipe sizing, pumps, control valves, flow meters, heat transfer (2018/2020/2022 editions) — [Crane TP410 site](https://tp410.com/home); [Crane ChemPharma](https://cranecpe.com/brand/tp410); [Goodreads](https://www.goodreads.com/book/show/5534167-flow-of-fluids-through-valves-fittings-and-pipe).

### Inferences
- Machinery's Handbook is the fastest lookup for thread dimensions, fits, material properties, machining data; Shigley's is better for design methodology and fatigue; Roark's for stress/deflection formulas; Marks' for broad data; Perry's/Crane for process/fluid domains.
- An AI should treat these as reference tables/formulas, not as design authority — always pair with governing code (ASME/ISO).

### Gaps
- Edition-specific page numbers not verified; publisher paywalls prevent full content access.

## Q2: What ASME standards must a mechanical design engineer know?

### Takeaway
ASME Y14.5 (GD&T) is the core tolerancing language; B1.1/B18 govern inch threads/fasteners; Y14.100 governs drawing practices; Section VIII governs pressure vessels; B31 governs piping; Section IX governs welding qualification.

### Cited Findings
- **ASME Y14.5 — Dimensioning and Tolerancing**: "establishes symbols, rules, definitions, requirements, defaults, and recommended practices for stating and interpreting geometric dimensioning & tolerancing (GD&T)" on drawings, models, digital data files; latest revision 2019 (344 pages); reviewed ~every 10 years; 17 standards in Y14 series — [ASME Y14.5 page](https://www.asme.org/codes-standards/y14-standards); [GD&T Basics](https://www.gdandtbasics.com/asme-y14-5-gdt-standard); [ANSI blog](https://blog.ansi.org/ansi/what-are-the-asme-y14-5-and-asme-y14-100-standards).
- **ASME Y14.5.1** — Mathematical Definition of Dimensioning and Tolerancing Principles. **Y14.43** — dimensioning/tolerancing for gages and fixtures. **Y14.49** — Supplemental Dimensioning and Tolerancing Specification (2025) — [ASME Y14 page](https://www.asme.org/codes-standards/y14-standards).
- **ASME B1.1 — Unified Inch Screw Threads (UN, UNR, UNJ)**: specifies thread form, series (UNC/UNF/UNEF/UN), class (1A/1B, 2A/2B, 3A/3B), allowance, tolerance, designation; covers UN/UNR/UNJ forms; 2024 edition — [ASME B1.1 page](https://www.asme.org/codes-standards/find-codes-standards/b1-1-unified-inch-screw-threads-un-unr-thread-form); [ANSI blog 2024](https://blog.ansi.org/ansi/asme-b1-1-2024-unified-inch-screw-threads); [California Fastener](https://www.californiafastener.com/spec-library/asme-b1-1).
- **ASME B18 — Fasteners**: series covering design, dimensions, materials, testing of bolts, screws, nuts, washers, studs; B18.2.1 (square/hex/heavy hex/askew head bolts & screws, inch), B18.2.6 (structural fasteners), B18.12 glossary, B18.18 quality assurance, B18.24 PIN code system — [Bolt Products](https://www.boltproducts.com/blog/asme-b18-fasteners-the-building-blocks-of-engineering-precision); [ASME B18.2.6 scope](https://jl-fasteners.com/pic/1/ASME%20B18.2.6-2006.pdf); [Part Solutions](https://partsolutions.com/partsolutions/asme-b18).
- **ASME Y14.100 — Engineering Drawing Practices**: establishes essential requirements and reference documents for preparation/revision of manual or computer-generated engineering drawings and associated lists; used with Y14.24, Y14.34, Y14.35, Y14.41; 2017 edition (64 pp.) — [ASME Y14.100 page](https://www.asme.org/codes-standards/find-codes-standards/y14-100-engineering-drawing-practices); [ANSI webstore](https://webstore.ansi.org/standards/asme/asmey141002013).
- **ASME Section VIII — Rules for Construction of Pressure Vessels** (BPVC): design, fabrication, inspection, testing, certification of pressure vessels at internal/external pressures exceeding 15 psig; Division 1 general (most common), Division 2 alternative rules, Division 3 high pressure; ~100,000 copies in 100 countries — [ASME VIII.1 page](https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-1-bpvc-section-viii-rules-construction-pressure-vessels-division-1); [PetroSync](https://www.petrosync.com/blog/asme-section-viii); [WeldFabWorld](https://www.weldfabworld.com/asme-section-viii-division-1).
- **ASME B31 — Code for Pressure Piping**: family including B31.1 Power Piping (steam/water/oil/gas/air; power plants), B31.3 Process Piping (petroleum/chemical/pharma/cryo; materials, design, fabrication, examination, testing), B31.4 liquid pipelines, B31.8 gas transmission/distribution, B31.5 refrigeration, B31.9 building services, B31.12 hydrogen — [ASME B31 piping](https://www.asme.org/resources/b31piping); [Inspectioneering](https://inspectioneering.com/tag/asme+b31); [ASME B31.3 page](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping).
- **ASME Section IX — Welding, Brazing, and Fusing Qualifications**: qualification of welders, welding operators, brazers, brazing operators, and welding/brazing procedures (WPS/PQR); variable-based approach; used with Section VIII and B31 — [ASME Section IX course](https://www.asme.org/learning-development/find-course/asme-bpv-code-section-ix-welding-brazing-fusing-qualifications-(2)); [Inspenet](https://inspenet.com/en/articles/asme-section-ix-pressure-vessel-welding).

### Inferences
- For any pressure-containing part, Section VIII/Section IX/B31 take precedence over general machine design texts.
- An AI should never compute pressure vessel wall thickness from Shigley's alone; must invoke Section VIII formulas and material allowable stresses.

### Gaps
- ASME standards are copyrighted; only scope/abstract publicly available; full text requires purchase.

## Q3: What ISO standards must a mechanical design engineer know?

### Takeaway
ISO 286 (fits/tolerances), ISO 128/129 (drawing presentation/dimensioning), ISO 8015 (GPS fundamentals), ISO 2768 (general tolerances), ISO 9001 (QMS), ISO 14001 (EMS) are the core; ISO 898 for metric fastener mechanical properties.

### Cited Findings
- **ISO 286 — Geometrical Product Specifications (GPS): ISO code system for tolerances on linear sizes**: Part 1 basis of tolerances, deviations and fits; Part 2 tables of standard tolerance classes and limit deviations for holes and shafts; defines clearance/transition/interference fits via hole-basis/shaft-basis (e.g., H7/g6); 2010 edition; essential for interchangeability — [ISO 286-1 page](https://standards.iteh.ai/catalog/standards/iso/8447967a-a60c-4980-a9bc-04c64d4db96f/iso-286-1-2010); [EngLab tables](https://engineerlaboratory.com/resources/shaft-tolerances-and-fits-iso-286); [RoyMech](https://www.roymech.co.uk/Useful_Tables/ISO_Tolerances/ISO_LIMITS.htm).
- **ISO 128 — Technical Product Documentation: General Principles of Presentation**: graphical representation on technical drawings; applies to manual and CAD (not 3D models); 15 parts (lines, views, sections); ISO 128-2 covers basic conventions for lines — [Wikipedia ISO 128](https://en.wikipedia.org/wiki/ISO_128); [ISO ICS 01.100.01](https://www.iso.org/ics/01.100.01.html).
- **ISO 129 — Technical Product Documentation: Presentation of Dimensions and Tolerances**: Part 1 general principles of dimensioning; Part 4 shipbuilding, Part 5 structural metalwork — [ISO ICS](https://www.iso.org/ics/01.100.01.html); [ISO 129-1 2004 PDF](https://s538bda2d5ed2d98d.jimcontent.com/download/version/1588561433/module/9041319182/name/ISO%20129_2004.pdf).
- **ISO 8015 — GPS: Fundamentals, Concepts, Principles and Rules**: specifies fundamental concepts/principles/rules for all GPS standards; applies to interpretation of GPS indications on all drawings; defines independency principle, envelope principle, rigid workpiece principle, functional control principle, reference condition (20°C) — [ISO 8015:2011](https://www.iso.org/standard/55979.html); [CERN ISO-GPS handbook](https://indico.cern.ch/event/1607702/contributions/6774136/attachments/3169744/5634588/Handbook-ISO-GPS-Dimensioning-Cetiso-EN.pdf).
- **ISO 2768 — Geometrical Product Specifications: General Tolerances**: Part 1 linear/angular dimensions in 4 classes (f/m/c/v); Part 2 geometrical tolerances in 3 classes (H/K/L); simplifies drawings by default tolerances for untoleranced features; being revised into single ISO 2768 (2026 edition) — [ISO 2768 page](https://www.iso.org/standard/85741.html); [3ERP](https://www.3erp.com/blog/iso-2768-standard); [LEADRP](https://leadrp.net/blog/the-basics-of-general-tolerance-standard-iso-2768-mk).
- **ISO 9001 — Quality Management Systems**: specifies QMS requirements; applicable to any organization; sector adaptations (aerospace, pharma, etc.); 2015 edition; 2026 revision underway — [ISO 9001 explained](https://www.iso.org/insights/iso-9001-explained); [ASQ](https://asq.org/quality-resources/iso-9001).
- **ISO 14001 — Environmental Management Systems**: specifies EMS requirements; Clause 4.3 scope determination; 2015 edition; 2026 revision underway; often integrated with ISO 9001 — [ISO 14001:2015](https://www.iso.org/standard/60857.html); [CertBetter](https://certbetter.com/blog/how-to-determine-the-scope-of-an-environmental-management-system).
- **ISO 898 — Mechanical Properties of Fasteners (carbon/alloy steel)**: Part 1 bolts/screws/studs (property classes 4.6–12.9), Part 2 nuts, Part 5 set screws, Part 6 nuts fine pitch, Part 7 torsional test; metric counterpart to SAE J429 — [California Fastener](https://www.californiafastener.com/spec-library/iso-898-1); [ISO/AWI 898-1](https://www.iso.org/standard/93478.html).

### Inferences
- ISO GPS (8015/1101/286/2768) is a coherent system; mixing ASME Y14.5 and ISO GPS requires explicit drawing note (e.g., "ISO 2768-mK" or "ASME Y14.5").
- An AI must state which standard system (ASME vs ISO) the drawing follows before applying tolerances.

### Gaps
- ISO 1101 (geometrical tolerancing) and ISO 14405 (dimensional tolerancing) not deeply covered; ISO 898-3/4 (stainless fasteners) not covered.

## Q4: What fastener standards must be consulted?

### Takeaway
Use ASME B1.1 + SAE J429 (or ASTM equivalents) for inch fasteners; ISO 898 + ISO metric thread standards for metric; ASME B18 for dimensions/quality; ANSI/ASME B1.1 for thread data.

### Cited Findings
- **SAE J429 — Mechanical and Material Requirements for Externally Threaded Fasteners (inch)**: covers steel bolts/screws/studs/sems/U-bolts up to 1-1/2 in for automotive/industrial; defines Grade 2/5/8 strength (tensile/yield/hardness); head markings (radial lines); counterpart to ASTM A307/A449/A354 family; ISO 898 is metric counterpart — [California Fastener](https://www.californiafastener.com/spec-library/sae-j429); [SAE J429 PDF](https://www.finesz.com/pic/SAE%20J429-1999.pdf); [Portland Bolt](https://www.portlandbolt.com/technical/specifications/sae-j429).
- **ISO 898-1/2/5/6/7** — metric fastener mechanical properties (property classes 4.6, 5.8, 8.8, 10.9, 12.9); counterpart to SAE J429; ASTM F568M harmonized — [California Fastener](https://www.californiafastener.com/spec-library/iso-898-1); [ISO 898-1 2013 PDF](https://cdn.standards.iteh.ai/samples/60610/e211f7b6697643f192d041ceceb1f2be/ISO-898-1-2013.pdf).
- **ASME B18** — fastener dimensions, quality assurance (B18.18), PIN code (B18.24) — [Bolt Products](https://www.boltproducts.com/blog/asme-b18-fasteners-the-building-blocks-of-engineering-precision).
- **ANSI/ASME B1.1** — thread dimensions/tolerances for inch threads (see Q2).
- **ASTM fastener specs** (A307, A325, A490, A354, F3125, F436, A563, A194, F568M) define material/heat-treatment for structural bolts; cross-referenced by ASME B18.2.6 — [ASME B18.2.6 2019 PDF](https://fpg-co.com/Standards/ASME%20B18.2.6-2019.pdf).

### Inferences
- An AI selecting a fastener must state the unit system (inch vs metric) and the property class/grade; mixing SAE grade numbers with metric property classes is a common error.
- Nut grade matching: SAE J995 for inch nuts; ISO 898-2 for metric nuts.

### Gaps
- ASTM F568M and ISO 3506 (stainless) not deeply covered.

## Q5: What gear, welding, and piping standards must be consulted?

### Takeaway
AGMA 2001 (gear rating) plus ISO 6336 for metric gears; AWS D1.1 for structural steel welding; ASME Section IX for welding qualification; ASME B31 for piping; ASME Section VIII for pressure vessels.

### Cited Findings
- **AGMA** (American Gear Manufacturers Association): accredited US gear standards body; AGMA 2001-D04 "Fundamental Rating Factors and Calculation Methods for Involute Spur and Helical Gear Teeth" — rating formulas, not performance assurance; for experienced gear designers; AGMA 6102-C15 vehicle power transmission gears; AGMA 911-B21 aerospace gears; AGMA vs ISO: AGMA empirical/North-America focused, ISO global harmonization — [AGMA 2001-D04](https://members.motionpower.org/MyAGMA/MyAGMA/Store/Item_Detail.aspx?iProductCode=2001_D04&Category=STANDARDS); [Eureka Patsnap AGMA vs ISO](https://eureka.patsnap.com/article/agma-vs-iso-gear-standards-whats-the-difference); [AGMA catalog](https://members.agma.org/common/Uploaded%20files/__AGMA%20Publications%20Catalog.pdf).
- **AWS D1.1/D1.1M — Structural Welding Code–Steel**: premier AWS welding code; originally 1928; 2025 edition (25th); covers fabrication/erection of welded steel structures; materials/design/fabrication/inspection/qualification/reporting; applies to carbon/low-alloy steels ≥1/8 in (3 mm), yield ≤100 ksi (690 MPa); referenced by IBC and AISC 360; does NOT cover pressure vessels/piping (use ASME IX/B31), sheet steel <1/8 in (D1.3), stainless (D1.6), aluminum (D1.2), reinforcing (D1.4), bridges (D1.5) — [AWS D1.1 page](https://www.aws.org/standards-and-publications/codes-and-standards/d1-1); [AWS D1.1 2015 PDF](https://pubs.aws.org/Download_PDFS/D1.1-D1.1M-2015-PV.pdf); [therness](https://www.therness.com/blog/aws-d1-1-structural-welding-code-acceptance-inspection).
- **ASME Section IX** (see Q2) — welding/brazing/fusing qualification (WPS/PQR/welder qual).
- **ASME B31** (see Q2) — piping.
- **ASME Section VIII** (see Q2) — pressure vessels.

### Inferences
- Gears: Shigley's references AGMA 908-B89 for geometry factors; an AI should cite AGMA/ISO numbers, not invent rating factors.
- Welding: AWS D1.1 for structural steel fabrication; ASME IX for procedure/welder qualification on pressure equipment; ASME VIII/B31 for design allowables.

### Gaps
- ISO 6336 (gear rating) scope not individually researched; AWS D1.1 2025 full text not accessed.

## Q6: What tolerance/fit standards must be consulted?

### Takeaway
ISO 286 (metric hole/shaft fits), ANSI B4.1 (inch fits), ISO 2768 (general tolerances), ISO 8015 (GPS fundamentals), ASME Y14.5 (GD&T). ANSI B4.1 and ISO 286 are the inch/metric counterparts.

### Cited Findings
- **ANSI B4.1 — Preferred Limits and Fits for Cylindrical Parts (inch)**: defines preferred tolerances/allowances for nonthreaded cylindrical features; 10 tolerance grades; basic sizes up to 19.69 in (system up to 200 in); fit groups RC (running/sliding), LC (locational clearance), LT (locational transition), LN (locational interference), FN (force/shrink); symbols not shown on drawings, only sizes — [Coban Engineering](https://www.cobanengineering.com/Tolerances/ANSILimitsAndFits.asp); [Engineers Edge](https://www.engineersedge.com/mechanical,045tolerances/preffered-mechanical-tolerances.htm); [KSU ANSI tables](https://fac.ksu.edu.sa/sites/default/files/fits_us_tables_ansi_b4.1-1967_r1987.pdf).
- **ISO 286** (see Q3) — metric hole/shaft fits (H7/g6 etc.).
- **ISO 2768** (see Q3) — general tolerances for untoleranced features.
- **ISO 8015** (see Q3) — GPS fundamentals (independency/envelope principles).
- **ASME Y14.5** (see Q2) — GD&T.

### Inferences
- An AI must not mix inch fit classes (RC/LC/FN) with metric tolerance grades (IT6/IT7); convert via Machinery's Handbook tables if needed.

### Gaps
- ANSI B4.2 (metric preferred fits) not covered; ISO 14405 (dimensional tolerancing) not covered.

## Q7: What material standards and designations must be consulted?

### Takeaway
AISI/SAE numbering designates steel composition; ASTM specifies material properties/products; SAE J429/ISO 898 for fasteners; ASME for pressure vessel materials (Section II).

### Cited Findings
- **AISI/SAE steel grade system**: four-digit designation; first two digits = alloy family (1xxx carbon, 2xxx nickel, 3xxx Ni-Cr, 4xxx Mo, 5xxx Cr, 6xxx Cr-V, 7xxx W, 8xxx Ni-Cr-V, 9xxx Si-Mn); last two digits = carbon content (×0.01%); prefixes (B/C/D/E) for manufacturing method (AISI), suffix H for hardenability; AISI ceased writing specs, now SAE designations — [AZoM](https://www.azom.com/article.aspx?ArticleID=6151); [Specialty Steel](https://www.specialtysteel.com/blog/alloy-steel/steel-specifications-aisi-sae-ams-and-mil); [PMPA](https://www.pmpa.org/tag/aisi-sae-steel-grade-nomenclature); [Wikipedia SAE steel grades](https://en.wikipedia.org/wiki/SAE_steel_grades).
- **ASTM International**: 13,000+ standards; material specifications and test methods for metals, plastics, ceramics; used in construction, manufacturing, materials science; ASME references ASTM for material allowables in pressure vessels (e.g., SA-516, SA-106) — [ASTM](https://www.astm.org); [Navrang Steel ASTM vs ASME](https://www.navrangsteel.com/blog/astm-vs-asme-differences-applications); [School of PE](https://schoolofpe.com/blogs/news/american-society-for-testing-and-materials-astm-standards-html).
- **ASME Section II** (Materials) — referenced by Section VIII/B31 for allowable stresses; not individually researched here.

### Inferences
- An AI quoting "AISI 4140" should note it's a SAE designation (composition only), not a full material spec; mechanical properties require ASTM/SAE/ASME spec plus heat treatment.

### Gaps
- ASTM individual specs (A36, A516, A106, A240, etc.) and ASME Section II not covered; AMS (aerospace material specs) not covered.

## Q8: What fluid/thermal/structural reference manuals are must-haves?

### Takeaway
Crane TP-410 for pipe flow; Perry's for process/thermal; Roark's for stress/deflection; Machinery's Handbook for general data. (Covered in Q1/Q5.)

### Cited Findings
- Crane TP-410 (see Q1) — fluid flow in pipes/valves/fittings/pumps; 2022 edition adds sensible heat transfer, pumps, control valves, flow meters — [Crane BSU 2018](https://www.cranebsu.com/en/news/view/new-flow-of-fluids-tp-410-2018-edition-now-available); [tp410.com](https://tp410.com/home).
- Perry's (see Q1) — heat transfer, fluid flow, distillation, reactors.
- Roark's (see Q1) — stress/strain/deflection formulas.
- Marks' (see Q1) — broad mechanical data.

### Inferences
- For pipe sizing/pressure drop, prefer Crane TP-410 or Darcy-Weisbach with Moody chart; for pump selection, Crane + Perry's.

### Gaps
- Idelchik (flow resistance) and Cameron Hydraulic Data not covered.

## Q9: How should an AI design assistant consult these references?

### Takeaway
Always identify governing standard system first (ASME vs ISO, inch vs metric); cite standard + edition; use handbooks for data/formulas but defer to codes for safety-critical limits; never fabricate values; flag when standard text unavailable.

### Cited Findings
- ASME Y14.5 is "the authoritative guideline for the design language of GD&T" establishing symbols, rules, definitions, requirements, defaults, recommended practices — [GD&T Basics](https://www.gdandtbasics.com/asme-y14-5-gdt-standard).
- ISO 8015 defines fundamental GPS concepts/principles/rules including independency principle (each spec fulfilled independently unless linked) and envelope principle — [ISO 8015:2011](https://www.iso.org/standard/55979.html); [CERN handbook](https://indico.cern.ch/event/1607702/contributions/6774136/attachments/3169744/5634588/Handbook-ISO-GPS-Dimensioning-Cetiso-EN.pdf).
- ISO 2768 general tolerances apply only when drawing references "ISO 2768-mK" in title block; ASME Y14.5 Rule #1 (envelope) provides default form control — [Haizol](https://www.haizol.com/blog/iso-2768-tolerance).
- AGMA 2001 rating factors require "knowledge and judgment... from years of accumulated experience"; empirical factors are general; intended for experienced gear designers — [AGMA 2001-D04](https://members.motionpower.org/MyAGMA/MyAGMA/Store/Item_Detail.aspx?iProductCode=2001_D04&Category=STANDARDS).
- AWS D1.1 is "not a guideline" but referenced by IBC and AISC 360; non-conformance is a code issue — [therness](https://www.therness.com/blog/aws-d1-1-structural-welding-code-acceptance-inspection).

### Inferences
- AI workflow: (1) determine unit system and standard family from drawing/title block; (2) identify governing code (pressure vessel → Section VIII; piping → B31; structural steel weld → D1.1); (3) use handbooks (Machinery's/Roark's/Marks') for data and formulas; (4) cite standard + edition + clause/table; (5) if value unavailable, mark as gap rather than invent.
- AI should never state a pressure vessel thickness, gear rating, or weld size without invoking the governing code.

### Gaps
- No single authoritative "AI consulting" protocol exists in sources; guidance above is synthesized.

## Q10: What gaps remain in this catalog?

### Takeaway
Several important references not covered: ASME Section II materials, ISO 1101/14405, ANSI B4.2, AMS aerospace specs, Cameron Hydraulic Data, Idelchik, and current edition verification for all standards.

### Cited Findings
- Sources used are publisher/standards-body pages, engineering education sites, and forums; full standard texts are paywalled — [ASME store](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping); [ISO](https://www.iso.org/standard/55979.html); [AWS](https://www.aws.org/standards-and-publications/codes-and-standards/d1-1).

### Inferences
- The report writer should treat this catalog as a pointer list; exact clause values require licensed standard access.

### Gaps
- Edition currency: standards revised frequently (e.g., ASME Y14.5 2019, B1.1 2024, B31.3 2024, Section VIII 2025, D1.1 2025, ISO 2768 new edition 2026); verify current edition before use.
- No access to full text of any standard; only scope/abstract/TOC-level info.
- AGMA individual standard numbers beyond 2001/6102/911 not enumerated.
- ASTM individual material specs not enumerated.
- DIN individual standards not enumerated (30,000+ documents); only general scope described.
- Perry's full table of contents not retrieved.