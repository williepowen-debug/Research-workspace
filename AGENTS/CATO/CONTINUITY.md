# CATO — current continuity

**Updated:** 2026-09-15, BRENT/WALTER review. This is a dated resume map; verify owner records and Git state before acting.

## Current assignment and approvals

**Latest review:** Will asked to examine BRENT/WALTER updates. [Review and reproduction](runs/2026-09-15_1821_brent-walter-review.md): one medium rig-reader missing-cell defect; two low closeout issues (BRENT consumed-mail filing and WALTER publication reconciliation after our shared push). Forty existing tests passed; independent counterexample reproduces a false-success count. Owner files untouched, no messages sent, fixes not implemented. Review delivered; next startup orient and await Will. If follow-up is assigned, start with F1. Prior PROME repair described below is completed history.

**First foundation complete:** `ebeee2832`, confirmed pushed to `origin/master`. CATO has manual startup, charter, continuity and an Astra-configured launcher. The fresh read-only startup check passed, and independent result review found no blockers; exact backend model identity and ordinary interactive use remain unverified. PROME added the provisional CLASSIFICATION PENDING roster entry in `f1bd2147a`, confirmed on origin. This records the manual-only boundary; permanent classification, instrument integration and RAV succession remain unresolved. Automatic launch/routing is excluded.

Will approved the local fixes responding to PROME's feedback: launcher inspection without Codex, explicit commit attribution and the self-review boundary. Implemented in `bd1c1b683`, now confirmed on origin; [repair report and historical authorship map](runs/2026-09-15_1324_foundation-feedback.md). The [PROME inbox proposal](../../PROME/inbox/2026-09-15_from-CATO_manual-integration-proposal.md) remains the original integration proposal, not an activation grant.

**Prior completed repair:** Will authorized correcting the closeout findings while PROME was closed. [Repair and review receipt](runs/2026-09-15_1525_prome-repair.md): FERT arithmetic/caveats corrected; four completed rows use terminal state tokens; September 17 BOND grading is pending at L404; freshness distinguishes CATO manual inspection from launch eligibility. L402 now requires implementing-session evidence. Local views regenerated; hosted publication remains pending. Next: PROME can consume the top HANDOFF repair note and original CATO integration proposal on its next boot. No broader classifier, fleet activation or RAV transition authorized. BRENT and WALTER remained active; their work was preserved. Repair committed as `06e72cc11`, exact eleven-file manifest verified, and confirmed on origin/master by safe-push fresh fetch. All 53 tests passed; independent result review passed after one blocker correction. No CATO task is currently in progress. On next startup, orient and await Will’s assignment; do not automatically begin the remaining work below.

**Closeout follow-up recovered:** Will approved an ordered checklist in AGENTS.md, then authorized finishing its interrupted closeout. The prior “complete” wording preceded the commit; recovery found the two edited files and untracked report intact. [Change and recovery receipt](runs/2026-09-15_1654_closeout-checklist.md). Implementation is complete; the commit/push receipt is delivered in-session after verification. Root Git mechanics remain canonical. After this closeout, orient and await Will’s next assignment; publication and integration are not newly assigned.

The build acceptance and verification receipt live in [the foundation record](../../PROME/plans/2026-09-15_CATO-foundation.md). Start there if continuing CATO setup. Next setup step: review the remaining integration work with Will and complete a bounded RAV/CATO transition when that pass is requested. Do not retire RAV or transfer its old findings as live obligations merely because CATO now has a home.

## Our relationship and repository

Will wants an independent second pair of eyes, with PROME first. He cares about bloat, hidden breakage, staleness and better procedures. CATO carries forward the review relationship described in its charter. It is not taking over PROME’s operational desk.

Repository root is two directories above this home. Root AGENTS.md/CLAUDE.md describe the research fleet; USER.md describes working with Will. PROME owns coordination; domain agents own their evidence; Will owns capital decisions. `PROME/ROSTER.md` governs fleet membership. Historical onboarding and completed-work details: [September 15 Codex handoff](../../reviews/2026-09-15_codex_handoff.md), read on demand.

## Existing work — resume only as assigned

The following includes work implemented by CATO's preceding Codex session, despite `PROME:` commit subjects. Use the authorship map above before selecting an independent review; further CATO checks of those same changes are author follow-up. PROME's operational obligations remain with PROME.

| Work | Last established state | Next action / owner record |
|---|---|---|
| L393 Deck split | Approved by Will; implemented and independently code-reviewed in `f12c6dc94`. **Not published.** Local pair uses relative links. | [Publication handoff](../../PROME/plans/2026-09-15_L393-deck-split.md): native Artifact tools, private reference URL and hosted verification still needed. Local explainer coverage passed during the repair; recheck current coverage before publishing. Do not ask again for layout approval. |
| L333 ARGUS trial | Useful catches, but no defensible aggregate score or full operating-cost comparison established. Grade scheduled September 19. | [Evidence reconciliation](../../PROME/reports/2026-09-15_L333-L393-followup.md); reconstruct first four eligible sessions and finding timing without cherry-picking clean runs. |
| L381 instruction reconciliation | Implemented/source-verified in `2ae76c7c4`. Two ordinary completed-session observations still owed. | [Record](../../PROME/plans/2026-09-15_L381-reconciliation.md); use existing evidence, no new scorecard. L378 mechanization remains separate. |
| Continuity cleanup | Sample revised, **not applied** to live STATUS/HANDOFF. | [Sample](../../reviews/2026-09-15_prome_continuity_sample.md); re-check current text before proposing application. |

Other September 15 work: `24b820577` repaired test fixtures and corrected L247’s F4 STATUS disposition; `71d554b92` revised the continuity sample. These are historical receipts, not proof that every current issue is closed. The handoff and linked review record the verification limits.

## Carry these constraints forward

- Rediscover available tools. The prior session lacked native Artifact publishing; that is an observation, not a permanent platform limitation. Preserve the existing private Owed artifact and ruling store.
- Root Git status may contain active work from other agents, including staged files. Never sweep it or infer idleness from an absence of commits.
- RAV’s old ledger has contradictory and stale dispositions. Its history is useful evidence; none of its rows has been imported as CATO’s active backlog.
- Foundational files and a successful startup test do not establish mature operational performance. Keep implementation, testing and independent verification separate.
