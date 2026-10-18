# Reliability and safety constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/reliability_safety.md;
O'Connor & Kleyner, Modarres, MIL-STD-882, ISO 12100/13849.

## Safety factors
- Static: 1.5-2.0 for ductile, 2.0-4.0 for brittle, 4.0+ for unknown loads.
- Fatigue: 2.0-3.0 typical. Creep: 1.5-2.0.
- Safety factor = (allowable stress) / (working stress). Safety margin =
  (allowable - working) / allowable.
- Always state the basis: material uncertainty, load uncertainty, consequence.

## Reliability
- Bathtub curve: infant mortality -> useful life -> wear-out.
- MTTF (mean time to failure) for non-repairable; MTBF for repairable.
- Weibull: R(t) = exp(-(t/eta)^beta). beta<1 infant mortality, beta=1 random,
  beta>1 wear-out. eta = characteristic life.
- Series system: R_s = product(R_i). Parallel: R_p = 1 - product(1-R_i).
- Redundancy: n-1, n-2 for critical systems. Derating: operate below rated capacity.

## Failure analysis
- FMEA: identify failure modes, effects, causes. Risk Priority Number (RPN) =
  severity * occurrence * detection. Target high RPN items.
- FTA: top-down fault tree, AND/OR gates, probability of top event.
- HAZOP: systematic hazard identification (deviation analysis).
- Root cause: 5 Whys, fishbone (Ishikawa), fractography (visual/microscopic).

## Design for reliability
- Fail-safe: failure leads to safe state (brakes engage on power loss).
- Fail-operational: system continues operating after failure (redundancy).
- Damage tolerance: design for crack growth, inspect before failure.
- Derating: operate at 50-70% of rated capacity for longer life.

## Standards
- ISO 12100: risk assessment for machinery (hazard identification, risk estimation,
  risk reduction). ISO 13849: safety of machinery (performance levels PL a-e).
- IEC 61508: functional safety (SIL 1-4). MIL-STD-882: system safety.
- ASME B30/B31: crane/piping safety. OSHA: workplace safety.

## Fatigue reliability
- Scatter in fatigue data: use statistical methods (Weibull on fatigue life).
- Design for 99% reliability: use lower confidence bound of S-N curve.
- Inspect for cracks before critical life (damage tolerance).

## AI rules
- Always state safety factor and its basis.
- For safety-critical parts: use fail-safe design, redundancy, inspection.
- Run FMEA on new designs; target RPN > 100 for action.
- Consider human error: guards, interlocks, clear labeling.