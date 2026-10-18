# Power transmission constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/power_transmission.md;
Shigley, Mott, Hamrock, AGMA, SKF, Gates.

## Shafts
- Design for fatigue: modified Goodman with combined bending+torsion.
  sigma_a = Kf*Ma/Z, tau_a = Kfs*Ta/Z. sigma_vm = sqrt(sigma_a^2 + 3*tau_a^2).
  Se = ka*kb*kc*kd*ke*kf*Se'. Safety factor n = Se/sigma_vm (or yield check).
- Keyseat stress concentration: Kt = 2.14 (square), 2.62 (Woodruff), 3.0 (end mill).
- Critical speed: avoid operating near natural frequency (whirl). Use Rayleigh method.
- Deflection: limit slope for gears (<0.0005 rad) and bearings (<0.001 rad).
- Retaining rings: use for axial location of bearings/gears. Shoulders for thrust.

## Bearings
- Life: L10 = (C/P)^p hours, where p=3 (ball), p=10/3 (roller). L10h = L10*1e6/(60*n).
- Selection: radial load -> deep groove ball; combined load -> angular contact;
  heavy radial -> cylindrical roller; axial -> thrust. Speed: ball > roller.
- Lubrication: grease (sealed, low maintenance) or oil (high speed, cooling).
  Sealed bearings for small shops. Relubricate per manufacturer schedule.
- Mounting: interference fit on rotating ring, clearance on stationary ring.
  Preload for angular contact (precision, rigidity).

## Gears
- Spur: bending stress (AGMA) sigma = Wt*Ko*Kv*Ks/(m*F*J). Contact stress
  (Hertzian) sigma_H = Cp*sqrt(Wt*Ko*Kv*Ks/(d*F*I)).
- Helical: higher load capacity, smoother, axial thrust. Use for high speed.
- Bevel: right-angle power transmission. Spiral bevel for smoothness.
- Worm: high ratio (up to 100:1), self-locking if lead angle < friction angle.
  Efficiency low (50-90%). Use for speed reduction, not power transmission.
- Planetary: compact, high ratio, coaxial. Use for space-constrained designs.
- Backlash: 0.04-0.1mm for precision; more for thermal expansion.
- Profile shift: avoid undercutting (z_min = 2/sin^2(phi)).

## Belts
- V-belt: power capacity from manufacturer tables. Wrap angle >= 120 deg.
  Center distance: 0.7-2.0x larger pulley diameter. Tension with idler.
- Timing belt: positive drive, no slip. Tooth shear and tensile limits.
- Speed ratio: i = d2/d1. Max speed: V-belt ~25 m/s, timing ~50 m/s.

## Chains
- Roller chain: power rating from manufacturer (Mädler/ISO 606). Lubrication
  critical (drip or bath). Wear elongation limit: 3% (replace).
- Sprocket: min teeth 17 (avoid polygon effect). Speed ratio i = z2/z1.

## Couplings
- Rigid: sleeve, flange, clamp. Use when misalignment < 0.05mm.
- Flexible: jaw (spider), Oldham, bellows, diaphragm, grid, gear. Absorb
  misalignment and vibration.
- Universal joint: for angular misalignment. CV joint: constant velocity.
- Safety: shear pin (sacrificial), slip (friction, resettable).

## Clutches/brakes
- Friction disk: torque = mu*F*r_m*n (n = number of surfaces). Heat dissipation
  critical. Use for engagement/disengagement.
- Centrifugal: engages at speed. Use for small engines, go-karts.
- Dog (jaw): positive engagement, no slip. Use for indexing, low speed.
- Electromagnetic: clean, fast. Use for automation, frequent cycling.
- Band brake: simple, wrapping friction. Disk brake: high performance, cooling.

## System integration
- Shaft diameter is the master variable: drives bearing bore, gear bore, housing
  bolt circle, coupling size.
- Design flow: power/torque -> shaft diameter (fatigue) -> bearing selection ->
  gear selection -> housing design -> bolt sizing.
- Standardize: use same shaft diameter, bolt size, bearing series across a design.