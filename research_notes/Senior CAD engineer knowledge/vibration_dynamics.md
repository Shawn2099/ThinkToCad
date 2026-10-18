# Vibration and Dynamics for Mechanical Design

## Free and forced vibration: SDOF, natural frequency, damping ratio, transmissibility

### Takeaway
A single-degree-of-freedom mass-spring-damper is the foundational model: natural frequency scales as √(k/m), damping ratio ζ characterizes decay vs. critical damping, and forced response shows resonance when excitation frequency approaches natural frequency; transmissibility quantifies how much vibration is transmitted through a mount.

### Cited Findings
- Undamped natural frequency: f_n = (1/2π)√(k/m), ω_n = √(k/m) — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Critical damping coefficient: c_c = 2√(km); damping ratio ζ = c/c_c = c/(2√(km)) — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration); [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Damped natural frequency: f_d = f_n√(1−ζ²); for ζ=0.1, f_d is only ~1% below f_n — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Free-vibration decay: x(t)=X e^(−ζω_n t) cos(√(1−ζ²)ω_n t − φ) — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Forced harmonic response amplitude: X = (F_0/k)/√((1−r²)²+(2ζr)²), r=f/f_n; phase φ=arctan(−2ζr/(1−r²)) — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Resonance occurs when forcing frequency nears natural frequency (r≈1); in rotor-bearing systems any rotational speed exciting a natural frequency is a critical speed — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Metal structures (airframe, crankshafts) have damping factors <0.05; automotive suspensions 0.2–0.3 — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Q factor relation: Q=1/(2ζ); ζ=α/ω_n where α is exponential decay rate — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Logarithmic decrement: δ=ln(x_0/x_1); ζ=δ/√(δ²+(2π)²) — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Percentage overshoot: PO=100 exp(−ζπ/√(1−ζ²)) — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).

### Inferences
- Increasing stiffness raises natural frequency (stiffening/detuning); increasing mass lowers it — useful for resonance avoidance by design.
- Lightly damped metal structures (ζ<0.05) amplify resonance severely; damping treatments needed near resonances.
- Transmissibility (ratio of transmitted to input vibration) follows the same denominator as forced response; isolation (T<1) requires excitation frequency well above natural frequency (typically r>√2 for passive isolators).

### Gaps
- Transmissibility closed-form T(r,ζ) not explicitly given in fetched sources; standard formula T=√(1+(2ζr)²)/√((1−r²)²+(2ζr)²) — not cited here, flag as needing verification against Rao/Inman.
- ISO 10816 velocity severity zones not fetched (no Wikipedia article); values unverified in this note.

## Multi-DOF systems: modal analysis, eigenvalues/eigenvectors, mode shapes

### Takeaway
Multi-DOF vibration reduces to an eigenvalue problem yielding natural frequencies (eigenvalues) and mode shapes (eigenvectors); modal superposition lets any response be built from modes, and modal testing validates FEA models.

### Cited Findings
- Modal analysis studies dynamic properties in the frequency domain by exciting a component to target its mode shapes and recording vibration with a sensor network — [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis).
- Modern experimental modal analysis uses accelerometers/load cells (or non-contact laser vibrometer/photogrammetry), DAQ with ADC, and host PC; SIMO, MISO (mathematically identical via reciprocity), and MIMO approaches — [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis).
- Typical excitation signals: impulse, broadband, swept sine, chirp — [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis).
- Analysis relies on Fourier analysis; transfer function reveals resonances whose modal mass, frequency, and damping ratio are estimated — [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis).
- Identification methods: SDOF vs MDOF, time-domain vs frequency-domain, least-squares fit for modal constants — [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis).
- Mode shapes can be superposed to compute response to any excitation; results correlate with FEA normal modes — [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis).
- Rotordynamic MDOF equation: M q̈ + (C+G) q̇ + (K+N) q = f(t), with symmetric M,C,K and skew-symmetric gyroscopic G; eigenvectors are spin-speed dependent — [Wikipedia, Rotordynamics](https://en.wikipedia.org/wiki/Rotordynamics).
- Rayleigh quotient / Dunkerley's method approximate first natural frequency of beams/shafts — [Wikipedia, Critical speed](https://en.wikipedia.org/wiki/Critical_speed).

### Inferences
- For design, first mode dominates; higher modes matter for broadband excitation and local component resonances.
- Operational modal analysis (ambient excitation) is needed for in-service structures where forced testing is impractical.
- Gyroscopic terms split forward/backward whirl frequencies; Campbell diagram visualizes interference with spin speed.

### Gaps
- Explicit eigenvalue formulation (K−ω²M)φ=0 and orthogonality/normalization details not in fetched sources; cite Rao/Inman/Thomson & Dahleh.
- Complex mode shapes with non-proportional damping not covered in fetched material.

## Rotating machinery: critical speed, unbalance response, balancing (static/dynamic), whirl

### Takeaway
Rotating shafts have critical speeds where spin rate matches a natural frequency; unbalance forces grow with Ω² and cause whirl, so rotors are balanced (statically in one plane, dynamically in two) and designed to pass criticals quickly or operate supercritically.

### Cited Findings
- Critical speed is the theoretical angular velocity that excites the natural frequency of a rotating object (shaft, propeller, leadscrew, gear); resonance occurs regardless of orientation — [Wikipedia, Critical speed](https://en.wikipedia.org/wiki/Critical_speed).
- Unbalanced mass of rotating parts causes deflection creating resonant vibration at critical speeds; magnitude depends on shaft/support stiffness, total mass, unbalance, damping — [Wikipedia, Critical speed](https://en.wikipedia.org/wiki/Critical_speed).
- Rayleigh–Ritz first natural frequency: ω_1 ≈ √(g Σ w_i y_i / Σ w_i y_i²); single-segment simplification ω_1 ≈ √(g/y_max); convert rad/s to RPM by ×60/(2π) — [Wikipedia, Critical speed](https://en.wikipedia.org/wiki/Critical_speed).
- Good practice: max operating speed should not exceed 75% of critical speed (citation needed in source); some systems operate supercritically, accelerating through first natural frequency quickly — [Wikipedia, Critical speed](https://en.wikipedia.org/wiki/Critical_speed).
- Jeffcott rotor: m r̈ + k r = m ε Ω² sin(Ωt); lateral oscillation (whirl) frequency Ω/2π, amplitude influenced by spin speed and dynamic amplification near natural frequency — [Wikipedia, Rotordynamics](https://en.wikipedia.org/wiki/Rotordynamics).
- Cross-coupled stiffness can drive instability if large enough relative to direct damping/stiffness — [Wikipedia, Rotordynamics](https://en.wikipedia.org/wiki/Rotordynamics).
- Campbell diagram: forward/backward whirl curves; critical speeds at intersections with synchronous spin-speed line — [Wikipedia, Rotordynamics](https://en.wikipedia.org/wiki/Rotordynamics).
- Balancing machine measures unbalance via vibration sensors on suspension; hard-bearing (rigid suspension) vs soft-bearing (moveable suspension) — [Wikipedia, Balancing machine](https://en.wikipedia.org/wiki/Balancing_machine).
- Static balancing: one plane, part rests on geometric center, two perpendicular sensors; faster/cheaper but less accurate — [Wikipedia, Balancing machine](https://en.wikipedia.org/wiki/Balancing_machine).
- Dynamic balancing: two planes (correction planes); trial weights calibrate because correction-plane locations along axis are unknown — [Wikipedia, Balancing machine](https://en.wikipedia.org/wiki/Balancing_machine).
- Portable balancing machines balance in-situ running parts (turbines, pumps, motors) with accelerometers and photocell — [Wikipedia, Balancing machine](https://en.wikipedia.org/wiki/Balancing_machine).
- Blade balancing: software sorts blades to minimize residual unbalance before final correction — [Wikipedia, Balancing machine](https://en.wikipedia.org/wiki/Balancing_machine).

### Inferences
- For rotordynamics, gyroscopic and cross-coupled terms mean eigenvalues are complex and speed-dependent; stability (not just frequency) must be checked.
- Whirl direction matters: forward whirl can lock to spin speed (synchronous) at criticals; backward whirl may cause nonsynchronous instabilities.
- Balancing to ISO 1940/21940 grades (G2.5, G6.3, etc.) is standard practice — not in fetched sources; flag as needing verification.

### Gaps
- ISO 1940/21940 balance quality grades and permissible residual unbalance formulas not in fetched sources.
- Whirl amplitude formulas and stability thresholds (e.g., cross-coupled stiffness/damping ratio) need authoritative source (Childs, Vance).
- Campbell diagram construction details beyond description.

## Vibration isolation: transmissibility, isolation efficiency, mounts, natural frequency selection

### Takeaway
Passive isolation acts as a mechanical low-pass filter: T≈1 below natural frequency, amplification at resonance (limited by damping), and roll-off above; choose mounts with natural frequency well below the lowest disturbing frequency, trading damping (less peak amplification but less high-frequency roll-off).

### Cited Findings
- Passive isolators: air (1.5–3 Hz, large systems 0.5 Hz), springs (3–9 Hz), elastomer/cork pads (3–40 Hz), molded elastomer mounts (10–20+ Hz), negative-stiffness (0.17–2.5 Hz), wire rope (10–40+ Hz), base isolators (seismic), tuned mass dampers — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).
- Negative-stiffness isolators: stiffness K=K_S−K_N, vertical/horizontal natural frequencies as low as 0.2–0.5 Hz; used for sensitive instruments/electron microscopes — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).
- Transmissibility curve: below natural frequency T≈1; at resonance amplification limited by damping; above resonance roll-off to low values. Passive isolator = mechanical low-pass filter — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).
- For any given frequency above natural frequency, lower natural frequency gives greater isolation — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).
- Damping reduces amplification at resonance but reduces high-frequency isolation (roll-off decreases as damping increases) — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).
- Passive isolation works both directions (payload from support and support from payload); subframe isolation doubles high-frequency attenuation at cost of added low-frequency modes — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).
- Active isolation uses feedback (accelerometer/geophone sensor, controller, electromagnetic/piezo actuator) for stronger suppression, used for sub-micrometer precision and semiconductor lithography — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).
- Selection factors: size, weight, movement, side effects, environment (industrial/lab, indoor/outdoor, corrosive, clean room, temperature, vacuum, magnetism, acoustic), cost, adjustment, maintenance, size constraints, vibration frequencies/amplitudes/directions, specs — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).
- ASHRAE and VISCMA provide isolator/spring-deflection specs for HVAC/building applications — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).

### Inferences
- For a machine on soft mounts, ensure operating speed > ~3× (preferably >5×) mount natural frequency to get useful isolation; otherwise amplification.
- Damping ratio selection: enough to limit resonance peak (Q) but not so much as to kill high-frequency roll-off; often ζ≈0.05–0.15 for elastomer mounts.
- Negative-stiffness/air systems needed when isolating sub-Hz (microscopy, lithography); elastomer pads adequate for machinery > a few Hz.

### Gaps
- Isolation efficiency percentage formula and mount stiffness selection equations (e.g., static deflection δ=mg/k) not explicitly in fetched sources; standard design charts needed from Harris & Piersol.
- ASHRAE/VISCMA specific deflection requirements (e.g., spring deflection ≥0.5 in for fans) not fetched.

## Damping: types (viscous, Coulomb, hysteretic), loss factor, damping treatments

### Takeaway
Damping is energy dissipation; viscous (velocity-proportional), Coulomb (constant friction), and hysteretic (displacement-proportional, material) types behave differently; loss factor η=2ζω/ω_n is preferred for material damping because ζ varies with frequency.

### Cited Findings
- Damping: loss of energy of oscillating system by dissipation; examples: viscous drag, surface friction, radiation, electrical resistance, material absorption — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Damping ratio regimes: undamped (ζ=0), underdamped (0<ζ<1), critically damped (ζ=1), overdamped (ζ>1); critical damping returns to equilibrium in minimum time — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Viscous drag: force proportional to velocity (dashpot); used in automatic/anti-slam doors — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Coulomb damping (dry friction) not detailed in fetched source; standard type in vibration texts — flag as needing Rao/Inman citation.
- Magnetic damping: eddy currents dissipate kinetic energy as heat; used in roller-coaster brakes — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Magnetorheological dampers: MR fluid viscosity changes with magnetic field — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Material damping: metals/ceramics/glass very light; polymers higher due to Van der Waals bond breaking/reforming; thermosets less than thermoplastics due to cross-linking — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Loss factor: η=2ζ(ω/ω_n); makes loss factor approximately constant over wide frequency range for light damping — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Q factor: Q=1/(2ζ); high Q = slow decay relative to oscillation (e.g., tuning fork) — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Logarithmic decrement relates adjacent peak amplitudes to ζ — [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping).
- Damping treatments: elastomer mounts, fluid dampers, constrained-layer damping, wire rope isolators; air springs for trucks — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).

### Inferences
- For vibration isolation mounts, elastomers provide both spring and damping; damping ratio increases with frequency/temperature for polymers (loss factor more stable metric).
- Hysteretic damping (structural damping) is modeled as complex stiffness k(1+iη); η≈2ζ near resonance — standard in rotordynamics.
- Adding damping is most effective when vibration is near resonance; at high frequency, damping can worsen isolation.

### Gaps
- Coulomb (dry friction) damping and hysteretic damping equations not in fetched Wikipedia sources; need Rao/Inman/Thomson.
- Specific damping treatments (constrained-layer, viscoelastic, tuned mass damper design) details not fetched beyond list.
- Temperature/frequency dependence of elastomer loss factor (master curves) not covered.

## Shock and impact: shock response spectrum, pulse duration, energy absorption

### Takeaway
Shock is characterized by SRS: peak acceleration a SDOF would experience vs its natural frequency; pulse duration and Q/damping define severity; energy absorption uses crumple zones, dampers, and packaging to limit transmitted force.

### Cited Findings
- SRS: graphical representation of a shock/transient acceleration input in terms of how an SDOF (mass on spring) would respond; horizontal axis natural frequency, vertical axis peak acceleration — [Wikipedia, Shock response spectrum](https://en.wikipedia.org/wiki/Shock_response_spectrum).
- SRS calculation: pick damping ratio/Q, pick frequency f, simulate SDOF response, record max instantaneous absolute acceleration, repeat across frequencies — [Wikipedia, Shock response spectrum](https://en.wikipedia.org/wiki/Shock_response_spectrum).
- Zero damping gives maximum response; very high damping gives horizontal line; 5% damping → Q=10; SRS plot must specify Q — [Wikipedia, Shock response spectrum](https://en.wikipedia.org/wiki/Shock_response_spectrum).
- SRS not unique (many waveforms give same SRS); does not contain full transient info; not for fatigue (loses cycle count); not for significantly nonlinear systems — [Wikipedia, Shock response spectrum](https://en.wikipedia.org/wiki/Shock_response_spectrum).
- SRS references: Harris & Piersol "Harris Shock and Vibration Handbook"; Lalanne "Mechanical Vibration and Shock Analysis"; MIL-STD-810G 516.6 — [Wikipedia, Shock response spectrum](https://en.wikipedia.org/wiki/Shock_response_spectrum).
- MIL-STD-810 shock test methods: 516.8 (functional, transportation, fragility, transit drop, crash hazard, bench handling, pendulum impact, catapult/arrested landing), 517.3 pyroshock, 519.8 gunfire shock, 522.2 ballistic shock — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).
- Energy absorption: package cushioning, shock mounts, crumple zones; MIL-STD-810 transit drop evaluates packaging — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).

### Inferences
- Design for shock: keep component natural frequencies away from SRS peaks; add damping to flatten peaks; use isolation with low natural frequency for shock (but check static deflection limits).
- Pulse duration vs natural period: if pulse is short relative to natural period, response is velocity (impulse) limited; if long, quasi-static.
- Energy absorption devices (dampers, crushable materials) trade peak force for stroke; size by impact energy ½mv².

### Gaps
- Shock pulse shapes (half-sine, triangular, trapezoidal), pulse duration effects, and shock spectra formulas not in fetched sources; need Harris & Piersol / Lalanne.
- Energy absorption design equations (e.g., crush force, stroke) not covered.
- MIL-STD-810 specific shock levels (g, ms) not extracted; standard itself must be consulted.

## Resonance avoidance: detuning, adding mass/stiffness, damping

### Takeaway
Avoid resonance by detuning (shifting natural frequency away from excitation by changing mass/stiffness), adding damping to limit amplification, and ensuring operating speed stays below ~75% of critical speed or passes quickly through it.

### Cited Findings
- Resonance: when forcing frequency nears natural frequency, amplitude can become extremely high in lightly damped systems — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Natural frequency formula f_n=(1/2π)√(k/m): increasing stiffness raises f_n; increasing mass lowers f_n — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Critical speed practice: max operating speed should not exceed 75% of critical speed (citation needed in source); supercritical operation possible by rapid acceleration through first natural frequency — [Wikipedia, Critical speed](https://en.wikipedia.org/wiki/Critical_speed).
- Bridge design: keep natural frequencies away from excitation (footsteps, wind); groups break step to avoid synchronous excitation — [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis).
- Buildings: natural frequency must not match expected earthquake frequency — [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis).
- Damping reduces amplification at resonance; metal structures need damping treatments (ζ<0.05) — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Tuned mass dampers reduce harmonic vibration in buildings/structures with narrow-band mass — [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation).

### Inferences
- Design rules: (1) compute all natural frequencies (FEA/modal test); (2) compare to excitation spectrum (rotor speed × harmonics, gear mesh, blade pass, motor electrical); (3) detune by ≥20–30% (rule of thumb, not sourced); (4) add damping if detuning impossible; (5) stiffen supports to raise natural frequencies above excitation.
- Adding mass lowers natural frequency — can be used to detune below excitation but may conflict with performance/weight.
- Stiffening (adding ribs/gussets) raises natural frequency and is usually preferred for rotating machinery.

### Gaps
- Quantitative detuning margins (e.g., ±20% or factor 1.3) not in fetched sources; common practice but unverified here.
- MIL-STD-810 vibration test levels (random PSD, sine sweep) not extracted; need standard.

## Measurement: accelerometers, FFT, modal testing, operating deflection shapes

### Takeaway
Vibration measurement uses accelerometers (piezoelectric/capacitive/MEMS) feeding FFT-based spectra for frequency identification; modal testing extracts modal parameters; ODS shows actual operating motion; condition monitoring trends vibration for predictive maintenance.

### Cited Findings
- Accelerometer: measures proper acceleration; types: piezoelectric (high freq, high temp), piezoresistive (shock), capacitive (low freq), MEMS (small/cheap), thermal (convective), servo (force-balance) — [Wikipedia, Accelerometer](https://en.wikipedia.org/wiki/Accelerometer).
- Accelerometers used for machinery health monitoring (bearings, turbines, pumps, fans, compressors), structural health monitoring, NVH, seismic — [Wikipedia, Accelerometer](https://en.wikipedia.org/wiki/Accelerometer).
- Piezoelectric accelerometers use PZT/quartz crystals; MEMS use capacitive comb/proof mass; damping from residual gas — [Wikipedia, Accelerometer](https://en.wikipedia.org/wiki/Accelerometer).
- Vibration analysis: units of displacement/velocity/acceleration as time waveform; spectrum from FFT of TWF; spectrum pinpoints faulty components — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Modal testing: excite structure (shaker/hammer), measure response at many points, extract modal mass/frequency/damping; SIMO/MISO/MIMO; reciprocity — [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis).
- Operating deflection shapes (ODS): actual motion under operating loads; not in fetched sources beyond modal analysis mention — flag.
- Machine condition monitoring uses accelerometers on bearings; trends detect imbalance, misalignment, bearing faults, resonance — [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration).
- Building/bridge SHM uses accelerometers with OMA to estimate modal parameters over time — [Wikipedia, Accelerometer](https://en.wikipedia.org/wiki/Accelerometer).
- ISO 4866 and ISO 10137 referenced for structural vibration measurement/serviceability — [Wikipedia, Accelerometer](https://en.wikipedia.org/wiki/Accelerometer).

### Inferences
- Choose accelerometer by frequency range and amplitude: piezoelectric for high-freq machinery (kHz), MEMS/IEPE for low-freq building monitoring, piezoresistive for shock.
- Mounting matters: stud > adhesive > magnetic; poor mounting loses high-frequency response.
- FFT spectrum identifies fault frequencies (1×, 2×, gear mesh, bearing defect frequencies); time waveform captures transients.

### Gaps
- Operating deflection shapes (ODS) methodology and distinction from mode shapes not in fetched sources.
- Accelerometer sensitivity, range, and mounting resonance details not quantified here.
- FFT windowing, averaging, and resolution trade-offs not covered.

## Vibration standards: ISO 10816, ISO 20816, MIL-STD-810

### Takeaway
ISO 10816/20816 (vibration severity for rotating machinery by velocity zones) and MIL-STD-810 (environmental test methods including vibration, shock, pyroshock) are the principal vibration standards; MIL-STD-810 is tailorable and not certifiable by third parties.

### Cited Findings
- MIL-STD-810: US DoD Test Method Standard, Environmental Engineering Considerations and Laboratory Tests; specifies environmental tests to determine equipment survivability over service life; chamber tests replicate effects rather than environments — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).
- Current version: MIL-STD-810H (2019) with Change Notice 1 (2022); G replaced by H in 2019 — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).
- Test Method 514.8 Vibration: simulates vibration environments; random, sine-on-random, helicopter scrambled; requires force rating F=m·a, velocity/displacement limits; multi-axis (527.2) replaces legacy single-axis — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).
- Test Method 516.8 Shock: functional, transportation, fragility, transit drop, crash hazard, bench handling, pendulum impact, catapult/arrested landing — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).
- Test Method 517.3 Pyroshock; 519.8 Gunfire shock; 522.2 Ballistic shock; 525.2 Time Waveform Replication; 527.2 Multi-Exciter; 528.1 Shipboard equipment — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).
- MIL-STD-810 also covers: low pressure, temperature, humidity, salt fog, sand/dust, immersion, acceleration, acoustic noise, icing, combined environments — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).
- MIL-STD-810 is tailorable: no third-party certification; vendor claims of compliance can be misleading; must specify test methods, parameter limits, internal vs independent testing — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).
- Related standards: DO-160 (airborne), UK Def Stan 00-35, NATO AECTP-100, MIL-DTL-901E (ship shock), IEST recommended practices — [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810).
- ISO 10816/20816: Wikipedia articles not found (404); known as vibration severity evaluation for rotating machinery (velocity-based zones A/B/C/D) — flag as unverified in this note; ISO 4866 and ISO 10137 cited for structural vibration measurement/serviceability — [Wikipedia, Accelerometer](https://en.wikipedia.org/wiki/Accelerometer).

### Inferences
- For commercial products, MIL-STD-810 compliance claims should be verified against specific test methods and levels; standard is a guide, not a mandatory spec for non-defense.
- ISO 10816/20816 zones (A: new, B: acceptable, C: restricted, D: damage) are velocity RMS thresholds depending on machine type/speed — common industry knowledge, not sourced here.
- For machinery health monitoring, trend vibration velocity (mm/s RMS) per ISO 10816 zones; accelerometers + FFT provide the data.

### Gaps
- ISO 10816 and ISO 20816 specific zone thresholds and measurement procedures not fetched (no Wikipedia articles); must consult standard documents directly.
- MIL-STD-810 specific vibration PSD levels, shock pulse amplitudes/durations not extracted; need standard text.
- IEC 60068 (environmental testing) and ISO 10816-3/20816-3 not covered.

---

## Sources
- [Wikipedia, Vibration](https://en.wikipedia.org/wiki/Vibration)
- [Wikipedia, Vibration isolation](https://en.wikipedia.org/wiki/Vibration_isolation)
- [Wikipedia, Damping](https://en.wikipedia.org/wiki/Damping)
- [Wikipedia, Critical speed](https://en.wikipedia.org/wiki/Critical_speed)
- [Wikipedia, Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis)
- [Wikipedia, Shock response spectrum](https://en.wikipedia.org/wiki/Shock_response_spectrum)
- [Wikipedia, Rotordynamics](https://en.wikipedia.org/wiki/Rotordynamics)
- [Wikipedia, Balancing machine](https://en.wikipedia.org/wiki/Balancing_machine)
- [Wikipedia, Accelerometer](https://en.wikipedia.org/wiki/Accelerometer)
- [Wikipedia, MIL-STD-810](https://en.wikipedia.org/wiki/MIL-STD-810)

Textbooks cited as needed (not fetched): Rao "Mechanical Vibrations"; Inman "Engineering Vibration"; Thomson & Dahleh "Theory of Vibration with Applications"; Shigley (vibration chapters); Harris & Piersol "Harris Shock and Vibration Handbook"; Lalanne "Mechanical Vibration and Shock Analysis".
