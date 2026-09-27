#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "data" / "profile.json"
README = ROOT / "README.md"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(PROFILE.read_text(encoding="utf-8"))
    check(data["identity"]["name"] == "Arian Gogani", "canonical name drifted")
    check(data["identity"]["school"] == "Granite Bay High School", "school is missing")
    check(data["links"]["linkedin"].endswith("/arian-gogani-nobulex/"), "wrong LinkedIn profile")
    check("4017b0369" not in json.dumps(data), "old duplicate profile leaked into public identity data")
    check(len(data["projects"]) == 3, "selected project count changed")
    check(len(data["architecture"]) == 4, "architecture must retain four explicit stages")

    subprocess.run([sys.executable, str(ROOT / "scripts" / "render.py")], check=True)
    rendered = README.read_text(encoding="utf-8")
    check("Granite Bay High School" in rendered, "generated README omits school")
    check("PASS / FAIL / INDETERMINATE" in rendered, "evidence states are missing")
    check("PERMIT / BLOCK / ESCALATE" in rendered, "decision states are missing")
    check("data/profile.json" in rendered, "canonical source is not disclosed")
    print("profile checks: 10/10 passed")


if __name__ == "__main__":
    main()
