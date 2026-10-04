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
    check(len(data["projects"]) == 4, "selected project count changed")
    check(any(p["name"] == "Surka" and "No completed real-world swaps" in p["proof"] for p in data["projects"]), "Surka entry omits its traction limit")
    check(len(data["architecture"]) == 4, "architecture must retain four explicit stages")
    achievements = data["achievements"]
    check(len(achievements) == 19, "evidence ledger count changed")
    check([item["rank"] for item in achievements] == list(range(1, 20)), "ledger ranking is not contiguous")
    check(all(item["links"] for item in achievements), "an achievement has no public evidence link")
    check(all(item["caveat"] for item in achievements), "an achievement omits its limitation")
    check(any(item["status"] == "Approved by one reviewer; open" and any("/pull/2217" in link["url"] for link in item["links"]) for item in achievements), "open OWASP approval is missing or overstated")

    subprocess.run([sys.executable, str(ROOT / "scripts" / "render.py")], check=True)
    rendered = README.read_text(encoding="utf-8")
    check("Granite Bay High School" in rendered, "generated README omits school")
    check("PASS / FAIL / INDETERMINATE" in rendered, "evidence states are missing")
    check("PERMIT / BLOCK / ESCALATE" in rendered, "decision states are missing")
    check("prototype" in rendered.lower(), "generated README does not identify the gateway as a prototype")
    check("not deployed" in rendered.lower(), "generated README omits deployment status")
    check("data/profile.json" in rendered, "canonical source is not disclosed")
    check("complete Evidence Ledger" in rendered, "generated README omits ledger link")
    check("Press kit" in rendered and "/press.html" in rendered, "generated README omits press kit")
    check("Link-check CI currently fails" not in json.dumps(data), "profile evidence data still reports a stale CI failure")
    check("killbill/killbill/pull/2320" in rendered and "killbill/killbill/pull/2321" in rendered, "generated README omits the two open billing fixes")
    print("profile checks passed")


if __name__ == "__main__":
    main()
