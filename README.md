# ThinkToCad — Knowledge-Guided Agentic Design Toolkit

A general CAD helping toolkit: **knowledge base + contracts + feedback loop + memory**
wrapped around an AI agent, with MATLAB / FreeCAD / build123d exposed as MCP tools.
Packaged as an **installable skill + MCP server bundle**.

> The AI reasons. The tools judge. The memory learns.
> (See `KNOWLEDGE_AGENT.md` for the research basis.)

## Install (as a skill)

```bash
git clone <this-repo> thinktocad
cd thinktocad
pip install -e .
thinktocad-install-skill
```

This copies `SKILLS.md` + `skills/` + `knowledge/` + `contracts/` into
`~/.claude/skills/thinktocad/` so Claude Code / OpenCode pick it up automatically.
Restart your agent after installing.

## Install (MCP servers)

```bash
pip install -e .[cad]          # adds build123d
build123d-mcp &               # geometry creation
freecad-mcp &                 # verification
matlab-mcp &                  # simulation
```

Register them in your agent's MCP config (e.g. `opencode.json` or Claude's
`mcpServers`) pointing at the commands above.

## Layout

```
thinktocad/
├── SKILLS.md              # skill entry point (loaded by the agent)
├── skills/                # domain skill files
├── knowledge/             # engineering brain (mechanisms, constraints, lessons, graph)
├── contracts/             # per-design contracts (YAML)
├── memory/                # per-design attempt history + lessons
├── runtime/               # design_agent.py loop
├── mcp/                   # MCP servers (build123d, freecad, matlab)
├── tools/                 # validator/feedback tools
├── specs/                 # frozen spec values
├── scripts/               # install helpers
└── pyproject.toml
```

## The five stages

`Inspect → Specify → Build → Validate → Deliver`

## The runtime loop

`Spec → Build → Validate → Learn → Improve → Repeat`

The kernel is the referee: build123d executes, FreeCAD verifies, MATLAB simulates.
The LLM never decides if something works — the tools do.

## What NOT to build

No new LLM, no new CAD kernel, no generic agent framework, no text-to-CAD generator.
The value is in the **knowledge packaging**.

## Getting started

1. Read `WORKFLOW.md` (end-to-end process: Ideate -> Research -> Specify -> Build -> Validate -> Review -> Deliver).
2. Read `guides/DESIGN_TEXTBOOKS.md` (pointer guide: which book/standard owns each topic; 0-to-professional roadmap).
3. Read `guides/SENIOR_CAD_KNOWLEDGE.md` (senior-level design knowledge: GD&T, FEA, materials, assembly, drawing, surface finish, fasteners, power transmission, vibration, reliability, cost).
4. Read `guides/CAD_PARTS_SOURCES.md` (where to find pre-made CAD models, mechanisms, and parts).
5. Read `guides/AI_CAD_RESEARCH_CATALOG.md` (master index of ~170+ AI+CAD research papers, 2024-2026).
6. Read `guides/MECHANISM_CATALOG.md` (master index of ~228 mechanisms with selection guidance).
7. Read `guides/AI_AGENT_TOOLKIT_GUIDE.md` (how to build AI agent toolkits from OpenAI/Anthropic/Google patterns).
8. Read `skills/SKILLS.md`.
4. Read `knowledge/graph.yaml`.
4. Copy `contracts/_template.yaml` to `contracts/<name>.yaml`.
5. Run `python -m thinktocad.runtime.design_agent <name>` (skeleton — implement the loop).
6. Start an MCP server: `build123d-mcp` / `freecad-mcp` / `matlab-mcp`.
