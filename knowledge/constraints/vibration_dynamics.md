# Vibration and dynamics constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/vibration_dynamics.md;
Rao, Inman, Thomson & Dahleh, Shigley.

## Natural frequency
- Single DOF: omega_n = sqrt(k/m). f_n = omega_n/(2*pi).
- Avoid operating speed within +/-20% of any natural frequency (resonance).
- For shafts: critical speed (whirl) = (1/2*pi)*sqrt(k/m). Design above or below.

## Damping
- Viscous: F = c*v. Damping ratio zeta = c/(2*sqrt(k*m)). Underdamped
  (zeta<1): oscillates. Overdamped (zeta>1): no oscillation.
- Transmissibility: TR = sqrt(1+(2*zeta*r)^2) / sqrt((1-r^2)^2+(2*zeta*r)^2),
  where r = f/f_n. Isolation (TR<1) requires r > sqrt(2).
- For vibration isolation: f_n < f_excitation/sqrt(2). Use soft mounts.

## Multi-DOF
- Modal analysis: solve eigenvalue problem for natural frequencies and mode shapes.
- Use FEA for complex geometry. Check first 3-5 modes.
- Mode shapes: identify which parts move most; reinforce or dampen.

## Rotating machinery
- Unbalance: F = m*e*omega^2. Balance to reduce. Static balance: center of mass
  on axis. Dynamic balance: principal axis alignment.
- Critical speed: first critical = first natural frequency of rotating shaft.
  Design operating speed < 0.7*critical or > 1.3*critical.

## Shock and impact
- Shock response spectrum (SRS): peak response for a given input pulse.
- Energy absorption: use dampers, crush zones, springs. Impulse = integral(F*dt).
- For impact: check peak stress < yield; use dynamic load factor (1.5-3.0).

## Vibration standards
- ISO 10816/20816: vibration severity zones (A/B/C/D) for rotating machines.
- MIL-STD-810: environmental test methods (vibration, shock, temp).

## DFM rules
- Avoid thin, flexible parts in vibration environments (add ribs/stiffeners).
- Use dampers (rubber mounts, springs) for vibration-sensitive components.
- Secure wiring and hoses to prevent fatigue from vibration.
- Test: run at operating speed, measure vibration, check against ISO zones.