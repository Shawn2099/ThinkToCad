"""ThinkToCad MCP server: FreeCAD verification (mass, interference, clearance, render).

Run: python -m mcp.freecad_server   (or `freecad-mcp` after pip install)
"""
from __future__ import annotations

try:
    from fastmcp import FastMCP
except ImportError:  # pragma: no cover
    FastMCP = None

mcp = FastMCP("thinktocad-freecad") if FastMCP else None


def _not_impl(name: str) -> dict:
    return {"ok": False, "error": f"{name}: not implemented", "data": None}


if mcp is not None:
    @mcp.tool()
    def mass_properties(step_path: str) -> dict:
        """Return mass, volume, center of gravity of a STEP file."""
        return _not_impl("mass_properties")

    @mcp.tool()
    def interference(a_path: str, b_path: str) -> dict:
        """Boolean intersection volume between two STEP files. 0 = no clash."""
        return _not_impl("interference")

    @mcp.tool()
    def min_clearance(a_path: str, b_path: str) -> dict:
        """Minimum distance between two bodies (mm)."""
        return _not_impl("min_clearance")

    @mcp.tool()
    def render_preview(step_path: str, views: str = "iso,front,top") -> dict:
        """Render a STEP file to PNG images (base64). For vision critique."""
        return _not_impl("render_preview")

    @mcp.tool()
    def check_watertight(stl_path: str) -> dict:
        """Check whether an STL mesh is closed/manifold."""
        return _not_impl("check_watertight")


def main() -> None:
    if mcp is None:
        raise SystemExit("fastmcp not installed. Run: pip install fastmcp")
    mcp.run()


if __name__ == "__main__":
    main()
