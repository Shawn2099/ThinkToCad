"""Tests for the execution pipeline (guide sections 5 and 6).

Covers retry, circuit breaker, tracing/metrics, and batch execution
(read-parallel / write-sequential, order preservation, sibling isolation).
"""
from __future__ import annotations

import time

from thinktocad.tools.errors import ErrorCode, ToolError
from thinktocad.tools.execution import CircuitBreaker, ExecutionContext, RetryPolicy
from thinktocad.tools.observability import Metrics, RecordingTracer
from thinktocad.tools.registry import ToolRegistry, safe_tool


def test_retries_transient_failure():
    registry = ToolRegistry()
    state = {"n": 0}

    @safe_tool(registry=registry, side_effect="read", max_retries=3, timeout_s=5)
    def flaky(x: int) -> dict:
        """Flaky."""
        state["n"] += 1
        if state["n"] < 3:
            raise ToolError(ErrorCode.TIMEOUT, "transient")
        return {"n": state["n"]}

    ctx = ExecutionContext(retry=RetryPolicy(base_delay_s=0.0, jitter=False))
    envelope = registry.execute_with("flaky", {"x": 1}, ctx=ctx)
    assert envelope["ok"] is True
    assert envelope["data"]["n"] == 3
    assert state["n"] == 3


def test_does_not_retry_permanent_failure():
    registry = ToolRegistry()
    state = {"n": 0}

    @safe_tool(registry=registry, side_effect="read")
    def permanent(x: int) -> dict:
        """Permanent."""
        state["n"] += 1
        raise ToolError(ErrorCode.NOT_FOUND, "gone")

    envelope = registry.execute_with("permanent", {"x": 1}, ctx=ExecutionContext())
    assert envelope["ok"] is False
    assert envelope["error"]["code"] == "NOT_FOUND"
    assert state["n"] == 1


def test_circuit_breaker_opens():
    registry = ToolRegistry()

    @safe_tool(registry=registry, side_effect="read")
    def always_fail(x: int) -> dict:
        """Always fails."""
        raise ToolError(ErrorCode.BACKEND_UNAVAILABLE, "down")

    breaker = CircuitBreaker(failure_threshold=2, cooldown_s=60)
    ctx = ExecutionContext(breaker=breaker, retry=RetryPolicy(max_attempts=1))
    registry.execute_with("always_fail", {"x": 1}, ctx=ctx)
    registry.execute_with("always_fail", {"x": 1}, ctx=ctx)
    assert breaker.state == "open"

    envelope = registry.execute_with("always_fail", {"x": 1}, ctx=ctx)
    assert envelope["error"]["code"] == "CIRCUIT_OPEN"
    assert envelope["error"]["retryable"] is True


def test_tracing_and_metrics():
    registry = ToolRegistry()

    @safe_tool(registry=registry, side_effect="read")
    def hi(x: int) -> dict:
        """Hi."""
        return {"x": x}

    tracer = RecordingTracer()
    metrics = Metrics()
    ctx = ExecutionContext(tracer=tracer, metrics=metrics)
    registry.execute_with("hi", {"x": 1}, ctx=ctx)

    assert len(tracer.spans) == 1
    assert tracer.spans[0].attributes["gen_ai.tool.name"] == "hi"
    assert metrics.counters.get("tool.calls[hi]") == 1
    assert "tool.duration[hi]" in metrics.durations


def _batch_registry() -> ToolRegistry:
    registry = ToolRegistry()

    @safe_tool(registry=registry, side_effect="read", timeout_s=5)
    def slow_read(tag: str) -> dict:
        """Slow read."""
        time.sleep(0.2)
        return {"tag": tag}

    @safe_tool(registry=registry, side_effect="write", timeout_s=5)
    def write_it(tag: str) -> dict:
        """Write."""
        return {"wrote": tag}

    @safe_tool(registry=registry, side_effect="read", timeout_s=5)
    def boom(tag: str) -> dict:
        """Boom."""
        raise ToolError(ErrorCode.NOT_FOUND, "nope")

    return registry


def test_batch_reads_run_in_parallel_and_preserve_order():
    registry = _batch_registry()
    calls = [{"name": "slow_read", "args": {"tag": str(i)}} for i in range(4)]
    start = time.perf_counter()
    results = registry.execute_all(calls, ctx=ExecutionContext())
    elapsed = time.perf_counter() - start

    assert all(r["ok"] for r in results)
    assert [r["data"]["tag"] for r in results] == ["0", "1", "2", "3"]
    assert elapsed < 0.6  # sequential would be >= 0.8s


def test_batch_isolates_sibling_failures():
    registry = _batch_registry()
    calls = [
        {"name": "slow_read", "args": {"tag": "a"}},
        {"name": "boom", "args": {"tag": "b"}},
        {"name": "slow_read", "args": {"tag": "c"}},
    ]
    results = registry.execute_all(calls, ctx=ExecutionContext())
    assert results[0]["ok"] is True
    assert results[2]["ok"] is True
    assert results[1]["ok"] is False
    assert results[1]["error"]["code"] == "NOT_FOUND"


def test_batch_unknown_tool_returns_error_envelope():
    registry = _batch_registry()
    results = registry.execute_all([{"name": "nope", "args": {}}], ctx=ExecutionContext())
    assert results[0]["ok"] is False
    assert results[0]["error"]["code"] == "NOT_FOUND"
