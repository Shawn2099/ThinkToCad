"""Provider-agnostic ReAct agent loop (SKILLS.md section 3, guide sections 4-5).

Five termination conditions:

1. final output (no tool calls, or an explicit ``final``);
2. ``max_turns`` exceeded;
3. handoff to another agent;
4. human-in-the-loop interrupt;
5. guardrail tripwire / explicit exit.

The model is injected as ``model_fn(messages, tools, state) -> Turn`` so the loop is
provider-neutral. Tool calls run through the registry's batch executor (read-parallel,
write-sequential, order preserved, sibling failures isolated) and hooks fire at
``before_model`` / ``before_tools`` / ``after_turn``.
"""
from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from ..tools.execution import ExecutionContext
from ..tools.registry import REGISTRY, ToolRegistry


@dataclass
class Turn:
    """One model turn: either tool calls, or a terminal signal."""

    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    text: str | None = None
    final: Any | None = None
    handoff: str | None = None
    interrupt: Any | None = None
    tripwire: str | None = None


ModelFn = Callable[[list[dict], list[dict], dict], Turn]
Hook = Callable[[dict], None]


@dataclass
class Budget:
    max_turns: int = 20
    max_tool_calls: int = 100
    max_seconds: float | None = None


@dataclass
class RunResult:
    termination: str
    result: Any
    state: dict
    turns: int
    tool_calls: int


class AgentLoop:
    """A bounded ReAct loop with hooks and five termination conditions."""

    def __init__(
        self,
        registry: ToolRegistry | None = None,
        context: ExecutionContext | None = None,
        budget: Budget | None = None,
    ) -> None:
        self.registry = registry or REGISTRY
        self.context = context or ExecutionContext()
        self.budget = budget or Budget()
        self.before_model: list[Hook] = []
        self.before_tools: list[Hook] = []
        self.after_turn: list[Hook] = []

    def run(self, model_fn: ModelFn, initial_state: dict | None = None) -> RunResult:
        state: dict[str, Any] = dict(initial_state or {})
        state.setdefault("messages", [])
        state.setdefault("history", [])
        turns = 0
        tool_calls = 0
        started = time.perf_counter()
        schemas = self.registry.schemas()

        while True:
            if turns >= self.budget.max_turns:
                return RunResult("max_turns_exceeded", None, state, turns, tool_calls)
            if (
                self.budget.max_seconds is not None
                and time.perf_counter() - started >= self.budget.max_seconds
            ):
                return RunResult("budget_exceeded", None, state, turns, tool_calls)

            for hook in self.before_model:
                hook(state)

            turn = model_fn(state["messages"], schemas, state)
            turns += 1

            if turn.final is not None:
                return RunResult("final_output", turn.final, state, turns, tool_calls)
            if turn.handoff:
                return RunResult("handoff", {"handoff": turn.handoff}, state, turns, tool_calls)
            if turn.interrupt is not None:
                return RunResult("interrupt", {"interrupt": turn.interrupt}, state, turns, tool_calls)
            if turn.tripwire:
                return RunResult(
                    "guardrail_tripwire", {"tripwire": turn.tripwire}, state, turns, tool_calls
                )

            calls = turn.tool_calls
            if not calls:
                return RunResult("final_output", turn.text, state, turns, tool_calls)

            for hook in self.before_tools:
                hook(state)

            tool_calls += len(calls)
            if tool_calls > self.budget.max_tool_calls:
                return RunResult("budget_exceeded", None, state, turns, tool_calls)

            results = self.registry.execute_all(calls, ctx=self.context)
            for call, result in zip(calls, results):
                state["history"].append({"tool_call": call, "result": result})
            state["last_results"] = results

            for hook in self.after_turn:
                hook(state)
