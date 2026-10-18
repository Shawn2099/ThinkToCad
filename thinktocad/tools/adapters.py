"""Provider schema adapters (guide sections 3 and 12).

One canonical :class:`~thinktocad.tools.registry.ToolDefinition` is adapted to the
OpenAI / Anthropic / Gemini / MCP envelopes at the boundary, plus strict-mode
conversion, so the same tool never needs to be authored per provider.
"""
from __future__ import annotations

from typing import Any

_GEMINI_TYPES = {
    "string": "STRING",
    "integer": "INTEGER",
    "number": "NUMBER",
    "boolean": "BOOLEAN",
    "array": "ARRAY",
    "object": "OBJECT",
}


def strictify(schema: dict[str, Any]) -> dict[str, Any]:
    """Convert a schema to OpenAI strict mode.

    Every object gets ``additionalProperties: false`` and lists **all** properties in
    ``required``; properties that were optional (had a default, or were nullable) become
    nullable unions ``type: ["x", "null"]``.
    """

    def convert(node: Any) -> Any:
        if not isinstance(node, dict):
            return node
        node = dict(node)
        if node.get("type") == "object":
            properties: dict[str, Any] = {}
            for key, value in (node.get("properties") or {}).items():
                value = convert(value)
                optional = "default" in value or value.get("nullable")
                value.pop("default", None)
                value.pop("nullable", None)
                if optional and isinstance(value.get("type"), str):
                    value["type"] = [value["type"], "null"]
                properties[key] = value
            node["properties"] = properties
            node["required"] = list(properties)
            node["additionalProperties"] = False
        if node.get("type") == "array" and "items" in node:
            node["items"] = convert(node["items"])
        return node

    return convert(schema)


def _to_gemini(node: Any) -> Any:
    if not isinstance(node, dict):
        return node
    node = dict(node)
    type_value = node.get("type")
    if isinstance(type_value, list):
        type_value = next((t for t in type_value if t != "null"), "string")
    if isinstance(type_value, str):
        node["type"] = _GEMINI_TYPES.get(type_value, "STRING")
    for key in ("additionalProperties", "nullable", "default"):
        node.pop(key, None)
    if "properties" in node:
        node["properties"] = {k: _to_gemini(v) for k, v in node["properties"].items()}
    if "items" in node:
        node["items"] = _to_gemini(node["items"])
    return node


def to_openai(tool: Any) -> dict[str, Any]:
    return {
        "type": "function",
        "name": tool.name,
        "description": tool.description,
        "parameters": strictify(tool.input_schema),
        "strict": True,
    }


def to_anthropic(tool: Any) -> dict[str, Any]:
    return {
        "name": tool.name,
        "description": tool.description,
        "input_schema": tool.input_schema,
    }


def to_gemini(tool: Any) -> dict[str, Any]:
    return {
        "name": tool.name,
        "description": tool.description,
        "parameters": _to_gemini(tool.input_schema),
    }


def to_mcp(tool: Any) -> dict[str, Any]:
    return {
        "name": tool.name,
        "description": tool.description,
        "inputSchema": tool.input_schema,
        "annotations": {
            "readOnlyHint": tool.side_effect == "read",
            "destructiveHint": tool.side_effect in ("write", "exec"),
        },
    }


#: Map a provider name to its adapter.
ADAPTERS = {
    "openai": to_openai,
    "anthropic": to_anthropic,
    "gemini": to_gemini,
    "google": to_gemini,
    "mcp": to_mcp,
}


def export(tools: list[Any], provider: str) -> list[dict[str, Any]]:
    """Adapt every tool to a provider envelope."""
    adapter = ADAPTERS.get(provider.lower())
    if adapter is None:
        raise ValueError(f"unknown provider: {provider!r}; use {sorted(ADAPTERS)}")
    return [adapter(tool) for tool in tools]
