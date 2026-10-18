# cv_joint

**Type:** coupling
**Function:** Transmit power at an angle with constant velocity (no speed fluctuation).

## How it works
Constant-velocity joint maintains equal input/output speed through the angle. Types: Rzeppa (ball), double Cardan, Thompson. Typical automotive half-shaft application.

## Key dimensions / equations
- omega_out = omega_in (constant) at any operating angle (within limits).
- Double Cardan = two U-joints 90deg out of phase with equal angles.
- Operating angle limits higher than single U-joint.

## Constraints
- More complex and costly than U-joint.
- Boot/seal needed to retain grease.
- Wear affects CV performance.

## Failure modes
- Boot tear -> grease loss and contamination.
- Ball/track wear causing clicking.
- Overload at high angles.

## When to use
Front-wheel-drive half-shafts, steering drives, high-angle power transmission.

## DFM (small workshop)
Use commercial CV joints; protect boots; avoid extreme angles/overload.

## Sources
clutches_brakes_couplings_indexing.md