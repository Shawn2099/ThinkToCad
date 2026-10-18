# helical_extension_spring

**Type:** spring
**Function:** Store energy and exert a pulling force when stretched, returning to free length.

## How it works
Coiled wire spring with hooks/loops at ends; axial load extends spring. Has initial tension (preload) keeping coils closed until load exceeds it. Rate linear after initial tension.

## Key dimensions / equations
- Spring rate k = G*d^4/(8*D^3*n_a) (same as compression).
- Initial tension keeps coils closed; load F = F_initial + k*x.
- Hook stress concentration must be checked (higher stress at hooks).
- Body stress and hook bending.

## Constraints
- Hooks are stress concentrators; fatigue often starts at hooks.
- Initial tension must be overcome before extension.
- Lateral stability; avoid over-extension.

## Failure modes
- Fatigue fracture at hooks.
- Hook deformation/unbending.
- Permanent set if overstretched.

## When to use
Returns, trampolines, garage doors, tension mechanisms, latches.

## DFM (small workshop)
Use standard hooks, avoid sharp bends, consider full-loop or threaded inserts, lubricate.

## Sources
joints_fasteners_bearings_springs.md