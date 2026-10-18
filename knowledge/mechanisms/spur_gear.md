# spur_gear

**Type:** mechanism
**Function:** Transmit power between parallel shafts with straight teeth and no axial thrust.

## How it works
Two gears with straight teeth parallel to the axis mesh; smaller member is the pinion. Gear ratio T_2/T_1 = N_2/N_1, omega_2/omega_1 = N_1/N_2. Involute profile gives constant velocity ratio and tolerates center-distance variation.

## Key dimensions / equations
- Pitch diameter d = N*m; center distance a = (m/2)(N_1+N_2); module m = p/pi.
- Standard modules: 0.1-50 (preferred list); DP = 25.4/m.
- Minimum teeth to avoid undercutting z_min = 2/sin^2phi (~17 for 20deg, ~32 for 14.5deg).
- Pressure angle phi commonly 14.5deg, 20deg, 25deg.
- Contact ratio m_c = length of action / base pitch.

## Constraints
- Noisy at high speed; pitch-line speed >? use helical above ~? (source: helical for >25 m/s).
- Pinion teeth >=~17 (20deg) to avoid undercutting.
- Backlash accumulates in trains; needs control for precision.

## Failure modes
- Pitting, scuffing, wear, root fatigue from overload/poor lubrication.
- Undercutting weakens tooth when pinion < z_min.
- Breakage from shock/overload.

## When to use
General parallel-shaft power transmission, gearboxes, clocks, workshop machines.

## DFM (small workshop)
Use standard-module off-the-shelf gears (m = 1-4), avoid pinions <18 teeth unless profile-shifted, lubricate.

## Sources
cams_and_gears.md