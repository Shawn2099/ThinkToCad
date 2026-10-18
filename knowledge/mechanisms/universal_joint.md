# universal_joint

**Type:** coupling
**Function:** Transmit power between shafts at an angle, with speed fluctuation (non-constant velocity).

## How it works
Two hinges (yokes) at 90deg connected by a cross (spider); allows angular misalignment. Output speed varies: omega_2 = omega_1*cos(beta)/(1 - sin^2(beta)*cos^2(gamma_1)). Max recommended operating angle ~15-20deg for a single joint.

## Key dimensions / equations
- Speed fluctuation: omega_2 = omega_1*cos beta / (1 - sin^2 beta * cos^2 gamma_1).
- Max recommended angle ~15-20deg single joint.
- Double Cardan (two U-joints 90deg out of phase, equal angles) acts as CV joint.

## Constraints
- Speed fluctuation causes vibration; limit angle or use paired joints.
- Needs lubrication (cross bearings).
- Not constant velocity.

## Failure modes
- Cross-bearing wear.
- Vibration at high angle/speed.
- Seizure from lubrication failure.

## When to use
Drivelines, steering columns, non-collinear shafts at moderate angles.

## DFM (small workshop)
Use standard U-joints, limit angle, lubricate, pair joints for CV where needed.

## Sources
clutches_brakes_couplings_indexing.md