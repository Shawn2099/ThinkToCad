# rack_and_pinion

**Type:** mechanism
**Function:** Convert rotary motion into linear motion (or vice versa) via a gear (pinion) meshing with a straight rack.

## How it works
A pinion gear meshes with a linear rack (gear with infinite radius). Rotation of pinion drives rack linearly; rack motion can drive pinion. Provides precise, backlash-controllable linear drive.

## Key dimensions / equations
- Linear displacement x = (pi*m*N_pinion*theta)/(360deg) for module m, theta in degrees; or x = r*theta (r = pitch radius).
- Gear ratio in linear terms: speed = omega*r.
- Backlash minimized by spring-loaded or split pinions, or adjustable mesh.

## Constraints
- Rack must be straight and well supported; deflection affects accuracy.
- Backlash on reversal unless controlled.
- Pinion teeth >= z_min to avoid undercutting.

## When to use
CNC axes, steering systems, 3D printers, linear actuators, lifts.

## DFM (small workshop)
Use standard module racks/pinions, support rack along length, add anti-backlash (spring or split pinion).

## Sources
cams_and_gears.md