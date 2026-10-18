"""ThinkToCad MCP server: build123d geometry creation.

Run: python -m thinktocad.mcp.build123d_server   (or `build123d-mcp` after pip install)
"""
from __future__ import annotations
import datetime
import subprocess
import sys
from pathlib import Path

try:
    from fastmcp import FastMCP
except ImportError:  # pragma: no cover
    FastMCP = None

def _find_root() -> Path:
    here = Path(__file__).resolve().parent
    for cand in [here, *here.parents]:
        if (cand / "knowledge").is_dir():
            return cand
    return here.parent.parent.parent

ROOT = _find_root()

mcp = FastMCP("thinktocad-build123d") if FastMCP else None


def _run_code_sandboxed(code: str, timeout: int = 120) -> dict:
    """Execute build123d code in a subprocess. Returns {ok, stdout, stderr, artifacts, workdir}."""
    workdir = ROOT / "output" / ("run_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f"))
    workdir.mkdir(parents=True, exist_ok=True)
    script = workdir / "part.py"
    script.write_text(code, encoding="utf-8")
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True, text=True, timeout=timeout, cwd=str(workdir),
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"timeout ({timeout}s)", "stdout": "", "stderr": "", "artifacts": [], "workdir": str(workdir)}
    artifacts = [str(p) for p in workdir.iterdir() if p.is_file() and p.suffix.lower() in (".step", ".stp", ".stl", ".dxf", ".png", ".json")]
    return {
        "ok": proc.returncode == 0,
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "artifacts": artifacts,
        "workdir": str(workdir),
        "error": None if proc.returncode == 0 else (proc.stderr.strip() or "non-zero exit"),
    }


if mcp is not None:
    @mcp.tool()
    def create_part(code: str, timeout: int = 120) -> dict:
        """Execute build123d Python code in a sandboxed subprocess.

        The code should build geometry and export it (e.g. export_step(part, 'out.step')).
        Returns {ok, stdout, stderr, artifacts, workdir, error}. The kernel is the referee.
        """
        return _run_code_sandboxed(code, timeout=timeout)

    @mcp.tool()
    def validate_code(code: str) -> dict:
        """Static check: compile the code without executing. Returns {ok, error}."""
        try:
            compile(code, "<thinktocad>", "exec")
            return {"ok": True, "error": None}
        except SyntaxError as e:
            return {"ok": False, "error": str(e)}


def main() -> None:
    if mcp is None:
        raise SystemExit("fastmcp not installed. Run: pip install fastmcp")
    mcp.run()


if __name__ == "__main__":
    main()
