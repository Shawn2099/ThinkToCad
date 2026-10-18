"""A small deterministic eval suite over the ThinkToCad domain tools (guide section 11).

Run from the repo root::

    python -m thinktocad.evals.tasks

Exit code is non-zero when any task fails, so it can gate CI.
"""
from __future__ import annotations

from ..tools import contracts, knowledge, verification  # noqa: F401  (register tools)
from ..tools.registry import REGISTRY
from .graders import data_at, error_code
from .harness import Task, run_suite

_PROSE_CONTRACT = {
    "name": "x",
    "function": "y",
    "constraints": {"wall": "about 5 mm"},
    "mechanisms": ["m"],
    "validation": [{}],
}


TASKS: list[Task] = [
    Task(
        name="knowledge_corpus_present",
        calls=[{"name": "list_mechanisms", "args": {"response_format": "concise"}}],
        grader=data_at(0, "count"),
        description="the knowledge base exposes its mechanism corpus",
    ),
    Task(
        name="retrieve_known_mechanism",
        calls=[
            {
                "name": "retrieve_knowledge",
                "args": {"mechanisms": ["spacer_sleeve"], "include_constraints": False},
            }
        ],
        grader=data_at(0, "mechanisms.0.id", "spacer_sleeve"),
    ),
    Task(
        name="dfm_flags_thin_wall",
        calls=[{"name": "dfm_check", "args": {"process": "fdm", "features": {"wall_mm": 0.3}}}],
        grader=data_at(0, "passed", False),
    ),
    Task(
        name="contract_rejects_prose_constraint",
        calls=[{"name": "check_contract", "args": {"contract": _PROSE_CONTRACT}}],
        grader=data_at(0, "valid", False),
    ),
    Task(
        name="g2_requires_credibility_tier",
        calls=[
            {
                "name": "check_gate",
                "args": {
                    "gate": "G2",
                    "inputs": {
                        "checks": [{"name": "mass", "pass": True}],
                        "deterministic": True,
                    },
                },
            }
        ],
        grader=data_at(0, "passed", False),
    ),
    Task(
        name="missing_contract_is_not_found",
        calls=[{"name": "get_contract", "args": {"name": "no_such_contract"}}],
        grader=error_code(0, "NOT_FOUND"),
    ),
]


def main() -> int:
    suite = run_suite(REGISTRY, TASKS)
    for result in suite.results:
        status = "PASS" if result.passed else "FAIL"
        print(f"[{status}] {result.name} — {result.detail}")
    print(suite.summary())
    return 0 if suite.passed == suite.total else 1


if __name__ == "__main__":
    raise SystemExit(main())
