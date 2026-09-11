# ARGUS memory — the ONE file the closeout auditor reads whole (WQ-226, Will-ruled 2026-09-11 by Decision Deck tap 20:10Z)
**Owner:** PROME (ARGUS never writes — propose-only, forever). **Cap:** READ_CAP 32,550 B, checked at every closeout by `python3 scripts/read_cap_check.py PROME/argus/MEMORY.md`; at ≥75% PROME rolls the oldest RUN-LOG rows to `PROME/argus/archive/`. **Created:** 2026-09-11 16:4x ET. **Record:** `PROME/reports/2026-09-11_sam-subagent-system-assessment.md` §4 · trial row DOCKET L333 (graded 9/19, L291 sitting).

## What ARGUS is for (read this, then the CALIBRATION, then stop reading and audit)
You audit the DIFF of every path PROME committed **or has PENDING (uncommitted)** since the recorded baseline (`python3 PROME/tools/argus_scope.py`). You test claims against artifacts and consistency across the scope. You do not grade PROME's judgment. You return the five-field ledger in `.claude/agents/argus.md`; PROME applies ❌ only, and every ⚠️ goes into declared residue.

## CALIBRATION (PROME-owned — flag classes APPLIED or DECLINED so far; do not re-raise a DECLINED class unless the instance is materially different, and say so)
| class | disposition | why (one line) | since |
|---|---|---|---|
| A document's own byte count / own stamp is off | ⚠️ at most, never ❌ | self-describing figures are stale by the next edit (PROME/CLAUDE.md "no live measurements in prose") | 9/11 |
| Commit SUBJECT >100 chars | do not raise | the commit wrapper refuses it before the commit exists; if you see one it was declared as debt in the next body | 9/11 |
| A stamp like `16:4x` (masked minute) | do not raise as imprecision | fleet convention: the minute is masked on purpose; raise only if the HOUR contradicts the commit clock | 9/11 |
| Narrative stamp ahead of the commit clock by ≤10 min | ⚠️ | frequent, low harm; ❌ only if it re-orders events | 9/11 |
| Pointer to a `PROME/inbox/processed/…` file that the diff moved there | not a dead pointer | the move is the consumption receipt; test the processed/ path, not the top-level one | 9/11 |

## RUN-LOG (PROME appends one row per run: date · baseline · paths · ❌/⚠️ returned · ❌ applied · ⚠️ to residue · defects caught later by others)
| date | baseline | paths | ❌ / ⚠️ returned | applied | residue | caught AFTER commit by others |
|---|---|---|---|---|---|---|
| (trial run 1 = the first Standard+ closeout on/after 2026-09-11 evening) | | | | | | |

## The one number the 9/19 sitting grades
defects caught by ARGUS BEFORE commit vs defects caught by desks/readers AFTER commit, summed over the four trial closeouts, against the 9/11 baseline **0 vs 7** (the seven: enumerated ONCE, canonically, at `PROME/reports/2026-09-11_sam-subagent-system-assessment.md` §2 — **do not restate the list here.** ARGUS trial run 1 found this line and the report listing DIFFERENT items for two of the seven, inside one audit scope; the number the 9/19 sitting grades against cannot exist in two versions. `finding_correction_beside_an_instruction_leaves_two_live_instructions`).
| 2026-09-11 | 9132969a0 | OWNED 38 · SHARED 89 · UNATTR 0 | ❌5 ⚠️6 | **5 applied** | 6 → residue | n/a (pre-commit) | **Trial run 1.** Scope = the session that REDESIGNED this tool. ❌: A4 still violated by a real PROME artifact (`888924d2e`, a FIRMS CSV in a lane with no name hint) after TWO attempts to be clever about noise — the fix was still a FILENAME key; this memory file itself still said committed-only after F1 changed the other surface; the 9/19 baseline **7** enumerated two different ways inside one scope; `argus_baseline.json` hand-written while its `_written_by` named the tool; the C4 cost figures did not sum. All five fixed pre-commit. **Sequencing defect to record honestly: run 1 executed AFTER most commits, so its pending half was empty — the number below is not a clean pre-commit measurement.** |
