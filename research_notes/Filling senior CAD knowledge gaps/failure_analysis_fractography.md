# Failure Analysis and Fractography

## What are the main failure modes (fatigue, overload, corrosion, wear, creep, brittle fracture, stress corrosion cracking)?

### Takeaway
Most mechanical failures are dominated by fatigue and corrosion-assisted cracking; overload produces ductile/brittle rupture, wear removes material, and creep dominates at high temperature/long time. The fracture surface usually preserves evidence of which mode acted.

### Cited Findings
- Fatigue failures follow the same basic steps for high- and low-cycle: crack initiation, stage I (crystallographic/shear) growth, stage II (perpendicular to load) growth, then final fast fracture, often brittle-looking even in ductile alloys — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- High-cycle fatigue (>10^4 cycles) is stress-controlled and mostly elastic; low-cycle fatigue (<10^4 cycles) involves significant plasticity and is strain-controlled — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- Stress corrosion cracking (SCC) is subcritical crack growth in a corrosive environment, with K_Iscc often <1% of K_Ic for susceptible alloy/environment pairs (e.g., 13Cr steel in 3% NaCl: K_Ic 60 vs K_Iscc 12 MN/m^3/2; 18Cr-8Ni in 42% MgCl2: 200 vs 10) — [Wikipedia: Stress corrosion cracking](https://en.wikipedia.org/wiki/Stress_corrosion_cracking).
- Brittle fracture propagates rapidly with little or no plastic deformation; ductile fracture propagates slowly with large plastic deformation and usually arrests when load is removed — [Wikipedia: Brittle fracture](https://en.wikipedia.org/wiki/Brittle_fracture).
- Transgranular fracture (through grains) is typical at room temperature; intergranular fracture (along grain boundaries) becomes more common when grain-boundary strength is reduced (e.g., elevated temperature, sensitization) — [Wikipedia: Brittle fracture](https://en.wikipedia.org/wiki/Brittle_fracture).
- SCC affects metals, polymers (environmental stress cracking), ceramics, and glass; prevention includes material selection, protective coatings, cathodic protection, environmental control, and inspection — [Wikipedia: Stress corrosion cracking](https://en.wikipedia.org/wiki/Stress_corrosion_cracking).
- Notable SCC failures: Silver Bridge (1967, eyebar, chlorides/rust, 46 fatalities), Natchitoches pipeline (1965), Aloha Airlines 243 (1988, fuselage skin), Trans-Alaska Pipeline (2001), NDK Crystal autoclave (2009) — [Wikipedia: Stress corrosion cracking](https://en.wikipedia.org/wiki/Stress_corrosion_cracking).
- Brittle-fracture disasters include pressure vessels (Great Molasses Flood 1919, New Jersey molasses tank 1973), bridges (Silver Bridge 1967, Hoan Bridge 2000), ships (Titanic 1912, Liberty ships, SS Schenectady 1943) — [Wikipedia: Brittle fracture](https://en.wikipedia.org/wiki/Brittle_fracture).

### Inferences
- A single component often fails by a sequence (e.g., fatigue crack initiates at a corrosion pit, then SCC accelerates growth), so the dominant mode must be established from the whole surface, not one feature.
- "Brittle-looking" fatigue final fracture can be mistaken for overload brittle fracture; check for fatigue marks (striations/beach marks) elsewhere on the surface.

### Gaps
- No reliable quantitative wear-rate or creep-rupture data was retrieved; creep/wear details here are from general engineering knowledge, not cited sources in this note.

## How to read fracture surfaces: fatigue striations, beach marks, ratchet marks, chevron patterns, dimples, cleavage, intergranular vs transgranular

### Takeaway
Macro features (beach marks, ratchet marks, chevrons) locate origin and growth direction; micro features (striations, dimples, cleavage facets, grain-boundary facets) identify the mechanism.

### Cited Findings
- Beach marks (clamshell marks) and striations are characteristic of fatigue crack growth; striations mark the crack-tip position per loading cycle and their width equals growth per cycle — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)); [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- Ratchet marks occur where multiple crack fronts originating at different points meet; they help identify multiple initiation sites — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography) (general fractography usage; verify in ASM Fractography).
- Hachures are lines on a fracture surface that can be traced back to the origin of the fracture — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- SEM image of microvoid coalescence on a ductile fracture surface (6061-T6 Al) shows dimpled rupture; SEM is used to resolve fine-scale mechanism features — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- Ductile fracture is accompanied by large plastic deformation and crack arrest/blunting; brittle fracture shows rapid propagation with little plastic deformation — [Wikipedia: Brittle fracture](https://en.wikipedia.org/wiki/Brittle_fracture).
- Transgranular vs intergranular: crack through grains vs along grain boundaries; grain-boundary weakening (temperature/sensitization) favors intergranular — [Wikipedia: Brittle fracture](https://en.wikipedia.org/wiki/Brittle_fracture).
- Chevron (herringbone) patterns point back toward the crack origin and are typical of brittle fracture in plates/shafts; (flag: chevron details from general engineering knowledge, not retrieved source).

### Inferences
- Beach marks are macroscopic and may be absent in high-frequency/constant-amplitude fatigue; striations are microscopic and require SEM.
- Multiple ratchet marks imply multiple origins (e.g., thread roots, keyways, corrosion pits), often a design or manufacturing issue rather than a single defect.

### Gaps
- Detailed definitions of ratchet marks and chevron patterns were not found in retrieved sources; treat as standard fractography knowledge to verify against ASM Fractography/ASM Handbook Vol. 12.

## Fractography: SEM, optical, macro vs micro. What features indicate what?

### Takeaway
Start macro (visual/low-power optical) to map crack extent, origins, and growth directions; use SEM (with EDS) for mechanism identification at the micro scale; combine into a fracture-surface map.

### Cited Findings
- Fractography is the study of fracture surfaces to determine cause of failure; methods are routinely used in forensic engineering/failure analysis and in materials research — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- Initial examination is commonly macro scale using low-power optical microscopy and oblique lighting to identify extent of cracking, possible modes, and likely origins; optical microscopy/macrophotography are often enough if the loading pattern is known — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- USB microscopes are useful for hand-held examination of fracture surfaces with LED illumination — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- SEM provides much higher resolution than optical microscopy but samples are examined in partial vacuum and without color; improved SEMs allow near-atmospheric pressure; SEM combined with EDS allows elemental analysis of very small areas — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- Fatigue fracture in rubber brake seal showing striations at left (SEM) illustrates micro-scale fatigue evidence — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- Fracture surface maps (schematics) can isolate features showing how a crack initiated and grew with time — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- Quantitative fractography compares load history (e.g., g-meter) with lab fatigue records to predict forces and crack progression — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography) (Goldsmith, Wanhill, Molent, Eng. Failure Analysis, 2019).

### Inferences
- Macro tells "where/when direction"; micro tells "how (mechanism)"; neither alone is sufficient for root cause—loading history and material condition must be integrated.

### Gaps
- No source retrieved on AFM, scanning acoustic microscopy, or advanced 3D fractography; listed only as general practice (unverified).

## Root cause analysis methods: 5 Whys, fishbone (Ishikawa), fault tree analysis (FTA), FMEA

### Takeaway
FMEA/FTA are preventive (before failure); 5 Whys/fishbone are reactive root-cause tools. Use FTA for complex logical dependencies, FMEA for component-level risk prioritization, 5 Whys for simple chains, fishbone for brainstorming multiple cause categories.

### Cited Findings
- Failure analysis process collects and analyzes data to determine cause, often to determine corrective actions or liability; forensic engineering methods (fatigue cracks, SCC, ESC) are used to trace defects — [Wikipedia: Failure analysis](https://en.wikipedia.org/wiki/Failure_analysis).
- FMEA and FTA are methods that can be used during prototyping to analyze failures before a product is marketed — [Wikipedia: Failure analysis](https://en.wikipedia.org/wiki/Failure_analysis).
- No-fault-found (NFF) situations occur when an originally reported failure mode cannot be duplicated; causes include oxidation, defective connections, temporary shorts/opens, software bugs, environmental factors, operator error — [Wikipedia: Failure analysis](https://en.wikipedia.org/wiki/Failure_analysis).
- Human factors can be assessed when determining cause; witness statements help reconstruct sequence of events and chain of cause/effect — [Wikipedia: Failure analysis](https://en.wikipedia.org/wiki/Failure_analysis).
- (Flag) Detailed mechanics of 5 Whys, Ishikawa fishbone, FTA gate logic, and FMEA RPN scoring are standard quality-engineering practice; not retrieved from sources in this note—verify against ASQ/ISO 31010 or IEC 61025.

### Inferences
- For a failed component, combine fractographic evidence (mechanism) with process/material/design data (cause); RCA method choice depends on complexity and available data.

### Gaps
- No reliable sourced detail on 5 Whys/Ishikawa/FTA/FMEA steps in retrieved material; provide from standard references only with verification flag.

## Case studies: real failure examples (bridges, aircraft, pressure vessels, rotating shafts, bolts)

### Takeaway
Historical failures show recurring themes: fatigue at stress concentrations, corrosion-assisted cracking, manufacturing defects, and maintenance/inspection gaps.

### Cited Findings
- Versailles train crash (1842): broken locomotive axle from fatigue; early recognition of crack growth under repeated loading and stress concentration — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- de Havilland Comet (1954): metal fatigue of pressure cabin at ADF window (sharp corners, punch rivets, thin skin); led to rounded windows and revised pressure-cabin strength requirements — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- Alexander L. Kielland (1980): fatigue crack in bracing D-6 from 6 mm fillet weld holding a non-load-bearing flange plate; lamellar tearing and cold cracks contributed; 123 fatalities — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- Silver Bridge (1967): SCC of eyebar (rust in joint, high residual stress, high load, low temperature); 46 fatalities; led to nationwide bridge reappraisal — [Wikipedia: Stress corrosion cracking](https://en.wikipedia.org/wiki/Stress_corrosion_cracking).
- Aloha Airlines Flight 243 (1988): partial fuselage failure from SCC in aluminum skin due to repeated pressurization/depressurization; changed maintenance/inspection procedures — [Wikipedia: Stress corrosion cracking](https://en.wikipedia.org/wiki/Stress_corrosion_cracking).
- Bay Bridge shear key rods: failed by hydrogen embrittlement; rods met strength requirements but inhomogeneous structure gave low toughness; analysis included SEM, metallography, hardness, tensile, Charpy, chemical analysis — [Wikipedia: Failure analysis](https://en.wikipedia.org/wiki/Failure_analysis).
- Breast implant catheter (fractography example): overload at connection plus microcracks from failed adhesive bond; silicone rubber is weak in tear/shear — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- Maritime patrol aircraft lower wing plank: non-critical fatigue crack in 3.2 mm AA7075-T6 at fastener hole; quantitative fractography correlated load history (g-meter) with crack growth — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).

### Inferences
- Sharp corners, rivet holes, and fillet welds are recurring initiation sites; design changes (radius corners, better weld profiles) address root causes beyond material selection.

### Gaps
- Pressure-vessel and rotating-shaft/bolt-specific case studies beyond those cited were not retrieved; add from ASM Handbook Vol. 11 case histories (unverified here).

## ASM Handbook Vol. 11 (Failure Analysis) structure and key chapters

### Takeaway
ASM Handbook Vol. 11 "Failure Analysis and Prevention" is the canonical reference; Vol. 12 covers fractography. Specific chapter lists below are from memory and must be verified against the actual handbook.

### Cited Findings
- Fractography is covered in ASM Handbook, Volume 12 (Mills, Kathleen, 1991) per Wikipedia references — [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- Electronic Failure Analysis Handbook (Martin, Perry L.) and Microelectronics Failure Analysis (ASM International, 5th ed. 2004) are cited failure-analysis references — [Wikipedia: Failure analysis](https://en.wikipedia.org/wiki/Failure_analysis).
- (Flag) Typical Vol. 11 contents (from general knowledge, unverified): introduction to failure analysis and prevention; visual examination and light microscopy; SEM; TEM; quantitative fractography; chemical analysis; mechanical testing; nondestructive testing; metallography; case histories by material/component (ferrous, nonferrous, polymers, ceramics, composites); corrosion and wear; fatigue; fracture mechanics; hydrogen embrittlement; high-temperature failures; failure of welds, bolts, gears, bearings, shafts; FMEA/FTA overview.

### Inferences
- Vol. 11 emphasizes a systematic process (visual → nondestructive → SEM/metallography → mechanical/chemical testing → root cause → corrective action), matching the Bay Bridge case-study sequence.

### Gaps
- Exact chapter titles, authors, and page numbers for ASM Handbook Vol. 11 were not retrieved; verify before citing in final deliverables.

## Common failure patterns by component: shafts, bolts, gears, bearings, welds

### Takeaway
Each component has characteristic initiation sites and mechanisms: shafts at stress concentrations (fatigue), bolts at threads/under-head (fatigue, hydrogen embrittlement), gears at contact surfaces (pitting/scuffing), bearings at raceways (spalling/brinelling), welds in HAZ (cracking/fatigue).

### Cited Findings
- Fatigue cracks commonly initiate at stress concentrators: holes, keyways, sharp changes of load direction, inclusions, voids, surface defects — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- Persistent slip bands (PSBs) and intrusions/extrusions on surfaces are crack initiation sites in metals under cyclic loading — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- Hydrogen embrittlement suspected in Bay Bridge shear key rods; cracks from hydrogen under high tensile load plus hydrogen in material — [Wikipedia: Failure analysis](https://en.wikipedia.org/wiki/Failure_analysis).
- Weld-related factors in Kielland: poor fillet-weld profile, lamellar tearing, cold cracks contributed to fatigue failure — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- (Flag) Component-specific patterns (gears pitting/scuffing, bearing spalling/brinelling, HAZ cracking) are standard mechanical-engineering knowledge; not retrieved from sources in this note—verify against ASM Handbook Vol. 11 and AGMA/ISO standards.

### Inferences
- Design/inspection should target the known initiation sites for each component; most fatigue life is consumed in crack growth, so early detection (NDT) is effective.

### Gaps
- No retrieved sources on gear pitting/scuffing, bearing spalling/brinelling, or HAZ cracking specifics; treat as unverified standard practice.

## How to distinguish overload vs fatigue vs corrosion vs wear on a fracture surface

### Takeaway
Overload: no cyclic marks, often ductile dimples or brittle cleavage/chevrons, single event. Fatigue: beach marks/striations, progressive growth from an origin. Corrosion/SCC: branching, intergranular/transgranular facets, oxide/corrosion products, subcritical growth. Wear: material loss, smeared/deformed surfaces, not a single fracture.

### Cited Findings
- Fatigue: striations per cycle, beach marks, origin at stress concentrator; final fracture may look brittle — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)); [Wikipedia: Fractography](https://en.wikipedia.org/wiki/Fractography).
- Brittle vs ductile: brittle propagates rapidly with little plastic deformation; ductile slowly with large plastic deformation and crack blunting/arrest — [Wikipedia: Brittle fracture](https://en.wikipedia.org/wiki/Brittle_fracture).
- SCC: subcritical crack growth in corrosive environment, K_Iscc << K_Ic; transgranular/intergranular depending on alloy/environment; examples include chlorides in stainless steels/aluminum — [Wikipedia: Stress corrosion cracking](https://en.wikipedia.org/wiki/Stress_corrosion_cracking).
- Wear is material removal by mechanical action; (flag: wear-fractography specifics not retrieved—verify).

### Inferences
- If a surface shows both fatigue marks and corrosion products, suspect corrosion-fatigue (synergistic); distinguish by environment exposure and crack morphology.

### Gaps
- No retrieved source explicitly contrasts overload vs fatigue vs corrosion vs wear on fracture surfaces; synthesis here mixes cited facts with standard practice (flag).

## NTSB/FAA accident reports as case studies

### Takeaway
NTSB/FAA reports (and equivalents like AAIB/RAE) are primary, authoritative case studies; they combine fractography, metallurgy, and operational data to establish probable cause and recommendations.

### Cited Findings
- Aloha Airlines Flight 243 (1988): NTSB investigation found SCC in fuselage skin from repeated pressurization cycles; led to inspection/maintenance changes — [Wikipedia: Stress corrosion cracking](https://en.wikipedia.org/wiki/Stress_corrosion_cracking).
- de Havilland Comet (1954): RAE water-tank fatigue tests identified pressure-cabin failure at ADF window; influenced airworthiness requirements — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- List of fatigue-related aviation accidents includes Aloha 243, Comet, United 232, JAL 123, China Airlines 611, Chalk's 101, etc. — [Wikipedia: Fatigue (material)](https://en.wikipedia.org/wiki/Fatigue_(material)).
- NTSB report commonly cited for Aloha 243: NTSB/AAR-89/03 (flag: verify report number against NTSB.gov before citing).

### Inferences
- Accident reports are the gold standard for "what failed and why" because they integrate fractography with operational/maintenance records; they should be cited with report numbers and dates.

### Gaps
- Specific NTSB/FAA report numbers, docket items, and URLs were not retrieved; verify on ntsb.gov/faa.gov before final citation. No direct fetch of NTSB reports was performed.
