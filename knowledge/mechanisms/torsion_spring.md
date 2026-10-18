# torsion_spring

**Type:** spring
**Function:** Store energy and exert a torque when twisted about its axis.

## How it works
Coiled wire spring loaded by twisting (rotation) about its central axis; legs apply torque. Used in clothespins, hinges, counterbalances, mousetraps.

## Key dimensions / equations
- Torque T = k_theta*theta (angular rate k_theta).
- Related to helical spring rate with bending in wire; rate proportional E*d^4/(D*n_a) (approx).
- Body stress and arm deflection must be checked.
- End forms (legs) determine mounting and load direction.

## Constraints
- Legs are stress concentrators; fatigue risk.
- Must be supported to prevent buckling/bowing.
- Direction of wind matters (left/right hand).

## Failure modes
- Fatigue fracture at legs or body.
- Leg deformation.
- Permanent set if over-twisted.

## When to use
Hinges, counterbalances, ratchets, clothespins, lids.

## DFM (small workshop)
Use standard torsion springs, ensure correct wind direction, support body, avoid over-twist.

## Sources
joints_fasteners_bearings_springs.md