# brief_pin_check.py #17 split: a pin already behind at the brief's own commit blocks again — 2026-11-18

**Authority:** NEXUS schema-owner answer `edcd280634` (amendment 11 first sentence unchanged: the pin must EQUAL STATUS HEAD at the moment the brief is committed), relayed by PROME prome-6e 15:42 ET as the next step inside WQ-719 A (no Will word needed, PROME's reading). #18 (rebase-orphaned pin) is WILL_QUEUE row 721: NOT touched here.

## Acceptance conditions (written before the build, 15:45 ET)

| # | Condition |
|---|---|
| A1 | Brief committed while STATUS HEAD was X, pin names an OLDER STATUS commit than X → new token `STALE-AT-COMMIT`, ⛔, rc 1 |
| A2 | Pin equal to STATUS HEAD as of the brief's commit, STATUS moved later → `STALE-PIN`, ⚠️, rc 0 (unchanged from cd64583eae) |
| A3 | Brief folded in the SAME commit as a STATUS change, STATUS moved later → `STALE-PIN` advisory, never `STALE-AT-COMMIT` (the same-commit fold satisfies A11 by construction) |
| A4 | `PIN-UNRESOLVED` unchanged (rc 1); a blocking class still outranks `CANNOT-EVALUATE` (rc 2); an advisory stale pin still does not mask rc 2 |
| A5 | The rc-1 tag names exactly the blocking class(es) present |
| A6 | Live run reported; any live `STALE-AT-COMMIT` is checked at git by hand before it is called real |
| A7 | Mutation: with the split removed (every stale pin graded `STALE-PIN`), the new legs FAIL |
| A8 | One diff-only independent read (Opus) before it is called fixed |

## Build and verification (15:41–15:45 ET)

- **Code:** STATUS HEAD as of the brief's commit = the last STATUS commit reachable from it. If the pin does not match it and the brief commit did not itself touch STATUS → `STALE-AT-COMMIT`. The distance is counted by ancestry (`rev-list --count pin..s_at_b -- STATUS`); if the pin is not an ancestor, the line says "another line of history". The rc-1 tag lists the blocking classes present.
- **A1–A5:** met. Selftest 21/21 (new fixtures G and H, rc legs for G and C+H, three tag legs).
- **A6:** met. Live 15:45 ET rc 0, no STALE-AT-COMMIT (FLG and OTTO remain later lag).
- **A7:** met. With the split removed, 3 legs FAIL; with the same-commit exemption removed, 2 legs FAIL.
- **A8 independent read #2:** Opus, diff-only, its own fixtures including merges and deletions. **ACCEPT WITH RESIDUE.**
  - **❌ row 6:** on non-linear history the line printed "-1 STATUS commit(s) older", counted by log position. Fixed with the ancestry test. Re-run on the reader's fixtures: Q1 and P1 now say "not an ancestor of it"; G and P8 say "1 older"; P5 and P7 stay STALE-PIN.
  - **⚠️ row 8:** the STALE-PIN docstring over-claimed for a brief history with no STATUS commit. Reworded.
  - The fix round was checked on the reader's fixtures and the selftest only; it was not re-read.
- **Residue, declared:**
  - **Rows 12 and 13 (policy, NEXUS/Will):** a commit that touches a brief without changing its content blocks if the pin lags. That covers a mode-only change, and another desk's sweep editing a header line. The only remedy offered, a re-pin, would assert freshness nobody checked. No live case.
  - **Row 7:** an unproven "older" is now worded "not an ancestor".
  - **Row 14:** STATUS deleted and re-added. Minor.
  - **Rows 11 and 22:** predate this diff (a pin dropped by a merge, a desk directory rename).
- **WQ-721 A (Will 15:44 ET):** the CHECKS On_FAIL text now says the unresolvable pin is corrected pointer-only at the closeout where the script reports it. The script's own PIN-UNRESOLVED line gives no instruction, so no code change; return codes unchanged.
