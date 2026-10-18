# Knowledge Base (the "engineering brain")

Three kinds of knowledge:

| Type | What it contains | Where |
|---|---|---|
| Declarative | Facts: stock sizes, material properties, standards | `mechanisms/`, `constraints/` |
| Procedural | How to do things: design steps, workflows | `graph.yaml`, `skills/` |
| Experiential | What worked/failed: lessons from past designs | `lessons/`, `memory/` |

Best structure: knowledge graph - entities connected by relationships
("requires", "conflicts with", "replaces"). See `graph.yaml`.

Populate `mechanisms/` and `constraints/` with one markdown file per entity.
Populate `lessons/` after every failed or successful design.
