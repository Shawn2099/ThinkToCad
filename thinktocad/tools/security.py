"""Security helpers: static code screening and path scoping (guide section 9).

Policy alone is not enough for untrusted code, so tools that execute model-generated
code or read model-provided paths screen them first. These are the first line of
defense, paired with the OS-level sandbox the executing tool provides (subprocess +
timeout + cwd isolation).
"""
from __future__ import annotations

import ast
from pathlib import Path

from .errors import ErrorCode, ToolError

#: Builtin calls that must never appear in model-generated CAD code.
DENIED_CALLS = {"eval", "exec", "compile", "__import__"}

#: ``module.attr`` calls that are refused (shell, network, destructive file ops).
DENIED_ATTR_CALLS = {
    ("os", "system"),
    ("os", "popen"),
    ("os", "remove"),
    ("os", "rmdir"),
    ("os", "unlink"),
    ("subprocess", "run"),
    ("subprocess", "Popen"),
    ("subprocess", "call"),
    ("subprocess", "check_output"),
    ("subprocess", "check_call"),
    ("shutil", "rmtree"),
    ("shutil", "move"),
    ("socket", "socket"),
    ("socket", "create_connection"),
    ("urllib", "urlopen"),
    ("requests", "get"),
    ("requests", "post"),
}

#: Modules that may not be imported at all.
DENIED_IMPORTS = {"subprocess", "socket", "ctypes", "shutil", "importlib", "requests", "urllib"}


def scan_code(code: str) -> list[str]:
    """Return the unsafe constructs in ``code`` (empty list means clean)."""
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        return [f"syntax error: {exc}"]

    findings: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id in DENIED_CALLS:
                findings.add(f"call to {func.id}()")
            elif isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
                if (func.value.id, func.attr) in DENIED_ATTR_CALLS:
                    findings.add(f"call to {func.value.id}.{func.attr}()")
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in DENIED_IMPORTS:
                    findings.add(f"import {alias.name}")
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".")[0] in DENIED_IMPORTS:
                findings.add(f"from {node.module} import ...")
    return sorted(findings)


def assert_safe_code(code: str) -> None:
    """Raise ``UNSAFE_CODE`` if ``code`` contains a refused construct."""
    findings = scan_code(code)
    if findings:
        raise ToolError(
            ErrorCode.UNSAFE_CODE,
            "refused unsafe code: " + "; ".join(findings),
            suggested_fix="remove shell/network/dynamic-execution constructs; CAD code "
            "should only use build123d and write artifacts",
            details={"findings": findings},
        )


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


class PathScope:
    """Restrict file access to a set of allowed roots (path-traversal defense)."""

    def __init__(self, roots: list[str | Path]) -> None:
        self.roots = [Path(root).resolve() for root in roots]

    def resolve(self, path: str | Path, base: Path | None = None) -> Path:
        candidate = Path(path)
        if not candidate.is_absolute():
            candidate = (base or self.roots[0]) / candidate
        resolved = candidate.resolve()
        if not any(_is_within(resolved, root) for root in self.roots):
            raise ToolError(
                ErrorCode.POLICY_DENIED,
                f"path outside the allowed roots: {resolved}",
                suggested_fix="write artifacts under the run directory",
                details={"roots": [str(root) for root in self.roots]},
            )
        return resolved
