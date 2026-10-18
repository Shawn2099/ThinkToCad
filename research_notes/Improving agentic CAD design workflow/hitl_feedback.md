# Human-in-the-Loop Feedback Mechanisms for Agentic CAD Design Workflows

## How AI design tools present intermediate results for user approval

### Takeaway
AI design tools present intermediate results as galleries of generated alternatives (with renders/geometry), parametric sliders over precomputed design spaces, or locked-element + natural-language refinement loops; the best fit for a non-expert visualizer is a small curated set of 3D previews plus a "change this one thing" affordance rather than raw parameter tables.

### Cited Findings
- Autodesk Generative Design (Fusion/Revit) generates a multitude of solutions from user-defined objectives, constraints, and a design space; the user then explores outcomes and selects the one that best solves the challenge, or uses an outcome as the basis for a new study — [Autodesk](https://www.autodesk.com/solutions/generative-design); [Autodesk Revit learning](https://www.autodesk.com/learn/ondemand/curated/generative-design-in-revit/2vvRHPHJ3zejmWPTjt8KNS).
- nTop (nTopology) handles complex lattice/implicit geometry via field-driven design and reusable workflows; best for additive-first companies but specialized — [CoLab guide](https://www.colabsoftware.com/guides/how-generative-design-works-a-guide-for-engineering-managers); [Leo AI comparison](https://www.getleo.ai/blog/best-generative-engineering-design-platforms).
- Onshape enables simultaneous editing, real-time feedback, and stakeholder collaboration around CAD models — [Onshape resource center](https://www.onshape.com/en/resource-center/videos/cad-experts-guide-to-collaborative-design).
- "Neural CAD" generates multiple editable CAD models from a request and lets users lock down specific elements (e.g., a stairwell) while using natural-language prompts to change other elements (e.g., structural materials), recomputing the rest — [DEVELOP3D](https://www.develop3d.com/cad/neural-cad-accelerates-design-exploration).
- MIT (Schulz et al., 2017) "Interactive Design Space Exploration and Optimization for CAD Models" precomputes a parametric CAD sample set and uses interpolation to let users explore geometry variations in real time, displaying physical properties (mass, surface area, drag, moment of inertia) alongside the geometry — [MIT CDFG PDF](https://cdfg.mit.edu/pdf/journal/2017-schulz-interactive-design-space-exploration-and-optimization-for.pdf).
- SUPPLE (Gajos & Weld) generated interfaces from constraints/objective functions representing device affordances, user preferences, and user ability — cited in [Apple ML designer feedback paper](https://arxiv.org/abs/2509.16779).

### Inferences
- For a non-expert who visualizes but does not CAD, raw parametric tables are inappropriate; a gallery of 3-6 rendered 3D previews plus a "lock / change this" control (Neural CAD pattern) matches how non-experts already approve AI output.
- Precomputing a design space and interpolating (Schulz) is what makes real-time slider exploration feasible without re-running solvers.

### Gaps
- I found no source quantifying how many alternatives non-expert users can effectively compare in a gallery (e.g., 3 vs 6 vs 12); treat as an open design question.

## Feedback modalities: approve/reject, natural language, sliders, sketch overlays

### Takeaway
Designer-aligned modalities (sketching/annotation overlays and direct revision) produce higher-quality, lower-noise feedback than binary approve/reject rankings; sketching gives the best quality/quantity balance, and grounded annotations (boxes + text) outperform free-form comments because they localize the flaw.

### Cited Findings
- Apple CHI 2026 study (21 professional designers, ~1460 annotations): agreement between independent HCI experts and designers on the preferred UI was 49.2% for ranking (binary approve/reject, near chance), 57.3% for commenting, 63.6% for sketching, and 76.1% for revision — [arXiv 2509.16779](https://arxiv.org/abs/2509.16779).
- In the same study, designers collected 1063 rankings (4.8/min) but only 64 revisions (3.45 min each); sketching yielded 181 annotations and commenting 152. Sketching produced more comments per UI (2.7 vs 1.9) with shorter text (42.2 vs 87.1 chars) — [arXiv 2509.16779 §5.1.4](https://arxiv.org/abs/2509.16779).
- Sketching comments were lower-level and region-specific ("make this text larger"); commenting comments were higher-level ("poor information hierarchy") — [arXiv 2509.16779 §5.1.4](https://arxiv.org/abs/2509.16779).
- Training a generator on sketch-derived feedback gave the best model (Elo 1054, win rate 0.59) vs revision (1026, 0.54), UIClip (1009, 0.52), base (977, 0.46), commenting (970, 0.45), ranking (962, 0.44); commenting/ranking did not improve or slightly degraded performance — [arXiv 2509.16779 §5.2.3](https://arxiv.org/abs/2509.16779).
- Hartmann et al. (d.note) identified commenting, sketching, and revising as core designer revision activities and showed change tracking + annotations + alternatives improve revision efficiency — cited in [Apple paper §2.3](https://arxiv.org/abs/2509.16779).
- RLHF-Blender supports multiple feedback types: evaluative, comparative, corrective, demonstrative, and descriptive — cited in [Apple paper §2.2](https://arxiv.org/abs/2509.16779) (Metz et al., 2023).
- Preference-based Bayesian optimization (Astudillo et al., 2020; Cheng et al.) learns from pairwise preferences ("which do you prefer?") rather than absolute scores, which are more reliable for subjective human judgments; outputs a menu of designs for final selection — [Astudillo 2020](http://proceedings.mlr.press/v108/astudillo20a/astudillo20a.pdf); [Cheng et al.](https://cseweb.ucsd.edu/~jmcauley/workshops/scmls20/papers/scmls20_paper_29.pdf).
- Brochu (2010) examined Bayesian optimization when the objective function requires human feedback — [UBC circle](https://circle.ubc.ca/handle/2429/30519).

### Inferences
- For a non-expert CAD user, prefer a hybrid: 3D preview + (a) approve/reject on a small curated set, (b) sketch/region annotation ("make this wall taller") for partial changes, (c) natural-language edits for global changes; avoid pure ranking because it forces choices between flawed options and yields noisy signal.
- Sliders are appropriate only when backed by a precomputed design space (Schulz) and should be paired with live 3D preview; otherwise they overwhelm non-experts.

### Gaps
- No direct comparison of slider vs sketch-overlay efficacy for CAD geometry (vs UI) was found; UI findings are transferred by analogy.

## Partial approval and "change this one thing"

### Takeaway
Partial approval is best supported by (1) region-grounded annotations that target specific parts, (2) "lock" controls that freeze approved elements while the rest is regenerated, and (3) treating each distinct fix as a separate training/iteration data point rather than forcing a single canonical answer ("agreeing to disagree").

### Cited Findings
- Apple paper: sketch annotations associate text with a bounding box, enabling region-specific fixes ("make this text larger"); commenting yielded higher-level fixes — [arXiv 2509.16779 §4.2.3/5.1.4](https://arxiv.org/abs/2509.16779).
- Apple paper "Agreeing to Disagree": multiple designers may diagnose the same flaw but propose different fixes (e.g., color highlight vs. isolation); instead of forcing a ranking choice, each fix becomes a new data point, training the model to consider multiple solutions — [arXiv 2509.16779 §6.1](https://arxiv.org/abs/2509.16779).
- Neural CAD lets users lock down specific elements (e.g., a stairwell) and use natural-language prompts to change others, recomputing dependent geometry — [DEVELOP3D](https://www.develop3d.com/cad/neural-cad-accelerates-design-exploration).
- Parametric CAD design intent: parameters (dimensions, materials) can be modified to produce unique outcomes, enabling targeted edits without rebuilding the model — [PTC](https://www.ptc.com/en/technologies/cad/generative-design).

### Inferences
- A "change this one thing" interaction maps naturally to locking approved geometry and re-running generation on the unlocked subset, exactly the Neural CAD lock pattern.
- For non-experts, the system should translate a natural-language partial edit into a parameter change + re-render rather than expose the parameter directly.

### Gaps
- I found no empirical study measuring how often non-expert users successfully express partial edits in natural language vs. sketch annotations in a CAD context.

## Design space exploration and preference learning

### Takeaway
Design space exploration precomputes/interpolates a parametric CAD space for real-time visual exploration of geometry + physics; preference learning (especially pairwise, uncertainty-aware Bayesian optimization) turns subjective user choices into a learned utility without requiring numeric scores, outputting a small menu of candidates for final selection.

### Cited Findings
- Schulz et al. (2017) "Interactive Design Space Exploration and Optimization for CAD Models": harnesses parametric CAD data, precomputes samples, interpolates for real-time shape exploration, and displays physical properties (mass, surface area, drag, moment of inertia) — [MIT CDFG PDF](https://cdfg.mit.edu/pdf/journal/2017-schulz-interactive-design-space-exploration-and-optimization-for.pdf).
- Astudillo et al. (2020) "Multi-attribute Bayesian optimization with interactive preference learning": learns preferences from DM feedback, acknowledges uncertainty in the learned utility, and outputs a menu of evaluated designs for final selection; more efficient than multi-objective optimization — [PMLR](http://proceedings.mlr.press/v108/astudillo20a/astudillo20a.pdf).
- Cheng et al. "Preference-Based Bayesian Optimization in High Dimensions with Human Feedback": pairwise preferences are a more reliable measure than absolute numerical scores; LINESPAR algorithm over preference data — [UCSD](https://cseweb.ucsd.edu/~jmcauley/workshops/scmls20/papers/scmls20_paper_29.pdf).
- Autodesk Generative Design: AI explores a wide design space based on inputs, generating and evaluating many alternatives; generative design is an origination tool for early conceptual phases — [CoLab guide](https://www.colabsoftware.com/guides/how-generative-design-works-a-guide-for-engineering-managers); [Autodesk](https://www.autodesk.com/solutions/generative-design).
- PTC generative design: AI generates manufacture-ready alternatives; parametric design allows manual exploration by changing parameters — [PTC](https://www.ptc.com/en/technologies/cad/generative-design).

### Inferences
- A non-expert-facing CAD agent should combine (a) a generative/parametric design space (Schulz-style precomputation where feasible) with (b) pairwise preference learning so the user only ever answers "which of these two do you prefer?" — never numeric scoring.

### Gaps
- I found no source on how many preference queries a non-expert tolerates before fatigue in a CAD context; general BO literature uses "limited number" but no fixed number.

## Avoiding user fatigue in iterative loops

### Takeaway
Fatigue is reduced by reserving human review for high-risk/ambiguous decisions, using checkpoint/resume state, batching feedback, preferring richer single-screen feedback (sketch/revision) over high-volume low-quality ranking, and stopping when improvements plateau (~3 iterations) or cost exceeds benefit.

### Cited Findings
- HITL UX guidance: requiring approval for every AI action slows systems and causes "approval fatigue" (routine clicks); review should be reserved for decisions with risk, ambiguity, or real impact; "sending too much work back to humans" is a named pitfall — [Aufait UX](https://www.aufaitux.com/blog/human-in-the-loop-ux).
- Redis HITL patterns: checkpoint (serialized agent state) is the collaboration surface enabling pause/resume; latency compounds across layers — [Redis](https://redis.io/blog/ai-human-in-the-loop).
- NN/g iterative design: measured usability rises per iteration until quality plateaus; median improvement from first to last version 165%; mean ~3 iterations; estimated ~38% improvement between versions (rough, 4 case studies) — [NN/g](https://www.nngroup.com/articles/iterative-design).
- Midrocket stopping criteria: key metrics above target, no critical usability issues, stakeholders validated direction, or cost of further iteration exceeds expected benefit; diminishing returns — [Midrocket](https://midrocket.com/en/guides/iterative-design-process).
- IxDF: stop when further iterations bring only minor improvements or add unnecessary complexity, or resources are exhausted — [IxDF](https://ixdf.org/literature/topics/iterative-development).
- Apple paper: ranking produced 15x more annotations but lower quality and degraded the model; sketching balanced quality and quantity; richer single-screen feedback outperformed high-volume binary ranking — [arXiv 2509.16779 §5.1.4/6.2](https://arxiv.org/abs/2509.16779).

### Inferences
- For a CAD agent, default to ~3 review rounds with a plateau check, and only escalate to human review for ambiguous geometry/physics trade-offs; batch multiple small suggestions into one review screen.

### Gaps
- No CAD-specific study on optimal batch size for review screens was found.

## Optimal number of iterations and when to stop

### Takeaway
Empirical UX data suggests ~3 iterations until plateau (NN/g); Bayesian optimization stops at a max-iteration or satisfactory-level criterion and can reach near-optimal within ~5 queries in low-dimensional human-feedback settings; stopping should combine plateau detection with cost-benefit and risk thresholds.

### Cited Findings
- NN/g: median 3 iterations; usability plateaus; do not expect exponential improvements indefinitely — [NN/g](https://www.nngroup.com/articles/iterative-design).
- Midrocket: infinite iteration is counterproductive; diminishing returns — [Midrocket](https://midrocket.com/en/guides/iterative-design-process).
- Bayesian optimization stopping criterion: max number of iterations or satisfactory optimization level — [Serokell BO overview](https://serokell.io/blog/bayesian-optimization-algorithm).
- Kim et al. (2017): Bayesian optimization found a near-optimal parameter within five iterations for wearable device personalization with human feedback — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5604949).
- IxDF: halt when goals/user needs met, minor improvements only, or resources exhausted — [IxDF](https://ixdf.org/literature/topics/iterative-development).

### Inferences
- A practical default for the agentic CAD Review stage: cap at ~5 iterations, stop early if the user approves or if two consecutive rounds yield no change in approved elements; escalate only on ambiguity.

### Gaps
- No source gives an iteration count specifically for CAD generation with non-expert users; the ~3/~5 figures come from UI usability and hyperparameter-tuning domains.

## "Design by critique" and refinement from feedback

### Takeaway
"Design by critique" patterns treat feedback as first-class, localized, multi-solution artifacts (comments, sketches, revisions) that are converted into machine-learnable preference data or direct edits; critique should be grounded on the rendered result, support multiple alternative fixes, and close a feedback loop back into generation.

### Cited Findings
- Apple paper: designer-aligned interactions (commenting, sketching, revising) converted into preference pairs; critique on the rendered UI outperforms rubric-based ranking; "agreeing to disagree" supports multiple fixes — [arXiv 2509.16779](https://arxiv.org/abs/2509.16779).
- UICrit (Duan et al., UIST 2024): dataset and methods for automated design evaluation via UI critique; generating automatic feedback on UI mockups with LLMs — cited in [Apple paper](https://arxiv.org/abs/2509.16779) (Duan et al. 2024a/b).
- Duan et al. (CHI 2024) "Visual Prompting with Iterative Refinement for Design Critique Generation" — [arXiv 2412.16829](https://arxiv.org/abs/2412.16829).
- Hartmann et al. d.note: revising UIs via change tracking, annotations, and alternatives; Charrette (O'Leary et al.): feedback during design reviews; CrowdCrit (Luther et al.): crowdsourcing and aggregating visual design critique — cited in [Apple paper §2.3/1](https://arxiv.org/abs/2509.16779).
- Tampere University framework: LLM + CAD with image/voice input, generating CAD code, with a closed feedback loop refining iteratively until user specs met; targets non-professionals — [Tampere research portal](https://researchportal.tuni.fi/en/publications/generative-ai-meets-cad-enhancing-engineering-design-to-manufactu).
- AI-for-design review (Shi et al., CSCW 2023, 93 papers): AI assists refining drafts through iterations; refinement communicates professional treatment of visuals — [Shi PDF](https://xiaoyangtao.github.io/assets/pubs/2023CSCW_AI4Design_Shi.pdf).

### Inferences
- Apply the Apple pattern to CAD: render the generated model, let the user sketch/annotate or comment on the render, then have the agent apply the fix and re-render; keep the critique grounded on the visual rather than on CAD parameters.
- Support multiple alternative fixes per critique (agree to disagree) so the agent can propose variants instead of a single re-generation.

### Gaps
- I found no CAD-specific "design by critique" dataset or benchmark analogous to UICrit; transfer from UI critique research is by analogy.