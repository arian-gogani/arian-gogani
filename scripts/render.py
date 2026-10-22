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

[Portfolio]({links['portfolio']}) · [Press kit]({links['portfolio']}/press.html) · [Nobulex]({links['nobulex']}) · [LinkedIn]({links['linkedin']}) · [X]({links['x']})

</div>

## What I am building

My current work is Nobulex: billing accuracy for usage-based products. Billing code can return success and still produce the wrong amount. I find a reproducible case, check that a regression test fails on the old behavior and passes on the fix, and state what I did not examine. [The Kill Bill case and two open fixes]({links['nobulex']}/research-killbill-catalog-replay) are public. This is research and a fixed-scope audit practice, not a deployed billing product or customer validation.

I also maintain a decision-integrity gateway prototype for automated financial actions. It is implemented and tested locally; it is not deployed in a customer production path. It keeps two questions separate:

1. **What does the available evidence establish?** `PASS`, `FAIL`, or `INDETERMINATE`.
2. **What may the system do next?** `PERMIT`, `BLOCK`, or `ESCALATE`.

That separation matters because missing or unreadable evidence should never quietly become approval.

## Measured, not rounded up

| {metrics['merged_conformance_prs']} |
|:---:|
| merged conformance-harness PRs |

<sub>Counted from merged pull requests #12, #15, #22, #23 and #24 in ScopeBlind's public conformance repository. These were prior agent-governance work, not billing customers.</sub>

## Prior prototype architecture

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
