"""Tests for the advisory visual-check tools."""
from __future__ import annotations

from thinktocad import paths
from thinktocad.tools import visual


def test_build_visual_check_payload_is_advisory():
    envelope = visual.build_visual_check(
        design="bracket",
        render_path="output/run_1/iso.png",
        intent="holds the motor and clears the deck",
        expected_features=["4 mounting holes", "motor boss"],
        stage="part",
    )
    assert envelope["ok"] is True
    data = envelope["data"]
    assert data["advisory"] is True
    assert "bracket" in data["prompt"]
    assert "4 mounting holes" in data["prompt"]


def test_build_visual_check_rejects_bad_stage():
    envelope = visual.build_visual_check(
        design="x", render_path="p.png", intent="i", stage="nope"
    )
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "INVALID_ARGUMENT"


def test_record_visual_check_writes_memory(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "MEMORY", tmp_path)
    first = visual.record_visual_check(
        design="bracket", render_path="iso.png", verdict="FAIL", notes="hole missing"
    )
    assert first["ok"] is True
    assert first["data"]["passed"] is False
    assert (tmp_path / "designs" / "bracket" / "visual_1.json").exists()

    second = visual.record_visual_check(design="bracket", render_path="iso.png", verdict="PASS")
    assert second["data"]["visual"] == 2
    assert second["data"]["passed"] is True
