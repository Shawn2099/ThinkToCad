"""Stateful tool simulator (guide section 11, pattern 27).

For multi-turn tests without live backends: script each tool's response, which may read
and write shared state, and record every call. The simulated registry is a drop-in for
the real one.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

from ..tools.registry import ToolRegistry, safe_tool

#: A script receives (args, state) and returns the tool's data payload.
Script = Callable[[dict, dict], Any]


class ToolSimulator:
    def __init__(self) -> None:
        self.scripts: dict[str, Script] = {}
        self.calls: list[dict] = []
        self.state: dict[str, Any] = {}

    def script(self, name: str, fn: Script, *, side_effect: str = "read") -> ToolSimulator:
        self.scripts[name] = fn
        self._side_effects = getattr(self, "_side_effects", {})
        self._side_effects[name] = side_effect
        return self

    def build(self) -> ToolRegistry:
        registry = ToolRegistry()
        for name, fn in self.scripts.items():
            self._register(registry, name, fn)
        return registry

    def _register(self, registry: ToolRegistry, name: str, fn: Script) -> None:
        side_effect = getattr(self, "_side_effects", {}).get(name, "read")

        def impl(**kwargs: Any) -> Any:
            self.calls.append({"name": name, "args": kwargs})
            return fn(kwargs, self.state)

        impl.__name__ = name
        impl.__doc__ = f"Simulated tool '{name}'."
        safe_tool(registry=registry, name=name, side_effect=side_effect)(impl)
