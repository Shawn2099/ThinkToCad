# bolted_joint

**Type:** joint
**Function:** Clamp parts together via threaded fasteners to transmit load and allow disassembly.

## How it works
Bolts provide preload (clamping force) that keeps joint surfaces in compression; load is transferred by friction/preload and, if slipped, by bolt shear. Torque T = K*F*d (K ~ 0.20) estimates preload; target preload ~75% of proof load.

## Key dimensions / equations
- ISO 898-1 property classes: 4.6-12.9; stress areas As (mm^2): M6 20.1, M8 36.6, M10 58.0, M12 84.3, M16 157, M20 245.
- Proof loads Fp (kN), class 8.8: M6 11.6, M8 21.2, M10 33.7, M12 48.9, M16 91.0, M20 147.
- Torque T = 0.20 x 0.85 x Fp x d (N*m); examples 8.8: M6 11.8, M8 28.8, M10 57.3, M12 99.8, M16 247.5, M20 500.
- Thread engagement ~1.0-1.5d in steel, 2-3d in Al/cast iron (rule of thumb).

## Constraints
- Torque is indirect preload control; friction/lubrication/coatings change preload.
- Requires locking (nyloc, threadlocker, safety wire, cotter pins, tab washers) under vibration.
- Bolted flanges need gasket seating and torque sequence.

## Failure modes
- Loosening from vibration without locking.
- Over-torque -> yielding/stripping; under-torque -> slip/fatigue.
- Fatigue at thread root under cyclic load.

## When to use
General assemblies needing disassembly, maintenance, adjustment; pressure vessels/flanges.

## DFM (small workshop)
Standardize on M6/M8/M10 8.8/10.9 with nyloc or threadlocker; use star-pattern torque; re-torque after heat cycles.

## Sources
joints_fasteners_bearings_springs.md