"""ThinkToCad MCP server - the knowledge / contract / memory layer.

Run: ``thinktocad-mcp`` (stdio) or ``python -m thinktocad.mcp.server``.

The server exposes three MCP primitives:

* **tools** - the domain tool layer (knowledge, contracts, DFM gate, flow gates, memory);
* **resources** - the knowledge base and the agent skill as readable URIs;
* **prompts** - the design flow, stage guidance and DFM rules as slash-commands.

Geometry, verification and simulation are provided by the external MCP servers
(``build123d-mcp``, ``freecad-mcp``, ``matlab-mcp``) - see
``reports/Agentic CAD tooling landscape.md``. Keeping the tool surfaces non-overlapping
avoids tool-selection errors (``guides/AI_AGENT_TOOLKIT_GUIDE.md`` section 2).

Environment:
    THINKTOCAD_POLICY=strict  ask before writes; deny code execution
    THINKTOCAD_TRACE=1        record per-tool spans in memory (debugging)
"""
from __future__ import annotations

import os
from typing import Any

from ..tools import contracts, knowledge, verification  # noqa: F401  (registers tools)
from ..tools.execution import ExecutionContext
from ..tools.observability import RecordingTracer
from ..tools.policy import ToolPolicy
from ..tools.registry import REGISTRY, set_default_context

INSTRUCTIONS = (
    "ThinkToCad: knowledge-guided CAD design. Provides the engineering knowledge base, "
    "contract handling, the DFM gate, the design-flow gates, and design memory as tools; "
    "the knowledge base and skill as resources; and the design flow as prompts. Use the "
    "external MCP servers (build123d-mcp, freecad-mcp, matlab-mcp) for geometry, "
    "verification and simulation. The kernel is the referee - never declare a part valid "
    "yourself; the user has the final word."
)


def configure_context() -> ExecutionContext:
    """Build the execution context from the environment and install it globally."""
    policy = (
        ToolPolicy.strict()
        if os.environ.get("THINKTOCAD_POLICY", "").lower() == "strict"
        else None
    )
    context = ExecutionContext(policy=policy)
    if os.environ.get("THINKTOCAD_TRACE"):
        context.tracer = RecordingTracer()
    set_default_context(context)
    return context


def build_server() -> Any:
    """Build the FastMCP server: tools + resources + prompts."""
    from fastmcp import FastMCP

    from .prompts import register_prompts
    from .resources import register_resources

    configure_context()
    mcp = FastMCP("thinktocad", instructions=INSTRUCTIONS)
    for tool in REGISTRY.tools():
        mcp.add_tool(tool.handler)
    register_resources(mcp)
    register_prompts(mcp)
    return mcp


def main() -> None:
    build_server().run()


if __name__ == "__main__":
    main()
