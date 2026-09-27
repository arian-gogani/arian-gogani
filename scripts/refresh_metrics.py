#!/usr/bin/env python3
"""Refresh only measured GitHub metrics, then regenerate the README."""

from __future__ import annotations

import json
import os
import urllib.request
from datetime import date
from pathlib import Path

from render import DATA, load_profile, main as render_readme


def github_json(path: str) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "arian-gogani-profile-metrics",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def main() -> None:
    profile = load_profile()
    repo = github_json("/repos/arian-gogani/nobulex")
    before = (
        profile["metrics"]["nobulex_stars"],
        profile["metrics"]["nobulex_forks"],
    )
    after = (int(repo["stargazers_count"]), int(repo["forks_count"]))
    if before != after:
        profile["metrics"]["nobulex_stars"] = after[0]
        profile["metrics"]["nobulex_forks"] = after[1]
        profile["metrics"]["measured_at"] = date.today().isoformat()
        DATA.write_text(json.dumps(profile, indent=2) + "\n", encoding="utf-8")
    render_readme()


if __name__ == "__main__":
    main()
