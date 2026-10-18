"""Visual self-check tools (Seek-CAD / CADSmith pattern).

The VLM check is **advisory**: exact kernel/MATLAB metrics are primary, the VLM screens
for the human, and the human is the final word. ``build_visual_check`` produces the
payload the host feeds to its vision model (render path + intent + expected features);
``record_visual_check`` stores the verdict in design memory.

These are portable tools that work with any client: the host's own LLM does the vision.
(MCP *sampling* could let the server call the client's model directly, but client support
is uneven, so the payload/record split is the safe default.)
"""
from __future__ import annotations

import datetime as _dt
import json
from dataclasses import dataclass, field
from typing import Any

from .. import paths
from .errors import ErrorCode, ToolError
from .registry import safe_tool

_VALID_STAGES = ("part", "assembly")


@dataclass
class VisualCheck:
    """A request for a vision-model verdict on a rendered part or assembly."""

    design: str
    render_path: str
    intent: str
    expected_features: list[str] = field(default_factory=list)
    views: list[str] = field(default_factory=lambda: ["iso", "front", "top"])
    stage: str = "part"

    def prompt(self) -> str:
        features = "\n".join(f"- {item}" for item in self.expected_features) or "- (none listed)"
        return (
            f"You are checking a CAD render for '{self.design}' ({self.stage}).\n"
            f"Intent: {self.intent}\n"
            f"Expected features:\n{features}\n\n"
            "Inspect the attached render(s) and answer:\n"
            "1. Are all expected features present and correctly oriented?\n"
            "2. Do the proportions match the intent?\n"
            "3. Any obvious defect (missing feature, wrong orientation, collision)?\n"
            "Reply with verdict PASS or FAIL, then one line per concern. This is advisory: "
            "the kernel and MATLAB metrics decide correctness; the human decides delivery."
        )

    def to_payload(self) -> dict[str, Any]:
        return {
            "design": self.design,
            "stage": self.stage,
            "render_path": self.render_path,
            "views": self.views,
            "intent": self.intent,
            "expected_features": self.expected_features,
            "prompt": self.prompt(),
            "advisory": True,
            "authority": "advisory (kernel + MATLAB are primary; human decides)",
        }


def _check(
    design: str,
    render_path: str,
    intent: str,
    expected_features: list[str] | None,
    stage: str,
    views: list[str] | None,
) -> VisualCheck:
    if stage not in _VALID_STAGES:
        raise ToolError(
            ErrorCode.INVALID_ARGUMENT,
            f"invalid stage: {stage}",
            suggested_fix=f"use one of: {', '.join(_VALID_STAGES)}",
        )
    return VisualCheck(
        design=design,
        render_path=render_path,
        intent=intent,
        expected_features=list(expected_features or []),
        stage=stage,
        views=list(views or ["iso", "front", "top"]),
    )


@safe_tool(side_effect="read", timeout_s=10)
def build_visual_check(
    design: str,
    render_path: str,
    intent: str,
    expected_features: list[str] | None = None,
    stage: str = "part",
    views: list[str] | None = None,
) -> dict:
    """Build a vision-model check payload for a rendered part or assembly.

    Use after a part is built or after assembly, BEFORE human review. Returns the render
    path, the intent, the expected features and a ready-to-send prompt. The verdict is
    advisory: kernel/MATLAB metrics decide correctness; the human has the final word.
    Side effect: read-only.

    Args:
        design: design name (matches the contract name).
        render_path: path to the rendered image (iso/ortho).
        intent: what the part or assembly must be, in one sentence.
        expected_features: features the render must show.
        stage: "part" or "assembly".
        views: which views the render contains (default iso, front, top).
    """
    return _check(design, render_path, intent, expected_features, stage, views).to_payload()


@safe_tool(side_effect="write", timeout_s=10)
def record_visual_check(
    design: str,
    render_path: str,
    verdict: str,
    notes: str = "",
    stage: str = "part",
) -> dict:
    """Record a vision-model verdict on a render into design memory.

    Writes memory/designs/<design>/visual_N.json. The verdict is advisory: it screens for
    the human but never overrides a kernel/MATLAB pass. Side effect: write.

    Args:
        design: design name.
        render_path: the rendered image that was checked.
        verdict: "PASS" or "FAIL" (free text starting with either is accepted).
        notes: one line per concern.
        stage: "part" or "assembly".
    """
    check = _check(design, render_path, "", [], stage, None)
    passed = verdict.strip().upper().startswith("PASS")
    record = {
        "design": design,
        "stage": check.stage,
        "render_path": render_path,
        "verdict": "PASS" if passed else "FAIL",
        "passed": passed,
        "notes": notes,
        "advisory": True,
        "authority": "advisory (kernel + MATLAB are primary; human decides)",
        "timestamp": _dt.datetime.now().isoformat(timespec="seconds"),
    }
    target = paths.MEMORY / "designs" / design
    target.mkdir(parents=True, exist_ok=True)
    number = len(list(target.glob("visual_*.json"))) + 1
    path = target / f"visual_{number}.json"
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return {"path": str(path), "visual": number, "passed": passed}
