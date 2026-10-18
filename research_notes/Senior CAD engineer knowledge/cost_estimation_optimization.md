# Cost Estimation and Design Optimization for Mechanical Design

## Cost estimation methods: parametric, analogous, bottom-up, ABC. When to use each.

### Takeaway
Cost estimation for manufactured parts spans a spectrum from rough order-of-magnitude (analogous/parametric) to definitive (bottom-up with measured quantities); method choice should track design definition level and required accuracy, with ABC used to attribute overhead to cost drivers.

### Cited Findings
- A cost estimate is the summation of individual cost elements using established methods and valid data to estimate future costs of a program based on what is known today (GAO definition) — [Wikipedia: Cost estimate](https://en.wikipedia.org/wiki/Cost_estimate).
- Estimate classes (AACE/DOE): Class 5 order-of-magnitude (0–2% definition), Class 4 concept (1–15%), Class 3 preliminary (10–40%), Class 2 substantive (30–70%), Class 1 definitive (50–100%); accuracy ranges tighten as definition increases — [Wikipedia: Cost estimate](https://en.wikipedia.org/wiki/Cost_estimate).
- Definitive (Class 1) estimates are prepared from fully designed plans: review design, take off/quantify scope into line items with measured quantities, then apply costs (quantity × material/labor cost), plus overhead, profit, taxes, bonds, escalation, contingency; documented as a Basis of Estimate (BOE) — [Wikipedia: Cost estimate](https://en.wikipedia.org/wiki/Cost_estimate).
- Order-of-magnitude (Class 5) estimates use experience/judgment, historical values/charts, rules of thumb, factor estimating (scale cost of similar facility by size/place/time), and cost modeling when little design info exists — [Wikipedia: Cost estimate](https://en.wikipedia.org/wiki/Cost_estimate).
- Manufacturing cost = direct materials + direct labor + manufacturing overhead (indirect labor, indirect materials, machine depreciation, rent, insurance, electricity, freight) — [Wikipedia: Manufacturing cost](https://en.wikipedia.org/wiki/Manufacturing_cost), citing Ostwald & McLaren (2004) *Cost Analysis and Estimating for Engineering and Management*.
- Activity-based costing (ABC) identifies activities and assigns cost of each activity to products/services by actual consumption; uses cost drivers to attach activity costs to outputs; more indirect cost moved into direct cost than conventional costing — [Wikipedia: Activity-based costing](https://en.wikipedia.org/wiki/Activity-based_costing), citing CIMA (2008) and Kaplan & Bruns (1987).
- ABC historically developed in US manufacturing 1970s–80s (CAM-I); Cooper & Kaplan (Harvard Business Review, 1988) popularized it; later Drucker (1999) — [Wikipedia: Activity-based costing](https://en.wikipedia.org/wiki/Activity-based_costing).
- ABC limitations: expensive/difficult to implement manually; treats fixed costs as variable; some overhead (business-sustaining) untraceable; applicability bound to data-capture cost — [Wikipedia: Activity-based costing](https://en.wikipedia.org/wiki/Activity-based_costing).

### Inferences
- For a small workshop/frugal design: early concept → parametric/analogous (factor estimating, rules of thumb); detailed CAD → bottom-up (quantity takeoff × unit rates); ABC only if multiple products share processes and overhead attribution matters.
- Parametric estimating in the construction sense uses statistical relationships (cost as function of parameters); analogous estimating uses a single similar past item scaled — [inference from cost estimate classes above].

### Gaps
- No reliable source found in this pass for aPriori/DFMPro internal algorithms or pricing; treat as commercial tool claims (unverified). Specific "when to use each" decision trees from Ulrich & Eppinger / Dieter not retrieved (textbook content not online in this pass).

## Cost drivers: material, labor, machine time, tooling, setup, overhead, quality. How each scales with design choices.

### Takeaway
Cost of a machined/formed part is dominated by setup and machine time (per-flip overhead) plus material form; design choices that reduce number of operations, material hardness/form, and tolerance tightness yield outsized savings.

### Cited Findings
- For CNC machining, cost is driven by time: machining time, setup time, NC programming, fixturing; objective is minimize time — [Wikipedia: Design for manufacturability (CNC section)](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Each operation ("flip of the part") incurs setup, machine, load/unload, and programming time; minimizing number of operations yields significant savings; volume (10–300 parts) amortizes setup into noise — [Wikipedia: Design for manufacturability](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Material type: aluminum/brass easy; steel/stainless/titanium/exotic alloys harder, longer; fiberglass/carbon-filled plastics reduce machinability; soft/gummy plastics problematic — [Wikipedia: Design for manufacturability](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Material form: bar stock ~half cost per pound vs plate (aluminum example); specify cheapest form serving geometry — [Wikipedia: Design for manufacturability](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Tolerances: tighter tolerance → more expensive; specify loosest functional tolerance — [Wikipedia: Design for manufacturability](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Design/shape: material removal volume and tool L:D ratio; <3:1 optimum; chamfers cheaper than radii; 3D interpolated radii ~10× cost; undercuts more expensive; smaller tools more expensive — [Wikipedia: Design for manufacturability](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Manufacturing overhead includes indirect labor, indirect materials, depreciation, rent, insurance, electricity, freight — [Wikipedia: Manufacturing cost](https://en.wikipedia.org/wiki/Manufacturing_cost).
- ABC: cost driver is factor creating cost of activity (e.g., machine hours, transaction time) — [Wikipedia: Activity-based costing](https://en.wikipedia.org/wiki/Activity-based_costing).

### Inferences
- Setup cost is largely fixed per batch; per-part cost falls with volume; for frugal one-off/small batches, design for single-setup (single op) dominates.
- Material cost scales with volume removed (buy-to-fly ratio); near-net-shape processes reduce material and machining.

### Gaps
- No sourced quantitative scaling laws (e.g., cost vs tolerance exponent) retrieved; flag as unverified. Boothroyd-Dewhurst DFMA time-standard data not retrieved.

## Design-to-cost: target costing, value engineering, cost drivers in design (part count, tolerance, surface finish, material, process).

### Takeaway
Design-to-cost sets a cost target before design and drives decisions via value engineering (function/cost ratio) and DFM; key levers are part count, tolerance, finish, material, and process selection.

### Cited Findings
- Target costing referenced via Cooper & Slagmulder (1997) *Target Costing and Value Engineering* (further reading in VE article) — [Wikipedia: Value engineering](https://en.wikipedia.org/wiki/Value_engineering).
- Value engineering: systematic analysis of functions to lower cost with tolerable performance loss; value = function/cost; functions described as active-verb + measurable-noun; uses how/why questioning — [Wikipedia: Value engineering](https://en.wikipedia.org/wiki/Value_engineering).
- VE originated at GE during WWII (Lawrence Miles) as value analysis/value control; formalized by US Navy 1957 — [Wikipedia: Value engineering](https://en.wikipedia.org/wiki/Value_engineering).
- VE mandated for US federal agencies (41 U.S.C. 4306); FAR Part 48 — [Wikipedia: Value engineering](https://en.wikipedia.org/wiki/Value_engineering).
- VE risks: can become cost-cutting euphemism compromising safety/performance (Grenfell Tower cladding ~£300k saving; Pruitt-Igoe) — [Wikipedia: Value engineering](https://en.wikipedia.org/wiki/Value_engineering).
- DFM: designing product to reduce manufacturing cost and ease manufacture; factors: raw material type/form, tolerances, secondary processing/finishing — [Wikipedia: Design for manufacturability](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- DFMA (Boothroyd-Dewhurst) referenced as related to DFM — [Wikipedia: Design for manufacturability](https://en.wikipedia.org/wiki/Design_for_manufacturability).
- Frugal innovation linked under engineering approaches alongside value engineering — [Wikipedia: Value engineering](https://en.wikipedia.org/wiki/Value_engineering).

### Inferences
- Target costing (cost target set from market price minus profit) is standard in Ulrich & Eppinger Product Design and Development (not retrieved here); apply as design-to-cost anchor.
- Part-count reduction (assembly) is a Boothroyd-Dewhurst DFA lever; fewer parts → fewer operations → lower cost.

### Gaps
- Specific target-costing formulas and DFA part-count equations not retrieved (textbook sources not online). Surface-finish cost scaling not sourced.

## Optimization: parametric optimization (gradient-based, DOE), topology optimization, shape optimization, size optimization. Multi-objective (Pareto, NSGA-II).

### Takeaway
Optimization ranges from sizing/shape (parametric, gradient-based) to topology (material distribution, SIMP), with multi-objective problems solved via Pareto fronts and evolutionary algorithms such as NSGA-II.

### Cited Findings
- Topology optimization: optimizes material layout in a design space for loads/boundary conditions/constraints; differs from shape and sizing optimization in that design can attain any shape — [Wikipedia: Topology optimization](https://en.wikipedia.org/wiki/Topology_optimization).
- Conventional topology optimization uses FEM; solved via gradient-based methods (optimality criteria, method of moving asymptotes) or non-gradient (genetic algorithms) — [Wikipedia: Topology optimization](https://en.wikipedia.org/wiki/Topology_optimization).
- SIMP interpolation: E = E0 + ρ^p (E1 - E0), p ∈ [1,3], penalizes intermediate densities; non-convexities introduced — [Wikipedia: Topology optimization](https://en.wikipedia.org/wiki/Topology_optimization).
- Topology optimization results often hard to manufacture; manufacturability constraints active research; additive manufacturing enables direct use — [Wikipedia: Topology optimization](https://en.wikipedia.org/wiki/Topology_optimization).
- Design optimization listed as a design concept — [Wikipedia: Design for manufacturability (see also)](https://en.wikipedia.org/wiki/Design_for_manufacturability).

### Inferences
- Parametric (size) optimization: vary dimensions; gradient-based when smooth/convex; use DOE when black-box/expensive.
- Multi-objective (Pareto, NSGA-II): standard evolutionary multi-objective optimization; not sourced here—flag as general knowledge.

### Gaps
- NSGA-II specifics, shape optimization algorithms, and parametric gradient-based methods (adjoint, finite differences) not retrieved from sources this pass. Flag unverified.

## Design of experiments (DOE): full factorial, fractional factorial, Taguchi, response surface methodology.

### Takeaway
DOE replaces one-factor-at-a-time with structured factorial designs; fractional factorials and Taguchi orthogonal arrays reduce runs, while RSM (central composite/Box-Behnken) fits quadratic models for optimization.

### Cited Findings
- DOE: construction of procedures explaining how changes in independent (input) variables affect dependent (response) variables; includes control variables — [Wikipedia: Design of experiments](https://en.wikipedia.org/wiki/Design_of_experiments).
- Fisher's principles: comparison, randomization, replication, blocking, orthogonality, multifactorial experiments (vs one-factor-at-a-time) — [Wikipedia: Design of experiments](https://en.wikipedia.org/wiki/Design_of_experiments).
- Plackett-Burman designs (1946) and Rao's orthogonal arrays central to Taguchi methods (developed at ISI early 1950s) — [Wikipedia: Design of experiments](https://en.wikipedia.org/wiki/Design_of_experiments).
- Response surface methodology (RSM) linked as optimal designs for regression models; Box-Behnken and central composite designs mentioned in see-also — [Wikipedia: Design of experiments](https://en.wikipedia.org/wiki/Design_of_experiments).
- Factorial design image referenced; full factorial vs response surface with second-degree polynomial — [Wikipedia: Design of experiments](https://en.wikipedia.org/wiki/Design_of_experiments).

### Inferences
- Full factorial: all combinations; cost grows 2^k (or 3^k); use for few factors.
- Fractional factorial: subset, assumes higher-order interactions negligible; Taguchi uses orthogonal arrays for robust design.
- RSM: after screening, fit quadratic via central composite/Box-Behnken to find optimum.

### Gaps
- Specific run counts, aliasing structure, and Taguchi S/N ratios not retrieved; flag. Montgomery/Box textbooks cited generally.

## Sensitivity analysis: which parameters most affect cost/performance.

### Takeaway
Sensitivity analysis identifies parameters with largest effect on cost/performance; typically done via DOE main effects, regression coefficients, or local perturbation (finite differences) of parametric cost models.

### Cited Findings
- No dedicated sensitivity-analysis source retrieved this pass beyond DOE/Fisher principles (randomization, blocking, orthogonality) and cost-driver discussion — [Wikipedia: Design of experiments](https://en.wikipedia.org/wiki/Design_of_experiments); [Wikipedia: Design for manufacturability](https://en.wikipedia.org/wiki/Design_for_manufacturability).

### Inferences
- In practice: vary one parameter at a time or use DOE main-effect plots; tornado diagrams for cost; Monte Carlo for uncertainty. (General engineering practice; not sourced here—flag.)

### Gaps
- Sourced methods (Sobol, Morris screening, adjoint sensitivity) not retrieved. Flag as unverified/gap.

## Life cycle cost: operating cost, maintenance, energy, disposal.

### Takeaway
Life-cycle cost analysis (LCCA) selects the most cost-effective option across purchase, operation, sustainment, and disposal; differs from total cost of ownership; includes operating/maintenance/energy/disposal.

### Cited Findings
- LCCA: economic analysis tool to determine most cost-effective option to purchase, run, sustain, or dispose of an object/process; used for economic sustainability — [Wikipedia: Life-cycle cost analysis](https://en.wikipedia.org/wiki/Life-cycle_cost_analysis).
- LCCA differs from TCOA: LCCA finds most cost-effective option across life; TCOA analyzes direct and indirect cost of an item — [Wikipedia: Life-cycle cost analysis](https://en.wikipedia.org/wiki/Life-cycle_cost_analysis), citing Bearfield & Dubnick (2016).
- Green design: operating costs and capital added to decide investment effect; ISO 15686 referenced via value engineering see-also — [Wikipedia: Life-cycle cost analysis](https://en.wikipedia.org/wiki/Life-cycle_cost_analysis); [Wikipedia: Value engineering](https://en.wikipedia.org/wiki/Value_engineering).

### Inferences
- For frugal workshop: energy/maintenance often dominate over material for powered tools; LCCA favors repairable, efficient designs.

### Gaps
- Discounting/NPV formulas, maintenance models, disposal cost data not retrieved. Flag.

## Cost databases and estimation tools: aPriori, DFMPro, custom parametric models.

### Takeaway
Commercial should-cost/DFM tools (aPriori, DFMPro) automate parametric cost models; custom parametric models are feasible for small workshops using historical rates and quantity takeoffs.

### Cited Findings
- Should-cost modeling: documented calculation by customer to understand supplier costs and challenge prices; providers maintain cost data — [Wikipedia: Cost estimate](https://en.wikipedia.org/wiki/Cost_estimate).
- Cost databases/indexes used to price quantified line items; RSMeans mentioned for construction — [Wikipedia: Cost estimate](https://en.wikipedia.org/wiki/Cost_estimate).
- Cost indexes adjust capital costs for time/technology/materials/labor/inflation — [Wikipedia: Cost estimate](https://en.wikipedia.org/wiki/Cost_estimate).

### Inferences
- aPriori/DFMPro: commercial tools; specific capabilities not verified in this pass (unverified).
- Custom parametric model for small workshop: cost = material (mass × $/kg) + machine time (minutes × rate) + setup (per batch) + tooling amortization + overhead %; calibrate with historical jobs.

### Gaps
- No sourced detail on aPriori/DFMPro. Flag as unverified commercial claims. No sourced cost-rate benchmarks for machining (shop rates vary by region).