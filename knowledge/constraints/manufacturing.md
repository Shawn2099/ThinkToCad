# Manufacturing constraints (general small workshop)

- No CNC assumed; hand tools + drill press + angle grinder acceptable.
- Avoid features requiring milling (slots, pockets) unless a mill is available.
- Prefer drilling, sawing, filing, welding, bolting.
- Minimum bend radius for 2 mm sheet steel: 2 mm (1x thickness).
- Weld access: at least 30 mm clearance for electrode/hand.
- Use standard drill sizes; avoid odd diameters.
- Tolerances: +/-0.5 mm for welded assemblies, +/-0.1 mm for machined fits.

## From research (Senior CAD engineer knowledge/manufacturing_dfm.md)
- Machining: turning/milling/drilling/grinding/EDM. Tolerances +/-0.05-0.2mm,
  surface finish 0.4-3.2 Ra, min feature ~0.5mm. Constraints: tool access,
  aspect ratio < 5, corner radius >= tool radius.
- Casting: sand/die/investment. Draft angles 1-3 deg, wall thickness 3-6mm,
  fillets R>=3mm, shrinkage allowance 1-2%. Porosity risk in thick sections.
- Sheet metal: min bend radius = 1x thickness (steel), K-factor ~0.44,
  springback compensation. Hole-to-edge distance >= 2x thickness. Deep draw
  LDR <= 2.0.
- Welding: fillet/butt, access >= 30mm, distortion control (symmetric welds,
  pre-bend), HAZ affects toughness. AWS D1.1 allowables.
- 3D printing: FDM (min wall 1mm, overhangs <45deg, supports), SLA (0.1mm
  layers), SLS (no supports needed). Anisotropy: strength lower in Z direction.
- Injection molding: draft 1-2 deg, wall 1.5-3mm, ribs 0.6x wall, bosses, gates,
  ejection.
- Process selection: machining for prototypes/low volume; casting/forging for high
  volume; 3D printing for complex geometry/prototypes; sheet metal for enclosures.
- Small workshop: hand tools + drill press + grinder + welder. Avoid features
  requiring milling beyond drill press. Use standard stock sizes. Buy-out
  threads/gears.