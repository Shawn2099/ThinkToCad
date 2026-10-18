# Joints, Fasteners, Bearings, and Springs — Mechanical Design Catalog

## Fasteners (bolts/screws, grades, preload, torque-tension, thread engagement, self-locking, rivets, pins, keys, retaining rings)

### Takeaway
Metric threaded fasteners are governed by ISO 898-1 property classes (4.6–12.9); a target preload of ~75–85% of proof load is typical, with torque estimated by T = K·F·d (K ≈ 0.20). Thread engagement, locking, and standard small parts (pins, keys, rings) follow workshop practice and manufacturer/standard references.

### Cited Findings
- ISO metric steel fastener property classes include 4.6, 4.8, 5.6, 5.8, 6.8, 8.8, 9.8, 10.9, and 12.9; ISO 898-1:2013 remains the current edition (reviewed/confirmed 2025). — [RoyMech](https://www.roymech.co.uk/Useful_Tables/Screws/Screw_loads.htm)
- Nominal tensile stress areas As,nom (mm²): M6 20.1, M8 36.6, M10 58.0, M12 84.3, M14 115, M16 157, M20 245, M22 303, M24 353, M30 561, M36 817. — [RoyMech](https://www.roymech.co.uk/Useful_Tables/Screws/Screw_loads.htm)
- Minimum ultimate tensile loads Fm,min (kN), property class 8.8: M6 16.1, M8 29.2, M10 46.4, M12 67.4, M14 92.0, M16 125, M20 203, M22 252, M24 293, M30 466, M36 678; class 10.9: M6 20.9 … M36 850; class 12.9: M6 24.5 … M36 997. — [Engineering ToolBox](https://www.engineeringtoolbox.com/metric-bolts-minimum-ultimate-tensile-proof-loads-d_2026.html); [RoyMech](https://www.roymech.co.uk/Useful_Tables/Screws/Screw_loads.htm)
- Proof loads Fp (kN), class 8.8: M6 11.6, M8 21.2, M10 33.7, M12 48.9, M14 66.7, M16 91.0, M20 147, M22 182, M24 212, M30 337, M36 490; class 10.9: M6 16.7 … M36 678; class 12.9: M6 19.5 … M36 792. — [RoyMech](https://www.roymech.co.uk/Useful_Tables/Screws/Screw_loads.htm)
- Proof load is the max tensile force without plastic deformation; material stays elastic up to proof load, typically 85–95% of yield strength. Acceptable clamp (preload) load is typically 75% of proof load. — [Engineering ToolBox](https://www.engineeringtoolbox.com/metric-bolts-minimum-ultimate-tensile-proof-loads-d_2026.html)
- Estimated tightening torque T = K·Fm·d with K = 0.20, Fm = 0.85·Fp (i.e., T = 0.20 × 0.85 × Fp × d). Example torques (N·m), class 8.8: M6 11.8, M8 28.8, M10 57.3, M12 99.8, M16 247.5, M20 500, M24 865, M30 1719. — [RoyMech](https://www.roymech.co.uk/Useful_Tables/Screws/Screw_loads.htm)
- Torque is only an indirect preload-control method; friction consumes much of the applied torque; lubrication/coatings/surface condition change preload for the same torque. For critical joints use an appropriate tightening procedure rather than a generic torque table. — [RoyMech](https://www.roymech.co.uk/Useful_Tables/Screws/Screw_loads.htm)
- Metric coarse and fine threads both covered by ISO 898-1; fine-pitch stress areas and proof loads tabulated separately (e.g., M8×1.0, M10×1.0/1.25, M12×1.25/1.5). — [Engineering ToolBox](https://www.engineeringtoolbox.com/metric-bolts-minimum-ultimate-tensile-proof-loads-d_2026.html)
- UNC/UNF inch threads and SAE J429 grades (Grade 2/5/8) are the US equivalents; tensile/proof loads tabulated per size. — [Engineering ToolBox (US bolts)](https://www.engineeringtoolbox.com/us-bolts-tensile-proof-load-d_2066.html)
- Thread locking methods: nyloc nuts, threadlocking adhesives, prevailing-torque nuts, safety wire, cotter pins, tab washers. — [RoyMech — Screw Thread Locking Systems](https://www.roymech.co.uk/Useful_Tables/Screws/Locking.html)
- Retaining rings: DIN 471 = external (shaft) circlips, DIN 472 = internal (bore) circlips; size range roughly Ø3–300 mm shaft and Ø8–400 mm bore; spring steel. — [Rotorclip](https://www.rotorclip.com/din-standard-retaining-rings-circlips-tapered-section/); [Impex Industrial](https://impexindustrialcorporation.com/blog/din-471-vs-din-472)
- Machine keys: square/flat keys, Woodruff keys (ASME B17.2, used on shafts ~0.25–2.5 in dia), gib-head (tapered) keys (DIN 6887 / BS 46). — [Huyett](https://www.huyett.com/blog/machine-key-comprehensive-guide); [Machine Design](https://www.machinedesign.com/archive/article/21831730/shaft-keys-101); [Keyseaters Woodruff chart](https://www.keyseaters.com/local/woodruff-key-size-chart-asme-b17-2-dimensions-keyseat-reference-nmt/)
- Pins: dowel, clevis, cotter, taper pins are standard workshop fasteners; dimensions in manufacturer/standard tables. — [RoyMech — Circlips/Pins](https://www.roymech.co.uk/Useful_Tables/Circlips/)
- Rivets: solid/blind (pop) rivets common for sheet/assembly; design data in rivet tables. — [RoyMech — Rivets](https://www.roymech.co.uk/Useful_Tables/Rivets.html)

### Inferences
- For small workshop assemblies, M6/M8/M10 in 8.8 or 10.9 with nyloc or threadlocker is the default; 12.9 is reserved for high-strength, non-corrosive, controlled-torque joints.
- Thread engagement of ~1.0–1.5d in steel (2–3d in aluminum/cast iron) is commonly used as a rule of thumb; verify against ISO 965 thread limits for safety-critical joints.
- Self-locking is best achieved by threadlocker (medium strength) for general use; nyloc nuts are preferred for vibration/repeated disassembly; prevailing-torque nuts for high temperature.

### Gaps
- Exact thread-engagement length equations and self-locking torque values were not sourced.
- UNC/UNF load tables, SAE grade mechanical properties, and rivet/pin/key dimensional tables were not retrieved; consult Machinery's Handbook / ASME B1.1 / SAE J429 / ISO 8734.
- Threadlocker grades (e.g., Loctite 243/271) and nyloc temperature limits were not sourced.

## Joints (welded, brazed/soldered, adhesives, press-fit/shrink-fit, pinned, bolted flanges; efficiency and fatigue)

### Takeaway
Welded joint efficiency varies strongly with weld type and inspection level: double-welded butt joints reach 1.00 (full NDE), while single full-fillet lap joints without plug welds are ~0.45. Bolted joints rely on preload; other joint types (brazed/soldered, adhesive, press/shrink-fit, pinned, flanged) are standard categories but were not sourced in detail here.

### Cited Findings
- Joint efficiency E = strength of joint / strength of base material (percentage), used in ASME/API codes; varies with weld type and extent of NDE. — [Engineers Edge](https://www.engineersedge.com/weld/welded_joint_efficiency_14419.htm)
- Welded joint efficiency table (full inspection / spot / not inspected): double-welded (or equivalent) butt joint 1.00 / 0.85 / 0.70; single-welded butt with backing strip remaining 0.90 / 0.80 / 0.65; single-welded butt without backing strip — / — / 0.60; double full-fillet lap joint — / — / 0.55; single full-fillet lap with plug welds — / — / 0.50; single full-fillet lap without plug welds — / — / 0.45. — [Engineers Edge](https://www.engineersedge.com/weld/welded_joint_efficiency_14419.htm)
- Butt welds distribute load uniformly and achieve higher efficiency in tension; fillet welds act in shear along the throat and tolerate more fit-up variation. — [Therness](https://www.therness.com/blog/weld-joint-design-types-sizing-iso-acceptance-criteria/)
- Bolted joint preload/clamping and torque relationships per ISO 898-1 (see Fasteners section). — [RoyMech](https://www.roymech.co.uk/Useful_Tables/Screws/Screw_loads.htm)

### Inferences
- For workshop fabrication, fillet welds are convenient but should be derated (~0.45–0.55) for pressure/structural calculations; butt welds with full penetration are preferred for primary load paths.
- Bolted flanged joints should be designed for gasket seating and operating loads using preload from the Fasteners section; use torque sequence (star pattern) and re-torque after heat cycles.
- Press-fit/shrink-fit joints rely on interference; small parts typically use light interference (h7/p6, h7/s6) and benefit from chamfers and lubrication; thermal expansion (ΔT ≈ interference / (α·d)) is the sizing basis.

### Gaps
- No sourced data for brazed/soldered joint strengths, adhesive bond design (overlap length, peel), press/shrink-fit interference tables, pinned joint design, or bolted flange gasket factors.
- Fatigue detail categories (S-N curves, notch factors) and weld fatigue improvement methods were not sourced; consult IIW/EC3/Eurocode or Shigley.

## Bearings (ball, roller, plain/sleeve, thrust; L10 life, load ratings, fit, lubrication, sealing)

### Takeaway
Rolling-bearing life is sized by L10 = (C/P)^p million revolutions (p = 3 for ball, 10/3 for roller) using catalog dynamic load rating C and equivalent load P; shaft/housing fits follow ISO 286 tolerance zones (e.g., shaft g6/h6/j6/k5/m5/n6, housing H7/J7/K7).

### Cited Findings
- Basic rating life L10 = (C/P)^p, in millions of revolutions, where C = basic dynamic load rating and P = equivalent dynamic bearing load. — [SKF — Bearing life](https://www.skf.com/us/products/thin-section-bearings/introduction-thin-section/bearing-load-and-life/bearing-life); [Maintenance World](https://maintenanceworld.com/2016/09/30/meaning-bearing-life/)
- Life exponent p = 3 for ball bearings and p = 10/3 for roller bearings. — [Kapent](https://kapent.com/maximizing-bearing-life/); [EngiCalcHub (ISO 281)](https://engicalchub.com/calculators/bearing-life-calculator/)
- C (basic dynamic load rating) is the load at which a bearing achieves a calculated life of 1 million revolutions (ISO 281). — [SKF — Basic dynamic load rating C](https://www.skf.com/group/products/rolling-bearings/principles-of-rolling-bearing-selection/bearing-selection-process/bearing-size/size-selection-based-on-rating-life/basic-dynamic-load-rating-c)
- Rolling-bearing fits on shaft/housing are specified by ISO 286 tolerance zones; common selections: shaft g6, h6, j6, k5, m5, n6; housing H7, J7, K7 (rotating inner ring → interference shaft fit; rotating outer ring → interference housing fit). — [Starnex bearing tolerance chart](https://starnexindustrialspares.com/technical-resources/bearing-tolerance-chart); [SKF — Tolerances and resultant fits](https://www.skf.com/group/products/rolling-bearings/principles-of-rolling-bearing-selection/bearing-selection-process/bearing-interfaces/tolerances-and-resultant-fits)
- Common bearing types: deep-groove ball, angular-contact ball, cylindrical roller, tapered roller, needle roller, thrust (ball/roller), and plain/sleeve bearings. — [SKF product families](https://www.skf.com/group/products/rolling-bearings/principles-of-rolling-bearing-selection/bearing-selection-process/bearing-size/size-selection-based-on-rating-life/basic-dynamic-load-rating-c)
- For initial lubrication only, service life in hours uses Gh = b1·b2·b3·rating life (regular relubrication basis). — [SKF — Basic rating life calculation](https://www.skf.com/us/products/plain-bearings/spherical-plain-bearings-rod-ends/principles/selecting-bearing-size/basic-rating-life-calculation)

### Inferences
- For small workshop shafts (Ø10–40 mm), deep-groove ball bearings (60xx/62xx series) are the default; use angular contact for combined radial/axial loads and tapered rollers for high radial+thrust loads.
- Fit selection: rotating shaft with stationary housing → tighter shaft fit (k5/m5/n6) and looser housing fit (H7); reverse for rotating housing.
- Sealing choice: rubber (contact) seals for dusty/wet environments with higher friction; metal shields for high speed/low friction; open bearings for grease-packed, clean environments.
- Lubrication: grease (NLGI 2) for most small bearings; oil for high speed; relubrication interval scales with speed and load.

### Gaps
- Dynamic/static load rating tables by bearing number, lubrication viscosity/relubrication intervals, sealing ratings, and bearing material/heat-treatment specifics were not sourced.
- Static load rating C0 and equivalent static load P0 formula were not sourced.
- Plain/sleeve bearing (PV) limits and hydrodynamic design were not sourced.

## Springs (helical compression/extension/torsion, leaf, Belleville, gas, constant-force; rate, solid height, buckling, fatigue, materials)

### Takeaway
Helical spring rate k = G·d⁴/(8·D³·n_a) with D = D_outer − d and G = E/[2(1+ν)]; solid height L_solid = d·(N+1) for unground ends or d·N for ground ends. Helical compression/extension/torsion and conical springs are standard catalog items; leaf, Belleville, gas, and constant-force springs were not sourced.

### Cited Findings
- Spring rate k = G·d⁴/(8·D³·n_a), where d = wire diameter, D = mean diameter, n_a = active coils, G = shear modulus. — [Compression Spring](https://www.compressionspring.com/helical-spring-formulas-and-equations.html); [Acxess Spring](https://www.acxesspring.com/spring-constant-calculator.html)
- Hooke's law: k = F/x (load per unit deflection). — [Compression Spring](https://www.compressionspring.com/helical-spring-formulas-and-equations.html)
- Mean diameter D = D_outer − d; shear modulus G = E/[2(1+ν)] (E = Young's modulus, ν = Poisson's ratio). — [Compression Spring](https://www.compressionspring.com/helical-spring-formulas-and-equations.html)
- Solid height: L_solid = d·(N+1) for unground ends; L_solid = d·N for ground ends. — [Compression Spring](https://www.compressionspring.com/helical-spring-formulas-and-equations.html)
- Pitch: p = (L − 3d)/n_a (closed ends), (L − 2d)/n_a (closed & ground), (L − 5d)/n_a (double closed), (L − d)/n_a (open ends). — [Compression Spring](https://www.compressionspring.com/helical-spring-formulas-and-equations.html)
- Catalog spring types: compression, extension, torsion, conical (helical). — [Compression Spring](https://www.compressionspring.com/compression-spring-stock-catalog.html); [Acxess Spring](https://www.acxesspring.com/)
- Music wire is a common spring material in textbook problems. — [Chegg problem set](https://www.chegg.com/homework-help/questions-and-answers/problem-3-28-points-helical-compression-spring-made-hard-drawn-spring-steel-wire-2-mm-diam-q265280692)

### Inferences
- For small workshop springs, music wire (ASTM A228) or stainless (A313, 302/316) are default; phosphor bronze for electrical/corrosive; oil-tempered (A229) for larger, lower-cost springs.
- Design checks: max shear stress at solid (τ = K·(8FD)/(πd³)), spring index C = D/d (target 4–12), buckling for slender springs (L_free/D > ~4 → use guide/parallel springs or reduce free length), and fatigue via modified Goodman with shot peening for cyclic service.
- Extension springs need initial tension and hook stress concentration checks; torsion springs need body stress and arm deflection; both need end-form design for DFM.

### Gaps
- Buckling curves/critical slenderness, fatigue (Goodman/Soderberg) equations, Belleville/leaf/gas/constant-force spring formulas, and material property tables (G, E, allowable stress by material/temper) were not sourced.
- Standard wire sizes and spring index limits were not sourced; consult Shigley/Mott/Machinery's Handbook and spring manufacturer catalogs.
- Shot peening, presetting, and corrosion protection specifics were not sourced.
---
*Sources: Engineering ToolBox, RoyMech, SKF, Compression Spring/Acxess Spring, Engineers Edge, Rotorclip/Impex, Huyett, Machine Design, Keyseaters, Therness, Kapent, EngiCalcHub, Maintenance World, Chegg. Research conducted 2026-10-19.*
