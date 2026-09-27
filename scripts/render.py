#!/usr/bin/env python3
"""Render the GitHub profile README from the canonical public profile data."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "profile.json"
README = ROOT / "README.md"


def load_profile() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def render(profile: dict) -> str:
    ident = profile["identity"]
    links = profile["links"]
    metrics = profile["metrics"]
    projects = profile["projects"]
    architecture = profile["architecture"]
    results = profile["external_results"]

    project_rows = "\n".join(
        f"| [**{p['name']}**]({p['url']}) | {p['description']} | {p['proof']} |"
        for p in projects
    )
    architecture_rows = "\n\n".join(
        f"**{a['step']} · {a['name']}**\n\n{a['description']}"
        for a in architecture
    )
    result_rows = "\n".join(
        f"- [**{r['label']}**]({r['url']}) - {r['detail']}" for r in results
    )

    return f'''<div align="center">

# Arian Gogani

**{ident['role']} · {ident['school']}**

{ident['bio']}

[Portfolio]({links['portfolio']}) · [Nobulex]({links['nobulex']}) · [LinkedIn]({links['linkedin']}) · [X]({links['x']})

</div>

## What I am building

I work on one question: **what did a successful-looking verification result actually check?**

My current work is Nobulex, an open-source decision-integrity gateway prototype for automated financial actions. The gateway is implemented and tested locally; it is not deployed in a customer production path. It keeps two questions separate:

1. **What does the available evidence establish?** `PASS`, `FAIL`, or `INDETERMINATE`.
2. **What may the system do next?** `PERMIT`, `BLOCK`, or `ESCALATE`.

That separation matters because missing or unreadable evidence should never quietly become approval.

## Measured, not rounded up

| {metrics['nobulex_stars']} | {metrics['nobulex_forks']} | {metrics['verification_fixtures']} | {metrics['merged_conformance_prs']} |
|:---:|:---:|:---:|:---:|
| stars on Nobulex | forks of Nobulex | executable research fixtures | merged conformance-harness PRs |

<sub>GitHub metrics measured {metrics['measured_at']}. Fixture and PR counts link to inspectable artifacts below.</sub>

## Architecture

```text
proposed action
      │
      ▼
evidence binding ──► PASS / FAIL / INDETERMINATE
      │
      ▼
bounded policy   ──► PERMIT / BLOCK / ESCALATE
      │
      ▼
signed decision receipt
```

{architecture_rows}

## Selected work

| Project | What it does | What is inspectable |
|---|---|---|
{project_rows}

## External results

{result_rows}

[**Open the complete Evidence Ledger →**]({links['portfolio']}/evidence.html)

The ledger separates normative changes, merged code, references, listings, open or closed contributions, and self-published research. A merge or listing is never presented as an endorsement.

## Working standard

I publish the command, the expected result, and the limitation beside the claim. If a result cannot establish something, it should say so. If I am wrong, the correction stays visible.

<sub>Canonical profile data: [`data/profile.json`](data/profile.json). This README is generated from it.</sub>
'''


def main() -> None:
    README.write_text(render(load_profile()), encoding="utf-8")


if __name__ == "__main__":
    main()
