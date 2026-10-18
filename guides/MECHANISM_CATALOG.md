# ThinkToCad Master Mechanism Catalog

Pointer/guide index for the ThinkToCad mechanical knowledge base. Lists every mechanism captured in the research notes (`research_notes/Top 200 mechanisms catalog/`) with a snake_case id, one-line description, motion/function, selection guidance, and key constraint. Detailed per-mechanism entries (geometry, sizing, failure modes, when-to-use) live in `knowledge/mechanisms/*.md` (65 exist today; more to be added).

All text is ASCII. Counts are approximate; mechanisms flagged "(unverified)" lack a confirmed source in the research notes.

---

## 1. Purpose and how to use this catalog

- Use this file as the **first stop** when a design requirement names a motion, force, or function ("I need rotary to linear", "I need to index 6 positions", "I need overload protection").
- Step 1: Read section 2 (AI selection rules) and the relevant category table(s).
- Step 2: Match the requirement's motion class and constraints to candidate ids.
- Step 3: Open the detailed entry in `knowledge/mechanisms/<id>.md` for sizing, constraints, and failure modes. If no detailed file exists yet, the research notes and cited sources are the next reference.
- Step 4: When adding a new mechanism, append a row here AND create `knowledge/mechanisms/<id>.md` following the `spacer_sleeve.md` format (Type, Function, How it works, Constraints, Failure modes, When to use).

Conventions:
- `id` is snake_case and unique across the catalog.
- Motion type uses `->` for conversion (e.g. `rotary -> linear`); `<->` for bidirectional.
- "When to select" is 1-2 lines; "Key constraint" is the dominant limitation.

---

## 2. AI selection rules (how to pick a mechanism from a requirement)

1. **Classify the motion first.** Determine input motion, output motion, and conversion (rotary<->linear, rotary<->rotary, linear<->linear, intermittent, scaling, holding). Filter candidates by motion class before considering performance.
2. **Match the function.** Transmission (gears/belts/chains/screws), conversion (linkages/cams/screws), indexing/locking (Geneva, ratchet, detent, toggle), actuation (hydraulic/pneumatic/electric/smart material), or joining/fastening/bearing.
3. **Apply hard constraints early.** Space envelope, shaft angle (parallel/crossed/skew/90 deg), self-locking need, zero-backlash need, speed, torque, precision, environment (dirty/wet/vacuum/high-temp), cost, serviceability.
4. **Prefer the simplest mechanism that satisfies the motion class** (e.g. spur gear before harmonic drive; leadscrew before ball screw) unless precision/speed/backlash demands otherwise.
5. **Check limitations against the application.** Backlash, wear, lubrication, contamination sensitivity, temperature limits, fatigue life, assembly access.
6. **Verify with manufacturer data** for rated torque, misalignment, life (L10 for bearings), and safety factors (typically 1.25-2.3 for industrial drives). This catalog gives guidance, not ratings.
7. **Prefer detailed entries.** If `knowledge/mechanisms/<id>.md` exists, use it; otherwise flag the mechanism as needing a detailed entry.
8. **Avoid duplicates.** Some mechanisms appear in multiple families (e.g. rack-and-pinion is both a gear and a converter); the primary home is noted in its category; cross-references are given in section 4.

---

## 3. Categories with mechanism tables

### 3.1 Linkages & motion conversion

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| four_bar_linkage | Four rigid links in a closed loop; kinematics governed by Grashof condition (s+l <= p+q). | rotary <-> rotary / oscillatory | General motion/path/function generation. | Coupler curve complexity; transmission angle can become poor. |
| crank_rocker_four_bar | Grashof four-bar with shortest link as input crank (360 deg) and output link rocking. | rotary -> oscillatory | Continuous input to oscillating output. | Rocker angle limited; possible dead centers. |
| drag_link_four_bar | Shortest link ground-adjacent; both cranks rotate continuously. | rotary -> rotary (phase offset) | Synchronize two rotating shafts with phase offset. | Coupler may rotate; speed variation. |
| double_rocker_four_bar | Neither input nor output rotates fully; both rock; shortest link is coupler. | oscillatory <-> oscillatory | Clamping, folding, toggle-like action. | No continuous rotation; limited travel. |
| parallelogram_linkage | Opposite links equal and parallel; coupler translates without rotation. | rotary -> translation (approx) | Keep orientation constant during motion. | Bulky; parallelogram constraint. |
| anti_parallelogram_linkage | Opposite links equal but crossed; coupler rotates in opposite sense. | rotary <-> rotary (opposite) | Coupled opposite rotation. | Link crossing; interference. |
| toggle_linkage | Four-bar arranged so transmission angle reaches 0/180 deg, giving infinite mechanical advantage at toggle. | rotary/linear -> clamping force | Clamping, pressing, latching. | Low speed near toggle; must pass over-center. |
| bell_crank | L-shaped lever redirecting motion by an angle (typically 90 deg). | rotary <-> linear/rotary (direction change) | Change direction of cable/rod motion. | Friction at pivot; single plane. |
| slider_crank_inline | Crank rotates; connecting rod drives slider constrained to a line through crank center. | rotary <-> linear | Engines, compressors, pumps. | Side thrust; vibration; rod angle. |
| offset_slider_crank | Slider axis offset from crank center by eccentricity e. | rotary <-> linear | Reduce side thrust; compact engines. | Asymmetric motion; more complex. |
| inverted_slider_crank | Inverted form where sliding pair is the frame link. | rotary <-> linear (inverted) | Quick-return shapers. | Wear in slot. |
| double_slider_linkage | Two sliders in perpendicular grooves in a middle disc (Oldham). | rotary <-> rotary (offset shafts) | Connect misaligned parallel shafts. | Speed variation; wear. |
| scotch_yoke | Rotating pin in a slot drives a yoke; sinusoidal linear motion. | rotary <-> linear (sinusoidal) | Pure sinusoidal output; compact. | High sliding friction; wear; pin stress. |
| quick_return_whitworth | Crank-shaper; cutting stroke slower than return stroke via slotted lever. | rotary -> reciprocating (asymmetric) | Shaping/planing with faster idle return. | Impact at reversal; limited ratio. |
| quick_return_crank_shaper | Slotted lever driven by crank; return faster than cutting. | rotary -> reciprocating | Machine tools. | Slot wear; limited ratio (~2.5:1). |
| quick_return_hydraulic | Hydraulic cylinder with adjustable flow for different advance/return speeds. | hydraulic -> linear (adjustable) | Adjustable stroke timing, high force. | Requires hydraulic power; leakage. |
| geneva_drive | Intermittent motion: driving pin enters slot in driven wheel; dwell between steps; locking disc. | rotary -> intermittent rotary | Indexing, film advance, conveyors, tool changers. | Impact at engagement; speed limited; backlash. |
| ratchet_and_pawl | Toothed wheel allows rotation one way; pawl prevents reverse. | rotary -> one-way rotary | Hoisting, braking, winding, feed. | Noise; wear; backlash; not high speed. |
| escapement | Regulates release of energy in discrete steps; converts continuous input to intermittent output. | rotary -> intermittent (regulated) | Timekeeping, precise stepping. | Friction; precision needed. |
| pantograph | Parallelogram linkage that scales/copies motion. | motion scaling/copying | Copying, engraving, scaling drawings, lifts. | Friction; accuracy; size. |
| lazy_tongs | Folding scissor-like linkage amplifying reach; multiple parallelogram segments. | linear amplification | Reach tools, compact stowage. | Low stiffness; buckling. |
| chebyshev_linkage | Four-bar approximate straight-line mechanism. | rotary -> approx. straight line | Leg mechanisms, walking machines. | Approximate; limited stroke. |
| peaucellier_lipkin_linkage | Eight-bar exact straight-line mechanism. | rotary -> exact straight line | Exact straight-line motion (precision). | Complex; many joints; friction. |
| scott_russell_linkage | Exact straight-line motion from a sliding input. | linear -> exact straight line | Exact straight-line from slider. | Sliding friction; space. |
| watt_linkage | Three-bar approximate straight-line; coupler midpoint traces near-straight arc. | rotary -> approx. straight line | Steam engine piston guidance, suspensions. | Approximate; limited stroke. |
| hoeken_linkage | Four-bar variant with approximately constant horizontal velocity over part of stroke. | rotary -> approx. constant-velocity straight line | Conveyors needing constant speed. | Approximate; limited range. |
| roberts_linkage | Four-bar approximate straight-line mechanism. | rotary -> approx. straight line | Straight-line approximation. | Approximate. |
| stephenson_six_bar | Six-bar with two ternary links for motion/function generation. | rotary <-> rotary/oscillatory (varies) | Complex motion generation. | Design complexity; many variables. |
| watt_six_bar | Six-bar with coupler having attached ternary link. | varies | Steering mechanisms, valve gear. | Complexity. |
| rocker_lever | Simple lever rotating about a pivot; amplifies/redirects force/motion. | rotary <-> linear/rotary | Simple force/motion redirection. | Limited travel. |
| star_wheel_ratchet | Spring-loaded detent indexes a pointed rotor one step per stroke. | incremental rotary per stroke | Indexing tables, counters. | Limited steps; backlash. |
| scissor_lift | Crossed X-pattern links producing vertical motion (pantograph family). | rotary/hydraulic -> vertical linear | Aerial work platforms, tables, jacks. | Force grows unbounded near fully collapsed; side loads dangerous. |

### 3.2 Cams & followers

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| plate_cam | Cut from flat plate; follower moves in plane perpendicular to camshaft axis; most common. | rotary -> linear/oscillatory (programmed) | Simple rotary->reciprocating at moderate speed. | Wear; Hertz stress; design complexity. |
| cylindrical_barrel_cam | Follower rides in groove cut into cylinder surface; positive positioning (no spring needed). | rotary -> linear (perp. to axis) | Multi-groove, sequential motion, machine-tool drives. | Groove manufacturing; follower wear. |
| constant_lead_barrel_cam | Follower position linear with rotation (like a lead screw). | rotary -> linear (constant lead) | Lathe threading cross-slide settings. | Limited to linear profile. |
| cylindrical_cam_two_inputs | Output radial to cylinder; supports two inputs. | multi-input -> radial output | Naval gun fire-control, analog computers (legacy). | Complex; obsolete for most uses. |
| face_cam | Follower rides on face of a disk, often in a slot (captive, positive positioning). | rotary -> linear (parallel to axis) | Repetitive motion, function generation, scroll chucks. | Wear; slot manufacturing. |
| heart_shaped_cam | Symmetric heart returns a shaft to a set position by roller pressure. | rotary -> return-to-set position | Clock synchronization, reset mechanisms. | Specialized; limited applications. |
| snail_drop_cam | Follower raised over 24 h in spiral path terminating in sharp cutoff (drop). | rotary -> timed drop | Clocking-in clocks, day-advance. | Precision needed; wear. |
| linear_cam | Cam element moves in a straight line; input is linear motion. | linear -> linear/oscillatory | Pin-tumbler locks, key-duplication machines. | Wear; limited stroke. |
| globoidal_cam | Hourglass-shaped cam for high-speed indexing/conjugate drives. (unverified) | rotary -> intermittent rotary | High-speed indexing. | Complex geometry; cost. |
| conjugate_dual_cam | Paired cams with two followers to eliminate backlash/clearance. (unverified) | rotary -> precise linear/oscillatory | Precision motion. | Complexity; cost. |
| preloaded_cam | Spring-preloaded follower maintaining contact to avoid jump. (unverified) | rotary -> linear/oscillatory | High-speed cams needing contact. | Spring fatigue; design. |
| cam_follower | Specialized roller/needle bearing following cam lobes; stud or yoke style; shapes: knife-edge, roller, flat-faced, spherical, mushroom, oscillating. | follows cam profile | Reduce wear vs knife-edge/flat at high load/speed. | Load/speed limits; misalignment tolerance (~0.5 deg crowned). |

### 3.3 Gears & gear trains

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| spur_gear | Cylindrical gear with straight teeth parallel to axis; parallel shafts only. | rotary <-> rotary | Low cost, moderate speed, parallel shafts. | Noisy at high speed; no axial thrust. |
| helical_gear | Angled teeth; smoother/quieter; parallel or crossed. | rotary <-> rotary | Smoother/quieter parallel or crossed shafts. | Axial thrust (needs thrust bearing). |
| internal_gear | Teeth point inward; nested with external pinion; both same sense. | rotary <-> rotary | Planetary ring gears, compact drives. | Assembly; center distance fixed. |
| crown_gear | Teeth project at right angles to plane; meshes with escapements/clocks. | rotary <-> rotary (90 deg) | Clocks, escapements, low-speed bevel. | Low speed (<5 m/s small gears). |
| bevel_gear_straight | Intersecting axes (typically 90 deg); conical pitch surface. | rotary <-> rotary (intersecting axes) | Change shaft angle under load, 90 deg. | Matched pairs; precise mounting; noise at speed. |
| spiral_bevel_gear | Bevel gear with curved (helical) teeth; less vibration/noise. | rotary <-> rotary (intersecting axes) | Quiet high-speed 90 deg drives. | Replaced in pairs; cost. |
| hypoid_gear | Spiral bevel with non-intersecting (skew) axes; hyperbolic pitch surface. | rotary <-> rotary (skew axes) | Automotive final drives, railcar transmissions. | Special EP oil; efficiency trade-off with offset. |
| worm_drive | Worm meshes worm wheel; 90 deg axes; compact high reduction; self-locking possible. | rotary <-> rotary (90 deg, high ratio) | Compact high ratio; self-locking; cost. | Low efficiency at high ratio; not back-drivable. |
| planetary_epicyclic_gear | Sun, planet(s), carrier, ring; coaxial I/O; three-shaft device. | rotary <-> rotary (coaxial) | Automatic transmissions, high torque density, multiple inputs. | Complexity; assembly constraints. |
| rack_and_pinion | Circular pinion meshes linear rack. | rotary <-> linear | High speed, long travel, steering. | Backlash; noise; lubrication. |
| face_gear | Cylindrical pinion meshes disk with teeth on face. (unverified) | rotary <-> rotary | Special 90 deg drives. | Limited sources; verify. |
| harmonic_drive | Strain-wave gearing: wave generator, flexspline, circular spline; zero backlash. | rotary <-> rotary (high ratio, coaxial) | Robotics, aerospace, precision. | Flexspline fatigue limits torque; cost. |
| cycloidal_drive | Eccentric input drives cycloidal disc; meshes stationary ring; output pins. | rotary <-> rotary (high ratio) | Robotics actuators, high-torque compact reducers. | Vibration if unbalanced; cost. |
| differential | Three-shaft gear train; output speed = average of two inputs. | speed averaging / torque vectoring | Vehicles, clocks, analog computers. | Complexity; open/limited-slip variants. |
| herringbone_double_helical_gear | Two helical gears of opposite hand; no axial thrust. | rotary <-> rotary | Marine turbines, high-power parallel shafts. | Harder/more expensive to manufacture. |
| non_circular_gear | Non-round pitch curves for variable ratio/oscillation. | rotary <-> rotary (variable ratio) | Textile machines, potentiometers, CVTs, presses. | Tight tolerances; specialized. |
| elliptical_gear | Special case of non-circular gear (elliptical pitch curve). (unverified) | rotary <-> rotary (variable ratio) | Variable ratio applications. | Unverified beyond non-circular gear. |
| nutating_gear | Conical gear rolling with nutating motion. (unverified) | rotary <-> rotary | Speed reducers. | Unverified; limited sources. |
| bevel_planetary | Planetary set with bevel gears for angled axes. (unverified) | rotary <-> rotary (angled axes) | Pencil sharpeners, differentials. | Unverified specifics. |
| magnetic_gear | Non-contact torque transmission via modulated magnetic fields. (unverified) | rotary <-> rotary (contactless) | Oil-free, maintenance-free drives. | Unverified; limited torque density. |
| sun_and_planet_gear | Early planetary variant (Watt) with planet meshing sun and ring. (unverified) | rotary <-> rotary | Historical mechanism design. | Unverified. |
| cycloid_gear_profile | Cycloid tooth form vs involute; used in clocks. (unverified) | rotary <-> rotary | Clocks, low-speed precision. | Unverified; involute dominates modern. |

### 3.4 Springs

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| helical_compression_spring | Open-coil helix resisting compressive load; wire loaded in torsion. | energy storage (compression) | Valves, returns, automotive suspension. | Buckling if slender; fatigue. |
| helical_extension_spring | Close-coiled helix resisting tensile load; has initial tension. | energy storage (tension) | Trampolines, garage doors, returns. | Stress concentration at hooks; fatigue. |
| helical_torsion_spring | Resists torque in plane normal to coil axis; wire stressed in bending (not torsion). | energy storage (torsion) | Garage doors, clothespins, mousetraps. | Wire in bending; fatigue; misnamed. |
| belleville_spring | Tapered washer; nonlinear force-deflection; compact high load/low deflection. | energy storage (compression, nonlinear) | Gun recoil, flanges, bolted joints, clutches. | Stacking complexity; hysteresis. |
| leaf_spring | Flat spring, semi-elliptic or cantilever, graduated leaves; interleaf friction. | energy storage (bending) | Automotive rear suspension, trucks, rail. | Interleaf friction; weight; space. |
| torsion_bar_spring | Straight solid/hollow bar twisted in torsional shear. | energy storage (torsion) | Automotive suspension, stabilizer bars. | Stress concentration; fatigue. |
| spiral_clock_spring | Flat strip wound spiral; stores rotational energy over multiple turns. | energy storage (rotation) | Steering wheel clock springs, seat mechanisms, medical. | Limited cycles; fatigue; space. |
| constant_force_spring | Tightly coiled ribbon exerting nearly constant force as unrolled. | energy storage (constant force) | Counterbalances, retractable tape rules, window sashes. | Limited stroke; friction. |
| volute_spring | Conical spring of wide thin strip; coils nest; longer travel than helical conical. | energy storage (compression, variable rate) | Variable-rate scales, tank suspension. | Complex manufacture; fatigue. |
| wave_spring | Flat wire marcelled into wavy pattern. | energy storage (compression, compact) | Valve wear compensation, bearing preload. | Lower load than coil; fatigue. |
| gas_spring | Volume of compressed gas; force from pressure x area. | energy storage (pneumatic) | Office chairs, hatches, automotive. | Seal leakage; temperature dependence. |
| rubber_urethane_spring | Elastomeric blocks loaded in shear/compression. | energy storage (elastomeric) | Shock absorption, vibration isolation, bump stops. | Aging; temperature; creep. |
| finger_spring_washer | Flat spring fingers for preload/retention. | preload/retention | Ball-bearing preload, fastener security. | Limited load; fatigue. |
| die_spring | Heavy-duty compression spring (color-coded by load). | energy storage (compression, heavy duty) | Dies, clutches, brakes, farm/aircraft mechanisms. | Cost; size. |
| garter_spring | Helical spring in circular form (extension) for seals/retaining rings. | sealing/retention | Seals, retaining rings. | Installation; fatigue. |

### 3.5 Clutches

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| friction_disk_clutch_single | Friction plates pressed axially by spring/diaphragm; torque from friction. | engage/disengage torque (single plate) | Automotive manual transmissions, general. | Wear; heat; engagement smoothness. |
| friction_disk_clutch_multi | Multiple friction plates for higher torque in compact space. | engage/disengage torque (multi plate) | Limited radial space, high torque. | More wear surfaces; complexity. |
| cone_clutch | Conical friction surfaces; self-energizing (wedge). | engage/disengage torque | Older transmissions, marine, machinery. | Grabby engagement; chatter. |
| centrifugal_clutch | Friction shoes pivoted on driving member engage drum above threshold rpm. | auto-engage by speed | Scooters, small engines, conveyors. | Torque rises with speed; wear. |
| dog_jaw_clutch | Interlocking jaws/teeth; no slip, instantaneous engagement. | positive engage/disengage | Gearboxes, PTOs (no speed differential). | Shock on engagement; no slip. |
| overrunning_clutch | Transmits torque one direction, freewheels other (roller-ramp, sprag, wedge-ramp subtypes). | one-way torque transmission | Starters, conveyors, backstops. | Subtype trade-offs: sprag highest density, roller-ramp longest life. |
| wrap_spring_clutch | Helical spring tightens on cylindrical sleeve to transmit torque one direction. | one-way torque (light duty) | Low cost, light-duty, low speed. | Low speed/torque; wear. |
| electromagnetic_friction_clutch | Electrically magnetized armature clamps friction disks. | electrically engaged torque | Automation, tension control, motor testing. | Power needed; heat; wear. |
| magnetic_particle_clutch | Powder aligns under magnetic field; infinitely adjustable torque. | slip/positioning torque | Tensioning, positioning, slip operation. | Heat at slip; limited torque. |
| hysteresis_clutch | Torque from hysteresis losses in drag cup; constant torque independent of slip speed. | constant torque (slip) | Fractional power, almost no wear. | Low torque; cost. |
| fluid_coupling | Hydrodynamic torque transmission via impeller/turbine in oil. | smooth torque transmission | High-inertia starts, automatics. | Slip losses; heat; no mechanical wear. |
| pneumatic_hydraulic_clutch | Air/oil pressure engages multi-plate or cone. | actuated torque transmission | Fast, remote actuation; industrial automation. | Requires fluid power; seals. |

### 3.6 Brakes

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| external_shoe_drum_brake | Shoes press against outer drum surface; self-energizing (leading shoe). | friction braking (external) | Simple, low cost; legacy. | Fade-prone; cooling. |
| internal_shoe_drum_brake | Shoes press against inner drum surface. | friction braking (internal) | Automotive rear, parking brakes. | Fade ~250-300 C; cooling. |
| disk_brake | Caliper clamps pads on rotor. | friction braking (disk) | Automotive front, motorcycles, aircraft. | Needs hydraulic actuation; noise. |
| band_brake | Flexible band with friction lining wraps drum. | friction braking (band) | Conveyors, hoists, winches. | One-direction high torque; wear. |
| electromagnetic_friction_brake | Electrically actuated friction or particle/hysteresis. | electrically actuated braking | Fast response; ~80% of power-applied brakes. | Power needed; heat; wear. |
| magnetic_particle_brake | Powder aligns under field; adjustable braking torque. | adjustable braking torque | Tensioning, positioning. | Heat at slip; limited torque. |
| hysteresis_brake | Constant braking torque independent of speed. | constant braking torque | Fractional power, no wear. | Low torque; cost. |
| eddy_current_brake | Non-contact; induced currents in rotating conductive disk create opposing torque. | non-contact braking | Trains, roller coasters, aircraft. | Torque -> 0 at 0 rpm; needs cooling. |
| regenerative_brake | Motor acts as generator, returns energy to battery/flywheel. | energy-recovering braking | EVs, trains, flywheel KERS. | Limited by battery state; needs friction brake for low speed. |
| parking_emergency_brake | Mechanical (cable) or electronic; holds vehicle stationary. | holding brake | Parking/emergency stop. | Rarely effective for high-speed stops. |

### 3.7 Couplings

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| sleeve_muff_coupling | Single-piece cylindrical sleeve bored to fit both shaft ends. | rigid torque transmission | Permanent, well-aligned shafts; cost/rigidity. | No misalignment compensation; alignment critical. |
| split_muff_coupling | Sleeve split into two halves bolted around shafts. | rigid torque transmission | Heavy industrial; easy disassembly. | Lower torque than solid; bolts need torque. |
| flange_coupling | Two flanges bolted together, hubs keyed to shafts. | rigid torque transmission | Turbines, pumps, marine, generator sets. | Precise alignment; heavy; backlash possible. |
| clamp_compression_coupling | Two-piece clamp or tapered bushing (Taper-Lock/QD) locks without keyway. | rigid, zero backlash | Precision, frequent removal, keyless connection. | Rigid (no misalignment); bore limits. |
| jaw_spider_coupling | Two hubs with interlocking jaws and elastomeric spider insert. | flexible torque (damping) | General-purpose, damping, moderate misalignment. | Spider wear; backlash (~<5 arc-min); not extreme. |
| oldham_coupling | Three-piece: two hubs with perpendicular slots and floating center disc. | flexible, large parallel misalignment | Large parallel misalignment in tight axial space, zero backlash. | Center disc wears; not fail-safe; limited angular. |
| beam_helical_coupling | Single piece of bar stock with helical cuts creating flexible element. | flexible, zero backlash | Precision positioning, servo, encoder. | Limited torque; fatigue under parallel misalignment. |
| bellows_coupling | Two hubs joined by thin-walled stainless-steel bellows. | flexible, high stiffness | Zero backlash + high stiffness + low inertia. | Low damping; sensitive to parallel misalignment. |
| diaphragm_disc_coupling | Torque through thin metal discs/diaphragms clamped between hubs. | flexible, high speed | Turbines, compressors, high-speed precision. | Low damping; expensive; precise alignment. |
| grid_coupling | Two grooved hubs connected by tapered steel spring (grid) in serpentine path. | flexible, high torque | High torque + shock/vibration damping. | Requires lubrication; maintenance. |
| gear_coupling | Sleeve with internal teeth meshing with external teeth on hubs; lubricated. | flexible, very high torque | Very high torque, torsional rigidity, high speed. | Lubrication; wear; no damping. |
| chain_coupling | Two sprocket hubs connected by roller chain. | flexible, low cost | Cost-sensitive, moderate torque, easy service. | Lubrication; wear; noise; lower speed. |
| tire_coupling | Elastomeric tire element between hubs; highly flexible. (details flagged unverified) | flexible, high damping | High misalignment + damping, moderate loads. | Elastomer aging; lower torque/speed. |
| universal_joint_hooke | Cross-and-yoke connecting two shafts at an angle. | large angle, speed fluctuation | Large angles, cost, where fluctuation acceptable. | Speed non-uniformity (single); lubrication. |
| cv_joint | Constant-velocity joint (Rzeppa, tripod, etc.). | large angle, constant velocity | High speed + large angle + constant velocity. | Complex; costly; boot/lubrication; wear. |
| shear_pin_torque_limiter | Coupling halves connected by shear pins failing at predetermined torque. | overload protection (shear) | Infrequent overloads, precise protection. | Replace pins after event; downtime. |
| slip_friction_torque_limiter | Frictionally engaged surfaces slip when torque exceeds set value; auto re-engages. | overload protection (slip) | Frequent minor overloads, automatic recovery. | Wear during slipping; heat. |
| ball_detent_torque_limiter | Balls in detents transmit torque; roll out on overload; re-engages at set position. | overload protection (positive-locking) | Precision axes needing overload protection with minimal backlash. | More complex; cost; ratcheting wear. |

### 3.8 Power transmission

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| shaft | Rotating member, usually circular, transmits power/motion; supports gears, pulleys, etc. | power transmission (rotary) | Always present in rotary power trains; size per torque/bending/critical speed. | Fatigue, misalignment bending, corrosion. |
| pulley_sheave | Wheel transmitting motion via belts (flat, V, timing). | power transmission (belt) | Cost, shock absorption, overload protection (belt slip). | Slip (friction belts); wear; tension maintenance. |
| sprocket | Toothed wheel engaging chain or toothed belt; no slip. | power transmission (chain/belt) | Positive (non-slip) transmission, dirty/wet environments. | Lubrication; wear; noise; no overload protection. |
| idler | Free-spinning pulley/sprocket changing belt/chain path; increases wrap angle. | belt/chain guidance | Automotive accessory drives, long belt runs. | Bearing wear; alignment; added friction. |
| tensioner | Device (eccentric, spring-loaded, adjustable, automatic) maintaining tension. | tension maintenance | Long belts, variable loads, automatic tension. | Complexity; spring fatigue; maintenance. |
| gearbox_speed_reducer | Enclosed gear train reducing speed and multiplying torque. | speed reduction / torque multiplication | By ratio, torque, backlash, efficiency, shaft geometry, self-locking. | Cost; backlash; efficiency varies (worm lowest). |
| planetary_gearbox | Sun drives planet gears inside ring gear; coaxial; load shared. | speed reduction (coaxial, high torque) | Compact high-torque coaxial servo axes. | Complex; cost; fixed structure. |
| worm_gearbox | Worm meshes bronze worm wheel; right-angle; self-locking above ~20-25:1. | speed reduction (right-angle, self-locking) | Right-angle, high ratio, self-locking, cost. | Low efficiency; heat; not back-drivable. |
| cycloidal_gearbox | Eccentric cam discs drive rollers; two-stage; virtually backlash-free. | speed reduction (high torque, precision) | High torque + precision + shock loads. | Cost; complexity; lower efficiency than planetary. |
| harmonic_gearbox | Three components: wave generator, flexspline, circular spline; zero backlash. | speed reduction (zero backlash, compact) | Zero backlash in compact space, lower torque. | Flexspline fatigue limits torque; cost. |
| lead_screw | Screw and nut with sliding (trapezoidal) thread; converts rotation to linear. | rotary -> linear (sliding) | Cost-sensitive, moderate duty, self-locking, low speed. | Lower efficiency; wear; backlash unless preloaded. |
| ball_screw | Screw and nut with recirculating balls; rolling contact; high efficiency. | rotary <-> linear (rolling, high efficiency) | Precision linear motion, high speed/duty, efficiency. | Cost; lubrication; not self-locking; contamination sensitivity. |
| roller_screw | Screw with planetary/recirculating rollers; many contact points. | rotary <-> linear (highest load/stiffness) | Extreme loads, long life, high acceleration, compact high-force. | Highest cost; complex; lubrication; contamination. |

### 3.9 Fasteners

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| hex_bolt | Externally threaded fastener with hexagonal head; may have unthreaded grip length. | clamping (threaded) | Removable joint, moderate-to-high loads, controlled preload. | Needs nut and access both sides; can loosen under vibration. |
| socket_head_cap_screw | Cylindrical head with internal hex socket; high-strength alloy steel. | clamping (threaded, compact) | Limited wrench clearance, high strength, compact assembly. | Socket can strip; less torque than hex for large sizes. |
| countersunk_flat_head_screw | Conical head seats flush in countersunk hole. | clamping (flush) | Flush surface required, light-to-moderate loads. | Weaker head; countersink required. |
| round_head_machine_screw | Domed head with slotted/Phillips drive; mates with tapped hole or nut. | clamping (light) | Light loads, general assembly, low cost. | Low torque capacity; head protrudes. |
| carriage_bolt | Smooth rounded head with square neck that bites into material. | clamping (wood/soft) | Wood/soft materials, smooth exposed head, one-side tooling. | Requires square hole/soft material; lower strength. |
| stud | Headless externally threaded rod; one end screwed into part, other takes nut. | clamping (frequent disassembly) | Frequent disassembly, threaded holes in soft/cast parts. | Requires tapped hole; removal can be difficult. |
| hex_nut | Six-sided internally threaded nut mating with bolt/stud. | clamping (threaded) | Standard removable clamping. | Can loosen under vibration; needs locking if dynamic. |
| nyloc_nut | Hex nut with nylon insert resisting loosening. | clamping (vibration-resistant) | Vibration/loosening risk, moderate temperature. | Temperature limit of nylon; prevailing torque. |
| flange_nut | Hex nut with integral washer flange. | clamping (load distribution) | Need load distribution without separate washer. | Flange can embed in soft materials. |
| t_nut | Nut with flange and prongs embedding in wood/composite. | anchoring (wood/panel) | Threaded fastening into wood/panel. | Can pull out under high load. |
| flat_washer | Thin annular disc to distribute bolt load. | load distribution | Soft materials, large holes, surface protection. | Can relax; not a lock by itself. |
| spring_lock_washer | Split helical spring washer applying spring force. | locking (light) | Low-cost vibration resistance (non-critical). | Effectiveness debated; can damage surfaces. |
| toothed_lock_washer | Washer with radial teeth biting into mating surfaces. | locking (positive) | Need positive locking, soft substrates. | Damages surfaces; not for high preload. |
| solid_rivet | Smooth shank with factory head; tail bucked into shop head. | permanent fastening (shear) | Permanent shear joint, both-side access, high reliability. | Requires access both sides; removal destructive. |
| blind_rivet | Tubular rivet with mandrel; installed from one side. | permanent fastening (one-side) | One-side access, moderate loads, speed. | Lower strength than solid; hole size critical. |
| semi_tubular_rivet | Rivet with partial hole at tail; rolled over with ~1/4 force of solid. | permanent fastening (pivot) | Pivot points, high-volume production. | Less strength than solid; requires tooling. |
| dowel_pin | Precision ground solid cylinder pressed into reamed hole. | location/shear | Precise location; two dowels + bolts for clamping. | Requires reamed hole; over-constraint risk. |
| clevis_pin | Smooth cylindrical pin with head and cross-hole for cotter pin. | pivot (serviceable) | Serviceable pivot connection. | Requires cotter pin; clearance fit. |
| cotter_pin | Split pin inserted through hole; legs bent to lock. | locking (light) | Locking pins/nuts, light duty. | One-time-ish; low strength. |
| taper_pin | Conical pin pressed into tapered reamed hole. | location + light torque | Precise location with light torque, removable. | Requires tapered reamer; cost. |
| spring_roll_pin | Hollow slotted or coiled spring steel pin gripping drilled hole. | location + light/moderate torque | Forgiving holes, light torque, low cost. | Lower precision than dowel; can loosen. |
| grooved_pin | Solid pin with longitudinal grooves compressing to grip drilled hole. | press retention | Press retention in drilled holes. | Less precise than dowel. |
| square_key | Square cross-section key seated in shaft/keyway transmitting torque. | torque transmission | Torque transmission, sacrificial weak link. | Stress concentration; loosening; speed limits. |
| flat_parallel_key | Rectangular key (width > height), common metric (DIN 6885). | torque transmission (metric) | Standard shaft-hub torque (metric). | Stress concentration. |
| woodruff_key | Semicircular (half-moon) key seating in curved keyseat. | torque transmission (tapered shafts) | Tapered shafts, easy assembly, moderate torque. | Weaker than square for same size. |
| gib_head_taper_key | Tapered key with gib head for extraction. | torque transmission (heavy, removable) | Heavy torque, need removable key. | Requires tapered keyway; cost. |
| retaining_ring_circlip | Spring steel ring seated in groove on shaft/bore; axial retention. | axial retention | Axial retention in grooved shaft/bore. | Groove required; limited thrust; wear. |
| e_clip | E-shaped ring snapping onto shaft/groove from side. | axial retention (light, tool-free) | Light loads, fast assembly. | Lower capacity than grooved rings. |
| spiral_retaining_ring | Multi-turn constant-section ring with 360 deg contact. | axial retention (higher thrust) | Higher thrust than standard circlip. | Cost; special install. |
| push_on_retainer | Toothed washer pushed onto shaft; one-time use. | axial retention (one-time) | One-time assembly, no groove, low cost. | One-time use; damages shaft; low capacity. |
| set_screw | Headless screw threaded into part to clamp/lock another part. | positioning/locking | Positioning/locking, light-to-moderate torque (with key for high torque). | Can damage shaft; loosens; low torque alone. |
| threaded_insert | Internal thread repair/anchor inserted into parent material. | thread repair/anchoring | Repair or threaded hole in soft material. | Installation tooling; cost; pull-out if misinstalled. |

### 3.10 Joints

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| bolted_joint | Threaded fastener clamps parts; load by friction (preload) or shank shear/bearing. | clamping (serviceable) | Serviceable, high load, dissimilar materials. | Needs holes/access; can loosen; preload control. |
| fillet_welded_joint | Triangular bead in corner (T/lap/corner); fails across throat. | permanent joining (corner) | General fabrication, corner/lap joints, moderate loads. | Distortion; HAZ; fatigue at toe; similar metals. |
| butt_welded_joint | Edges butted and fused through full thickness. | permanent joining (full strength) | Full strength, flush joint, compatible metals. | Edge prep; root access; distortion; cost. |
| spot_welded_joint | Resistance weld at discrete points joining sheet. | permanent joining (sheet, automated) | High-volume thin sheet, automated production. | Stress concentration; fatigue; electrode access. |
| seam_welded_joint | Continuous/overlapping spot welds along seam; can be watertight. | permanent joining (sealed seam) | Leak-tight sheet joints. | Distortion; slower than spot; thickness limits. |
| riveted_joint | Permanent fastener in shear; plates in bearing; does not loosen. | permanent joining (shear) | Permanent shear joint, vibration, thin sheet. | Needs holes; removal destructive; labor. |
| pinned_joint | Pin in shear for location/torque. | location/shear | Location/shear, removable pivot. | Not for clamping; over-constraint. |
| keyed_joint | Key in keyway transmits torque between shaft and hub. | torque transmission | Torque transmission, sacrificial failure. | Stress concentration; loosening; speed limits. |
| press_fit_joint | Shaft pressed into undersized hole; retention by friction/interference. | permanent/semi-permanent fit | Permanent/semi-permanent fit, no fastener access. | Assembly force; hoop stress; disassembly difficult. |
| adhesive_bonded_joint | Load transferred through thin adhesive layer over overlap. | bonding (shear) | Thin/dissimilar materials, sealed/smooth joints. | Surface prep critical; cure time; weak peel. |
| snap_fit_joint | Integral flexible features interlock during assembly (plastics). | tool-free assembly | High-volume plastic parts, light loads. | Plastic material limits; fatigue. |
| dovetail_joint | Interlocking trapezoidal pins/tails in wood. | wood joining (pull-out) | Wood furniture, pull-out loads, aesthetics. | Difficult to cut; skill required. |
| mortise_and_tenon_joint | Tenon inserted into mortise. | wood joining (structural) | Structural wood frames. | Time-consuming; visible if not hidden. |
| tongue_and_groove_joint | Tongue on one board fits groove on another. | wood joining (alignment) | Panels/flooring alignment. | Weak if not glued; machining needed. |

### 3.11 Bearings

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| deep_groove_ball_bearing | Single-row ball bearing with deep race grooves; radial + moderate axial both directions. | rotary support (general) | General-purpose rotary, moderate loads, high speed. | Lower load than rollers; axial limited. |
| angular_contact_ball_bearing | Ball bearing with contact angle; combined radial and one-direction axial. | rotary support (combined, precision) | Combined loads, precision, high speed. | Needs preload/pairing for bidirectional axial. |
| thrust_ball_bearing | Flat washers with balls; supports axial (thrust) loads only. | rotary support (axial only) | Pure axial load. | No radial capacity; speed limits. |
| cylindrical_roller_bearing | Cylindrical rollers between races; high radial capacity, low axial. | rotary support (high radial) | High radial load, good alignment. | Poor misalignment tolerance; low axial. |
| tapered_roller_bearing | Conical rollers/races support both radial and axial. | rotary support (combined, heavy) | Combined loads, automotive, heavy. | More expensive; friction from collar; preload. |
| needle_roller_bearing | Long thin rollers; small OD, high radial capacity in limited space. | rotary support (compact) | Space-constrained high radial load. | Shorter fatigue life; contamination sensitive. |
| spherical_roller_bearing | Barrel rollers in spherical outer race; accommodates misalignment. | rotary support (heavy, misalignment) | Heavy load with misalignment. | Higher friction/cost; sliding. |
| carb_toroidal_roller_bearing | Toroidal rollers; accommodates misalignment and axial displacement; non-locating. | rotary support (non-locating) | Non-locating bearing paired with locating. | Non-locating; must pair with locating bearing. |
| plain_sleeve_bearing | Shaft slides in hole/bushing; no rolling elements; cheapest. | rotary support (low cost) | Low cost, high load, low speed, dirty environments. | Higher friction; wear; lubrication needed. |
| hydrodynamic_journal_bearing | Fluid film separates surfaces via shaft rotation; full-film lubrication. | rotary support (high speed/load) | High speed, high load, continuous operation. | Needs rotation to lift; oil whirl risk; start/stop wear. |
| hydrostatic_bearing | Externally pumped fluid film; supports load at zero speed. | rotary support (precision, zero speed) | Precision, heavy load, low speed/start-stop. | Pump/complexity; contamination; cost. |
| magnetic_bearing | Magnetic levitation; no contact; highest speeds. | rotary support (contactless) | Oil-free, ultra-high speed, vacuum, long life. | Power/control required; backup bearing; cost. |
| air_bearing | Gas (air) film separates surfaces; non-contact. | rotary support (ultra-precision) | Ultra-precision, clean, light load. | Low load; contamination sensitivity; air supply. |
| flexure_bearing | Elastic deformation provides motion; no contact friction. | rotary support (no backlash) | Ultra-precision, small motion, no maintenance. | Limited travel; fatigue life depends on strain. |
| jewel_bearing | Sapphire/ruby plain bearing for low friction in instruments. | rotary support (tiny, low load) | Tiny, low-load, high precision. | Brittle; low load; cost. |

### 3.12 Indexing & locking

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| ball_detent | Ball plunger engages detent/notch; holds until specified release force. | discrete angular positions | Rotary switches, indexing fixtures, tool turrets. | Wear; limited holding force. |
| spring_plunger | Spring-loaded pin/ball in hollow cylinder for indexing/positioning/securing. | spring detent | Fixtures, indexing, locating, ejectors. | Limited holding force; wear. |
| index_plunger | Hand-retractable positive locking at discrete holes (taper/rotary-cam). | positive locking | Machine setup, swiveling/sliding element locking. | Manual operation. |
| toggle_clamp | Over-center linkage; max clamping force when three pivots align (dead center). | binary (open/locked) | Workholding, fixtures, presses. | Requires proper over-center design; high input force to unlock. |
| snap_action_mechanism | Over-center spring and lever device for valves/switches. | bistable toggle | Switches, valves, thermostats. | Limited stroke; friction. |
| ball_lock_pin | High-strength quick-release alignment pin; push to release balls. | binary (locked/released) | Fixtures, aerospace, marine, changeover. | Requires mating bushing/receptacle; cost. |
| quick_release_pin | Ring-grip pin; pull to remove; retaining ball holds in place. | binary (locked/released) | General assembly, tight spaces. | Lower strength than ball-lock. |
| bistable_compliant_mechanism | Two stable equilibrium positions; energy stored in flexible segments. | bistable (zero-power hold) | Switches, closures, hinges, grippers. | Limited stroke/rotation (flexures ~10-20 deg). |
| bayonet_coupling | Twist-lock fastener with lugs engaging slots. (unverified) | binary twist-lock | Light bulbs, lenses, connectors. | Requires alignment; wear. |
| locking_ring_snap_ring | Retains components on shafts/bores. (unverified) | retention | Shafts, bores, bearings. | Axial retention only. |
| cam_lock | Eccentric cam rotates to clamp. (unverified) | binary clamp | Furniture, cabinets, fixtures. | Limited force; wear. |

### 3.13 Actuators

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| hydraulic_cylinder | Pressurized oil -> linear motion via cylinder/piston. | hydraulic -> linear | Construction equipment, presses, aircraft surfaces, heavy machinery. | Leaks; maintenance; heavy. |
| pneumatic_cylinder | Compressed air -> linear or rotary motion via cylinders. | pneumatic -> linear/rotary | Automation, packaging, clamping, valves. | Low precision (compressible air); lower force. |
| solenoid | Electromagnetic coil drives plunger; fast on/off. | electric -> linear/rotary (on/off) | Valves, locks, relays, latches. | Short stroke; on/off only. |
| stepper_motor | Rotates in fixed increments/steps; precise open-loop control. | electric -> discrete rotary | Printers, CNC, robotics, indexing. | Torque drops with speed; resonance; stall. |
| servo_motor_bldc | Closed-loop with feedback; high speed and force-sensitive. | electric -> rotary (closed-loop) | CNC, robotics, camera tracking. | Cost; complexity; tuning. |
| piezoelectric_actuator | Converse piezoelectric effect converts electricity to deformation. | electric -> micro displacement/force | Nanopositioning, inkjet, optics, micro-robotics. | Small stroke; high voltage; brittle. |
| shape_memory_alloy_actuator | Recovers predetermined shape when heated (martensite->austenite). | thermal -> shape recovery | Soft robots, wearable, biomedical, aerospace. | Slow cooling; hysteresis; fatigue; low efficiency. |
| thermal_bimetal | Two metals with different CTE bonded; bends with temperature. (unverified) | temperature -> bending | Thermostats, temperature switches. | Slow; low force; hysteresis. |
| pneumatic_artificial_muscle | McKibben: pneumatic soft actuator contracting upon pressurization via braided sleeve. | pneumatic -> contraction | Soft robots, exoskeletons, prosthetics. | Nonlinear; hysteresis; bladder fatigue. |
| magnetostrictive_actuator | Magnetic field -> strain (micro-motion). | magnetic -> strain | Sonar, precision positioning. | High cost; eddy currents. |

### 3.14 Special mechanisms (compliant, parallel, straight-line, etc.)

| id | Description | Motion type / function | When to select | Key constraint / limitation |
|---|---|---|---|---|
| scissor_lift | Crossed X-pattern links producing vertical motion. | vertical lift | Aerial work platforms, tables, jacks. | Force unbounded near flat; side loads dangerous. |
| compliant_mechanism_flexure | Gains mobility from elastic deformation of flexible members; monolithic. | elastic motion (no backlash) | Precision stages, MEMS, grippers. | Limited stroke (10-20 deg); fatigue. |
| compliant_gripper | Monolithic gripper using flexures; passive alignment. | grasping (elastic) | Pick-and-place, surgery. | Buckling; stress. |
| delta_robot | Parallel robot; 3 DOF translation (4-DOF variant adds rotation). | high-speed pick-and-place | Packaging, PCB, medical, haptics, 3D printing. | Small workspace; parallel singularities. |
| stewart_platform | 6 DOF; six linear actuators with spherical/universal joints. | 6-DOF motion | Flight simulators, force-torque sensors. | Complex kinematics; small workspace. |
| constant_force_mechanism | Delivers constant force over large displacement (spring/cam/counterweight). | constant force | Lamps, exoskeletons, elevators, windows. | Complexity; stroke limits. |
| over_center_mechanism | Three pivots, two fixed distances, third varies; dead-center yields max force. | bistable (special) | Clamps, switches, lifts. | Unlock force; vibration sensitivity. |

---

## 4. Quick selection guide: "I need X motion" -> mechanism candidates

- **Rotary -> linear:** slider_crank_inline, offset_slider_crank, scotch_yoke, rack_and_pinion, leadscrew, ball_screw, roller_screw, cam_and_follower (see 3.2 plate_cam), hydraulic_cylinder, pneumatic_cylinder.
- **Rotary -> oscillatory:** crank_rocker_four_bar, cam_and_follower, eccentric (non_circular_gear).
- **Rotary -> rotary (speed/torque conversion):** spur_gear, helical_gear, bevel_gear_straight, spiral_bevel_gear, hypoid_gear, worm_drive, planetary_epicyclic_gear, harmonic_drive, cycloidal_drive, differential, non_circular_gear.
- **Rotary -> intermittent rotary:** geneva_drive, ratchet_and_pawl, escapement, star_wheel_ratchet.
- **Linear -> linear (amplification/scaling):** pantograph, lazy_tongs, scissor_lift.
- **Exact straight-line motion:** peaucellier_lipkin_linkage, scott_russell_linkage.
- **Approximate straight-line motion:** watt_linkage, chebyshev_linkage, hoeken_linkage, roberts_linkage.
- **One-way / overrunning torque:** overrunning_clutch, wrap_spring_clutch, ratchet_and_pawl.
- **Engage/disengage torque on demand:** friction_disk_clutch_single, friction_disk_clutch_multi, cone_clutch, dog_jaw_clutch, electromagnetic_friction_clutch, pneumatic_hydraulic_clutch.
- **Overload protection:** shear_pin_torque_limiter, slip_friction_torque_limiter, ball_detent_torque_limiter.
- **High misalignment between shafts:** oldham_coupling, beam_helical_coupling, bellows_coupling, tire_coupling, universal_joint_hooke, cv_joint.
- **Zero backlash:** beam_helical_coupling, bellows_coupling, diaphragm_disc_coupling, harmonic_drive, cycloidal_drive, clamp_compression_coupling.
- **Self-locking:** worm_drive, worm_gearbox, leadscrew (possible), ratchet_and_pawl.
- **Indexing/locking positions:** geneva_drive, ball_detent, spring_plunger, index_plunger, toggle_clamp, ball_lock_pin, quick_release_pin.
- **High force, compact:** hydraulic_cylinder, belleville_spring, roller_screw, wedge-ramp (overrunning).
- **Precision micro-motion:** piezoelectric_actuator, flexure_bearing, air_bearing, compliant_mechanism_flexure.
- **6-DOF motion:** stewart_platform.
- **High-speed pick-and-place:** delta_robot.
- **Constant force over stroke:** constant_force_spring, constant_force_mechanism, gas_spring.
- **Holding at zero speed:** parking_emergency_brake, hydrostatic_bearing, magnetic_bearing (with control), toggle_clamp.

---

## 5. Mechanism count summary

| Category | Count |
|---|---|
| Linkages & motion conversion | 32 |
| Cams & followers | 12 |
| Gears & gear trains | 22 |
| Springs | 15 |
| Clutches | 12 |
| Brakes | 10 |
| Couplings | 18 |
| Power transmission | 13 |
| Fasteners | 32 |
| Joints | 14 |
| Bearings | 15 |
| Indexing & locking | 11 |
| Actuators | 10 |
| Special mechanisms | 7 |
| **Total** | **228** |

Note: some mechanisms are cross-listed by family (e.g. rack-and-pinion appears under Gears; leadscrew/ball_screw/roller_screw under Power transmission; toggle under Linkages and toggle_clamp under Indexing). Counts above count each row once in its primary category.

---

## 6. References

Research notes (source of this catalog):
- `research_notes/Top 200 mechanisms catalog/linkages_motion_conversion.md`
- `research_notes/Top 200 mechanisms catalog/cams_gears.md`
- `research_notes/Top 200 mechanisms catalog/springs_clutches_brakes.md`
- `research_notes/Top 200 mechanisms catalog/couplings_power_transmission.md`
- `research_notes/Top 200 mechanisms catalog/fasteners_joints_bearings.md`
- `research_notes/Top 200 mechanisms catalog/indexing_actuators_special.md`

Detailed entries: `knowledge/mechanisms/*.md` (65 exist; more to be added). Format reference: `knowledge/mechanisms/spacer_sleeve.md`.

Textbooks/standards cited in the research notes: Artobolevsky *Mechanisms in Modern Engineering Design*; Chironis & Sclater *Mechanisms and Mechanical Devices Sourcebook*; Norton *Design of Machinery*; Shigley *Mechanical Engineering Design*; Mabie & Reinholtz *Mechanisms and Dynamics of Machinery*; ANSI/ASME/ISO fastener and bearing standards; AGMA gear standards. Per-entry sources and URLs are recorded in the research notes. Items marked (unverified) lack a confirmed source in this session.

---

## Appendix A. Cross-references (mechanisms appearing in multiple families)

- `rack_and_pinion`: primary home Gears & gear trains (3.3); also a rotary<->linear converter (see 4).
- `leadscrew`, `ball_screw`, `roller_screw`: primary home Power transmission (3.8); also rotary<->linear converters.
- `geneva_drive`, `ratchet_and_pawl`, `escapement`: primary home Linkages (3.1); also Indexing (3.12 family).
- `toggle_linkage` (Linkages) vs `toggle_clamp` (Indexing): linkage principle vs workholding device.
- `snap_fit_joint` (Joints) vs `snap_action_mechanism` (Indexing): assembly feature vs bistable device.
- `bistable_compliant_mechanism` (Indexing) vs `compliant_mechanism_flexure` (Special): bistable vs general compliant.
- `constant_force_spring` (Springs) vs `constant_force_mechanism` (Special): component vs system.
- `overrunning_clutch` (Clutches) shares ratchet principle with `ratchet_and_pawl` (Linkages).
- `universal_joint_hooke`, `cv_joint` (Couplings) are also power-transmission elements.
- `harmonic_drive`/`cycloidal_drive` (Gears) appear as `harmonic_gearbox`/`cycloidal_gearbox` (Power transmission) at product level.

## Appendix B. Contribution checklist

When adding a new mechanism:
1. Add a row to the correct category table in section 3 (id, description, motion, when to select, constraint).
2. Create `knowledge/mechanisms/<id>.md` using the `spacer_sleeve.md` template (Type, Function, How it works, Constraints, Failure modes, When to use).
3. Update the count in section 5 and the cross-references in Appendix A if needed.
4. Mark unverified items explicitly.