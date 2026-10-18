# v_belt

**Type:** mechanism
**Function:** Transmit power between shafts via a wedged belt on sheaves, using friction amplified by wedge action.

## How it works
Belt with trapezoidal cross-section sits in V-grooved sheaves; wedge shape increases normal force and friction, allowing higher torque before slip. Installed by reducing center distance then tensioning (never roll onto sheave).

## Key dimensions / equations
- Speed ratio omega_1/omega_2 = D_2/D_1 (slip negligible).
- Wrap angle = 180deg - 2*arcsin((D-d)/(2C)); keep small-sheave wrap >= 120deg.
- Belt speed: avoid <1000 ft/min (use chains) or >6500 ft/min (instability).
- Max reduction: 6:1 plain V-belt, 7:1 cogged.
- Profiles: classical (A,B,C,D), narrow (3V,5V,8V), cogged (AX,BX,5VX) with 2-3% efficiency gain.

## Constraints
- Requires adjustable center distance for tensioning.
- Misalignment scrubs sidewalls (heat); under-tension -> slip/glazing; over-tension -> bearing damage.
- Matched sets for multi-groove drives.

## Failure modes
- Slip and glazing from low tension.
- Sidewall wear from misalignment.
- Cord breakage if rolled onto sheave.

## When to use
Motor-to-shaft power in workshops; cheap, forgiving alignment.

## DFM (small workshop)
Include adjustable motor mount/tensioner; align with straightedge; use standard profiles and off-the-shelf sheaves.

## Sources
cams_and_gears.md