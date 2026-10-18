"""Canonical, provider-neutral tool contract and registry.

Implements ``guides/AI_AGENT_TOOLKIT_GUIDE.md``:

* section 3 - one canonical ``ToolDefinition`` adapted at the provider boundary;
* section 4 - a registry as the single source of truth (last-write-wins);
* section 5 - per-tool timeout, read-parallel / write-sequential batch execution,
  call-order preservation, sibling-failure isolation;
* section 6 - structured error envelope; never raise into the loop.

A tool is a plain function whose body returns the ``data`` payload or raises
:class:`~thinktocad.tools.errors.ToolError`. :func:`safe_tool` registers it and returns a
wrapper that runs the full pipeline (see :mod:`.execution`) and always returns::

    {"ok": bool, "data": <payload> | None,
     "error": {code, message, retryable, suggested_fix, details} | None}
"""
from __future__ import annotations

import functools
import inspect
import types
import typing
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Literal

from . import execution
from .errors import ErrorCode, ToolError

SideEffect = Literal["read", "write", "exec", "orchestrate"]


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
    return execution.error_envelope(
        code, message, retryable=retryable, suggested_fix=suggested_fix, details=details
    )


# --------------------------------------------------------------------------- #
# Schema generation
# --------------------------------------------------------------------------- #
_PY_TO_JSON: dict[Any, str] = {str: "string", int: "integer", float: "number", bool: "boolean"}


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
    except Exception:  # noqa: BLE001 - unresolvable forward refs; fall back to no annotations
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
# Definition
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class ToolDefinition:
    """The durable unit (guide section 3).

    ``fn`` is the raw implementation (returns ``data`` or raises ``ToolError``) and is
    what the pipeline executes; ``handler`` is the wrapped callable that always returns
    an envelope and is what the MCP/provider boundary exposes.
    """

    name: str
    description: str
    input_schema: dict[str, Any]
    side_effect: SideEffect
    fn: Callable[..., Any]
    handler: Callable[..., dict[str, Any]]
    output_schema: dict[str, Any] | None = None
    timeout_s: float | None = 30.0
    retryable: bool = True
    max_retries: int = 2


# --------------------------------------------------------------------------- #
# Registry
# --------------------------------------------------------------------------- #
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
        return self.execute_with(name, kwargs)

    def execute_with(
        self, name: str, args: dict[str, Any], ctx: execution.ExecutionContext | None = None
    ) -> dict[str, Any]:
        try:
            tool = self.get(name)
        except ToolError as exc:
            return {"ok": False, "data": None, "error": exc.to_error()}
        return execution.run_call(
            name=tool.name,
            fn=tool.fn,
            args=dict(args),
            ctx=ctx or DEFAULT_CONTEXT,
            side_effect=tool.side_effect,
            timeout_s=tool.timeout_s,
            retryable=tool.retryable,
            max_attempts=1 + tool.max_retries,
        )

    def execute_all(
        self, calls: list[dict[str, Any]], ctx: execution.ExecutionContext | None = None
    ) -> list[dict[str, Any]]:
        """Run a batch in order: reads in parallel, writes sequentially.

        Call order is preserved in the output list and a failed call never discards its
        successful siblings (guide section 5).
        """
        ctx = ctx or DEFAULT_CONTEXT
        results: list[dict[str, Any] | None] = [None] * len(calls)
        reads: list[tuple[int, ToolDefinition, dict]] = []
        writes: list[tuple[int, ToolDefinition, dict]] = []

        for index, call in enumerate(calls):
            try:
                tool = self.get(call["name"])
            except ToolError as exc:
                results[index] = {"ok": False, "data": None, "error": exc.to_error()}
                continue
            bucket = reads if tool.side_effect == "read" else writes
            bucket.append((index, tool, call))

        if reads:
            futures = {
                index: execution.BATCH_EXECUTOR.submit(
                    execution.run_call,
                    name=tool.name,
                    fn=tool.fn,
                    args=dict(call.get("args", {})),
                    ctx=ctx,
                    side_effect=tool.side_effect,
                    timeout_s=tool.timeout_s,
                    call_id=call.get("call_id", ""),
                    retryable=tool.retryable,
                    max_attempts=1 + tool.max_retries,
                )
                for index, tool, call in reads
            }
            for index, future in futures.items():
                try:
                    results[index] = future.result()
                except Exception as exc:  # noqa: BLE001
                    results[index] = err(
                        ErrorCode.INTERNAL_ERROR, f"{type(exc).__name__}: {exc}"
                    )

        for index, tool, call in writes:
            results[index] = execution.run_call(
                name=tool.name,
                fn=tool.fn,
                args=dict(call.get("args", {})),
                ctx=ctx,
                side_effect=tool.side_effect,
                timeout_s=tool.timeout_s,
                call_id=call.get("call_id", ""),
                retryable=tool.retryable,
                max_attempts=1 + tool.max_retries,
            )

        return results  # type: ignore[return-value]


#: Process-wide registry populated by the ``@safe_tool`` decorator.
REGISTRY = ToolRegistry()

#: Default execution context (tracing, metrics, policy, guardrails, retry).
DEFAULT_CONTEXT = execution.ExecutionContext()


def set_default_context(ctx: execution.ExecutionContext) -> None:
    """Replace the process-wide default execution context."""
    global DEFAULT_CONTEXT
    DEFAULT_CONTEXT = ctx


# --------------------------------------------------------------------------- #
# The @safe_tool decorator
# --------------------------------------------------------------------------- #
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
    """Register a function as a tool whose exposed callable always returns an envelope.

    The wrapped callable preserves the original signature and docstring so the MCP
    boundary can generate its schema, and never raises: the full pipeline (policy,
    guardrails, retry, timeout, tracing) runs inside :func:`.execution.run_call`.
    """

    def deco(fn: Callable[..., Any]) -> Callable[..., dict[str, Any]]:
        tool_name = name or fn.__name__

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> dict[str, Any]:
            try:
                bound = inspect.signature(fn).bind(*args, **kwargs)
                bound.apply_defaults()
            except TypeError as exc:
                return execution.error_envelope(
                    ErrorCode.INVALID_ARGUMENT,
                    f"bad arguments for {tool_name}: {exc}",
                    suggested_fix="check the tool's input schema and retry",
                )
            return execution.run_call(
                name=tool_name,
                fn=fn,
                args=dict(bound.arguments),
                ctx=DEFAULT_CONTEXT,
                side_effect=side_effect,
                timeout_s=timeout_s,
                retryable=retryable,
                max_attempts=1 + max_retries,
            )

        wrapper.__signature__ = inspect.signature(fn)  # type: ignore[attr-defined]
        registry.register(
            ToolDefinition(
                name=tool_name,
                description=(description or (fn.__doc__ or "").strip()),
                input_schema=schema_from_signature(fn),
                side_effect=side_effect,
                fn=fn,
                handler=wrapper,
                output_schema=output_schema,
                timeout_s=timeout_s,
                retryable=retryable,
                max_retries=max_retries,
            )
        )
        return wrapper

    return deco
