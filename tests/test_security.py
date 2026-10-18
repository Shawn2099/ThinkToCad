"""Tests for the static code screen and path scoping (guide section 9)."""
from __future__ import annotations

import pytest

from thinktocad.tools.errors import ToolError
from thinktocad.tools.security import PathScope, assert_safe_code, scan_code


def test_scan_code_allows_build123d():
    code = "from build123d import *\npart = Box(10, 10, 10)\nexport_step(part, 'out.step')\n"
    assert scan_code(code) == []


def test_scan_code_flags_shell_and_network():
    findings = scan_code("import os\nos.system('rm -rf /')\n")
    assert any("os.system" in f for f in findings)

    findings = scan_code("import subprocess\nsubprocess.run(['ls'])\n")
    assert any("subprocess" in f for f in findings)


def test_scan_code_flags_dynamic_execution():
    findings = scan_code("eval('1+1')\n")
    assert any("eval()" in f for f in findings)


def test_scan_code_flags_syntax_error():
    assert scan_code("def broken(:\n") != []


def test_assert_safe_code_raises():
    with pytest.raises(ToolError) as info:
        assert_safe_code("import socket\nsocket.socket()\n")
    assert info.value.code == "UNSAFE_CODE"


def test_path_scope_allows_inside(tmp_path):
    scope = PathScope([tmp_path])
    assert scope.resolve("artifacts/out.step") == (tmp_path / "artifacts" / "out.step").resolve()


def test_path_scope_blocks_outside(tmp_path):
    scope = PathScope([tmp_path])
    with pytest.raises(ToolError) as info:
        scope.resolve(str(tmp_path.parent / "evil.txt"))
    assert info.value.code == "POLICY_DENIED"
