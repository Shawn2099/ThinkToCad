"""Contract tools: load and validate ``contracts/<name>.yaml``.

A contract is the source of truth for one design item: function + numbers-only
constraints + candidate mechanisms + validation checks (see ``WORKFLOW.md`` stage 3).
"""
from __future__ import annotations

import yaml

from .. import paths
from .errors import ErrorCode, ToolError
from .registry import safe_tool


def _load_contract(name: str) -> dict:
    path = paths.CONTRACTS / f"{name}.yaml"
    if not path.exists():
        raise ToolError(
            ErrorCode.NOT_FOUND,
            f"contract not found: {name}",
            suggested_fix=f"create contracts/{name}.yaml from contracts/_template.yaml",
        )
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        raise ToolError(ErrorCode.CONTRACT_INVALID, f"invalid YAML: {exc}") from None


@safe_tool(side_effect="read", timeout_s=10)
def get_contract(name: str) -> dict:
    """Load a design contract by name from contracts/<name>.yaml.

    A contract defines one design item: its function, numeric constraints, candidate
    mechanisms, and validation checks. Use it in the Specify stage and before building.
    Side effect: read-only.

    Args:
        name: contract name without the .yaml extension.
    """
    path = paths.CONTRACTS / f"{name}.yaml"
    return {"name": name, "path": str(path), "contract": _load_contract(name)}


@safe_tool(side_effect="read", timeout_s=10)
def check_contract(name: str | None = None, contract: dict | None = None) -> dict:
    """Validate a contract: required fields present and constraints are numbers only.

    This is the Specify-stage gate — "every constraint is a number or stock size, not a
    vibe". Returns {"valid": bool, "issues": [str, ...]} so the model can fix and retry.
    Side effect: read-only.

    Args:
        name: load and check contracts/<name>.yaml.
        contract: check this in-memory contract dict instead (e.g. a draft).
    """
    if contract is None:
        if not name:
            raise ToolError(ErrorCode.INVALID_ARGUMENT, "provide `name` or `contract`")
        contract = _load_contract(name)

    issues: list[str] = []
    if not contract.get("name"):
        issues.append("missing: name")
    if not contract.get("function"):
        issues.append("missing: function")

    constraints = contract.get("constraints")
    if not isinstance(constraints, dict) or not constraints:
        issues.append("missing or empty: constraints")
    else:
        for key, value in constraints.items():
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                issues.append(
                    f"constraint '{key}' must be a number, got "
                    f"{type(value).__name__}: {value!r}"
                )

    if not isinstance(contract.get("mechanisms"), list) or not contract["mechanisms"]:
        issues.append("missing or empty: mechanisms")
    if not isinstance(contract.get("validation"), list) or not contract["validation"]:
        issues.append("missing or empty: validation")

    return {"valid": not issues, "issues": issues}
