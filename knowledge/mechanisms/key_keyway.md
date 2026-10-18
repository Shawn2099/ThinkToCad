# key_keyway

**Type:** fastener
**Function:** Transmit torque between shaft and hub (gear/pulley) via a key seated in matching keyways.

## How it works
A key (square, flat, Woodruff, or gib-head) fits in keyways cut in shaft and hub, preventing relative rotation. Torque transferred by shear/bearing on key sides.

## Key dimensions / equations
- Square/flat keys per standard (ASME B17.1); Woodruff keys (ASME B17.2) for shafts ~0.25-2.5 in dia.
- Gib-head (tapered) keys (DIN 6887 / BS 46) for removable hubs.
- Key shear: tau = T/(r*pid^2/4) approximated; size per standard tables.

## Constraints
- Keyway weakens shaft (stress concentration).
- Requires accurate keyway machining.
- Backlash if key loose; interference if too tight.

## Failure modes
- Key shear under overload.
- Keyway crushing/wear.
- Fretting and corrosion in keyway.

## When to use
Gears, pulleys, sprockets, couplings on shafts.

## DFM (small workshop)
Use standard square keys, machine keyways with end mills/broaches, prefer Woodruff for small shafts, add set screw for retention.

## Sources
joints_fasteners_bearings_springs.md