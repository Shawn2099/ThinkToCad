# Reliability Engineering and Safety for Mechanical Design

## Safety Factors (Selection, Typical Values, Safety Factor vs. Safety Margin)

### Takeaway
A safety factor is the ratio of actual strength/capability to required (design) load; it is chosen based on uncertainty in loads/materials/analysis and the consequence of failure, with typical values ranging from ~1.2 (aerospace) to 4+ (pressure vessels, connections), while the margin of safety expresses the same information as a relative excess (FoS − 1, with two common definitions).

### Cited Findings
- A factor of safety (FoS/SF) expresses how much stronger a system is than it needs to be for its specified maximum load; it is often computed analytically because full testing is impractical — [Wikipedia, "Factor of safety"](https://en.wikipedia.org/wiki/Factor_of_safety).
- There are two definitions of FoS: (1) the realized ratio of absolute strength to actual applied load (a calculated value), and (2) a required constant imposed by law/standard/contract (design factor). The realized FoS must exceed the required design factor — [Wikipedia, "Factor of safety"](https://en.wikipedia.org/wiki/Factor_of_safety).
- "Safety factor" (actual) vs. "design factor" (required): the design factor is defined in advance for an application and is not a calculation; the safety factor is the ratio of maximum strength to intended load for the actual item — [Wikipedia, "Factor of safety"](https://en.wikipedia.org/wiki/Factor_of_safety).
- Margin of safety (MoS/MS) has two usages: (a) as structural capability, MS = FoS − 1 (failure load/design load − 1), where 0 means no extra load capacity; (b) as requirement verification, MS = (realized FoS / design safety factor) − 1, where 0 means the part exactly meets the required strength — [Wikipedia, "Factor of safety"](https://en.wikipedia.org/wiki/Factor_of_safety).
- In aerospace/nuclear practice, margin of safety is often used in place of FoS and is defined as FS − 1 — [OSTI, "MOS for USQ White Paper" (2013)](https://www.osti.gov/servlets/purl/1134068).
- NASA-STD-5001 defines FoS as multiplying factors applied to limit loads/stresses for analytical/test assessment, and MS = [Allowable / (Limit Load × FoS)] − 1; selection depends on materials, attachment methods (e.g., bonding), and verification approach (prototype vs. protoflight) — [NASA-STD-5001B w/Change 3 (2022)](https://standards.nasa.gov/sites/default/files/standards/NASA/B-w/CHANGE-3/3/2022-10-24-NASA-STD-5001B-w-Change-3-Approved.pdf).
- Shigley: matters of uncertainty are addressed by the design factor and factor of safety in deterministic or statistical (reliability) sense; reliability is the area of the margin-of-safety distribution above zero, and the shaded overlap of stress/strength distributions is "interference" — [Shigley, "Mechanical Engineering Design" (PDF)](https://dl.icdst.org/pdfs/files3/ad7608c18e740b0e402c025fa3187de8.pdf).
- Appropriate design factors depend on accuracy of load predictions, strength/wear estimates, environmental effects, consequences of failure, and cost of over-engineering; components whose failure could cause substantial financial loss, serious injury, or death may use SF ≥ 4 (often 10), while non-critical components might use 2 — [Wikipedia, "Factor of safety"](https://en.wikipedia.org/wiki/Factor_of_safety).
- Typical values: buildings 2.0 per member; pressure vessels 3.5–4.0; automobiles 3.0; aircraft/spacecraft 1.2–4.0 (aerospace ~1.5; pressurized fuselage 2.0; main landing gear 1.25); ductile metals use lower values, brittle materials higher — [Wikipedia, "Factor of safety"](https://en.wikipedia.org/wiki/Factor_of_safety).
- FRP/composite recommended static safety factors: flexural members 2.5, compression members 3.0, shear 3.0, connections 4.0; impact/dynamic loads typically require 2× the static safety factor; creep requires higher factors — [Strongwell, "Section 7 Safety Factors"](https://www.strongwell.com/wp-content/uploads/2013/05/Section07.pdf).
- City University London table: exceptionally reliable materials with certainly known loads 1.25–1.50; stochastic (reliability) approach selects materials/processing/dimensions so probability of failure stays below a pre-selected value — [City University London, ME2104-A-1](https://www.staff.city.ac.uk/~ra600/ME2105/Analysis/ME2104-A-1.pdf).
- Safety factors compensate for material/load tolerances, uncertainty of anticipated loading (magnitude/type/placement), analysis assumptions, and fabrication tolerances; final selection is the designer's responsibility — [Strongwell, "Section 7 Safety Factors"](https://www.strongwell.com/wp-content/uploads/2013/05/Section07.pdf).

### Inferences
- The 1.5–4.0 range in the prompt maps to: ~1.2–2.0 aerospace (weight-critical), ~2.0 buildings, ~3.0 machinery/automotive, ~3.5–4.0 pressure vessels/connections, with higher factors for brittle materials, uncertain loads, and severe consequences.
- Deterministic FoS is a crude proxy for reliability; Shigley's interference model shows why two designs with the same FoS can have very different failure probabilities depending on scatter.

### Gaps
- No single authoritative table of safety factors by material/load/consequence was found across sources; values are industry- and code-specific (verify against applicable codes).
- The "four or higher (often ten)" and typical-value claims in Wikipedia are flagged [citation needed] in the source.

## Reliability (Bathtub Curve, MTTF/MTBF, Weibull, RBD, Series/Parallel)

### Takeaway
Reliability is the probability of performing an intended function for a stated time under stated conditions; the bathtub curve describes three life phases (infant mortality, useful life, wear-out), MTTF/MTBF quantify average life for non-repairable/repairable items, the Weibull distribution (shape γ, scale α) models all three phases, and series/parallel/k-out-of-n RBD formulas combine component reliabilities.

### Cited Findings
- Bathtub curve: empirical plot of failure rate h(t) vs. time with three periods — Early Failure/Infant Mortality (decreasing rate, weeks to months), Intrinsic/Stable (constant rate, majority of useful life), Wearout (increasing rate) — [NIST/SEMATECH Handbook, §8.1.2.4](https://itl.nist.gov/div898/handbook/apr/section1/apr124.htm).
- The bathtub curve also applies to repairable systems, where the vertical axis is the repair rate / rate of occurrence of failures (ROCOF) — [NIST/SEMATECH Handbook, §8.1.2.4](https://itl.nist.gov/div898/handbook/apr/section1/apr124.htm).
- Not every product experiences an infant-mortality or wear-out period; the curve is a general trend — [ASTM, "What Is Reliability?" (JF18)](https://marketing.astm.org/acton/attachment/9652/f-08d1/0/-/-/-/-/JF18-Data-Points.pdf).
- MTTF = expected time to failure for a non-repairable system; MTBF = average time between failures for a repairable system; MTBF = accumulated operating time / number of failures; FIT = 10^9 / MTBF — [Infineon, "Power System Reliability Modeling" (2024)](https://www.infineon.com/assets/row/public/documents/24/59/infineon-power-system-reliability-modeling-whitepaper-en.pdf?fileId=8ac78c8c8fc2dd9c01900610fb6d5bc4).
- Reliability R(t) = P(T > t), the probability a part functions at least time t; failure rate λ = 1/MTBF for constant-rate (exponential) failures — [Texas Instruments, "MTTF, Failrate, Reliability, and Life Testing" (SBFA011)](https://www.ti.com/lit/an/sbfa011/sbfa011.pdf?ts=1787667868181).
- Weibull PDF: f(t,γ,α) = (γ/t)(t/α)^γ exp(−(t/α)^γ); CDF F(t)=1−exp(−(t/α)^γ); reliability R(t)=exp(−(t/α)^γ); failure rate h(t)=(γ/α)(t/α)^(γ−1); mean = α Γ(1+1/γ) — [NIST/SEMATECH Handbook, §8.1.6.2 (Weibull)](https://www.itl.nist.gov/div898/handbook/apr/section1/apr162.htm).
- Weibull parameters: scale α = characteristic life (time at which 63.2% of population has failed), shape γ (also called m or β); γ<1 decreasing failure rate (infant mortality), γ=1 constant (exponential, α=MTTF), γ>1 increasing (wear-out) — [NIST/SEMATECH Handbook, §8.1.6.2](https://www.itl.nist.gov/div898/handbook/apr/section1/apr162.htm); [Infineon (2024)](https://www.infineon.com/assets/row/public/documents/24/59/infineon-power-system-reliability-modeling-whitepaper-en.pdf?fileId=8ac78c8c8fc2dd9c01900610fb6d5bc4).
- Symbol confusion: various texts use β or m for shape and η/c/ν for scale; some software swaps α and β — [NIST/SEMATECH Handbook, §8.1.6.2](https://www.itl.nist.gov/div898/handbook/apr/section1/apr162.htm).
- Three-parameter Weibull adds location/shift μ (no failure before μ) — [NIST/SEMATECH Handbook, §8.1.6.2](https://www.itl.nist.gov/div898/handbook/apr/section1/apr162.htm).
- Reliability block diagram (RBD): system functions if there is a path of functioning components between terminals a and b; series structure function φ = ∏ x_i; parallel φ = 1 − ∏(1−x_i) — [Vatn, NTNU, "Reliability and Maintenance" (2023)](https://jvatn.folk.ntnu.no/eLearning/TPK4161/Slides/ReliabilityAndMaintenance.pdf).
- Series system: R_series(t) = ∏ R_i(t); failure rates add; reliability is lower than any component. Parallel: R_parallel(t) = 1 − ∏(1 − R_i(t)); reliability exceeds any component. k-out-of-n is intermediate (series = n-out-of-n, parallel = 1-out-of-n) — [Relyence, "Mathematical Foundations for RBD" (2026)](https://relyence.com/wp-content/uploads/2026/03/Mathematical-Foundations-for-Reliability-Block-Diagram.pdf).
- MTBF for series = 1/(Σ 1/MTBF_i); parallel (no repair) MTBF = MTBF × (1 + 1/2 + … + 1/n); availability A = MTBF/(MTBF + MTTR) — [Pixelbeat reliability calculator](http://www.pixelbeat.org/docs/reliability_calculator).
- Complex systems can often be reduced by successive series/parallel/k-out-of-n reduction to a single equivalent component — [NIST/SEMATECH Handbook, §8.1.8.6](https://www.itl.nist.gov/div898/handbook//apr/section1/apr186.htm).

### Inferences
- Series systems dominate mechanical assemblies (all components must function), so component-level reliability and derating are critical; parallel redundancy is reserved for safety-critical functions.
- The Weibull shape parameter maps directly to the bathtub phases, making it the natural model for fatigue/life data.

### Gaps
- No detailed source on standby (cold/warm) redundancy or repairable-system availability modeling beyond the basic formulas above.

## Failure Analysis (FMEA, FTA, FMECA, HAZOP)

### Takeaway
FMEA is a bottom-up, inductive method to identify failure modes and their effects; FMECA adds a criticality analysis (qualitative or quantitative) and RPN = S×O×D prioritization; FTA is a top-down, deductive fault-tree method for a single undesired event; HAZOP uses guide words on process/operation deviations. Standards include IEC 60812 (FMEA/FMECA), IEC 61025 (FTA), IEC 61882 (HAZOP), SAE J1739/ARP 4761, AIAG FMEA-4, and MIL-STD-1629A.

### Cited Findings
- FMEA: systematic method to identify how items/processes might fail to perform their function, with local and global effects; IEC 60812:2018 covers planning, performing, documenting, maintaining FMEA/FMECA for hardware, software, processes, human action, and interfaces — [IEC 60812 (ANSI store)](https://webstore.ansi.org/standards/iec/iec60812ed2018).
- FMEA originated as MIL-P-1629 (1949); it is a forward/bottom-up search: initiating event = component failure, goal = identify effect — [MIT OCW, "System Safety" (16.63J)](https://ocw.mit.edu/courses/16-63j-system-safety-spring-2016/398a8339b4aae04a89a7f9bf13e52bab_MIT16_63JS16_LecNotes8.pdf).
- FMECA = FMEA + Criticality Analysis (CA); MIL-STD-1629A describes qualitative and quantitative criticality analysis and worksheet formats — [NASA extapps, MIL-STD-1629A](https://extapps.ksc.nasa.gov/Reliability/Documents/milstd1629_FMEA.pdf).
- ReliaSoft: FMEA/FMECA identify failure modes, assess risk, rank issues, and drive corrective actions; RPN = Severity × Occurrence × Detection; criticality matrix alternative; standards include SAE J1739, AIAG FMEA-4, MIL-STD-1629A — [ReliaSoft, "Basics: FMEA"](https://help.reliasoft.com/articles/content/basics/fmea.htm).
- FTA: top-down deductive analysis focusing on one particular undesired event, identifying causal relationships (logic gates); IEC 61025 — [IOP, "Comparative study FMEA vs FTA" (2017)](https://iopscience.iop.org/article/10.1088/1757-899X/252/1/012046/pdf).
- HAZOP: developed by Imperial Chemical Industries in early 1960s; uses guide words on process/operation deviations; team-based with diverse disciplines; applicable to new designs; tends to yield protective devices rather than design changes — [MIT OCW, "System Safety" (16.63J)](https://ocw.mit.edu/courses/16-63j-system-safety-spring-2016/398a8339b4aae04a89a7f9bf13e52bab_MIT16_63JS16_LecNotes8.pdf).
- AIChE/CCPS tool suite: simple qualitative (HAZOP, what-if/checklist, FMEA); simple risk (FMECA, LOPA); detailed quantitative (fault trees, event trees) — [AIChE, "Introduction to Hazard Identification and Risk Analysis"](https://www.aiche.org/ccps/introduction-hazard-identification-and-risk-analysis).
- FMEA limitations: handles only component failures (not unsafe interactions/design/requirements), single failures only, requires detailed design, works best on hardware/mechanical components; inefficient (analyzes unimportant + important failures) — [MIT OCW, "System Safety" (16.63J)](https://ocw.mit.edu/courses/16-63j-system-safety-spring-2016/398a8339b4aae04a89a7f9bf13e52bab_MIT16_63JS16_LecNotes8.pdf).
- Leveson (STAMP): traditional methods (FMEA, FTA, HAZOP, FMECA) assume accidents are chains of component failures; may miss software/control/interaction hazards — [Leveson, "Engineering a Safer World" (MIT PSAS)](https://psas.scripts.mit.edu/home/wp-content/uploads/2017/03/Nancy-Leveson_STAMP-Intro-2017.pdf).

### Inferences
- FMEA/FMECA are best for component-level, bottom-up risk ranking during design; FTA is best for demonstrating probability of a specific top-level undesired event; HAZOP is best for process/plant deviations; combine them for comprehensive safety cases.

### Gaps
- No detailed source on HAZOP guide-word set or FTA gate symbols beyond general descriptions; consult IEC 61882 and IEC 61025 directly.
- MIL-STD-1629A was cancelled in 1984; modern practice uses IEC 60812 / AIAG / SAE standards — verify which applies to your domain.

## Failure Investigation (Root Cause Analysis, Fishbone, 5 Whys, Fractography)

### Takeaway
Root cause analysis (RCA) is a structured, evidence-based team process that distinguishes symptoms/contributing factors from systemic root causes; 5 Whys drills down causal chains, fishbone (Ishikawa) diagrams categorize potential causes, and fractography examines fracture surfaces to identify failure origin and mode (source not verified here).

### Cited Findings
- 5 Whys: developed by Sakichi Toyoda; ask "Why?" repeatedly (typically 3–5+, until no meaningful answer) to uncover cause-and-effect and reach root cause; validate by asking whether correcting the candidate cause would prevent recurrence — [LA County, "The 5 Whys & Fishbone Diagram"](http://www.publichealth.lacounty.gov/qiap/docs/Topic3-Fishbone.pdf); [CMS, "Five Whys Tool for RCA"](https://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/QAPI/Downloads/FiveWhys.pdf).
- Fishbone (cause-and-effect/Ishikawa) diagram: visually displays multiple causes for a problem and sorts ideas into categories; used with 5 Whys; team-based brainstorming — [CMS, "How to Use the Fishbone Tool for RCA"](https://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/QAPI/Downloads/FishboneRevised.pdf); [AHRQ, "Job Aid: 5 Whys and Fishbone Diagrams"](https://www.ahrq.gov/sites/default/files/wysiwyg/ncepcr/resources/job-aid-5-whys.pdf).
- RCA principles: aims at root causes (more effective than treating symptoms); performed systematically with documented evidence; usually more than one root cause; can be applied to almost any situation; distinguish physical, human, and latent/organizational causes — [DOE Massachusetts, "Root Cause Analysis Protocol: Fishbone"](https://www.doe.mass.edu/turnaround/level4/root-cause-analysis-protocol-fishbone.pdf).
- RCA validates root causes by asking "If this cause were removed, would the event have been prevented?" — [CMS, "Five Whys Tool for RCA"](https://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/QAPI/Downloads/FiveWhys.pdf).

### Inferences
- 5 Whys is fast but can oversimplify multi-cause failures; fishbone forces breadth across categories; combine with evidence-based validation to avoid stopping at symptoms.

### Gaps
- Fractography (fracture-surface examination for crack origin, propagation markings, overload vs. fatigue) was not sourced in this research; standard references include ASTM E2333 and failure-analysis handbooks — verify before citing.
- No mechanical-specific RCA standard (e.g., Apollo/MORT, TapRooT) sourced here.

## Design for Reliability (Redundancy, Derating, Fail-Safe vs. Fail-Operational, Damage Tolerance)

### Takeaway
Design-for-reliability strategies (in order of precedence per NASA) are: eliminate the failure mode, design for fault tolerance (redundancy), design for fail-safety, provide early warning/fault diagnosis, and issue special maintenance instructions; supporting techniques include derating, durability/damage tolerance, and safety margins. Fail-safe and fail-operational are distinct: fail-safe minimizes harm on failure; fail-operational keeps functioning through a failure via redundancy.

### Cited Findings
- NASA reliability discipline: strategies in order of precedence to prevent failures: (a) improve design to eliminate the failure mode, (b) design for fault tolerance (redundancy), (c) design for fail-safety (failure affects function but no injury/additional damage), (d) provide early warnings via fault diagnosis; if not viable, issue special maintenance instructions — [NASA, "Reliability Discipline: Overview of Methods"](https://extapps.ksc.nasa.gov/Reliability/Documents/Reliability_Discipline_Overview_of_Methods.pdf).
- Reliability improvement strategies during design: Zero-Failure Design; Fault Tolerance (redundant elements switch to backup/alternative mode); Derating (component used well below capability rating); Durability (longer useful life or damage tolerance); Safety Margins (worst-case stresses and margins) — [NASA, "Reliability Discipline: Overview of Methods"](https://extapps.ksc.nasa.gov/Reliability/Documents/Reliability_Discipline_Overview_of_Methods.pdf).
- Redundancy: hardware redundancy (passive/active/hybrid), M-of-N systems, k-out-of-n; information redundancy (ECC, RAID); software redundancy (design diversity, N-version programming); time redundancy — [arXiv, "Dependability in Embedded Systems" (2024)](https://arxiv.org/html/2404.10509v1).
- Fail-safe: a design feature that, on failure, inherently responds to cause minimal or no harm to equipment/environment/people; if a system cannot be made fail-safe (continuous availability needed), use redundancy, fault tolerance, or contingency plans — [Wikipedia, "Fail-safe"](https://en.wikipedia.org/wiki/Fail-safe).
- Fail-safe vs. fail-secure: fail-safe prevents harm; fail-secure prevents unauthorized access/data loss on failure; sometimes opposite (e.g., fire doors unlock for escape) — [Wikipedia, "Fail-safe"](https://en.wikipedia.org/wiki/Fail-safe).
- Fail-active operational: installed on highly redundant systems so a single failure is tolerated (fail active) and a second failure is detected, then the system shuts down (fail passive); e.g., triple modular redundancy with voting (aircraft inertial navigation, pitot tubes) — [Wikipedia, "Fail-safe"](https://en.wikipedia.org/wiki/Fail-safe).
- Some systems can never be made fail-safe because continuous availability is needed; redundancy/fault tolerance/contingency plans are used instead — [Wikipedia, "Fail-safe"](https://en.wikipedia.org/wiki/Fail-safe).

### Inferences
- For mechanical design, "damage tolerance" (inspectable, slow crack growth) is the aerospace approach when fail-safe alone is insufficient; derating and worst-case margins are the baseline for non-critical parts.

### Gaps
- Damage tolerance methodology (crack-growth analysis, inspection intervals) was only mentioned in passing by NASA overview; no detailed source on damage-tolerance standards (e.g., MIL-HDBK-? / FAA AC 25.571) was retrieved — verify.
- Derating guidelines with specific derating ratios by component type were not sourced.

## Standards (ISO 13849, ISO 12100, IEC 61508, MIL-STD-882)

### Takeaway
ISO 12100 provides the machinery risk-assessment/risk-reduction methodology; ISO 13849-1 covers safety-related parts of control systems (SRP/CS) and Performance Levels (PL a–e) for high/continuous demand; IEC 61508 is the generic functional-safety standard with SIL 1–4 for E/E/PE systems; MIL-STD-882 is the US DoD system-safety standard (not directly sourced here).

### Cited Findings
- ISO 12100:2010: specifies basic terminology, principles, and methodology for achieving safety in machinery design; principles of risk assessment and risk reduction (hazard identification, risk estimation/evaluation, risk reduction); documentation and verification; basis for type-B/C standards; does not address risk/damage to animals, property, or environment — [ISO, ISO 12100:2010](https://www.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/05/15/51528.html).
- ISO 13849-1:2023 (Ed. 4): methodology and requirements for design/integration of safety-related parts of control systems (SRP/CS) performing safety functions, including software; applies to high-demand and continuous modes (not low demand — see IEC 61508); uses Performance Level (PLr) determined via ISO 12100 risk assessment — [ISO, ISO 13849-1:2023](https://www.iso.org/standard/73481.html); [ISO OBP](https://www.iso.org/obp/ui/en#!iso:std:73481:en).
- IEC 61508: functional safety for electrical/electronic/programmable electronic (E/E/PE) safety-related systems; defines safety as freedom from unacceptable risk; risk-based approach; Safety Integrity Levels SIL 1–4 (SIL 4 highest); provides generic requirements and is the basis for sector/product standards (IEC 62061 machinery, IEC 61511 process, IEC 61513 nuclear, IEC 61800-5-2 power drives) — [IEC, "Overview of IEC 61508 & Functional Safety" (2022 PDF)](https://assets.iec.ch/public/acos/IEC%2061508%20%26%20Functional%20Safety-2022.pdf?2023040501); [IEC functional-safety FAQ](https://www.iec.ch/functional-safety/faq).
- IEC 61508 required SIL performance is expressed as average probability of dangerous failure on demand (low demand) or average frequency of dangerous failure (high/continuous demand) — [IEC functional-safety FAQ](https://www.iec.ch/functional-safety/faq).
- ISO/TR 22100-2:2013 describes the relationship between ISO 12100 (risk assessment/reduction) and ISO 13849-1 (SRP/CS) — [ISO, ISO/TR 22100-2:2013](https://www.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/06/31/63158.html).
- MIL-STD-1629A (procedures for FMECA) was published by US DoD and cancelled in 1984; still referenced historically — [NASA extapps, MIL-STD-1629A](https://extapps.ksc.nasa.gov/Reliability/Documents/milstd1629_FMEA.pdf).

### Inferences
- For machinery, the typical chain is ISO 12100 (risk assessment) → determine required PL (ISO 13849-1 Annex A) → design SRP/CS to that PL; for E/E/PE systems, use IEC 61508/62061.

### Gaps
- MIL-STD-882 (system safety) was not directly sourced; it is commonly cited as the DoD standard for system safety program requirements (e.g., MIL-STD-882E) — verify against the current revision.
- Exact SIL/PL target tables and hardware-fault-tolerance requirements require the standards themselves.

## Fatigue Reliability (Probabilistic S-N, Scatter Factors)

### Takeaway
Probabilistic S-N (P-S-N) curves express stress-life at a specified survival probability (commonly Weibull/normal/Gumbel models per ISO 12107/ASTM E739-91); scatter factors (typically 2–4) convert median fatigue life to a "safe" life corresponding to high reliability (e.g., 99.87%), and probabilistic methods can recover 37–175% of the conservatism of deterministic scatter factors.

### Cited Findings
- P-S-N curves: S-N relation at a specified survival probability P_s; scatter of fatigue life described by normal, Weibull, and Gumbel distributions; ISO 12107 and ASTM E739-91 are common statistical models — [ScienceDirect, "Fatigue failure mechanisms ... CFRP–steel joints" (2023)](https://www.sciencedirect.com/science/article/abs/pii/S0142112322007204).
- Two-parameter Weibull recommended for fatigue life design as it constrains data without excessive safety redundancy; a safety factor of 1.5 may be insufficient for fatigue-susceptible joints — [ScienceDirect, "Fatigue failure mechanisms ... CFRP–steel joints" (2023)](https://www.sciencedirect.com/science/article/abs/pii/S0142112322007204).
- Probabilistic S-N studies use Weibull parameters for scattered fatigue life; R-S-N curves cannot be extrapolated to minimum expected life or very high reliability — [PMC, "A modification in Weibull parameters..." (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10579224).
- Fatigue scatter factor: ratio of median life N_50 to safe life N_99.87, describing reliability of fatigue analysis/test results; GJB67.6-2008: scatter factor generally 4 for average load spectrum (99.87% reliability), 2–4 for severe load spectrum — [ICAS, "Study on Fatigue Scatter Factor under Severe Load Spectrum" (2020)](https://www.icas.org/icas_archive/ICAS2020/data/papers/ICAS2020_0904_paper.pdf).
- NASA spectral fatigue guideline: deterministic scatter factors of 2–4 are applied to mean fatigue life to obtain "safe" life; a scatter factor of 2 corresponds to reliability index 5.6, factor 4 to 11.2; probabilistic approach allows specifying reliability explicitly and can increase allowable life by 37% (vs. factor 2) to 175% (vs. factor 4) — [NASA JSC, "Preferred Practice GD-AP-2303 Spectral Fatigue Reliability"](https://extapps.ksc.nasa.gov/Reliability/Documents/Preferred_Practices/2303.pdf).
- Cycles-to-failure data have coefficients of variation typically 30–40%, sometimes >100% — [NASA CR-3697, "Statistical Summaries of Fatigue Data" (1983)](https://ntrs.nasa.gov/api/citations/19830021460/downloads/19830021460.pdf).
- Fatigue S-N curves are commonly characterized at constant amplitude; design uses lower-bound envelope lines 2–3 standard deviations below the least-squares fit — [NASA CR-3697 (1983)](https://ntrs.nasa.gov/api/citations/19830021460/downloads/19830021460.pdf).

### Inferences
- Deterministic scatter factors (2–4) bake in unquantified conservatism; P-S-N curves make the reliability level explicit and can justify longer lives when data quality is good.

### Gaps
- No source on damage-tolerance inspection intervals or probabilistic fracture mechanics (Paris law) was retrieved.
- Scatter-factor values vary by standard (GJB, FAA, EASA, Airbus/Boeing) and were not comprehensively compared.

## Human Factors / Ergonomics in Safety

### Takeaway
Human factors/ergonomics (HFE) designs work systems to fit human capabilities and limitations, reducing errors, accidents, and injury; it spans physical, cognitive, and organizational ergonomics, and is codified in standards such as EN 614-1/EN 894-2 and ISO 11064, with poor HFE repeatedly identified as a root cause of major accidents.

### Cited Findings
- IEA definition: ergonomics/human factors is the scientific discipline concerned with understanding interactions between humans and other system elements, and the profession that applies theory, principles, data, and methods to optimize human well-being and overall system performance — [TUM Mechanical Engineering](https://www.mec.ed.tum.de/en/lfe/about/human-factors-and-ergonomics); [Cambridge excerpt, Sujan & Pickup](https://assets.cambridge.org/97810477/56013/excerpt/9781047756013_excerpt.pdf).
- HSE: ergonomics reduces potential for accidents, injury, and ill-health and improves performance/productivity; poor design is a root cause of major accidents (Texas City, Herald of Free Enterprise, Ladbroke Grove); EN 614 Parts 1/2, EN 11064, ISO 11064, EEMUA 191/201 are key standards — [HSE, "Human factors – Design"](https://www.hse.gov.uk//humanfactors/topics/design.htm).
- HSE leaflet: ergonomics considers job demands, equipment design, information, physical/mental capabilities, and organizational environment; early consideration in design yields better results — [HSE, "Ergonomics and human factors at work" (INDG90)](https://www.hse.gov.uk//pubns/indg90.pdf).
- EU OSH: Machinery Directive (2006/42/EC, repealed by Regulation 2023/1230/EU from 2027) requires ergonomic design; EN 614-1 specifies ergonomic design principles for machinery; EN 894-2 covers control actuators — [EU-OSHA OSHwiki, "Human-machine interface"](https://oshwiki.osha.europa.eu/hr/themes/human-machine-interface).
- CDC/NIOSH: human-factors design of machine safeguards determines whether safeguards are actually used; safeguarding that meets a standard but is hard to use may be ineffective — [CDC stacks, "Design for Health and Safety" ch. 7.5 (2015)](https://stacks.cdc.gov/view/cdc/185473/cdc_185473_DS1.pdf).
- EU-OSHA forecast: cognitive ergonomics and HMI complexity are emerging risks; neglect of human-factor design in interfaces increases mental strain and errors — [EU-OSHA, "OHS in figures" (2009)](https://osha.europa.eu/sites/default/files/en_TE8010196EN-N.pdf).
- HFE contributes to safety through human reliability analysis, error prevention, workspace/control/display design, and procedure design — [OSTI, "Human Factors in Design" (2013)](https://www.osti.gov/servlets/purl/1110674).

### Inferences
- For mechanical products, ergonomics is most impactful at the interface level (controls, displays, guarding, maintenance access); cognitive ergonomics matters increasingly with automation/AI.

### Gaps
- No quantitative human-error probability data (e.g., THERP/HEART) sourced here; consult human-reliability-analysis references for probabilities.
- Standards citations (EN 614, ISO 11064) noted but not summarized in detail.
