# Indexing, Actuator, and Special Mechanisms Catalog

Compiled from Wikipedia mechanism articles, engineering references (Carr Lane, Elesa-Ganter, DESTACO, Halder, McMaster-Carr), patent literature (Google Patents), and robotics textbooks (Modern Robotics, Merlet). Unverified/uncited entries are flagged.

## Indexing and Locking Mechanisms

### Takeaway
Indexing and locking mechanisms convert continuous or arbitrary motion into discrete, repeatable positions (Geneva/Maltese cross, ratchet/pawl, star wheel, escapement) or provide positive retention (detent, toggle clamp, over-center, ball lock pin, bayonet, snap-fit, locking ring), trading speed/precision for simplicity and passive holding.

### Cited Findings
- Geneva drive translates continuous rotary motion into intermittent rotary motion, with a raised circular blocking disc that locks the driven wheel between steps — [Wikipedia](https://en.wikipedia.org/wiki/Geneva_drive); [Scribd](https://www.scribd.com/document/829452969/Geneva-and-Rachet-Wheel-1).
- Common Geneva applications: pen change in plotters, automated sampling, banknote counters, CNC tool changers, turret lathes/screw machines/turret drills, indexing heads and rotary tables, and film projection (precisely repeatable stopped position minimizes jitter) — [Wikipedia](https://en.wikipedia.org/wiki/Geneva_drive).
- Geneva drive (Maltese cross) has a driver with a pin engaging slots in the driven wheel; the locking disc prevents motion between steps; used where intermittent motion and precise stopped positions are needed — [Maltese cross paper](https://doi.org/10.3844/ajeassp.2018.891.900).
- Ratchet and pawl: one-directional incremental rotation; pawl spring-held against wheel; reversible pawl tooth shapes exist for bidirectional feed; overrunning clutch is a special form — [CMU mechanisms](https://www.cs.cmu.edu/~rapidproto/mechanisms/chpt8.html).
- Star-wheel ratchet: spring-loaded detent indexes a pointed rotor one step per stroke — [Firgelli](https://www.firgelliauto.com/blogs/mechanisms/star-wheel-ratchet).
- Ball detent vs ratchet: ratchet for one-directional (e.g., ratchet wrench); ball detent for incremental clockwise/counterclockwise indexing — [YouTube ratchet/detent](https://www.youtube.com/watch?v=qUkXTm1FJAw).
- Toggle clamp: over-center linkage; max clamping force when three pivots align (dead center); holding force FH in over-center lock position; force multiplication by toggle link principle; retracts for unobstructed loading — [Elesa-Ganter](https://www.elesa-ganter.com/siteassets/assets/PDF-Instructions/technical_annex/Toggle_Clamps_EN.pdf); [DESTACO](https://destaco.se/wp-content/uploads/2025/04/DESTACO-Manual-Tech-Cyl-25.pdf).
- Toggle clamp (patent US3347542A): hold-down lever actuated by reciprocal actuator; linkages linearly aligned at hold-down position rather than over-center for maximum force; concise configuration — [Google Patents](https://patents.google.com/patent/US3347542A/en).
- Over-center mechanism: three pivots, two fixed distances by rigid parts, third varies; dead-center position yields maximum force; built to rest in locked state — [Applied Mechanics (Jönköping)](https://mechanics.ju.se/Mechanisms/OverCentre.html).
- Snap-action mechanism (patent US2405014A): over-center spring and lever device for valves/switches; main and secondary levers fulcrumed and connected by spring; magnet can restrain secondary lever until sufficient spring tension — [Google Patents](https://patents.google.com/patent/US2405014A/en).
- Snap-on clamps: constant clamping force by spring pressure without tools; handle clicks at clamping end; spring force always constant, preventing over/under tightening — [Canadian Metalworking](https://www.canadianmetalworking.com/canadianmetalworking/product/metalworking/clamps-use-snap-on-system-to-provide-uniform-and-positive-clamping).
- Ball lock pin: high-strength quick-release alignment pin; positive locking until button pushed moves center spindle forward allowing locking balls to retract; single-acting (push to release) and double-acting (push or pull); diameters 3/16"–1" (5–20 mm), grip lengths up to 6" (150 mm); shear strengths ~2,100–200,000 N depending on size — [Carr Lane](https://www.carrlane.com/product/ball-lock-pins-quick-release-pins/ball-lock-pins/ball-lock-pins/ball-lock-pins-ring-handle); [Harcourt technical info](https://www.harcourt.co/overview_documents/Ball%20Lock%20Pins%20Technical%20Info.pdf).
- Quick-release pins (ring-grip): split ring folds down; pull to remove; retaining ball holds in place; vibration-resistant variants; locking variants push head to insert then pull ring to remove — [McMaster-Carr](https://www.mcmaster.com/products/quick-release-pins/fastener-head-type~ring/).
- Spring plunger / detent spring: spring-loaded pin/ball in hollow cylinder; eases indexing, positioning, securing; spring force keeps pin in position; ball plunger and spring plunger variants; hand-retractable and index plungers with tapered/rotary-cam versions — [Wikipedia](https://en.wikipedia.org/wiki/Spring_plunger); [Carr Lane](https://www.carrlane.com/engineering-resources/technical-information/manual-workholding/locating-devices/spring-loaded-devices); [Halder](https://www.halder.com/PM/Standard-Parts/Machine-and-Fixture-Elements/Spring-Plungers).
- Ball plunger in detent applications: engages corresponding detent/notch; holds until specified force applied to release; provides precise positioning and repeatability — [Monroe Engineering](https://monroeengineering.com/info-plunger-ball-plungers-how-they-function-in-detent-applications.php).
- Bayonet coupling: (no reliable source retrieved in this pass) — flagged unverified; commonly a twist-lock fastener with lugs engaging slots; applications: light bulbs, camera lenses, RF connectors.
- Locking ring / snap ring: (no reliable source retrieved) — flagged; retains components on shafts/bores.
- Cam lock: (no reliable source retrieved) — flagged; eccentric cam rotates to clamp.
- Maltese cross (Geneva) used in watches as stopwork to limit mainspring tension range, ensuring constant torque delivery to escapement — [Grail Watch](https://grailwatch.com/blogs/journal/history-and-uses-of-the-maltese-cross-mechanism-1).
- Escapement: maintains and counts oscillations of regulator; bistable elastic member (leaf spring in buckling) stores/releases energy; patent EP3475763B1 describes single exhaust mobile with winding star and locking wheel, trigger lever, bistable leaf spring — [Google Patents](https://patents.google.com/patent/EP3475763B1/en).
- Bistable compliant mechanisms: two stable equilibrium positions; energy stored in flexible segments; reduced part count; applied as switches/closures/hinges — [BYU bistable paper](https://www.et.byu.edu/~bdjensen/publications/byubistablepaper.pdf).

### Inferences
- Indexing precision trades off against speed: Geneva/star-wheel/escapement give discrete repeatable positions with mechanical locking, while ball-lock pins and spring plungers give fast manual reconfiguration.
- Over-center/toggle geometry is the common thread linking toggle clamps, snap-action, and (in reverse role) scissor-lift actuation force blow-up.

### Gaps
- No authoritative DOF/kinematic parameter tables retrieved for bayonet, cam lock, locking ring, snap-fit, detent, Maltese cross beyond Geneva; flagged as unverified.
- No quantitative force/stroke data for toggle clamps beyond manufacturer holding-force tables (not captured).

---

#### Indexing/Locking Mechanism Catalog (summary)

| Mechanism | DOF / Motion | Key Parameters | Advantages | Limitations | Typical Applications |
|---|---|---|---|---|---|
| Geneva (Maltese cross) drive | 1 DOF in (continuous rotary) → intermittent rotary out | Number of slots (typically 4, 6, 8); driver pin; locking disc diameter | Precise repeatable stops; simple; locks between steps | Impact loads at engagement; fixed step angle; not for high speed | Film projectors, CNC tool changers, turrets, rotary tables, plotters, banknote counters — [Wikipedia](https://en.wikipedia.org/wiki/Geneva_drive) |
| Ratchet & pawl | 1 DOF (unidirectional incremental rotary) | Tooth count; pawl spring force; tooth angle | Simple; one-way locking; high torque capacity | Noise; wear; no reverse without reversible pawl | Wrenches, winches, jacks, feed mechanisms, conveyor drives — [CMU](https://www.cs.cmu.edu/~rapidproto/mechanisms/chpt8.html) |
| Star-wheel ratchet | 1 DOF (incremental rotary per stroke) | Tooth count; detent spring force | Step per stroke; compact | Limited steps; backlash | Indexing tables, counters — [Firgelli](https://www.firgelliauto.com/blogs/mechanisms/star-wheel-ratchet) |
| Ball detent (indexing plunger) | Discrete angular positions | Ball diameter; spring force; notch count/spacing | Bidirectional indexing; simple | Wear; limited holding force | Rotary switches, indexing fixtures, tool turrets — [YouTube](https://www.youtube.com/watch?v=qUkXTm1FJAw) |
| Spring plunger / ball plunger | Linear spring-loaded detent | Spring force; stroke; tip shape (ball/pin/flat) | Repeatable positioning; quick release; screw-in install | Limited holding force; wear | Fixtures, indexing, locating, ejectors — [Wikipedia](https://en.wikipedia.org/wiki/Spring_plunger); [Carr Lane](https://www.carrlane.com/engineering-resources/technical-information/manual-workholding/locating-devices/spring-loaded-devices) |
| Index plunger (hand-retractable) | Positive locking at discrete holes | Taper 15°; rotary-cam retraction; shear strength | High holding force; positive lock | Manual operation | Machine setup, swiveling/sliding element locking — [Ganter](https://www.ganternorm.com/en/products/3.1-Indexing-locking-blocking-with-pins-and-ball-shaped-elements/Indexing-plungers) |
| Toggle clamp (over-center) | 1 DOF (binary: open/locked) | Link lengths; over-center travel; holding force FH; exerting force Fs | Force multiplication; positive lock; vibration resistant | Requires proper over-center design; high input force to unlock | Workholding, fixtures, presses — [Elesa-Ganter](https://www.elesa-ganter.com/siteassets/assets/PDF-Instructions/technical_annex/Toggle_Clamps_EN.pdf); [DESTACO](https://destaco.se/wp-content/uploads/2025/04/DESTACO-Manual-Tech-Cyl-25.pdf) |
| Snap-action (over-center spring) | 1 DOF (bistable toggle) | Spring stiffness; lever geometry; magnet restraint | Rapid switching; high impact force | Limited stroke; friction | Switches, valves, thermostats — [US2405014A](https://patents.google.com/patent/US2405014A/en) |
| Ball lock pin (quick-release) | Binary (locked/released) | Diameter 5–20 mm; grip length ≤150 mm; single/double acting | Fast; high shear strength; self-locking | Requires mating bushing/receptacle; cost | Fixtures, aerospace, marine, equipment changeover — [Carr Lane](https://www.carrlane.com/product/ball-lock-pins-quick-release-pins/ball-lock-pins/ball-lock-pins/ball-lock-pins-ring-handle) |
| Quick-release pin (ring-grip) | Binary | Diameter; grip length; material (steel/SS) | One-finger removal; low cost | Lower strength than ball-lock | General assembly, tight spaces — [McMaster-Carr](https://www.mcmaster.com/products/quick-release-pins/fastener-head-type~ring/) |
| Escapement | Intermittent (clock regulator) | Escape wheel teeth; bistable leaf spring; winding star | Precise timekeeping; impulse delivery | Complex; friction; isochronism sensitivity | Mechanical watches/clocks — [EP3475763B1](https://patents.google.com/patent/EP3475763B1/en) |
| Bistable compliant mechanism | 1 DOF (two stable states) | Flexure geometry; strain energy | Zero-power holding; low part count; no backlash | Limited stroke/rotation (flexures ~10–20°) | Switches, closures, hinges, grippers — [BYU](https://www.et.byu.edu/~bdjensen/publications/byubistablepaper.pdf); [compliantmechanisms.byu.edu](https://compliantmechanisms.byu.edu/about-compliant-mechanisms) |
| Bayonet coupling | Binary twist-lock | Lug count; slot geometry | Fast; positive lock; high torque | Requires alignment; wear | Light bulbs, lenses, connectors — *unverified* |
| Locking ring / snap ring | Retention | Groove diameter; material | Simple; low cost | Axial retention only | Shafts, bores, bearings — *unverified* |
| Cam lock | Binary | Eccentricity; cam profile | Quick clamp; adjustable | Limited force; wear | Furniture, cabinets, fixtures — *unverified* |
| Snap-fit | Binary (assembly/disassembly) | Interference; cantilever beam; material strain | Tool-free assembly; low cost | Plastic fatigue; one-time use often | Consumer products, enclosures — *unverified* |

## Actuators

### Takeaway
Actuators convert energy (hydraulic, pneumatic, electrical, thermal) into mechanical motion; selection trades force (hydraulic), speed/simplicity (pneumatic), precision/controllability (electric servo/stepper), and miniaturization/bandwidth (piezoelectric, SMA, bimetal, pneumatic muscle).

### Cited Findings
- Actuator: device converting energy into motion; sources electrical, pneumatic, hydraulic, thermal; types linear/rotary/solenoid/micro — [MK North America](https://www.mknorthamerica.com/Blog/an-engineers-guide-to-actuators-types-applications-and-selection-criteria); [Firgelli](https://www.firgelli.com/pages/actuators).
- Hydraulic actuator: pressurized fluid (oil) → linear motion via cylinder/piston; high force output and precise control; thousands of PSI possible — [LINAK](https://www.linak-us.com/products/linear-actuators/what-is-an-actuator); [Electromate](https://www.electromate.com/news/post/whats-the-difference-between-pneumatic-hydraulic-and-electrical-actuators).
- Pneumatic actuator: compressed air → linear or rotary motion via cylinders; faster speeds, simpler control; 80–120 PSI typical; less precise due to air compressibility — [LINAK](https://www.linak-us.com/products/linear-actuators/what-is-an-actuator); [YouTube linear actuator guide](https://www.youtube.com/watch?v=YzgFyO_W2nM&vl=en).
- Electric actuator: motors (stepper, servo, BLDC), solenoids, piezoelectric elements; highest precision/controllability; electric actuators replacing air cylinders for reduced downtime/energy/precision — [Tolomatic](https://www.tolomatic.com/info-center/resource-details/choosing-stepper-servo-actuators-to-replace-air-cylinders).
- Solenoid actuator: linear or rotary; electromagnetic coil drives plunger; fast on/off; simple — [Firgelli](https://www.firgelli.com/pages/actuators).
- Stepper motor: rotates in fixed increments/steps; precise open-loop control; excellent for low-speed, high-torque, high-repeatability — [Firgelli](https://www.firgelli.com/pages/actuators); [Tolomatic](https://www.tolomatic.com/info-center/resource-details/choosing-stepper-servo-actuators-to-replace-air-cylinders).
- Servo motor: closed-loop with feedback; high speed and force-sensitive applications; BLDC servo for higher speeds — [Tolomatic](https://www.tolomatic.com/info-center/resource-details/choosing-stepper-servo-actuators-to-replace-air-cylinders).
- Piezoelectric actuator: converse piezoelectric effect converts electrical energy to deformation; fast response, high stiffness, high power density, DC operation without lubrication/cooling; micro-motion actuator — [ejosat review](https://doi.org/10.31590/ejosat.653751); [Hollerbach/Hunter/Ballantyne comparative analysis](https://bdml.stanford.edu/twiki/pub/Main/PerchingLinks/Hollerbach_Hunter_Ballantyne_1992_A_Comparative_Analysis_of_Actuator_Technologies_for_Robotics.pdf).
- Shape memory alloy (SMA) actuator: recovers predetermined shape when heated (martensite→austenite); high energy density (up to 10 J/cm³), can lift >100× weight, 200 MPa actuating stress, 570× human muscle force, 25× EAP force; one-way/biased/two-way types; thermal (Joule heating) or magnetic activation — [ejosat review](https://doi.org/10.31590/ejosat.653751); [Wiley Advanced Materials review](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202208517); [MDPI SMA artificial muscle](https://www.mdpi.com/2076-0825/14/5/248).
- Thermal bimetal: (no reliable source retrieved this pass) — flagged; two metals with different CTE bonded; bends with temperature; used in thermostats.
- Pneumatic muscle (McKibben): pneumatic soft actuator contracting upon pressurization via braided sleeve; used in soft robots; artificial muscle — [IOP variable damping](https://iopscience.iop.org/article/10.1088/1361-665X/adf7ec); [SMA artificial muscle review](https://doi.org/10.1088/1361-665x/acf1e8).
- Artificial muscle taxonomy: dielectric elastomers, piezoelectric, IPMC, LCE, SMA, SMP, magnetic SMA, pneumatic (PAM), hydraulic; activated by pressure/thermal/photonic/magnetic/electric — [SMA review](https://doi.org/10.1088/1361-665x/acf1e8).
- Magnetostrictive actuators: micro-motion; high bandwidth — [comparative analysis](https://bdml.stanford.edu/twiki/pub/Main/PerchingLinks/Hollerbach_Hunter_Ballantyne_1992_A_Comparative_Analysis_of_Actuator_Technologies_for_Robotics.pdf).
- Magnetostrictive/EAP/polymeric actuators: promising new technologies; comparative analysis vs electromagnetic/hydraulic/pneumatic — [comparative analysis](https://bdml.stanford.edu/twiki/pub/Main/PerchingLinks/Hollerbach_Hunter_Ballantyne_1992_A_Comparative_Analysis_of_Actuator_Technologies_for_Robotics.pdf).

### Inferences
- Hydraulic dominates high-force/low-speed; pneumatic dominates high-speed/low-cost; electric (servo/stepper) dominates precision/repeatability; smart materials (piezo, SMA) dominate miniaturization and high-bandwidth micro-motion.

### Gaps
- No specific solenoid force/stroke or bimetal CTE data captured; flagged unverified where no source.

---

#### Actuator Catalog (summary)

| Actuator | Energy → Motion | Key Parameters | Advantages | Limitations | Typical Applications |
|---|---|---|---|---|---|
| Hydraulic cylinder | Pressurized oil → linear | Pressure (thousands PSI), bore, stroke, rod diameter | Very high force; precise; rigid | Leaks; maintenance; heavy; compressibility (slight) | Construction equipment, presses, aircraft flight surfaces, heavy machinery — [LINAK](https://www.linak-us.com/products/linear-actuators/what-is-an-actuator) |
| Pneumatic cylinder | Compressed air → linear/rotary | Pressure 80–120 PSI, bore, stroke | Fast; simple; low cost; clean | Low precision (compressible air); lower force | Automation, packaging, clamping, valves — [LINAK](https://www.linak-us.com/products/linear-actuators/what-is-an-actuator) |
| Solenoid | Electricity → linear/rotary (on/off) | Coil voltage, stroke, force | Fast switching; simple; compact | Short stroke; on/off only (proportional rare) | Valves, locks, relays, latches — [Firgelli](https://www.firgelli.com/pages/actuators) |
| Stepper motor | Electricity → discrete rotary | Step angle, holding torque, speed | Open-loop precision; no feedback needed | Torque drops with speed; resonance; stall | Printers, CNC, robotics, indexing — [Firgelli](https://www.firgelli.com/pages/actuators); [Tolomatic](https://www.tolomatic.com/info-center/resource-details/choosing-stepper-servo-actuators-to-replace-air-cylinders) |
| Servo motor (BLDC) | Electricity → rotary (closed-loop) | Torque, speed, encoder resolution | High speed; force-sensitive; precise | Cost; complexity; tuning | CNC, robotics, camera tracking — [Firgelli](https://www.firgelli.com/pages/actuators); [Tolomatic](https://www.tolomatic.com/info-center/resource-details/choosing-stepper-servo-actuators-to-replace-air-cylinders) |
| Piezoelectric | Electricity → micro displacement/force | Voltage, stroke (µm), blocking force, stiffness | µs response; high stiffness; no lubrication; DC | Small stroke; high voltage; brittle | Nanopositioning, inkjet, optics, micro-robotics — [ejosat](https://doi.org/10.31590/ejosat.653751) |
| Shape memory alloy (SMA) | Heat (Joule) → shape recovery | Transformation temps As/Af/Ms/Mf; strain 4–8%; stress 200 MPa | High energy density; large force/weight; compact; silent | Slow cooling; hysteresis; fatigue; low efficiency | Soft robots, wearable devices, biomedical, aerospace — [Wiley](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202208517); [MDPI](https://www.mdpi.com/2076-0825/14/5/248) |
| Thermal bimetal | Temperature → bending | CTE mismatch; thickness; geometry | Passive; no power; simple | Slow; low force; hysteresis | Thermostats, temperature switches — *unverified* |
| Pneumatic artificial muscle (McKibben) | Compressed air → contraction | Pressure, diameter, braid angle, length | High power/weight; compliant; soft | Nonlinear; hysteresis; fatigue of bladder | Soft robots, exoskeletons, prosthetics — [IOP](https://iopscience.iop.org/article/10.1088/1361-665X/adf7ec) |
| Magnetostrictive | Magnetic field → strain | Field strength, alloy (Terfenol-D) | High bandwidth; force | High cost; eddy currents | Sonar, precision positioning — [comparative](https://bdml.stanford.edu/twiki/pub/Main/PerchingLinks/Hollerbach_Hunter_Ballantyne_1992_A_Comparative_Analysis_of_Actuator_Technologies_for_Robotics.pdf) |

## Special Mechanisms

### Takeaway
Special mechanisms include motion-scaling linkages (pantograph, lazy tongs, scissor lift), straight-line generators (Watt, Chebyshev, Peaucellier, Scott Russell, Hoeken), compliant mechanisms (flexure hinges, bistable, grippers), parallel robots (delta, Stewart), and energy/force-conditioning devices (constant-force, over-center, snap-action).

### Cited Findings
- Pantograph: parallelogram linkage scaling motion; used for copying/enlarging drawings, sculpting, minting, engraving, milling; pantograph mirror shown — [Wikipedia](https://en.wikipedia.org/wiki/Pantograph); [Scissors mechanism](https://en.wikipedia.org/wiki/Scissor_mechanism).
- Scissor mechanism / scissor lift: crossed X-pattern links; vertical motion; can be hydraulic/pneumatic/mechanical; used in lifts, folding tables, keyboard mechanisms; pantograph family — [Wikipedia](https://en.wikipedia.org/wiki/Scissor_mechanism); [Handling.com](https://handling.com/guide/scissor-lift-mechanism/).
- Scissor lift force: actuator force largest near fully collapsed position due to low mechanical advantage; links form parallelograms; sliding joints needed; thin links buckle under compression — [LivePhysics](https://livephysics.com/infographics/robotics-scissor-lift-mechanism/).
- Lazy tongs: motion multiplier; parallelogram-based; used in scissor lifts — [Applied Mechanics (Jönköping)](https://mechanics.ju.se/Mechanisms/Parallelograms.html); [Notes & Sketches](https://www.notesandsketches.co.uk/PDF/Scissors_lift.pdf).
- Pantograph scales motion; lazy tongs multiply motion; parallelogram keeps part parallel to itself — [Applied Mechanics](https://mechanics.ju.se/Mechanisms/Parallelograms.html).
- Four-bar linkage: simplest closed-chain movable linkage; four bars, four revolute joints, one fixed; planar/spherical/spatial variants; classifications: crank-rocker, double-crank, double-rocker, parallelogram, anti-parallelogram; Grashof criterion determines mobility — [Wikipedia](https://en.wikipedia.org/wiki/Four-bar_linkage); [3D Mechanism](https://www.3dmechanism.com/post/four-bar-linkage-mechanism-explained).
- Straight-line mechanisms: convert rotary/angular to straight-line motion; approximate (Watt, Chebyshev, Roberts, Evans/Horse-head) and exact (Peaucellier-Lipkin, Scott Russell) using only revolute joints (except Hoecken needs sliding joint) — [Wikipedia](https://en.wikipedia.org/wiki/Straight-line_mechanism); [Ohio University atlas](https://people.ohio.edu/williams/html/PDF/MechanismAtlas.pdf).
- Watt linkage (1784): approximate straight line; point P on coupler traces lemniscate of Bernoulli; used to guide steam-engine piston (~1.2 m stroke); also car suspensions; optimal when cranks parallel and perpendicular to coupler, angular amplitude ≤20° — [Portuguese thesis excerpt](https://repositorium.uminho.pt/bitstreams/6be08a4a-fee4-44ac-94ea-ba4aff224b9e/download).
- Watt's parallel motion: combines Watt's linkage with pantograph to amplify approximate straight-line movement — [Wikipedia straight-line](https://en.wikipedia.org/wiki/Straight-line_mechanism).
- Chebyshev linkage: approximate straight line; Chebyshev lambda linkage is cognate — [Wikipedia](https://en.wikipedia.org/wiki/Straight-line_mechanism).
- Peaucellier-Lipkin: exact straight-line motion (first such mechanism, 1864); most popular exact straight-line linkage — [Ohio atlas](https://people.ohio.edu/williams/html/PDF/MechanismAtlas.pdf); [Portuguese thesis](https://repositorium.uminho.pt/bitstreams/6be08a4a-fee4-44ac-94ea-ba4aff224b9e/download).
- Scott Russell: exact straight-line motion; transforms rectilinear motion to perpendicular rectilinear motion; AB=BC=BP/2 relation; also called Evans/grasshopper mechanism — [Portuguese thesis](https://repositorium.uminho.pt/bitstreams/6be08a4a-fee4-44ac-94ea-ba4aff224b9e/download).
- Hoeken linkage (1926): requires sliding joint; approximate straight line — [Wikipedia](https://en.wikipedia.org/wiki/Straight-line_mechanism); [Rector blog](https://blog.rectorsquid.com/sample-linkage-mechanisms-2).
- Compliant mechanism: gains mobility from elastic deformation of flexible members rather than movable joints; monolithic; no backlash/wear; can be fabricated flat (stamping, laser/water-jet, 3D printing); flexure hinges; compliant grippers — [BYU compliant mechanisms](https://compliantmechanisms.byu.edu/about-compliant-mechanisms); [ScienceDirect](https://www.sciencedirect.com/topics/engineering/compliant-mechanism).
- Flexure hinge: compliant joint; typical flexure joints limited to 10–20° rotation — [Reddit ME](https://www.reddit.com/r/MechanicalEngineering/comments/q1n8w9/compliant_mechanismsim_a_little_obsessed_right_now).
- Compliant gripper: monolithic, no actuators/sensors in passive designs; 5-DOF flexure gripper for pick-and-place/insertion; inverted flexure for large jaw rotation — [Academia.edu](https://www.academia.edu/Documents/in/Compliant_Mechanism).
- Delta robot: parallel robot; 3 DOF translation (4-DOF variant adds rotation); invented 1980s by Reymond Clavel (EPFL); parallelograms maintain end-effector orientation; actuators in base → light moving parts → high speed (up to 300 picks/min); used in packaging, PCB placement, medical (Surgiscope), haptics, 3D printing; US patent 4,976,582 — [Wikipedia](https://en.wikipedia.org/wiki/delta_robot).
- Stewart platform (Gough-Stewart): 6 DOF; six linear actuators (prismatic) with spherical/universal joints; flight simulators, 6-axis force-torque sensors; high load/weight ratio; invented ~1949 (Gough) / 1965 (Stewart) — [Modern Robotics](https://modernrobotics.northwestern.edu/nu-gm-book-resource/kinematics-of-closed-chains/); [Wikipedia parallel robot](https://en.wikipedia.org/wiki/Parallel_robot); [Merlet](https://www-sop.inria.fr/coprin/PDF/merlet_rsj92.pdf).
- Parallel robot: moving platform connected to base by multiple actuated legs; inverse kinematics often straightforward, forward kinematics complex (up to 6 solutions for 3×RPR); singularities — [Modern Robotics](https://modernrobotics.northwestern.edu/nu-gm-book-resource/kinematics-of-closed-chains/).
- Constant-force mechanism: delivers constant force over large displacement; constant-force spring (spiral band) unwinds at nearly constant force; used for gravity compensation/balancing (Anglepoise lamp, zero-free-length spring); counterweight/pantograph/cam-spring/magnetic variants — [PMC exoskeleton](https://pmc.ncbi.nlm.nih.gov/articles/PMC10754060/); [MDPI gravity compensation review](https://www.mdpi.com/2076-0825/15/2/111); [Constant force spring physics](https://physicslabs.colorado.edu/demos/mechanics/newtons-second-law/force-mass-and-acceleration/constant-force-spring/).
- Constant-force spring: thin band of spring steel tightly wound on spool; unwinding force nearly constant after initial extension; friction <2.6%; force fluctuation <8.6% — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10754060/).
- Anglepoise lamp balancing: zero-free-length spring (stiffness k = mgr/bc) gives exact balance; George Carwardine 1931–35 patents — [Proc. Inst. Mech. Eng.](https://doi.org/10.1243/0954406001523137).
- Over-center mechanism (special role): in scissor lift, actuator force grows without bound as lift folds flat; toggle in reverse role — [Applied Mechanics](https://mechanics.ju.se/Mechanisms/OverCentre.html).
- Snap-action: over-center spring/lever; used in switches/valves; magnetic restraint variant — [US2405014A](https://patents.google.com/patent/US2405014A/en).

### Inferences
- Exact straight-line mechanisms (Peaucellier, Scott Russell) need more links than approximate ones (Watt, Chebyshev) but eliminate prismatic joints' friction/wear.
- Parallel robots trade workspace for stiffness/speed; delta for high-speed pick-and-place, Stewart for 6-DOF simulation.

### Gaps
- No detailed kinematic equations/DOF for pantograph, lazy tongs, scissor lift stages retrieved beyond general descriptions.
- No source for thermal bimetal specifics or bayonet/cam lock/snap-fit/locking ring details.

---

#### Special Mechanism Catalog (summary)

| Mechanism | DOF / Motion | Key Parameters | Advantages | Limitations | Typical Applications |
|---|---|---|---|---|---|
| Pantograph | 1 DOF (scaled copy) | Arm lengths; scale ratio | Exact scaling; simple | Planar only (basic); bulk | Drafting, engraving, milling, sculpting — [Wikipedia](https://en.wikipedia.org/wiki/Pantograph) |
| Lazy tongs | 1 DOF (multiplied extension) | Number of stages; link length | Large extension from compact | Low stiffness; side-load sensitive | Scissor lifts, reach tools — [Notes & Sketches](https://www.notesandsketches.co.uk/PDF/Scissors_lift.pdf) |
| Scissor lift | 1 DOF (vertical) | Link length; stage count; angle | Compact fold; stable platform | Force ∞ near flat; side loads dangerous | Aerial work platforms, tables, jacks — [Wikipedia](https://en.wikipedia.org/wiki/Scissor_mechanism) |
| Four-bar linkage (variants) | 1 DOF | Link lengths; Grashof condition | Versatile; simple | Coupler curve complexity; transmission angle | Engines, suspensions, robotics — [Wikipedia](https://en.wikipedia.org/wiki/Four-bar_linkage) |
| Watt linkage | 1 DOF (approx. straight line) | Crank/coupler lengths; ≤20° amplitude | Few parts; widely used | Approximate only | Steam engines, car suspensions — [thesis](https://repositorium.uminho.pt/bitstreams/6be08a4a-fee4-44ac-94ea-ba4aff224b9e/download) |
| Chebyshev linkage | 1 DOF (approx. straight line) | Link ratios | Better straightness over stroke | Approximate | Machine tools — [Wikipedia](https://en.wikipedia.org/wiki/Straight-line_mechanism) |
| Peaucellier-Lipkin | 1 DOF (exact straight line) | 8 links; inversion circle | Exact; no prismatic joint | More parts; bulk | Precision instruments — [Ohio atlas](https://people.ohio.edu/williams/html/PDF/MechanismAtlas.pdf) |
| Scott Russell | 1 DOF (exact straight line, perpendicular) | AB=BC=BP/2 | Exact; perpendicular conversion | Long guide link needed | Steam engines, locomotives — [thesis](https://repositorium.uminho.pt/bitstreams/6be08a4a-fee4-44ac-94ea-ba4aff224b9e/download) |
| Hoeken | 1 DOF (approx. straight line) | Sliding joint | Good accuracy | Requires prismatic joint | Machine tools — [Wikipedia](https://en.wikipedia.org/wiki/Straight-line_mechanism) |
| Compliant mechanism / flexure hinge | 1 DOF (elastic) | Flexure thickness/length; material | No backlash/wear; monolithic; precise | Limited stroke (10–20°); fatigue | Precision stages, MEMS, grippers — [BYU](https://compliantmechanisms.byu.edu/about-compliant-mechanisms) |
| Compliant gripper | 1+ DOF (elastic) | Jaw rotation; mechanical advantage | Monolithic; passive alignment | Buckling; stress | Pick-and-place, surgery — [Academia](https://www.academia.edu/Documents/in/Compliant_Mechanism) |
| Delta robot | 3 DOF (4-DOF variant) | Arm length; base size | Very fast; high stiffness/weight | Small workspace; parallel singularities | Packaging, PCB, medical, haptics, 3D printing — [Wikipedia](https://en.wikipedia.org/wiki/delta_robot) |
| Stewart platform | 6 DOF | Leg lengths; joint types (S/U) | Full 6-DOF; high load/weight | Complex kinematics; small workspace | Flight simulators, force-torque sensors — [Wikipedia](https://en.wikipedia.org/wiki/Parallel_robot); [Modern Robotics](https://modernrobotics.northwestern.edu/nu-gm-book-resource/kinematics-of-closed-chains/) |
| Constant-force mechanism | 1 DOF (constant F) | Spring geometry; cam profile; counterweight | Gravity compensation; neutral equilibrium | Complexity; stroke limits | Lamps, exoskeletons, elevators, windows — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10754060/); [MDPI](https://www.mdpi.com/2076-0825/15/2/111) |
| Over-center (special) | 1 DOF (bistable) | Pivot alignment; spring | Positive lock; force amplification | Unlock force; vibration sensitivity | Clamps, switches, lifts — [Applied Mechanics](https://mechanics.ju.se/Mechanisms/OverCentre.html) |
| Snap-action | 1 DOF (bistable) | Spring stiffness; lever geometry | Rapid switching; high impact | Limited stroke | Switches, valves, thermostats — [US2405014A](https://patents.google.com/patent/US2405014A/en) |

## References (consolidated)
- Wikipedia: Geneva drive, Four-bar linkage, Straight-line mechanism, Scissor mechanism, Pantograph, Spring plunger, Delta robot, Parallel robot — https://en.wikipedia.org
- Applied Mechanics (Jönköping University): Over-centre, Straight-line, Parallelograms/pantographs/scissors, Spring balancing — https://mechanics.ju.se/Mechanisms/
- Modern Robotics (Lynch & Park): Kinematics of closed chains — https://modernrobotics.northwestern.edu
- Merlet: Parallel manipulators — https://www-sop.inria.fr/coprin/PDF/merlet_rsj92.pdf
- Ohio University mechanism atlas — https://people.ohio.edu/williams/html/PDF/MechanismAtlas.pdf
- Patent US2405014A (snap action), US3347542A (toggle clamp), EP3475763B1 (escapement), US4976582 (delta robot) — https://patents.google.com
- Carr Lane, Elesa-Ganter, DESTACO, Halder, McMaster-Carr, Firgelli, Monroe Engineering — manufacturer technical resources
- BYUI/Stanford comparative actuator analysis — https://bdml.stanford.edu
- Compliant mechanisms (BYU) — https://compliantmechanisms.byu.edu
- MDPI reviews (SMA artificial muscle, gravity compensation) — https://www.mdpi.com
- PMC (constant-force springs) — https://pmc.ncbi.nlm.nih.gov
- IOP (pneumatic muscle/SMA damping) — https://iopscience.iop.org