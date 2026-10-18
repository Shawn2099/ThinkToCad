# Materials Selection and Failure Analysis for Mechanical Design

## Material Properties: Strength, Stiffness, Density, Hardness, Toughness, Ductility, Thermal, Corrosion, Machinability, Weldability

### Takeaway
Material selection is governed by a small set of measurable properties (yield/ultimate/fatigue strength, E/G, density, hardness, toughness, ductility, thermal coefficients, corrosion resistance, machinability, weldability); for small-workshop frugal design, density and cost often dominate because E and σ_y are fixed by alloy class, while heat-treatment condition and form/availability vary most.

### Cited Findings
- Yield strength is the highest stress a material can withstand without significant plastic deformation; ultimate strength is the maximum engineering stress; fracture stress is the stress at fracture. Stiffness is the stress/strain ratio in the elastic region (elastic moduli). Ductility is the strain before fracture; ductile materials neck before failure. — [Physics UIUC lecture notes](https://courses.physics.illinois.edu/me598dm/sp2020/4.selection.pdf)
- Specific stiffness E/ρ and specific strength σ_f/ρ are the canonical performance indices for light, stiff/strong tie rods (Ashby 2005/2011). — [NASA "Materials Selection for Aerospace Systems"](https://ntrs.nasa.gov/api/citations/20120001798/downloads/20120001798.pdf)
- Aluminum density ≈ 2.7 g/cm³ vs steel ≈ 7.83 g/cm³ (about one-third); one cubic foot of steel ≈ 490 lb, aluminum ≈ 170 lb. Aluminum has an inert oxide film giving corrosion resistance; thermal conductivity of Al alloys ≈ 50–60% of copper. — [NIST "Aluminum and Aluminum Alloys" (Davis)](https://materialsdata.nist.gov/bitstream/handle/11115/173/Aluminum%20and%20Aluminum%20Alloys%20Davis.pdf)
- 6061-T6: density 2.7 g/cc, UTS 310 MPa, yield 276 MPa, E 68.9 GPa, G 26 GPa, Brinell 95, fatigue strength 96.5 MPa (5×10⁸ cycles reversed), CTE 23.6 µm/m·°C, thermal conductivity 130 W/m·K, elongation 12–17%. — [ASM MatWeb 6061-T6](https://asm.matweb.com/search/SpecificMaterial.asp?bassnum=MA6061t6)
- 7075-T6: density 2.81 g/cc, UTS 572 MPa, yield 503 MPa, E 71.7 GPa, G 26.9 GPa, shear strength 331 MPa, fatigue strength 159 MPa, fracture toughness K_IC 20–29 MPa·m½ (orientation dependent), CTE 23.6 µm/m·°C, thermal conductivity 130 W/m·K. — [ASM MatWeb 7075-T6](https://asm.matweb.com/search/SpecificMaterial.asp?bassnum=MA7075T6)
- 4140 (annealed/typical): density 7.85 g/cc, UTS ≈ 655 MPa, yield ≈ 415 MPa, elongation 25%, hardness 217–241 HB; heat-treated UTS 850–1000 MPa, yield ~655 MPa, hardness 28–32 HRC. — [vovanoxiwi/ASTM A434 doc](https://cdn.prod.website-files.com/6724a8c8e50f1d4bb74ee90b/6895dfb255998799181c401f_vovanoxiwi.pdf)
- 4340 (prehardened 250–280 HB): density 7.85 g/cc, YS 660–760 MPa, UTS 800–900 MPa, elongation 17–20%, Charpy V 40 J; Q&T (limiting section 30 mm) yield ≥1005–1125 MPa, UTS 1150–1300+ MPa. — [Industeel 4340 datasheet](https://industeel.arcelormittal.com/fichier/ds-mold-4340)
- Engineering plastics comparison (Pro Plastics): PEEK (max service 480°F, tensile 16 ksi yield, flexural modulus 600 ksi, relative cost $$$$$), Ultem (338°F, 17 ksi, 500 ksi), Delrin (180°F, 11 ksi, 470 ksi, $$), Nylon (185°F, 12 ksi, 450 ksi, $$), PTFE (500°F, 3.2 ksi at break, 72 ksi), UHMW (180°F, 3.1 ksi, 87 ksi, $). — [Pro Plastics comparison](https://www.proplasticsinc.com/en/materials/comparison)
- Delrin (POM-H): tensile 10 ksi, flexural modulus 410 ksi, density 0.051 lb/in³, moisture absorption 0.22% (24 h)/0.9% (sat), COF vs steel 0.20, max continuous 180°F. Nylon 6/6: tensile 12 ksi, flexural 400 ksi, density 0.041 lb/in³, moisture 1.2%/2.5%, COF 0.30–0.40, max 220°F. — [RivCut Delrin vs Nylon](https://www.rivcut.com/blog/delrin-vs-nylon)
- UHMW-PE: tensile 3,100 psi, elongation 350%, flexural modulus 110 ksi, Shore D 64, notched Izod 18 ft·lb/in, COF 0.10–0.20, max service 180°F, water absorption slight. Nylon: tensile 12,400 psi, elongation 90%, flexural 410 ksi, Izod 1.2, COF 0.28, max 210°F, water absorption 1.2%. — [Curbell UHMW vs Nylon](https://www.curbellplastics.com/resource-library/material-selection-tools/plastic-material-comparisons/uhmw-vs-nylon)
- PEEK: continuous service to 480°F (250°C), tensile ~100 MPa, moisture 0.1%; costs 7–20× Delrin/nylon in rod form ($180–300/ft for 2" dia vs $15–25/ft Delrin, $10–20/ft nylon). — [MakerStage PEEK/Delrin/nylon guide](https://www.makerstage.com/resources/cnc-plastics-comparison)
- Machinability/weldability notes: aluminum has good machinability but poor weldability in high-strength grades (7075 rated D for weldability); 6061 has good weldability. Delrin machines best among plastics; PEEK needs sharp tools and heat control. — [ThyssenKrupp 7075 datasheet (weldability ratings)](https://ucpcdn.thyssenkrupp.com/_legacy/UCPthyssenkruppBAMXUK/assets.files/material-data-sheets/aluminium/7075.pdf); [RivCut PEEK vs Delrin](https://www.rivcut.com/blog/peek-vs-delrin-machining)

### Inferences
- For frugal workshop design, the actionable split is: choose alloy class by strength/stiffness/temperature need (steel vs Al vs plastic), then choose temper/heat-treatment and form by availability and cost; E and density are essentially fixed by class, so geometry (section) does more work than material.
- Plastics substitute for metals mainly on cost/corrosion/weight and where loads are light; nylon's moisture absorption makes it risky for tight-tolerance parts, favoring Delrin/PEEK.
- 7075-T6's high strength comes with poor weldability and stress-corrosion sensitivity; 6061-T6 is the default general-purpose Al.

### Gaps
- No single authoritative table of all properties (hardness, toughness, thermal) for every grade cited; values are supplier/standard typical and vary by form and heat treatment. Manufacturer datasheets and ASTM/EN product standards are the authoritative source for design values.
- Brass/bronze and composite (CFRP/GFRP) property data not quantified here beyond class-level statements; needs supplier datasheets.

---

## Material Selection Methods: Ashby Charts, Performance Indices, Screening and Ranking

### Takeaway
Ashby's method: translate design requirements into (1) constraints (property limits), (2) objectives (minimize mass/cost), (3) free variables (geometry/material), derive a material index M = (property combination), screen candidates by constraints, then rank survivors by index on log-log Ashby charts; for frugal design, add cost and availability as explicit constraints.

### Cited Findings
- Ashby method steps: (1) translate design requirements, (2) screen by constraints (property limits such as max service temp, corrosion), (3) rank by performance index, (4) seek supporting information (datasheets, price, availability). — [UIUC ME598 lecture notes](https://courses.physics.illinois.edu/me598dm/sp2020/4.selection.pdf)
- Performance index: a combination of material properties that, when maximized, maximizes performance; e.g., specific stiffness E/ρ and specific strength σ_f/ρ for light, stiff/strong tie rods/beams. More generally M_i = f(M_1, M_2, …) with exponents from the functional/geometric separation. — [NASA materials selection](https://ntrs.nasa.gov/api/citations/20120001798/downloads/20120001798.pdf); [Ashby 2nd ed. (UTC)](https://www.utc.fr/~hagegebe/UV/MQ12/CORRECTIONS_TD/%5BASHBY99%5D%20-%20Materials%20Selection%20In%20Mechanical%20Design%202Ed.pdf)
- Ashby charts are log-log plots of two properties (e.g., E vs ρ, σ_y vs ρ, K_IC vs ρ); lines of constant performance index are straight lines; materials above the line are better. Material classes occupy distinct "bubbles" (metals, polymers, ceramics, composites, foams). — [UIUC notes](https://courses.physics.illinois.edu/me598dm/sp2020/4.selection.pdf); [MIT CBA materials table](https://fab.cba.mit.edu/classes/865.21/topics/mechanical_design/materials/)
- Light, stiff beam index: maximize E^(1/2)/ρ (or E^(1/3)/ρ for panels); light, strong tie-rod: σ_y/ρ; light, strong beam (strength-limited): σ_y^(2/3)/ρ. Cost included via cost per unit property. — [Ashby 2nd ed. (UTC)](https://www.utc.fr/~hagegebe/UV/MQ12/CORRECTIONS_TD/%5BASHBY99%5D%20-%20Materials%20Selection%20In%20Mechanical%20Design%202Ed.pdf)
- ASM Handbook Vol. 20 "Materials Selection and Design" (Dieter ed.) documents material property charts (modulus-density, strength-density, fracture toughness-density, modulus-strength, specific stiffness-specific strength, thermal charts) and performance indices. — [ASM Digital Library](https://dl.asminternational.org/handbooks/edited-volume/59/chapter/685860/Material-Property-Charts)
- Screening vs ranking: screening uses hard limits (e.g., T_service ≥ 200°C, non-magnetic, corrosion-resistant to salt water); ranking uses indices. Cost and availability are treated as material attributes (price includes extraction, processing, forming, disposal). — [Ashby 2nd ed.](https://www.utc.fr/~hagegebe/UV/MQ12/CORRECTIONS_TD/%5BASHBY99%5D%20-%20Materials%20Selection%20In%20Mechanical%20Design%202Ed.pdf)
- Multi-criteria decision methods (e.g., VIKOR combined with Ashby indices) used in practice for automotive lightweighting, combining design/cost/environmental indices. — [MDPI Machines 2025](https://www.mdpi.com/2075-1702/13/1/63)
- Practical workshop table (MIT CBA): 6061 Al E=69 GPa, ρ=2710 kg/m³, cost ~$87 for 6mm×24×24", machinability "breezy with waterjet, painful on shopbot"; steel E=200 GPa, ρ=7860, cost ~$200. — [MIT CBA](https://fab.cba.mit.edu/classes/865.21/topics/mechanical_design/materials/)

### Inferences
- For a small workshop, the realistic short list is usually: mild steel (1018/1045), 4140, 304/316 SS, 6061-T6, 7075-T6, Delrin, nylon, UHMW, PEEK — chosen by availability and standard stock sizes, then checked against constraints.
- Cost per unit property (e.g., $/MPa·m³/kg) is more useful than $/kg for structural parts; for one-off workshop parts, stock size and minimum order often dominate.

### Gaps
- No verified cost database in these notes; prices are indicative and region/supplier dependent; CES/Ashby databases and supplier quotes are the source.

---

## Failure Modes: Yielding, Fatigue, Creep, Wear, Corrosion, Brittle Fracture

### Takeaway
Most mechanical service failures are fatigue (~90% per ASM); design against fatigue (endurance limit with Marin factors, mean-stress criteria), yielding (von Mises/Tresca), and environment (corrosion/wear) covers the majority of workshop failures; brittle fracture is governed by flaw size and toughness (K_IC), requiring fracture-mechanics treatment for high-strength/critical parts.

### Cited Findings

**Yielding**
- Tresca (maximum shear stress): yield when τ_max = σ_y/2; von Mises (distortion energy): yield when σ_vm = σ_y, where σ_vm = sqrt(((σ1−σ2)²+(σ2−σ3)²+(σ3−σ1)²)/2). Both are pressure-independent and apply to ductile metals; Tresca is ~15% more conservative than von Mises in plane stress. — [MIT Unified M5.3](https://web.mit.edu/16.unified/www/SPRING/materials/Lectures/M5.3-Unified09.pdf); [Auckland plasticity notes](https://pkel015.connect.amazon.auckland.ac.nz/SolidMechanicsBooks/Part_II/08_Plasticity/08_Plasticity_03_YieldCriteria.pdf)
- Von Mises can be written for plane stress as σ1² − σ1σ2 + σ2² = σ_y². — [MIT notes](https://web.mit.edu/16.unified/www/SPRING/materials/Lectures/M5.3-Unified09.pdf)
- For brittle materials, maximum principal stress (Rankine) is used; Tresca/von Mises do not apply well because brittle materials fracture rather than yield. — [UIUC TAM 251](https://courses.physics.illinois.edu/tam251/su2021/TAM251_Chapter10_FailureTheories_prelecture_Johnson.pdf)

**Fatigue**
- Fatigue contributes to ~90% of all mechanical service failures; fatigue failures occur at stresses far below single-load failure stress. — [ASM "Elements of Metallurgy and Engineering Alloys" (icdst pdf)](https://dl.icdst.org/pdfs/files/98887906524869bb3a115372888c0dc4.pdf)
- S-N (stress-life) method: Basquin equation for finite life; endurance limit S_e for steels (plateaus ~10⁶ cycles). Aluminum has no fatigue limit — use finite-life methods. — [Quadco S-N/Haigh calculator notes](https://www.quadco.engineering/en/know-how/sn-haigh-diagram-calculator.htm)
- Endurance limit modified by Marin factors: S_e = S_e'·k_a·k_b·k_c·k_d·k_e·k_misc (surface finish k_a, size k_b, load type k_c, temperature k_d, reliability k_e). Rotating-beam value S_e' ≈ 0.5·S_ut for steels (capped ~700 MPa). — [Quadco](https://www.quadco.engineering/en/know-how/sn-haigh-diagram-calculator.htm)
- Mean-stress criteria (Haigh diagram): Goodman: σ_a/S_e + σ_m/S_ut = 1/n; Soderberg: σ_a/S_e + σ_m/S_y = 1/n (most conservative, guards against yield); Gerber: (σ_a/S_e) + (σ_m/S_ut)² = 1/n (parabolic, closer to test data for ductile metals). Test data usually fall between Goodman and Gerber; notched data fall closer to Goodman; Soderberg seldom used. — [ScienceDirect Goodman overview](https://www.sciencedirect.com/topics/engineering/goodman-diagram); [ASM Elements of Metallurgy](https://dl.icdst.org/pdfs/files/98887906524869bb3a115372888c0dc4.pdf); [Dowling/fundamentals of metal fatigue](https://mbarkey.eng.ua.edu/courses/AEM649/CH1.pdf)
- Strain-life (ε-N, low-cycle fatigue) for plastic strain ranges; fracture-mechanics (Paris law, ΔK) for crack growth; SIF K_I = Yσ√(πa), compare to K_IC. — [Shigley/ME471 MSU notes](https://www.egr.msu.edu/~pkwon/me471/Lect%206.3.pdf) (general); fracture toughness values e.g., 7075-T6 K_IC 20–29 MPa·m½.
- Marin factors example: for 1045 steel, S_e' = 310 MPa, k_a=0.821, k_b=0.902, k_c=1, k_e=1 → S_e = 229.5 MPa. — [Quadco](https://www.quadco.engineering/en/know-how/sn-haigh-diagram-calculator.htm)

**Creep**
- Creep is time-dependent deformation under sustained load at elevated temperature; relevant when T > ~0.3–0.4 T_m (homologous). Not covered in depth by cited sources here; design uses creep rupture strength and Larson-Miller parameter. — [flagged as gap below]

**Wear**
- Four main mechanisms: adhesive, abrasive, surface fatigue, corrosive (tribochemical); fretting is a combination of adhesive + corrosive + abrasive wear in small-amplitude oscillation. — [ASTM STP41912S "Various Modes of Wear"](https://store.astm.org/stp41912s.html); [ScienceDirect Wear overview](https://www.sciencedirect.com/topics/engineering/wear-damage)
- Adhesive wear: cold-welding of asperities then shear; influenced by crystal structure (HCP lower friction/wear than cubic). Wear volume ∝ 1/hardness of softer material (Archard-type). — [ASTM STP41912S](https://store.astm.org/stp41912s.html)
- Abrasive wear: hard surface or third body cuts soft surface; governed by hardness, work hardening. — [ASTM STP41912S](https://store.astm.org/stp41912s.html)
- Fretting: small-amplitude oscillation (e.g., shrink fits, bolted joints, bearings) → oxidational wear, subsurface fatigue; accelerates with load cycles; design: avoid, lubricate, use interference-fit tolerances, or select materials with low fretting tendency. — [PMC fretting study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11051016); [ScienceDirect wear overview](https://www.sciencedirect.com/topics/engineering/wear-damage)
- Galling resistance is a standard test (ASTM G98) and a key selection criterion for stainless-steel threaded fasteners/sliding pairs. — [ASTM corrosion/wear standards](https://store.astm.org/products-services/standards-and-publications/standards/corrosion-standards-and-wear-standards.html)

**Corrosion**
- Forms: galvanic (two dissimilar metals in electrolyte — e.g., Al + steel, Cu + steel), crevice, pitting, stress corrosion cracking (SCC), intergranular, exfoliation. Galvanic series: pair metals close in the series; coat the more noble/lower-rated metal; avoid unfavorable combos (copper gutters with Al downspouts; steel bolts on brass in marine). — [NIST CIS 9 corrosion](https://nvlpubs.nist.gov/nistpubs/Legacy/CIS/nbscis9.pdf)
- SCC: certain metal-environment combos (Al alloys + salt water; bent iron + fertilizers). Mitigation: avoid combos, stress relieve, use resistant grades (316 SS, 7075-T73). — [NIST CIS 9](https://nvlpubs.nist.gov/nistpubs/Legacy/CIS/nbscis9.pdf)
- ASTM corrosion/wear standards list: SCC, pitting, crevice, galvanic, cavitation erosion, intergranular, exfoliation, cyclic potentiodynamic polarization. — [ASTM](https://store.astm.org/products-services/standards-and-publications/standards/corrosion-standards-and-wear-standards.html)

**Brittle fracture**
- Brittle fracture is governed by flaw size and toughness; Weibull statistics for brittle materials (ceramics); K_IC for metals. Modified-Mohr/Coulomb-Mohr for brittle materials under multiaxial stress. — [Caltech thesis intro](https://thesis.caltech.edu/18643/03/gorske_thesis_chapter1_introduction.pdf); [Stanford ME111 modified-Mohr](https://web.stanford.edu/class/me111/handouts/lecture_21.pdf)
- High-strength steels and Al 7xxx are notch-sensitive; 7075-T6 has K_IC ~20–29 MPa·m½ vs 6061-T6 ~29 MPa·m½. — [ASM MatWeb](https://asm.matweb.com/search/SpecificMaterial.asp?bassnum=MA7075T6); [ASM MatWeb 6061](https://asm.matweb.com/search/SpecificMaterial.asp?bassnum=MA6061t6)

### Inferences
- Default design flow: check static yield (von Mises) with safety factor 1.5–3; check fatigue (Goodman, with Marin factors) for cyclic parts; check environment (corrosion, wear) for the operating medium; check fracture toughness for high-strength/notched parts.
- For workshop parts, most failures are fatigue + corrosion + wear; creep is rarely relevant below ~150°C for steels.

### Gaps
- Creep data (creep rupture, Larson-Miller) not sourced here; for high-temperature design consult ASM Handbook Vol. 1 / specialized creep data.
- Fracture-mechanics crack-growth (Paris constants) not quantified per alloy.

---

## Heat Treatment: Annealing, Normalizing, Hardening, Tempering, Case Hardening, Precipitation Hardening

### Takeaway
Heat treatment is the lever that converts a single alloy into a family of property sets: annealing softens for machining/forming, normalizing refines grain, quench-and-temper raises strength/hardness with controlled toughness, case hardening gives hard wear-resistant surfaces over tough cores, and precipitation (age) hardening is how Al and maraging steels reach high strength; tempering temperature is the main strength-vs-toughness dial.

### Cited Findings
- Heat treatment types: annealing (full, stress-relief, recrystallization, spheroidizing), normalizing, hardening (quench), tempering, austempering, martempering, case hardening (carburizing, nitriding, cyaniding, carbonitriding, flame/induction). — [RCET heat treatment notes](https://www.rcet.org.in/uploads/academics/rohini_82463510230.pdf)
- Annealing: heat to above upper critical temp and slow cool (furnace); refines grains, removes strain, improves machinability/formability. Stress-relief: heat below critical (600–700°C) then slow cool. Recrystallization: removes cold-work strain. Spheroidizing: softens high-carbon steel for machining. — [RCET](https://www.rcet.org.in/uploads/academics/rohini_82463510230.pdf); [GTZ trainees' handbook](https://ftpmirror.your.org/pub/misc/cd3wd/1003/_me_annealing_hardening_tempering_gtz077ce_en_139320_.pdf)
- Normalizing: heat above upper critical and air cool; produces finer pearlite/ferrite than annealing, higher strength/hardness than annealed, more uniform. — [RCET](https://www.rcet.org.in/uploads/academics/rohini_82463510230.pdf)
- Hardening: heat to hardening temp (hypo-eutectoid: 30–50°C above upper critical; hyper-eutectoid: 30–50°C above lower critical), hold, quench in water/oil/brine; forms martensite; raises tensile/yield strength, hardness, wear resistance. — [RCET](https://www.rcet.org.in/uploads/academics/rohini_82463510230.pdf)
- Tempering: reheat hardened steel below lower critical (200–500°C typical), soak, air cool; relieves residual stress, improves ductility/toughness at some hardness loss. Tempering effect is combination of time and temperature. Avoid 250–450°C temper brittleness in 4340-type steels. — [RCET](https://www.rcet.org.in/uploads/academics/rohini_82463510230.pdf); [Industeel 4340 (avoid 250–450°C)](https://industeel.arcelormittal.com/fichier/ds-mold-4340)
- Case hardening (surface hardening): diffuse C/N into surface of low-carbon steel; gives hard wear-resistant case over tough ductile core. Carburizing (gas/pack/liquid) raises surface C to ~0.8%; nitriding introduces N (no quench needed, low distortion); cyaniding/carbonitriding faster; flame/induction hardening for localized hardening. — [RCET](https://www.rcet.org.in/uploads/academics/rohini_82463510230.pdf); [ThyssenKrupp case-hardening steels (0.07–0.31% C, surface to ~0.8% C)](https://www.thyssenkrupp-steel.com/media/content_1/publikationen/produktinformationen/c_stahl/thyssenkrupp_c-staehle_product_information_steel_en.pdf)
- Case-hardening steels (e.g., 8620): low carbon (0.18–0.23%) for tough core; SAE 8620 is the standard case-hardening alloy steel. — [AIMS steel grades](https://aimsindustrial.com.au/blogs/product-guides/steel-grades-comparison)
- Precipitation (age) hardening: solution anneal → quench → age (natural or artificial); basis of 6061/7075 Al strength and maraging steels. For 18Ni maraging 250: solution anneal 800–815°C, age 480°C/3 h; peak strength at 800–815°C anneal; grain growth if >6 h at 955°C. — [ASM HTS maraging note](https://www.asminternational.org/hts/effect-of-annealing-time-and-temperature-on-aged-properties)
- 4140 heat-treatment study: annealing 900°C/2 h, normalizing 919°C/2 h, oil quench 944°C/1 h found optimum for hardness+impact; hardening highest hardness, tempering improved tensile, annealing highest ductility; hardness decreased and impact energy increased with temperature/time for all three. — [PMC 4140 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12397307)
- 42CrMo4 (4140 equiv.) annealing: hardness drops from ~355 HV to ~165 HV with spheroidizing anneal, improving cold formability (cold hardening ability up to 185%). — [PMC 42CrMo4 annealing](https://pmc.ncbi.nlm.nih.gov/articles/PMC7254350)
- ASM Handbook Vol. 4 (Heat Treating) and "Practical Heat Treating: Basic Principles" (Dossett, ASM 2020) cover austenitizing, quenching systems, tempering, temper embrittlement, precipitation hardening. — [ASM](https://dl.asminternational.org/technical-books/monograph/141/chapter/2419178/Hardening-and-Tempering-of-Steel)

### Inferences
- For workshop: buy 4140/4340 in annealed condition, machine, then Q&T to spec; buy 6061-T6 / 7075-T6 in final temper (re-heat-treating Al in a small shop is impractical without furnace control).
- Case hardening (carburizing) is the route to hard wear surfaces on cheap low-carbon steel; nitriding is lower-distortion for precision parts.

### Gaps
- Specific tempering curves (hardness vs temper temp) for each grade not reproduced here; use ASM Handbook Vol. 4 / supplier datasheets.
- Austempering/martempering parameters and bainite structures not quantified.

---

## Common Engineering Materials: Steels, Aluminum, Brass/Bronze, Plastics, Composites

### Takeaway
Default palette for a small workshop: mild steel 1018/1045 for general fabrication and shafts; 4140/4340 (Q&T) for high-strength shafts/gears; 304/316 SS for corrosion resistance; 6061-T6 for general Al structures; 7075-T6 for high-strength Al; Delrin for precision plastics; UHMW for wear strips; PEEK only when temperature/chemistry demand it.

### Cited Findings

**Steels**
- SAE/AISI numbering: 4 digits; first two = class (1xxx carbon, 2xxx Ni, 3xxx Ni-Cr, 4xxx Mo, 41xx Cr-Mo, 43xx Ni-Cr-Mo, 5xxx Cr, 6xxx Cr-V, 8xxx Ni-Cr-Mo, 9xxx Si-Mn); last two = carbon content in 0.01% (e.g., 1045 = 0.45% C plain carbon). AISI stopped involvement in 1995; SAE (J1086) maintains. — [Wikipedia SAE steel grades](https://en.wikipedia.org/wiki/SAE_steel_grades); [Engineering ToolBox](https://www.engineeringtoolbox.com/aisi-sae-steel-numbering-system-d_1449.html); [PMPA](https://www.pmpa.org/tag/aisi-sae-steel-grade-nomenclature)
- 1018: low carbon 0.15–0.20%, weldable, machinable, cold-formable; general fabrication, shafts, mild fasteners. 1045: medium carbon 0.43–0.50%, shaft grade, higher strength. — [AIMS](https://aimsindustrial.com.au/blogs/product-guides/steel-grades-comparison)
- 1095: high carbon 0.90–1.03%, spring/blade steel. 11xx resulfurized free-machining; 12xx resulfurized+rephosphorized. — [Engineering ToolBox](https://www.engineeringtoolbox.com/aisi-sae-steel-numbering-system-d_1449.html)
- 4140 (Cr-Mo): C 0.38–0.43, Cr 0.80–1.10, Mo 0.15–0.25; workhorse alloy steel; hydraulic shafts, gears, bolts Grade 8.8+, axles, crankshafts. 4340 (Ni-Cr-Mo): C 0.38–0.43, Ni 1.65–2.00, Cr 0.70–0.90, Mo 0.20–0.30; highest-strength common alloy steel; crankshafts, landing gear, heavy transmission shafts, Grade 10.9/12.9 fasteners. — [AIMS](https://aimsindustrial.com.au/blogs/product-guides/steel-grades-comparison)
- 4340 has higher hardenability and toughness than 4140 (Ni); risk of quench cracking on small sections due to high hardenability. — [4140 vs 4340 pdf](https://cdn.prod.website-files.com/6868bc545db8016bfc8c083f/68abbd86fc6971e1a6b2877b_pufijokixunagugepepaso.pdf)
- Stainless: 300 series austenitic (304, 316); 316 adds Mo for chloride resistance (marine grade). 316L extra-low carbon for welding/reactor vessels. 400 series martensitic/ferritic. 200 series austenitic Mn-Ni. — [Wikipedia SAE](https://en.wikipedia.org/wiki/SAE_steel_grades)
- Tool steels: M2 (HSS cutting), H13 (hot-work die), D2 (cold-work die). — [AIMS](https://aimsindustrial.com.au/blogs/product-guides/steel-grades-comparison)
- 90% of all metal used in technology is iron-based. — [Ashby (icdst)](https://dl.icdst.org/pdfs/files3/319da279b227abb7b415931e0594a983.pdf)

**Aluminum**
- 1xxx pure Al (electrical/chemical); 2xxx Cu (aerospace, e.g., 2024); 3xxx Mn; 4xxx Si; 5xxx Mg (marine); 6xxx Mg-Si (6061 general purpose, good weldability); 7xxx Zn (7075 high strength, poor weldability). — [NIST Al overview](https://materialsdata.nist.gov/bitstream/handle/11115/173/Aluminum%20and%20Aluminum%20Alloys%20Davis.pdf)
- 6061-T6: UTS 310 MPa, yield 276 MPa, E 68.9 GPa, density 2.7 g/cc, good weldability/corrosion resistance, machinability 50%. — [ASM MatWeb 6061](https://asm.matweb.com/search/SpecificMaterial.asp?bassnum=MA6061t6)
- 7075-T6: UTS 572 MPa, yield 503 MPa, E 71.7 GPa, density 2.81 g/cc, high strength but poor weldability (D), stress-corrosion sensitive; T73 temper improves SCC resistance. — [ASM MatWeb 7075](https://asm.matweb.com/search/SpecificMaterial.asp?bassnum=MA7075T6); [ThyssenKrupp 7075](https://ucpcdn.thyssenkrupp.com/_legacy/UCPthyssenkruppBAMXUK/assets.files/material-data-sheets/aluminium/7075.pdf)

**Brass/Bronze (class-level, unverified specifics)**
- Brass (Cu-Zn): good machinability, corrosion resistance, non-sparking; bronze (Cu-Sn): bearings, wear resistance; naval brass/bronze for marine. Specific grades/properties not sourced here — gap. — [no specific source; flagged]

**Plastics**
- Delrin (POM-H): best machinability, dimensional stability, low moisture, good wear/fatigue; gears, bushings, precision parts; max 180°F. — [RivCut](https://www.rivcut.com/blog/delrin-vs-nylon); [Pro Plastics](https://www.proplasticsinc.com/en/materials/comparison)
- Nylon 6/6: stronger/tougher, higher temp (220°F), absorbs moisture (dimensional change); bearings, gears; lubricated with oil/grease performs well. — [RivCut](https://www.rivcut.com/blog/delrin-vs-nylon); [Curbell](https://www.curbellplastics.com/resource-library/material-selection-tools/plastic-material-comparisons/uhmw-vs-nylon)
- UHMW-PE: extreme abrasion/wear resistance, low friction, tough, cheap; wear strips, chain guides, dock fenders; max 180°F; poor machinability for fine detail (soft). — [Curbell](https://www.curbellplastics.com/resource-library/material-selection-tools/plastic-material-comparisons/uhmw-vs-nylon); [Pro Plastics](https://www.proplasticsinc.com/en/materials/comparison)
- PEEK: high temp (480°F), strength, chemical resistance, sterilizable; aerospace/medical; 7–20× cost of Delrin; machines with sharp tools, heat control. — [MakerStage](https://www.makerstage.com/resources/cnc-plastics-comparison); [RivCut PEEK vs Delrin](https://www.rivcut.com/blog/peek-vs-delrin-machining)
- PTFE: lowest friction, extreme chemical/temp resistance, poor mechanical strength/wear; seals, gaskets, valve seats. Ultem (PEI): high temp, strength, good machinability. — [Pro Plastics](https://www.proplasticsinc.com/en/materials/comparison); [Laird Plastics](https://lairdplastics.com/engineering-plastics)

**Composites**
- CFRP/GFRP: high specific stiffness/strength; anisotropic (properties along fiber direction); machining difficult (delamination, dust); repair/inspection harder. Not quantified here — gap. — [class-level; no specific source]

### Inferences
- Rule of thumb: if a part sees < 180°F and moderate load, try Delrin or 6061 first; if wear-dominated, UHMW or bronze; if high strength and fatigue, 4140/4340 Q&T; if corrosion, 316 SS or 6061; if extreme temp/chem, PEEK/PTFE.

### Gaps
- Brass/bronze grade-level data (C360 free-machining brass, C932 bearing bronze, etc.) not sourced.
- Composite (CFRP/GFRP) property data and DFM not sourced.

---

## Material Standards: AISI/SAE, ASTM, ISO, EN

### Takeaway
Use SAE/AISI for steel grade numbers (1045, 4140), ASTM for product specifications and test methods (A29, A434, B308, E8, E18), ISO/EN for international equivalence (C45, 42CrMo4, 1.0503); cross-reference via grade-equivalence tables; specify both grade and condition/temper and the governing standard.

### Cited Findings
- SAE J1086 numbering metals and alloys; AISI originally co-maintained but dropped out in 1995 (never wrote specs). Four-digit carbon/alloy steels; stainless three-digit. — [Wikipedia SAE](https://en.wikipedia.org/wiki/SAE_steel_grades)
- ASTM A29/A434: hot-wrought alloy steel bars (includes 4140) — chemical composition and mechanical properties. ASTM B308/B308M: 6061-T6 aluminum. ASTM E8: tension testing; E18: Rockwell hardness; G-series: wear/corrosion tests. — [ASTM 6061-T6](https://www.astm.org/b0308_b0308m-20.html); [ASTM corrosion/wear standards](https://store.astm.org/products-services/standards-and-publications/standards/corrosion-standards-and-wear-standards.html)
- ISO 683 / EN 10027: European steel designation (symbolic + numeric). Equivalences: SAE 1045 ≈ EN C45 (1.0503); 1018 ≈ C20 (1.0402); 4140 ≈ EN 42CrMo4 / 41CrMo4 / SCM440; 4340 ≈ 34CrNiMo6 (1.6565) / EN24; M2 ≈ HS6-5-2C (1.3343); H13 ≈ X40CrMoV5-1 (1.2344). — [AIMS steel grades comparison](https://aimsindustrial.com.au/blogs/product-guides/steel-grades-comparison)
- Aluminum designation: AA/ANSI H35.1 system (1xxx–8xxx series by major alloying element; temper designations T6, T651, T73 etc.). — [ANSI/AA H35.1 preview](https://webstore.ansi.org/preview-pages/AA/preview_AA+ANSIH35.1.pdf); [SAE J452 for Al casting alloys](https://www.sae.org/standards/j452_201801-general-information-chemical-compositions-mechanical-physical-properties-sae-aluminum-casting-alloys)
- Standards Australia adopted SAE/AISI numbering with 'K' prefix for carbon steels (AS 1442) and SAE number directly for alloy (AS 1444). — [AIMS](https://aimsindustrial.com.au/blogs/product-guides/steel-grades-comparison)

### Inferences
- Always specify grade + temper/condition + standard (e.g., "AISI 4140, ASTM A29, Q&T to 28–32 HRC") to avoid receiving the wrong condition.
- For international sourcing, use EN/ISO numeric designations and request mill certs.

### Gaps
- Full ISO/EN-to-AISI equivalence tables for all grades not reproduced; use supplier/standard cross-reference tables.

---

## DFM, Cost, and Availability Notes for Small-Workshop / Frugal Design

### Takeaway
For frugal workshop design, prefer standard stock sizes and common grades (1018/1045, 4140 annealed, 6061-T6, 304 SS, Delrin, UHMW); design around available forms (round bar, plate, sheet) and avoid exotic grades that require minimum orders or heat-treatment facilities.

### Cited Findings
- Cost drivers: material cost dominates for plastics (PEEK 7–20× Delrin); for metals, machining time often exceeds material cost. Machining rates ~$75–125/hr for plastics; material cost for a 3×3×1" bracket: PEEK $40–80 vs Delrin/nylon $3–8. — [MakerStage](https://www.makerstage.com/resources/cnc-plastics-comparison)
- Machinability ratings: Delrin excellent (±0.001" achievable, 8–16 Ra finish); PEEK good but needs sharp tools and heat control; UHMW soft/difficult for fine detail; 6061 machines moderately; 7075 harder; 4140/4340 in annealed condition machinable but work-hardens. — [RivCut PEEK vs Delrin](https://www.rivcut.com/blog/peek-vs-delrin-machining); [RivCut Delrin vs Nylon](https://www.rivcut.com/blog/delrin-vs-nylon); [Pro Plastics](https://www.proplasticsinc.com/en/materials/comparison)
- Weldability: 6061 good; 7075 poor (D); 304/316 good (316L for heavy sections); 1018/1045 good; 4140/4340 weldable with preheat/postheat. — [ThyssenKrupp 7075 (weldability D)](https://ucpcdn.thyssenkrupp.com/_legacy/UCPthyssenkruppBAMXUK/assets.files/material-data-sheets/aluminium/7075.pdf); [class-level for steels]
- Formability: Al 6061/5052 good; 7075 limited; plastics all machinable; steel 1018 cold-formable, 4140 less so.
- Availability: standard stock forms (round bar, plate, sheet, tube) in common grades; exotic grades (7075 large sections, PEEK) have long lead times and minimum orders.
- DFM for plastics: account for moisture absorption (nylon grows); design generous radii; avoid thin walls in soft plastics; use appropriate feeds/speeds to avoid melting (Delrin).
- DFM for metals: design for available bar/plate sizes; avoid deep pockets in hard materials; consider heat-treatment distortion (Q&T); leave machining allowance on Q&T parts.

### Inferences
- A practical frugal-selection checklist: (1) define loads/environment/life; (2) pick candidate class from availability; (3) check constraints (temp, corrosion, wear); (4) check yield + fatigue + environment; (5) pick standard stock form/size; (6) verify cost and lead time; (7) specify grade+condition+standard.

### Gaps
- No verified regional cost/availability data; supplier quotes required.
- No quantitative machinability ratings beyond qualitative (Delrin "excellent", etc.) and the 0–100 Al machinability scale (6061=50, 7075=70).