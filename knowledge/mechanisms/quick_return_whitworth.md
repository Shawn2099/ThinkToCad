# quick_return_whitworth

**Type:** mechanism
**Function:** Provide a faster return stroke than cutting stroke for reciprocating machines (shapers/slotting).

## How it works
Whitworth quick-return: crank (link 2) fixed; driving crank rotates; slider on crank pin slides in slotted bar pivoted at D; connecting rod carries ram. Cutting stroke is slower (larger angle), return stroke faster (smaller angle).

## Key dimensions / equations
- Two common types: crank-and-slotted lever (crank-shaper) and Whitworth.
- Time ratio = angle of cutting stroke / angle of return stroke (alpha/beta or beta/alpha depending on type).
- Imbalance angle beta = 180deg*(Q-1)/(Q+1).
- Shaper stroke range typically 175-900 mm.

## Constraints
- Requires rigid ram guides; alignment critical.
- Quick return increases acceleration/inertia loads.
- Geometry must avoid binding at extremes.

## Failure modes
- Ram guide wear.
- Crank-pin/slot wear.
- Vibration from acceleration discontinuity at stroke ends.

## When to use
Shapers, slotting machines, reciprocating cutters where idle time should be minimized.

## DFM (small workshop)
Use hardened crank pin and slotted bar, lubricate, keep strokes moderate, prototype timing.

## Sources
linkages.md