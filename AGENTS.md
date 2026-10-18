# AGENTS.md

ThinkToCad — a knowledge/skill + MCP-server bundle for **knowledge-guided agentic
mechanical CAD**. The repo is mostly curated engineering knowledge (markdown/YAML)
plus a thin, partly-stubbed Python skeleton. A capability described in the docs is
not necessarily implemented — check the code before relying on it.

## Repo shape (the layout block in `README.md` is aspirational and misleading)

- `thinktocad/` is **only** the installable Python package: `runtime/design_agent.py`,
  `mcp/*_server.py`, `scripts/install_skill.py`, `tools/` (README only, no code).
- Content lives at the repo root, **not** under `thinktocad/`: `knowledge/`,
  `contracts/`, `skills/`, `specs/`, `memory/`, `research_notes/`, `reports/`.
- Root guides: `WORKFLOW.md` (end-to-end process), `SKILLS.md` (agent skill),
  `guides/MECHANISM_CATALOG.md`, `guides/DESIGN_TEXTBOOKS.md`,
  `guides/SENIOR_CAD_KNOWLEDGE.md`, `guides/CAD_PARTS_SOURCES.md`,
  `guides/AI_CAD_RESEARCH_CATALOG.md`, `guides/AI_AGENT_TOOLKIT_GUIDE.md`,
  `KNOWLEDGE_AGENT.md`.
- `pyproject.toml` lists packages explicitly — a new subpackage under `thinktocad/`
  must be added to `[tool.setuptools] packages` or it will not install.

## Commands

- `pip install -e .` — core deps (pyyaml, fastmcp)
- `pip install -e .[cad]` — adds build123d + cadquery
- `pip install -e .[dev]` — adds pytest + ruff (tests live in `tests/`)
- `python -m thinktocad.runtime.design_agent <contract_name>` — loads
  `contracts/<name>.yaml`; the loop needs a `step_fn` that is not wired up yet.
- `thinktocad-install-skill` — copies root `SKILLS.md` + `skills/` + `knowledge/` +
  `contracts/` into `~/.claude/skills/thinktocad`.
- `thinktocad-mcp` — the product MCP server (knowledge / contracts / DFM gate / memory),
  also `python -m thinktocad.mcp.server`. Exposes the **domain layer only**.
- Legacy per-backend modules `thinktocad.mcp.build123d_server` / `freecad_server` /
  `matlab_server` exist but are **not** the product surface — geometry/verify/sim come
  from the external `build123d-mcp` / `freecad-mcp` / `matlab-mcp` servers (pzfreo,
  neka-nat, MathWorks). Declaring those names here would shadow those installs.
- Windows (this environment): the README's `&` background syntax is Unix-only —
  drop it or use `Start-Process`.

## What actually works vs. what is stubbed

- Works: the domain tool layer in `thinktocad/tools/` (canonical registry + structured
  envelopes + knowledge / contracts / DFM gate / memory), served by `thinktocad-mcp`;
  `build123d_server.create_part` and `validate_code`.
- Stubs: every tool in `freecad_server.py` and `matlab_server.py` returns
  `{"ok": False, "error": "... not implemented"}`; `design_agent._tool_validate`
  and `_tool_simulate` are TODOs.
- Tests live in `tests/` (`pytest -q`). No CI or lint config yet.

## Invariants (the "kernel is the referee" contract)

- The LLM never declares pass/fail: build123d executes, FreeCAD verifies, MATLAB
  simulates. Tools return structured errors as tool results and **never raise into
  the loop**.
- Every tool returns a structured dict (`{"ok", "data"/..., "error"}`); validation
  feedback is JSON, not prose.
- Units are mm internally; params are snake_case with a unit suffix (`length_mm`,
  `mass_kg`). One source of truth per dimension: contract → spec → code; never
  hard-code a dimension in CAD code.

## Conventions when editing content

- One design = one contract: copy `contracts/_template.yaml` →
  `contracts/<name>.yaml`. Every constraint is a number or stock size, no prose.
- Mechanisms: `knowledge/mechanisms/<snake_case_id>.md` with sections Type /
  Function / How it works / Constraints / Failure modes / When to use. Index rows in
  `guides/MECHANISM_CATALOG.md` (its count was stale — there are ~228 files).
  Relationships go in `knowledge/graph.yaml`.
- Constraints: `knowledge/constraints/*.md`. Lessons: `knowledge/lessons/`. Attempts:
  `memory/designs/<name>/attempt_N.yaml`.
- Knowledge write-back carries trust tiers T1–T4 (`WORKFLOW.md` stage 8); never
  silently overwrite a higher-trust entry with a lower-trust one.

## Gotchas

- `skills/SKILLS.md` is a stale, shorter copy; the maintained skill is the root
  `SKILLS.md` (the installer copies both). Edit the root one.
- `ROOT` is discovered by walking up for a `knowledge/` dir (`design_agent`) or
  `SKILLS.md` (`install_skill`) — moving those directories breaks path resolution.
- Git repo: remote `origin` → `https://github.com/Shawn2099/ThinkToCad.git`. `WORKFLOW.md`
  treats git commits as a deliverable and provenance mechanism.
- Docs reference `constraints/manufacturing_profile.md` and root-level `runtime/`,
  `mcp/`, `tools/`; the code dirs are under `thinktocad/`, and the manufacturing-profile
  file is a per-user artifact to be created, not present.
