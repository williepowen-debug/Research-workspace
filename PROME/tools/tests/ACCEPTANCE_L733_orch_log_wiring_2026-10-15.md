# ACCEPTANCE — L733: wire the EXISTING orchestration-log writer and checker (last-mile wiring plan, step 1)

**Written:** 2026-10-15 15:1x ET (PROME `prome-81`, desktop), BEFORE any edit (WQ-229). **Row:** DOCKET L733 (10/16). **Plan:** `PROME/plans/2026-10-15_last-mile-wiring-PLAN.md` § step 1. **Authority:** Will 14:38 ET 10/15 ("focus on working on these improvements after we reboot"); this is the session's ONE process change under the ceiling (`PROME/CLAUDE.md` § Session Process Controls).

## The defect, in its own terms (not the symptom)

`scripts/orch_log.py` (DAEDALUS, 9/3: `append` validates the new row and the existing ledger, appends ONE row atomically under a lock, and regenerates `PROME/state/ORCH_INFLIGHT.md` as its last step; `check` validates the whole ledger; 21-drill `--selftest`) has been the canonical writer since DOCKET L262 RESOLVED (9/4). No procedure routes to it: `git log -S orch_log.py -- PROME/CLOSEOUT.md PROME/BOOT.md PROME/ORCHESTRATION_PLAYBOOK.md` = nothing; the two `/closeout` runner copies name only `RUN-LOG row`; `prome_gate closeout` never runs `check`. Result on 10/15: every row typed by hand; two rows merged plus a blank line, found hours later by a hand width check. The view's own header proves the class: at this boot `ORCH_INFLIGHT.md` read `generated 2026-10-14 (1038 data rows)` while the ledger held 1097 data rows — 59 rows entered without the writer.

**Completion vocabulary used here (plan § vocabulary):** IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED (WQ-229) plus **WIRED** = the procedure sites route to the tool and the displaced manual action is removed, and **OBSERVED** = an instrument shows the tool was used by an ordinary workflow. (Writing the two new words into `PROME/CLAUDE.md` is a charter edit and waits for Will's word; they are used here as prose.)

## Acceptance conditions (properties; the test list derives from these)

| # | Condition | How it is checked |
|---|---|---|
| A1 | **WIRED — procedure sites.** Every site where an ORCH_LOG row is WRITTEN names `python3 scripts/orch_log.py append …` as the writer, with the flags that matter (`--date --desk --tier --touch --trigger --delivered --zero_capital --notes`, typed counts only as integers or omitted): CLOSEOUT.md Pre-closeout item 3 (the WQ-249 enumeration), CLOSEOUT.md step 8 (the ARGUS RUN-LOG row), ORCHESTRATION_PLAYBOOK.md § Two-tier "Ledger" line (the spawn step) and its "PROME closeout hook" line, and the `/closeout` runner (both copies). The hand-append wording ("logs to", "record … in ORCH_LOG.tsv" with no writer named) is REPLACED, never annotated — one live instruction per site. | `grep -n "orch_log.py" PROME/CLOSEOUT.md PROME/ORCHESTRATION_PLAYBOOK.md PROME/.claude/skills/closeout/SKILL.md .claude/skills/closeout/SKILL.md` ≥ 1 hit per file at the named sites; `grep -n "logs to \`PROME/state/ORCH_LOG.tsv\`" PROME/ORCHESTRATION_PLAYBOOK.md` = 0 |
| A2 | **Gate, BLOCKING — the ledger validates.** `prome_gate.py closeout` runs `scripts/orch_log.py check` as a BLOCKING row; a 12-column row, prose in a typed cell, a negative count or an unknown touch token stops the closeout at step 9 with the row named. | AST test: `mode_closeout` contains a `run_script(BLOCK, …, [sys.executable, "scripts/orch_log.py", "check"], …)` call; fixture: a ledger with one 12-column row ⇒ the gate row is BLOCKING and not ok |
| A3 | **Gate, BLOCKING — OBSERVED.** `prome_gate.py closeout` compares the view's header (`# generated <date> · source … (<N> data rows)`) with the live ledger's data-row count. Equal ⇒ ok. Ledger > view ⇒ not ok, detail names how many rows entered without the writer and the remedy (`orch_log.py check`, then `orch_log.py view`, and name the hand-typed rows in the closeout report). **Count, not date:** a same-day hand row passes a date test. | `check_orch_log_observed()` unit tests on fixtures (below) + AST test that `mode_closeout` calls it through `guard` |
| A4 | **Missing information fails LOUD.** A missing or unparseable view header, or an unreadable ledger, is reported as a failed BLOCKING row with UNKNOWN in the detail — never a pass, never a silent default. | fixture: no `ORCH_INFLIGHT.md`; fixture: a view whose header lacks the `(N data rows)` form |
| A5 | **The remedy is the writer's own view.** After a hand row is validated and `orch_log.py view` run, A3 passes; a writer append whose view step failed (the writer prints ⚠️ ROW APPENDED BUT VIEW NOT REGENERATED) is caught by A3 and repaired the same way. | fixture: append by writer ⇒ pass; hand row then `view` ⇒ pass |
| A6 | **Wrong owner / perimeter.** Only `PROME/state/ORCH_LOG.tsv` and `PROME/state/ORCH_INFLIGHT.md` are read; archive containers (`PROME/archive/ORCH_LOG_*.tsv`) never enter the count; a rotation (which rewrites hot + view under the lock) passes. | fixture with an archive file present ⇒ count unchanged |
| A7 | **The runners stay a pair.** Root and PROME `/closeout` skill copies identical after the edit (`check_claude_dir_drift` passes at the gate). | `diff -q` both copies; the gate's parity row |
| A8 | **One closeout runs with zero hand-typed rows.** This session's own ORCH_LOG rows (the WALTER/LIQUID/VULCAN doorbells need no rows — they are Will-launched desks; the ARGUS RUN-LOG row; PUBLISH CLOSE rows; any BROCK spawn) are appended with the writer, and A3 passes at the closeout gate on the live files. | the closeout gate's A2/A3 rows read ok; `git show <closeout commit> -- PROME/state/ORCH_INFLIGHT.md` shows the regenerated view in the same commit as the ledger rows |
| A9 | **Nothing else moves.** No rule's meaning changes; no tier, cap, authority or route changes; `PROME/CLAUDE.md` is not edited (charter; ask-first); BOOT.md is not edited (it carries no ORCH_LOG write step). | diff review by the independent reader |

## Neighbour categories (tests README; CONSIDER each, justified N/A is an answer)

| # | Category | Disposition |
|---|---|---|
| 1 | Ordinary | A2 clean ledger ⇒ ok; A3 equal counts ⇒ ok; a hand row ⇒ A2 or A3 fails with the row/count named |
| 2 | 🔴 Overlap | a row that is BOTH in the hot ledger and already in an archive container (a rotation that wrote the archive and failed before the hot replace — the writer's documented recoverable state): A6 counts the hot file only, so A3 compares hot against the view the rotation regenerated; the double copy is the scorecard consumer's to report (orch_log.py docstring), not this check's. Tested: archive present, count unchanged |
| 3 | Wrong owner | A6: archives excluded; a desk's own `board_log.tsv` or any other TSV never read. Tested by perimeter (the function names two paths) |
| 4 | Missing information | A4: no view · header without the count form · unreadable ledger ⇒ failed BLOCKING row with UNKNOWN. Tested |
| 5 | Concurrent activity | N/A beyond the writer: `append` already serializes under `fcntl.flock` and regenerates the view inside the lock; the check is read-only. Two sessions appending in turn each leave a view equal to the ledger. One residual: a check that reads the ledger while another session's `append` is mid-write sees a torn count for that instant — a re-run resolves it; not mechanized |

## Reads and completion note (filled as the work proceeds)

- **Read budget (WQ-178 / L511):** this is a batch over five files plus a gate change touching a BLOCKING row ⇒ a consequential repair: ONE independent read of the RESULT (diff + this file + a counterexample of the reader's own) before the step is called fixed; ❌ fixed, ⚠️ into the residue block below; a second read only if a ❌ fix changed a rule's meaning. Reads: 0 at writing.
- **States:** IMPLEMENTED — pending · TESTED — pending (`python3 -m unittest PROME/tools/tests/test_orch_log_wiring_L733.py`; `scripts/orch_log.py --selftest` 21/21; one live `prome_gate.py closeout --tier standard` run) · INDEPENDENTLY VERIFIED — pending · STILL UNRESOLVED — (filled at closeout).

## Declared residue

(filled after the read)
