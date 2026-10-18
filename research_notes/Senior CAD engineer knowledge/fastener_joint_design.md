# Fastener and Joint Design (Mechanical Engineering Reference)

Scope: actionable sizing and selection for bolted, riveted, pinned, keyed, welded, adhesive, and press-fit/shrink-fit joints. Sources: Shigley *Mechanical Engineering Design* (Budynas & Nisbett), Juvinall & Marshek *Fundamentals of Machine Component Design*, Bickford *Introduction to the Design and Behavior of Bolted Joints*, NASA fastener standards (NASA-STD-5020A, MSFC-STD-486B, NASA Fastener Design Manual), AWS D1.1, VDI 2230, ISO 898/286, ASME B18.8, and industry references. Equations/allowables are representative; verify against the governing standard and material data for the application.

---

## Bolted Joints

### Takeaway
A properly preloaded bolted tension joint carries most external load through release of member compression, not bolt tension; size the bolt tensile stress area, preload (typically 65–90% of proof/yield), torque via T = K F d (K ≈ 0.15–0.25), and check separation, proof, fatigue (Goodman with mean stress), and eccentric bolt-group capacity.

### Cited Findings
- Tensile stress area A_t is the effective area of a threaded rod for stress calculations; it is the area of an unthreaded rod with the same tensile strength, based on the average of pitch and root diameters — [Shigley ch. 8 slides (ITU)](https://web.itu.edu.tr/~halit/Makel/Ch_8_slides_m.pdf).
- Proof load is the maximum load a bolt can withstand without permanent set; proof strength S_p = F_p/A_t corresponds to the proportional limit, slightly below yield, and is typically used for static strength of the bolt — [Shigley ch. 8 slides](https://web.itu.edu.tr/~halit/Makel/Ch_8_slides_m.pdf).
- Bolt stiffness for an axially loaded rod: k_b = E_b A_b / l, where l is grip length (everything compressed, including washers) — [Shigley ch. 8 slides](https://web.itu.edu.tr/~halit/Makel/Ch_8_slides_m.pdf).
- Member stiffness k_m uses Shigley's frustum (conical stress field) or Bickford's cylindrical (Q-factor) stress-field model; Q = d_c/d for the idealized cylindrical field — [OSTI Guideline for Bolted Joint Design and Analysis (2008)](https://www.osti.gov/servlets/purl/929124).
- Torque–tension: T = K F_i d (nut factor K); Shigley's derived K assumes washer-face diameter 1.5 d, collar diameter d_c = 1.25 d, and includes thread friction and collar friction terms — [Shigley ch. 8 slides](https://web.itu.edu.tr/~halit/Makel/Ch_8_slides_m.pdf).
- Typical K ≈ 0.20 for as-received (dry) steel; lubrication lowers scatter significantly (σ ≈ 2.9 kN vs 4.9 kN for unlubricated) but changes mean preload little — [Shigley ch. 8 slides](https://web.itu.edu.tr/~halit/Makel/Ch_8_slides_m.pdf).
- Preload is usually set at 65–90% of yield strength; a properly preloaded bolt carries only a small fraction (often <20%) of external load because member stiffness k_m >> bolt stiffness k_b — [NASA "Preloaded Joint Analysis Methodology for Space Flight Systems"](https://ntrs.nasa.gov/api/citations/19960012183/downloads/19960012183.pdf).
- Stiffness (load) factor C = k_b/(k_b + k_m). Bolt load under external P: F_b = F_i + C P. Member load: F_m = F_i − (1−C)P. Joint separates when F_m = 0, i.e. P_sep = F_i/(1−C) — [Shigley ch. 8 (Philadelphia univ. notes)](https://www.philadelphia.edu.jo/academics/mgogazeh/uploads/DESIGN%202%20CH%208.pdf).
- Static strength checks: bolt yielding n = F_p/F_b,max; separation n_sep = F_i/[(1−C)P] (or P_sep/P_max); recommended preload often F_i = 0.75 F_p (as stated in the task; Shigley examples use F_i = 0.9 F_p) — [Shigley ch. 8 notes](https://www.philadelphia.edu.jo/academics/mgogazeh/uploads/DESIGN%202%20CH%208.pdf); [TTU three-textbook fatigue comparison](https://www.myweb.ttu.edu/amosedal/documents/BTJfatigue.pdf).
- Fatigue of tension joint: alternating bolt stress σ_a = K_f · C·ΔP/(2 A_t) (Shigley treats K_f as a strength-reduction factor on endurance limit); mean stress σ_m = [F_i + (1+C)P_max/2]/A_t (approx.); Goodman criterion (σ_a/S_e)+(σ_m/S_ut)=1/n. Juvinall and Spotts handle K_f differently, giving S_e values differing by ~3× — [TTU comparison of Shigley/Juvinall/Spotts](https://www.myweb.ttu.edu/amosedal/documents/BTJfatigue.pdf).
- Fatigue failures occur near the end of the threaded portion (stress concentration at thread root); machining the shank down to the thread root diameter (reduced shank) improves fatigue life — [NASA Fastener Design Manual](https://ntrs.nasa.gov/api/citations/19900009424/downloads/19900009424.pdf).
- Eccentric bolt groups: primary shear V/n per bolt plus secondary shear from moment M·r_i/Σr_i²; resultant per bolt compared to allowable; elastic method (polar moment of inertia) is conservative; AISC Instantaneous Center of Rotation method gives higher capacity — [AISC bolt-group paper (Brandt)](https://ej.aisc.org/index.php/engj/article/download/378/377); [AISC eccentric/inclined loads (Iwankiw)](https://ej.aisc.org/index.php/engj/article/download/493/492).
- Combined tension + shear interaction (AISC): V ≤ V_c(1 − T/T_c) (bearing type) or sqrt((T/T_c)²+(V/V_c)²) ≤ 1 variants; eccentricity of bracket connections — [AISC combined shear/tension (Zweig)](https://ej.aisc.org/index.php/engj/article/download/51/50/50).
- NASA-STD-5020A covers preload variation Γ, torque–tension uncertainty, multi-fastener preloading sequences, separation factor of safety F_Ssep, and interaction formulas for combined shear+tension+bending — [NASA-STD-5020A w/Change 1](https://www.nasa.gov/wp-content/uploads/2018/01/nasa-std-5020a_w-chg_1_nasa_fastener_standards.pdf).

### Inferences
- Because k_m >> k_b for typical metal joints, high preload is the single most effective defense against fatigue and separation; the bolt sees only ~C·ΔP alternating stress.
- Lubricated joints are preferred where preload scatter matters (fatigue-critical, gasketed) even though mean K changes little.
- For non-tabulated bolt patterns, use the elastic method (conservative) or implement the IC method numerically.

### Gaps
- Exact Shigley fatigue equations (σ_a, σ_m, Goodman) not fully extracted from the PDFs here; verify against Shigley 10th ed. ch. 8.11 and the TTU comparison document.
- Nut-factor tables and proof-load values by grade (ISO 898-1 classes 8.8/10.9/12.9, SAE grades) not captured; use manufacturer/standard tables.
- Multi-bolt preload sequence and gasketed-joint (ASME VIII) rules not covered in depth.

---

## Thread Engagement

### Takeaway
Design so the bolt fractures in tension before threads strip: minimum effective engagement ≈1.0 d for steel-on-steel, 1.5–2.0 d for aluminum, 2.0 d for cast iron/zinc, 2.0–2.5 d for plastics; total engagement m_ges = m_eff + 2P.

### Cited Findings
- Thread stripping is sudden and occurs at loads below the bolt's tensile capacity when engagement is too short; the design goal is bolt shank fracture as the controlled, predictable failure mode — [Nord-Lock "Thread engagement in a tapped hole"](https://www.nord-lock.com/learnings/bolting-tips/2015/the-experts-thread-engagement-in-a-tapped-hole); [Component Solutions Group](https://www.componentsolutionsgroup.com/blog/thread-engagement-explained/).
- VDI 2230 minimum effective engagement for the nut-thread-critical case (R_S < 1): m_eff_min = (R_m·A_s·P)/[C_1·C_3·τ_BM·(P/2 + (d_min − D_2max)·tan 30°)·π·d_min]; C_1 = 1.0 for standard through-hole joints with s/d ≥ 1.9 — [ssbolts VDI 2230 engagement article](https://ssbolts.com/fastener-information-center/strength-grades-standards/bolt-nut-grade-compatibility-proof-load-thread-stripping).
- Total engagement length including entry supplement: m_ges = m_eff + 2P — [ssbolts](https://ssbolts.com/fastener-information-center/strength-grades-standards/bolt-nut-grade-compatibility-proof-load-thread-stripping).
- Practical minimum m_eff by parent material: steel (standard nut) 1.0 d; steel (high-strength nut) 0.8 d; cast iron 1.25 d; aluminum alloys 1.5–2.0 d; zinc die casting 2.0 d; plastics 2.0–2.5 d — [ssbolts](https://ssbolts.com/fastener-information-center/strength-grades-standards/bolt-nut-grade-compatibility-proof-load-thread-stripping).
- Rule-of-thumb chart (hardened steel 1.0×d, low-carbon steel 1.2×d, ductile iron 1.25×d, magnesium 2.2×d, reinforced plastics 2.5×d, soft plastics 3.0×d) — [Component Solutions Group engagement chart](https://www.componentsolutionsgroup.com/blog/minimum-thread-engagement-explained).
- Standard steel-on-steel: ~1.0 d; aluminum: ~2.0 d — [Nord-Lock](https://www.nord-lock.com/learnings/bolting-tips/2015/the-experts-thread-engagement-in-a-tapped-hole).
- Shear-out capacity ≥ bolt tensile capacity: L_eng = (A_t·F_t)/(π·d_n·0.577·F_y,host); worked example 3/8"-16 Grade 5 in A36 gives ≈1.01 d — [Industrial Monitor Direct](https://industrialmonitordirect.com/blogs/knowledgebase/bolt-thread-engagement-calculation-for-tensile-strength).
- Stainless-steel host reduces shear yield, increasing required engagement (304/316 annealed ≈1.20 d) — [Industrial Monitor Direct](https://industrialmonitordirect.com/blogs/knowledgebase/bolt-thread-engagement-calculation-for-tensile-strength).
- With identical materials, the nut's shear area is ~15–20% larger than the bolt's for the same engagement length, so the bolt threads strip first only if engagement is short — [ssbolts](https://ssbolts.com/fastener-information-center/strength-grades-standards/bolt-nut-grade-compatibility-proof-load-thread-stripping).
- AISC 360 J3.3 requires minimum thread engagement of 1.0 bolt diameter for structural connections — [Industrial Monitor Direct](https://industrialmonitordirect.com/blogs/knowledgebase/bolt-thread-engagement-calculation-for-tensile-strength).

### Inferences
- First 1–2 threads at bolt tip and hole mouth are incomplete and should not count toward engagement.
- For blind holes, cap engagement so the bolt does not bottom out; add thread-relief/undercut at shank-to-thread transition.
- Softer/weaker host material dominates; size engagement to host shear strength, not bolt grade.

### Gaps
- Full Alexander (1977) analytical engagement formula not captured; use for critical joints.
- Metric VDI 2230 graphical guidance (Fig. 36, M4–M39, grades 8.8/10.9/12.9) not reproduced here.

---

## Locking (Anti-Loosening)

### Takeaway
Preload is the primary anti-loosening measure; supplement with positive mechanical locks (cotter pins, safety wire) for critical joints, chemical threadlockers for vibration, prevailing-torque nuts for convenience; match method to temperature, reusability, and serviceability.

### Cited Findings
- Self-loosening is driven by transverse joint slip under vibration; ensuring sufficient clamp force and using proven locking devices is key — [BoltScience self-loosening](https://www.boltscience.com/pages/vibloose.htm).
- Nyloc (nylon-insert) nuts: nylon collar forms frictional grip; reusable a few cycles; temperature limit ~80 °C (FSAE rule) — [DesignJudges threaded fasteners](https://www.designjudges.com/articles/threaded-fasteners); [Nylok](https://nylok.com/pre-applied-processes/mechanical-locking/).
- Prevailing-torque (distorted-thread or nylon-patch) nuts create built-in frictional drag; limited reusability (1–5 cycles) and higher installation torque; add drag torque to specified installation torque (MSFC-STD-486B note 5) — [Component Solutions Group thread-locking guide](https://www.componentsolutionsgroup.com/blog/thread-locking-methods); [DesignJudges](https://www.designjudges.com/articles/threaded-fasteners).
- Chemical threadlockers (anaerobic, e.g., Loctite) cure in absence of air with metal ions; strong against vibration and seal against moisture/corrosion; strengths from low (purple) to permanent (red) — [AFT Fasteners threadlockers](https://www.aftfasteners.com/threadlockers-nylon-patches); [Component Solutions Group](https://www.componentsolutionsgroup.com/blog/thread-locking-methods).
- Positive mechanical locks: castle nut + cotter pin, safety wire (drilled head/shank), lock plates — physically prevent rotation; exceptional security and visual confirmation; require drilled fasteners and more labor — [Component Solutions Group](https://www.componentsolutionsgroup.com/blog/thread-locking-methods); [DesignJudges](https://www.designjudges.com/articles/threaded-fasteners).
- FSAE T.8.3.2 acceptable positive locks: safety wire, cotter pins, nylon lock nuts (≤80 °C), prevailing-torque lock nuts; lock washers, nylon patches, and threadlockers do NOT meet positive-locking requirement — [DesignJudges](https://www.designjudges.com/articles/threaded-fasteners).
- Safety-wire/cotter-pin installation per FAA AC 43.13-1B ch. 7 §7 — [DesignJudges](https://www.designjudges.com/articles/threaded-fasteners).
- Nylok nylon patch: min −70 °F / max 250 °F (≈121 °C) — [AFT Fasteners](https://www.aftfasteners.com/threadlockers-nylon-patches).
- NIST RP386: cotter pins and slotted/castellated nuts tested; most locking devices showed little change in static torque–tension relation vs. standard nuts — [NIST RP386](https://nvlpubs.nist.gov/nistpubs/jres/7/jresv7n5p945_a2b.pdf).
- Split lock washers are generally not recommended; Nord-Lock/Schnorr wedge washers and flanged/serrated nuts are alternatives — [EngiCalcsHub bolt torque guide](https://engicalchub.com/guides/bolt-torque-guide); [BoltScience](https://www.boltscience.com/pages/vibloose.htm).

### Inferences
- For severe vibration + high temperature, prefer all-metal prevailing-torque nuts or positive locks (cotter/safety wire) over nylon.
- Threadlockers add prevailing torque; include in installation torque budget.

### Gaps
- Breakaway/prevailing-torque strength values by threadlocker grade (e.g., Loctite 243/271) not fully captured; use vendor data (AFT Fasteners lists some ranges).

---

## Riveted Joints

### Takeaway
Rivets are permanent, shear-carrying fasteners; treat riveted and bolted shear joints identically (Shigley); design against rivet shear, bearing (crushing), and plate tension tearing; typical efficiencies 50–88% by joint type; self-piercing and solid rivets remain common in sheet-metal/aircraft.

### Cited Findings
- Two main types: lap joints (overlap) and butt joints (plates butted, joined via cover/strap plates) — [ScienceDirect riveted joint overview](https://www.sciencedirect.com/topics/materials-science/riveted-joint).
- Rivets fail by single shear, double shear, or crushing; plates fail by shear, tension tearing, or crushing; design assumes equal load sharing, uniform shear stress, no combined stresses — [ScienceDirect riveted joint overview](https://www.sciencedirect.com/topics/materials-science/riveted-joint).
- Design (allowable) stresses often taken as 20% of ultimate: tensile 75 MPa, shear 60 MPa, bearing 131 MPa (from Oberg/Machinery's Handbook values cited) — [ScienceDirect riveted joint overview](https://www.sciencedirect.com/topics/materials-science/riveted-joint).
- Safe tensile load based on shear: L = n·(π d²/4)·τ_allow (single shear) etc.; bearing: L = n·d·t·σ_bearing; tension: L = (w − n d)·t·σ_t — [ScienceDirect riveted joint overview](https://www.sciencedirect.com/topics/materials-science/riveted-joint).
- Efficiency = (strength of riveted joint)/(strength of solid plate)×100; typical efficiencies: lap single 50–60%, double 60–72%, triple 72–80%; butt (double strap) single 55–60%, double 76–84%, triple 80–88% — [IDC Online riveted joints](https://www.idc-online.com/technical_references/pdfs/mechanical_engineering/Riveted_Joints.pdf).
- Shigley: riveted and bolted shear joints treated identically; failure modes include rivet bending, pure shear, plate tension, bearing, edge shear; bearing stress often limits load (example: bolt shear allows 62.5 kip, members bearing limits to 54 kip) — [Shigley joint design (IITM)](https://ae.iitm.ac.in/~nidish/courses/as3020/files/mod1/jointdesign.pdf).
- Rivet/bolt spacing: minimum 3 d (some sources 2.5 d) between centers; edge distance ≥1.5 d; pitch and margin rules per design handbooks — [Riveted joint design PDF (rskr.irimee)](https://rskr.irimee.in/sites/default/files/DESIGN%20&%20DRAWING%20OF%20RIVETED%20JOINT.pdf).
- Hot vs cold riveting; leak-proof joints require caulking; rivet materials include carbon steel, aluminum alloys, copper, stainless — [IDC Online](https://www.idc-online.com/technical_references/pdfs/mechanical_engineering/Riveted_Joints.pdf).
- Self-piercing rivets (SPR) for aluminum sheet; fatigue life depends on rivet orientation — [UMich SPR fatigue study](https://backend.production.deepblue-documents.lib.umich.edu/server/api/core/bitstreams/97dd0b12-d9bc-48c6-8dce-c0b3cb7d1482/content).
- Standards: BS 4620, ANSI B18.1.2, AISC Guide to Design Criteria for Bolted and Riveted Joints — [ScienceDirect](https://www.sciencedirect.com/topics/materials-science/riveted-joint).

### Inferences
- Prefer rivets for permanent sheet-metal/aircraft joints where welding distortion or heat is unacceptable; bolts where serviceability matters.
- Double-strap butt joints give highest efficiency; use for pressure vessels/boilers (historical).

### Gaps
- Modern structural rivet (blind/pop rivet) design data and fatigue categories not covered.
- Creep/relaxation of riveted joints not addressed.

---

## Pins (Dowel, Clevis, Cotter, Taper, Spring/Roll)

### Takeaway
Pins carry shear (and sometimes location/alignment); size as double/single shear with bearing; choose type by function—dowel for precise location, clevis for pivoting/removable joints, taper for self-locking alignment, spring/roll for quick assembly in slightly oversized holes.

### Cited Findings
- Pin types: dowel (hardened, ground, precise location), clevis (with cotter/retainer, pivoting), cotter (split pin for retention), taper (1:48 or 1:50 taper, self-locking), spring/roll (slotted or spiral, elastic radial tension in hole) — [McMaster-Carr pin catalog](https://www.mcmaster.com/products/pins); [WM Berg pins](https://www.wmberg.com/products/fasteners-and-hardware/pins).
- Standards: ASME B18.8.1 (clevis & cotter), ASME B18.8.2 (taper, dowel, straight, grooved, spring) — [GlobalSpec ASME B18.8.2](https://standards.globalspec.com/std/14349533/asme-b18-8-2).
- Shear design: V = F/A (single shear) or F/(2A) (double shear); bearing stress σ_b = F/(d·t); check both shear and bearing; pin material usually harder than members — standard machine-design practice (Shigley/Mott).
- Spring pin (roll) shear capacities by diameter and type (slotted/spiral, light/standard/heavy duty) per ISO 8748/8750/8752/13337; e.g., 6 mm standard-duty ≈ 11 kN, 8 mm ≈ 19.5 kN (Bossard table) — [Bossard shear loads for pins PDF](https://assets.eu.ctfassets.net/0vp0u5uh75zd/51I2xrq4GyROKWA6GGoRt9/7b2d2347b05c8ece20089c3e5fc7dd80/078_Shear_loads_pins_Fastening_EN_01_2025.pdf).
- Taper pins: standard taper 1:48 (US) / 1:50 (metric); used for locating and securing, self-locking by interference along taper — [ASME B18.8.2 / McMaster taper pins](https://www.mcmaster.com/products/taper-dowel-pins).
- Cotter pins: split pins inserted through drilled hole and bent; used with clevis/castle nuts; sizes 1/32"–3/4" per ASME B18.8.1 — [ASME B18.8.1 preview](https://webstore.ansi.org/preview-pages/ASME/preview_B18-8-1_2014_w_CPRT.pdf).
- Shear pins: designed to fail at a specified torque to protect machinery (overload protection) — [McMaster shear pins](https://www.mcmaster.com/products/pins/pin-type~shear).
- Dowel pins: hardened ground pins for precise alignment; may be used as pivots/shafts; soft dowel pins for assembly aids — [WM Berg](https://www.wmberg.com/products/fasteners-and-hardware/pins).

### Inferences
- Use dowels for location (not primary load) unless sized for shear; use clevis + cotter for removable pivots; use spring pins for quick, vibration-resistant assembly in soft/oversized holes.
- For shear-critical pins, check bearing in the weaker member and consider double-shear arrangements (2× capacity) with two load paths.

### Gaps
- General (non-spring) pin shear-strength allowables by material/grade not tabulated here; use material shear strength / safety factor.
- Taper-pin pull-out/assembly force and torque capacity not covered.

---

## Keys (Square, Flat, Woodruff, Gib-Head)

### Takeaway
Keys transmit torque between shaft and hub via shear and crushing (bearing); size key width/length so shear and crushing stresses are below allowables; square keys (w = t = d/4) are equally strong in shear and crushing when σ_ck = 2 τ; account for keyway stress concentration in shaft fatigue.

### Cited Findings
- Standard proportions (IS 2292/2293): square key w = d/4, t = d/4; flat (rectangular) key w = d/4, t = d/6; gib-head key w = d/4, t = 2w/3 = d/6, with gib head for removal — [RCET design of machine elements notes](https://www.rcet.org.in/uploads/academics/regulation2021/rohini_62936719978.pdf); [UOM keys & coupling notes](https://wwww.uomus.edu.iq/img/lectures21/MUCLecture_2021_112525292.pdf).
- Torque capacity: T = F·(D/2), where F = τ·w·L (shear) or σ_c·t·L (crushing); for square key τ and σ_c/2 give equal strength, so w = t — [RCET notes](https://www.rcet.org.in/uploads/academics/regulation2021/rohini_62936719978.pdf); [Engineers Edge key design](https://www.engineersedge.com/gears/design_of_square_key__13740.htm).
- Service factor K_s combines application (K_a), keyway (K_d), and fatigue (K_f) or wear (K_w) factors; shear stress τ = T·K_s/[w·L·(D/2)·N]; safety factor F_s = S_s/τ — [Engineers Edge](https://www.engineersedge.com/gears/design_of_square_key__13740.htm).
- Square keys preferred through ~4.5" shaft diameter; flat keys for larger shafts or thin-wall hubs — [ScienceDirect keyways overview](https://www.sciencedirect.com/topics/engineering/keyways).
- Woodruff key: semicircular segment, self-aligning, eliminates milling near shoulders (reduces stress concentration), used on tapered shafts; deeper keyway weakens shaft — [Wikipedia keyway](https://en.wikipedia.org/wiki/Keyway_(engineering)); [RCET notes](https://www.rcet.org.in/uploads/academics/regulation2021/rohini_62936719978.pdf).
- Gib-head key: tapered, with head for removal; used at shaft ends — [RCET notes](https://www.rcet.org.in/uploads/academics/regulation2021/rohini_62936719978.pdf).
- Keyway stress concentration: Neuber and Leven formulas for K_t as function of keyway depth h and corner radius r; for semi-circular groove K_t = 1 + 2√(h/r) (Neuber, per cited source); practical corner radius ≈ 0.1 h — [ScienceDirect keyways overview](https://www.sciencedirect.com/topics/engineering/keyways).
- Keyway weakens shaft torsional strength; Moore's experimental weakening factor cited in machine-design notes — [UOM notes](https://wwww.uomus.edu.iq/img/lectures21/MUCLecture_2021_112525292.pdf).
- FE/shape-optimization work shows up to ~50% reduction in keyway stress concentration with optimized (super-elliptical) keyway profiles — [Pedersen, J. Strain Analysis, 2010](https://journals.sagepub.com/doi/10.1177/030932471004500804).

### Inferences
- For fatigue-critical shafts, use Woodruff keys or optimized keyways, large corner radii, and avoid keyways near stress risers (shoulders).
- Key length should be at least ~1.5× shaft diameter for adequate bearing; check hub wall thickness for crushing.

### Gaps
- Full Neuber formula (Eq. 10.35 in cited source) not reproduced; verify in Peterson/Pilkey stress-concentration references.
- Exact keyway weakening factor formula not captured (source gives numerical example only).

---

## Welded Joints

### Takeaway
Welded joints are permanent and economical; size fillet welds by throat shear (τ = F/(0.707·w·L) for 45° fillet), butt (groove) welds by full section; follow AWS D1.1 allowable stresses and fatigue categories, control distortion/HAZ with preheat and proper WPS per ASME IX.

### Cited Findings
- AWS D1.1: effective throat of a fillet weld is the shortest distance from joint root to weld face; stress on the effective throat is treated as shear regardless of load direction — [AWS D1.1:2000 (law.resource.org)](https://law.resource.org/pub/us/cfr/ibr/003/aws.d1.1.2000.pdf).
- AWS D1.1 allowable stresses table (Table 2.3/4.3) and fatigue provisions (Table 2.4/4.5) for nontubular connections; fatigue categories by weld type/location (plain material, groove welds, fillet welds, attachments) — [AWS D1.1:2000](https://law.resource.org/pub/us/cfr/ibr/003/aws.d1.1.2000.pdf); [AWS D1.1 2015 preview](https://webstore.ansi.org/preview-pages/AWS/preview_AWS+D1.1+D1.1M-2015.pdf).
- AWS D1.1 permits a 50% directional strength increase for fillet welds loaded perpendicular to the weld axis (transverse vs. longitudinal) — [AISC fillet/PJP welds final report](https://www.aisc.org/media/rp2pj0bm/fillet-and-pjp-welds-final-report-rev1.pdf).
- Weld group eccentricity: AISC instantaneous-center-of-rotation method with inelastic load-deformation; elastic polar-moment method is conservative — [AISC eccentrically loaded weld groups (Tide)](https://ej.aisc.org/index.php/engj/article/download/354/353); [AISC inclined/eccentric (Iwankiw)](https://ej.aisc.org/index.php/engj/article/download/493/492).
- Fillet weld size rules: minimum fillet weld size by thicker part thickness; maximum single-pass size; CJP/PJP groove weld requirements; backing/backgouging for CJP — [AWS D1.1 2020 index](https://pubs.aws.org/Download_PDFS/D1_1_D1_1M_2020_index_PV.pdf).
- ASME Section IX governs WPS/PQR and welder performance qualification; AWS D1.1 references qualified procedures and personnel — [AWS D1.1 2020 index](https://pubs.aws.org/Download_PDFS/D1_1_D1_1M_2020_index_PV.pdf).
- Distortion control: balance welds, use proper sequence, preheat, fixtures; HAZ properties depend on base metal and heat input; preheat per Annex B (AWS D1.1) — [AWS D1.1 2025 public review](https://pubs.aws.org/Download_PDFS/D1.1-E25-DS5-BTPublicReviewPV.pdf).
- Fatigue life enhancement: improve weld profile (grind toes), use larger welds, avoid attachments in high-stress regions; AWS D1.1 §9 (tubular) and §4 (nontubular) fatigue provisions — [AWS D1.1 2020 index](https://pubs.aws.org/Download_PDFS/D1_1_D1_1M_2020_index_PV.pdf).
- Butt (groove) welds in tension between members of different thickness/width require tapered transition (slope ≤1:2.5) when tensile stress > 1/3 allowable — [AWS D1.1:2000](https://law.resource.org/pub/us/cfr/ibr/003/aws.d1.1.2000.pdf).
- Load-carrying fillet-welded joints: fatigue capacity depends on stress range and weld throat; normal stress on throat can control for high obtuse dihedral angles — [AISC fillet/PJP report](https://www.aisc.org/media/rp2pj0bm/fillet-and-pjp-welds-final-report-rev1.pdf).

### Inferences
- For fatigue-critical steel structures, prefer CJP groove welds or ground fillet toes; use AWS D1.1 fatigue category tables with stress ranges.
- For non-structural/machine parts, fillet welds sized by throat shear with a safety factor are typical; verify against base-metal strength too.

### Gaps
- Specific allowable stress values (e.g., 0.30 F_EXX for fillet shear) not extracted from AWS tables here; use the code tables directly.
- ASME Section IX WPS/PQR details not covered; consult the standard.
- Aluminum/other alloy welding (AWS D1.2/D1.3) not covered.

---

## Adhesive Bonds

### Takeaway
Adhesives excel in shear/compression; design joints to avoid peel and cleavage (single lap bends and peaks stress at ends); prefer scarf/stepped/double-lap for uniform stress; surface preparation is usually the controlling factor; typical bondline thickness 0.005–0.015 in.

### Cited Findings
- Joint-design ranking (Ellsworth): scarf excellent; tapered/stepped/double lap very good; simple lap good; butt poor in thin sheet; strap fair; double strap very good — [Ellsworth Adhesives technical bulletin](https://prod.ellsworth.com/globalassets/literature-library/manufacturer/ellsworth-adhesives/ellsworth-adhesives-technical-bulletin-what-adhesive-works-best-for-your-application.pdf).
- Basic design rules: avoid peel and cleavage; prefer compression and shear; maximize bond area within constraints — [Sika structural bonding guideline](https://industry.sika.com/dms/getdocument.get/172620f2-f511-40f0-87e2-b9822d9e4d75_global-industry/general-guidelinestructuralbonding.pdf).
- Single lap joint bends under load, creating peel/cleavage stress peaks at the ends of the overlap; tapered lap or adhesive bridges reduce peaks; scarf or stepped lap give more uniform stress distribution — [Sika guideline](https://industry.sika.com/dms/getdocument.get/172620f2-f511-40f0-87e2-b9822d9e4d75_global-industry/general-guidelinestructuralbonding.pdf).
- Scarf joint: angle θ between adhesive layer axis and adherend axis (0° = butt, 90° = lap); scarf angle controls ratio of peel to shear stress; peel stress normal to scarf surface σ = F sin²θ/A, shear τ = F sinθ cosθ/A (per Clarke 1996 cited) — [ScienceDirect scarf angle overview](https://www.sciencedirect.com/topics/engineering/scarf-angle).
- NASA scarf/stepped-lap analysis: bond load transfer concentrates at the end from which the softer adherend extends; restrict length of end step of stiffer adherend; peel stresses limit thick double/single lap more than shear — [NASA scarf/stepped-lap report](https://ntrs.nasa.gov/api/citations/19740005084/downloads/19740005084.pdf).
- Surface preparation standards: ASTM D2651 (metal surfaces), ASTM D3933 (aluminum phosphoric acid anodizing), ASTM D1002 (lap shear) — [NASA PRC-1001](https://www.nasa.gov/wp-content/uploads/2023/03/prc-1001-current.pdf).
- NASA PRC-1001 bondline thickness: paste adhesive 0.000–0.015 in depending on layers; film adhesive overlaps not permitted; primer as specified — [NASA PRC-1001](https://www.nasa.gov/wp-content/uploads/2023/03/prc-1001-current.pdf).
- Surface prep for aluminum: sanding + phosphoric acid anodizing; untreated aluminum gives lowest bond strength (useful as baseline/troubleshooting) — [ARL lap-shear prep guide](https://www.govinfo.gov/content/pkg/GOVPUB-D101-PURL-gpo128473/pdf/GOVPUB-D101-PURL-gpo128473.pdf); [Metal-metal bonding study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10610595/).
- Adhesive types: epoxies (high strength, rigid), acrylics, polyurethanes (tough/flexible), cyanoacrylates (fast), anaerobics (threadlocking), phenolics; choose by substrate, temperature, environment — general (Ellsworth/industry).
- Peel tests (T-peel, floating roller) used to verify peel resistance; well-designed joints minimize peel — [Sika guideline](https://industry.sika.com/dms/getdocument.get/172620f2-f511-40f0-87e2-b9822d9e4d75_global-industry/general-guidelinestructuralbonding.pdf).

### Inferences
- Adhesive strength data (lap shear) is from standardized specimens; real joint strength depends heavily on peel; design to shear, verify peel.
- For composite/metal hybrid structures, scarf/stepped joints are preferred; butt with doublers is common.

### Gaps
- Quantitative design allowables by adhesive family (shear/peel strengths, modulus) not captured; use vendor/TDS and ASTM D1002 data.
- Durability (moisture/temperature degradation) models not covered.

---

## Press-Fit / Shrink-Fit

### Takeaway
Press fits generate contact pressure via elastic interference; size interference for required torque/axial capacity, then check hub hoop stress (keep below ~0.5·σ_y); use shrink-fit for large interference; apply roughness smoothing correction and tolerance worst cases.

### Cited Findings
- Lamé contact pressure: p = δ/[d·(C_hub + C_shaft)], where C = (1/E)[(D²+d²)/(D²−d²) + ν] for hub and (1/E)(1−ν) for solid shaft — [True Precision Machining press-fit calculator](https://www.trueprecisionmachining.com/engineering/calculators/press-fit/); [MechanixCalc DIN 7190](https://www.mechanixcalc.com/pressfit).
- Hub hoop stress at bore: σ_t = p·(D²+d²)/(D²−d²) — highest stress in the joint; keep below 0.5·σ_y (conservative) or check von Mises with SF ≥ 2.0 (DIN 7190) — [True Precision](https://www.trueprecisionmachining.com/engineering/calculators/press-fit/); [MechanixCalc](https://www.mechanixcalc.com/pressfit).
- Torque capacity: T = f·p·π·d²·L/2; axial holding force: F = f·p·π·d·L — [ScienceDirect interference fit overview](https://www.sciencedirect.com/topics/engineering/interference-fit); [Dalloway press-fit calculator](https://dalloways.com/press-fit-calculator).
- Shrink-fit assembly temperature: ΔT = (δ + c)/(α·d) (heat hub or cool shaft) — [VMT press-fit guide](https://vmtcnc.com/press-fit); [Dalloway](https://dalloways.com/press-fit-calculator).
- Practical interference limit for steel hubs ≈ 0.001·D (1‰ of diameter); beyond this hoop stress approaches yield — [VMT press-fit guide](https://vmtcnc.com/press-fit).
- ISO 286 fits: H7/p6 (light press), H7/s6 (medium drive), H7/u6 (force fit); ANSI B4.1 FN1–FN4 equivalents — [VMT](https://vmtcnc.com/press-fit).
- DIN 7190 roughness smoothing correction: effective interference δ_eff = δ_min − 0.8·(Rz_shaft + Rz_hub) — [MechanixCalc](https://www.mechanixcalc.com/pressfit).
- Friction coefficient μ: dry steel-on-steel ≈0.10–0.25; lubricated ≈0.05–0.08; μ is a direct multiplier on capacity — [VMT](https://vmtcnc.com/press-fit); [Dalloway](https://dalloways.com/press-fit-calculator).
- Tolerance worst case: max material condition sets hub stress/press force; least material condition sets minimum holding capacity — [True Precision](https://www.trueprecisionmachining.com/engineering/calculators/press-fit/).
- Friction scatter ±30%; safety-critical joints add keys/splines rather than relying on fit alone — [Dalloway](https://dalloways.com/press-fit-calculator).

### Inferences
- Thin-walled hubs convert less interference to pressure; check wall ratio (D/d) before assuming capacity.
- For dissimilar materials, check residual interference at operating temperature (thermal loosening).
- Shrink-fit avoids scored bores on long engagements; use for railway wheels, large gears.

### Gaps
- Full DIN 7190-1 procedure (including fretting fatigue, axial strain) not captured; use the standard/calculator.
- Composite (anisotropic) hub interference fits not covered.

---

## Selection: When to Use Which Joint

### Takeaway
Choose by permanence, load type, environment, serviceability, and cost: bolts for serviceable/inspection-critical joints; rivets for permanent sheet/aircraft; welds for permanent high-strength/low-cost; adhesives for dissimilar materials/damping; press-fits for torque transmission; pins/keys for location and torque transfer.

### Cited Findings
- Mechanical joints divide into non-permanent (can be disassembled without damage: bolts, screws, pins, keys) and permanent (rivets, welds, adhesives, press-fits) — [IDC Online riveted joints](https://www.idc-online.com/technical_references/pdfs/mechanical_engineering/Riveted_Joints.pdf).
- Joint design is as important as component design; a weak joint spoils a carefully designed part — [IDC Online](https://www.idc-online.com/technical_references/pdfs/mechanical_engineering/Riveted_Joints.pdf).
- Bolts: best for serviceability, inspection, preload-controlled clamping, vibration (with locking), and combined loads; cost moderate (fastener + labor).
- Rivets: permanent, good in shear, low cost in production, used in aircraft/sheet metal; poor serviceability; efficiency 50–88%.
- Welds: permanent, high strength, economical for steel; distortion/HAZ and NDT requirements; serviceability poor (cut to remove).
- Adhesives: excellent for dissimilar materials, sealing, damping, and uniform stress (scarf/stepped); require surface prep; poor peel resistance unless designed; serviceability poor.
- Press-fits: compact, no fasteners, good torque transmission; requires precise machining and assembly force; serviceability moderate (press out).
- Pins/keys: location and torque transfer; low cost; keys allow axial sliding (feather); pins for pivots/retention.
- Positive locking (cotter/safety wire) for critical/safety joints; prevailing-torque/chemical for convenience — [Component Solutions Group](https://www.componentsolutionsgroup.com/blog/thread-locking-methods); [DesignJudges](https://www.designjudges.com/articles/threaded-fasteners).

### Inferences
- For safety-critical or certification joints (aerospace), prefer positive mechanical locks or redundant fasteners over friction-only locking.
- Total cost = fastener + labor + inspection + rework risk; adhesives/welds shift cost to process control.

### Gaps
- Quantitative cost comparisons and serviceability ratings by industry not sourced; treat as engineering judgment.
- Corrosion/galvanic considerations for mixed-material joints not covered.
