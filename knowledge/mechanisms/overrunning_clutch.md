# overrunning_clutch

**Type:** clutch
**Function:** Transmit torque in one direction only, freewheeling when driven shaft outruns driver.

## How it works
Special form of ratchet: spring-loaded rollers/sprags wedge between inner and outer races when driven forward, and freewheel when driven shaft spins faster. Used in starters, conveyors, PTO safety.

## Key dimensions / equations
- Engagement by wedging of rollers/sprags; torque capacity depends on spring preload and wedge angle.
- Freewheel speed differential triggers disengagement.
- Self-locking wedge angle condition (mu > tan alpha).

## Constraints
- Cannot provide engine braking (freewheels on overrun).
- Pair with separate brake if deceleration needed.
- Direction-specific; reverse requires reconfiguration.

## Failure modes
- Roller/sprag wear.
- Spring fatigue.
- Seizure from contamination.

## When to use
Conveyors, starters, PTO safety, unidirectional drives.

## DFM (small workshop)
Use sealed commercial units where possible; keep clean and lubricated.

## Sources
clutches_brakes_couplings_indexing.md