# timing_belt

**Type:** mechanism
**Function:** Provide synchronous, backlash-free power transmission between shafts via toothed belt and pulleys.

## How it works
Toothed (cogged) belt meshes with toothed pulleys; no slip, so speed ratio is exact. Used where timing/positioning must be precise (camshaft drives, CNC, 3D printers).

## Key dimensions / equations
- Speed ratio = pulley tooth counts (exact, no slip).
- Backlash-free by tooth mesh; tension affects meshing but not ratio.
- Pitch (tooth spacing) standardized by belt family.

## Constraints
- Requires tensioning; over-tension damages bearings.
- Belt and pulley must match tooth profile.
- Less tolerant of misalignment than V-belt.

## Failure modes
- Tooth shear/strip if overloaded.
- Belt stretch over time affecting tension.
- Pulley wear causing backlash.

## When to use
Camshaft drives, CNC/3D-printer axes, synchronous positioning, precision motion.

## DFM (small workshop)
Use standard belt/pulley sets (HTD, GT2, etc.), include tensioner, keep runs straight.

## Sources
cams_and_gears.md