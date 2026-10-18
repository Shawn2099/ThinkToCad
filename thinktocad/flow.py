"""The ThinkToCad design flow: stages and gates.

The process (``WORKFLOW.md`` and the synthesized final flow)::

    Ideate -> Research -> Specify -> Build -> Validate -> Review -> Deliver -> Learn

with four gates between stages:

* **G1 confidence**  - after Specify; every constraint numeric, mechanism fit, >= 0.80.
* **G2 verification** - after Validate; every check passes, deterministic, credibility tiered.
* **G3 publish**      - before Deliver; rebuild at parameter extremes, specs green.
* **G4 human**        - after Review; the user approves (the final word).

These gates are executable so an agent cannot skip them by prose.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Stage(str, Enum):
    IDEATE = "ideate"
    RESEARCH = "research"
    SPECIFY = "specify"
    BUILD = "build"
    VALIDATE = "validate"
    REVIEW = "review"
    DELIVER = "deliver"
    LEARN = "learn"


STAGE_ORDER: list[Stage] = [
    Stage.IDEATE,
    Stage.RESEARCH,
    Stage.SPECIFY,
    Stage.BUILD,
    Stage.VALIDATE,
    Stage.REVIEW,
    Stage.DELIVER,
    Stage.LEARN,
]

#: Which gates must pass before leaving each stage. A stage can require several (the
#: Review -> Deliver transition needs both the human gate G4 and the publish gate G3,
#: matching WORKFLOW.md stages 6, 6.5 and 7).
STAGE_GATE: dict[Stage, list[str]] = {
    Stage.SPECIFY: ["G1"],
    Stage.VALIDATE: ["G2"],
    Stage.REVIEW: ["G4", "G3"],
}

CONFIDENCE_SUBSCORES = (
    "mechanism_fit",
    "constraint_completeness",
    "manufacturability",
    "physics_coverage",
    "standards_coverage",
)
CONFIDENCE_THRESHOLD = 0.80

#: Ordered credibility tiers (CAD/CAE Copilot V&V-40 style); never assume production_ready.
CREDIBILITY_TIERS = (
    "critique_finding",
    "surrogate_prediction",
    "proxy_assembly_result",
    "executed_solver_result",
)


def _gate(name: str, passed: bool, score: float | None, reasons: list[str]) -> dict[str, Any]:
    return {"gate": name, "passed": passed, "score": score, "reasons": reasons}


def confidence_gate(subscores: dict[str, float], threshold: float = CONFIDENCE_THRESHOLD) -> dict:
    """G1: mean of the five subscores must reach ``threshold``."""
    missing = [key for key in CONFIDENCE_SUBSCORES if key not in subscores]
    if missing:
        return _gate("G1", False, None, [f"missing subscores: {missing}"])
    score = sum(float(subscores[key]) for key in CONFIDENCE_SUBSCORES) / len(CONFIDENCE_SUBSCORES)
    passed = score >= threshold
    return _gate("G1", passed, score, [] if passed else [f"confidence {score:.2f} < {threshold}"])


def verification_gate(
    checks: list[dict], deterministic: bool, credibility: str | None
) -> dict:
    """G2: every check passes, the build is deterministic, and a credibility tier is set."""
    reasons: list[str] = []
    failed = [c.get("name", "?") for c in checks if not c.get("pass")]
    reasons += [f"check failed: {name}" for name in failed]
    if not deterministic:
        reasons.append("build is not deterministic (mesh bytes differ)")
    if credibility not in CREDIBILITY_TIERS:
        reasons.append(f"credibility tier not recorded (got {credibility!r})")
    return _gate("G2", not reasons, None, reasons)


def publish_gate(extremes_ok: bool, specs_green: bool, deterministic: bool) -> dict:
    """G3: rebuild at parameter extremes, all specs green, deterministic."""
    reasons: list[str] = []
    if not extremes_ok:
        reasons.append("failed at a parameter extreme")
    if not specs_green:
        reasons.append("a spec is red")
    if not deterministic:
        reasons.append("non-deterministic result")
    return _gate("G3", not reasons, None, reasons)


def human_gate(approved: bool) -> dict:
    """G4: the user's decision is final."""
    return _gate("G4", bool(approved), None, [] if approved else ["awaiting user approval"])


GATES = {
    "G1": confidence_gate,
    "G2": verification_gate,
    "G3": publish_gate,
    "G4": human_gate,
}


@dataclass
class FlowState:
    """Tracks progress through the stages and the gate verdicts."""

    stage: Stage = Stage.IDEATE
    gate_results: dict[str, dict] = field(default_factory=dict)
    overrides: list[dict] = field(default_factory=list)

    def advance(self) -> Stage:
        """Move to the next stage (requires the current stage's gates to have passed)."""
        missing = [
            gate
            for gate in STAGE_GATE.get(self.stage, [])
            if not self.gate_results.get(gate, {}).get("passed")
        ]
        if missing:
            raise PermissionError(
                f"cannot leave {self.stage.value}: gate {', '.join(missing)} not passed"
            )
        index = STAGE_ORDER.index(self.stage)
        if index + 1 >= len(STAGE_ORDER):
            return self.stage
        self.stage = STAGE_ORDER[index + 1]
        return self.stage

    def record_gate(self, result: dict) -> None:
        self.gate_results[result["gate"]] = result

    def override(self, gate: str, reason: str) -> None:
        """Deliberately bypass a gate, recording why (never silent)."""
        self.overrides.append({"gate": gate, "reason": reason})
        self.gate_results[gate] = _gate(gate, True, None, [f"OVERRIDDEN: {reason}"])
