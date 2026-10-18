# Surface finish constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/surface_finish.md;
ISO 1302, ISO 25178, ASME B46.1.

## Roughness parameters
- Ra: arithmetic average roughness (most common). Rz: average max height. Rq: RMS.
  Rt: total height. Rmax: max peak-to-valley. Rsk: skewness. Rku: kurtosis.
- Grade numbers N1-N12 correspond to Ra values (N1 = 0.025 Ra, N12 = 50 Ra).
- Areal parameters (ISO 25178): Sa, Sq, Ssk, Sku for 3D surface texture.

## Typical finishes by process
- Turned: 1.6-3.2 Ra. Milled: 1.6-6.3. Ground: 0.4-1.6. Polished: 0.1-0.4.
- As-cast: 6.3-25. As-forged: 3.2-12.5. 3D printed: varies (FDM 10-25, SLA 0.5-2).
- Default (as-machined): 3.2 Ra for non-functional surfaces.

## Functional effects
- Friction/wear: lower Ra reduces friction and wear. Bearing surfaces need 0.4-0.8.
- Fatigue: surface finish affects endurance limit (Marin factor ka). Rougher = lower fatigue life.
- Corrosion: rougher surfaces corrode faster (crevices). Sealing: need 0.8-1.6 for gaskets.
- Coating adhesion: moderate roughness (1.6-3.2) improves adhesion.

## Measurement
- Stylus profilometer: contact, most common. Optical: non-contact, for soft materials.
- Comparison blocks: visual/tactile comparison to standard samples.
- Cutoff length: 0.8mm for Ra 0.1-2, 2.5mm for 2-10, 8mm for >10.

## DFM rules
- Specify finish only where function requires (cost driver).
- Default finish for unmarked surfaces (ISO 2768 or shop default).
- Avoid over-specifying (0.1 Ra on non-functional surfaces = wasted cost).
- Match finish to process capability (don't spec ground finish on as-cast part).
- Consider lay direction for sealing surfaces (perpendicular to leak path).