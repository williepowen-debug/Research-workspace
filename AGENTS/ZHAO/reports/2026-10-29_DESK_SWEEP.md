# ZHAO desk sweep — 2026-10-29 13:4x ET (Will: "sweep of ZHAO files/folders… anything owed, incomplete, broken, stale/old?")

Read-only audit; nothing fixed in this pass except this file. Ranked.

## A. Broken / mis-delivered
| # | Finding | Evidence | Owner |
|---|---|---|---|
| A1 | **Two outbox packets were never delivered.** 10/16 → MIDAS (−41% is June CRUDE imports, not copper; it answers MIDAS's 10/12 ask). 10/20 → VULCAN/WATT/HAWK/HENRY/BRENT: §2 MOFCOM 公告48 (23 AI + 12 PV technologies proposed for the export catalogue) and §3 the Graham-Act sanctions EO → BRENT. Neither is superseded by the delivered 10/29 packet. | no copy in any recipient inbox; PROME memos 10/16 and 10/20 processed, no relay | PROME (route) |
| A2 | **Recurring data releases dropped off the calendar after 9/30.** No CATALYSTS rows for Sep/Oct trade, CPI/PPI, SAFE reserves, RatingDog, Korea TIC or Sep TIC. So boot never flagged the dark period. | docket/CATALYSTS.tsv | ZHAO |
| A3 | catalyst_countdown counts DONE rows and RESOLVED DOCKET rows as live (DAEDALUS D3/D4, 10/14). Two range rows are mis-classed `confirmed` (D14). | scripts/catalyst_countdown.py (last edit 8/21) | ZHAO |
| A4 | CATALYSTS rows left open after grading: 10/16 Aug TIC (P1, graded 10/16) · Plenum (graded today) · 9/07 reserves leg (52 days past) · 10/01 H.4.1 (28 days, unread). | CATALYSTS.tsv | ZHAO |

## B. Stale — dashboard numbers older than their next print
| Item | Desk value | Newer print exists |
|---|---|---|
| FX reserves / gold (VX-1.07) | end-JUNE | Jul, Aug, Sep (SAFE ~7th of the month) |
| CPI / PPI | AUG | Sep (~mid-Oct) |
| Trade (nominal) | AUG | Sep (~mid-Oct) |
| RatingDog PMI (VX-6.14) | AUG | Sep; Oct due ~11/2 |
| Korea UST (VX-2.07), anchor selling (VX-7.01) | JUL TIC | Aug TIC (10/16) |
| China 10Y CGB, China-US gap (VX-2.08/2.09) | 9/18 | daily |
| KOSPI flows (2.06), land sales (3.03/6.13), LGFV (6.01), banks (6.05) | Jul | Jan–Sep fiscal data out mid-Oct |
| NPL / debt rows 6.02–6.04, 6.07, 6.09 | FEB (258d) | freeze or refresh |
| Vectors 8/10/11 (energy, Gulf) | other desks' 7/4–9/6 reads | ask BRENT/HAWK |
| KB.tsv | **87** ACTIVE rows past Stale_By (29 Oct, 24 Sep) | no reader (NEXT #9) |

## C. Owed (STATUS NEXT ACTIONS + DAEDALUS 10/14 list)
- Belgium kill-leg re-spec — deferred to **10/23, now 6 days late**.
- Vectors 6 and 9 re-spec as two-directional (KB-168) — owed since 9/18; both read 🟢 on a managed yuan.
- Explain the Aug China −$12.25B / Belgium +$19.85B residuals; decide whether to re-score Vector 1.
- PBOC fixing series (chinamoney) · ChinaBond CGB primary · VX row for the Chinese clock · Vector 8 VX row.
- MOFCOM 公告 39/43/45/47 not located; 公告2025年第72号 primary; 46号 clause-2 content unverified (11/27 clock).
- ZHA-05 window LAPSED (H1) and was never graded or re-registered; ZHA-10 Date_Made defect. **No open forecast on the 11/10 clocks or the NPCSC.**
- DAEDALUS D7 (NEXUS CALIBRATION is still 8/21 content; FORWARD CATALYSTS header "refreshed 9/17"; LPR 9/20 row) · D8 (STATUS header/bottom-line stacking) · D9 (TRADE.md unfreeze rule) · D11 (VX_HISTORY: freeze or resume) · D12 (OPEN_THREADS 7/09: re-issue or archive).
- Unverified claim held: MP Materials / USA Rare Earth listing (NEXT #13).

## D. Housekeeping
- **CLAUDE.md = 32,525 B against the 32,550 B cap: 25 B of headroom.** Any charter edit breaches it, so a rotation is needed before the next one.
- No `workbook/LEDGER_GLOB` (most desks declare one); CATALYSTS.tsv is outside the staleness scan.
- Retirement-eligible (>60d, no live-doc reference): reports 7/16 domain sweep, 8/03 P3 prereg, 8/21 boot.py audit, 8/21 June TIC; workbook/STATUS_archive_20260325.md (misfiled in workbook/).
- NEXUS_BRIEF stacks 7 "As of" lines (10/9 → 10/29).

## Healthy
Inbox empty except one info item · corrections PASS · all other outbox packets delivered · read caps OK (STATUS 25.8 KB, brief 24.8 KB) · TIC/China level current · today's refresh closed the 8 key-figure flags · TRADE.md and LAST_COMPLETION.md correctly frozen.
