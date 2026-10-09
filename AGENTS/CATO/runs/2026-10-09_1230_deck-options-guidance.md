# Deck options and grouping — CATO guidance, October 9, 2026

## Recommendation

Proceed toward selectable choices, with the proposal corrected before implementation. Choice-specific consequences belong in Change A. A choice must preserve its meaning and source revision, not merely its letter. Independent decisions need independent identities through rendering, storage and pickup. Keep the three action-state sections; domain filtering is useful, but urgent items need an unfiltered visible area or an equally explicit visibility rule. Do not treat these observations as Will's approval or start implementation.

Source pin: `6f8cd2e6a`, PROME proposal `proposals/2026-10-09_deck-options-and-grouping-PROPOSAL.md`, registered L660. Reviewed that full proposal, relevant `tools/decision_deck.py` render/store code, BOOT step3b, existing runtime fixture portions and owner authority/review clauses. Existing code is evidence of the proposed integration boundary, not a fresh audit of the complete Deck. Some broad navigation/row output truncated; no claims rely on unseen portions. WALTER pending-bookmark file dirty at entry; PROME live owner. No owner edit, send, launch, render, hosted read, tap or store access.

## Concrete proposal gaps

**DP1 — labels do not preserve the approved meaning (consequential).** Proposed tap stores `choice=B` and `options_shown=[A,B,C]`. Counterexample: build1 B permits an action subject to condition X; build2 B has different terms. Both arrays are identical. Existing `build` field identifies a build but the proposal provides no guaranteed immutable mapping to the content shown. Save the presented option descriptions/conditions and authoritative source identity, or retain an immutable versioned decision definition that the tap references. Old-build pickup must use that version; a material conflict with current terms needs reconciliation, not silent application to the new B. Acceptance: unchanged labels with changed terms, old page tapped after republish, deleted/withdrawn option, and selected B not in displayed set.

The proposed guard greps the owner artifact for a label. That does not establish authorization: A/B may occur in unrelated text, an old choice list or a rejected alternative. Bind label and meaning to the cited current decision/option block and revision. Do not claim token presence makes invented choices impossible. No universal parser or new owner schema prescribed; choose the smallest reliable representation within the existing generator.

**DP2 — two cards sharing a WQ can overwrite the effective ruling (consequential).** Proposal offers two cards OR two rows for WQ302's TLT and HBAN choices. Existing UI snapshot groups latest by `wq`; BOOT3b likewise groups by WQ, latest ts rules and earlier taps are marked consumed. Thus two separate taps on the same WQ become alternatives instead of independent decisions. Either split into independently identified WQ rows or use stable decision/subdecision IDs throughout UI, tap store, history and pickup. Acceptance: choose TLT A then HBAN R-B; both remain effective, and revising TLT alone leaves HBAN intact. Rendering two cards alone is insufficient.

**DP3 — option consequences cannot be a later enhancement (material usability).** Existing explainer renders If yes / If no; proposal defers `if_<LABEL>` to brainstorm10. With A/B/C actions, those binary consequences may mislead. Initial release must show each choice's meaning, consequence and relevant conditions next to its control, while preserving owner labels. Ordinary binary rows may retain their current layout. Notes continue to carry Will's amendments; token validation does not override explicit operator words.

**DP4 — filtering can hide urgent cards (material usability).** Proposal says filters keep due-today work visible, but a persisted Rates filter would hide a new Energy expiry. Sorting inside the selected subset cannot fix exclusion. Keep a due-today/overdue strip visible outside filters, or explicitly choose another behavior that preserves urgent visibility; show active filter and easy All reset. Acceptance: save one domain, publish urgent work in another, reopen page and verify it is visible. Do not infer hosted behavior from the proposal.

## Product priority and boundaries

1. Complete option semantics and independent pickup as one coherent A release, independently review the diff and rendered interaction, and preserve existing binary/Done/Later/offline/store-error behavior.
2. Show exact due time/timezone and distinguish recorded from picked up. Current page already shows per-tap awaiting/picked-up status, so improve its visibility rather than claiming this capability is wholly absent. A countdown is optional after the authoritative timestamp is right. Neither pickup nor approval means a trade executed.
3. Add domain filters while retaining the action-state sections and urgent visibility. Plain labels such as System change and Action needed are easier than Rule/Hands. A second kind-filter row is optional if it materially helps find work.
4. The case against can improve decisions; owner source links support verification. Defer money sorting and since-last-visit mechanics until the core flow works. Premium, maximum loss and exercise cash are different quantities and should not be mixed into a single opaque rank. No batch approval proposed.

No code built or tests run for this proposal-only assessment. No approval, date change or policy exception inferred. Useful next artifact is a revised bounded proposal addressing DP1–DP4, then the implementation/result review under PROME's existing process. No extra standing audit, reviewer layer or architecture project is recommended.

## Delivery

CATO report and changed continuity only; checks and Git receipt follow in-session. No external source or live financial quote used.

Verified readable weekday inputs: PROME DOCKET/GATES/WILL_QUEUE, CATO CONTINUITY and this report; checker5/5 clean. Optional desk STATUS/CALENDAR/CATALYSTS remain absent and omitted. Direct startup byte measurements: CATO AGENTS6,465 / CHARTER9,921 / CONTINUITY26,333; root CLAUDE24,961 / USER5,200 / AGENTS5,313, all below32,550. Generic CATO read-cap's previously observed missing-local-CLAUDE CANNOT-EVALUATE remains, not a pass. Orphan advisory flags only WALTER's pending-bookmark state; preserved. Index empty and own whitespace check clean before staging. No changed numerical figure, ledger or auto-memory invokes conditional checks. Exact two CATO files only; no pull over foreign work.
