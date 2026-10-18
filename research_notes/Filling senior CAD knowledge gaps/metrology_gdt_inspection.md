# Metrology and GD&T Inspection for Mechanical Engineering

## 1. Measurement Tools: Calipers, Micrometers, Dial Indicators, Height Gauges, Bore Gauges, Thread Gauges, Feeler Gauges, Go/No-Go Gauges

### Takeaway
Handheld and bench metrology tools cover the vast majority of shop-floor dimensional checks; each has a defined accuracy envelope, and choosing the right tool (and not over-claiming its accuracy) is the first defense against bad inspection data.

### Cited Findings
- Calipers (vernier, dial, digital) are general-purpose comparative length instruments; the Wikipedia "Calipers" entry is linked from the CMM article's measuring-tool list — [Wikipedia: Coordinate-measuring machine (measuring tools list)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Micrometers (device) are referenced in the same measuring-tool index as the standard instrument for precise small-dimension measurement — [Wikipedia: Micrometer (device)](https://en.wikipedia.org/wiki/Micrometer_(device)).
- Feeler gauge is listed among measuring and alignment tools used to measure small clearances/gaps — [Wikipedia: Feeler gauge](https://en.wikipedia.org/wiki/Feeler_gauge).
- Thread pitch gauge is listed as the tool for verifying thread pitch — [Wikipedia: Thread pitch gauge](https://en.wikipedia.org/wiki/Thread_pitch_gauge).
- Go/no-go gauge is cited in the First Article Inspection article as a standard calibrated tool for dimensional inspection — [Wikipedia: First article inspection](https://en.wikipedia.org/wiki/First_article_inspection).
- ASME Y14.5 Rule 12 states dimensions and tolerances are valid at 20 °C (68 °F) and 101.3 kPa (14.69 psi) unless stated otherwise — [Wikipedia: Geometric dimensioning and tolerancing (Purpose and rules)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ASME Y14.5 Rule 13: unless explicitly stated, dimensions and tolerances apply only in a free-state condition — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).

### Inferences
- Hand tools (calipers ~0.02–0.05 mm, micrometers ~0.001–0.005 mm typical) are appropriate for ±tolerance verification only when their uncertainty is < ~10–20 % of the tolerance; for tight GD&T features, CMM is required.
- Free-state requirement (Rule 13) means clamping/fixturing can invalidate a measurement unless the drawing specifies a restrained condition.

### Gaps
- Specific accuracy/resolution figures for each tool type (e.g., dial indicator least count, bore gauge range) were not sourced; rely on manufacturer datasheets and standards such as ASME B89.1 (not retrieved here).

## 2. CMM (Coordinate Measuring Machine): Types, Probing, Programming, Accuracy, Uncertainty

### Takeaway
CMMs measure point clouds in a 3D Cartesian frame; accuracy is expressed as a length-dependent uncertainty (ISO 10360), and modern machines use touch-trigger or scanning probes with DCC programming.

### Cited Findings
- A CMM senses discrete points on a part surface with a probe and reports position in XYZ Cartesian coordinates; points form a point cloud describing surfaces of interest — [Wikipedia: Coordinate-measuring machine (Description)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Bridge (gantry) CMM: superstructure has two legs (inside/outside) moving along a granite table on air bearings; carriage traverses between legs (Y), quill provides Z — [Wikipedia: Coordinate-measuring machine (Machine body)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- First CMM developed by Ferranti (Scotland, 1950s), 2-axis; 3-axis models in 1960s (DEA, LK); computer control in early 1970s; Brown & Sharpe produced first working CMM for sale — [Wikipedia: Coordinate-measuring machine](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Portable CMMs: articulated arms with 6–7 rotary-encoded axes; lighter, usable in uncontrolled environments, but somewhat less accurate than bridge CMMs — [Wikipedia: Coordinate-measuring machine (Portable)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Multisensor machines combine touch probes with laser, video, or white-light sensors — [Wikipedia: Coordinate-measuring machine (Multisensor)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Touch-trigger probe (Renishaw, David McMurtry) sends X,Y,Z coordinate on contact; electronic trigger reduced operator-dependent pressure errors and enabled CNC/DCC — [Wikipedia: Coordinate-measuring machine (Mechanical probe)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Scanning probes drag along surface taking points at intervals; typically more accurate and faster than touch-trigger; noncontact laser/white-light scanning produces point clouds for 3D models/reverse engineering — [Wikipedia: Coordinate-measuring machine (Scanning probe systems)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Typical probe repeatability within one micron (0.00005 in) over the entire measurement volume for touch-probe CMMs — [Wikipedia: Coordinate-measuring machine (Accuracy)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Accuracy given as uncertainty factor as a function of distance; probes calibrated with traceable standards; movement verified with gauges — [Wikipedia: Coordinate-measuring machine (Accuracy)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- ISO 10360 series verifies CMM performance: PForm (probing deviation measuring form of a sphere), PSize (probing deviation measuring size of a sphere), EUni (length measurement deviation on spheres from one direction), EBi (length measurement deviation on spheres from left and right) — [Wikipedia: Coordinate-measuring machine (Standardization)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- ISO 10360 parts: -1 Vocabulary; -2 CMMs used for measuring linear dimensions; -7 CMMs with imaging probing systems; -8 CMMs with optical distance sensors — [Wikipedia: Coordinate-measuring machine (Standardization)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Machine frames now use granite, aluminum alloy, ceramic, black granite, silicon carbide for stiffness; air bearings for friction-free travel — [Wikipedia: Coordinate-measuring machine (Parts)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Micro/nano-scale probing challenges: high-aspect-ratio probes, low contact forces, environmental sensitivity (humidity, stiction) — [Wikipedia: Coordinate-measuring machine](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).

### Inferences
- For an AI design assistant: recommend CMM for any GD&T feature (position, profile, runout) where tolerance < ~0.05 mm or where datum-derived measurement is required; hand tools only for simple size checks.
- Bridge CMMs are the lab standard; portable arms trade accuracy for accessibility (large parts, in-situ).

### Gaps
- Programming details (DMIS, PC-DMIS), specific accuracy classes (e.g., ISO 10360-2 E values), and temperature compensation software internals were not sourced.

## 3. GD&T Inspection: Measuring Position, Flatness, Perpendicularity, Runout, Profile; Datum Establishment on CMM; True Position Calculation

### Takeaway
GD&T inspection constructs geometric features from point clouds and evaluates them against datum reference frames; true position is computed as a diametric deviation from basic (theoretically exact) dimensions.

### Cited Findings
- GD&T is a symbolic language on drawings/3D models defining nominal geometry and permissible variation in form, orientation, location, and size; tolerances via feature control frames — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- A datum is a theoretically exact plane, line, point, or axis; datum feature is a physical feature identified by a datum feature symbol — [Wikipedia: Geometric dimensioning and tolerancing (Datums)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ASME Y14.5 Rule 12: dimensions/tolerances valid at 20 °C unless stated otherwise; Rule 13: free-state condition unless stated otherwise — [Wikipedia: Geometric dimensioning and tolerancing (Purpose and rules)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Geometric characteristics table (ASME Y14.5): Form (straightness, flatness, circularity, cylindricity); Profile (profile of a line, profile of a surface); Orientation (perpendicularity, angularity, parallelism); Location (position, concentricity, symmetry); Runout (circular runout, total runout) — [Wikipedia: Geometric dimensioning and tolerancing (Symbols)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Position tolerance (⌖) is a location control applied only to features of size; tolerance zone is cylindrical (with Ø) or two parallel planes (without Ø) — [Wikipedia: Position tolerance](https://en.wikipedia.org/wiki/Position_tolerance); [GD&T Basics: True Position](https://www.gdandtbasics.com/true-position/).
- True position is the exact coordinate defined by basic dimensions; actual position deviation computed from measured X/Y (or X/Y/Z) offsets: diametric deviation = 2 × sqrt(ΔX² + ΔY²) — [GD&T Basics: True Position](https://www.gdandtbasics.com/true-position/).
- Example: measured offsets 0.003 in X and 0.002 in Y → diametric deviation 0.007 in; compare to stated 0.008 in tolerance → pass — [GD&T Basics: True Position](https://www.gdandtbasics.com/true-position/).
- Position with MMC allows bonus tolerance: bonus = measured hole size − MMC hole size (for holes); gage Ø (pin gage) = Min Ø of hole (MMC) − true position tolerance — [GD&T Basics: True Position](https://www.gdandtbasics.com/true-position/).
- Flatness is a form control with no datum reference; measured as deviation of surface points from a best-fit plane (min-max) — [Wikipedia: Geometric dimensioning and tolerancing (Symbols)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Perpendicularity is an orientation control requiring a datum; controls axis/plane at 90° to datum; can be combined with position — [GD&T Basics: True Position](https://www.gdandtbasics.com/true-position/); [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Runout (circular/total) is measured with a dial indicator on a rotating part relative to a datum axis — [Wikipedia: Geometric dimensioning and tolerancing (Symbols)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Profile of a surface/line controls form, orientation, location of surfaces; can be used without datum as form control — [Wikipedia: Geometric dimensioning and tolerancing (Symbols)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Datum establishment on CMM: construct primary datum plane (least-squares or min-max) from point cloud, then secondary/tertiary datums; datum reference frame locates true position via basic dimensions — inferred from GD&T principles; [GD&T Basics: True Position](https://www.gdandtbasics.com/true-position/).
- Position with a single datum effectively acts as perpendicularity; composite feature control frames separate pattern location from feature-to-feature relation — [GD&T Basics comments](https://www.gdandtbasics.com/true-position/).

### Inferences
- On a CMM, always measure datums first and establish the datum reference frame before evaluating position/profile; evaluating position in part coordinates without datum alignment is a common error.
- For cylindrical features, take multiple points along depth to capture orientation/tilt, not just a single cross-section.

### Gaps
- Specific CMM datum algorithms (least-squares vs. minimum zone/ISO 1101), filtering, and measurement strategy (point density) were not sourced from primary standards here.

## 4. Surface Finish Measurement: Stylus Profilometer (Ra, Rz), Optical Methods, Comparison Blocks, Cutoff Lengths

### Takeaway
Surface roughness is the high-frequency component of surface texture; Ra (arithmetic average) is the most common parameter, measured with stylus or optical profilometers under ISO 4287/4288 rules with defined cutoff lengths; comparison blocks give a quick shop-floor check.

### Cited Findings
- Surface roughness quantifies deviations normal to the ideal surface; roughness is the high-frequency, short-wavelength component — [Wikipedia: Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness).
- Ra = (1/lr) ∫ |z(x)| dx, the arithmetic average of absolute deviations from the mean line over evaluation length — [Wikipedia: Surface roughness (Amplitude parameters)](https://en.wikipedia.org/wiki/Surface_roughness).
- Rz = average of (Rp_i + Rv_i) over n sampling lengths; Rq = RMS average; Rsk (skewness), Rku (kurtosis) — [Wikipedia: Surface roughness (Amplitude parameters)](https://en.wikipedia.org/wiki/Surface_roughness).
- Rz JIS based on five highest peaks/valleys; Rz DIN = average Rt over sampling lengths — [Wikipedia: Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness).
- ISO grade numbers N1–N12 map Ra from 0.025 µm (N1) to 50 µm (N12) (table) — [Wikipedia: Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness).
- Profile parameters standardized in BS EN ISO 4287:2000 (= ISO 4287:1997), "M" (mean line) system; ISO 4288 governs rules/procedures for assessment — [Wikipedia: Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness); [Wikipedia: Geometric dimensioning and tolerancing (ISO standards list)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Areal parameters (Sa, Sq, Sz) per ISO 25178; optical instruments measure over an area; contact systems can stitch multiple 2D scans — [Wikipedia: Surface roughness (Areal)](https://en.wikipedia.org/wiki/Surface_roughness).
- Stylus (diamond tip) contact profilometers and optical methods (white-light interferometer, laser scanning confocal microscope) both used; comparison blocks for manual comparison — [Wikipedia: Surface roughness (Role and effect)](https://en.wikipedia.org/wiki/Surface_roughness).
- ASME B46.1 is the US standard for surface texture (roughness, waviness, lay) — [Wikipedia: Surface roughness (References)](https://en.wikipedia.org/wiki/Surface_roughness).
- ISO 3274 covers nominal characteristics of contact (stylus) instruments; ISO 1302 covers indication of surface texture on drawings — [Wikipedia: Geometric dimensioning and tolerancing (ISO standards)](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).

### Inferences
- Cutoff length selection (e.g., 0.8 mm vs 2.5 mm) must match the expected roughness and instrument; wrong cutoff changes Ra significantly. (Specific cutoff values per ISO 4288 not retrieved — see Gaps.)
- Most manufacturing prints set an upper limit on Ra; cylinder bores may require a minimum roughness for oil retention.

### Gaps
- Exact cutoff lengths (λc) and evaluation lengths per ISO 4288 for each Ra range were not retrieved. Comparison-block grades and optical-method resolution limits not detailed here.

## 5. Dimensional Tolerancing: Verifying ISO 286 Fits, Tolerance Stack-Up Verification

### Takeaway
ISO 286 (limits and fits) defines hole/shaft tolerance codes (e.g., H7/h6); verification computes actual clearance/interference from measured sizes; stack-up checks ensure assembly.

### Cited Findings
- Engineering fits grouped into clearance, transition (location), and interference; ISO is the international standard, ANSI still used in North America — [Wikipedia: Engineering fit](https://en.wikipedia.org/wiki/Engineering_fit).
- Hole-basis vs. shaft-basis: hole size held constant (H) and shaft varied, or vice versa — [Wikipedia: Engineering fit (Hole and shaft basis)](https://en.wikipedia.org/wiki/Engineering_fit).
- ISO alpha-numeric code: uppercase = hole tolerance, lowercase = shaft tolerance; e.g., H7/h6; potential clearance = largest hole − smallest shaft (and smallest hole − largest shaft) — [Wikipedia: Engineering fit](https://en.wikipedia.org/wiki/Engineering_fit).
- Clearance fits: H11/c11 (loose running) through H7/h6 (location/clearance) with example: H8/f7 on 50 mm → clearance +0.025 to +0.089 mm — [Wikipedia: Engineering fit (Clearance fits)](https://en.wikipedia.org/wiki/Engineering_fit).
- Transition fits: H7/k6 (similar) and H7/n6 (fixed) — [Wikipedia: Engineering fit (Transition fits)](https://en.wikipedia.org/wiki/Engineering_fit).
- Interference fits: H7/p6 (press), H7/s6 (driving), H7/u6 (forced) — [Wikipedia: Engineering fit (Interference fits)](https://en.wikipedia.org/wiki/Engineering_fit).
- ANSI RC (running/clearance) fits RC1–RC9 with descriptions — [Wikipedia: Engineering fit (RC fits)](https://en.wikipedia.org/wiki/Engineering_fit).
- Common tolerance table for 0–120 mm (H7, h6, etc.) — [Wikipedia: Engineering fit (Useful tolerances)](https://en.wikipedia.org/wiki/Engineering_fit).
- ASME Y14.5 Rule 1: all dimensions must have a tolerance; Rule 2: dimensions and tolerancing fully define each feature — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).

### Inferences
- Verification of an ISO fit: measure hole and shaft, compute min/max clearance; compare to the fit's specified clearance/interference range; a single part failing either bound is nonconforming.
- Tolerance stack-up (worst-case or RSS) is not detailed in retrieved sources; rely on standard mechanical design references (not sourced here).

### Gaps
- ISO 286 standard document itself and RSS/worst-case stack-up methods were not retrieved; NIST/ASME guidelines on stack-up not found.

## 6. Measurement Uncertainty: GUM, Type A/B, Expanded Uncertainty

### Takeaway
GUM (JCGM 100) defines measurement uncertainty via probability distributions of input quantities propagated through a measurement model; Type A (statistical) and Type B (other information) evaluations combine into standard uncertainty, then expanded uncertainty via coverage factor k (typically 2 for ~95 %).

### Cited Findings
- Measurement uncertainty is the statistical dispersion of values attributed to a measured quantity; a result is complete only with its uncertainty — [Wikipedia: Measurement uncertainty](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- GUM (Guide to the Expression of Uncertainty in Measurement, JCGM 100:2008) is the definitive document; adopted by NMIs and ISO/IEC 17025 — [Wikipedia: Measurement uncertainty (Background)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- Measurement model Y = f(X₁,…,X_N); input quantities characterized by probability distributions; estimates x_i with standard uncertainties u(x_i) — [Wikipedia: Measurement uncertainty (Indirect measurement)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- Type A evaluation: from repeated measured values (Gaussian or t-distribution for small samples) — [Wikipedia: Measurement uncertainty (Type A and Type B)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- Type B evaluation: from scientific judgement/other information; if only an interval [a,b] is known, use rectangular distribution — [Wikipedia: Measurement uncertainty (Type A and Type B)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- Sensitivity coefficients c_i = ∂f/∂X_i; law of propagation of uncertainty: u²(y) = Σ c_i² u²(x_i) (plus covariance terms) — [Wikipedia: Measurement uncertainty (Sensitivity coefficients)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- Uncertainty evaluation stages: formulation (define measurand, inputs, model, distributions) and calculation (propagation + summarizing: estimate, standard uncertainty, coverage interval) — [Wikipedia: Measurement uncertainty (Uncertainty evaluation)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- Propagation approaches: GUM framework (law of propagation, Gaussian/t), analytic methods, Monte Carlo (JCGM 101) — [Wikipedia: Measurement uncertainty (Uncertainty evaluation)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- Coverage interval with specified coverage probability; expanded uncertainty U = k·u_c (k≈2 for ~95 %) — implied by standard GUM practice; [Wikipedia: Measurement uncertainty](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- ASME B89.7.3.1 (decision rules for conformance), B89.7.3.2 (evaluation of dimensional measurement uncertainty), B89.7.3.3 (reliability of uncertainty statements), B89.7.4 (uncertainty and conformance testing risk analysis) — [Wikipedia: Measurement uncertainty (Background)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- JCGM 101 (Monte Carlo), JCGM 102 (multivariate), JCGM 104 (introduction), JCGM 106 (uncertainty in conformity assessment), JCGM 200 (VIM) — [Wikipedia: Measurement uncertainty (References/External links)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- NIST uncertainty guidelines referenced — [Wikipedia: Measurement uncertainty (External links)](https://en.wikipedia.org/wiki/Measurement_uncertainty).

### Inferences
- For CMM inspection, combine probe repeatability (Type A, from repeated measurements) with scale accuracy, temperature, and probing force (Type B) into combined standard uncertainty; report expanded uncertainty with k=2.

### Gaps
- Specific coverage-factor tables, guard-banding/decision rules (ASME B89.7.3.1 details), and example uncertainty budgets for CMMs were not retrieved.

## 7. Inspection Plans: First Article Inspection (FAI), In-Process Inspection, Final Inspection, Sampling Plans (AQL)

### Takeaway
FAI validates a new/changed process by fully inspecting the first part; in-process and final inspections use defined sampling (AQL tables) to balance risk and cost.

### Cited Findings
- First Article Inspection (FAI): production validation process verifying that a new or modified process produces conforming parts meeting the drawing spec; typically the supplier performs and the purchaser reviews; may use CMMs, calipers, go/no-go gauges, material tests — [Wikipedia: First article inspection](https://en.wikipedia.org/wiki/First_article_inspection).
- FAI can fulfill process validation for QMS (ISO 9001, EN 9100, AS 9100); aerospace uses SAE AS9102 (Forms 1/2/3), part of AS 9145 APQP/PPAP — [Wikipedia: First article inspection](https://en.wikipedia.org/wiki/First_article_inspection).
- FAI purposes: verify drawing accuracy, verify every production parameter, verify tooling capability, verify manufacturer's ability to meet production needs — [Wikipedia: First article inspection (Type)](https://en.wikipedia.org/wiki/First_article_inspection).
- Acceptable Quality Limit (AQL): worst tolerable process average (in % or ratio) still acceptable; inspection standard prescribing range of defective components acceptable in random sampling; defects classified critical/major/minor — [Wikipedia: Acceptable quality limit](https://en.wikipedia.org/wiki/Acceptable_quality_limit).
- AQL terminology shifted from "acceptable quality level" to "acceptance quality level" (ANSI/ASQ Z1.4-2008 Sampling Procedures and Tables for Inspection by Attributes) — [Wikipedia: Acceptable quality limit](https://en.wikipedia.org/wiki/Acceptable_quality_limit).
- RQL (rejectable quality limit/level) is the complementary term — [Wikipedia: Acceptable quality limit](https://en.wikipedia.org/wiki/Acceptable_quality_limit).

### Inferences
- For an AI design assistant: recommend FAI on first production run and after any process/tooling/drawing change; use AQL sampling for lot acceptance in production; 100 % inspection for safety-critical features.

### Gaps
- Specific AQL table values (sample sizes, accept/reject numbers), ISO 2859 parts, and in-process vs. final inspection criteria were not retrieved.

## 8. Common Pitfalls: Wrong Datum, Temperature Effects, Clamping Deformation, Dirty Surfaces

### Takeaway
Most inspection failures are process errors, not part errors: wrong datum alignment, temperature drift, clamping distortion, and contamination can all produce false rejects (or false accepts).

### Cited Findings
- ASME Y14.5 Rule 12: dimensions/tolerances valid at 20 °C (68 °F); temperature deviations require correction — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ASME Y14.5 Rule 13: free-state condition unless stated otherwise; clamping/restraining changes form unless a restrained condition is specified — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Measurement uncertainty includes systematic errors from instrument alignment and ambient temperature differing from stipulated conditions; correction terms should be included in the measurement model — [Wikipedia: Measurement uncertainty (Indirect measurement)](https://en.wikipedia.org/wiki/Measurement_uncertainty).
- CMM measurement is sensitive to environment; portable CMMs usable in uncontrolled environments but less accurate — [Wikipedia: Coordinate-measuring machine (Portable)](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Micro-scale probing susceptible to humidity and surface interactions (stiction) — [Wikipedia: Coordinate-measuring machine](https://en.wikipedia.org/wiki/Coordinate-measuring_machine).
- Surface roughness measurement depends on filtering, mean-line calculation, and measurement physics; small changes greatly affect calculated parameters — [Wikipedia: Surface roughness](https://en.wikipedia.org/wiki/Surface_roughness).
- GD&T position inspection requires correct datum reference frame; measuring in part coordinates without datum alignment is wrong — [GD&T Basics: True Position](https://www.gdandtbasics.com/true-position/).

### Inferences
- Always clean parts before inspection (chips, oil, coolant) to avoid false point-cloud outliers on CMM and stylus damage on profilometers.
- Use thermal soak to 20 °C; for large parts or tight tolerances, apply temperature correction.
- Minimize clamping force; use free-state fixtures; if restrained condition is specified, document the restraint.

### Gaps
- Quantitative temperature-expansion coefficients, recommended clamping forces, and cleaning procedures were not sourced; rely on shop practice and standards (e.g., ISO 1) not retrieved.
`;
write({path: "C:\\Users\\malliath\\Desktop\\CADResearch\\research_notes\\Filling senior CAD knowledge gaps\\metrology_gdt_inspection.md", content});