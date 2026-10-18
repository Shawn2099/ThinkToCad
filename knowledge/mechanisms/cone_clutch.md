# cone_clutch

**Type:** clutch
**Function:** Transmit torque via friction on a conical surface, with wedging action aiding engagement.

## How it works
Friction material on outside of a conical surface; axial force creates normal force and torque. Wedging action on engagement; common as synchronizer ring in manual transmissions.

## Key dimensions / equations
- Torque T = (mu*F*r_m)/sin(alpha) (alpha = cone half-angle).
- Self-locking when mu > tan(alpha).
- Smaller axial force needed than disk clutch for same torque (wedge).

## Constraints
- Self-locking can make disengagement difficult.
- Cone angle must be chosen to avoid self-lock for controllable clutches.
- Wear changes cone angle over time.

## Failure modes
- Seizure if self-locked.
- Wear altering engagement.
- Overheating from slip.

## When to use
Synchronizers, compact clutches, low-speed engagement.

## DFM (small workshop)
Choose alpha so mu < tan(alpha) for controllable release; use replaceable lining; keep surfaces true.

## Sources
clutches_brakes_couplings_indexing.md