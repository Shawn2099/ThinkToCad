# planetary_gear

**Type:** mechanism
**Function:** Provide high torque density and coaxial input/output with selectable ratios via sun, planets, carrier, and ring.

## How it works
Epicyclic train: sun gear, planet gears on a carrier, and ring (annulus). Kinematic relation N_s*omega_s + N_r*omega_r = (N_s+N_r)*omega_c. Fixed-carrier ratios: carrier locked -> omega_s/omega_r = -N_r/N_s; ring locked -> omega_s/omega_c = 1+N_r/N_s; sun locked -> omega_r/omega_c = 1+N_s/N_r.

## Key dimensions / equations
- Assembly condition: (N_s + N_r)/n_p = integer.
- Torque: tau_r = tau_s*N_r/N_s; tau_c = -tau_s*(N_r+N_s)/N_s; power balance tau_romega_r+tau_comega_c+tau_somega_s=0.
- Compound planets (meshed/stepped) for larger ratios.
- Harmonic/strain-wave variant: flexspline differs by 2 teeth from circular spline -> zero backlash, high ratio.

## Constraints
- Planet count and assembly condition must be satisfied.
- Planet bearings and load sharing critical.
- Backlash control for precision.

## Failure modes
- Planet bearing failure.
- Uneven load sharing (manufacturing errors).
- Ring/sun tooth fatigue.

## When to use
Automatic transmissions, robotics, winches, high-torque compact drives, coaxial reducers.

## DFM (small workshop)
Use off-the-shelf planetary gearboxes where possible; ensure assembly condition; lubricate planets.

## Sources
cams_and_gears.md