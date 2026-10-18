# escapement

**Type:** mechanism
**Function:** Release energy from a spring/weight in regulated steps governed by an oscillator (pendulum/balance).

## How it works
An escape wheel is intermittently released by pallets driven by an oscillator; each impulse advances the wheel one tooth. True escapements release force to drive the load; main power flows through the escapement.

## Key dimensions / equations
- Types: recoil, Graham (dead-beat), Swiss lever.
- Efficiency < 50% (more than half power lost in escapement).
- Graham (dead-beat): curved locking faces -> no recoil during lock.
- Swiss lever: flat locking faces ~15deg from escape-circle radius -> "draw" (~1deg extra) to keep pallet in place.
- Optimum impulse face perpendicular to bisector; max efficiency when pallet impulse face at 90deg to halfway direction.

## Constraints
- Lock/drop/draw angles highly sensitive; small config changes cause large performance changes.
- Requires great experience for high precision.
- Low efficiency; not for power transmission.

## Failure modes
- Loss of lock (runaway) if draw insufficient.
- Excessive recoil in recoil escapements.
- Tooth/pallet wear affecting timing.

## When to use
Clocks, watches, timers, regulated stepping where timing matters.

## DFM (small workshop)
Only for timing applications; use proven geometries (Graham/Swiss lever), harden pallets/teeth, lubricate lightly.

## Sources
linkages.md