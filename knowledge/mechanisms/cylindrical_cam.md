# cylindrical_cam

**Type:** mechanism
**Function:** Convert cam rotation into linear (or programmed) follower motion parallel to the camshaft axis using a grooved cylinder.

## How it works
Follower rides in a groove cut into a rotating cylinder (barrel). Can be form-closed (positive positioning, no spring) and implement multi-rotation programs; constant-lead variant gives displacement proportional rotation (like a lead screw).

## Key dimensions / equations
- Displacement proportional to rotation for constant-lead: x = (lead/360deg)*theta.
- Can encode arbitrary multi-rotation programs via groove profile.
- Pressure angle limits apply (<=30deg translating / <=35deg rotating).

## Constraints
- Groove must be machinable; undercutting risk.
- Form-closed needs precision groove; force-closed needs spring.
- Manufacturing more complex than plate cam.

## Failure modes
- Groove wear and follower seizure.
- Binding at high pressure angle.
- Debris ingress in groove.

## When to use
Shift barrels, machine-tool drives, multi-step indexing, positive-positioning programs.

## DFM (small workshop)
Use simple constant-lead or stepped grooves; harden cam and follower; seal against chips.

## Sources
cams_and_gears.md