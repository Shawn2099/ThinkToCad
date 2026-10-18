# pin_joint

**Type:** joint
**Function:** Connect parts allowing relative rotation (revolute joint) while transmitting shear loads.

## How it works
A cylindrical or tapered pin passes through aligned holes in two parts, allowing rotation about the pin axis. Dowel pins provide location; clevis/cotter pins provide removable pivots.

## Key dimensions / equations
- Pin in double shear: V = 2*(pid^2/4)*tau_all.
- Fits: H7/h6 or reamed holes for dowels.
- Taper pins self-lock via taper.

## Constraints
- Pin must resist shear and bearing stress.
- Holes must be accurately aligned and reamed.
- Wear at pin/hole interface; lubricate or use bushings.

## Failure modes
- Pin shear under overload.
- Hole elongation/wear.
- Loosening of retaining (cotter/snap) ring.

## When to use
Linkage pivots, hinges, clevis connections, locating dowels.

## DFM (small workshop)
Use standard dowel/clevis pins, ream holes, add grease, retain with rings or cotter pins.

## Sources
joints_fasteners_bearings_springs.md