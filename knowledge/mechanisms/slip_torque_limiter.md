# slip_torque_limiter

**Type:** coupling
**Function:** Slip at a preset torque and automatically re-engage when torque drops.

## How it works
Frictionally engaged surfaces slip when torque exceeds set value; torque adjustable via spring load. Auto re-engages when torque falls.

## Key dimensions / equations
- Setting torque >= ~1.3 x max operating torque (typical).
- Slip torque range (e.g., 0.5-12,000 Nm vendor).
- Wear/heat during slipping.

## Constraints
- Wear and heat during slip.
- Re-engages at reduced speed for high inertia.
- Needs monitoring.

## Failure modes
- Lining wear.
- Overheating.
- Spring fatigue.

## When to use
Packaging, printing, conveyors, machine tools.

## DFM (small workshop)
Use commercial units; set above normal torque; provide cooling/ventilation.

## Sources
couplings_power_transmission.md