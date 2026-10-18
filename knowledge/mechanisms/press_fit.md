# press_fit

**Type:** joint
**Function:** Join parts by interference fit (shaft in hole) relying on elastic deformation and friction.

## How it works
A shaft (or pin) is pressed into a slightly smaller hole; interference creates radial pressure and friction that resists axial/rotational loads. Assembly by pressing or thermal expansion (shrink fit).

## Key dimensions / equations
- Common tolerance zones: h7/p6, h7/s6 (light interference).
- Thermal expansion sizing: DeltaT ~ interference / (alpha*d).
- Fit selection per ISO 286 (H7/h6 common tight fit).

## Constraints
- Requires accurate diameters and surface finish.
- Assembly force can damage parts; use chamfers and lubrication.
- Disassembly difficult; may need heating/press.

## Failure modes
- Fretting wear under cyclic load.
- Cracking of hub if interference too high.
- Seizure/galling during assembly.

## When to use
Bearings on shafts, gears on shafts, pins, permanent assemblies.

## DFM (small workshop)
Use light interference (h7/p6), chamfer entries, lubricate, heat hub/cool shaft for assembly.

## Sources
joints_fasteners_bearings_springs.md