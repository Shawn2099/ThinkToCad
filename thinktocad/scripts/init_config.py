"""Write the ThinkToCad MCP server config for a client (installability).

Usage::

    thinktocad-init --client opencode          # ./opencode.json
    thinktocad-init --client vscode            # ./.vscode/mcp.json
    thinktocad-init --client claude --root C:\\path\\to\\repo
    thinktocad-init --client cursor

``--root`` is passed to the server as ``--root PATH`` (transport-agnostic, works even
when the client's working directory is not the repo). The command is idempotent: if the
target file exists it is merged, not overwritten.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Callable

SERVER = "thinktocad"
BIN = "thinktocad-mcp"


def _argv(root: str | None) -> list[str]:
    return [BIN] + (["--root", root] if root else [])


def _opencode(root: str | None) -> dict[str, Any]:
    return {
        "mcp": {
            "servers": {
                SERVER: {
                    "type": "local",
                    "timeout": {"startup": 180000},
                    "command": _argv(root),
                }
            }
        }
    }


def _stdio_entry(root: str | None) -> dict[str, Any]:
    entry: dict[str, Any] = {"type": "stdio", "command": BIN}
    if root:
        entry["args"] = ["--root", root]
    return entry


def _vscode(root: str | None) -> dict[str, Any]:
    return {"servers": {SERVER: _stdio_entry(root)}}


def _claude(root: str | None) -> dict[str, Any]:
    return {"mcpServers": {SERVER: _stdio_entry(root)}}


#: client -> (relative config path, builder)
CLIENTS: dict[str, tuple[str, Callable[[str | None], dict[str, Any]]]] = {
    "opencode": ("opencode.json", _opencode),
    "vscode": (".vscode/mcp.json", _vscode),
    "claude": ("claude_desktop_config.json", _claude),
    "cursor": (".cursor/mcp.json", _claude),
}


def _deep_merge(base: dict, new: dict) -> dict:
    """Merge ``new`` into ``base`` recursively; ``new`` wins on conflicts."""
    result = dict(base)
    for key, value in new.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def write_config(client: str, directory: str | Path, root: str | None = None) -> Path:
    """Write (or merge) the MCP config for ``client`` under ``directory``."""
    if client not in CLIENTS:
        raise ValueError(f"unknown client: {client!r}; use {sorted(CLIENTS)}")
    filename, builder = CLIENTS[client]
    target = Path(directory) / filename
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists():
        existing = json.loads(target.read_text(encoding="utf-8") or "{}")
        merged = _deep_merge(existing, builder(root))
    else:
        merged = builder(root)

    target.write_text(json.dumps(merged, indent=2) + "\n", encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="Write the ThinkToCad MCP client config.")
    parser.add_argument("--client", required=True, choices=sorted(CLIENTS))
    parser.add_argument("--path", default=".", help="directory to write the config into")
    parser.add_argument("--root", default=None, help="repo root (passed to the server)")
    args = parser.parse_args()

    target = write_config(args.client, args.path, args.root)
    print(f"wrote {target}")
    print("restart your client to load the thinktocad MCP server.")


if __name__ == "__main__":
    main()
