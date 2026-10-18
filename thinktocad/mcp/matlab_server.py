"""ThinkToCad MCP server: MATLAB simulation gates.

Run: python -m mcp.matlab_server   (or `matlab-mcp` after pip install)
"""
from __future__ import annotations

try:
    from fastmcp import FastMCP
except ImportError:  # pragma: no cover
    FastMCP = None

mcp = FastMCP("thinktocad-matlab") if FastMCP else None


def _not_impl(name: str) -> dict:
    return {"ok": False, "error": f"{name}: not implemented", "data": None}


if mcp is not None:
    @mcp.tool()
    def run_sim(script_path: str) -> dict:
        """Run a MATLAB sim script. Returns {ok, gates: {name: PASS/FAIL}, fails}."""
        return _not_impl("run_sim")

    @mcp.tool()
    def run_gate(script_path: str, gate_name: str) -> dict:
        """Run a single named gate from a sim script."""
        return _not_impl("run_gate")


def main() -> None:
    if mcp is None:
        raise SystemExit("fastmcp not installed. Run: pip install fastmcp")
    mcp.run()


if __name__ == "__main__":
    main()
