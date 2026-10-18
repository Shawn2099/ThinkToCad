# inverted_slider_crank

**Type:** mechanism
**Function:** Convert between rotary and sliding motion with the coupler (connecting rod) as the ground link.

## How it works
Inversion of the slider-crank where the connecting rod becomes the fixed frame; the slider connects directly to the crank. Used where the frame must move relative to ground or where compact actuation is needed.

## Key dimensions / equations
- Same base kinematics as slider-crank with link roles swapped: ground = former coupler.
- Applications: backhoe/crane actuators, swinging gates, oscillatory engines.

## Constraints
- Frame (coupler) must be rigidly mounted; geometry less intuitive.
- Same guide-alignment requirements as slider-crank.

## Failure modes
- Guide wear and binding.
- Pivot/bearing wear.
- Interference at extreme positions.

## When to use
Backhoe booms, crane actuators, swinging gates, compact linear actuators.

## DFM (small workshop)
Reuse slider-crank parts where possible; ensure ground link is stiff; lubricate pins.

## Sources
linkages.md