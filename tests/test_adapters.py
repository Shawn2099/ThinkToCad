"""Tests for provider adapters and result formatting (guide sections 3, 7, 12)."""
from __future__ import annotations

from thinktocad.tools.adapters import export, strictify, to_anthropic, to_gemini, to_mcp, to_openai
from thinktocad.tools.formatting import artifact, paginate, truncate_text
from thinktocad.tools.registry import REGISTRY

# ensure domain tools are registered
from thinktocad.tools import contracts, knowledge, verification  # noqa: F401


def test_strictify_makes_all_required_and_nullable():
    schema = {
        "type": "object",
        "properties": {"a": {"type": "string"}, "b": {"type": "integer", "default": 3}},
        "required": ["a"],
        "additionalProperties": False,
    }
    strict = strictify(schema)
    assert strict["additionalProperties"] is False
    assert set(strict["required"]) == {"a", "b"}
    assert strict["properties"]["b"]["type"] == ["integer", "null"]
    assert "default" not in strict["properties"]["b"]


def test_provider_envelopes():
    tool = REGISTRY.get("dfm_check")
    openai = to_openai(tool)
    assert openai["type"] == "function"
    assert openai["strict"] is True

    anthropic = to_anthropic(tool)
    assert "input_schema" in anthropic

    gemini = to_gemini(tool)
    assert gemini["parameters"]["type"] == "OBJECT"

    mcp = to_mcp(tool)
    assert mcp["annotations"]["readOnlyHint"] is True


def test_export_all_providers():
    for provider in ("openai", "anthropic", "gemini", "mcp"):
        assert len(export(REGISTRY.tools(), provider)) == len(REGISTRY.tools())


def test_paginate_steers():
    result = paginate(list(range(5)), limit=2)
    assert result["total"] == 5
    assert result["truncated"] is True
    assert "hint" in result


def test_truncate_text_steers():
    result = truncate_text("x" * 100, limit=10)
    assert result["truncated"] is True
    assert result["total_chars"] == 100
    assert "hint" in result


def test_artifact_reference():
    assert artifact("out.step", "step") == {"path": "out.step", "kind": "step"}
