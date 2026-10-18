"""Tests for memory recall and the manufacturing profile."""
from __future__ import annotations

from thinktocad import paths
from thinktocad.tools import knowledge, verification


def test_recall_reads_past_attempts(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "MEMORY", tmp_path)
    verification.save_attempt(
        design="widget", status="failed", mechanism="spacer_sleeve", notes="tilted"
    )
    verification.save_attempt(design="widget", status="passed", mechanism="slotted_bracket")

    envelope = knowledge.recall(design="widget", include_lessons=False)
    assert envelope["ok"] is True
    attempts = envelope["data"]["attempts"]
    assert len(attempts) == 2
    assert attempts[0]["record"]["status"] == "failed"


def test_recall_searches_lessons(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "KNOWLEDGE", tmp_path)
    (tmp_path / "lessons").mkdir(parents=True)
    (tmp_path / "lessons" / "wall_rule.md").write_text(
        "# Wall rule\nmin wall 2 mm", encoding="utf-8"
    )
    (tmp_path / "lessons" / "other.md").write_text("# Other\nsomething", encoding="utf-8")

    envelope = knowledge.recall(query="wall", include_attempts=False)
    assert envelope["ok"] is True
    ids = [lesson["id"] for lesson in envelope["data"]["lessons"]]
    assert "wall_rule" in ids
    assert "other" not in ids


def test_manufacturing_profile_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "ROOT", tmp_path)
    saved = verification.save_manufacturing_profile(
        processes=["hand_tools", "sheet_metal"],
        materials=["mild steel"],
        tolerances={"general_mm": 0.5},
        batch_size="one-off",
    )
    assert saved["ok"] is True
    assert (tmp_path / "manufacturing_profile.yaml").exists()

    got = verification.get_manufacturing_profile()
    assert got["data"]["profile"]["processes"] == ["hand_tools", "sheet_metal"]


def test_manufacturing_profile_rejects_unknown_process(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "ROOT", tmp_path)
    envelope = verification.save_manufacturing_profile(processes=["magic"])
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "INVALID_ARGUMENT"


def test_dfm_check_falls_back_to_profile_process(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "ROOT", tmp_path)
    verification.save_manufacturing_profile(processes=["hand_tools"])
    envelope = verification.dfm_check(features={"hole_dia_mm": 2.0})
    assert envelope["ok"] is True
    assert envelope["data"]["process"] == "hand_tools"
    assert envelope["data"]["passed"] is False


def test_dfm_check_without_process_or_profile(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "ROOT", tmp_path)
    envelope = verification.dfm_check(features={"wall_mm": 1.0})
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "INVALID_ARGUMENT"
