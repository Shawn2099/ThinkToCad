# hysteresis_clutch

**Type:** clutch
**Function:** Transmit constant torque from hysteresis losses in a drag cup, largely independent of slip speed.

## How it works
A permanent-magnet or excited rotor creates hysteresis losses in a drag cup; torque is nearly constant across slip speed. Very low wear (non-contact-ish) for fractional power.

## Key dimensions / equations
- Torque constant vs. slip speed (within range).
- Power = T * omega_slip dissipated as heat.
- Torque set by magnet strength and cup material.

## Constraints
- Fractional power only.
- Heat dissipation limits continuous slip.
- Higher cost per torque than friction.

## Failure modes
- Demagnetization from heat/overload.
- Bearing wear.
- Cup material fatigue.

## When to use
Tension control, testing, low-power drives needing constant torque.

## DFM (small workshop)
Use commercial units; respect thermal limits; avoid shock loads.

## Sources
springs_clutches_brakes.md