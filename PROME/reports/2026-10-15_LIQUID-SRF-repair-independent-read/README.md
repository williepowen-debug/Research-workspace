# LIQUID alert/SRF repair — independent read #1 (WQ-229) · VERDICT: HOLD

**Record written 2026-10-15 08:36 ET by PROME prome-73.**

**Reader:** PROME-spawned read-only reviewer (Claude Code Agent tool, general-purpose, model Opus), launched 08:23 ET 2026-10-15 by PROME prome-73 (ORCH_LOG `PROME-READER-LIQUID-SRF` touch `2-SPAWN-READER-WQ229`; the 10/14 reader died in the 03:08 ET crash with nothing delivered — episode reads 0 → 1). **Subject:** commit `d186bb16a` to `AGENTS/LIQUID/scripts/hy_oas_watch.py` and `AGENTS/LIQUID/scripts/boot.py`; acceptance file committed before the code at `701511870`; author's report `AGENTS/LIQUID/research/2026-10-14_alert-SRF-repair/REPORT.md`; author's tests `scripts/test_alert_srf_repair.py`. **Method:** mirror workspace under the PROME scratchpad (`ws/` = current code, `old/` = pre-repair code at 701511870; both byte-identical to the repo at read time), network blocked (`unshare -rn`), fetch mocked; nothing written in the repository. The author's 18 tests and the watcher selftest pass in the mirror (VERIFIED). Not run: `boot.py --selftest`, `baseline-probes.py` (writes into the repo) — UNKNOWN. Receipts: `ce-receipts.txt` (08:32:56–08:33:39 EDT). Harness: `harness/ce_watch.py` · `ce_srf.py` · `ce_absent.py` (run against a mirror of the two scripts, never the live files). The `ws/`/`old/` mirrors are not preserved — rebuild from git at `d186bb16a` / `701511870`.

**Disposition (PROME, WQ-229):** the repair stands IMPLEMENTED · TESTED (author) · READ ONCE (this ledger) · **NOT INDEPENDENTLY VERIFIED — HOLD.** Both ❌ are older than the repair and need bad upstream data; the repaired code fails no case the old code passed and does better on every changed path. Clearance = the two fail-closed fixes + two tests named below, then a second read (the result read) inside the episode budget. The ledger below is the reviewer's final message, verbatim (HTML entities un-escaped).

---

**VERDICT: HOLD.** Two of my own counterexamples fail properties the acceptance file names (CE6 and CE1 below). Both faults are older than the repair: the code from before it fails them the same way, and the repair didn't make them worse. Both also need bad upstream data to happen. Everything the repair actually changed passed every case I ran, and in each case it did better than the old code.

I reviewed commit `d186bb16a`. No later commit touches either script, and my mirror copies are byte-identical to the repo files. All runs used a mirror workspace under `/tmp/claude-1000/-home-willi-Research-workspace-PROME/16d245b5-0cb3-4174-b43d-e76c4903c384/scratchpad/liquid-review/`, with the network blocked (`unshare -rn`) and fetch mocked. `ws/` holds the current code; `old/` holds the pre-repair code archived at 701511870. I wrote nothing in the repo. The author's 18 tests and the watcher selftest pass in the mirror (VERIFIED). I did not run `boot.py --selftest` or `baseline-probes.py`, because the latter writes into the repo (UNKNOWN). All receipts are in `.../liquid-review/ce-receipts.log`, timed 08:32:56–08:33:39 EDT 2026-10-15.

**How to reproduce.** Set `S=<the scratch root>`, then:
- Watcher cases: `cd $S && MKTDATA_REEXEC=1 FORGE_CACHE_DIR=$S/cache unshare -rn $S/ws/.venv/bin/python3 $S/harness/ce_watch.py $S/{ws|old} <case>`
- SRF cases: the same command with `ce_srf.py $S/{ws|old}`
- Missing-SIGNALS case: `ce_absent.py $S/ws`

## Acceptance conditions, restated

| # | What it requires | Met? | Where | Token |
|---|---|---|---|---|
| 1 | Every consumer (packet, SIGNALS, alert log) gets every fresh event in full: no 240-character cut, one dated row per event, each with its own target, priority and guard. Kill and widening notes intact. Routing and file-only delivery unchanged. | Yes | `hy_oas_watch.py:335-350, 406-410, 492-493`; the old `[:240]` is gone; the diff adds no git or network calls | VERIFIED |
| 2 | A recovered event keeps its original date, kept apart from the current quote. An unparseable date shows as UNKNOWN, never today. | Yes, but the wording is wrong in one edge case (W3) | `:322-332, 360-370, 348-349` | VERIFIED |
| 3 | No change to thresholds, operators, counts or the one-time kill rule. Existing dedup keys still honoured, no duplicates on reruns, polling gaps can't skip a reset, a single known observation can't fire. | No under CE1 (duplicated date); also W2 (overlapping runs) | `:69-98, 393, 415` | VERIFIED |
| 4 | The SRF total is graded only when both legs have known, matching dates. A missing date, missing value or failed leg means no grade; a sum across dates is never stamped with the later day. Strict >$50B kept. | No under CE6 | `boot.py:151-171`; the gap sits in the unchanged `fred_series`, `boot.py:76` | VERIFIED |
| 5 | HY spread readings (latest and first-published) are rounded to whole basis points (bp) before comparing: 259 qualifies, 260/261 don't, float noise can't move the edge. | Yes, for FRED's 2-decimal data | `:436, 464` | VERIFIED |
| 6 | STATUS, MEMORY and the verdict-prep note keep required LIQ-07 inputs separate from optional context; missing context never blocks a verdict. | Yes | diff `701511870..d186bb16a` of STATUS, MEMORY and `credit-funding-refresh/REPORT.md` | VERIFIED |
| 7 | Protected files untouched; tests use only temporary paths. | Yes | the commit's file list has no gate, prediction, letter, calendar, FORGE config or swap-tool file; tests patch every destination | VERIFIED |

## Assertion ledger

**❌ CE6 — SRF grades a cross-date sum and stamps it with the later day (acceptance #4)**
- **Artifact:** `boot.py:76`, where `fred_series` returns `vals[0]` (the first value that parses) alongside `obs[0]["date"]` (the newest row's date). The new guard at `boot.py:151-171` trusts that pairing.
- **Command:** `ce_srf.py` on both `ws` and `old`. Treasury leg rows: `[{10-13,"ND"},{10-10,"30.000"}]`; MBS leg: `[{10-13,"30.000"}]`.
- **Observed:** both old and new code print `('$60.00B','🔴','2026-10-13','ABOVE $50B — escalate…')`. A 10-10 value is summed with a 10-13 value and dated 10-13.
- **Proposed change:** give each SRF leg the date of the row its value actually came from (for example `fred_pairs(...)[0]`), or fail the leg when the newest row doesn't parse. Add a test for a non-numeric newest row.
- **Caveat:** older than the repair. FRED marks missing values as ".", which `fetch.py` drops, so this needs some other non-numeric value to arrive (INFERRED: low likelihood).
- **Token:** VERIFIED.

**❌ CE1 — a duplicated first-published date fires the one-time kill on a single close (acceptance #3: "Single known kill observation cannot fire")**
- **Artifact:** `hy_oas_watch.py:436-437` (no dedup by date), `:84-98` and `:69-81` (both count rows, not distinct dates).
- **Command:** case `dup_obs` on `ws` and `old`. First-published rows: 07-01 2.72, 07-02 2.70, 07-03 2.59, 07-03 2.59.
- **Observed:** both versions give `sub260: 2`, set `kill_met_on: '2026-07-03'` (the permanent marker only a human can clear) and send the red ALL alert. The control case without the duplicate gives `sub260: 1` and no alert.
- **Proposed change:** in `_first_published`, return None when any observation date repeats. The kill check then fails closed and logs VINTAGE-FETCH-FAIL. This adds an input check without changing the threshold, operator or count rule. Add a test.
- **Caveat:** older than the repair. It needs the FRED vintage endpoint to return more than one row per date, i.e. to ignore `output_type=4`. KILL_MEMO §6 records another FRED path silently ignoring a parameter, so this isn't impossible (INFERRED: low likelihood, high consequence).
- **Token:** VERIFIED.

**⚠️ W1 — a write failure mid-delivery loses an event from SIGNALS for good (CE2; the author disclosed this)**
- **Artifact:** `:405-416`.
- **Command:** case `dest_fail`, where the second SIGNALS row raises `OSError` 28.
- **Observed:** the escalation row was written, the 07-02 kill row was not, and both were marked delivered. Reruns the same day and the next day write nothing. watch.log shows `DELIVER-FAIL SIGNALS` without saying that 1 of 2 rows landed. The packet did carry both events.
- **Missing-SIGNALS case** (`ce_absent.py`): logs `DELIVER-FAIL SIGNALS — destination absent`, the key is still recorded, and 0 rows appear after the file is restored. This matches the author's disclosure.
- **Proposed change:** none within this repair's scope. Optionally log the row count written before a failure.
- **Token:** VERIFIED.

**⚠️ W2 — two overlapping runs duplicate every SIGNALS row**
- **Artifact:** `:392-416`, `:503`; there is no lock.
- **Command:** case `concurrent`, where the second run reads the old state before the first run writes its own.
- **Observed:** 4 SIGNALS rows with the new code, 2 with the old. The race is older than the repair; it just scales with events per fire now.
- **Proposed change:** none required. A lock file if a manual run and the 13:00 timer can overlap.
- **Token:** VERIFIED.

**⚠️ W3 — when the first-published series runs ahead of the latest quote, wording and labels go wrong (dates stay correct)**
- **Artifact:** `:486`, `:131-136`, `:152`.
- **Case `fp_ahead`:** a fresh 07-03 kill next to a 07-02 quote is called "recovered historical", with the text "missed run… may be a DUPLICATE". That wording could lead a reader to discount a new event.
- **Case `fp_ahead_ordinary`:** the alert reads "first-published HY OAS 257bps … on 3 consecutive closes (as-of 2026-07-03)", but 257 is the 07-06 value.
- **Precondition:** the FRED cache lag (5 minutes) or the two FRED endpoints being out of sync (INFERRED: rare).
- **Proposed change:** let the late-kill text name "first-publication frontier differs from latest quote" as a possible cause, and print the date of `recent[0]`.
- **Token:** VERIFIED for the behaviour, INFERRED for the likelihood.

**⚠️ W4 — rounding to whole bp can drop a sub-bp reading out of the kill range**
- **Artifact:** `:436`.
- **Command:** case `halfbp`.
- **Observed:** 2.595, 2.596 and 2.599 give `sub260=0` with the new code and 2 with the old.
- **Why it's only a warning:** KILL_MEMO §3 says FRED publishes to 0.01%, so these values can't occur today. A finer feed would be rounded silently rather than flagged.
- **Proposed change:** optionally flag (fail closed) when a value isn't within about 1e-6 of a whole bp, instead of rounding it.
- **Token:** VERIFIED for the behaviour, INFERRED for the risk.

**⚠️ W5 — SRF display and neighbouring-letter notes**
- **Command:** `ce_srf.py`, case CE5b.
- **Observed:** a total of $50.001B prints as `$50.00B 🔴 ABOVE $50B`. The grade is correct but the 2-decimal display hides why. This is older than the repair.
- **Also (INFERRED):** at exactly $50.000B this row shows green, while LIQ-07's letter uses ≥$50B on a different series (RPONTTLD). The acceptance deliberately keeps that difference.
- **Also (VERIFIED):** watcher rows are appended at the end of SIGNALS.md, under its `## Archived` heading. The 6th cell, which carries "current quote observation", has no matching column in the 5-column Active table. Also older than the repair.
- **Proposed change:** none in scope.

**⚠️ W6 — the author's 39-observation replay can't see the change at `:486`**
- **Artifact:** `baseline-probes.py:58-61` drives both old and new `decide()` with the new `!= d` rule, so it doesn't exercise the main-loop change.
- **Command:** read only. Not re-run because the script writes into the repo.
- **Proposed change:** none. It's a coverage note.
- **Token:** INFERRED.

**✅ Passing results**
- **CE5:** all 50,001 three-decimal splits of exactly $50.000B through the real `build_domestic` produced 0 grades above 50 (VERIFIED).
- **CE7:** a holiday on one leg (Treasury 10-10, MBS 10-13) gives UNGRADEABLE ⚪ with both components dated. The old code gave `$60.00B 🔴` dated 10-13. The repair works (VERIFIED).
- **Content checks:** in my runs every kill row carries "If the arbiter is dark" and "do NOT retire the thesis", every escalation row carries "strict `>280` SUSTAINED" and "Do not size off this packet", and foreign rows survive (VERIFIED).
- **Bad values:** nan/inf parse failures fail closed. A nan in the first-published series now becomes VINTAGE-FETCH-FAIL; the old code silently treated it as a reset (VERIFIED by reading `:436-440, 466`).

VERDICT: HOLD — CE6 (acceptance #4: unparseable newest SRF row makes a cross-date sum graded and dated to the later day) and CE1 (acceptance #3: a duplicated first-published date fires the one-time kill on one close). Both are older than the repair and the repaired code fails no case the old code passed; small fail-closed fixes plus two tests would clear them.
