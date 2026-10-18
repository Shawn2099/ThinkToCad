"""Install ThinkToCad as a Claude Code / OpenCode skill.

Copies SKILLS.md + skills/ + knowledge/ into the user's skills directory
(default: ~/.claude/skills/thinktocad) so the agent loads it automatically.
"""
from __future__ import annotations
import argparse
import os
import shutil
from pathlib import Path

def _find_root() -> Path:
    # Walk up from this file until we find the directory containing SKILLS.md
    here = Path(__file__).resolve().parent
    for cand in [here, *here.parents]:
        if (cand / "SKILLS.md").exists():
            return cand
    return here.parent.parent.parent

ROOT = _find_root()
SKILL_FILES = ["SKILLS.md"]
SKILL_DIRS = ["skills", "knowledge", "contracts", "guides"]


def default_skills_dir() -> Path:
    # Claude Code / OpenCode convention
    base = Path(os.path.expanduser("~")) / ".claude" / "skills"
    return base / "thinktocad"


def install(target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for f in SKILL_FILES:
        src = ROOT / f
        if src.exists():
            shutil.copy2(src, target / f)
    for d in SKILL_DIRS:
        src = ROOT / d
        if src.exists():
            dst = target / d
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    print(f"Installed ThinkToCad skill to: {target}")
    print("Restart your agent (Claude Code / OpenCode) to load it.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Install ThinkToCad as an agent skill.")
    parser.add_argument("--target", type=Path, default=None,
                        help="Override skills install directory.")
    args = parser.parse_args()
    target = args.target or default_skills_dir()
    install(target)


if __name__ == "__main__":
    main()
