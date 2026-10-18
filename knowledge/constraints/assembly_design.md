# Assembly design constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/assembly_design.md;
Boothroyd-Dewhurst, Mott, Shigley.

## Mates and constraints
- Coincident: faces/edges coincide (removes 1 DOF per plane).
- Concentric: axes align (removes 2 DOF).
- Distance/angle: fixed offset or angle.
- Screw: rotation + translation coupled (thread pitch).
- Gear/cam: motion ratio coupling.
- Weld: permanently joins (no DOF, remove for assembly).
- Flexible: allows motion (springs, hinges).
- Avoid over-constraining: each part should have exactly the DOF needed.

## Interference and clearance
- Clash detection: boolean intersection volume must be 0.
- Minimum clearance: check at worst-case tolerance stack-up.
- Motion study: verify range of motion, no collision during operation.

## Assembly tolerance
- Stack-up: worst-case (guaranteed fit, conservative) or RSS (statistical,
  ~99.73% at 3 sigma). Use worst-case for safety-critical/low-volume.
- Datum reference frames: 3-2-1 principle (primary 3 DOF, secondary 2, tertiary 1).
- Tolerance allocation: distribute assembly tolerance among components.

## Assembly methods
- Bolted: reusable, adjustable, good for maintenance. Use for disassembly.
- Riveted: permanent, vibration-resistant. Use for thin sheet, high volume.
- Welded: permanent, strong, low cost. Use for structural, no disassembly.
- Pinned: precise location, shear load. Use for alignment.
- Press-fit: torque/transmission, no fasteners. Use for bearings, gears on shafts.
- Snap-fit: no tools, fast assembly. Use for plastics, consumer products.
- Adhesive: distributes load, seals. Use for dissimilar materials, large area.

## Design for Assembly (DFA)
- Boothroyd-Dewhurst: minimize part count, ease handling/insertion.
- DFA index = (theoretical min parts * 3s) / (total assembly time).
- Target: reduce part count, standardize fasteners, design for top-down assembly.
- Handling time factors: size, weight, symmetry, nesting, tangling.
- Insertion time factors: alignment, resistance, fastening method.

## Top-down vs bottom-up
- Top-down: start with assembly, derive parts. Better for interfaces.
- Bottom-up: design parts independently, then assemble. Risk of interface mismatch.
- Prefer top-down for complex assemblies; bottom-up for standard components.

## Common pitfalls
- Over-constraining (redundant mates causing solve failures).
- Floating parts (missing mates).
- Interference not caught (no clash check).
- Tolerance stack-up not analyzed (parts don't fit at extremes).
- Assembly sequence not planned (can't assemble in real life).

## AI rules
- Always run interference check (volume = 0).
- Always check clearance at worst-case tolerance.
- Prefer top-down for new assemblies.
- Minimize part count; standardize fasteners.
- Verify assembly sequence is feasible (access for tools).