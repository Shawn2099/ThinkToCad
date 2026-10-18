# MCP and CAD Tooling Landscape

## Geometry kernels: build123d, CadQuery, OCCT/OCP bindings

### Takeaway
build123d and CadQuery are both mature, Apache-2.0 licensed Python BREP frameworks built on the Open Cascade (OCCT) kernel. build123d is the newer, more Pythonic refactor; CadQuery is the older, larger community project. Both have working MCP servers or the building blocks for one.

### Cited Findings

- **build123d** (v0.13.0, released Sep 21 2026) is a pure-Python parametric BREP modeling framework built on Open Cascade. License: Apache-2.0. Python support: 3.11–3.14. API surface: dual interface — Algebra Mode (stateless, operator-driven: `obj += sub_obj`, `Plane.XZ * Rectangle(...)`) and Builder Mode (`with BuildPart() as p:` context-based). Supports 1D/2D/3D shape classes, selectors with filtering/sorting/grouping, export to STEP/STL/SVG/DXF, import from STEP/SVG. PyPI package: `build123d`. — [PyPI build123d](https://pypi.org/project/build123d/); [GitHub gumyr/build123d](https://github.com/gumyr/build123d)

- **CadQuery** (v2.8.0, released Jun 21 2026) is a Python parametric CAD scripting framework based on OCCT. License: Apache-2.0. Python support: PyPI metadata says >=3.11; the README states pip wheels support Python 3.9–3.12 (conflicting — PyPI `Requires: >=3.11` is authoritative for the current release). API: fluent/chain-based (`cq.Workplane("XY").box(1,1,1).edges("|Z").fillet(0.1)`), `cadquery.occ_impl.shapes` for lower-level BREP. Built-in visualization via trame + vtk (`cadquery.vis.show`). Export: STEP, DXF, STL, VRML, AMF, 3MF. Stars: 6.0k on GitHub. Development Status classifier: 5 – Production/Stable. — [PyPI cadquery](https://pypi.org/project/cadquery/); [GitHub CadQuery/cadquery](https://github.com/CadQuery/cadquery)

- **cadquery-ocp (OCP)** (v8.0.1.1.0, released Oct 5 2026) is the official Python wrapper for Open CASCADE Technology, generated using pywrap. License: Apache-2.0. Python: 3.11–3.14. Provides thin bindings to all OCCT modules. Binary wheels are 47–68 MB per platform. Typing stubs available separately as `cadquery-ocp-stubs`. This is the low-level kernel layer that both CadQuery and (indirectly) build123d build upon. — [PyPI cadquery-ocp](https://pypi.org/project/cadquery-ocp/); [GitHub CadQuery/OCP](https://github.com/CadQuery/OCP)

- **build123d is derived from CadQuery** but extensively refactored into an independent framework. The two projects share conceptual DNA but have diverged APIs. — [PyPI build123d](https://pypi.org/project/build123d/)

### Inferences
- Both frameworks use the same OCCT kernel underneath, so geometry quality and BREP capabilities are equivalent at the kernel level.
- build123d's dual-mode API (algebraic + builder) is more flexible for LLM-generated code because the algebraic mode is more composable and stateless.
- CadQuery's larger community (6.0k vs ~100 stars for build123d) means more examples, Stack Overflow answers, and third-party integrations.
- Neither framework has a "hard" dependency on the other; they can coexist but share the OCP kernel.

### Gaps
- No independent benchmark comparing build123d vs CadQuery for LLM-generated CAD code quality was found in this research.

---

## MCP servers for build123d

### Takeaway
A production-ready MCP server for build123d exists (`build123d-mcp` by pzfreo, Apache-2.0), with tools for code execution, rendering, measurement, validation, and multi-format export. It is the most complete build123d MCP server found.

### Cited Findings

- **build123d-mcp** (pzfreo) — "MCP server for build123d to improve AI cognition when creating 3D CAD models." License: Apache-2.0. Stars: 117. Forks: 15. Python: 3.11–3.14. Install: `uv tool run --python 3.12 build123d-mcp@latest`. PyPI: `build123d-mcp`. Listed on MCP Registry. — [GitHub pzfreo/build123d-mcp](https://github.com/pzfreo/build123d-mcp); [PyPI build123d-mcp](https://pypi.org/project/build123d-mcp/)

- **API surface / tools**: execute build123d code in a persistent CAD session; render PNG/SVG/DXF previews; measure volume/area/bounding boxes/topology/centers of mass; find holes/bosses/countersinks/hole patterns; check printability, fit/alignment comparisons, export validity; import STEP/STL for comparison; export STEP/STL/DXF/SVG; save/restore session snapshots; produce 2D engineering drawing previews; `install_skill` for workflow guidance (modeling/drawing/repair). — [GitHub pzfreo/build123d-mcp](https://github.com/pzfreo/build123d-mcp)

- **HTTP mode** available: `--transport http --host 127.0.0.1 --port 8000` (no built-in auth; single shared session unless host provides per-request middleware). — [GitHub pzfreo/build123d-mcp](https://github.com/pzfreo/build123d-mcp)

- **Benchmark claim**: On the public CADGenBench leaderboard (June 2026), using build123d-mcp raised the same model's score from 0.360 to 0.457 and CAD validity from 88% to 100%. — [GitHub pzfreo/build123d-mcp](https://github.com/pzfreo/build123d-mcp)

- **No other build123d MCP servers** were found in the GitHub search or MCP Registry with comparable functionality.

### Inferences
- build123d-mcp is the de facto standard MCP server for build123d and is production-ready for local stdio use.
- The server's `execute` tool runs arbitrary build123d code in a subprocess — this is the primary integration pattern (LLM writes code → server executes → returns result + render).
- The CADGenBench results suggest measurable quality improvement when an LLM uses iterative build-execute-render loops vs one-shot code generation.

### Gaps
- The CADGenBench leaderboard claim is self-reported by the build123d-mcp author; no independent verification was found.

---

## FreeCAD MCP servers

### Takeaway
Multiple FreeCAD MCP servers exist (183 GitHub repos match "freecad mcp"). The most popular is `neka-nat/freecad-mcp` (2.9k stars, MIT), which provides a two-component architecture (in-FreeCAD addon + external MCP server) with tools for model creation/editing, Python script execution, document inspection, and FEM analysis.

### Cited Findings

- **neka-nat/freecad-mcp** — "FreeCAD MCP (Model Context Protocol) server." License: MIT. Stars: 2.9k. Forks: 353. Python. Updated within days of research date. Architecture: two components — an addon running inside FreeCAD (RPC server) and an MCP server launched by the client. Install: `uvx freecad-mcp`. Tools include: create/edit models, run Python scripts, inspect documents, run FEM analyses. — [GitHub neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp)

- **spkane/freecad-addon-robust-mcp-server** — "The FreeCAD Robust MCP server and MCP Bridge Workbench/Addon." Stars: 257. Python. — [GitHub](https://github.com/spkane/freecad-addon-robust-mcp-server)

- **ghbalf/freecad-ai** — "AI-powered assistant workbench for FreeCAD — generate 3D models from natural language." Stars: 577. Python. Updated 2 days ago. — [GitHub](https://github.com/ghbalf/freecad-ai)

- **bonninr/freecad_mcp** — "FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor." Stars: 228. Python. Last updated Mar 2025. — [GitHub](https://github.com/bonninr/freecad_mcp)

- **contextform/freecad-mcp** — "Open-source Model Context Protocol server for FreeCAD automation." Stars: 136. Python. Last updated Aug 2025. — [GitHub](https://github.com/contextform/freecad-mcp)

- **blwfish/freecad-mcp** — "MCP server for FreeCAD — 32 tools for AI-assisted 3D CAD modeling." Stars: 60. Updated 20 hours ago. — [GitHub](https://github.com/blwfish/freecad-mcp)

- FreeCAD itself is licensed LGPL-2.1+ (the application); the MCP servers listed above are MIT or similarly permissive.

### Inferences
- The FreeCAD MCP ecosystem is fragmented: at least 9 distinct servers exist with overlapping functionality, indicating no single standard has emerged.
- neka-nat/freecad-mcp's 2.9k stars and active development make it the de facto leader.
- FreeCAD MCP servers generally provide: document inspection, Python code execution inside FreeCAD, model creation/editing via FreeCAD's API, export to STEP/STL. FEM analysis is mentioned for neka-nat's server.
- FreeCAD's GUI-centric architecture means most MCP servers require a running FreeCAD instance (with RPC server addon), unlike build123d-mcp which runs headless.
- TechDraw 2D drawing generation, mass properties, and interference/clash detection are available through FreeCAD's Python API (Part.getMass(), Part.distToShape(), TechDraw module) but specific MCP tool exposure varies by server.

### Gaps
- Detailed tool-by-tool comparison across all FreeCAD MCP servers was not feasible within this research scope; the list above is a survey, not a deep comparison.
- No FreeCAD MCP server explicitly advertises "interference/clash detection" or "min clearance" as a named tool in their README; these would need to be composed from FreeCAD's lower-level API (e.g., `Part.Shape.common()`, `Part.Shape.distToShape()`).

---

## MATLAB MCP servers

### Takeaway
MathWorks ships an official MATLAB MCP Server (`matlab/matlab-mcp-server`, 1.7k stars, Go binary) with tools for code execution, static analysis, test running, and session management. It requires a MATLAB license (R2021a+) and is governed by the MathWorks Software License Agreement. Several community alternatives exist but are far less mature.

### Cited Findings

- **matlab/matlab-mcp-server** (official MathWorks) — "Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®." Language: Go (compiled binary). Stars: 1.7k. Forks: 151. License: MathWorks proprietary (see LICENSE.md in repo). Requires MATLAB R2021a+ on system PATH. — [GitHub matlab/matlab-mcp-server](https://github.com/matlab/matlab-mcp-server)

- **Tools**: `detect_matlab_toolboxes` (list installed toolboxes + versions); `check_matlab_code` (static analysis: style, errors, deprecated functions, performance); `evaluate_matlab_code` (execute code string, return output); `run_matlab_file` (execute .m or .p file); `run_matlab_test_file` (execute MATLAB unit tests). — [GitHub matlab/matlab-mcp-server](https://github.com/matlab/matlab-mcp-server)

- **Resources**: `matlab_coding_guidelines` (coding standards), `plain_text_live_code_guidelines` (Live Script format rules). — [GitHub matlab/matlab-mcp-server](https://github.com/matlab/matlab-mcp-server)

- **Session modes**: `new` (start new MATLAB), `auto` (connect to existing or start new), `existing` (connect to shared session via `shareMATLABSession()`). Desktop or nodesktop display modes. — [GitHub matlab/matlab-mcp-server](https://github.com/matlab/matlab-mcp-server)

- **Licensing constraint**: "MCP servers are only permitted to be used with MATLAB in accordance with the MathWorks Software License Agreement, and must not be shared by multiple users. Contact MathWorks if you need to support shared or centralized server use." — [GitHub matlab/matlab-mcp-server](https://github.com/matlab/matlab-mcp-server)

- **Community alternatives**: WilliamCloudQi/matlab-mcp-server (54 stars, JavaScript); Tsuchijo/matlab-mcp (40 stars, Python); jigarbhoye04/MatlabMCP (20 stars, Python, uses Matlab Engine API). All are experimental/low-maturity. — [GitHub search](https://github.com/search?q=matlab+mcp+server&type=repositories)

- **MATLAB Production Server MCP**: `matlab/mcp-framework-matlab-production-server` (34 stars) — publish MATLAB functions as MCP tools for AI agents using MATLAB Production Server. — [GitHub](https://github.com/matlab/mcp-framework-matlab-production-server)

### Inferences
- The official MathWorks server is production-ready but requires a MATLAB license and is proprietary.
- For a knowledge-guided CAD stack, the MATLAB server would handle simulation/analysis workflows (FEA post-processing, optimization, control system design), not geometry creation.
- Community MATLAB MCP servers are not production-ready; the official server is the only viable option for serious use.
- The "must not be shared by multiple users" licensing constraint means each developer/agent needs their own MATLAB license.

### Gaps
- No MATLAB MCP server provides CAD-specific tools (geometry, mass properties, interference); they are general MATLAB code execution wrappers.

---

## Validator, render, and mesh libraries

### Takeaway
For mesh validation (watertight checks, mass properties, boolean operations), **trimesh** (MIT, pure Python) is the primary tool. For 2D DXF drawings, **ezdxf** (MIT, Production/Stable) is the standard. For 3D rendering and visualization, **VTK** (BSD) and **Open3D** (MIT) are the main options. None of these have dedicated MCP servers; they are library-level dependencies that an MCP server would wrap.

### Cited Findings

- **trimesh** (v5.1.1, released Oct 2 2026) — pure Python 3.10+ library for loading, processing, analyzing, and viewing triangular meshes. License: MIT. Only hard dependency: numpy. Key capabilities: `mesh.is_watertight`, `mesh.euler_number`, `mesh.volume`, `mesh.center_mass`, `mesh.moment_inertia`, `mesh.convex_hull`, boolean operations (via Manifold3D or Blender), ray-mesh queries, mesh repair (winding, normals, holes), slicing, voxelization, Laplacian smoothing, minimum-volume oriented bounding boxes. Import: STL/OBJ/PLY/GLTF/GLB/3MF/OFF. Export: STL/PLY/OBJ/GLB/GLTF/COLLADA. Development Status: 4 – Beta. — [PyPI trimesh](https://pypi.org/project/trimesh/); [GitHub mikedh/trimesh](https://github.com/mikedh/trimesh)

- **ezdxf** (v1.4.5, released Oct 16 2026) — Python package to create/manipulate DXF drawings. License: MIT. Python: >=3.10. Development Status: 5 – Production/Stable. Read/write DXF versions R12–R2018. `drawing` add-on provides interfaces to matplotlib (PNG/PDF/SVG export) and PyQt5. Optional C extensions included in binary wheels. CLI: `ezdxf draw -o file.png file.dxf`. — [PyPI ezdxf](https://pypi.org/project/ezdxf/); [GitHub mozman/ezdxf](https://github.com/mozman/ezdxf)

- **Open3D** (v0.20.0, released Sep 16 2026) — open-source library for 3D data processing. License: MIT. Python: >=3.10. Development Status classifier: 3 – Alpha (note: this seems stale/misleading; Open3D is widely used in production since 2018, but the PyPI classifier says Alpha). Capabilities: 3D data structures, scene reconstruction, surface alignment, 3D visualization, PBR rendering, GPU acceleration, ML support (PyTorch/TensorFlow). C++ backend with Python frontend. Wheels are 48–400 MB. — [PyPI open3d](https://pypi.org/project/open3d/); [GitHub isl-org/Open3D](https://github.com/isl-org/Open3D)

- **VTK** (v9.7.1, released Sep 28 2026) — open-source toolkit for 3D computer graphics, image processing, and visualization. License: BSD 3-clause. Python: >=3.10. Mature (initial release 1994). Used by academia, government labs (Los Alamos), and commercial firms. Capabilities: surface reconstruction, implicit modeling, decimation, hardware-accelerated volume rendering, LOD control. — [PyPI vtk](https://pypi.org/project/vtk/)

- **Watertight/interference/clearance checking**: No dedicated standalone library was found. These capabilities are distributed across:
  - trimesh: `is_watertight`, `is_volume`, boolean ops via Manifold3D
  - OCP/cadquery-ocp: `BRepAlgoAPI_Common` (intersection), `BRepAlgoAPI_Cut` (difference), `ShapeAnalysis` classes for clearance
  - FreeCAD: `Part.Shape.common()`, `Part.Shape.distToShape()`, `Part.getMass()`
  - build123d: `Shape.is_valid()`, volume/area via `Shape.volume` / `Shape.area`

### Inferences
- trimesh is the natural choice for mesh-level validation in an LLM-generated CAD pipeline because it is pure Python (easy install), MIT licensed (no commercial restrictions), and has explicit watertight/volume/inertia checks.
- ezdxf is the standard for 2D drawing export and is Production/Stable.
- VTK and Open3D are rendering/visualization backends; VTK is more mature and commercially battle-tested, Open3D has better Python ergonomics and ML integration.
- For interference/clash detection and min clearance, there is no off-the-shelf MCP tool — this would need to be built on top of OCP's `BRepAlgoAPI` boolean operations or trimesh's Manifold3D booleans.
- An MCP server wrapping trimesh + ezdxf for mesh validation and 2D drawing export would need to be written; no such server was found in this research.

### Gaps
- No dedicated "CAD validator MCP server" exists that wraps trimesh/ezdxf/OCP validation behind a single MCP interface.
- Open3D's PyPI Development Status classifier (Alpha) appears inconsistent with its real-world adoption; this may be a metadata issue.

---

## Production-ready vs experimental summary

### Production-ready (suitable for commercial/open-source reuse)

| Item | License | Maturity | MCP server exists? |
|------|---------|----------|-------------------|
| build123d | Apache-2.0 | Active, monthly releases | Yes — `build123d-mcp` (Apache-2.0) |
| CadQuery | Apache-2.0 | 5 – Production/Stable | No dedicated MCP server found |
| cadquery-ocp (OCP) | Apache-2.0 | Active, tracks OCCT releases | No (library only) |
| trimesh | MIT | 4 – Beta | No (library only) |
| ezdxf | MIT | 5 – Production/Stable | No (library only) |
| VTK | BSD 3-clause | Very mature (since 1994) | No (library only) |
| FreeCAD MCP (neka-nat) | MIT | 2.9k stars, very active | Yes |
| MATLAB MCP (MathWorks) | Proprietary | Official, 1.7k stars | Yes — requires MATLAB license |

### Experimental / community / low-maturity

| Item | License | Notes |
|------|---------|-------|
| Open3D | MIT | PyPI says Alpha; widely used but large wheels |
| build123d-mcp | Apache-2.0 | 117 stars; production-ready but small community |
| Community FreeCAD MCP servers | Various | 9+ competing servers, fragmented |
| Community MATLAB MCP servers | Various | 20–54 stars, not production-ready |

### Licensing constraints for commercial reuse

- **Apache-2.0** (build123d, CadQuery, OCP): Permissive; allows commercial use, modification, distribution; requires attribution and notice of changes. No copyleft.
- **MIT** (trimesh, ezdxf, neka-nat/freecad-mcp): Permissive; allows commercial use; requires attribution only. No copyleft.
- **BSD 3-clause** (VTK): Permissive; allows commercial use; requires attribution and non-endorsement. No copyleft.
- **MathWorks proprietary** (matlab-mcp-server): Requires MATLAB license; "must not be shared by multiple users" — each agent/developer needs their own license.
- **FreeCAD itself**: LGPL-2.1+ — but this applies to FreeCAD the application, not to the MIT-licensed MCP servers that talk to it.
