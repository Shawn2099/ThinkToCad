# double_rocker

**Type:** mechanism
**Function:** Produce bounded oscillation of both ground-connected links from a single input oscillation.

## How it works
Four-bar linkage where the link opposite the shortest is the ground; both side links (rockers) oscillate over limited angles. No link fully rotates; used where two coordinated swinging motions are needed.

## Key dimensions / equations
- Grashof: S + L <= P + Q with link opposite shortest grounded.
- Both output links rock; input is one rocker.
- Transmission angle mu: keep mu_min >= 40-45deg.

## Constraints
- No full rotation; input must be oscillatory (cam or crank with limited travel).
- Both rockers have limited angular range.
- mu_min must stay >= 40-45deg.

## Failure modes
- Binding at extreme positions.
- Backlash in pin joints amplifies positional error.
- Wear at four pivots.

## When to use
Ackermann steering, coordinated swinging linkages, where both outputs must stay bounded.

## DFM (small workshop)
Simple pin joints, standard bar stock, prototype motion range before finalizing.

## Sources
linkages.md