# dog_clutch

**Type:** clutch
**Function:** Provide positive, no-slip engagement for low-speed or indexed motion.

## How it works
Interlocking teeth (dogs) on two hubs engage/disengage axially. No slip when engaged; engagement under load causes impact. Used in non-synchronous transmissions and indexing.

## Key dimensions / equations
- Torque capacity limited by tooth shear: tau = T/(r*pid^2/4) (pin/tooth) with safety factor.
- Engagement speed should be low or synchronized.
- Chamfers/lead-ins reduce impact.

## Constraints
- Engagement under load causes impact; limit speed/inertia.
- Cannot slip; overload causes breakage.
- Requires axial actuation.

## Failure modes
- Tooth chipping/breakage from impact.
- Wear from repeated engagement.
- Misalignment causing partial engagement.

## When to use
Indexing, PTO, low-speed positive drives, gear selection.

## DFM (small workshop)
Use hardened teeth, chamfers, limit engagement speed, add inertia control.

## Sources
clutches_brakes_couplings_indexing.md