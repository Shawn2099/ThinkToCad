# plate_cam

**Type:** mechanism
**Function:** Convert cam rotation into programmed follower motion in a plane perpendicular to the camshaft axis.

## How it works
A disk cam (plate) rotates; a follower rides on its profile. Follower motion = rise (away), dwell (rest), return (toward). Profile is the pitch curve offset from base circle by follower radius. Closure force- or form-closed.

## Key dimensions / equations
- Base circle = smallest circle to cam profile; prime circle radius = follower radius + base circle radius.
- Pressure angle phi <= 30deg (translating follower) / <= 35deg (rotating follower).
- Fundamental law: follower position, velocity, acceleration continuous; jerk finite.
- Profiles: SHM s = h/2[1-cos(pitheta/beta)]; cycloidal s = h[theta/beta - (1/2pi) sin(2pitheta/beta)]; 4-5-6-7 polynomial s = h[35(theta/beta)^4 - 84(theta/beta)^5 + 70(theta/beta)^6 - 20(theta/beta)^7].
- Valve-cam: phi = pi/2 - theta/2; centre distance C = L/(1-sin phi); tip radius r = R - L*sin phi/(1-sin phi).

## Constraints
- Pressure angle must stay <=30deg/35deg or follower binds.
- Profile curvature must exceed follower radius to avoid undercutting.
- Force-closed needs spring to maintain contact.

## Failure modes
- Binding/jamming at excessive pressure angle.
- Vibration from infinite jerk (trapezoidal/SHM discontinuities).
- Follower wear; lubrication needed.

## When to use
Valve trains, indexing, packaging, function generation, automated machinery.

## DFM (small workshop)
Prefer roller followers and form-closed grooves for positive positioning; use cycloidal/4-5-6-7 profiles when vibration matters.

## Sources
cams_and_gears.md