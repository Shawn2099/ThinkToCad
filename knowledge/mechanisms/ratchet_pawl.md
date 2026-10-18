# ratchet_pawl

**Type:** mechanism
**Function:** Allow motion in one direction while preventing reverse motion.

## How it works
Ratchet wheel with asymmetric teeth; an oscillating lever carries a driving pawl that pushes the wheel forward on the power stroke and slides over teeth on the return, while a holding pawl prevents backward motion. Spring holds pawls against wheel.

## Key dimensions / equations
- Design rule: common normal at contact point N must pass between pawl and wheel centers; otherwise pawl forced out of contact under load.
- Backlash <= tooth spacing; minimize with fine pitch.
- Reversible pawl needs modified tooth shape for drive in either direction.

## Constraints
- Pawl spring must maintain contact; spring fatigue risk.
- Tooth wear reduces accuracy over time.
- Backlash limited by tooth pitch.

## Failure modes
- Pawl forced out of contact if common normal outside limits.
- Tooth/pawl wear and chipping.
- Spring fatigue or loss of preload.

## When to use
Jacks, socket wrenches, cable ties, seatbelts, anti-rollback, feed mechanisms.

## DFM (small workshop)
Harden teeth and pawl, use standard spring, add lubrication, keep pitch fine for low backlash.

## Sources
linkages.md