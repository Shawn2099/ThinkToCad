# Materials selection and failure constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/materials_selection_failure.md;
Ashby, Callister, Dieter, Dowling, ASM Handbook.

## Material properties (key)
- Strength: yield (Sy), ultimate (Su), fatigue endurance limit (Se).
- Stiffness: Young's modulus (E), shear modulus (G), Poisson's ratio (nu).
- Density (rho), hardness (HRC/HB), toughness (K_IC), ductility (% elongation).
- Thermal: conductivity (k), expansion (alpha), specific heat (cp).
- Process: machinability, weldability, formability, castability.

## Material selection (Ashby method)
- Performance index: maximize M = property ratio (e.g., strength/density for
  lightweight, E^(1/2)/rho for stiff+light, E^(1/3)/rho for stiff+light+cheap).
- Screen by constraints (max temp, corrosion, cost, manufacturability), then rank
  by performance index, then refine with local factors (availability, supplier).
- Use Ashby charts (strength vs density, stiffness vs density) for visual selection.

## Failure modes
- Yielding: von Mises (ductile) or Tresca. Safety factor SF = Sy / sigma_vm.
- Fatigue: S-N (high cycle, >1e3 cycles), strain-life (low cycle). Goodman:
  sigma_a/Se + sigma_m/Su = 1. Soderberg (more conservative): sigma_a/Se +
  sigma_m/Sy = 1. Gerber (less conservative, curved).
- Marin factors for endurance limit: Se = ka*kb*kc*kd*ke*kf*Se'.
- Fracture: K_IC = Y*sigma*sqrt(pi*a). Use for brittle materials or crack-prone.
- Creep: for high temp (>0.4 Tm). Rupture life, creep rate.
- Wear: adhesive, abrasive, corrosive, fretting. Hardness and lubrication matter.
- Corrosion: galvanic (dissimilar metals), pitting, stress corrosion cracking.

## Common engineering materials
- Steels: 1018 (general), 1045 (shafts), 4140 (high strength), 4340 (aerospace),
  304/316 SS (corrosion), tool steels (hardness).
- Aluminum: 6061-T6 (general), 7075-T6 (high strength, aerospace).
- Brass/bronze: bearing surfaces, corrosion resistance.
- Plastics: Delrin (POM, low friction), nylon (tough), UHMWPE (wear), PEEK (high temp).
- Composites: CFRP/GFRP for lightweight, anisotropic (design for fiber direction).

## Heat treatment
- Annealing: soften, improve ductility. Normalizing: refine grain.
- Hardening + tempering: increase strength/hardness. Case hardening (carburizing,
  nitriding): hard surface, tough core.
- Precipitation hardening: age hardening (7075-T6, 17-4 PH).

## Standards
- AISI/SAE steel grades (10xx, 41xx, 43xx). ASTM (A36, A572, etc.). ISO/EN.
- Always cross-check property tables against supplier datasheets (ASM Handbook).

## AI rules
- Never use textbook property tables as design allowables; use supplier datasheets.
- Apply appropriate safety factor (1.5-4.0) based on load certainty and consequence.
- For fatigue, always check: mean stress, stress concentration, surface finish factor.
- Match material to manufacturing process (machinability, weldability, castability).