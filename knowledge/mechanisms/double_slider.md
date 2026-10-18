# double_slider

**Type:** mechanism
**Function:** Convert motion between two sliding (prismatic) members via a coupler link.

## How it works
Four-bar chain of type PRRP: two prismatic joints (sliders) and two revolute joints. A coupler link connects the two sliders; motion of one slider drives the other. Includes elliptical trammel and scotch-yoke variants.

## Key dimensions / equations
- Mobility M = 1 (PRRP closed chain).
- Slider strokes related by coupler length: x^2 + y^2 = L^2 (elliptical trammel) for perpendicular sliders.
- Scotch yoke is a PRRP inversion with one slider as crank pin.

## Constraints
- Sliders need accurate guides/bushings; wear at sliding contacts.
- Coupler must not bind in guides.
- Lubrication required for sliding surfaces.

## Failure modes
- Guide wear and backlash.
- Coupler interference at extreme positions.
- Seizure if lubrication fails.

## When to use
Elliptical motion generation, scotch-yoke drives, quick-return mechanisms, compact linear drives.

## DFM (small workshop)
Use linear bearings or bronze bushings in bored guides, keep coupler simple, add grease fittings.

## Sources
linkages.md