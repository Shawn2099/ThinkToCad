# Machining Shop-Floor Reference (Speeds, Feeds, Tools, DFM)

## Speed and Feed Tables

### Takeaway
Cutting speed is set primarily by tool material and work material: HSS is the conservative baseline, carbide runs ~2.5× faster, and ceramic/CBN/diamond far higher; feeds scale with diameter and rigidity. Shop practice starts from published tables and derates for manual oil application, small machines, and deep holes.

### Cited Findings
- Formula: N (rpm) = 12·V (sfm)/(π·D (in)); f (in/min) = N·fr (drilling) or N·ft·(#teeth) (milling). Metric: V (m/min) = π·D (m)·N/1000. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- HSS surface speeds (sfm / m/min): mild steel .2-.3C 100 / 30.5; steel .4-.5C 60 / 18.3; aluminum alloys 250 / 76.2; brass 360 250 / 76.2; bronze high-tensile 100 / 30.5; cast iron soft 100 / 30.5, medium 80 / 24.4, hard chilled 20 / 6.1; stainless free-machining 40 / 12.2, work-hardening 20 / 6.1; titanium 20 / 6.1; tool steel 40 / 12.2; Inconel 25 / 7.6; Hastelloy 20 / 6.1; Monel 25 / 7.6; magnesium 300 / 91.4; Acetal 250 / 76.2. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- Carbide multiplier: surface speeds ×2.5 for carbide tools; HEM/HSM toolpaths ×1.5–2.0. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- Manual-oil derating: scale feed and speed to 60% of calculated (flooded) values. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- Drilling feeds (HSS/carbide, in/rev): under 1/8" up to 0.002; 1/8–1/4" 0.002–0.004; 1/4–1/2" 0.004–0.008; 1/2–1" 0.008–0.016; 1"+ 0.016+. Rule of thumb: feed = 1–3% of drill diameter. Multiply feed ×0.5 for difficult materials, flexible setups, or light machines. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- End-mill feeds (in/tooth): Delrin 0.008–0.030; Al 0.004–0.012; brass 360 0.004–0.012; bronze 0.002–0.006; cast iron 0.002–0.006; mild steel 0.002–0.008; steel .4-.5C 0.002–0.006; tool steel 0.0015–0.004; stainless free-machining 0.002–0.006, work-hardening 0.0015–0.004; titanium 0.0015–0.004; Inconel/Hastelloy/Monel 0.0015–0.004; magnesium 0.004–0.012. Table values typical for 3/4–1.5" cutters. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- Kalpakjian turning ranges (carbide/ceramic, m/min): aluminum 200–1000; gray cast iron 60–900; copper alloys 50–700; high-temp alloys 20–400; steels 50–500; stainless 50–300; thermoplastics 90–240; titanium 10–100; tungsten 60–150. Speeds for HSS are lower; higher ranges for coated carbides/cermets; diamond far higher. Feeds generally 0.15–1.0 mm/rev; depths of cut 0.5–12 mm. — [Kalpakjian & Schmid, via Common Machining Processes PDF](https://ocw.sumdu.edu.ua/system/collection_nodes/blobs/000/109/608/original/Common_Machining_Processes.pdf)
- Kalpakjian milling ranges (carbide/ceramic/cermet/diamond, m/min): aluminum 300–3000; gray cast iron 90–1300; copper 90–1000; high-temp 30–550; steels 60–450; stainless 90–500; thermoplastics 90–1400; titanium 40–150. Feeds 0.08–0.46 mm/tooth; depths 1–8 mm. — [Kalpakjian & Schmid, via Common Machining Processes PDF](https://ocw.sumdu.edu.ua/system/collection_nodes/blobs/000/109/608/original/Common_Machining_Processes.pdf)
- Machinery's Handbook 31st ed. provides combined feed/speed (optimum/average) pairs at ~45-min tool life for turning/milling/drilling/reaming with grade-specific data (HSS, carbide, ceramic, cermet, CBN, PCD); adjustment tables for feed, depth of cut, lead angle, radial depth, and tool life (15–180 min). — [Machinery's Handbook 31st ed.](https://online.flippingbook.com/view/954192180/1238-1239/)
- Specific energy (W·s/mm³): aluminum 0.4–1.1; cast iron 1.6–5.5; copper 1.4–3.3; high-temp 3.3–8.5; magnesium 0.4–0.6; nickel 4.9–6.8; stainless 3.0–5.2; steel 2.7–9.3; titanium 3.0–4.1. Multiply ×1.25 for dull tools. — [Kalpakjian & Schmid, Common Machining Processes](https://ocw.sumdu.edu.ua/system/collection_nodes/blobs/000/109/608/original/Common_Machining_Processes.pdf)

### Inferences
- For a small workshop on manual machines, the HSS baseline derated to 60% with manual oil is the safe starting point; carbide's 2.5× multiplier is only realized with rigid setups and adequate coolant.
- Kalpakjian's upper ranges exceed typical shop capability; treat them as CNC/rigid-machine ceilings, not manual-machine targets.

### Gaps
- No complete Machinery's Handbook Table 1 (turning steels) numeric grid reproduced here; only structure and ranges. Full per-grade optimum/average pairs require the handbook. — [Machinery's Handbook 31st ed.](https://online.flippingbook.com/view/954192180/1233/)

## Tool Selection (HSS vs Carbide, Coatings, Inserts, Tool Life)

### Takeaway
HSS is tough, cheap, and regrindable—best for complex geometry (drills, taps, form tools) and interrupted cuts at low speed. Carbide is harder and hotter-running, best for production and high speed. Coatings (TiN → TiAlN → AlTiN) raise the usable temperature ceiling; geometry (rake, nose radius, chip breaker) must match material and cut type.

### Cited Findings
- HSS: heat-treated to Rc ~65, 12–20% W (T-grade) or 6% W + 5% Mo (M-grade); still used extensively for complex geometry such as drills; regrindable; thin coatings. — [MSU cutting tool notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- Cemented carbide (WC-Co): high compressive strength, hot hardness, wear resistance, thermal conductivity; tougher grades (high Co, large grain) for roughing/milling; harder grades (low Co) for finishing. Add TiC/TaC for steel-cutting grades to resist crater wear. — [MSU cutting tool notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- Cermets (TiC/TiN/TiCN with Ni/Mo binders): high-speed finishing/semifinishing of steels, stainless, cast iron; higher speeds than carbide; low feed for better finish. — [MSU cutting tool notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- Ceramics (alumina, Si₃N₄, sialon, whisker-reinforced): finishing of hardened steels at high speed, low depth/feed, rigid setup; not for heavy interrupted cuts. CBN for steels/nickel alloys; diamond for nonferrous (not ferrous—transforms to carbon). — [MSU cutting tool notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- Coating thickness: CVD/PVD 2.5–13 µm (0.0001–0.0005 in); best at high speed where dynamic force and thermal shock are minimal. — [MSU cutting tool notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- PVD vs CVD: PVD lower deposition temp preserves edge toughness, compressive residual stress, sharper edges, finer grain, higher microhardness—better for interrupted cuts (milling, threading) and finishing. CVD better adhesion; thicker coatings; multilayer designs. — [SVC hard coating review](https://www.svc.org/clientuploads/directory/resource_library/99_345.pdf)
- Coating properties (hardness/temp/friction): TiN 22–33 GPa, 500–600 °C, µ 0.40–0.55, 1–7 µm, general wet machining of less-hard materials. TiAlN 29–36 GPa, 700–900 °C, µ 0.35–0.60, 1–4 µm, dry machining of hard materials. AlTiN 32–39 GPa, 850–1000 °C, µ 0.50–0.70, 1–4 µm, high-speed dry machining of hard materials. TiCN 32 GPa, 400 °C, µ 0.20. RUnaTEC 45 GPa, 1200 °C. — [Material Science Research India](https://www.materialsciencejournal.org/vol17no2/an-insight-into-tin-tialn-and-altin-hard-coatings-for-cutting-tools/); [RUKO](https://ruko.de/en/knowledge/know-how/tin-tialn-altin-a-comparison-of-coatings/)
- Service life multipliers vs uncoated: TiN up to 3×, TiAlN up to 10×, AlTiN up to 14× (application-dependent). — [Material Science Research India](https://www.materialsciencejournal.org/vol17no2/an-insight-into-tin-tialn-and-altin-hard-coatings-for-cutting-tools/)
- TiAlN/AlTiN form an Al₂O₃+TiO₂ passive layer at >800 °C that dissipates heat via chip removal, enabling higher speed. — [Material Science Research India](https://www.materialsciencejournal.org/vol17no2/an-insight-into-tin-tialn-and-altin-hard-coatings-for-cutting-tools/)
- Tapping test (GG25 cast iron, dry, 50 m/min): TiAlN coating doubled tap life vs uncoated; TiAlN+WC/C lowest wear in transition zone. — [Coatings (MDPI)](https://doi.org/10.3390/coatings10050464)
- Rake angle by tool material: HSS +5° to +20°; carbide −5° to +10°; ceramic −5° to −15° (negative for strength at high temp). — [MSU cutting tool notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- Chip breakers: groove/obstruction types force chip curl so it fractures; needed to control long stringy chips. — [MSU cutting tool notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- C-grade carbide classification: C1–C4 non-steel grades (roughing→precision finishing) by toughness/wear; C5–C8 steel grades with TiC/TaC for crater resistance. High Co for roughing/milling, low Co for finishing. — [MSU cutting tool notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- Taylor tool life equation: V·Tⁿ = C (V m/min, T min); generalized V·Tⁿ·fᵖ·dᵠ = C. n ≈ 0.1–0.15 (HSS), 0.2–0.25 (carbide), 0.6–1.0 (ceramic); C = speed for 1-min life. — [ASEE study](https://peer.asee.org/a-study-of-tool-life-sensitivity-to-cutting-speed.pdf); [MSU notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool); [Poriyaan](https://mech.poriyaan.in/topic/tool-life-31720/)
- Taylor constants table: HSS n=0.125, C=70 m/min (steel work) / 120 (non-steel); carbide n=0.25, C=500 (steel) / 900 (non-steel); ceramic n=0.6, C=3000 (steel). — [MSU notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- Extended n ranges: HSS 0.1–0.5; tungsten carbide 0.2–0.4; ceramic 0.4–0.6. — [Poriyaan](https://mech.poriyaan.in/topic/tool-life-31720/)
- Tool life criteria in practice: complete failure; visual flank/crater wear; fingernail test; sound change; ribbony/stringy chips; surface finish degradation; increased power; part count; cumulative cutting time. — [MSU notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- ISO 3685 defines long-term tool-life test (turning/milling, steel/cast iron) for HSS, sintered carbide, ceramic; criterion flank wear VB. — [Sci. paper, DOI 10.22223/tr.2012-2/1917](https://doi.org/10.22223/tr.2012-2/1917)

### Inferences
- For a small shop, HSS remains the right choice for drills/taps/reamers and one-off form tools; carbide inserts dominate turning/milling production work where speed and insert indexing matter.
- PVD coatings belong on sharp-edged and interrupted-cut tools (milling, threading); CVD on heavy continuous turning.

### Gaps
- No single universal C value for a given grade—C depends on feed, depth, work material; vendor catalogs (Sandvik/Seco/Kennametal) give application-specific data. Flag unverified if quoting generic constants.

## Machining Operations

### Takeaway
Each operation has characteristic geometry, tooling, and parameter rules: turning uses single-point inserts with nose radius; milling uses rotating multi-tooth cutters; drilling needs peck cycles beyond ~3–4× diameter; boring/reaming/tapping refine holes. Reamers run at ~half drill speed and 2× feed.

### Cited Findings
- Turning: depth of cut generally 0.5–12 mm; feeds 0.15–1 mm/rev; cutting speed varies by tool material. Roughing uses large depth/feed, finishing uses small depth/feed and larger nose radius for finish. — [Kalpakjian, Common Machining Processes](https://ocw.sumdu.edu.ua/system/collection_nodes/blobs/000/109/608/original/Common_Machining_Processes.pdf)
- Nose radius wear and feed marks: surface finish in turning governed by feed and nose radius (f²/(8·R) theoretical). — [Kalpakjian & Schmid](https://ocw.sumdu.edu.ua/system/collection_nodes/blobs/000/109/608/original/Common_Machining_Processes.pdf) (surface finish section)
- Milling types: plain/peripheral (slab), face, end, slot/slit, form, straddle. Feed per tooth f = v/(N·W) (v travel speed, W rpm, N teeth). MRR = v·w·d. — [MIT 2.810 machining lecture](https://web.mit.edu/2.810/www/files/lectures/lec5-machining-2019.pdf)
- Face milling: based on 10-tooth 8" cutter, 15° lead angle, 3/64" nose radius, ap=0.1", width ratio 3/4; adjust with Tables 15b–15d. — [Machinery's Handbook 31st ed.](https://online.flippingbook.com/view/954192180/1238-1239/)
- End milling example: 3-tooth, 20° helix, 1" dia, ap 0.2", full slot (radial 1"). — [Machinery's Handbook 31st ed.](https://online.flippingbook.com/view/954192180/1238-1239/)
- Drilling: cutting speed varies along edge, zero at center; large thrust force; flutes evacuate chips; friction at OD. Twist drills usually HSS. — [MSU notes](https://www.egr.msu.edu/~pkwon/me478/cuttingtool)
- Peck drilling: recommended peck depth = one drill diameter with flooded coolant; 50% of diameter with manual oil/low pressure. For holes >3×D without through-spindle coolant, reduce speed an additional 50%. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- Countersinking: ~25% of speed, same feed per rev as equivalent drill. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- Annular cutter plunging: 75% speed, 25% feed of peripheral; do not plunge <0.001 ipt in strain-hardening materials (304 SS, titanium). — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- Reaming: run at half spindle speed and twice feed per rev of equivalent drill. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- Parting on lathe: speeds as calculated; feed 0.001 in/rev (steels) to 0.005 (plastics) on CNC; manual lathe max ~600 rpm chuck for safety. — [UF Design Lab](https://web.mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm)
- Boring: internal surfaces/profiles; boring bar stiffness critical to avoid chatter; tolerance ~0.025 mm achievable. — [Kalpakjian, Common Machining Processes](https://ocw.sumdu.edu.ua/system/collection_nodes/blobs/000/109/608/original/Common_Machining_Processes.pdf)
- Reaming tolerance: ±0.005–0.02 mm; boring ±0.005–0.01 mm; drilling ±0.05–0.15 mm. — [Sinbo DFM hole guide](https://www.sinbo-machining.com/wiki/dfm/hole-design)
- Broaching: good finish, costly tooling, high production rate; tolerance 0.025–0.15 mm. — [Kalpakjian, Common Machining Processes](https://ocw.sumdu.edu.ua/system/collection_nodes/blobs/000/109/608/original/Common_Machining_Processes.pdf)
- Tapping: thread engagement 1.5×D steel/stainless/titanium, 2×D aluminum/magnesium, 2.5×D+ plastics. Blind holes need ≥3 pitches or ~0.5×D extra drilled depth. — [SSG MFG design guide](https://ssgmfg.com/design-guides/cnc-machining); [TPM DFM guide](https://www.trueprecisionmachining.com/engineering/dfm-guide/)
- Kalpakjian hole-making chapter covers drilling, reaming, tapping, boring machines. — [Kalpakjian & Schmid TOC](https://www.pearson.com/en-us/subject-catalog/p/manufacturing-engineering-and-technology/P200000011629/9780138309466)

### Inferences
- Reaming is a sizing/finishing operation, not a stock-removal operation: leave 0.1–0.3 mm (0.004–0.012 in) for the reamer.
- For deep holes, peck cycles and through-spindle coolant dominate cost more than cutting speed.

### Gaps
- Tapping speeds/feeds not quantified in sources beyond "straight oils or heavy-duty emulsifiable oils ideal for drilling and tapping" and engagement depths. — [American Machinist/Fictiv](https://www.americanmachinist.com/machining-cutting/article/21278638/choosing-the-right-coolants-and-lubricants-for-machining-operations-fictiv)

## DFM for Machining

### Takeaway
Design to standard tools and stock: standard drill sizes, internal radii ≥ tool radius + margin, wall thickness ≥ material minimum, hole depth ≤ 4×D (10× with peck), thread engagement 1.5×D. Every non-standard feature adds a setup, tool change, or secondary process.

### Cited Findings
- Internal corner radius: ≥1/3 cavity depth, minimum 0.8 mm (0.030 in); slightly larger than cutter radius (~1.3× cutter radius) so tool arcs through; use same radius everywhere to avoid tool changes. — [Hubs](https://www.hubs.com/knowledge-base/reducing-cnc-machining-costs-design-tips/); [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining); [TPM DFM guide](https://www.trueprecisionmachining.com/engineering/dfm-guide/)
- Avoid radii equal to standard tool sizes (tool must stop and pivot). Radii should be above 0.5 mm. — [Xometry design guide](https://xometry.pro/wp-content/uploads/2023/07/EN-CNC-Machining-Design-Guide.pdf)
- Pocket depth ≤ 4× pocket width; cutter reach ideally <3× diameter. — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)
- Wall thickness minimum: metal 0.8 mm (steel/stainless ≥1.0 mm), plastic ≥1.5 mm. Absolute minimums ~0.5 mm metal, 1.0 mm plastic (assess case by case). Wall height < ~10× thickness. — [Hubs](https://www.hubs.com/knowledge-base/reducing-cnc-machining-costs-design-tips/); [Rapid Mfg](https://rapidmanufacturing.com.au/dfm-guide-cnc); [Xometry](https://xometry.pro/wp-content/uploads/2023/07/EN-CNC-Machining-Design-Guide.pdf); [Protolabs](https://www.protolabs.com/en-gb/services/cnc-machining/cnc-milling/high-speed-cnc-milling/) (0.5 mm min metal)
- Min hole diameter: CNC drilled ≥1.0 mm (≥1.5 mm preferred); sub-1 mm requires micro-drilling. Twist drill min 0.5 mm. — [Rapid Mfg](https://rapidmanufacturing.com.au/dfm-guide-cnc); [Sinbo](https://www.sinbo-machining.com/wiki/dfm/hole-design); [Protolabs](https://www.protolabs.com/en-gb/services/cnc-machining/cnc-milling/high-speed-cnc-milling/) (0.5 mm)
- Hole depth: standard ≤3–4×D; up to 10× with peck drilling; beyond → gun drilling. — [Hubs](https://www.hubs.com/knowledge-base/reducing-cnc-machining-costs-design-tips/); [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining); [Sinbo](https://www.sinbo-machining.com/wiki/dfm/hole-design)
- Standard metric drill sizes: 0.1 mm increments 1–13 mm; 0.5 mm increments above 13 mm. Fractional/letter/number drills in inch. Reamed holes at standard reamer sizes. — [Xometry](https://xometry.pro/wp-content/uploads/2023/07/EN-CNC-Machining-Design-Guide.pdf); [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)
- Tapped thread depth: 1.5×D in steel, up to 2× in aluminum/plastic. Tap drill depth = thread depth + 3 pitches (≈0.5×D) for blind holes. — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining); [TPM](https://www.trueprecisionmachining.com/engineering/dfm-guide/)
- Blind holes: allow 118° or 135° drill point cone at bottom; dimension depth to full diameter. — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)
- Small feature aspect ratio: width:height < 4:1; add bracing above. — [Hubs](https://www.hubs.com/knowledge-base/reducing-cnc-machining-costs-design-tips/)
- Chamfer/break edges: 0.25–0.5 mm ×45°; call out "break sharp edges" for the rest. — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)
- Default tolerance: ±0.005 in (±0.13 mm) or ISO 2768-m; tighten only fits/datums. — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)
- Hole entry on angled surface requires milled flat spot (adds cost). — [Rapid Mfg](https://rapidmanufacturing.com.au/dfm-guide-cnc)
- Design to stock sizes: leave 0.8–1.5 mm under standard bar/plate per side. — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)
- Put features on as few faces as possible (1–2 setups on 3-axis). — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)
- Draft angles for casting (not machining) are a casting-DFM concern; machining allowances on castings require removing scale (reduce speed 5–10%). — [Machinery's Handbook 31st ed.](https://online.flippingbook.com/view/954192180/1233/)

### Inferences
- In a small shop, standardizing on a few corner radii (e.g., R3 and R6) and one drill set minimizes tool changes and cost.
- Draft angles apply to cast/forged blanks; machined features themselves need no draft.

### Gaps
- No sourced universal minimum for undercut depth or keyseat sizes; match standard cutters. — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)

## Shop-Floor Knowledge (Chatter, Wear, BUE, Work Hardening, Burrs, Coolant)

### Takeaway
Most machining problems trace to rigidity, speed/feed mismatch, or material stickiness. Fixes are usually: increase rigidity, adjust speed/feed in the correct direction, use sharper/positive geometry, apply coolant correctly, and vary depth of cut.

### Cited Findings
- Chatter causes (turning/milling): poor setup, improper insert selection, low cutting speed, chatter-prone geometry, too-light cut, long tool overhang, thin walls. Fixes: sharp inserts, more positive chipbreaker, increase feed, increase lead angle, smaller nose radius, improve rigidity, reduce depth of cut, reduce speed, vibration-dampening holders. — [CarbideDepot troubleshooting](https://www.carbidedepot.com/formulas-turning-troubleshoot.htm); [Kezuriba](https://kezuriba.net/en/troubles/); [Garr Tool](https://www.garrtool.com/wp-content/uploads/2018/11/TECHNICAL.pdf)
- Flank wear: caused by high cutting speed or low wear-resistance grade; also abrasion/erosion at low speed (hard inclusions), diffusion at high speed. Fixes: reduce speed (sometimes increase feed), more wear-resistant/harder grade, correct coolant. — [Seco](https://www.secotools.com/article/tool_wear_patterns_in_machining?language=en); [CarbideDepot](https://www.carbidedepot.com/formulas-turning-troubleshoot.htm); [Iscar](https://www.iscar.com/en-us/products/insert-wear-troubleshooting/milling)
- Crater wear: thermal—diffusion/decomposition at high speed; abrasive at low. Caused by excessive temp/pressure on rake face. Fixes: reduce speed/feed, coolant, positive geometry, Al₂O₃-containing coatings, free-cutting geometry. — [Seco](https://www.secotools.com/article/tool_wear_patterns_in_machining?language=en); [Sandvik Coromant](https://www.sandvik.coromant.com/en-us/knowledge/materials/wear-on-cutting-edges)
- Built-up edge (BUE): adhesion of workpiece to cutting edge; occurs in gummy materials (low-carbon steel, stainless, aluminum) at low speed/feed, negative geometry. Eventually breaks off taking tool material → chipping. Fixes: increase speed and/or feed, sharper/positive rake, smoother rake face, PVD-coated or cermet or polished carbide grades, coolant. — [Seco](https://www.secotools.com/article/tool_wear_patterns_in_machining?language=en); [Sandvik Coromant](https://www.sandvik.coromant.com/en-us/knowledge/materials/wear-on-cutting-edges); [Schell Tools](https://www.schell-tools.com/en/troubleshooting-cutting-tools-wear)
- Notch wear: localized wear at depth-of-cut line; caused by work-hardened surface scale (stainless, superalloys, cast/forged surfaces) and hard inclusions. Fixes: reduce feed, vary depth of cut, tougher grade, reinforced edge, smaller entry angle. — [Seco](https://www.secotools.com/article/tool_wear_patterns_in_machining?language=en); [Sandvik Coromant](https://www.sandvik.coromant.com/en-us/knowledge/materials/wear-on-cutting-edges)
- Thermal cracks: rapid hot/cold cycling (interrupted cuts, milling, intermittent coolant). Fixes: correct coolant application or turn it off, tougher grade, reduce speed/feed, free-cutting geometry. — [Seco](https://www.secotools.com/article/tool_wear_patterns_in_machining?language=en); [Sandvik Coromant](https://www.sandvik.coromant.com/en-us/knowledge/materials/wear-on-cutting-edges)
- Chipping: mechanical overload, vibration, hard inclusions, BUE, brittle grade. Fixes: tougher grade, reinforced edge, increase speed, chatter-free geometry, vibration-dampening holders, reduce feed. — [Seco](https://www.secotools.com/article/tool_wear_patterns_in_machining?language=en); [Iscar](https://www.iscar.com/en-us/products/insert-wear-troubleshooting/milling)
- Plastic deformation: cutting temp too high for grade; harder grades and thicker coatings resist. — [Sandvik Coromant](https://www.sandvik.coromant.com/en-us/knowledge/materials/wear-on-cutting-edges)
- Work hardening: stainless and superalloys strain-harden; depth of cut must exceed the hardened layer; use positive geometry and adequate feed. Notch wear is the tell. — [CarbideDepot](https://www.carbidedepot.com/formulas-turning-troubleshoot.htm); [Kezuriba (stainless quirks)](https://kezuriba.net/en/troubles/)
- Burrs: 6 causes/9 fixes in turning/milling (feed, geometry, wear). Edge break 0.25–0.5 mm chamfer; deburr. — [Kezuriba](https://kezuriba.net/en/troubles/); [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)
- Coolant types: straight/cutting oils (neat, mineral/vegetable/animal/synthetic, EP additives) for heavy low-speed (drilling, tapping, broaching); soluble/emulsifiable oils (oil+water emulsion) for turning/milling; semi-synthetic (5–30% oil) mixed operations; synthetic (oil-free, water-based polymer) for high-speed/heat (grinding, turning). — [SME metalcutting fluids guide](https://www.sme.org/globalassets/sme.org/media/training-guides/dv05pub41_study_guide.pdf); [American Machinist/Fictiv](https://www.americanmachinist.com/machining-cutting/article/21278638/choosing-the-right-coolants-and-lubricants-for-machining-operations-fictiv); [Amsoil](https://amsoilcontent.com/Industrial/IND682_Lubrication_Logic_Cutting_and_Grinding_Oils_10-25.pdf)
- Water-based fluids diluted 2–25% (common 3–10%); pH 8.5–9.5; water-miscible. Straight oils not mixed with water; better lubricity, not for high speed. — [OSHwiki metalworking fluids](https://oshwiki.osha.europa.eu/en/themes/metalworking-fluids); [Sci. review](https://www.sciencedirect.com/science/article/pii/S2090447922001411)
- Application: flooding (low-pressure nozzle) most common; high-pressure/high-volume most effective for cooling and chip removal; mist; manual. — [SME guide](https://www.sme.org/globalassets/sme.org/media/training-guides/dv05pub41_study_guide.pdf)
- Coolant selection by operation: turning/milling → emulsifiable or semi-synthetic; drilling/tapping → straight oils or heavy-duty emulsifiable; grinding → synthetic/semi-synthetic low-viscosity; broaching → high-viscosity heavy-duty emulsifiable. — [American Machinist/Fictiv](https://www.americanmachinist.com/machining-cutting/article/21278638/choosing-the-right-coolants-and-lubricants-for-machining-operations-fictiv)
- Cast iron: often machined dry (no coolant) due to graphite lubrication; coolant can cause thermal shock. — [SME guide](https://www.sme.org/globalassets/sme.org/media/training-guides/dv05pub41_study_guide.pdf)
- Copper: neat oils corrosive to copper—avoid. — [American Machinist/Fictiv](https://www.americanmachinist.com/machining-cutting/article/21278638/choosing-the-right-coolants-and-lubricants-for-machining-operations-fictiv)
- Thermal cracks aggravated by coolant in interrupted cuts; sometimes shut coolant off. — [Seco](https://www.secotools.com/article/tool_wear_patterns_in_machining?language=en); [Iscar](https://www.iscar.com/en-us/products/insert-wear-troubleshooting/milling)
- Material-specific quirks: stainless work-hardening/welding/boundary wear; aluminum BUE/chips; titanium heat/welding/ignition; cast iron powdery chips/edge chipping/scale; hardened steel; Ni-base alloys; magnesium chip ignition; mild steel. — [Kezuriba](https://kezuriba.net/en/troubles/)

### Inferences
- In a small shop with manual machines, cutting dry or with manual oil (derated 60%) is common; flooding requires enclosure and pump. Match coolant to the most demanding operation in the shop.
- If one coolant for all, a semi-synthetic is the pragmatic compromise.

### Gaps
- No sourced numeric coolant concentration by material beyond 3–10% general and 2–25% range; follow manufacturer data. — [OSHwiki](https://oshwiki.osha.europa.eu/en/themes/metalworking-fluids)

## Surface Finish by Process

### Takeaway
Surface finish is a process-capability ladder: rough machining Ra 3.2–6.3 µm, finish turning/milling 0.4–1.6 µm, grinding 0.1–0.8 µm, honing/lapping 0.05–0.1 µm, superfinishing 0.012–0.025 µm. Each step down roughly doubles cost; specify only what function requires.

### Cited Findings
- Ra ranges by process (µm): sawing/planing/shaping 12.5–25; sand casting 6.3–12.5 (12.5–25 as-cast); rough turning/milling 3.2–6.3; finish turning/milling 0.8–1.6; surface grinding 0.2–0.4; cylindrical grinding 0.1–0.2; honing/lapping 0.05–0.1; superfinishing/polishing 0.012–0.025. — [Mech Codex](https://mechcodex.com/reference/surface-roughness-produced-by-common-machining-operations-turning); [Machinery's Handbook §12]
- Extended process table (typical/best Ra µm): rough turning (carbide) 1.6–6.3 / 0.8; finish turning (sharp carbide) 0.4–1.6 / 0.1; diamond turning 0.025–0.1 / 0.012; face milling 0.8–3.2 / 0.4; end milling (sidewall) 1.6–6.3 / 0.4; rough boring 1.6–6.3 / 0.8; finish boring 0.4–1.6 / 0.1; drilling 1.6–6.3 / 0.8; reaming 0.4–1.6 / 0.2; tapping 1.6–3.2 / 0.8; broaching 0.8–1.6 / 0.4; hobbing 0.8–3.2 / 0.4. — [MetricMech process-to-Ra chart](https://metricmech.com/reference/surface-finish-chart)
- Grinding/finishing: rough grinding (24–46 grit) 0.4–1.6 / 0.2; fine grinding (80–120 grit) 0.1–0.4 / 0.05; precision grinding (220+ grit) 0.025–0.1 / 0.012; cylindrical 0.1–0.8 / 0.05; centerless 0.2–0.8 / 0.1; honing 0.05–0.4 / 0.013; lapping 0.013–0.1 / 0.006; polishing 0.025–0.4 / 0.012; superfinishing 0.013–0.1 / 0.006; electropolishing 0.2–0.8 / 0.05. — [MetricMech](https://metricmech.com/reference/surface-finish-chart)
- Casting/forging: sand cast 12.5–25 (best 6.3); permanent mold 3.2–6.3 (1.6); die cast 1.6–6.3 (0.8); investment cast 1.6–3.2 (0.8); shell mold 3.2–6.3 (1.6); hot forging open die 6.3–25 (3.2); closed die 3.2–12.5 (1.6); cold forging 0.8–3.2 (0.4); PM as-sintered 1.6–3.2 (0.8). — [MetricMech](https://metricmech.com/reference/surface-finish-chart)
- General machining ranges: milling 0.8–6.3; turning/boring 0.4–6.3; drilling 1.6–6.3; reaming 0.4–1.6; grinding 0.1–1.6; honing 0.05–0.4; lapping/superfinishing 0.012–0.1; polishing 0.025–0.2; EDM 0.4–6.3. — [Ideambox surface finish reference](https://ideambox.com/assets/downloads/surface-finish-reference.pdf)
- ISO N grades (Ra µm): N1 0.025, N2 0.05, N3 0.1, N4 0.2, N5 0.4, N6 0.8, N7 1.6, N8 3.2, N9 6.3, N10 12.5, N11 25, N12 50. Each step ~2×. — [NORAMARK](https://www.noramark.com/resources/charts/surface-finish-chart/); [MetricMech](https://metricmech.com/reference/surface-finish-chart)
- Ra-to-Rz: Rz ≈ 4–7×Ra depending on texture (turned 4–5, milled 4–6, ground 5–7, honed 5–7, lapped 6–8, EDM 5–6). Rq ≈ 1.11×Ra. — [MetricMech](https://metricmech.com/reference/surface-finish-chart); [Bal Seal](https://www.balseal.com/wp-content/uploads/2022/03/Measuring_Surface_FinishesTR_51-1.pdf)
- Cost scaling: Ra ≥3.2 baseline; 0.8–1.6 → 1.5–2×; 0.4–0.8 → 3–4×; 0.1–0.4 → 5–8×; ≤0.1 → 10×+. — [MetricMech](https://metricmech.com/reference/surface-finish-chart); [Ideambox](https://ideambox.com/assets/downloads/surface-finish-reference.pdf)
- Functional targets: dynamic seal/O-ring sliding 0.1–0.4; static seal groove 0.8–1.6; sliding/journal bearing 0.2–0.8; fatigue-critical ≤0.4; press/interference fit 0.4–1.6; mating/clamping/gasket 1.6–3.2; general non-critical 1.6–6.3; paint/adhesion 1.6–6.3. — [Ideambox](https://ideambox.com/assets/downloads/surface-finish-reference.pdf)
- Surface finish affects dimensions: combined profile height ≈4×Ra; tolerance on diameter should be ≥4×Ra or roughness can exceed tolerance. — [Bal Seal](https://www.balseal.com/wp-content/uploads/2022/03/Measuring_Surface_FinishesTR_51-1.pdf)
- Units: 1 µm = 39.37 µin; always specify unit on drawing (ISO 1302). — [MetricMech](https://metricmech.com/reference/surface-finish-chart); [Bal Seal](https://www.balseal.com/wp-content/uploads/2022/03/Measuring_Surface_FinishesTR_51-1.pdf)
- Machining tolerance note: surface scale on castings is harder; reduce speed 5–10%. — [Machinery's Handbook 31st ed.](https://online.flippingbook.com/view/954192180/1233/)

### Inferences
- For a small shop, default to Ra 3.2 µm (N8) general, Ra 1.6 µm (N7) for bearing/seal surfaces, and grinding only where function demands <0.8 µm.

### Gaps
- Diamond turning (0.025–0.1 µm) requires ultra-precision machines not typical of small shops; treat as special process.

## Tolerances Achievable

### Takeaway
Tolerance is a cost driver: rough machining ±0.1 mm, finish machining ±0.025 mm, grinding ±0.005 mm, lapping ±0.001 mm. Process capability from Kalpakjian confirms turning/boring/drilling/milling ranges; tighter needs secondary operations.

### Cited Findings
- User/shop targets: rough machining ±0.1 mm, finish machining ±0.025 mm, grinding ±0.005 mm, lapping ±0.001 mm. — [Assignment brief]
- Kalpakjian process characteristics (± mm): turning fine 0.05–0.13, rough 0.13, skiving 0.025–0.05; boring 0.025; drilling 0.075; milling 0.13–0.25; planing 0.08–0.13; shaping 0.05–0.13; broaching 0.025–0.15; sawing 0.8. — [Kalpakjian, Common Machining Processes](https://ocw.sumdu.edu.ua/system/collection_nodes/blobs/000/109/608/original/Common_Machining_Processes.pdf)
- Hole-making tolerances: drilling ±0.05–0.15 mm; reaming ±0.005–0.02 mm; boring ±0.005–0.01 mm; gun drilling ±0.01–0.05 mm. — [Sinbo](https://www.sinbo-machining.com/wiki/dfm/hole-design)
- Default drawing tolerance ±0.005 in (±0.13 mm) or ISO 2768-m. — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)
- ISO 2768 medium/fine general tolerances commonly used; tighter than ±0.025 mm usually requires grinding or honing. — [SSG MFG](https://ssgmfg.com/design-guides/cnc-machining)

### Inferences
- Design to ±0.13 mm (ISO 2768-m) as default; reserve ±0.025 mm for fits/datums; grinding only for <±0.01 mm.

### Gaps
- No sourced tolerance for tapping or threading beyond engagement depths; thread pitch tolerance depends on standard (ISO metric thread tolerances).

## Fixturing

### Takeaway
Fixturing determines achievable accuracy and speed: vises for prismatic parts, collets for round stock (0.0002" TIR), chucks for larger/odd rounds, custom fixtures for production. Rigidity and access for tools are as important as holding force.

### Cited Findings
- Workholding definition: locate and secure workpiece against machining forces without deforming it; repeatable setups are ideal. — [Reid Supply](https://www.reidsupply.com/en-us/industry-news/introduction-to-workholding-solutions)
- Milling workholding: vises (most basic, hard/soft/step jaws), T-slot clamps, fixture plates, parallels, V-blocks, angle plates. Lathe: 3-jaw (self-centering, round/hex), 4-jaw (independent, eccentric/irregular), collet chucks, magnetic chucks. — [Reid Supply](https://www.reidsupply.com/en-us/industry-news/introduction-to-workholding-solutions)
- Vise: best for blocks/plates/rectangular parts; fast setup; high force; 0.0005" repeatability; 5–15 min setup; jaw options hard/soft/step. — [Rivcut](https://www.rivcut.com/blog/cnc-workholding-methods)
- Soft jaws: milled/3D-printed to cradle odd geometry and round objects; avoid diameter variation and uneven pressure. — [Autodesk Fusion blog](https://www.autodesk.com/products/fusion-360/blog/understanding-the-top-10-cnc-fixturing-types/)
- Collets: even pressure all around; best for round bar; 0.0002" TIR or better; each fits one size; common on CNC lathes and 5C/R8. — [Rivcut](https://www.rivcut.com/blog/cnc-workholding-methods)
- Chucks: 3-jaw scroll centers round parts automatically (0.001–0.003" TIR); 4-jaw independent for square/odd shapes; 6-jaw; wider size range than collets but less even grip. High-precision shops start with chuck, finish with collet. — [Rivcut](https://www.rivcut.com/blog/cnc-workholding-methods)
- Clamps/toe clamps: bolt to table/fixture plate; press down/side; for large/odd parts; slower setup; watch clamp marks and tool clearance. — [Rivcut](https://www.rivcut.com/blog/cnc-workholding-methods)
- Vacuum tables: suction for thin flat parts; ~14 psi holding force; no clamps in tool path; cannot hold porous materials (cast iron, some plastics); light cuts only. — [Rivcut](https://www.rivcut.com/blog/cnc-workholding-methods)
- Custom fixtures: built for one part; ROI breakeven usually 20–50 parts; high upfront cost. — [Rivcut](https://www.rivcut.com/blog/cnc-workholding-methods)
- Tombstones/trunnions (4/5-axis): multi-face access and high part counts; low-profile fixturing essential for 5-axis tool clearance. — [Defusco](https://www.defusco.com/cnc-workholding-fixtures/)
- Vacuum cannot hold porous materials; air leaks break seal. — [Rivcut](https://www.rivcut.com/blog/cnc-workholding-methods)
- Tool access: pocket depth, holder clearance, and clamps must not obstruct toolpath; use parallels to lift part for through-drilling. — [Reid Supply](https://www.reidsupply.com/en-us/industry-news/introduction-to-workholding-solutions); [Rivcut](https://www.rivcut.com/blog/cnc-workholding-methods)
- 5C collets range 1/16" to 1"; expanding mandrels for internal-bore holding with full OD access. — [Autodesk Fusion blog](https://www.autodesk.com/products/fusion-360/blog/understanding-the-top-10-cnc-fixturing-types/); [Defusco](https://www.defusco.com/cnc-workholding-fixtures/)

### Inferences
- For a small shop, a quality milling vise with soft jaws plus a 5C collet block covers most prismatic and round work; add custom fixtures only for repeat jobs.

### Gaps
- No sourced clamping-force magnitudes or torque values beyond "use torque wrench for consistent clamping." — [Rivcut](https://www.rivcut.com/blog/cnc-workholding-methods)