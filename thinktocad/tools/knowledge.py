"""Knowledge-base tools: list, retrieve, and recall mechanisms / constraints / lessons.

Read-only. The knowledge base is the differentiator of ThinkToCad
(``reports/Agentic CAD tooling landscape.md``); these tools expose it as structured data
instead of prose RAG, and ``recall`` closes the learning loop by reading past attempts
and lessons back.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

from .. import paths
from .registry import safe_tool

_FUNCTION_RE = re.compile(r"\*\*Function:\*\*\s*(.+)", re.IGNORECASE)


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _mechanism_ids() -> list[str]:
    directory = paths.KNOWLEDGE / "mechanisms"
    if not directory.is_dir():
        return []
    return sorted(p.stem for p in directory.glob("*.md") if p.stem.lower() != "readme")


def _clip(text: str, response_format: str, concise_limit: int = 700) -> str:
    if response_format == "detailed" or len(text) <= concise_limit:
        return text
    return text[:concise_limit].rstrip() + "\n… (truncated; use response_format=\"detailed\")"


@safe_tool(side_effect="read", timeout_s=15)
def list_mechanisms(response_format: str = "concise") -> dict:
    """List every mechanism in the ThinkToCad knowledge base.

    Use this first to discover candidate mechanisms by id (snake_case) before pulling
    full entries with retrieve_knowledge. Prefer this over reading the
    knowledge/mechanisms directory directly. Side effect: read-only.

    Args:
        response_format: "concise" (ids only) or "detailed" (id plus its one-line
            Function).
    """
    ids = _mechanism_ids()
    if response_format == "detailed":
        items = []
        for mid in ids:
            text = _read(paths.KNOWLEDGE / "mechanisms" / f"{mid}.md")
            match = _FUNCTION_RE.search(text)
            items.append({"id": mid, "function": match.group(1).strip() if match else ""})
        return {"count": len(items), "mechanisms": items}
    return {"count": len(ids), "mechanisms": ids}


@safe_tool(side_effect="read", timeout_s=20)
def retrieve_knowledge(
    mechanisms: list[str] | None = None,
    include_constraints: bool = True,
    include_lessons: bool = False,
    query: str | None = None,
    response_format: str = "concise",
) -> dict:
    """Retrieve knowledge entries (mechanisms, constraints, lessons) as structured data.

    Use during the Research and Specify stages to ground a design in known mechanisms
    and manufacturing constraints. Prefer targeted mechanism ids over a broad query.
    Side effect: read-only.

    Args:
        mechanisms: mechanism ids to fetch (see list_mechanisms).
        include_constraints: also return every knowledge/constraints/*.md entry.
        include_lessons: also return every knowledge/lessons/*.md entry.
        query: case-insensitive substring matched against mechanism ids when
            `mechanisms` is not given.
        response_format: "concise" (truncate long files) or "detailed" (full text).
    """
    result: dict = {"mechanisms": [], "constraints": [], "lessons": [], "missing": []}

    ids: list[str] = list(mechanisms) if mechanisms else []
    if not ids and query:
        needle = query.lower()
        ids = [m for m in _mechanism_ids() if needle in m]

    for mid in ids:
        path = paths.KNOWLEDGE / "mechanisms" / f"{mid}.md"
        if path.exists():
            result["mechanisms"].append(
                {"id": mid, "text": _clip(_read(path), response_format)}
            )
        else:
            result["missing"].append(mid)

    if include_constraints:
        cdir = paths.KNOWLEDGE / "constraints"
        if cdir.is_dir():
            for path in sorted(cdir.glob("*.md")):
                if path.stem.lower() == "readme":
                    continue
                result["constraints"].append(
                    {"id": path.stem, "text": _clip(_read(path), response_format)}
                )

    if include_lessons:
        ldir = paths.KNOWLEDGE / "lessons"
        if ldir.is_dir():
            for path in sorted(ldir.glob("*.md")):
                if path.stem.lower() == "readme":
                    continue
                result["lessons"].append(
                    {"id": path.stem, "text": _clip(_read(path), response_format)}
                )

    return result


@safe_tool(side_effect="read", timeout_s=20)
def recall(
    design: str | None = None,
    query: str | None = None,
    include_attempts: bool = True,
    include_lessons: bool = True,
    limit: int = 20,
    response_format: str = "concise",
) -> dict:
    """Recall what past designs tried — attempts and lessons — before starting again.

    Closes the learning loop: read memory so a failed approach is not repeated. Returns
    the attempt records for a design and/or lessons whose text matches `query`. Call this
    at the start of Research/Specify. Side effect: read-only.

    Args:
        design: design name; returns memory/designs/<design>/attempt_*.yaml.
        query: case-insensitive substring matched against lesson text (and, when no
            design is given, against design directory names).
        include_attempts: include attempt records.
        include_lessons: include lessons.
        limit: maximum attempts and lessons returned.
        response_format: "concise" (truncate long lessons) or "detailed".
    """
    result: dict = {"design": design, "attempts": [], "lessons": [], "designs": []}
    designs_dir = paths.MEMORY / "designs"

    if design and include_attempts and (designs_dir / design).is_dir():
        files = sorted((designs_dir / design).glob("attempt_*.yaml"))
        for path in files[-limit:]:
            try:
                result["attempts"].append(
                    {"file": path.name, "record": yaml.safe_load(_read(path)) or {}}
                )
            except yaml.YAMLError:
                result["attempts"].append({"file": path.name, "record": None})

    if query and not design and designs_dir.is_dir():
        needle = query.lower()
        result["designs"] = sorted(
            p.name for p in designs_dir.iterdir() if p.is_dir() and needle in p.name.lower()
        )[:limit]

    if include_lessons:
        lessons_dir = paths.KNOWLEDGE / "lessons"
        if lessons_dir.is_dir():
            needle = (query or "").lower()
            for path in sorted(lessons_dir.glob("*.md")):
                if path.stem.lower() == "readme":
                    continue
                text = _read(path)
                if needle and needle not in text.lower() and needle not in path.stem.lower():
                    continue
                result["lessons"].append(
                    {"id": path.stem, "text": _clip(text, response_format)}
                )
                if len(result["lessons"]) >= limit:
                    break

    return result
