# face_cam

**Type:** mechanism
**Function:** Convert cam rotation into follower motion riding on the face of a disk, often in a slot for positive positioning.

## How it works
Follower rides on the face (end) of a rotating disk; commonly in a slot/groove for positive positioning. Can implement repetitive motion (closed curve groove) or function generation (stopped groove). Example: scroll plate in a scroll chuck.

## Key dimensions / equations
- Profile laid out on disk face; radial/axial displacement per cam angle.
- Pressure angle limits apply (<=30deg/35deg).
- Fundamental law: continuous s, v, a; finite jerk.

## Constraints
- Face must be flat and true; runout affects motion.
- Slot machining on a face is harder than plate-cam profile.
- Wear on face surface.

## Failure modes
- Face wear causing profile error.
- Follower jumping if force-closed and under-sprung.
- Binding at excessive pressure angle.

## When to use
Scroll chucks, repetitive motion devices, function generators, end-face actuation.

## DFM (small workshop)
Keep profiles simple; use roller followers; machine face true; lubricate.

## Sources
cams_and_gears.md