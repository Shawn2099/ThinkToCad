# Assembly Design and Analysis

Dense reference for an AI CAD design assistant (build123d/FreeCAD workflow). Covers mates/constraints, interference & clearance, assembly tolerance, assembly methods, DFA, top-down vs bottom-up, modular design, documentation, and pitfalls. Sources: Wikipedia engineering articles cited inline; textbook/standard items (Mott *Machine Elements*, Shigley, Boothroyd/Dewhurst/Knight) noted where no URL exists and flagged as unverified where appropriate.

## Assembly Constraints / Mates

### Takeaway
Mates (constraints) remove degrees of freedom between parts; a fully (properly) constrained part has 0 DOF relative to its mates, while over-constraining creates redundant constraints that make assemblies fragile and unsolvable.

### Cited Findings
- A datum is a theoretically exact plane, line, point, or axis; a datum reference frame describes how a part fits or functions within an assembly — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- GD&T dimensions/tolerances are valid at 20 °C and 101.3 kPa unless otherwise stated (ASME Y14.5 rule) — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Engineering fits fall into three categories: clearance, transition/location, and interference; hole-basis vs shaft-basis systems determine which part's size is held constant — [Wikipedia: Engineering fit](https://en.wikipedia.org/wiki/Engineering_fit).
- Interference fits (press/force/friction fits) are fastenings held by friction after parts are pushed together; assembled by force or by thermal expansion/contraction (shrink fit) — [Wikipedia: Interference fit](https://en.wikipedia.org/wiki/Interference_fit).

### Inferences
- Common mate types and the DOF they remove (standard CAD semantics, e.g. SolidWorks/Fusion/FreeCAD-style):
  - **Coincident / Mate (face-to-face):** aligns two planar faces; removes 3 DOF (translation normal + 2 rotations). Often combined with concentric to fully locate a part.
  - **Concentric:** aligns two cylindrical axes; removes 2 radial DOF (X,Y translation), leaves axial slide + rotation. Combine with a coincident/planar mate to fully locate.
  - **Distance / Parallel offset:** fixes a scalar distance between two entities (planes/points/axes); removes 1 DOF. Used for spacers, shims, gaps.
  - **Angle:** fixes relative orientation between two planes/axes; removes 1 rotational DOF.
  - **Gear:** couples rotation of two cylindrical parts by a ratio (teeth ratio); drives motion study.
  - **Cam:** follower constrained to a cam profile; defines motion.
  - **Screw / Hinge (helical):** combines rotation and translation along an axis by a pitch; models threaded fasteners and lead screws.
  - **Weld / Rigid (Lock):** removes all 6 DOF; treats two parts as one rigid body. Use for permanent joints; avoids mate solver load.
  - **Flexible / Spring / Slot:** allows limited motion (e.g., spring compression, slot slider); used in mechanism studies.
- **Top-level assembly strategy:** ground one part (fix to origin) to remove the whole-assembly 6 DOF; mate everything else to it. Avoid "floating" parts with no path to ground.
- **Over-constraining pitfalls:** redundant mates (e.g., two coincident face mates on non-coplanar faces, or concentric + 3 point mates) create conflicting constraints; solvers may fail or silently drop mates. Prefer a minimal mate set (3-2-1 locating).
- **FreeCAD/build123d specifics (unverified against current docs):** FreeCAD Assembly workbench uses "Joint" objects (Fixed, Revolute, Cylindrical, Slider, Ball, Distance, Angle, Gear, Screw, etc.) rather than traditional mates; build123d uses `Compound`/`Location` and assembly via `Part` wrapping with `mate_to`-style transforms. Verify API names against current build123d docs before coding — I could not fetch live docs (transport error); treat as unverified.

### Gaps
- Live FreeCAD Assembly workbench and build123d assembly API documentation could not be fetched (FreeCAD wiki behind Anubis bot-check; build123d docs transport error). Exact constraint/joint names and method signatures should be verified against current docs before implementation.
- CAD-vendor-specific mate solver behavior (SolidWorks vs Fusion vs FreeCAD) not sourced here; only general semantics provided.

## Interference and Clearance Analysis

### Takeaway
Interference (clash) detection must be run at multiple assembly states (as-built, worst-case tolerance, and motion extremes); static clash checks alone miss dynamic and tolerance-driven interferences.

### Cited Findings
- Interference fits require force or thermal methods (force press, shrink fit) and are used for bearing-housing/shaft mounting — [Wikipedia: Interference fit](https://en.wikipedia.org/wiki/Interference_fit).
- Clearance fits allow sliding/rotation; transition fits require light pressing — [Wikipedia: Engineering fit](https://en.wikipedia.org/wiki/Engineering_fit).
- GD&T position tolerance controls hole location relative to datums; bonus tolerance applies at MMC — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).

### Inferences
- **Clash types:** hard clash (solid interference, penetration), soft clash (clearance violation below threshold), motion clash (interference during movement).
- **Minimum clearance:** define a global minimum clearance (e.g., 0.5–1 mm for machined parts, larger for castings/weldments) and check all component pairs against it; use distance queries between faces/edges.
- **Motion study:** animate joints (gear, screw, cam, slider) through full range; check collision at each frame; export min-clearance over time.
- **Tolerance-driven clash:** a part that clears nominally may interfere at tolerance extremes; run clash checks at worst-case (max material) conditions for critical interfaces (bearings, seals, gears).
- **build123d/FreeCAD workflow (unverified):** use bounding-box pre-filter then exact mesh/B-rep intersection; FreeCAD has "Check for issues" / assembly collision tools; build123d can compute via `Shape.common()` / distance queries. Verify exact API.

### Gaps
- No sourced minimum-clearance thresholds found; values above are engineering rules of thumb from training (unverified). Use project-specific requirements.
- No sourced procedure for tolerance-aware clash in FreeCAD/build123d; treat as unverified.

## Assembly Tolerance (Stack-up)

### Takeaway
Choose worst-case for safety-critical/low-volume or when parts are not statistically controlled; RSS when processes are stable and centered; Monte Carlo when distributions are non-normal or assemblies are complex.

### Cited Findings
- Fit categories and ISO/ANSI limits-and-fits (H7/h6 etc.) define clearance/interference ranges from hole/shaft tolerances — [Wikipedia: Engineering fit](https://en.wikipedia.org/wiki/Engineering_fit).
- GD&T datums and datum reference frames define how parts are located for measurement; MMC/LMC modifiers affect bonus tolerance — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- GD&T applies at 20 °C free-state unless stated otherwise — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).

### Inferences
- **Linear stack-up (1D):** for dimensions in series along one direction, assembly dimension = sum of part dimensions; tolerance stack = sum of component tolerances (worst case) or RSS.
  - Worst case: T_asm = Σ T_i. Guarantees fit for all parts within spec; conservative; used for safety-critical.
  - RSS (statistical): T_asm_rss = √(Σ T_i²). Assumes independent, centered, normal distributions; predicts ~99.7% (±3σ) yield for normal inputs; less conservative.
  - Monte Carlo: sample each input distribution (normal/uniform/triangular), compute assembly dimension, repeat N (e.g., 10⁴–10⁶), derive mean, σ, and percentile bounds (e.g., 99.73% → ±3σ or 99.999% → ±4.5σ for Six Sigma).
- **Datum reference frames (DRF):** a 3-2-1 scheme — primary datum (3 points, plane) removes 3 DOF; secondary (2 points, line/axis) removes 2; tertiary (1 point) removes 1. Assemblies mate parts to datums, not raw faces, to avoid tolerance ambiguity.
- **Tolerance allocation:** distribute an assembly tolerance budget among parts. Methods: equal division, proportional to cost/difficulty, or optimization (minimize cost subject to σ_asm ≤ target). Worst-case allocation: T_part_i = T_budget × (cost weight_i / Σ cost weights) (rule of thumb).
- **Thermal effects:** at non-20 °C, apply thermal expansion α·L·ΔT; for dissimilar materials (e.g., Al vs steel) this can dominate the stack-up.
- **Geometric (GD&T) stack-up:** position tolerances of holes/pins relative to datums; use true position tolerance zones (circular/diametral) and consider MMC bonus tolerance when parts are at MMC. Profile tolerances control surfaces.
- **build123d/FreeCAD:** tolerance is not native to geometry; document via PMI/GD&T on drawings; use external stack-up tools or scripts. (unverified)

### Gaps
- No sourced tolerance-allocation optimization formulas found; methods above are standard engineering practice from training (unverified against specific textbooks).
- Monte Carlo sample-size/yield-percentile conventions vary by company; not sourced here.

## Assembly Methods

### Takeaway
Select joining method by load type, service environment, disassembly need, and cost: bolted for maintainable high-load joints, welded for permanent/sealed, snap-fit for low-cost plastic consumer products, adhesive for thin/lightweight/composite, press-fit for bearings and hubs.

### Cited Findings
- Interference fits assembled by force or thermal expansion; used for bearings on shafts/housings — [Wikipedia: Interference fit](https://en.wikipedia.org/wiki/Interference_fit).
- ISO/ANSI fits: clearance for sliding, transition for location, interference for press — [Wikipedia: Engineering fit](https://en.wikipedia.org/wiki/Engineering_fit).
- Mott, *Machine Elements in Mechanical Design* (5th ed.) cited as reference for interference fits (ANSI) — [Wikipedia: Engineering fit](https://en.wikipedia.org/wiki/Engineering_fit).

### Inferences
- **Bolted/screwed:** removable, high clamp load, good for metals; requires access, torque control, thread engagement (≥1.5× dia in steel, ≥2× in Al), preload, and locking (lock washer/threadlocker) against vibration. Cost: medium.
- **Riveted:** permanent, fast, good for sheet metal and thin sections; no threads; requires access to both sides (solid rivets) or one side (blind/pop rivets). Lower fatigue strength than bolts in some cases.
- **Welded:** permanent, sealed, high strength, low part count; requires weldable materials, skilled labor, fixtures, and post-weld distortion control; poor for disassembly.
- **Pinned:** locates parts rotationally/axially with dowel/spring pins; good for alignment and shear loads; low cost; not for tension.
- **Press-fit (interference):** bearing mounts, bushings, hubs; no fasteners; requires chamfers, alignment, and force/thermal process control.
- **Snap-fit:** cantilever/hook or annular (ring) snaps in plastics; very low assembly cost, no tools; limited load, creep, and fatigue; design for deflection within elastic limit; add lead-in chamfers.
- **Adhesive:** bonds dissimilar/thin/composite materials, distributes load, seals; surface prep critical; cure time; temperature/chemical limits; poor for peel loads unless designed.
- **Selection criteria:** load (static/dynamic/fatigue), environment (temp, corrosion, chemicals), disassembly/service need, materials, production volume, cost, skill/automation, and accessibility.

### Gaps
- No sourced selection matrix or quantitative criteria (e.g., torque values, thread-engagement ratios) found; ratios above are standard rules of thumb from training (unverified). Verify with Mott/Shigley for specific applications.

## Design for Assembly (DFA)

### Takeaway
DFA's biggest lever is part-count reduction via the three Boothroyd criteria; then minimize handling/insertion time through symmetry, self-locating features, and top-down insertion.

### Cited Findings
- DFA reduces assembly cost by reducing part count and improving ease of grasping, orienting, inserting — [Wikipedia: Design for assembly](https://en.wikipedia.org/wiki/Design_for_assembly).
- Boothroyd developed DFA at UMass Amherst (NSF-funded), starting 1977; computerized version (Boothroyd & Dewhurst) from 1981 — [Wikipedia: Design for assembly](https://en.wikipedia.org/wiki/Design_for_assembly).
- Three criteria to determine if a part can be eliminated/combined with another — [Wikipedia: Design for assembly](https://en.wikipedia.org/wiki/Design_for_assembly).
- Boothroyd & Dewhurst, Knight: *Product Design for Manufacture and Assembly* (2nd ed., 2002); Boothroyd *Assembly Automation and Product Design* (2nd ed., 2005) — [Wikipedia: Design for assembly](https://en.wikipedia.org/wiki/Design_for_assembly).
- AEM (Hitachi Assembly Evaluation Method) based on "one motion for one part" with point-loss standard — [Wikipedia: Design for assembly](https://en.wikipedia.org/wiki/Design_for_assembly).
- DFA savings examples: Xerox estimated hundreds of millions (1981); Ford credited ~$1B (1988) — [Wikipedia: Design for assembly](https://en.wikipedia.org/wiki/Design_for_assembly).
- Sony Walkman designed for vertical assembly (straight-down insertion only); IBM Proprinter used DFAA rules — [Wikipedia: Design for assembly](https://en.wikipedia.org/wiki/Design_for_assembly).
- Modular Function Deployment (MFD) paired with DFA to simplify assembly via part reduction — [Wikipedia: Modular design](https://en.wikipedia.org/wiki/Modular_design).

### Inferences
- **Boothroyd three criteria (part must be separate if any is true):**
  1. The part moves relative to all other parts already assembled (during normal operation).
  2. The part must be of a different material or isolated from all other parts (e.g., for electrical/thermal isolation).
  3. The part must be separate to allow assembly/disassembly (access) of other parts.
  If none is true → candidate for elimination/combination.
- **DFA index:** ratio of theoretical minimum parts (N_min) to actual parts (N_actual), often combined with assembly time: DFA index = N_min / N_actual (or assembly efficiency = (N_min × t_avg) / T_asm). Higher is better; target > 0.5–0.6 typical.
- **Handling time factors:** symmetry (rotational symmetry reduces orienting time), size/weight, nesting/tangling, slipperiness, need for tools, fragility. Design parts for easy grasp and unambiguous orientation (asymmetry in one direction only where needed).
- **Insertion time factors:** chamfers/lead-ins, self-locating features, top-down (vertical) insertion, no reorientation, snap/press without tools, adequate clearance.
- **Assembly sequence optimization:** minimize direction changes, avoid flipping the assembly, insert from top when possible, assemble in sub-assemblies, defer fragile/precision parts.
- **build123d/FreeCAD application:** reduce part count in CAD by combining via boolean union where criteria allow; model assembly sequence as a tree; keep BOM aligned with combined parts.

### Gaps
- Exact Boothroyd handling/insertion time tables and cost coefficients are proprietary to DFA software; not sourced here. Use licensed DFA tools or textbook tables (Boothroyd/Dewhurst/Knight) for quantitative time estimates.
- DFA index formula variants vary; the simple ratio above is a common simplification (unverified against the canonical method).

## Top-Down vs Bottom-Up Assembly Design

### Takeaway
Use top-down when interfaces and envelopes must be defined before parts exist (complex, tightly coupled systems); bottom-up when reusing standard parts/libraries; hybrid (top-down skeleton + bottom-up standard parts) is typical in practice.

### Cited Findings
- Modular design: functional partitioning into modules with well-defined interfaces; platform systems vs. modular systems — [Wikipedia: Modular design](https://en.wikipedia.org/wiki/Modular_design).
- Bottom-up optimization vs top-down design mentioned in modular/constructal design context — [Wikipedia: Modular design](https://en.wikipedia.org/wiki/Modular_design).

### Inferences
- **Bottom-up:** design individual parts first, then assemble; fast when reusing library/standard parts; risk of interface mismatches and interference discovered late.
- **Top-down:** define assembly skeleton (datums, envelopes, interfaces, motion paths) first; derive parts from the assembly context (in-context references); ensures fit and motion but creates fragile external references and heavier files.
- **Hybrid (recommended):** top-down skeleton defines interfaces/clearances; bottom-up standard parts (fasteners, bearings, motors) inserted; detail parts designed in context of skeleton; freeze interfaces before detailing.
- **CAD practice:** use assembly-level sketches/reference geometry as the single source of truth for interfaces; avoid excessive in-context (top-down) references that break on restructure; document interface contracts.

### Gaps
- No sourced quantitative comparison of top-down vs bottom-up outcomes; guidance is practice-based (unverified).

## Modular Design, Platform Architecture, Commonality

### Takeaway
Modularity trades higher design complexity for flexibility and reuse; commonality reduces cost/variety but can compromise optimal fit—balance via platform + optional modules.

### Cited Findings
- Modular design subdivides a system into independently created/modified/replaced modules with well-defined interfaces — [Wikipedia: Modular design](https://en.wikipedia.org/wiki/Modular_design).
- Platform systems (car platforms, USB) use component modularity; true modular systems (higher-dimensional modularity) are rare — [Wikipedia: Modular design](https://en.wikipedia.org/wiki/Modular_design).
- Modular design combines mass-production standardization with customization; MFD paired with DFA — [Wikipedia: Modular design](https://en.wikipedia.org/wiki/Modular_design).
- Benefits: cost, customization, interoperability, shorter learning, flexibility, sustainability; drawbacks: higher design complexity requiring systems expertise — [Wikipedia: Modular design](https://en.wikipedia.org/wiki/Modular_design).
- Platform systems examples: cars, computers, solar panels, elevators, furniture — [Wikipedia: Modular design](https://en.wikipedia.org/wiki/Modular_design).

### Inferences
- **Commonality:** share parts/interfaces across product variants to reduce SKU count, inventory, and tooling; measure via commonality index (e.g., % parts shared).
- **Platform architecture:** a base platform (chassis, powertrain, core frame) with variant modules (bodies, accessories) enables product families and faster time-to-market.
- **Trade-offs:** over-commonality forces suboptimal geometry (heavier, looser fits); under-commonality loses scale economies. Decide commonality at interfaces, not internals.
- **Assembly impact:** modular interfaces need robust locating features (dowels, pins, poka-yoke) and consistent fastener patterns to keep assembly time low across variants.

### Gaps
- No sourced commonality-index formulas or platform-cost models found; concepts above are general practice (unverified).

## Assembly Documentation

### Takeaway
Documentation must capture BOM (with revisions), assembly drawings with datums/PMI, exploded views with sequence numbers, and step-by-step instructions; keep BOM and CAD synchronized.

### Cited Findings
- GD&T on drawings defines nominal geometry and permissible variation; ASME Y14.5 / ISO GPS standards govern — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- GD&T data exchange exists at presentation/representation/validation levels between CAD systems — [Wikipedia: Geometric dimensioning and tolerancing](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).

### Inferences
- **BOM:** structured list (part number, description, qty, material, revision, source); distinguish purchased vs. manufactured; include hardware (fasteners) with quantities; revision control is critical.
- **Assembly drawings:** show exploded view, BOM balloon numbers, torque specs, mate/assembly notes, and key datums; include general tolerances block and finish notes.
- **Exploded views:** show assembly order and spatial relationships; number parts in assembly sequence; use arrows/paths.
- **Assembly instructions:** step-by-step with tools, torque, safety, and inspection checkpoints; include exploded sub-assembly views.
- **PMI (Product Manufacturing Information):** embed GD&T in 3D model (ASME Y14.41 / ISO 16792) for model-based definition; reduces drawing ambiguity.
- **build123d/FreeCAD:** export BOM from part metadata; use FreeCAD TechDraw for assembly drawings; exploded views via manual transform or dedicated tools (unverified).

### Gaps
- FreeCAD TechDraw/assembly-documentation capabilities not sourced here (wiki blocked); verify current feature set.

## Common Pitfalls

### Takeaway
Most assembly failures stem from over-constraining, missing ground reference, uncaught tolerance-driven interference, and BOM/CAD desync—catch them with constraint audits and worst-case clash checks.

### Cited Findings
- (No direct source; pitfalls below are synthesis.)

### Inferences
- **Over-constraining:** redundant mates cause solver failures or dropped constraints; audit mate count per part (aim for ≤6 effective constraints).
- **Floating parts:** parts with no path to ground; always ground one base part.
- **Missing mates:** parts appear located but aren't constrained; they shift on rebuild; check DOF (should be 0 for fixed parts).
- **Interference not caught:** static nominal clash checks miss motion and tolerance extremes; run clash at worst-case material conditions and through full motion range.
- **Tolerance stack not analyzed:** assemblies that fit nominally fail in production; perform 1D/3D stack-up before release.
- **Datum misuse:** mating to raw faces instead of datums creates ambiguous, non-repeatable location; use 3-2-1 datums.
- **BOM/CAD desync:** part numbers/revisions drift; enforce single source of truth and revision control.
- **Ignoring thermal expansion:** dissimilar materials at temperature extremes can bind or rattle.
- **Assembly sequence not validated:** parts that can't be inserted in the planned order; build a physical or virtual assembly sequence.

### Gaps
- Pitfall list is practice-based synthesis; no external source cited. Treat as unverified guidance.
</content>