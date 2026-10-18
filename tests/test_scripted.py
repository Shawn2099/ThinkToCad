"""Integration test: the real AgentLoop runs end to end with a scripted model."""
from __future__ import annotations

from thinktocad import paths
from thinktocad.runtime.loop import Budget
from thinktocad.runtime.scripted import run_scripted


def test_scripted_loop_runs_end_to_end(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "MEMORY", tmp_path)
    plan = [
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
            },
        ),
    ]

    result = run_scripted("cut_height_adjust", plan)

    assert result.termination == "final_output"
    assert result.turns == 5
    assert result.tool_calls == 4
    # the attempt was written under the patched memory root
    assert (tmp_path / "designs" / "cut_height_adjust" / "attempt_1.yaml").exists()


def test_scripted_loop_stops_at_max_turns(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "MEMORY", tmp_path)
    # a plan longer than the budget -> the loop must terminate by budget
    plan = [("check_contract", {"name": "cut_height_adjust"})] * 5
    result = run_scripted("cut_height_adjust", plan, budget=Budget(max_turns=3))
    assert result.termination == "max_turns_exceeded"
    assert result.turns == 3
