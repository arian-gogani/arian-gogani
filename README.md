<div align="center">

# Arian Gogani

**Student builder and open-source researcher · Granite Bay High School**

I build reproducible systems that test what AI verification actually checked, then turn the result into evidence a stranger can inspect.

[Portfolio](https://arian-gogani.github.io) · [Press kit](https://arian-gogani.github.io/press.html) · [Nobulex](https://nobulex.com) · [LinkedIn](https://www.linkedin.com/in/arian-gogani-nobulex/) · [X](https://x.com/nobulexlabs)

</div>

## What I am building

My current work is Nobulex: billing accuracy for usage-based products. Billing code can return success and still produce the wrong amount. I find a reproducible case, check that a regression test fails on the old behavior and passes on the fix, and state what I did not examine. [The Kill Bill case and two open fixes](https://nobulex.com/research-killbill-catalog-replay) are public. This is research and a fixed-scope audit practice, not a deployed billing product or customer validation.

I also maintain a decision-integrity gateway prototype for automated financial actions. It is implemented and tested locally; it is not deployed in a customer production path. It keeps two questions separate:

1. **What does the available evidence establish?** `PASS`, `FAIL`, or `INDETERMINATE`.
2. **What may the system do next?** `PERMIT`, `BLOCK`, or `ESCALATE`.

That separation matters because missing or unreadable evidence should never quietly become approval.

## Measured, not rounded up

| 5 |
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
| [**Nobulex**](https://nobulex.com/research-killbill-catalog-replay) | Reproduces billing errors that can return success while producing the wrong amount. The current work is a fixed-scope audit and mutation-based regression checks, not a deployed product. | The Kill Bill case links two open fixes and states the tested revision and limits. |
| [**Decision-integrity gateway**](https://github.com/arian-gogani/nobulex-registry) | A Python prototype that separates evidence status from execution policy before a financial action can proceed. | PASS, FAIL, or INDETERMINATE evidence feeds a separate PERMIT, BLOCK, or ESCALATE decision. |
| [**Fail-open corpus**](https://github.com/arian-gogani/failopen) | Minimal reproductions of evaluators and safety checks that can report success without completing the check their result appears to certify. | Each published case names its reproduction limits instead of generalizing from one defect. |
| [**Surka**](https://github.com/arian-gogani/surka) | A small app for keeping two-sided cross-promotion swaps on track, from agreed terms through delivery evidence and results. | The public app is live at [surka.vercel.app](https://surka.vercel.app). No completed real-world swaps or paying users are claimed. |

## External results

- [**Five conformance-harness pull requests merged**](https://github.com/ScopeBlind/agent-governance-testvectors/pulls?q=is%3Apr+author%3Aarian-gogani+is%3Amerged) - The public research distinguishes merged changes from endorsement and freshly reruns only the case it says it reruns.
- [**Two Kill Bill catalog-billing fixes proposed upstream**](https://nobulex.com/research-killbill-catalog-replay) - Open [PR #2320](https://github.com/killbill/killbill/pull/2320) and [PR #2321](https://github.com/killbill/killbill/pull/2321) have released-tag H2 invoice checks that were red before and green after. Current-master CI is unverified; these are proposals, not merged fixes or customer results.
- [**OWASP receipt-guidance update merged**](https://github.com/OWASP/CheatSheetSeries/pull/2217) - The narrowed PR merged on 2 October 2026. A merge is not an OWASP endorsement of Nobulex.
- [**A verifier defect reproduced and fixed upstream**](https://github.com/ScopeBlind/agent-governance-testvectors/pull/24) - The maintainer reproduced the failure, released a corrected verifier, and confirmed all four negative checks.

[**Open the complete Evidence Ledger →**](https://arian-gogani.github.io/evidence.html)

The ledger separates normative changes, merged code, references, listings, open or closed contributions, and self-published research. A merge or listing is never presented as an endorsement.

## Working standard

I publish the command, the expected result, and the limitation beside the claim. If a result cannot establish something, it should say so. If I am wrong, the correction stays visible.

<sub>Canonical profile data: [`data/profile.json`](data/profile.json). This README is generated from it.</sub>
