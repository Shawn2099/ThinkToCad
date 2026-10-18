# Drawing Standards (Engineering Drawings)

Research notes for an AI design assistant generating TechDraw output. Sources: Wikipedia (Engineering drawing, ISO 128, ISO 7200, GD&T, Surface finish, Dimensioning on drawings), Engineering LibreTexts section views, ASME Y14.100 page, ISO 2768 / NORAMARK chart, ISO 2768 general-tolerance document. Items not directly sourced are flagged.

## 1. Drawing views (orthographic, isometric, sections, auxiliary, detail)

### Takeaway
Use the minimum set of orthographic views (front + top + right side is the core group) plus isometric for visualization; add section views only to expose internal features; follow first-angle (ISO/Europe) or third-angle (US/Canada) projection consistently and mark it with the projection symbol.

### Cited Findings
- Multiview projection shows the object as seen from front, right, left, top, bottom, back; views are positioned by first-angle or third-angle projection rules — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- First-angle projection (ISO standard, primarily Europe): projectors originate as if from behind the viewer onto the plane behind the object; top view is under the front view, right view is at the left of the front view. Third-angle projection (primarily US/Canada, default per ASME Y14.3M): projectors originate from the far side onto the plane in front; left view on left, top view on top — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Not all six principal views are required; generally only as many views as are necessary to convey all needed information clearly and economically — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Auxiliary view: an orthographic view projected onto a plane other than the six primary planes; used when an object contains an inclined plane so that plane (and other significant features) appear in true size and shape; requires the line of sight perpendicular to the referenced plane — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Isometric projection: axonometric projection with equal scales along each axis; corresponds to rotation of ±45° about the vertical axis then ±35.264° about the horizontal axis from an orthographic view — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Full section: cutting plane passes straight through the entire portion of the part. Half section: shows half the part sectioned and half as exterior; reserved for symmetrical parts; a center line separates the halves. Offset section: cutting plane offset/bent to capture misaligned features; offsets not shown as lines in the section view. Broken-out section: partial section within an existing view, separated by a short freehand break line; no cutting plane line. Revolved section: cross-section rotated 90° about its axis and superimposed on the existing view. Removed section: taken out of alignment and placed elsewhere (may use a different scale). Aligned section: inclined feature imagined rotated to align with a principal axis to show true shape/size — [Engineering LibreTexts 3.2 Section Views](https://eng.libretexts.org/Courses/Illinois_Institute_of_Technology/Introduction_to_Engineering_Drawing_and_Design/03%3A_Module_C_-__Auxiliary_views_section_views_isometric_and_oblique_projections/3.02%3A_Section_Views); [WTCS Blueprint Reading ch. 11](https://wtcs.pressbooks.pub/blueprintreading/chapter/11-section-views/).
- Hidden lines are typically omitted in section views because internal features are shown in section; webs, ribs, and spokes are not hatched even when cut by the cutting plane — [Engineering LibreTexts 3.2](https://eng.libretexts.org/Courses/Illinois_Institute_of_Technology/Introduction_to_Engineering_Drawing_and_Design/03%3A_Module_C_-__Auxiliary_views_section_views_isometric_and_oblique_projections/3.02%3A_Section_Views).
- Rotating parts (shafts except complex inner contours), axes, cones, bolts, and standardized parts (pins, screws, rivets, nuts, washers) are not sectioned when their symmetry axis lies in the drawing plane (DIN ISO 128-3) — [TU Darmstadt CAD norm info](https://www.iim.maschinenbau.tu-darmstadt.de/CAD-Tutorial/CAD-Norminfo/2_basics_for_standardcompliant_design_of_technical_drawings/2_view_cuts_and_hatching/index.en.html).

### Inferences
- For TechDraw, default to front/top/right in third-angle for US contexts (or first-angle for ISO/EU contexts) and add a section view only where internal features are not clear from hidden lines; do not section standard hardware.
- Broken-out sections are cheaper than full sections for a single local detail.

### Gaps
- ASME Y14.3 projection symbol placement and exact view-naming conventions not fetched from primary standard; only Wikipedia-level description used.

## 2. Dimensioning (linear, angular, radial, diametral, ordinate, chain, baseline, tabular)

### Takeaway
Dimension each feature once, in the view that best defines it, using ISO 129-1 presentation rules; prefer baseline/ordinate coordinate dimensioning for hole patterns to avoid tolerance stack-up; keep dimensions aligned, uniform, and off hidden lines.

### Cited Findings
- ISO 129-1:2018 governs presentation of dimensions and tolerances on technical drawings; ISO 2768-1/2 define general tolerances — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Linear dimensions use extension lines spaced at the feature distance plus a perpendicular dimension line with arrowheads; the value is placed at the midpoint. Ordinate dimensions use one horizontal and one vertical extension line to establish a common origin (marked 0) and other features are located by x/y distances — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Circular features: radial dimensions use "R" + value; diametral dimensions use the diameter symbol (⌀) + value; a radially aligned leader points to the feature. Symbols: □ square, ⌀ diameter, R radius, SR spherical radius, S⌀ spherical diameter — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing); [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Repetitive elements: a single dimension line carrying "count × value = total" — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Dimensioning types: coordinate (polar or baseline), tabulated (letters with a value table), parallel/baseline (common origin), combined — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Auxiliary dimensions are placed in parentheses; verification dimensions in a rounded box; equal dimensions may be replaced by "=" — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Dimension components: dimension number, dimension line, auxiliary/projection lines, extension/reference lines, note lines, symbols, endpoints (15° isosceles triangle arrowhead) — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Fundamental rules: dimension lines must not cross anything; extension lines meet dimension lines at 90°; dimensions aligned/ordered with one line above another; detail dimensions closest to the part then general; the leader must not touch the visible profile; hidden lines must not be dimensioned; spacing uniform; arrowhead length ≈ numeral height; leader to a circle must be radial; dimension lines must not cross extension lines or coincide with object lines; decimal point/comma clear; numbers outside hatched areas; axes/edges never used as dimension lines; chords/angles/arcs dimensioned two ways (parallel or concentric) — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Arrangement rules: include all dimensions needed to make the part; do not duplicate dimensions across views; do not dimension from hidden lines (break the part if needed); a single extension line cannot serve two views — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Symmetrical parts: partial dimension line ending in an arrow at the extension line, the other end protruding slightly past the axis of symmetry; dimension placed on the right — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Revised dimensions: cross out the old (still legible) and place the new next to it; the new value takes precedence over scale; dimensions at a different scale are underlined — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).

### Inferences
- For TechDraw, use baseline/ordinate dimensioning for bolt-hole circles and slot patterns to keep each feature's tolerance independent of others; avoid chain dimensioning on critical fits.
- Auxiliary (parenthesized) dimensions can document derived sizes without creating a second controlling requirement.

### Gaps
- ASME Y14.43 specific chain/baseline/ordinate rules were not fetched; only ISO 129-1 and the Wikipedia synthesis are cited.
- Whether TechDraw natively emits ordinate dimensions is a tool-capability question, out of research scope.

## 3. Tolerancing on drawings (unilateral, bilateral, limit, GD&T, general/ISO 2768)

### Takeaway
Every dimension must carry a tolerance (direct ±, limit, or a GD&T feature control frame) or fall under a general tolerance block (ISO 2768 class); state the invoked standard on the drawing; do not mix ASME envelope and ISO GPS assumptions.

### Cited Findings
- ASME Y14.5 fundamental rules: (1) all dimensions must have a tolerance (plus/minus directly, from a general block/note, or geometric for basic dimensions); exceptions are min, max, stock, and reference dimensions; (2) dimensions and tolerancing must fully define each feature and measurement from the drawing is not allowed; (3) minimum number of dimensions; (4) dimensions arranged to represent function and mating with one unambiguous interpretation; (5) no explicit manufacturing methods; (6) manufacturing-only dimensions marked non-mandatory; (7) maximum readability, applied to visible lines in true profiles; (8) gauge/code dimensions given with the gauge/code number in parentheses; (9) 90° angles assumed when lines are shown at right angles without a specified angle; (10) basic 90° assumed for patterns; (11) basic zero assumed where axes/center planes/surfaces are shown coincident; (12) valid at 20 °C and 101.3 kPa unless stated; (13) free-state unless stated; (14) apply to full length/width/depth unless stated; (15) apply at the drawing level; (16) coordinate systems right-handed with labeled axes and positive directions — [Wikipedia: GD&T](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Geometric tolerance types in a feature control frame: equal bilateral, unequal bilateral, unilateral, or floating zone; profile tolerances are equal bilateral unless otherwise specified; position tolerances are always equal bilateral — [Wikipedia: GD&T](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- ISO 2768-1: general (default) tolerances for linear and angular dimensions without individual tolerance indications, in four classes f (fine), m (medium), c (coarse), v (very coarse); applies to metal removal and sheet metal; linear tolerances by basic size range; angular tolerances by shorter side length; invoke via title block, e.g. "GENERAL TOLERANCE ISO 2768 - m" — [ISO 2768-1:1989](https://www.iso.org/standard/7748.html); [NORAMARK ISO 2768 chart](https://www.noramark.com/resources/charts/iso-2768-general-tolerances/).
- ISO 2768-1 linear deviations (mm), by size range: 0.5–3: ±0.05/0.10/0.20/—; 3–6: ±0.05/0.10/0.30/0.50; 6–30: ±0.10/0.20/0.50/1.00; 30–120: ±0.15/0.30/0.80/1.50; 120–400: ±0.20/0.50/1.20/2.50; 400–1000: ±0.30/0.80/2.00/4.00; 1000–2000: ±0.50/1.20/3.00/6.00; 2000–4000: —/2.00/4.00/8.00 (f/m/c/v) — [NORAMARK ISO 2768 chart](https://www.noramark.com/resources/charts/iso-2768-general-tolerances/).
- ISO 2768-2 covers general geometric tolerances for features without individual tolerance indications — [ISO 2768-1:1989](https://www.iso.org/standard/7748.html).
- A revised ISO 2768 is under publication (expected 2026-10) and will replace ISO 2768-1:1989 — [ISO 2768](https://www.iso.org/standard/85741.html).
- ASME Y14.5 envelope principle (Rule #1) versus ISO GPS independency principle (ISO 8015); ISO GPS invocation principle: invoking part of the ISO GPS system invokes the entire system — [SV-JME 2023 overview](https://doi.org/10.5545/sv-jme.2023.753).
- A new ISO 22081 addresses general geometrical and size specifications — [GlobalSpec ISO 22081](https://standards.globalspec.com/std/14223152/iso-22081).

### Inferences
- For TechDraw, set the general tolerance in the title block as "ISO 2768-m" (or f/c/v) and tolerance only functional/critical dimensions individually; use feature control frames for GD&T (see gdt_tolerancing.md).
- Avoid mixing ASME Y14.5 envelope-rule drawings with ISO GPS-invoked drawings on the same project.

### Gaps
- Plain-dimension unilateral/bilateral/limit tolerance notation rules were not separately sourced; treated as standard knowledge.
- Imperial (inch) conversion tables for ISO 2768 were not verified for this note.
- gdt_tolerancing.md was referenced but not read; GD&T details here are limited to the Wikipedia summary.

## 4. Title block (fields, revision block, zones, scale, projection)

### Takeaway
Every drawing must have a title block (ISO 7200 defines eight mandatory fields); add a revision block, zone grid, scale, projection symbol, units, default tolerances, and the "DO NOT SCALE DRAWING" note.

### Cited Findings
- Every engineering drawing must have a title block conveying: drawing title, drawing number, part number(s), design activity name, identifying code (e.g. CAGE code), address, measurement units, default tolerances, boilerplate general specs, and IP-rights warning — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- ISO 7200 (Technical product documentation — Data fields in title blocks and document headers) standardizes eight mandatory data fields: Title; Created by; Approved by; Legal owner; Document type; Drawing number; Sheet number and total sheets; Date of issue — [Wikipedia: ISO 7200](https://en.wikipedia.org/wiki/ISO_7200).
- Revisions block: a tabulated list of drawing revisions documenting revision control; traditionally at top right — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Zones: drawing divided by an alphanumeric grid with labels along margins (A–D up the sides, 1–6 along top/bottom); zone names like A5, D2, B1 — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Scale: drawings are scale drawings at a stated ratio; include "DO NOT SCALE DRAWING"; label "NTS" if not to scale — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Projection: first-angle (ISO, Europe) vs third-angle (US/Canada, ASME Y14.3M); the determining symbol is placed in the title block/frame — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Title block traditional locations: bottom right (most common), top right, or center — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Notes list: general notes (apply to whole drawing) and flagnotes/delta notes (apply only where flagged) — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- BOM/parts list: tabular list of materials and parts; traditionally above the title block or in a separate document — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Next assembly / "where used" block: list of higher assemblies using this part; commonly adjacent to the title block — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Parameter tabulations: dimensions called out by variable names (A, B, C) with a table of values per part number — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).

### Inferences
- For TechDraw, place the title block at bottom right, revision block at top right, include the projection symbol and scale, units, and default tolerance (ISO 2768-m), plus "DO NOT SCALE DRAWING".

### Gaps
- Exact ASME Y14.1 title block dimensions and revision-block format (Y14.35) were not fetched.

## 5. Drawing types (detail, assembly, BOM, exploded view, installation)

### Takeaway
A detail drawing fully defines one part; an assembly drawing (master drawing) ties parts together with quantities, materials, and cross-references; BOM/parts list, exploded view, and installation drawing convey assembly and service information.

### Cited Findings
- Detail drawing: specifies the geometry necessary for construction of a single component; usually several drawings needed per component — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Assembly drawing ("master drawing"): gives drawing numbers of detailed components, quantities required, construction materials, and possibly 3D images to locate items — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- BOM/parts list (list of materials): tabular list of materials used to make a part and parts used to make an assembly; may include heat treatment and finishing per part number; sometimes a separate document — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- Exploded view: referenced as a CAD/assembly presentation type (linked from the engineering drawing template) — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- ISO 7519 covers principles of presentation for assembly drawings (related standard) — [Wikipedia: ISO 128](https://en.wikipedia.org/wiki/ISO_128).
- An engineering drawing is a legal instrument: the purchase order plus the drawing plus ancillary specs constitute the contract — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).

### Inferences
- TechDraw should emit one detail drawing per part and one assembly drawing containing a BOM table and (optionally) an exploded view for assembly guidance.

### Gaps
- Installation-drawing conventions and exploded-view dimensioning rules were not sourced; flagged as unverified.

## 6. Standards (ASME Y14.x series, ISO 128/129/1302)

### Takeaway
Invoke one coherent standard set on the drawing: ASME Y14 series for US practice (Y14.100 practices, Y14.5 GD&T, Y14.3 projections, Y14.1 sheets, Y14.2 lines, Y14.6 threads, Y14.43 dimensioning) or ISO 128/129/1302/7200 for international practice.

### Cited Findings
- ASME Y14.100-2017 establishes essential requirements and reference documents for preparation and revision of engineering drawings and associated lists; intended to be used with ASME Y14.24, Y14.34, Y14.35, Y14.41; incorporates Y14.42 digital approval — [ASME Y14.100](https://www.asme.org/codes-standards/find-codes-standards/y14-100-engineering-drawing-practices).
- ASME Y14.5-2018 (R2024) and Y14.100-2017 package establishes uniform practices for stating and interpreting dimensioning and tolerancing and essential drawing-preparation requirements — [ANSI webstore](https://webstore.ansi.org/standards/asme/asmey14100dimensioning).
- ISO 128: general principles of presentation in technical drawings (graphical representation); ISO 128-1 introduction/fundamental requirements, -2 basic conventions for lines, -3 views/sections/cuts, -100 index; applies to manual and computer-based drawings but not 3D CAD models — [Wikipedia: ISO 128](https://en.wikipedia.org/wiki/ISO_128).
- ISO 129: technical drawings — indication of dimensions and tolerances; ISO 129-1:2018 general principles — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings) (related standards in ISO 128 wiki).
- ISO 1302: indication of surface texture in technical product documentation (ISO GPS general standard) — [Wikipedia: GD&T](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing); surface finish wiki notes ISO 1302:2002 was withdrawn in favor of ISO 21920-1:2021 — [Wikipedia: Surface finish](https://en.wikipedia.org/wiki/Surface_finish).
- ISO 5457: sizes and layout of drawing sheets; ISO 5455: scales; ISO 7519: presentation of assembly drawings; ISO 216: paper sizes — [Wikipedia: ISO 128](https://en.wikipedia.org/wiki/ISO_128).
- ASME Y14.3M: projection standard (third-angle default in US/Canada); ASME Y14.1: sheet sizes; ASME Y14.2: line conventions — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- ISO 7200: title block data fields — [Wikipedia: ISO 7200](https://en.wikipedia.org/wiki/ISO_7200).

### Inferences
- State the invoked standard on the drawing (e.g., "DIMENSIONING AND TOLERANCING PER ASME Y14.5" or "ISO 129-1"), since invoking part of ISO GPS invokes the entire system.

### Gaps
- Y14.6 (screw threads), Y14.43 (dimensioning), Y14.2 (line conventions) specifics were not fetched; only named. Y14.3 projection details beyond Wikipedia not sourced.

## 7. Surface finish symbols (Ra, Rz, Rq, lay, manufacturing method)

### Takeaway
Surface texture is defined by lay, roughness (Ra/Rz/Rq), and waviness; specify via ASME Y14.36M (US) or ISO 1302/ISO 21920-1 (international) with the parameter value and lay symbol when function requires.

### Cited Findings
- Surface finish (surface texture) comprises three characteristics: lay, surface roughness, and waviness; lay is the predominant surface pattern direction, ordinarily determined by the production method — [Wikipedia: Surface finish](https://en.wikipedia.org/wiki/Surface_finish).
- Surface roughness is the usual meaning of "surface finish" in engineering; lower number = smoother; measured by contact (profilometer stylus) or non-contact (interferometry, confocal, etc.) methods — [Wikipedia: Surface finish](https://en.wikipedia.org/wiki/Surface_finish).
- Specification standards: US uses ASME Y14.36M; international ISO 1302:2002 (withdrawn in favor of ISO 21920-1:2021) — [Wikipedia: Surface finish](https://en.wikipedia.org/wiki/Surface_finish).
- ISO 1302 is listed among ISO GPS general standards for surface texture; related: ISO 4287 (profile terms), ISO 4288 (assessment rules), ISO 25178 (areal texture) — [Wikipedia: GD&T](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Cost generally rises as surface finish improves; manufacturing process capability and roughness are linked — [Wikipedia: Surface finish](https://en.wikipedia.org/wiki/Surface_finish).

### Inferences
- For TechDraw, add a surface finish symbol with Ra value and lay symbol on functional surfaces (sliding/sealing/bearing); leave non-functional surfaces to process capability.

### Gaps
- Exact symbol geometry, parameter definitions (Ra vs Rz vs Rq), and lay-symbol letters (=, ⊥, X, M, C, R) were not sourced from ISO 1302/ISO 21920; flagged unverified.

## 8. Weld symbols (AWS A2.4)

### Takeaway
Weld symbols per AWS A2.4 communicate weld type, size, length, pitch, and supplementary conditions (all-around, field weld, contour/finish) via a reference line, arrow, and tail; AWS D1.1 is the structural welding code adopted by ANSI.

### Cited Findings
- AWS publishes codes on welding; AWS D1.1 covers general requirements for structural welding and has been adopted by ANSI as a US national standard — [Wikipedia: American Welding Society](https://en.wikipedia.org/wiki/American_Welding_Society).
- AWS A2.4 is cited (task scope) as the standard for weld symbols; detailed symbol rules were not fetched from a primary source in this research — unverified.

### Inferences
- For TechDraw, support basic weld symbols (fillet, groove V/U/J/bevel) with size and length, plus all-around and field-weld supplementary symbols.

### Gaps
- All weld-symbol specifics (reference line/arrow/tail layout, weld type symbols, size/length/pitch placement, all-around/field weld markers, contour/finish symbols) are flagged unverified; recommend separate verification against AWS A2.4.

## 9. Sheet sizes and scales

### Takeaway
Use ISO A-series (A0–A4, constant 1:√2 aspect ratio) or ANSI/ASME Y14.1 (A–E); state scale in the title block; never scale the drawing; label NTS if not to scale.

### Cited Findings
- Drawing sizes typically comply with ISO (world standard) or ANSI/ASME Y14.1 (American); metric sizes correspond to ISO paper sizes; US customary A-size corresponds to letter, B-size to ledger/tabloid — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- All ISO paper sizes share the same aspect ratio 1:√2, allowing enlargement/reduction between sizes without wasted space — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- ISO 5457 covers sizes and layout of drawing sheets; ISO 5455 covers scales; ISO 216 covers paper sizes — [Wikipedia: ISO 128](https://en.wikipedia.org/wiki/ISO_128).
- Scale is stated as a ratio; "DO NOT SCALE DRAWING" boilerplate is common — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).

### Inferences
- For TechDraw, default to A3 or A4 (ISO) or ANSI B/C; put the scale in the title block; include "DO NOT SCALE DRAWING".

### Gaps
- Exact ANSI sheet dimensions (A 8.5×11 in, B 11×17, C 17×22, D 22×34, E 34×44) and ISO A-series millimetre dimensions are from standard knowledge, not sourced here; flagged unverified.

## 10. Drawing checklists and common errors

### Takeaway
A compliant drawing has a complete title block, sufficient but minimal views, no hidden-line dimensioning, one dimension per feature, a tolerance on every dimension (or a general block), conventional sectioning, a declared projection/scale, and no scaling assumptions.

### Cited Findings
- Key information such as dimensions is specified in one place to avoid redundancy and inconsistency; only requirements are specified; suitable tolerances given for critical dimensions — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).
- ASME Y14.5 rules imply common errors: undimensioned features, assuming dimensions, redundant dimensions, specifying manufacturing methods, dimensions not on visible lines in true profiles, non-right-handed coordinates — [Wikipedia: GD&T](https://en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing).
- Dimensioning rules imply errors: crossing dimension lines, dimensioning hidden lines, using axes/edges as dimension lines, duplicating dimensions across views, non-uniform spacing — [Wikipedia: Dimensioning on drawings](https://en.wikipedia.org/wiki/Dimensioning_on_drawings).
- Section-view conventions: hidden lines omitted unless needed; webs/ribs/spokes not hatched; standard hardware not sectioned — [Engineering LibreTexts 3.2](https://eng.libretexts.org/Courses/Illinois_Institute_of_Technology/Introduction_to_Engineering_Drawing_and_Design/03%3A_Module_C_-__Auxiliary_views_section_views_isometric_and_oblique_projections/3.02%3A_Section_Views).
- Scale: never scale a drawing; label NTS when not to scale — [Wikipedia: Engineering drawing](https://en.wikipedia.org/wiki/Engineering_drawing).

### Inferences
- TechDraw should run a pre-release checklist: all features dimensioned once; no hidden-line dims; tolerance on every dim or general block; title block complete (ISO 7200 fields); projection symbol present; views sufficient but minimal; sections follow conventions; invoked standard stated.

### Gaps
- No single formal checklist standard was sourced; this list is synthesized from the rules above (inference).
