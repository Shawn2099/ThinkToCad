# Manufacturing Processes and Design-for-Manufacturing (DFM) for Mechanical Design

## Machining (turning, milling, drilling, boring, grinding, EDM)

### Takeaway
Machining cost is dominated by setup time, number of part orientations, and tolerance; design should minimize operations, keep tool aspect ratios within limits, use standard stock, and reserve EDM for finishing small features.

### Cited Findings
- CNC cost is driven by time including setup, fixturing, programming, and load/unload; unless 4th/5th axis is used a CNC can only approach the part from one direction, so each side requires a separate operation (flip) — [Wikipedia: Design for manufacturability (CNC machining)](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- A part with 5 operations at 1.5 h setup each but only 30 min total machine time incurs 7.5 h of charge; volumes of 100–300 amortize setup into the noise — [Wikipedia: Design for manufacturability (CNC machining)](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Easiest metals to machine are aluminum and brass; steel, stainless steel, titanium, and exotic alloys are much harder and slower — [Wikipedia: Design for manufacturability (CNC machining)](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Bar stock is generally about half the cost of plate per pound for aluminum — [Wikipedia: Design for manufacturability (CNC machining)](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Specify the loosest tolerance that serves function; tighter tolerances raise cost — [Wikipedia: Design for manufacturability (CNC machining)](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- For milling cutters an L:D ratio of 3:1 or under is optimum; for holes keep L:D under 10:1 — [Wikipedia: Design for manufacturability (CNC machining)](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Chamfers cost less than radii on outer horizontal edges; 3D-interpolated radii on non-coplanar edges incur ~10× cost; undercuts and smaller tools are more expensive — [Wikipedia: Design for manufacturability (CNC machining)](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- EDM can machine hard metals and very complex shapes; the wire diameter must be less than double the minimum internal corner radius (high-tensile brass wire 0.006 in; steel-core/Mo 0.002–0.004 in; W 0.0008–0.002 in) — [Wikipedia: Rule-based DFM analysis for EDM](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_electric_discharge_machining).
- In EDM, through holes are preferred to blind holes for dielectric flow; sharp corners should be avoided (slight overcut/undercut); relax surface finish to reduce passes; remove bulk stock by conventional machining and finish with EDM; stack parts for simultaneous machining — [Wikipedia: Rule-based DFM analysis for EDM](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_electric_discharge_machining).

### Inferences
- For a small workshop without CNC, manual machining favors simple 2.5D features, generous radii, and loose tolerances; EDM is generally unavailable, so avoid undercuts and tiny internal corners.
- Tool access and part stiffness, not just nominal tolerances, drive achievable accuracy.

### Gaps
- No cited data on typical grinding tolerances/finishes or turning-specific aspect ratios; unverified in this research.

## Casting (sand, die/investment)

### Takeaway
Casting favors near-net shapes with draft, uniform wall thickness, generous fillets, and adequate radii; sand casting is cheap/flexible but rough, die casting is high-volume/precision, investment casting gives the best surface/accuracy at higher cost.

### Cited Findings
- Sand casting: a slight taper (draft) must be used on surfaces perpendicular to the parting line for pattern removal; cores should be avoided when possible due to extra setup/cost; risers/gating control flow; gas pockets cause internal voids — [Wikipedia: Sand casting (design requirements)](https://en.wikipedia.org/wiki/Sand_casting).
- Sand casting mold sand characteristics include refractoriness, permeability, surface finish, cohesiveness, collapsibility; facing sand 30–100 mm thick — [Wikipedia: Sand casting (mold materials)](https://en.wikipedia.org/wiki/Sand_casting).
- Investment casting: almost any castable metal; size 3 g to several hundred kg; tolerance 0.1 mm for first 25 mm plus 0.02 mm per added cm; surface finish 1.3–4 μm RMS; holes cannot be smaller than 1/16 in and no deeper than ~1.5× diameter — [Wikipedia: Investment casting (details/disadvantages)](https://en.wikipedia.org/wiki/Investment_casting).
- Die casting: minimum sections 0.63 mm (Zn), 0.89 mm (Al), 1.27 mm (Mg, brass/bronze); minimum draft 1:200 (Zn), 1:100 (Al/Mg), 1:80 (brass/bronze); thickest section should be <13 mm; draft on all surfaces parallel to die opening direction; bosses need uniform wall thickness; ribs add strength without added wall thickness — [Wikipedia: Die casting (design geometry/cast metal)](https://en.wikipedia.org/wiki/Die_casting).
- Die casting: high pressure (10–175 MPa) fills thin sections quickly but entraps air; vents along parting lines; standard process leaves some porosity, so no heat treat/weld unless pore-free/vacuum variants — [Wikipedia: Die casting (process/disadvantages)](https://en.wikipedia.org/wiki/Die_casting).
- Die casting shrinkage/porosity: yield ~67%; discontinuities avoided by rapid fill; misruns/cold shuts from cold dies, low metal temp, dirty metal, lack of venting, excess lubricant — [Wikipedia: Die casting (process/inspection)](https://en.wikipedia.org/wiki/Die_casting).
- Casting contraction allowance: pattern must be slightly larger than finished part due to solidification shrinkage; cores create undercuts/cavities — [Wikipedia: Sand casting (patterns)](https://en.wikipedia.org/wiki/Sand_casting).

### Inferences
- For small workshop metal casting (sand), avoid cores and deep narrow pockets, add draft, and expect machining of critical surfaces.
- Die casting is only economical at high volume due to capital cost.

### Gaps
- No cited draft-angle numeric ranges for sand/investment casting specifically; unverified in this research.

## Forging (open/closed die, flash, tolerances)

### Takeaway
Forging yields denser, stronger parts than casting; closed-die forging needs draft (Al ≥3°, steel 5–7°), generous fillets/radii, low wide ribs, single flat parting plane, and tolerances grouped by feature type; flash aids die filling.

### Cited Findings
- Forging produces denser microstructure, more defined grain patterns, less porosity than casting; all solid metals/alloys forgeable with forgeability rating — [Wikipedia: Rule-based DFM analysis for forging](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_forging).
- Open-die: cylindrical billet upset between flat dies; closed-die (impression): dies with cavity, flash gutter creates flash that promotes die filling — [Wikipedia: Rule-based DFM analysis for forging](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_forging).
- Hot forging: lower yield strength/force, higher ductility, but less precise tolerances from thermal contraction/warping; cold forging: better surface finish, dimensional control, reproducibility, but higher forces/heavier tooling — [Wikipedia: Rule-based DFM analysis for forging](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_forging).
- Closed-die design rules: part along single flat plane if possible; parting surface through center; draft ≥3° Al, 5–7° steel; generous fillets/radii; ribs low and wide; balanced sections; tolerances not closer than necessary — [Wikipedia: Rule-based DFM analysis for forging](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_forging).
- Flash can account for 20–45% of starting material; flashless forging saves material but needs complex die/better lubrication/placement — [Wikipedia: Rule-based DFM analysis for forging](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_forging).
- Upset forging rules: unsupported length upset in one blow limited to 3× diameter; lengths >3× diameter may be upset if upset diameter ≤1.5× stock diameter; otherwise unsupported metal beyond die face ≤ diameter — [Wikipedia: Rule-based DFM analysis for forging](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_forging).
- Automatic hot forging: tolerances usually ±0.3 mm, draft 0.5–1°, no flash, 20–30% material savings vs conventional forging, rates up to 180 ppm — [Wikipedia: Rule-based DFM analysis for forging](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_forging).
- Precision/net-shape forging: minimal/no machining, less draft 1° to 0°, but costly — [Wikipedia: Rule-based DFM analysis for forging](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_forging).

### Inferences
- For a small shop, hand/blacksmith forging is open-die only; closed-die forging needs capital tooling and is for volume.

### Gaps
- Specific tolerance tables by group not quantified beyond categories in source; unverified numeric values not included.

## Sheet metal (bending, punching, shearing, deep drawing, hemming)

### Takeaway
Sheet-metal design must account for bend radius, K-factor/springback, bend deduction/allowance, die/punch radii, and drawing ratios; keep bends consistent and avoid sharp internal corners.

### Cited Findings
- Bending: air bending angle accuracy ~±0.5°; V-opening width 6T for ≤3 mm sheet to 12T for ≥10 mm; bottoming bend radius must be ≥0.8T–2T for sheet steel; coining can reach 0.4T radius with 5T V opening — [Wikipedia: Bending (metalworking)](https://en.wikipedia.org/wiki/Bending_\(metalworking\)).
- K-factor ranges 0.3–0.5 depending on material/process; rule-of-thumb table by radius/material for air/bottoming/coining — [Wikipedia: Bending (metalworking)](https://en.wikipedia.org/wiki/Bending_\(metalworking\)).
- Bend allowance BA = A(π/180)(R+K·T); bend deduction BD = 2(R+T)tan(A/2)−BA — [Wikipedia: Bending (metalworking)](https://en.wikipedia.org/wiki/Bending_\(metalworking\)).
- Springback requires over-bending; neutral axis location is empirical — [Wikipedia: Bending (metalworking)](https://en.wikipedia.org/wiki/Bending_\(metalworking\)).
- Deep drawing: material needs good formability/ductility and low yield strength; clearance > thickness but not excessive (avoid wrinkling); die corner radius 5–10× thickness; punch corner radius 4–10× thickness; drawing ratio (blank dia/punch dia) usually ≤2 — [Wikipedia: Rule-based DFM analysis for deep drawing](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_deep_drawing).
- Hemming/seaming available as sheet-metal joining (see bending article "See also") — [Wikipedia: Bending (metalworking)](https://en.wikipedia.org/wiki/Bending_\(metalworking\)).

### Inferences
- For small workshop bending with hand brake/press, use generous radii, avoid tight tolerances, and design flat patterns with standard K-factor approximations; deep drawing needs dedicated dies and is not frugal.

### Gaps
- No cited punching/shearing/hemming DFM rules beyond bending; unverified.

## Welding (arc, MIG, TIG, spot, friction stir)

### Takeaway
Welding joins by melting (or solid-state); design for access, joint geometry, distortion control, and HAZ; solid-state (friction stir) reduces HAZ and distortion but needs machine access and tooling.

### Cited Findings
- Welding processes: gas, arc (SMAW stick, GMAW MIG, FCAW, GTAW TIG, SAW), resistance/spot, energy beam (laser, electron beam), solid-state (friction, friction stir, cold, diffusion) — [Wikipedia: Welding](https://en.wikipedia.org/wiki/Welding).
- Arc welding uses shielding gas/flux to protect weld pool; GMAW (MIG) uses continuous wire and inert/semi-inert gas for higher speed; SMAW uses coated consumable electrode with slag removal — [Wikipedia: Welding](https://en.wikipedia.org/wiki/Welding).
- Solid-state welding joins with pressure without melting; friction stir welding invented 1991 at TWI — [Wikipedia: Welding](https://en.wikipedia.org/wiki/Welding).
- HAZ: zone where base metal not melted but microstructure altered by heat; weld distortion and residual stresses increase with slower cooling (oxy-fuel) — [Wikipedia: Welding](https://en.wikipedia.org/wiki/Welding).
- Welding hazards require PPE; joint geometry and access affect quality — [Wikipedia: Welding](https://en.wikipedia.org/wiki/Welding).

### Inferences
- Small shop: SMAW (stick) is cheapest/versatile for ferrous field work; MIG for speed; TIG for precision/thin; spot welding for sheet assemblies; friction stir uncommon (needs machine).
- Design parts to allow torch access, minimize distortion (symmetric welds, clamping, heat sinking), and avoid welding through porosity-prone castings.

### Gaps
- No cited quantitative distortion/HAZ size values; unverified.

## Additive manufacturing (FDM, SLA, SLS, metal DMLS/SLM)

### Takeaway
AM removes tooling and allows complexity, but each process has orientation, support, anisotropy, and minimum-feature limits; design for build orientation and reduce supports.

### Cited Findings
- DMLS: min sintering width 0.6–0.9 mm defines min external feature; support structures needed for downward surfaces <45°; overhangs <45° should be avoided; weaker properties along build direction (anisotropy); max build size ~228×228×304 mm; accuracy depends on 50–100 μm powder and 0.02–0.05 mm layers; orient to minimize height along build direction; complexity adds no cost — [Wikipedia: Rule-based DFM analysis for DMLS](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_direct_metal_laser_sintering).
- SLA: min wall thickness (supported/unsupported), overhang max unsupported length/min unsupported angle, max bridge span, min vertical pillar diameter, min groove/emboss dimensions, min clearance, min hole diameter/curvature, min internal volume; supports needed for shallow angles; typical support-free threshold ~45°; orientation affects finish/time/supports — [Wikipedia: DFM analysis for stereolithography](https://en.wikipedia.org/wiki/DFM_analysis_for_stereolithography).
- FDM/FFF: cannot produce unsupported stalactites; overhang slope limited; layer adhesion depends on temperature; nozzle 0.3–1.0 mm; materials include PLA, ABS, PETG, nylon, PC, TPU; printing PLA at 18–25 °C, ABS needs ~60–70 °C chamber — [Wikipedia: Fused filament fabrication](https://en.wikipedia.org/wiki/Fused_filament_fabrication).
- SLS/metal AM: powder bed processes (SLS, SLM, EBM) are PM applications; metal AM growing in aerospace/biomedical/defense/automotive — [Wikipedia: Powder metallurgy](https://en.wikipedia.org/wiki/Powder_metallurgy).

### Inferences
- Small shop with FDM printer: design with 45° overhang rule, avoid supports where possible, orient for strength in horizontal plane, and expect anisotropy; reserve SLA/DMLS to service bureaus.

### Gaps
- No cited SLS-specific DFM rules (overhangs/supports for polymer SLS) in sources; unverified.

## Injection molding (draft, wall thickness, ribs, bosses, gates, ejection)

### Takeaway
Injection molding needs draft on draw-direction sides, uniform wall thickness, ribs/bosses with proper ratios, well-placed gates, and ejector-friendly geometry; mold cost rises with cavities/undercuts.

### Cited Findings
- Injection molding: molten material forced into mold cavity; molds steel/aluminum; parting line, sprue, gate marks, ejector pin marks unavoidable — [Wikipedia: Injection moulding](https://en.wikipedia.org/wiki/Injection_moulding).
- Draft on sides parallel to draw direction eases release; insufficient draft causes deformation/damage; shrinkage must be accounted — [Wikipedia: Injection moulding (mould design)](https://en.wikipedia.org/wiki/Injection_moulding).
- Features must not overhang in draw direction unless slides/lifters used; slides increase mold cost — [Wikipedia: Injection moulding (mould design)](https://en.wikipedia.org/wiki/Injection_moulding).
- Tolerance example: ±0.008 in for 1 in LDPE part with 0.125 in wall — [Wikipedia: Injection moulding (tolerances)](https://en.wikipedia.org/wiki/Injection_moulding).
- Die casting cross-over: bosses need universal wall thickness; ribs provide strength without added wall thickness; holes/windows need generous draft — [Wikipedia: Die casting (design geometry)](https://en.wikipedia.org/wiki/Die_casting).
- Defects: sink marks from thick zones/low holding; weld/knit lines where flow fronts meet; short shots from low pressure/cold mold; warping from uneven cooling; flash from damaged parting line/low clamp — [Wikipedia: Injection moulding (moulding defects)](https://en.wikipedia.org/wiki/Injection_moulding).
- Mold cost increases with cavities, complexity, surface finish, tolerance, threads, undercuts — [Wikipedia: Injection moulding (cost)](https://en.wikipedia.org/wiki/Injection_moulding).

### Inferences
- For small-batch prototypes, avoid injection molding (high mold cost); consider CNC or 3D printing.

### Gaps
- No cited specific rib/boss thickness ratios or gate types; unverified in this research.

## Other processes (extrusion, stamping, powder metallurgy)

### Takeaway
Extrusion suits constant cross-sections with uniform wall thickness; PM suits small complex metal parts with near-net shape and porosity control; stamping is high-volume sheet forming.

### Cited Findings
- Extrusion: min thickness 1 mm Al / 3 mm carbon steel; internal corners fillet min 0.5–1 mm; solid profiles cheaper/easier; fewer cavities in hollow profiles; channel width:height ~1:3 (up to 1:4 with radii); symmetry avoids die overstress; length tolerance typical ±1 mm (0.2%) on 500 mm UPVC; extrusion ratio up to 75:1 common — [Wikipedia: Rule-based analysis of extrusion process](https://en.wikipedia.org/wiki/Rule-based_analysis_of_extrusion_process).
- Powder metallurgy: press-and-sinter with 5–15% porosity; die pressing rules: max surface area <20 in², height-to-diameter <7:1, walls >0.08 in, adjacent wall ratios <2.5:1; isostatic compaction tolerances ±0.008 in axial, ±0.020 in radial; MIM for complex 95–99% dense parts; HIP for full density — [Wikipedia: Powder metallurgy](https://en.wikipedia.org/wiki/Powder_metallurgy).
- Stamping: not covered by cited sources beyond sheet-metal bending/punching; high-volume forming assumed — [Wikipedia: Bending (metalworking)](https://en.wikipedia.org/wiki/Bending_\(metalworking\)).

### Inferences
- For small workshop, extrusion is outsourced (die costs); PM is not feasible DIY.

### Gaps
- No cited stamping-specific DFM rules; unverified.

## Process selection

### Takeaway
Select process by material, geometry, tolerance, surface finish, volume, and capital; high-volume processes (die casting, injection molding, forging, stamping) amortize tooling; low-volume favors machining, casting, or AM.

### Cited Findings
- Volume effect: CNC setup amortization; die casting/injection molding high capital but low per-part; forging high initial die cost but low recurring — [Wikipedia: Design for manufacturability (CNC)](https://en.wikipedia.org/wiki/Design_for_manufacturability), [Wikipedia: Die casting](https://en.wikipedia.org/wiki/Die_casting), [Wikipedia: Injection moulding](https://en.wikipedia.org/wiki/Injection_moulding).
- Material form cost: bar stock ~ half plate per lb — [Wikipedia: Design for manufacturability (CNC)](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Process capability summary: casting for complex shapes/any metal; machining for precision/tolerances; AM for complexity/no tooling but anisotropy/supports; PM for small metal parts/near-net shape — [Wikipedia: Design for manufacturability](https://en.wikipedia.org/wiki/Design_for_manufacturability), [Wikipedia: Powder metallurgy](https://en.wikipedia.org/wiki/Powder_metallurgy), [Wikipedia: DMLS DFM](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_direct_metal_laser_sintering).

### Inferences
- Decision flow: (1) material & quantity; (2) tolerance/surface; (3) geometry complexity; (4) budget/tooling; (5) available shop equipment.

### Gaps
- No formal process-selection matrix cited; constructed from cited capabilities.

## Small workshop / frugal context

### Takeaway
With hand tools, drill press, grinder, welder: favor machining simple features, welding fabrications, sand casting (if foundry available), and FDM 3D printing; avoid processes needing capital tooling/dies.

### Cited Findings
- FDM printers low cost (<$1000 after patent expiry 2009) and accessible — [Wikipedia: Fused filament fabrication](https://en.wikipedia.org/wiki/Fused_filament_fabrication).
- Open-die forging/blacksmithing is manual and suits short runs/custom work — [Wikipedia: Rule-based DFM analysis for forging](https://en.wikipedia.org/wiki/Rule-based_DFM_analysis_for_forging).
- SMAW (stick) welding is versatile, inexpensive equipment, suited to shop/field work — [Wikipedia: Welding](https://en.wikipedia.org/wiki/Welding).
- Sand casting molds are relatively cheap and sand reusable — [Wikipedia: Sand casting](https://en.wikipedia.org/wiki/Sand_casting).

### Inferences
- A frugal AI design assistant should default to: welded sheet/plate + drilled holes + ground edges; FDM for plastic prototypes; avoid tight tolerances, undercuts, and processes requiring dies.

### Gaps
- No cited guidance on hand-tool tolerances or drill-press capabilities; unverified.
