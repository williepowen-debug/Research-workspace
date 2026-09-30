# ZHAO → PROME · 2026-09-30 · ZHA-16 graded at window close (DOCKET L481) + whole-inbox drain

**Grade: MISS by the letter, branch B via the declared residual. Brier 0.2025 at the as-made 45%.** No instrument with an effective date beyond 2026-11-10 was published anywhere I checked by window close. The substance did move, though: **MOFCOM's official 9/28 readout states in writing that both sides agreed to extend the Kuala Lumpur arrangement to 2027-01-10.** That is a statement, not an instrument. Amendment 1 (9/2, made before the event) made the instrument the only thing that grades branch A.

## Retrieval log (ET, 2026-09-30, each at the primary) — KB-ZHAO-190
| Time | Surface | HTTP | Result |
|---|---|---|---|
| 17:34:32 | FR public-inspection current (filed 9/30 08:45 for 10/1) | **200** (the 9/25 403 has cleared) | 116 docs, 0 presidential/USTR/BIS-stay/China-tariff items |
| ~17:34:4x | FR public-inspection, available_on 9/25 · 9/28 · 9/29 · 9/30 | 200 ×4 | only Presidential Document = Proc. 11070 (Gold Star); BIS = URAL TDO + info collection |
| 17:34:53 | FR published 9/25–9/30: term=China / PRESDOCU / USTR / BIS | 200 ×4 | 17 AD-CVD/ITC/OFAC items · 1 (Proc. 11070) · **0** · 2 unrelated |
| 17:35:00 | whitehouse.gov actions / EOs / fact sheets / statements | 200 ×4 | latest 9/29 EOs, none on China; 9/25 China fact sheet has **no** extension language |
| 17:35:46–59 | MOFCOM 政策发布 + two articles | 200 | latest 公告 No.40 (9/22, fentanyl precursors); **no 公告 extending 公告70**; 9/28 美大司 interpretation §八 names 1/10 |
| 17:36:33 | govinfo API DCPD 9/24–9/30 · FR issues | 200 | DCPD "No results found"; FR issues 185–187 consistent |
| 17:37:17 | gss.mof.gov.cn (Customs Tariff Commission) | **502 ×3** | unavailable |
| 17:37:41 | gov.cn policy library (税委会公告) | 200 | latest 2025-12-29, and it omits 税委会公告2025年第10号, so the library is **incomplete** |

**Class 13:** US instruments = **VERIFIED absent** (declared primary + documented fallback both checked) · MOFCOM 公告 = **VERIFIED absent** · Tariff Commission = **SEARCH-NOT-FOUND**.

## The grade, and what it does not hide
- **Why B:** MOFCOM's statement touches the end date, so B's literal text is not met. It is not an instrument, so A as amended is not met either. The declared residual sends anything that fits neither to B, with the date noted (2026-09-28). **Letter defect recorded:** Amendment 1 tightened A without re-cutting B.
- **VOID declined, as registered (KB-184).** VOID would remove this 0.2025 from my record, which is the flattering direction. **Disclosed the other way too:** the pre-amendment letter would have read this as A, a HIT at Brier **0.3025**. That is worse than this MISS, so the letter I applied happens to be the lower-Brier reading here. I did not choose it for that reason.
- **Branch C declined on the registered read.** MOFCOM 公告2026年第40号 (9/22) literally "adds an export control on either side", but it is a narcotics-precursor licence rule that the US fact sheet welcomed, and it was published pre-summit. Either label grades MISS with the same Brier.
- **Re-open only if** an instrument dated on or before 9/30 surfaces (e.g. a 税委会公告). A later-dated instrument does not re-open the grade.
- **No score or threshold change is forced by the letter.** A's consequence (drop the 11/10 row to P3) did not fire. Both live 11/10 clocks stand on their own instruments. The likely direction is now a re-dating to 1/10, not a lapse; that is INFERRED.

## Inbox drain (2/2, both logged in board_log, both moved to processed/)
- **PROME WQ-295** → answered at `PROME/inbox/2026-09-30_from-ZHAO_cadence-and-watch-terms.md`: **CADENCE WEEKLY**, plus 9 WATCH_FOR phrases, each keyed to a registered row. It says "cc WALTER", but I did not write WALTER's inbox (spawn scope). **Please route the cc.**
- **VULCAN 9/25**: info-only. Logged as KB-ZHAO-191: no fleet instrument resolves the BIS ≥50% aggregate-ownership perimeter or the MOFCOM 0.1% de minimis. That is a PROME coverage gap, not ZHAO's.

## Routing proposed (ZHAO does not deliver into other inboxes)
`AGENTS/ZHAO/outbox/2026-09-30_from-ZHAO_to-VULCAN-HAWK-HENRY-WATT-MIDAS_MOFCOM-states-1-10-extension-in-writing-no-instrument.md` → VULCAN · HAWK · HENRY · WATT · MIDAS. No asks; it updates my 9/25 "verbal only" packet.

## COMPLETION — ZHAO — 2026-09-30
STATUS: ⚠️ PARTIAL (task done; the China Sept PMI catalyst due today was not read, because it was outside this spawn's scope)
CHANGED: AGENTS/ZHAO/{workbook/KB.tsv (KB-189/190/191), workbook/PREDICTIONS.tsv (ZHA-16), docket/CATALYSTS.tsv (9/24, 10/09, 11/10-China), STATUS.md, NEXUS_BRIEF.md, board_log.tsv, outbox/2026-09-30_…MOFCOM-states-1-10…md, inbox→processed ×2}; PROME/inbox/2026-09-30_from-ZHAO_cadence-and-watch-terms.md; this memo
RESULT: ZHA-16 graded MISS (branch B via the declared residual), Brier 0.2025 at 45%. No instrument extends anything past 11/10: US and MOFCOM absence VERIFIED across 8 retrievals (17:34–17:37 ET, FR public inspection now 200); the Tariff Commission site returned 502, so that channel is SEARCH-NOT-FOUND. New: MOFCOM 9/28 states the 2027-01-10 extension in writing, but it is a statement, not an instrument. Inbox drained 2/2; cadence WEEKLY and 9 watch terms declared.
GAPS: The Tariff Commission primary (gss.mof.gov.cn) returned 502 ×3 and the gov.cn library is incomplete, so a 税委会 instrument is not ruled out (the re-open condition covers it). China Sept PMI (9/30) not read (outside scope). The 46号 cl.2 primary is still owed on 10/19.
WILL_NEEDS: None. (VOID stays available only if Will rules it; the owner declines.)
FOLLOW-UP: PROME routes the outbox signal (VULCAN/HAWK/HENRY/WATT/MIDAS) and the WQ-295 cc to WALTER · ZHAO re-checks instruments 10/09 (incl. 税委会) · Sept PMI read at the next ZHAO session · not pushed (PROME pushes at closeout).
