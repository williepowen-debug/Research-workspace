# TERRY TRADE BOOK
**Created:** 2026-06-20

> ⚠️ **RE-TRIGGER (READ_CAP rule 7): rows for closed/dead cards were rotated 2026-09-03 → `archive/TRADE_BOOK_ARCHIVE_2026-09-03.md`. Re-measure at any append, or on 2026-12-03, whichever comes first** (`read_cap_check.py --agent TERRY`). This is a dated cut, NOT a claim that the file stays lean.

Human-readable ledger of Terry-reviewed trade plans. Full cards should live under `setups/YYYY-MM-DD_ticker_structure.md` when created.

| Date | Setup | Thesis owner | Terry verdict | Will decision | Status | Card |
|---|---|---|---|---|---|---|


> ⤵️ **3 rows ROTATED 2026-10-22 → `archive/TRADE_BOOK_ARCHIVE_2026-10-22.md`** (crc32 `06a498fe`, 4428 B, verbatim): TRY-NOTRADE-CCLPRINT (NO TRADE, 9/19) and TRY-EXIT-USO35 ×2 (PARKED/declined 9/9–9/10). Cards unchanged in `setups/`.
| **2026-09-19** | **TRY-COND-NCLHDEC14P** — NCLH Dec-18-2026 $14P (ATM), the only cruise structure that clears on measurement | CRUISE (row 1, conv 3, WATCH — WQ-218 ①, **spent edge**; the ~$1.3B forced-raise leg retired by CRUISE 9/19) | **CONDITIONAL — NO CARD.** Structure clears every stable test (88 DTE Mon = in the 60–90 band, spread **2.25%**, OI **3,870**, flat ~50% skew, leg gate rc=0) and the envelope is real (6 of 8 prints down, **last FOUR all −8.6 to −15.3%**). **But EV vs its own 8-print base rate is ≈ 0** (−9.7% to −0.2%); it is positive only on the last-4 sample (+22 to +31%) — **n=4, subjective, labelled so**. ⛔ **THE STRADDLE REASON IS WITHDRAWN** (it read *"Dec-18 ATM straddle = 21.0% of spot, so an −11% print is half the priced move"*): **a long put's breakeven is `strike − premium` = `$12.65` = `−10.41%`, which an −11% print clears, marking +21% to +30% at the print with 44 DTE left.** ✅ **True reason EV ≈ 0: at IV 45% the 6 DOWN prints average `+15.0%` and the 2 UP prints average `−69.7%` — the UP-TAIL kills it, not the size of the down move.** ⚠️ **NCLH skips November: the 10/30 expiry dies 5 days BEFORE the 11/4 print** | **not put to Will** — no measured edge to put behind a card; `$0` moved | **CONDITIONAL - NOT PROPOSED** | none — `options/PRINT_ENVELOPE_CRUISE_2026-09-19.md` |

> ⤵️ **16 rows for closed/dead/retired cards ROTATED 2026-09-03 → `archive/TRADE_BOOK_ARCHIVE_2026-09-03.md`** (crc32 `e7bb56ed`, 29,389 B, verbatim). Read-cap remedy, Will-approved. Kept here: every row mentioning a card with a live forward obligation.
> ⤵️ **2 `TRY-MGMT-USO135C` rows ROTATED 2026-09-14 → `archive/TRADE_BOOK_ARCHIVE_2026-09-14.md`** (crc32 `0202b01b`, 2,156 B, verbatim). **Criterion = this file's own 2026-09-03 rule — no live forward obligation:** the `USO Oct-16 $135C` is CLOSED (leg A 9/2 ×1 price UNKNOWN/`WQ-167`; remaining ×1 SOLD **2026-09-09 @ $17.55, net $1,754.30, realized +$1,043.64**) and `GATE-TERRY-USO135C` is **RESOLVED/terminal**, B/C and the 10/09 time stop discharged. Verified on GATES.tsv · FORGE/STATUS.md · INDEX.md/SETUPS.tsv · the sale receipt BEFORE the cut. **Cut because this session's own `TRY-MGMT-USORH150165` row took the file 354 B over the 32,550 B READ-CAP — the over-run was mine, so I cleared it.**
> ⤵️ **9 rows ROTATED 2026-10-08 → `archive/TRADE_BOOK_ARCHIVE_2026-10-08.md`** (crc32 `03a498ec`, 8285 B, verbatim): `TRY-FIRE-004` ×8 (CLOSED 9/30; its CLOSED row was written and rotated in the same edit) + `TRY-EXIT-TLT85P` ×1 (CLOSED 9/10). ⛔ No live-card row moved.

## Status Values

- `DRAFT` — under construction, not ready for approval.
- `PROPOSED` — ready for Will approve/reject.
- `APPROVED` — Will approved; execution still external/manual.
- `REJECTED` — Will rejected.
- `ACTIVE` — known open position; requires broker truth.
- `CLOSED` — closed with postmortem complete.
- `EXPIRED/SUPERSEDED` — no longer actionable.
> Entry/approval/fill history rotated verbatim2026-10-19 to `archive/TRADE_BOOK_ENTRY_HISTORY_2026-10-19.md` (crc32 `2002f356`). Current rows below govern. Recheck size at any append or2026-12-03.

## Owner management reconciliation — 2026-09-08

Prior rows above are dated records. These rows supersede their current-state claims; no trade or new proposal was made.

| Date | Setup | Thesis owner | Terry verdict | Will decision | Status | Card |
|---|---|---|---|---|---|---|
| 2026-09-08 | TRY-WAL-ROLL70 — 1× recorded Robinhood | WAL / REGINALD | FIRED | WQ-144 fill 9/2; WQ-167 GTC permanently UNKNOWN | FIRED / LIVE — manual $4.40 harvest, parent 9/8 17:32 ET vendor mid $2.05 below at sample, no GTC re-ask; owner close grade 9/2 0-of-3, 9/3–9/8 consumer bars routed. 12/04 time stop; no roll | `setups/WAL_dec18-70P-duration-roll_2026-09-01.md` |
| **2026-09-11 (re-arm)** | **TRY-BRENT-REFINER — GATE MEASURED, GATE FAILS INVERTED. NO FILL. State UNCHANGED.** WQ-213 (Will 9/10 16:42) is PLACE IT at a fresh mark on a day refiners are RED against oil. **9/11 10:59 ET: VLO +2.19% `$393.88` and USO −2.91% `$153.77` — BOTH legs fail, in opposite directions to the gate**; MPC/PSX/DINO/CRAK all green, so it is the complex, not a single name. PROME's independent 10:05 read agrees. **The 9/10 gate does NOT carry: a day-colour gate is a `MOMENT` property (`RISK_RULES` #14) and expires with the session that measured it.** Size re-marked `$1,033` → **`$1,181.64`** (VLO +14.33% since the 8/27 approval); the `$500` cap now binds at −42.3% (was −48%) and is still not the operative limit. **Will's approval STANDS and is enforced, not re-litigated — WQ-213 stays OPEN, hands owed, blocked on a qualifying TAPE.** `$0` moved, no order, no gate shaved. | **BRENT** (thesis) / **TERRY** (construction) | 🟢 **STAGED (unchanged)** |
| **2026-09-18 (fill day)** | **TRY-BRENT-REFINER — `WQ-213` RE-AFFIRMED 9/17 21:25; FILL = WILL'S HAND TODAY; measurement on the card, receipt OWED. State UNCHANGED (STAGED until the receipt).** | BRENT (thesis) / TERRY (construction) | **STAGED** | ✅ **Will, verbatim 9/17: *"I will enter VLO tomorrow market closed for now."*** Condition ② discharged by his ruling. | **STAGED — receipt owed. 11:10 ET: VLO `$415.62` +0.75% GREEN (30-day HIGH) / USO `$156.10` +0.51% GREEN ⇒ the card's entry gate NOT MET — stated, not a bar (root #5). Root #6: shares, no premium, no break. Crack matched-Nov `$108.53` (+$1.00 vs 9/17c) STABLE ⇒ desk rec FILL by the 9/14 self-limit. Fresh mark `3 × VLO = $1,246.86` (MOMENT). Sleeve after add `$7,022.56`, 100% undefended; oil ceiling STILL unnamed. ⛔ `CL=F`/`BZ=F` −4% today = ROLL ARTIFACTS, crude UP on every named month.** | `BRENT_refiner-distillate-strong-leg_2026-08-27.md` |
| **2026-09-18 (fill)** | **TRY-BRENT-REFINER — FIRED / LIVE, 1 of 3 filled.** | BRENT (thesis) / TERRY (construction) | **FIRED** | ✅ **Will's hand: BUY 1 VLO limit $412.00 Day, FILLED $412.00** (receipt pasted 12:34 ET; account/time not in it) | **FIRED / LIVE — 1 share @ $412.00; two more remain STAGED under the scaling rec (gate day or ~$375; stand down on crack <$95).** No execution grade (no same-timestamp mark). Sleeve 100% undefended; oil ceiling still unnamed. `L412` closes on this receipt (PROME); ANVIL mirrors at the next reconcile. | `BRENT_refiner-distillate-strong-leg_2026-08-27.md` |


| 2026-10-11 | TRY-NOTRADE-WQ409-SPY — SPY Dec18 770/760P candidate ×1 | VIOLET | NO TRADE | PASSED WQ-418 October11; ruling5a8168f95 | NO TRADE; 0 contracts/$0 moved; VIOLET consumption unverified | `setups/SPY_dec18-770-760P_pre-CPI-TAKE-PASS_2026-10-11.md` |

| 2026-10-12 | TRY-BRENT-REFINER — held-share precision definition only | BRENT/HENRY | FIRED | WQ-420 approved October11 | FIRED / LIVE, one held share; exact prospective insert encoded, staged2 stood down; no new grade/order; independent result read PENDING | `setups/VLO-SHARE_management-proposal_2026-09-28.md` §2-bis |
| 2026-10-12 | TRY-BRENT-REFINER — afternoon existing held-share observation | BRENT/TERRY | FIRED | WQ386/420 existing rule | FIRED / LIVE, one recorded held share; A-notice/exit UNKNOWN from0be151800, source proof incomplete; no new notice/SELL/order, B1–B3 not regraded | `setups/VLO-SHARE_management-proposal_2026-09-28.md` October12 afternoon assessment |
| 2026-10-12 | MGMT-QQQ755C-OCT12 — ×1 held, Will value$2 | Will | CONDITIONAL | Preparation only | CONDITIONAL; sale preferred today, roll unapproved; broker bid/orders missing | `setups/QQQ755C_oct12-sell-or-roll_2026-10-12.md` |
| 2026-10-12 | MGMT-USO150C-OCT14 — ×2 snapshot-held | Will/BRENT context | CONDITIONAL | Preparation only | CONDITIONAL; sale preferred on profitable broker bid; no inherited October9 stop/roll approval | `setups/USO150C_oct14-sell-or-roll_2026-10-12.md` |

| 2026-10-12 | TRY-NOTRADE-MPC-L689 — refiner-margin resilience | BRENT | NO TRADE | Not put to Will; construction PASS | NO TRADE; size0/$0; MPC spread$611.30over cap, green premium/no measured exception, economics/book incomplete | `setups/MPC_refiner-margin-resilience_L689_2026-10-12.md` |

> Historical September3 seven-line expiry-pass batch rotated verbatim to `archive/TRADE_BOOK_EXPIRY_PASS_2026-09-03_rotated_2026-10-12.md`; dated approvals/outcomes remain history, current cards/INDEX govern.

## October13 broker follow-through (Activity receivedOctober13; fill times UNKNOWN)

| Date | Setup | Thesis owner | Terry verdict | Will decision | Status | Card |
|---|---|---|---|---|---|---|
| 2026-10-13 | MGMT-QQQ755C-OCT12 | Will | CLOSED | Outcome recorded | CLOSED — expiredOctober12; −$144.66; canceled sell not fill | `setups/QQQ755C_oct12-sell-or-roll_2026-10-12.md` |
| 2026-10-13 | MGMT-QQQ745P-OCT15 | Will | CLOSED | Sale evidenced | CLOSED — remaining1 soldOctober12; incremental+$109.68, not cohort total again | `setups/QQQ745P-740P_oct15-sell-or-roll_2026-10-07.md` |
| 2026-10-13 | MGMT-TLT82P-OCT16 | Will | CLOSED | Sale evidenced | CLOSED — remaining1 soldOctober12; incremental+$232.67; prior partial separate | `setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md` |
| 2026-10-13 | MGMT-DURSHORT-EXIT-WQ291 | BOND/Will | CONDITIONAL | WQ357 prior LATER | CONDITIONAL — TLT CLOSED; TBT5 survivesOctober14 decisionclock; derived sale+$35.95, no new rule | `setups/DURATION-SHORTS_exit-card_WQ291_2026-10-01.md` |
| 2026-10-14 | MGMT-QQQ744P-OCT14 | Will | CLOSED | Filled sale recorded | CLOSED — sold1 at8.22/net821.32; derived realized+545.66 | `setups/QQQ744P_oct14-sell-or-roll_2026-10-13.md` |

| 2026-10-14 | MGMT-QQQ740P-OCT15 | Will | CONDITIONAL | Partial filled sale recorded | CONDITIONAL — sold1 at6.71/net670.32; remaining3/basis1591.99; derived incremental+139.66 conditional no unseen basis change | `setups/QQQ745P-740P_oct15-sell-or-roll_2026-10-07.md` |
| 2026-10-14 | MGMT-OZK40P-NOV20 | OZK desk (evidence); Will's hand | CONDITIONAL | Pending — WQ-425 card returned to Will | CONDITIONAL — SELL ×4 to close before the Tue 10/20 AMC print (window Thu 10/15 – Mon 10/19 15:30 ET, backstop Tue 10/20 15:30 ET); no roll; RED flip conditions on card | `setups/OZK40P_nov20-sell-or-roll_preprint_2026-10-14.md` |
| 2026-10-14 | MGMT-WAL65P-DEC18 | WAL desk / REGINALD; Will's hand | CONDITIONAL | Pending — WQ-425 card returned to Will | CONDITIONAL — lean SELL ×4 before the Mon 10/19 AMC print (window to Mon 10/19 15:30 ET); HOLD ×4 alternative with post-print read by Wed 10/21 15:00 ET; no roll | `setups/WAL65P_dec18-preprint-management_2026-10-14.md` |
| 2026-10-15 | MGMT-QQQ740P-OCT15 | Will | CLOSED | Will's own sale 10/14 (broker-verified 10/15 capture) | CLOSED — ×3 sold 10/14 net $3,474.93; derived +$1,882.94; cohort +$2,022.60 incl. +$139.66 (never add both) | `setups/QQQ745P-740P_oct15-sell-or-roll_2026-10-07.md` |
| 2026-10-15 | MGMT-USO150C-OCT14 | Will/BRENT context | CLOSED | Will's own sale 10/14 (broker-verified 10/15 capture) | CLOSED — ×2 sold 10/14 net $760.68; derived +$385.35 | `setups/USO150C_oct14-sell-or-roll_2026-10-12.md` |
| 2026-10-15 | MGMT-OZK40P-NOV20 | OZK desk (evidence); Will's hand | CONDITIONAL | RULED SELL ×4 — WQ-428, Will 10/14 21:32 ET | CONDITIONAL — ruled sale, order/fill not yet seen (no OZK order in Pending at the 10/15 10:10 capture); fill owed by Tue 10/20 15:30 ET | `setups/OZK40P_nov20-sell-or-roll_preprint_2026-10-14.md` |
| 2026-10-15 | MGMT-WAL65P-DEC18 | WAL desk / REGINALD; Will's hand | CONDITIONAL | RULED A (SELL ×4) — WQ-429, Will 10/14 21:32 ET | CONDITIONAL — ruled sale, order/fill not yet seen (no WAL order in Pending at the 10/15 10:10 capture); fill owed by Mon 10/19 15:30 ET | `setups/WAL65P_dec18-preprint-management_2026-10-14.md` |
| 2026-10-15 | MGMT-HBAN16P-OCT16 | none (Will) | CONDITIONAL | RULED R-B — WQ-302, Deck 12:2x ET | CONDITIONAL — ×1 rides; one look Fri 10/16 before 16:00 ET, close if still ITM (Will's hand) | `setups/HBAN_oct16-16P_ITM-management-card_2026-09-26.md` |
| 2026-10-15 | MGMT-DURSHORT-EXIT-WQ291 | BOND | CONDITIONAL | APPROVED — WQ-357, Deck 12:2x ET | CONDITIONAL — exit TBT ×5 on Will's order; no TLT sale; fill owed | `setups/DURATION-SHORTS_exit-card_WQ291_2026-10-01.md` |
| 2026-10-15 | TRY-COND-QQQ-DATED-DOWNSIDE | Will (no agent thesis) | CLOSED | DECLINED — WQ-365, Deck 12:03 ET | CLOSED — never approved, never filled, $0; card retired | `setups/QQQ_dec18-put-spread_dated-downside_2026-10-02.md` |

## October19 broker management — current recommendations, preparation only

| Date | Setup | Thesis owner | Terry verdict | Will decision | Status | Card |
|---|---|---|---|---|---|---|
| 2026-10-19 | MGMT-QQQ720P-OCT20 | Will-direct | CONDITIONAL | Approval/broker re-mark owed | CONDITIONAL — ×1 captured; sale preferred; no roll; proposed time stop 2026-10-20 14:30 ET | `setups/QQQ720P_20261020-sell-or-roll_2026-10-19.md` |
| 2026-10-19 | MGMT-QQQ719P-OCT20 | Will-direct | CONDITIONAL | Approval/broker re-mark owed | CONDITIONAL — ×1 captured; sale preferred; no roll; proposed time stop 2026-10-20 14:30 ET | `setups/QQQ719P_20261020-sell-or-roll_2026-10-19.md` |
| 2026-10-19 | MGMT-QQQ715P-OCT20 | Will-direct | CONDITIONAL | Approval/broker re-mark owed | CONDITIONAL — ×1 captured; sale preferred; no roll; proposed time stop 2026-10-20 14:30 ET | `setups/QQQ715P_20261020-sell-or-roll_2026-10-19.md` |
| 2026-10-19 | MGMT-CRWV56P-OCT23 | Will-direct | CONDITIONAL | Approval/broker re-mark owed | CONDITIONAL — ×1 captured; sale preferred; no roll; proposed time stop 2026-10-22 15:00 ET | `setups/CRWV56P_20261023-sell-or-roll_2026-10-19.md` |
| 2026-10-19 | MGMT-USO163C-OCT23 | Will-direct | CONDITIONAL | Approval/broker re-mark owed | CONDITIONAL — ×1 captured; sale preferred; no roll; proposed time stop 2026-10-22 15:00 ET | `setups/USO163C_20261023-sell-or-roll_2026-10-19.md` |
| 2026-10-19 | MGMT-USO165C-OCT28 | Will-direct | CONDITIONAL | Approval/broker re-mark owed | CONDITIONAL — ×1 captured; sale preferred; no roll; proposed time stop 2026-10-27 15:00 ET | `setups/USO165C_20261028-sell-or-roll_2026-10-19.md` |
| 2026-10-19 | MGMT-CMG28P-OCT30 | Will-direct | CONDITIONAL | Approval/broker re-mark owed | CONDITIONAL — ×1 captured; sale preferred; no roll; proposed time stop 2026-10-29 15:00 ET | `setups/CMG28P_20261030-sell-or-roll_2026-10-19.md` |
| 2026-10-19 | MGMT-USO165C-OCT30 | Will-direct | CONDITIONAL | Approval/broker re-mark owed | CONDITIONAL — ×1 captured; sale preferred; no roll; proposed time stop 2026-10-29 15:00 ET | `setups/USO165C_20261030-sell-or-roll_2026-10-19.md` |
| 2026-10-19 | MGMT-WAL65P-DEC18 | WAL / REGINALD | CONDITIONAL | WQ-429 preprint window ended, no extension | CONDITIONAL — ×4 held at October19 capture; post-print owner read/quote/Will choice owed; October21 15:00 evidence checkpoint | `setups/WAL65P_dec18-preprint-management_2026-10-14.md` |
| 2026-10-19 | MGMT-OZK40P-NOV20 | OZK | CONDITIONAL | WQ-428 SELL approved | CONDITIONAL — ×4 held at October19 capture; October20 15:30 backstop unchanged; no fill | `setups/OZK40P_nov20-sell-or-roll_preprint_2026-10-14.md` |
| 2026-10-19 | MGMT-DURSHORT-EXIT-WQ291 | BOND | CONDITIONAL | WQ-357 SELL approved | CONDITIONAL — TBT×5 held, fill owed; no TLT position/sale | `setups/DURATION-SHORTS_exit-card_WQ291_2026-10-01.md` |
| 2026-10-19 | MGMT-VLO-SHARE | BRENT / HENRY | CONDITIONAL | Original-share rule only | CONDITIONAL — VLO total3; original1rule scope; added2scope UNKNOWN; SCALE TERMINAL; October16/19 no grade | `setups/VLO-SHARE_management-proposal_2026-09-28.md` |
| 2026-10-19 | TRY-BRENT-REFINER | BRENT | FIRED | No scale revival | FIRED / LIVE — total3captured; original1rule scope, later2 UNKNOWN; SCALE TERMINAL | `setups/BRENT_refiner-distillate-strong-leg_2026-08-27.md` |

| 2026-10-19 continuation | MGMT-WAL65P-DEC18 | WAL / REGINALD | CONDITIONAL | Fresh post-print A/B owed; WQ429 ended/no renewal | CONDITIONAL — committed owner/source verification complete; lean SELL4 next liquid session vs explicit call hold; broker quote/new Will ruling owed | `setups/WAL65P_dec18-preprint-management_2026-10-14.md` |
| 2026-10-19 continuation | MGMT-VLO-SHARE | BRENT / HENRY | CONDITIONAL | Original1scope only; added2 A/B NOT APPROVED | CONDITIONAL — prospective same-letter/manual-scope choice prepared; total3; no scale revival or retrospective grade | `setups/VLO-SHARE_management-proposal_2026-09-28.md` |

| 2026-10-19 catchup | MGMT-VLO-SHARE | BRENT/HENRY | CONDITIONAL | Original1scope only | CONDITIONAL — A10/16and10/19 NOT FIRED/no notice; C3ESTIMATE99.4509072906/99.8656630518; added2scopeUNKNOWN; no order | `setups/VLO-SHARE_management-proposal_2026-09-28.md` |
| 2026-10-19 catchup | TRY-FIRE-002 | CARL/REGINALD | STAGED | Ungradedarchivechoice toWill | STAGED — KEEP DORMANT reply10/10 consumed10/11, re-lockNO; reviewwrittenlate, no entry or archive execution | `setups/PRINT-TRIGGER_WAL-EGBN-build.md` |
| 2026-10-19 catchup | TRY-COND-NCLHDEC14P | CRUISE | CONDITIONAL | No card/entry | CONDITIONAL — NOT PROPOSED; Q3dateconfirmed10/29,10/30expiryspansrelease; owner/edge prerequisitesremain, no freshpricing | `options/PRINT_ENVELOPE_CRUISE_2026-09-19.md` (datedanalysis) |

| 2026-10-20 | MGMT-QQQ720P-OCT20 | Will-direct | CLOSED | Filled STC1at6.66/net665.32 | CLOSED — holding0; derived realized+474.66; no repeatbooking | `setups/QQQ720P_20261020-sell-or-roll_2026-10-19.md` |
| 2026-10-20 | MGMT-USO165C-OCT30 | Will-direct | CONDITIONAL | BTO addition1recorded; management choice owed | CONDITIONAL — now2held/basis586.32/value370; old1ticket superseded | `setups/USO165C_20261030-sell-or-roll_2026-10-19.md` |
| 2026-10-20 | MGMT-QQQ715P-OCT22 | Will-direct | CONDITIONAL | Filled BTO1recorded; management choice owed | CONDITIONAL — held1; proposedOctober21 15:00ET sale; no rollapproved | `setups/QQQ715P_20261022-sell-or-roll_2026-10-20.md` |
| 2026-10-20 | IDEA-VST-OCT20 | Evidence on card | CONDITIONAL | NOT APPROVED | CONDITIONAL — NOT-FIRED;VST2common;X1closed | `setups/VST_common_power-scarcity_2026-10-20.md` |
| 2026-10-20 | IDEA-IEF-OCT20 | Evidence on card | CONDITIONAL | NOT APPROVED | CONDITIONAL — NOT-FIRED;IEF90/92C3;X1closed | `setups/IEF_jan90-92C_safe-asset-rebound_2026-10-20.md` |
| 2026-10-20 | IDEA-RSP-OCT20 | Evidence on card | CONDITIONAL | NOT APPROVED | CONDITIONAL — NOT-FIRED;RSP215/225C1;X1closed | `setups/RSP_jan215-225C_breadth-confirmation_2026-10-20.md` |
| 2026-10-20 | IDEA-FXY-OCT20 | Evidence on card | CONDITIONAL | NOT APPROVED | CONDITIONAL — NOT-FIRED;FXY58/60C1;X1closed | `setups/FXY_jan58-60C_yen-confirmation_2026-10-20.md` |
| 2026-10-20 | TRY-COND-CRWV-RALLYFADE | VULCAN/LIQUID | CONDITIONAL | WQ442prepareonly | CONDITIONAL — NOT-FIRED;65/60P1,max201.30 | `setups/CRWV_jan15-put-spread_relief-rally-fade_CONCEPT_2026-10-15.md` |
| 2026-10-22 | IDEA-QQQ-PUTWALL-OCT22 | HENRY/VULCAN/LIQUID | CONDITIONAL | NOT APPROVED | CONDITIONAL — NOT-FIRED; QQQ Nov-20 690/670P x1; X1 closed | `setups/QQQ_nov20-690-670P_gamma-negative-putwall_2026-10-22.md` |
| 2026-10-22 | IDEA-USO-POSTELECTION-OCT22 | BRENT/FALCON | CONDITIONAL | NOT APPROVED | CONDITIONAL — NOT-FIRED; USO Jan-15 170/185C x1; X1 closed | `setups/USO_jan15-170-185C_post-election-strike-window_2026-10-22.md` |
| 2026-10-22 | IDEA-OKTA-SECWAVE-OCT22 | Will premise (no fleet owner) | CONDITIONAL | NOT APPROVED | CONDITIONAL — NOT-FIRED; OKTA Nov-20 220/230C x1; X1 closed | `setups/OKTA_nov20-220-230C_agent-credential-security-wave_2026-10-22.md` |
