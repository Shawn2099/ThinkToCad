# drum_brake

**Type:** brake
**Function:** Absorb energy by pressing shoes against the inner surface of a rotating drum.

## How it works
Shoes (lined) press outward against drum inner surface; friction converts kinetic energy to heat. Cheaper but wears faster and overheats more than disc brakes.

## Key dimensions / equations
- Torque T = mu*F_shoe*r_drum*(number of shoes) with leading/trailing shoe factors.
- Leading shoe self-energizes (force multiplication).
- Power P = T*omega; temperature rise DeltaT = Q/(m*c).

## Constraints
- Overheats faster than disc; fade-prone.
- Shoe adjustment needed as lining wears.
- Drum must be round and true.

## Failure modes
- Fade from overheating.
- Lining wear and uneven contact.
- Drum scoring/cracking.

## When to use
Low-duty holding/parking brakes, low-cost applications.

## DFM (small workshop)
Use for parking/holding; vented drums if duty higher; check leading-shoe factors per textbook.

## Sources
clutches_brakes_couplings_indexing.md