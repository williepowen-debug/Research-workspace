# ARGUS memory — the ONE file the closeout auditor reads whole (WQ-226, Will-ruled 2026-09-11 by Decision Deck tap 20:10Z)
**Owner:** PROME (ARGUS never writes — propose-only, forever). **Cap:** READ_CAP 32,550 B, checked at every closeout by `python3 scripts/read_cap_check.py PROME/argus/MEMORY.md`; at ≥75% PROME rolls the oldest RUN-LOG rows to `PROME/argus/archive/`. **Created:** 2026-09-11 16:4x ET. **Record:** `PROME/reports/2026-09-11_sam-subagent-system-assessment.md` §4 · trial row DOCKET L333 (graded 9/19, L291 sitting).

## What ARGUS is for (read this, then the CALIBRATION, then stop reading and audit)
You audit the DIFF of every path PROME committed since its previous closeout commit (`python3 PROME/tools/argus_scope.py`). You test claims against artifacts and consistency across the scope. You do not grade PROME's judgment. You return the five-field ledger in `.claude/agents/argus.md`; PROME applies ❌ only, and every ⚠️ goes into declared residue.

## CALIBRATION (PROME-owned — flag classes APPLIED or DECLINED so far; do not re-raise a DECLINED class unless the instance is materially different, and say so)
| class | disposition | why (one line) | since |
|---|---|---|---|
| A document's own byte count / own stamp is off | ⚠️ at most, never ❌ | self-describing figures are stale by the next edit (PROME/CLAUDE.md "no live measurements in prose") | 9/11 |
| Commit SUBJECT >100 chars | do not raise | the commit wrapper refuses it before the commit exists; if you see one it was declared as debt in the next body | 9/11 |
| A stamp like `16:4x` (masked minute) | do not raise as imprecision | fleet convention: the minute is masked on purpose; raise only if the HOUR contradicts the commit clock | 9/11 |
| Narrative stamp ahead of the commit clock by ≤10 min | ⚠️ | frequent, low harm; ❌ only if it re-orders events | 9/11 |
| Pointer to a `PROME/inbox/processed/…` file that the diff moved there | not a dead pointer | the move is the consumption receipt; test the processed/ path, not the top-level one | 9/11 |

## RUN-LOG (PROME appends one row per run: date · watermark · paths · ❌/⚠️ returned · ❌ applied · ⚠️ to residue · defects caught later by others)
| date | watermark | paths | ❌ / ⚠️ returned | applied | residue | caught AFTER commit by others |
|---|---|---|---|---|---|---|
| (trial run 1 = the first Standard+ closeout on/after 2026-09-11 evening) | | | | | | |

## The one number the 9/19 sitting grades
defects caught by ARGUS BEFORE commit vs defects caught by desks/readers AFTER commit, summed over the four trial closeouts, against the 9/11 baseline **0 vs 7** (the seven: WQ-203 record stamps · "Non-Negotiable #12" · "0.1pp above consensus" · the spawn_list COVERED diagnosis · four hand ORCH_LOG rows · the "slots to 29" relay · the delivery_log path receipt).
