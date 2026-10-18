# Couplings and Power-Transmission Mechanisms

## Coupling Types: Rigid, Flexible, and Safety

### Takeaway
Shaft couplings divide into rigid (zero misalignment tolerance, highest torsional stiffness/torque), flexible (metallic or elastomeric elements accommodating angular/parallel/axial misalignment), and safety/overload couplings (shear-pin, friction-slip, or positive-locking ball-detent) that protect drivetrains; selection trades misalignment capacity, torque, torsional stiffness, backlash, and damping. Sources: Fractory, IQS Directory, Ruland, Lovejoy, Falk/Rexnord, KTR, Wikipedia.

### Cited Findings
- Two basic coupling families are rigid and flexible; rigid couplings transmit torque directly but cannot accommodate misalignment between shafts — [Scribd Types of Couplings](https://www.scribd.com/doc/43687101/Couplings).
- Rigid couplings are preferred for high-precision setups; flexible couplings for systems with misalignment, vibration, or protective functions — [TSUBAKI](https://www.ustsubaki.com/resources/knowledge-center/what-is-the-difference-between-rigid-and-flexible-couplings).
- Rigid couplings must be perfectly aligned; even good initial alignment changes over time (foundation settling, thermal growth) — [TSUBAKI](https://www.ustsubaki.com/resources/knowledge-center/what-is-the-difference-between-rigid-and-flexible-couplings).
- Shaft misalignment occurs in three orientations: angular, parallel (radial), and axial — [AutomationDirect drive couplings](https://cdn.automationdirect.com/static/specs/drvcpl.pdf).
- Flexible couplings compensate for misalignment that arises from thermal expansion, vibration, shaft movement, and gradual loss of positioning accuracy — [IQS Directory](https://www.iqsdirectory.com/articles/shaft-couplings.html).
- Selection factors: torque (hp), max speed (rpm), permissible misalignment, stiffness, inertia, shock absorption, vibration damping, mounting, environment, cost — [IQS Directory](https://www.iqsdirectory.com/articles/shaft-couplings.html).
- Coupling selection rule of thumb for servo motors: max torque capacity 5–10× motor peak torque — [MISUMI Mech Lab](https://us.misumi-ec.com/blog/the-perfect-pair-couplings); [YouTube shaft coupling types](https://www.youtube.com/watch?v=gzUgKDQMPyc).
- Coupling is a four-way trade between misalignment tolerance, torque capacity, torsional stiffness, and backlash — [Wolfer](https://www.wofler.com/en/couplings-bushings.html).
- Standards referenced: DIN 5480 (involute spline), ISO 14691 (general flexible couplings), AGMA 9000 (balance classes for high-speed couplings) — [Wolfer](https://www.wofler.com/en/couplings-bushings.html).

### Inferences
- Because rigid couplings act as a single shaft, they are favored for turbines/vertical pumps where concentricity and torsional rigidity dominate over misalignment tolerance.

### Gaps
- No single authoritative table of misalignment limits across all coupling types was found; values are manufacturer-specific (flagged per type below).

#### Rigid couplings

**1. Sleeve / muff coupling (continuous sleeve)**
- Description: Single-piece cylindrical sleeve bored to fit both shaft ends, keyed or set-screwed; acts as one shaft. Powerdrive catalog lists "Continuous Sleeve Coupling Type Gc02 & Gc05" — [Powerdrive E-Catalog](https://www.powerdrive.com/Downloads/ECatalogs/Coupling/Coupling.pdf).
- Misalignment capacity: none (rigid) — [Fractory](https://fractory.com/types-of-couplings).
- Torque capacity: high for size; limited by bore/key; Powerdrive lists flange sleeve variants for higher torque.
- Advantages: simple, low cost, compact, zero backlash.
- Limitations: requires perfect alignment; no shock damping; difficult to install/remove on long shafts.
- Applications: vertical pumps, turbines, low-cost general drives — [TSUBAKI](https://www.ustsubaki.com/resources/knowledge-center/what-is-the-difference-between-rigid-and-flexible-couplings).
- When to select: permanent, well-aligned shafts where cost and rigidity matter.

**2. Split-muff coupling**
- Description: Sleeve split into two halves bolted around shafts; allows assembly without moving equipment.
- Misalignment: none (rigid).
- Advantages: easy installation/removal; accommodates larger shafts.
- Limitations: lower torque than solid sleeve; bolts require torque; alignment still critical.
- Applications: heavy industrial, where disassembly must be easy.

**3. Flange coupling**
- Description: Two flanges bolted together, hubs keyed to shafts; rigid. Fractory lists as rigid type — [Fractory](https://fractory.com/types-of-couplings).
- Misalignment: none (rigid); can tolerate tiny errors only if flexible (marine/rubber-bushed variants exist, not covered).
- Torque: very high; used in large turbines and marine drives.
- Advantages: high torque, easy inspection, can be unbolted.
- Limitations: precise alignment; heavy; backlash at bolted interface possible.
- Applications: turbines, pumps, marine propulsion, generator sets.

**4. Clamp (compression) coupling / taper lock / QD bushing**
- Description: Two-piece clamp or tapered bushing (Taper-Lock/QD) that locks to shaft via radial screws without keyway; zero backlash — [Wolfer](https://www.wofler.com/en/couplings-bushings.html) (clamp style, true zero backlash); [eINDUSTRIFY](https://eindustrify.com/blog/power-transmission-systems-component-types-functions) (taper bushings quick mount).
- Misalignment: none (rigid).
- Advantages: no keyway damage, fast mount/dismount, concentric, zero backlash.
- Limitations: rigid (no misalignment compensation), bore size limits.
- Applications: servo/precision drives, pulleys/sprockets mounting, machinery where keyless connection desired.
- When to select: precision, frequent removal, or when keyways are undesirable.

#### Flexible metallic couplings

**5. Jaw / spider coupling (elastomeric)**
- Description: Two hubs with interlocking jaws and an elastomeric "spider" insert; torque transmitted in compression; fail-safe (jaws interlock if spider fails) — [Lovejoy/JBJ](https://www.jbj.co.uk/e-publications/straight-jaw-spider-type-couplings-for-power-transmission/); [Ruland](https://www.ruland.com/media/wysiwyg/PDF/Coupling-Failure-Article.pdf).
- Misalignment: angular ~0.5°, parallel ~0.010 in (0.25 mm) typical for NBR spider; temp range -40 to 232 °C — [Lovejoy/JBJ chart](https://www.jbj.co.uk/e-publications/straight-jaw-spider-type-couplings-for-power-transmission/).
- Torque: Lovejoy sizes up to tens of thousands in-lb; Rexnord Omega E50 HDY ~9,560 in-lb (1,080 Nm) — [Rexnord](https://www.rexnord.com/products/couplings/elastomeric-coupling-parts-and-kits/elements-flexible/omega-close-coupled-elastomeric-elements?page=20).
- Advantages: vibration damping, shock absorption, electrical isolation (nonmetallic spider), fail-safe, no lubrication, wide temp range.
- Limitations: spider wear/fatigue; backlash (~<5 arc-min); radial stiffness beyond limits loads bearings; not for high torque/high speed extremes.
- Applications: pumps, conveyors, general industrial, servo (small sizes).
- When to select: general-purpose, damping needed, moderate misalignment, cost-sensitive.

**6. Oldham coupling**
- Description: Three-piece: two hubs with perpendicular slots and a floating center disc (typically nylon/acetal) that slides in slots; transmits torque while accommodating large parallel misalignment — [Ruland](https://www.ruland.com/media/wysiwyg/PDF/Coupling-Failure-Article.pdf); [Wolfer](https://www.wofler.com/en/couplings-bushings.html).
- Misalignment: large radial (parallel) compliance; e.g. OnDrive Oldham ~2.4 mm radial for D=55 mm; limited angular (~±? small) — [SDP/SI Rivin](https://sdp-si.com/Rivin/art1.php); Wolfer lists axial ±0.4 mm, radial ±0.15 mm, angular ±1° for its range.
- Torque: low to moderate (e.g. D=55 mm rated 4.5 Nm in one example) — [SDP/SI](https://sdp-si.com/Rivin/art1.php).
- Advantages: zero backlash (metallic versions), large parallel misalignment in short axial space, electrically isolating (nonmetallic disc), no maintenance.
- Limitations: center disc wears; not fail-safe (disengages on disc failure); limited angular; ratcheting torque rating same reversing or single-direction (no divide-by factors) — [Design World (Ruland)](https://www.designworldonline.com/tips-understanding-torque-bellows-oldham-couplings).
- Applications: stepper/servo positioning, robotics, printers, medical devices.
- When to select: large parallel misalignment in tight axial space, zero backlash needed.

**7. Beam (helical) coupling**
- Description: Single piece of bar stock with helical cuts (single/multi-beam) creating flexible element; transmits torque while flexing — [Ruland](https://www.ruland.com/media/wysiwyg/PDF/Coupling-Failure-Article.pdf); [Wolfer](https://www.wofler.com/en/couplings-bushings.html).
- Misalignment: excellent angular and axial; lower parallel capability; Wolfer: axial ±0.4, radial ±0.15, angular ±1° (range); single beam must not be used for parallel misalignment in two planes simultaneously (fatigue) — [Ruland](https://www.ruland.com/media/wysiwyg/PDF/Coupling-Failure-Article.pdf).
- Torque: low to moderate; torsionally rigid; zero backlash.
- Advantages: zero backlash, high torsional stiffness, low inertia, no maintenance, good for servo/encoder.
- Limitations: limited torque; fatigue under parallel misalignment; not for shock/damping; can fail if misalignment excessive.
- Applications: stepper/servo drives, encoders, ball-screw drives, robotics.
- When to select: precision positioning, zero backlash, high torsional stiffness, moderate misalignment.

**8. Bellows coupling**
- Description: Two hubs joined by thin-walled stainless-steel bellows; metallic flexible element — [Ruland Belflex](https://docs.rs-online.com/2aaf/0900766b80405a83.pdf); [R+W](https://blog.rw-america.com/hs-fs/hub/237991/file-39863538-pdf/docs/basics_of_flexible_bellows_couplings.pdf).
- Misalignment: angular, parallel, and axial simultaneously; low restoring forces; R+W recommends alignment within 0.2–0.4 mm parallel for infinite fatigue life; axial up to ~0.016 in (0.4 mm) — [R+W](https://blog.rw-america.com/hs-fs/hub/237991/file-39863538-pdf/docs/basics_of_flexible_bellows_couplings.pdf); [Lovejoy](https://www.lovejoy-inc.com/wp-content/uploads/2018/01/MotionControl2010.pdf).
- Torque: low to moderate (R+W miniature up to ~300 Nm for its range); high torsional stiffness.
- Advantages: zero backlash, very low inertia, low bearing loads (constant), no maintenance, high torsional rigidity, fatigue-resistant if aligned.
- Limitations: low damping (failed in damping applications), sensitive to parallel misalignment, higher cost.
- Applications: semiconductor, medical, servo/encoder, high-speed precision.
- When to select: zero backlash + high stiffness + low inertia; misalignment small and well-controlled.

**9. Diaphragm / disc (membrane) coupling**
- Description: Torque transmitted through thin metal discs/diaphragms clamped between hubs; zero backlash, high torsional stiffness — [Ruland Discflex](https://docs.rs-online.com/2aaf/0900766b80405a83.pdf); [Wolfer](https://www.wofler.com/en/couplings-bushings.html).
- Misalignment: angular and axial; limited parallel; high-speed (turbines ≥3,000 rpm) — [Pumps & Systems](https://www.pumpsandsystems.com/coupling-types-different-applications).
- Torque: high; used in turbines and high-speed equipment.
- Advantages: zero backlash, high speed, no lubrication, handles high torque at speed.
- Limitations: low damping, sensitive to misalignment, expensive, requires precision alignment.
- Applications: turbines, compressors, pumps, high-speed rotating machinery.
- When to select: high speed, high torque, precision, torsional rigidity.

**10. Grid coupling**
- Description: Two grooved hubs connected by a tapered steel spring (grid) in a serpentine path; metallic flexible — [Falk Steelflex](https://www.rexnord.com/contentitems/techlibrary/documents/cp5-004_productsheet); [SKF](https://cdn.skfmediahub.skf.com/api/public/094c13cfb3420f44/pdf_preview_medium/094c13cfb3420f44_pdf_preview_medium.pdf).
- Misalignment: angular, parallel, axial (all three planes); SKF claims vibration reduction up to 30%.
- Torque: very high — Falk up to 932,250 Nm (8,250,000 lb-in), max bore 508 mm, speeds up to ~6,000 rpm — [Falk](https://www.rexnord.com/contentitems/techlibrary/documents/cp5-004_productsheet).
- Advantages: high torque, shock/vibration absorption (torsional deflection), lubricated (grease), grid replaceable without disturbing hubs, wide size range.
- Limitations: requires lubrication, moderate misalignment (less than elastomeric), more maintenance than elastomeric.
- Applications: pumps, blowers, compressors, conveyors, marine, heavy industry.
- When to select: high torque + shock/vibration damping + moderate misalignment.

**11. Gear coupling**
- Description: Sleeve with internal teeth meshing with external teeth on hubs; lubricated; allows misalignment via tooth clearance/contour — [Pumps & Systems](https://www.pumpsandsystems.com/coupling-types-different-applications); [ComInTec](https://grupogaes.com/wp-content/uploads/2020/11/ACOPLA-COMINTEC.pdf).
- Misalignment: angular and parallel (depends on tooth contour and clearance); torsionally stiff.
- Torque: very high; high-speed and high-torque/low-speed applications.
- Advantages: highest torque density, torsional rigidity, handles shock somewhat.
- Limitations: requires lubrication, wear, no damping, alignment more critical than elastomeric.
- Applications: turbines, compressors, rolling mills, marine, heavy drives.
- When to select: very high torque, torsional rigidity, high speed.

**12. Chain coupling**
- Description: Two sprocket hubs connected by a roller chain (single/double strand); flexible — [Morse/Purvis](https://www.purvisindustries.com/ASSETS/DOCUMENTS/ITEMS/EN/Morse_108763_Specification_Sheet.pdf); [ComInTec](https://grupogaes.com/wp-content/uploads/2020/11/ACOPLA-COMINTEC.pdf).
- Misalignment: some angular and parallel (double-strand accommodates more).
- Torque: moderate to high; simple.
- Advantages: low cost, easy maintenance, accommodates misalignment, can be used as torque-limiter coupling (Morse).
- Limitations: requires lubrication, wear, noise, lower speed.
- Applications: conveyors, agricultural, general industrial.
- When to select: cost-sensitive, moderate torque, easy service.

**13. Tire (tyre) coupling**
- Description: Elastomeric tire element between hubs; highly flexible, large misalignment and damping — mentioned in [Instagram/industrial] and manufacturer catalogs; flagged: details from training, verify.
- Misalignment: high angular/parallel/axial.
- Torque: moderate.
- Advantages: excellent damping, large misalignment, no metal contact, no lubrication.
- Limitations: elastomer aging, lower torque/speed than metallic.
- Applications: compressors, pumps, conveyors, marine.
- When to select: high misalignment + damping, moderate loads.

**14. Universal joint (Hooke/Cardan)**
- Description: Cross-and-yoke (spider) connecting two shafts at an angle; transmits torque with speed fluctuation unless double jointed — [Wikipedia CV joint](https://en.wikipedia.org/wiki/CV_joint); [ScienceDirect](https://www.sciencedirect.com/topics/engineering/universal-joints).
- Misalignment: operating angles up to ~15–25° (single); speed fluctuation increases with angle; double Hooke's (double Cardan) cancels fluctuation.
- Torque: high; simple, robust.
- Advantages: simple, high torque, large angles, compact.
- Limitations: speed non-uniformity (single), notchy at high angles, requires lubrication, shorter life at high angles.
- Applications: automotive driveshafts (older/RWD), agricultural PTO, machinery.
- When to select: large angles, cost, where speed fluctuation acceptable or double joint used.

**15. Constant-velocity (CV) joint**
- Description: Transmits torque at constant angular velocity across an angle; types: Rzeppa (ball), Birfield, tripod (plunging), Weiss, Tracta, Thompson, double Cardan — [Wikipedia](https://en.wikipedia.org/wiki/CV_joint); [ScienceDirect](https://www.sciencedirect.com/topics/engineering/universal-joints).
- Misalignment: up to ~45–50° (fixed type) and ~80° deviation for wide-angle CV; plunging types allow axial travel up to ~50 mm — [Alberta research](https://open.alberta.ca/dataset/5c0c3e39-a04e-430a-81c3-24f1fd825be1/resource/e0b1a84b-08bf-43c8-9418-0628e0881b20/download/743-cv-joints-afmrc.pdf); [USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12359695).
- Torque: high (automotive axle).
- Advantages: constant velocity (no vibration), large angles, plunging (axial) travel, high efficiency (~95% at 45°) — [ScienceDirect](https://www.sciencedirect.com/topics/engineering/universal-joints).
- Limitations: complex, costly, requires boot/lubrication, wear.
- Applications: FWD/RWD/4WD vehicles, steering axles, robotics.
- When to select: high speed + large angle + constant velocity required.

#### Safety / overload couplings

**16. Shear-pin coupling**
- Description: Coupling halves connected by shear pins that fail at predetermined torque, physically separating drive from driven — [KOP-FLEX](https://www.ahrinternational.com/PDF_catalogues/Kop-Flex/Torque_Overload_Release_Coupling.pdf); [McMaster-Carr](https://www.mcmaster.com/products/torque-limiters/shaft-diameter~1-8).
- Misalignment: depends on base coupling (often flexible element); McMaster shear couplings allow ~0.031 in parallel, 2° angular.
- Torque: set by pin shear strength; hollow pins for adjustable values; KOP-FLEX series H up to 25,100 Nm — [KOP-FLEX](https://www.ahrinternational.com/PDF_catalogues/Kop-Flex/Torque_Overload_Release_Coupling.pdf).
- Advantages: precise, repeatable release; protects expensive components; simple.
- Limitations: must replace pins after event; downtime; release torque > normal starting torque.
- Applications: rolling mills, pumps, conveyors, crushers.
- When to select: infrequent overloads, precise protection, acceptable downtime for pin replacement.

**17. Slip / friction torque limiter**
- Description: Frictionally engaged surfaces slip when torque exceeds set value; auto re-engages when torque drops — [KTR RUFLEX](https://uat.ktr.com/us/en/products/ruflex-torque-limiters/ruflex-with-rotex); [Morse/Purvis](https://www.purvisindustries.com/ASSETS/DOCUMENTS/ITEMS/EN/Morse_108763_Specification_Sheet.pdf).
- Misalignment: depends on paired coupling; KTR combines with ROTEX/BoWex.
- Torque: KTR RUFLEX 0.5–12,000 Nm — [KTR](https://www.ktr.com/us/en/products/torque-limiters-overload-couplings/).
- Advantages: automatic re-engagement, no replacement parts, adjustable, protects against jams.
- Limitations: wear during slipping, heat, needs monitoring; re-engages at reduced speed for high inertia.
- Applications: packaging, printing, conveyors, machine tools.
- When to select: frequent minor overloads, automatic recovery desired.

**18. Positive-locking ball-detent torque limiter (ratchet/synchronous)**
- Description: Balls in detents transmit torque; on overload balls roll out, separating drive; re-engages at set position; backlash-free variants (KTR-SI, SYNTEX) — [KTR](https://www.ktr.com/us/en/products/torque-limiters-overload-couplings/).
- Torque: varies by size.
- Advantages: precise, repeatable, backlash-free, fast disengagement, idle-rotation versions for high inertia.
- Limitations: more complex, cost; ratcheting wear if not monitored.
- Applications: robotics, automation, servo axes, packaging.
- When to select: precision axes needing overload protection with minimal backlash.

## Power Transmission Elements

### Takeaway
Power transmission elements include shafts, pulleys, sprockets, idlers, tensioners, gearboxes/speed reducers, and screw drives (lead/ball/roller); selection balances ratio, torque, efficiency, backlash, stiffness, and geometry (inline/right-angle/coaxial). Sources: Fractory, ATO, Nabtesco, Harmonic Drive, Schaeffler, Thomson, SKF.

### Cited Findings
- Mechanical power transmission methods: belts, chains, gears, shafts, couplings, screws; belts are common and suit slow to very high speeds — [Fractory](https://fractory.com/mechanical-power-transmission).
- Shaft: rotating member, usually circular, transmits power/motion; supports gears, pulleys, sprockets, couplings; failures from fatigue, misalignment, corrosion, overload — [DAV University notes](https://davuniversity.org/images/files/study-material/MEC103-Mechanical%20Engineering%20Fundamentals-Power%20Transmission%20Devices%20-%20Belt,%20Rope,%20Chain,%20%20Gear,%20Keys.pdf); [BTL-UK](https://blog.btl-uk.com/elements-of-mechanical-power-transmission-systems).
- Pulleys transfer motion from belts and set speed/torque ratios; taper bushings allow quick mount/dismount — [eINDUSTRIFY](https://eindustrify.com/blog/power-transmission-systems-component-types-functions).
- Sprockets drive chains/toothed belts; styles A–D by hub configuration — [DAV University notes](https://davuniversity.org/images/files/study-material/MEC103-Mechanical%20Engineering%20Fundamentals-Power%20Transmission%20Devices%20-%20Belt,%20Rope,%20Chain,%20%20Gear,%20Keys.pdf).
- Idlers/tensioners maintain belt tension, increase wrap angle, reduce vibration; types: eccentric, spring-loaded, adjustable-arm — [tec-science](https://www.tec-science.com/mechanical-power-transmission/belt-drive/belt-tensioner-systems-for-belt-drives); [McMaster-Carr](https://www.mcmaster.com/products/idler-tensioners).
- Speed reducer: lowers motor speed, multiplies torque by gear ratio; reflected inertia reduced by square of ratio — [ATO](https://www.ato.com/speed-reducers).
- Gearbox types: spur, helical, planetary, worm, bevel, cycloidal, harmonic (strain-wave) — [greensky-power](https://greensky-power.com/different-types-of-speed-reducers); [ZHY Gear](https://www.zhygear.com/comparing-types-gearboxes/).
- Lead screws: sliding contact (acme/trapezoidal); economical, good precision; efficiency lower than ball screws — [Thomson](https://www.thomsonlinear.com/en/products/lead-screws).
- Ball screws: recirculating balls; high efficiency, load capacity, positioning accuracy; DN value limits speed — [THK](https://tech.thk.com/en/products/pdf_download.php?file=E_15_BallScrew.pdf); [Thomson](https://www.thomsonlinear.com/downloads/screws/Precision_Screws_ctuk.pdf).
- Roller screws: planetary/recirculating rollers; highest load capacity, stiffness, life, shock tolerance; up to 50% higher speed than comparable ball screw — [SKF](https://www.skf.com/skf/campaign/mechatronicsin/media/4351_EN.pdf); [Tolomatic](https://www.tolomatic.com/products/product-details/roller-screw); [Schaeffler](https://medias.schaeffler.us/en/linear-motion/roller-screws).

### Inferences
- For precision servo axes, roller/ball screws dominate linear motion; for rotary axes, harmonic/cycloidal gearboxes provide near-zero backlash.

### Gaps
- No comprehensive efficiency tables found for all gearbox types in one source; values cited are typical ranges from greensky-power and ATO.

#### Power-transmission elements (detailed)

**19. Shaft**
- Description: Rotating member, usually circular, transmits power/motion; provides axis for gears, pulleys, flywheels, cranks, sprockets, couplings — [DAV University](https://davuniversity.org/images/files/study-material/MEC103-Mechanical%20Engineering%20Fundamentals-Power%20Transmission%20Devices%20-%20Belt,%20Rope,%20Chain,%20%20Gear,%20Keys.pdf).
- Misalignment: N/A (shaft itself); must be sized for torque, bending, critical speed.
- Advantages: fundamental, versatile.
- Limitations: fatigue, misalignment-induced bending, corrosion, excessive loading — [BTL-UK](https://blog.btl-uk.com/elements-of-mechanical-power-transmission-systems).
- Applications: all rotating machinery.
- When to select: always present in rotary power trains; size per torque/bending/critical speed.

**20. Pulley (sheave)**
- Description: Wheel transmitting motion via belts (flat, V, timing/toothed); sets speed/torque ratio; drive vs idler — [eINDUSTRIFY](https://eindustrify.com/blog/power-transmission-systems-component-types-functions); [Gates](https://www.gates.com/us/en/power-transmission/power-transmission-components/idler-pulleys.html).
- Types: flat, V-groove, timing (toothed), multi-groove (serpentine).
- Misalignment: must be aligned; small errors cause wear.
- Advantages: simple, low cost, overload protection (belt slip), shock absorption.
- Limitations: slip (friction belts), wear, tension maintenance, speed ratio limited by belt.
- Applications: HVAC, automotive, conveyors, general industry.
- When to select: cost, shock absorption, overload protection, long center distances.

**21. Sprocket**
- Description: Toothed wheel engaging chain or toothed belt; transmits motion without slip — [DAV University](https://davuniversity.org/images/files/study-material/MEC103-Mechanical%20Engineering%20Fundamentals-Power%20Transmission%20Devices%20-%20Belt,%20Rope,%20Chain,%20%20Gear,%20Keys.pdf).
- Styles: A (no hub extension), B (one side), C (both sides), D (detachable bolt-on hub) — [DAV University](https://davuniversity.org/images/files/study-material/MEC103-Mechanical%20Engineering%20Fundamentals-Power%20Transmission%20Devices%20-%20Belt,%20Rope,%20Chain,%20%20Gear,%20Keys.pdf).
- Misalignment: limited; precise alignment needed.
- Advantages: positive drive (no slip), high torque, compact.
- Limitations: lubrication, wear, noise, no overload protection.
- Applications: conveyors, bicycles, agricultural, industrial chain drives.
- When to select: positive (non-slip) transmission, dirty/wet environments, precise ratio.

**22. Idler**
- Description: Free-spinning pulley/sprocket that changes belt/chain path, increases wrap angle, reduces vibration; can be smooth or toothed — [Gates](https://www.gates.com/us/en/power-transmission/power-transmission-components/idler-pulleys.html); [tec-science](https://www.tec-science.com/mechanical-power-transmission/belt-drive/belt-tensioner-systems-for-belt-drives).
- Advantages: increases power capacity, reduces vibration, guides belt.
- Limitations: bearing wear, alignment, added friction.
- Applications: automotive accessory drives, long belt runs.

**23. Tensioner**
- Description: Device (eccentric, spring-loaded, adjustable-arm, automatic) maintaining belt/chain tension; absorbs load changes — [tec-science](https://www.tec-science.com/mechanical-power-transmission/belt-drive/belt-tensioner-systems-for-belt-drives); [McMaster-Carr](https://www.mcmaster.com/products/idler-tensioners).
- Types: eccentric pulley, spring-loaded arm, adjustable screw, automatic (hydraulic/spring), tensioning ring.
- Advantages: compensates stretch/temperature, absorbs shock, extends belt life.
- Limitations: added complexity, spring fatigue, maintenance.
- Applications: automotive, conveyors, industrial belt drives.
- When to select: long belts, variable loads, automatic maintenance of tension.

**24. Gearbox / speed reducer (general)**
- Description: Enclosed gear train reducing speed and multiplying torque; motor-mounted or standalone — [ATO](https://www.ato.com/speed-reducers).
- Types and comparison — [greensky-power](https://greensky-power.com/different-types-of-speed-reducers):
  - Spur: 1:1–10:1 per stage (to 200:1 multi), 96–98% efficiency, moderate backlash, inline, not self-locking.
  - Helical: 1:1–10:1, 95–98%, low-moderate backlash, inline/parallel.
  - Planetary: 3:1–10:1 (to 1000:1), 95–97%, very low backlash (1–16 arcmin), coaxial.
  - Worm: 5:1–100:1, 50–90% (falls with ratio), right-angle, self-locking above ~20–25:1.
  - Cycloidal: 6:1–87:1 (to 7569:1 multi), 85–93%, low backlash (1–5 arcmin).
  - Harmonic (strain-wave): 30:1–320:1, 60–90%, ultra-low backlash (<1 arcmin), coaxial.
  - Bevel: 1:1–6:1 per stage, 95–98%, right-angle.
- Advantages: precise ratio, compact, enclosed lubrication.
- Limitations: cost, backlash, efficiency varies (worm lowest), maintenance.
- Applications: robotics, conveyors, machine tools, AGVs, wind turbines.
- When to select: by ratio, torque, backlash, efficiency, shaft geometry, self-locking need.

**25. Planetary gearbox (detail)**
- Description: Sun gear drives planet gears inside ring gear; coaxial, load shared across multiple teeth — [Neugart](https://www.neugart.com/en-us/planetary-gear-reducer); [ZHY Gear](https://www.zhygear.com/comparing-types-gearboxes/).
- Advantages: compact, high torque density, high efficiency (95–97%), low backlash, long life.
- Limitations: complex, cost, fixed structure (locked component set at factory).
- Applications: servos, robotics, AGVs, wind turbines (speed-increasing stages).
- When to select: compact high-torque coaxial servo axes.

**26. Worm gearbox (detail)**
- Description: Worm (screw) meshes bronze worm wheel; right-angle; large ratio in one stage; self-locking above ~20–25:1 — [ATO](https://www.ato.com/speed-reducers); [Superior Gearbox](https://www.superiorgearbox.com/products/worm-gear/low-input-speed-worm-reducers).
- Advantages: high ratio in small package, self-locking, low cost, right-angle.
- Limitations: low efficiency (50–90%, worse at high ratio), heat, not back-drivable.
- Applications: conveyors, lifts, gates, indexing tables.
- When to select: right-angle, high ratio, self-locking, cost-sensitive.

**27. Cycloidal gearbox**
- Description: Eccentric cam discs drive rollers in housing; two-stage reduction; virtually backlash-free — [Nabtesco](https://www.nabtesco.de/en/products/cycloidal-gears); [Nabtesco functional principle](https://www.nabtesco.de/en/service/faq/technologies/functional-principle-of-cycloidal-gears).
- Specs: hysteresis <1 arcmin, pure backlash 0.1–0.2 arcmin, torque up to 70,000 Nm, shock load up to 500% rated, ratios 30:1 to 300:1+.
- Advantages: high torque, high rigidity, shock tolerance, compact, long life.
- Limitations: cost, complexity, lower efficiency than planetary.
- Applications: robotics (axes 1–3), rotary indexers, machine tools.
- When to select: high torque + precision + shock loads.

**28. Harmonic (strain-wave) drive**
- Description: Three components: wave generator (elliptical bearing), flexspline (thin cup with teeth), circular spline; zero backlash — [Harmonic Drive](https://harmonicdrive.de/fileadmin/Downloads/Produkte/Kataloge/Harmonic_Drive_Gears_EN_1053522.pdf); [Nabtesco strain wave](https://www.nabtesco.de/en/products/strain-wave-gears).
- Specs: ratios 30:1–320:1, zero backlash, ultra-low hysteresis; for lower torque ranges.
- Advantages: zero backlash, compact, lightweight, high precision.
- Limitations: flexspline fatigue limits torque; lower torque than cycloidal; cost.
- Applications: robotics (wrist/hand axes), aerospace, medical, precision instruments.
- When to select: zero backlash in compact space, lower torque.

**29. Lead screw (acme/trapezoidal)**
- Description: Screw and nut with sliding (trapezoidal) thread; converts rotation to linear motion; economical — [Thomson](https://www.thomsonlinear.com/en/products/lead-screws).
- Misalignment: none (linear axis); tolerates some; side loads not tolerated.
- Efficiency: moderate (sliding friction); lower than ball screws.
- Advantages: low cost, simple, self-locking possible, quiet, compact.
- Limitations: lower efficiency, wear, backlash unless preloaded, speed limited.
- Applications: actuators, lifts, medical beds, low-cost positioning.
- When to select: cost-sensitive, moderate duty, self-locking, low speed.

**30. Ball screw**
- Description: Screw and nut with recirculating balls in gothic-arc profile; rolling contact; high efficiency — [THK](https://tech.thk.com/en/products/pdf_download.php?file=E_15_BallScrew.pdf); [Thomson](https://www.thomsonlinear.com/downloads/screws/Precision_Screws_ctuk.pdf).
- Specs: efficiency ~90%+, DN value limits speed (e.g. N2=180,000/D for THK caged); accuracy grades (P5 etc.).
- Advantages: high efficiency, high load capacity, precise positioning, long life, high speed.
- Limitations: cost, requires lubrication, not self-locking, sensitive to contamination, preload needed for zero backlash.
- Applications: CNC machines, robotics, semiconductor, aerospace.
- When to select: precision linear motion, high speed/duty, efficiency.

**31. Roller screw (planetary/recirculating)**
- Description: Screw with planetary/recirculating rollers; many contact points; highest load/stiffness — [SKF](https://www.skf.com/skf/campaign/mechatronicsin/media/4351_EN.pdf); [Tolomatic](https://www.tolomatic.com/products/product-details/roller-screw); [Schaeffler](https://medias.schaeffler.us/en/linear-motion/roller-screws).
- Specs: Schaeffler diameters 8–240 mm, leads 2–50 mm, dynamic load up to 3,994 kN; speed up to 50% higher than comparable ball screw; acceleration up to 3×.
- Advantages: very high dynamic/static load, high stiffness, long life, shock tolerance, fine lead (down to 1 mm) for high resolution.
- Limitations: highest cost, complex, lubrication, contamination sensitivity.
- Applications: aerospace, defense, heavy machinery, injection molding, medical.
- When to select: extreme loads, long life, high acceleration, compact high-force.

## Selection Criteria and Design Considerations

### Takeaway
Selection should match misalignment (type and magnitude), torque/speed, torsional stiffness and backlash requirements, damping, environment, and cost; use manufacturer sizing (service factors ~1.25–2.3 for industrial drives) and verify alignment. Sources: IQS Directory, AutomationDirect, SKF, Falk.

### Cited Findings
- Coupling must not contribute to vibration; select based on desired dampening; jaw couplings damp well — [Ruland](https://www.ruland.com/media/wysiwyg/PDF/Coupling-Failure-Article.pdf).
- Excessive misalignment accelerates premature failure; bellows couplings need alignment within 0.2–0.4 mm parallel for infinite life — [R+W](https://blog.rw-america.com/hs-fs/hub/237991/file-39863538-pdf/docs/basics_of_flexible_bellows_couplings.pdf).
- Service factors: e.g. 1.25 for lobe blower; SKF example 2.29 for boiler feed pump; torque limiter switching torque ≥30% above max operating torque — [Powerdrive](https://www.powerdrive.com/Downloads/ECatalogs/Coupling/Coupling.pdf); [KTR](https://uat.ktr.com/us/en/products/ruflex-torque-limiters/ruflex-with-rotex).
- For high torque/high speed: gear, grid, disc couplings; elastomeric popular up to ~115 hp/100 rpm general industrial pumps — [Pumps & Systems](https://www.pumpsandsystems.com/coupling-types-different-applications).
- Turbine-driven equipment ≥3,000 rpm: disc coupling — [Pumps & Systems](https://www.pumpsandsystems.com/coupling-types-different-applications).
- High torque: gear or grid coupling — [Pumps & Systems](https://www.pumpsandsystems.com/coupling-types-different-applications).

### Inferences
- Rigid couplings suit only where alignment is maintained and precision dominates; otherwise flexible metallic/elastomeric improve reliability.

### Gaps
- No universal standard (ISO/AGMA) table of coupling misalignment ratings found; manufacturer data governs. Flagged as unverified where from training only (tire coupling details).