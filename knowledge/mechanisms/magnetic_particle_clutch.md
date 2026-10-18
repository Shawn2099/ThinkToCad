# magnetic_particle_clutch

**Type:** clutch
**Function:** Provide infinitely adjustable torque via magnetic particles aligning in a cavity under a magnetic field.

## How it works
Magnetic particles in a rotor cavity align under DC excitation, creating a shear-coupling torque proportional to field strength. Allows slip operation for tensioning/positioning.

## Key dimensions / equations
- Torque proportional to coil current and particle volume.
- Slip power = T * omega_slip; heat dissipation limits duty.
- Response time depends on coil inductance.

## Constraints
- Requires electrical power and control.
- Heat buildup under continuous slip.
- Lower torque density than friction clutches.

## Failure modes
- Particle degradation/contamination.
- Coil overheating.
- Seal leakage (if wet).

## When to use
Tension control, positioning, dynamometers, soft-start.

## DFM (small workshop)
Use commercial units; provide ventilation/fusing; avoid excessive slip speed.

## Sources
springs_clutches_brakes.md