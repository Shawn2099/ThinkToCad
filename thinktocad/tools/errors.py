"""Structured error taxonomy for ThinkToCad tools.

Tools return a structured envelope and never raise into the agent loop
(``guides/AI_AGENT_TOOLKIT_GUIDE.md`` sections 1 and 6). ``ToolError`` is the one
exception type a tool body may raise; the ``@safe_tool`` wrapper converts it into the
``error`` half of the envelope. Error codes encode retryability so the model can tell
"fix your input and retry" from "do not retry" from "transient, back off".
"""
from __future__ import annotations

from typing import Any


class ErrorCode:
    """Machine-readable error codes (guide section 6, "error categories")."""

    INVALID_ARGUMENT = "INVALID_ARGUMENT"        # bad input; model corrects and retries
    NOT_FOUND = "NOT_FOUND"                      # permanent
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"          # permanent (until built)
    TIMEOUT = "TIMEOUT"                          # transient; safe to retry as-is
    BACKEND_UNAVAILABLE = "BACKEND_UNAVAILABLE"  # transient (external server down)
    DESIGN_RULE_VIOLATION = "DESIGN_RULE_VIOLATION"  # a gate refused the action
    CONTRACT_INVALID = "CONTRACT_INVALID"        # contract failed its schema check
    INTERNAL_ERROR = "INTERNAL_ERROR"            # unexpected; permanent
    POLICY_DENIED = "POLICY_DENIED"              # permanent; a deny rule matched
    APPROVAL_REQUIRED = "APPROVAL_REQUIRED"      # HITL pause; retry after approval
    UNSAFE_CODE = "UNSAFE_CODE"                  # permanent; static screen failed
    GUARDRAIL_TRIPPED = "GUARDRAIL_TRIPPED"      # permanent; a tripwire fired
    CIRCUIT_OPEN = "CIRCUIT_OPEN"                # transient; a dependency is failing
    CANCELLED = "CANCELLED"                      # run cancelled


# Codes that are safe to retry without changing the input.
RETRYABLE_AS_IS: frozenset[str] = frozenset(
    {
        ErrorCode.TIMEOUT,
        ErrorCode.BACKEND_UNAVAILABLE,
        ErrorCode.CIRCUIT_OPEN,
        ErrorCode.APPROVAL_REQUIRED,
    }
)


class ToolError(Exception):
    """A structured, model-visible tool failure.

    Args:
        code: one of :class:`ErrorCode`.
        message: specific cause (short, plain text, no secrets).
        retryable: override the default retryability for ``code``.
        suggested_fix: the next step the model should take.
        details: structured context (param names, values, thresholds).
    """

    def __init__(
        self,
        code: str,
        message: str,
        *,
        retryable: bool | None = None,
        suggested_fix: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.retryable = RETRYABLE_AS_IS.__contains__(code) if retryable is None else retryable
        self.suggested_fix = suggested_fix
        self.details = details or {}

    def to_error(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "message": self.message,
            "retryable": self.retryable,
            "suggested_fix": self.suggested_fix,
            "details": self.details,
        }
