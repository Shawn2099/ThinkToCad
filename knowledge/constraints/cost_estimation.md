# Cost estimation and optimization constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/cost_estimation_optimization.md;
Ulrich & Eppinger, Boothroyd-Dewhurst, Dieter, Kalpakjian.

## Cost estimation methods
- Parametric: cost = f(parameters) from historical data. Fast, less accurate.
- Analogous: compare to similar past products. Good for early estimates.
- Bottom-up: sum of material + labor + machine + tooling + overhead. Most accurate.
- Activity-based costing (ABC): allocate overhead by activity. Good for complex.
- Should-cost: estimate what a part should cost (for negotiation).

## Cost drivers (design levers)
- Part count: fewer parts = lower assembly cost. (DFA)
- Material: choose cheapest that meets requirements. Avoid exotic materials.
- Tolerances: tighter = more expensive (machining, inspection). Use standard tolerances.
- Surface finish: finer = more expensive. Specify only where needed.
- Process: casting/forging for high volume; machining for low volume/prototypes.
- Tooling: high upfront (dies, molds) but low per-part. Amortize over volume.
- Assembly: snap-fits > screws > welds (for speed). Minimize fastener types.

## Design-to-cost
- Target costing: set target cost, design to meet it. Value engineering: maximize
  function/cost ratio. Cost drivers in design: part count, tolerance, finish,
  material, process, assembly method.

## Optimization methods
- Parametric: vary parameters, evaluate objective (cost, weight, stress). Use DOE.
- Topology optimization: optimize material distribution for stiffness/weight.
- Shape optimization: optimize geometry (fillets, holes, ribs).
- Size optimization: optimize dimensions (thickness, diameter).
- Multi-objective: Pareto front (trade-off between cost and performance).
- DOE: full factorial (all combinations), fractional factorial (screening),
  Taguchi (robust design), response surface (optimization).

## Sensitivity analysis
- Identify which parameters most affect cost/performance. Focus design effort there.
- Use tornado charts or Morris screening for high-dimensional spaces.

## Life cycle cost
- Operating cost: energy, maintenance, consumables. Often exceeds manufacturing cost.
- Maintenance: accessibility, standard parts, diagnostic features.
- Disposal: recyclability, hazardous materials.

## AI rules
- Estimate cost early and update as design matures.
- Flag cost drivers: tight tolerances, fine finishes, exotic materials, complex geometry.
- Recommend DFM: reduce part count, standardize, use default tolerances/finishes.
- For small workshops: prefer machining over casting (no tooling), standard stock
  sizes, hand-tool-friendly features.