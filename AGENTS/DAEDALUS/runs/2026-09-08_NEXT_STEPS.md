# Recommended next steps — 2026-09-08

Recommendations only; no listed work executed in this planning read.

| Order | Work | Completion evidence |
|---|---|---|
| 1 | Repair DAEDALUS profile freshness semantics before relying on the alert count | Distinguish full/section refresh from receipt metadata. OSPREY's warning disappeared after our receipt-only header update despite an explicit statement that no refresh occurred. profile_clock_check.vintage_of chooses the maximum header date, including future checkpoint dates on other profiles. Reproduce both failures and verify a remedy with explicit vintage semantics and clean/alert cases; do not mass-reset profile dates. |
| 2 | Run the overdue PROME judgment-tail sweep | Read current Will-facing content and its owner sources, sample completed dispositions, compare standing instructions with actual execution; produce a bounded findings table and an explicit L5 verdict. Sweep last ran 22 days ago against 21-day cadence. No PROME mutation during review. |
| 3 | Resolve the nearest owner-verification obligations | By September 11: HAW-18 existing-canon application with PROME/HAWK, BRENT post-repair acceptance, NEXUS follow-up and scorecard render 3. Verify whether owner work has advanced before reopening a queued task. |
| 4 | Keep the scheduled review sequence, with explicit deliverables | September 10 validate_all scope; September 12 tooling and cadence-spec review; September 14 ladder-integrity including invented tool/count gates; September 15 production review and map history rotation. BROCK still alerts (48 days vs 45); OSPREY remains a refresh obligation despite the false-clear clock. |

OSPREY's strike-feed proposal is no longer grounds to infer an empty scripts directory: new uncommitted owner script/output paths appeared during our drain. Read that work before offering another implementation. Receipt processing is complete; next value comes from verifying that existing fixes and decisions hold at their consumers.
