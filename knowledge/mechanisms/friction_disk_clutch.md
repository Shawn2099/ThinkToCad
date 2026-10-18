# friction_disk_clutch

**Type:** clutch
**Function:** Transmit torque between shafts by friction between a disk and flywheel/pressure plate, allowing controlled engagement.

## How it works
Friction disk pressed against flywheel by spring; torque transmitted by friction. Single-plate dry (common) or multi-plate wet (oil bath) with lower mu but smoother/longer life. Torque capacity T = mu*F*r_m (single contact) or n*mu*F*r_m (multi-plate, n interfaces).

## Key dimensions / equations
- T = mu*F*r_m (single contact); multi-plate T = n*mu*F*r_m.
- Cone clutch: T = (mu*F*r_m)/sin(alpha); self-locking if mu > tan(alpha).
- Centrifugal engagement: F_c = m*r*omega^2 overcomes spring preload; engagement RPM proportional sqrt(k*x/(m*r)).

## Constraints
- Slippage increases wear; minimize slip time.
- Heat dissipation limits duty; ventilation needed.
- Wet clutches have lower mu; compensate with more plates.

## Failure modes
- Lining wear and glazing.
- Overheating/fade.
- Spring fatigue (pressure plate).

## When to use
Manual transmissions, machine tool drives, general power transmission.

## DFM (small workshop)
Use cast-iron/steel plates with replaceable organic or sintered-bronze lining; bolted (not riveted) linings for serviceability; keep surfaces flat within 0.05 mm.

## Sources
clutches_brakes_couplings_indexing.md