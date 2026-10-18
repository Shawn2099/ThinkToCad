# drag_link

**Type:** mechanism
**Function:** Transmit rotation between two shafts with both side links fully rotating (double-crank).

## How it works
Four-bar linkage where the shortest link is the ground (frame); both ground-connected side links (cranks) rotate fully. The floating coupler "drags" between them, giving two full rotations per cycle.

## Key dimensions / equations
- Grashof: S + L <= P + Q with shortest link = ground (frame).
- Both side links fully rotate; coupler motion is complex (non-simple).
- Common drive ratio 1:1 (equal crank lengths) or varied.

## Constraints
- Requires rigid frame; coupler must clear both cranks.
- Timing/phase between shafts fixed by link lengths.
- mu_min >= 40-45deg to avoid binding.

## Failure modes
- Coupler interference with cranks if clearances small.
- Binding at toggle positions.
- Bearing wear at four pivots.

## When to use
Windshield-wiper drives, pumpjacks, parallel shaft rotation transfer, locomotive side rods.

## DFM (small workshop)
Use matched cranks, simple pin joints, ensure coupler clearance; lubricate all four pivots.

## Sources
linkages.md