# gearbox

**Type:** mechanism
**Function:** Enclosed gear train that reduces speed and multiplies torque for a motor or drive.

## How it works
Input shaft drives gear train (spur, helical, planetary, worm, bevel, cycloidal, harmonic) in an enclosed, lubricated housing. Reflected inertia reduces by square of ratio.

## Key dimensions / equations
- Output speed = input speed / ratio.
- Output torque = input torque * ratio * efficiency.
- Efficiency varies by type (worm lowest, spur/helical highest).

## Constraints
- Cost, backlash, maintenance.
- Thermal limits.
- Alignment and mounting.

## Failure modes
- Gear tooth wear/pitting.
- Bearing failure.
- Lubrication breakdown.

## When to use
Robotics, conveyors, machine tools, AGVs, wind turbines.

## DFM (small workshop)
Select by ratio/torque/backlash/efficiency; use off-the-shelf reducers; maintain oil.

## Sources
couplings_power_transmission.md