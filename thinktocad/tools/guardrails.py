"""Guardrail pipeline and tripwires (guide sections 6 and 9).

A guardrail is a callable ``(tool_name, payload) -> payload | None``:

* return ``None``  -> pass the payload through unchanged;
* return a value   -> replace the payload (input args or output data);
* raise ``Tripwire`` -> halt the call; the call returns ``GUARDRAIL_TRIPPED``.

Input guardrails can therefore skip or rewrite arguments (e.g. cache/override); output
guardrails can redact or replace results. Tripwires are for catastrophic violations.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

Guardrail = Callable[[str, Any], Any | None]


class Tripwire(Exception):
    """Raised by a guardrail to halt a call (terminal)."""


class GuardrailPipeline:
    def __init__(
        self,
        input_guardrails: list[Guardrail] | None = None,
        output_guardrails: list[Guardrail] | None = None,
    ) -> None:
        self.input_guardrails: list[Guardrail] = list(input_guardrails or [])
        self.output_guardrails: list[Guardrail] = list(output_guardrails or [])

    def run_input(self, name: str, args: dict[str, Any]) -> dict[str, Any]:
        for guardrail in self.input_guardrails:
            replacement = guardrail(name, args)
            if replacement is not None:
                args = replacement
        return args

    def run_output(self, name: str, data: Any) -> Any:
        for guardrail in self.output_guardrails:
            replacement = guardrail(name, data)
            if replacement is not None:
                data = replacement
        return data


#: A pipeline that changes nothing.
EMPTY = GuardrailPipeline()
