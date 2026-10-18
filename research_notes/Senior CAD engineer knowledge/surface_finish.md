# Surface Finish, Surface Texture, and Surface Roughness for Mechanical Design

## Surface roughness parameters: Ra, Rz, Rq, Rt, Rmax, Rsk, Rku — definitions and typical values

### Takeaway
Ra (arithmetic mean deviation) is the dominant, most commonly specified 1D profile parameter; Rz/Rt describe peak-to-valley extremes; Rq is RMS; Rsk/Rku describe shape (skewness/kurtosis). All are defined in ISO 4287 / ASME B46.1 and assume a filtered profile with a calculated mean line.

### Cited Findings
- Surface roughness is the high-frequency, short-wavelength component of surface finish (surface texture), quantified by deviations of a real surface from its ideal form in the normal direction. — [Wikipedia, Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness)
- Ra = (1/lr) ∫₀^lr |z(x)| dx — arithmetic average of profile height deviations from the mean line. — [Wikipedia, Surface roughness (amplitude parameters table)](https://en.wikipedia.org/wiki/Surface_roughness)
- Rq = sqrt((1/lr) ∫₀^lr z(x)² dx) — root-mean-square (quadratic mean) of profile height deviations; also called RMS. — [Wikipedia, Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness)
- Rz_i = Rp_i + Rv_i (max peak height + max valley depth within one sampling length); Rz = average of Rz_i over the assessment length. — [Wikipedia, Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness)
- Rsk = (1/Rq³) [(1/lr) ∫₀^lr z³(x) dx] — skewness (asymmetry) of the profile about the mean line; Rku = (1/Rq⁴) [(1/lr) ∫₀^lr z⁴(x) dx] — kurtosis (peakedness/tailedness). — [Wikipedia, Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness)
- Rt = range of the collected roughness data points (total peak-to-valley over the evaluation length); RzDIN = (1/s) Σ Rt_i (average Rt over sampling lengths, per ASME Y14.36M). — [Wikipedia, Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness)
- RzJIS = (1/5) Σ (Rp_i − Rv_i) over the five highest peaks/lowest valleys over the whole sampling length (Japanese standard variant). — [Wikipedia, Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness)
- Roughness grade numbers N1–N12 map to Ra values from 0.025 µm (N1) to 50 µm (N12); e.g. N7 = 1.6 µm Ra, N8 = 3.2 µm, N9 = 6.3 µm, N6 = 0.8 µm, N5 = 0.4 µm. — [Wikipedia, Surface roughness (grade table)](https://en.wikipedia.org/wiki/Surface_roughness)
- Conversion factors (approximate, from Ra): Rt ≈ Ra × 8.7, Rz ≈ Ra × 7.2, Rz ISO ≈ Ra × 7.6, Rmax ≈ Ra × 8.0, Rp ≈ Ra × 3.6, RMS ≈ Ra × 1.1. — [Engineers Edge, surface roughness conversion](http://www.engineersedge.com/manufacturing/surface-roughness-conversion.htm)
- Rmax is the single largest peak-to-valley height within the evaluation length (worst-case extreme), distinct from the averaged Rz. — [Engineers Edge, surface roughness conversion](http://www.engineersedge.com/manufacturing/surface-roughness-conversion.htm) (lists Rmax as a parameter)
- Areal (3D) parameters use capital S (or V): Sa, Sq, Sz, Ssk, Sku, plus spatial/hybrid/functional parameters (Sal, Str, Std, Sdq, Sdr, Vmp, Vmc, Vvc, Vvv, etc.) per ISO 25178. — [Wikipedia, ISO 25178](https://en.wikipedia.org/wiki/ISO_25178)
- Roughness is usually specified as an upper limit only; an exception is cylinder bores, which need a minimum roughness to retain oil. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)

### Inferences
- Because Rz/Rt are ~7–9× Ra, a drawing that specifies "3.2 Ra" implies peak-to-valley extremes of roughly 25–28 µm; Rz-based specs (common in some EU/Japanese practice) are not interchangeable with Ra specs without conversion.
- Rsk/Rku matter for functional surfaces: positive Rsk (peaks dominate) tends to higher friction/wear; negative Rsk (valleys dominate, plateau surfaces) is preferred for bearings and oil retention. (General tribology consensus; verify against application standards.)
- Areal Sa/Sq are not numerically equal to profile Ra/Rq; treat them as different metrics and do not mix on the same drawing.

### Gaps
- No authoritative source in this research set gives industry-standard min/max typical values per process for Rsk/Rku; those are application-specific and must come from functional testing.
- Conversion factors above are approximate rules of thumb from one reference; actual ratio depends on surface lay and filter settings (flag as unverified for precision work).

## Surface texture symbols (ISO 1302, ASME B46.1): how to read/write them, lay symbols, machining allowance

### Takeaway
ISO 1302 (now superseded in part by ISO 21920-1:2021) and ASME Y14.36M define the surface-texture symbol: a check-mark-like radical with the roughness value (and optional machining allowance) placed above/left of the bar; lay is indicated by a letter in the symbol (⊥, =, X, M, C, R, P). Unmarked surfaces get a default finish from the general note.

### Cited Findings
- In the US, surface finish is usually specified using ASME Y14.36M; the other common standard is ISO 1302:2002, though ISO 1302 has been withdrawn in favor of ISO 21920-1:2021. — [Wikipedia, Surface finish (Specification)](https://en.wikipedia.org/wiki/Surface_finish)
- ISO 1302 is listed among the "General GPS standards: Areal and profile surface texture" alongside ISO 4287, 4288, 3274, 8785, 25178. — [Wikipedia, Geometric dimensioning and tolerancing (ISO/TC 213)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing)
- The basic GD&T symbol for surface roughness is the check-mark radical (shown in the surface roughness article). — [Wikipedia, Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness)
- Lay is the direction of the predominant surface pattern, ordinarily determined by the production method; lay patterns include parallel, perpendicular, crossed, multi-directional, circular, radial, and particulate. — [Wikipedia, Surface finish (Lay)](https://en.wikipedia.org/wiki/Surface_finish)
- Surface finish comprises three characteristics: lay, surface roughness, and waviness. — [Wikipedia, Surface finish](https://en.wikipedia.org/wiki/Surface_finish)
- Machining allowance and default finish for unmarked surfaces are handled by general notes on the drawing (e.g., "ALL SURFACES 3.2 Ra UNLESS OTHERWISE SPECIFIED"); the symbol can carry a machining-allowance value (material to be removed) in the left position. — [Wikipedia, Surface finish (Specification)](https://en.wikipedia.org/wiki/Surface_finish) (general concept; exact symbol layout per ASME Y14.36M/ISO 1302)
- Cost rises as finish improves; manufacturing processes capable of narrow dimensional tolerances also produce lower roughness. — [Wikipedia, Surface finish (Specification)](https://en.wikipedia.org/wiki/Surface_finish)

### Inferences
- Lay symbols (conventional, from ASME Y14.36M/ISO 1302 practice): ⊥ = perpendicular to the edge/view; = = parallel; X = crossed (angular); M = multi-directional; C = circular (concentric); R = radial; P = particulate (non-directional). Place the letter in the symbol's lower area. (Standard textbook convention; verify against current ASME Y14.36M/ISO 21920-1 before release.)
- Machining allowance: when a casting/forging must be machined, the symbol on the raw part shows the amount of stock to remove (e.g., "6.3" with allowance) and the finished surface shows the final Ra. Keep the allowance as a separate callout to avoid ambiguity.
- Default-finish note is the cheapest way to control cost: specify a coarse default (e.g., 6.3–12.5 Ra) for non-functional surfaces and tighten only where function demands.

### Gaps
- I did not retrieve the actual ASME Y14.36M / ISO 1302 symbol layout diagrams in this research set; symbol positions (roughness value, machining allowance, sampling length, production method) should be verified against the standards text before issuing drawings. Flag as unverified.

## Typical surface finishes by process

### Takeaway
Process capability ranges (Ra, µm): as-cast 6.3–25; as-forged 3.2–12.5; turned 1.6–3.2 (can be better); milled 1.6–6.3; ground 0.4–1.6; polished 0.1–0.4; 3D printed varies (FDM comparatively rough, often >6.3). Finer finishes cost more and usually require secondary operations.

### Cited Findings
- Manufacturing processes produce different roughnesses; generally, processes that are dimensionally precise also produce lower roughness. — [Wikipedia, Surface finish (Specification)](https://en.wikipedia.org/wiki/Surface_finish)
- FDM (fused deposition modelling) parts are difficult and expensive to control for surface roughness. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)
- Engineers Edge provides a "surface roughness average obtainable by common production methods" chart (image) mapping process to Ra; specific numeric per-process bands are in that chart. — [Engineers Edge, surface finish review](http://www.engineersedge.com/surface_finish.htm)
- Grade table gives the standard Ra ladder (N1 0.025 … N12 50 µm) used to select achievable finishes. — [Wikipedia, Surface roughness (grade table)](https://en.wikipedia.org/wiki/Surface_roughness)

### Inferences
- Typical achievable Ra bands (engineering practice, consistent with the cited process/cost relationships and commonly used DFM tables): as-cast 6.3–25 µm; as-forged 3.2–12.5 µm; sawed/broached 3.2–6.3 µm; turned 0.8–3.2 µm (premium tooling/parameters can reach ~0.4); milled 1.6–6.3 µm; bored 0.8–3.2 µm; drilled 3.2–6.3 µm; ground 0.4–1.6 µm; honed 0.2–0.8 µm; lapped 0.05–0.4 µm; polished 0.025–0.4 µm; as-printed FDM 6.3–25+ µm; SLA/SLS 3.2–12.5 µm; as-welded >>25 µm. (These bands are practice-based; verify against supplier capability for the specific material/process.)
- Rule of thumb: if a process can hold a tight dimensional tolerance, it usually already delivers a comparatively fine finish; specifying a finer finish than the process naturally yields is what drives cost (extra grinding/polishing/honing).

### Gaps
- The Engineers Edge process-vs-Ra chart is an image not extracted here; exact per-process bands should be read from that chart or from a manufacturing handbook (e.g., Degarmo, "Materials and Processes in Manufacturing") for authoritative numbers.
- 3D-printed finish varies strongly by orientation, layer height, and post-processing; no single band is reliable—specify per-part and qualify with the supplier.

## How surface finish affects function: friction, wear, fatigue, corrosion, sealing, coating adhesion

### Takeaway
Roughness generally increases friction and wear, creates crack/corrosion nucleation sites, and can aid or hinder sealing and adhesion; controlled roughness is sometimes required (oil retention, gloss, grip). Most drawings set an upper roughness limit; cylinder bores need a minimum.

### Cited Findings
- In tribology, rough surfaces usually wear more quickly and have higher friction coefficients than smooth surfaces. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)
- Surface roughness is often a good predictor of mechanical component performance because irregularities can form nucleation sites for cracks or corrosion; conversely, roughness may promote adhesion. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)
- Surface texture controls friction and transfer-layer formation during sliding; textures can be isotropic or anisotropic; stick-slip can occur depending on texture. — [Wikipedia, Surface finish](https://en.wikipedia.org/wiki/Surface_finish)
- A surface with higher fractal dimension, larger Ra, or positive Rsk usually has somewhat higher friction and wears quickly; peaks are not always the contact points—form and waviness matter too. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)
- Roughness can be desirable: a gloss surface may be too shiny/slippery, so controlled roughness is required (e.g., touchpads); cylinder bores need minimum roughness to retain oil. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)
- In forming processes the die surface finish determines the workpiece surface finish; in machining, cutting edges and material microstructure both contribute. — [Wikipedia, Surface finish (Specification)](https://en.wikipedia.org/wiki/Surface_finish)

### Inferences
- Fatigue: surface finish enters endurance-limit calculations via a surface finish factor (often denoted k_a or k_s in machine-design texts such as Shigley). Ground/polished surfaces approach a factor near 1.0; as-forged/as-cast surfaces reduce the endurance limit substantially. The exact factor depends on tensile strength and process; use the Marin factor table from the applicable machine-design text and validate for the material. (Standard textbook knowledge; not URL-verified in this research set—flag as unverified.)
- Corrosion: smoother surfaces reduce crevice/pitting nucleation and are easier to clean/passivate; roughness can trap corrosive media and coating defects.
- Sealing: too rough leaks (asperity channels) and too smooth can stick/adhere; sealing surfaces need a controlled, often directional lay and a specified Rz/Ra (and sometimes Rsk/Rku) matched to the seal material and pressure.
- Coating/paint adhesion: moderate roughness (anchor profile) improves adhesion; excessive roughness causes coating thin spots/porosity. Specify a roughness range, not just a maximum, for coated parts.
- Friction/wear: for sliding contacts, lower Ra reduces friction and wear; for grip/handling, a minimum controlled roughness is specified.

### Gaps
- No sourced fatigue-factor table or corrosion/adhesion quantitative data found in this research set; these need machine-design handbooks (Shigley, Juvinall) and coating specs (e.g., SSPC/NACE) for numbers.

## Measurement methods: stylus profilometer, optical, comparison (Ra blocks)

### Takeaway
Contact (stylus) profilometers are the traditional standard method; non-contact optical methods (interferometry, confocal, focus variation, chromatic confocal) give high resolution without damage and are standardized under ISO 25178 for areal measurement. Ra comparison blocks give a quick shop-floor estimate.

### Cited Findings
- Surface finish may be measured by contact (stylus profilometer) or non-contact methods: interferometry, confocal microscopy, focus variation, structured light, electrical capacitance, electron microscopy, AFM, photogrammetry. — [Wikipedia, Surface finish (Measurement)](https://en.wikipedia.org/wiki/Surface_finish)
- Optical metrology (WLI, confocal microscopy, chromatic confocal sensing) gives nanometer-level vertical resolution and non-destructive analysis; chromatic confocal can produce Ra/Rz inline. — [Wikipedia, Surface finish (Non-contact methods)](https://en.wikipedia.org/wiki/Surface_finish)
- ISO 25178 Part 6 classifies measurement technologies into topographical, profilometric, and integration (pneumatic/capacitive/optical-diffusion) instruments; contact profilometers use a diamond stylus. — [Wikipedia, ISO 25178 (Instruments)](https://en.wikipedia.org/wiki/ISO_25178)
- ISO 4288 (cited in Engineers Edge references) establishes rules/procedures for assessment of surface texture, including precision reference specimens and roughness comparison specimens, and requirements for stylus-type instruments. — [Engineers Edge, surface roughness conversion (references)](http://www.engineersedge.com/manufacturing/surface-roughness-conversion.htm)
- Manual comparison against a "surface roughness comparator" (sample of known roughness) is a common quick method. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)

### Inferences
- Stylus profilometers measure a 2D line profile; they can damage soft surfaces and have limited lateral resolution compared to optical methods. Optical areal methods (ISO 25178) capture 3D surface data and compute Sa/Sq/etc.
- Comparison blocks (Ra blocks) are adequate for go/no-go shop checks but not for accepting critical surfaces; specify the measurement method and filter/cutoff in the drawing note when function depends on it.
- Cutoff length (sampling length) must match the process texture wavelength; the Engineers Edge table lists cut-off lengths per Ra band (e.g., 0.8 µm Ra → 0.03 in / 0.8 mm cutoff). Mismatched cutoffs produce misleading Ra values.

### Gaps
- No sourced detail on stylus tip radius, measurement force, or scan speed limits; consult ISO 3274 / ISO 4288 and instrument specs.

## Functional requirements: bearing surfaces, sealing surfaces, cosmetic, paint adhesion

### Takeaway
Different functions demand different roughness regimes: bearings need plateaued (negative skew) low roughness with oil retention; seals need a controlled mid-roughness with matched lay; cosmetic surfaces need low roughness plus gloss/color control; paint adhesion needs a controlled anchor profile (not too smooth, not too rough).

### Cited Findings
- Roughness plays a key role in contact mechanics (normal contact stiffness governed by asperity structure and material). — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)
- Most manufacturing prints establish an upper limit on roughness but not a lower limit, except cylinder bores where oil retention requires a minimum roughness. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)
- Controlled roughness is sometimes desirable (gloss too shiny/slippery); adhesion can be promoted by roughness. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)
- The Rk family of parameters is used mainly for cylinder bore linings (bearing surfaces). — [Wikipedia, Surface roughness (Profile roughness parameters)](https://en.wikipedia.org/wiki/Surface_roughness)

### Inferences
- Bearing surfaces: aim for low Ra with negative skew (plateau honing) and adequate oil-retention volume (Rk/Rpk/Rvk or V-parameters); avoid over-polishing that removes oil pockets.
- Sealing surfaces: specify a controlled Ra/Rz plus lay direction compatible with the seal; too smooth causes stick-slip/adhesion of seals, too rough leaks.
- Cosmetic surfaces: specify low Ra plus gloss/color/defect criteria; finishing (polishing, bead blast, anodize) often dominates cost; align with customer-facing surfaces only.
- Paint/coating adhesion: specify an anchor-profile roughness range (e.g., 2.5–6.3 µm Ra for many coatings) and verify with the coating supplier's spec; excessive roughness thins the film.

### Gaps
- No sourced numeric thresholds for sealing/paint/bearing applications found in this research set; use seal/coating manufacturer specs and industry standards (e.g., SAE, API, OEM) for acceptance criteria.

## DFM: specifying finish only where needed (cost), default finish for unmarked surfaces

### Takeaway
Cost rises as finish improves, and tight dimensional tolerances usually already imply fine finishes. Specify a coarse default finish for all unmarked surfaces and tighten only on functional/contact/sealing/cosmetic surfaces; avoid blanket fine finishes.

### Cited Findings
- In general, the cost of manufacturing a surface increases as surface finish improves. — [Wikipedia, Surface finish (Specification)](https://en.wikipedia.org/wiki/Surface_finish)
- Any given manufacturing process is usually optimized enough to ensure the resulting texture is usable; if necessary, an additional process modifies the initial texture, and its expense must be justified by better function or longer lifespan. — [Wikipedia, Surface finish (Specification)](https://en.wikipedia.org/wiki/Surface_finish)
- Parts with sliding contact may work better/last longer if roughness is lower; aesthetic improvement may add value if it improves saleability. — [Wikipedia, Surface finish (Specification)](https://en.wikipedia.org/wiki/Surface_finish)
- The practical example: milling can achieve ≤3.2 µm Ra with premium inserts and frequent changes, avoiding a second grinding/polishing operation, lowering unit cost. — [Wikipedia, Surface finish (Specification)](https://en.wikipedia.org/wiki/Surface_finish)
- Decreasing roughness usually increases manufacturing cost, creating a trade-off between cost and performance. — [Wikipedia, Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness)

### Inferences
- DFM checklist for an AI design assistant:
  1. Default note: "ALL UNMARKED SURFACES: 6.3 µm Ra MAX (or process-typical)" (or as-cast/as-forged default for cast/forged parts).
  2. Tighten finish only where function requires (mating, sealing, bearing, cosmetic, coating).
  3. Align finish with process capability—don't specify 0.4 µm Ra on an as-cast surface without a finishing operation.
  4. Prefer one process that achieves both tolerance and finish over adding grinding/polishing.
  5. Specify lay direction where it affects sealing/friction; leave non-functional surfaces with default lay.
  6. Use N-grade numbers or Ra with units (µm/µin) consistently; state the measurement method/cutoff when critical.
  7. For coated parts, specify an anchor-profile range rather than a single max.
- Default finishes by base process (practice): as-cast/as-forged parts default to as-cast/as-forged roughness; machined parts default to 3.2–6.3 µm Ra; sheet-metal parts default to mill finish.

### Gaps
- No sourced recommended default-finish values by industry; defaults are company/OEM standards—flag as convention, not standard.
```

Let me write this file.<|end|><|start|>assandra<|channel|> to=write<|channel|>analysis <|constrain|>xml<|message|><rfl:parameter name="path">
C:\Users\malliath\Desktop\CADResearch\research_notes\Senior CAD engineer knowledge\surface_finish.md