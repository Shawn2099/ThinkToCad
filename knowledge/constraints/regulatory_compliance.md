# Regulatory compliance constraints (from research)

Sources: research_notes/Filling senior CAD knowledge gaps/regulatory_compliance.md;
ISO 12100, ISO 13849, IEC 61508, Machinery Directive 2006/42/EC, OSHA 1910.

## Machinery safety (ISO 12100)
- Risk assessment: identify hazards, estimate risk (severity x probability),
  reduce risk (eliminate, guard, inform). Iterate until acceptable.
- ISO 13849: safety of machinery, performance levels (PL a-e). Categories B, 1-4.
  Higher PL = more reliable safety function.
- IEC 61508: functional safety, SIL 1-4. IEC 62061: machinery-specific.

## CE marking (EU)
- Machinery Directive 2006/42/EC: scope, essential health and safety
  requirements (EHSR). Technical file: design docs, risk assessment, test reports.
- Declaration of conformity (DoC): manufacturer declares compliance.
- CE mark: affix to product. Notified body for high-risk machines (Annex IV).
- Harmonized standards (EN ISO 12100, EN ISO 13849) give presumption of conformity.

## OSHA (US)
- 1910.212: machine guarding (point of operation, rotating parts, in-running
  nip points). Guards must prevent access to hazard zone.
- 1910.147: lockout/tagout (LOTO) for servicing. Energy control program required.
- 1926: construction machinery (if applicable).

## Pressure vessels (ASME)
- ASME BPVC Section VIII: design, fabrication, inspection of pressure vessels.
- Section IX: welding qualifications. B31: piping. Use for tanks, boilers, pipes.

## Electrical
- IEC 60204-1: electrical equipment of machines (wiring, grounding, e-stops).
- UL/CSA: third-party certification for electrical safety (NRTL marks).

## Environmental
- RoHS: restricts 10 hazardous substances (Pb, Hg, Cd, Cr6+, PBB, PBDE, etc.).
- REACH: SVHC notification (>0.1% by weight). WEEE: end-of-life recycling.
- Conflict minerals: 3TG (tin, tantalum, tungsten, gold) due diligence.

## Ergonomics
- ISO 11226: manual handling. ISO 14738: anthropometric requirements for
  machinery. Design for operator reach, force, posture.

## Design for compliance
- Risk assessment first (ISO 12100). Identify all hazards.
- Safety guards: physical barriers, interlocks, light curtains.
- Emergency stop: accessible, red/yellow, category 0/1 stop.
- Lockout points: accessible energy isolation.
- Labeling: warnings, operating instructions, CE mark.
- Documentation: technical file, DoC, user manual.

## AI rules
- Run risk assessment (ISO 12100) for every new machine design.
- Identify applicable standards early (CE, OSHA, ASME, ISO).
- Design guards and interlocks into the concept, not as afterthoughts.
- Flag regulatory requirements in the contract (standards: field).