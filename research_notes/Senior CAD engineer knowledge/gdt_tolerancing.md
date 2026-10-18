# GD&T and Tolerance Analysis for Mechanical Design

## Q1: What are the 14 GD&T symbols and their categories?

### Takeaway
ASME Y14.5-2009 defines 14 geometric characteristics in five categories (form, orientation, location, profile, runout); Y14.5-2018 withdrew concentricity and symmetry, leaving 12. ISO 1101 retains all of them.

### Cited Findings
- The 14 characteristics grouped into five categories: Form (straightness, flatness, circularity, cylindricity); Orientation (angularity, perpendicularity, parallelism); Location (position, concentricity, symmetry); Profile (profile of a line, profile of a surface); Runout (circular runout, total runout) — [GD&T Basics, "The ASME Y14.5 GD&T Standard"](https://www.gdandtbasics.com/asme-y14-5-gdt-standard/).
- "ASME Y14.5-2009 and earlier define 14 geometric characteristics in five groups... Y14.5-2018 withdrew concentricity and symmetry, leaving 12, but both still turn up on older drawings and in ISO 1101" — [NORAMARK GD&T Symbols Chart](https://www.noramark.com/resources/charts/gdt-symbols/).
- "In the 2018 revision, both concentricity and symmetry were eliminated and are no longer supported" — [Wikipedia, "Geometric dimensioning and tolerancing"](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Form controls never reference a datum; orientation and runout always require one; location usually requires one; profile's datum use is optional — [GD&T Basics](https://www.gdandtbasics.com/asme-y14-5-gdt-standard/) and [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Only position, straightness (axis), and orientation controls (angularity, perpendicularity, parallelism) can take MMC/LMC modifiers; profile, runout, concentricity, symmetry cannot (RFS only) — [GD&T Basics MMC page](https://www.gdandtbasics.com/maximum-material-condition/).

### Inferences
- For new designs, replace concentricity/symmetry with position or runout; legacy drawings invoking 2009 or ISO may still use them.
- An AI generating drawings should default to the 12-characteristic 2018 set unless the drawing header invokes 2009/ISO.

### Gaps
- Exact Unicode/ASCII art symbol rendering for each characteristic is not reproduced here; use standard symbol fonts (GD&T font) in CAD.

## Q2: What are the 5 tolerance types (size, form, orientation, location, runout) and how do they interact?

### Takeaway
The five tolerance types build in increasing constraint: size (limits) → form → orientation → location → runout; each higher type implies the lower ones in some cases (e.g., position implies orientation/location; runout implies form+orientation).

### Cited Findings
- Y14.5 sections: Section 5 Form (straightness, flatness, circularity, cylindricity); Section 6 Orientation (angularity, perpendicularity, parallelism); Section 7 Location (position, concentricity, symmetry); Section 8 Profile (line/surface); Section 9 Runout (circular/total) — [GD&T Basics](https://www.gdandtbasics.com/asme-y14-5-gdt-standard/).
- "Orientation tolerances are used to control rotation of a feature relative to a datum. They cannot be used to control location." — [GD&T Basics](https://www.gdandtbasics.com/asme-y14-5-gdt-standard/).
- "Profile tolerances can control size, form, orientation, and/or location" depending on datums referenced — [GD&T Basics](https://www.gdandtbasics.com/asme-y14-5-gdt-standard/).
- "Runout is a tolerance used to control variation in a surface when it is rotated about a datum axis... circular runout applies to a single surface; total runout applies to all surfaces with rotational symmetry" — [GD&T Basics](https://www.gdandtbasics.com/asme-y14-5-gdt-standard/).
- Rule #1 (Envelope Principle): size tolerance also controls form by default (perfect form at MMC) unless independency is specified — [GD&T Basics MMC page](https://www.gdandtbasics.com/maximum-material-condition/).

### Inferences
- Applying a form tolerance (e.g., flatness) on a surface already sized does not locate it; pair with position/profile for location.
- Profile of a surface is the most versatile single control because it can subsume form+orientation+location.

### Gaps
- ISO's "independency principle" vs ASME Rule #1 nuance (ISO 8015 default independency) not fully detailed here; flagged.

## Q3: ASME Y14.5 vs ISO GPS

### Takeaway
ASME Y14.5 is a single self-contained document (four editions: 1982, 1994, 2009, 2018); ISO GPS is a family of standards (ISO 1101, 128, 2768, 8015, 14405, 286, etc.) under ISO/TC 213, with fundamental differences: envelope (ASME default) vs independency (ISO default), and ISO uses "maximum/least material requirement" (MMR/LMR) rather than MMC/LMC.

### Cited Findings
- "There are two main standards... ISO publishes GPS Standards, ASME publishes Y14.5... ISO standards typically only address a single topic at a time" — [Wikipedia GD&T](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ISO GPS masterplan TR 14638 distinguishes fundamental/global/general/complementary GPS standards; ISO 8015 = "Concepts, principles and rules" (fundamental) — [Wikipedia GD&T](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ISO GPS list includes ISO 1101 (geometrical tolerancing), ISO 5459 (datums), ISO 2692 (MMR/LMR/RPR), ISO 14406 (extraction), ISO 128 (technical product documentation), ISO 129 (dimensions/tolerances) — [Wikipedia GD&T](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ASME Y14.5 editions: 1982 (ANSI Y14.5M), 1994 (ASME Y14.5M), 2009, 2018; "2009 version is the most widely used" — [GD&T Basics](https://www.gdandtbasics.com/asme-y14-5-gdt-standard/).
- ISO 16792:2021 digital product definition derived from ASME Y14.41 by permission — [Wikipedia GD&T](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ISO uses MMR/LMR/RPR (ISO 2692) instead of MMC/LMC; ISO envelope requirement indicated by circled E (Ⓔ) symbol (ISO-only) — [GD&T Basics MMC page footer (Envelope Requirement ISO Only)](https://www.gdandtbasics.com/maximum-material-condition/).

### Inferences
- A drawing must declare which standard governs (title block note "ASME Y14.5-2018" or "ISO GPS"); mixing defaults leads to misinterpretation.
- ISO default = independency (size and form independent) unless envelope symbol Ⓔ applied; ASME default = envelope (Rule #1) unless independency noted.

### Gaps
- Detailed ISO 14405 (dimensional tolerancing) and ISO 14406 (extraction) specifics not sourced; flagged as unverified here.

## Q4: Standard fits and ISO 286

### Takeaway
ISO 286 defines hole-basis (H) and shaft-basis (h) systems; preferred fits range from H11/c11 (loose running) through H7/g6 (sliding), H7/h6 (locational clearance), H7/k6 and H7/n6 (transition), to H7/p6, H7/s6, H7/u6 (interference). Select by function: clearance for motion, transition for location, interference for torque/press.

### Cited Findings
- Preferred fits table (ISO 286 / ANSI B4.2): H11/c11 loose running; H9/d9 free running; H8/f7 close running; H7/g6 sliding; H7/h6 locational clearance; H7/k6 locational transition; H7/n6 locational transition (more interference); H7/p6 locational interference; H7/s6 medium drive; H7/u6 force fit — [Engineers Edge preferred tolerances](https://www.engineersedge.com/manufacturing/preferred_mechanical_tolerances_metric_iso_286_13166.htm) and [EICAC limits/fits table](https://eicac.co.uk/limits-fits-and-tolerances/).
- "Hole-basis fit system: fits where the fundamental deviation of the hole is zero (lower limit deviation zero); shaft-basis: fundamental deviation of shaft is zero" — [E3S Conf paper on ISO 286 fits](https://doi.org/10.1051/e3sconf/202340210033).
- "Preference is given to the hole system, since it is usually much more difficult and expensive to make and measure a hole than a shaft" — [E3S Conf paper](https://doi.org/10.1051/e3sconf/202340210033).
- H7/g6 at Ø25 mm gives 7–41 µm diametral clearance; H7/k6 gives -15 to +19 µm (transition); H7/p6 gives -35 to -1 µm (interference) — [calcengines ISO 286 fit calculator](https://calcengines.com/mechanical/fits-tolerances/iso-286-fit-calculator/).
- "A transition fit can end up as either clearance or interference... H7/k6 and H7/n6 are both like this" — [NovaSolver ISO fit selector](https://novasolver.jp/en/tools/iso-fit-selector.html).
- "If the minimum clearance is 0 or more → clearance fit; if the maximum clearance is 0 or less → interference fit; in between → transition fit" — [NovaSolver](https://novasolver.jp/en/tools/iso-fit-selector.html).

### Inferences
- For an AI generating drawings: default to hole-basis H7 for bores and vary shaft letter (g6/k6/n6/p6/s6/u6) by function; use h6 shaft basis only when shaft is the constrained feature (e.g., dowel pins).
- Transition fits cannot guarantee motion or torque; use clearance or interference respectively.

### Gaps
- Full ISO 286 deviation tables (IT grades 01–18) and shaft-basis preferred fits not reproduced; calculator sources cited.

## Q5: Tolerance stack-up methods

### Takeaway
Four methods: worst-case (arithmetic, 100% coverage, conservative, costly), RSS/statistical (normal distribution, ~99.73% at ±3σ, assumes independence), Monte Carlo (handles non-linear/non-normal/complex), and statistical tolerancing with mean shifts. Choose by production volume, criticality, and distribution knowledge.

### Cited Findings
- Worst-case: "calculates maximum deviation from sum of variations"; "often lead to costly reductions in specified tolerance values"; use for safety-critical failure modes — [Enventive tolerance analysis](https://enventive.com/tolerance-analysis-resources/worst-case-rss-and-monte-carlo-simulation-calculations-for-tolerance-analysis/).
- RSS: "assumes normal (Gaussian) distribution"; "assumes linearity of geometries"; "most commonly used" for rapid iterative decision making — [Enventive](https://enventive.com/tolerance-analysis-resources/worst-case-rss-and-monte-carlo-simulation-calculations-for-tolerance-analysis/).
- RSS formula: T_assy = sqrt(T1²+T2²+...+Tn²) (when sensitivities = ±1); assumes centered normal with ±3σ = tolerance span and independent variation — [Scholz tolerance stacking report](https://faculty.washington.edu/fscholz/Reports/isstech-95-030.pdf).
- Monte Carlo: uses random sampling from distributions; suited to non-linear surfaces, non-normal distributions, changing contact points; slower but more accurate — [Enventive](https://enventive.com/tolerance-analysis-resources/worst-case-rss-and-monte-carlo-simulation-calculations-for-tolerance-analysis/).
- RSS guarantees 99.73% of products within limits (0.27% fallout) at ±3σ; Monte Carlo needed when Y=F(X) is non-normal — [ASQ presentation via static.prod01](https://static.prod01.ue1.p.pcomm.net/communityasq/user_content/forums/topics/files/6734/b4cbb407b039c11ae39fd8f51839940e-asq_rss_mc_presentation_march_16_2023.pdf).
- Statistical tolerancing symbol (ST) on drawings indicates SPC-monitored tolerances — [Scholz report](https://faculty.washington.edu/fscholz/Reports/isstech-95-030.pdf).

### Inferences
- For high-volume production with capable processes, RSS reduces cost; for safety-critical or low-volume, use worst-case.
- An AI should flag when a stack-up involves identical parts from one process (mean-shift risk) or thermal expansion (violates independence).

### Gaps
- Monte Carlo iteration count guidance (3M cited) and convergence criteria not fully sourced; flagged.

## Q6: Datum reference frames and how they work

### Takeaway
A DRF is a Cartesian coordinate system (3 mutually perpendicular planes) that constrains a part's 6 degrees of freedom (3 translations + 3 rotations) via datum features in primary/secondary/tertiary order (3-2-1 principle); basic dimensions then orient/locate tolerance zones relative to it.

### Cited Findings
- "A datum is a theoretically exact point, line, or plane"; "Without a datum reference, a part can move in three spatial directions or rotate about three different axes... six degrees of freedom" — [GD&T Basics](https://www.gdandtbasics.com/asme-y14-5-gdt-standard/).
- 3-2-1 principle: primary datum constrains 3 DOF (1 translation + 2 rotations) via 3-point contact; secondary constrains 2 DOF (1 translation + 1 rotation) via 2-point contact; tertiary constrains 1 DOF (1 translation) via 1-point contact — [OpenExamPrep ASME GDTP guide](https://open-exam-prep.com/study-guides/asme-gdtp-technologist/ch4/dof-and-321-principle).
- "Datum Feature Simulators serve as bridges between the imperfect real world of datum features and the perfect imaginary world of datums" — [Quality Magazine DRF workshop](https://www.qualitymag.com/articles/88829-gd-t-workshop-establishing-datum-reference-frames).
- DRF construction steps: decode FCF → identify datum features → construct simulators → extract datums → constrain starter coordinate system → marry features to simulators — [Quality Magazine DRF construction](https://www.qualitymag.com/articles/88854-gd-t-workshop-the-drf-construction-process).
- Datum precedence rules: datum features used in order appearing in FCF (left to right); degrees of constraint precedence (pitch/yaw → roll → translation); non-override; can-may-must (maximum utilization) — [Quality Magazine DRF construction](https://www.qualitymag.com/articles/88854-gd-t-workshop-the-drf-construction-process).
- Planar datum controls 2 rotations + 1 translation at max; cylindrical datum controls 2 rotations + 2 translations at max — [Berez fundamentals](https://doi.org/10.5281/zenodo.7647256).
- ASME focuses on degrees-of-freedom constrained; ISO focuses on rigid motions keeping surface invariant (complementary views) — [ASME J. of Manufacturing Science paper](https://doi.org/10.1115/1.4054304).

### Inferences
- Functional datums (mating surfaces) should be primary; arbitrary machined surfaces as primary datums cause inspection/assembly mismatches.
- Datum reference letters (A, B, C...) must be used in FCF in precedence order; reordering changes the DRF.

### Gaps
- Composite datum features and datum targets (point/line/area) details not fully sourced; flagged.

## Q7: Geometric tolerances — definitions and applications

### Takeaway
Each geometric control has a specific tolerance zone and datum rule; choosing the right one requires matching design intent (form vs orientation vs location vs runout vs profile).

### Cited Findings
- Straightness: line element on surface, or derived median line (axis) of a pin/hole; no datum; MMC allowed only on feature of size (axis) — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Flatness: surface between two parallel planes; no datum; "on a flat surface, parallelism also limits flatness to same value" — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Circularity: each cross-section between two concentric circles; no datum; RFS only — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Cylindricity: whole cylindrical surface between two coaxial cylinders; no datum; RFS only — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Angularity: surface/axis/center plane at basic angle to datum; datum required; MMC only on FOS — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Perpendicularity: 90° to datum; datum required; MMC on FOS — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Parallelism: parallel to datum; datum required; MMC on FOS — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Position: feature-of-size axis/center plane within cylinder/planes at basic location; datums usually required; MMC/LMC allowed — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Concentricity (withdrawn 2018): derived median points within cylinder about datum axis; RFS only — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Symmetry (withdrawn 2018): derived median points within zone about datum center plane; RFS only — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Profile of a line: 2D zone along cross-section; datum optional; RFS only — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Profile of a surface: 3D zone wrapping whole surface; datum optional; RFS only; "most versatile control" — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Circular runout: FIM at each cross-section as part rotates about datum axis; datum required; RFS only — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).
- Total runout: whole surface in one sweep about datum axis; datum required; RFS only — [NORAMARK](https://www.noramark.com/resources/charts/gdt-symbols/).

### Inferences
- Use position (not concentricity) for hole patterns; use runout for rotating parts; use profile when surface form+location matter.
- Circular runout is cheaper to inspect than total runout; specify total only when taper/straightness along the surface matters.

### Gaps
- Tolerance zone shapes (cylinder vs two planes) for each control when applied to surfaces vs FOS fully detailed in standard; summarized here.

## Q8: Material condition modifiers (MMC, LMC, RFS) and bonus tolerance

### Takeaway
MMC applies tolerance at maximum material (smallest hole/largest pin) and grants bonus tolerance as feature departs toward LMC; LMC protects minimum wall/edge distance; RFS (default in ASME) holds tolerance constant; modifiers apply only to features of size and only to certain controls.

### Cited Findings
- MMC definition: "condition in which a feature contains maximum amount of material within stated limits" — hole MMC = smallest hole; pin MMC = largest pin — [GD&T Basics MMC](https://www.gdandtbasics.com/maximum-material-condition/).
- MMC applicable controls: straightness (axis), parallelism, perpendicularity, angularity, position — [GD&T Basics MMC](https://www.gdandtbasics.com/maximum-material-condition/).
- "Bonus Tolerance = Difference between MMC & Actual condition" — [GD&T Basics MMC](https://www.gdandtbasics.com/maximum-material-condition/).
- LMC: opposite of MMC; used to protect minimum wall thickness/edge distance — [GD&T Basics (via MMC page links)](https://www.gdandtbasics.com/maximum-material-condition/).
- RFS: default when no modifier shown; "no bonus tolerance"; tolerance stays constant regardless of feature size — [GD&T Basics MMC](https://www.gdandtbasics.com/maximum-material-condition/) ("Default to Regardless of feature size").
- Virtual condition / boundary: for assembly, gauge size = MMC ± GD&T tolerance; MMB/LMB apply to datums referenced with M/L modifiers (datum shift, not bonus) — [GD&T Basics MMC comments (Matt Derr)](https://www.gdandtbasics.com/maximum-material-condition/).
- Projected tolerance zone (P modifier): moves tolerance zone above part by stated height; used on threaded/press-fit holes — [GD&T Basics symbols list](https://www.gdandtbasics.com/maximum-material-condition/).

### Inferences
- Use MMC for assembly-critical holes/pins to enable functional (go) gauging and gain bonus tolerance.
- Use LMC when wall thickness or edge distance is the critical constraint.
- Don't apply MMC to profile/circularity/runout (not permitted); use RFS.

### Gaps
- Reciprocity requirement (RPR, ISO 2692) and MMB/LMB detailed rules not fully sourced; flagged.

## Q9: Drawing practices (dimensioning, tolerancing blocks, general tolerances, title block)

### Takeaway
Drawings must fully define geometry with minimum dimensions; basic dimensions have no tolerance (tolerance from FCF); general tolerances (ISO 2768-m/f/c/v or ASME default block) cover untoleranced dimensions; title block declares standard, units, material, scale, revision.

### Cited Findings
- ASME Y14.5 fundamental rules: all dimensions must have tolerance (direct, block, or note); basic dimensions get tolerance from related FCF; drawings should have minimum dimensions; 90° angles assumed; dimensions valid at 20°C — [Wikipedia GD&T "Purpose and rules"](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ISO 2768 general tolerances: ISO 2768-1 (linear/angular dimensions) with classes f (fine), m (medium), c (coarse), v (very coarse); ISO 2768-2 (geometric tolerances for form/orientation) with classes H, K, L — [Engineers Edge (references ISO 2768)](https://www.engineersedge.com/manufacturing/preferred_mechanical_tolerances_metric_iso_286_13166.htm).
- ISO 128 (technical product documentation general principles) and ISO 129 (indication of dimensions and tolerances) govern drawing presentation — [Wikipedia GD&T "Documents and standards"](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ISO 1 (standard reference temperature 20°C) for geometrical/dimensional properties — [Wikipedia ISO list](https://en.wikipedia.org/wiki/List_of_ISO_standards_1%E2%80%931999).
- Free-state condition applies unless stated otherwise (ASME Rule #13); restrained condition noted with Ⓕ symbol — [Wikipedia GD&T rules](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing) and [GD&T Basics symbols](https://www.gdandtbasics.com/maximum-material-condition/).

### Inferences
- An AI generating a drawing should include a general tolerance note ("Unless otherwise specified, tolerances per ISO 2768-m" or ASME default block) and a title block declaring standard, units, material, finish, revision.
- Avoid redundant dimensions; use basic dimensions for GD&T-controlled features.

### Gaps
- Detailed ISO 2768-1 tolerance tables (f/m/c/v values by size range) and ISO 2768-2 geometric classes not reproduced; calculator/source tables flagged. ASME Y14.5 default tolerance block format not sourced in detail.