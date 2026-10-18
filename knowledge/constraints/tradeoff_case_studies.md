# Trade-off and decision-making constraints (from research)

Sources: research_notes/Filling senior CAD knowledge gaps/tradeoff_case_studies.md;
Ullman, Pahl & Beitz, Pugh, Dieter.

## Design trade-off analysis
- Design is decision-making under uncertainty with competing objectives.
- Common trade-offs: cost vs performance, weight vs strength, manufacturability
  vs function, precision vs cost, speed vs accuracy.
- Methods: Pugh matrix (concept scoring with datum), weighted decision matrix,
  AHP (analytic hierarchy process), Pareto analysis, sensitivity analysis.

## Pugh matrix (concept scoring)
- Select a datum concept (usually simplest or current design).
- Score each concept +1 (better), 0 (same), -1 (worse) vs datum on each criterion.
- Sum scores; refine top concepts; iterate (controlled convergence).
- Warning: results depend on datum choice; use multiple datums or weighted scoring.

## Weighted decision matrix
- Assign weights to criteria (sum = 1.0). Score each concept 1-5 on each criterion.
- Total = sum(weight * score). Higher = better.
- Use for final selection among 2-4 candidates.

## Pareto analysis
- 80/20 rule: 20% of features drive 80% of cost/effort.
- Focus design effort on high-impact items. Eliminate or simplify low-impact features.
- A posteriori Pareto: after optimization, identify non-dominated solutions.

## Design reviews
- Staged reviews: concept, preliminary, critical, final.
- Checklist: function, safety, manufacturability, cost, standards, testability,
  maintenance, documentation.
- Common findings: missing requirements, unverified assumptions, tolerance issues,
  assembly problems, cost drivers.

## "Good enough" decisions
- Stop iterating when: user approves, or two consecutive rounds yield no change
  in approved elements, or budget exhausted (~5 iterations, ~3 review rounds).
- Perfect is the enemy of good: accept 90% solution if cost of 100% is 10x.
- Document the compromise and the reason (traceability).

## Value engineering
- Value = Function / Cost. Maximize function, minimize cost.
- FAST diagram: function analysis (verb-noun). Identify unnecessary functions.
- Target: 20-40% cost reduction by rethinking design, not just cutting material.
- Best applied at concept stage (before detail design locks in cost).

## Case study lessons
- Hyatt walkway: connection detail changed without re-analysis -> collapse.
  Lesson: any design change requires re-analysis.
- Challenger: normalization of deviance (O-ring erosion accepted as normal).
  Lesson: never accept recurring anomalies without root cause.
- Tacoma Narrows: aeroelastic flutter not considered. Lesson: check all
  loading modes, not just static.
- Grenfell: material substitution without fire safety review. Lesson: material
  changes require full re-evaluation.

## AI rules
- Use Pugh matrix for concept selection (2-4 candidates).
- Use weighted matrix for final selection.
- Always document trade-offs and the reason for the chosen option.
- Run design reviews at concept, preliminary, and final stages.
- Flag "good enough" decisions and the remaining risk.