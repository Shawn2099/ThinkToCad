# Human Evaluation Rubric — ThinkToCad Design Outputs

Used for the human-in-the-loop gate (G4) and for paper reporting.
Each rater scores independently; report mean + std + inter-rater agreement (Cohen's κ).

## Rater instructions
Rate each generated design (render + STEP + BOM entry) on the 5 criteria below.
Use the scale 1 (poor) to 5 (excellent). Leave a one-line justification per criterion.

## Criteria

### 1. Functional correctness (weight 0.30)
Does the part perform its stated function?
- 1: Does not function at all
- 2: Functions only in a narrow range
- 3: Functions in the stated range with minor issues
- 4: Functions reliably across the full range
- 5: Functions reliably and exceeds the stated range

### 2. Manufacturability (weight 0.25)
Can the part be made with the user's actual shop (per manufacturing profile)?
- 1: Requires processes/tools the user does not have
- 2: Requires significant rework or special tooling
- 3: Manufacturable with available tools, marginal DFM
- 4: Clean DFM, standard stock sizes, no special tooling
- 5: Optimal for the shop; minimal waste, standard fixturing

### 3. Geometric validity (weight 0.20)
Is the CAD model valid and well-formed?
- 1: Fails to build or has invalid geometry
- 2: Builds but has interference / non-manifold / open shells
- 3: Valid geometry, minor clearance issues
- 4: Valid, watertight, correct clearances
- 5: Valid, watertight, optimal clearances, deterministic rebuild

### 4. Design clarity (weight 0.15)
Is the design easy to understand, modify, and maintain?
- 1: Opaque, no parametric structure
- 2: Partially parametric, hard to modify
- 3: Parametric but naming/conventions inconsistent
- 4: Clear parametric structure, good naming
- 5: Exemplary: documented, parametric, easy to modify

### 5. Overall preference (weight 0.10)
Compared to the baseline (human-designed or prior version), which do you prefer?
- 1: Much worse
- 2: Worse
- 3: About the same
- 4: Better
- 5: Much better

## Scoring
Composite = 0.30×C1 + 0.25×C2 + 0.20×C3 + 0.15×C4 + 0.10×C5

Report: mean composite, std, min, max, and % designs scoring ≥ 4.0.

## Inter-rater agreement
Report Cohen's κ (or Krippendorff's α for >2 raters) on the binary "acceptable (≥4.0)" decision. Target: κ ≥ 0.6 (substantial agreement).