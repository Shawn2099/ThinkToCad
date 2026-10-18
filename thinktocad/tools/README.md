# Validator / feedback tools

The "eyes" of the agent. Without these, the AI cannot self-correct.

- `render_preview.py` — render STEP/STL to PNG (isometric + orthographic) for vision critique.
- `check_watertight.py` — verify mesh is closed/manifold.
- `measure_mass.py` — mass, volume, CG from a STEP file.
- `check_interference.py` — boolean intersection volume between two parts.
- `check_clearance.py` — minimum distance between two bodies.

All tools: CLI-friendly, JSON output on stdout, non-zero exit on hard failure.
The agent calls them via MCP or as subprocesses and feeds results back into the loop.
