# eddy_current_brake

**Type:** brake
**Function:** Provide non-contact braking torque via induced currents in a conductor moving through a magnetic field.

## How it works
A conductive disk rotates in a magnetic field; induced eddy currents create opposing torque proportional to speed and field strength. No contact wear; needs cooling.

## Key dimensions / equations
- Torque T proportional to speed omega and excitation current.
- T -> 0 at zero speed (cannot hold).
- Heat dissipation Q = T * omega.

## Constraints
- Cannot hold at zero speed.
- Requires cooling (air/water).
- Torque falls at low speed.

## Failure modes
- Overheating.
- Magnet/coil failure.
- Corrosion of conductive disk.

## When to use
Trains, roller coasters, aircraft, heavy-vehicle retarders.

## DFM (small workshop)
Use commercial retarders; ensure cooling and speed range.

## Sources
springs_clutches_brakes.md