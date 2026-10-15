# RED closeout hardening — build spec for the fresh session (Will: "do the build in a fresh window", 2026-10-15 14:46 ET)

**Scope approved in principle by Will 2026-10-15 14:46 ET; the build itself runs in a NEW session on a non-catalyst slot.** Comparison basis: PROME/CLOSEOUT.md · WALTER tiered closeout + closeout_run.py · CARL consistency_check.py · BROCK brock_selfcheck.py · SAM closeout_check.py (and its 9/19 lesson) · TERRY ledger_sweep.py. RED's current closeout = CLAUDE.md § WRITE-BACK + § ADDENDUM CLOSEOUT.

## Why (measured 2026-10-15, S53)
Every RED check is per-file. Nothing asked whether STATUS, the TSVs and the NEXUS brief agreed. Result at boot: STATUS showed 10 open challenges vs 6 in canon; three prediction tallies disagreed; FT-10 read four ways; and RED's own 10:33 addendum skipped two mandatory steps (A2 SCRATCH, A4→W3 CHANGELOG) with no instrument noticing — a cold reader did.

## Build, in order (each falsified before trusted — finding_test_the_guard_not_just_the_guarded)
1. **`scripts/closeout_check.py`** (read-only; exit 0 clean / 1 findings / 2 cannot run). Checks:
   a. STATUS open-challenge table == set of non-RESOLVED rows in `workbook/CHALLENGES.tsv` (IDs, grade token, status token).
   b. Prediction tally line (NC/NW/NA) == counts off `workbook/PREDICTIONS.tsv`, and identical on STATUS, CALENDAR and NEXUS_BRIEF.
   c. Every registry `state` token appears identically beside its row in the STATUS trigger table; the STATUS header's FT counts (e.g. "FT-02 1 of 3") match the registry.
   d. SCRATCH carries a section whose stamp is within 60 min of STATUS's newest stamp (A2 floor).
   e. If `registry/FALSIFICATION_TRIGGERS.tsv` (state col), `workbook/VX_HISTORY.tsv` or the STATUS weights table changed vs HEAD → `thesis/CHANGELOG.md` has an entry dated today (A4→W3), and OUTBOX has an entry dated today (A4→W8).
   f. NEXUS_BRIEF header carries the same HOLD / net-bear as STATUS.
   g. Aggregate the existing instruments: schema_check, gen_trigger_scan --check, review_debt --quiet (axes ①–④), read_cap_check --agent RED, claim_check weekday, memory_index_check --slug (if a memory was written), ledger_staleness --nudge RED.
   **Falsification vintage:** run it against the files at commit `75e1b12b3` (pre-fix): it MUST flag (a) 10 vs 6, (b) three tallies, (c) FT-10, and against `47b622ddf` it must flag (d)/(e) for the 10:33 addendum. Then run on HEAD: clean.
2. **Generate the two mirror tables** (challenge table, tally line) from the TSVs into STATUS between `<!-- GEN:… -->` markers via `scripts/status_mirrors.py --write` / `--check`; the check in 1(a)/(b) then reads the generator's output. Generation beats checking (finding_hand_fixing_named_rows_is_not_fixing_the_class).
3. **Charter edits** (rules only; reasons → CHARTER_PROVENANCE.md § 3): add a **Bounce** tier (mid-day restart, 3–5 SCRATCH lines, optional checkpoint commit) beside first-ending (W1–W10) and later-ending (addendum); add **SKIPPED reporting** — any step not run or run by reasoning instead of by the instrument is named SKIPPED in the closeout message and the headline is PARTIAL; pull root 1b–1e commands inline into W10 (CARL's form); retitle WRITE-BACK as "WRITE-BACK (this IS the closeout)" (SAM's 9/19 lesson); make closeout_check.py the gate before W10's commit (exit 1 blocks).
4. **Closeout report shape:** COMMITTED / PUSHED named separately with the safe-push receipt line verbatim; SKIPPED list or "none"; what is owed at next boot.
5. Also queued, same session if time: the `--help` refusal on boot.py / review_debt.py / schema_check.py (SCRATCH 6d) and the BASIS hash compare (SCRATCH 6b).

## Not in scope
The Network Sweep (Will holding), any thesis work, any threshold change.
