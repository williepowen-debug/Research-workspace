# 2026-10-23 — To: PROME (from WALTER, walter-e2, boot-health pass on Will's word "Lets fix boot health issues", 00:46 ET)

**Two items for PROME. Neither is urgent; both were measured this sitting.**

## 1. ORCH_INFLIGHT.md is over the read budget, and the remedy is upstream (yours)

`PROME/state/ORCH_INFLIGHT.md` = **36,178 B** at 04:39Z 10/23, over the 32,550 B budget on WALTER's boot step 9b `whole` read (`scripts/read_cap_check.py --agent WALTER` 🔴 FINDING; it was 34,212 B at the 10/22 night boot). The file is generated, so rotation and rewording cannot fix it (the check says so itself); the fix is in what `scripts/orch_log.py view` projects.

Measured by section (bytes):

| Section | Bytes | Share |
|---|---:|---:|
| IN-FLIGHT rows (112) | 10,998 | 30% |
| Last `drained>0` per desk (103) | 11,279 | 31% |
| "Desks with a TOUCH row but NO drained>0" name list (469 names) | 13,274 | 37% |

- The 469-name list states of itself that it "proves nothing about liveness". Replacing it with a count (or a pointer to the TSV) would bring the view to about 23 KB, under budget, with no loss to WALTER's 9b use: WALTER reads IN-FLIGHT and the drained table, never that list.
- 33 IN-FLIGHT rows are dated September 25 to October 9 (coldreaders, helpers, ARGUS spawns from 10/03). If they finished, closing them is a second, smaller saving.

**ASK:** choose the projection change (or decline) at your next process pass. WALTER keeps reading the file whole until then and keeps reporting the finding.

## 2. Aged unconsumed deliveries: all BACKLOG, none EXPIRED; HOMER holds three ACTION items

Doctor `delivered_but_unconsumed`: 15 items older than 2 days at 6 desks, 5 ACTION. I classified each under BOARD_CONSUMPTION_SPEC §3.7 by reading the handoffs: **no dated consuming decision has passed on any of them, so all are BACKLOG (consumed at the owner's next boot), none EXPIRED, none COSTLY.**

| Desk | ACTION | INFO | Oldest | Note |
|---|---:|---:|---|---|
| HOMER | 3 | 0 | 10/20 | 001 NAR pending sales, 014 construction starts/permits basis, 028 housing hours and mortgage spread bases; HOMER STATUS last 10/19 |
| CRUISE | 1 | 1 | 10/19 | 019 repeat-losers counter-evidence |
| CATO | 1 | 0 | 10/19 | 012 owner-update relay; CATO is manual (Will-launched only) |
| SAM | 0 | 6 | 10/20 | — |
| BOND | 0 | 2 | 10/20 | — |
| OTTO | 0 | 1 | 10/19 | plus 2 consumed-but-unfiled (OTTO's filing hygiene) |

**Recommendation (not a doorbell; HOMER's state is UNKNOWN, not DARK):** if a HOMER wake is already planned, these three ride it; if not, they can wait for HOMER's next session, since none carries a deadline. Your call under existing authority.

## Done on WALTER's side this sitting (for your record, no action)

- `LABOR_DOWN` INDEX section retired: SIG-W-20261007-013 re-filed to CONSUMER_STAGFLATION through a new generator ledger `AGENTS/WALTER/registry/CLUSTER_RECATEGORIZATIONS.tsv` (Will chose the mechanism 10/23; signal file untouched).
- 22 delivery_log NOTE rows classified once (`AGENTS/WALTER/registry/NOTE_ROWS_REVIEWED.tsv`): 8 correct notes, 14 rows that were corrections carried as notes. Your copy of the 9/14 `-015` NOTE is one of those; `SIG-W-20260914-015` and `-025` now carry `status: PARTIALLY-CORRECTED` markers.

**Source:** doctor and `read_cap_check` runs 2026-10-23 04:35–04:55Z; handoff reads in `AGENTS/<desk>/inbox/WALTER/`.
**Priority:** 🟡
