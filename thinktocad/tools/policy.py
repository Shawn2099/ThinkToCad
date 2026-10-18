"""Deny-wins tool policy (guide section 9).

Precedence is **DENY > ASK > ALLOW** (deny rules match even in bypass mode). Rules are
globs matched against the tool name and, optionally, against the string form of any
argument value (``Tool(arg pattern)``). ``ASK`` is the human-in-the-loop hook: the call
returns ``APPROVAL_REQUIRED`` and can be replayed once approved.
"""
from __future__ import annotations

import fnmatch
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Decision(str, Enum):
    ALLOW = "allow"
    ASK = "ask"
    DENY = "deny"


@dataclass(frozen=True)
class Rule:
    decision: Decision
    tool_pattern: str
    arg_pattern: str | None = None

    def matches(self, tool: str, args: dict[str, Any]) -> bool:
        if not fnmatch.fnmatchcase(tool, self.tool_pattern):
            return False
        if self.arg_pattern is None:
            return True
        return any(fnmatch.fnmatchcase(str(v), self.arg_pattern) for v in args.values())


@dataclass
class ToolPolicy:
    """An ordered rule set with a default decision for unmatched tools."""

    deny: list[Rule] = field(default_factory=list)
    ask: list[Rule] = field(default_factory=list)
    allow: list[Rule] = field(default_factory=list)
    default: Decision = Decision.ALLOW

    def evaluate(self, tool: str, args: dict[str, Any] | None = None) -> Decision:
        args = args or {}
        for rule in self.deny:
            if rule.matches(tool, args):
                return Decision.DENY
        for rule in self.ask:
            if rule.matches(tool, args):
                return Decision.ASK
        for rule in self.allow:
            if rule.matches(tool, args):
                return Decision.ALLOW
        return self.default

    @classmethod
    def permissive(cls) -> "ToolPolicy":
        """Allow everything (default for a trusted, local toolkit)."""
        return cls()

    @classmethod
    def strict(cls) -> "ToolPolicy":
        """Deny code execution, ask before writes, default to asking."""
        return cls(
            deny=[
                Rule(Decision.DENY, "run_*", None),
                Rule(Decision.DENY, "exec_*", None),
            ],
            ask=[
                Rule(Decision.ASK, "save_*", None),
                Rule(Decision.ASK, "create_*", None),
                Rule(Decision.ASK, "publish_*", None),
            ],
            default=Decision.ASK,
        )
