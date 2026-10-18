# DESIGN TEXTBOOKS: Pointer Guide for an AI Design Assistant

Purpose: help an AI design assistant (and the student it guides) pick the right book, chapter, or standard for any mechanical design question, and progress from beginner (0) to professional design engineer. This file is a pointer/guide only. It does not reproduce textbook equations or standard values; it routes you to the source that owns them.

Sources: six research notes in `research_notes/Machine design textbooks and CAD guide/` (listed in Section 7). Facts below are synthesized from those notes; unverified items are flagged in Section 6.

---

## 1. Purpose and how to use this guide

### 1.1 What this guide is

- A routing layer between a design question and the book/standard that owns the answer.
- A level map: which books belong at which stage of a designer's development.
- A citation discipline: every answer should name the book/standard, edition, and chapter/section (or clause/table) it came from.
- Not a substitute for the books or the standards: it contains no full derivations, no rated design values, and no licensed standard text.

### 1.2 AI pointer rules (follow in order)

1. Classify the question by topic using Section 2 (Master index) or Section 5 (Quick lookup).
2. Select the PRIMARY reference for that topic. If it is unavailable, out of scope, or contradicted by the user's context, use the SECONDARY reference, then the consult-when notes.
3. Cite the source in the answer: `Book Title, Author, edition, chapter/section` (and `Standard number, edition, clause/table` when a standard governs).
4. Never invent equations. Use only equation families named in the research notes or in the governing standard. If an equation is not verified, say so and point to the book/standard instead of deriving it.
5. Prefer the book's own equations and nomenclature. Do not silently translate between books (e.g., do not mix Shigley's Marin factors with Hamrock's notation without stating it).
6. State assumptions: jurisdiction (ASME vs ISO, inch vs metric, IS), unit system, material, process, and load type. These decide which book/standard applies.
7. Treat standards as normative and textbooks as pedagogical. For a production drawing, pressure vessel, gear rating, or weld size, the governing code (ASME/ISO/AWS/AGMA) wins over any textbook summary.
8. If the user asks "design the whole thing," route through the power-transmission integration texts (Mott, Shigley) and require interface consistency (shaft diameter -> bearing -> gear -> housing), not isolated part sizing.
9. If two books conflict, prefer the one matching the user's standard system and state the assumption (e.g., AGMA/ISO for Shigley/Norton/Hamrock; IS for Bhandari/Khurmi).
10. When data is missing (property tables, cost rates, software UI steps), mark it as a gap rather than fabricating a value.

### 1.3 When NOT to use a book

- Do not use a textbook to set a safety-critical limit (pressure vessel wall thickness, gear rating, weld size, structural bolt pretension). Use the governing code: ASME Section VIII / B31, AGMA 2001 / ISO 6336, AWS D1.1, ASTM/SAE, ASME B1.1/B18.
- Do not use a textbook's GD&T summary in place of ASME Y14.5 or ISO GPS when interpreting a production drawing. The standard is normative; the textbook is explanatory.
- Do not use an older or regional text (Spotts 2004, Khurmi unverified) for current standards data without cross-checking against a current standard or a modern text (Shigley/Norton/Hamrock).
- Do not use a materials textbook property table as a design allowable. Cross-check against supplier datasheets, MatWeb, or ASTM/ASME material specs.
- Do not use CAD/CAM theory texts (Zeid, Groover) as software manuals. For button-click steps, use the vendor's current documentation (Autodesk, PTC, SolidWorks).
- Do not use a single book for the whole journey. Kinematics, machine design, materials, manufacturing, and standards are different families; route by topic.

---

## 2. Master index: topic -> reference

Columns: Primary = first book/standard to open. Secondary = backup or deeper source. Consult when = trigger condition.

| Topic | Primary reference | Secondary reference | Consult when |
|---|---|---|---|
| Fasteners / screws (threaded) | Shigley, Ch. 8 (screws, fasteners, nonpermanent joints) | Bhandari, Ch. 6-7; Hamrock, Ch. 16; Mott, Ch. 17/19 | Thread stress, preload, joint stiffness, self-locking, IS threads, power screws |
| Shafts | Shigley, Ch. 7 (shafts and shaft components) | Norton MD (shafts/keys/couplings); Mott, Ch. 8; Bhandari, Ch. 9; Spotts, Ch. 3 | Deflection, critical speed, fatigue, key/coupling selection, ASME shaft design |
| Gears (spur/helical/bevel/worm) | Shigley, Ch. 13-15 (gears) | Mott, Ch. 9-10; Mabie, Ch. 4-7; Uicker, Ch. 6-10 | Gear bending/pitting stress, AGMA/ISO rating, geometry factors, minimum teeth |
| Bearings (rolling element) | Shigley, Ch. 11 (rolling-contact bearings) | Hamrock, Ch. 13 (deepest); Mott, Ch. 9; Bhandari, Ch. 15 | Bearing life (L10), load rating, selection from catalogs, lubrication |
| Bearings (journal / hydrodynamic) | Hamrock, Ch. 12 (hydrodynamic/hydrostatic) | Shigley, Ch. 12 (lubrication and journal bearings); Mott, Ch. 16 | Petroff/Sommerfeld, minimum film thickness, hydrostatic design |
| Springs | Shigley, Ch. 10 (mechanical springs) | Mott, Ch. 14; Bhandari, Ch. 10; Spotts, Ch. 4; Hamrock, Ch. 17 | Wahl factor, buckling, fatigue of springs, gas/wave springs |
| Clutches and brakes | Shigley, Ch. 16 (clutches, brakes, couplings, flywheels) | Mott, Ch. 22; Bhandari, Ch. 11-12; Spotts, Ch. 6; Hamrock, Ch. 18 | Friction materials, thermal capacity, band brakes, cone clutches |
| Belts and chains | Shigley, Ch. 17 (flexible mechanical elements) | Mott, Ch. 7; Bhandari, Ch. 13-14; Spotts, Ch. 6; Hamrock, Ch. 19 | Belt tension, chain pull, service factors, selection |
| Welded joints | Shigley, Ch. 9 (welding, bonding, permanent joints) | Mott, Ch. 15 (welded joints); Bhandari, Ch. 8; Spotts, Ch. 7; Hamrock (advanced welding) | Weld size, throat stress, fatigue of welds, AWS D1.1, ASME IX |
| Rivets / pins / keys / miscellaneous | Spotts, Ch. 12 (miscellaneous machine elements) | Shigley, Ch. 8-9; Mott; Bhandari | Keys, pins, snap/retaining rings, form synthesis |
| Fatigue (S-N, endurance limit) | Shigley, Ch. 6 (fatigue / variable loading) | Bannantine et al.; Dowling; ASM Handbook Vol. 19; Juvinall | Marin factors, endurance limit, cumulative damage, notched components |
| Fatigue (strain-life, Coffin-Manson) | Dowling, Mechanical Behavior of Materials | Bannantine et al.; Suresh | Low-cycle fatigue, strain-life, mean stress |
| Fracture mechanics (K, J, CTOD, Paris) | Anderson, Fracture Mechanics | Dowling; Hertzberg; Juvinall; Dieter | Crack size, damage tolerance, fracture toughness, Paris law |
| Failure theories (static) | Shigley, Ch. 5 (static loading) | Juvinall; Bhandari, Ch. 4; Spotts, Ch. 2 | von Mises, Tresca, Mohr-Coulomb, ductile vs brittle |
| Materials selection | Ashby, Materials Selection in Mechanical Design | Callister; Dieter | Performance indices, Ashby charts, cost-weighted selection |
| Tolerances and fits (metric) | ISO 286 (linear sizes) | Mott, Ch. 13; Shigley, Ch. 20 (GD&T); Machinery's Handbook | Hole/shaft fits (H7/g6), IT grades, general tolerances (ISO 2768) |
| Tolerances and fits (inch) | ANSI B4.1 (preferred limits and fits) | Machinery's Handbook | RC/LC/LT/LN/FN fits, tolerance grades |
| GD&T | ASME Y14.5 (US) or ISO 1101/ISO 5459/ISO 128/ISO 129 (international) | Giesecke; Madsen; Shigley, Ch. 20 | Feature control frames, datums, MMC/LMC, profile, runout |
| Kinematics and synthesis (linkages) | Norton, Design of Machinery | Uicker/Pennock/Shigley; Erdman and Sandor; Mabie; McCarthy and Soh | Mobility/Grashof, graphical/analytical synthesis, Burmester, curvature |
| Cams | Norton, Design of Machinery, Ch. 8 and Ch. 15 | Norton Cam Design and Manufacturing Handbook; Rothbart; Rao/Dukkipati | Cam profiles, follower motion, cam dynamics, manufacturing |
| Vibrations | Uicker/Pennock/Shigley, Ch. 17 | Rao and Dukkipati; Ghosh and Mallik; Singiresu Rao, Mechanical Vibrations | Natural frequency, critical speed, damping, balancing |
| FEA (modeling judgment) | Cook, Finite Element Modeling for Stress Analysis | Moaveni (ANSYS workflow); Logan (derivations); Reddy (theory) | Element choice, mesh, boundary conditions, loads, convergence |
| CAD modeling (theory) | Zeid, CAD/CAM Theory and Practice | Groover, CAD/CAM; Chang, CAD/CAM/CAE | Geometry kernels, transformations, splines, solid modeling representations |
| CAD modeling (practice) | Parametric texts (Shih/SDC) + vendor docs | Autodesk Fusion 360 Help | Feature trees, constraints, assemblies, drawings per kernel |
| Manufacturing processes | Kalpakjian and Schmid, Manufacturing Engineering and Technology | Groover, Fundamentals of Modern Manufacturing | Process selection, capabilities, tolerances, DFM rules |
| DFM / DFA | Boothroyd, Dewhurst, and Knight, Product Design for Manufacture and Assembly | Kalpakjian; Groover | Assembly time/cost, part count, process cost models, design rules |
| Standards (general) | Standards catalog: Machinery's Handbook + governing code | ASME/ISO/AWS/AGMA/ANSI/ASTM/SAE (see Section 3) | Pressure vessels, piping, welding, gears, fasteners, fits, materials |

---

## 3. Book catalog

Grouped by family. Each entry: Title / Author / Edition / Level / Owns / Key equations / Consult when / AI usage note. "Key equations" lists named equation families only (not formulas).

### 3.1 Machine design core

**Shigley's Mechanical Engineering Design**
- Authors: J. Keith Nisbett and Richard G. Budynas (legacy author Joseph E. Shigley); McGraw-Hill.
- Edition: 12th ed. (2024 US release / 2025 SI edition), 1120 pp.
- Level: junior-level undergrad through practicing engineer.
- Owns: static and fatigue failure theories, shafts, fasteners and nonpermanent joints, welded and permanent joints, springs, rolling and journal bearings, gears, clutches/brakes/couplings/flywheels, flexible elements, power-transmission case study, FEA intro, GD&T.
- Key equations: distortion-energy (von Mises) and maximum-shear (Tresca); Soderberg/Goodman/Gerber; Marin factors (ka-kf); Lewis gear bending; AGMA pitting/bending factors; Hertzian contact stress; Wahl spring stress factor; Johnson/Euler columns.
- Consult when: general component sizing with ANSI/AGMA/ISO standards; default reference when no specific book is indicated.
- AI note: broadest single-volume coverage; modern editions include FEA and GD&T chapters. Do not use as the default for IS-standard (Indian) problems. Edition numbering differs by region; state the edition.

**Norton, Machine Design: An Integrated Approach**
- Author: Robert L. Norton (WPI).
- Edition: 6th ed., 2021, 1120 pp., ISBN 978-0-13-751687-2.
- Level: junior to senior mechanical engineering.
- Owns: failure theory and analysis, fatigue (surface failure/pitting as a distinct topic), fracture mechanics intro, FEA, case studies of integrated assemblies, computer-aided solution workflows.
- Key equations: fatigue failure theories, surface failure/pitting, fracture mechanics intro, FEA.
- Consult when: fatigue-dominated high-cycle assemblies, FEA application, case-study integration of multiple elements (shaft-bearing-gear-housing).
- AI note: strongest on interfaces between elements. Weaker default for Indian/UK syllabi expecting IS and SI-only examples.

**Mott, Machine Elements in Mechanical Design**
- Authors: Robert L. Mott, Edward M. Vavrek, Jyhwen Wang.
- Edition: 6th ed., 2018, ISBN 978-0-13-444118-4.
- Level: undergraduate, mechanical engineering technology and first courses.
- Owns: complete power-transmission design flow (belts/chains, shafts, bearings, lubrication, spur/helical/bevel/worm gears, springs, screws/fasteners, welds), plus tolerances and fits, electric motors, linear motion, clutches/brakes.
- Key equations: power-transmission integration flow, tolerances-and-fits chapter, belt/chain/gear sizing.
- Consult when: design a complete gearbox/power transmission from motor to load; tolerances and fits; motor selection.
- AI note: best for interface consistency. Less graduate-level failure theory than Shigley/Norton. Check for a 7th ed. before citing.

**Juvinall and Marshek, Fundamentals of Machine Component Design**
- Authors: Robert C. Juvinall, Kurt M. Marshek.
- Edition: 7th ed., 2020, 800 pp., ISBN 978-1-119-72360-8.
- Level: undergraduate through graduate.
- Owns: fundamentals-to-component pipeline, failure theories, fatigue design, fracture mechanics (crack growth, stress intensity), material selection including composites, wear theory and wear models, graphical problem-solving (force-flow diagrams).
- Key equations: stress-intensity factors, crack growth under alternating loads, wear models.
- Consult when: fracture/fatigue-crack problems, wear questions, force-flow reasoning.
- AI note: best on "how to think about failure"; fewer commercial component-selection tables than Mott.

**Bhandari, Design of Machine Elements**
- Author: V. B. Bhandari.
- Edition: 5th ed., 2021, ISBN 978-93-90177-47-9 (4th ed. 2017, 934 pp.).
- Level: Indian B.Tech / competitive-exam preparation.
- Owns: IS-standard design, AICTE-aligned syllabus, IC engine components, cylinders and pressure vessels, flywheel design, step-by-step solved examples.
- Key equations: IS-based thread/bearing/gear specs, 356 solved examples (4th ed. counts).
- Consult when: IS standards, Indian manufacturing catalogs, GATE-style problems.
- AI note: cross-check modern ISO/AGMA against Shigley/Norton. 5th ed. page count not confirmed; verify edition.

**Spotts, Shoup, and Hornberger, Design of Machine Elements**
- Authors: M. F. Spotts, T. E. Shoup, L. E. Hornberger.
- Edition: 8th ed., 2004, 808 pp., ISBN 0-13-048989-1 (SI edition).
- Level: undergraduate.
- Owns: miscellaneous machine elements (keys, pins, snap rings, retaining rings), principles of form synthesis, design with plastic materials, structured example format (problem/given/assumptions/method/solution), spreadsheet modules.
- Key equations: structured example format template; plastics design.
- Consult when: miscellaneous elements, form synthesis, plastics, worked-example templates.
- AI note: last widely cited edition is 2004; dated on materials/manufacturing/FEA. Prefer Shigley/Norton for modern content. No 9th ed. verified.

**Hamrock, Jacobson, and Schmid, Fundamentals of Machine Elements**
- Authors: Steven R. Schmid, Bernard J. Hamrock, Bo. O. Jacobson.
- Edition: 3rd ed., 2013 (ISBN 978-1-4398-9132-2, 626 pp.); SI version 2014.
- Level: 3rd/4th-year undergraduate or reference for practicing engineers (requires calculus).
- Owns: tribology, hydrodynamic and hydrostatic bearings and seals, rolling-element bearings, lubrication, friction and wear, Hertzian contact, fatigue (staircase method), advanced welding, design synthesis of gears, modern case studies.
- Key equations: Hertzian contact, staircase endurance limit, bearing life and lubricant selection.
- Consult when: bearings, lubrication, tribology, Hertzian contact, advanced welding, statistical fatigue.
- AI note: tribology authority among these texts. Pair with Shigley (Shigley for sizing/standards, Hamrock for contact/bearing theory). No 4th ed. verified.

**Khurmi and Gupta, A Textbook of Machine Design**
- Authors: R. S. Khurmi, J. K. Gupta; S. Chand.
- Edition: latest S. Chand edition (not verified from a primary source).
- Level: Indian B.Tech programs and competitive exams.
- Owns: traditional machine design, IS-based design data, step-by-step problems (scope not verified beyond general coverage).
- Key equations: not verified in this research.
- Consult when: a syllabus or problem set explicitly references Khurmi.
- AI note: edition, year, page count, and TOC were not verified. Cross-check equations against Shigley/Bhandari.

**Other widely cited texts (secondary)**
- Maleev and Hartman, Machine Design; Burr and Cheatham, Mechanical Analysis and Design (2nd ed.); PSG College of Technology, Design Data Book of Engineers.
- Consult only when a syllabus or problem set explicitly references them. PSG Data Book is a data reference, not theory.

### 3.2 Kinematics and dynamics of machinery

**Norton, Design of Machinery: An Introduction to the Synthesis and Analysis of Mechanisms and Machines**
- Author: Robert L. Norton (WPI); McGraw-Hill.
- Edition: 6th ed., 2019/2020, ISBN 978-1-260-11331-0.
- Level: undergraduate to first graduate course.
- Owns: graphical and analytical linkage synthesis, position/velocity/acceleration analysis, cam design (kinematics and dynamics), gear trains, dynamic force analysis, balancing, engine dynamics, multicylinder engines, cam- and servo-driven mechanisms.
- Key equations: linkage synthesis, cam profiles, gear trains, dynamic force analysis, balancing.
- Consult when: linkage/cam/gear-train kinematics, mechanism synthesis, cam dynamics.
- AI note: route kinematics questions here; route stress/fatigue/sizing to machine design texts. Ships software appendices.

**Uicker, Pennock, and Shigley, Theory of Machines and Mechanisms**
- Authors: John J. Uicker Jr., Gordon R. Pennock, Joseph E. Shigley.
- Edition: 6th ed. (Cambridge, HB ISBN 9781009303675); 5th ed. (Oxford, ISBN 9780195371239).
- Level: undergraduate.
- Owns: planar, spherical, and spatial mechanisms; position/velocity/acceleration with advanced methods (instant centers, kinematic coefficients, Euler-Savary, Bobillier, centrodes, curvature); cams; spur/helical/bevel/worm gears; gear trains; linkage synthesis; spatial mechanisms and robotics; static and dynamic force analysis; vibration; engine dynamics; balancing; cam dynamics; flywheels; governors; gyroscopes.
- Key equations: advanced kinematic methods, curvature, spatial mechanism equations.
- Consult when: exhaustive kinematics, gear-family detail, spatial mechanisms, robotics.
- AI note: most exhaustive single-volume kinematics reference. Good breadth reference.

**Mabie and Reinholtz, Mechanisms and Dynamics of Machinery**
- Authors: Hamilton H. Mabie, Charles F. Reinholtz.
- Edition: 4th ed., 1991, 656 pp., ISBN 978-0-471-80237-2.
- Level: undergraduate course in kinematics.
- Owns: gear families (spur/nonstandard spur/bevel/helical/worm) with AGMA standards, force analysis of machinery, balancing, synthesis introduction, spatial mechanisms and robotics, cam motion specification.
- Key equations: AGMA gear standards, force-analysis methods, balancing.
- Consult when: AGMA gear sizing, force analysis, balancing.
- AI note: includes latest AGMA standards (as of 4th ed.) and BASIC/FORTRAN programs. Last cited edition is 1991; verify currency.

**Rao and Dukkipati, Mechanism and Machine Theory**
- Authors: J. S. Rao, R. V. Dukkipati.
- Edition: 2nd ed., 2006/2007, 624 pp.
- Level: undergraduate basic course (two-semester).
- Owns: cams, spur/helical/worm/bevel gears, gear trains, hydrodynamic lubrication, static/inertia/combined force analysis, flywheel, balancing of rotating components and linkages, gear forces, governors and gyroscopes, vibrations, critical speeds.
- Key equations: gear forces, balancing, vibrations, critical speeds.
- Consult when: vibrations and critical speeds, governors, balancing of linkages.
- AI note: unified coverage; useful for Indian curricula.

**Ghosh and Mallik, Theory of Mechanisms and Machines**
- Authors: Amitabha Ghosh, Asok Kumar Mallik.
- Edition: 2nd ed., 1988 (viii + 586 pp.); 3rd ed. also published.
- Level: undergraduate mechanisms and machines.
- Owns: kinematic analysis (graphical emphasis), synthesis, dynamic analysis, engine mechanisms, governors, balancing, cams, gears, gyroscopes, vibrations, rotating shafts.
- Key equations: engine mechanisms, governors, balancing, vibrations.
- Consult when: Indian syllabi, engine mechanisms, governors.
- AI note: more advanced/specialized topics than most undergraduate texts.

**Erdman and Sandor, Mechanism Design: Analysis and Synthesis**
- Authors: Arthur G. Erdman, George N. Sandor (with Sridhar Kota in 4th ed.).
- Edition: Vol. 1, 4th ed., 2001 (ISBN 978-0-13-040872-3); Vol. 2, Advanced Mechanism Design, 1984 (ISBN 0-13-011437-5).
- Level: Vol. 1 undergraduate; Vol. 2 graduate.
- Owns: computer-aided mechanism design; complex-number approach; Vol. 2: advanced synthesis (four/five-position motion generation, Burmester theory, circle/center-point curves, multiloop synthesis), curvature theory (centrodes, Euler-Savary, Bobillier, Ball's point), advanced dynamics (matrix/kinetostatics, time response, Lagrange, free/damped/forced vibration, rotor and linkage balancing, kineto-elastodynamics), spatial mechanisms and robotics (DH transforms).
- Key equations: Burmester theory, curvature (Euler-Savary, Bobillier), kineto-elastodynamics, shaking force/moment.
- Consult when: 4-5 position synthesis, curvature, elastodynamics, linkage balancing, spatial mechanisms.
- AI note: CAD/CAM/CAE emphasis; includes LINCAGES package.

**McCarthy and Soh, Geometric Design of Linkages**
- Authors: J. Michael McCarthy, Gim Song Soh.
- Edition: 2nd ed., 2010/2011, ISBN 978-1-4419-7891-2 / 978-1-4614-2767-4.
- Level: graduate/advanced (interdisciplinary applied mathematics).
- Owns: mathematical theory of design for articulated mechanical systems; algebraic synthesis (constraint equations, bilinear structure, five-position solution); planar, spherical, and spatial chains; dyad/triad synthesis; platform manipulators.
- Key equations: constraint-equation synthesis, dual quaternions, Plucker coordinates.
- Consult when: algebraic (constraint-equation) synthesis, spherical/spatial linkage synthesis, platform manipulators.
- AI note: mathematical (not graphical) synthesis foundation; useful for coding synthesis.

**Norton, Cam Design and Manufacturing Handbook (companion)**
- Author: Robert L. Norton; Industrial Press.
- Edition: 3rd ed.
- Level: practitioner.
- Owns: comprehensive cam design and manufacturing; spline functions; cam research.
- Consult when: cam design and manufacturing depth beyond a chapter.
- AI note: specialized cam reference.

**Other kinematics texts (secondary)**
- Rothbart, Cams: Design, Dynamics, and Accuracy (Wiley, 2004): cam dynamics/accuracy.
- Hartenberg and Denavit, Kinematic Synthesis of Linkages (McGraw-Hill, 1964): classic analytical synthesis (dyads, Burmester).
- Jensen, Classical and Modern Mechanisms for Engineers and Inventors (Marcel Dekker, 1991): mechanism catalog/number synthesis.
- Khurmi and Gupta, Theory of Machines (S. Chand); Rattan, Theory of Machines (McGraw-Hill): Indian undergraduate mechanisms.
- Singiresu S. Rao, Mechanical Vibrations (Pearson): vibration analysis reference.

### 3.3 CAD/CAM/CAE, drawing, and GD&T

**Zeid, CAD/CAM Theory and Practice**
- Author: Ibrahim Zeid; McGraw-Hill.
- Level: undergraduate junior/senior to early graduate; theory-oriented.
- Owns: geometric modeling (wireframe, surface, solid; B-rep, CSG), coordinate transformations, Bezier/B-spline/NURBS, NC/CNC part programming, tool-path generation, CAD data exchange (IGES/STEP concepts), FEM overview, robotics and group technology.
- Key equations: transformations, spline basis, B-rep vs CSG trade-offs.
- Consult when: geometric modeling theory, curve/surface math, solid-modeling representations, NC tool-path logic.
- AI note: authority for theory; not a modern parametric CAD UI guide. Cross-check NC code against ISO 6983 and machine manuals.

**Groover, CAD/CAM: Computer-Aided Design and Manufacturing**
- Author: Mikell P. Groover; Pearson.
- Level: undergraduate junior/senior; applied.
- Owns: CAD fundamentals and hardware, geometric modeling, design analysis (FEA/optimization overview), NC programming and CNC, DNC, group technology and cellular manufacturing, FMS, CAPP, CAD/CAM databases and CIM, rapid prototyping.
- Key equations: process-level CAD-to-CAM data flow, CAPP.
- Consult when: CAD-to-CAM pipeline, NC/G-code logic, group technology/CAPP, CIM concepts.
- AI note: balances CAD theory with manufacturing reality. Pair with Zeid for deeper geometry math.

**Chang (et al.), CAD/CAM/CAE**
- Author: commonly attributed to Tien-Chien Chang et al.; edition/authorship varies by publisher.
- Level: undergraduate through graduate; comprehensive.
- Owns: full CAx chain (CAD modeling, CAM NC/tool paths, CAE FEA/optimization/tolerancing/assembly).
- Key equations: integration concepts across the digital thread.
- Consult when: reasoning across design-to-analysis-to-manufacturing rather than one domain.
- AI note: use as a map of the CAx pipeline; defer to domain texts for depth. Exact edition/author/ISBN not verified; confirm before citing pages.

**Parametric modeling texts (vendor-specific)**
- Titles/authors: SDC Publications tutorials (e.g., Randy Shih, Parametric Modeling with Creo Parametric / SolidWorks series); PTC's own Creo training.
- Level: beginner to intermediate practitioner; software-specific.
- Owns: design intent, sketch constraints, parametric features (extrude, revolve, sweep, loft), parent/child relationships, assemblies and mates, configurations, drawings from models, sheet metal.
- Consult when: generating or interpreting parametric feature sequences, constraint sets, or assembly mate definitions for a specific CAD kernel.
- AI note: mirror vendor-specific idioms; always tag advice with target CAD system/version. Use official vendor docs for API/automation.

**Autodesk Fusion 360 official documentation**
- Source: Autodesk Help (https://help.autodesk.com/view/fusion360/ENU/).
- Level: beginner to advanced practitioner; software-specific.
- Owns: parametric modeling, T-splines/surfacing, assemblies, drawings, simulation (static, modal, thermal), generative design, CAM toolpaths (2.5D/3D/5-axis), post-processors, additive manufacturing.
- Consult when: Fusion 360 scripts, toolpaths, generative-design parameters, simulation setup.
- AI note: authoritative for Fusion-specific commands/parameters. Cloud features change frequently; cite the help URL and version.

**Giesecke et al., Technical Drawing with Engineering Graphics**
- Authors: Frederick E. Giesecke (deceased), Shawna Lockhart, et al.
- Edition: 15th ed., 2021/2022, ISBN 9780137400140.
- Level: undergraduate freshman/sophomore engineering graphics.
- Owns: visualization, sketching, orthographic projection, sections, auxiliary views, dimensioning, tolerancing, threads and fasteners, working drawings and revision control, surface finish, gears and cams, welding representation, axonometric/perspective.
- Key equations: drawing conventions, view generation, thread/fastener callouts.
- Consult when: producing or interpreting 2D engineering drawings, views, sections, dimensioning schemes, thread/fastener callouts.
- AI note: de-facto US engineering-graphics text; standards-aligned (ANSI/ASME + ISO). Pair with ASME Y14.5/ISO for tolerance semantics.

**Madsen, Engineering Drawing and Design**
- Author: David A. Madsen.
- Edition: ISBN 978-1111309572 (Delmar/Cengage).
- Level: undergraduate engineering graphics/drafting; applied.
- Owns: drafting standards and conventions, CAD-based drawing, orthographic/auxiliary/section views, dimensioning and tolerancing, GD&T, threads and fasteners, working drawings, welding, gears/cams, piping and structural drawings.
- Consult when: production drawings, drafting standards, CAD-based documentation workflows.
- AI note: more manufacturing/documentation-oriented than Giesecke. Cross-check standards since editions track evolving standards.

**ASME Y14.5, Dimensioning and Tolerancing (GD&T standard)**
- Source: ASME/ANSI; current revision 2018 (344 pp.), reviewed about every 10 years.
- Level: professional standard; authoritative rule set.
- Owns: symbols, datums, form/orientation/location/profile/runout tolerances, material-condition modifiers (MMC/LMC/RFS), rules and defaults, feature control frames, bonus tolerance, projected tolerance zones.
- Consult when: assigning or interpreting a GD&T callout, feature control frame, datum scheme, or material-condition modifier on an ASME-governed drawing.
- AI note: normative for ASME-governed drawings; cite specific section/figure. Do not mix ASME and ISO GPS rules. Note 2018 dropped concentricity/symmetry (vs 2009).

**ISO 128 family (technical product documentation presentation)**
- Source: ISO (ISO 128-1:2020, 128-2:2020, 128-3:2022, etc.).
- Level: international standard.
- Owns: general principles of presentation (lines, views, sections, cuts, projection methods) for manual and CAD drawings.
- Consult when: producing or interpreting drawings to ISO conventions.
- AI note: use for line types, view layout, section conventions on ISO-governed drawings. Pair with ISO 129 for dimensions.

**ISO 129 (presentation of dimensions and tolerances)**
- Source: ISO (ISO 129-1:2018, etc.).
- Level: international standard.
- Owns: how dimensions and tolerances are presented on technical drawings (ISO conventions).
- Consult when: dimensioning a drawing to ISO conventions or interpreting ISO dimension/tolerance callouts.
- AI note: do not conflate with ASME Y14.5 rules.

**ISO 286 (linear-size tolerances)**
- Source: ISO (ISO 286-1:2010, ISO 286-2:2010).
- Level: international standard.
- Owns: ISO tolerance system for linear sizes: IT grades, fundamental deviations, hole-basis and shaft-basis fits, preferred sizes.
- Consult when: selecting a fit (e.g., H7/g6) or computing tolerance limits for cylindrical features on ISO-governed parts.
- AI note: covers size tolerances only, not form/position. Cross-check with ISO 406 and ISO 1101.

**FEA texts**
- Cook, Finite Element Modeling for Stress Analysis (Wiley): modeling decisions, meshing, loads, boundary conditions, result interpretation, convergence. Consult for FEM model setup and sanity-checking.
- Moaveni, Finite Element Analysis: Theory and Application with ANSYS (Pearson): introductory FEA plus ANSYS workflow. Consult for beginner FEA workflow; verify ANSYS steps against current docs.
- Logan, A First Course in the Finite Element Method (Cengage): stiffness-matrix formulation from first principles. Consult for derivations and hand calculations.
- Reddy, An Introduction to the Finite Element Method (McGraw-Hill): variational principles, weak forms, convergence. Consult for theoretical foundations and proofs.

### 3.4 Materials and failure

**Callister, Materials Science and Engineering: An Introduction**
- Authors: William D. Callister Jr. (and David G. Rethwisch in later editions); Wiley.
- Edition: 10th ed., 2018, 992 pp., ISBN 978-1-119-40549-8.
- Level: undergraduate freshman/sophomore.
- Owns: structure, properties, processing, and performance of metals/ceramics/polymers/composites; corrosion, failure, phase diagrams; mechanical properties (stress-strain, hardness, fatigue, creep, fracture).
- Key equations: stress-strain, hardness, fatigue/creep introductions, phase diagrams.
- Consult when: material selection by property, stress-strain curves, phase diagrams, heat treatment, failure modes.
- AI note: property and processing authority. Cross-check specific values against supplier datasheets/MatWeb. Cite edition (tables vary).

**Ashby, Materials Selection in Mechanical Design**
- Author: Michael F. Ashby; Butterworth-Heinemann/Elsevier.
- Edition: multiple editions (1st 1992; newer through 2024).
- Level: undergraduate junior/senior through graduate; design-oriented.
- Owns: systematic materials selection, performance indices, material property charts (Ashby charts), cost models, case studies (shafts, beams, springs, pressure vessels).
- Key equations: performance indices (strength/density, stiffness/density), selection methodology.
- Consult when: ranking or selecting materials for a function, computing performance indices.
- AI note: definitive materials-selection methodology. Combine with Callister (property detail) and Dieter (metallurgical depth). Verify indices against updated databases (CES/MaterialUniverse).

**Dieter, Mechanical Metallurgy**
- Author: George E. Dieter (with Bacon in later editions); McGraw-Hill.
- Edition: 3rd ed., 1988 (1st ed. 1961).
- Level: graduate/advanced undergraduate; metallurgy-focused.
- Owns: mechanical behavior of metals: elasticity, plasticity, dislocations, strengthening mechanisms, fracture, fatigue, creep, testing, metal forming mechanics.
- Key equations: yield criteria, work hardening, strengthening, fracture/fatigue/creep of metals.
- Consult when: plastic deformation, strengthening, fatigue crack growth, fracture toughness, metal-forming mechanics.
- AI note: deep metallurgical treatment. Reflects mid-20th-century metallurgy; cross-check modern alloys/standards.

**Dowling, Mechanical Behavior of Materials**
- Authors: Norman E. Dowling (with Kampe and Kral in later editions); Pearson.
- Edition: 4th ed., 2012/2013.
- Level: undergraduate/graduate.
- Owns: mechanical behavior across metals, polymers, ceramics, composites; stress-strain, fatigue (S-N, strain-life, fracture mechanics), creep.
- Key equations: S-N, strain-life (Coffin-Manson), fracture mechanics, creep.
- Consult when: S-N/strain-life fatigue life, creep of non-metals, fracture mechanics.
- AI note: comprehensive across material classes.

**Anderson, Fracture Mechanics: Fundamentals and Applications**
- Author: Ted L. Anderson; CRC Press.
- Edition: 4th ed., 2017 (1st ed. 1991).
- Level: graduate/advanced.
- Owns: LEFM/EPFM, stress intensity, K_IC, J-integral, CTOD, R-curves, dynamic fracture, fatigue crack growth.
- Key equations: K, J, CTOD, Paris law.
- Consult when: K_IC, J, CTOD, damage-tolerance crack sizes.

**Suresh, Fatigue of Materials**
- Author: Subra Suresh; Cambridge University Press.
- Edition: 2nd ed., 1998 (1st ed. 1991).
- Level: graduate/advanced.
- Owns: fatigue mechanisms, crack initiation and propagation, low/high-cycle, multiaxial, environmental and thermal fatigue, fatigue of composites/ceramics.
- Key equations: fatigue thresholds, closure, multiaxial/environmental fatigue.
- Consult when: fatigue thresholds, closure, multiaxial/environmental fatigue.

**Bannantine, Comer, and Handrock, Fundamentals of Metal Fatigue Analysis**
- Authors: Julie A. Bannantine, Jess J. Comer, James L. Handrock; Prentice Hall.
- Edition: 1990.
- Level: undergraduate/graduate.
- Owns: practical fatigue of notched components: S-N, strain-life, fracture mechanics, mean-stress corrections, cumulative damage.
- Key equations: notched-component fatigue life, cumulative damage.
- Consult when: notched-component fatigue life, cumulative damage.

**Hertzberg, Vinci, and Hertzberg, Deformation and Fracture Mechanics of Engineering Materials**
- Authors: Richard W. Hertzberg, Richard P. Vinci, Jason L. Hertzberg; Wiley.
- Edition: 5th ed., 2012 (1st ed. 1976).
- Level: undergraduate/graduate.
- Owns: deformation, fracture, fatigue, and creep across metals, polymers, ceramics, composites.
- Key equations: deformation, fracture, fatigue, creep across material classes.
- Consult when: deformation/fracture across multiple material classes.

**ASM Handbook, Vol. 11 (Failure Analysis and Prevention) and Vol. 19 (Fatigue and Fracture)**
- Source: ASM International.
- Level: professional reference.
- Owns: failure modes, fractography, case histories, material-specific fatigue/fracture data.
- Consult when: failure-mode identification, fractography, case histories, data.

**Shigley (materials/failure context)**
- Use Shigley for machine-design failure criteria, endurance limits, stress concentration, and component design. See 3.1.

### 3.5 Manufacturing and DFM

**Kalpakjian and Schmid, Manufacturing Engineering and Technology**
- Authors: Serope Kalpakjian, Steven R. Schmid; Pearson.
- Level: undergraduate sophomore/junior; comprehensive.
- Owns: casting, forming, machining, joining, finishing, materials, metrology, CNC, automation, lean/quality, DFM.
- Key equations: process capabilities, tolerances, machining allowances, DFM rules.
- Consult when: choosing or comparing manufacturing processes, setting tolerances/machining allowances, DFM advice.
- AI note: broadest single-volume manufacturing reference; process-capability and DFM authority. Cross-check feeds/speeds/tolerances against vendor data.

**Groover, Fundamentals of Modern Manufacturing**
- Author: Mikell P. Groover; Wiley.
- Level: undergraduate; systems-oriented.
- Owns: engineering materials, casting/forming/machining/joining, CNC and automation, industrial robotics, FMS, group technology, lean production, quality control, sustainable manufacturing.
- Key equations: manufacturing systems, automation, lean.
- Consult when: automation, robotics, FMS, lean, system-level manufacturing decisions.
- AI note: complement to Kalpakjian (Kalpakjian for process mechanics, Groover for systems/automation/lean).

**Boothroyd, Dewhurst, and Knight, Product Design for Manufacture and Assembly (PDMA)**
- Authors: Geoffrey Boothroyd, Peter Dewhurst, Winston A. Knight; CRC Press/Taylor and Francis.
- Level: undergraduate design through practitioner; method-focused.
- Owns: DFMA: quantifying manufacturability and assemblability, estimating manufacturing cost and assembly time, redesign for fewer parts and easier assembly.
- Key equations: DFA (assembly time/cost, handling/insertion), DFM (machining cost models, process selection), design rules, part consolidation, tolerance/cost trade-offs.
- Consult when: evaluating a design for assembly cost, part count, or manufacturability; proposing DFM/DFMA redesigns with quantified savings.
- AI note: authoritative quantitative DFMA method. Verify cost constants against current labor/rate data (book rates are dated).

### 3.6 Standards and handbooks

**Machinery's Handbook**
- Source: Industrial Press, New York; continuous publication since 1914; 32nd edition announced.
- Level: universal desk reference.
- Owns: mathematics, mechanics and strength of materials, properties/treatment/testing of materials, dimensioning/gaging/measuring, tooling, machining, manufacturing processes, fasteners, etc.
- Consult when: thread dimensions, fits, material properties, machining data, general lookup.
- AI note: fastest lookup for data; not design authority. Companion Machinery's Handbook Guide (32nd ed.) teaches table/formula use.

**Roark's Formulas for Stress and Strain**
- Authors: Roark, Young, now Budynas and Sadegh; McGraw-Hill.
- Edition: 9th ed., March 2020 (first published 1938).
- Level: practitioner reference.
- Owns: analytical formulas for stresses, strains, deflections; tables organized chapter/table/case/subcase; bearing/shear stress, stress concentrations, material behavior, stress/strain measurement, fatigue and fracture mechanics, stresses in fasteners/joints, composites.
- Consult when: stress/deflection formulas, stress concentration factors, fastener/joint stresses.
- AI note: formula handbook; not a design code.

**Marks' Standard Handbook for Mechanical Engineers**
- Source: McGraw-Hill; first published 1916 by Lionel S. Marks.
- Edition: 12th ed., 2017 (100th anniversary); 160+ expert contributors.
- Level: broad reference.
- Owns: math tables, units, mechanics of solids, material properties, applied mechanics, ethics, digital control, sensors/actuators, vehicle electrification (new in 12th).
- Consult when: broad mechanical data, material properties, applied mechanics.
- AI note: broad data; not component-sizing methodology.

**Perry's Chemical Engineers' Handbook**
- Source: McGraw-Hill; first published 1934.
- Edition: 9th ed., 2018; about 2,700 pp., 1,900 illustrations.
- Level: process/chemical reference.
- Owns: mass/energy balance, heat transfer, fluid flow, thermodynamics, distillation, reactors.
- Consult when: process/mechanical interface, heat exchangers, pressure vessels, thermal systems.
- AI note: process/fluid domain; not machine design.

**Crane Technical Paper No. 410, Flow of Fluids Through Valves, Pipes, Pumps, and Fittings**
- Source: Crane; introduced 1942.
- Editions: 2018/2020/2022.
- Level: fluid-flow reference.
- Owns: K-factors, friction losses, pipe sizing, pumps, control valves, flow meters, heat transfer.
- Consult when: pipe sizing, pressure drop, pump selection, valve losses.
- AI note: fluid-flow authority; pair with Perry's.

**ASME standards (mechanical design)**
- Y14.5 Dimensioning and Tolerancing (GD&T): 2018/2019, 344 pp.; 17 standards in Y14 series.
- Y14.100 Engineering Drawing Practices: 2017, 64 pp.
- B1.1 Unified Inch Screw Threads (UN/UNR/UNJ): 2024 ed.
- B18 Fasteners: dimensions, materials, testing, quality assurance (B18.18), PIN code (B18.24).
- Section VIII Rules for Construction of Pressure Vessels: Div. 1/2/3.
- B31 Code for Pressure Piping: B31.1, B31.3, B31.4, B31.5, B31.8, B31.9, B31.12.
- Section IX Welding, Brazing, and Fusing Qualifications: WPS/PQR/welder qual.
- Consult when: pressure-containing parts, structural welding, inch threads/fasteners, drawing practices.
- AI note: copyrighted; only scope/abstract publicly available. Never compute pressure vessel thickness from Shigley alone.

**ISO standards (mechanical design)**
- ISO 286: linear-size tolerances, IT grades, hole/shaft fits (2010).
- ISO 128: technical product documentation presentation (lines, views, sections).
- ISO 129: presentation of dimensions and tolerances.
- ISO 8015: GPS fundamentals (independency, envelope, rigid workpiece, 20 C reference).
- ISO 2768: general tolerances (being revised into a single ISO 2768, 2026 ed.).
- ISO 9001: quality management systems (2015; 2026 revision underway).
- ISO 14001: environmental management systems (2015; 2026 revision underway).
- ISO 898: mechanical properties of fasteners (property classes 4.6-12.9).
- Consult when: metric tolerances/fits, international drawings, QMS/EMS, metric fasteners.
- AI note: ISO GPS is a coherent system; state the standard system before applying tolerances.

**Fastener standards**
- SAE J429: inch bolt grades 2/5/8 with head markings.
- ISO 898: metric property classes 4.6-12.9.
- ASME B18: fastener dimensions and quality.
- ASTM specs: A307, A325, A490, A354, F3125, F436, A563, A194, F568M (structural bolts).
- Nut grades: SAE J995 (inch), ISO 898-2 (metric).
- Consult when: fastener selection by grade/property class.
- AI note: never mix SAE grade numbers with metric property classes. State unit system.

**Gear, welding, and piping standards**
- AGMA 2001-D04: fundamental rating factors and calculation methods for involute spur and helical gear teeth (for experienced gear designers; empirical factors).
- AGMA 6102-C15: vehicle power transmission gears; AGMA 911-B21: aerospace gears.
- ISO 6336: gear rating (scope not individually researched here).
- AWS D1.1/D1.1M: structural welding code-steel (2025 ed., 25th); carbon/low-alloy steels >= 1/8 in, yield <= 100 ksi; referenced by IBC and AISC 360.
- ASME Section IX: welding/brazing/fusing qualification.
- ASME B31: piping.
- Consult when: gear rating, structural steel welding, pressure equipment welding qual.
- AI note: AGMA rating factors require experience and judgment; cite standard numbers, do not invent factors.

**Tolerance and fit standards**
- ANSI B4.1: preferred limits and fits for cylindrical parts (inch): RC/LC/LT/LN/FN fit groups, 10 tolerance grades, basic sizes up to 19.69 in.
- ISO 286: metric hole/shaft fits.
- ISO 2768: general tolerances for untoleranced features (applies only when referenced in title block).
- ISO 8015: GPS fundamentals (independency/envelope principles).
- ASME Y14.5: GD&T.
- Consult when: fit selection, general tolerances, GD&T.
- AI note: do not mix inch fit classes (RC/LC/FN) with metric tolerance grades (IT6/IT7).

**Material standards and designations**
- AISI/SAE steel grade system: four-digit designation; first two digits = alloy family; last two = carbon content (x0.01%); prefixes B/C/D/E for manufacturing method; suffix H for hardenability. AISI ceased writing specs; now SAE designations.
- ASTM International: 13,000+ standards; material specs and test methods.
- ASME Section II: materials; referenced by Section VIII/B31 for allowables.
- Consult when: interpreting steel grades, material specs, allowables.
- AI note: "AISI 4140" is a composition designation only, not a full material spec; mechanical properties require ASTM/SAE/ASME spec plus heat treatment.

---

## 4. Zero to professional roadmap

Stages, typical durations, core focus, books, skills, projects, certifications, and desk references. Paths vary by country, institution, and industry.

| Stage | Duration | Core focus | Key books/resources | Software | Certifications | Demonstrator projects | Desk references |
|---|---|---|---|---|---|---|---|
| 0. Pre-engineering | Years -1 to 1 | Calculus, physics, chemistry, intro programming, sketching | Calculus/physics texts; Callister (intro); Giesecke (drawing) | Basic CAD (Fusion 360/SolidWorks student) | None | Make a simple part; read a drawing | None |
| 1. Freshman/sophomore (engineering science) | Years 1-2 | Statics, dynamics, mechanics of materials, thermofluids, materials, numerical methods | Callister; Shigley ch.1-4,20; Zeid/Groover (CAD theory); Kalpakjian (manufacturing overview); Logan (FEA intro) | CAD modeling; Excel/MATLAB | None | Cornerstone design project; SAE Mini Baja/Formula SAE | None |
| 2. Junior (component design) | Year 3 | Machine elements, kinematics, FEA, manufacturing processes, materials selection | Shigley (full); Norton Design of Machinery; Mott; Hamrock (bearings); Cook (FEA); Ashby; Kalpakjian; Boothroyd-Dewhurst | SolidWorks/Creo/Inventor; ANSYS/SolidWorks Simulation | FE exam prep (EIT) | Size a shaft/bearing/spring; gearbox design; tolerance stack-up | Shigley; Machinery's Handbook |
| 3. Senior (system design) | Year 4 | Capstone, DFM, GD&T, standards, PLM, testing | Shigley; Norton Machine Design; Madsen; ASME Y14.5; ISO 286/2768; AGMA 2001 (if gears) | SolidWorks + PDM; FEA; CAM awareness | GDTP Technologist; FE exam | Capstone with standards and realistic constraints; tested prototype | Shigley; Y14.5; ISO 286 |
| 4. Junior practitioner (EIT) | 0-3 yr | Supervised execution, drawings, basic DFM, basic FEA | Shigley; Machinery's Handbook; Roark's; ASME Y14.5; ISO 286 | Deep in one CAD kernel; one FEA tool | EIT/EI; GDTP Technologist | Tolerance-stack bracket; welded frame; released drawing set with ECO | Machinery's Handbook; Roark's; Y14.5 |
| 5. Mid-career (owner) | 3-8 yr | Subsystem ownership, specialization, mentoring, validation | Norton MD; Juvinall (fracture/wear); Reddy (FEM); Dieter/Dowling/Anderson; Boothroyd-Dewhurst | CAD + FEA + CAM literacy; PLM | PE license (US) / IEng (UK); GDTP Senior | Owned subsystem with EVT/DVT/PVT; DFM cost reduction | Roark's; Marks'; Boothroyd-Dewhurst |
| 6. Senior/lead (technical authority) | 8-15 yr | System/platform ownership, standards authority, cross-team leadership | Roark's; Marks'; ASM Handbook; Perry's/Crane TP-410 (domain); AGMA/ASME Section VIII/B31 (domain) | Full CAE; CFD/thermal as needed | CEng (UK); PE (US) | System platform with standards compliance; mentoring; design standards | Marks'; ASM Handbook; domain standards |
| 7. Executive/fellow | 15+ yr | Technology strategy, budget, organization | Domain-specific references; standards committees | Strategy, not tools | Technical Fellow / Director / VP / CTO | Multi-year technology roadmaps | Domain references |

Core competencies of a professional design engineer (from ABET outcomes, IISE body of knowledge, and job postings): mechanics/materials fundamentals; component sizing and failure analysis (static + fatigue, fracture, wear); mechanism/kinematics and tolerancing; CAD/parametric modeling and 2D drawing with GD&T; FEA/CAE setup and validation; manufacturing-process selection and DFM/DFA; material selection; standards application; PLM/ECO and documentation; communication, teamwork, and project leadership.

Certifications and standards knowledge expected:
- US: ABET-accredited BS + FE exam (EIT/EI) + PE license (4 years progressive experience + PE exam). GDTP Technologist (no experience) / GDTP Senior (3 years GD&T experience) for ASME Y14.5. Standards: ASME Y14.5, Y14.100, B1.1, B18, Section VIII, B31, Section IX; ISO 286, 128, 129, 8015, 2768, 9001, 14001, 898; ANSI B4.1; SAE J429; ASTM specs; AGMA 2001; AWS D1.1.
- UK/Commonwealth: IMechE EngTech/IEng/CEng (academic + experience + competence demonstration against 5 core competences).
- Domain: AWS D1.1 welding; ASME Section VIII/B31 pressure equipment; ISO 9001/14001; industry standards (AS9100, IATF 16949, Stanag) as required.

Software skills expected: deep in one CAD kernel (SolidWorks most requested; AutoCAD for 2D; Creo, Inventor, CATIA, NX, Fusion 360); FEA (ANSYS, Abaqus, SolidWorks Simulation); CAM awareness (Fusion 360 CAM, Mastercam); PLM/PDM (Windchill, Arena, SolidWorks PDM); Excel/MATLAB/Python for automation. Depth in one kernel beats surface knowledge of many.

Demonstrator project ladder: (0) make a part and read its drawing; (1) tolerance stack-up on a mating assembly; (2) size a component (shaft/bearing/spring) by hand to Shigley; (3) full gearbox/power-transmission design (Mott-style); (4) FEA-validated, DFM-reviewed, GD&T-dimensioned part released to manufacturing with ECO; (5) owned subsystem with validation plan (EVT/DVT/PVT); (6) system/platform with standards compliance and team leadership.

---

## 5. Topic-to-book decision tree / quick lookup

Step 1: Identify the question family.
- Stress/deflection formula -> Roark's; then verify against code.
- Component sizing with standards -> Shigley (default) or Mott (integration) or Bhandari (IS).
- Fatigue life (cycles) -> Shigley (endurance) + Dowling/Bannantine (S-N/strain-life).
- Crack growth/damage tolerance -> Anderson; then Dowling/Hertzberg.
- Material choice -> Ashby; then Callister/Dieter.
- Kinematics/motion -> Norton Design of Machinery; then Uicker/Pennock.
- Cam design -> Norton Design of Machinery ch.8/15 + Norton Cam Handbook.
- Bearing/lubrication -> Hamrock; then Shigley.
- Manufacturing process choice -> Kalpakjian; then Groover.
- DFM/assembly cost -> Boothroyd-Dewhurst.
- Drawing/GD&T -> Giesecke/Madsen + ASME Y14.5 or ISO GPS.
- Fit/tolerance selection -> ISO 286 (metric) or ANSI B4.1 (inch) + Machinery's Handbook.
- Standards lookup -> Section 3.6 + governing code.

Step 2: Quick lookup cues (question -> reference).

- "Gear bending stress" -> Shigley Ch. 14 (spur and helical gears) / AGMA 2001.
- "Gear pitting/contact stress" -> Shigley Ch. 14 / AGMA 2001 / Hamrock (Hertzian contact).
- "Minimum teeth to avoid undercutting" -> Shigley Ch. 13-14 or Uicker ch. 6.
- "Shaft diameter under combined bending and torsion" -> Shigley Ch. 7 / ASME shaft standard.
- "Bearing life L10" -> Shigley Ch. 11 / Hamrock Ch. 13 / catalog.
- "Journal bearing minimum film thickness" -> Hamrock Ch. 12 / Shigley Ch. 12.
- "Spring rate and Wahl stress factor" -> Shigley Ch. 10 / Mott Ch. 14.
- "Clutch/brake torque capacity" -> Shigley Ch. 16 / Mott Ch. 22.
- "Belt tension and service factor" -> Shigley Ch. 17 / Mott Ch. 7.
- "Weld throat stress / weld size" -> Shigley Ch. 9 / AWS D1.1 (structural) / ASME IX (pressure).
- "Key/pin/snap ring selection" -> Spotts Ch. 12 / Machinery's Handbook.
- "Fatigue endurance limit with Marin factors" -> Shigley Ch. 6.
- "Fatigue life of a notched part" -> Bannantine et al. / Dowling.
- "Crack size for damage tolerance" -> Anderson (K, J, CTOD, Paris).
- "Which material for lightest/stiffest/cheapest" -> Ashby (performance indices).
- "Phase diagram / heat treatment" -> Callister / Dieter.
- "Plastic deformation / strengthening" -> Dieter.
- "Four-bar mobility/Grashof" -> Norton Design of Machinery ch. 2 / Uicker ch. 1.
- "Linkage synthesis for 2-3 positions" -> Norton ch. 3/5 or Erdman vol. 1.
- "Linkage synthesis for 4-5 positions / Burmester" -> Erdman vol. 2 ch. 3 or McCarthy and Soh.
- "Cam profile design" -> Norton Design of Machinery ch. 8 + Cam Handbook.
- "Gear train ratio" -> Norton Design of Machinery ch. 9 / Uicker ch. 10 / Mabie ch. 7.
- "Critical speed / vibration" -> Uicker ch. 17 / Rao ch. 18-19.
- "Balancing a rotor or linkage" -> Erdman vol. 2 ch. 5 / Uicker ch. 19 / Mabie ch. 10.
- "FEA element choice / mesh / BCs" -> Cook / Moaveni.
- "FEA stiffness matrix derivation" -> Logan / Reddy.
- "NC/G-code logic" -> Groover / Zeid.
- "Parametric feature tree for Creo/SolidWorks/Inventor" -> Shih/SDC texts + vendor docs.
- "Fusion 360 toolpath / simulation" -> Autodesk Fusion 360 Help.
- "Manufacturing process selection" -> Kalpakjian.
- "Assembly time and cost estimate" -> Boothroyd-Dewhurst.
- "Engineering drawing views/sections" -> Giesecke / Madsen.
- "GD&T callout interpretation" -> ASME Y14.5 (US) or ISO GPS (international).
- "Metric fit H7/g6" -> ISO 286.
- "Inch fit RC/LC/FN" -> ANSI B4.1.
- "Steel grade interpretation (AISI/SAE)" -> Material standards (AISI/SAE + ASTM/ASME).
- "Pressure vessel wall thickness" -> ASME Section VIII (not a textbook).
- "Piping pressure drop" -> Crane TP-410.
- "Welding procedure qualification" -> ASME Section IX / AWS D1.1 (structural).

---

## 6. Gaps and cautions

- Edition currency unverified for several texts: Spotts (last confirmed 8th ed. 2004, no 9th ed. found); Mott (last confirmed 6th ed. 2018, check for 7th); Khurmi (edition, year, page count, TOC not verified from a primary source); Mabie (last cited 4th ed. 1991); Hamrock (last cited 3rd ed. 2013/2014, check for 4th).
- Shigley edition numbering differs by region (US "2024 release" vs. UK "12th ed. SI 2025"). Treat as 12th edition family and state the edition in citations.
- Chang (CAD/CAM/CAE) exact edition/author/ISBN not verified in the research; confirm before citing pages.
- Khurmi scope/topic ownership not verified; do not attribute specific chapters without confirmation.
- Google Scholar citation counts were not collected for most books; only Hamrock's CRC record (298 citations) and an ASME review (10 citations) are sourced. Do not quote citation counts as verified.
- No side-by-side equation-level comparison across books was performed. If a specific equation is needed, fetch the relevant chapter/standard.
- Standards are copyrighted and paywalled; only scope/abstract/TOC-level information is available in the research notes. Exact clause values require licensed access. Never fabricate standard values.
- Standards revise frequently (ASME Y14.5 2018/2019, B1.1 2024, B31.3 2024, Section VIII 2025, AWS D1.1 2025, ISO 2768 new ed. 2026). Verify current edition before use.
- Regional texts (Bhandari, Khurmi, Ghosh/Mallik, Rao/Dukkipati) assume IS/Indian syllabi; Shigley/Norton/Hamrock assume ANSI/AGMA/ISO. Tag jurisdiction in every recommendation.
- Older texts (Dieter 1988, Bannantine 1990, Suresh 1998, Mabie 1991, Spotts 2004) remain canonical for concepts but may be dated on data, materials, and standards. Cross-check against current sources.
- Property tables, cost rates, and software UIs are edition/version-dependent. Cross-check against supplier data, solver docs, and standard revisions.
- The roadmap durations are cross-industry averages; aerospace/medical-device careers often run longer in each stage than consumer products.
- Web search was unavailable in the research environment; bibliographic facts rely on fetched pages plus established domain knowledge. Verify ISBNs/editions independently before publication.

---

## 7. References to research notes

All source notes are under `C:\Users\malliath\Desktop\CADResearch\research_notes\Machine design textbooks and CAD guide\`:

1. `core_machine_design_books.md` - Core machine design textbooks (Shigley, Norton, Mott, Juvinall, Bhandari, Spotts, Hamrock, Khurmi, other texts; topic ownership matrix).
2. `cad_cam_cae_books.md` - CAD/CAM/CAE, engineering drawing/GD&T, FEA, manufacturing, materials textbooks and standards.
3. `kinematics_dynamics_books.md` - Kinematics and dynamics of machinery textbooks (Norton, Uicker/Pennock, Mabie, Rao, Ghosh, Erdman/Sandor, McCarthy/Soh, cams/gears).
4. `materials_failure_books.md` - Materials science, failure analysis, fatigue and fracture textbooks.
5. `standards_handbooks.md` - Engineering standards, handbooks, and reference manuals (ASME, ISO, fasteners, gears, welding, piping, tolerances, materials).
6. `zero_to_professional.md` - Zero-to-professional mechanical design engineer roadmap (stages, competencies, certifications, software, desk references, projects).

When a fact in this guide conflicts with a primary source, prefer the primary source and update this guide.
