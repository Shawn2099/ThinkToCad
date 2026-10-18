"""Result-formatting helpers (guide section 7): token-efficient, steering truncation.

Return paths and ids plus status, not payloads. When truncating, point the model at the
efficient strategy instead of silently dropping data.
"""
from __future__ import annotations

from typing import Any


def paginate(
    items: list[Any], limit: int = 20, offset: int = 0, hint: str | None = None
) -> dict:
    """Window a list; sets ``truncated`` and a steering ``hint`` when more remain."""
    total = len(items)
    result = {
        "items": items[offset : offset + limit],
        "total": total,
        "offset": offset,
        "limit": limit,
    }
    if offset + limit < total:
        result["truncated"] = True
        result["hint"] = hint or "increase offset to page, or narrow with a filter"
    return result


def truncate_text(text: str, limit: int = 4000, hint: str | None = None) -> dict:
    """Clip long text; the hint steers toward the efficient strategy."""
    if len(text) <= limit:
        return {"text": text, "truncated": False}
    return {
        "text": text[:limit],
        "truncated": True,
        "total_chars": len(text),
        "hint": hint or 'use response_format="concise" or request a specific id',
    }


def artifact(path: str, kind: str | None = None) -> dict:
    """Reference an on-disk artifact by path instead of inlining its bytes."""
    return {"path": str(path), "kind": kind}
