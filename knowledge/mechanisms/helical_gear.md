# helical_gear

**Type:** mechanism
**Function:** Transmit power between (usually) parallel shafts with angled teeth for smoother, quieter, higher-load operation.

## How it works
Teeth are cut at a helix angle psi; engagement is gradual (line contact grows across the face), reducing noise and increasing load capacity. Produces axial thrust unless double-helical/herringbone.

## Key dimensions / equations
- Pitch relations: p_n = p cos psi; pitch diameter d = N*m_n/cos psi; normal DP P_nd = P_d/cos psi.
- Axial thrust = F_t tan psi (needs thrust bearings).
- Double-helical/herringbone cancels axial thrust.
- Helical gears considered for pitch-line speed > 25 m/s.

## Constraints
- Axial thrust requires thrust bearings.
- More complex/expensive to manufacture than spur.
- Crossed helical for non-parallel shafts has point contact (lower capacity).

## Failure modes
- Thrust-bearing overload if not sized.
- Pitting/scuffing/root fatigue from overload/poor lubrication.
- Axial thrust can push gears apart.

## When to use
High-speed/noisy-sensitive drives, automotive transmissions, precision gearboxes.

## DFM (small workshop)
Use off-the-shelf helical gears; add thrust bearings; consider herringbone to cancel thrust.

## Sources
cams_and_gears.md