# GD&T and tolerance analysis constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/gdt_tolerancing.md;
ASME Y14.5, ISO 1101/2768/286/8015, ISO 1302.

## Symbols and categories
- 14 characteristics in 5 categories (ASME Y14.5-2009): Form (straightness, flatness,
  circularity, cylindricity), Orientation (angularity, perpendicularity, parallelism),
  Location (position, concentricity, symmetry), Profile (line, surface), Runout
  (circular, total).
- Y14.5-2018 withdrew concentricity and symmetry (12 remain). ISO 1101 retains all.
- Form controls need no datum; orientation/runout always need one; location usually;
  profile optional. Only position, straightness (axis), orientation controls can take
  MMC/LMC modifiers; profile/runout/concentricity/symmetry are RFS only.

## ASME vs ISO GPS
- ASME Y14.5 is one self-contained document (editions 1982/1994/2009/2018);
  ISO GPS is a family (ISO 1101, 128, 129, 2768, 286, 8015, 14405, 5459, 2692).
- ASME default = envelope (Rule #1: size controls form at MMC) unless independency
  noted. ISO default = independency (ISO 8015) unless envelope symbol (E) applied.
- ISO uses MMR/LMR/RPR (ISO 2692) instead of MMC/LMC. Mixing defaults causes
  misinterpretation: declare the governing standard in the title block.

## Standard fits (ISO 286)
- Hole-basis (H) preferred: H11/c11 loose running; H9/d9 free running; H8/f7 close
  running; H7/g6 sliding; H7/h6 locational clearance; H7/k6, H7/n6 locational
  transition; H7/p6, H7/s6, H7/u6 interference.
- Default to H7 bores and vary shaft letter by function; use shaft-basis (h6) only
  when the shaft is the constrained feature (dowel pins).
- Transition fits cannot guarantee motion or torque; use clearance or interference.

## Tolerance stack-up
- Worst-case: arithmetic sum, 100% coverage, conservative, costly. Use for
  safety-critical or low-volume.
- RSS: sqrt(sum of squares), assumes normal + independence + linearity; ~99.73%
  within +/-3 sigma. Use for high-volume capable processes.
- Monte Carlo: random sampling; use for non-linear surfaces, non-normal, changing
  contact points. Slower but more accurate.
- Flag mean-shift risk (identical parts from one process) and thermal expansion
  (violates independence).

## Datum reference frames
- DRF = 3 mutually perpendicular planes constraining 6 DOF via 3-2-1 principle:
  primary 3 DOF (3-point contact), secondary 2 DOF (2-point), tertiary 1 DOF.
- Functional datums (mating surfaces) should be primary; arbitrary machined
  surfaces as primary cause inspection/assembly mismatches.
- Datum precedence order in FCF must be followed (left to right); reordering
  changes the DRF.

## Rules for AI
- Apply Rule #1 (envelope) by default for ASME; independency for ISO unless (E).
- Default to 12-characteristic 2018 set for new designs; use 14 (2009/ISO) only
  when drawing header invokes them.
- Never specify concentricity/symmetry for new designs; use position or runout.
- Profile of a surface is the most versatile single control (form+orientation+location).
- Hole-basis H7 default; vary shaft letter by function.
- Declare governing standard in title block. Never mix ASME and ISO defaults silently.