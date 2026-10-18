# Failure analysis and fractography constraints (from research)

Sources: research_notes/Filling senior CAD knowledge gaps/failure_analysis_fractography.md;
ASM Handbook Vol. 11, Wikipedia (fractography, fatigue, SCC, brittle fracture).

## Failure modes (dominant: fatigue + corrosion-assisted)
- Fatigue: crack initiation -> stage I (shear/crystallographic) -> stage II
  (perpendicular to load) -> final fast fracture. High-cycle (>1e4) stress-controlled;
  low-cycle (<1e4) strain-controlled with plasticity.
- Overload: ductile (large plastic deformation, dimples) or brittle (little
  plastic deformation, cleavage). Brittle propagates rapidly, arrests when load removed.
- Stress corrosion cracking (SCC): subcritical crack growth in corrosive env.
  K_Iscc often <1% of K_Ic (e.g., 13Cr steel in 3% NaCl: K_Ic 60 vs K_Iscc 12).
  Prevention: material selection, coatings, cathodic protection, inspection.
- Creep: high temp (>0.4 Tm), long time. Rupture life, creep rate.
- Wear: adhesive, abrasive, corrosive, fretting. Hardness and lubrication matter.

## Reading fracture surfaces
- Macro (visual/low-power optical): locate origin, growth direction, crack extent.
  Oblique lighting. Macro tells "where/when"; micro tells "how".
- Micro (SEM, with EDS): striations (fatigue, width = growth per cycle),
  dimples (ductile rupture), cleavage facets (brittle), grain-boundary facets
  (intergranular, temp/sensitization).
- Beach marks (clamshell): macroscopic fatigue, may be absent at constant amplitude.
- Ratchet marks: multiple crack fronts meeting -> multiple initiation sites
  (design/manufacturing issue, not single defect).
- Chevron (herringbone): point back to origin; typical of brittle fracture.
- Hachures: lines traceable to origin.

## Fractography workflow
1. Macro exam (visual + low-power optical) -> map crack extent, origins, directions.
2. Micro exam (SEM + EDS) -> identify mechanism (striations, dimples, cleavage).
3. Integrate with loading history and material condition -> root cause.
4. Neither macro nor micro alone is sufficient.

## Component-specific patterns
- Shafts: fatigue at stress concentrations (keyways, shoulders, threads).
- Bolts: hydrogen embrittlement, fatigue at thread roots.
- Gears: pitting (contact fatigue), scuffing (lubrication failure).
- Bearings: spalling (fatigue), brinelling (overload).
- Welds: HAZ cracking, fatigue at toe.

## Root cause analysis methods
- 5 Whys: simple chains, quick. FMEA/FTA: preventive (before failure).
- Fishbone (Ishikawa): brainstorming multiple cause categories.
- FTA: complex logical dependencies (AND/OR gates).
- FMEA: component-level risk prioritization (RPN = severity x occurrence x detection).
- NFF (no-fault-found): oxidation, defective connections, temp shorts/opens,
  software bugs, environmental factors, operator error.

## AI rules
- Start macro, then micro. Never declare mechanism from one feature.
- "Brittle-looking" fatigue final fracture can be mistaken for overload brittle
  fracture; check for fatigue marks elsewhere.
- Combine fractographic evidence with process/material/design data.
- Flag unverified items (chevron details, ratchet marks) against ASM Fractography.