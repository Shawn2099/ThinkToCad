"""ThinkToCad design runtime: contract loading + the ReAct loop.

This is the programmatic entry point. It wires the contract, the knowledge base, the
tool registry and the agent loop together. The model is injected, so the runtime is
provider-agnostic::

    from thinktocad.runtime.design_agent import design

    def model_fn(messages, tools, state) -> Turn: ...   # your LLM

    result = design("cut_height_adjust", model_fn)

CLI: ``python -m thinktocad.runtime.design_agent <contract_name>`` prints the loaded
contract and the registered tool names (there is no built-in model).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

import yaml

from .. import paths
from ..tools.execution import ExecutionContext
from ..tools.registry import REGISTRY
from .loop import AgentLoop, Budget, ModelFn, RunResult, Turn

__all__ = ["Contract", "load_contract", "retrieve_knowledge", "design", "AgentLoop", "Turn"]


@dataclass
class Contract:
    name: str
    function: str
    constraints: dict[str, Any]
    mechanisms: list[str]
    validation: list[dict[str, Any]] = field(default_factory=list)
    deliverables: list[str] = field(default_factory=list)


def load_contract(name: str) -> Contract:
    """Load ``contracts/<name>.yaml`` into a :class:`Contract`."""
    path = paths.CONTRACTS / f"{name}.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return Contract(
        name=data.get("name", name),
        function=data.get("function", ""),
        constraints=data.get("constraints", {}) or {},
        mechanisms=data.get("mechanisms", []) or [],
        validation=data.get("validation", []) or [],
        deliverables=data.get("deliverables", []) or [],
    )


def retrieve_knowledge(mechanisms: list[str]) -> dict[str, Any]:
    """Fetch knowledge entries via the registered tool (structured, never raises)."""
    envelope = REGISTRY.execute(
        "retrieve_knowledge", mechanisms=mechanisms, include_constraints=True
    )
    return envelope.get("data") or {"mechanisms": [], "constraints": []}


def design(
    contract_name: str,
    model_fn: ModelFn,
    *,
    context: ExecutionContext | None = None,
    budget: Budget | None = None,
    initial_state: dict | None = None,
) -> RunResult:
    """Run the agent loop for a contract.

    The initial state carries the contract, its constraints, and the retrieved knowledge
    so the model can plan against them.
    """
    contract = load_contract(contract_name)
    knowledge = retrieve_knowledge(contract.mechanisms)

    state: dict[str, Any] = {
        "contract": contract,
        "constraints": contract.constraints,
        "mechanisms": contract.mechanisms,
        "knowledge": knowledge,
        **(initial_state or {}),
    }
    loop = AgentLoop(registry=REGISTRY, context=context, budget=budget)
    return loop.run(model_fn, state)


def _main() -> None:
    import sys

    name = sys.argv[1] if len(sys.argv) > 1 else ""
    if not name:
        print("usage: python -m thinktocad.runtime.design_agent <contract_name>")
        print("registered tools:", ", ".join(REGISTRY.names()))
        return
    try:
        contract = load_contract(name)
    except FileNotFoundError:
        print(f"contract not found: contracts/{name}.yaml")
        return
    print(f"contract: {contract.name} — {contract.function}")
    print("constraints:", contract.constraints)
    print("mechanisms:", contract.mechanisms)
    print("registered tools:", ", ".join(REGISTRY.names()))
    print("supply a model_fn to thinktocad.runtime.design_agent.design() to run the loop.")


if __name__ == "__main__":
    _main()
