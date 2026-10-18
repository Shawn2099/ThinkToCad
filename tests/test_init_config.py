"""Tests for the MCP client config writer (thinktocad-init)."""
from __future__ import annotations

import json

from thinktocad.scripts.init_config import CLIENTS, write_config


def test_write_opencode(tmp_path):
    path = write_config("opencode", tmp_path, root="C:/repo")
    data = json.loads(path.read_text(encoding="utf-8"))
    entry = data["mcp"]["servers"]["thinktocad"]
    assert entry["command"] == ["thinktocad-mcp"]
    assert entry["environment"]["THINKTOCAD_ROOT"] == "C:/repo"


def test_write_vscode(tmp_path):
    path = write_config("vscode", tmp_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["servers"]["thinktocad"]["type"] == "stdio"
    assert path.name == "mcp.json"


def test_merge_preserves_existing_servers(tmp_path):
    (tmp_path / "opencode.json").write_text(
        json.dumps({"mcp": {"servers": {"other": {"type": "local"}}}}), encoding="utf-8"
    )
    path = write_config("opencode", tmp_path)
    servers = json.loads(path.read_text(encoding="utf-8"))["mcp"]["servers"]
    assert "other" in servers
    assert "thinktocad" in servers


def test_all_clients_have_paths():
    assert set(CLIENTS) == {"opencode", "vscode", "claude", "cursor"}
