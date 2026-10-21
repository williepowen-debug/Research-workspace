# ACCEPTANCE — fire-time new-vs-persisting split (WQ-467 read 1 C4; Will "yes go ahead now" 2026-10-21 11:02 ET)

**Written before the code** (WQ-229). Process change 5 of 5 this session. Closes the DOCKET row registered 2026-10-21 for C4.

## Defect, in its own terms
`scripts/firetime_check.py` keeps owner-routed flags on its list ("persist") and does not separate new flags from old ones (47 at the 10/21 boot). Under WQ-467, a fire-time ACTION OWED line needs a disposition for all of its flags. So either every persisting flag is re-answered at every boot, or a NEW DATE flag that needs a full logic re-read hides inside a blanket "routed".

## Design
- `PROME/tools/firetime_delta.py` parses a fire-time log into flag keys: artifact · kind · stable core. A DATE DRIFT core is "artifact says <date> ('<token>')", without the docket "near:" list, which changes as DOCKET changes. A DEAD POINTER core is the pointer. UNREADABLE and other kinds use the message.
- **Baseline:** `PROME/state/firetime_dispositioned.tsv` (tracked, so it travels between machines). One row per dispositioned flag: key fields · date first dispositioned · pointer to the disposition record.
- **Compare:** current flags minus baseline = NEW. Current flags in the baseline = PERSISTING (each carries its pointer).
- **Accept (AMENDED after read 1, ❌2/⚠️4):** `--accept --pointer <existing record>` rewrites the baseline to exactly the current flag set. Rows already present keep their original date and pointer; new rows get today's date and the given pointer; flags no longer present drop out. Accept refuses an incomplete or crashed log and a pointer that does not exist. A baseline row absent from the current run is itself OWED at the gate. It is removed with `--prune`, which drops only rows no longer reported, adds nothing, and is always allowed, even while a NEW flag is deferred (AMENDED after read 2, ❌A). A recurrence after a prune reads NEW. If the prune is skipped, the gate keeps reporting the line as owed for as long as the row is absent. The window in which a recurrence could read as persisting is therefore a boot where PROME ignored an owed prune, and that boot is already PARTIAL.
- **Gate:** the fire-time check stays ACTION class. It passes (✅ `[action]`) when there are 0 NEW flags. It flags `[ACTION OWED]` when there is ≥1 NEW flag and names them. Persisting flags are counted with the baseline's pointers and are not owed.

## Acceptance conditions
- **FD1 — new vs persisting:** a flag whose key is in the baseline is PERSISTING; any other flag is NEW. Changes only in the "near:" text of a DATE DRIFT flag do not make it new.
- **FD2 — owed only when new:** the gate's fire-time line is ✅ with 0 new flags, and `[ACTION OWED]` naming each new flag (up to a stated cap, with the rest counted) when there are any.
- **FD3 — fail closed:** a missing or unreadable baseline counts every flag as NEW and says so. It never reads as clean.
- **FD4 — accept is explicit:** the baseline changes only through `--accept` with a non-empty `--pointer`. The gate never writes it.
- **FD5 — accept is faithful:** after accept, the baseline equals the current flag set. Kept rows keep their first date and pointer; dropped flags leave.
- **FD6 — no flag lost:** the parser counts the same number of flags as the indented ⚠️ lines in the log. A parse miss is reported, never silently dropped.

## Neighbours (consider)
- **Ordinary:** the 10/21 boot's 47 flags, seeded as the baseline (pointer `PROME/reports/2026-10-21_firetime-boot-flags-disposition.md`), give 0 new on the same log.
- **Overlap:** one artifact can carry both new and persisting flags; each flag is judged separately.
- **Wrong owner:** the fire-time checker is DAEDALUS's and is not modified. This is PROME's own boot tooling. The false-positive classes stay on DAEDALUS's row.
- **Missing information:** no baseline gives all flags NEW plus a note (FD3). An unreadable log is a gate error, as now.
- **Concurrent activity:** two machines run serially. The baseline is a tracked file committed by PROME only.

## Reads
- **reads: 1.** Independent read 1, 2026-10-21 ~11:07 ET (Opus, own counterexamples in scratch; the live baseline was never written): **HOLD, 2 ❌ · 5 ⚠️.**
  - **❌1 FIXED:** a crashed `firetime_check` exits 1 and read as ✅ clean. Now `firetime_delta.validate` refuses a traceback, rc 1 without the `→ N flag(s).` footer, a footer count ≠ printed flags, and rc 0 with flags; the gate records each as UNKNOWN (not ok) and keeps the checker's last line (⚠️5 fixed too).
  - **❌2 FIXED:** baseline rows absent from the run are counted and OWED until `--accept` prunes them.
  - **⚠️3 FIXED:** BOOT.md says accept runs ONLY when every NEW flag is done or routed; a deferred flag is never accepted.
  - **⚠️4 FIXED:** accept needs an existing pointer and a complete log, and prints the flags it adds and how many it prunes.
  - **⚠️7 REFUTED:** `PROME/CLAUDE.md` § Process ceiling reads FIVE since 7ec4bd663 (Will 10:05 ET), so 5 of 5 is within the ceiling.
  - 8 tests added (16 total).
  - **Live receipt (CORRECTED after read 2, ⚠️C):** the first gate dry run after the fix owed a prune of 3 rows *no longer reported*. They were not necessarily fixed: all three are in `AGENTS/LABOR/STATUS.md`, LABOR removed only `12/24`, and the `2027-01-01` / `2027-01-15` lines are still there, probably because nearby DOCKET rows changed (INFERRED). The baseline was pruned with `--accept` on a complete 11:05 ET run → 44 flags, 0 NEW, 0 stale. If those two return, they read NEW, which is the safe direction.
  - **State:** IMPLEMENTED · TESTED. The ❌1 fix touches a gate, so read 2 is owed (WQ-229).

## Declared residue (WQ-178)
- **⚠️6:** the DATE DRIFT key (artifact · date · token) persists across a rewrite of the artifact and across a new DOCKET row near that date. A new instruction line reusing a dispositioned date in the same file, or a newly registered nearby DOCKET row, is not re-owed. Candidate fix: re-owe a persisting DATE flag whose artifact was committed after `first_dispositioned`. Carried on the C4 DOCKET row (dated 10/25, L768).
- **ALLOWLIST EXPIRED keys** include a line number, so an allowlist renumbering reads as NEW (too fine, safe direction).
- **Read 2 (2026-10-21 ~11:13 ET, Opus): HOLD, 1 ❌ · 5 ⚠️.**
  - **Confirmed:** the ❌1 crash fix holds against fresh crash forms (`os._exit(1)`, `sys.exit('msg')`, signal −9, partial output + exit). The ⚠️7 refutation is confirmed.
  - **❌A FIXED:** `--prune` mode added (drops only rows no longer reported; adds nothing; always allowed); a three-boot test covers deferred NEW, then prune, then recurrence reading NEW.
  - **⚠️B FIXED:** with rc unknown (the CLI path), a log with no artifact lines and no flags is refused, and `--pointer` must be a file.
  - **⚠️C:** the receipt is corrected above.
  - **⚠️D:** the L768 artifact cell now names this file.
  - **⚠️E FIXED:** the gate's owner text carries the done/routed-only accept rule, `--prune` and the commit step; BOOT.md no longer says it does not list checks, and says a prune's disposition is "done: pruned".
  - **⚠️F FIXED (message):** rc 1 with no output reads "rc 1 with no footer". The repeated `sys.path` insert is cosmetic and is left as is.
  - 4 tests added (20 total).
- **reads: 2 of 3.** ❌A changed the accept rule's meaning, so a third read is permitted (WQ-229 / Review budget).
- **Read 3 (FINAL, 2026-10-21 ~11:17 ET, Opus): RELEASE, 0 ❌ · 4 ⚠️.** ❌A VERIFIED fixed: the three-boot sequence with `--prune` gives the recurring flag as NEW. No gate path reads ✅ while a NEW flag exists or a baseline row is absent. The live baseline's md5 was unchanged by the read. The 20 tests pass. **Episode closed at 3 reads.** State: IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED for everything read 3 examined. Nothing was changed after read 3.

## Declared residue from read 3 (WQ-178 — ⚠️ not fixed; carried on DOCKET L768)
- **R3-1 (truncated log):** a log holding only ✅ lines (a run killed before its first flag) passes `--prune`/`--accept` as a clean 0-flag run, because the checker prints no footer at 0 flags. This fails closed (rows come back NEW), but the next accept loses their first date and pointer. The real fix is a completion marker in `scripts/firetime_check.py` (DAEDALUS-owned).
- **R3-2 (prune from the wrong log):** pruning from an older log that still contains a fixed flag removes nothing and prints ✅. The gate's prune text says `<log>`, not `<this log>`. Candidate fixes: write `<this log>`, and print ⚠️ when 0 rows are removed. Until then, PROME prunes only from the same boot's log.
- **R3-3 (nothing to check):** when the checker prints `no artifacts to check` (rc 0) and the baseline has rows, the gate owes a prune that both `--prune` and `--accept` refuse. The line stays owed and the boot PARTIAL until the window has artifacts. This fails closed and should be rare.
- **R3-4 (wording):** BOOT.md step 5 still says "Fire-time: rc=1 always means act". Under C4, an rc 1 run with 0 NEW reads ✅. That errs toward acting, but it contradicts "NEW flags only are owed". "done: pruned" appears only in BOOT.md, and the gate's prune hint lacks the `python3 PROME/tools/` prefix. Rewording step 5 changes a rule's meaning, so it is carried rather than edited unreviewed.
