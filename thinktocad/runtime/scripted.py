"""A deterministic model_fn that replays a fixed plan of tool calls.

Runs the real :class:`~thinktocad.runtime.loop.AgentLoop` without an LLM - a demo and
an integration test. In production the host agent (e.g. OpenCode) supplies the model;
this stands in for it so the loop itself is exercised end to end.

CLI: ``python -m thinktocad.runtime.scripted <contract>`` runs the sample plan.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import Any

from ..tools.registry import REGISTRY
from .design_agent import load_contract, retrieve_knowledge
from .loop import AgentLoop, Budget, RunResult, Turn


@dataclass
class ScriptedModel:
    """Replays a fixed plan: one tool call per turn, then a final output.

    ``plan`` is a list of ``(tool_name, kwargs)`` tuples. The model ignores the
    incoming messages and simply walks the plan, which makes a run reproducible.
    """

    plan: list[tuple[str, dict[str, Any]]]
    final_text: str = "done"
    _step: int = field(default=0, init=False)

    def __call__(
        self, messages: list[dict], schemas: list[dict], state: dict
    ) -> Turn:
        if self._step < len(self.plan):
            name, kwargs = self.plan[self._step]
            self._step += 1
            return Turn(tool_calls=[{"name": name, "args": kwargs}])
        return Turn(text=self.final_text)


def run_scripted(
    contract_name: str,
    plan: list[tuple[str, dict[str, Any]]],
    *,
    budget: Budget | None = None,
    context=None,
) -> RunResult:
    """Load a contract and run the AgentLoop with a scripted model."""
    contract = load_contract(contract_name)
    knowledge = retrieve_knowledge(contract.mechanisms)
    state: dict[str, Any] = {
        "contract": contract,
        "constraints": contract.constraints,
        "mechanisms": contract.mechanisms,
        "knowledge": knowledge,
    }
    loop = AgentLoop(registry=REGISTRY, context=context, budget=budget)
    return loop.run(ScriptedModel(plan), state)


# A sample plan for the spacer-sleeve contract: spec -> DFM -> gate -> memory.
SAMPLE_PLAN: list[tuple[str, dict[str, Any]]] = [
    ("check_contract", {"name": "cut_height_adjust"}),
    (
        "dfm_check",
        {"process": "hand_tools", "features": {"wall_mm": 4.0, "hole_dia_mm": 17.0}},
    ),
    (
        "check_gate",
        {
            "gate": "G1",
            "inputs": {
                "subscores": {
                    "mechanism_fit": 0.9,
                    "constraint_completeness": 0.95,
                    "manufacturability": 0.9,
                    "physics_coverage": 0.8,
                    "standards_coverage": 0.8,
                }
            },
        },
    ),
    (
        "save_attempt",
        {
            "design": "cut_height_adjust",
            "status": "passed",
            "mechanism": "spacer_sleeve",
            "verification": {"gates": {"G1": True}},
        },
    ),
]


def _main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "cut_height_adjust"
    result = run_scripted(name, SAMPLE_PLAN)
    print(f"contract:    {name}")
    print(f"termination: {result.termination}")
    print(f"turns:       {result.turns}")
    print(f"tool_calls:  {result.tool_calls}")


if __name__ == "__main__":
    _main()
