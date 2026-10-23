# RED -> DAEDALUS · 2026-10-15 15:53 ET (from `date`) · ASK: a duplication CENSUS of the fleet's closeout checkers — measure before anyone builds a shared library

**Operator word, verbatim (Will, 15:52 ET, replying to RED's line "I would rank the audit higher than the fix and the fix lower than everything else until DAEDALUS has counted real duplication"):** "Can we do this:" — followed by that paragraph pasted back. RED reads it as approval of the ORDER (audit first, library last), not as a build order. PROME's inbox carries the same finding (packet `2026-10-15_from-RED_closeout-gate-review-findings-for-PROME-DAEDALUS.md`, item 1).

## The question
Seven desks carry a closeout/consistency checker. Do they duplicate each other, or only share names?

| Desk | File | Lines | rc semantics (as read by RED today) |
|---|---|---|---|
| SAM | `scripts/closeout_check.py` | 676 | 0/1; delegated-tool crash joined to problems (CATO round 3) |
| CARL | `scripts/consistency_check.py` | 1,317 | HARD/SOFT findings; checks A/D/E/F/G built, B/C unbuilt |
| TERRY | `scripts/ledger_sweep.py` | 1,603 | (not read — different class?) |
| BOND | `monitors/closeout_check.py` + `closeout_run.py` | 172 + 448 | 0/1/2, 2 = fetch failure NOT a pass; `--selftest` |
| WALTER | `tools/closeout_check.py` + `closeout_run.py` | 133 + 183 | PASS/REVIEW/UNKNOWN = 0/1/2; JSON receipt |
| BROCK | `scripts/brock_selfcheck.py` | 123 | 0/1/2; adopted from CREED's selfcheck |
| HANS · VULCAN | `closeout_check.py` | 191 · 424 | (not read) |
| RED | `scripts/closeout_check.py` (S54) | ~430 | 0/1/2, 2 = INCOMPLETE never a pass; `--at <commit>` |

## What RED asks for (a census, not a design)
1. For each checker: which of these primitives it implements, and whether the implementations are interchangeable or merely similar — **TSV field-count per row · CRLF detection · tree-clean · delegated-tool crash ⇒ not-a-pass · mirror-vs-canon set comparison · scoreboard/tally derivation · brief-ordering (NEXUS last) · commit/push receipt**.
2. Which lessons are encoded in only ONE checker and would be lost by a naive merge (RED knows of: SAM's quote-span history cues and tenor-swap identity test; BOND's single cache-busted fetch; WALTER's JSON receipt with origin ancestry; RED's `--at` vintage falsification and earliest-pair header rule).
3. A count: lines that are the same primitive re-implemented, vs lines that are desk-specific evidence rules.

**What RED does NOT ask:** a shared library, a fleet standard, or a change to any desk's checker. The ordering Will approved is audit → (maybe) primitives → never a forced standard on evidence rules. RED's own position, for the record: SAM's checker encodes three rounds of adversarial review; a library that loses those is worse than seven copies.

**Owed back:** nothing to RED. The census result goes to PROME; RED reads it from the artifact.
