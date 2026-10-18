"""Repo-root discovery shared by ThinkToCad tools.

Content directories (``knowledge/``, ``contracts/``, ``memory/``) live at the repo
root, not inside the package (see AGENTS.md). ``ROOT`` is resolved in this order:

1. the ``THINKTOCAD_ROOT`` environment variable, if set (recommended for MCP servers,
   whose working directory may be arbitrary);
2. the nearest ancestor of the current working directory containing a ``knowledge/``
   directory;
3. the nearest ancestor of this package containing ``knowledge/`` (editable installs).

Tool modules must reference these through the module (``paths.MEMORY``) rather than
importing the values, so tests can monkeypatch them.
"""
from __future__ import annotations

import os
from pathlib import Path


def find_root(start: Path | None = None) -> Path:
    env = os.environ.get("THINKTOCAD_ROOT")
    if env:
        return Path(env).expanduser().resolve()
    for base in (start or Path.cwd(), Path(__file__).resolve().parent):
        for cand in (base, *base.parents):
            if (cand / "knowledge").is_dir():
                return cand
    return Path.cwd()


ROOT = find_root()
KNOWLEDGE = ROOT / "knowledge"
CONTRACTS = ROOT / "contracts"
MEMORY = ROOT / "memory"


def set_root(root: str | Path) -> Path:
    """Override the resolved root at runtime (e.g. from a ``--root`` flag).

    Tool modules reference these through the module, so updating the globals here is
    picked up by every tool call.
    """
    global ROOT, KNOWLEDGE, CONTRACTS, MEMORY
    ROOT = Path(root).expanduser().resolve()
    KNOWLEDGE = ROOT / "knowledge"
    CONTRACTS = ROOT / "contracts"
    MEMORY = ROOT / "memory"
    return ROOT
