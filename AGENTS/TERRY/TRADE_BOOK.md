# TERRY TRADE BOOK
**Created:** 2026-06-20

> ⚠️ **RE-TRIGGER (READ_CAP rule 7): rows for closed/dead cards were rotated 2026-09-03 → `archive/TRADE_BOOK_ARCHIVE_2026-09-03.md`. Re-measure at any append, or on 2026-12-03, whichever comes first** (`read_cap_check.py --agent TERRY`). This is a dated cut, NOT a claim that the file stays lean.

Human-readable ledger of Terry-reviewed trade plans. Full cards should live under `setups/YYYY-MM-DD_ticker_structure.md` when created.

| Date | Setup | Thesis owner | Terry verdict | Will decision | Status | Card |
|---|---|---|---|---|---|---|


> ⤵️ **46 rows ROTATED 2026-11-06 → `archive/TRADE_BOOK_ARCHIVE_2026-11-06.md`** (crc32 `306b1517`, 13953 B, verbatim): every row of 16 setup_ids whose last row was terminal. Cards unchanged in `setups/`.
> ⤵️ **41 rows ROTATED 2026-10-29 → `archive/TRADE_BOOK_ARCHIVE_2026-10-29.md`** (crc32 `ff9348e3`, 9,330 B, verbatim): every row of 22 setup_ids whose last row was terminal (7 MGMT lines closed at the 10/29 capture, DURSHORT-EXIT and USO-POSTELECTION resolved by Will 10/29, plus earlier CLOSED/NO TRADE ids). Cards unchanged.
> ⤵️ **3 rows ROTATED 2026-10-22 → `archive/TRADE_BOOK_ARCHIVE_2026-10-22.md`** (crc32 `06a498fe`, 4428 B, verbatim): TRY-NOTRADE-CCLPRINT (NO TRADE, 9/19) and TRY-EXIT-USO35 ×2 (PARKED/declined 9/9–9/10). Cards unchanged in `setups/`.

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





> Historical September3 seven-line expiry-pass batch rotated verbatim to `archive/TRADE_BOOK_EXPIRY_PASS_2026-09-03_rotated_2026-10-12.md`; dated approvals/outcomes remain history, current cards/INDEX govern.

## October13 broker follow-through (Activity receivedOctober13; fill times UNKNOWN)

| Date | Setup | Thesis owner | Terry verdict | Will decision | Status | Card |
|---|---|---|---|---|---|---|

| 2026-10-14 | MGMT-OZK40P-NOV20 | OZK desk (evidence); Will's hand | CONDITIONAL | Pending — WQ-425 card returned to Will | CONDITIONAL — SELL ×4 to close before the Tue 10/20 AMC print (window Thu 10/15 – Mon 10/19 15:30 ET, backstop Tue 10/20 15:30 ET); no roll; RED flip conditions on card | `setups/OZK40P_nov20-sell-or-roll_preprint_2026-10-14.md` |
| 2026-10-14 | MGMT-WAL65P-DEC18 | WAL desk / REGINALD; Will's hand | CONDITIONAL | Pending — WQ-425 card returned to Will | CONDITIONAL — lean SELL ×4 before the Mon 10/19 AMC print (window to Mon 10/19 15:30 ET); HOLD ×4 alternative with post-print read by Wed 10/21 15:00 ET; no roll | `setups/WAL65P_dec18-preprint-management_2026-10-14.md` |
| 2026-10-15 | MGMT-OZK40P-NOV20 | OZK desk (evidence); Will's hand | CONDITIONAL | RULED SELL ×4 — WQ-428, Will 10/14 21:32 ET | CONDITIONAL — ruled sale, order/fill not yet seen (no OZK order in Pending at the 10/15 10:10 capture); fill owed by Tue 10/20 15:30 ET | `setups/OZK40P_nov20-sell-or-roll_preprint_2026-10-14.md` |
| 2026-10-15 | MGMT-WAL65P-DEC18 | WAL desk / REGINALD; Will's hand | CONDITIONAL | RULED A (SELL ×4) — WQ-429, Will 10/14 21:32 ET | CONDITIONAL — ruled sale, order/fill not yet seen (no WAL order in Pending at the 10/15 10:10 capture); fill owed by Mon 10/19 15:30 ET | `setups/WAL65P_dec18-preprint-management_2026-10-14.md` |
| 2026-10-15 | MGMT-HBAN16P-OCT16 | none (Will) | CONDITIONAL | RULED R-B — WQ-302, Deck 12:2x ET | CONDITIONAL — ×1 rides; one look Fri 10/16 before 16:00 ET, close if still ITM (Will's hand) | `setups/HBAN_oct16-16P_ITM-management-card_2026-09-26.md` |

## October19 broker management — current recommendations, preparation only

| Date | Setup | Thesis owner | Terry verdict | Will decision | Status | Card |
|---|---|---|---|---|---|---|
| 2026-10-19 | MGMT-WAL65P-DEC18 | WAL / REGINALD | CONDITIONAL | WQ-429 preprint window ended, no extension | CONDITIONAL — ×4 held at October19 capture; post-print owner read/quote/Will choice owed; October21 15:00 evidence checkpoint | `setups/WAL65P_dec18-preprint-management_2026-10-14.md` |
| 2026-10-19 | MGMT-OZK40P-NOV20 | OZK | CONDITIONAL | WQ-428 SELL approved | CONDITIONAL — ×4 held at October19 capture; October20 15:30 backstop unchanged; no fill | `setups/OZK40P_nov20-sell-or-roll_preprint_2026-10-14.md` |

| 2026-10-19 continuation | MGMT-WAL65P-DEC18 | WAL / REGINALD | CONDITIONAL | Fresh post-print A/B owed; WQ429 ended/no renewal | CONDITIONAL — committed owner/source verification complete; lean SELL4 next liquid session vs explicit call hold; broker quote/new Will ruling owed | `setups/WAL65P_dec18-preprint-management_2026-10-14.md` |


| 2026-10-23 | IDEA-CREDIT-HYG-BDC-OCT23 | REGINALD/DEWEY/BROCK | CONDITIONAL | NOT APPROVED (WQ-509 commission) | CONDITIONAL — NOT-FIRED; HYG Jan-15 77/74P x4 rec, alt HTGC 16P x5 | `setups/CREDIT_hyg-jan15-77-74P_or_htgc-16P_REG-T-04_2026-10-23.md` |
| 2026-10-23 | IDEA-ORCL-PUTSPREAD-OCT23 | PROME ELLISON | CONDITIONAL | NOT APPROVED (WQ-499 commission) | CONDITIONAL — NOT-FIRED; ORCL Dec-18 115/100P x1 | `setups/ORCL_dec18-115-100P_credit-equity-gap_2026-10-23.md` |
| 2026-10-24 | IDEA-CREDIT-HYG-BDC-OCT23 | REGINALD/DEWEY/BROCK | CONDITIONAL | APPROVED leg (a) WQ-513 A (Will 10/23 21:15 ET); leg (b) not approved | CONDITIONAL — APPROVED NOT-FIRED; HYG Jan-15 77/74P x4 <= $1.00 on REG-T-04 + green HYG day by 11/13 | `setups/CREDIT_hyg-jan15-77-74P_or_htgc-16P_REG-T-04_2026-10-23.md` |
| 2026-10-24 | IDEA-ORCL-PUTSPREAD-OCT23 | PROME ELLISON | CONDITIONAL | APPROVED WQ-514 A (Will 10/23 21:15 ET), conditional on IR-verified FQ2 date | CONDITIONAL — APPROVED NOT-FIRED; ORCL Dec-18 115/100P x1 <= $4.40 on CDS >= 350 + ORCL >= $120 + green day by 11/20 | `setups/ORCL_dec18-115-100P_credit-equity-gap_2026-10-23.md` |
| 2026-10-31 | IDEA-UNG-SSW-OCT31 | AEOLUS/BRENT | CONDITIONAL | NOT APPROVED (proposed 2026-10-31, PROME spawn WQ-569) | CONDITIONAL — NOT-FIRED; UNG Jan-15-2027 10/12C x5, limit ≤ $0.50, max loss $256.50; fires on an AEOLUS-logged observed vortex reversal by 11/12, then a red UNG day by 11/20; X1 CLOSED | `setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md` |
| 2026-11-02 | IDEA-UNG-SSW-OCT31 | AEOLUS/BRENT | CONDITIONAL | APPROVED WQ-573 (Will 10/31 14:23 ET, "573 - approve", as written) | CONDITIONAL — APPROVED NOT-FIRED; UNG Jan-15-2027 10/12C x5, limit ≤ $0.50, max loss $256.50; T1 not observed at 11/02 (+14.1 m/s [10/29]); window to 11/12 | `setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md` |

| 2026-11-02 | IDEA-UNG-SSW-OCT31 | AEOLUS / BRENT | CONDITIONAL | WQ-573 unchanged; refresh only per f28fc8021 | CONDITIONAL — APPROVED NOT-FIRED on record; canonical weather grade pending; fresh GFS Nov 2 06Z +5.53155 m/s, positive sampled analysis; 10:22 chain outer .47, x5 screen loss $241.50; cap $256.50 unchanged; green day blocks; both $10.40 guards bind | `setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md` |

| 2026-11-05 | MGMT-GLD-SHARES-OCT24 | MIDAS | CONDITIONAL | Rails only | CONDITIONAL — 18 shares at the 11/5 capture | `setups/GLD-SHARES_management-rails_2026-10-24.md` |
| 2026-11-05 | IDEA-HYG-FOLLOW-NOV05 | LIQUID/REGINALD | CONDITIONAL | WQ-615 undecided | CONDITIONAL — NOT-FIRED; HYG Jan-15 76/73P ×5 ≤ $0.60, max loss $306.50 | `setups/HYG_jan15-76-73P_credit-follows-hedge_2026-11-05.md` |
| 2026-11-05 | IDEA-QQQ-200D-NOV05 | none, HENRY levels | CONDITIONAL | WQ-617 undecided | CONDITIONAL — NOT-FIRED; QQQ Dec-18 670/680C ×1 ≤ $4.90, max loss $491.30 | `setups/QQQ_dec18-670-680C_200day-reclaim_2026-11-05.md` |
| 2026-11-05 | IDEA-HYG-FOLLOW-NOV05 | LIQUID/REGINALD | CONDITIONAL | APPROVED WQ-615 A, Will 2026-11-05 13:59 ET | CONDITIONAL — APPROVED NOT-FIRED; ×5 ≤ $0.60, max loss $306.50; GATE-TERRY-HYG-FOLLOW-01 | `setups/HYG_jan15-76-73P_credit-follows-hedge_2026-11-05.md` |
| 2026-11-05 | IDEA-QQQ-200D-NOV05 | none, HENRY levels | CONDITIONAL | WQ-617 C, Will 2026-11-05 13:59 ET, NOT approved | CONDITIONAL — NOT-FIRED, NOT approved; decide at a fire by 11/20 | `setups/QQQ_dec18-670-680C_200day-reclaim_2026-11-05.md` |
| 2026-11-05 | IDEA-UNG-SSW-OCT31 | AEOLUS / BRENT | CONDITIONAL | WQ-573 unchanged | CONDITIONAL — APPROVED FIRED; T1 11/5 14:35 ET, ECMWF 12Z −0.279244 m/s; UNG Jan-15-2027 10/12C ×5 ≤ $0.50, max loss $256.50; order presented, no fill (Will 16:15 ET: spread not bought; separate Robinhood Dec-24 $10.5 call ×1, `NOTE-UNG105C-DEC24`) | `setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md` |
| 2026-11-06 | IDEA-HYG-FOLLOW-NOV05 | LIQUID/REGINALD | CONDITIONAL | WQ-615 unchanged | CONDITIONAL — APPROVED FIRED; T1(a) HY 348 [11/5], read 10:09 EST; HYG Jan-15-2027 76/73P ×5 ≤ $0.60, max loss $306.50; order presented, no fill known | `setups/HYG_jan15-76-73P_credit-follows-hedge_2026-11-05.md` |
| 2026-11-08 | IDEA-UNG-SSW-OCT31 | AEOLUS / BRENT | CONDITIONAL | ENDED by Will 2026-11-07 09:22 ET | CLOSED — ended unfilled, $0; GATE-TERRY-UNG-01 retired; NOTE-UNG105C-DEC24 stands as Will's own position, no prompts | `setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md` |
| 2026-11-09 | IDEA-HYG-FOLLOW-NOV05 | LIQUID/REGINALD | CONDITIONAL | WQ-663 B, Will 2026-11-09 23:10 ET | CONDITIONAL — APPROVED FIRED; green-day entry condition waived on this card only (root rule #6 break, figures on card); ×5 ≤ $0.60, max loss $306.50, window 12/4; no fill known | `setups/HYG_jan15-76-73P_credit-follows-hedge_2026-11-05.md` |
