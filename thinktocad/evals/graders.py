"""Reusable deterministic graders for eval tasks (guide section 11)."""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

Grader = Callable[[list[dict]], dict]


def all_succeeded(results: list[dict]) -> dict:
    ok = all(result.get("ok") for result in results)
    return {"passed": ok, "detail": f"{sum(bool(r.get('ok')) for r in results)}/{len(results)} ok"}


def tool_ok(index: int = 0) -> Grader:
    def grader(results: list[dict]) -> dict:
        result = results[index]
        return {"passed": bool(result.get("ok")), "detail": f"tool[{index}] ok={result.get('ok')}"}

    return grader


def data_at(index: int, path: str, expected: Any = None) -> Grader:
    """Assert a dotted path into ``results[index]["data"]``.

    ``expected=None`` only checks that the path exists.
    """

    def grader(results: list[dict]) -> dict:
        current: Any = results[index].get("data")
        for key in path.split("."):
            if isinstance(current, dict):
                current = current.get(key)
            elif isinstance(current, list) and key.lstrip("-").isdigit():
                position = int(key)
                current = (
                    current[position] if -len(current) <= position < len(current) else None
                )
            else:
                current = None
                break
        passed = current is not None if expected is None else current == expected
        return {"passed": passed, "detail": f"data[{index}].{path} = {current!r}"}

    return grader


def error_code(index: int, code: str) -> Grader:
    def grader(results: list[dict]) -> dict:
        error = results[index].get("error") or {}
        return {"passed": error.get("code") == code, "detail": f"code={error.get('code')!r}"}

    return grader
