# welded_joint

**Type:** joint
**Function:** Permanently join metal parts by fusion, with strength depending on weld type and inspection level.

## How it works
Base metal is melted and fused (often with filler) to form a joint. Butt welds distribute load uniformly (higher efficiency); fillet welds act in shear along the throat and tolerate more fit-up variation.

## Key dimensions / equations
- Joint efficiency E = strength of joint / strength of base material.
- Double-welded (or equivalent) butt joint: 1.00 (full NDE) / 0.85 (spot) / 0.70 (none).
- Single-welded butt with backing strip: 0.90 / 0.80 / 0.65.
- Single-welded butt without backing strip: 0.60 (not inspected).
- Double full-fillet lap: 0.55; single full-fillet lap with plug welds: 0.50; without plug welds: 0.45.

## Constraints
- Fillet welds should be derated (~0.45-0.55) for structural/pressure calculations.
- Requires proper fit-up, access, and skill.
- Inspection (NDE) affects allowable efficiency.

## Failure modes
- Fatigue at weld toe/root under cyclic load.
- Lack of fusion/penetration.
- Distortion and residual stress.

## When to use
Permanent load paths, frames, pressure vessels, heavy structures.

## DFM (small workshop)
Prefer fillet welds for convenience but derate; use butt welds with full penetration for primary load paths; bolt where disassembly needed.

## Sources
joints_fasteners_bearings_springs.md