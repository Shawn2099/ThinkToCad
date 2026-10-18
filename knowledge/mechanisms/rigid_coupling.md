# rigid_coupling

**Type:** coupling
**Function:** Connect two shafts rigidly for power transmission, requiring precise alignment.

## How it works
No flexible element; transmits torque with zero backlash and high stiffness. Types: sleeve/muff (pipe with keyway), split-muff/clamp (two halves bolted), flange (bolted flanges for heavy loads), tapered shaft lock (keyless).

## Key dimensions / equations
- Sleeve: keyway transmits torque; pin/key shear limits.
- Clamp/split-muff allows assembly without moving shafts.
- Flange: bolt circle and bolt shear/tension design.
- Alignment must be held within ~0.05 mm TIR.

## Constraints
- Requires precise alignment; misalignment damages bearings.
- No misalignment accommodation.
- Permanent-ish (except split/clamp types).

## Failure modes
- Bearing damage from misalignment.
- Key shear or bolt failure under overload.
- Fretting at interface.

## When to use
Precisely aligned shafts, high stiffness, zero backlash (encoders, spindles).

## DFM (small workshop)
Use keyed + set-screw or clamp hubs; avoid welding hubs to shafts unless permanent.

## Sources
clutches_brakes_couplings_indexing.md