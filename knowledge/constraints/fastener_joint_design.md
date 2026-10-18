# Fastener and joint design constraints (from research)

Sources: research_notes/Senior CAD engineer knowledge/fastener_joint_design.md;
Shigley, Bickford, Mott, Juvinall, AWS D1.1, ASME VIII.

## Bolted joints
- Preload: Fm = 0.75 * Fp (proof load) typical. Torque: T = K * F * d (K=0.20
  dry, 0.15 lubricated).
- Stress area: As = pi/4 * (d - 0.9382*p)^2 (metric). Proof load: Fp = Sp * As.
- Joint stiffness: kb (bolt) and km (members). Load factor C = kb/(kb+km).
- Separation load: F_sep = Fp / C. Fatigue: Goodman with mean stress from preload.
- Eccentric loading: use elastic or IC method for bolt group. Interaction equation:
  (sigma/sigma_allow)^2 + (tau/tau_allow)^2 <= 1.

## Thread engagement
- Minimum engagement: 1.0*d for steel, 1.5*d for cast iron, 2.0-2.5*d for aluminum/plastic.
- Thread stripping vs bolt failure: design so bolt fails first (ductile failure visible).

## Locking methods
- Nyloc: up to 80C, self-locking, reusable 3-5 times. Threadlocker: anaerobic,
  permanent or removable. Safety wire: aerospace, positive lock. Cotter pins: shear.

## Welded joints
- Fillet weld: throat = 0.707*leg, shear stress = F/throat_area.
- Butt weld: full penetration, strength = base metal. Partial penetration: throat
  = depth of penetration.
- AWS D1.1: allowable shear = 0.3*Fu (fillet), 0.3*Fy (base). Fatigue categories
  (A-G) for cyclic loads.
- Distortion: minimize heat input, use symmetric welds, pre-bend. HAZ: affects
  toughness, avoid in critical areas.

## Rivets
- Shear: tau = F/(n*A_rivet). Bearing: sigma_b = F/(d*t). Tearing: sigma_t =
  F/((w-n*d)*t). Efficiency: 50-88% depending on pattern.

## Pins
- Dowel: precision location, shear. Clevis: pivot, double shear. Cotter: tapered,
  self-locking. Spring (roll) pins: flexible, good for cast/soft materials.
- Shear capacity: V = 0.5*Sy*A (single shear), V = Sy*A (double shear).

## Keys
- Square key: width = height = d/4. Torque capacity: T = (Sy/2)*w*l*d/2.
- Woodruff: semicircular, for tapered shafts. Gib-head: removable.
- Keyway stress concentration: Kt = 2.14 (square key). Fatigue optimization:
  round keyway ends, larger fillet radius.

## Press-fit / shrink-fit
- Interference pressure: p = E*delta/(2*r) * (1 - nu^2) (simplified).
- Hoop stress: sigma_h = p*r/t. Torque capacity: T = mu*p*A*r.
- Assembly: shrink fit (heat outer, cool inner). ISO 286 interference fits (H7/s6,
  H7/u6). DIN 7190 includes roughness correction.

## Adhesive bonds
- Types: epoxy (high strength), cyanoacrylate (fast), anaerobic (threadlocker),
  silicone (flexible, sealing), polyurethane (tough, flexible).
- Joint design: lap (shear), scarf (tension), butt (weak in peel). Avoid peel loads.
- Surface prep: clean, roughen, primer. Bondline thickness: 0.1-0.5mm optimal.

## AI rules
- Size bolts for preload + external load + fatigue. Check separation load.
- Use standard bolt sizes and grades (8.8, 10.9, 12.9 metric).
- Weld size = min(leg of thinner part, 0.7*thicker part thickness).
- Press-fit interference: 0.001-0.002*d for steel, 0.002-0.004*d for aluminum.
- Prefer bolted joints for serviceability, welded for permanent/low cost.