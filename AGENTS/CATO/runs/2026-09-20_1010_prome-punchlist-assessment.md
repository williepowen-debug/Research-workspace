# PROME punch-list — calendar scope, received handoffs and existing controls

September 20, 2026, approximately 10:10 EDT. Will relayed PROME's CRUISE-sweep receipt and three proposed next actions. Snapshot HEAD `6639cbfa8`; working tree initially clean. Bounded inspection of CRUISE `91fa9b0be`, existing CATO receipts, two SAM relay artifacts, root consumer-check rule/tool and PROME closeout reference, plus JPX primary calendar sources. No PROME operational boot, desk launch, owner edit or message performed.

## Recommendation to Will

Prioritize a correctly scoped Japan calendar entry; reconcile the CATO handoff list against existing receipts instead of building a redundant relay; support a short proposal that extends the existing consumer-check closeout practice to retired narrative claims and task checkboxes. These are recommendations, not approvals or newly launched tasks.

## F1 — High for scheduling: “Japan closed” omits derivatives holiday trading

JPX's [market-holiday calendar](https://www.jpx.co.jp/english/corporate/about-jpx/calendar/) lists September 21, 22 and 23, 2026 as holidays. But its explicit [September 18 announcement](https://www.jpx.co.jp/english/news/2040/20260918-01.html) says derivatives holiday trading will operate on **all three days**. The [eligible-product rules](https://www.jpx.co.jp/english/derivatives/rules/holidaytrading/) include index futures/options and commodity futures/options, while excluding JGB futures/options, interest-rate futures and securities options.

Suggested docket scope: **September 21–23 Japan cash-equity holidays; eligible OSE/TOCOM index and commodity derivatives remain open for holiday trading; JGB and interest-rate futures are not eligible.** Consumers should use their instrument's schedule rather than inherit a blanket market closure. In particular, “no Tokyo market” must not be read as all Japan-linked exchange products being unavailable. Other venues, OTC FX, bank settlement, MOF curve publication and auctions were not independently verified in this pass.

No matching Silver Week/“Japan closed” event was found in the inspected PROME DOCKET using the named-event phrases. That supports PROME's proposed registration work, not an assertion that every related date is absent. No DOCKET row written by CATO.

## Handoff reconciliation — much of the proposed delivery is already received

| PROME item | CATO receipt/disposition |
|---|---|
| CRUISE R6 dividend correction | Already added to [original R6](2026-09-19_1808_cruise-review.md), recorded in `e453eca49`; prospective total-return ruling received. No repeat handoff needed. |
| SAM ruling / follow-up | [Ruling review](2026-09-19_2137_sam-ruling-review.md), [correction recheck](2026-09-19_2205_sam-correction-recheck.md), [stopping receipt](2026-09-19_2326_sam-stopping-receipt.md) already exist. This pass read the PROME inbox packets `2026-09-19_from-SAM_CATO-R4-RULED-sam28-regraded-qualified-sam31-holds.md` and `2026-09-19_from-SAM_CATO-2nd-review-upheld-4of4-correction-pass-complete.md`; those subjects and revisions are covered by the receipts. |
| TERRY withdrawal | Already received and recorded in [CRUISE next-step assessment](2026-09-19_2130_cruise-next-step-assessment.md) and [v3 review](2026-09-20_0950_cruise-test-v3-review.md). The incorrect accusation and zero-event-premium assertion were withdrawn. Replacement pricing work was not thereby certified. |

PROME's short labels **ADD-1/ADD-2** were not found as exact artifact labels in the scoped search, so do not claim their identities solely from the numbering. Ask PROME to map those aliases to paths/revisions and compare them with the existing receipts. A short index of received items and any actual delta is more useful than another long four-item handoff. This is reconciliation, not a request that Will manually relay the same material again. CATO remains manual-only; no automatic inbox/launch/routing change is proposed.

## CRUISE sweep receipt — bounded completion supported

`91fa9b0be` implements the five listed surface corrections: convergence-table funding-gap wording, KB-CRU-075 capex-sensitivity caveat, WATCHLIST's unpriced-equity-raise claim, and the two completed-source/date checkboxes. The key corrected capex note explicitly records approximately +$170M becoming −$30M in the −5% cash-flow scenario with an extra $200M capex. The summary now also says the model is an endpoint test, not a liquidity clearance. This verifies the listed edits, not the native doorbell, every source calculation or a fleet-wide sweep.

The underlying missing cash schedule remains missing; “a draw confirms the schedule” is still too strong for an endpoint model. Interpret it as consistent with modelled borrowing, not verification of timing or absence of distress. Closing PROME's bounded delivery/sweep task must not silently discharge the substantive funding-model limit already recorded in the [earlier review](2026-09-19_2034_cruise-followup.md).

## Process proposal — extend an existing control, distinguish wording from meaning

Root `CLAUDE.md` session-end **1c** already requires consumer checks when superseding cited figures, explicitly including `--self` for the author's own figures and fixing by pattern rather than only by a supplied hit list. `PROME/CLOSEOUT.md` step 6 incorporates root steps 1b–1e. `scripts/consumer_check.py` documents its numeric-token focus and already distinguishes historical/superseded hits; its `--mirror-map` mode supports literal nonnumeric tokens in a declared scope. This is not an operation with no propagation control at all.

The real proposal is to clarify the trigger/scope for **retired qualitative claims and completed task states**, plus whether the existing step actually ran. A bounded candidate mechanism: name the retired claim and replacement meaning; search the owner's current summaries, tables, exit rules, checklists and known consumer instructions using distinctive text and paraphrases; classify each hit as live, clearly historical or unrelated; reread the final replacement for the original logical error. Preserve history and unrelated work. Literal grep finds candidate copies but cannot certify semantic propagation; a paraphrase or a newly overclaimed replacement can still be wrong.

PROME can draft that small amendment under Will's direction. Do not infer that three episodes prove absence of a control, install another gate, or launch a fleet-wide audit from this receipt. The memory-index and HEARTBEAT_COLD items were not independently reviewed here; their quoted ownership/next-pass disposition is not being expanded.

Only this CATO report and continuity authored. No DOCKET registration, consolidated peer packet, process implementation, market state, trade, grade or owner file changed. Weekday check passed four files, whitespace check passed and index was empty before staging. Orphan advisory identified concurrent OSPREY edits to STRIKES.tsv and KB.tsv; both preserved and flagged to Will in-session. Exact-path commit/push receipt follows in-session. Review complete; next orient and await Will.
