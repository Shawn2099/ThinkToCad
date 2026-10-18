# torsion_bar_spring

**Type:** spring
**Function:** Store energy by twisting a straight solid or hollow bar in torsional shear.

## How it works
A straight bar fixed at one end and loaded by a lever/arm at the other twists about its axis. Deflection angle theta = T L / (G J), spring rate k_theta = pi G D^4 / (32 L) (solid).

## Key dimensions / equations
- theta = T L/(G J); k_theta = pi G D^4/(32 L) (solid round).
- Hollow bar: J = pi (D_o^4 - D_i^4)/32.
- Stress tau = T r / J.

## Constraints
- Length and diameter set stiffness; packaging often limits length.
- Fatigue at surface; shot peening helps.
- Requires secure anchoring at both ends.

## Failure modes
- Fatigue cracking from cyclic twist.
- Permanent set from overload.
- Buckling/torsional instability in slender bars.

## When to use
Automotive suspension and stabilizer bars, compact rotary spring needs.

## DFM (small workshop)
Use round bar stock; calculate twist and stress; provide keyed/flat ends for torque transfer.

## Sources
springs_clutches_brakes.md