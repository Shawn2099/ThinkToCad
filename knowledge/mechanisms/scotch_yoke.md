# scotch_yoke

**Type:** mechanism
**Function:** Convert rotary motion into pure sinusoidal linear motion.

## How it works
Crank pin slides in a slot in a yoke; yoke reciprocates linearly. Pin engagement with slot converts rotation to sinusoidal displacement with no connecting-rod secondary imbalance.

## Key dimensions / equations
- x = r cos theta; stroke = 2r.
- v = -r omega sin theta; a = -r omega^2 cos theta.
- Torque T = p*A*d (actuator) varies with angle.

## Constraints
- Single line contact at pin/slot -> high contact pressure, wear.
- Requires lubrication; speed limited.
- Balancing needed at speed.

## Failure modes
- Pin/slot wear and seizure.
- Yoke slot elongation.
- High contact stress causing galling.

## When to use
Low-speed sinusoidal drives: compressors, valve actuators, test rigs.

## DFM (small workshop)
Harden pin and slot, provide lubrication, keep speeds low, guard moving parts.

## Sources
linkages.md