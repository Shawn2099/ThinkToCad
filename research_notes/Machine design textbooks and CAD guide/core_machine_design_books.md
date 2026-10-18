# Core Machine Design Textbooks: Pointer Guide for an AI Design Assistant

Scope: Authoritative, widely-used machine design / machine elements textbooks at B.Tech/M.Tech (junior–senior undergrad to graduate) level, with topic ownership, equation families, level, strengths/weaknesses, and "consult when..." guidance for an AI design assistant. Companion to CAD/FEA references; not a substitute for standards (AGMA, ISO, ASME, etc.).

---

## Shigley's Mechanical Engineering Design (Budynas & Nisbett)

### Takeaway
The de facto global standard undergraduate machine design text; broadest single-volume coverage of failure theories, fatigue, and all major mechanical elements, with deep ANSI/ISO standards integration; best default reference for an AI when a specific book is not indicated.

### Cited Findings
- Full title: *Shigley's Mechanical Engineering Design*; authors J. Keith Nisbett and Richard G. Budynas (legacy author Joseph E. Shigley); McGraw Hill. — [McGraw Hill (UK)](https://www.mheducation.co.uk/shigley-s-mechanical-engineering-design-12th-edition-si-units-9781526850171-emea); [McGraw Hill (US)](https://www.mheducation.com/highered/product/shigleys-mechanical-engineering-design-nisbett.html)
- Current edition: 12th ed. (2024 release / 2025 SI edition), 1120 pages. — [VitalSource](https://www.vitalsource.com/en-uk/products/shigley-39-s-mechanical-engineering-design-ise-nisbett-v9781264675845); [Google Books](https://books.google.com/books/about/Shigley_s_Mechanical_Engineering_Design.html?id=ikUR0AEACAAJ)
- Publisher describes it as "the standard in machine design for nearly 50 years." — [McGraw Hill](https://www.mheducation.com/highered/product/shigleys-mechanical-engineering-design-nisbett.html)
- Table of contents (12th ed.): Part 1 Basics (1 Introduction, 2 Materials, 3 Load & Stress Analysis, 4 Deflection & Stiffness); Part 2 Failure Prevention (5 Static Loading, 6 Fatigue/Variable Loading); Part 3 Design of Mechanical Elements (7 Shafts & Shaft Components, 8 Screws/Fasteners/Nonpermanent Joints, 9 Welding/Bonding/Permanent Joints, 10 Mechanical Springs, 11 Rolling-Contact Bearings, 12 Lubrication & Journal Bearings, 13 Gears-General, 14 Spur & Helical Gears, 15 Bevel & Worm Gears, 16 Clutches/Brakes/Couplings/Flywheels, 17 Flexible Mechanical Elements, 18 Power Transmission Case Study); Part 4 Special Topics (19 FEA, 20 GD&T). — [McGraw Hill UK TOC](https://www.mheducation.co.uk/shigley-s-mechanical-engineering-design-12th-edition-si-units-9781526850171-emea)
- 10th ed. note: statistical material (Ch. 20 statistical considerations, Sec. 6-17) was trimmed and integrated where used; Weibull retained in bearings chapter. — [McGraw Hill Info Center (10/e)](https://glencoe.mheducation.com/sites/0073398209/information_center_view0/)
- 8th ed. (2008): 1059 pp.; earlier editions carried "Statistical Considerations" as a full chapter (Ch. 18). — [WorldCat](https://search.worldcat.org/title/70836665)
- Level: intended for "students beginning the study of mechanical engineering design" (junior-level undergrad), but used as a reference by practicing engineers. — [McGraw Hill](https://www.mheducation.com/highered/product/shigleys-mechanical-engineering-design-nisbett.html)

### Inferences
- Shigley "owns" the canonical equation sets an AI should default to: distortion-energy (von Mises) and maximum-shear (Tresca) static failure theories; Soderberg/Goodman/Gerber fatigue criteria; Marin factors (ka, kb, kc, kd, ke, kf); Lewis gear bending; AGMA pitting/bending factors; Hertzian contact stress for bearings/gears; Wahl spring stress factor; Johnson/Euler columns. These are the equations most other texts reuse.
- The 2024 release's retention of GD&T and FEA chapters makes it the best single text for linking machine design to manufacturing tolerances and numerical analysis.
- Its breadth means per-topic depth is moderate; for deep tribology/bearing theory or manufacturing-process detail, pair with Hamrock or Mott.

### Gaps
- No reliable Google Scholar citation count located for the book itself (publisher/author pages did not expose it); WorldCat shows 13 reviews for the 8th ed. only. — [WorldCat](https://search.worldcat.org/title/70836665)
- Exact edition-to-year mapping for 11th/12th releases varies by region (US "2024 release" vs. UK "12th ed. SI 2025"); treat as 12th edition family.

---

## Norton: Machine Design: An Integrated Approach

### Takeaway
Best text for an AI when the question involves fatigue-dominated, high-cycle machine assemblies and case-study-style integration of multiple elements; strongest on fracture mechanics intro, FEA application, and CAE/computer-aided solution files.

### Cited Findings
- Full title: *Machine Design: An Integrated Approach*, 6th ed.; author Robert L. Norton (Worcester Polytechnic Institute, Milton P. Higgins II Distinguished Professor Emeritus). — [Pearson](https://www.pearson.com/en-us/subject-catalog/p/machine-design-an-integrated-approach/P200000003435/9780137516872); [Amazon](https://www.amazon.com/Machine-Design-Integrated-Approach-6th/dp/0135184231)
- 6th ed. published 2021 (©2022), 1120 pp., ISBN 978-0-13-751687-2; 5th ed. 2014, 1060 pp.; 4th ed. 2011, 1028 pp. — [Pearson](https://www.pearson.com/en-us/subject-catalog/p/machine-design-an-integrated-approach/P200000003435/9780137516872); [Goodreads editions](https://www.goodreads.com/work/editions/238465-machine-design-an-integrated-approach)
- Aimed at junior-to-senior mechanical engineering students; emphasizes failure theory/analysis plus synthesis/design of machine elements. — [Pearson](https://www.pearson.com/en-us/subject-catalog/p/machine-design-an-integrated-approach/P200000003435/9780137516872)
- Author draws on 50+ years of industry/consulting design experience and 40 years teaching. — [Pearson](https://www.pearson.com/en-us/subject-catalog/p/machine-design-an-integrated-approach/P200000003435/9780137516872)
- Contents (4th ed. representative): Part I Fundamentals (Introduction to design; Materials and processes; Load determination; Stress/strain/deflection; Static failure theories; Fatigue failure theories; Surface failure; FEA); Part II Machine Design (Design case studies; Shafts/keys/couplings; Bearings & lubrication; Spur gears; Helical/bevel/worm gears; Spring design; Screws & fasteners; Weldments; Clutches & brakes); Appendices (material properties, beam tables, stress-concentration factors, answers). — [WorldCat (4th ed.)](https://search.worldcat.org/title/Machine-design-:-an-integrated-approach/oclc/473443730)
- Includes 75 examples + 25 case study solutions; CD-ROM with ~1000 case studies/sample solutions compatible with Excel/MATLAB/Mathcad/TKSolver; author-written kinematic/dynamic/stress programs. — [designofmachinery.com (Norton MD page)](https://designofmachinery.com/books/machine-design/)
- Amazon rating: 4.1/5 (37 reviews); Goodreads ~4.0–4.12 across editions. — [Amazon](https://www.amazon.com/Machine-Design-Integrated-Approach-6th/dp/0135184231); [Goodreads](https://www.goodreads.com/work/editions/238465-machine-design-an-integrated-approach)

### Inferences
- Norton's "integrated approach" ties elements together through recurring case studies of the same assembly across chapters — useful for an AI reasoning about interfaces (shaft–bearing–gear–housing) rather than isolated parts.
- Best consulted for: fatigue failure theories (surface failure/pitting included as a distinct topic), fracture mechanics intro, FEA chapter, case-study-driven design of assemblies, computer-aided solution workflows.
- Weaker default for Indian/UK syllabi that expect Indian Standards (IS) and SI-only worked examples; Bhandari/Khurmi may be preferred there.

### Gaps
- No Google Scholar citation count located; book reviews in ASME J. Mech. Des. not found in this pass.
- Edition numbering in India (Pearson India 5th ed. 2022) sometimes lags US releases; verify edition/year when citing.

---

## Norton: Design of Machinery (kinematics focus)

### Takeaway
The standard kinematics/synthesis text; consult it (not the machine-design books) for linkage synthesis, cam design, gear trains kinematics, velocity/acceleration analysis, and mechanism design — complementary to, not a replacement for, machine design texts.

### Cited Findings
- Full title: *Design of Machinery: An Introduction to the Synthesis and Analysis of Mechanisms and Machines*, 6th ed.; author Robert L. Norton (WPI); McGraw Hill; 2019; ISBN 978-0-07-352935-6. — [designofmachinery.com](https://designofmachinery.com/books/design-of-machinery/)
- Used in hundreds of schools in the US/Canada and worldwide; translated into Greek, Korean, Spanish, Turkish, and Chinese. — [designofmachinery.com](https://designofmachinery.com/books/design-of-machinery/)
- Emphasis on synthesis and design; covers linkage analysis, cam design, gear trains; includes downloadable Working Model animations of 100+ examples, custom design programs, MATLAB models; 6th ed. adds 82 Master Lecture Videos. — [designofmachinery.com](https://designofmachinery.com/books/design-of-machinery/)
- Student/professor resources and errata maintained on author's site. — [designofmachinery.com](https://designofmachinery.com/books/design-of-machinery/)

### Inferences
- An AI should route kinematics questions (Grashof, four-bar synthesis, cam profiles, instantaneous centers, gear ratios/trains) to this text; route stress/fatigue/component-sizing questions to machine design texts.
- Norton's two books together (Machine Design + Design of Machinery) cover both "what the part is" and "how the mechanism moves."

### Gaps
- No detailed TOC captured in this pass (PDF sample available on author site); precise chapter list not verified here.

---

## Mott: Machine Elements in Mechanical Design

### Takeaway
The most readable, application-first text for undergraduates; uniquely organized around designing a complete power-transmission system (Part II), with strong belt/chain/gear/bearing/shaft integration and a dedicated tolerances-and-fits chapter.

### Cited Findings
- Full title: *Machine Elements in Mechanical Design*, 6th ed.; authors Robert L. Mott, Edward M. Vavrek, Jyhwen Wang; Pearson, ©2018 (print ISBN 978-0-13-444118-4). — [Pearson](https://www.pearson.com/en-us/subject-catalog/p/machine-elements-in-mechanical-design/P200000001541/9780137561452); [VitalSource](https://www.vitalsource.com/products/machine-elements-in-mechanical-design-robert-l-mott-edward-m-v9780134451947)
- Three-part structure: Part I Principles of Design & Stress Analysis (Ch. 1–6: nature of design, materials, stress/deformation, combined stresses, design for different loading, columns); Part II Design of a Mechanical Drive (Ch. 7–15: belts/chains/wire rope, shafts, rolling bearings, lubrication, spur gears, helical/bevel/worm gears, springs, screws/fasteners, welded joints, completion of power transmission); Part III Design Details & Other Machine Elements (plain bearings, linear motion, tolerances & fits, clutches/brakes, electric motors, design projects). — [Pearson TOC (from PDF)](https://ftp.idu.ac.id/wp-content/uploads/ebook/tdg/DESIGN%20SISTEM%20DAYA%20GERAK/Machine%20Elements%20in%20Mechanical%20Design.pdf)
- Promotes spreadsheets/computer-aided calculation; uses SI and US customary roughly equally; includes Internet site lists per chapter. — [Pearson preface](https://ftp.idu.ac.id/wp-content/uploads/ebook/tdg/DESIGN%20SISTEM%20DAYA%20GERAK/Machine%20Elements%20in%20Mechanical%20Design.pdf)
- Notable chapters absent in some competitors: Ch. 13 Tolerances and Fits, Ch. 21 Electric Motors and Controls, Ch. 17 Linear Motion Elements (power/ball screws). — [TOC](https://ftp.idu.ac.id/wp-content/uploads/ebook/tdg/DESIGN%20SISTEM%20DAYA%20GERAK/Machine%20Elements%20in%20Mechanical%20Design.pdf)
- Adopted at Stony Brook (MEC410) with rolling-contact bearings, gears, shafting, springs, fasteners, belts, clutches. — [Stony Brook syllabus](http://me.stonybrook.edu/undergraduate/_docs/syllabus_spring2025/MEC410_Syllabus_Spring2025.pdf)
- "Highly rated by students and instructors for readability." — [Pearson](https://www.pearson.com/en-us/subject-catalog/p/machine-elements-in-mechanical-design/P200000001541/9780137561452)

### Inferences
- Mott is the best single text for an AI answering "design a complete gearbox/power transmission from motor to load" because Part II forces interface consistency (shaft diameters, bearing selection, gear ratios, belt ratios in one flow).
- Good default for mechanical engineering technology programs and first courses; less emphasis on graduate-level failure theory than Shigley/Norton.
- Topic ownership: tolerances & fits, electric motor selection, linear motion elements (power/ball screws) — areas Shigley covers only briefly (GD&T) or not at all.

### Gaps
- No Google Scholar citation count located.
- 6th ed. (2018) may be the latest; check for 7th ed. before citing.

---

## Juvinall & Marshek: Fundamentals of Machine Component Design

### Takeaway
Strongest on fundamentals-to-component pipeline and fracture mechanics; best consulted for failure theories, fatigue, crack growth/stress intensity, wear theory, and the graphical problem-solving methodology (free-body/force-flow diagrams).

### Cited Findings
- Full title: *Fundamentals of Machine Component Design*, 7th ed.; authors Robert C. Juvinall, Kurt M. Marshek; Wiley, 2020 (ISBN 978-1-119-72360-8, 800 pp.) / 2019 print (742 pp., ISBN 978-1-119-47568-2). — [Wiley](https://www.wiley.com/en-us/Fundamentals+of+Machine+Component+Design%2C+7th+Edition-p-9781119723608); [Google Books](https://books.google.com/books/about/Fundamentals_of_Machine_Component_Design.html?id=nB7zDwAAQBAJ)
- Scope: free body diagrams, force flow concepts, failure theories, fatigue design; applications to bearings, springs, brakes, clutches, fasteners; fracture mechanics (fatigue crack growth, stress intensity factors); material selection including composites; wear theory and wear models. — [Wiley](https://www.wiley.com/en-us/Fundamentals+of+Machine+Component+Design%2C+7th+Edition-p-9781119723608)
- Problem-solving methodology uses a graphical procedural framework; appendices on processing methods, joinability, failure modes, material properties. — [Wiley](https://www.wiley.com/en-us/Fundamentals+of+Machine+Component+Design%2C+7th+Edition-p-9781119723608)
- ASME J. Manuf. Sci. Eng. reviewed earlier edition (1991). — [ASME Digital Collection](https://asmedigitalcollection.asme.org/manufacturingscience/article/113/2/246/454920/Fundamentals-of-Machine-Component-Design)

### Inferences
- Juvinall owns "how to think about failure" — stress-intensity-factor charts, crack-growth under alternating loads, wear models — making it the best text for an AI handling fracture/fatigue-crack and wear questions, which Shigley/Mott treat more briefly.
- Strong on conceptual visualization (force-flow diagrams), helpful for AI generating explanatory reasoning rather than just numbers.
- Less of a "design manual with catalog data" than Mott; fewer commercial component-selection tables.

### Gaps
- No Google Scholar citation count located.
- Older editions (3rd/5th) still cited in some syllabi (e.g., IIT Guwahati references 3rd ed.) — verify edition when citing. — [IITG syllabus](https://iitg.ac.in/mech/academics/undergraduate/latest/sem-5/design-of-machine-elements/)

---

## Bhandari: Design of Machine Elements

### Takeaway
The dominant Indian-university text; consult for IS-standard-based design, GATE/competitive-exam problem styles, and Indian manufacturing context; strong practical, step-by-step solved examples.

### Cited Findings
- Full title: *Design of Machine Elements*, 5th ed.; author V. B. Bhandari; McGraw Hill India, ©2021 (ISBN 978-93-90177-47-9); 4th ed. 2017 (934 pp., ISBN 978-93-392-2112-6). — [McGraw Hill India](https://www.mheducation.co.in/design-of-machine-elements-9789390177479-india); [Amazon.com](https://www.amazon.com/Design-Machine-Elements-V-Bhandari/dp/9390177472)
- Rated 4.5/5 from 878 Amazon reviews. — [Amazon.com](https://www.amazon.com/Design-Machine-Elements-V-Bhandari/dp/9390177472)
- TOC (5th ed.): Ch. 1 Introduction; 2 Engineering Materials; 3 Manufacturing Considerations in Design; 4 Theories of Failure for Static Loading; 5 Theories of Failure for Dynamic Loading; 6 Power Screws; 7 Threaded Joints; 8 Welded & Riveted Joints; 9 Shafts, Keys and Couplings; 10 Springs; 11 Clutches; 12 Brakes; 13 Belt and Rope Drives; 14 Chain Drives; 15 Rolling Contact Bearings; 16 Sliding Contact Bearings; 17 Spur Gears; 18 Helical Gears; 19 Bevel Gears; 20 Worm Gears; 21 Flywheel; 22 Cylinders and Pressure Vessels; 23 Design of IC Engines; Index. — [McGraw Hill India](https://www.mheducation.co.in/design-of-machine-elements-9789390177479-india)
- Features: latest AICTE model curriculum; Indian Standards throughout; GATE/competitive-exam question sets; outcome-based learning; 717+ short-answer questions, 356 solved examples, 216 practice problems (4th ed. counts). — [McGraw Hill India](https://www.mheducation.co.in/design-of-machine-elements-9789390177479-india); [IIT Delhi library (4th ed.)](https://libcat.iitd.ac.in/bib/244547)
- Covers prescribed machine design syllabus for various Indian universities; uses Indian products in component selection. — [IIT Delhi library](https://libcat.iitd.ac.in/bib/244547)
- IIT Guwahati lists Bhandari 4th ed. as a reference alongside Shigley 10th ed. — [IITG syllabus](https://iitg.ac.in/mech/academics/undergraduate/latest/sem-5/design-of-machine-elements/)

### Inferences
- Bhandari is the right consult for Indian Standards (IS) thread/bearing/gear specs, AICTE-aligned course problems, and Indian manufacturing catalogs; Shigley/Norton default to ANSI/AGMA/ISO.
- Topic ownership: IC engine components (Ch. 23) and cylinders/pressure vessels (Ch. 22) are covered more prominently than in Shigley's main flow; flywheel design (Ch. 21) is a dedicated chapter.
- Amazon rating 4.5 with 878 reviews suggests strong practitioner/student approval in the Indian market.

### Gaps
- No Google Scholar citation count located.
- 5th ed. page count not confirmed in this pass (4th ed. = 934 pp.).

---

## Spotts, Shoup, Hornberger: Design of Machine Elements

### Takeaway
A classic, phenomenological, spreadsheet-heavy undergraduate text; best for an AI needing full derivations, structured example format (problem/given/assumptions/method/solution), and a dedicated plastics-design chapter.

### Cited Findings
- Full title: *Design of Machine Elements*, 8th ed.; authors M. F. Spotts, T. E. Shoup, L. E. Hornberger; Pearson Prentice Hall, 2004 (ISBN 0-13-048989-1), 808 pp. (SI edition). — [Pearson](https://www.pearson.com/en-us/subject-catalog/p/design-of-machine-elements/P200000006702/9780130489890); [ASME J. Mech. Des. review](https://asmedigitalcollection.asme.org/mechanicaldesign/article/126/1/201/445744/Design-of-Machine-Elements-Eighth-Edition)
- ASME review: "rich with content and examples"; recommends for undergrads, grad students, and practicing engineers as a reference; 10 citations recorded for the review. — [ASME J. Mech. Des.](https://asmedigitalcollection.asme.org/mechanicaldesign/article/126/1/201/445744/Design-of-Machine-Elements-Eighth-Edition)
- TOC (8th ed.): 1 Fundamental Principles; 2 Working Stresses and Failure Theories; 3 Design of Shafts; 4 Springs; 5 Screws; 6 Belts, Clutches, Brakes, and Chains; 7 Welded and Riveted Connections; 8 Lubrication; 9 Ball and Roller Bearings; 10 Spur Gears; 11 Helical, Bevel and Worm Gears; 12 Miscellaneous Machine Elements; 13 Principles of Form Synthesis; 14 Engineering Materials; 15 Designing with Plastic Materials; Appendix A Spreadsheet Modules. — [Pearson TOC](https://www.pearson.com/en-us/subject-catalog/p/design-of-machine-elements/P200000006702/9780130489890)
- 8th ed. improvements over 7th: structured example format (problem statement, given, assumptions, solution method, solution details); 54 improved spreadsheets with unit-system drop-downs; new chapter on design with plastic materials (Hornberger). — [ASME J. Mech. Des.](https://asmedigitalcollection.asme.org/mechanicaldesign/article/126/1/201/445744/Design-of-Machine-Elements-Eighth-Edition)
- Authors' combined 80+ years of industry/classroom experience. — [ASME J. Mech. Des.](https://asmedigitalcollection.asme.org/mechanicaldesign/article/126/1/201/445744/Design-of-Machine-Elements-Eighth-Edition)

### Inferences
- Spotts owns "miscellaneous machine elements" (Ch. 12) and "principles of form synthesis" (Ch. 13) — topics (snap rings, keys, pins, retaining rings, form synthesis) that other texts bury in appendices.
- The structured example format is a good template for an AI to mirror when producing step-by-step design solutions.
- Last widely cited edition is 8th (2004); may be dated on materials/manufacturing and FEA; prefer Shigley/Norton for modern content.

### Gaps
- No evidence of a 9th edition in this pass; confirm currency before relying on it for standards references.
- No Google Scholar citation count located.

---

## Hamrock, Jacobson, Schmid: Fundamentals of Machine Elements

### Takeaway
The most theory-and-tribology-deep text; consult for hydrodynamic/hydrostatic bearings, lubrication, friction/wear, Hertzian contact, fatigue staircase method, advanced welding, and modern case studies; graduate-friendly.

### Cited Findings
- Full title: *Fundamentals of Machine Elements*, 3rd ed.; authors Steven R. Schmid, Bernard J. Hamrock, Bo. O. Jacobson; CRC Press/Taylor & Francis, 2013 (ISBN 978-1-4398-9132-2, 626 pp.); SI version 2014 (ISBN 978-1-4822-4750-3). — [Routledge/CRC](https://www.routledge.com/Fundamentals-of-Machine-Elements/Schmid-Hamrock-Jacobson/p/book/9781439891322); [Taylor & Francis](https://www.taylorfrancis.com/books/mono/10.1201/b14229/fundamentals-machine-elements-bo-jacobson-bernard-hamrock-steven-schmid)
- DOI citation record: 298 citations for the book. — [doi.org/10.1201/b17120](https://doi.org/10.1201/b17120)
- Authors: Hamrock (Ohio State, ex-NASA Lewis tribology; h-index 33, 8,191 citations); Jacobson (Lund/Chalmers/Luleå; h-index 20, 3,840 citations); Schmid (Notre Dame; h-index 21, 3,413 citations). — [doi.org/10.1201/b17120](https://doi.org/10.1201/b17120)
- TOC: Part I Fundamentals (Ch. 1 Introduction, 2 Load/Stress/Strain, 3 Materials & Manufacturing, 4 Stresses & Strains, 5 Deformation, 6 Failure Prediction Static, 7 Fatigue & Impact, 8 Lubrication/Friction/Wear); Part II Machine Elements (Ch. 9 Columns, 10 Cylinders, 11 Shafting & Associated Parts, 12 Hydrodynamic & Hydrostatic Bearings & Seals, 13 Rolling-Element Bearings, 14 Spur Gears, 15 Helical/Bevel/Worm Gears, 16 Fasteners & Power Screws, 17 Springs, 18 Brakes & Clutches, 19 Flexible Machine Elements). — [StandardsMedia TOC](https://www.standardsmedia.com/Fundamentals-of-Machine-Elements-3rd-Edition-7899-book.html); [CERN record](http://cds.cern.ch/record/2295426)
- 3rd ed. new features: heat-affected zone in welding; design synthesis of spur/bevel/worm gears; unified selection of multiple rolling-element bearing types; advanced welding (brazing, friction, spot); staircase method for endurance limit; design of couplings, snap rings, wave & gas springs, hydrostatic bearings; case studies (windmill bearings, powder-metal gears, welds in blisks, roller-coaster brakes). — [Routledge](https://www.routledge.com/Fundamentals-of-Machine-Elements/Schmid-Hamrock-Jacobson/p/book/9781439891322)
- Intended as 3rd/4th-year course or reference for practicing engineers; requires calculus; links design to manufacturing. — [Routledge](https://www.routledge.com/Fundamentals-of-Machine-Elements/Schmid-Hamrock-Jacobson/p/book/9781439891322)

### Inferences
- Hamrock is the tribology authority among these texts — its bearing/lubrication chapters (hydrodynamic/hydrostatic, rolling-element selection) are deeper than Shigley/Mott; consult it for bearing life, lubricant selection, wear.
- The staircase method for endurance limit and fracture-mechanics fatigue approach are distinctive; useful when an AI must handle statistical fatigue or crack-growth.
- Best paired with Shigley for a complete answer: Shigley for component-sizing equations/standards, Hamrock for contact/bearing/lubrication theory.

### Gaps
- No newer than 3rd ed. (2013/2014) located; check for 4th ed.
- Citation count (298) is for the CRC record, not necessarily a Google Scholar count; treat as indicative.

---

## Khurmi & Gupta: A Textbook of Machine Design

### Takeaway
A long-standing, exam-oriented Indian text; consult for Indian university syllabi, IS-standard practice, and traditional step-by-step machine design problems; verify edition and cross-check equations against Shigley/Bhandari.

### Cited Findings
- Full title: *A Textbook of Machine Design*; authors R. S. Khurmi and J. K. Gupta; S. Chand (publisher of Indian engineering texts). — [Amazon.com](https://www.amazon.com/TEXTBOOK-MACHINE-DESIGN-R-S-Khurmi/dp/8121925371)
- Amazon listing confirms authors R.S. Khurmi and J.K. Gupta; ISBN 9788121925372 (print) / 978812192524X variant. — [Amazon.com](https://www.amazon.com/TEXTBOOK-MACHINE-DESIGN-R-S-Khurmi/dp/8121925371)
- Frequently paired with Bhandari in Indian curricula as a reference; IIT Guwahati syllabus references Indian texts alongside Shigley. — [IITG syllabus](https://iitg.ac.in/mech/academics/undergraduate/latest/sem-5/design-of-machine-elements/)

### Inferences
- Khurmi & Gupta is widely used in Indian B.Tech programs and competitive exams; its problem sets and design data (IS-based) are valuable for Indian-context answers.
- As an older-generation text, its equation presentations and standards references may lag current ISO/AGMA; an AI should cross-check against Shigley/Bhandari for modern standards.

### Gaps
- Edition number, publication year, page count, and TOC were not verified from a primary source in this pass (Amazon page was JS-rendered); treat edition as "latest S. Chand edition" and confirm before citing.
- No Google Scholar citation count located.
- Scope/topic ownership not verified beyond general machine design coverage; do not attribute specific chapters to it without confirmation.

---

## Other widely-cited texts

### Takeaway
A small set of secondary texts worth routing to for specific needs: Maleev & Hartman for traditional/legacy problems, Burr & Cheatham for mechanical analysis, PSG Design Data Book for Indian design data, and Shigley/Norton for the mainstream.

### Cited Findings
- IIT Guwahati Design of Machine Elements syllabus references: Budynas & Nisbett *Shigley's* 10th ed. (text); references include Bhandari 4th ed., Spotts/Shoup/Hornberger 8th ed., Juvinall & Marshek 3rd ed., Burr & Cheatham *Mechanical Analysis and Design* 2nd ed., Maleev & Hartman *Machine Design* 5th ed., and PSG College of Technology *Design Data Book of Engineers*. — [IITG syllabus](https://iitg.ac.in/mech/academics/undergraduate/latest/sem-5/design-of-machine-elements/)
- Norton's site also lists *Cam Design and Manufacturing Handbook* and *Cam Design – A Primer* as companion texts. — [designofmachinery.com](https://designofmachinery.com/books/design-of-machinery/)

### Inferences
- PSG Design Data Book is a data (not theory) reference — consult for Indian-standard dimension tables, material properties, and fit/limit data rather than derivations.
- Maleev & Hartman and Burr & Cheatham are legacy/traditional texts; consult only when a syllabus or problem set explicitly references them.

### Gaps
- Detailed scope/TOC for Maleev & Hartman, Burr & Cheatham, and PSG Data Book not captured in this pass; treat as "mentioned in syllabi, not verified here."

---

## Topic ownership & consult-when matrix (AI usage guide)

### Takeaway
Route by topic: default to Shigley for most component-sizing; Norton for fatigue/assembly/case studies and kinematics (via Design of Machinery); Mott for full power-transmission integration and tolerances; Juvinall for fracture/wear fundamentals; Hamrock for bearings/lubrication/tribology; Bhandari/Khurmi for IS-standard/Indian-context problems; Spotts for miscellaneous elements and worked-example templates.

### Cited Findings
- Topic coverage cross-check (from TOCs above):
  - Fasteners/screws: Shigley Ch. 8 (screws/fasteners/nonpermanent joints) + Ch. 9 (welding/permanent); Norton MD (screws & fasteners, weldments); Mott Ch. 17 (linear motion/power screws) + Ch. 19 (fasteners) + Ch. 20 (bolted/welded); Juvinall (fasteners chapter); Bhandari Ch. 6 (power screws), 7 (threaded), 8 (welded/riveted); Spotts Ch. 5 (screws), 7 (welded/riveted); Hamrock Ch. 16 (fasteners & power screws).
  - Gears: Shigley Ch. 13–15 (general, spur/helical, bevel/worm); Norton MD (spur, helical/bevel/worm); Mott Ch. 9–10; Bhandari Ch. 17–20; Spotts Ch. 10–11; Hamrock Ch. 14–15.
  - Bearings: Shigley Ch. 11 (rolling), 12 (journal/lubrication); Norton MD (bearings & lubrication); Mott Ch. 9 (rolling), 16 (plain); Bhandari Ch. 15 (rolling), 16 (sliding); Spotts Ch. 8 (lubrication), 9 (ball/roller); Hamrock Ch. 12 (hydrodynamic/hydrostatic), 13 (rolling-element) — deepest.
  - Shafts: Shigley Ch. 7; Norton MD (shafts/keys/couplings); Mott Ch. 8 (shafts); Bhandari Ch. 9; Spotts Ch. 3; Hamrock Ch. 11.
  - Springs: Shigley Ch. 10; Norton MD (spring design); Mott Ch. 14; Bhandari Ch. 10; Spotts Ch. 4; Hamrock Ch. 17.
  - Welds: Shigley Ch. 9; Norton MD (weldments); Mott Ch. 15 (welded joints); Bhandari Ch. 8; Spotts Ch. 7.
  - Clutches/brakes: Shigley Ch. 16; Norton MD (clutches & brakes); Mott Ch. 22; Bhandari Ch. 11–12; Spotts Ch. 6; Hamrock Ch. 18.
  - Couplings: Shigley Ch. 16 (couplings); Mott Ch. 8/15; Hamrock (couplings in 3rd ed. new).
  - Belts/chains: Shigley Ch. 17 (flexible mechanical elements); Norton MD (via integrated cases); Mott Ch. 7; Bhandari Ch. 13–14; Spotts Ch. 6; Hamrock Ch. 19.
  - Fatigue/failure theories: Shigley Ch. 5–6 (static + variable) + Marin factors; Norton MD (fatigue failure theories, surface failure, fracture mechanics intro); Juvinall (failure theories + fracture mechanics + crack growth); Bhandari Ch. 4–5; Spotts Ch. 2; Hamrock Ch. 6–7 (incl. staircase method).
  - Tolerances/fits: Mott Ch. 13 (dedicated); Shigley Ch. 20 (GD&T); Spotts (manufacturing/materials); Bhandari Ch. 3 (manufacturing considerations).
  - Kinematics/synthesis: Norton *Design of Machinery* (linkages, cams, gear trains).

### Inferences
- "Consult when..." cheat-sheet for an AI:
  - General component sizing with standards → Shigley.
  - Fatigue-dominated/high-cycle assembly, FEA, fracture intro → Norton MD.
  - Linkage/cam/gear-train kinematics → Norton Design of Machinery.
  - Complete power-transmission design, tolerances, motor selection → Mott.
  - Fracture mechanics, crack growth, wear models, force-flow reasoning → Juvinall.
  - IS standards, Indian manufacturing, GATE-style problems → Bhandari (and Khurmi).
  - Miscellaneous elements (keys, pins, snap rings), form synthesis, structured examples, plastics → Spotts.
  - Bearings/lubrication/tribology, Hertzian contact, advanced welding, staircase fatigue → Hamrock.
- When books conflict on an equation, prefer the standard the user's context implies (AGMA/ISO for Shigley/Norton/Hamrock; IS for Bhandari/Khurmi) and state the assumption.

### Gaps
- No side-by-side equation-level comparison performed; if needed, fetch specific chapters.
- Citation counts (Google Scholar) not obtained for any book; only Hamrock's CRC record (298 citations) and ASME review citations (10) are sourced.

---

## Research gaps

### Takeaway
Edition currency and Khurmi specifics are the main unverified items; standards-level verification should be done against primary standards, not textbooks.

### Cited Findings
- Spotts 8th ed. (2004) may be the last edition; no 9th ed. found. — [Pearson](https://www.pearson.com/en-us/subject-catalog/p/design-of-machine-elements/P200000006702/9780130489890)
- Mott 6th ed. (2018) may be latest; check for 7th. — [Pearson](https://www.pearson.com/en-us/subject-catalog/p/machine-elements-in-mechanical-design/P200000001541/9780137561452)
- Khurmi edition/year/page count/TOC not verified from primary source. — [Amazon.com](https://www.amazon.com/TEXTBOOK-MACHINE-DESIGN-R-S-Khurmi/dp/8121925371)
- Shigley edition numbering differs by region (US "2024 release" vs. UK "12th ed. SI 2025"). — [McGraw Hill UK](https://www.mheducation.co.uk/shigley-s-mechanical-engineering-design-12th-edition-si-units-9781526850171-emea)

### Inferences
- For an AI assistant, textbook equations should be treated as pedagogical defaults; final designs must be checked against the governing standard (AGMA, ISO, ASME, IS) and manufacturer catalogs.

### Gaps
- Google Scholar citation counts for all books remain uncollected.
- Detailed TOCs for Khurmi & Gupta, Maleev & Hartman, Burr & Cheatham, PSG Design Data Book not captured.
- No verification of whether newer editions exist for Spotts (post-8th) or Mott (post-6th).
