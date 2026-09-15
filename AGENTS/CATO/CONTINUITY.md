# CATO — current continuity

**Updated:** 2026-09-15. This is a dated resume map; verify owner records and Git state before acting.

## Current assignment and approvals

Will approved the RAV review’s direction and asked to build **the first part**, explicitly allowing staged work. This phase creates CATO’s manual startup, charter, continuity and Astra launcher. Fleet registration, automatic routing and the RAV succession migration remain later work; do not silently complete them during orientation.

The build acceptance and verification receipt live in [the foundation record](../../PROME/plans/2026-09-15_CATO-foundation.md). Start there if continuing CATO setup. Next setup step: review the remaining integration work with Will and complete a bounded RAV/CATO transition when that pass is requested. Do not retire RAV or transfer its old findings as live obligations merely because CATO now has a home.

## Our relationship and repository

Will wants an independent second pair of eyes, with PROME first. He cares about bloat, hidden breakage, staleness and better procedures. CATO carries forward the review relationship described in its charter. It is not taking over PROME’s operational desk.

Repository root is two directories above this home. Root AGENTS.md/CLAUDE.md describe the research fleet; USER.md describes working with Will. PROME owns coordination; domain agents own their evidence; Will owns capital decisions. `PROME/ROSTER.md` governs fleet membership. Historical onboarding and completed-work details: [September 15 Codex handoff](../../reviews/2026-09-15_codex_handoff.md), read on demand.

## Existing work — resume only as assigned

| Work | Last established state | Next action / owner record |
|---|---|---|
| L393 Deck split | Approved by Will; implemented and independently code-reviewed in `f12c6dc94`. **Not published.** Local pair uses relative links. | [Publication handoff](../../PROME/plans/2026-09-15_L393-deck-split.md): native Artifact tools, private reference URL, WQ-253 explainer and hosted verification still needed. Do not ask again for layout approval. |
| L333 ARGUS trial | Useful catches, but no defensible aggregate score or full operating-cost comparison established. Grade scheduled September 19. | [Evidence reconciliation](../../PROME/reports/2026-09-15_L333-L393-followup.md); reconstruct first four eligible sessions and finding timing without cherry-picking clean runs. |
| L381 instruction reconciliation | Implemented/source-verified in `2ae76c7c4`. Two ordinary completed-session observations still owed. | [Record](../../PROME/plans/2026-09-15_L381-reconciliation.md); use existing evidence, no new scorecard. L378 mechanization remains separate. |
| Continuity cleanup | Sample revised, **not applied** to live STATUS/HANDOFF. | [Sample](../../reviews/2026-09-15_prome_continuity_sample.md); re-check current text before proposing application. |

Other September 15 work: `24b820577` repaired test fixtures and corrected L247’s F4 STATUS disposition; `71d554b92` revised the continuity sample. These are historical receipts, not proof that every current issue is closed. The handoff and linked review record the verification limits.

## Carry these constraints forward

- Rediscover available tools. The prior session lacked native Artifact publishing; that is an observation, not a permanent platform limitation. Preserve the existing private Owed artifact and ruling store.
- Root Git status may contain active work from other agents, including staged files. Never sweep it or infer idleness from an absence of commits.
- RAV’s old ledger has contradictory and stale dispositions. Its history is useful evidence; none of its rows has been imported as CATO’s active backlog.
- Foundational files and a successful startup test do not establish mature operational performance. Keep implementation, testing and independent verification separate.
