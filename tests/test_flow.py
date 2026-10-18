"""Tests for the design flow stages and gates (thinktocad.flow)."""
from __future__ import annotations

import pytest

from thinktocad import flow
from thinktocad.flow import FlowState, Stage

_GOOD = {key: 0.9 for key in flow.CONFIDENCE_SUBSCORES}
_BAD = {key: 0.5 for key in flow.CONFIDENCE_SUBSCORES}


def test_confidence_gate():
    assert flow.confidence_gate(_GOOD)["passed"] is True
    assert flow.confidence_gate(_BAD)["passed"] is False
    assert flow.confidence_gate({"mechanism_fit": 1.0})["passed"] is False


def test_verification_gate_requires_credibility():
    passed = flow.verification_gate(
        [{"name": "mass", "pass": True}], True, "executed_solver_result"
    )
    assert passed["passed"] is True

    failed_check = flow.verification_gate(
        [{"name": "mass", "pass": False}], True, "executed_solver_result"
    )
    assert failed_check["passed"] is False

    no_tier = flow.verification_gate([{"name": "mass", "pass": True}], True, None)
    assert no_tier["passed"] is False

    nondet = flow.verification_gate(
        [{"name": "mass", "pass": True}], False, "executed_solver_result"
    )
    assert nondet["passed"] is False


def test_publish_and_human_gates():
    assert flow.publish_gate(True, True, True)["passed"] is True
    assert flow.publish_gate(True, False, True)["passed"] is False
    assert flow.human_gate(True)["passed"] is True
    assert flow.human_gate(False)["passed"] is False


def test_flowstate_blocks_advance_until_gate_passes():
    state = FlowState(stage=Stage.SPECIFY)
    with pytest.raises(PermissionError):
        state.advance()

    state.record_gate(flow.confidence_gate(_GOOD))
    assert state.advance() is Stage.BUILD


def test_flowstate_override_is_recorded():
    state = FlowState(stage=Stage.SPECIFY)
    state.override("G1", "user accepted the risk")
    assert state.advance() is Stage.BUILD
    assert state.overrides == [{"gate": "G1", "reason": "user accepted the risk"}]


def test_gate_registry_covers_all():
    assert set(flow.GATES) == {"G1", "G2", "G3", "G4"}


def test_flowstate_requires_publish_gate_before_deliver():
    # WORKFLOW.md stage 6.5: the publish gate must pass before Deliver.
    state = FlowState(stage=Stage.REVIEW)
    state.record_gate(flow.human_gate(True))
    with pytest.raises(PermissionError):
        state.advance()  # G3 (publish) still missing
    state.record_gate(flow.publish_gate(True, True, True))
    assert state.advance() is Stage.DELIVER
