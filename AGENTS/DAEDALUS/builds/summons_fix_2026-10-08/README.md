# L548 summons fix — isolated patch for PROME (built 2026-10-08, DAEDALUS)

⛔ Not built by PROME 9/29 — the session's one process change was the registry line (R1).

**State: IMPLEMENTED + TESTED (author). NOT INDEPENDENTLY VERIFIED.** It changes a gate check's output contract, so it is a consequential repair (WQ-229) and owes one independent reader with its own counterexample before it is called fixed. Live `PROME/tools/` untouched; nothing committed outside this directory.

## What changed (`summons-fix.patch`, 2 files)
- `prome_gate.py` — `check_desk_catalyst_summons(today=None)`: forward-window rows (TODAY · in Nd) listed FIRST and in FULL; past-due rows become one bit per desk, `<DESK> N past-due (oldest <date>) — owner prunes`; dead ledgers unchanged; the complete list (every row, old per-row text, plus a count of undated rows skipped) goes to a run-dir log with the standard `full output: <path>` suffix; a log-write failure says `full output: UNAVAILABLE (...)` and never loses the check. Severity, name, WQ-184 owner text, ok-rule and quiet detail unchanged; both call sites still `guard(check_desk_catalyst_summons)`.
- `prome_gate.py` — `_check_log_path(name)` extracted from `run_script` (same LOG_DIR lazy-init and `NN-<slug>.txt` naming), so the summons log reuses the one mechanism; `run_script` behaviour unchanged.
- New `PROME/tools/tests/test_summons_window_first_L548.py` — 11 tests from ACCEPTANCE.md AC-a…AC-g + neighbours.

## Live ledgers, same bytes, same clock (Thu 2026-10-08 08:17 ET; LABOR sha256 9cf49011…, VULCAN 22e79db6…)
**Before:** `VULCAN 2026-10-05 [P2] CME + Silicon Data list cash-settled COMPUTE  (PAST-DUE 3d — ungraded?) · LABOR 2026-10-08 [HIGH] Initial claims … (TODAY) · LABOR 2026-10-08 [MED] Canadian counter-tariffs … (TODAY) · VULCAN 2026-10-09 [P1] GPU-rental panel reading 5 … (in 1d) (+3 more)` — three VULCAN 10/09 rows (mag7 post-close · MU 10-K · TSMC 6-K) hidden today.
**After:** `LABOR 2026-10-08 [HIGH] … (TODAY) · LABOR 2026-10-08 [MED] … (TODAY) · VULCAN 2026-10-09 [P1] GPU-rental … (in 1d) · VULCAN 2026-10-09 [P1] mag7.py POST-CLOSE reading … (in 1d) · VULCAN 2026-10-09 [P2] MU FY2026 10-K … (in 1d) · VULCAN 2026-10-09 [P2] TSMC September revenue 6-K … (in 1d) · VULCAN 1 past-due (oldest 2026-10-05) — owner prunes` + `full output: …/00-desk-catalyst-summons-bd-02-.txt` (7 lines, untruncated).

## Test receipts (scratch copies of HEAD 45b320134; never the live tree)
| Run | Result |
|---|---|
| new file on CURRENT code | Ran 11 · FAILED failures=5 errors=1 · rc 1 (6 defect tests fail; 5 contract tests pass) |
| new file on PATCHED code | Ran 11 · OK · rc 0 |
| whole `PROME/tools/tests` discover, base vs patched (archive, no .git) | 733 run each; base 75 FAIL/ERROR, patched 69 — the difference is exactly the 6 new tests; the 69 others are identical in both (no-.git, fetch/FRED environment) |
| git-backed scratch: gate_isolation_L294_F7 · agent_freshness_L294_F4 · external_findings · dashboard_build_receipt_L339 · new file | 128 run each; base 11 FAIL/ERROR, patched 5 — the 5 are identical in both (pre-existing, see residue) |
| `git apply --check` on the live repo root | OK (both paths) at 08:2x ET; applying to a copy of live `prome_gate.py` reproduces the `after` hashes in `target_hashes.json` |

## Apply (PROME, in its own process slot — WQ-299 R1)
1. `sha256sum PROME/tools/prome_gate.py` must equal `target_hashes.json` before; if not, stop — do not three-way an outdated patch.
2. `git apply AGENTS/DAEDALUS/builds/summons_fix_2026-10-08/summons-fix.patch`
3. `python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_summons_window_first_L548.py` (expect 11 OK), then the existing gate suites.
4. `python3 PROME/tools/prome_gate.py boot` (non-advancing) — the summons line lists the forward window in full and ends with `full output:`.
5. Independent reader (consequential repair) before calling L548 fixed.

## Residue (declared, not fixed)
- Undated ledger rows are still skipped in the DETAIL (unchanged behaviour); they are counted only in the full log — and when NOTHING else flags (quiet case, AC-f) no log is written, so undated rows stay silent there. This falls short of ACCEPTANCE.md's missing-information row ("no longer silent anywhere"); declared, not fixed, because surfacing them would change the quiet detail AC-f freezes.
- Forward-window detail is unbounded by design (window = `SUMMONS_WINDOW_DAYS`, 2d); a ledger with dozens of rows in two days would print them all — the property the row asks for.
- Past-due bit carries count + oldest date only; the per-row past-due text lives in the log.
- Out of scope, seen while testing: `test_gate_isolation_L294_F7.NoFabricatedDefaults.test_no_bare_check_call_sites_remain` FAILS on live HEAD today (two unguarded `check_orch_closeout()` call sites) — pre-existing, PROME's, not touched here.

## Independent result read — 2026-10-08 (added after the read; no code change)
Fresh-context Opus reader, own counterexamples (300-ledger differential fuzz, collision/run-dir cases, live end-to-end gate run): **ACCEPT-WITH-RESIDUE, ❌ 0 · ⚠️ 5 · ✅ 12** — `INDEPENDENT_READ_2026-10-08.md`. Residue R1 (an unbalanced quote in a `notes` field makes csv swallow later rows ⇒ a false "quiet", pre-existing) and R2 (an ISO-shaped invalid date aborts the rest of its ledger, pre-existing) belong to a separate follow-up row, not this patch; R3 corrected in ACCEPTANCE.md (pointer only); R4/R5 optional hardening. State now: IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED (patch as built; the ACCEPTANCE cell edit after the read is a pointer fix and unreviewed).
