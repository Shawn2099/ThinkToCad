"""Tests for the eval harness, graders and the stateful tool simulator."""
from __future__ import annotations

from thinktocad.evals import ToolSimulator, run_suite
from thinktocad.evals.graders import data_at, error_code
from thinktocad.evals.harness import Task
from thinktocad.evals.tasks import TASKS
from thinktocad.tools.registry import REGISTRY


def test_domain_eval_suite_passes():
    suite = run_suite(REGISTRY, TASKS)
    assert suite.passed == suite.total, suite.summary()
    assert suite.pass_rate == 1.0


def test_grader_detects_failure():
    task = Task(
        name="expects_missing_contract",
        calls=[{"name": "get_contract", "args": {"name": "_template"}}],
        grader=error_code(0, "NOT_FOUND"),  # _template exists, so this should fail
    )
    result = run_suite(REGISTRY, [task]).results[0]
    assert result.passed is False


def test_simulator_is_stateful_and_records_calls():
    simulator = ToolSimulator()

    def counter(args, state):
        state["n"] = state.get("n", 0) + 1
        return {"count": state["n"]}

    simulator.script("counter", counter)
    registry = simulator.build()

    results = registry.execute_all([{"name": "counter", "args": {}}] * 3)
    assert [r["data"]["count"] for r in results] == [1, 2, 3]
    assert len(simulator.calls) == 3


def test_grader_data_at_nested():
    grader = data_at(0, "mechanisms.0.id", "spacer_sleeve")
    fake = [{"ok": True, "data": {"mechanisms": [{"id": "spacer_sleeve"}]}}]
    assert grader(fake)["passed"] is True
