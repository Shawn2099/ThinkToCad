# Cam and Gear Mechanisms Catalog

## Cam mechanisms, followers, and motion laws

### Takeaway
Cams convert rotary or sliding input into programmed follower motion; the profile, follower type, and motion law together determine speed, acceleration, contact stress, and noise. Gear trains transmit torque/ratio between shafts; selection among spur, helical, bevel, worm, planetary, and special drives trades efficiency, ratio, backlash, compactness, and cost.

### Cited Findings
- **Cam (general)** — a rotating or sliding piece in a mechanical linkage used especially in transforming rotary motion into linear motion; converts rotational motion to reciprocating or oscillating motion (Wikipedia "Cam (mechanism)", https://en.wikipedia.org/wiki/Cam_(mechanism)).
- **Displacement diagram** — relates angular position (degrees) to follower radial displacement; defines rise (follower away from cam center), dwell (follower at rest), return (follower toward cam center) (Wikipedia "Cam (mechanism)").
- **Base circle** — smallest circle that can be drawn to the cam profile; **prime circle** radius = follower radius + base circle radius; **pitch curve** is radial curve traced by radial displacements away from prime circle; **lobe separation angle (LSA)** is angle between adjacent intake/exhaust lobes (Wikipedia "Cam (mechanism)").
- **Plate (disc/radial) cam** — cut from flat metal/plate; follower moves in plane perpendicular to camshaft axis; most common type; used in machine-tool programming cams, dishwasher/washer electromechanical controllers, IC engine camshafts (Wikipedia "Cam (mechanism)").
- **Cylindrical (barrel) cam** — follower rides in groove cut into cylinder surface; converts rotation to linear motion perpendicular to cylinder axis; can have multiple grooves; positive positioning (no spring needed); applications: machine-tool drives, reciprocating saws, sequential-transmission shift barrels (motorcycles) (Wikipedia "Cam (mechanism)").
- **Constant-lead barrel cam** — follower position linear with rotation (like a lead screw); used in lathe threading cross-slide settings (Wikipedia "Cam (mechanism)").
- **Cylindrical cam with two inputs** — output radial to cylinder; formerly common in naval gun fire-control and mechanical analog computers (Wikipedia "Cam (mechanism)").
- **Face cam** — follower rides on face of a disk, often in a slot (captive, positive positioning); can provide repetitive motion (closed curve groove) or function generation (stopped groove); constant-lead form used in scroll chuck; motion parallel to cam axis example: traditional sash-window lock (self-locking via friction like worm gear); three-output form in stereo phonograph (Wikipedia "Cam (mechanism)").
- **Heart-shaped cam** — symmetric heart returns a shaft to a set position by roller pressure; used on early Post Office master clocks to synchronize with GMT (Wikipedia "Cam (mechanism)").
- **Snail (drop) cam** — follower raised over 24 h in spiral path terminating in sharp cutoff; drops to drive day-advance at midnight in clocking-in clocks; uses roller cam for most travel then solid follower for precise drop (Wikipedia "Cam (mechanism)").
- **Linear cam** — cam element moves in straight line rather than rotates; input is linear motion; profile may be cut into edges/slots/surface; example: pin-tumbler lock key (pins as followers), key-duplication machines (Wikipedia "Cam (mechanism)").
- **Globoidal cam** — (hourglass-shaped cam used in indexing/conjugate drives) — not covered in fetched sources; flagged unverified; commonly cited in mechanism texts (e.g., Norton) for high-speed indexing (UNVERIFIED).
- **Conjugate (dual) cam** — paired cams with two followers to eliminate backlash/clearance; used for precision motion; flagged: only generic conjugate concept implied by positive-positioning cams in Wikipedia; specifics UNVERIFIED from fetched sources.
- **Preloaded cam** — spring-preloaded follower maintaining contact to avoid jump; standard practice noted indirectly (spring provision) in Wikipedia cylindrical/face cam descriptions; specifics UNVERIFIED.
- **Cam followers — construction** — specialized roller/needle bearing following cam lobes; stud style (stud included) vs yoke style (hole through middle); modern stud follower patented 1937 by Thomas L. Robinson, McGill (Wikipedia "Cam follower", https://en.wikipedia.org/wiki/Cam_follower).
- **Follower anti-friction elements**: full-complement needle rollers (high radial load, no thrust); caged needle rollers (higher speed, lower load); roller design (two rows, heavy duty, some thrust); bushing (light duty, maintenance-free, ~25% load of roller stud) (Wikipedia "Cam follower").
- **Follower shape**: cylindrical OD vs crowned OD (compensates up to 0.5° misalignment vs 0.06°; lower load capacity) (Wikipedia "Cam follower").
- **Stud features**: standard vs heavy stud; slot or hex drive; eccentric stud for backlash adjustment (range = 2× eccentricity) (Wikipedia "Cam follower").
- **Track followers**: V-groove/flanged OD; ball/tapered-roller elements for thrust (Wikipedia "Cam follower").
- **Cam follower types by contact shape (per task list)**: knife-edge, roller, flat-faced, spherical, mushroom, oscillating/rocker followers — standard mechanical-engineering classification (Norton "Design of Machinery"; Shigley) cited in Wikipedia cam article references; specific per-type details UNVERIFIED from fetched sources (flagged).

### Inferences
- Positive positioning (groove/captive follower) is preferred where dwell accuracy and high speed matter; spring-loaded open followers suit simpler/low-speed cams.
- Cylindrical/face cams support multi-input or multi-output function generation not possible with simple disk cams.
- Roller followers reduce wear vs knife-edge/flat at high load/speed; flat-faced followers can handle higher contact stress in certain profiles (inference from bearing-type construction).

### Gaps
- No fetched source for globoidal cam geometry, conjugate/preloaded cam specifics, or per-follower-type (knife-edge/roller/flat/spherical/mushroom/oscillating) design equations; rely on Norton/Shigley/Mott textbooks (UNVERIFIED here).
- Motion-law details (below) not in fetched Wikipedia; standard textbook values flagged.

## Cam motion laws

### Takeaway
Motion laws (rise/return profiles) trade peak acceleration, jerk, and contact force; dwell-rise-dwell profiles dominate valve/automation cams, while cycloidal and polynomial laws reduce jerk and vibration at high speed.

### Cited Findings
- **Dwell-rise-dwell** — basic displacement diagram: constant velocity rise, dwell, similar return; standard for simple cams (Wikipedia "Cam (mechanism)" Fig. 2 and intro).
- **Constant velocity / constant acceleration / SHM / cycloidal / polynomial (3-4-5, 4-5-6-7) / modified trapezoid / modified sine** — standard motion-law set listed in task; not detailed in fetched Wikipedia; standard in Norton "Design of Machinery" and Shigley "Theory of Machines and Mechanisms" (cited in Wikipedia cam refs) — UNVERIFIED details here; flag.
- **Cam profile design relation** (disk cam, circular-arc approximation): given lift L and dwell angle θ, with φ = π/2 − θ/2, C = L/(1 − sin φ), r = R − L·sin φ/(1 − sin φ), where R = base radius, r = tip radius, C = center distance (Wikipedia "Cam (mechanism)").
- **Valve-cam note** — convex curve between onset and max lift reduces acceleration but needs large shaft diameter; in practice tangent to base circle appears on profile (Wikipedia "Cam (mechanism)").

### Inferences
- Cycloidal and polynomial laws preferred for high-speed/precision; modified trapezoid balances acceleration and jerk for automotive valves.

### Gaps
- No fetched equations for SHM/constant-accel/cycloidal/polynomial/modified-trapezoid profiles; consult Norton/Shigley (UNVERIFIED).

## Gear mechanisms

### Takeaway
Gears transmit rotation/torque between shafts; classification by axis relation (parallel/crossed/skew), tooth cut (straight/helical/double-helical/worm), and profile (involute/cycloid) determines efficiency, noise, ratio, and load capacity. Special drives (planetary, harmonic, cycloidal, worm, hypoid) extend ratio and compactness at efficiency/backlash trade-offs.

### Cited Findings

**Basic gear principles** (Wikipedia "Gear", https://en.wikipedia.org/wiki/Gear)
- Gear ratio r = N2/N1; T2/T1 = r; ω2/ω1 = 1/r; smaller member = pinion.
- Axis relations: parallel (opposite sense; internal nested = same sense), crossed (bevel, axes intersect), skew (hypoid, axes skew).
- Tooth cut: straight (spur, bevel), helical, double-helical (herringbone), worm.
- Profiles: involute (modern standard), cycloid (clocks), artisanal cage/lantern.
- Materials: bronze/iron historical; steel (strength/cost), aluminum (light), plastics (molded, sacrificial), wood (historical).
- Manufacture: casting, injection molding, powder metallurgy, blanking, gear cutting (hobbing/shaping/milling/broaching), heat treatment.
- Ideal gear: rigid body, fixed axis; action surface N-fold symmetry; backlash.

**Spur gear** (Wikipedia "Gear" straight section)
- Cylindrical gear with teeth straight parallel to axis; external or internal; parallel shafts only; no axial thrust; excellent moderate speed, noisy at high speed; straight bevel variant for crossed axes <5 m/s or <1000 rpm small gears.

**Helical gear** (Wikipedia "Gear" helical section)
- Teeth angled (helix); parallel or crossed configuration; smoother/quieter than spur; axial thrust (thrust bearing needed); crossed helical for non-parallel non-intersecting axes (lower capacity).
- Herringbone/double-helical eliminates axial thrust by opposing hands (see below).

**Internal gear** (Wikipedia "Gear" internal/external)
- Teeth point inward; nested with external pinion; both rotate same sense; used in planetary ring gears.

**Crown gear (face/contrate gear)** (Wikipedia "Gear" crown section)
- Teeth project at right angles to plane; meshes with escapements/clocks; bevel variant (crown bevel, 90° pitch angle).

**Bevel gear (straight)** (Wikipedia "Bevel gear", https://en.wikipedia.org/wiki/Bevel_gear)
- Axes intersect; conical pitch surface; typically 90°; external (teeth outward), internal (teeth inward), crown (90° pitch angle).
- Straight tooth lines: simplest; limited to <1000 ft/min or <1000 rpm small gears due to impact noise.
- Mitre gears: equal teeth, 90°, 1:1 ratio.
- Applications: differentials, hand drills, rotorcraft drive, floodgates, locomotives, marine, printing presses, power plants.
- Advantages: change operating angle, mechanical advantage via tooth count; disadvantages: matched pairs only, precise mounting, bearing forces.

**Spiral bevel gear** (Wikipedia "Spiral bevel gear", https://en.wikipedia.org/wiki/Spiral_bevel_gear)
- Bevel gear with helical (curved) teeth; less vibration/noise than straight; opposite hands for pinion/gear; replaced in pairs.
- Spiral angle = angle between tooth trace and pitch cone element.
- Zerol bevel: curved but not angled (intermediate).

**Hypoid gear** (same article)
- Spiral bevel with non-intersecting (skew) axes; hyperbolic pitch surface; pinion offset below/above crown wheel; larger pinion diameter, more contact; sliding action → special EP gear oil; stronger, quieter, higher ratios than bevel; used in automotive final drives (rear axle) and railcar transmissions; higher offset → more torque but lower efficiency/fuel economy.

**Worm drive** (Wikipedia "Worm drive", https://en.wikipedia.org/wiki/Worm_drive)
- Worm (screw) meshes worm wheel; 90° axes; single-start gives ratio = wheel teeth:1 (compact high reduction); self-locking possible (large ratios, friction); types: non-throated, single-throated, double-throated; worms: enveloping (hourglass), double-enveloping (globoidal); multi-start reduces ratio and braking effect.
- Direction of transmission generally not reversible at large ratios.
- Applications: steering (pre-power steering), presses, rolling mills, conveyors, mining, rudders, circular saws, milling heads/rotary tables, elevators/escalators, musical-instrument tuners, plastic motor gearboxes, hose clamps, centrifuges/blowers (reverse).
- Torsen differential uses worm wheels/planetary worms.

**Planetary (epicyclic) gearing** (Wikipedia "Epicyclic gearing", https://en.wikipedia.org/wiki/Epicyclic_gearing)
- Sun, planet(s), carrier, ring (annulus); three-shaft device; holding one member stationary yields three ratios; coaxial input/output; compact, high torque-to-weight, multiple inputs (power splitting).
- Kinematics: Ns·ωs + Nr·ωr = (Ns+Nr)·ωc; fixed carrier ratio R = −Nr/Ns.
- Types: simple, compound (meshed-planet, stepped-planet, multi-stage); stepped planets need timing marks.
- Applications: automatic transmissions, bicycle hub gears, tractors/construction, hybrid vehicles, analog computers, astronomical mechanisms (Antikythera), pencil sharpeners.
- Advantages: coaxial, high ratio in small volume, multiple inputs; disadvantages: complexity, assembly constraints.

**Rack and pinion** (Wikipedia "Rack and pinion", https://en.wikipedia.org/wiki/Rack_and_pinion)
- Circular pinion meshes linear rack; converts rotary ↔ linear; higher linear speed than worm+rack (full turn = pitch circumference vs one tooth); used in rack railways, arbor/drill presses, valve actuators, stairlifts, lock gates, electric gates, automotive steering.
- Arcuate rack possible; double-rack for balanced torque.

**Face gear** — (Wikipedia gear article: crown gear; face gear not separately fetched) — face gear = cylindrical pinion meshes disk with teeth on face; not covered in detail; flagged: general face-gear concept UNVERIFIED beyond crown gear note. Standard in AGMA 203.02/ISO 23509 (flagged).

**Harmonic drive (strain wave gearing)** (Wikipedia "Strain wave gearing", https://en.wikipedia.org/wiki/Strain_wave_gearing)
- Three components: wave generator (elliptical plug + bearing), flex spline (cup with teeth), circular spline (internal teeth); flex spline has 2 fewer teeth than circular spline; ratio R = (flex − circular)/flex (negative, e.g., −0.01 → 100:1); no backlash, compact/light, high ratio, coaxial, excellent repeatability; disadvantages: torsional wind-up; used in robotics and aerospace (Apollo LRV wheels, Skylab winches).

**Cycloidal drive** (Wikipedia "Cycloidal drive", https://en.wikipedia.org/wiki/Cycloidal_drive)
- Eccentric input drives cycloidal disc; disc perimeter meshes stationary ring gear; output pins; reduction r = (P−L)/L; zero backlash, high torque capacity, compact; single-stage efficiency ~93%, double ~86%; ratios up to 119:1 single, 7,569:1 double; vibration if unbalanced (use 2+ discs); applications: robotics actuators, high-torque compact reducers.

**Differential** (Wikipedia "Differential (mechanical device)", https://en.wikipedia.org/wiki/Differential_(mechanical_device))
- Three-shaft gear train; output speed = average of two inputs; open (ring-and-pinion bevel, spur-gear, epicyclic) and limited-slip/locking variants; torque vectoring; uses: vehicles (cornering), clocks (equation of time), analog computers (differential analyzers), Mars rover rocker-bogie suspension.

**Herringbone/double-helical gear** (Wikipedia "Herringbone gear", https://en.wikipedia.org/wiki/Herringbone_gear)
- Two helical gears of opposite hand side-by-side (V-shaped teeth); no axial thrust; smooth power transfer; harder/more expensive to manufacture; central gap or Wuest apex; used in marine steam turbines, Citroën final drives, Panhard camshaft timing.

**Non-circular gear** (Wikipedia "Non-circular gear", https://en.wikipedia.org/wiki/Non-circular_gear)
- Non-round pitch curves for variable ratio/oscillation; usually spur; tight tolerances; applications: textile machines, potentiometers, CVTs, window shades, mechanical presses, hydraulic engines.

**Elliptical gear** — special case of non-circular gear (elliptical pitch curve); not separately covered; flagged UNVERIFIED beyond non-circular gear article.

**Nutating gear** — (not in fetched sources) — conical gear rolling with nutating motion; used in speed reducers (e.g., NuVinci CVT uses balls; nutating drives in some reducers); flagged UNVERIFIED.

**Bevel planetary** — planetary set with bevel gears for angled axes (pencil sharpeners, differentials); mentioned in epicyclic article ("axes can be placed at an angle, introducing bevel gear elements"); specifics UNVERIFIED.

**Magnetic gear** — non-contact torque transmission via modulated magnetic fields; noted in Wikipedia "Gear" (non-rigid gears); flagged UNVERIFIED specifics.

**Sun and planet gear** — early planetary variant (Watt) with planet meshing sun and ring; listed in gear nav; specifics not fetched; flagged UNVERIFIED.

**Cycloid gear (tooth profile)** — cycloid tooth form vs involute; used in clocks; not fetched in detail; flagged UNVERIFIED.

### Inferences
- For high reduction in compact volume: harmonic or cycloidal drives; for cost/efficiency at moderate ratios: spur/helical; for 90° axis change under load: spiral bevel/hypoid; for self-locking/very high ratio cheaply: worm.
- Hypoid preferred over worm in automotive final drives due to efficiency, but requires EP oil and precise setup.
- Planetary gearsets dominate automatic transmissions due to coaxial I/O and ratio flexibility.

### Gaps
- No fetched sources for face gear, nutating gear, bevel planetary, elliptical gear, magnetic gear, sun-and-planet gear, globoidal cam, conjugate/preloaded cam specifics, and cam motion-law equations; rely on Norton/Shigley/Mott/AGMA (UNVERIFIED).
- AGMA standards cited only indirectly via Wikipedia references (ANSI/AGMA 1012-G05 nomenclature); detailed standard requirements not fetched.
- Google Patents not fetched (web search unavailable); patent references (Musser 1957 harmonic, Braren 1925 cycloidal, Robinson 1937 cam follower) cited via Wikipedia.

## Selection guide (when to select)

### Takeaway
Select cam type by motion profile and speed; select gear type by axis angle, ratio, efficiency, backlash, and cost constraints.

### Cited Findings
- **Cam selection**: plate cam for simple rotary→reciprocating at moderate speed; cylindrical/face for positive positioning, multi-input/output, function generation; linear for straight-line input (locks); heart/snail for clocking/synchronization.
- **Gear selection**: spur for parallel shafts, low cost, moderate speed; helical for smoother/quieter parallel or crossed; bevel for intersecting axes (90°); hypoid for automotive final drives; worm for compact high ratio/self-locking; planetary for coaxial high torque density/multiple inputs; harmonic/cycloidal for zero backlash/high ratio/robotics; rack-and-pinion for rotary↔linear; differential for speed averaging; non-circular for variable ratio.

### Inferences
- High-precision/robotics favors harmonic or cycloidal; heavy industry favors herringbone/hypoid/planetary; consumer products favor molded spur/plastic gears.

### Gaps
- Quantitative selection thresholds (speed limits, efficiency percentages beyond cycloidal 93%/86%) not fully sourced; consult AGMA/Norton (UNVERIFIED).
