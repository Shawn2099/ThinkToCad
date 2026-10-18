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

CLI::

    thinktocad-mcp [--root PATH] [--policy strict] [--trace]

``--root`` is the reliable way to point the server at a repo when the client's working
directory is not the repo (env ``THINKTOCAD_ROOT`` is the fallback).
"""
from __future__ import annotations

import argparse
import os
from typing import Any

INSTRUCTIONS = (
    "ThinkToCad: knowledge-guided CAD design. Provides the engineering knowledge base, "
    "contract handling, the DFM gate, the design-flow gates, and design memory as tools; "
    "the knowledge base and skill as resources; and the design flow as prompts. Use the "
    "external MCP servers (build123d-mcp, freecad-mcp, matlab-mcp) for geometry, "
    "verification and simulation. The kernel is the referee - never declare a part valid "
    "yourself; the user has the final word."
)


def _register_tools() -> None:
    # Importing the modules runs their @safe_tool registrations.
    from ..tools import contracts, knowledge, verification, visual  # noqa: F401


def configure_context(*, policy: str | None = None, trace: bool = False, ablation: set[str] | None = None) -> Any:
    """Build the execution context from arguments/environment and install it globally."""
    from ..tools.execution import ExecutionContext
    from ..tools.observability import RecordingTracer
    from ..tools.policy import ToolPolicy
    from ..tools.registry import set_default_context

    selected = (policy or os.environ.get("THINKTOCAD_POLICY") or "").lower()
    disabled = set(ablation or ())
    env_disabled = os.environ.get("THINKTOCAD_DISABLE", "")
    if env_disabled:
        disabled |= {item.strip() for item in env_disabled.split(",") if item.strip()}
    context = ExecutionContext(policy=ToolPolicy.strict() if selected == "strict" else None, disabled_tools=disabled)
    if trace or os.environ.get("THINKTOCAD_TRACE"):
        context.tracer = RecordingTracer()
    set_default_context(context)
    return context


def build_server(
    root: str | None = None, policy: str | None = None, trace: bool = False,
    ablation: set[str] | None = None,
) -> Any:
    """Build the FastMCP server: tools + resources + prompts."""
    if root:
        from .. import paths

        paths.set_root(root)

    _register_tools()
    configure_context(policy=policy, trace=trace, ablation=ablation)

    from fastmcp import FastMCP
    from fastmcp.tools import Tool
    from mcp.types import ToolAnnotations

    from ..tools.registry import REGISTRY
    from .prompts import register_prompts
    from .resources import register_resources

    mcp = FastMCP("thinktocad", instructions=INSTRUCTIONS)
    for tool in REGISTRY.tools():
        annotations = ToolAnnotations(
            readOnlyHint=tool.side_effect == "read",
            destructiveHint=tool.side_effect in ("write", "exec"),
        )
        mcp.add_tool(
            Tool.from_function(
                fn=tool.handler,
                name=tool.name,
                description=tool.description,
                annotations=annotations,
            )
        )
    register_resources(mcp)
    register_prompts(mcp)
    return mcp


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="thinktocad-mcp", description="ThinkToCad MCP server (stdio)."
    )
    parser.add_argument("--root", default=None, help="repo root (overrides discovery)")
    parser.add_argument("--policy", default=None, choices=["permissive", "strict"])
    parser.add_argument("--trace", action="store_true", help="record per-tool spans")
    parser.add_argument("--ablation", default=None, help="comma-separated tool names to disable")
    args = parser.parse_args()
    ablation = {x.strip() for x in args.ablation.split(",")} if args.ablation else None
    build_server(root=args.root, policy=args.policy, trace=args.trace, ablation=ablation).run()


if __name__ == "__main__":
    main()
