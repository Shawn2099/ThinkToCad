# FEA/CAE constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/fea_cae.md;
Cook, Moaveni, Logan, Reddy; FreeCAD FEM; NAFEMS; V&V-40.

## Analysis types
- Linear static: small displacement, linear material, no contact. Fast, first pass.
- Nonlinear: large displacement, plasticity, contact. Use when geometry/material
  is nonlinear or loads are large.
- Modal: natural frequencies and mode shapes. Check operating frequency is not
  near a natural frequency (avoid resonance).
- Buckling: critical load for slender/compressive members.
- Thermal: steady-state or transient temperature; couple to structural (thermal stress).
- Dynamic/transient: time-varying loads, impact, shock.

## Meshing
- Element types: tet (general), hex (preferred for accuracy), wedge, shell (thin
  walls), beam (slender members).
- Mesh convergence: h-refinement (smaller elements) until results change < 5%.
  Report convergence study. GCI/Richardson extrapolation for credibility.
- Aspect ratio < 5 preferred; Jacobian > 0.3. Avoid sliver elements.
- Mesh singularities at sharp corners; fillet or use local refinement.

## Boundary conditions
- Fixed/pinned: avoid over-constraining; use symmetry planes to reduce model.
- Remote loads for bolted connections; bolt pretension for preload.
- Pressure for hydrostatic/air loads. Thermal for temperature-dependent.
- Always check reaction forces balance applied loads.

## Material models
- Linear elastic for first pass (E, nu). Plastic (bilinear/multilinear) for
  yield/failure. Hyperelastic for rubber. Creep for high-temp. Fatigue for cyclic.
- Use material property tables from standards/suppliers, not textbook defaults.

## Contact
- Bonded: glued/welded. No-penetration: contact without sliding. Frictional:
  sliding with friction. Separation: contact can open.
- Contact stiffness and penetration: check no excessive penetration.

## Results interpretation
- Von Mises: ductile materials under combined stress (yield criterion).
- Principal stresses: brittle materials, crack initiation.
- Safety factor: yield/allowable stress; use >1.5 for static, fatigue requires
  more. Report which theory (von Mises vs Tresca) and the value.
- Displacement: check against functional limits (deflection, clearance).
- Strain: for fatigue and large deformation.

## Common pitfalls
- Stress singularities at sharp corners (fillet or ignore local peak).
- Unrealistic BCs (over-constraining, missing contact).
- Wrong units (mm vs m, MPa vs Pa).
- Mesh too coarse (no convergence check).
- Ignoring contact (bonded when it should slide).

## Design loop integration
- Use hand calcs for simple, well-understood cases (Shigley formulas).
- Use FEA for complex geometry, unknown stress concentrations, assemblies.
- Always verify FEA with a hand calc or known benchmark (NAFEMS).
- Credibility tier: critique -> surrogate -> proxy -> executed solver. Never
  assume production_ready without validation.

## AI rules
- Always report element type, mesh size, and convergence status.
- Flag singularities and suggest fillets.
- Never trust a single mesh; require a convergence check.
- For safety-critical parts, require FEA + hand calc + test.