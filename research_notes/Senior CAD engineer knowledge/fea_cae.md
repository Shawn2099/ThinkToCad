# FEA/CAE for Mechanical Design — Dense Reference for an AI Design Assistant

## 1. Types of FEA

### Takeaway
FEA decomposes a continuum into elements and solves PDEs; choose the analysis type by the dominant physics (static vs. dynamic, linear vs. nonlinear, thermal, modal, buckling, contact). Linear static is the default first pass; add nonlinearities only when physics demand it.

### Cited Findings
- Linear static analysis assumes small displacements, linear elastic material, and loads proportional to displacement; it is the baseline for sizing and sanity checks — [GoEngineer](https://www.goengineer.com/blog/when-to-move-from-linear-to-nonlinear-finite-element-analysis); [Cadence](https://www.cadence.com/en_US/home/explore/what-is-finite-element-analysis-definition.html).
- Nonlinear FEA covers three sources: material nonlinearity (plasticity, hyperelasticity, creep), geometric nonlinearity (large deformation, NLGEOM), and contact/boundary nonlinearity; use a Static, General step for quasi-static plasticity/hyperelasticity, Riks/arc-length for instability/snap-through, and dynamic (implicit or explicit) for inertia or highly nonlinear contact — [GoEngineer](https://www.goengineer.com/blog/when-to-move-from-linear-to-nonlinear-finite-element-analysis).
- Dynamic steps are useful not only when mass/inertia matter but also for quasi-static problems where highly nonlinear behavior or complex contact prevents static convergence — [GoEngineer](https://www.goengineer.com/blog/when-to-move-from-linear-to-nonlinear-finite-element-analysis).
- Modal (natural frequency) analysis solves the eigenvalue problem (K, M) to give natural frequencies and mode shapes; typically no damping; used for vibration, resonance, NVH — [Czero Solutions](https://czero-solutions.com/finite-element-analysis).
- Linear (eigenvalue) buckling computes bifurcation loads from a reference load case; nonlinear buckling activates large deflection (NLGEOM,ON) and tracks the limit load with possible plasticity — [ANSYS Help](https://ansyshelp.ansys.com/public/views/secured/corp/v251/en/ans_str/Hlp_G_STR7_4.html).
- Buckling safety factors of ~3 are commonly applied in practice because linear eigenvalue buckling overpredicts; imperfection (perturbation) magnitude/location strongly affects limit load — [ANSYS tutorial (video)](https://www.youtube.com/watch?v=ZljfZ70toyY).
- Thermal analysis: steady/transient heat transfer; coupled (thermo-structural) and uncoupled; pure heat transfer; BCs include initial temperature, heat flux, temperature, body heat source — [FreeCAD FEM CalculiX](https://wiki.freecad.org/FEM_CalculiX); [FreeCAD Workbench](https://wiki.freecad.org/FEM_Workbench).
- Transient/dynamic: time-stepping with inertia and damping; implicit (unconditionally stable, larger steps) vs. explicit (conditionally stable, small steps, impact/crash) — [GoEngineer](https://www.goengineer.com/blog/when-to-move-from-linear-to-nonlinear-finite-element-analysis).
- Fatigue/durability: S-N / strain-life / fracture-mechanics approaches; often a separate post-processing (fe-safe) on stress results — [Czero Solutions](https://czero-solutions.com/finite-element-analysis); [Advanses](https://advanses.com/materials-testing-downloads).

### Inferences
- Start with linear static for every new design; escalate to nonlinear only after identifying nonlinearity (plastic yielding, large deflection, contact, buckling) — inferred from [GoEngineer](https://www.goengineer.com/blog/when-to-move-from-linear-to-nonlinear-finite-element-analysis) and [Cadence](https://www.cadence.com/en_US/home/explore/what-is-finite-element-analysis-definition.html).

### Gaps
- No source found giving exact threshold criteria (e.g., "when strain > 5% use nonlinear") beyond general guidance; treat as engineering judgment.

## 2. Meshing: Element Types, Density, Refinement, Convergence, Quality

### Takeaway
Mesh choice dominates accuracy and cost: prefer hex/quads for regular solids and shells, use tets for complex geometry; refine only in high-gradient regions; verify mesh quality via aspect ratio, Jacobian, and scaled Jacobian; converge the mesh before trusting peak stresses.

### Cited Findings
- CalculiX/FreeCAD element library: 3D solid tet (C3D4, C3D10), hex (C3D8/R, C3D20/R), wedge (C3D6, C3D15); shell tri (S3, S6) and quad (S4/R, S8/R); membrane (M3D3/4/6/8); 2D plane stress/strain/axisymmetric (CPS/CPE/CAX3/6, CPS4/8...); beam/truss (B31/R, B32/R, T3D2/3) — [FreeCAD FEM CalculiX](https://wiki.freecad.org/FEM_CalculiX).
- FreeCAD meshers: Netgen or Gmsh; recommend mesh as last step due to geometry association; boundary-layer and region (localized) meshing available — [FreeCAD FEM tutorial](https://wiki.freecad.org/FEM_tutorial); [FreeCAD Workbench](https://wiki.freecad.org/FEM_Workbench).
- Shell elements should be used when width:thickness ratio > 10–20; quadrilateral shells preferred over triangles in bending (triangles are overly stiff) — [FEA Academy](https://www.fea-academy.com/index.php/component/content/article/27-blog/fea-generalities/72-good-modeling-practices).
- A large-scale 2022 comparison study (ACM TOG) compares tetrahedral vs. hexahedral elements for elliptic PDEs across beam bending/twisting, plane-with-hole, high aspect ratio, etc. — [ACM](https://dl.acm.org/doi/10.1145/3508372).
- Aspect ratio (ideal = 1): acceptable tet 1–3, hex 1–4, wedge 1–3, tri/quad 1–1.3 — [Sandia CUBIT tet](https://www.sandia.gov/files/cubit/15.4/help_manual/WebHelp/mesh_generation/mesh_quality_assessment/tetrahedral_metrics.htm); [Sandia CUBIT hex](https://www.sandia.gov/files/cubit/15.4/help_manual/WebHelp/mesh_generation/mesh_quality_assessment/hexahedral_metrics.htm); [Sandia CUBIT wedge](https://www.sandia.gov/files/cubit/15.4/help_manual/WebHelp/mesh_generation/mesh_quality_assessment/wedge_metrics.htm); [DIANA](https://manuals.dianafea.com/d110/en/1465843-1465936-mesh-quality-metrics.html).
- Jacobian (min pointwise volume): negative indicates inverted (invalid) element; scaled Jacobian acceptable tet 0.2–1, hex 0.5–1, wedge 0.5–1; distortion acceptable ≥0.5 (ideal 1) — [Sandia CUBIT](https://www.sandia.gov/files/cubit/15.4/help_manual/WebHelp/mesh_generation/mesh_quality_assessment/tetrahedral_metrics.htm); [DIANA](https://manuals.dianafea.com/d110/en/1465843-1465936-mesh-quality-metrics.html).
- ANSYS performs automatic element shape testing (aspect ratio, Jacobian ratio, warping factor) with default limits by element type; warping factor >0.1 can be problematic for flat-shell theory — [ANSYS Help](https://ansyshelp.ansys.com/public/views/secured/corp/v251/en/ans_thry/thy_et7.html).
- h-refinement: reduce element size; p-refinement: increase polynomial order; both drive discretization error down; displacement converges faster than stress — [EPJ convergence study](https://www.epj-conferences.org/articles/epjconf/pdf/2026/32/epjconf_icramen2026_03003.pdf).
- Meshing practice: run a coarse mesh first to identify critical regions, then refine locally; do not fine-mesh the whole model; check convergence by doubling density in critical regions until change <5% — [FEA Academy](https://www.fea-academy.com/index.php/component/content/article/27-blog/fea-generalities/72-good-modeling-practices); [Cadence](https://www.cadence.com/en_US/home/explore/what-is-finite-element-analysis-definition.html).

### Inferences
- For a build123d→FreeCAD pipeline: export STEP, import into FreeCAD, run Gmsh/Netgen with region refinement at holes/fillets; check tet aspect ratio ≤3 and scaled Jacobian ≥0.2 before solving.

### Gaps
- No single authoritative "acceptable" threshold across solvers; values above are from Sandia CUBIT/DIANA and may differ from FreeCAD/Gmsh defaults.

## 3. Boundary Conditions

### Takeaway
Boundary conditions are the #1 source of error: apply the minimum constraint needed for equilibrium, keep constraints away from regions of interest (Saint-Venant), and avoid point supports that create singularities.

### Cited Findings
- Fixed constraint: restrains all translational (and rotational for beams/shells) DOF; displacement BC allows selecting specific DOF and values (0 = fix, nonzero = enforced motion); rotations controllable only for shell/beam elements — [FreeCAD blog FEM](https://blog.freecad.org/2025/09/16/getting-started-with-fem); [FreeCAD Workbench](https://wiki.freecad.org/FEM_Workbench).
- Symmetry BC: zero normal displacement on the symmetry plane; cyclic symmetry models a sector with periodicity (low/high boundaries), requires cylindrical coordinate system and constraints to prevent rigid motion — [SimuTech cyclic symmetry](https://simutechgroup.com/cyclic-symmetry-considerations-in-ansys-workbench-mechanical); [SimScale forum](https://www.simscale.com/forum/t/setting-up-symmetry-boundary-conditions-and-circular-symmetry/37453).
- Remote loads: apply load at a remote point (e.g., bolted joint) transferred to a surface via rigid/beam coupling — [FEA Academy](https://www.fea-academy.com/index.php/component/content/article/27-blog/fea-generalities/72-good-modeling-practices).
- Bolt pretension: applied to cylindrical face/section cutting through the bolt; supports scoping to cylindrical face, straight edge, body, beam connection; can maintain initial adjustment across steps (connector motion) so clamping force evolves with external load — [ANSYS Help](https://ansyshelp.ansys.com/public/views/secured/corp/v251/en/wb_sim/ds_Pretension.html); [LearnFEA](https://learnfea.com/bolt-pre-tension-techniques-in-abaqus).
- Pressure: normal to surface; gravity/self-weight available for significant mass — [FreeCAD blog FEM](https://blog.freecad.org/2025/09/16/getting-started-with-fem).
- Thermal BCs/loads: initial temperature, heat flux, temperature, body heat source — [FreeCAD FEM CalculiX](https://wiki.freecad.org/FEM_CalculiX).
- Cylindrical coordinate systems allow BCs/loads in local coords; needed for cyclic symmetry and rotating parts — [FreeCAD blog FEM](https://blog.freecad.org/2025/09/16/getting-started-with-fem).
- Boundary conditions often generate singularities where a fixed constraint ends; spread constraints over a set of nodes/faces and keep them far from regions of interest — [Engineering.com](https://www.engineering.com/avoiding-singularities-in-fea-boundary-conditions); [FEA Academy](https://www.fea-academy.com/index.php/component/content/article/27-blog/fea-generalities/72-good-modeling-practices).
- Elastic (spring) supports can eliminate BC-edge singularities but stiffness must be realistic — [Engineering.com](https://www.engineering.com/avoiding-singularities-in-fea-boundary-conditions).

### Inferences
- For build123d/FreeCAD: prefer "Displacement BC" over "Fixed" when only partial constraint is physical; use symmetry to cut model size; verify equilibrium via reaction forces.

### Gaps
- No source found quantifying "how far" constraints must be from regions of interest beyond Saint-Venant's principle (typically several characteristic lengths).

## 4. Material Models

### Takeaway
Material model choice must match the strain regime: linear elastic for small strains; bilinear/multilinear elastoplastic for metals yielding; hyperelastic for rubbers; creep for high-temperature long-term; Johnson-Cook for rate/temperature-dependent metals.

### Cited Findings
- Linear elastic: E, Poisson's ratio, density; valid for small strains below yield — [SimScale](https://www.simscale.com/blog/guide-to-nonlinear-material-models).
- Plasticity: yield criterion typically von Mises; bilinear (E + tangent modulus ET ≈ 1% E) or multilinear hardening from true stress-strain; isotropic/kinematic hardening; engineering vs. true stress-strain diverge beyond ~5% strain — [SimScale](https://www.simscale.com/blog/guide-to-nonlinear-material-models); [MIT Bathe lecture (video)](https://www.youtube.com/watch?v=GpV_9EtObvs).
- Hyperelastic (rubber/elastomers): based on strain energy density functions; models include Mooney-Rivlin, Ogden, Yeoh, Arruda-Boyce, Marlow, polynomial, van der Waals; used for large, fully recoverable deformations — [Advanses](https://advanses.com/materials-testing-downloads); [CAEassistant](https://caeassistant.com/blog/hyperelastic-material-abaqus-model).
- Viscoelastic creep: time-dependent; Maxwell/Kelvin-Voigt for linear; Bailey-Norton and Findley for nonlinear long-term creep; hyperelastic + creep for rubber — [PART Engineering](https://www.partengineering.com/en/blog/simulation-of-the-long-term-behavior-of-plastic-components); [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6631056).
- Fatigue: high-cycle (S-N) and low-cycle (strain-life); dedicated tools (fe-safe); damage evolution — [Advanses](https://advanses.com/materials-testing-downloads); [SimScale](https://www.simscale.com/blog/guide-to-nonlinear-material-models).
- Rate/temperature-dependent metals: Johnson-Cook — [SimScale](https://www.simscale.com/blog/guide-to-nonlinear-material-models).
- SimScale (Code_Aster/Marc) supports: elastic-perfectly plastic, bilinear/multilinear hardening, Johnson-Cook — [SimScale](https://www.simscale.com/blog/guide-to-nonlinear-material-models).
- Abaqus hyperelastic library: Neo-Hooke, Mooney-Rivlin, Ogden, Yeoh, polynomial, van der Waals, Arruda-Boyce; custom via UHYPER — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6631056).

### Inferences
- For a steel bracket: linear elastic first; if peak von Mises exceeds yield, switch to multilinear elastoplastic and check residual deformation. For rubber seals: hyperelastic (Mooney-Rivlin or Ogden from test data), never linear elastic.

### Gaps
- No source found giving specific tangent-modulus percentages beyond "typically ~1% of E" (MIT lecture); material data must come from testing.

## 5. Contact

### Takeaway
Contact is a nonlinearity: pick the contact type that matches the physical joint (bonded for welds/glue, frictional for bolted/sliding, frictionless for lubricated, no-separation for guided sliding); control penetration via contact stiffness and verify convergence.

### Cited Findings
- Bonded (tied): surfaces permanently joined, no relative motion or separation; linear contact, fastest — [SDC Verifier](https://sdcverifier.com/structural-engineering-101/what-are-contact-conditions-in-fea-2); [LinkedIn/Adhikary](https://www.linkedin.com/posts/biplabradhikary_fea-contactmodeling-bondedcontact-activity-7375838227963834368-T6Jz).
- No separation: no penetration/separation but frictionless tangential sliding allowed — [SDC Verifier](https://sdcverifier.com/structural-engineering-101/what-are-contact-conditions-in-fea-2); [SimuTech](https://simutechgroup.com/resources/blog/understanding-contacts-in-ansys-mechanical).
- Frictionless: no penetration, zero friction (sliding free) — [SDC Verifier](https://sdcverifier.com/structural-engineering-101/what-are-contact-conditions-in-fea-2).
- Frictional: Coulomb model (static/dynamic/viscous friction); stick/slip — [LinkedIn/Adhikary](https://www.linkedin.com/posts/biplabradhikary_fea-contactmodeling-bondedcontact-activity-7375838227963834368-T6Jz); [UF MAE notes](https://web.mae.ufl.edu/nkim/egm6352/Chap5.pdf).
- Rough: infinite friction (no slip) but can separate — [YouTube feaClass](https://www.youtube.com/watch?v=VZDbIVqkuM8).
- Hard vs. soft contact: hard = no penetration (Lagrange multiplier); soft = small penetration with pressure-overclosure — [LinkedIn/Adhikary](https://www.linkedin.com/posts/biplabradhikary_fea-contactmodeling-bondedcontact-activity-7375838227963834368-T6Jz).
- Tie constraint: fully bonded, no sliding/separation; self-contact for folding; thermal contact transfers heat — [LinkedIn/Adhikary](https://www.linkedin.com/posts/biplabradhikary_fea-contactmodeling-bondedcontact-activity-7375838227963834368-T6Jz).
- Contact stiffness must be low enough for convergence and high enough to limit penetration to acceptable levels; penetration is the gap closure error — [MechSol](https://www.mechsol.com/blog/fea-in-depth-contact-stiffness-explained).
- Abaqus contact definitions: general contact (automated, expensive), contact pairs, contact elements (GAP*); self-contact and multibody in one definition — [Fidelis](https://www.fidelisfea.com/post/contact-in-fea-what-is-it-and-how-should-it-be-implemented).
- Ansys Mechanical offers bonded, frictional, no-separation, frictionless, etc. with contact formulation (pure penalty, augmented Lagrange, MPC) and detection (on gauss point, nodal) — [SimuTech](https://simutechgroup.com/resources/blog/understanding-contacts-in-ansys-mechanical).

### Inferences
- Ignoring contact (bonding everything) over-stiffens assemblies and under-predicts stresses in bolted joints; use frictional contact for bolted flanges and check bolt force/reaction.

### Gaps
- No source found giving numeric "acceptable penetration" thresholds; depends on characteristic length and solver.

## 6. Results Interpretation

### Takeaway
Use von Mises for ductile metals, max principal stress for brittle materials, displacement for stiffness/serviceability, strain for large-deformation elastomers, reaction forces for equilibrium checks; never read peak stress inside a singularity.

### Cited Findings
- Von Mises (equivalent) stress: predicts yielding of ductile materials; scalar combining normal and shear; yield when σ_vm ≥ σ_y — [SDC Verifier](https://sdcverifier.com/articles/what-is-von-mises-stress); [CAEassistant](https://caeassistant.com/blog/von-mises-stress-abaqus-mohrs-circle).
- Principal stress: max/min normal stress on planes with zero shear; governs brittle fracture and fatigue crack initiation; use for brittle materials (cast iron, glass, ceramics) — [SimScale](https://www.simscale.com/docs/simwiki/fea-finite-element-analysis/principal-stress-and-principal-strain); [LinkedIn/AESG](https://www.linkedin.com/posts/aesg_cae-mechanicalengineering-ansys-activity-7435359386899976192-nB1b).
- Safety factor FoS = σ_y / σ_vm (for ductile) or σ_ult/σ_max (for brittle); FoS>1 below yield; utilization = σ_vm/σ_allow ≤ 1 — [SDC Verifier](https://sdcverifier.com/articles/what-is-von-mises-stress).
- Displacement: deformation magnitude; used for stiffness, serviceability, clearance checks; not affected by stress singularities (displacements converge even where stress diverges) — [Autodesk Nastran](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Why-do-stress-keep-going-up-when-the-mesh-is-refined-in-Autodesk-Simulation-Mechanical.html).
- Strain: engineering/true strain; equivalent (von Mises) strain; relevant for elastomers, large deformation, fatigue strain-life — [SimScale](https://www.simscale.com/docs/simwiki/fea-finite-element-analysis/principal-stress-and-principal-strain); [DIANA](https://manuals.dianafea.com/d100/Theory/node117.html).
- Reaction forces: output at fixed/displacement BCs; check global equilibrium (ΣF = applied loads) — [FreeCAD FEM CalculiX](https://wiki.freecad.org/FEM_CalculiX).
- Von Mises is derived (distortion energy) and does not represent an actual stress component; principal stresses are actual tensor invariants — [SimScale](https://www.simscale.com/docs/simwiki/fea-finite-element-analysis/principal-stress-and-principal-strain).
- Post-processing: check unaveraged (element) stresses, not just nodal-averaged contours; verify coordinate system for components — [FEA Academy](https://www.fea-academy.com/index.php/component/content/article/27-blog/fea-generalities/72-good-modeling-practices).

### Inferences
- For a ductile steel part under static load: check max von Mises vs. yield with FoS ≥ 1.5–2 (application-dependent); for a cast-iron part: check max principal tensile vs. ultimate; for a rubber seal: check max strain vs. elongation limit.

### Gaps
- No source found giving universal FoS values; depend on code/standard and consequence of failure.

## 7. Mesh Convergence: Verification

### Takeaway
A mesh is "good enough" when a 3-level refinement study shows monotonic convergence with small GCI (typically <5%, ideally <2%) and the quantity of interest changes <5% when density doubles; always check the asymptotic range.

### Cited Findings
- Grid refinement ratio r = h_coarse/h_fine; recommended r ≥ 1.3 so differences are meaningful; r = 2 (halving mesh size) common — [GCI video](https://www.youtube.com/watch?v=F6DgY3Zs4i8); [NASA](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html).
- Observed order of convergence: p = ln(|ε_32/ε_21|)/ln(r), where ε_32 = φ_3−φ_2, ε_21 = φ_2−φ_1 (coarse→medium→fine) — [NASA](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html); [EPJ](https://www.epj-conferences.org/articles/epjconf/pdf/2026/32/epjconf_icramen2026_03003.pdf).
- Richardson extrapolation (continuum estimate): φ_ext = φ_fine + (φ_fine − φ_medium)/(r^p − 1) — [NASA](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html); [Matforge](https://matforge.org/mesh-quality-convergence-studies-guide-2).
- Grid Convergence Index: GCI = F_s |ε|/(r^p − 1); factor of safety F_s = 1.25 for 3-grid studies, 3.0 for 2-grid; small GCI = mesh-independent — [Volupe](https://volupe.com/support/grid-convergence-index-calculator); [NASA](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html).
- Convergence ratio R = ε_21/ε_32: monotonic convergence 0<R<1 (ideal), oscillatory convergence R<0, divergence R>1; Richardson extrapolation only valid for monotonic convergence — [Volupe](https://volupe.com/support/grid-convergence-index-calculator); [CFD university](https://cfd.university/blog/how-to-manage-uncertainty-in-cfd-the-grid-convergence-index).
- Asymptotic range check: ratio of successive GCIs ≈ 1 (or GCI_21/GCI_32 ≈ r^p) indicates the mesh is in the asymptotic range — [NASA](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html); [MACH-Aero](https://mdolab-mach-aero.readthedocs-hosted.com/en/latest/machAeroTutorials/airfoilanalysis_gridRefinementStudy.html).
- Discretization uncertainty of ~1.3% reported for a converged FEA study; displacement converges faster than stress — [EPJ](https://www.epj-conferences.org/articles/epjconf/pdf/2026/32/epjconf_icramen2026_03003.pdf).
- ASME V&V 20 standardizes GCI reporting for CFD; ASME V&V 10 for solid mechanics — [NAFEMS standards list](https://www.nafems.org/publications/standards/standards-a-e); [TrueFoundry skills](https://www.truefoundry.com/skills-registry/skill/HeshamFS-materials-simulation-skills-convergence-study).

### Inferences
- Practical rule: run coarse/medium/fine; if peak von Mises changes <5% from medium to fine and GCI <5%, accept the fine mesh; if a singularity is present, exclude it and converge a stress at a defined distance away.

### Gaps
- GCI originated in CFD (Roache 1994); its direct application to structural FEA with singularities/contacts is less standardized; ASME V&V 10 provides solid-mechanics guidance but no single numeric acceptance threshold.

## 8. Common Pitfalls

### Takeaway
The biggest FEA errors are not mesh-related but modeling-related: stress singularities, unrealistic BCs, unit inconsistency, and over-trusting peak stresses. Displacements converge; peak stresses at singularities do not.

### Cited Findings
- Stress singularities occur at sharp re-entrant corners, point loads, point supports, and abrupt BC changes; stress grows without bound as mesh refines; results never converge — [COMSOL](https://www.comsol.com/blogs/singularities-in-finite-element-models-dealing-with-red-spots); [Autodesk Nastran](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Why-do-stress-keep-going-up-when-the-mesh-is-refined-in-Autodesk-Simulation-Mechanical.html); [Enterfea](https://enterfea.com/stress-singularity-an-honest-discussion).
- Displacements are NOT affected by singularities; stress one or two elements away from the corner is more realistic — [Autodesk Nastran](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Why-do-stress-keep-going-up-when-the-mesh-is-refined-in-Autodesk-Simulation-Mechanical.html); [Fidelis](https://www.fidelisfea.com/post/stress-singularities-at-reentrant-corners-a-fundamental-problem-in-fea).
- Remedies: model a fillet/radius (converts singularity to stress concentration), spread point loads/BCs over an area, use pressure instead of point force, use plasticity, probe stress at a defined distance, use section forces, or ignore if far from region of interest — [COMSOL](https://www.comsol.com/blogs/singularities-in-finite-element-models-dealing-with-red-spots); [Fidelis](https://www.fidelisfea.com/post/stress-singularities-at-reentrant-corners-a-fundamental-problem-in-fea); [Engineering.com](https://www.engineering.com/avoiding-singularities-in-fea-boundary-conditions).
- Stress concentration (finite, converges) vs. stress singularity (infinite, diverges) — distinguish; Kt from Peterson/Roark for standard geometries — [Fidelis](https://www.fidelisfea.com/post/stress-singularities-at-reentrant-corners-a-fundamental-problem-in-fea); [Engineering SE](https://engineering.stackexchange.com/questions/65817/why-does-stress-at-a-re-entrant-corner-fail-to-converge-with-mesh-refinement-in).
- BC singularities: abrupt end of a fixed constraint acts like a sharp corner; use elastic supports or extend constraint — [Engineering.com](https://www.engineering.com/avoiding-singularities-in-fea-boundary-conditions).
- Unrealistic BCs: over-constraining (too rigid), wrong DOF, point supports; BCs are often the hardest part of setup — [FEA Academy](https://www.fea-academy.com/index.php/component/content/article/27-blog/fea-generalities/72-good-modeling-practices); [Engineering.com](https://www.engineering.com/avoiding-singularities-in-fea-boundary-conditions).
- Units: CalculiX is unitless; FreeCAD always writes SI(mm): length mm, force N, stress MPa (and mass in tonnes) — inconsistent units are a top error source — [FreeCAD FEM CalculiX](https://wiki.freecad.org/FEM_CalculiX); [FEA Academy](https://www.fea-academy.com/index.php/component/content/article/27-blog/fea-generalities/72-good-modeling-practices).
- Mesh too coarse: misses stress concentrations; too fine everywhere: wasted compute; use local refinement — [FEA Academy](https://www.fea-academy.com/index.php/component/content/article/27-blog/fea-generalities/72-good-modeling-practices).
- Ignoring contact: bonding everything over-stiffens; wrong contact type (e.g., bonded instead of frictional) changes load path — [Fidelis](https://www.fidelisfea.com/post/contact-in-fea-what-is-it-and-how-should-it-be-implemented).
- Other pitfalls: duplicate elements, incompatible elements, incorrect thickness/section, wrong coordinate system for post-processing, relying only on graphics, underestimating resources — [FEA Academy](https://www.fea-academy.com/index.php/component/content/article/27-blog/fea-generalities/72-good-modeling-practices).
- Nonlinear creep with singularity: high stress^power causes tiny time steps; enclose singularity in an elastic domain — [COMSOL](https://www.comsol.com/blogs/singularities-in-finite-element-models-dealing-with-red-spots).

### Inferences
- For an AI assistant: always flag peak stresses located at corners/constraints/point loads as suspect; recommend a fillet or a probe at a defined offset before reporting a number.

### Gaps
- No source found for a numeric "safe distance" from a singularity; rule of thumb "one or two elements away" from [Fidelis](https://www.fidelisfea.com/post/stress-singularities-at-reentrant-corners-a-fundamental-problem-in-fea).

## 9. FEA in the Design Loop: FEA vs. Hand Calculations

### Takeaway
Use hand calculations for simple, standard, transparent sizing and sanity checks; use FEA for complex geometry, stress concentrations, contact, nonlinearity, dynamic/modal behavior; best practice is a hybrid: hand calc first pass, FEA for critical details, hand calc to verify FEA.

### Cited Findings
- Hand calcs: fast (minutes), transparent assumptions, no software cost, adequate for simple/idealized problems; FEA: handles 3D stress concentrations, contact, nonlinearity, coupled physics, dynamic/modal — [Cadence](https://www.cadence.com/en_US/home/explore/what-is-finite-element-analysis-definition.html); [Panache](https://www.panacheg.com/blog/when-to-use-fea-vs-hand-calculations-structural-design); [ASRE](https://asrengineering.com/2019/04/02/fea-vs-hand-calculations/).
- FEA excels where closed-form fails: 3D stress concentration around holes/fillets, contact (friction, impact, sliding), material nonlinearity, coupled physics, dynamic behavior — [Cadence](https://www.cadence.com/en_US/home/explore/what-is-finite-element-analysis-definition.html).
- Decision criteria (Panache 7-question): stress concentrations/re-entrant corners/welded transitions → FEA solids with convergence; statically indeterminate or nonlinear (contact, gap, slip, buckling) → nonlinear FEA; non-building structures (tank, rack, vessel) → FEA for modal/impulsive; time-critical simple geometry → hand calc with conservative assumptions; client/AHJ requires PE-stamped FEA → FEA — [Panache](https://www.panacheg.com/blog/when-to-use-fea-vs-hand-calculations-structural-design).
- Hybrid workflow: hand calcs establish load path, member sizes, reactions first; FEA for critical details (weld peaks, gusset buckling, modal, nonlinear contact); hand checks validate FEA — [Panache](https://www.panacheg.com/blog/when-to-use-fea-vs-hand-calculations-structural-design); [ASRE](https://asrengineering.com/2019/04/02/fea-vs-hand-calculations/).
- Cost/time: hand calc few hours; mesh-converged PE-stamped FEA 8–16 hours base, scales with size/nonlinearity/load cases; FEA can be 3–5× hand-calc effort but often the only code-compliant path — [Panache](https://www.panacheg.com/blog/when-to-use-fea-vs-hand-calculations-structural-design).
- If hand calc and FEA disagree substantially, do not average; investigate assumptions — [Turn2Engineering](https://turn2engineering.com/mechanical-engineering/mechanical-design/stress-analysis).
- Validate FEA: compare hand calcs for simple cases (e.g., cantilever beam bending), physical prototype testing, mesh convergence — [Cadence](https://www.cadence.com/en_US/home/explore/what-is-finite-element-analysis-definition.html); [Autodesk](https://www.autodesk.com/solutions/simulation/finite-element-analysis).
- Roark's Formulas for Stress and Strain useful for validating FEA with closed-form solutions — [Eng-Tips](https://www.eng-tips.com/threads/fea-verification-with-hand-calculations.436985/).

### Inferences
- For build123d-generated parts: run a quick hand calc (σ = F/A, beam bending) to bound the FEA answer before trusting it; if FEA is >2× hand calc, suspect a singularity or BC error.

### Gaps
- No source found for a universal FoS or acceptable disagreement percentage between hand calc and FEA.

## 10. Software Landscape

### Takeaway
For the build123d/FreeCAD workflow, use FreeCAD FEM (CalculiX default) with Gmsh/Netgen; escalate to ANSYS/Abaqus for complex nonlinear/contact/fatigue; use Code_Aster (via SimScale) or Elmer for advanced multiphysics; all share the same fundamentals.

### Cited Findings
- FreeCAD FEM: default solver CalculiX (linear/nonlinear static, frequency, linear buckling, coupled/uncoupled thermal-structural, pure heat transfer, electrostatic); also Elmer, Z88, Mystran; meshers Netgen/Gmsh; SI(mm) units — [FreeCAD FEM CalculiX](https://wiki.freecad.org/FEM_CalculiX); [FreeCAD Workbench](https://wiki.freecad.org/FEM_Workbench); [FreeCAD install](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/FEM_Install.md).
- CalculiX: open-source (GPL) solver; input file text-based; supports beam/shell/solid elements; reduced integration benefits for slender shells/beams — [CalculiX manual](https://www.uni-kassel.de/its/files/its/2_IT-Dienste_Software/HPC/ccx_2.5.pdf).
- build123d exports STEP/STL/SVG; import STEP into FreeCAD for FEM; build123d-FreeCAD workbench converts OCP shapes to FreeCAD Part shapes — [build123d README](https://github.com/gumyr/build123d); [build123d-FreeCAD converter](https://raw.githubusercontent.com/jopdorp/build123d-freecad/main/b123d_cq_workbench/converter.py).
- ANSYS Mechanical: broad contact options, nonlinear, eigenvalue/nonlinear buckling, element shape checks; Workbench integration — [ANSYS Help](https://ansyshelp.ansys.com/public/views/secured/corp/v251/en/ans_str/Hlp_G_STR7_4.html); [SimuTech](https://simutechgroup.com/resources/blog/understanding-contacts-in-ansys-mechanical).
- ABAQUS: Standard (implicit) + Explicit; hyperelastic library; fe-safe fatigue; Tosca/Isight optimization; connector motion for bolt pretension — [GoEngineer](https://www.goengineer.com/blog/when-to-move-from-linear-to-nonlinear-finite-element-analysis); [LearnFEA](https://learnfea.com/bolt-pre-tension-techniques-in-abaqus).
- SolidWorks Simulation: integrated CAD, von Mises/principal stress, FoS plots, animation of deformation — [YouTube SolidWorks](https://www.youtube.com/watch?v=l-NcmulNao0).
- Fusion 360: cloud-based simulation (structural, thermal, modal) integrated with CAD.
- Code_Aster: open-source solver used by SimScale; nonlinear structural, thermal, contact — [SimScale](https://www.simscale.com/blog/guide-to-nonlinear-material-models).
- Elmer: open-source multiphysics (thermal, EM, fluid-structure) available in FreeCAD — [FreeCAD Workbench](https://wiki.freecad.org/FEM_Workbench).
- NAFEMS: industry association for simulation best practice; standards listing includes ASME V&V 10/20/40 — [NAFEMS](https://www.nafems.org/); [NAFEMS standards](https://www.nafems.org/publications/standards/standards-a-e).

### Inferences
- Recommended pipeline: build123d (Python) → export STEP → FreeCAD FEM (Gmsh mesh, CalculiX solve) → post-process in FreeCAD/ParaView; escalate to ANSYS/Abaqus only for nonlinear/contact/fatigue beyond CalculiX capability.

### Gaps
- FreeCAD FEM lacks some advanced features (e.g., full nonlinear contact robustness, fatigue) vs. commercial solvers; verify CalculiX version capabilities for your analysis type.

## 11. Verification & Validation (V&V)

### Takeaway
Verification (did we solve the equations right?) via mesh convergence and code checks; validation (did we solve the right equations?) via physical testing; ASME V&V 10/20/40 and NAFEMS provide the framework.

### Cited Findings
- ASME V&V 10-2006: Guide for Verification and Validation in Computational Solid Mechanics; V&V 10.1-2012: illustration; V&V 20-2009: CFD/heat transfer — [ASME/NAFEMS](https://www.nafems.org/publications/standards/standards-a-e); [ASME PDF](https://files.asme.org/Catalog/Codes/PrintBook/33929.pdf).
- ASME V&V 40-2018: Assessing Credibility of Computational Modeling through V&V, Application to Medical Devices; framework based on context of use and model risk; applicable beyond medical — [NAFEMS webinar](https://www.nafems.org/publications/resource_center/w_sep_21_global_2); [ASME V&V 40](https://event.asme.org/Events/media/library/resources/v-v/VVUQ-2022-VVUQ-40.pdf).
- NAFEMS offers V&V training and a simulation quality management framework; NAFEMS validation spectrum — [NAFEMS events](https://www.nafems.org/events/nafems/2024/verification-validation-in-engineering-simulation-americas-october24/).
- V&V distinguishes code verification (manufactured solutions), calculation verification (mesh convergence, iterative error), and validation (comparison to experiments) — [NAFEMS events](https://www.nafems.org/events/nafems/2026/verification-and-validation-in-engineering-simulation-online-01).
- NASA NTRS documents stresses at singularities can grow with mesh refinement rather than converge — [Turn2Engineering](https://turn2engineering.com/mechanical-engineering/mechanical-design/stress-analysis).

### Inferences
- For an AI assistant: always pair a simulation result with at least a mesh-convergence check (verification) and, where possible, a hand-calc or test comparison (validation).

### Gaps
- No source found detailing full V&V 40 implementation steps beyond framework overview; requires the standard document itself.

---

**Unverified items flagged:** universal FoS values, acceptable penetration thresholds, safe distance from singularities, and exact nonlinear-escalation strain thresholds are not sourced and require engineering judgment or the referenced standards.
