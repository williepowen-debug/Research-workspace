# L739 — gate-payoff test, PROME's fleet half (read 2026-10-29 09:2x ET)

**Row:** DOCKET L739 (Will 2026-10-15 15:52 ET, verbatim "Can we do this:" on RED's three pushback lines; RED's share delivered 10/28, packet `PROME/inbox/processed/2026-10-28_from-RED_S57-catchup-L739-verdict-and-weights.md`). **Owner of the verdict:** RED (its own STATUS). **This file:** PROME's read of the other desks, the control group RED's result needs.

## Method (the same proxy RED used, applied fleet-wide)
- **Unit:** lines changed (added + deleted) in each desk's own `AGENTS/<DESK>/` by commits whose subject names that desk, from `git log --numstat`. Lines, not minutes: no desk keeps minute records, and RED's own share used lines too.
- **Windows:** BEFORE = 2026-10-01 00:00 to 2026-10-15 15:52 ET (Will's word); AFTER = 2026-10-15 15:52 to 2026-10-29 09:00 ET.
- **Apparatus** = paths matching scripts/, tools/, `.py`, `.sh`, CLAUDE.md, PROTOCOL.md, boot/closeout files, design/, registry/, tests, LESSONS, MEMORY, MAINTENANCE, hooks, READS, checker files. Everything else (research, workbook, STATUS, reports, inbox) = domain.
- **Verdict per desk:** FELL / ROSE if the apparatus share moved more than 5 points with at least 200 lines in both windows; FLAT otherwise; UNKNOWN when either window has fewer than 200 lines or no commits (as the row says: never zero).
- **Not read:** MAINTENANCE-class entries and SCRATCH "WHAT I DID" blocks. The row names them; only RED keeps a MAINTENANCE file, so the line proxy is the only fleet-comparable instrument. A desk without such records reads UNKNOWN on minutes; the line proxy below is the stated substitute, disclosed as such.

## Result (apparatus share of desk-authored lines)

| Desk | Before % · lines · commits | After % · lines · commits | Verdict |
|---|---|---|---|
| AEOLUS | 0.3 · 6,219 · 18 | 2.4 · 2,950 · 2 | FLAT |
| BOND | 2.4 · 264,986 · 29 | 1.6 · 162,116 · 8 | FLAT |
| BRENT | 4.5 · 348,402 · 143 | 0.7 · 221,470 · 73 | FLAT |
| BROCK | 3.9 · 11,495 · 36 | 2.9 · 27,565 · 34 | FLAT |
| CARL | 3.1 · 31,082 · 42 | 7.4 · 32,677 · 81 | FLAT |
| CATO | 12.2 · 12,094 · 92 | 16.0 · 7,926 · 101 | FLAT |
| CORAL | 6.0 · 2,310 · 14 | 0.2 · 1,662 · 5 | FELL |
| CREED | 0.8 · 1,748 · 22 | 8.0 · 3,201 · 15 | ROSE |
| CRUISE | 2.2 · 898 · 16 | 11.6 · 4,908 · 28 | ROSE |
| CYPHER | — · 0 · 0 | 4.8 · 13,964 · 40 | UNKNOWN |
| DAEDALUS | 11.2 · 49,273 · 139 | 6.7 · 46,983 · 84 | FLAT |
| DEWEY | 0.6 · 89,975 · 23 | 14.4 · 15,981 · 61 | ROSE |
| FALCON | 16.6 · 6,633 · 38 | 1.5 · 16,109 · 30 | FELL |
| FERT | 1.5 · 1,143 · 14 | 1.2 · 51,561 · 22 | FLAT |
| FLG | 4.4 · 68 · 2 | 1.3 · 9,641 · 21 | UNKNOWN |
| GIBBS | — · 0 · 0 | 9.8 · 2,286 · 14 | UNKNOWN |
| HANS | 20.9 · 1,056 · 10 | 14.2 · 2,088 · 16 | FELL |
| HAWK | 7.0 · 574 · 5 | 11.2 · 4,974 · 20 | FLAT |
| HENRY | 6.2 · 3,705 · 12 | 0.6 · 249,038 · 22 | FELL |
| HOMER | 0.8 · 1,127 · 7 | 1.5 · 17,938 · 14 | FLAT |
| ISHM | — · 0 · 0 | 0.3 · 109,169 · 15 | UNKNOWN |
| LABOR | 0.6 · 6,441 · 25 | 15.0 · 4,301 · 31 | ROSE |
| LIQUID | 11.0 · 58,214 · 63 | 0.2 · 401,828 · 71 | FELL |
| MARCO | 21.2 · 1,582 · 14 | 1.0 · 62,364 · 18 | FELL |
| MIDAS | 18.0 · 166,909 · 35 | 4.1 · 377,895 · 44 | FELL |
| NEXUS | 2.1 · 8,846 · 34 | 2.0 · 105,845 · 54 | FLAT |
| ORACLE | 28.8 · 925 · 6 | 4.4 · 4,098 · 12 | FELL |
| OSPREY | 39.7 · 1,985 · 18 | 43.7 · 1,997 · 24 | FLAT |
| OTTO | 31.4 · 3,273 · 26 | 4.0 · 42,920 · 47 | FELL |
| OZK | 0.8 · 183,731 · 35 | 0.7 · 83,740 · 29 | FLAT |
| RED | 37.3 · 6,852 · 46 | 7.5 · 1,616 · 11 | FELL (RED's own: 45.2% → 2.6% on its narrower perimeter) |
| REGINALD | 8.4 · 44,766 · 130 | 1.5 · 206,437 · 92 | FELL |
| SAM | 5.6 · 2,625 · 12 | 1.5 · 39,771 · 18 | FLAT |
| SHADE | 6.4 · 5,350 · 42 | 7.5 · 2,447 · 5 | FLAT |
| TERRY | 8.8 · 20,280 · 125 | 1.5 · 139,311 · 57 | FELL |
| VIOLET | 2.6 · 73,588 · 19 | 39.2 · 227,886 · 10 | ROSE |
| VULCAN | 12.3 · 7,975 · 30 | 1.8 · 98,995 · 57 | FELL |
| WAL | 1.8 · 43,395 · 32 | 1.1 · 97,813 · 42 | FLAT |
| WALTER | 11.0 · 175,586 · 367 | 5.9 · 812,961 · 280 | FELL |
| WATT | 0.3 · 44,777 · 20 | 0.0 · 86,250 · 17 | FLAT |
| YURI | 0.2 · 76,300 · 18 | 24.6 · 141,194 · 12 | ROSE |
| ZHAO | 18.4 · 158 · 2 | 1.8 · 435 · 4 | UNKNOWN |
| RAV · YEYOU | under 200 lines | — | UNKNOWN |

**Tally over 36 desks with both windows readable: FELL 14 · ROSE 6 · FLAT 16; UNKNOWN 7.**

## Reading
- RED's apparatus share fell, as RED's own rule required for "the gate paid". But **14 of 36 readable desks fell by the same proxy, and none of them had RED's gate.** The fall is a fleet-wide pattern in this fortnight, not a signature of RED's gate.
- The likeliest common cause is on the record, not inferred from this table: the after-window holds the WQ-530 process-backlog triage, Will's 10/20 "trade ideas loosened" turn and a run of Will-launched catch-up sessions that moved large data and research files (LIQUID 401,828 lines, WALTER 812,961, MIDAS 377,895, HENRY 249,038). Big domain dumps shrink any desk's apparatus share without a minute of apparatus work changing.
- The proxy's weaknesses cut both ways and are the same for every row: lines are not minutes; one large TSV or saved source file dominates a window; the path pattern is PROME's (a desk's own checker under `research/` reads as domain); the subject-prefix rule drops commits whose subject does not name the desk.
- **What the fleet half therefore says:** RED's verdict on its pre-stated rule stands as RED's; the control group does not let the fall be attributed to the gate. If the gate's payoff is to be shown, it needs a measure the data-dump confound does not move (apparatus commits per session, or MAINTENANCE minutes kept at the desks that have none). That is a design question for RED and DAEDALUS (the companion census, L739's sibling row), not a finding this read can supply.

$0 moved. No threshold, grade or weight changed. Packet to RED: `AGENTS/RED/inbox/2026-10-29_from-PROME_L739-fleet-read.md`.
