"""Unit tests for the ThinkToCad domain tools (knowledge, contracts, DFM, memory)."""
from __future__ import annotations

from thinktocad import paths
from thinktocad.tools import contracts, knowledge, verification
from thinktocad.tools.registry import REGISTRY

DOMAIN_TOOLS = {
    "list_mechanisms",
    "retrieve_knowledge",
    "get_contract",
    "check_contract",
    "dfm_check",
    "save_attempt",
    "save_lesson",
}


def test_registry_exposes_domain_tools_with_valid_schemas():
    assert DOMAIN_TOOLS <= set(REGISTRY.names())
    for schema in REGISTRY.schemas():
        assert schema["inputSchema"]["type"] == "object"
        assert schema["sideEffect"] in {"read", "write", "exec", "orchestrate"}


def test_list_mechanisms():
    envelope = knowledge.list_mechanisms()
    assert envelope["ok"] is True
    assert envelope["data"]["count"] > 100
    assert "spacer_sleeve" in envelope["data"]["mechanisms"]


def test_retrieve_knowledge_known_id():
    envelope = knowledge.retrieve_knowledge(
        mechanisms=["spacer_sleeve"], include_constraints=False
    )
    assert envelope["ok"] is True
    assert envelope["data"]["mechanisms"][0]["id"] == "spacer_sleeve"
    assert "sleeve" in envelope["data"]["mechanisms"][0]["text"].lower()


def test_retrieve_knowledge_reports_missing_ids():
    envelope = knowledge.retrieve_knowledge(
        mechanisms=["does_not_exist"], include_constraints=False
    )
    assert envelope["ok"] is True
    assert envelope["data"]["missing"] == ["does_not_exist"]


def test_get_contract_not_found():
    envelope = contracts.get_contract("no_such_contract")
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "NOT_FOUND"


def test_get_contract_template():
    envelope = contracts.get_contract("_template")
    assert envelope["ok"] is True
    assert envelope["data"]["contract"]["name"] == "example_part"


def test_check_contract_accepts_valid_numbers():
    contract = {
        "name": "x",
        "function": "y",
        "constraints": {"wall_mm": 2.0},
        "mechanisms": ["spacer_sleeve"],
        "validation": [{"type": "mass"}],
    }
    envelope = contracts.check_contract(contract=contract)
    assert envelope["ok"] is True
    assert envelope["data"]["valid"] is True


def test_check_contract_rejects_prose_constraint():
    contract = {
        "name": "x",
        "function": "y",
        "constraints": {"wall": "about 5 mm"},
        "mechanisms": ["m"],
        "validation": [{}],
    }
    envelope = contracts.check_contract(contract=contract)
    assert envelope["ok"] is True
    assert envelope["data"]["valid"] is False
    assert any("must be a number" in issue for issue in envelope["data"]["issues"])


def test_dfm_check_fails_thin_wall():
    envelope = verification.dfm_check(process="fdm", features={"wall_mm": 0.4})
    assert envelope["ok"] is True
    assert envelope["data"]["passed"] is False
    assert envelope["data"]["issues"][0]["metric"] == "wall_mm"


def test_dfm_check_passes():
    envelope = verification.dfm_check(process="fdm", features={"wall_mm": 2.0})
    assert envelope["data"]["passed"] is True


def test_dfm_check_unknown_process():
    envelope = verification.dfm_check(process="magic", features={})
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "INVALID_ARGUMENT"


def test_save_attempt_appends(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "MEMORY", tmp_path)
    first = verification.save_attempt(
        design="widget", status="passed", mechanism="spacer_sleeve",
        verification={"mass_kg": 0.4},
    )
    assert first["ok"] is True
    assert (tmp_path / "designs" / "widget" / "attempt_1.yaml").exists()
    second = verification.save_attempt(design="widget", status="failed")
    assert second["data"]["attempt"] == 2


def test_save_attempt_rejects_bad_status():
    envelope = verification.save_attempt(design="w", status="nope")
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "INVALID_ARGUMENT"


def test_save_lesson_trust_guard(tmp_path, monkeypatch):
    monkeypatch.setattr(paths, "KNOWLEDGE", tmp_path / "knowledge")
    saved = verification.save_lesson(
        title="Wall rule", body="min wall 2 mm", trust="T2", source="ISO 2768"
    )
    assert saved["ok"] is True

    refused = verification.save_lesson(title="Wall rule", body="min wall 1 mm", trust="T4")
    assert refused["ok"] is False
    assert refused["error"]["code"] == "DESIGN_RULE_VIOLATION"

    overridden = verification.save_lesson(
        title="Wall rule", body="revised", trust="T4", override=True
    )
    assert overridden["ok"] is True
