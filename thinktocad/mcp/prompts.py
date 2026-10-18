"""MCP prompts: the design flow, stage guidance, and DFM rules as user-invoked templates.

Prompts are user-controlled (guide section 8); clients surface them as slash-commands.
This is how the ThinkToCad *skill* reaches MCP-only clients (OpenCode, VS Code) that have
no skills directory.
"""
from __future__ import annotations

from typing import Any

from .. import flow
from ..tools.verification import dfm_rules_for

_STAGE_HINTS: dict[flow.Stage, str] = {
    flow.Stage.IDEATE: (
        "Capture the idea, usage context, sketches, candidate mechanisms, and the "
        "MANUFACTURING PROFILE (tools, materials, tolerances, batch size)."
    ),
    flow.Stage.RESEARCH: (
        "Search the knowledge base (list_mechanisms, retrieve_knowledge) and trusted "
        "sources; shortlist 2-4 mechanisms; write trusted findings back (T1-T4)."
    ),
    flow.Stage.SPECIFY: (
        "Emit a contract: every constraint a number or stock size. Run check_contract "
        "and pass gate G1 (check_gate)."
    ),
    flow.Stage.BUILD: (
        "Plan then construct. Sim first (matlab-mcp), then model (build123d-mcp). "
        "Enforce DFM with dfm_check."
    ),
    flow.Stage.VALIDATE: (
        "Verify with freecad-mcp (validity, interference=0, clearance, mass) and MATLAB "
        "gates; check determinism; pass gate G2 (check_gate)."
    ),
    flow.Stage.REVIEW: (
        "Render, run the advisory VLM check, then let the user interact in FreeCAD "
        "(the final word). Gate G4."
    ),
    flow.Stage.DELIVER: (
        "TechDraw + BOM + git commit; pass gate G3 (parameter extremes, specs green, "
        "deterministic)."
    ),
    flow.Stage.LEARN: (
        "Write attempt_N.yaml (pass or fail) and lessons; update graph.yaml."
    ),
}


def flow_text() -> str:
    """The full 8-stage flow and its four gates."""
    lines = ["# ThinkToCad design flow", "", "Stages:"]
    for index, stage in enumerate(flow.STAGE_ORDER, 1):
        gate = flow.STAGE_GATE.get(stage)
        suffix = f"  [gate {gate}]" if gate else ""
        lines.append(f"{index}. {stage.value}{suffix} - {_STAGE_HINTS[stage]}")
    lines += [
        "",
        "Gates (must pass before advancing):",
        "- G1 confidence: mean of "
        + ", ".join(flow.CONFIDENCE_SUBSCORES)
        + f" >= {flow.CONFIDENCE_THRESHOLD}",
        "- G2 verification: every check passes, deterministic, credibility tier recorded",
        "- G3 publish: rebuild at parameter extremes, all specs green",
        "- G4 human: the user approves (the final word)",
        "",
        "Verification order: backend tools (build123d/FreeCAD/MATLAB via MCP) -> advisory "
        "VLM render check -> the user in FreeCAD.",
        "The kernel is the referee: never declare a part valid yourself.",
    ]
    return "\n".join(lines)


def stage_text(stage: str) -> str:
    """Guidance for a single stage."""
    try:
        selected = flow.Stage(stage.strip().lower())
    except ValueError:
        valid = ", ".join(item.value for item in flow.STAGE_ORDER)
        return f"Unknown stage {stage!r}. Valid stages: {valid}."
    lines = [f"# Stage: {selected.value}", _STAGE_HINTS[selected]]
    gate = flow.STAGE_GATE.get(selected)
    if gate:
        lines.append(f"Before leaving this stage, pass gate {gate} (use the check_gate tool).")
    return "\n".join(lines)


def dfm_text(process: str) -> str:
    """DFM minimums for a process."""
    rules = dfm_rules_for(process)
    if not rules:
        from ..tools.verification import _DFM_RULES

        return f"Unknown process {process!r}. Known: {', '.join(sorted(_DFM_RULES))}."
    lines = [f"# DFM rules: {process}"]
    lines += [f"- {key}: >= {value} mm" for key, value in rules.items()]
    lines.append("Use the dfm_check tool to enforce these.")
    return "\n".join(lines)


def register_prompts(mcp: Any) -> None:
    """Register the flow / stage / DFM prompts on a FastMCP server."""

    @mcp.prompt(description="The ThinkToCad 8-stage design flow and its four gates.")
    def design_flow() -> str:
        """Return the full design flow and gates."""
        return flow_text()

    @mcp.prompt(description="Guidance for one stage of the design flow.")
    def design_stage(stage: str) -> str:
        """Return guidance for one stage (ideate, research, specify, build, validate, review, deliver, learn)."""
        return stage_text(stage)

    @mcp.prompt(description="DFM rules for a manufacturing process.")
    def dfm_rules(process: str) -> str:
        """Return minimum DFM values (fdm, sla, sheet_metal, cast, machining, hand_tools)."""
        return dfm_text(process)
