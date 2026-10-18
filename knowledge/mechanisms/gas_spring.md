# gas_spring

**Type:** spring
**Function:** Provide adjustable, near-constant force over stroke by compressing a sealed volume of gas.

## How it works
A piston compresses gas in a cylinder; force = pressure x piston area. Gas acts as the spring; an orifice/damping may be included. Force stays roughly constant over stroke.

## Key dimensions / equations
- F = p A (gas pressure times piston area).
- p V^gamma = constant (isentropic approx) for sealed gas.
- Stroke and end-of-stroke damping set by geometry.

## Constraints
- Requires seals; leakage over time.
- Temperature affects pressure/force.
- Not self-locking; needs mechanical lock if holding.

## Failure modes
- Seal leakage/loss of pressure.
- Rod bending from side loads.
- Over-pressurization or corrosion.

## When to use
Office chairs, hatches, automotive lids, adjustable supports.

## DFM (small workshop)
Use commercial gas struts; design mounts for axial load only; protect from side loads.

## Sources
springs_clutches_brakes.md