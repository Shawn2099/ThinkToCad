# band_brake

**Type:** brake
**Function:** Clamp a rotating drum by wrapping a band (strap) around it.

## How it works
A band (with friction lining) wraps around a drum; tension differential across the band creates braking torque. Simple, compact, high torque; self-locking possible.

## Key dimensions / equations
- Torque T = F*r (F = band tension differential x effective radius).
- Self-locking when mu*theta >= ln(F_1/F_2) (capstan/Euler-Eytelwein); lock if mu*theta >= 1 (for F_2 -> 0).
- Wrap angle theta affects capacity.

## Constraints
- Fade and grabbiness; needs woven lining.
- Release requires overcoming self-lock (if locked).
- Heat dissipation limited.

## Failure modes
- Fade under sustained braking.
- Band wear and glazing.
- Grabbing/chatter.

## When to use
Winches, hoists, compact high-torque holding, emergency brakes.

## DFM (small workshop)
Use woven lining, generous wrap angle, vent/cool, provide release mechanism.

## Sources
clutches_brakes_couplings_indexing.md