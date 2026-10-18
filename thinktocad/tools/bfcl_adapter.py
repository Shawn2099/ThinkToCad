"""BFCL (Berkeley Function Calling Leaderboard) adapter.

Converts the canonical ThinkToCad tool registry into BFCL's evaluation format so
the tool layer can be benchmarked against the de-facto standard for function
calling (gorilla.cs.berkeley.edu/leaderboard.html).

BFCL expects a list of function definitions with name, description, parameters
(JSON Schema), plus test cases of (query, expected_tool_calls). This adapter
produces the function-definition side; test cases are authored per experiment.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .registry import ToolDefinition, ToolRegistry


def to_bfcl_function(tool: ToolDefinition) -> dict[str, Any]:
    """Convert one ToolDefinition to a BFCL function spec."""
    return {
        "name": tool.name,
        "description": tool.description,
        "parameters": tool.input_schema,
    }


def export_bfcl(registry: ToolRegistry, out_path: str | Path | None = None) -> list[dict[str, Any]]:
    """Export all registered tools as BFCL function definitions."""
    functions = [to_bfcl_function(t) for t in registry.tools()]
    if out_path is not None:
        Path(out_path).write_text(json.dumps(functions, indent=2), encoding="utf-8")
    return functions


def build_test_case(
    query: str,
    expected_calls: list[dict[str, Any]],
    category: str = "simple",
) -> dict[str, Any]:
    """Build a BFCL-style test case.

    expected_calls: list of {"name": str, "arguments": dict}.
    """
    return {
        "id": None,
        "question": [[{"role": "user", "content": query}]],
        "function": [],  # filled at eval time with the exported functions
        "ground_truth": expected_calls,
        "category": category,
    }