# HENRY desk sweep, 2026-11-05 10:40 EST (Will-requested)

Read-only except this file and one correction of a false line in STATUS.md. Prior sweep: reports/2026-10-21_desk-sweep.md, whose C5 carry-ins are not re-listed because it closed them.

## OWED
| # | Finding | Evidence | Severity |
|---|---|---|---|
| O1 | WATCH_FOR verdict never answered, 35 days. WALTER's R3 test 10/1: 3 passed, 3 rejected, 7 replacements offered; asks adopt or decline by name in a packet to PROME/inbox | inbox/processed/2026-10-01_from-WALTER_R3-watch-for-verdicts.md; DOCKET L565, dated 11/3, lists HENRY outstanding | 🟠 |
| O2 | My 11/5 packet and STATUS said no past-due HENRY row. FALSE: the scan keyed on the owner column; L565 names HENRY in its text. The 10/21 sweep read L565 and missed it too | PROME/inbox/2026-11-05_from-HENRY_catch-up-to-live-data.md | 🟠 corrected |
| O3 | Today's gamma_flip.py change not logged in MAINTENANCE.md | grep "IV = 0" MAINTENANCE.md = 0 | 🟡 |
| O4 | 8 WALTER cards logged deferred 9/17 "to next boot", never reopened, one ACTION (SIG-W-20260914-027). All 7+ weeks old | board_log.tsv, one row each | 🟡 |
| O5 | Operating Dashboard 10/22; its prediction panel says no live row while HEN-57/58/59 are OPEN | dashboard/dashboard_tpl.html:287 | 🟡 scheduled |

## BROKEN / WRONG
| # | Finding | Evidence | Severity |
|---|---|---|---|
| B1 | SPX red line in ACTIVE THRESHOLDS is 6,494, a March level my charter calls retired and dead | STATUS.md:116 vs CLAUDE.md:193 | 🟠 Will's level; not changed |
| B2 | Charter inbox protocol step 2 tells me to check VX.tsv and FLOW.tsv, both FROZEN and marked do-not-read | CLAUDE.md § Inbox Processing Protocol | 🟠 |
| B3 | Charter says HENRY owns ISM and VIX/vol regime; ISHM owns the ISM trigger (WQ-507 A), VIOLET the vol broadcast | CLAUDE.md:121,123 and role line | 🟡 |
| B4 | Boot quoted at ~12s; measured 168.7s 11/5. --quick 5s; credit 3.7s, gamma 1.3s, fetch 2s, so the cost is by elimination step (g), the fleet-wide consumer scan (timeout 180s) | CLAUDE.md step 3c; boot.py:617. Not directly timed | 🟡 |
| B5 | Step (g) printed 525 hidden lines, mostly coincidental number matches in airline and SEC files; zero certified stale | 11/5 boot; consumer_check --old 7706 --old 7711 37 candidates | 🟡 |
| B6 | ECON_CALENDAR says ISM Mfg <49; STATUS bands are <50/<48/<47 and the trigger is ISHM's | domain/ECON_CALENDAR.md Key Thresholds | 🟡 |
| B7 | Cross-horizon put wall label: PUBLISHED metric names drift (put_wall, put_wall_14d, put_wall_WITHHELD, ndx_walls_WITHHELD), so the ledger cannot be read as one wall series | workbook/PUBLISHED.tsv | 🟡 |
| B8 | Broken pointers: STATUS.md § BREADTH to PROME/inbox/... (moved to processed); CLAUDE.md FLEET_DIRECTORY.md and walter_route_check.py resolve only under AGENTS/DAEDALUS/ | STATUS.md:94; CLAUDE.md:43,141 | 🟢 |

## STALE
| # | Finding | Evidence | Severity |
|---|---|---|---|
| S1 | REFERENCE_TABLES still shows March levels and "CTAs flip at 6,494" in the live sequence | domain/REFERENCE_TABLES.md:11-24 | 🟡 |
| S2 | research/README.md last updated 3/5, repeats the demoted "0DTE 65%" as a finding | research/README.md | 🟡 |
| S3 | 18 KB rows ACTIVE, 13 from 8/6-9/2, including "gamma flipped POSITIVE" and "kill 7bp away" | workbook/KB.tsv | 🟡 |
| S4 | MEMORY.md carries superseded notes: line 34 two-machine concurrency (now serial), line 46 pull credit from siblings (reversed by line 49), line 49 "divide by... no" | MEMORY.md | 🟡 |
| S5 | Auto-memory reference says dashboard version 2 of 10/21; STATUS said version 4 of 10/22 | memory/auto/reference_henry_operating_dashboard.md | 🟢 |
| S6 | LAST_COMPLETION.md is 11/2; overwritten at closeout, expected | — | 🟢 |
| S7 | ECON_CALENDAR passed rows stay; rebuild due before 11/20 | domain/ECON_CALENDAR.md:7 | 🟢 dated |

## RETIREMENT CANDIDATES (root Data Hygiene: >60 days, not boot-read, no live reference)
JULY_NODE_PRELOAD_2026-07-06.md (referenced from PREDICTIONS.tsv: check first) · domain/sources/ 2 files · reports/2026-08-28_DELIVERY, _T3v2_COSPEC, 2026-08-29_HEN-42_FLIP_RECORD · workbook/KB_AUDIT.md · research/outputs + research/prompts (41 files with research/credit, Feb-Mar; research/credit has 11 live references, keep). Moves need a read of each reference.

## INCOMPLETE / MISSING
| # | Finding | Severity |
|---|---|---|
| M1 | Charter FILES table omits reports/, status_archive/, KB_AUDIT.md | 🟢 |
| M2 | No SPX −10% row in ACTIVE THRESHOLDS though the charter send-table has it (7,037 from the 7,818.93 record) | 🟡 |
| M3 | SOXX 450→~141: no split record, unconfirmed | 🟡 |
| M4 | 4 predictions EXPIRED ungraded (HEN-17, 18, 20, 31); PREDICTIONS still 23 status tokens, grandfathered | 🟢 |
| M5 | Consensus UNKNOWN on all six 11/2-11/5 release rows; no consensus source on this desk | 🟡 |
| M6 | research/ 118 MB on disk, 37 MB tracked; 3 October folders hold 113 MB, largest tracked file 10 MB | 🟢 |
| M7 | My 11/5 rotation dropped the STATUS pointer to the 10/29 carried items and the EO 14421 line; now only in STATUS_COLD ROT-11/05. Reviewed: AAL, F1, WQ-507/508, CYPHER boundary, DGX are closed; EO 14421 is conditional | 🟢 |

## CLEAN (checked)
All 3 scripts and the dashboard builder compile; boot --selftest PASS; PREDICTIONS 54 rows 7 columns, no duplicates; KB 169 rows 15 columns, no duplicates; board_log 834 rows, no duplicate signals; PUBLISHED 4 columns; all wikilinks resolve; read cap rc=0, LESSONS 75%; corrections check rc=0; evals 3/3 PASS 10/21; STATUS 138 lines, MEMORY 70.
