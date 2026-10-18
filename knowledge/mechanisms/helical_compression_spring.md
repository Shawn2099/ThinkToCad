# helical_compression_spring

**Type:** spring
**Function:** Store energy and exert a pushing force when compressed, returning to free length.

## How it works
Coiled wire spring; axial load compresses coils, reducing length. Energy stored as torsional shear in wire. Rate linear (Hooke's law) within elastic range.

## Key dimensions / equations
- Spring rate k = G*d^4/(8*D^3*n_a), d = wire dia, D = mean dia, n_a = active coils.
- Mean diameter D = D_outer - d; shear modulus G = E/[2(1+nu)].
- Hooke's law: k = F/x.
- Solid height: L_solid = d*(N+1) unground ends; d*N ground ends.
- Pitch: p = (L - 3d)/n_a (closed ends), (L - 2d)/n_a (closed & ground), (L - 5d)/n_a (double closed), (L - d)/n_a (open ends).
- Spring index C = D/d (target 4-12).

## Constraints
- Buckling if L_free/D > ~4 (use guide/parallel springs).
- Max shear stress at solid: tau = K*(8FD)/(pid^3).
- Fatigue under cyclic load (modified Goodman; shot peen).

## Failure modes
- Fatigue fracture from cyclic loading.
- Buckling/bowing in slender springs.
- Settling (permanent deformation) if overstressed.

## When to use
Valves, clutches, returns, shock absorption, general machine springs.

## DFM (small workshop)
Use music wire (ASTM A228) or stainless (A313); standard wire sizes; add guide for slender springs.

## Sources
joints_fasteners_bearings_springs.md