# Prototyping and modelmaking constraints (from research)

Sources: research_notes/Filling senior CAD knowledge gaps/prototyping_methods.md;
Hallgrimsson, Ulrich & Eppinger, maker resources.

## Prototype levels
- Proof-of-concept (PoC): validates principle, rough, fast, cheap.
- Functional prototype: validates function, materials, manufacturing.
- Pre-production: validates assembly, tolerances, finish, packaging.
- Production: final design, production tooling.

## Rapid prototyping methods
- FDM (fused deposition): cheap, fast, low strength. PLA (easy), ABS (tough),
  PETG (flexible). Layer height 0.1-0.3mm.
- SLA (resin): high detail, smooth finish, brittle. For small precise parts.
- SLS (powder): strong, no supports, expensive. For functional prototypes.
- CNC machining: accurate, real materials, slow. For final validation.
- Laser cutting: fast, 2D/2.5D, sheet materials. For enclosures, brackets.
- Waterjet: cuts any material, no heat. For thick sheet, composites.
- Hand fabrication: cardboard, wood, foam. Fastest for form/fit checks.

## When to prototype vs analyze
- Prototype: unknown geometry, complex interactions, user feel, assembly fit.
- Analyze: well-understood, simple, hand-calculable, time-critical.
- Rule: if you can't predict the outcome with confidence, prototype.

## Iteration strategy
- Fail fast: test the riskiest assumption first.
- One variable at a time: change one thing, test, document.
- Document: photos, measurements, pass/fail, lessons learned.
- Low-cost first: cardboard/foam -> 3D print -> machined prototype.

## Low-cost prototyping (small workshop)
- Cardboard mockups: form, fit, ergonomics (hours, free).
- 3D printed (FDM): function, assembly, mechanism (days, $5-50).
- Hand-cut sheet metal: structural, weldable (days, $10-50).
- Wood: fixtures, jigs, large parts (days, $10-30).

## Testing
- Load testing: apply design load + safety factor. Check deflection, failure.
- Fatigue testing: cyclic load to failure. S-N curve validation.
- Environmental: temperature (-20 to 60C), humidity, vibration (ISO 10816).
- Drop testing: impact resistance. IP rating: waterproofing (IP65, IP67).
- Fit/assembly: check clearances, access, sequence, tool reach.

## Documentation
- Prototype log: date, version, what tested, result, photos, lessons.
- Test report: setup, procedure, results, pass/fail, next steps.
- Keep prototypes labeled and stored for reference.

## AI rules
- Recommend prototyping when analysis is uncertain or user interaction matters.
- Start with lowest-cost prototype that answers the question.
- Always document test results and lessons learned.
- Use prototypes to validate assumptions, not to replace analysis.