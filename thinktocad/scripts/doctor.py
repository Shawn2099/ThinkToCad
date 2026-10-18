"""Environment doctor: check the repo layout and the external CAD backends.

Usage::

    thinktocad-doctor

Exit code is non-zero when a *required* check fails (repo layout + core deps). Backend
checks (build123d, MATLAB, FreeCAD and their MCP servers) are warnings: they are needed
for the geometry/verify/sim stages but not for the knowledge layer.
"""
from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path

from .. import paths


def _module(name: str) -> bool:
    try:
        return importlib.util.find_spec(name) is not None
    except (ImportError, ValueError):
        return False


def _first(*candidates: str | None) -> str | None:
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    return None


def _glob_first(base: str, pattern: str) -> str | None:
    root = Path(base)
    if not root.is_dir():
        return None
    matches = sorted(root.glob(pattern))
    return str(matches[0]) if matches else None


def checks() -> list[tuple[str, bool, str, bool]]:
    """Return ``(name, ok, detail, required)`` rows."""
    home = Path.home()
    rows: list[tuple[str, bool, str, bool]] = [
        ("repo root", paths.ROOT.is_dir(), str(paths.ROOT), True),
        ("knowledge/", paths.KNOWLEDGE.is_dir(), "", True),
        ("contracts/", paths.CONTRACTS.is_dir(), "", True),
        ("memory/", paths.MEMORY.is_dir(), "", False),
        ("pyyaml", _module("yaml"), "", True),
        ("fastmcp", _module("fastmcp"), "", True),
        ("build123d", _module("build123d"), "", False),
        ("build123d-mcp", _module("build123d_mcp"), "", False),
    ]

    matlab = shutil.which("matlab") or _glob_first(
        r"C:\Program Files\MATLAB", "*/bin/matlab.exe"
    )
    rows.append(("MATLAB", bool(matlab), matlab or "", False))
    matlab_mcp = shutil.which("matlab-mcp-server-windows-x64") or _first(
        str(home / ".local" / "bin" / "matlab-mcp-server-windows-x64.exe")
    )
    rows.append(("MATLAB MCP", bool(matlab_mcp), matlab_mcp or "", False))

    freecad = shutil.which("FreeCAD") or _glob_first(
        r"C:\Program Files", "FreeCAD*/bin/FreeCAD.exe"
    )
    rows.append(("FreeCAD", bool(freecad), freecad or "", False))
    freecad_mcp = shutil.which("freecad-mcp") or _first(
        str(home / ".local" / "bin" / "freecad-mcp.exe")
    )
    rows.append(("FreeCAD MCP", bool(freecad_mcp), freecad_mcp or "", False))

    return rows


def main() -> None:
    print("ThinkToCad doctor\n")
    failures = 0
    for name, ok, detail, required in checks():
        mark = "PASS" if ok else ("FAIL" if required else "WARN")
        if not ok and required:
            failures += 1
        print(f"[{mark}] {name:<16} {detail}")
    print()
    if failures:
        print(f"{failures} required check(s) failed.")
        raise SystemExit(1)
    print("core checks passed; WARN lines are optional backends.")


if __name__ == "__main__":
    main()
