"""Single-call pipeline and batch executor (guide sections 5 and 6).

``run_call`` runs one tool call through the full pipeline and always returns an
envelope::

    policy -> cancellation -> input guardrails -> span
           -> circuit breaker -> retry + timeout -> fn
           -> output guardrails -> metrics -> envelope

``run_call`` never raises. ``Executor`` (in :mod:`.registry`) runs batches with
read-parallel / write-sequential execution, preserves call order, and isolates sibling
failures.
"""
from __future__ import annotations

import random
import time
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeout
from dataclasses import dataclass, field
from typing import Any

from .errors import ErrorCode, ToolError
from .guardrails import EMPTY, GuardrailPipeline, Tripwire
from .observability import Metrics, NullTracer, Tracer
from .policy import Decision, ToolPolicy

ToolFn = Callable[..., Any]

# Separate pools: batch workers submit inner timeout tasks, so sharing one pool could
# deadlock when every worker waits on a nested future.
BATCH_EXECUTOR = ThreadPoolExecutor(max_workers=8, thread_name_prefix="thinktocad-batch")
CALL_EXECUTOR = ThreadPoolExecutor(max_workers=8, thread_name_prefix="thinktocad-call")


@dataclass
class RetryPolicy:
    """Retry transient failures silently with exponential backoff and jitter."""

    max_attempts: int = 3
    base_delay_s: float = 0.05
    max_delay_s: float = 1.0
    jitter: bool = True

    def delay(self, attempt: int) -> float:
        raw = min(self.max_delay_s, self.base_delay_s * (2 ** (attempt - 1)))
        if self.jitter:
            raw *= 0.5 + random.random()
        return raw


class CircuitBreaker:
    """closed -> open (fail fast) -> half-open (probe) -> closed."""

    def __init__(self, failure_threshold: int = 5, cooldown_s: float = 30.0) -> None:
        self.failure_threshold = failure_threshold
        self.cooldown_s = cooldown_s
        self._failures = 0
        self._opened_at = 0.0
        self.state = "closed"
        self.transitions: list[tuple[str, str]] = []

    def _transition(self, to: str) -> None:
        if to != self.state:
            self.transitions.append((self.state, to))
            self.state = to

    def allow(self) -> bool:
        if self.state == "open":
            if time.perf_counter() - self._opened_at >= self.cooldown_s:
                self._transition("half-open")
                return True
            return False
        return True

    def record(self, ok: bool) -> None:
        if ok:
            self._failures = 0
            self._transition("closed")
            return
        self._failures += 1
        if self.state == "half-open" or self._failures >= self.failure_threshold:
            self._opened_at = time.perf_counter()
            self._transition("open")


@dataclass
class ExecutionContext:
    """Everything the pipeline needs; sensible defaults make it optional."""

    tracer: Tracer = field(default_factory=NullTracer)
    metrics: Metrics = field(default_factory=Metrics)
    policy: ToolPolicy | None = None
    guardrails: GuardrailPipeline = field(default_factory=lambda: EMPTY)
    retry: RetryPolicy = field(default_factory=RetryPolicy)
    breaker: CircuitBreaker | None = None
    approved: bool = False
    cancelled: bool = False


def error_envelope(
    code: str,
    message: str,
    *,
    retryable: bool = False,
    suggested_fix: str | None = None,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "ok": False,
        "data": None,
        "error": {
            "code": code,
            "message": message,
            "retryable": retryable,
            "suggested_fix": suggested_fix,
            "details": details or {},
        },
    }


def _call_with_timeout(fn: ToolFn, args: dict[str, Any], timeout_s: float | None) -> Any:
    if not timeout_s:
        return fn(**args)
    future = CALL_EXECUTOR.submit(fn, **args)
    try:
        return future.result(timeout=timeout_s)
    except FuturesTimeout:
        raise ToolError(
            ErrorCode.TIMEOUT,
            f"tool exceeded its {timeout_s:g}s budget",
            suggested_fix="reduce the request scope or raise this tool's timeout",
        ) from None


def _finish(ctx: ExecutionContext, name: str, started: float, envelope: dict[str, Any]) -> dict:
    ctx.metrics.observe(f"tool.duration[{name}]", time.perf_counter() - started)
    if not envelope["ok"]:
        ctx.metrics.inc(f"tool.errors[{name}]")
    return envelope


def run_call(
    *,
    name: str,
    fn: ToolFn,
    args: dict[str, Any],
    ctx: ExecutionContext,
    side_effect: str = "read",
    timeout_s: float | None = 30.0,
    call_id: str = "",
    retryable: bool = True,
    max_attempts: int | None = None,
) -> dict[str, Any]:
    """Run one tool call through the full pipeline; never raises."""
    started = time.perf_counter()
    ctx.metrics.inc(f"tool.calls[{name}]")

    if ctx.policy is not None:
        decision = ctx.policy.evaluate(name, args)
        if decision is Decision.DENY:
            return _finish(ctx, name, started, error_envelope(
                ErrorCode.POLICY_DENIED, f"policy denied tool: {name}",
                suggested_fix="this tool is not permitted by the current policy"))
        if decision is Decision.ASK and not ctx.approved:
            return _finish(ctx, name, started, error_envelope(
                ErrorCode.APPROVAL_REQUIRED, f"approval required for tool: {name}",
                retryable=True, suggested_fix="approve, then replay with approved=true"))

    if ctx.cancelled:
        return _finish(ctx, name, started,
                       error_envelope(ErrorCode.CANCELLED, "run cancelled"))

    try:
        args = ctx.guardrails.run_input(name, args)
    except Tripwire as exc:
        return _finish(ctx, name, started, error_envelope(
            ErrorCode.GUARDRAIL_TRIPPED, f"input guardrail tripped: {exc}"))

    attributes = {
        "gen_ai.operation.name": "execute_tool",
        "gen_ai.tool.name": name,
        "gen_ai.tool.call.id": call_id,
        "thinktocad.side_effect": side_effect,
    }
    attempts = 1 if not retryable else (max_attempts or ctx.retry.max_attempts)

    with ctx.tracer.span(f"gen_ai.tool.call {name}", attributes) as span:
        if ctx.breaker is not None and not ctx.breaker.allow():
            span.error = ErrorCode.CIRCUIT_OPEN
            return _finish(ctx, name, started, error_envelope(
                ErrorCode.CIRCUIT_OPEN, f"circuit open for tool: {name}", retryable=True,
                suggested_fix="wait for the cooldown, then retry"))

        last_error: dict[str, Any] | None = None
        for attempt in range(1, attempts + 1):
            try:
                data = _call_with_timeout(fn, args, timeout_s)
                if ctx.breaker is not None:
                    ctx.breaker.record(True)
                try:
                    data = ctx.guardrails.run_output(name, data)
                except Tripwire as exc:
                    span.error = ErrorCode.GUARDRAIL_TRIPPED
                    return _finish(ctx, name, started, error_envelope(
                        ErrorCode.GUARDRAIL_TRIPPED, f"output guardrail tripped: {exc}"))
                return _finish(ctx, name, started, {"ok": True, "data": data, "error": None})
            except ToolError as exc:
                last_error = exc.to_error()
                if ctx.breaker is not None:
                    ctx.breaker.record(False)
                if not exc.retryable or attempt >= attempts:
                    span.error = exc.code
                    return _finish(ctx, name, started,
                                   {"ok": False, "data": None, "error": last_error})
                time.sleep(ctx.retry.delay(attempt))
            except Exception as exc:  # noqa: BLE001 - the whole point: never raise
                span.error = ErrorCode.INTERNAL_ERROR
                if ctx.breaker is not None:
                    ctx.breaker.record(False)
                return _finish(ctx, name, started, error_envelope(
                    ErrorCode.INTERNAL_ERROR, f"{type(exc).__name__}: {exc}",
                    suggested_fix="report this as a bug; do not retry unchanged"))

        return _finish(ctx, name, started,
                       {"ok": False, "data": None, "error": last_error})
