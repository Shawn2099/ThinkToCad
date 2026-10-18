# bell_crank

**Type:** mechanism
**Function:** Redirect force/motion through an arbitrary angle using an L-shaped (or angled) lever.

## How it works
A lever pivoted at its vertex; input on one arm produces output on the other arm at a chosen angle (90deg common). Arm-length ratio sets mechanical advantage (MA = L_out/L_in for force).

## Key dimensions / equations
- MA = L_out / L_in (force) for ideal lever.
- Pivot at vertex; angle between arms arbitrary.
- Practical limit: ratios above ~4:1 cause flex; switch to toggle or screw clamp.

## Constraints
- Pivot must resist bending; long arms flex.
- Bearing at vertex carries combined loads.
- Angle fixed by arm geometry.

## Failure modes
- Arm flex/bending at high ratios.
- Pivot wear/loosening.
- Fatigue at stress concentrations.

## When to use
Aircraft aileron runs, bicycle brakes, robot grippers, redirecting cable/rod motion.

## DFM (small workshop)
Use thick arms or triangulated gussets, quality pivot bearing, keep ratios <=4:1.

## Sources
linkages.md