<div align="center">

# Arian Gogani

**Student builder and open-source researcher · Granite Bay High School**

I build reproducible systems that test what AI verification actually checked, then turn the result into evidence a stranger can inspect.

[Portfolio](https://arian-gogani.github.io) · [Press kit](https://arian-gogani.github.io/press.html) · [Nobulex](https://nobulex.com) · [LinkedIn](https://www.linkedin.com/in/arian-gogani-nobulex/) · [X](https://x.com/nobulexlabs)

</div>

## What I am building

I work on one question: **what did a successful-looking verification result actually check?**

My current work is Nobulex, an open-source decision-integrity gateway prototype for automated financial actions. The gateway is implemented and tested locally; it is not deployed in a customer production path. It keeps two questions separate:

1. **What does the available evidence establish?** `PASS`, `FAIL`, or `INDETERMINATE`.
2. **What may the system do next?** `PERMIT`, `BLOCK`, or `ESCALATE`.

That separation matters because missing or unreadable evidence should never quietly become approval.

I am also testing a narrower billing question: when a dry run and final invoice share a missing price change, what independent check would catch it before issuance? [The Kill Bill case and two open fixes](https://nobulex.com/research-killbill-catalog-replay) are public. This is research, not a deployed billing product or customer validation.

## Measured, not rounded up

| 40 | 11 | 27 | 4 |
|:---:|:---:|:---:|:---:|
| stars on Nobulex | forks of Nobulex | executable research fixtures | merged conformance-harness PRs |

<sub>GitHub metrics measured 2026-10-01. Fixture and PR counts link to inspectable artifacts below.</sub>

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

**01 · Collect evidence**

Bind the proposed action to the exact inputs, sources, timestamps, and identities it depends on.

**02 · Establish status**

Return PASS, FAIL, or INDETERMINATE. Missing evidence never becomes a clean result.

**03 · Apply policy**

A bounded deterministic policy returns PERMIT, BLOCK, or ESCALATE.

**04 · Preserve the decision**

Sign a receipt that binds the action, evidence references, policy version, and outcome.

## Selected work

| Project | What it does | What is inspectable |
|---|---|---|
| [**Nobulex**](https://github.com/arian-gogani/nobulex) | Executable research on verification boundaries: skipped coverage, self-selected trust anchors, policy scope, log integrity, and ambiguous evidence. | 27 synthetic fixtures, six paired historical parser cases, and public CI. |
| [**Decision-integrity gateway**](https://github.com/arian-gogani/nobulex-registry) | A Python prototype that separates evidence status from execution policy before a financial action can proceed. | PASS, FAIL, or INDETERMINATE evidence feeds a separate PERMIT, BLOCK, or ESCALATE decision. |
| [**Fail-open corpus**](https://github.com/arian-gogani/failopen) | Minimal reproductions of evaluators and safety checks that can report success without completing the check their result appears to certify. | Each published case names its reproduction limits instead of generalizing from one defect. |
| [**Surka**](https://github.com/arian-gogani/surka) | A small app for keeping two-sided cross-promotion swaps on track, from agreed terms through delivery evidence and results. | The public app is live at [surka.vercel.app](https://surka.vercel.app). No completed real-world swaps or paying users are claimed. |

## External results

- [**Four conformance-harness pull requests merged**](https://github.com/ScopeBlind/agent-governance-testvectors/pulls?q=is%3Apr+author%3Aarian-gogani+is%3Amerged) - The public research distinguishes merged changes from endorsement and freshly reruns only the case it says it reruns.
- [**Two Kill Bill catalog-billing fixes proposed upstream**](https://nobulex.com/research-killbill-catalog-replay) - Open [PR #2320](https://github.com/killbill/killbill/pull/2320) and [PR #2321](https://github.com/killbill/killbill/pull/2321) have released-tag H2 invoice checks that were red before and green after. Current-master CI is unverified; these are proposals, not merged fixes or customer results.
- [**OWASP receipt-guidance update approved by a reviewer**](https://github.com/OWASP/CheatSheetSeries/pull/2217) - The narrowed PR is still open and under review. Approval is not a merge or endorsement.
- [**A verifier defect reproduced and fixed upstream**](https://github.com/ScopeBlind/agent-governance-testvectors/pull/24) - The maintainer reproduced the failure, released a corrected verifier, and confirmed all four negative checks.
- [**Verification-boundary research runs in public CI**](https://github.com/arian-gogani/nobulex/actions/workflows/verification-boundaries.yml) - The fixture expectations, historical replay metadata, and deliberate-regression checks are inspectable.

[**Open the complete Evidence Ledger →**](https://arian-gogani.github.io/evidence.html)

The ledger separates normative changes, merged code, references, listings, open or closed contributions, and self-published research. A merge or listing is never presented as an endorsement.

## Working standard

I publish the command, the expected result, and the limitation beside the claim. If a result cannot establish something, it should say so. If I am wrong, the correction stays visible.

<sub>Canonical profile data: [`data/profile.json`](data/profile.json). This README is generated from it.</sub>
