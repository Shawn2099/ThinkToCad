"""Visual self-check payloads (Seek-CAD / CADSmith pattern).

The VLM check is **advisory**: exact kernel/MATLAB metrics are primary, the VLM screens
for the human, and the human is the final word. This module builds the payload the host
agent feeds to its vision model, and the record written back to memory.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class VisualCheck:
    """A request for a vision-model verdict on a rendered part or assembly."""

    design: str
    render_path: str
    intent: str
    expected_features: list[str] = field(default_factory=list)
    views: list[str] = field(default_factory=lambda: ["iso", "front", "top"])
    stage: str = "part"  # "part" | "assembly"

    def prompt(self) -> str:
        features = "\n".join(f"- {f}" for f in self.expected_features) or "- (none listed)"
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
        }


def record_verdict(check: VisualCheck, verdict: str, notes: str = "") -> dict[str, Any]:
    """Normalise a vision-model verdict into a memory record."""
    passed = verdict.strip().upper().startswith("PASS")
    return {
        "design": check.design,
        "stage": check.stage,
        "render_path": check.render_path,
        "verdict": "PASS" if passed else "FAIL",
        "passed": passed,
        "notes": notes,
        "advisory": True,
        "authority": "advisory (kernel + MATLAB are primary; human decides)",
    }
