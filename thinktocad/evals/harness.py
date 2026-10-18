"""Eval harness (guide section 11, patterns 25-26).

Deterministic, no LLM required: a task runs a sequence of tool calls and grades the
outcomes. An optional judge hook can add LLM-as-judge scoring later. This is the
"unit-style eval" (assert tool calls and results) plus a suite-level pass rate for CI
gating.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from ..tools.execution import ExecutionContext
from ..tools.registry import ToolRegistry

#: A grader takes the list of result envelopes and returns {"passed", "score", "detail"}.
Grader = Callable[[list[dict]], dict]


@dataclass
class Task:
    name: str
    calls: list[dict]
    grader: Grader
    description: str = ""


@dataclass
class TaskResult:
    name: str
    passed: bool
    score: float
    detail: str
    results: list[dict]


@dataclass
class SuiteResult:
    results: list[TaskResult] = field(default_factory=list)

    @property
    def passed(self) -> int:
        return sum(1 for result in self.results if result.passed)

    @property
    def total(self) -> int:
        return len(self.results)

    @property
    def pass_rate(self) -> float:
        return self.passed / self.total if self.total else 0.0

    def summary(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "total": self.total,
            "pass_rate": self.pass_rate,
            "failures": [r.name for r in self.results if not r.passed],
        }


def run_task(
    registry: ToolRegistry, task: Task, ctx: ExecutionContext | None = None
) -> TaskResult:
    results = registry.execute_all(task.calls, ctx=ctx or ExecutionContext())
    verdict = task.grader(results)
    passed = bool(verdict.get("passed"))
    return TaskResult(
        name=task.name,
        passed=passed,
        score=float(verdict.get("score", 1.0 if passed else 0.0)),
        detail=str(verdict.get("detail", "")),
        results=results,
    )


def run_suite(
    registry: ToolRegistry, tasks: list[Task], ctx: ExecutionContext | None = None
) -> SuiteResult:
    return SuiteResult([run_task(registry, task, ctx) for task in tasks])
