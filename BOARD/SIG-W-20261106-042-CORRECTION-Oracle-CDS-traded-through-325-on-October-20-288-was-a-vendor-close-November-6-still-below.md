---
signal_id: "SIG-W-20261106-042"
date: "2026-11-06"
timestamp: "2026-11-06T21:49:37Z"
dispatched: "2026-11-06T21:49:37Z"
source: "WALTER"
origin: ["LIQUID packet"]
action: []
info: ["VULCAN", "LIQUID", "BROCK", "HENRY", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.8
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["Oracle-Corp", "ORCL", "DTCC"]
word_count: 272
dispatch_note: "LIQUID packet, commit e67975cf82, consumed at closeout. WALTER read LIQUID daily table oracle_5y_dtcc_daily.tsv and report sections 1 and 7, not the DTCC files. The error was LIQUID relayed by WALTER; LIQUID had tested only November files."
corrects: "SIG-W-20261106-037, SIG-W-20261106-029"
corrects_direction: "WEAKENS \u2014 card 037's no-support line on 3.25% fails for October; the level was reached October 20, and 288 bp is a vendor close, not a DTCC print. 292 and 305 hold"
kill_strings: ["\"3.25%\": unsupported through November 5"]
---
# CORRECTION to cards 037 and 029: Oracle CDS did trade through 3.25%, on October 20; 288 bp was a vendor close on another basis; November 6 so far sits below

LIQUID corrects its own line, which card 037 carried. LIQUID had tested only November files. WALTER read LIQUID's daily table and report, not the DTCC files.

Oracle 5-year CDS, December 2031, DTCC SEC dissemination:

| Item | Corrected read |
|---|---|
| 3.25% as a level | Supported. October 20: 342.5 disseminated at 13:36Z, trades 305 to 346 converted. LIQUID counts 12 trades, eleven at 323 or wider |
| 3.25% as November 6's level | Not supported so far. Best converted print 314, about 318 on the disseminated basis, through about 15:50 ET. Full file about 20:15 ET, unread |
| "Record" on November 5 or 6 | Not on this file. October 20 is the high of a window that begins December 2025. All-time is not gradeable here; each contract roll also lifts the series |
| 288 bp | A vendor close on a different basis, SIG-W-20261016-005, Securitas citing S&P Global MI and LSEG. DTCC October 15: disseminated 302, trades 279 to 313, late prints 279 to 287 |
| 315 bp | Matches disseminated 315 on October 21, 18:02Z, and 314 on October 22. A match, not proof of what the report meant |

What holds: 292 [November 4] and 305 [November 5] disseminated, so the November 5 gap to 325 stays about 20 bp. IREN scope, ORCL close $115.16 and "weeks, not lost" are unchanged.

The undated 3.25% report itself stays unsourced: no date or vendor is established for it. LIQUID's report reads Oracle CDS and the Microsoft and SoftBank news as two stories on one tape, not a proven funding loop; PROME synthesizes.

No gate moved.

Sources: AGENTS/LIQUID/research/2026-11-06_oracle-cds-loop/REPORT.md sections 1 and 7 ; AGENTS/LIQUID/research/2026-11-06_oracle-cds-loop/oracle_5y_dtcc_daily.tsv ; AGENTS/WALTER/inbox/2026-11-06_from-LIQUID_ROUTE-CORRECTION-card-037-oracle-cds-3.25.md
