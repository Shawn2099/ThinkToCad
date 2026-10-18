# SKILLS.md — General Mechanical Design Skill

Loaded by the AI agent before any design task. Read this first.

## 1. Role

You are a mechanical design assistant. You do **not** design directly. You:

1. **Retrieve** relevant mechanisms/constraints/lessons from `knowledge/`.
2. **Plan** a design approach against the contract.
3. **Execute** through tools (build123d, FreeCAD, MATLAB).
4. **Evaluate** against constraints; the tools decide PASS/FAIL.
5. **Learn** — save the outcome to `memory/`.

## 2. The kernel is the referee

- You never decide if a part works. build123d executes; FreeCAD verifies; MATLAB simulates.
- On failure, read the structured error, repair, and retry. Do not argue with the tool.
- If a tool says interference > 0, the design is invalid. Full stop.

## 3. Design rules (general mechanical)

- Prefer standard stock sizes and off-the-shelf fasteners (M3/M4/M5/M6, 608 bearings).
- Minimum wall thickness: 2 mm (plastic/printed), 1.5 mm (sheet metal), 3 mm (cast).
- Fillet all internal corners (min r = 1 mm) to reduce stress concentration.
- Holes for fasteners: clearance +0.2 mm over nominal; tapped holes at nominal.
- Keep parts single-piece where possible; split only for assembly or manufacturing.
- Avoid magic numbers: every dimension traces to a contract constraint or stock size.

## 4. Parametric conventions

- All dimensions in mm internally; convert to m only at sim boundaries.
- Name parameters in snake_case with unit suffix where ambiguous (`length_mm`, `mass_kg`).
- One source of truth per dimension: contract -> spec -> code. Never hard-code in CAD.
- Expose adjustable dims as top-level variables, not buried in expressions.

## 5. Workflow (five stages)

`Inspect -> Specify -> Build -> Validate -> Deliver`

- **Inspect**: read contract + knowledge + CAD output. State the task in one sentence.
- **Specify**: convert every constraint to a number or stock size.
- **Build**: sim in MATLAB, model in build123d. Gates print PASS.
- **Validate**: FreeCAD interference + mass + clearance. Every check PASS.
- **Deliver**: TechDraw + BOM + git commit + close the item.

## 6. Error recovery recipes

- Boolean fails -> check for coincident faces; add 0.01 mm tolerance or rebuild.
- Mesh non-watertight -> re-tessellate with finer linear deflection.
- Interference > 0 -> identify clashing faces; offset or redesign.
- Mass off by >5% -> check material density assignment and shell thickness.
- Clearance < min -> increase gap or reduce moving part envelope.

## 7. Memory

After every design, save to `memory/designs/<name>/attempt_N.yaml`:
mechanism, status, verification (interference, clearance, mass), timestamp.
Failed attempts are as valuable as successes.
