# FLG TRIGGERS NOTES ARCHIVE — rotated 2026-11-16

Verbatim text rotated out of `workbook/TRIGGERS.tsv` on 2026-11-16 (read-cap rotate-tier: 27,943 B = 86% of the 32,550 B budget; rule 5 stop below 70%). History, never current: each segment was superseded by a later note or a consumed check in the live row. crc32 of each segment = UTF-8 bytes exactly as between its fences. Segments joined with " | " where several adjoining note segments moved together.

## header line 1 (prior-refresh chain from 2026-11-01 back, the 2026-10-21 Staleness sweep stamp and the superseded Next field)

crc32 `18fa5955`

```
 ; prior 2026-11-01 (T-01 CONSUMED for Q3 and re-dated to the Q4 Call Report 2027-02-14, notes rotated to archive/TRIGGERS_NOTES_ARCHIVE_2026-11-01.md; T-02 M3 gap ask added; T-04 Call Report MF read) ; prior 2026-10-28 (notes appended T-01 CDR pull worked, T-07 price, T-10 call cross-check + $2.9B rent-regulated, T-12 discovery deadline passed/outcome unknown; no Next_Check moved) ; prior 2026-10-23 (Q3 print consumed: T-03 re-dated to the Q4 release [EST] 2027-01-29; T-07/T-08/T-12 re-dated to the 10-Q wake 2026-11-09) ; prior 2026-10-22 (fix pass from the 10/22 desk sweep: T-02/T-04/T-09/T-10 text corrected to KB-045/KB-052 and the 10/21 re-key; T-08 anchor note clarified; T-01 FFIEC token note) ; prior 2026-10-21 (catch-up wave 2, pre-print: T-03 CONFIRMED HARD 10/23 06:00/08:00 ET; T-08 leg 2 re-graded VERIFIED at the docket; T-12 three corrections + two open risks; T-07 RED broke 10/7, 10/21 close $11.07; T-04/T-05 re-keyed to the rail's 10-Q instruments) ; prior 2026-10-01 (T-08 FIRED 10/1, graded by FLG) ; prior 2026-09-27 (T-13 registered; T-03 re-dated 10/16) | Staleness sweep: 2026-10-21 | Next: T-03/T-07/T-08/T-12 at the 2026-10-23 wake (DOCKET L522), then T-02/T-04/T-05 2026-11-09
```

## T-03 Notes segment(s) — the 10/21 HARD confirmation and the 10/23 consumption

crc32 `7dd62265`

```
✅ 2026-10-21 CONFIRMED HARD (PROME 10/16 packet, re-verified by FLG 10/21 22:2x ET at finviz.com/news/400829 = issuer PR 2026-10-09): Q3-2026 release Fri 2026-10-23 ~06:00 ET, call 08:00 ET (Otting, Smith, Raffetto; webcast ir.flagstar.com; replay to 10/27, archive to 11/20). Same date as the 9/27 [EST] => no re-date of the wake; Anchor_Type EVENT -> HARD. The 10/16 Next_Check was consumed late (FLG idle 10/1-10/21; boot flagged it 10/21). Pre-print frame written BEFORE the print: reports/2026-10-21_Q3-2026_PREPRINT_FRAME.md (KB-FLG-072). || CONSUMED 2026-10-23 08:3x ET by FLG (PROME prome-03 spawn, DOCKET L522 print leg): 8-K acc 0000910073-26-000080 read (release + deck; call UNREAD - no transcript reachable, replay to 10/27); graded in reports/2026-10-23_Q3-2026_PRINT_GRADE.md (KB-FLG-086..091). RE-DATED to the Q4-2026 release [EST] 2027-01-29 (Q4-2025 release was 2026-01-30, 8-K acc 0000910073-26-000018); Anchor_Type HARD -> EVENT until the issuer PR confirms a date.
```

## T-07 Notes segment(s) — the 10/21, 10/23 and 10/28 price reads

crc32 `8051244e`

```
2026-10-21 FLG (wave 2; REGINALD 10/07 packet consumed): RED BROKE on the 10/07 settled close $11.30 (REGINALD-graded; -20.6% vs FROZEN $14.24). No band beyond RED; no further price packet is registered. FLG read 10/21 22:20 ET (fetch.py + yfinance daily closes): close $11.07 (-0.45%) = -22.3% vs FROZEN $14.24; 10/19 close $10.96 = lowest in the window. 9/30 -> 10/21: FLG -5.1% vs KRE +1.7% vs VLY +3.2% => FLG-specific residual ~-7 to -8pp. CAUSE UNKNOWN: EDGAR CIK 910073 newest filings = two Form 4s 2026-10-16 (both code F = tax withholding, not sales); no 8-K since 7/24. Price is not a thesis input; no position (TRADE.md). Next_Check stays 2026-10-23 (backup only; REGINALD's vx_ladder_check.py is the detector) (KB-FLG-074). || 2026-10-23: fetch.py 08:37 ET returned $11.44 as-of 2026-10-22 (stale, pre-market); print day reaction not read by FLG. Price is not a thesis input (frame rule 9). Next_Check -> 2026-11-09 (10-Q wake; backup only, REGINALD detector owns the row). | 2026-10-28 FLG: close $10.16 [fetch.py, 10/28]; REGINALD: ladder exhausted, 14 settled closes below RED since 10/7 (REGINALD STATUS 10/28). Row state unchanged.
```

## T-08 Notes segment(s) — the 10/23 rotation pointer and the 10/23 post-fire read

crc32 `12495016`

```
📦 ROTATED 2026-10-23 (read-cap rotate-tier, 79 percent): the 10/1 FIRE grade and the 10/21 leg-2 re-grade moved VERBATIM to archive/TRIGGERS_NOTES_ARCHIVE_2026-10-23.md § T-08 (crc32 9f970fd9). Their state, unchanged: FIRED 10/1 on the letter (Order #58 0%/0% in force, KB-FLG-071); leg 2 VERIFIED at the docket through doc 253, after that UNKNOWN (KB-FLG-073); Response EXECUTED; expectation pre-registered: Q3/Q4-2026 commentary not formation, Q2-2027 near-zero (T-09), bite Q2-2028 (T-11). || 2026-10-23 post-fire read on the Q3 release/deck: issuer now names rent regulation as a credit-cost driver (CEO) and leads the provision attribution with higher rates; FY2026 provision guide $90-140M -> $160-170M, FY2027 $100-150M -> $175-225M; MF >=50% RR ALLL 2.87% -> 2.97%, but the RR NON-ACCRUAL reserve fell $76M -> $72M (KB-FLG-086/087/090). No freeze quantification. Next_Check -> 2026-11-09: 10-Q roll-forward + FDM read (T-02/T-13).
```

## T-12 Notes segment(s) — the 10/21 corrections, the 10/28 and the 11/07 notes

crc32 `4717e155`

```
🔁 2026-10-21 CORRECTIONS (PROME 10/01 packet; artifact PROME/data/2026-10-01_NYSCEF-453580-2026-docket-read.md, verified by FLG): (1) '8/21 transfer' WITHDRAWN — 8/21 was the adjourned RETURN DATE of the order to show cause (doc 24); NY County record received 7/22, Richmond 8/24; the transfer date itself was not seen. (2) The '~9/16 discovery order' = an INTERIM decision and order dated 9/16 (doc 222, cited not read) granting count four to the extent of limited discovery and RESERVING decision on the rest; further orders 9/18 (doc 226) and 9/24 (doc 239: screenshots by 9/29, complete response within 30 days of 9/24 = ~10/24). (3) Case status 'Disposed-Court Date/Application Pending' is NOT a decision — both orders read are marked NON-FINAL DISPOSITION; no judgment seen. TWO OPEN RISKS now carried here: (a) an EMERGENCY-RELIEF motion after petitioners review the City's production (doc 240: 'will continue to assess the need to seek emergency and interim relief'; their 10/1 letter on the initial production, doc 244, UNREAD); (b) a MERITS ruling annulling Order #58 after its effective date — petitioners say it 'will affect lease renewals through September 30, 2027'. WATCH DECISION (FLG, 10/21): no new registered gate (GATE-FLG-T08 is terminal; a new gate would be a Will-gated registration). Coverage = this row at each FLG wake + the WALTER intake term; FLG adopted a clean set of 17 R3-tested phrases (8 landed + 9 adds) incl. 'restraining order rent freeze' (a PRECURSOR hit is wanted for risk (a)) and the city-wins pair, packet to PROME/inbox 2026-10-21. Documents FLG needs read (Will's hands, asked via PROME): doc 244 and every entry after doc 253, best after the ~10/24 production. Next_Check stays 2026-10-23 (KB-FLG-073). || 2026-10-23: release and deck silent on the case; no ruling inferred (frame rule 8). NYSCEF still 403 from this box; the ~10/24 City production and docs 244 + after 253 remain Will's hands via PROME. Next_Check -> 2026-11-09 (next FLG wake); intake term covers the gap. | 2026-10-28 FLG: ~10/24 City discovery-response deadline PASSED, outcome UNKNOWN — no merits ruling or production reported in news through 10/28 (KB-096). A news NOT-FOUND is not a docket read; docs after 253 still need Will's browser. | 2026-11-07: 10-Q Note 17 and Part II silent on Kenilworth, no ruling inferred. City discovery response outcome still UNKNOWN; NYSCEF needs a browser. Re-dated to the judge-stated end-of-year marker.
```

## T-13 (whole row; RETIRED 2026-11-07, Next_Check RETIRED)

crc32 `6f4492cf`

```
T-13	Q3-2026 FDM + payoff read — WQ-313 item 1 (PROME DOCKET L522): Will's verbatim reconciliation question on the Q2-26 MF subsequent-default disclosures ($29M three months vs $286M six months), plus the MF modification stock/past-due split and the non-accrual payoff leg	Q3-26 release (~10/23 EST) + 10-Q (~11/9 EST) FDM tables and non-accrual roll-forward	RETIRED	RULE	one-off	KB-FLG-069/070 left the modification finding UNRECONCILED; Will ruled (20:49 ET 9/27) the 47% is a changing aggregate population, not a cohort failure rate	REGISTERED 2026-09-27 21:19 ET at closeout, PROME ask. CHECK-BY 2026-11-13 (PROME DOCKET L522). If the Q3 data is insufficient: record the figures AS REPORTED, "unreconciled / not cohort-identifiable" — NO interpretive round (Will). Q3 may not identify the Q2 cohort. | 2026-11-07 RETIRED, consumed at the Q3 10-Q: figures recorded as reported, unreconciled / not cohort-identifiable, no interpretive round (Will 2026-09-27 20:49 ET). Report section 4, KB-FLG-107. MF modified stock $471M, current $264M, 90+ $207M. Non-accrual payoffs Q3 $76M, cures $144M.
```
