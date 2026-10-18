# Drawing standards constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/drawing_standards.md;
ASME Y14.x, ISO 128/129/1302, Giesecke, Madsen.

## Views
- Orthographic: front, top, side (minimum 2-3 views for 3D clarity).
- Section views: full, half, offset, broken-out, revolved, removed. Use to show
  internal features.
- Auxiliary views: for inclined surfaces. Detail views: for small features.
- Isometric: for visualization, not for dimensioning.

## Dimensioning
- Linear: horizontal/vertical/aligned. Angular: degrees. Radial/diametral: R/Dia.
- Ordinate: from a datum (for many holes). Chain: sequential (accumulates error).
  Baseline: from common datum (preferred for accuracy).
- Dimension placement: outside the view, clear of geometry. Leader lines for holes.
- One dimension per feature; no redundant dimensions.

## Tolerancing on drawings
- Unilateral: +0/-x or +x/-0. Bilateral: +/- x. Limit: upper/lower values.
- General tolerances: ISO 2768-m (medium) default for unmarked dimensions.
- GD&T: per ASME Y14.5 or ISO GPS (declare in title block). See gdt_tolerancing.md.

## Title block
- Required: part name, number, material, scale, projection (1st/3rd angle),
  standard (ASME/ISO), revision, date, drawn by, checked by.
- Revision block: track changes with date and description.
- Scale: 1:1 preferred; state scale if different.

## Drawing types
- Detail drawing: single part with all dimensions and tolerances.
- Assembly drawing: all parts assembled, BOM, balloon callouts.
- Exploded view: parts separated to show assembly order.
- Installation drawing: how to install in the larger system.

## Surface finish
- ISO 1302 / ASME B46.1 symbols. Ra values: turned 1.6-3.2, milled 1.6-6.3,
  ground 0.4-1.6, polished 0.1-0.4, as-cast 6.3-25.
- Specify finish only where function requires (cost). Default finish for unmarked.
- Lay symbols: parallel, perpendicular, circular, radial, multidirectional.

## Weld symbols
- AWS A2.4 / ISO 2553. Types: fillet, groove (V, bevel, U, J), plug, slot.
- Size, length, pitch, all-around, field weld. Weld size = leg length for fillet.
- Reference line, arrow side vs other side.

## Sheet sizes and scales
- ISO: A4 (210x297), A3 (297x420), A2, A1, A0. ANSI: Letter, Tabloid, C, D, E.
- Scale: 1:1, 1:2, 1:5, 1:10, 2:1, etc. State on drawing.

## Drawing checklists
- All features dimensioned? No redundant dims? Tolerances specified?
- GD&T applied where function requires? Datum reference frame defined?
- Material and finish specified? Title block complete? Scale stated?
- Standard declared? Revision block present?

## AI rules
- Always include title block with standard declaration.
- Use baseline dimensioning for accuracy (avoid chain).
- Apply GD&T only where function requires (position for holes, flatness for seals).
- Specify surface finish only on functional surfaces.
- Default to ISO 2768-m for unmarked tolerances.