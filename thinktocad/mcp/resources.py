"""MCP resources: the skill and the knowledge base as readable URIs.

Resources are application-driven, URI-addressed data (guide section 8). Clients browse
them without a tool call; the templated ones take a path parameter. This is how the
knowledge base and the agent skill reach MCP-only clients.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from .. import paths

SKILL_URI = "thinktocad://skill"
FLOW_URI = "thinktocad://flow"


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return f"(not found: {path})"


def register_resources(mcp: Any) -> None:
    """Register the knowledge + skill resources on a FastMCP server."""

    @mcp.resource(SKILL_URI, name="skill", description="The ThinkToCad agent skill (SKILLS.md).")
    def skill() -> str:
        return _read(paths.ROOT / "SKILLS.md")

    @mcp.resource(
        "thinktocad://knowledge/mechanisms/{mechanism_id}",
        name="mechanism",
        description="A mechanism entry from knowledge/mechanisms/.",
    )
    def mechanism(mechanism_id: str) -> str:
        return _read(paths.KNOWLEDGE / "mechanisms" / f"{mechanism_id}.md")

    @mcp.resource(
        "thinktocad://knowledge/constraints/{name}",
        name="constraint",
        description="A constraint entry from knowledge/constraints/.",
    )
    def constraint(name: str) -> str:
        return _read(paths.KNOWLEDGE / "constraints" / f"{name}.md")

    @mcp.resource(
        "thinktocad://knowledge/lessons/{name}",
        name="lesson",
        description="A lesson from knowledge/lessons/.",
    )
    def lesson(name: str) -> str:
        return _read(paths.KNOWLEDGE / "lessons" / f"{name}.md")

    @mcp.resource(
        "thinktocad://knowledge/graph",
        name="knowledge-graph",
        description="The knowledge graph: entities and relationships.",
    )
    def graph() -> str:
        return _read(paths.KNOWLEDGE / "graph.yaml")

    @mcp.resource(
        "thinktocad://contracts/{name}",
        name="contract",
        description="A design contract from contracts/.",
    )
    def contract(name: str) -> str:
        return _read(paths.CONTRACTS / f"{name}.yaml")
