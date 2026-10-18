# slider_crank

**Type:** mechanism
**Function:** Convert rotary crank motion into reciprocating (linear) slider motion.

## How it works
Three revolute + one prismatic joint (RRRP). Crank rotates about fixed pivot; connecting rod links crank pin to slider; slider reciprocates along a straight guide. In-line when slider travel line passes through crank pivot; offset otherwise.

## Key dimensions / equations
- Piston displacement from TDC: x = r cos alpha + sqrt(l^2 - r^2 sin^2 alpha), where r = crank radius, l = connecting-rod length, alpha = crank angle from TDC.
- Approximate (l >> r): x ~ r cos alpha + l.
- Torque tau = F r sin(alpha+beta).
- Design rule: crank = stroke/2; connecting rod l >= 3*crank radius.
- Offset design: L1 = S*[sin theta_M sin(theta_M-beta)/sin beta]; L2 = S*[(sin theta_M - sin(theta_M-beta))/(2 sin beta)]; L3 = S*[(sin theta_M + sin(theta_M-beta))/(2 sin beta)].

## Constraints
- Requires rigid slider guide; alignment critical.
- Secondary imbalance from finite l/r; balance shafts for high speed.
- Cannot start from rest at TDC/BDC under connecting-rod force (locomotive wheels staggered).

## Failure modes
- Guide wear and seizure.
- Connecting-rod buckling under compression.
- Bearing wear at crank pin and wrist pin.

## When to use
Engines, compressors, pumps, presses, reciprocating actuators.

## DFM (small workshop)
Use bronze bushings at pins, keep l/r >= 3, provide oil lubrication, avoid over-speed.

## Sources
linkages.md