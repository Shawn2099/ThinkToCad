# four_bar_linkage

**Type:** mechanism
**Function:** Convert input crank rotation into output rocker oscillation (or full rotation) through a closed four-link chain.

## How it works
Four rigid links (ground frame, input crank, coupler, output link) connected in a loop by four revolute joints. Input rotation of the crank drives the coupler, which drives the output link. Motion family determined by Grashof condition and which link is grounded.

## Key dimensions / equations
- Mobility M = 1 (planar 4-bar with four 1-DOF joints).
- Grashof: S + L <= P + Q (S shortest, L longest, P/Q intermediate) -> at least one link fully rotates.
- Classification (Grashof): shortest link grounded -> double-crank (drag-link); link adjacent to shortest grounded -> crank-rocker; link opposite shortest grounded -> double-rocker.
- Time ratio Q = (180deg+beta)/(180deg-beta); imbalance angle beta = 180deg*(Q-1)/(Q+1).
- Transmission angle mu: keep mu_min >= 40-45deg to avoid binding.

## Constraints
- mu_min must stay above ~40-45deg or mechanism binds/stalls under load.
- Grashof margin P+Q-S-L avoids change-point ambiguity.
- Joint tolerances stack with link count.

## Failure modes
- Binding/stalling when mu -> 0deg/180deg.
- Change-point folding when S+L = P+Q.
- Pin/bushing wear; needs lubrication.

## When to use
Rotary-to-oscillatory or rotary-to-rotary motion with 1 DOF; windshield wipers, pumps, steering, presses.

## DFM (small workshop)
Use simple pin joints (bolts/bushings), standard bar-stock links, avoid near-collinear toggle unless deliberate; prototype and measure mu.

## Sources
linkages.md