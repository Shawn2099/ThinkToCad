# centrifugal_clutch

**Type:** clutch
**Function:** Automatically engage as input speed rises and disengage as it falls, without manual control.

## How it works
Shoes/pads held inward by springs; centrifugal force F_c = m*r*omega^2 swings them outward to contact the drum when speed exceeds engagement threshold. Used in small engines/scooters/chainsaws.

## Key dimensions / equations
- Engagement speed proportional sqrt(k*x/(m*r)) (spring preload k*x, mass m at radius r).
- Torque capacity grows with speed above engagement.
- Must handle slip during engagement (heat).

## Constraints
- Engagement speed set by spring preload and shoe mass/radius.
- Slip during engagement generates heat; needs cooling.
- Not for precise torque control.

## Failure modes
- Shoe wear and spring fatigue.
- Overheating from prolonged slip.
- Drum scoring.

## When to use
Small engines, scooters, chainsaws, simple automatic drives.

## DFM (small workshop)
Use replaceable shoes, vented drum, standard springs; ensure engagement speed above idle.

## Sources
clutches_brakes_couplings_indexing.md