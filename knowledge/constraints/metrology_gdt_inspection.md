# Metrology and GD&T inspection constraints (from research)

Sources: research_notes/Filling senior CAD knowledge gaps/metrology_gdt_inspection.md;
Jain, Krulikowski, ASME Y14.5.1, ISO 10360, GUM.

## Measurement tools
- Calipers: +/-0.02-0.05mm. Micrometers: +/-0.001-0.005mm. Dial indicators:
  +/-0.001-0.01mm. Height gauges: +/-0.01mm.
- Bore gauges: +/-0.001-0.005mm. Thread gauges: go/no-go. Feeler gauges: 0.05-1mm.
- CMM: touch (discrete points) or scanning (continuous). Accuracy 1-5 microns.
  Types: bridge (most common), cantilever (small parts), gantry (large parts).

## GD&T inspection
- Position: measure actual feature location vs. true position; calculate deviation
  from datum reference frame. Formula: position tolerance = 2*sqrt(dx^2+dy^2).
- Flatness: measure points on surface; fit to parallel planes; max-min.
- Perpendicularity: measure angle between surface and datum; convert to tolerance zone.
- Runout: rotate part about datum axis; measure radial variation (circular runout)
  or full surface variation (total runout).
- Profile: measure points against theoretical profile; calculate deviation.
- Datum establishment on CMM: primary (3 points), secondary (2 points), tertiary
  (1 point) = 3-2-1 principle.

## Surface finish measurement
- Stylus profilometer: contact, most common. Ra (average), Rz (max height).
  Cutoff length: 0.8mm for Ra 0.1-2, 2.5mm for 2-10, 8mm for >10.
- Optical: non-contact (white light interferometry, confocal). For soft materials.
- Comparison blocks: visual/tactile comparison to standard samples.

## Measurement uncertainty
- Type A: statistical (repeated measurements). Type B: from calibration certs,
  resolution, temperature. Combined: u_c = sqrt(sum of squares). Expanded: U =
  k * u_c (k=2 for 95% confidence).

## Inspection plans
- First article inspection (FAI): verify first production part against drawing.
  AS9102 for aerospace. Record all dimensions and GD&T.
- In-process: check critical dimensions during production. Sampling (AQL).
- Final inspection: verify all requirements before shipment.

## Common pitfalls
- Measuring on wrong datum (datum not established correctly).
- Temperature effects: parts expand/contract. Measure at 20C (standard).
- Part deformation under clamping: use minimal clamping force.
- Dirty surfaces: clean before measuring.
- Probe radius compensation: CMM probes have radius; software compensates.
- Measuring form on a CMM: use enough points (minimum 3 for flatness, more for
  complex surfaces).

## AI rules
- Always specify measurement method for critical dimensions.
- Use go/no-go gauges for production (fast, cheap).
- CMM for complex GD&T and first article inspection.
- Specify surface finish measurement method (Ra/Rz, cutoff length).
- Flag unverified measurement setups; require calibration records.