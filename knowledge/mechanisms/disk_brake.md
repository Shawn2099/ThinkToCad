# disk_brake

**Type:** brake
**Function:** Absorb kinetic energy by friction between pads and a rotating disk/rotor.

## How it works
Pads pinch a rotating disk (rotor) via caliper; friction converts kinetic energy to heat. Disc brakes reject heat well (vented rotors) and resist fade better than drums.

## Key dimensions / equations
- Braking torque T = mu*F_clamp*r_eff (r_eff ~ mean pad radius).
- Braking power P = T*omega.
- Temperature rise DeltaT = Q/(m*c) (Q absorbed energy, m mass, c specific heat).
- Kinetic energy K = 1/2*m*v^2; braking distance scales with v^2.

## Constraints
- Requires hydraulic/pneumatic/mechanical actuation.
- Pad and rotor wear; needs replacement.
- Heat management critical for duty.

## Failure modes
- Fade from overheating.
- Pad glazing/wear.
- Rotor warping/cracking from thermal stress.

## When to use
High-duty braking, machinery stops, vehicles, test rigs.

## DFM (small workshop)
Use cast-iron vented rotor, bolted pads, keep surfaces flat within 0.05 mm, provide ventilation.

## Sources
clutches_brakes_couplings_indexing.md