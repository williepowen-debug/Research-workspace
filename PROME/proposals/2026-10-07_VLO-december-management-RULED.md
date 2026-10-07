# VLO held-share price-rule extension — WQ-386 RULED APPROVED

Status: **RULED APPROVED October 7, 2026.** Will, directly in this PROME conversation, verbatim: **“okay approved”**, after the plain-language explanation of WQ-386. Recorded 2026-10-07T14:24:57-04:00. Approval covers the reviewed held-share-only amendment below, including the stated roll-only-exit and calibration limitations; no sale, add or order was approved. WQ-252 remains the broader basis sitting; WQ-330 is the underlying held-share rule.

## Acceptance conditions, written before proposed operational wording

1. One current share only; no new position, add, size, order or execution authority. No amendment of HEN-46, terminal VLO-SCALE, or the dead HEN-F3 prediction.
2. Name the same delivery month on both legs, first and last applicable session, the governing source hierarchy, strict thresholds, uncertainty treatment and post-window default.
3. Require no fresh observation from an expired contract. No indefinite suspension created by a two-contract comparison.
4. Preserve an earlier triggered exit; no month switch or missing value cancels it. No back-adjustment, persistence test or roll exception hidden in a month change.
5. Show an explicit counterexample in which the month switch alone produces the exit; disclose uncertain original threshold calibration and manual monitoring latency.
6. Owner integration and Will approval remain distinct from this read-only preparation. Validate exact wording with an independently selected Sol reviewer before presenting as ready.

Neighbour cases considered: ordinary valid reading; overlap around switch and an outstanding November exit; wrong or continuous contract; missing/near-line data; concurrent owner activity (no helper desk writes). This is a proposed letter, not software; review its case outcomes, no executable production control claimed.

## Approved amendment

**Approve option A from the existing DAEDALUS memo for the ONE held VLO share only: fixed matched December from October 15, with no roll window and no threshold adjustment.** It preserves a price exit through earnings without requiring an expiring-contract comparison. It explicitly accepts that December's lower margin can cause an exit at the switch. A real, observable margin and a simple rule are preferable here to an adjusted series or extra suppression logic with uncertain calibration.

Approved exact letter — Will approved October 7, before the October 14 deadline:

> For GATE-TERRY-VLO-HELD-01 leg A only, November matched HOX26×42−CLX26 governs through the October 14, 2026 settlement. December matched HOZ26×42−CLZ26 governs the settlement observations dated October 15 through November 19, 2026, inclusive. Verify named-contract identity on each pull; a continuous ticker or wrong delivery month is rejected. No automatic January roll is authorized.
>
> The held-share thresholds remain strictly below $95 per barrel for notice only and strictly below $90.16 per barrel for TERRY's SELL recommendation. The stock price is not the crack and is not a new stop. The switch is unconditional on the two months agreeing: an accepted December reading below $90.16 may trigger the exit even if November remains above it. No offset, persistence requirement, roll-window suppression or threshold recalibration is adopted.
>
> Preserve the existing source order and observation standard: (1) CME settlement; (2) the vendor daily row dated to that session, finalized and accepted only within $0.15 of (3); (3) 14:28–14:30 ET one-minute volume-weighted settlement-window proxy, labelled ESTIMATE. Reject duplicated-volume/provisional daily rows. If only (3) is available within ±$0.15 of $90.16, or a required leg/window/identity is missing, the observation is UNKNOWN, not a fire. Do not substitute a later session's value or a stale expired-contract value. Re-read at the next touch under the existing missing-data rule. This extension creates no automatic monitor or guaranteed touch cadence.
>
> An exit established under the prior governing November observation remains owed after the switch; an outstanding exit is not cancelled by a higher December reading, missing data or the end of the observation window. TERRY writes the recommendation at its next touch; Will executes at the next regular session under the existing card. No order is placed by the desk.
>
> Review the next basis by November 18, 2026. If no further ruling is made, new leg-A observations become SUSPENDED/UNKNOWN after the November 19 settlement. An already-established exit still remains owed. Policy legs B1–B3 and their existing execution limitations continue unchanged until sale or withdrawal. This is authority to maintain the existing share's management rule, not to buy or re-enter.

If Will declines or makes no ruling by October 14, the existing letter governs: new A observations suspend after October 14; B1 continues. A later approval requires a newly stated prospective effective date; this proposal does not retroactively grade the intervening period.

## Evidence and tradeoffs

- Position: Will confirmed October 7 that he still holds the one Fidelity share bought September 18 at $412. Marks/P&L were not refreshed. Evidence receipt: `PROME/reviews/2026-10-07_VLO/MANAGEMENT_PASS.md`.
- Existing card: `AGENTS/TERRY/setups/VLO-SHARE_management-proposal_2026-09-28.md`, §§2–3,5. Its November basis expires after October 14 unless Will rules. Its prescribed latency is the gap between desk touches, not continuous coverage.
- Options: `PROME/inbox/processed/2026-10-01_from-DAEDALUS_WQ-252-crack-contract-month-options-memo.md`. September Nov−Dec step median $4.72/bbl, range −$0.03 to $7.24. Months straddled $95 in 7/21 sessions but $90.16 in 0/21. These are historical, single-vendor observations, not predicted firing probabilities.
- HENRY response: `PROME/inbox/processed/2026-10-02_from-HENRY_WQ-252-step-measurements-and-calibration-pair.md`. Replication uses the SAME vendor, not an independent data source. **The $90.16 calibration's July 23 heating-oil contract identity is UNKNOWN. HENRY withdrew its claim that the baseline was verified as a matched pair. Keeping the number is an explicit operational choice, not a claim that it is newly validated for December.**
- Expiry: [CME Chapter 200 §200102.F](https://www.cmegroup.com/rulebook/NYMEX/2/200.pdf), read October 7, ends crude trading three business days before the 25th, or before the preceding last business day when the 25th is nonbusiness. Calendar application: October 25 is Sunday, October 23 preceding business day, so CLX26 ends October 20; November 25 is Wednesday, so CLZ26 ends November 20. These derived dates agree with the saved vendor expiries; no separate populated contract-calendar row obtained. The candidate ends December observations one session before CLZ26 expiry.
- The expiry-based alternative A′ retains November for October 15, 16 and 19: **three**, not four, additional trading sessions. Its proposed ±2-session D window would include October 21–22, when fresh CLX26 observations are unavailable. An operational D would need both a finite cutoff and a rule for the missing outgoing contract. Merely adding D does not eliminate a persistent curve-induced crossing; it delays the decision and changes the approved exit timing.
- Earnings call: October 22 at 10:00 ET on [Valero's event page](https://investorvalero.com/events-and-presentations/default.aspx), read October 7. This proposal retains an observation basis across that event but is not an earnings-hold recommendation or price forecast.

## Required cases

| Hypothetical observation | Candidate outcome |
|---|---|
| Oct 14 Nov $94, Dec $89, both accepted | November governs: notice only; December diagnostic only. |
| Oct 15 Nov $94, Dec $89, both unchanged from prior day | December governs: exit. The month switch alone changes the outcome, explicitly accepted by this proposal. |
| Oct 15 Dec $90.16, official settlement | No exit: strict less-than; notice applies. |
| Oct 15 Dec proxy $90.10, only source 3 | UNKNOWN for exit: inside ±$0.15 band, no automatic sale. |
| Oct 15 Dec valid above exit, Oct 14 Nov accepted $89 with exit outstanding | Prior November exit remains owed. |
| Oct 21 Nov unavailable, Dec accepted $89 | December exit; no dependence on November after switch. |
| Oct 21 only continuous HO=F/CL=F available | Reject; UNKNOWN; no fabricated fire or month substitution. |
| Nov 19 valid Dec $89, recommendation written after Nov 19 | Established exit remains owed despite suspension of new observations. |
| Nov 20 no successor ruling, Dec still has trading data | New A observations suspended by the proposed end date; B1 continues. |

## Review and integration status

IMPLEMENTED: Will ruling recorded; PROME gate schedule, position-management mapping and decision records updated. TERRY canonical card integration is separately owed by the owner packet; no domain files edited by PROME.
TESTED: case table assessed against existing card and hypothetical observations; no software or live-monitor test claimed.
INDEPENDENTLY VERIFIED: `/root/vlo_final_review`, explicitly selected `gpt-6.1-sol` with high reasoning, returned READY FOR WILL DECISION with zero consequential blockers and no mandatory wording fix. PROME consumed the response and received explicit closeout receipt; no files/Git/subprocesses changed by that reviewer.
STILL UNRESOLVED: owner integration; original calibration identity; current official settlement access. These last two data limitations are disclosed and are not cured by choosing a month.

Read-only helper roles are advisory drafting/verification, not persistent TERRY/DAEDALUS owner sessions or fresh owner grades. Domain files remain untouched. Two initial helpers were inadvertently launched with inherited model identity UNKNOWN, contrary to USER.md's explicit Sol preference; their further research was stopped when found. Their outputs are retained as attributed draft evidence, not relabelled as Sol. The final independent reviewer was explicitly selected Sol. Model-selection deviation is recorded in ORCH_LOG.

Read-only draft deliveries: `/root/vlo_terry_review` and `/root/vlo_basis_review` both recommended option A alone; each returned an explicit no-files/no-subprocesses closeout receipt after PROME's ask. TERRY-perspective reasoning: proportionate to one share, no hidden delay, explicit roll-only exit risk. Basis-perspective reasoning: December-only grading removes the expired-contract dependency; the earlier memo's October 15–19 count is three sessions; D's five-session window and missing data do not support a promised two-session maximum delay. These are attributed helper analyses, not owner endorsements.

Independent reviewer counterexample: official November $90.16 and December $90.00 remain unchanged October 14→15. October 14 yields notice only; October 15 yields an exit solely from the month change. If instead only source 3 reports December $90.01, exactly $0.15 below $90.16, the inclusive uncertainty band yields UNKNOWN. This verifies the distinct strict-price and estimate-band boundaries without changing the draft.

Declared review residue (five warnings, retained): uncertain original calibration; same-vendor historical replication does not establish independent market evidence or forward probabilities; manual monitoring does not promise detection before earnings; official current CME settlement remains unavailable/no fresh grade here; Will approval is now recorded; canonical owner integration is still owed. PROME registration is authorized; this record does not claim a new owner price grade. The broader HEN-46/WQ-252 sitting remains open.


## Approval integration receipt

The approved block above preserves the independently reviewed operational wording. GATES retains the last owner grade as historical and records this ruling as a control update, not a new market observation. Next management review is November 18; new price observations suspend after November 19 absent another ruling. The outgoing gate row is preserved in `PROME/archive/GATES_STATE_HISTORY_2026-10-07_WQ386.md`. TERRY owns its card/status integration; the dated inbox packet carries Will's verbatim ruling via this record. Owner-session discovery remains incomplete across runtimes; no duplicate desk writer launched. Publication to the private Deck is unavailable in this runtime and remains pending; local WQ is canonical.

### WQ-386 OPEN row at ruling (history)

| 386 | ⚖️ **VLO held-share price rule: approve fixed matched December from 2026-10-15 through 2026-11-19, with no rollover waiting window.** Keep $95 notice / $90.16 exit; policy legs unchanged. One share only. | RULE / [Approve] — held-position management amendment | 2026-10-14 | 10/7 | **APPROVE option A for the held share only**; independent Sol wording review: READY FOR WILL DECISION, no consequential blockers. A switch alone may trigger an exit; the original $90.16 contract calibration remains UNVERIFIED. | User authorized preparation 10/7, not adoption. Exact letter and review: `PROME/proposals/2026-10-07_VLO-december-management-PROPOSAL.md`. WQ-252 / DOCKET L471 is the broader basis sitting, still open for HEN-46; no scale revival or HEN-F3 successor. Read-only TERRY/basis helpers favor A; no canonical owner endorsement claimed. Missing data remain UNKNOWN; manual touches only. Without approval, A suspends after 10/14; under this amendment it suspends after 11/19 absent a successor, without cancelling an established exit. Pre-registration queue parse: 19 open / 18 actionable / 1 blocked; no dated row 7d overdue, so cap/aged triage not triggered. |
