# electromagnetic_clutch

**Type:** clutch
**Function:** Engage/disengage remotely via an integral electromagnet, with optional smooth magnetic-particle slip.

## How it works
An electromagnet pulls friction plates together when energized; de-energized, spring disengages. Magnetic-particle type uses particles clumping under DC for smooth engagement/slippage.

## Key dimensions / equations
- Torque proportional coil current and friction interface count (vendor curves).
- Engagement time depends on coil inductance and air gap.
- Heat dissipation limits continuous slip (particle type).

## Constraints
- Requires electrical power and control.
- Torque vs. current curves vendor-specific.
- Heat buildup under slip.

## Failure modes
- Coil burnout from overvoltage/overheating.
- Wear of friction surfaces.
- Air gap change affecting engagement.

## When to use
Remote/automated engagement, motor-integrated clutches, soft-start applications.

## DFM (small workshop)
Use commercial units; ensure proper voltage/current; provide ventilation and fusing.

## Sources
clutches_brakes_couplings_indexing.md