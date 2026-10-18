# hysteresis_brake

**Type:** brake
**Function:** Provide constant braking torque from hysteresis losses, largely independent of speed.

## How it works
Hysteresis losses in a drag cup under a magnetic field produce braking torque nearly constant across speed. Fractional power, very low wear.

## Key dimensions / equations
- Torque constant vs. speed (within range).
- Power = T * omega dissipated as heat.
- Torque set by magnet strength and cup material.

## Constraints
- Fractional power only.
- Thermal limits on continuous slip.
- Cost per torque high.

## Failure modes
- Demagnetization from heat.
- Bearing wear.
- Cup fatigue.

## When to use
Tension control, testing, low-power braking.

## DFM (small workshop)
Use commercial units; respect thermal limits; avoid shocks.

## Sources
springs_clutches_brakes.md