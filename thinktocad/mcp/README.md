# ThinkToCad MCP server

`thinktocad-mcp` is the **domain layer** of ThinkToCad: knowledge, contracts, DFM,
flow gates, visual check, and design memory. It is the only in-repo MCP server.

Geometry, verification and simulation are **external MCP servers**, kept separate so
the tool surfaces do not overlap:

| Server | Responsibility |
|--------|----------------|
| `build123d-mcp` | Create geometry from Python code (subprocess); returns step/stl paths + validity. |
| `freecad-mcp` | Verify geometry: mass, CG, interference, clearance, watertight, render preview. |
| `matlab-mcp` / `matlab -batch` | Run simulation scripts; return PASS/FAIL gates and numbers. |

Run the domain server with the `thinktocad-mcp` console script or
`python -m thinktocad.mcp.server`.

## Tool contract

Every tool returns a structured envelope and never raises into the agent loop:

```
{"ok": bool, "data": {...}, "error": {"code", "message", "retryable", "suggested_fix"}}
```

See `thinktocad/tools/errors.py` for the error taxonomy.

## Status

Fully implemented (13 tools). 87 tests, CI, ruff, eval harness.
