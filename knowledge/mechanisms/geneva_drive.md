# geneva_drive

**Type:** mechanism
**Function:** Convert continuous rotation into intermittent rotary motion with a locking dwell between steps.

## How it works
Drive wheel carries a pin that enters slots in the driven (Geneva) wheel, advancing it one step per revolution; a raised circular locking disc locks the driven wheel between steps. Minimum 3 slots; commonly 4-12.

## Key dimensions / equations
- Step angle (driven) = 360deg/n per drive revolution.
- Semi-indexing angle (driven) alpha = pi/n; (driver) beta = pi(n-2)/(2n).
- Indexing time ratio nu = beta/pi (e.g., 0.25 for 4-slot).
- Example (4-slot): R = 40 mm, centre distance a = 56.5 mm, pin radius r_p = 2.5 mm, slot width 5 mm, slot length 25 mm, shaft 15 mm.
- Design criterion: centrelines of slot and crank mutually perpendicular at engagement/disengagement.

## Constraints
- Acceleration discontinuity at engagement/disengagement -> impact/jerk.
- Requires lubrication; often enclosed in oil capsule.
- Slot count >=3; rarely >18.

## Failure modes
- Impact wear at slot entry/exit.
- Pin breakage from shock.
- Locking-disc wear causing backlash.

## When to use
Film projectors, indexing tables, CNC turrets, dial indicators, automatic machinery.

## DFM (small workshop)
Use hardened pins/slots, lubricate, add dwell cam or servo if smoothness required; groove-cam variant mitigates impact.

## Sources
linkages.md