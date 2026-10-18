"""ThinkToCad runtime: Spec -> Build -> Validate -> Learn -> Deliver.

Implements a ReAct-shaped agentic loop with five termination conditions,
hook points, and the kernel-as-referee rule. MCP tool bodies are stubs until
the corresponding servers are implemented.
"""
from __future__ import annotations
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

import yaml

def _find_root() -> Path:
    here = Path(__file__).resolve().parent
    for cand in [here, *here.parents]:
        if (cand / "knowledge").is_dir():
            return cand
    return here.parent.parent.parent

ROOT = _find_root()
KNOWLEDGE = ROOT / "knowledge"
CONTRACTS = ROOT / "contracts"
MEMORY = ROOT / "memory"


@dataclass
class Contract:
    name: str
    function: str
    constraints: dict[str, Any]
    mechanisms: list[str]
    validation: list[dict[str, Any]]
    deliverables: list[str] = field(default_factory=list)


@dataclass
class ToolResult:
    call_id: str
    content: str
    is_error: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


# Hook type: (state) -> None or modified state
Hook = Callable[[dict[str, Any]], None]


class AgentLoop:
    """Minimal ReAct loop with termination conditions and hooks."""

    def __init__(self, max_turns: int = 20):
        self.max_turns = max_turns
        self.before_model: list[Hook] = []
        self.before_tools: list[Hook] = []
        self.after_turn: list[Hook] = []

    def run(self, initial_state: dict[str, Any], step_fn: Callable[[dict], dict]) -> dict[str, Any]:
        state = dict(initial_state)
        state.setdefault("turn", 0)
        state.setdefault("history", [])
        state.setdefault("done", False)
        state.setdefault("result", None)

        while not state["done"]:
            if self.max_turns is not None and state["turn"] >= self.max_turns:
                state["done"] = True
                state["termination"] = "max_turns_exceeded"
                break

            for h in self.before_model:
                h(state)

            # step_fn: one model turn -> {tool_calls: [...], final: str|None, handoff: str|None, ...}
            turn = step_fn(state)
            state["turn"] += 1

            if turn.get("final") is not None:
                state["done"] = True
                state["termination"] = "final_output"
                state["result"] = turn["final"]
                break

            if turn.get("handoff") is not None:
                state["done"] = True
                state["termination"] = "handoff"
                state["result"] = {"handoff": turn["handoff"]}
                break

            if turn.get("interrupt") is not None:
                state["done"] = True
                state["termination"] = "interrupt"
                state["result"] = {"interrupt": turn["interrupt"]}
                break

            if turn.get("tripwire"):
                state["done"] = True
                state["termination"] = "guardrail_tripwire"
                state["result"] = {"tripwire": turn["tripwire"]}
                break

            tool_calls = turn.get("tool_calls", [])
            if not tool_calls:
                # No tool calls and no final -> treat as final text
                state["done"] = True
                state["termination"] = "final_output"
                state["result"] = turn.get("text")
                break

            for h in self.before_tools:
                h(state)

            # Execute tool calls (sequential here; parallelize read-only in MCP layer)
            results: list[ToolResult] = []
            for tc in tool_calls:
                r = _execute_tool(tc)
                results.append(r)
                state["history"].append({"tool_call": tc, "result": r})

            state["last_results"] = results

            for h in self.after_turn:
                h(state)

        return state


def _execute_tool(tc: dict[str, Any]) -> ToolResult:
    """Dispatch a tool call. Returns ToolResult; never raises."""
    name = tc.get("name", "")
    args = tc.get("args", {}) or {}
    call_id = tc.get("call_id", "")
    try:
        if name == "build":
            return _tool_build(args, call_id)
        if name == "validate":
            return _tool_validate(args, call_id)
        if name == "simulate":
            return _tool_simulate(args, call_id)
        return ToolResult(call_id=call_id, content=f"unknown tool: {name}", is_error=True)
    except Exception as e:  # noqa: BLE001
        return ToolResult(call_id=call_id, content=f"{type(e).__name__}: {e}", is_error=True)


def _tool_build(args: dict[str, Any], call_id: str) -> ToolResult:
    code = args.get("code", "")
    # Sandbox: write to temp file, run with system python, capture output.
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(code)
        tmp = f.name
    try:
        proc = subprocess.run(
            [sys.executable, tmp],
            capture_output=True, text=True, timeout=60,
        )
        ok = proc.returncode == 0
        content = (proc.stdout or "") + ("\nSTDERR:\n" + proc.stderr if proc.stderr else "")
        return ToolResult(call_id=call_id, content=content.strip() or "(no output)",
                          is_error=not ok, metadata={"returncode": proc.returncode})
    except subprocess.TimeoutExpired:
        return ToolResult(call_id=call_id, content="timeout (60s)", is_error=True)
    finally:
        try:
            Path(tmp).unlink(missing_ok=True)
        except OSError:
            pass


def _tool_validate(args: dict[str, Any], call_id: str) -> ToolResult:
    # TODO: call freecad MCP (mass, interference, clearance). Stub.
    return ToolResult(call_id=call_id, content="validate: not implemented (freecad MCP)", is_error=True)


def _tool_simulate(args: dict[str, Any], call_id: str) -> ToolResult:
    # TODO: call matlab MCP. Stub.
    return ToolResult(call_id=call_id, content="simulate: not implemented (matlab MCP)", is_error=True)


def load_contract(name: str) -> Contract:
    with open(CONTRACTS / f"{name}.yaml") as f:
        d = yaml.safe_load(f)
    return Contract(**d)


def retrieve_knowledge(mechanisms: list[str]) -> dict[str, Any]:
    """Look up mechanisms/constraints/lessons. Minimal: read matching files."""
    result: dict[str, Any] = {"mechanisms": [], "constraints": [], "lessons": []}
    for m in mechanisms:
        p = KNOWLEDGE / "mechanisms" / f"{m}.md"
        if p.exists():
            result["mechanisms"].append({"id": m, "text": p.read_text(encoding="utf-8")})
    # Always include all constraints
    cdir = KNOWLEDGE / "constraints"
    if cdir.exists():
        for p in cdir.glob("*.md"):
            result["constraints"].append({"id": p.stem, "text": p.read_text(encoding="utf-8")})
    return result


def save_memory(contract: Contract, result: dict[str, Any], verification: dict[str, Any]) -> None:
    target_dir = MEMORY / "designs" / contract.name
    target_dir.mkdir(parents=True, exist_ok=True)
    attempts = list(target_dir.glob("attempt_*.yaml"))
    n = len(attempts) + 1
    import datetime
    payload = {
        "mechanism": result.get("mechanism"),
        "status": "passed" if verification.get("pass") else "failed",
        "verification": verification,
        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    with open(target_dir / f"attempt_{n}.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(payload, f, sort_keys=False)


def design(contract_name: str, step_fn: Callable[[dict], dict]) -> dict[str, Any]:
    """Run the full design loop for a contract."""
    contract = load_contract(contract_name)
    knowledge = retrieve_knowledge(contract.mechanisms)

    initial_state = {
        "contract": contract,
        "knowledge": knowledge,
        "constraints": contract.constraints,
        "mechanisms": contract.mechanisms,
        "mechanism_index": 0,
    }

    loop = AgentLoop(max_turns=20)
    # Hook: log turn count
    def log_turn(state):
        pass
    loop.after_turn.append(log_turn)

    state = loop.run(initial_state, step_fn)

    if state.get("termination") == "final_output" and state.get("result"):
        save_memory(contract, {"mechanism": state.get("mechanism")}, {"pass": True})
    return state


if __name__ == "__main__":
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "example_part"
    print(f"Contract '{name}' loaded. Implement step_fn to run the loop.")
    c = load_contract(name) if (CONTRACTS / f"{name}.yaml").exists() else None
    if c:
        print(c)
