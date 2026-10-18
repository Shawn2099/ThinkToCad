# Regulatory Compliance and Certification for Mechanical/Machinery Design

## Machinery Safety: ISO 12100, ISO 13849, IEC 61508

### Takeaway
Machinery safety is built on a three-layer stack: ISO 12100 defines the risk-assessment methodology, ISO 13849 (machinery-specific) and IEC 61508 (generic functional safety) quantify the required reliability of safety-related control functions via Performance Levels (PL) and Safety Integrity Levels (SIL).

### Cited Findings
- ISO 12100:2010 "Safety of machinery — General principles for design — Risk assessment and risk reduction" specifies basic terminology, principles, and a methodology for achieving safety in machinery design; it is intended as a basis for type-B/type-C safety standards and does not deal with risk to domestic animals, property, or the environment — [ISO 12100:2010](https://www.iso.org/standard/51528.html).
- ISO 12100 is developed by ISO/TC 199 "Safety of machinery" — [ISO 12100:2010](https://www.iso.org/standard/51528.html).
- ISO 13849 applies to parts of machinery control systems assigned to safety functions (safety-related parts of a control system, SRP/CS); it has two parts — ISO 13849-1 (design principles) and ISO 13849-2 (validation) — [Wikipedia: ISO 13849](https://en.wikipedia.org/wiki/ISO_13849).
- ISO 13849-1 covers mechanical, electrical, electronic, and fluidic (hydraulic/pneumatic) technologies; it is simplified for the machinery sector relative to the generic IEC 61508 — [Wikipedia: ISO 13849](https://en.wikipedia.org/wiki/ISO_13849).
- Performance Level (PL) is a band of failure rates a–e quantified as Probability of Dangerous Failure per hour (PFHd), from PLa < 1×10⁻⁴ (highest failure rate) to PLe ≥ 1×10⁻⁸ (lowest); the PL of a function depends on architecture (Category B/1/2/3/4), MTTFd, DCavg, and CCF measures — [Wikipedia: ISO 13849](https://en.wikipedia.org/wiki/ISO_13849).
- Category B (single channel, MTTFd Low/Medium, no diagnostics) max PL = b; Category 1 (well-tried components, MTTFd High) max PL = c; Category 2 (single channel + diagnostics, DCavg 60–99%) max PL = d; Category 3 (redundant, no single failure loses safety function) max PL = e; Category 4 (redundant, MTTFd High, DCavg ≥ 99%) PL = e — [Wikipedia: ISO 13849](https://en.wikipedia.org/wiki/ISO_13849).
- A 2013 informal stakeholder survey found >89% of machine builders and >90% of component manufacturers/service providers use ISO 13849 as the primary functional safety standard — [Wikipedia: ISO 13849](https://en.wikipedia.org/wiki/ISO_13849).
- IEC 61508 is the generic international standard "Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems" (E/E/PE), applicable to all industries; it defines functional safety and uses a safety life cycle of 16 phases (analysis/realisation/operation) — [Wikipedia: IEC 61508](https://en.wikipedia.org/wiki/IEC_61508).
- IEC 61508 defines Safety Integrity Level (SIL) 1–4 with target failure rates; for low-demand mode (≤1 demand/year) SIL is probability of failure on demand (SIL 1: ≥10⁻² to <10⁻¹ … SIL 4: ≥10⁻⁵ to <10⁻⁴); for high-demand/continuous mode SIL is PFH (SIL 1: ≥10⁻⁶ to <10⁻⁵ … SIL 4: ≥10⁻⁹ to <10⁻⁸) — [Wikipedia: IEC 61508](https://en.wikipedia.org/wiki/IEC_61508).
- Achieved SIL is evaluated by three measures: Systematic Capability (SC), Architecture Constraints (Route 1h/2h), and Probability of Dangerous Failure analysis — [Wikipedia: IEC 61508](https://en.wikipedia.org/wiki/IEC_61508).
- IEC 62061 is the machinery-specific implementation of IEC 61508, applicable to system-level design of machinery safety-related electrical control systems — [Wikipedia: IEC 61508](https://en.wikipedia.org/wiki/IEC_61508).
- Risk assessment under ISO 13849-1 is based on ISO 12100 performed by the machine manufacturer; intrinsic risk (no safeguards) is determined first, then risk reduction achieved by controls — [Wikipedia: ISO 13849](https://en.wikipedia.org/wiki/ISO_13849).

### Inferences
- For small machinery, ISO 13849 is the practical path: it reuses ISO 12100 risk assessment and quantifies control-system reliability without requiring full IEC 61508 SIL analysis; IEC 62061 is the alternative for electrical control systems.
- A designer should size guards/interlocks to the PLr derived from risk assessment; Category 3/4 redundant architectures are needed for the highest risk functions (PL e).

### Gaps
- Exact ISO 12100 risk-assessment steps (hazard identification, risk estimation, risk evaluation, risk reduction hierarchy) are not reproduced here; the full text is paid (ISO 12100:2010, 77 pp). Source: [ISO 12100:2010](https://www.iso.org/standard/51528.html). Flag: unverified beyond abstract.

## CE Marking: Machinery Directive 2006/42/EC

### Takeaway
CE marking under the Machinery Directive requires satisfying Annex I essential health and safety requirements (EHSR), preparing a technical file, and issuing an EC declaration of conformity; most machinery is self-certified, but Annex IV high-risk machinery needs a notified body.

### Cited Findings
- Directive 2006/42/EC of the European Parliament and of the Council of 17 May 2006 on machinery (recast of 98/37/EC), OJ L 157, 9.6.2006, pp. 24–86; in force, current consolidated version 30/05/2026 — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Scope: machinery, interchangeable equipment, safety components, lifting accessories, chains/ropes/webbing, removable mechanical transmission devices, partly completed machinery; exclusions include vehicles, seagoing vessels, military/police machinery, research machinery, nuclear machinery, weapons, etc. — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- "Machinery" includes assemblies with a drive system other than directly applied human/animal effort, at least one moving part; partly completed machinery cannot perform a specific application on its own — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Article 5: before placing on market/putting into service, manufacturer or authorised representative must (a) satisfy Annex I EHSR, (b) ensure technical file (Annex VII Part A) available, (c) provide instructions, (d) carry out conformity assessment per Article 12, (e) draw up EC declaration of conformity (Annex II Part 1 Section A) accompanying machinery, (f) affix CE marking per Article 16 — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Article 7: machinery bearing CE marking + EC declaration of conformity is presumed compliant; machinery manufactured in conformity with a harmonised standard whose reference is published in the OJEU is presumed to comply with the EHSR covered by that standard — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Recital (23): manufacturer must carry out a risk assessment to determine applicable EHSR and measures — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Recital (24): technical construction file must be prepared before EC declaration of conformity; need not be permanently available in material form but must be available on request; need not include detailed plans of subassemblies unless essential — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Recital (20): manufacturers retain full responsibility for certifying conformity; for certain higher-risk machinery a stricter certification procedure is desirable — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Recital (21): CE marking is the only marking guaranteeing conformity; misleading marks prohibited — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Article 4: market surveillance; machinery may be placed on market/put into service only if it satisfies directive and does not endanger health/safety when properly installed, maintained, and used for intended purpose — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Article 6: at trade fairs/exhibitions non-conforming machinery may be shown with a visible sign indicating non-conformity and that it will not be made available until brought into conformity — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).

### Inferences
- For small machinery, compliance is typically via self-certification: apply harmonised standards (e.g., EN ISO 12100, EN ISO 13849, EN 60204-1) to gain presumption of conformity, compile technical file, sign EC DoC, affix CE mark.
- Annex IV machinery (e.g., certain lifting, woodworking, food-processing, injection-moulding machines) requires notified-body involvement; flag: exact Annex IV list not reproduced here.

### Gaps
- Annex I EHSR detailed clauses, Annex VII technical file contents, Annex II DoC template, and Annex IV high-risk machinery list require the full directive text; not fully reproduced. Source: [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).

## OSHA: 29 CFR 1910 (General Industry), 1926 (Construction), Machine Guarding, LOTO

### Takeaway
OSHA regulates workplace safety (not product certification); for machinery, 29 CFR 1910.212 requires point-of-operation guarding and 1910.147 requires lockout/tagout-capable energy isolating devices, with lockout-capable devices mandatory on new/replaced equipment after 1990.

### Cited Findings
- 29 CFR 1910.212 "General requirements for all machines": one or more methods of machine guarding shall protect operator and others from hazards such as point of operation, ingoing nip points, rotating parts, flying chips and sparks; examples include barrier guards, two-hand tripping devices, electronic safety devices — [OSHA 1910.212](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212).
- Guards shall be affixed to the machine where possible; guard shall not offer an accident hazard in itself — [OSHA 1910.212](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212).
- Point of operation is the area where work is performed on material; machines whose operation exposes an employee to injury shall have point-of-operation guarding conforming to appropriate standards, or designed to prevent any part of the body in the danger zone during the operating cycle — [OSHA 1910.212](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212).
- Machines usually requiring point-of-operation guarding include guillotine cutters, shears, alligator shears, power presses, milling machines, power saws, jointers, portable power tools, forming rolls and calenders — [OSHA 1910.212](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212).
- Revolving drums, barrels, containers shall be guarded by an enclosure interlocked with the drive so the container cannot revolve unless the guard is in place — [OSHA 1910.212](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212).
- Fan blades with periphery less than 7 ft above floor/working level shall be guarded with openings no larger than 1/2 inch — [OSHA 1910.212](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212).
- Machines designed for a fixed location shall be securely anchored to prevent walking/moving — [OSHA 1910.212](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212).
- 29 CFR 1910.147 LOTO: covers servicing/maintenance where unexpected energization/start-up or release of stored energy could cause injury; establishes minimum performance requirements for control of hazardous energy — [OSHA 1910.147](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147).
- After January 2, 1990, whenever replacement or major repair/renovation/modification of machine or equipment is performed, and whenever new machines are installed, energy isolating devices shall be designed to accept a lockout device — [OSHA 1910.147](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147).
- LOTO requires an energy control program: procedures, training, periodic inspections; lockout (or tagout if device not capable of being locked); energy control procedure documented; locks/tags singularly identified, standardized, substantial, identifiable; periodic inspection at least annually; training for authorized/affected/other employees — [OSHA 1910.147](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147).
- Construction industry is covered by 29 CFR 1926 (not 1910.147, which excludes construction/agriculture); 1926 has its own machine-guarding/lockout provisions. Flag: specific 1926 sections not verified here.

### Inferences
- A machine designer selling into the US should design energy-isolating devices (disconnects, valves) with lock hasps and provide lockout points; this is a design-for-compliance requirement even though LOTO is an employer program.
- Guarding design should follow ANSI/RIA standards (e.g., ANSI B11 series, RIA 15.06) in addition to OSHA; flag: ANSI/RIA specifics not verified here.

### Gaps
- OSHA state plans and sector-specific standards (1910 Subparts, 1926) not fully covered. Source: [OSHA machine guarding](https://www.osha.gov/machine-guarding).

## Pressure Vessels: ASME BPVC Section VIII, Section IX, B31

### Takeaway
ASME BPVC governs pressure-vessel design/construction (Section VIII), welding/brazing qualification (Section IX), and piping (B31 series); for small machinery these apply only when the machine contains a pressurized vessel or piping above applicable thresholds.

### Cited Findings
- ASME is the leading international developer of codes and standards for pressure technology, power plants, piping, nuclear components, etc. — [ASME Codes & Standards](https://www.asme.org/codes-standards).
- ASME offers certification & accreditation programs (e.g., ASME certification for pressure vessels) — [ASME](https://www.asme.org/certification-accreditation).
- Flag: specific ASME BPVC Section VIII Div. 1/2/3 design rules, Section IX welding procedure/performance qualification, and B31.1/B31.3 piping rules are drawn from established engineering knowledge, not verified against primary text in this research. Verify against current code editions before use.

### Inferences
- A small machine with an air receiver, hydraulic accumulator, or steam boiler may fall under ASME Section VIII and possibly jurisdictional boiler/pressure-vessel laws (state/local); design pressure, MAWP, hydrostatic test, nameplate, and inspection openings are typical requirements.
- Welded pressure parts require qualified WPS/PQR and welder performance qualification per ASME Section IX (or AWS/ISO equivalents).

### Gaps
- No primary ASME text fetched; thresholds, formulas, and edition years unverified. Source: [ASME Codes & Standards](https://www.asme.org/codes-standards).

## Electrical: IEC 60204-1, UL/CSA Standards

### Takeaway
IEC 60204-1 governs electrical equipment of machines (LV ≤1000 V AC / 1500 V DC), including EMC, overcurrent protection, bonding, emergency stop, safe torque off, control-circuit protection, testing, marking and documentation; UL/CSA provide North American safety certification via NRTL testing.

### Cited Findings
- IEC 60204-1 / EN 60204-1 "Safety of machinery — Electrical equipment of machines — Part 1: General requirements" covers electrical supply, EMC, overcurrent/overvoltage protection, short-circuit rating, protective bonding, shock protection, incoming supply and switching, safe torque off, emergency stop, control circuit protection, testing, marking and documentation — [Wikipedia: IEC 60204](https://en.wikipedia.org/wiki/IEC_60204).
- Scope: low-voltage machines (≤1000 V AC / ≤1500 V DC), supply frequency ≤200 Hz; excludes hand-portable machines and machines where electrical energy is directly used as a working tool; specialized machines covered by other parts (31 sewing, 32 hoisting, 33 semiconductor, 34 machine tools) — [Wikipedia: IEC 60204](https://en.wikipedia.org/wiki/IEC_60204).
- UL Solutions (formerly Underwriters Laboratories) is a global safety certification company and one of several OSHA-approved Nationally Recognized Testing Laboratories (NRTLs); UL Standards & Engagement develops standards — [Wikipedia: UL](https://en.wikipedia.org/wiki/UL_(safety_organization)).
- UL marks (UL Listed, UL Recognized Component) indicate product/component safety certification; Recognized Component Mark (ЯU) is used on components intended for UL-certified end products — [Wikipedia: UL](https://en.wikipedia.org/wiki/UL_(safety_organization)).
- CSA (Canadian Standards Association) operates similarly for Canada; UL Solutions of Canada issues certifications. Flag: CSA specifics not verified here.

### Inferences
- For CE marking, EN 60204-1 (harmonised) provides presumption of conformity for electrical equipment; for North America, UL/CSA listing is typically required by customers/inspectors even where not legally mandated for machinery.

### Gaps
- Specific UL/CSA standard numbers for machinery (e.g., UL 508A industrial control panels) beyond those listed in the UL standards catalog were not verified. Source: [Wikipedia: UL](https://en.wikipedia.org/wiki/UL_(safety_organization)).

## Environmental: RoHS, REACH, WEEE, Conflict Minerals

### Takeaway
Environmental compliance for machinery with electrical/electronic content requires RoHS substance restrictions, REACH chemical obligations (SVHC notification/authorisation), WEEE end-of-life producer responsibility, and (for SEC-reporting or EU-importing firms) conflict-minerals due diligence on 3TG.

### Cited Findings
- RoHS (2002/95/EC, recast 2011/65/EU) restricts 10 substances in EEE: Pb, Hg, Cd, Cr6+, PBB, PBDE, DEHP, BBP, DBP, DIBP; max 0.1% (1000 ppm) by weight per homogeneous material, 0.01% (100 ppm) for Cd — [Wikipedia: RoHS](https://en.wikipedia.org/wiki/RoHS).
- RoHS 2 requires CE marking as the only permitted indication of RoHS compliance; manufacturer must maintain technical file demonstrating conformity (via test data for all materials or harmonised standard EN IEC 63000:2018) — [Wikipedia: RoHS](https://en.wikipedia.org/wiki/RoHS).
- RoHS scope exclusions include large-scale stationary industrial tools, large-scale fixed installations, means of transport, non-road mobile machinery for professional use, R&D equipment, etc. — [Wikipedia: RoHS](https://en.wikipedia.org/wiki/RoHS).
- REACH (Regulation (EC) No 1907/2006) requires registration of substances manufactured/imported ≥1 tonne/year; SVHCs (253 on candidate list as of Feb 2026) require notification if present >0.1% by mass in articles and >1 tonne/year; authorisation for continued use — [Wikipedia: REACH](https://en.wikipedia.org/wiki/Registration,_Evaluation,_Authorisation_and_Restriction_of_Chemicals).
- REACH applies to chemicals in articles; "no data, no market" — unregistered substances cannot be supplied — [Wikipedia: REACH](https://en.wikipedia.org/wiki/Registration,_Evaluation,_Authorisation_and_Restriction_of_Chemicals).
- WEEE Directive 2012/19/EU: producer responsibility for collection, recycling, recovery of WEEE; crossed-out wheelie-bin marking; applies to EEE categories — [Wikipedia: WEEE](https://en.wikipedia.org/wiki/Waste_Electrical_and_Electronic_Equipment_Directive).
- Conflict minerals: US Dodd-Frank Section 1502 requires SEC-reporting companies to audit supply chains and report use of 3TG (tantalum, tin, tungsten, gold) from DRC/adjoining countries; reporting options: DRC Conflict Free / Not DRC Conflict Free / DRC Conflict Undeterminable — [Wikipedia: Conflict minerals law](https://en.wikipedia.org/wiki/Conflict_minerals_law).
- EU Regulation (EU) 2017/821 requires mandatory due diligence for EU importers of 3TG from conflict-affected/high-risk areas, effective July 2017 with some provisions deferred to Jan 2021 — [Wikipedia: Conflict minerals law](https://en.wikipedia.org/wiki/Conflict_minerals_law).
- OECD Due Diligence Guidance (2011) is the reference standard for conflict-minerals supply-chain traceability — [Wikipedia: Conflict minerals law](https://en.wikipedia.org/wiki/Conflict_minerals_law).

### Inferences
- Small machinery with PCBs, wiring, or electronic controls is in scope for RoHS/WEEE; purely mechanical machinery without electrical content is largely out of scope.
- REACH SVHC notification at 0.1% by mass is a common trigger for component suppliers; designers should request material declarations (IPC-1752) from suppliers.

### Gaps
- Conflict minerals cobalt (not yet codified in 3TG but under consideration) and other regional regimes (China RoHS) not fully covered. Source: [Wikipedia: Conflict minerals law](https://en.wikipedia.org/wiki/Conflict_minerals_law); [Wikipedia: RoHS](https://en.wikipedia.org/wiki/RoHS).

## Ergonomics: ISO 11226, ISO 14738

### Takeaway
Ergonomic compliance for machinery workstations requires ISO 11226 limits for manual handling/postures and ISO 14738 anthropometric requirements for workstation layout; these feed into Machinery Directive Annex I EHSR on human-machine interaction.

### Cited Findings
- Flag: ISO 11226 (manual handling) and ISO 14738 (anthropometric requirements for machinery workstations) are cited in the objective; specific clauses, edition years, and dimensional limits were not verified against primary sources in this research. Treat as training-knowledge references only.
- ISO 12100 (cited above) and the Machinery Directive Annex I require consideration of ergonomics/human factors in design — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042); [ISO 12100:2010](https://www.iso.org/standard/51528.html).

### Inferences
- Designers should provide adjustable workstation heights, reach envelopes, force limits, and avoid sustained awkward postures; these reduce musculoskeletal risk and support CE compliance.

### Gaps
- Primary ISO 11226/14738 text not fetched; all specifics unverified.

## How to Design for Compliance

### Takeaway
Design for compliance means: perform ISO 12100 risk assessment, apply the hierarchy of risk reduction (eliminate → substitute → safeguard → inform), size safety functions to PLr (ISO 13849) or SIL (IEC 61508), and provide guards, interlocks, emergency stops, lockout points, labeling, and documentation.

### Cited Findings
- ISO 12100 specifies principles of risk assessment and risk reduction to help designers achieve safety; procedures for identifying hazards and estimating/evaluating risks during relevant life-cycle phases, and for elimination of hazards or sufficient risk reduction; guidance on documentation and verification — [ISO 12100:2010](https://www.iso.org/standard/51528.html).
- ISO 13849-1 safety functions include safety-related stop, start/restart, manual reset, local control, muting, response time, safety-related parameters, fluctuation/loss/restoration of power sources — [Wikipedia: ISO 13849](https://en.wikipedia.org/wiki/ISO_13849).
- ISO 13849 Annex A decision tree (Figure A.1) determines required PL (PLr) from risk; not itself a risk-assessment tool — [Wikipedia: ISO 13849](https://en.wikipedia.org/wiki/ISO_13849).
- OSHA 1910.212: guarding methods include barrier guards, two-hand tripping devices, electronic safety devices; point-of-operation guarding must prevent any part of the body in the danger zone during the operating cycle — [OSHA 1910.212](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212).
- OSHA 1910.212: revolving drums/barrels/containers guarded by enclosure interlocked with drive so container cannot revolve unless guard in place — [OSHA 1910.212](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.212).
- Machinery Directive Annex I EHSR requires risk assessment, safety, and consideration of all life-cycle phases; technical documentation must include instructions — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).

### Inferences
- Practical design checklist for small machinery: (1) ISO 12100 risk assessment → hazard list + risk matrix; (2) define safety functions and PLr; (3) select guard type (fixed/movable/interlocked) + interlock category (ISO 13849); (4) emergency stop per ISO 13850 (flag: not verified here); (5) lockout points (OSHA 1910.147); (6) labeling/pictograms (ISO 7010); (7) technical file + DoC for CE.
- Interlocked movable guards should use trapped-key or safety-switch interlocks achieving at least Category 3 / PL d for high-risk points of operation.

### Gaps
- Specific guard design standards (EN 953, ISO 14120), emergency-stop standard (ISO 13850), and labeling standard (ISO 7010/ISO 1219) details not verified here.

## Certification Process: Self-Certification (CE), Third-Party (UL, CSA), Notified Body

### Takeaway
CE marking for most machinery is self-certification by the manufacturer (technical file + DoC + CE mark); Annex IV high-risk machinery requires notified-body conformity assessment; UL/CSA certification is voluntary third-party testing typically required by North American customers.

### Cited Findings
- Machinery Directive: manufacturer retains full responsibility for certifying conformity; for certain higher-risk machinery a stricter certification procedure is desirable — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- CE marking is the only marking guaranteeing conformity to the directive; machinery bearing CE mark + EC DoC is presumed compliant; conformity with published harmonised standards gives presumption of conformity with covered EHSR — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- Article 5 steps (EHSR, technical file, instructions, conformity assessment, DoC, CE mark) define the self-certification route — [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
- UL is one of several OSHA-approved NRTLs; UL Solutions (for-profit) performs product testing/certification, UL Standards & Engagement develops standards — [Wikipedia: UL](https://en.wikipedia.org/wiki/UL_(safety_organization)).
- IEC 61508 certification is third-party attestation by accredited certification bodies (e.g., exida, Intertek, SGS-TÜV, TÜV, UL) operating under ISO/IEC 17065 and accredited by national accreditation bodies under ISO/IEC 17011 — [Wikipedia: IEC 61508](https://en.wikipedia.org/wiki/IEC_61508).
- Notified body: EU member states designate notified bodies for conformity assessment of Annex IV machinery; manufacturer may choose self-certification for non-Annex-IV machinery. Flag: specific notified-body procedure modules (Annexes) not reproduced here.

### Inferences
- Certification cost/time trade-off: CE self-certification is low-cost but places liability on manufacturer; UL/CSA listing adds credibility and market access in North America; notified-body assessment is mandatory only for Annex IV machinery.

### Gaps
- Exact list of Annex IV machinery categories, notified-body procedure modules (A, B, C, etc.), and CSA-specific process not verified here. Source: [EUR-Lex 32006L0042](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0042).
