# shear_pin_coupling

**Type:** coupling
**Function:** Protect driven machinery by shearing a pin at a predetermined overload torque.

## How it works
A coupling hub and shaft connected by a shear pin; pin shears when torque exceeds design value, disconnecting drive. Replace pin to restore. Simple, cheap overload protection.

## Key dimensions / equations
- Shear capacity T = tau_all * (pid^2/4) * r (pin radius r, shear stress tau_all).
- Use safety factor per Shigley.
- Pin diameter sized for desired shear torque.

## Constraints
- Requires pin replacement after trip; downtime.
- Shear torque tolerance depends on pin material/quality.
- Not for frequent overload events.

## Failure modes
- Fatigue/shear at wrong torque if pin degraded.
- Seizure if pin doesn't shear cleanly.
- Collateral damage if trip too late.

## When to use
Pumps, gearboxes, conveyors, any expensive driven element or hazard.

## DFM (small workshop)
Use standard dowel pins of known material; size via bolt-shear formula; keep spares.

## Sources
clutches_brakes_couplings_indexing.md