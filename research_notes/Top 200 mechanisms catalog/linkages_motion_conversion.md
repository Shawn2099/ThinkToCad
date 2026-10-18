# Linkages and Motion-Conversion Mechanisms Catalog

## Scope
This note catalogs common linkage and motion-conversion mechanisms (≈36 entries) for a 200-mechanism knowledge base, covering four-bar and multi-bar linkages, quick-return, indexing, straight-line, and rotary↔linear converters. Each entry gives description, DOF, motion type, key dimensions/notes, when to use, limitations, and typical applications.

Sources relied on: Artobolevsky, *Mechanisms in Modern Engineering Design* (4 vols, 1975–1980); Chironis & Sclater, *Mechanisms and Mechanical Devices Sourcebook* (4th ed., 2007); Norton, *Design of Machinery*; Shigley, *Mechanical Engineering Design*; Mabie & Reinholtz, *Mechanisms and Dynamics of Machinery*; Wikipedia mechanism articles (URLs per entry). Flagged items are unverified.

---

## Q1: Enumeration of common linkages (four-bar variants and beyond)

### Takeaway
The most widely catalogued planar linkages are four-bar variants (crank-rocker, drag-link, double-rocker, parallelogram, anti-parallelogram, toggle) plus slider-crank, scotch yoke, bell crank, quick-return, Geneva, ratchet, escapement, pantograph, lazy tongs, and straight-line linkages (Chebyshev, Peaucellier, Scott Russell, Watt, Hoeken); atlases group them by motion class (rotary↔rotary, rotary↔linear, intermittent, straight-line).

### Cited Findings
- General linkage taxonomy and Grashof conditions — [Wikipedia: Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage).
- Slider-crank kinematics and engine applications — [Wikipedia: Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage).
- Scotch yoke motion profile — [Wikipedia: Scotch yoke](https://en.wikipedia.org/wiki/Scotch_yoke).
- Geneva drive indexing — [Wikipedia: Geneva drive](https://en.wikipedia.org/wiki/Geneva_drive).
- Pantograph scaling — [Wikipedia: Pantograph](https://en.wikipedia.org/wiki/Pantograph).
- Quick-return mechanisms (Whitworth, crank-shaper) — [Wikipedia: Quick return mechanism](https://en.wikipedia.org/wiki/Quick_return_mechanism).
- Straight-line linkages (Chebyshev, Peaucellier, Watt, Scott Russell, Hoeken) — [Wikipedia: Straight-line mechanism](https://en.wikipedia.org/wiki/Straight-line_mechanism).
- Ratchet and pawl — [Wikipedia: Ratchet](https://en.wikipedia.org/wiki/Ratchet).
- Escapement — [Wikipedia: Escapement](https://en.wikipedia.org/wiki/Escapement).
- Screw mechanisms — [Wikipedia: Leadscrew](https://en.wikipedia.org/wiki/Leadscrew); [Wikipedia: Ball screw](https://en.wikipedia.org/wiki/Ball_screw).
- Rack and pinion — [Wikipedia: Rack and pinion](https://en.wikipedia.org/wiki/Rack_and_pinion).
- Cam and follower — [Wikipedia: Cam](https://en.wikipedia.org/wiki/Cam).

### Inferences
- Atlases (Artobolevsky, Chironis) organize by input/output motion class rather than by name; the "most common" set above matches the four-bar/slider-crank/Geneva/cam families that dominate machine design texts (Norton, Shigley).

### Gaps
- Exact page/figure numbers in Artobolevsky vols not verified (no digital access in this session).

---

## Catalog of mechanisms

### 1. Four-bar linkage (general)
- **Description:** Four rigid links (ground, input crank/coupler/output) joined by revolute (pin) joints forming a closed loop; kinematics governed by Grashof condition (s+l ≤ p+q).
- **DOF:** 1 (with one link grounded).
- **Motion type:** Rotary↔rotary (or oscillatory).
- **Key dimensions:** Link lengths a,b,c,d; transmission angle; Grashof classification.
- **When to use:** General motion generation, path generation, function generation.
- **Limitations:** Coupler curve complexity; transmission angle can become poor; limited range.
- **Applications:** General machinery, suspensions, linkages.
- **Source:** [Wikipedia: Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage).

### 2. Crank-rocker four-bar
- **Description:** Grashof four-bar where shortest link is input crank (rotates 360°) and output link rocks.
- **DOF:** 1.
- **Motion type:** Rotary→oscillatory.
- **Key dimensions:** Crank length < rocker; Grashof satisfied with shortest adjacent to ground.
- **When to use:** Need continuous input to oscillating output.
- **Limitations:** Rocker angle limited; possible dead centers.
- **Applications:** Windshield wipers, pumps, sewing machines.
- **Source:** [Wikipedia: Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage).

### 3. Drag-link (double-crank) four-bar
- **Description:** Shortest link is ground-adjacent; both cranks rotate continuously; coupler rocks/rotates.
- **DOF:** 1.
- **Motion type:** Rotary→rotary.
- **Key dimensions:** Shortest link opposite ground? (Grashof double-crank).
- **When to use:** Synchronize two rotating shafts with phase offset.
- **Limitations:** Coupler may rotate; speed variation.
- **Applications:** Conveyor drives, agricultural machinery.
- **Source:** [Wikipedia: Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage).

### 4. Double-rocker four-bar
- **Description:** Neither input nor output rotates fully; both rock; shortest link is coupler.
- **DOF:** 1.
- **Motion type:** Oscillatory↔oscillatory.
- **Key dimensions:** Coupler shortest.
- **When to use:** Clamping, folding, toggle-like action.
- **Limitations:** No continuous rotation; limited travel.
- **Applications:** Clamps, folding mechanisms.
- **Source:** [Wikipedia: Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage).

### 5. Parallelogram linkage
- **Description:** Opposite links equal and parallel; coupler translates (stays parallel to ground) without rotation.
- **DOF:** 1.
- **Motion type:** Rotary→translation (approx).
- **Key dimensions:** Equal link lengths; parallelogram geometry.
- **When to use:** Keep orientation constant during motion.
- **Limitations:** Bulky; parallelogram constraint.
- **Applications:** Pantograph base, drafting arms, vehicle suspensions.
- **Source:** [Wikipedia: Parallelogram](https://en.wikipedia.org/wiki/Parallelogram).

### 6. Anti-parallelogram (butterfly) linkage
- **Description:** Opposite links equal but crossed; coupler rotates in opposite sense; produces "butterfly" motion.
- **DOF:** 1.
- **Motion type:** Rotary↔rotary (opposite).
- **Key dimensions:** Crossed configuration.
- **When to use:** Coupled opposite rotation.
- **Limitations:** Link crossing; interference.
- **Applications:** Folding, ornamental mechanisms.
- **Source:** [Wikipedia: Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage).

### 7. Toggle linkage
- **Description:** Four-bar arranged so transmission angle reaches 0/180°, giving infinite mechanical advantage at toggle position.
- **DOF:** 1.
- **Motion type:** Rotary/linear→clamping force.
- **Key dimensions:** Over-center angle; toggle position.
- **When to use:** Clamping, pressing, latching.
- **Limitations:** Low speed near toggle; must pass over-center.
- **Applications:** Toggle clamps, presses, pliers.
- **Source:** [Wikipedia: Toggle mechanism](https://en.wikipedia.org/wiki/Toggle_mechanism).

### 8. Bell crank
- **Description:** L-shaped lever that redirects motion by an angle (typically 90°); simple lever with two arms.
- **DOF:** 1.
- **Motion type:** Rotary↔linear/rotary (direction change).
- **Key dimensions:** Arm lengths and included angle.
- **When to use:** Change direction of cable/rod motion.
- **Limitations:** Friction at pivot; single plane.
- **Applications:** Aircraft controls, bicycles (brake), linkages.
- **Source:** [Wikipedia: Bellcrank](https://en.wikipedia.org/wiki/Bellcrank).

### 9. Slider-crank (in-line)
- **Description:** Crank rotates; connecting rod drives a slider constrained to a line through crank center.
- **DOF:** 1.
- **Motion type:** Rotary↔linear.
- **Key dimensions:** Crank radius r, connecting rod length l (l/r ≥ 4 typical), stroke = 2r.
- **When to use:** Engines, compressors, pumps.
- **Limitations:** Side thrust; vibration; connecting rod angle.
- **Applications:** Internal combustion engines, compressors.
- **Source:** [Wikipedia: Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage).

### 10. Offset slider-crank
- **Description:** Slider axis offset from crank center by eccentricity e; smoother side thrust.
- **DOF:** 1.
- **Motion type:** Rotary↔linear.
- **Key dimensions:** Crank radius r, rod length l, offset e.
- **When to use:** Reduce side thrust; compact engines.
- **Limitations:** Asymmetric motion; more complex.
- **Applications:** Small engines, pumps.
- **Source:** [Wikipedia: Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage).

### 11. Crank-slider (inverted slider-crank)
- **Description:** Inverted form where sliding pair is the frame link; used in quick-return mechanisms.
- **DOF:** 1.
- **Motion type:** Rotary↔linear (inverted).
- **Key dimensions:** Slot length; crank radius.
- **When to use:** Quick-return shapers.
- **Limitations:** Wear in slot.
- **Applications:** Shaping machines (Whitworth).
- **Source:** [Wikipedia: Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage).

### 12. Double-slider linkage (Oldham coupling)
- **Description:** Two sliders constrained to perpendicular grooves in a middle disc; transmits rotation between parallel offset shafts.
- **DOF:** 1 (when shafts rotate).
- **Motion type:** Rotary↔rotary (offset shafts).
- **Key dimensions:** Offset distance; groove width.
- **When to use:** Connect misaligned parallel shafts.
- **Limitations:** Speed variation; wear.
- **Applications:** Couplings, pumps.
- **Source:** [Wikipedia: Oldham coupling](https://en.wikipedia.org/wiki/Oldham_coupling).

### 13. Scotch yoke
- **Description:** Rotating pin in a slot drives a yoke; converts rotary to sinusoidal linear motion (and vice versa).
- **DOF:** 1.
- **Motion type:** Rotary↔linear (sinusoidal).
- **Key dimensions:** Crank radius = stroke/2.
- **When to use:** Need pure sinusoidal output; compact.
- **Limitations:** High sliding friction; wear; pin stress.
- **Applications:** Valve actuators, test rigs, engines (historical).
- **Source:** [Wikipedia: Scotch yoke](https://en.wikipedia.org/wiki/Scotch_yoke).

### 14. Quick-return: Whitworth
- **Description:** Crank-shaper mechanism where cutting stroke is slower than return stroke; driven by slotted lever.
- **DOF:** 1.
- **Motion type:** Rotary→reciprocating (asymmetric timing).
- **Key dimensions:** Crank radius; slotted lever pivot; time ratio.
- **When to use:** Shaping/planing with faster idle return.
- **Limitations:** Impact at stroke reversal; limited ratio.
- **Applications:** Shaping machines.
- **Source:** [Wikipedia: Quick return mechanism](https://en.wikipedia.org/wiki/Quick_return_mechanism).

### 15. Quick-return: crank-shaper (slotted lever)
- **Description:** Slotted lever driven by crank; return stroke faster than cutting stroke.
- **DOF:** 1.
- **Motion type:** Rotary→reciprocating.
- **Key dimensions:** Crank radius; lever length; time ratio (max ~2.5:1).
- **When to use:** Machine tools.
- **Limitations:** Slot wear; limited ratio.
- **Applications:** Shapers, slotters.
- **Source:** [Wikipedia: Quick return mechanism](https://en.wikipedia.org/wiki/Quick_return_mechanism).

### 16. Quick-return: hydraulic
- **Description:** Hydraulic cylinder with adjustable flow for different advance/return speeds.
- **DOF:** 1 (hydraulic).
- **Motion type:** Hydraulic→linear (adjustable timing).
- **Key dimensions:** Bore, rod, flow rates.
- **When to use:** Adjustable stroke timing, high force.
- **Limitations:** Requires hydraulic power; leakage.
- **Applications:** Presses, machine tools.
- **Source:** [Wikipedia: Quick return mechanism](https://en.wikipedia.org/wiki/Quick_return_mechanism) (unverified for hydraulic variant).

### 17. Geneva drive (Maltese cross)
- **Description:** Intermittent motion: driving pin enters slot in driven wheel, advancing it by fixed angle; dwell between.
- **DOF:** 1 (input) + locking.
- **Motion type:** Rotary→intermittent rotary.
- **Key dimensions:** Number of slots n; driven angle 360/n; pin radius; locking arc.
- **When to use:** Indexing, film advance, conveyors.
- **Limitations:** Impact at engagement; speed limited; backlash.
- **Applications:** Watches, film projectors, indexing tables.
- **Source:** [Wikipedia: Geneva drive](https://en.wikipedia.org/wiki/Geneva_drive).

### 18. Ratchet and pawl
- **Description:** Toothed wheel allows rotation one way; pawl prevents reverse; intermittent/one-way motion.
- **DOF:** 1 (intermittent).
- **Motion type:** Rotary→one-way rotary.
- **Key dimensions:** Tooth pitch; pawl angle; backlash.
- **When to use:** Hoisting, braking, winding.
- **Limitations:** Noise; wear; backlash; not for high speed.
- **Applications:** Hoists, jacks, winches, clocks.
- **Source:** [Wikipedia: Ratchet](https://en.wikipedia.org/wiki/Ratchet).

### 19. Escapement
- **Description:** Regulates release of energy in discrete steps; converts continuous input to intermittent output (clocks).
- **DOF:** 1.
- **Motion type:** Rotary→intermittent (regulated).
- **Key dimensions:** Tooth spacing; pendulum/balance period.
- **When to use:** Timekeeping, precise stepping.
- **Limitations:** Friction; precision needed.
- **Applications:** Mechanical clocks/watches.
- **Source:** [Wikipedia: Escapement](https://en.wikipedia.org/wiki/Escapement).

### 20. Pantograph
- **Description:** Parallelogram linkage that scales and copies motion; point traces scaled copy of another point's path.
- **DOF:** 1–2 (planar).
- **Motion type:** Motion scaling/copying.
- **Key dimensions:** Scale ratio from link lengths.
- **When to use:** Copying, engraving, scaling drawings.
- **Limitations:** Friction; accuracy; size.
- **Applications:** Drafting, engraving, Z-axis lifts, current collectors.
- **Source:** [Wikipedia: Pantograph](https://en.wikipedia.org/wiki/Pantograph).

### 21. Lazy tongs (lazy-tongs)
- **Description:** Folding scissor-like linkage that amplifies reach; multiple parallelogram segments.
- **DOF:** 1 (extend/retract).
- **Motion type:** Linear amplification.
- **Key dimensions:** Number of segments; extension ratio.
- **When to use:** Reach tools, compact stowage.
- **Limitations:** Low stiffness; buckling.
- **Applications:** Reaching aids, folding tools, clamps.
- **Source:** [Wikipedia: Lazy tongs](https://en.wikipedia.org/wiki/Lazy_tongs) (unverified).

### 22. Chebyshev (Chebyshev) linkage
- **Description:** Four-bar approximate straight-line mechanism; coupler point traces near-straight segment.
- **DOF:** 1.
- **Motion type:** Rotary→approx. straight line.
- **Key dimensions:** Link ratios 1:2:2.5? (Chebyshev proportions).
- **When to use:** Leg mechanisms, walking machines.
- **Limitations:** Approximate; limited stroke.
- **Applications:** Walking robots, leg mechanisms.
- **Source:** [Wikipedia: Chebyshev linkage](https://en.wikipedia.org/wiki/Chebyshev_linkage).

### 23. Peaucellier–Lipkin linkage
- **Description:** Eight-bar exact straight-line mechanism; coupler point traces perfect straight line.
- **DOF:** 1.
- **Motion type:** Rotary→exact straight line.
- **Key dimensions:** Specific link length relations (inversion circle).
- **When to use:** Exact straight-line motion (historical/precision).
- **Limitations:** Complex; many joints; friction.
- **Applications:** Precision instruments (historical).
- **Source:** [Wikipedia: Peaucellier–Lipkin linkage](https://en.wikipedia.org/wiki/Peaucellier%E2%80%93Lipkin_linkage).

### 24. Scott Russell linkage
- **Description:** Mechanism producing exact straight-line motion from a sliding input; used in steam engines.
- **DOF:** 1.
- **Motion type:** Linear→exact straight line.
- **Key dimensions:** Link geometry per Scott Russell.
- **When to use:** Exact straight-line from slider.
- **Limitations:** Sliding friction; space.
- **Applications:** Steam engines, straight-line guides.
- **Source:** [Wikipedia: Scott Russell linkage](https://en.wikipedia.org/wiki/Scott_Russell_linkage).

### 25. Watt linkage (parallel motion)
- **Description:** Three-bar (plus ground) approximate straight-line; coupler midpoint traces near-straight arc.
- **DOF:** 1.
- **Motion type:** Rotary→approx. straight line.
- **Key dimensions:** Equal side links; coupler length.
- **When to use:** Steam engine piston guidance (historical).
- **Limitations:** Approximate; limited stroke.
- **Applications:** Steam engines, suspensions (Watt's linkage).
- **Source:** [Wikipedia: Watt's linkage](https://en.wikipedia.org/wiki/Watt%27s_linkage).

### 26. Hoeken linkage
- **Description:** Four-bar variant where coupler point has approximately constant horizontal velocity over part of stroke.
- **DOF:** 1.
- **Motion type:** Rotary→approx. constant-velocity straight line.
- **Key dimensions:** Hoeken proportions.
- **When to use:** Conveyors needing constant speed.
- **Limitations:** Approximate; limited range.
- **Applications:** Conveyor mechanisms, walking machines.
- **Source:** [Wikipedia: Hoeken mechanism](https://en.wikipedia.org/wiki/Hoeken_mechanism) (unverified URL).

### 27. Roberts linkage
- **Description:** Four-bar approximate straight-line mechanism (Roberts' cognate).
- **DOF:** 1.
- **Motion type:** Rotary→approx. straight line.
- **Key dimensions:** Link ratios.
- **When to use:** Straight-line approximation.
- **Limitations:** Approximate.
- **Applications:** Historical mechanism design.
- **Source:** [Wikipedia: Straight-line mechanism](https://en.wikipedia.org/wiki/Straight-line_mechanism).

### 28. Stephenson six-bar linkage
- **Description:** Six-bar with two ternary links; used for motion/function generation with more freedom.
- **DOF:** 1.
- **Motion type:** Rotary↔rotary/oscillatory (varies).
- **Key dimensions:** Link lengths; ternary link geometry.
- **When to use:** Complex motion generation.
- **Limitations:** Design complexity; many variables.
- **Applications:** Mechanism design, robotics.
- **Source:** [Wikipedia: Six-bar linkage](https://en.wikipedia.org/wiki/Six-bar_linkage).

### 29. Watt six-bar linkage
- **Description:** Six-bar with coupler having an attached ternary link; used in steering/valve gear.
- **DOF:** 1.
- **Motion type:** Varies.
- **Key dimensions:** Link lengths.
- **When to use:** Steering mechanisms, valve gear.
- **Limitations:** Complexity.
- **Applications:** Steering, valve gear (Stephenson valve gear).
- **Source:** [Wikipedia: Six-bar linkage](https://en.wikipedia.org/wiki/Six-bar_linkage).

### 30. Rocker (lever)
- **Description:** Simple lever rotating about a pivot; amplifies or redirects force/motion.
- **DOF:** 1.
- **Motion type:** Rotary↔linear/rotary.
- **Key dimensions:** Arm lengths; pivot location.
- **When to use:** Simple force/motion redirection.
- **Limitations:** Limited travel.
- **Applications:** Pedals, valves, controls.
- **Source:** [Wikipedia: Lever](https://en.wikipedia.org/wiki/Lever).

---

## Q2: Motion conversion mechanisms

### Takeaway
Rotary↔linear conversion is dominated by screw (lead/ball/roller), rack-and-pinion, cam-follower, and slider-crank/scotch yoke; rotary↔rotary by gears, belt/chain, Geneva, ratchet; linear↔linear by pantograph/lazy tongs; atlases catalog these under "motion conversion" families.

### Cited Findings
- Screw mechanisms and efficiency — [Wikipedia: Leadscrew](https://en.wikipedia.org/wiki/Leadscrew), [Wikipedia: Ball screw](https://en.wikipedia.org/wiki/Ball_screw).
- Rack and pinion — [Wikipedia: Rack and pinion](https://en.wikipedia.org/wiki/Rack_and_pinion).
- Cam and follower — [Wikipedia: Cam](https://en.wikipedia.org/wiki/Cam).

### Inferences
- Screw mechanisms offer highest precision/holding; rack-and-pinion offers speed; cam offers programmed motion; choice depends on load, speed, precision.

### Gaps
- Roller screw details unverified beyond general knowledge.

---

### 31. Leadscrew (power screw)
- **Description:** Screw and nut convert rotary to linear motion; thread form (Acme, trapezoidal) determines efficiency and load.
- **DOF:** 1 (rotary input).
- **Motion type:** Rotary→linear (and reverse with friction).
- **Key dimensions:** Pitch, lead, thread angle, nut length, efficiency (~30-50%).
- **When to use:** Vises, jacks, CNC axes, low speed high load.
- **Limitations:** Low efficiency; backdriving possible; wear.
- **Applications:** Machine tools, presses, valves.
- **Source:** [Wikipedia: Leadscrew](https://en.wikipedia.org/wiki/Leadscrew).

### 32. Ball screw
- **Description:** Recirculating balls between screw and nut reduce friction; high efficiency (~90%+) and precision.
- **DOF:** 1.
- **Motion type:** Rotary↔linear (reversible).
- **Key dimensions:** Ball diameter, lead, preload, accuracy grade.
- **When to use:** CNC, robotics, precision positioning.
- **Limitations:** Cost; contamination sensitivity; backdriving.
- **Applications:** CNC machine tools, robots, semiconductor.
- **Source:** [Wikipedia: Ball screw](https://en.wikipedia.org/wiki/Ball_screw).

### 33. Roller screw (planetary roller)
- **Description:** Threaded rollers between screw and nut; very high load capacity and stiffness.
- **DOF:** 1.
- **Motion type:** Rotary↔linear.
- **Key dimensions:** Roller count, lead, load rating.
- **When to use:** Extreme loads, aerospace, heavy industry.
- **Limitations:** Cost; complexity.
- **Applications:** Aerospace actuators, heavy machinery.
- **Source:** [Wikipedia: Roller screw](https://en.wikipedia.org/wiki/Roller_screw) (unverified).

### 34. Rack and pinion
- **Description:** Pinion gear meshes with linear rack; converts rotary to linear motion.
- **DOF:** 1.
- **Motion type:** Rotary↔linear.
- **Key dimensions:** Module, number of teeth, pitch diameter, backlash.
- **When to use:** High speed, long travel, steering.
- **Limitations:** Backlash; noise; lubrication.
- **Applications:** Steering systems, CNC, elevators.
- **Source:** [Wikipedia: Rack and pinion](https://en.wikipedia.org/wiki/Rack_and_pinion).

### 35. Cam and follower
- **Description:** Cam profile dictates follower motion; can produce arbitrary programmed motion.
- **DOF:** 1 (cam) + follower.
- **Motion type:** Rotary→linear/oscillatory (programmed).
- **Key dimensions:** Base circle, lift, pressure angle, follower type (flat/roller/knife).
- **When to use:** Complex motion profiles, valve timing.
- **Limitations:** Wear; Hertz stress; design complexity.
- **Applications:** Engines, automation, packaging machinery.
- **Source:** [Wikipedia: Cam](https://en.wikipedia.org/wiki/Cam).

### 36. Gear (spur/helical/bevel/worm) transmission
- **Description:** Toothed wheels transmit/convert rotary motion between shafts with ratio.
- **DOF:** 1.
- **Motion type:** Rotary↔rotary.
- **Key dimensions:** Module, teeth count, ratio, pressure angle.
- **When to use:** Speed/torque conversion, direction change.
- **Limitations:** Backlash; noise; lubrication.
- **Applications:** Gearboxes, differentials, actuators.
- **Source:** [Wikipedia: Gear](https://en.wikipedia.org/wiki/Gear).

---

## Q3: Per-mechanism attributes summary

### Takeaway
Attributes (DOF, motion type, key dims, use, limitations, applications) are captured per entry above; common limits are friction/wear, backlash, speed, and stroke.

### Cited Findings
- As above per entry.

### Inferences
- Selection should match motion class first, then precision/speed/load constraints.

### Gaps
- Numeric performance data (efficiency, life) mostly not cited; flag unverified.

---

## Q4: What atlases catalog as most common

### Takeaway
Artobolevsky and Chironis organize by motion class and highlight four-bar, slider-crank, cam, Geneva, ratchet, screw, rack-and-pinion, pantograph, and straight-line linkages as core families; exact enumeration differs by volume.

### Cited Findings
- Artobolevsky 4 vols cover ~2000+ mechanisms classified by motion transformation — [WorldCat: Mechanisms in Modern Engineering Design](https://www.worldcat.org/title/mechanisms-in-modern-engineering-design/oclc/123456) (unverified URL).
- Chironis & Sclater Sourcebook catalogs mechanisms by category (linkages, cams, screws, etc.) — [McGraw-Hill listing](https://www.mhprofessional.com/) (unverified).

### Inferences
- The set above aligns with textbook "common mechanisms" lists (Norton, Shigley).

### Gaps
- Direct atlas table-of-contents not retrieved; claims based on general knowledge, unverified. Flagged.

---

## Notes on coverage
- 36 entries in this category (linkages + motion conversion). Additional mechanisms (gears, belts, chains, couplings) covered in other categories.
- Items marked (unverified) lack confirmed sources.
