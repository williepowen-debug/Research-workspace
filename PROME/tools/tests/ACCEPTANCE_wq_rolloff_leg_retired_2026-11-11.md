# ACCEPTANCE CONDITIONS — the queue check's roll-off leg is retired (D:L898)

**Written before the edit, 2026-11-11 12:06 ET (from `date`), PROME prome-2b.** Authority: Will in PROME's chat 2026-11-11 12:03 ET, verbatim "okay you have my approval do here what you think is best go ahead", on the list of five backlog items shown at 12:01 ET; class C12 (WQ-673 A). Scope: `check_will_queue()` in `PROME/tools/prome_gate.py`, the branch that reads the RECENTLY DONE section. No other check, no manual, no queue row.

**The defect in its own terms (D:L898):** the leg reports "nothing overdue for roll-off" while it cannot read the date in the done-row form in use ("Done 2026-10-31 12:40 ET"), so it passes silently. At this edit 117 of 210 done rows are older than seven days and none is flagged. A check that cannot fail is retired, not left printing an all-clear. The seven-day roll-off itself guards nothing: the file is read by digest and by tools, and the 11/11 queue review used the retained rows.

**Conditions**
1. `check_will_queue()` emits no `ROLL-OFF` problem for any input, and its all-clear text no longer says roll-off is checked.
2. Every other verdict is unchanged. On a synthetic queue holding a due-today row, a passed row, an aging undated row and done rows in the legacy datable form, the current form and a recent one, the problem list after the edit equals the list before it with the `ROLL-OFF` lines removed, in the same order.
3. On a copy of the live `PROME/WILL_QUEUE.md` the problem list is identical before and after.
4. `PROME/tools/queue_parser_selftest.py` passes after the edit.
5. The diff removes the done-section branch, the two words of all-clear text and corrects the comment that describes the leg. Nothing else in the file changes.
6. Rolling old done rows to `PROME/archive/` stays available by hand; no manual step names the gate's roll-off flag (checked: no hit for it in BOOT, CLOSEOUT, CLOSEOUT_PROCEDURES, SYSTEM or the closeout skill).

**Neighbours considered**
- Ordinary: the live queue, condition 3.
- Overlap: a done row in the legacy form that the old code COULD date and flagged; after the edit it is silent. That is the intended change, condition 2.
- Wrong owner: N/A, `prome_gate.py` is PROME's own tool and the queue is PROME's file.
- Missing information: a done row with fewer than three cells was skipped by this branch and is caught by `done_rows_check.py`; unchanged.
- Concurrent activity: N/A, the check reads one file once.

**Independent read:** one Opus reader who did not write the edit, with at least one counterexample of its own, before the repair is called fixed (a gate is touched).

## Results

**Recorded 2026-11-11 12:10 ET (from `date`), PROME prome-2b.**

| Condition | Result | Evidence |
|---|---|---|
| 1 | MET | harness: no `ROLL-OFF` in the new list on either input; all-clear text reads "stamp current; nothing due today, passed, aging or misfiled" |
| 2 | MET | synthetic queue: old 5 problems (2 `ROLL-OFF`), new 3, new equals old minus the `ROLL-OFF` lines in order |
| 3 | MET | copy of the live queue: old [] and new [] with 210 done rows present (the old leg flagged none of the 117 past seven days) |
| 4 | MET | `python3 PROME/tools/queue_parser_selftest.py` rc 0, 26/26 |
| 5 | MET | diff is three hunks, 5 insertions and 24 deletions (reader confirmed) |
| 6 | MET | no manual, skill, test or tool expects the flag or the old text (reader's search) |

**Independent read (Opus, `reader-rolloff`, ledger `reader_rolloff.md` in the session scratchpad): VERDICT ACCEPT, 0 failures, 3 warnings.** The reader confirmed the removed branch had no side effect (no `continue`, no touch of the actionable count, could not raise), ran 11 counterexamples of its own (done section before OPEN, a digit-led done row, a third section, no done section, malformed and impossible-date done rows, a second OPEN heading after done, a roll-off-only queue, truncation, CAP, a missing file, no stamp) with new equal to old minus `ROLL-OFF` on each, and ran the wq578, WQ467 and WQ460 gate tests. Not checked by the reader: pyflakes (not installed), `test_gate_isolation_L294_F7.py`, and the full gate in boot or closeout mode (both advance state).

**Declared residue (warnings, not fixed; no edit was made after the read):**
1. Two older comments in `prome_gate.py` (near the `_mmdd` year-roll note and in the MISFILED block) still describe roll-off as gate behaviour. Comments only; fix on contact.
2. A queue whose only problem was a roll-off row now reads clean, so that ACTION OWED line no longer appears. Intended.
3. `PROME/ideas/list.tsv` line 44 names the flag in idea text that no code reads.

**States:** IMPLEMENTED · TESTED (author harness and selftest) · INDEPENDENTLY VERIFIED (the read above) · STILL UNRESOLVED: nothing. The full gate has not been run end to end on the new code; tonight's closeout gate is its first full run.
