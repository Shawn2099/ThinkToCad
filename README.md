# ThinkToCad — Knowledge-Guided Agentic Design Toolkit

A CAD helping toolkit: **knowledge base + contracts + feedback loop + memory** wrapped
around an AI agent, with build123d / FreeCAD / MATLAB exposed as MCP tools. Packaged as
an **installable MCP server + agent skill**.

> The AI reasons. The tools judge. The memory learns. The user decides.

## Install (MCP server)

```bash
pip install -e .
thinktocad-mcp        # stdio MCP server: knowledge / contracts / DFM gate / memory
```

Register it in your agent's MCP config. **OpenCode** (`opencode.json`):

```json
{ "mcp": { "servers": { "thinktocad": {
  "type": "local", "timeout": { "startup": 180000 }, "command": ["thinktocad-mcp"] } } } }
```

**VS Code** (`.vscode/mcp.json`):

```json
{ "servers": { "thinktocad": { "type": "stdio", "command": "thinktocad-mcp" } } }
```

Geometry, verification and simulation come from the external MCP servers
(`build123d-mcp`, `freecad-mcp`, `matlab-mcp`) — ThinkToCad deliberately does not
duplicate them, so the tool surfaces never overlap.

Environment: `THINKTOCAD_ROOT` (repo root if not the cwd), `THINKTOCAD_POLICY=strict`
(ask before writes, deny code execution), `THINKTOCAD_TRACE=1` (record tool spans).

## Install (as a skill)

```bash
pip install -e .
thinktocad-install-skill     # copies SKILLS.md + skills/ + knowledge/ + contracts/
                             # into ~/.claude/skills/thinktocad/
```

## Layout

```
thinktocad/            # the installable Python package (the MCP server + tools)
├── paths.py           # repo-root discovery
├── tools/             # canonical tool contract + domain tools  (see tools/README.md)
├── mcp/server.py      # the `thinktocad-mcp` server
└── runtime/           # design_agent.py loop (skeleton)
knowledge/             # engineering brain: mechanisms, constraints, lessons, graph.yaml
contracts/             # per-design contracts (YAML) — copy _template.yaml
memory/                # per-design attempt history
skills/                # domain skill files (stale copy of root SKILLS.md)
specs/                 # frozen spec values
guides/                # pointer guides + the AI agent toolkit guide
research_notes/        # the research behind everything
reports/               # synthesized research reports
```

## Toolkit architecture

Every tool is a contract and returns a structured envelope; it never raises into the
loop. The execution pipeline (`thinktocad/tools/execution.py`):

```
policy -> cancellation -> input guardrails -> span
       -> circuit breaker -> retry + timeout -> fn
       -> output guardrails -> metrics -> envelope
```

```json
{"ok": true,  "data": {...}, "error": null}
{"ok": false, "data": null, "error": {"code": "...", "message": "...",
  "retryable": false, "suggested_fix": "...", "details": {}}}
```

Domain tools: `list_mechanisms`, `retrieve_knowledge`, `recall`, `get_contract`,
`check_contract`, `dfm_check`, `check_gate`, `get_manufacturing_profile`,
`save_manufacturing_profile`, `build_visual_check`, `record_visual_check`, `save_attempt`,
`save_lesson`.

### MCP surface

* **tools** — the domain tools above.
* **resources** — `thinktocad://skill`, `thinktocad://knowledge/mechanisms/{id}`,
  `thinktocad://knowledge/constraints/{name}`, `thinktocad://knowledge/lessons/{name}`,
  `thinktocad://knowledge/graph`, `thinktocad://contracts/{name}`.
* **prompts** — `design_flow`, `design_stage`, `dfm_rules` (slash-commands in the client).

`thinktocad-doctor` checks the repo layout and the external CAD backends. See
`guides/AI_AGENT_TOOLKIT_GUIDE.md` and `thinktocad/tools/README.md` for the module map.

## The flow

`Ideate → Research → Specify → Build → Validate → Review → Deliver → Learn`

Verification order: backend tools (build123d / FreeCAD / MATLAB via MCP) → VLM reads the
render → the user interacts in FreeCAD (final word). The kernel is the referee.

## What NOT to build

No new LLM, no new CAD kernel, no generic agent framework, no text-to-CAD generator.
The value is in the **knowledge packaging + feedback loop + memory**.

## Getting started

1. `WORKFLOW.md` — end-to-end process.
2. `SKILLS.md` — the agent skill (read first).
3. `guides/AI_AGENT_TOOLKIT_GUIDE.md` — how the toolkit is built.
4. `guides/MECHANISM_CATALOG.md`, `guides/DESIGN_TEXTBOOKS.md`,
   `guides/SENIOR_CAD_KNOWLEDGE.md`, `guides/CAD_PARTS_SOURCES.md` — domain guides.
5. Copy `contracts/_template.yaml` to `contracts/<name>.yaml`.
6. `pytest -q` — run the test suite.
