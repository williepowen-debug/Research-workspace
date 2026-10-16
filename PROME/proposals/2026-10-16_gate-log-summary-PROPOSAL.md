# Gate logs: counts in the verdict, drill-down on demand — PROPOSAL (process change 2 for the 10/16 PM sitting; needs WQ-445 A or a session exception)

**Written:** 2026-10-16 15:2x ET (PROME, session 8fb641db). **Source:** waste survey item 15 (`reports/2026-10-15_waste-survey.md`); ideas row 2026-10-15 "Gate logs summarised"; measured at this boot. **Class:** PROCESS (BOOT.md step 5 log-read contract · CLOSEOUT step 9 mirror · one gate summary line). **Status:** PROPOSED — not implemented; Will's word is the gate (the sitting's one process change is already spent on the ACTIVE_DECISIONS digest, 2d1292581).

## The cost, measured 15:2x ET at this boot (`measure.py` over `/tmp/prome-boot-8fb641db/`)
| Named log | Bytes | What it holds |
|---|---|---|
| 00 orchestrated-touch closeout evidence (WQ-249) | 114,868 | four-state counts on lines 2/7/24/25 (ASKED→receipt 4 · still working 16 · already closed 0 · went dark 28) + 608 `UNKNOWN` legacy rows from 9/1–10/12 that no boot can resolve |
| 29 session evidence beside due rows | 45,163 | one JSON line per desk saying presence UNKNOWN (the gate line already says rc=0, "fleet presence UNKNOWN") |
| 04 firetime flags | 26,897 | 49 carried flags, re-printed every sitting (survey item 14) |
| 27 spawn list · 30 read budgets · others | ~31,000 | the gate line carries each one's verdict and names |
| **Total named logs + gate.txt** | **217,895** | read "to EOF" through a 5.8 KB pager ≈ 38 calls at boot, again at closeout |

Today's boot read `gate.txt` to EOF and did NOT read the named logs to EOF — a SKIPPED control under the manual as written (disclosed in the 15:2x ET report correction). The gate's printed lines carried every verdict the boot acted on; the one item the logs held that the verdict line did not was the WQ-249 four-state count.

## Smallest edit
1. `PROME/tools/prome_gate.py` `check_orch_closeout`: the printed summary line carries the four counts and the names of today's touches (`ASKED→receipt 4 (CRUISE REGINALD ORACLE BROCK) · still working 16 · dark-before-ask 28 · UNKNOWN 608 (≤2026-10-12, legacy)`), read from the script's own output, never recomputed. Nothing else in the gate changes.
2. `PROME/BOOT.md` step 5 log-read contract: *"Read `gate.txt` to EOF. A named log is read (bounded reader, to EOF) ONLY when its gate line is ⚠️/❌ AND the line's preview does not name the item PROME must act on, or when PROME drills into one named flag. The WQ-249 log's four-state counts are on its gate line; its UNKNOWN rows older than the current week are legacy and are never a boot read."* Same sentence at `PROME/CLOSEOUT.md` step 9 (the closeout gate's logs), both runner copies' pointer lines unchanged.
3. READS.tsv: no row change (the logs are `summary`-class outputs already).

## Acceptance conditions (before editing, if approved)
| # | Category | Condition |
|---|---|---|
| A1 | Ordinary | the WQ-249 gate line shows the four counts + today's names; a fixture log with known counts renders the exact line |
| A2 | 🔴 Overlap | a touch that is ASKED→receipt today AND dark on an older row (BROCK 10/15 vs 10/16) counts once in each state, never netted |
| A3 | Wrong owner | the gate line never summarises another check's log; firetime's 49 flags stay firetime's |
| A4 | Missing information | a log without the four count lines ⇒ the gate line reads `counts UNKNOWN — read the log`, never zeros |
| A5 | Concurrent | N/A — single reader of a single run directory |
| A6 | Size | the gate line ≤ 300 chars; boot read bytes drop by the logs' size (measured at the next boot) |
| A7 | Wiring | WIRED = BOOT 5 + CLOSEOUT 9 sentences; OBSERVED = the next boot reads gate.txt only and reports no skipped control for the logs |

Reads: one Opus read (a gate-adjacent contract; WQ-447). Reversal = one revert.
