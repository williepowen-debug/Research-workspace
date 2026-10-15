# LIQUID alert/SRF repair — independent read #2 (the result read, WQ-229) · VERDICT: RELEASE

**Record written 2026-10-15 09:00 ET by PROME prome-73.**

**Reader:** a fresh PROME-spawned read-only reviewer (Claude Code Agent tool, general-purpose, model Opus), launched 08:47 ET 2026-10-15 by PROME prome-73 (ORCH_LOG `PROME-READER-LIQUID-SRF` touch `3-SPAWN-READER-WQ229-READ2`; episode reads 1 → 2). **Subject:** the author's fix for read #1's two ❌ — acceptance additions #8/#9 committed BEFORE the code at `88fece5a7`, code + two tests at `fd036576c`; author's note `AGENTS/LIQUID/research/2026-10-14_alert-SRF-repair/2026-10-15_CE1-CE6/FIX.md`. **Method:** mirrors by `git archive` under the PROME scratchpad (`ws/` = HEAD, `prefix/` = scripts at `d186bb16a` + HEAD test file, `old/` = `701511870`), network blocked (`unshare -rn`), read #1's harness re-run from a copy (it writes `runs/` beside itself), new counterexamples in `harness2/`, receipts in `receipts2/` (08:51–08:57 EDT). Nothing written in the repository. Not run: `baseline-probes.py` (writes into the repo); the author's live FRED 78-distinct-dates check (network blocked) — UNKNOWN.

## Disposition (PROME, WQ-229)
**IMPLEMENTED · TESTED (author, 20/20; the two new tests fail on the pre-fix code) · INDEPENDENTLY VERIFIED (read #1 HOLD → fix → read #2 RELEASE, with its own counterexamples; 0 differences on well-formed inputs across the differential runs).** The watcher and the SRF guard are VERIFIED as of `fd036576c`. The episode is CLOSED at two reads; any further change is a new episode.

**Declared residue (⚠️, unfixed by design — the budget's final read is spent; none is a ❌):**
- **N5 — non-canonical date strings.** The duplicate check compares raw date strings; the same day written `'2026-07-03 '`, `'2026-07-03T00:00:00'` or `'2026-7-03'` would count one close twice (and a malformed reset date can let a LATE kill fire across a reset). Pre-existing (identical on pre-fix code); needs date strings FRED's JSON never produces. Proposed: refuse the series unless every date is a 10-character ISO date (`date.fromisoformat`), ~3 lines + 1 test — **a NEW episode if LIQUID elects it**, not a correction to this one. If acceptance #8's summary sentence ("one distinct sub-260 close can never be counted twice") is read as absolute, this is the item that would have held; PROME reads #8 by its operative wording ("any observation date more than once") and records N5 here.
- **N1 — a refused series fails closed with only a watch.log trace** (`VINTAGE-FETCH-FAIL`); a feed that keeps duplicating leaves the kill leg blind until it stops. Acceptance #8 accepts this as written; optional boot-echo surfacing.
- **M9 — `fred_series` can return a value with no date and no error** (first parseable row lacking a `date` key): the SRF guard gives UNGRADEABLE, the Reserves row raises TypeError. Unreachable through `fetch.fred_fetch` (every row carries `o["date"]`, `fetch.py:363`). `fred_pairs` docstring at `boot.py:88` is stale. Optional.
- **M8 — the boot.py HY dashboard counts consecutive closes across a non-numeric middle row.** Outside this repair's acceptance ("the whole dashboard"); the watcher, the gate's actual grader, fails closed on `"ND"`.

The ledger below is the reviewer's final message, verbatim (HTML entities un-escaped).

---

No ❌. Both fixes clear read #1's two ❌ with no new hole opened. The one gap I found (N5, item 1 below) behaves identically in the pre-fix code and needs date strings FRED doesn't produce, so I've graded it ⚠️. Nothing in the repo was written; the repo shows no changes beyond those present at session start.

**Setup.** `S=<scratchpad>/liquid-review2`. Mirrors were extracted with `git archive`: `ws/` = HEAD · `prefix/` = the scripts at `d186bb16a` plus the HEAD test file · `old/` = `701511870`. `RUN = PYTHONDONTWRITEBYTECODE=1 MKTDATA_REEXEC=1 FORGE_CACHE_DIR=$S/cache unshare -rn $S/<ws|prefix>/.venv/bin/python3`. Read #1's harness was copied to `$S/harness/`, because `ce_watch.py` writes `runs/` beside its own parent folder and would write into `PROME/reports/` if run in place. My counterexamples are in `$S/harness2/` and all receipts are in `$S/receipts/` (08:51–08:57 EDT 2026-10-15). The mirror scripts are byte-identical to the working tree, and their SHA-256s match the before/after table in FIX.md.

## ⚠️ Warnings

**1. N5: the new duplicate check compares raw date strings, so the same day written differently still counts one close twice.**
- **Claim:** if one copy of a duplicated row has its date written as `'2026-07-03 '`, `'2026-07-03T00:00:00'` or `'2026-7-03'`, a single sub-260 close is counted twice and sets the permanent kill marker. The marker is stored as the malformed string, and `'2026-7-03'` produces an alert dated `UNKNOWN`. A related case, N5b/N5c, needs no duplicate at all. A resetting close dated `'2026-7-02'` sorts after every ISO date, so the next day's late-recovery path fires the kill across the reset (07-01 at 259, 07-02 at 270, 07-03 at 259 gives a LATE kill dated 07-03).
- **Artifact:** `hy_oas_watch.py:435-436` checks `o.get("date")` for duplicates; `:445` sorts the date strings. Nothing validates date format.
- **Command:** `$RUN $S/harness2/ce2_watch.py $S/{ws,prefix} N5_noncanonical_date_string` and `N5c_malformed_date_next_day`
- **Observed:** HEAD and pre-fix behave identically.
- **Why ⚠️, not ❌:** the fix didn't open this hole; the pre-fix code fails the same way. FRED's JSON always uses YYYY-MM-DD, and I know of no way to get mixed date formats from it. CE1's duplicate, by contrast, has a documented route: an ignored parameter. This matches how read #1 graded W4. It falls outside acceptance #8's operative wording ("any observation date more than once") but inside its summary sentence ("One distinct sub-260 close can never be counted twice"). If PROME reads that sentence as absolute, this is the item that holds.
- **Proposed change:** in `_first_published`, refuse the whole series unless every date is a 10-character string that `date.fromisoformat` accepts, and check duplicates on that. About 3 lines plus one test. It closes N5, N5b and N5c and keeps the existing fail-closed path.
- **Token:** VERIFIED for the behaviour, INFERRED for the likelihood.

**2. A refused series fails closed, but the only trace is a watch.log line.**
- **Claim (N1):** a duplicate on 06-29 suppresses a genuine 07-02/07-03 kill pair on run 1. Run 2, on a clean feed, raises a LATE alert with the original date 07-03, and a rerun is idempotent. Recovery works, but a feed that keeps duplicating leaves the kill leg blind indefinitely.
- **Artifact:** `boot.py:963` `watcher_echo` prints only zone, bps and observation date. On a refused run, the state's `sub260` is computed from the latest-revised quote while `count_basis` still says `"first-published-series"` (`hy_oas_watch.py:161`).
- **Command:** `$RUN $S/harness2/ce2_watch.py $S/ws N1_dup_elsewhere_suppresses_then_recovers`, plus a grep for `VINTAGE-FETCH-FAIL` over `*.py`, `*.md` and `*.sh`.
- **Observed:** run 1 records `sub260 1` with only VINTAGE-FETCH-FAIL logged. The grep found no other consumer: only watch.log, tests and docs.
- **Proposed change:** none required; acceptance #8 accepts this as written. Optionally, have the boot echo show the last VINTAGE-FETCH-FAIL.
- **Token:** VERIFIED for the behaviour; SEARCH-NOT-FOUND for any consumer.

**3. `fred_series` can now return a value with no date and no error.**
- **Claim (M9):** if the first parseable row has no `date` key, `fred_series` returns that value with date `None` and no error. The SRF guard handles it (M4 gives UNGRADEABLE). The Reserves row does not: `boot.py:547` (`d + " (as-of Wed)"`) raises TypeError and aborts `build_domestic`, where the pre-fix code rendered a misdated row. Separately, the `fred_pairs` docstring at `boot.py:88` still says `fred_series` "keeps only obs[0]["date"]", which is no longer true.
- **Command:** `$RUN $S/harness2/ce2_srf.py $S/{ws,prefix}`
- **Observed:** HEAD raises `TypeError`; pre-fix renders `2026-10-08 (as-of Wed)`. This can't happen through `fetch.fred_fetch`, which builds every row with `o["date"]` (`fetch.py:363`).
- **Proposed change:** treat a value with no date as an error, and fix the docstring. Optional.
- **Token:** VERIFIED for the behaviour, INFERRED that it is unreachable.

**4. M8: the boot.py HY dashboard counts consecutive closes across a non-numeric row in the middle.**
- **Claim:** `fred_series` still returns its list of recent values without dates. Rows 2.59 [10-13], ND [10-10], 2.59 [10-09] print "BEAR-AXIS KILL FIRED — HY <260 on 2 CONSECUTIVE closes" on both HEAD and pre-fix.
- **Artifact:** `boot.py:202-207` and `:244-246`.
- **Why it's only a warning:** the acceptance file puts "the whole dashboard" outside this repair. FRED's own missing-value marker (".") is dropped upstream as a day with no publication, which is correct; this case needs some other non-numeric code. The watcher, which is the gate's actual grader, fails closed on `"ND"`.
- **Proposed change:** none in scope.
- **Token:** VERIFIED for the behaviour, INFERRED for the likelihood.

## ✅ Passing results

**5. Process (task a).** The acceptance additions (#8 and #9) were committed before the code, and the fix changes no threshold, comparison operator, count rule or delivery-dedup key. `git merge-base --is-ancestor 88fece5a7 fd036576c` succeeds (08:37:27 then 08:39:46). In `git diff d186bb16a fd036576c`, the only lines with `=` are assignments. `sub_run`, `first_kill_date` and `decide` are untouched; the delivery key `f"{l[:24]}|{obs_date}"` is untouched; `add_srf_usage` is untouched; #8 and #9 describe the two properties as asked. VERIFIED.

**6. Tests (task b).** HEAD: 20/20 OK. Pre-fix with the HEAD test file: 18 pass, and exactly the two new tests FAIL, with read #1's symptoms (a kill packet is written; `('$60.00B','🔴','2026-10-13')`). The watcher selftest passes on both versions. `boot.py --selftest` passes on HEAD — this clears read #1's UNKNOWN on that selftest. Receipts `ws-tests.txt`, `prefix-tests.txt`, `ws-boot-selftest.txt`. VERIFIED.

**7. Read #1's cases re-run (task c).** CE1 (`dup_obs`) on HEAD: no `kill_met_on`, no packet, no SIGNALS row, VINTAGE-FETCH-FAIL logged; the no-duplicate control unchanged. CE6 on HEAD: `UNGRADEABLE ⚪`, T dated [10-10] and MBS dated [10-13]. Pre-fix reproduces both ❌. CE5: 0 of 50,001 splits graded above $50B. CE7 unchanged. Read #1's other six cases on HEAD are line-identical to read #1's receipts (`harness-r1.txt`, `harness-r1-others.txt`). VERIFIED.

**8. New counterexamples for the CE1 fix (task d; `ce2-watch.txt`).** N1 (duplicate elsewhere): refused, then recovered with the correct date · N2 (dates out of order but distinct): same as pre-fix · N3 (duplicate before the gate's start date): refused, as #8 requires · N4 (empty series, duplicated "." rows): refused · N6 (kill marker already set): kept; pre-fix double-counted here (sub260 = 4) · N7 (rows with no date key): refused · N8 (escalation alongside a duplicate): escalation unchanged. VERIFIED.

**9. New counterexamples for the CE6 fix (task d; `ce2-srf.txt`).** M1 (newest row parses, an older row doesn't): $60B graded 🔴 on 10-13, correct · M2b, M3 (legs land on different days, incl. one leg's only number 5 rows back): UNGRADEABLE · M2, M3b (both legs' newest rows non-numeric, older values on the same day): graded and stamped with that older date (10-10 or 10-06) — meets #4 and #9, no cross-date sum, no later-day stamp; no staleness flag, matching ordinary holiday handling · M5 (`nan`/`inf` newest): PARTIAL 🟠 · M7: the fix also corrects the HY-IG basis row (pre-fix graded 🟢 "[both 2026-10-13]" on 10-10/10-13 legs; HEAD UNGRADEABLE). VERIFIED.

**10. Ordinary inputs (`ce2-diff.txt`, `ce2-diff-sensitivity.txt`).** `_first_published`: 0 differences in 5,000 trials · `fred_series`: 0 in 5,000 · a non-numeric row anywhere except the newest: 0 in 4,131 · full multi-day `main()` runs: 0 in 400 scenarios (370 produced a packet) · the comparison detects real changes: 97 of 100 differ once a duplicate is injected. VERIFIED.

**11. Not run.** `baseline-probes.py` (writes into the repo); the author's live FRED check (network blocked). UNKNOWN.

**Ordinary inputs:** the fix changed nothing on well-formed inputs. Output changes only when a date repeats or the newest row doesn't parse.

VERDICT: RELEASE. Both ❌ are cleared and no new hole was opened. ⚠️ N5 (item 1) is the item that would hold the release if PROME reads #8's "never counted twice" as absolute; it is a roughly three-line date-validation fix.
