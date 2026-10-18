# AGENTS.md

ThinkToCad — a knowledge/skill + MCP-server bundle for **knowledge-guided agentic
mechanical CAD**. The repo is mostly curated engineering knowledge (markdown/YAML)
plus a thin, partly-stubbed Python skeleton. A capability described in the docs is
not necessarily implemented — check the code before relying on it.

## Repo shape (the layout block in `README.md` is aspirational and misleading)

- `thinktocad/` is the installable Python package: `flow.py` (stages + gates),
  `tools/` (registry, execution pipeline, domain tools), `runtime/` (ReAct loop,
  visual checks, `design_agent`), `mcp/server.py`, `evals/`, `scripts/`.
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
- `python -m thinktocad.runtime.design_agent <contract_name>` — prints the contract and
  the registered tools. The loop takes an injected model: `design(name, model_fn)`.
- `thinktocad-install-skill` — copies root `SKILLS.md` + `skills/` + `knowledge/` +
  `contracts/` into `~/.claude/skills/thinktocad`.
- `thinktocad-mcp` — the product MCP server (knowledge / contracts / DFM gate / flow
  gates / memory), also `python -m thinktocad.mcp.server`. Exposes the **domain layer
  only** — geometry/verify/sim come from the external `build123d-mcp` / `freecad-mcp` /
  `matlab-mcp` servers (pzfreo, neka-nat, MathWorks).
- `thinktocad-init --client opencode|vscode|claude|cursor` — writes/merges the MCP config.
- `python -m thinktocad.evals.tasks` — the deterministic domain eval suite (CI gates on it).
- Windows (this environment): the README's `&` background syntax is Unix-only —
  drop it or use `Start-Process`.

## What works

- The full domain tool layer (`thinktocad/tools/`) — canonical registry, structured
  envelopes, the execution pipeline (policy, guardrails, retry, circuit breaker, spans),
  and tools: `list_mechanisms`, `retrieve_knowledge`, `get_contract`, `check_contract`,
  `dfm_check`, `check_gate`, `save_attempt`, `save_lesson`.
- The design flow + gates (`thinktocad/flow.py`); the ReAct loop
  (`thinktocad/runtime/loop.py`, model injected); visual-check helpers
  (`thinktocad/runtime/visual.py`); the eval harness + tool simulator (`thinktocad/evals/`).
- Geometry/verify/sim are **not** implemented here — use the external MCP servers.
- Tests: `tests/` (`pytest -q`); CI in `.github/workflows/ci.yml`; lint config `[tool.ruff]`.

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
