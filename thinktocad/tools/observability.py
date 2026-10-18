"""Observability: per-tool spans and metrics (guide section 10).

Attribute names follow the OpenTelemetry GenAI semantic conventions so traces stay
portable across backends. Raw arguments and results are never recorded by default (they
may contain paths or secrets); only names, ids, durations and error types are.
"""
from __future__ import annotations

import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Any, Iterator, Protocol


@dataclass
class Span:
    name: str
    attributes: dict[str, Any] = field(default_factory=dict)
    start: float = field(default_factory=time.perf_counter)
    duration_s: float = 0.0
    error: str | None = None


class Tracer(Protocol):
    def span(
        self, name: str, attributes: dict[str, Any] | None = None
    ) -> Iterator[Span]: ...


class NullTracer:
    """A tracer that records nothing (the default)."""

    @contextmanager
    def span(
        self, name: str, attributes: dict[str, Any] | None = None
    ) -> Iterator[Span]:
        yield Span(name=name, attributes=dict(attributes or {}))


class RecordingTracer:
    """In-memory tracer for tests and debugging."""

    def __init__(self) -> None:
        self.spans: list[Span] = []

    @contextmanager
    def span(
        self, name: str, attributes: dict[str, Any] | None = None
    ) -> Iterator[Span]:
        span = Span(name=name, attributes=dict(attributes or {}))
        try:
            yield span
        except Exception as exc:  # noqa: BLE001 - record, then re-raise
            span.error = type(exc).__name__
            raise
        finally:
            span.duration_s = time.perf_counter() - span.start
            self.spans.append(span)


class Metrics:
    """Minimal counters and histograms (per-tool calls, errors, duration)."""

    def __init__(self) -> None:
        self.counters: dict[str, int] = {}
        self.durations: dict[str, list[float]] = {}

    def inc(self, name: str, value: int = 1) -> None:
        self.counters[name] = self.counters.get(name, 0) + value

    def observe(self, name: str, seconds: float) -> None:
        self.durations.setdefault(name, []).append(seconds)

    def snapshot(self) -> dict[str, Any]:
        summary: dict[str, Any] = {}
        for name, samples in self.durations.items():
            ordered = sorted(samples)
            summary[name] = {
                "count": len(ordered),
                "p50": ordered[len(ordered) // 2],
                "p95": ordered[min(len(ordered) - 1, int(len(ordered) * 0.95))],
                "max": ordered[-1],
            }
        return {"counters": dict(self.counters), "durations": summary}
