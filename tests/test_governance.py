"""Tests for the policy engine and guardrail pipeline (guide sections 6 and 9)."""
from __future__ import annotations

from thinktocad.tools.execution import ExecutionContext
from thinktocad.tools.guardrails import GuardrailPipeline, Tripwire
from thinktocad.tools.policy import Decision, Rule, ToolPolicy
from thinktocad.tools.registry import ToolRegistry, safe_tool


def _registry() -> ToolRegistry:
    registry = ToolRegistry()

    @safe_tool(registry=registry, side_effect="read")
    def secret(x: int) -> dict:
        """Secret."""
        return {"value": x, "secret": "s3cr3t"}

    return registry


def test_policy_deny_wins_over_allow():
    policy = ToolPolicy(
        deny=[Rule(Decision.DENY, "secret", None)],
        allow=[Rule(Decision.ALLOW, "*", None)],
    )
    assert policy.evaluate("secret") is Decision.DENY
    assert policy.evaluate("other") is Decision.ALLOW


def test_policy_arg_pattern():
    policy = ToolPolicy(deny=[Rule(Decision.DENY, "read", "*.env")])
    assert policy.evaluate("read", {"path": "a.env"}) is Decision.DENY
    assert policy.evaluate("read", {"path": "a.step"}) is Decision.ALLOW


def test_policy_strict_asks_before_writes():
    policy = ToolPolicy.strict()
    assert policy.evaluate("list_mechanisms") is Decision.ASK  # default ask
    assert policy.evaluate("save_attempt") is Decision.ASK


def test_run_call_denied_by_policy():
    registry = _registry()
    ctx = ExecutionContext(policy=ToolPolicy(deny=[Rule(Decision.DENY, "secret")]))
    envelope = registry.execute_with("secret", {"x": 1}, ctx=ctx)
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "POLICY_DENIED"


def test_run_call_ask_then_approved():
    registry = _registry()
    policy = ToolPolicy(ask=[Rule(Decision.ASK, "secret")])
    pending = registry.execute_with("secret", {"x": 1}, ctx=ExecutionContext(policy=policy))
    assert pending["error"]["code"] == "APPROVAL_REQUIRED"
    assert pending["error"]["retryable"] is True

    approved = registry.execute_with(
        "secret", {"x": 1}, ctx=ExecutionContext(policy=policy, approved=True)
    )
    assert approved["ok"] is True


def test_input_guardrail_replaces_args():
    registry = _registry()

    def force_x(name: str, args: dict) -> dict:
        return {**args, "x": 99}

    ctx = ExecutionContext(guardrails=GuardrailPipeline(input_guardrails=[force_x]))
    envelope = registry.execute_with("secret", {"x": 1}, ctx=ctx)
    assert envelope["data"]["value"] == 99


def test_output_guardrail_redacts():
    registry = _registry()

    def redact(name: str, data):
        if isinstance(data, dict) and "secret" in data:
            return {**data, "secret": "***"}
        return None

    ctx = ExecutionContext(guardrails=GuardrailPipeline(output_guardrails=[redact]))
    envelope = registry.execute_with("secret", {"x": 1}, ctx=ctx)
    assert envelope["data"]["secret"] == "***"


def test_tripwire_halts_call():
    registry = _registry()

    def block(name: str, args: dict):
        raise Tripwire("blocked")

    ctx = ExecutionContext(guardrails=GuardrailPipeline(input_guardrails=[block]))
    envelope = registry.execute_with("secret", {"x": 1}, ctx=ctx)
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "GUARDRAIL_TRIPPED"
