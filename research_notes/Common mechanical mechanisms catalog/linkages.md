# Linkage and Motion Mechanisms Catalog

Research notes for a mechanical design knowledge base. Sources: Wikipedia (Four-bar linkage, Slider-crank linkage, Geneva drive), Cornell eCommons mechanism notes, OCW METU four-bar chapter, FIRGELLI mechanism guides, Union College MER312 lecture, SteelJIS escapements, clock escapement mechanics, fiveflute scotch-yoke guide, engineersedge, design-of-machinery references, patent literature.

---

## Fundamental Linkage Types (Four-Bar, Slider-Crank, Scotch Yoke, Crank-Rocker, Drag-Link, Double-Rocker, Crank-Slider, Inverted Slider-Crank)

### Takeaway
Planar linkages are classified by joint type (RRRR 4R quadrilateral, RRRP slider-crank, PRRP double-slider) and by which link is grounded; the four-bar chain is the base kinematic family, with slider-crank and scotch-yoke as its prismatic-joint inversions.

### Cited Findings
- A four-bar linkage is the simplest closed-chain movable linkage: four bodies (bars/links) connected in a loop by four one-DOF joints (revolute R or prismatic P). Planar (parallel planes), spherical, and spatial variants exist. — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Three basic planar four-bar types by joint pattern: (1) RRRR planar quadrilateral; (2) RRRP slider-crank (3 revolute + 1 prismatic); (3) PRRP double-slider (2 revolute + 2 prismatic). — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Link roles: ground/fixed link (frame), crank (revolute link that can complete 360°), rocker (revolute link with limited angular range, not including 0° or 180°), 0-rocker (limited range including 0°), π-rocker (limited range including 180°), floating/coupler (connects input to output). A slider is a crank with pivot at infinity perpendicular to its travel. — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Crank-rocker: shorter side link (input) revolves; other side link rocks/oscillates. Double-crank (drag-link): both ground-connected links fully rotate. Double-rocker: both ground-connected links oscillate. — [CMU RapidProto chpt5](https://www.cs.cmu.edu/~rapidproto/mechanisms/chpt5.html); [FIRGELLI](https://www.firgelliauto.com/blogs/mechanisms/crank-rocker-mechanism); [OCW METU](https://ocw.metu.edu.tr/pluginfile.php/6885/mod_resource/content/1/ch7/7-1.htm)
- Drag-link (double-crank): shortest link is the frame; both side links rotate fully. Also called "drag link mechanism"; common in windshield-wiper drives and pumpjacks. — [OCW METU](https://ocw.metu.edu.tr/pluginfile.php/6885/mod_resource/content/1/ch7/7-1.htm); [FIRGELLI](https://www.firgelliauto.com/blogs/mechanisms/grashof-linkage)
- Double-rocker: link opposite the shortest link is the frame; both side links oscillate (e.g., Ackermann steering). — [OCW METU](https://ocw.metu.edu.tr/pluginfile.php/6885/mod_resource/content/1/ch7/7-1.htm); [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Slider-crank (crank-slider): 3 revolute + 1 prismatic joint. In-line: slider travel line passes through crank pivot → symmetric (balanced) motion, equal forward/return time. Offset: pivot not on slider line → quick-return (unequal stroke times). — [Wikipedia, Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage)
- Slider-crank kinematics: x = r cos α + sqrt(l² − r² sin² α) (piston displacement from TDC), where r = crank radius, l = connecting-rod length, α = crank angle from TDC. Approximate simple-harmonic x ≈ r cos α + l (valid l >> r). Torque τ = F r sin(α+β). — [Wikipedia, Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage)
- Design rule: crank (L2) = stroke/2; connecting rod (L3) ≥ 3 × crank length (to limit acceleration/secondary imbalance). — [Wikipedia, Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage)
- Offset slider-crank design equations (stroke S, imbalance angle β, angle of line M θ_M): L1 = S·[sin θ_M sin(θ_M−β)/sin β]; L2 = S·[(sin θ_M − sin(θ_M−β))/(2 sin β)]; L3 = S·[(sin θ_M + sin(θ_M−β))/(2 sin β)]. — [Wikipedia, Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage)
- Inverted slider-crank: connecting rod (coupler) becomes the ground link; slider connects directly to crank. Used in backhoe/crane actuators and swinging gates. — [Wikipedia, Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage)
- Slider-crank inversions: 1st (ground fixed) → reciprocating engine/compressor; 2nd (crank fixed) → Whitworth quick return, rotary engine; 3rd (connecting rod fixed) → slotted crank/oscillatory engine; 4th (slider fixed) → hand pump/bull engine. — [Wikipedia, Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage); [IIT KGP VLab quick-return](https://mr-iitkgp.vlabs.ac.in/exp/quick-return-mechanism/theory.html)
- Scotch yoke (PRRP double-slider): crank pin slides in a slot in the yoke, converting rotary to linear motion with pure sinusoidal motion. Equations: x = r cos θ; stroke = 2r; v = −r ω sin θ; a = −r ω² cos θ. — [FIRGELLI Scotch yoke](https://www.firgelliauto.com/blogs/mechanisms/scotch-yoke); [EngineersEdge](https://www.engineersedge.com/mechanics_machines/scotch_yoke_mechanism__14921.htm)
- Scotch-yoke advantages: exact simple-harmonic motion, no connecting-rod secondary imbalance, fewer parts; limitations: high contact pressure at pin/slot (line contact), wear, lubrication, balancing at speed; torque T = p·A·d (actuator) varies with angle; pin is single line contact. — [Assured Automation](https://assuredautomation.com/news-and-training/scotch-yoke-piston-actuators); [fiveflute guide](https://www.fiveflute.com/guide/how-to-design-a-scotch-yoke-mechanism); [FIRGELLI](https://www.firgelliauto.com/blogs/mechanisms/scotch-yoke)
- Other special 4R linkages: parallelogram/antiparallelogram, deltoid (Galloway/kite), trapezium (Arglin), Chebyshev, Hoecken, Roberts, Watt's, Scott-Russell (exact straight-line), Peaucellier–Lipkin (exact straight-line), pantograph, Ackermann steering. — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)

### Inferences
- For workshop-scale builds, slider-crank with l/r ≥ 3 and crank-rocker with transmission angle > 45° are the safest default choices; scotch yoke suits low-speed sinusoidal drives (compressors, valve actuators) where its simple kinematics outweigh pin wear.

### Gaps
- No specific dimensional tables for deltoid/trapezium linkages found; straight-line mechanism kinematics (Peaucellier, Scott-Russell) not covered in depth here.

---

## Grashof Conditions and Four-Bar Classification

### Takeaway
Grashof's condition S + L ≤ P + Q (shortest + longest ≤ sum of other two) determines whether a four-bar has at least one fully rotating link; combined with which link is grounded, it yields crank-rocker, drag-link (double-crank), or double-rocker, with non-Grashof chains yielding 0-rockers/π-rockers.

### Cited Findings
- Grashof condition: if S + L ≤ P + Q (S shortest, L longest, P/Q intermediate), the shortest link can rotate fully relative to a neighboring link. — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage); [OCW METU](https://ocw.metu.edu.tr/pluginfile.php/6885/mod_resource/content/1/ch7/7-1.htm)
- Classification by fixed link when Grashof satisfied: (a) shortest link fixed → double-crank (drag-link); (b) link adjacent to shortest fixed → crank-rocker; (c) link opposite shortest fixed → double-rocker. — [OCW METU](https://ocw.metu.edu.tr/pluginfile.php/6885/mod_resource/content/1/ch7/7-1.htm); [FIRGELLI Grashof](https://www.firgelliauto.com/blogs/mechanisms/grashof-linkage)
- Non-Grashof (S + L > P + Q): no link fully rotates; all four are rockers (0-rocker/π-rocker types). — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Special case S + L = P + Q: folding/change-point linkages (links become collinear twice per revolution); Grashof margin = P + Q − S − L. — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage); [FIRGELLI four-bar](https://www.firgelliauto.com/blogs/mechanisms/four-bar-linkage)
- Eight-case classification via T1 = g+h−a−b, T2 = b+g−a−h, T3 = b+h−a−g (a=input crank, b=output crank, g=ground, h=floating): Grashof rows (−−+ crank-crank, +++ crank-rocker, +−− rocker-crank, −+− rocker-rocker) and non-Grashof rows (−−− 0-rocker/0-rocker, −++ π-rocker/π-rocker, +−+ π-rocker/0-rocker, ++− 0-rocker/π-rocker). — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Four-bar has 1 DOF (3 moving rigid bodies × 3 variables − 4 pin joints × 2 constraints = 1). — [Illinois DynRef](https://dynref.engr.illinois.edu/aml.html)
- Transmission angle μ: angle between coupler and follower; optimum μ = 90°. Critical transmission angle is the value (min or 180−max) farthest from 90°. Practical design rule: keep minimum transmission angle above ~40–45° throughout the cycle to avoid binding/stalling under load. — [OCW METU](https://ocw.metu.edu.tr/pluginfile.php/6885/mod_resource/content/1/ch7/7-1.htm); [3dmechanism.com](https://www.3dmechanism.com/post/four-bar-linkage-mechanism-explained); [UArk pressbooks](https://uark.pressbooks.pub/mechanicaldesign/chapter/mechanism-analysis)
- Toggle positions occur when input crank and coupler are collinear (extreme positions), giving near-infinite mechanical advantage; transmission angle approaches 0°/180° at toggle. — [Union College MER312](https://rbb.union.edu/courses/mer312/content/data/Lectures/MER312%20L14%20Graphical%20Synthsys%20Intro.pdf); [3dmechanism.com](https://www.3dmechanism.com/post/four-bar-linkage-mechanism-explained)
- Time ratio Q = (time of slower stroke)/(time of quicker stroke) ≥ 1; for quick-return, imbalance angle β = 180°·(Q−1)/(Q+1). — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Quick-return examples: cutting machines, package-moving devices; symmetrical (balanced) examples: windshield wipers, engines/pistons, window cranks. — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)

### Inferences
- A Grashof crank-rocker with μ_min > 45° and l/r ratio giving β for the required Q is the default selection for rotary-to-oscillatory tasks; non-Grashof chains are only useful when bounded oscillation of both links is desired (e.g., steering).

### Gaps
- Exact algebraic formula for μ_min for arbitrary four-bar lengths not extracted (graphical/CAD or law-of-cosines method cited); see UArk pressbooks for cosine-law approach.

---

## Common Special Mechanisms (Toggle, Bell Crank, Rocker, Quick-Return, Geneva, Ratchet/Pawl, Escapement)

### Takeaway
Special mechanisms trade motion conversion (rotary↔linear, continuous↔intermittent, direction change) against wear and impact; each has well-known design limits (transmission angle, contact pressure, engagement/disengagement acceleration discontinuity).

### Cited Findings — Toggle
- Toggle linkage: two links meeting at a central pivot near 180°; provides enormous (theoretically infinite) mechanical advantage at end of stroke; self-locking near straight-line position. Used in toggle clamps, rock crushers, riveting machines, injection molding, press tools. — [Industrial Engineering World (FB)](https://www.facebook.com/100090508983109/posts/types-of-linkage-mechanisms-1-four-bar-linkage-the-simplest-closed-loop-linkage-/977970881896536); [DT Online bell crank/toggle](https://wiki.dtonline.org/index.php/Bell_Crank)
- Toggle clamp commercial types use toggle rather than high-ratio bell-crank because toggle gives effectively infinite MA at end of stroke without long-arm flex. — [FIRGELLI bell-crank](https://www.firgelliauto.com/blogs/mechanisms/bell-crank-lever-changing-direction-of-force)

### Cited Findings — Bell Crank
- Bell crank: L-shaped (or angled) lever pivoted at vertex; redirects force/motion through an arbitrary angle (90° common). Arm-length ratio sets mechanical advantage (MA = L_out/L_in for force). Named from Victorian doorbell/servant-bell linkages. Used in aircraft aileron runs, bicycle cantilever brakes, robot grippers. — [DT Online](https://wiki.dtonline.org/index.php/Bell_Crank); [FIRGELLI bell-crank](https://www.firgelliauto.com/blogs/mechanisms/bell-crank-lever-changing-direction-of-force)
- Practical limit: for ratios above ~4:1, switch to toggle or screw clamp (flex problem). — [FIRGELLI bell-crank](https://www.firgelliauto.com/blogs/mechanisms/bell-crank-lever-changing-direction-of-force)

### Cited Findings — Quick-Return (Whitworth & Crank-Shaper/Slotted-Lever)
- Two common quick-return types: (1) Crank and slotted lever (crank-shaper): link 3 (connecting rod) fixed; driving crank CB rotates; sliding block on crank pin slides in slotted bar AP, oscillating it; ram reciprocates along line perpendicular to AC. Time ratio = β/α (cutting/return angles). (2) Whitworth: link 2 (crank) fixed; driving crank CA rotates; slider on crank pin slides in slotted bar PA (pivoted at D); connecting rod PR carries ram. Time ratio = α/β. — [IIT KGP VLab](https://mr-iitkgp.vlabs.ac.in/exp/quick-return-mechanism/theory.html)
- Shaper size range typically 175–900 mm stroke; shaper removes metal on forward cutting stroke only; quick return reduces idle time. — [IRJMETS shaper paper](https://doi.org/10.56726/irjmets30469)
- Whitworth example dimensions from a student project: r1=2.5 cm, r2=1.0 cm, r4=6.5 cm, r5=3.0 cm, output slider 5.0 cm above lowest ground pin, phase θ1=90°. — [RobotPark Whitworth CAD report](https://www.robotpark.com/academy/LR/51029_Whit-Worth-QuickReturn-Mechanism-Robotpark.pdf)
- Whitworth dynamic analysis: input torque from static equilibrium of each link; output force F_L on slider; friction neglected; torque T_s = r_g2 cos(θ2+δ2) F_12y − ... (matrix formulation). — [RobotPark report](https://www.robotpark.com/academy/LR/51029_Whit-Worth-QuickReturn-Mechanism-Robotpark.pdf)

### Cited Findings — Geneva Drive (Maltese Cross)
- Geneva drive converts continuous rotation to intermittent rotary motion: drive wheel with a pin engages slots in driven wheel; a raised circular locking disc locks the driven wheel between steps. Minimum 3 slots; commonly 4–12 (rarely >18). Per revolution of drive, driven advances 360°/n. — [Wikipedia, Geneva drive](https://en.wikipedia.org/wiki/Geneva_drive); [Cornell eCommons ch.9](https://ecommons.cornell.edu/server/api/core/bitstreams/4686812a-7d97-47e4-8f46-1fb663eb41fd/content)
- Design equations (n slots, Z): semi-indexing angle (driven) α = π/Z; (driver) β = π(Z−2)/(2Z); locking section angle γ = π/2·(Z+2)?? (source gives γ = π/2 (Z+2) = 270° for Z=4, i.e. γ = (Z+2)π/2? check: for Z=4, (4+2)*90=540? source says 270°; likely γ = (Z−2)π/(2Z)?). Centre distance c, crank radius r2: basic criterion that centrelines of slot and crank are mutually perpendicular at engagement/disengagement. — [IJRAME Geneva paper](https://ijrame.com/wp-content/uploads/2021/07/V4i520.pdf)
- Geneva example (4-slot): R=40 mm (Geneva wheel radius), a=56.5 mm (centre distance), rd=60 mm (driving wheel radius), r=40 mm (cam radius), rp=2.5 mm (pin radius); slot width t=5 mm, slot length l=25 mm, shaft ds=15 mm. Indexing time ratio ν = β/π = 0.25 for Z=4. — [IJRAME Geneva paper](https://ijrame.com/wp-content/uploads/2021/07/V4i520.pdf)
- Limitation: acceleration discontinuity at engagement/disengagement → impact; conventional design simple/inexpensive (straight lines + circular arcs). Variants: groove-cam Geneva (controls pin radius/acceleration), locking-slide Geneva, internal groove Geneva (tangential entry), elliptical-gear drive Geneva (pin velocity minimum at entry). — [Cornell eCommons ch.9](https://ecommons.cornell.edu/server/api/core/bitstreams/4686812a-7d97-47e4-8f46-1fb663eb41fd/content); [IJRAME](https://ijrame.com/wp-content/uploads/2021/07/V4i520.pdf)
- Inverse Geneva: wheel rotates same direction as crank; less radial space; locking by circular segment wiping against rim. — [IJRAME](https://ijrame.com/wp-content/uploads/2021/07/V4i520.pdf)
- Applications: film projectors (intermittent sprocket), indexing devices for machine tools, automatic machinery, dial indicating, switch positioning. — [Analysis of Geneva Mechanisms (j09782)](https://doi.org/10.5594/j09782); [IJRAME](https://ijrame.com/wp-content/uploads/2021/07/V4i520.pdf)

### Cited Findings — Ratchet & Pawl
- Ratchet mechanism: ratchet wheel A, oscillating lever B carrying driving pawl C, supplementary (holding) pawl D prevents backward motion; when B moves CCW, C drives wheel a fraction of a revolution; on return stroke C slides over teeth while D holds wheel. — [CMU RapidProto chpt8](https://www.cs.cmu.edu/~rapidproto/mechanisms/chpt8.html)
- Design rule: common normal at contact point N must pass between pawl and wheel centers; otherwise pawl forced out of contact under load unless held by spring. Pawl held against wheel by spring during motion. Reversible pawl requires modified tooth shape for drive in either direction. — [CMU RapidProto chpt8](https://www.cs.cmu.edu/~rapidproto/mechanisms/chpt8.html)
- Overrunning clutch: special form of ratchet. — [CMU RapidProto chpt8](https://www.cs.cmu.edu/~rapidproto/mechanisms/chpt8.html)
- Inverse escapement (ratchet-like): solenoid/cam indexes wheel; one drive tooth must retract before other strikes (lost motion); impact-based indexing; up to ~3000 cpm; tooth wear affects accuracy less than ratchet. — [SteelJIS escapements](https://steeljis.com/roymech/cams_springs/escapements.php)

### Cited Findings — Escapement
- Escapement controls a spring/weight-driven mechanism so it moves in regulated steps governed by pendulum/oscillator; true escapements release force to drive load (control device), main power flows through escapement. Horological escapements: recoil, Graham (dead-beat), Swiss lever; efficiencies below 50% (more than half power lost in escapement). — [SteelJIS](https://steeljis.com/roymech/cams_springs/escapements.php); [Abbey Clock EscMechanics](https://abbeyclock.com/EscMechanics.pdf)
- Graham (dead-beat): curved locking faces so escape wheel does not move during lock (no recoil); preferred in clocks. Swiss lever watch: flat locking faces ~15° from escape circle radius → "draw" (~1° extra rotation) to keep pallet in place; detached lever. — [Abbey Clock](https://abbeyclock.com/EscMechanics.pdf)
- Power transfer: no power at 0° or 90° between tooth and pallet directions; optimum impulse face perpendicular to bisector; maximum efficiency when pallet's impulse face is at 90° to half-way direction. — [Abbey Clock](https://abbeyclock.com/EscMechanics.pdf)
- Escapements can control very large forces (steeple clocks ~hundreds of kN; fuse-bomb timers to 30,000–40,000 g). High-precision horological escapements require great experience; small config changes cause large performance changes. — [SteelJIS](https://steeljis.com/roymech/cams_springs/escapements.php)
- Inverse escapements are cam systems with follower driving cam; used in electromechanical counters; low cost. — [SteelJIS](https://steeljis.com/roymech/cams_springs/escapements.php)

### Inferences
- For workshop-scale intermittent indexing, Geneva (4–6 slots) is simplest and most robust; ratchet+pawl suits unidirectional feed with spring-loaded pawl; escapements are only justified when regulated timing (clock-like) is required.

### Gaps
- No detailed ratchet tooth geometry equations (tooth angle, pitch) found; CMU source gives qualitative design rule only. Escapement design equations (lock angle, drop, impulse angle) referenced but not fully extracted.

---

## Standard Texts Emphasis (Shigley, Norton, Mabie/Reinholtz, Uicker/Pennock/Shigley)

### Takeaway
Standard texts converge on Grashof classification, transmission-angle limits (~40–45° min), quick-return time ratio, and slider-crank l/r ≥ 3; Norton emphasizes synthesis/iteration, Shigley emphasizes strength/fatigue alongside kinematics, Mabie/Reinholtz and Uicker/Pennock/Shigley emphasize analytical kinematics (vector loops, complex numbers).

### Cited Findings
- Norton "Design of Machinery": vector-loop representation, complex numbers as vectors, four-bar and slider-crank position solutions, inverted slider-crank, quick-return mechanisms; synthesis via iterate-and-analyze. — [Norton 5th ed PDF (scribd)](https://www.scribd.com/document/266860705/ch4); [Norton PDF (mechfamily-ju)](https://mechfamily-ju.com/storage/images/files/file_17314351121Fr90.pdf)
- Shigley's Mechanical Engineering Design: terminology/equations/procedures foundational; integrates machine design with strength/fatigue. — [ICDST pdfs](https://dl.icdst.org/pdfs/files4/3fc7c88cb2a5f16a20ef69905c028d99.pdf)
- Mabie & Reinholtz "Mechanisms and Dynamics of Machinery" and Uicker/Pennock/Shigley "Theory of Machines and Mechanisms": analytical kinematics (vector loops, complex numbers); Grashof, transmission angle, toggle positions. — [referenced in searches; OCW METU cites standard texts](https://ocw.metu.edu.tr/pluginfile.php/6885/mod_resource/content/1/ch7/7-1.htm)
- Cornell eCommons "Mechanisms for Intermittent Motion" (ch.9): Geneva, ratchets, escapements dynamics; groove-cam Geneva variants. — [Cornell eCommons](https://ecommons.cornell.edu/server/api/core/bitstreams/4686812a-7d97-47e4-8f46-1fb663eb41fd/content)
- Myszka "Machines and Mechanisms: Applied Kinematic Analysis": time ratio, timing charts, symmetrical vs offset mechanisms, displacement/velocity/acceleration relations. — [cited in Wikipedia Four-bar references](https://en.wikipedia.org/wiki/Four-bar_linkage)

### Inferences
- Textbook consensus: design by dimensional synthesis (iterate-and-analyze), verify Grashof, check μ_min ≥ 40–45°, and for slider-cranks enforce l ≥ 3r; these are the rules an agent should apply automatically.

### Gaps
- Direct quotes/page numbers from Shigley/Norton/Mabie not retrieved (paywalled); reliance on secondary summaries and Wikipedia references.

---

## Notable Patents and Classic Designs

### Takeaway
Classic mechanisms are largely 19th-century inventions (Watt's parallel motion, Whitworth quick return, Geneva watch stop, ratchet) with modern patents refining details (toggle clamps, bell cranks, inverse escapements); Reuleaux/KMODDL at Cornell catalogs physical models.

### Cited Findings
- Bennett's linkage (spatial four-bar) — G.T. Bennett, 1903, "A New Mechanism," Engineering magazine. — [Wikipedia, Four-bar linkage references](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Whitworth quick return — Joseph Whitworth (19th c.), used in shapers/slotting machines; crank-and-slotted-lever variant by James Nasmyth-era shaper (1836 first metal-working paper). — [IRJMETS shaper paper](https://doi.org/10.56726/irjmets30469)
- Geneva drive — originated as watch stop to prevent overwinding mainspring (Geneva watches); now universal in film projectors. — [Analysis of Geneva Mechanisms](https://doi.org/10.5594/j09782)
- Reuleaux model collection at Cornell (KMODDL) catalogs four-bar linkage physical models. — [Wikipedia, Four-bar linkage external links](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Toggle clamp patent example: US4230351A "Link and lever operated toggle latch mechanism". — [Google Patents](https://patents.google.com/patent/US4230351A/en)
- Straight-line mechanisms: Chebyshev linkage, Scott-Russell, Watt's linkage (parallel motion), Peaucellier–Lipkin (exact), Hoecken, Roberts; used in steam engines and suspensions. — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)
- Watt's linkage used in train/car rear suspensions; Ackermann steering uses double-rocker. — [Wikipedia, Four-bar linkage](https://en.wikipedia.org/wiki/Four-bar_linkage)

### Inferences
- For new designs, prefer well-characterized families (crank-rocker, slider-crank, Geneva, toggle) with established design equations; novel linkages (Bennett, Klann, Jansen) require simulation/CAD verification.

### Gaps
- Specific patent numbers/dates for Whitworth, Geneva, ratchet, and escapement origins not retrieved; only US4230351A confirmed via search. Classic patent literature (Google Patents) would need deeper search for exact filing dates.

---

## DFM / Failure-Mode Notes (Cross-Cutting)

### Takeaway
Common failure modes: transmission-angle binding, pin/slot wear (scotch yoke), impact at Geneva engagement, pawl spring fatigue, escapement draw/lock sensitivity; mitigate with lubrication, hardening, spring pre-load, and μ_min ≥ 45°.

### Cited Findings
- Four-bar: mechanism can bind/stall when μ → 0°/180°; keep μ_min ≥ 40–45°; Grashof margin avoids change-point ambiguity. — [3dmechanism.com](https://www.3dmechanism.com/post/four-bar-linkage-mechanism-explained); [OCW METU](https://ocw.metu.edu.tr/pluginfile.php/6885/mod_resource/content/1/ch7/7-1.htm)
- Slider-crank: secondary imbalance from finite l/r; balance shafts needed in high-speed engines; crank at TDC/BDC cannot start from rest under connecting-rod force (locomotive wheels staggered). — [Wikipedia, Slider-crank linkage](https://en.wikipedia.org/wiki/Slider-crank_linkage)
- Scotch yoke: single line contact at pin/slot → high contact pressure, wear; requires lubrication, balancing, guarding; speed limited. — [Assured Automation](https://assuredautomation.com/news-and-training/scotch-yoke-piston-actuators); [fiveflute](https://www.fiveflute.com/guide/how-to-design-a-scotch-yoke-mechanism)
- Geneva: impact at engagement/disengagement due to acceleration discontinuity; groove-cam/elliptical-gear variants mitigate. — [Cornell eCommons ch.9](https://ecommons.cornell.edu/server/api/core/bitstreams/4686812a-7d97-47e4-8f46-1fb663eb41fd/content); [IJRAME](https://ijrame.com/wp-content/uploads/2021/07/V4i520.pdf)
- Ratchet: pawl forced out of contact if common normal outside limits → spring holds pawl; tooth wear reduces accuracy; reversible pawl needs modified teeth. — [CMU RapidProto chpt8](https://www.cs.cmu.edu/~rapidproto/mechanisms/chpt8.html)
- Escapement: <50% efficiency; lock/drop/draw sensitivity; small config changes cause large performance changes; high precision requires experience. — [Abbey Clock](https://abbeyclock.com/EscMechanics.pdf); [SteelJIS](https://steeljis.com/roymech/cams_springs/escapements.php)
- Bell crank: ratios >4:1 cause flex; switch to toggle/screw clamp. — [FIRGELLI bell-crank](https://www.firgelliauto.com/blogs/mechanisms/bell-crank-lever-changing-direction-of-force)

### Inferences
- A default workshop design checklist: (1) choose mechanism family by motion requirement; (2) size via cited equations; (3) verify Grashof (4-bars) and μ_min ≥ 45°; (4) enforce l ≥ 3r (slider-crank); (5) add lubrication/guards for sliding contacts; (6) prototype and measure.

### Gaps
- No quantitative wear/fatigue life equations (e.g., Hertz contact stress for scotch-yoke pin) retrieved; standard texts (Shigley ch. on contact stress) would supply these.