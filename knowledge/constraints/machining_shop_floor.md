# Machining and shop-floor constraints (from research)

Sources: research_notes/Filling senior CAD knowledge gaps/machining_shop_floor.md;
Machinery's Handbook, Kalpakjian & Schmid, Groover.

## Speeds and feeds (baseline)
- HSS cutting speed x1; carbide x3-5 (coated carbide higher).
- Coatings: TiN (general, +20% speed), TiAlN (high temp, +50%), AlTiN (dry/high
  speed). Hardness 2000-3000 HV, max temp 600-1000C.
- Tool life: Taylor equation V*T^n = C. Typical n=0.1-0.5.

## Operations
- Turning: roughing (high feed, depth) then finishing (low feed, high speed).
- Milling: face (flat surfaces), end (slots/pockets), slot (narrow cuts).
- Drilling: peck drilling for deep holes (>3x diameter), through vs blind.
- Boring: enlarge existing holes to precision. Reaming: finish to +/-0.01mm.
- Tapping: use tap drill (slightly larger than minor diameter). Thread milling
  for large threads.

## DFM for machining
- Min wall thickness: 1mm (aluminum), 1.5mm (steel). Min hole diameter: 1mm.
- Aspect ratio (depth/diameter): < 3 for drilling, < 5 for boring.
- Corner radius >= tool radius (no sharp internal corners). Standard radii:
  0.5, 1, 1.5, 2, 3, 5mm.
- Standard drill sizes: use metric (1, 1.5, 2, 2.5, ..., 10, 10.5, ...) or
  letter/number drills. Avoid odd diameters.
- Thread engagement: 1.0*d steel, 1.5*d cast iron, 2.0-2.5*d aluminum/plastic.
- Tolerances: rough +/-0.1mm, finish +/-0.025mm, grinding +/-0.005mm,
  lapping +/-0.001mm.

## Shop-floor knowledge
- Chatter: reduce depth of cut, increase speed, change tool geometry, add damping.
- Tool wear: flank (abrasion), crater (diffusion), BUE (built-up edge, low speed),
  notch (work hardening at depth of cut). Replace before failure.
- Work hardening: stainless steel, titanium. Use sharp tools, high speed, low feed.
- Burrs: minimize with sharp tools, proper feed; deburr after machining.
- Coolant: flood for steel/aluminum, mist for finishing, dry for cast iron/titanium.
  Coolant extends tool life 2-5x.

## Surface finish by process
- Turned: 1.6-3.2 Ra. Milled: 1.6-6.3. Ground: 0.4-1.6. Polished: 0.1-0.4.
- Honed: 0.1-0.8. Lapped: 0.05-0.2. As-cast: 6.3-25.
- Cost scales with finish: each halving of Ra ~2x cost.

## Fixturing
- Vise: general purpose, jaw width limits. Soft jaws for delicate parts.
- Collets: precision, round parts. Chucks: large parts, 3-jaw (quick) or
  4-jaw (precise). Clamps: irregular shapes.
- Access: ensure tool can reach all features; avoid fixturing over machined surfaces.

## AI rules
- Use standard drill sizes and tool radii. Avoid odd diameters.
- Specify finish only where function requires (cost).
- Default tolerance +/-0.1mm for machined parts; +/-0.025mm for precision.
- Check tool access for all features; flag inaccessible features.
- Prefer machining for prototypes/low volume; casting/forging for high volume.