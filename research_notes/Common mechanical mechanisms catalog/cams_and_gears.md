# Cams and Gears Mechanism Catalog

Research notes for a mechanical design knowledge base. Sources: Wikipedia (Cam mechanism, Gear, Epicyclic gearing), mechref.org mechanism-design pages (Cams, Gears), mechanical-design-handbook blog (V-belt), industrialmonitordirect.com (roller chain wrap angle), tec-science (gear undercutting), KHK gears, Cornell eCommons, patents (Google Patents), classic engineering references.

---

## Cam Mechanisms (Plate/Disk, Cylindrical, Face, Linear; Followers; Motion Laws; Geometry; Sizing)

### Takeaway
Cams convert a programmed profile into follower motion; design is governed by the "fundamental law of cam design" (continuous s, v, a and finite jerk), with pressure angle kept ≤30° (translating) / ≤35° (rotating) followers, and profile choice (SHM, cycloidal, polynomial, modified trapezoid) trading peak acceleration, velocity, and jerk.

### Cited Findings
- A cam is a rotating or sliding piece in a mechanical linkage used especially to transform rotary motion into linear (or oscillating) motion; a cam mechanism has two main components: the cam and the follower, which must stay in constant contact. — [Wikipedia, Cam (mechanism)](https://en.wikipedia.org/wiki/Cam_(mechanism))
- The follower's motion is characterized by rise (away from cam center), dwell (at rest), and return (toward cam center); displacement diagrams relate cam angle (deg) to follower radial displacement. — [Wikipedia, Cam (mechanism)](https://en.wikipedia.org/wiki/Cam_(mechanism))
- Cam geometries: radial (follower motion perpendicular to axis), cylindrical (parallel to axis), axial (cam slides linearly). Closure: force-closed (spring/gravity) or form-closed (geometry). Followers: roller (lowest friction, costlier) or static (knife-edge, flat-faced/mushroom). — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- Plate/disc/radial cam: follower moves in a plane perpendicular to the camshaft axis; key terms: base circle (smallest circle to cam profile), prime circle (radius = follower radius + base circle radius), pitch curve (radial displacements applied to prime circle), lobe separation angle (LSA). — [Wikipedia, Cam (mechanism)](https://en.wikipedia.org/wiki/Cam_(mechanism))
- Cylindrical/barrel cam: follower rides in a groove cut into a cylinder; converts rotation to linear motion perpendicular to the axis; can be form-closed (positive positioning, no spring) and provide multi-rotation programs; constant-lead variant gives linear displacement ∝ rotation (like a lead screw). — [Wikipedia, Cam (mechanism)](https://en.wikipedia.org/wiki/Cam_(mechanism))
- Face cam: follower rides on the face of a disk, often in a slot for positive positioning; can implement repetitive motion (closed curve groove) or function generation (stopped groove); common example scroll plate in a scroll chuck. — [Wikipedia, Cam (mechanism)](https://en.wikipedia.org/wiki/Cam_(mechanism))
- Linear cam: cam element moves in a straight line (plate/block/slot/surface profile); input is linear motion; example key of a pin-tumbler lock acting as cam with pins as followers. — [Wikipedia, Cam (mechanism)](https://en.wikipedia.org/wiki/Cam_(mechanism))
- Pressure angle φ is the angle between the follower velocity and the axis of transmission; should not exceed 30° for translating followers or 35° for rotating followers (high φ causes friction/wear/jamming). — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- Fundamental law of cam design: follower position, velocity, and acceleration must be continuous; jerk must be finite (rapid jerk excites harmonics/vibration). — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- Trapezoidal (linear) profile: discontinuous velocity → infinite acceleration spikes; not recommended. — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- Simple harmonic (SHM) profile: s(θ)= h/2[1−cos(πθ/β)], v(θ)= (πh/2β) sin(πθ/β), a(θ)= (π²h/2β²) cos(πθ/β); s and v continuous but acceleration discontinuous at section transitions → infinite jerk. — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- Cycloidal profile: a(θ)=2π(h/β²) sin(2πθ/β); s(θ)=h[θ/β − (1/2π) sin(2πθ/β)]; v(θ)=(h/β)[1−cos(2πθ/β)]; j(θ)=4π²(h/β³) cos(2πθ/β); position/velocity/acceleration continuous and jerk finite. — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- 4-5-6-7 polynomial profile: s(θ)=h[35(θ/β)^4 − 84(θ/β)^5 + 70(θ/β)^6 − 20(θ/β)^7]; 8 boundary conditions (s, v, a, j at 0 and β) → degree-7 polynomial; continuous jerk. — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- Profile selection trade-offs: low peak acceleration (modified trapezoid) for weak joints; low peak velocity (sinusoidal) for smoothing; less aggressive slope (harmonic) to reduce pressure angle. — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- Valve-cam tangent-circle construction: given lift L, base radius R, angle φ = π/2 − θ/2 (θ = dwell angle), center distance C = L/(1−sin φ), tip radius r = R − L·sin φ/(1−sin φ). — [Wikipedia, Cam (mechanism)](https://en.wikipedia.org/wiki/Cam_(mechanism))
- Heart-shaped cam returns a shaft to a set position by roller pressure (used in early Post Office master clocks to sync with GMT). Snail-drop cam raises a follower over 24 h then drops sharply to advance day mechanism; two coaxial snails (roller + solid follower) give precise timing. — [Wikipedia, Cam (mechanism)](https://en.wikipedia.org/wiki/Cam_(mechanism))
- Any normalized rise function s₀(θ) (s₀(0)=0, s₀(1)=1) can be scaled/shifted to any interval [θᵢ, θᵢ+β] and height [hᵢ, h_f]: s(θ)=(h_f−hᵢ) s₀((θ−θᵢ)/β)+hᵢ. — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- Standard cam references: Shigley & Uicker, "Theory of Machines and Mechanisms" (4th ed.) p.200 for cam design; Jensen, "Cam Design and Manufacture" (Industrial Press, 1965); Oberg, "Machinery's Handbook" 25th ed. pp.1050–1055. — [Wikipedia, Cam (mechanism)](https://en.wikipedia.org/wiki/Cam_(mechanism))

### Inferences
- For workshop-scale builds, prefer plate cams with roller followers and form-closed grooves for positive positioning; use cycloidal or 4-5-6-7 polynomial profiles when vibration matters, modified trapezoid when joint strength is the limit.
- Base circle and prime circle should be sized so that pitch-curve curvature remains comfortably larger than the follower radius; pressure-angle check (≤30°/35°) is the primary guard against binding.
- Linear cams (e.g., key duplication) are the natural choice when input is translational; cylindrical cams suit multi-rotation/positive-positioning programs (shift barrels, machine-tool drives).

### Gaps
- Detailed cam undercutting criterion (pitch-curve radius of curvature vs follower radius) and cam sizing equations (base circle radius selection, contact stress) were not extracted from fetched sources; standard texts (Norton, Shigley) cover these.
- Modified trapezoid equations and exact modified-trapezoid peak-acceleration coefficients not retrieved.
- No quantitative wear/fatigue life equations for cam followers (Hertz contact stress) retrieved.

---

## Gear Mechanisms (Spur, Helical, Bevel, Worm, Planetary, Rack-and-Pinion; Tooth Geometry; Ratios)

### Takeaway
Gears trade torque for speed through tooth count ratio N₂/N₁ with efficiency ~98–99% for spur/helical; involute profile is standard because it gives constant velocity ratio and tolerates center-distance variation; module (mm/tooth) or diametral pitch (teeth/in) sizes the set; minimum teeth to avoid undercutting ≈ 2/sin²φ (≈17 for 20°).

### Cited Findings
- Gear: rotating machine part with teeth meshing with another toothed part to transmit rotational motion/torque; smaller member of a pair is the pinion; gear ratio T₂/T₁ = N₂/N₁, ω₂/ω₁ = N₁/N₂. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Ideal-gear power: P = τω; gears in contact share linear velocity; compound trains mount two gears on one shaft to multiply ratios. — [mechref.org, Gears](https://www.mechref.org/md/Gears/)
- Gear types: spur (straight teeth, parallel shafts, no axial thrust, noisy at high speed); helical (angled teeth, smoother/quieter, higher load, axial thrust; >25 m/s pitch-line speed considered high); double-helical/herringbone (cancels axial thrust); worm (screw-like, 10:1–500:1 ratios, self-locking possible, low efficiency); bevel (conical, non-parallel axes, miter at 90°); hypoid (skew axes, point contact, viscous oil); rack-and-pinion (rotary↔linear). — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear); [mechref.org, Gears](https://www.mechref.org/md/Gears/)
- Helical gears: angled teeth engage gradually (line contact grows across face) vs spur line contact; parallel vs crossed configurations; E = β₁+β₂ (same hand) or β₁−β₂ (opposite hand). — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Worm gears: 1-start single thread; self-locking when lead angle small; double-enveloping (cone-drive) for more contact; right/left-handed. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Tooth profile: involute (standard, constant velocity ratio, tolerates center-spacing variation) vs cycloidal (clocks; requires exact center spacing); fundamental law of gearing (force always along same line). — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear); [mechref.org, Gears](https://www.mechref.org/md/Gears/)
- Module m = p/π (circular pitch p); for spur gears pitch diameter d = N·m; center distance a = (m/2)(N₁+N₂). Diametral pitch DP = N/d = π/p; conversion m = 25.4/DP (metric). Standard preferred modules: 0.1,0.2,0.3,0.4,0.5,0.6,0.8,1.0,1.25,1.5,2.0,2.5,3,4,5,6,8,10,12,16,20,25,32,40,50. Standard DP values include 3,4,5,6,8,10,12,16,20,24,32,48,64,72,80,96,100,120,200. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Helical pitch relations: p_n = p cos ψ; pitch diameter d = N·m_n/cos ψ; normal diametral pitch P_nd = P_d/cos ψ. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Pressure angle φ: complement of angle between force direction and line joining centers; for involute gears φ is constant (line of action straight, tangent to both base circles). — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Base circle: in involute gears tooth profile is the involute of the base circle; base circle radius is somewhat smaller than pitch circle radius. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Contact ratio m_c (ε): average number of tooth pairs in contact; transverse m_p = length of action / base pitch; face m_F = face width / axial pitch; total m_t = m_p + m_F. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Backlash: motion error when reversing direction due to tooth gap; provided by reducing tooth thickness by half the desired gap (or entirely off the gear for large-gear/small-pinion pairs) or by increasing center distance; zero-backlash methods: split gear with spring between halves, or tapered teeth with axial slide. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Undercut: fillet curve intersects working profile; minimum teeth to avoid undercutting z_min = 2/sin²φ (≈17 for 20°; ≈32 for 14.5°). — [tec-science, Undercut](https://www.tec-science.com/mechanical-power-transmission/involute-gear/undercut/); [KHK Gears](https://khkgears.net/new/gear_knowledge/gear_technical_reference/involute_gear_profile.html)
- Profile shift: displacement of basic rack datum line from reference cylinder, non-dimensionalized by normal module; used to specify tooth thickness (often for zero backlash) and to avoid undercutting on small pinions. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Long/short addendum teeth: engaging gears with unequal addendums (modified addendum teeth) to improve strength/balance. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Epicyclic/planetary gear train: sun, planet(s), carrier, ring (annulus); kinematic relation N_sω_s + N_rω_r = (N_s+N_r)ω_c; assembly condition (N_s+N_r)/n_p = integer; compound planets (meshed/stepped/multi-stage) for larger ratios. Fixed-carrier ratios: carrier locked → ω_s/ω_r = −N_r/N_s; ring locked → ω_s/ω_c = 1+N_r/N_s; sun locked → ω_r/ω_c = 1+N_s/N_r. — [Wikipedia, Epicyclic gearing](https://en.wikipedia.org/wiki/Epicyclic_gearing)
- Planetary torque ratios: τ_r = τ_s·N_r/N_s; τ_c = −τ_s·(N_r+N_s)/N_s; power balance τ_rω_r+τ_cω_c+τ_sω_s=0. — [Wikipedia, Epicyclic gearing](https://en.wikipedia.org/wiki/Epicyclic_gearing)
- Strain-wave (harmonic) gear: non-rigid (flexspline) gearing, zero backlash, compact, high ratios (robotics/aerospace); magnetic gears transmit torque via magnetic fields (no contact, no wear). — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Gear materials: steel (strength/cost), aluminum (lighter, easier machine), cast iron, engineering plastics (injection-molded, sacrificial), bronze (clocks); ~80% of gearing produced by net-shape molding (powder metallurgy/plastic injection/die casting). — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Gear failure mechanisms: wear, scuffing, pitting, micro-pitting, tooth flank fracture, tooth root fatigue fracture; driven by friction, Hertzian contact pressure, sliding/rolling, bending fatigue, lubrication; standards ISO 6336 and AGMA 2001 define calculation methods. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Standard pressure angles commonly 14.5°, 20°, 25° (industry practice); standard module and DP lists above. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)

### Inferences
- For workshop-scale power transmission, prefer standard-module spur gears (m = 1–4) with ≥18 teeth on the pinion to avoid undercutting; use helical gears where noise/speed matter (accept thrust bearings); worm drives for high single-stage ratios and self-locking.
- Planetary sets give the best torque density and coaxial I/O; check (N_s+N_r)/n_p is integer and use compound planets for larger ratios in compact volume.
- Involute gears tolerate small center-distance errors; cycloidal gears (clocks) do not — important for 3D-printed/hobby gears with loose tolerances.
- Plastic/sacrificial gears are sensible for low-load workshop prototypes and overload protection.

### Gaps
- Exact gear-tooth strength/bending (Lewis) and contact-stress (Hertz) equations, service factors, and AGMA/ISO rating procedures not extracted (paywalled standards); only failure-mechanism categories captured.
- Helical gear thrust-force formula and bevel-gear (spiral bevel) geometry equations not extracted.
- Backlash numeric tolerances/standards (AGMA backlash classes) not retrieved.
- Efficiency values for worm gears (typically 40–90% depending on lead angle) not sourced in fetched pages.

---

## Belts and Chains (V-Belt, Timing Belt, Roller Chain, Sprockets)

### Takeaway
V-belts dominate workshop power transmission (wedge multiplies friction; keep smaller-sheave wrap >120°, belt speed 1000–6500 ft/min, provide center-distance adjustment); roller chains give positive drive (no slip) with ≥120° wrap and 12–25 tooth minimum sprocket counts by speed; timing belts give synchronous, backlash-free motion for precision.

### Cited Findings
- Belt drive: flexible element on pulleys/sheaves; installed by reducing center distance then tensioning; tight side vs slack side; speed ratio ω₁/ω₂ = D₂/D₁ (belt slip negligible). — [mechanical-design-handbook blog, V-Belt](https://mechanical-design-handbook.blogspot.com/2007/09/v-belt-drive-design.html)
- V-belt wedge shape increases friction (higher torque before slip); high-strength cords in rubber; profiles: classical (A,B,C,D), narrow wedge (3V,5V,8V), cogged/raw-edge (AX,BX,5VX) with 2–3% efficiency gain. — [mechanical-design-handbook blog, V-Belt](https://mechanical-design-handbook.blogspot.com/2007/09/v-belt-drive-design.html)
- V-belt design rules: center distance adjustable (never "roll" belt onto sheave); wrap angle >120° on smaller sheave; belt speed avoid <1000 ft/min (use chains) or >6500 ft/min (dynamic instability); matched sets for multi-groove drives; max reduction ratio 6:1 plain V-belt, 7:1 cogged. — [mechanical-design-handbook blog, V-Belt](https://mechanical-design-handbook.blogspot.com/2007/09/v-belt-drive-design.html); [Quizlet V-belt study guide](https://quizlet.com/study-guides/comprehensive-guide-to-belt-drives-and-v-belt-design-princip-ed1e9a7e-07da-422d-97f8-b010e22151c2)
- Wrap angle formula: wrap = 180° − 2·arcsin((D−d)/(2C)) (D large sheave, d small sheave, C center distance); small-sheave wrap should be ≥120°. — [EngiCalcsHub V-belt center distance guide](https://engicalchub.com/guides/vbelt-center-distance-guide/)
- Belt failure causes: misalignment (scrubbing sidewalls, heat), improper tension (under-tension → slip/glazing/heat; over-tension → bearing damage); use laser alignment and sonic tension meters. — [mechanical-design-handbook blog, V-Belt](https://mechanical-design-handbook.blogspot.com/2007/09/v-belt-drive-design.html)
- Timing belt: synchronous (no slip), backlash-free; used in camshaft drives, CNC, 3D printers; pairs with timing pulleys; cogged. — [Wikipedia, Gear (comparison section)](https://en.wikipedia.org/wiki/Gear)
- Roller chain: positive drive (no slip), metallic links wrap around sprockets; requires minimum wrap angle 120° on small sprocket; recommended center distance ~30–50× chain pitch; sprocket minimum tooth counts 12–25 by speed to mitigate chordal action; chain tension: 2–3% mid-span movement of center distance for horizontal drives. — [industrialmonitordirect.com](https://industrialmonitordirect.com/blogs/knowledgebase/roller-chain-drive-design-wrap-angle-and-sprocket-tooth-count); [FIRGELLI chain drive calculator](https://www.firgelliauto.com/blogs/engineering-calculators/chain-drive-calculator-sprocket-length); [Jealco roller chain tensioning guide](https://www.jealco.com/blog/the-engineers-guide-how-to-properly-tension-a-roller-chain-for-maximum-service-life)
- Roller chain chordal action: speed fluctuation as joint passes over sprocket; mitigated by more teeth; efficiency approaches ~98% at proper speed; chains tolerate dirt and high torque; require lubrication. — [roymech.org roller chain](https://roymech.org/Useful_Tables/Drive/Roller_chain.html)
- Chain drive design recommendations: center distance great enough for ≥120° wrap; generally not exceed ~80× pitch without tensioner; avoid excessive sag. — [Maintenance World chain drive design](https://maintenanceworld.com/2013/06/28/chain-drive-design-recommendations/)
- Belts vs chains vs gears: belts flexible/quiet but slip; chains positive drive, higher torque, need lubrication; gears rigid/precise, fixed center distance. — [Wikipedia, Gear (comparison section)](https://en.wikipedia.org/wiki/Gear)

### Inferences
- For workshop machines: use V-belts for motor-to-shaft power (cheap, forgiving alignment), timing belts for synchronous/precision axes (CNC, 3D printer), roller chains for high-torque/dirty environments (conveyors, bicycles).
- Always include an adjustable motor mount or tensioner; never force a belt onto a sheave (breaks cords); for chains, size sprockets ≥12–17 teeth and keep wrap ≥120°.

### Gaps
- Belt length equations (open/crossed belt) and tension equations (T₁/T₂ = e^(μθ csc(β/2))) not extracted; standard texts (Shigley/Mott) provide these.
- Timing-belt tooth profiles (trapezoidal, curvilinear) and allowable loads not sourced.
- Chain pitch selection tables (ANSI chain numbers) and service factors not retrieved.

---

## Textbook Emphasis and Design Rules (Shigley, Norton, Mott, Juvinall/Marshek)

### Takeaway
Standard texts converge on: involute gearing with standard module/DP; minimum pinion teeth ≈17 (20°) to avoid undercutting; pressure angle 20° as default; keep gear contact ratio >1.2; cam fundamental law (continuous s,v,a, finite jerk); pressure angle limits; and design-by-iteration with verification.

### Cited Findings
- Shigley's Mechanical Engineering Design: foundational terminology/equations/procedures; integrates machine design with strength/fatigue; Ch.13 gears, cam design. — [ICDST pdfs](https://dl.icdst.org/pdfs/files4/3fc7c88cb2a5f16a20ef69905c028d99.pdf)
- Norton "Design of Machinery": vector-loop/complex-number kinematics; four-bar, slider-crank, quick-return, planetary; synthesis by iterate-and-analyze. — [Norton 5th ed PDF (scribd)](https://www.scribd.com/document/266860705/ch4); [mechfamily-ju Norton PDF](https://mechfamily-ju.com/storage/images/files/file_17314351121Fr90.pdf)
- Mott "Machine Elements in Mechanical Design" and Juvinall & Marshek "Fundamentals of Machine Component Design": machine-element design, gears, belts, chains, cams; strength/fatigue focus. — [referenced in general engineering education; not directly fetched]
- AGMA standards (ANSI/AGMA 2001, 1012) and ISO 6336 define gear nomenclature, rating, and failure calculation methods. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Machinery's Handbook (Oberg et al.): gear data, cam programming; preferred module/DP tables. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)

### Inferences
- Default workshop design checklist: (1) choose family by motion requirement; (2) size via module/DP and standard tables; (3) enforce z_min on pinions; (4) check contact ratio ≥1.2 and pressure angle; (5) verify cam pressure angle ≤30°/35° and jerk finite; (6) prototype and measure.

### Gaps
- Direct page-level quotes/numerical examples from Shigley/Norton/Mott/Juvinall not retrieved (paywalled); reliance on secondary summaries, Wikipedia, and mechref.
- Mott/Juvinall specific equations not directly fetched; treat as standard-text consensus.

---

## Notable Patents and Classic Designs

### Takeaway
Classic power-transmission inventions (Watt sun-and-planet, Whitworth quick-return, Oldham coupling, harmonic/strain-wave drive, Geneva watch stop) established the families still used; modern patents refine details (adjustable cams, compound planetary timing, double-enveloping worms).

### Cited Findings
- Adjustable cam patent US2922318A (Waldo J. Kelleigh, Electrical Apparatus Company, 1956) for use in mechanical engineering and weaponry. — [Google Patents US2922318A](https://patents.google.com/patent/US2922318A/en)
- Toggle clamp patent US4230351A "Link and lever operated toggle latch mechanism". — [Google Patents US4230351A](https://patents.google.com/patent/US4230351A/en)
- Oldham coupling: invented 1821 by John Oldham to connect misaligned (parallel-offset) shafts on a paddlewheel steamer; three-piece design (two slotted plates + disc). US3404545A. — [Google Patents US3404545A](https://patents.google.com/patent/US3404545A/en); [FIRGELLI Oldham coupling](https://www.firgelliauto.com/blogs/mechanisms/oldham-coupling)
- Harmonic/strain-wave gearing: invented by C. Walton Musser (1957); flexspline + wave generator; zero backlash, high ratio; used in robotics/aerospace. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Geneva drive: originated as watch stop to prevent overwinding mainspring; now used in film projectors, indexing devices, automatic machinery. — [Wikipedia, Geneva drive (referenced in prior research)](https://en.wikipedia.org/wiki/Geneva_drive)
- Harmonic drive patent/assembly: flexspline teeth count differs from circular spline by 2 for reduction. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Ravigneaux planetary gearset (compound, meshed planets) used in automatic transmissions. — [Wikipedia, Epicyclic gearing](https://en.wikipedia.org/wiki/Epicyclic_gearing)

### Inferences
- For new workshop designs, prefer well-characterized families (spur/planetary gears, plate cams, V-belt/chain drives) with established equations; novel mechanisms (harmonic drives, non-circular gears) need simulation/CAD and precise manufacturing.

### Gaps
- Exact patent numbers/dates for Whitworth quick-return, Geneva drive origin, and ratchet escapement not retrieved beyond US2922318A, US4230351A, US3404545A.
- Harmonic-drive detailed geometry (flexspline tooth count, wave-generator ellipse) not extracted.

---

## DFM and Failure-Mode Notes (Cross-Cutting)

### Takeaway
Common failures: cam pressure-angle binding and jerk-induced vibration; gear pitting/scuffing/root fatigue from overload/poor lubrication; belt slip/glazing from low tension and misalignment; chain chordal vibration and wear from low tooth counts; mitigate with standard modules, lubrication, alignment, and conservative sizing.

### Cited Findings
- Cam: mechanism binds when pressure angle exceeds 30°/35°; infinite jerk at discontinuities excites harmonics; roller followers reduce friction but cost more. — [mechref.org, Cams](https://www.mechref.org/md/Cams/)
- Gear: failure mechanisms wear, scuffing, pitting, micro-pitting, flank fracture, root fatigue; driven by friction, Hertzian pressure, sliding/rolling, bending fatigue, lubrication; standards ISO 6336/AGMA 2001. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Undercutting weakens tooth (fillet intersects profile) when pinion has <~17 teeth (20°); avoid via larger pinion, profile shift, or larger pressure angle. — [tec-science, Undercut](https://www.tec-science.com/mechanical-power-transmission/involute-gear/undercut/)
- Helical gears produce axial thrust (needs thrust bearings); double-helical cancels thrust; worm gears have sliding friction and low efficiency; hypoid needs viscous HP oil. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- V-belt: misalignment scrubs sidewalls (heat); under-tension → slip/glazing; over-tension → bearing damage; never roll belt onto sheave. — [mechanical-design-handbook blog, V-Belt](https://mechanical-design-handbook.blogspot.com/2007/09/v-belt-drive-design.html)
- Roller chain: chordal action causes speed fluctuation; keep sprocket teeth ≥12–25 by speed and wrap ≥120°; lubricate; avoid excessive center distance without tensioner. — [industrialmonitordirect.com](https://industrialmonitordirect.com/blogs/knowledgebase/roller-chain-drive-design-wrap-angle-and-sprocket-tooth-count); [Maintenance World](https://maintenanceworld.com/2013/06/28/chain-drive-design-recommendations/)
- Backlash causes motion error on reversal; minimize via zero-backlash gear designs (split/spring, tapered teeth) for precision. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)
- Gear backlash in long trains accumulates; planetary/rigid gears preferred for precision. — [Wikipedia, Gear](https://en.wikipedia.org/wiki/Gear)

### Inferences
- Workshop DFM defaults: use standard modules/DP and off-the-shelf gears; avoid pinions <18 teeth unless profile-shifted; lubricate gears/chains; align belts with straightedge or laser; include tension adjustment; prefer involute gears for tolerance forgiveness.

### Gaps
- Quantitative life equations (Hertz contact stress, bending fatigue, wear rates) and specific lubricant specifications not retrieved; standards (AGMA/ISO) required for rated designs.
- No quantitative cost/manufacturing process comparisons (hobbing vs 3D printing) beyond general notes.
