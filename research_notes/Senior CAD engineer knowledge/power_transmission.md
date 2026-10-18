# Power Transmission Design (Mechanical Engineering)

## Shafts: Torsion, Bending, Combined Loading, Fatigue, Deflection, Stress Concentrations

### Takeaway
A rotating transmission shaft is almost always sized by fatigue (modified Goodman with von Mises combined stress) rather than static stress, because bending is fully reversed while torque is steady; the diameter must also be checked for yielding, deflection, and critical speed, and stress concentrations (keyseats, shoulders, retaining rings) usually govern the final size.

### Cited Findings
- Shigley's Mechanical Engineering Design treats shaft design as material selection, geometric layout, static strength, fatigue strength, deflection/rigidity, and vibration due to natural frequency. — [Shigley Ch.7 slides, Philadelphia University](https://www.philadelphia.edu.jo/academics/mgogazeh/uploads/DESIGN%201%20CH7.pdf)
- Shaft stresses are customized for round shafts: σ_a = K_f M_a c/I, σ_m = K_f M_m c/I (bending); τ_a = K_fs T_a c/J, τ_m = K_fs T_m c/J (torsion), where K_f, K_fs are fatigue stress-concentration factors; axial loads usually ignored. — [IIT Bombay shafts notes (Shigley)](https://www.me.iitb.ac.in/~ramesh/courses/ME423/shafts.pdf)
- These alternating/midrange stresses are combined into alternating and midrange von Mises stresses, then substituted into a fatigue failure criterion (modified Goodman, Gerber, ASME-Elliptic, Soderberg). — [IIT Bombay shafts notes](https://www.me.iitb.ac.in/~ramesh/courses/ME423/shafts.pdf)
- Modified Goodman line: σ_a/S_e + σ_m/S_ut = 1/n (with von Mises stresses substituted); for a rotating shaft with steady bending and torsion, M_m = 0 and T_a = 0 simplify the equations. — [IIT Bombay shafts notes](https://www.me.iitb.ac.in/~ramesh/courses/ME423/shafts.pdf)
- Modified Goodman is widely used for the mean-stress effect; Soderberg inherently guards against yielding, ASME-Elliptic accounts for yielding but is not fully conservative, Gerber/Goodman require a separate yielding check. — [Shigley slides, SUT](http://eng.sut.ac.th/me/2014/document/MachineDesign1/document/Ch_7.pdf)
- Endurance limit modification: S_e = k_a k_b k_c k_d k_e k_f S_e' with S_e' ≈ 0.5 S_ut for steels; factors for surface finish, size, load type, temperature, reliability, miscellaneous. — [Shigley slides, City University](https://www.staff.city.ac.uk/~ra600/ME2105/Analysis/ME2104-A-1.pdf)
- NASA/Loewenthal proposed transmission shafting formula based on elliptical variation of endurance strength with steady torsion (combined cyclic bending + static torsion), with fatigue modifying factors; became basis for ANSI/ASME B106. — [NASA NTRS 19780000107](https://ntrs.nasa.gov/citations/19780000107); [NTRS 19790030937](https://ntrs.nasa.gov/citations/19790030937)
- Keyseat stress concentration (standard end-mill, r/d = 0.02): K_t = 2.14 bending, 2.62 torsion without key, 3.0 torsion with key in place (Peterson charts, per Shigley). — [Shigley slides, Philadelphia University](https://www.philadelphia.edu.jo/academics/mgogazeh/uploads/DESIGN%201%20CH7.pdf)
- Critical speed of shaft without load via Rayleigh's equation; deflection checks include bending, torsional, slope at bearings, shear deflection of short shafts. — [Shigley slides, City University](https://www.staff.city.ac.uk/~ra600/ME2105/Analysis/ME2104-A-1.pdf)
- IJERA study applied modified Goodman to a real shaft, obtaining FOS ≈ 1.72 (Goodman) vs 2.59 (FEA), ~10^7 cycles infinite life. — [IJERA Vol.3 Issue 4](https://www.ijera.com/papers/Vol3_issue4/FS3410611066.pdf)

### Inferences
- For a small workshop, a solid round steel shaft (ANSI 1020–1050, low carbon) with a single keyseat at each component location is the default; fatigue governs, but always check static yield at the keyseat and at shoulders/retaining rings where K_t is highest.
- Stress concentration factors are the single biggest source of error in hand shaft sizing; use K_f (fatigue) not K_t (static) for fatigue, with notch sensitivity q.
- Deflection/critical speed often governs long slender shafts and high-speed shafts even when stress is acceptable.

### Gaps
- Exact Shigley equation coefficients (size factor exponents, notch-sensitivity charts) are in the textbook and were not fully reproduced in the fetched lecture slides; verify against Shigley 10th ed. or Bhandari before coding.
- NASA elliptical criterion differs from modified Goodman; which to default to is a design choice not resolved by sources.

## Bearings: Selection, Types, L10 Life, Lubrication, Mounting

### Takeaway
Bearing selection follows ISO 281 rating life: L10 = (C/P)^p (p=3 ball, 10/3 roller) in millions of revolutions; choose type by load direction/speed/space, then verify fits, clearance, lubrication, sealing, and alignment; actual life is L10a modified by lubrication/contamination factors.

### Cited Findings
- SKF selection process: performance requirements/operating conditions → bearing type & arrangement → size → lubrication → operating temperature/speed → interfaces → execution → sealing/mounting/dismounting. — [SKF bearing selection process](https://www.skf.com/il/products/rolling-bearings/principles-of-rolling-bearing-selection/bearing-selection-process)
- L10 is basic rating life at 90% reliability under constant load/speed; L10 = (C/P)^p; L10h = L10×10^6/(60 n); p=3 ball bearings, 10/3 roller bearings. — [SKF size selection based on rating life](https://www.skf.com/il/products/rolling-bearings/principles-of-rolling-bearing-selection/bearing-selection-process/bearing-size/size-selection-based-on-rating-life); [MROSupply bearing basics](https://www.mrosupply.com/bearings/324511_mb-11_skf-bearing/)
- ISO 281 modified life L10a = a1 × aISO × L10 accounts for lubrication quality, contamination, speed, temperature, accuracy. — [MROSupply bearing basics](https://www.mrosupply.com/bearings/324511_mb-11_skf-bearing/)
- Type selection by load: deep groove ball = primarily radial/light-moderate axial; tapered roller = combined radial+axial heavy; thrust = pure axial; angular contact = combined with larger contact angle; needle = very limited radial space; roller bearings = heavier loads at medium speed, ball bearings = higher speed lower friction. — [SKF selection criteria](https://www.skf.com/us/products/rolling-bearings/principles-of-rolling-bearing-selection/bearing-selection-process/bearing-type-and-arrangement/selection-criteria); [MROSupply](https://www.mrosupply.com/bearings/324511_mb-11_skf-bearing/)
- Static load rating C0: max load without permanent deformation when stationary/slow; dynamic rating C determines L10. — [MROSupply](https://www.mrosupply.com/bearings/324511_mb-11_skf-bearing/)
- Improper lubrication causes over 40% of bearing failures; grease for low-medium speed sealed bearings, oil for high speed/circulation. — [MROSupply](https://www.mrosupply.com/bearings/324511_mb-11_skf-bearing/)
- Deep groove ball bearings: contact angle depends on load and clearance; self-aligning ball for misalignment; rigid bearings (deep groove, angular contact, cylindrical, needle, tapered roller) accommodate misalignment within internal clearance limits. — [SKF selection criteria](https://www.skf.com/us/products/rolling-bearings/principles-of-rolling-bearing-selection/bearing-selection-process/bearing-type-and-arrangement/selection-criteria)
- Tapered roller bearings: separable inner/outer rings facilitate mounting; preload two opposing bearings for rigid application; combined radial+axial in one direction. — [MROSupply SKF 32230](https://www.mrosupply.com/bearings/6488251_32230_skf-bearing/)
- Grease life (L10) for lubricated-for-life deep groove ball bearings follows Arrhenius-type temperature dependence; temperature is dominant. — [SKF grease life PDF](https://cdn.skfmediahub.skf.com/api/public/0901d1968033a3ee/pdf_preview_medium/0901d1968033a3ee_pdf_preview_medium.pdf)

### Inferences
- For small workshop machines: default to deep groove ball bearings (62xx/63xx series) for general shafts; use tapered roller pairs where combined loads/locating are needed; needle bearings where radial space is tight; thrust bearings for pure axial (e.g., lead screws).
- Bearing bore must match shaft diameter (standard ISO series); shaft diameter from fatigue sizing therefore directly selects bearing series — this is the key system-integration link.
- Preload tapered/angular-contact pairs to remove axial play in precision spindles; allow one bearing to float axially to avoid overconstraint.

### Gaps
- Specific fit tolerances (ISO shaft/housing tolerance classes like g6/h6/k6) and clearance classes (C2/C3/C4) values by size not retrieved; consult SKF catalog.
- Bearing mounting (press fits, heating, torque specs) and alignment tolerances not quantified in sources fetched.

## Gears: Spur, Helical, Bevel, Worm, Planetary, Rack-and-Pinion

### Takeaway
Gear design is governed by two AGMA checks — bending fatigue (Lewis/AGMA J-factor) and pitting/contact stress (Hertzian/AGMA I-factor) — with module, face width, and material hardness selected to satisfy both at the required life and reliability; worm gears trade efficiency (40–96%) for high single-stage ratios and possible self-locking.

### Cited Findings
- AGMA 2101-D04 (Fundamental Rating Factors) provides bending stress number and contact stress number equations with factors K_o, K_v, K_s, K_m, K_B, geometry factors J and I, and allowable stress numbers σ_FP, σ_HP by material/hardness. — [AGMA 2101-D04 preview (ANSI)](https://webstore.ansi.org/preview-pages/AGMA/preview_ANSI+AGMA+2101-D04.pdf); [AGMA 908-B89 geometry factors](https://webstore.ansi.org/preview-pages/AGMA/preview_AGMA+908-B89+R1999.pdf)
- AGMA allowable stress numbers are for unidirectional loading, 10^7 cycles, 99% reliability (Shigley road-map). — [Shigley spur gear example (mguler.etu.edu.tr)](http://mguler.etu.edu.tr/Spur_Gear_Example.pdf)
- Bending stress (AGMA): σ = W_t K_o K_v K_s K_m K_B/(F m J) (units consistent); contact stress: σ_c = C_p sqrt(W_t K_o K_v K_s K_m/(d F I)) (Shigley form). — [Shigley spur gear example](http://mguler.etu.edu.tr/Spur_Gear_Example.pdf); [DANotes Cambridge](https://www-mdp.eng.cam.ac.uk/web/library/enginfo/textbooks_dvd_only/DAN/gears/bending/bending.html)
- Geometry factor J decreases (stress increases) for small tooth counts; profile shift can raise J significantly for small pinions. — [DANotes Cambridge](https://www-mdp.eng.cam.ac.uk/web/library/enginfo/textbooks_dvd_only/DAN/gears/bending/bending.html)
- AGMA 901-A92 gives a closed-form minimum-volume spur/helical design procedure including profile shift selection. — [AGMA 901-A92 (KNTU)](https://wp.kntu.ac.ir/asgari/AGMA%20901-A92.pdf)
- Worm gear efficiency: η = tan λ / tan(λ + φ), where λ = lead angle, φ = friction angle (arctan μ); self-locking when λ < φ. Typical μ′ ≈ 0.03–0.08 for lubricated steel/bronze. — [Firgelli worm gear calculator](https://www.firgelliauto.com/blogs/engineering-calculators/worm-gear-calculator-ratio-efficiency); [TEA worm vs planetary](https://technische-antriebselemente.de/en/guides/worm-vs-planetary-gearbox)
- Worm gear ratio i = Z2/Z1 (wheel teeth / worm starts); ratios 5:1 to 80:1 (up to 100–360) in one stage; efficiency 40–96% depending on lead angle, speed, load, lubrication. — [ScienceDirect worm gears](https://www.sciencedirect.com/topics/engineering/worm-gears); [IOP research](https://iopscience.iop.org/article/10.1088/1757-899X/1220/1/012025/pdf)
- Self-locking generally from ~i ≥ 30 (small lead angle); output torque = motor torque × ratio × efficiency. — [TEA worm vs planetary](https://technische-antriebselemente.de/en/guides/worm-vs-planetary-gearbox); [AIMS worm gearbox guide](https://aimsindustrial.com.au/blogs/product-guides/worm-gearbox-selection-guide)
- Planetary gears: coaxial sun/planet/carrier/ring, load shared among 3–5 planets; efficiency 95–98% per stage, ratio 3–10 per stage, up to 1000 multi-stage; no self-locking. — [TEA gearboxes guide](https://technische-antriebselemente.de/en/guides/gearboxes/)
- Bevel gears: 90° axis offset, spiral quieter/higher speed; efficiency 95–98%, ratio 1–6 per stage. Spur: 97–99%, ratio 1.25–6 per stage. — [TEA gearboxes guide](https://technische-antriebselemente.de/en/guides/gearboxes/)
- Helical gears: higher load capacity and quieter than spur; thrust loads must be reacted by bearings. — [Harmonic Drive rack & pinion brochure (helical rack)](https://www.harmonicdrive.net/_hd/content/documents1/Rack-Pinion_Brochure.pdf)
- Backlash: excess tooth space over tooth thickness; allows for thermal/deformation; bevel pinions with few teeth get all backlash on gear; can be eliminated/preloaded with split pinions or dual-pinion systems. — [KHK backlash primer](https://khkgears.us/media/1n2lxhd5/gear-solutions_khk_a-primer-on-backlash-and-its-purpose-in-gear-designs.pdf); [Nidec rack & pinion](https://www.nidec-dtc.com/applying-rack-and-pinion-in-linear-drive-systems)
- Rack-and-pinion: module selection, helical racks for higher precision/lower noise; zero-backlash via split/dual pinion or preload; efficiency ~99%; hardened/ground racks for precision. — [Harmonic Drive](https://www.harmonicdrive.net/_hd/content/documents1/Rack-Pinion_Brochure.pdf); [Nidec](https://www.nidec-dtc.com/applying-rack-and-pinion-in-linear-drive-systems); [Nexen RPS](https://www.nexengroup.com/912745-controller-web-guide-gc300-remote-operation-obs)

### Inferences
- For small workshop builds, standard off-the-shelf spur/helical gearsets (module 1–4 mm) sized by AGMA bending first, then contact; worm reducers for high ratios/holding; planetary for compact high torque.
- Profile shift (addendum modification) is the cheap way to strengthen small pinions and avoid undercut; use AGMA 901 or Shigley guidance.
- Helical gears impose axial thrust; bearing arrangement must include thrust bearings (angular contact/tapered) to react it.

### Gaps
- Full AGMA factor tables (K_v, K_m, K_s, C_p, C_f, Z factors) and allowable stress numbers by hardness not reproduced here; need AGMA 2101-D04 tables.
- Planetary torque-sharing and carrier bearing sizing equations not retrieved.

## Belts: V-Belt, Timing Belt, Flat Belt

### Takeaway
Belt drive design is catalog-driven: select pitch/section from power and speed using manufacturer rating tables and service factors, then set center distance, wrap angle (≥120° preferred), and tension by installation/suggested tension; timing belts add tooth-shear and tensile-cord checks.

### Cited Findings
- Gates heavy-duty V-belt manual: design procedure using service factors, belt selection, minimum pulley diameters, tensioning, wrap angle, belt pull calculations; tension by installation/suggested tension with Krikit gauge; run-in retensioning. — [Gates heavy-duty V-belt design manual](https://www.gates.com/content/dam/documents-library/catalogs/heavy-duty-vbelt-drive-design-manual-en.pdf)
- Continental V-belt installation manual: proper tension essential; under-tension causes slippage/rollover/noise; tensioning tables by belt section. — [Continental V-belt installation manual](https://images.kleen-ritecorp.com/Documents/Manuals/Continental/BL0BX43/Continental%20BX43%20Raw%20Edge%20Cogged%20V-Belt%20Installation%20Manual%202018.pdf)
- V-belt wrap angle: larger on smaller pulley; minimum wrap typically ~120° for adequate friction; belt length/center distance formulas standard. — [Gates heavy-duty manual](https://www.gates.com/content/dam/documents-library/catalogs/heavy-duty-vbelt-drive-design-manual-en.pdf)
- Gates timing belt theory: pitch p = distance between tooth centerlines at pitch line; belt length L = p × z_b (whole teeth); pulley pitch diameter from root diameter and pitch differential; tensile stress proportional to strain in operating range; specific stiffness c_sp. — [Gates timing belt theory white paper](https://www.gates.com/content/dam/documents-library/whitepapers/timing-belt-theory-white-paper.pdf)
- Timing belt pitches: MXL/XL/L/H/XH/XXH (trapezoidal) and GT2/HTD curvilinear (2M–20M); pitch selection from design hp and faster-shaft rpm (Gates chart). — [Gates PowerGrip GT2 drive design manual](https://docs.rs-online.com/5016/0900766b8002d3b7.pdf); [Pfeifer timing belt profiles](https://www.pfeiferindustries.com/documents/Timing%20Belt%20Tooth%20Profiles%20and%20Pitches.pdf)
- Synchronous belt failure modes: tooth shear (from shock/over-tension), tensile cord fracture, land disintegration on small sprockets; curvilinear (HTD/GT) has complete tooth flank contact reducing stress concentration. — [Gates belt failure analysis (NTSB)](https://data.ntsb.gov/Docket/Document/docBLOB?FileExtension=.PDF&FileName=Gates%20Belt%20Failure%20Analysis%20Report-Master.PDF&ID=40414816)
- Polyurethane timing belts: tensile strengths listed by width (e.g., 8M/14M Poly Chain), allowable belt tension ≈ 15% of break strength typical; aramid/carbon cords for low stretch. — [Gates TPU catalog](https://www.gates.com/content/dam/documents-library/catalogs/gates-tpu-product-catalog.pdf); [Gates Poly Chain catalog](https://www.bsc-ind.com/ASSETS/DOCUMENTS/ITEMS/EN/Gates_187L050_Catalog.pdf)
- Gates Polyflex V-belts: 60° profile for compact high-speed drives, speeds >10,000 rpm. — [Gates Polyflex](https://www.gates.com/in/en/power-transmission/v-belts/pu-v-belts.p.8901-000000-000000.v.IN-8903-1320.html)

### Inferences
- For small workshop: prefer timing belts (no lubrication, precise) for moderate power; V-belts for higher power/rough service; flat belts rare.
- Belt pitch/section selection is table-driven by manufacturer; code should call catalog tables or DesignFlex rather than derive from first principles.
- Minimum pulley diameter governs belt life (bending fatigue of cords); never undersize pulley below manufacturer min.

### Gaps
- Explicit V-belt power-rating equations (e.g., (HP) = (T)(N)/63025 with service factor) not in fetched sources; standard formulas are in Shigley/Mott and manufacturer manuals.
- Flat belt (leather/rubber) creep and centrifugal tension equations not retrieved.

## Chains: Roller Chain, Silent Chain, Sprockets

### Takeaway
Roller chain drives are sized by manufacturer power-rating tables corrected for teeth, ratio, center distance, and load type, targeting ~15,000 h life with proper lubrication (≈98% efficiency); sprocket selection emphasizes minimum tooth count (≥17–19 to avoid polygonal effect) and alignment.

### Cited Findings
- ISO 606:2015 specifies short-pitch precision roller/bush chains and sprockets (dimensions, tolerances, min tensile/dynamic strength). — [ISO 606:2015](https://www.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/06/12/61232.html)
- ISO 10823:2004 guidelines for roller chain drive selection, ~15,000 h life; consult supplier for load/environment/maintenance variation. — [ISO 10823:2004](https://committee.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/03/15/31532.html); [ANSI preview ISO 10823](https://webstore.ansi.org/preview-pages/ISO/preview_ISO+10823-2004.pdf)
- Mädler roller chain dimensioning: P_B = P_N × K1 × K2 × K3 × K4 (corrected transmittable power for 15,000 h); K1 teeth factor (11 teeth →2.5, 19→1.35, 25→1.0, 37→0.64), K2 ratio factor, K3 center-distance factor, K4 load type factor (1.0–2.1); efficiency ≈98% with proper lubrication; slack span 1–2% of center distance; sprockets aligned/parallel shafts. — [Mädler roller chains PDF](https://blaetterkatalog.maedler.de/blaetterkatalog/catalogs/MAEDLER_Katalog43_EN/pdf/save/chapter/Roller%20chains%20DIN%20ISO%20606.pdf)
- Duplex chain = 1.75× simplex power, triplex = 2.5× simplex. — [Mädler](https://blaetterkatalog.maedler.de/blaetterkatalog/catalogs/MAEDLER_Katalog43_EN/pdf/save/chapter/Roller%20chains%20DIN%20ISO%20606.pdf)
- Chain lubrication is critical; ISO 10823 covers lubrication methods; poor lubrication shortens life drastically. — [ISO 10823 preview](https://webstore.ansi.org/preview-pages/ISO/preview_ISO+10823-2004.pdf)
- SKF ANSI roller chain sprockets available; sprocket selection by chain series and tooth count. — [SKF ANSI sprockets](https://www.skf.com/us/products/power-transmission/sprockets/ansi-roller-chain-sprockets)

### Inferences
- For small workshop: use ISO 606 roller chain with ≥17–19 teeth on smaller sprocket to reduce polygonal velocity ripple and wear; align shafts and set slack 1–2%.
- Multi-strand chains scale power but need matched sprockets and careful alignment.
- Silent chains (inverted tooth) for high speed/low noise not covered by sources fetched — flag.

### Gaps
- Silent chain (inverted-tooth) design equations and power ratings not retrieved.
- Chain wear elongation limits and replacement criteria not sourced.
- ANSI/ASME chain power-rating tables (Horsepower Ratings) not retrieved (catalog-driven).

## Couplings: Rigid, Flexible, Universal, CV, Safety

### Takeaway
Couplings transmit torque while accommodating (or not) misalignment; rigid couplings demand precise alignment, flexible couplings tolerate small angular/parallel/axial misalignment with reaction forces, universal joints handle large angles with speed fluctuation, and safety couplings (shear pin/slip) protect downstream equipment.

### Cited Findings
- Coupling functions: transmit power, accommodate misalignment, compensate for end movement. — [PMC flexible coupling rotor study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13216537)
- Rigid couplings: no misalignment compensation; higher torque capacity for size; require precise alignment. Flexible couplings: limited misalignment freedom with transmitted force; produce lateral/axial reaction loads on bearings. — [SDP/SI couplings tech info](https://sdp-si.com/Catalogs/D757-Couplings-Universal-Joints.php); [Cambridge Design Cookbook](https://www-mdp.eng.cam.ac.uk/web/library/enginfo/cookbook/machine/couplings/couplings.html)
- Universal joint: combines rigid+flexible traits; transmits higher loads with greater misalignment than flexible; produces cyclic speed fluctuation (rotational velocity error) scaling with operating angle. — [SDP/SI](https://sdp-si.com/Catalogs/D757-Couplings-Universal-Joints.php); [Cambridge Design Cookbook](https://www-mdp.eng.cam.ac.uk/web/library/enginfo/cookbook/machine/couplings/couplings.html)
- DOE shaft alignment tolerances table: parallel offset and angular misalignment by motor speed (e.g., 1800 rpm: 2.0 mils parallel / 0.6 mils per inch angular for excellent). Flexible couplings still require alignment; do not rely on flexibility to absorb large misalignment. — [DOE motor shaft alignment](https://www.energy.gov/sites/prod/files/2014/04/f15/importance_motor_shaft_motor_systemts4.pdf)
- McMaster-Carr catalog: misalignment coupling types (beam, bellows, disc, grid, spider, Oldham, universal joint) rated by torque and speed; parallel/angular/axial misalignment accommodation. — [McMaster misalignment couplings](https://www.mcmaster.com/products/misalignment-couplings)
- Zero-Max/HexaFlex/Lenze torsionally flexible couplings compensate axial/radial/angular misalignment and damp shock/vibration; backlash-free options for precision. — [Zero-Max](https://www.zero-max.com/flexible-shaft-couplings); [Lenze HexaFlex](https://www.lenze-selection.com/en-pl/products/couplings-and-shaft-and-flange-couplings/flexible-couplings-and-jaw-and-bolt-couplings/hexaflex-shaft-coupling)
- Safety couplings: shear pin (replaceable), slip/overload (friction torque limiter) protect downstream equipment; McMaster lists "Overload Protection" and "Torque Limiter" components. — [McMaster](https://www.mcmaster.com/products/misalignment-couplings)

### Inferences
- Default to a flexible jaw/spider or beam coupling for small workshop machine shafts; use rigid only for precision-aligned spindles; use universal joints for intersecting shafts at angles.
- Keep misalignment within coupling rating and still align to DOE tolerances to protect bearings.
- Add a shear-pin or slip coupling on the input side to protect gears/bearings from crash loads.

### Gaps
- Coupling stiffness (torsional/lateral) values and reaction-force equations not retrieved; needed for critical-speed analysis.
- CV joint design equations not sourced (automotive-focused).

## Clutches and Brakes: Friction Disk, Centrifugal, Dog, Electromagnetic, Band, Disk

### Takeaway
Clutches/brakes are sized by torque capacity (friction: T = μ F r, with uniform pressure vs uniform wear models) and by heat dissipation (energy per cycle vs cooling capacity); selection balances actuation method, cycle rate, and thermal capacity.

### Cited Findings
- Clutches/brakes function: transfer torque (clutch) or stop/hold load (brake); categories by engagement technique (friction, electromagnetic, mechanical lockup) and actuation (mechanical, electric, pneumatic, hydraulic, self-activating). — [Clutches and brakes PDF (UVA)](https://www.ele.uva.es/~jesman/BigSeti/ftp/Actuadores/Motores_etc/ClthBrk.pdf)
- Disk/axial clutches: friction members moved parallel to shaft; advantages vs rim: no centrifugal effects, large friction area in small space, better heat dissipation, more uniform pressure. Single-plate (2 surfaces) or multi-disk. Analysis by uniform wear or uniform pressure. — [Shigley CH16 clutches/brakes PDF (HU)](https://eis.hu.edu.jo/ACUploads/10526/CH%2016.pdf)
- Rim types: internal/external shoes; band types; disk/axial; cone. Self-energizing shoes; centrifugal (automatic, speed-controlled); magnetic; hydraulic/pneumatic. — [Shigley CH16](https://eis.hu.edu.jo/ACUploads/10526/CH%2016.pdf)
- Friction materials limit capacity by μ and max allowable pressure p_max, plus heat-dissipation surface. — [Shigley CH16](https://eis.hu.edu.jo/ACUploads/10526/CH%2016.pdf)
- Centrifugal clutch: internally expanding shoes held by spring; torque capacity rises with speed; formulas on Engineers Edge. — [Engineers Edge centrifugal clutch](https://www.engineersedge.com/mechanics_machines/centrifugal_clutch_13706.htm)
- Electromagnetic (powder) clutches/brakes: torque via magnetic powder chain; no static/dynamic friction difference; continuous slip capable; heat dissipation P = ...; allowable continuous heat dissipation vs speed curves; torque limiting. — [Mitsubishi electromagnetic clutches technical doc](https://dl.mitsubishielectric.co.jp/dl/fa/document/catalog/clutch/sh-170030eng/sh170030eng-a.pdf)
- Warner Electric: torque ratings to 1350 lb·ft, up to 100 HP; LK friction material ~60% torque of standard but longer life; heat dissipation rate (ft·lb/min) compared to energy input; motor overload factor K (e.g., 2.75) for clutch selection. — [Warner Electric catalog](https://www.warnerelectric.com/-/media/Project/Altramotion/shared/files/Literature/brand/warner-electric/catalogs/mcc-p-1264-we-en-us-web.pdf?rev=2c7c9b8f6ca44ee49d682af1d7a3adc2)
- Dog clutches: mechanical lockup, direct connection, no slip; for engagement at matched speeds. — [Clutch PDF (igulms)](https://igulms.iqdigit.com/storage/15928/Clutch.pdf)
- Multi-plate clutch: torque divided among plates, smaller size, better heat dissipation; used heavy vehicles/racing. — [Clutch PDF (igulms)](https://igulms.iqdigit.com/storage/15928/Clutch.pdf)
- Brake heat: braking power P = μ p v; temperature rise limits; ventilated discs; fade above ~600 K; heat dissipation by convection/radiation; 100 s cooldown after braking. — [IIETA brake disc thermal study](https://www.iieta.org/download/file/fid/183667); [COMSOL brake disc model](https://cds.comsol.com/model/download/185501/models.heat.brake_disc.pdf)
- Disc brake torque/thermal: heat generated at contact; cooling capacity depends on vane geometry and airflow. — [Bombek et al. brake cooling](https://stumejournals.com/journals/tm/2017/4/140.full.pdf)

### Inferences
- For small workshop machines: friction disk clutches for moderate torque with actuation; electromagnetic for automated/remote actuation; centrifugal for engine-driven equipment; dog clutches for indexing at zero relative speed.
- Always check thermal capacity for cyclic duty: energy per engagement × cycle rate ≤ heat dissipation capacity; else add cooling or larger unit.
- Use motor overload factor K≈2.75 when selecting clutches to motor-driven loads (Warner).

### Gaps
- Explicit friction disk torque equations (uniform pressure: T = μ F (r_o+r_i)/2 × (2/3)(r_o^3-r_i^3)/(r_o^2-r_i^2); uniform wear: T = 0.5 μ F (r_o+r_i)) not in fetched sources but standard Shigley; verify.
- Band brake and cone clutch sizing equations not retrieved.
- Friction coefficient values by material pair and max pressure not tabulated in sources.

## System Integration: Shaft Diameter → Bearing → Gear → Housing → Bolt Circle

### Takeaway
Shaft diameter is the master variable: it sets bearing bore (ISO series), gear bore/keyway, coupling bore, and housing bolt circle; interface consistency requires tolerances, keyways, shoulders, and retaining rings to be designed together rather than independently.

### Cited Findings
- Shaft layout: axial layout of components, supporting axial loads through one bearing to frame, torque transmission via keys/splines/press fits, assembly/disassembly. — [Shigley Ch.7 slides](https://www.philadelphia.edu.jo/academics/mgogazeh/uploads/DESIGN%201%20CH7.pdf); [SUT Shigley slides](http://eng.sut.ac.th/me/2014/document/MachineDesign1/document/Ch_7.pdf)
- Axial loads supported through a bearing to the frame; generally best for only one bearing to carry axial load (shoulder) to allow tolerances and prevent binding. — [Shigley slides, Philadelphia University](https://www.philadelphia.edu.jo/academics/mgogazeh/uploads/DESIGN%201%20CH7.pdf)
- Bearing arrangement: rigid bearings accommodate misalignment within internal clearance; fits, clearance class, mounting method are key interface factors. — [SKF bearing selection process](https://www.skf.com/il/products/rolling-bearings/principles-of-rolling-bearing-selection/bearing-selection-process)
- Gears impose radial/axial loads and thrust (helical/bevel/worm); bearing arrangement must react thrust; gear bore must match shaft diameter and keyway. — [Shigley slides](https://www.philadelphia.edu.jo/academics/mgogazeh/uploads/DESIGN%201%20CH7.pdf)
- Coupling bore must match shaft diameter; misalignment accommodation affects bearing loads. — [McMaster misalignment couplings](https://www.mcmaster.com/products/misalignment-couplings); [DOE alignment](https://www.energy.gov/sites/prod/files/2014/04/f15/importance_motor_shaft_motor_systemts4.pdf)
- Housing bolt circle and bearing outer diameter determine housing bore; bearing OD from selected series. — [SKF selection process](https://www.skf.com/il/products/rolling-bearings/principles-of-rolling-bearing-selection/bearing-selection-process)
- Keyways, shoulders, and retaining rings create stress concentrations and must be checked in shaft fatigue; keyseat K_t values above. — [Shigley slides, Philadelphia University](https://www.philadelphia.edu.jo/academics/mgogazeh/uploads/DESIGN%201%20CH7.pdf)

### Inferences
- Design flow for small workshop: (1) compute torque/power/speed; (2) select gear ratio/type; (3) size shaft by fatigue at worst stress concentration; (4) pick bearing series matching shaft diameter and load/life; (5) verify housing bore/bolt circle fits bearing OD; (6) select coupling bore; (7) check deflection/critical speed; (8) finalize keys/shoulders/retaining rings with stress-concentration factors.
- Keep one bearing axially locating (shoulder + snap ring) and the other floating to avoid overconstraint from thermal expansion.
- Standardize on common shaft diameters (e.g., 10/12/16/20/25/30 mm or 1/2/5/8/3/4/1 in) to maximize bearing/gear/coupling availability.

### Gaps
- No single source provides an integrated design procedure combining all elements; Mott (Machine Elements in Mechanical Design) is cited in objective as the integrated reference but was not retrieved.
- Tolerance stack-up and housing machining allowances not sourced.
- Bolt-circle sizing formulas (e.g., from bearing OD and fastener size) not retrieved.