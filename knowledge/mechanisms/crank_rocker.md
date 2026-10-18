# crank_rocker

**Type:** mechanism
**Function:** Convert continuous crank rotation into bounded rocker (oscillatory) output motion.

## How it works
Four-bar linkage where the shortest link is adjacent to ground and acts as the fully rotating input crank; the opposite side link is the output rocker that oscillates over a limited angle. Grashof condition satisfied with crank grounded adjacent to shortest.

## Key dimensions / equations
- Grashof: S + L <= P + Q; input crank is the shortest link.
- Crank length sets stroke; rocker angular range set by link lengths.
- Transmission angle mu: keep mu_min >= 40-45deg.
- Quick-return time ratio Q = (180+beta)/(180-beta) if offset/geometry imposes unequal strokes.

## Constraints
- Rocker angular travel limited by geometry; cannot exceed ~180deg in practice.
- mu_min must stay >= 40-45deg to avoid binding.
- Crank and rocker pivots need rigid supports.

## Failure modes
- Binding at extreme positions when mu -> 0deg.
- Overload if driven past rocker limits.
- Pin wear at pivots.

## When to use
Rotary-to-oscillatory tasks: windshield wipers, feed mechanisms, window cranks, pumps.

## DFM (small workshop)
Use standard bar stock, bolted pin joints with bushings, keep geometry simple and parametric for iterate-and-analyze sizing.

## Sources
linkages.md