"""Tests for the full MCP surface: tools + resources + prompts, and the doctor."""
from __future__ import annotations

import asyncio

from fastmcp import Client

from thinktocad.mcp.server import build_server


def _run(coro):
    return asyncio.run(coro)


def _first_text(result) -> str:
    contents = getattr(result, "contents", result)
    item = contents[0]
    return getattr(item, "text", str(item))


def _prompt_text(result) -> str:
    messages = getattr(result, "messages", result)
    content = messages[0].content
    return getattr(content, "text", str(content))


def test_tools_resources_and_prompts_are_exposed():
    async def go():
        async with Client(build_server()) as client:
            tools = await client.list_tools()
            templates = await client.list_resource_templates()
            prompts = await client.list_prompts()
            return (
                sorted(t.name for t in tools),
                sorted(t.uri_template for t in templates),
                sorted(p.name for p in prompts),
            )

    tools, templates, prompts = _run(go())
    assert len(tools) == 10 and "check_gate" in tools
    assert "build_visual_check" in tools and "record_visual_check" in tools
    assert any("mechanisms" in uri for uri in templates)
    assert {"design_flow", "design_stage", "dfm_rules"} <= set(prompts)


def test_skill_resource_reads_skills_md():
    async def go():
        async with Client(build_server()) as client:
            return await client.read_resource("thinktocad://skill")

    text = _first_text(_run(go()))
    assert "ThinkToCad" in text


def test_mechanism_resource_reads_entry():
    async def go():
        async with Client(build_server()) as client:
            return await client.read_resource(
                "thinktocad://knowledge/mechanisms/spacer_sleeve"
            )

    assert "sleeve" in _first_text(_run(go())).lower()


def test_design_flow_prompt_mentions_all_gates():
    async def go():
        async with Client(build_server()) as client:
            return await client.get_prompt("design_flow")

    text = _prompt_text(_run(go()))
    for gate in ("G1", "G2", "G3", "G4"):
        assert gate in text


def test_design_stage_prompt_is_stage_specific():
    async def go():
        async with Client(build_server()) as client:
            return await client.get_prompt("design_stage", {"stage": "specify"})

    text = _prompt_text(_run(go()))
    assert "G1" in text and "specify" in text.lower()


def test_doctor_core_checks_pass():
    from thinktocad.scripts import doctor

    rows = doctor.checks()
    required_failures = [name for (name, ok, _detail, required) in rows if required and not ok]
    assert required_failures == []


def test_server_root_override(tmp_path):
    """`--root` makes the server read a different repo (client cwd independent)."""
    from thinktocad import paths

    original = paths.ROOT
    (tmp_path / "knowledge" / "mechanisms").mkdir(parents=True)
    (tmp_path / "SKILLS.md").write_text("# Fake skill", encoding="utf-8")
    try:

        async def go():
            async with Client(build_server(root=str(tmp_path))) as client:
                return await client.read_resource("thinktocad://skill")

        assert "Fake skill" in _first_text(_run(go()))
    finally:
        paths.set_root(original)
