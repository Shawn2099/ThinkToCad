# Materials Science, Failure Analysis, Fatigue and Fracture Textbooks for an AI Design Assistant

## Which books should an AI design assistant treat as canonical references, and what does each cover?

### Takeaway
The canonical stack is: Callister for materials fundamentals; Ashby for material selection; Dieter/Hertzberg/Dowling for mechanical behavior; Anderson/Suresh for fracture and fatigue depth; Bannantine et al. for practical metal-fatigue analysis; ASM Handbook Vols. 11 and 19 for failure-analysis case data; and Shigley for machine-design failure criteria and endurance limits. Each owns distinct topics, so the assistant should route queries by failure mode and material class rather than defaulting to one text.

### Cited Findings
- Callister, W. D. Jr. and Rethwisch, D. G., *Materials Science and Engineering: An Introduction*, 10th ed., Wiley, 2018, 992 pp., ISBN 978-1-119-40549-8 — broad introductory coverage of metals, ceramics, polymers, composites, structure-processing-property relationships, mechanical properties, phase diagrams, and corrosion/creep introductions. — [Wiley product page](https://www.wiley.com/en-us/Materials+Science+and+Engineering%3A+An+Introduction%2C+10th+Edition-p-9781119405498); [OpenLibrary record](https://openlibrary.org/works/OL29157024W)
- Ashby, M. F., *Materials Selection in Mechanical Design*, multiple editions (1st 1992; newer editions through 2024), Butterworth-Heinemann/Elsevier. — systematic materials-selection methodology, property charts (Ashby charts), performance indices, and case studies. — [OpenLibrary record](https://openlibrary.org/works/OL8323422W)
- Dieter, G. E. (with Bacon, D. in later editions), *Mechanical Metallurgy*, 3rd ed., McGraw-Hill, 1988 (1st ed. 1961). — mechanical behavior of metals: elasticity, plasticity, dislocations, strengthening mechanisms, fracture, fatigue, and creep. — [OpenLibrary record](https://openlibrary.org/works/OL4469776W); [Internet Archive record](https://archive.org/details/mechanicalmetal00diet)
- Dowling, N. E. (with Kampe, S. L. and Kral, M. V. in later editions), *Mechanical Behavior of Materials*, 4th ed., Pearson, 2012/2013. — comprehensive mechanical behavior across metals, polymers, ceramics, and composites; stress-strain, fatigue (S-N, strain-life, fracture mechanics), creep. — [OpenLibrary record](https://openlibrary.org/works/OL1937964W)
- Anderson, T. L., *Fracture Mechanics: Fundamentals and Applications*, 4th ed., CRC Press, 2017 (1st ed. 1991). — LEFM/EPFM, stress intensity, K_IC, J-integral, CTOD, R-curves, dynamic fracture, fatigue crack growth. — [OpenLibrary record](https://openlibrary.org/works/OL8636683W)
- Suresh, S., *Fatigue of Materials*, 2nd ed., Cambridge University Press, 1998 (1st ed. 1991). — fatigue mechanisms, crack initiation and propagation, low/high-cycle, multiaxial, environmental and thermal fatigue, fatigue of composites/ceramics. — [OpenLibrary record](https://openlibrary.org/works/OL1862375W)
- Bannantine, J. A., Comer, J. J., and Handrock, J. L., *Fundamentals of Metal Fatigue Analysis*, Prentice Hall, 1990. — practical fatigue of notched components: S-N, strain-life, fracture mechanics, mean-stress corrections, cumulative damage. — [OpenLibrary record](https://openlibrary.org/works/OL4648900W)
- Hertzberg, R. W., Vinci, R. P., and Hertzberg, J. L., *Deformation and Fracture Mechanics of Engineering Materials*, 5th ed., Wiley, 2012 (1st ed. 1976). — deformation, fracture, fatigue, and creep across metals, polymers, ceramics, and composites. — [OpenLibrary record](https://openlibrary.org/works/OL21577321W)
- ASM International, *ASM Handbook, Vol. 11: Failure Analysis and Prevention* and *Vol. 19: Fatigue and Fracture* (plus related volumes). — failure modes, fractography, case histories, material-specific fatigue/fracture data. — [ASM International](https://www.asminternational.org); [OpenLibrary record (Fatigue and Fracture, Lampman ed.)](https://openlibrary.org/works/OL8689263W); [OpenLibrary record (case histories)](https://openlibrary.org/works/OL18227764W)
- Budynas, R. G. and Nisbett, J. K. (continuing Shigley's *Machine Design*), *Shigley's Mechanical Engineering Design*, latest eds. (1st ed. 1956 by J. E. Shigley), McGraw-Hill. — machine-design failure theories, fatigue endurance limits, stress concentration, shaft/bearing/gear design. — [OpenLibrary record](https://openlibrary.org/works/OL1923658W)

### Inferences
- An AI assistant can route most materials/failure queries to one of these ten sources: Callister (fundamentals), Ashby (selection), Dieter/Hertzberg/Dowling (behavior), Anderson/Suresh (fracture/fatigue depth), Bannantine (practical fatigue), ASM (case data), Shigley (design criteria).
- Older editions (Dieter 1961/1988, Bannantine 1990, Suresh 1998) remain canonical for concepts even where newer data exist; newer editions update data and add composites/polymers.

### Gaps
- Detailed tables of contents for each edition were not retrieved from primary sources in this pass (publisher TOC PDFs were not parseable and web search returned no results); chapter-level granularity above is from general knowledge of these standard texts and should be verified against the specific edition before citing page numbers.

## Cross-book topic-to-book ownership matrix

### Takeaway
No single book owns all topics; the assistant should combine sources (e.g., Ashby for selection plus Dowling for fatigue life plus Anderson for crack growth).

### Cited Findings
- Stress-strain / elasticity / plasticity: Dieter (metals) — [OpenLibrary](https://openlibrary.org/works/OL4469776W); Dowling (all classes) — [OpenLibrary](https://openlibrary.org/works/OL1937964W); Hertzberg (all classes) — [OpenLibrary](https://openlibrary.org/works/OL21577321W); Callister (intro) — [Wiley](https://www.wiley.com/en-us/Materials+Science+and+Engineering%3A+An+Introduction%2C+10th+Edition-p-9781119405498).
- Fatigue (S-N, endurance): Shigley (design endurance limits, Marin factors) — [OpenLibrary](https://openlibrary.org/works/OL1923658W); Bannantine (practical S-N) — [OpenLibrary](https://openlibrary.org/works/OL4648900W); ASM Vol. 19 (data) — [OpenLibrary](https://openlibrary.org/works/OL8689263W).
- Fatigue (strain-life, Coffin-Manson): Dowling — [OpenLibrary](https://openlibrary.org/works/OL1937964W); Bannantine — [OpenLibrary](https://openlibrary.org/works/OL4648900W); Suresh (mechanisms) — [OpenLibrary](https://openlibrary.org/works/OL1862375W).
- Fracture mechanics (K, J, CTOD, Paris): Anderson — [OpenLibrary](https://openlibrary.org/works/OL8636683W); Dowling — [OpenLibrary](https://openlibrary.org/works/OL1937964W); Hertzberg — [OpenLibrary](https://openlibrary.org/works/OL21577321W).
- Creep: Dowling — [OpenLibrary](https://openlibrary.org/works/OL1937964W); Dieter (metals) — [OpenLibrary](https://openlibrary.org/works/OL4469776W); Callister (intro) — [Wiley](https://www.wiley.com/en-us/Materials+Science+and+Engineering%3A+An+Introduction%2C+10th+Edition-p-9781119405498).
- Wear / corrosion: Callister (intro) — [Wiley](https://www.wiley.com/en-us/Materials+Science+and+Engineering%3A+An+Introduction%2C+10th+Edition-p-9781119405498); ASM Handbook (case data) — [OpenLibrary](https://openlibrary.org/works/OL18227764W).
- Material selection: Ashby — [OpenLibrary](https://openlibrary.org/works/OL8323422W).
- Heat treatment / microstructure: Callister — [Wiley](https://www.wiley.com/en-us/Materials+Science+and+Engineering%3A+An+Introduction%2C+10th+Edition-p-9781119405498); Dieter — [OpenLibrary](https://openlibrary.org/works/OL4469776W).
- Static failure theories (von Mises, Tresca, Mohr-Coulomb): Shigley — [OpenLibrary](https://openlibrary.org/works/OL1923658W).

### Inferences
- For an AI, the highest-value pairings are: Shigley (criteria) + ASM (data) for design checks; Dowling/Anderson (methods) + Suresh (mechanisms) for fatigue/fracture predictions.

### Gaps
- No quantitative equation sheets were extracted from the books in this pass; equations such as Basquin, Coffin-Manson, Paris, Goodman/Soderberg/Gerber, and Marin factors are standard and should be verified against the cited edition before use.

## Consult-when decision rules for the AI assistant

### Takeaway
Route by question type: fundamentals → Callister; selection → Ashby; metal plasticity → Dieter; fatigue life → Bannantine/Dowling; crack growth → Anderson; advanced fatigue → Suresh; failure root cause → ASM; machine-design criteria → Shigley.

### Cited Findings
- Use Callister when the user asks about crystal structure, phase diagrams, heat treatment, or material classes. — [Wiley](https://www.wiley.com/en-us/Materials+Science+and+Engineering%3A+An+Introduction%2C+10th+Edition-p-9781119405498)
- Use Ashby when the user asks which material to choose or to derive a material index. — [OpenLibrary](https://openlibrary.org/works/OL8323422W)
- Use Dieter when the user asks about yielding, work hardening, or metal forming. — [OpenLibrary](https://openlibrary.org/works/OL4469776W)
- Use Dowling when the user asks for S-N/strain-life fatigue life or creep of non-metals. — [OpenLibrary](https://openlibrary.org/works/OL1937964W)
- Use Anderson when the user asks for K_IC, J, CTOD, or damage-tolerance crack sizes. — [OpenLibrary](https://openlibrary.org/works/OL8636683W)
- Use Suresh when the user asks about fatigue thresholds, closure, or multiaxial/environmental fatigue. — [OpenLibrary](https://openlibrary.org/works/OL1862375W)
- Use Bannantine et al. when the user asks for notched-component fatigue life or cumulative damage. — [OpenLibrary](https://openlibrary.org/works/OL4648900W)
- Use ASM Handbook when the user asks for failure-mode identification, fractography, or case histories. — [ASM International](https://www.asminternational.org)
- Use Shigley when the user asks for static failure criteria, endurance limits, or machine-component design. — [OpenLibrary](https://openlibrary.org/works/OL1923658W)

### Inferences
- Combining Shigley criteria with ASM data and Dowling/Anderson methods gives a complete design-check workflow without over-relying on any single text.

### Gaps
- Edition-specific page numbers and worked-example references were not verified in this pass.
