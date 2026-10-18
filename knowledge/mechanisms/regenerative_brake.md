# regenerative_brake

**Type:** brake
**Function:** Recover kinetic energy by operating a motor as a generator, returning energy to a battery or flywheel.

## How it works
Motor acts as generator during deceleration, converting kinetic energy to electrical (or flywheel) energy. Limited by battery state and motor capacity; reduces friction brake wear.

## Key dimensions / equations
- Recovered energy <= 1/2 m v^2 (minus losses).
- Power limited by motor/generator rating and battery acceptance.
- Blending with friction brakes for low speed/holding.

## Constraints
- Cannot hold vehicle at standstill alone.
- Battery state limits recovery.
- Requires control system.

## Failure modes
- Battery overcharge if not managed.
- Reduced braking if battery full.
- System fault -> fallback to friction brakes.

## When to use
EVs, trains, flywheel KERS, hybrid vehicles.

## DFM (small workshop)
Use integrated drive controls; retain friction brakes for holding/emergency.

## Sources
springs_clutches_brakes.md