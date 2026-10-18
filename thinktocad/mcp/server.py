"""ThinkToCad MCP server - the knowledge / contract / memory layer.

Run: ``thinktocad-mcp`` (stdio) or ``python -m thinktocad.mcp.server``.

This server exposes only the *domain* layer: knowledge retrieval, contract handling,
the DFM gate, and memory write-back. Geometry, verification and simulation are provided
by the external MCP servers (``build123d-mcp``, ``freecad-mcp``, ``matlab-mcp``) - see
``reports/Agentic CAD tooling landscape.md``. Keeping the tool surfaces non-overlapping
avoids tool-selection errors (``guides/AI_AGENT_TOOLKIT_GUIDE.md`` section 2).
"""
from __future__ import annotations

from typing import Any

from ..tools.registry import REGISTRY

# Importing the tool modules runs their @safe_tool registrations.
from ..tools import contracts, knowledge, verification  # noqa: F401

INSTRUCTIONS = (
    "ThinkToCad: knowledge-guided CAD design. Exposes the engineering knowledge base, "
    "contract handling, the DFM gate, and design memory. Use the external MCP servers "
    "(build123d-mcp, freecad-mcp, matlab-mcp) for geometry, verification and simulation. "
    "The kernel is the referee - never declare a part valid yourself."
)


def build_server() -> Any:
    """Build the FastMCP server from the tool registry."""
    from fastmcp import FastMCP

    mcp = FastMCP("thinktocad", instructions=INSTRUCTIONS)
    for tool in REGISTRY.tools():
        mcp.add_tool(tool.handler)
    return mcp


def main() -> None:
    build_server().run()


if __name__ == "__main__":
    main()
