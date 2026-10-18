"""Canonical, provider-neutral tool contract and registry.

Implements ``guides/AI_AGENT_TOOLKIT_GUIDE.md``:

* section 3 - one canonical ``ToolDefinition`` (name, description, JSON Schema,
  side-effect class) adapted at the MCP boundary;
* section 4 - a registry as the single source of truth, last-write-wins;
* section 5 - per-tool timeout; never let one hung tool block the turn;
* section 6 - structured error envelope; never raise into the loop.

A tool is a plain function whose body returns the ``data`` payload or raises
:class:`~thinktocad.tools.errors.ToolError`. The :func:`safe_tool` decorator wraps it
so the callable exposed to the agent always returns::

    {"ok": bool,
     "data": <payload> | None,
     "error": {code, message, retryable, suggested_fix, details} | None}
"""
from __future__ import annotations

import functools
import inspect
import types
import typing
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeout
from dataclasses import dataclass
from typing import Any, Callable, Literal

from .errors import ErrorCode, ToolError

SideEffect = Literal["read", "write", "exec", "orchestrate"]

# Shared pool so per-tool timeouts do not spawn a thread per call. A timed-out tool is
# abandoned (guide section 5); the worker thread finishes in the background.
_EXECUTOR = ThreadPoolExecutor(max_workers=4, thread_name_prefix="thinktocad")


# --------------------------------------------------------------------------- #
# Envelopes
# --------------------------------------------------------------------------- #
def ok(data: Any = None) -> dict[str, Any]:
    """Build a success envelope."""
    return {"ok": True, "data": data, "error": None}


def err(
    code: str,
    message: str,
    *,
    retryable: bool = False,
    suggested_fix: str | None = None,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build an error envelope."""
    return {
        "ok": False,
        "data": None,
        "error": {
            "code": code,
            "message": message,
            "retryable": retryable,
            "suggested_fix": suggested_fix,
            "details": details or {},
        },
    }


# --------------------------------------------------------------------------- #
# Schema generation
# --------------------------------------------------------------------------- #
_PY_TO_JSON: dict[Any, str] = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
}


def _type_schema(ann: Any) -> dict[str, Any]:
    origin = typing.get_origin(ann)
    if origin is typing.Union or origin is types.UnionType:  # Optional[...] / X | None
        args = [a for a in typing.get_args(ann) if a is not type(None)]
        schema = dict(_type_schema(args[0])) if args else {"type": "string"}
        schema["nullable"] = True
        return schema
    if origin in (list, set, tuple, frozenset):
        args = typing.get_args(ann)
        return {"type": "array", "items": _type_schema(args[0]) if args else {}}
    if origin is dict:
        return {"type": "object"}
    if ann in _PY_TO_JSON:
        return {"type": _PY_TO_JSON[ann]}
    return {}


def schema_from_signature(fn: Callable[..., Any]) -> dict[str, Any]:
    """Build a JSON Schema (draft 2020-12 subset) from a function signature."""
    try:
        hints = typing.get_type_hints(fn)
    except Exception:  # unresolvable forward refs -> fall back to no annotations
        hints = {}
    props: dict[str, Any] = {}
    required: list[str] = []
    for pname, param in inspect.signature(fn).parameters.items():
        if param.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
            continue
        schema = dict(_type_schema(hints.get(pname, str)))
        if param.default is inspect.Parameter.empty:
            required.append(pname)
        elif param.default is not None:
            schema["default"] = param.default
        props[pname] = schema
    return {
        "type": "object",
        "properties": props,
        "required": required,
        "additionalProperties": False,
    }


# --------------------------------------------------------------------------- #
# Definition + registry
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class ToolDefinition:
    """The durable unit (guide section 3)."""

    name: str
    description: str
    input_schema: dict[str, Any]
    side_effect: SideEffect
    handler: Callable[..., dict[str, Any]]
    output_schema: dict[str, Any] | None = None
    timeout_s: float | None = 30.0
    retryable: bool = True
    max_retries: int = 2


class ToolRegistry:
    """A queryable catalogue of tools; last-write-wins on duplicate names."""

    def __init__(self) -> None:
        self._tools: dict[str, ToolDefinition] = {}

    def register(self, tool: ToolDefinition) -> None:
        if not tool.name:
            raise ValueError("tool name must be non-empty")
        self._tools[tool.name] = tool

    def get(self, name: str) -> ToolDefinition:
        try:
            return self._tools[name]
        except KeyError:
            raise ToolError(
                ErrorCode.NOT_FOUND,
                f"unknown tool: {name}",
                suggested_fix="call a name returned by tools/list",
            ) from None

    def tools(self) -> list[ToolDefinition]:
        return list(self._tools.values())

    def names(self) -> list[str]:
        return list(self._tools)

    def schemas(self) -> list[dict[str, Any]]:
        """Provider-neutral tool definitions (adapt at the provider boundary)."""
        return [
            {
                "name": t.name,
                "description": t.description,
                "inputSchema": t.input_schema,
                "sideEffect": t.side_effect,
            }
            for t in self._tools.values()
        ]

    def execute(self, name: str, **kwargs: Any) -> dict[str, Any]:
        """Execute a tool by name; always returns an envelope, never raises."""
        try:
            tool = self.get(name)
        except ToolError as exc:
            return {"ok": False, "data": None, "error": exc.to_error()}
        return tool.handler(**kwargs)


#: Process-wide registry populated by the ``@safe_tool`` decorator.
REGISTRY = ToolRegistry()


# --------------------------------------------------------------------------- #
# The @safe_tool decorator
# --------------------------------------------------------------------------- #
def _run_with_timeout(
    fn: Callable[..., Any], timeout_s: float | None, kwargs: dict[str, Any]
) -> Any:
    if not timeout_s:
        return fn(**kwargs)
    future = _EXECUTOR.submit(fn, **kwargs)
    try:
        return future.result(timeout=timeout_s)
    except FuturesTimeout:
        raise ToolError(
            ErrorCode.TIMEOUT,
            f"tool exceeded its {timeout_s:g}s budget",
            suggested_fix="reduce the request scope or raise this tool's timeout",
        ) from None


def safe_tool(
    *,
    name: str | None = None,
    side_effect: SideEffect = "read",
    timeout_s: float | None = 30.0,
    retryable: bool = True,
    max_retries: int = 2,
    description: str | None = None,
    output_schema: dict[str, Any] | None = None,
    registry: ToolRegistry = REGISTRY,
) -> Callable[[Callable[..., Any]], Callable[..., dict[str, Any]]]:
    """Register a function as a tool that always returns a structured envelope.

    The wrapped callable preserves the original signature and docstring so the MCP
    boundary can generate its schema, and never raises: ``ToolError`` becomes a typed
    error envelope, any other exception becomes ``INTERNAL_ERROR``.
    """

    def deco(fn: Callable[..., Any]) -> Callable[..., dict[str, Any]]:
        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> dict[str, Any]:
            try:
                bound = inspect.signature(fn).bind(*args, **kwargs)
                return ok(_run_with_timeout(fn, timeout_s, dict(bound.arguments)))
            except ToolError as exc:
                return {"ok": False, "data": None, "error": exc.to_error()}
            except Exception as exc:  # noqa: BLE001 - the whole point: never raise
                return err(
                    ErrorCode.INTERNAL_ERROR,
                    f"{type(exc).__name__}: {exc}",
                    retryable=False,
                    suggested_fix="report this as a bug; do not retry unchanged",
                )

        wrapper.__signature__ = inspect.signature(fn)  # type: ignore[attr-defined]
        registry.register(
            ToolDefinition(
                name=name or fn.__name__,
                description=(description or (fn.__doc__ or "").strip()),
                input_schema=schema_from_signature(fn),
                side_effect=side_effect,
                handler=wrapper,
                output_schema=output_schema,
                timeout_s=timeout_s,
                retryable=retryable,
                max_retries=max_retries,
            )
        )
        return wrapper

    return deco
