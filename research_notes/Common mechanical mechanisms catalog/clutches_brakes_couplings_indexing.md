# Common mechanical mechanisms catalog - clutches, brakes, couplings, indexing & locking

Scope: small/workshop-scale mechanical design. Dense, textbook-grounded catalog with selection, sizing equations, failure modes, and DFM notes. Primary sources: Wikipedia (mechanism articles), Shigley/Budynas/Nisbett Mechanical Engineering Design (10th ed., McGraw-Hill), Mott Machine Elements in Mechanical Design (Pearson), Juvinall & Marshek Fundamentals of Machine Component Design (Wiley), plus patent literature cited where relevant.

## 1. Clutches (friction, jaw/tooth, overrunning, electromagnetic, fluid)

### Takeaway
A clutch is a mechanical device that allows an output shaft to be disconnected from a rotating input shaft; selection is driven by torque capacity, engagement smoothness, heat dissipation, wear life, and the need for slip during engagement. Friction clutches dominate workshop practice; positive (jaw/dog) clutches suit no-slip, low-speed indexing; overrunning clutches give automatic one-way drive; electromagnetic and fluid couplings add remote/soft engagement.

### Cited Findings
- Definition and general function of a clutch as a disconnect between input/output shafts - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Dry clutch: friction disk pressed against flywheel by spring; majority of manual-transmission automotive clutches are dry - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Wet clutch: friction material runs in oil bath for cooling/lubrication; smoother engagement, longer life, lower efficiency; multi-plate stacks compensate for lower mu in oil - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Centrifugal clutch: automatically engages as input speed rises, disengages as it falls; used in small motorcycles, scooters, chainsaws - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Cone clutch: friction material on outside of conical surface; wedging action on engagement; common as synchronizer ring in manual transmissions - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Dog (jaw) clutch: non-slip positive engagement used in non-synchronous transmissions - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Single-revolution clutch: engages for exactly one revolution then disengages; early designs were dog clutches with cam disengagement; wrap-spring and cascaded-pawl variants for teleprinters/typewriters - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Electromagnetic clutch: engaged by integral electromagnet; magnetic-particle type has particles clumping under DC for smooth engagement/slippage - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Wrap-spring clutch: helical spring (often square wire) wraps tightly when driven one way, slips when driven the other; torque to slip grows exponentially with turns (capstan equation) - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Friction-clutch torque capacity (standard): T = mu * F * r_m for single contact, where mu = coefficient of friction, F = normal (axial) force, r_m = mean (effective) friction radius; for multi-plate: T = n * mu * F * r_m with n = number of friction interfaces - [Shigley, Budynas & Nisbett, Mechanical Engineering Design, 10th ed.](https://www.amazon.com/Mechanical-Engineering-Design-Richard-Budynas/dp/0073398207).
- Cone-clutch torque: T = (mu * F * r_m)/sin(alpha) (alpha = cone half-angle); self-locking when mu > tan(alpha) - [Shigley, Mechanical Engineering Design](https://www.amazon.com/Mechanical-Engineering-Design-Richard-Budynas/dp/0073398207); [Mott, Machine Elements in Mechanical Design](https://www.pearson.com/en-us/subject-catalog/p/machine-elements-in-mechanical-design/P200000003265).
- Centrifugal clutch engagement speed: springs hold shoes in until centrifugal force F_c = m * r * omega^2 overcomes spring preload; engagement RPM proportional to sqrt(k*x/(m*r)) - [Mott, Machine Elements in Mechanical Design](https://www.pearson.com/en-us/subject-catalog/p/machine-elements-in-mechanical-design/P200000003265).
- Overrunning/freewheel: disengages driveshaft from driven shaft when driven shaft spins faster than driveshaft; simplest form is two saw-toothed spring-loaded discs (ratchet); rugged form uses spring-loaded steel rollers in a driven cylinder; pawl-type bicycle freewheels use step-toothed drum with hardened steel pawls - [Wikipedia, "Freewheel"](https://en.wikipedia.org/wiki/Freewheel).
- Freewheel as automatic clutch enables gear changes without clutch pedal; Saab freewheel engage/disengage lever; coaster-brake bicycles - [Wikipedia, "Freewheel"](https://en.wikipedia.org/wiki/Freewheel).
- Sprag clutch (see also ratchet): roller/sprag one-way clutches used in helicopter autorotation, engine starters, PTO safety - [Wikipedia, "Freewheel"](https://en.wikipedia.org/wiki/Freewheel).
- Fluid coupling: hydrodynamic torque transfer via fluid; related to torque converter - [Wikipedia, "Coupling" (Fluid/Hydrodynamic)](https://en.wikipedia.org/wiki/Coupling).

### Inferences
- For workshop-scale power transmission, a dry single-plate friction clutch with cast-iron/steel plates and replaceable organic or sintered-bronze lining is the most maintainable choice; wet multi-plate suits high-duty or oil-bathed drivetrains.
- Positive (dog) clutches should be limited to low speed or indexed motion because engagement under load causes impact; add chamfers/lead-in and inertia limits.
- Overrunning clutches are ideal for unidirectional drives (conveyors, PTO, starters) but cannot provide engine braking; pair with separate brake if deceleration needed.

### Gaps
- No reliable source found for exact coefficient-of-friction values by lining material (organic vs. sintered bronze vs. ceramic) or for thermal capacity/temperature-rise equations for small clutches; consult manufacturer data and Shigley heat-dissipation sections.
- No single source for electromagnetic clutch torque vs. current curves; vendor datasheets required.

## 2. Brakes (shoe/drum, disk, band, electromagnetic)

### Takeaway
A brake inhibits motion by absorbing energy from a moving system, most often by friction; selection balances peak force, continuous power dissipation, fade resistance, noise, weight, and cooling. Disc brakes dominate modern high-duty use for heat rejection; drum/shoe brakes remain cheap; band brakes give simple wrap-around clamping; electromagnetic brakes suit motor-integrated or retarder duty.

### Cited Findings
- Definition: brake absorbs energy from moving system; friction converts kinetic energy to heat - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Kinetic energy K = 1/2 * m * v^2, so braking distance scales with v^2 at traction limit - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Frictional brake types: shoe/pad (drum, disc, band) and hydrodynamic; drum brake = shoes press inner surface of rotating drum; disc brake = pads pinch rotating disc/rotor; band brake = band wraps drum - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Disc brake rotor usually cast iron or ceramic; pads forced mechanically/hydraulically/pneumatically/electromagnetically - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Drum brakes wear faster due to overheating vs. disc - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Electromagnetic brakes: eddy-current (magnetic fields create resistance/heat) and regenerative (motor as generator) - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Brake characteristics: peak force, continuous power dissipation, fade, smoothness, pedal feel, drag, durability, weight, noise - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Fade: brake becomes less effective as it heats; cooling/ventilation strongly affect fade - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Foundation brake systems: "S" cam, disc, wedge - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Band brake torque: T = F * r (F = band tension differential x effective radius); self-locking when wrap angle theta satisfies mu * theta >= ln(F1/F2) (capstan/Euler-Eytelwein); lock occurs if mu*theta >= 1 (for F2 -> 0) - [Shigley, Mechanical Engineering Design](https://www.amazon.com/Mechanical-Engineering-Design-Richard-Budynas/dp/0073398207).
- Disc-brake torque: T = mu * F_clamp * r_eff (r_eff ~ mean pad radius); drum-brake torque: T = mu * F_shoe * r_drum * (number of shoes) with leading/trailing shoe factors - [Shigley, Mechanical Engineering Design](https://www.amazon.com/Mechanical-Engineering-Design-Richard-Budynas/dp/0073398207); [Mott, Machine Elements in Mechanical Design](https://www.pearson.com/en-us/subject-catalog/p/machine-elements-in-mechanical-design/P200000003265).
- Heat dissipation/power: P = T * omega (braking power); temperature rise deltaT = Q/(m*c) for absorbed energy Q, with heat split between rotor and pads/air - [Shigley, Mechanical Engineering Design](https://www.amazon.com/Mechanical-Engineering-Design-Richard-Budynas/dp/0073398207).

### Inferences
- For small workshop machines, a simple disc brake (caliper + cast-iron rotor) with vented rotor gives best fade resistance per cost; drum brakes acceptable for low-duty parking/holding.
- Band brakes are attractive for compact, high-torque holding (e.g., winches) but suffer from fade and grabbiness; use woven lining and generous wrap.
- Electromagnetic (eddy-current) brakes need no contact wear but require speed to generate torque; use as retarders, not for holding.

### Gaps
- No source found for specific brake-lining mu ranges by temperature or for cooling-fin/ventilation sizing equations; rely on manufacturer data and Shigley thermal sections.
- No reliable source for drum-brake leading-shoe force-multiplication (self-energization) factor derivation beyond textbook; see Shigley ch. on brakes.

## 3. Couplings (rigid, flexible, safety, misalignment)

### Takeaway
A coupling connects two shafts to transmit power while permitting some misalignment and end movement; rigid couplings demand precise alignment, flexible couplings absorb misalignment and vibration, safety couplings protect machinery by slipping or shearing at overload. Selection trades torque density, misalignment capacity, stiffness, backlash, and maintenance.

### Cited Findings
- Definition: coupling connects shafts at ends for power transmission; permits misalignment/end movement; does not normally allow disconnection in operation, except torque-limiting types - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Rigid couplings: sleeve/muff (pipe with keyway, gib-head key), split-muff/clamp (two halves bolted around shaft), flange (bolted flanges, heavy loads) - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Clamp/split-muff allows assembly without moving shafts; used for heavy power at moderate speed - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Tapered shaft lock (keyless locking device): self-centering, no keyway wear, but higher cost - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Flexible couplings accommodate up to ~1.5 deg angular misalignment and some parallel misalignment; protect bearings from misalignment, vibration, shock, thermal expansion - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Jaw (spider/Lovejoy) coupling: elastomeric spider between jawed hubs; common, cheap, moderate misalignment - [Wikipedia, "Coupling" (Jaw)](https://en.wikipedia.org/wiki/Coupling).
- Oldham coupling: three discs with perpendicular tongue-and-groove; compact, handles parallel misalignment; named after John Oldham (1821) - [Wikipedia, "Coupling" (Oldham)](https://en.wikipedia.org/wiki/Coupling).
- Beam/helical coupling: single-piece spiral beam; no backlash; handles angular/parallel/axial misalignment; materials Al/SS/acetal/Ti - [Wikipedia, "Coupling" (Beam)](https://en.wikipedia.org/wiki/Coupling).
- Diaphragm coupling: torque across flexible plate(s) from OD to ID; disc coupling: torque through stainless-steel disc pack tangentially - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Grid coupling: two hubs + metallic grid spring + cover; high torque density, vibration damping, limited misalignment - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Gear coupling: internal/external gear pairs, crowned teeth; higher torque density than U-joint in same space; limited to 4-5 deg angular misalignment - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Universal joint (U-joint/Hooke/Cardan): two hinges at 90 deg; not constant velocity; output speed varies: omega2 = omega1 * cos(beta) / (1 - sin^2(beta) * cos^2(gamma1)); max recommended operating angle ~15-20 deg for single joint - [Wikipedia, "Universal joint"](https://en.wikipedia.org/wiki/Universal_joint).
- Double Cardan (two U-joints 90 deg out of phase with equal angles) acts as CV joint - [Wikipedia, "Universal joint"](https://en.wikipedia.org/wiki/Universal_joint).
- Constant-velocity (CV) joint: Rzeppa, double Cardan, Thompson; maintains constant speed through angle; typical automotive half-shaft - [Wikipedia, "Coupling" (Constant velocity)](https://en.wikipedia.org/wiki/Coupling); [Wikipedia, "Constant-velocity joint"](https://en.wikipedia.org/wiki/Constant-velocity_joint).
- Misalignment accommodation: flexible couplings typically up to ~1.5 deg angular, some parallel offset; U-joint higher angle but non-CV; gear coupling 4-5 deg - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Safety couplings: shear-pin (fails at overload, replace pin) and slip (friction) couplings; torque limiter protects driven machinery - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Coupling maintenance: inspect, clean, lubricate; failure causes include improper installation, poor selection, operation beyond design - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).

### Inferences
- For small workshop shafts (<=25 mm) with modest misalignment, jaw/spider or beam couplings are cheapest and easiest; use beam/helical where backlash-free motion control matters (encoders, CNC).
- Rigid (flange/sleeve) couplings only when alignment can be held within ~0.05 mm TIR; otherwise flexible.
- Safety (shear-pin/slip) couplings are worth the cost on any machine with expensive driven elements (pumps, gearboxes) or human hazard.

### Gaps
- No source found for quantitative coupling stiffness (torsional) or damping coefficients by type; manufacturer catalogs needed.
- No reliable source for shear-pin sizing equations (pin diameter vs. torque) beyond standard bolt-shear: tau_all = T/(r * pi * d^2/4); use safety factor per Shigley.

## 4. Indexing, locking, and latching mechanisms

### Takeaway
Indexing mechanisms convert continuous motion into discrete, repeatable positions (Geneva, ratchet, detent); locking/latching mechanisms secure position or hold load (pins, rings, cams, toggles, quick-release, over-center). Selection depends on step count, dwell, backlash, load, release speed, and safety (self-locking vs. quick release).

### Cited Findings
- Geneva drive: translates continuous rotation into intermittent rotary motion; drive wheel pin enters slot in driven wheel, advancing one step; blocking disc locks between steps; typical 3-18 slots; step angle = 360 deg/n; external vs. internal variants; used in film projectors, watches (Geneva stop), CNC turrets, index tables - [Wikipedia, "Geneva drive"](https://en.wikipedia.org/wiki/Geneva_drive).
- Geneva drive kinematics: acceleration discontinuity at pin entry/exit produces jerk/vibration; internal version motion >180 deg, external <180 deg - [Wikipedia, "Geneva drive"](https://en.wikipedia.org/wiki/Geneva_drive).
- Ratchet: allows motion in one direction, prevents reverse; gear/rack teeth asymmetric (gentle slope forward, steep reverse) with spring-loaded pawl; backlash <= tooth spacing - [Wikipedia, "Ratchet (device)"](https://en.wikipedia.org/wiki/Ratchet_(device)).
- Ratchet uses: socket wrenches, jacks, cable ties, seatbelts, anti-rollback - [Wikipedia, "Ratchet (device)"](https://en.wikipedia.org/wiki/Ratchet_(device)).
- Detent: mechanical or magnetic means to resist/arrest movement; spring-loaded ball detent in incremental depressions or spring steel snapping into notches; stepper motors have magnetic detents - [Wikipedia, "Detent"](https://en.wikipedia.org/wiki/Detent).
- Ball detent holding force (standard): F = k*x (spring preload) at engagement; release when applied torque exceeds mu*F*r (ball radius); use hardened balls/pins and case-hardened seats for wear - [Shigley, Mechanical Engineering Design](https://www.amazon.com/Mechanical-Engineering-Design-Richard-Budynas/dp/0073398207).
- Pin/lock ring (retaining ring, circlip, snap ring): axial retention of bearings/gears on shafts/bores; groove dimensions per standard; e.g., DIN 471 (external) / DIN 472 (internal) - [Mott, Machine Elements in Mechanical Design](https://www.pearson.com/en-us/subject-catalog/p/machine-elements-in-mechanical-design/P200000003265).
- Cam lock: latch of base + cam rotated by key/tool; straight or offset (reversible) cams; common on cabinets, tool chests - [Wikipedia, "Latch" (Cam lock)](https://en.wikipedia.org/wiki/Latch).
- Toggle clamp: also called draw latch/draw catch; claw/loop catches strike plate; over-center linkage provides self-locking hold-down force; used in jigs, fixtures, molds - [Wikipedia, "Latch" (Toggle latch)](https://en.wikipedia.org/wiki/Latch); [Wikipedia, "Clamp (tool)"](https://en.wikipedia.org/wiki/Clamp_(tool)).
- Over-center mechanism: linkage passes through dead center; holding force amplified by leverage; self-locking when toggle is beyond center and load keeps it there; release by pushing past center - [Wikipedia, "Latch" (Toggle latch)](https://en.wikipedia.org/wiki/Latch).
- Quick-release: cam-lever (skewer) type converts small lever motion into large clamping force via eccentric cam; used on bicycle wheels, clamps - [Wikipedia, "Clamp (tool)"](https://en.wikipedia.org/wiki/Clamp_(tool)) (spring clamp/toggle clamp references).
- Pin/lock indexing (locating pin, dowel, lock ring): positive location via cylindrical/taper pins; repeatability limited by fit (H7/h6 etc.) - [Mott, Machine Elements in Mechanical Design](https://www.pearson.com/en-us/subject-catalog/p/machine-elements-in-mechanical-design/P200000003265).

### Inferences
- For workshop fixtures, toggle clamps (over-center) give the best force-to-effort ratio and are self-locking; ensure the toggle passes clearly over center to avoid accidental release under vibration.
- Geneva drives suit precise intermittent indexing (CNC turrets, rotary tables) but introduce jerk; add dwell cams or use servo indexing where smoothness matters.
- Ball detents are cheapest for light detent/positioning; use magnetic detents where contact wear or contamination is a concern.

### Gaps
- No source found for toggle-clamp force-multiplication ratios or handle-force equations; use manufacturer (e.g., De-Sta-Co) datasheets.
- No reliable source for quick-release cam clamping force vs. lever angle; empirical testing required.
- No source for "pin/lock ring" as a combined term; treated as retaining rings + locating pins separately.

## 5. DFM notes (small workshop) - cross-cutting

### Takeaway
Small-workshop DFM favors off-the-shelf hardware (bearings, retaining rings, springs, friction linings), simple turned/milled geometry, standard fasteners, and serviceable wear parts; avoid exotic materials and tight tolerances unless function demands.

### Cited Findings
- Couplings are balanced at factory; re-balancing in service is difficult/expensive and only justified by tolerance requirements - [Wikipedia, "Coupling"](https://en.wikipedia.org/wiki/Coupling).
- Brake fade and cooling: ventilation and material choice dominate fade; drum brakes overheat faster than discs - [Wikipedia, "Brake"](https://en.wikipedia.org/wiki/Brake).
- Clutch slippage should be minimized to avoid increased wear rates - [Wikipedia, "Clutch"](https://en.wikipedia.org/wiki/Clutch).
- Geneva drive must be well lubricated and is often enclosed in oil capsule - [Wikipedia, "Geneva drive"](https://en.wikipedia.org/wiki/Geneva_drive).
- Ratchet backlash limited to tooth spacing; minimize with fine pitch or friction-surface ratchet - [Wikipedia, "Ratchet (device)"](https://en.wikipedia.org/wiki/Ratchet_(device)).

### Inferences
- Clutches/brakes: use cast iron or steel rotors/drums for heat capacity; organic or sintered-bronze linings; provide ventilation slots/holes; bolted (not riveted) linings for serviceability; keep friction surfaces flat within 0.05 mm.
- Couplings: prefer keyed + set-screw or clamp (split) hubs for shop builds; tapered locks for better balance; avoid welding hubs to shafts unless permanent.
- Indexing/locking: use standard dowel pins, retaining rings (DIN 471/472), and commercial detent springs/balls; machine grooves with standard tooling; add lubrication access.
- General: design for disassembly (bolts not welds), use common metric fasteners, allow wear-part replacement, and provide adjustment (shims/slots) for alignment.

### Gaps
- No source for specific tolerance tables (e.g., retaining-ring groove widths) in this note set; consult DIN/ISO standards or manufacturer catalogs.
- No source for cost/lead-time comparisons by manufacturing process; shop-specific.