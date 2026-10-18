"""Unit tests for the canonical tool contract (registry, envelopes, schema, timeout)."""
from __future__ import annotations

import time

from thinktocad.tools.errors import ErrorCode, ToolError
from thinktocad.tools.registry import (
    ToolRegistry,
    err,
    ok,
    safe_tool,
    schema_from_signature,
)


def test_ok_envelope_shape():
    assert ok({"x": 1}) == {"ok": True, "data": {"x": 1}, "error": None}


def test_err_envelope_shape():
    envelope = err(ErrorCode.NOT_FOUND, "nope", suggested_fix="try again")
    assert envelope["ok"] is False
    assert envelope["data"] is None
    assert envelope["error"]["code"] == "NOT_FOUND"
    assert envelope["error"]["suggested_fix"] == "try again"


def test_schema_from_signature():
    def fn(a: str, b: int = 3, c: float | None = None) -> dict:
        return {}

    schema = schema_from_signature(fn)
    assert schema["type"] == "object"
    assert schema["required"] == ["a"]
    assert schema["additionalProperties"] is False
    assert schema["properties"]["a"]["type"] == "string"
    assert schema["properties"]["b"]["default"] == 3
    assert schema["properties"]["c"]["nullable"] is True


def test_safe_tool_registers_and_wraps():
    registry = ToolRegistry()

    @safe_tool(registry=registry, side_effect="read")
    def add(a: int, b: int) -> dict:
        """Add two ints."""
        return {"sum": a + b}

    assert registry.names() == ["add"]
    assert registry.get("add").side_effect == "read"
    assert add(2, 3) == {"ok": True, "data": {"sum": 5}, "error": None}
    assert add(a=2, b=3)["data"]["sum"] == 5


def test_safe_tool_never_raises_on_toolerror():
    registry = ToolRegistry()

    @safe_tool(registry=registry)
    def boom(x: int) -> dict:
        """Boom."""
        raise ToolError(ErrorCode.INVALID_ARGUMENT, "bad x", suggested_fix="use x>0")

    envelope = boom(1)
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "INVALID_ARGUMENT"
    assert envelope["error"]["retryable"] is False


def test_safe_tool_wraps_unexpected_exception():
    registry = ToolRegistry()

    @safe_tool(registry=registry)
    def boom() -> dict:
        """Boom."""
        raise ValueError("kaboom")

    envelope = boom()
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "INTERNAL_ERROR"
    assert "kaboom" in envelope["error"]["message"]


def test_safe_tool_timeout_is_retryable():
    registry = ToolRegistry()

    @safe_tool(registry=registry, timeout_s=0.2)
    def slow() -> dict:
        """Slow."""
        time.sleep(2)
        return {}

    envelope = slow()
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "TIMEOUT"
    assert envelope["error"]["retryable"] is True


def test_registry_execute_unknown_tool():
    envelope = ToolRegistry().execute("nope")
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "NOT_FOUND"
