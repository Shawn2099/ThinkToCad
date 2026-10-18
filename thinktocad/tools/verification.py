"""DFM gate, design-flow gates, design memory, and trust-tiered lesson write-back.

* ``dfm_check``     - process-aware manufacturability gate (read).
* ``check_gate``    - evaluate a design-flow gate G1-G4 (read).
* ``save_attempt``  - append-only design memory with credibility + visual record (write).
* ``save_lesson``   - knowledge write-back guarded by trust tiers T1-T4 (write).
"""
from __future__ import annotations

import datetime as _dt
import re

import yaml

from .. import flow, paths
from .errors import ErrorCode, ToolError
from .registry import safe_tool

# Minimum practical values per process, synthesised from
# knowledge/constraints/manufacturing.md. Extend from the user's manufacturing profile.
_DFM_RULES: dict[str, dict[str, float]] = {
    "fdm": {"min_wall_mm": 1.0, "min_corner_radius_mm": 0.5, "min_hole_dia_mm": 1.5},
    "sla": {"min_wall_mm": 0.5, "min_corner_radius_mm": 0.2, "min_hole_dia_mm": 1.0},
    "sheet_metal": {
        "min_wall_mm": 1.0,
        "min_corner_radius_mm": 1.0,
        "min_hole_dia_mm": 1.0,
        "min_hole_edge_mm": 2.0,
    },
    "cast": {"min_wall_mm": 3.0, "min_corner_radius_mm": 3.0, "min_hole_dia_mm": 4.0},
    "machining": {"min_wall_mm": 0.8, "min_corner_radius_mm": 0.5, "min_hole_dia_mm": 1.0},
    "hand_tools": {"min_wall_mm": 2.0, "min_corner_radius_mm": 1.0, "min_hole_dia_mm": 3.0},
}

# feature metric -> DFM rule key
_METRIC_TO_RULE = {
    "wall_mm": "min_wall_mm",
    "corner_radius_mm": "min_corner_radius_mm",
    "hole_dia_mm": "min_hole_dia_mm",
    "hole_edge_mm": "min_hole_edge_mm",
}

# Trust tiers (WORKFLOW.md stage 8): higher number = higher trust.
_TRUST_RANK = {"T1": 4, "T2": 3, "T3": 2, "T4": 1}
_TRUST_RE = re.compile(r"^\s*Trust:\s*(T[1-4])\s*$", re.IGNORECASE | re.MULTILINE)


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.strip().lower()).strip("_") or "lesson"


def dfm_rules_for(process: str) -> dict[str, float] | None:
    """Return the DFM rule set for a process, or ``None`` if unknown."""
    return _DFM_RULES.get(process.strip().lower())


# --- manufacturing profile (the shop the user actually has) ----------------- #
_PROFILE_NAME = "manufacturing_profile.yaml"


def _profile_path():
    return paths.ROOT / _PROFILE_NAME


def _read_profile() -> dict | None:
    path = _profile_path()
    if not path.exists():
        return None
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return None


def _profile_primary_process() -> str | None:
    processes = (_read_profile() or {}).get("processes") or []
    return processes[0] if processes else None


@safe_tool(side_effect="read", timeout_s=10)
def dfm_check(
    process: str | None = None, features: dict | None = None, stock: dict | None = None
) -> dict:
    """Check proposed dimensions against manufacturing (DFM) rules for a process.

    Use during Specify and Build to enforce "design for manufacturing" for the shop the
    user actually has (captured at ideation). Returns {"passed": bool, "issues": [...]}
    with one issue per violated metric. Side effect: read-only.

    Args:
        process: one of fdm, sla, sheet_metal, cast, machining, hand_tools. If omitted,
            the primary process from the saved manufacturing profile is used.
        features: metric -> value in mm, e.g. {"wall_mm": 2.0,
            "corner_radius_mm": 1.0, "hole_dia_mm": 3.0, "hole_edge_mm": 5.0}.
        stock: optional preferred stock sizes, e.g. {"thickness_mm": [1, 2, 3]}; if
            given, thickness features not matching a stock size are flagged.
    """
    if process is None:
        process = _profile_primary_process()
    if process is None:
        raise ToolError(
            ErrorCode.INVALID_ARGUMENT,
            "no process given and no manufacturing profile saved",
            suggested_fix="pass a process, or call save_manufacturing_profile first",
        )
    rules = _DFM_RULES.get(process)
    if rules is None:
        raise ToolError(
            ErrorCode.INVALID_ARGUMENT,
            f"unknown process: {process}",
            suggested_fix=f"use one of: {', '.join(sorted(_DFM_RULES))}",
        )

    issues: list[dict] = []
    for metric, value in (features or {}).items():
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            issues.append({"metric": metric, "error": "value must be a number (mm)"})
            continue
        rule_key = _METRIC_TO_RULE.get(metric)
        if rule_key is None or rule_key not in rules:
            continue
        minimum = rules[rule_key]
        if value < minimum:
            issues.append(
                {
                    "metric": metric,
                    "value_mm": value,
                    "min_mm": minimum,
                    "process": process,
                    "severity": "blocker",
                }
            )

    if stock and stock.get("thickness_mm") and features.get("wall_mm") is not None:
        sizes = stock["thickness_mm"]
        if features["wall_mm"] not in sizes:
            issues.append(
                {
                    "metric": "wall_mm",
                    "value_mm": features["wall_mm"],
                    "allowed_stock_mm": sizes,
                    "severity": "warning",
                    "note": "not a preferred stock size",
                }
            )

    return {"process": process, "passed": not issues, "issues": issues}


@safe_tool(side_effect="read", timeout_s=10)
def check_gate(gate: str, inputs: dict) -> dict:
    """Evaluate a design-flow gate (G1-G4) and return its verdict.

    Gates: G1 confidence (subscores -> mean >= 0.80), G2 verification (all checks pass,
    deterministic, credibility tier recorded), G3 publish (extremes + specs + determinism),
    G4 human (approval). Call before advancing a stage; a stage cannot be left until its
    gate passes. Returns {"gate", "passed", "score", "reasons"}. Side effect: read-only.

    Args:
        gate: "G1", "G2", "G3", or "G4".
        inputs: gate-specific inputs. G1: {"subscores": {mechanism_fit, ...}}. G2:
            {"checks": [{"name","pass"}], "deterministic": bool, "credibility": str}.
            G3: {"extremes_ok": bool, "specs_green": bool, "deterministic": bool}.
            G4: {"approved": bool}.
    """
    key = gate.upper()
    if key not in flow.GATES:
        raise ToolError(
            ErrorCode.INVALID_ARGUMENT,
            f"unknown gate: {gate}",
            suggested_fix="use G1, G2, G3, or G4",
        )
    inputs = inputs or {}
    try:
        if key == "G1":
            return flow.confidence_gate(inputs.get("subscores", {}))
        if key == "G2":
            return flow.verification_gate(
                inputs.get("checks", []),
                bool(inputs.get("deterministic")),
                inputs.get("credibility"),
            )
        if key == "G3":
            return flow.publish_gate(
                bool(inputs.get("extremes_ok")),
                bool(inputs.get("specs_green")),
                bool(inputs.get("deterministic")),
            )
        return flow.human_gate(bool(inputs.get("approved")))
    except TypeError as exc:
        raise ToolError(
            ErrorCode.INVALID_ARGUMENT,
            f"bad inputs for {key}: {exc}",
            suggested_fix="see the tool description for the required inputs",
        ) from None


@safe_tool(side_effect="write", timeout_s=10)
def save_attempt(
    design: str,
    status: str,
    mechanism: str | None = None,
    verification: dict | None = None,
    notes: str | None = None,
    credibility: str | None = None,
    visual: dict | None = None,
) -> dict:
    """Append a design attempt record to memory/designs/<design>/attempt_N.yaml.

    Call after every build/validate cycle, pass or fail — failed attempts are as valuable
    as successes. The write is append-only and never overwrites. Side effect: write.

    Args:
        design: design name (matches the contract name).
        status: "passed", "failed", or "partial".
        mechanism: mechanism id that was tried.
        verification: verification summary (interference, clearance, mass, gates...).
        notes: free text — root cause or fix applied.
        credibility: ordered tier — critique_finding | surrogate_prediction |
            proxy_assembly_result | executed_solver_result.
        visual: the vision-model verdict record (see runtime.visual.record_verdict).
    """
    if status not in ("passed", "failed", "partial"):
        raise ToolError(
            ErrorCode.INVALID_ARGUMENT,
            f"invalid status: {status}",
            suggested_fix="use one of: passed, failed, partial",
        )
    target = paths.MEMORY / "designs" / design
    target.mkdir(parents=True, exist_ok=True)
    number = len(list(target.glob("attempt_*.yaml"))) + 1
    payload = {
        "design": design,
        "attempt": number,
        "status": status,
        "mechanism": mechanism,
        "verification": verification or {},
        "credibility": credibility,
        "visual": visual,
        "notes": notes,
        "timestamp": _dt.datetime.now().isoformat(timespec="seconds"),
    }
    path = target / f"attempt_{number}.yaml"
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    return {"path": str(path), "attempt": number}


@safe_tool(side_effect="write", timeout_s=10)
def save_lesson(
    title: str,
    body: str,
    trust: str = "T4",
    source: str | None = None,
    override: bool = False,
) -> dict:
    """Write a lesson or insight to knowledge/lessons/ with a trust tier (T1-T4).

    Tiers: T1 verified by tool, T2 cited standard/textbook, T3 heuristic, T4
    LLM-inferred. Never silently overwrites a higher-trust entry with a lower-trust one:
    if an existing lesson has an equal-or-higher tier, the write is refused unless
    override is true. Side effect: write.

    Args:
        title: short title; used as the filename (slugified).
        body: markdown — what happened / root cause / rule going forward.
        trust: "T1", "T2", "T3", or "T4".
        source: provenance (URL, standard, sim name).
        override: replace an equal-or-higher-trust lesson (requires new evidence).
    """
    if trust not in _TRUST_RANK:
        raise ToolError(
            ErrorCode.INVALID_ARGUMENT,
            f"invalid trust tier: {trust}",
            suggested_fix="use one of: T1, T2, T3, T4",
        )
    slug = _slug(title)
    lessons = paths.KNOWLEDGE / "lessons"
    lessons.mkdir(parents=True, exist_ok=True)
    path = lessons / f"{slug}.md"

    if path.exists() and not override:
        existing = _TRUST_RE.search(path.read_text(encoding="utf-8"))
        existing_tier = existing.group(1).upper() if existing else None
        if existing_tier and _TRUST_RANK[existing_tier] >= _TRUST_RANK[trust]:
            raise ToolError(
                ErrorCode.DESIGN_RULE_VIOLATION,
                f"refusing to overwrite a {existing_tier} lesson with {trust}: {slug}",
                suggested_fix="pass override=true only with new evidence",
                details={"existing_trust": existing_tier, "new_trust": trust},
            )

    content = (
        f"# {title}\n"
        f"Date: {_dt.date.today().isoformat()}\n"
        f"Trust: {trust}\n"
        f"Source: {source or 'n/a'}\n\n"
        f"{body.strip()}\n"
    )
    path.write_text(content, encoding="utf-8")
    return {"path": str(path), "slug": slug, "trust": trust}


@safe_tool(side_effect="read", timeout_s=10)
def get_manufacturing_profile() -> dict:
    """Read the saved manufacturing profile - the shop the user actually has.

    Returns {"profile": {...} | null, "path": str}. Capture it once during ideation with
    save_manufacturing_profile so the DFM gate and the agent reflect the real tools,
    materials and tolerances. Side effect: read-only.
    """
    return {"profile": _read_profile(), "path": str(_profile_path())}


@safe_tool(side_effect="write", timeout_s=10)
def save_manufacturing_profile(
    processes: list[str],
    materials: list[str] | None = None,
    tolerances: dict | None = None,
    batch_size: str | None = None,
    notes: str | None = None,
) -> dict:
    """Save the manufacturing profile captured at ideation.

    Records the processes the user actually has (fdm, sheet_metal, hand_tools, ...),
    available materials, achievable tolerances and batch size. The DFM gate reads this,
    so designs match the real shop. Side effect: write.

    Args:
        processes: available processes, e.g. ["hand_tools", "sheet_metal"].
        materials: available materials / stock, e.g. ["mild steel", "aluminium 6061"].
        tolerances: achievable tolerances, e.g. {"general_mm": 0.5, "machined_mm": 0.1}.
        batch_size: "one-off", "small", or "production".
        notes: free text - suppliers, constraints, tooling.
    """
    if not processes:
        raise ToolError(
            ErrorCode.INVALID_ARGUMENT,
            "at least one process is required",
            suggested_fix=f"use ids from: {', '.join(sorted(_DFM_RULES))}",
        )
    unknown = [name for name in processes if name not in _DFM_RULES]
    if unknown:
        raise ToolError(
            ErrorCode.INVALID_ARGUMENT,
            f"unknown process(es): {unknown}",
            suggested_fix=f"use ids from: {', '.join(sorted(_DFM_RULES))}",
        )
    profile = {
        "processes": list(processes),
        "materials": list(materials or []),
        "tolerances": dict(tolerances or {}),
        "batch_size": batch_size,
        "notes": notes,
        "saved": _dt.datetime.now().isoformat(timespec="seconds"),
    }
    path = _profile_path()
    path.write_text(yaml.safe_dump(profile, sort_keys=False), encoding="utf-8")
    return {"path": str(path), "profile": profile}
