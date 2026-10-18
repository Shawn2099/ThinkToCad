"""Tests for the ReAct loop termination conditions, hooks and budget."""
from __future__ import annotations

from thinktocad.runtime.loop import AgentLoop, Budget, Turn
from thinktocad.tools.registry import ToolRegistry, safe_tool


def _registry() -> ToolRegistry:
    registry = ToolRegistry()

    @safe_tool(registry=registry, side_effect="read")
    def echo(text: str) -> dict:
        """Echo the text."""
        return {"echo": text}

    return registry


def test_final_output_when_no_tool_calls():
    loop = AgentLoop(registry=_registry())
    result = loop.run(lambda messages, tools, state: Turn(text="done"))
    assert result.termination == "final_output"
    assert result.result == "done"


def test_executes_tools_then_finishes():
    loop = AgentLoop(registry=_registry())
    seen: dict = {}

    def model(messages, tools, state):
        if state.get("last_results"):
            seen["data"] = state["last_results"][0]["data"]
            return Turn(final="ok")
        return Turn(tool_calls=[{"name": "echo", "args": {"text": "hi"}}])

    result = loop.run(model)
    assert result.termination == "final_output"
    assert seen["data"] == {"echo": "hi"}
    assert result.tool_calls == 1


def test_max_turns_exceeded():
    loop = AgentLoop(registry=_registry(), budget=Budget(max_turns=3))

    def model(messages, tools, state):
        return Turn(tool_calls=[{"name": "echo", "args": {"text": "x"}}])

    result = loop.run(model)
    assert result.termination == "max_turns_exceeded"
    assert result.turns == 3


def test_other_termination_conditions():
    loop = AgentLoop(registry=_registry())
    assert loop.run(lambda m, t, s: Turn(interrupt={"q": "?"})).termination == "interrupt"
    assert loop.run(lambda m, t, s: Turn(tripwire="boom")).termination == "guardrail_tripwire"
    assert loop.run(lambda m, t, s: Turn(handoff="other")).termination == "handoff"


def test_tool_call_budget():
    loop = AgentLoop(registry=_registry(), budget=Budget(max_turns=100, max_tool_calls=2))

    def model(messages, tools, state):
        return Turn(
            tool_calls=[
                {"name": "echo", "args": {"text": "x"}},
                {"name": "echo", "args": {"text": "y"}},
            ]
        )

    assert loop.run(model).termination == "budget_exceeded"


def test_hooks_fire():
    loop = AgentLoop(registry=_registry())
    events: list[str] = []
    loop.before_model.append(lambda state: events.append("before_model"))
    loop.before_tools.append(lambda state: events.append("before_tools"))
    loop.after_turn.append(lambda state: events.append("after_turn"))

    def model(messages, tools, state):
        if state.get("last_results"):
            return Turn(final="ok")
        return Turn(tool_calls=[{"name": "echo", "args": {"text": "x"}}])

    loop.run(model)
    assert {"before_model", "before_tools", "after_turn"} <= set(events)
