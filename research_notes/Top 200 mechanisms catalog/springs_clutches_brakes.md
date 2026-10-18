# Springs, Clutches, and Brakes — Mechanism Catalog

## Springs

### Takeaway
Metal and elastomeric springs store mechanical energy through elastic deformation; the catalog spans helical compression/extension/torsion, Belleville (coned disc), leaf, gas, constant-force, volute, spiral/clock, torsion bar, rubber/urethane, wave, finger (cantilever), and die springs, each with distinct load–deflection laws and application niches (Shigley/Mott-style machine design; ANSI recognizes six spring types: compression, extension, torsion, garter, flat/cantilever, constant-force) [ANSI/EGD Ch. 18].

### Cited Findings
- Helical compression spring: open-coil helix resisting compressive load; wire loaded primarily in torsion; forms include cylindrical, conical, convex, concave; used in automotive suspension, valves, return springs — [Engineers Edge spring review](https://www.engineersedge.com/spring_general.htm); [Century Spring helical overview](https://www.centuryspring.com/helical-springs).
- Helical extension spring: close-coiled helix resisting tensile load; has initial tension; load–deflection F = k(δ) with pitch/active coils; used in trampolines, garage doors, return mechanisms — [Gardner Spring design equations](https://www.gardnerspring.com/wp-content/uploads/2025/10/SpringDesignEquations.pdf); [Engineers Edge](https://www.engineersedge.com/spring_general.htm).
- Helical torsion spring: resists torque in a plane normal to coil axis; wire stressed in bending (not torsion); arms transmit load; close-wound body; applications: garage doors, clothespins, mousetraps, camera pop-ups — [RoyMech torsion spring formulas](https://www.roymech.co.uk/Useful_Tables/Springs/Springs_Torsion.html); [Wikipedia Torsion spring](https://en.wikipedia.org/wiki/Torsion_spring).
- Belleville (coned disc) spring: tapered washer, nonlinear force–deflection, compact, high load/low deflection; stacked series/parallel/combination; applications: gun recoil, pipe flanges, bolted joints, differential-expansion compensation, clutches/brakes — [ScienceDirect Belleville overview](https://www.sciencedirect.com/topics/engineering/belleville-spring); [SAE AE-21 Spring Design Manual](https://saemobilus.sae.org/books/spring-design-manual-ae-21).
- Leaf (multi-leaf) spring: flat spring, semi-elliptic or cantilever, graduated leaves; interleaf friction; automotive rear suspension, trucks, rail; design based on F, L, deflection, stress — [ScienceDirect/Marghitsu Mechanical Engineer's Handbook](https://www.sciencedirect.com/topics/engineering/belleville-spring); [SAE AE-21](https://saemobilus.sae.org/books/spring-design-manual-ae-21).
- Torsion bar spring: straight solid/hollow bar twisted in torsional shear; θ = TL/(GJ), kθ = πGD⁴/(32L); automotive suspension, stabilizer bars — [RoyMech](https://www.roymech.co.uk/Useful_Tables/Springs/Springs_Torsion.html); [Cambridge DANotes](https://www-mdp.eng.cam.ac.uk/web/library/enginfo/textbooks_dvd_only/DAN/springs/intro/intro.html).
- Spiral torsion / clock spring: flat strip wound spiral; one end on arbour, other on housing; stores rotational energy over multiple turns; steering wheel clock spring (airbag/electrical continuity), seat mechanisms, medical, aerospace — [Lesjöfors spiral torsion applications](https://www.lesjofors.com/en/technology/insights/spiral-torsion-spring-applications); [European Springs clock springs](https://www.europeansprings.com/custom-springs/clock-springs/); [Wikipedia Torsion spring](https://en.wikipedia.org/wiki/Torsion_spring).
- Constant-force spring: tightly coiled ribbon, exerts nearly constant force as unrolled; long extension; counterbalances, retractable tape rules, window sashes, typewriter carriage returns — [MW Components constant force](https://www.mwcomponents.com/constant-force-springs); [Shigley slides](https://www.slideshare.net/slideshow/ch-10-slidesm/248238886).
- Volute spring: conical spring of wide thin strip wound flat so coils nest; longer travel than helical conical; variable-rate scales, Stuart tank suspension — [Shigley slides](https://www.slideshare.net/slideshow/ch-10-slidesm/248238886); [Wikipedia Spring (device)](https://levantado.ddns.net/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Compression_springs.html).
- Wave spring: flat wire marcelled into wavy pattern (wave washer, single/multi-turn, linear, interlaced); high force in small axial space; valve wear compensation, bearing preload — [Rotor Clip interlaced wave case study](https://www.rotorclip.com/resources/case-study-an-interlaced-wave-spring-solution-for-high-force-space-constrained-applications).
- Gas spring: volume of compressed gas (pneumatic); force from pressure × area; adjustable, constant force over stroke; office chairs, hatches, automotive — [Cambridge DANotes](https://www-mdp.eng.cam.ac.uk/web/library/enginfo/textbooks_dvd_only/DAN/springs/intro/intro.html); [SAE HS-1576 pneumatic springs](https://saemobilus.sae.org/books/spring-design-manual-ae-21).
- Rubber/urethane spring: elastomeric blocks loaded in shear/compression; shock absorption, vibration isolation, bump stops; nonlinear, damping — [Cambridge DANotes](https://www-mdp.eng.cam.ac.uk/web/library/enginfo/textbooks_dvd_only/DAN/springs/intro/intro.html).
- Finger (cantilever) spring washer: flat spring fingers for preload/retention; ball-bearing preload, fastener security — [EGD Ch.18 finger spring washer Fig.18.12](https://omni.deanza.edu/dmt/documents/books/egd_lamit/EGD_Chapter_18.pdf).
- Die spring: heavy-duty compression spring (color-coded by load) for dies, clutches, brakes, farm/aircraft mechanisms — [Lee Spring HEFTY die springs](https://www.leespring.com/sites/default/files/2023-03/lee-spring-catalog-us.pdf).
- Garter spring: helical spring in circular form (extension) for seals, retaining rings — [EGD Ch.18 ANSI spring types](https://omni.deanza.edu/dmt/documents/books/egd_lamit/EGD_Chapter_18.pdf).

### Inferences
- Load–deflection nonlinearity (Belleville, volute, gas) is preferred where space is constrained or progressive stiffness is desired; linear helical springs dominate general-purpose designs.
- Helical torsion springs are misnamed (wire in bending), which matters for stress analysis and fatigue (use bending stress, not torsion shear) — [RoyMech](https://www.roymech.co.uk/Useful_Tables/Springs/Springs_Torsion.html).

### Gaps
- No single source provided full formulas for every type; Shigley 10th ed. chapter 10 cited indirectly via slides; exact spring rates for gas/rubber springs depend on geometry and were not numerically sourced.
- Fatigue life (Goodman/Soderberg) specifics not sourced here.

## Clutches

### Takeaway
Clutches transmit torque between coaxial shafts on demand; they split into positive (no-slip, jaw/dog) and friction-dependent (disk, cone, band) plus automatic/one-way (centrifugal, overrunning sprag/roller/ratchet/wrap-spring) and actuated types (electromagnetic, pneumatic/hydraulic, fluid coupling, powder, hysteresis). Selection trades torque capacity, engagement smoothness, speed, wear, and control.

### Cited Findings
- Friction disk clutch (single/multi-plate): friction plates pressed axially by spring/diaphragm; torque T = μ·F·r·n (n plates); multi-plate increases capacity in compact space; diaphragm spring engagement; automotive manual transmissions — [Britannica clutch](https://mendel-qa.dev-ext.britannica.com/technology/clutch-machine-component); [patents DE1475402B2, DE2306255A1 multi-plate](https://patents.google.com/patent/DE2306255A1/en).
- Cone clutch: conical friction surfaces; self-energizing (wedge) gives high torque in small space but grabby engagement; used in older transmissions, marine, machinery — [Britannica](https://mendel-qa.dev-ext.britannica.com/technology/clutch-machine-component); [AutomationExpo cone clutch listings](https://www.automationexpo.com/article,classified/pneumatic-clutches,pneumatic-clutches).
- Centrifugal clutch: friction shoes pivoted on driving member, engage driven drum by centrifugal force above threshold rpm; torque capacity rises with speed; scooter/moped, small engines, conveyors — [Engineers Edge centrifugal clutch equations](https://www.engineersedge.com/mechanics_machines/centrifugal_clutch_13706.htm); [patent DE862235C](https://patents.google.com/patent/DE862235C/en).
- Dog (jaw/positive) clutch: interlocking jaws/teeth; no slip, high torque, instantaneous engagement with shock; gearboxes, PTOs (not for speed differential) — [Britannica positive clutch](https://mendel-qa.dev-ext.britannica.com/technology/clutch-machine-component).
- Overrunning clutch (one-way): transmits torque one direction, freewheels other; types: roller-ramp, sprag, ratchet/pawl, wrap-spring, wedge-ramp; sprag gives highest torque density and instant engagement with no backlash; roller-ramp longest life; wrap-spring lowest cost light-duty; wedge-ramp combines benefits — [Machine Design overrunning clutch](https://www.machinedesign.com/automation-iiot/article/21826947/overrunning-clutch-expands-capabilities); [Formsprag manual](https://hvhindustrial.com/storage/pdfs/Overrunning_Clutches_Application_Manual.pdf); [FIRGELLI](https://www.firgelliauto.com/en-de/blogs/mechanisms/overrunning-clutch).
- Wrap-spring clutch: helical spring tightens on cylindrical sleeve to transmit torque one direction; low cost, light-duty, low speed — [Machine Design](https://www.machinedesign.com/automation-iiot/article/21826947/overrunning-clutch-expands-capabilities).
- Electromagnetic clutch: electrically magnetized armature clamps friction disks; accurate engage/release; types: friction (single/multi-disk), magnetic particle, hysteresis; used in automation, tension control, motor testing — [Machine Design EM brakes/clutches](https://www.machinedesign.com/motors-drives/article/21828254/electromagnetic-brakes-and-clutches); [electric-clutches.com](https://www.electric-clutches.com/clutch_types.php).
- Magnetic particle clutch/brake: powder in cavity aligns under magnetic field; infinitely adjustable torque; slip operation, tensioning/positioning — [Machine Design](https://www.machinedesign.com/motors-drives/article/21828254/electromagnetic-brakes-and-clutches).
- Hysteresis clutch/brake: torque from hysteresis losses in drag cup; constant torque independent of slip speed; fractional power, almost no wear; permanent-magnet versions — [Machine Design](https://www.machinedesign.com/motors-drives/article/21828254/electromagnetic-brakes-and-clutches); [Magnetic Technologies](https://magnetictech.com/electric-hysteresis).
- Fluid coupling: hydrodynamic torque transmission via impeller/turbine in oil; smooth start, torque multiplication ~2:1; no mechanical wear; automotive automatics (torque converter adds stator) — [patent DE933186C fluid pressure clutch](https://patents.google.com/patent/DE933186C/en).
- Pneumatic/hydraulic actuated clutch: air/oil pressure engages multi-plate or cone; fast, remote actuation; industrial automation — [AutomationExpo pneumatic clutch listings](https://www.automationexpo.com/article,classified/pneumatic-clutches,pneumatic-clutches); [patent DE687280C](https://patents.google.com/patent/DE687280C/en).

### Inferences
- For high torque density in limited radial space, multi-plate friction or sprag overrunning clutches are preferred; cone clutches self-energize but risk chatter.
- Electromagnetic clutches dominate automation where precise, clean engagement is needed; fluid couplings dominate high-inertia starts.

### Gaps
- Torque capacity formulas for cone/clutch not sourced with numbers; manufacturer catalogs (Warner/Ogura/Altra) referenced only via Formsprag/SEPAC snippets; no verified rating tables.

## Brakes

### Takeaway
Brakes dissipate kinetic energy (friction, eddy currents, regenerative) or hold position; common types: shoe (external/internal drum), disk, band, electromagnetic (friction/particle/hysteresis), eddy current, regenerative, parking/emergency. Key concerns: braking torque, fade (~250–300 °C for friction), and cooling.

### Cited Findings
- Shoe (drum) brake: shoes press against inner drum surface; external/internal; simple, low cost, self-energizing (leading shoe); fade-prone; automotive rear, parking brakes — [VTechworks Ch.2 general principle](https://vtechworks.lib.vt.edu/bitstream/handle/10919/30598/CHAP1_DOC.pdf); [PMC brake fade study 250–300 °C](https://pmc.ncbi.nlm.nih.gov/articles/PMC8434285).
- Disk brake: caliper clamps pads on rotor; better cooling and fade resistance than drum; automotive front, motorcycles, aircraft — [VTechworks](https://vtechworks.lib.vt.edu/bitstream/handle/10919/30598/CHAP1_DOC.pdf); [IJERT comparative study](https://www.ijert.org/a-comparative-study-of-electromagnetic-braking-system).
- Band brake: flexible band with friction lining wraps drum; simple, high torque in one direction; conveyors, hoists, winches — [patent DE933186C mentions band brake](https://patents.google.com/patent/DE933186C/en).
- Electromagnetic brake: electrically actuated friction or particle/hysteresis; fast response; ~80% of power-applied brakes; supplementary retarder on heavy vehicles — [Machine Design](https://www.machinedesign.com/motors-drives/article/21828254/electromagnetic-brakes-and-clutches); [IJERT](https://www.ijert.org/a-comparative-study-of-electromagnetic-braking-system).
- Eddy current brake: non-contact; conductive disk rotates in magnetic field, induced currents create opposing torque; torque ∝ speed and current; no wear, needs cooling; trains, roller coasters, aircraft, heavy vehicles — [IJERT review](https://www.ijert.org/review-paper-on-eddy-current-and-electromagnetic-brake); [COMSOL](https://www.comsol.com/blogs/simulating-eddy-current-brakes?setlang=1); [Springer DS-50 study](https://link.springer.com/chapter/10.1007/978-981-99-7401-6_49).
- Regenerative braking: motor acts as generator, returns energy to battery/flywheel; limited by battery state; reduces friction brake wear; EVs, trains, flywheel KERS — [Wikipedia Regenerative braking](https://en.wikipedia.org/wiki/Regenerative_braking); [Tesla owner manual](https://www.tesla.com/ownersmanual/modely/en_eu/GUID-3DFFB071-C0F6-474D-8A45-17BE1A006365.html); [49 CFR 571.135 RBS](https://www.law.cornell.edu/cfr/text/49/571.135).
- Parking/emergency brake: mechanical (cable) or electronic; holds vehicle stationary; drum-in-hat or shoe; rarely effective for high-speed stops — [Motor.com parking brakes](https://www.motor.com/wp-content/uploads/2016/02/8_Brakeshop_0216.pdf); [Tesla manual](https://www.tesla.com/ownersmanual/models/en_us/GUID-3DFFB071-C0F6-474D-8A45-17BE1A006365.html).
- Brake fade: coefficient of friction drops above ~250–300 °C due to chemical decomposition of lining; mitigated by cooling, material choice, vented rotors — [PMC study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8434285); [VTechworks](https://vtechworks.lib.vt.edu/bitstream/handle/10919/30598/CHAP1_DOC.pdf).
- Cooling: natural/forced air, water-cooled eddy current retarders; water cooling equilibrium temperature ∝ coolant temp, flow >1 m/s diminishing returns — [ScienceDirect water-cooled ECB](https://www.sciencedirect.com/science/article/pii/S2214157X25013498).

### Inferences
- Friction brakes are necessary for low-speed/holding and emergency stops; eddy current/regenerative brakes excel at continuous high-speed retardation but cannot hold at zero speed (eddy current torque → 0 at 0 rpm).
- Parking brakes are often drum-in-hat to provide holding independent of service pads.

### Gaps
- No verified braking torque equations (e.g., shoe brake torque factor, disk brake clamping) with numerical coefficients were sourced; FMVSS 135 test procedures cited but not full formulas.
- Manufacturer-specific fade curves (Warner/Ogura/Altra) not sourced.

## Catalog Summary (counts)

Springs: helical compression, helical extension, helical torsion, Belleville (coned disc), leaf (semi-elliptic/cantilever), torsion bar, spiral/clock, constant-force, volute, wave, gas, rubber/urethane, finger (cantilever) washer, die, garter = 15.
Clutches: single-plate friction disk, multi-plate friction disk, cone, centrifugal, dog (jaw), overrunning (roller-ramp, sprag, ratchet, wrap-spring, wedge-ramp), wrap-spring, electromagnetic friction, magnetic particle, hysteresis, fluid coupling, pneumatic/hydraulic actuated = 13 (counting overrunning subtypes separately ≈ 17).
Brakes: external shoe, internal shoe (drum), disk, band, electromagnetic friction, magnetic particle, hysteresis, eddy current, regenerative, parking/emergency (drum-in-hat) = 10.
Total ≈ 38 mechanisms.

### Source notes
All findings cited inline; unverified items flagged as gaps. No fabrication of numeric ratings. Standards referenced: ANSI spring types (EGD Ch.18), SAE AE-21 Spring Design Manual, FMVSS 135 (49 CFR 571.135). Patents: DE862235C, DE352614C, DE687280C, DE1475402B2, DE2306255A1, DE933186C, EP0164183. Manufacturer catalogs: Lee Spring, Formsprag/Stieber (Altra), SEPAC, European Springs, Lesjöfors, MW Components, Rotor Clip. Textbooks: Shigley (via slides), Mott/Marghitsu Mechanical Engineer's Handbook (ScienceDirect), Norton (not directly sourced — flagged). Wikipedia used for definitions only.