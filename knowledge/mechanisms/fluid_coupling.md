# fluid_coupling

**Type:** coupling
**Function:** Transmit torque hydrodynamically via an impeller and turbine in oil for smooth, wear-free starts.

## How it works
Input impeller accelerates fluid; fluid drives output turbine. Torque transfer is smooth; slip allows speed difference. Torque multiplication ~2:1 basic; torque converters add a stator for more.

## Key dimensions / equations
- Torque transmitted ~ rho * n^2 * D^5 (scaling) (vendor curves).
- Slip speed = input - output speed.
- Efficiency rises with speed ratio; losses at low ratio.

## Constraints
- Slip generates heat; needs cooling.
- No fixed ratio; speed-dependent.
- Bulky and oil-filled.

## Failure modes
- Overheating from sustained slip.
- Seal/leakage.
- Fluid degradation.

## When to use
High-inertia starts, soft starts, automatic transmissions (with torque converter).

## DFM (small workshop)
Use commercial units; provide cooling and proper fluid; align carefully.

## Sources
springs_clutches_brakes.md