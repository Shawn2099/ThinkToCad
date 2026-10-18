# MCP servers for ThinkToCad

One FastMCP server per backend. Run with `python mcp/<name>_server.py`.

## Servers

- `build123d_server.py` — create geometry from Python code; returns step/stl paths + validity.
- `freecad_server.py` — verify geometry: mass, CG, interference, clearance, render preview.
- `matlab_server.py` — run sim scripts, return PASS/FAIL gates and numbers.

## Tool contract (all servers)

Each tool returns a structured dict:
```
{"ok": bool, "data": {...}, "error": str | None, "artifacts": [paths]}
```
Never raise into the agent loop; return ok=False with a readable error.

## Status

Skeleton only. Implement with `fastmcp` (pip install fastmcp).
See https://gofastmcp.com for the FastMCP API.
