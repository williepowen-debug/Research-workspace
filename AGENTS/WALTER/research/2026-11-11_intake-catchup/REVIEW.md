VERDICT: FAIL

Independent review, 2026-11-11, fresh context, read-only. The core catch-up is correct and first-deploy-safe. FAIL because acceptance case 7 does not hold as written, and because `--mark` can permanently skip a batch the scan never showed, which a catch-up repair is meant to stop. Each fix is small.

Evidence base: `git diff tools/intake_scan.py` is byte-identical to `intake_scan.diff`. 41 tests pass across test_intake_catchup, test_boot_repairs, test_cruise_capital_review and test_gpu_finance_review (.venv python). A read-only scan against the live lane (HEAD 5994815, saved = data/2026-11-10/news.json, no pointer stored) gives news_batches = [data/2026-11-10/news.json], 0 NEW, 14 suppressed and no non-OK health line, so nothing re-fires on deploy. The edge cases below were probed in a temporary lane through mock.patch.

## Findings (most severe first)

1. **The scan and `--mark` can run on different lane states, so `--mark` can absorb batches nobody saw. (intake_scan.py:636-638, 645-657)** `--mark` is a separate run. It recomputes `newest` and `recs` from liveness at mark time and stores `last_marked_batch = newest`. Scenario: the scan shows the range up to D3, WALTER routes, then something pulls the lane (a second 7e(a) pull, another session, lane tooling). `--mark` now emits D4 as well, writes every D4 key into `seen` and moves the pointer to D4. D4's WATCH_HIT/DEVELOPMENT items and its NEW_ALERT count are never displayed. The old code lost the newest batch the same way, but the pointer now makes the loss permanent: D4 is outside every later range. **Fix:** the report prints the newest batch it showed, `--mark --through <that path>` must match the current `saved` or REFUSE, and the pointer is set to that value. A cheaper alternative: `--mark` refuses when `saved` differs from the batch named in the last report, using a stamp kept in the scan output.

2. **Case 7 does not hold for a pointer that parses but is missing from the lane. (intake_scan.py:181-193 vs 196-202; test :91-96)** `news_batches` checks only the regex, never whether the file exists. With pointer `data/2026-10-01/news.json` absent, it returns every batch after 10-01. At the same time `pointer_health` prints MED "news catch-up OFF, newest batch only". The behaviour is the safe direction, but the health line is false. The test hides this: for the missing pointer it asserts only `pointer_health`, and it checks the `news_batches` fallback only for 'garbage'. **Fix:** pick one behaviour and make the code, the message and ACCEPTANCE agree. Recommended: keep date-based catch-up (it survives lane pruning) and reword the MED line to "pointer batch missing, catching up by date from <day>". Then amend case 7 and add the missing assertion.

3. **`--mark` moves the pointer past an unreadable batch. (intake_scan.py:298-305, 655-656)** An unreadable older batch emits one INFO `news:UNREADABLE:<path>` record. `--mark` then puts that key into `seen` and moves the pointer beyond the batch. When the file is repaired it is never scanned again, so its items are lost after a single ROUTINE line. **Fix:** set the stored pointer to the batch just before the first unreadable batch in the range (or leave it unchanged), so the unreadable batch is retried until it reads.

4. **A pointer later than `saved` is silent and causes re-fires. (intake_scan.py:184-193, 196-203, 655-656)** Pointer D5 with saved D3 can happen on a lane clone that is behind, for example a failed 7e(a) pull, or the other machine after `intake_seen.json` syncs through git. In that case `lo > hi`, the function returns [saved] and no health line prints when D5 exists. `--mark` then moves the pointer back to D3 and reconciles the D4/D5 keys out of `seen`. After the lane catches up, D4 and D5 re-fire as onsets, which means duplicate dispatches. **Fix:** print MED when the pointer day is later than the saved day, and never let `--mark` move the pointer backward.

5. **A missing `saved` drops NEW_ALERT and NEW_WATCH counts silently. (intake_scan.py:178-179, 292)** The old code emitted `news:NEW_ALERT:` from `by_class` even when `saved` was absent. The new code returns [] and emits nothing, with no health line. This is rare, but it is a fail-silent regression. **Fix:** when `saved` is missing and `by_class` has counts, emit the old record or a MED line.

6. **Silent skips in batch enumeration. (intake_scan.py:186-192)** An `OSError` on `iterdir` is swallowed, so catch-up turns off with no health line. A day directory without news.json is skipped with no notice. Directory names are not checked against the date pattern: a `2026-11-05_rerun` directory would fall inside the range (pointer 11-05, saved 11-06) and produce its own keys. Every lane directory observed is a plain date, so this is low. **Fix:** filter directory names with the date regex and add a MED line on `OSError`.

7. **The tests prove less than they claim.** test_3 (:65-69) uses pointer D2 with only D3 newer, so the catch-up range is empty. The same assertions pass on the old newest-only semantics, which means the test cannot tell catch-up apart from no catch-up. test_2 never asserts that D1 is absent. As a result, strict exclusion of the marked batch while catch-up is active is not tested in a way that tells old from new behaviour. **Fix:** use four days with pointer D2, assert D1 and D2 are absent and D3 and D4 are present. test_2 and test_5 do tell old from new behaviour: the old code never reads D2 and never writes the pointer.

8. **Minor, behaviour notes.** (a) The saved batch is now always read, where the old code read it only when `by_class` showed WATCH_HIT or DEVELOPMENT (:298-299). If `by_class` and the file disagree, per-item records can now appear that did not before. This is better, but it is an unannounced change. On the live 11-10 batch, `by_class` matches the file counts. (b) The pre-existing same-day-rewrite blind spot is unchanged: the per-batch key is the path, so a rewritten day file with new NEW_ALERT items stays suppressed. Per-item keys still fire. The lane git log shows each of the last 10 news.json files committed once. (c) A non-string pointer raises TypeError at :181/:200. That failure is loud, which is acceptable.

**Key compatibility: holds.** For `saved`, the per-batch key `news:{cls}:{batch}` (:314) is byte-identical to the old `news:{cls}:{saved}`. The per-item `news:WATCH_HIT|DEVELOPMENT:<sha1(title)[:12]>` is unchanged, and `hashlib` was already imported at module level (:40). Confirmed live: 0 re-fires.

**Outside the news block: unchanged.** The FRED, EIA, CFTC, EDGAR, Treasury, cruise and GPU code is untouched. `--json` gains one additive field, `news_batches`, and no in-repo consumer of the `--json` keys was found. Health gains `pointer_health` lines only.

## Acceptance cases

| # | Case | Result |
|---|------|--------|
| 1 | Install, no replay | HOLDS (test_1; confirmed live) |
| 2 | Catch-up D2+D3, existing key formats | HOLDS (test_2; distinguishes old from new) |
| 3 | Marked batch and older not re-read | HOLDS by code (:189 strict `lo < d`), but test_3 cannot tell old from new behaviour |
| 4 | Pointer at newest | HOLDS (test_4) |
| 5 | --mark advances, reconcile unchanged | HOLDS as specified; see findings 1, 3 and 4 for loss and re-fire paths |
| 6 | Unreadable older batch fails loud | HOLDS for the scan (test_6); the mark then skips the batch for good (finding 3) |
| 7 | Bad pointer: fallback plus MED | DOES NOT HOLD for a parseable pointer missing from the lane (finding 2); holds for an unparseable one |
| 8 | Unchanged elsewhere, existing suites pass | HOLDS (41/41; diff confined to the news block and main) |
| 9 | Visible range in the report | HOLDS (test_9; :677-679) |

## Follow-up read (fix diff)

FOLLOW-UP VERDICT: PASS WITH NOTES

Scope of this read: `intake_scan_fixes.diff` (from the reviewed version to now), ACCEPTANCE cases 10–14 and the updated `test_intake_catchup.py`. The catch-up suite passes 13/13 and the other three suites pass 33/33 (.venv python). Every counterexample below was run in a temporary lane through mock.patch. Nothing was run against the real registry.

| F | Status | Evidence |
|---|---|---|
| F1 scan/mark lane drift | PARTLY | Refusal at intake_scan.py:692 works. It also works with no stored pointer: the refusal returns 2 and `intake_seen.json` is untouched. Two gaps remain. A bare `--mark` only prints a WARNING. The charter step 7e(e) in AGENTS/WALTER/CLAUDE.md still says `intake_scan.py --mark` with no `--through`, so the protected path is not the documented one; that file belongs to its owner and the change needs a Will-gated edit. Second, a same-day rewrite of the newest file between scan and mark passes `--through`, because the path is unchanged. |
| F2 missing pointer | FIXED | news_batches checks that the pointer file exists and falls back to the newest batch (:196-203), consistent with the MED line; test_7 now asserts this. |
| F3 unreadable batch | PARTLY | An unreadable FIRST batch in range holds the pointer at the stored value: D2 is bad, the pointer stays at D1, and D3 is still scanned on every run. **Defect:** mark_pointer (:226-241) tests readability with `json.loads` alone, while the scan also calls `.get("items")` (:353-355). A valid-JSON non-object file such as `[]` or `null` makes the scan emit `news:UNREADABLE:data/2026-11-02/news.json`, but mark_pointer still moves to D3, so that batch is skipped for good. **Fix:** use the same test in both places, `isinstance(obj, dict)` (ideally one shared reader). Note: a batch that stays unreadable pins the pointer. After the first mark its UNREADABLE key sits only in [suppressed] and no health line prints, so the stall is visible only in the mark's "held before" line. Suggest a MED line whenever the pointer is held behind an unreadable batch. |
| F4 pointer ahead | PARTLY | Clone-behind case is FIXED: MED at :212 and the pointer never moves back, so D4 and D5 do not re-fire. **Lane rollback** (upstream rewrites history, so the pointer's D5 file is gone and saved is D3) is not covered. (a) Only the "missing" MED prints, and it says "the next --mark resets it". That is false: never-backward keeps D5, as probed. (b) If the lane then regains D4 and D5 in one pull, news_batches gives [D5], because the pointer exists again and lo >= hi. D4 is never scanned, and no health line prints at that point. This is rare. **Fix:** when the pointer file is missing, `--mark` should move the pointer to the newest readable batch (the never-backward rule applies only to a pointer that exists), or the MED text should be made true. |
| F5 missing saved | FIXED | :329-336 restores the count records. The key is `news:{cls}:`, the same as the old code whenever `saved` is absent or an empty string. |
| F6 enumeration | FIXED for the named items | Directory names are checked against the date pattern, an `OSError` on data/ gives a MED line, and day directories without news.json inside the range give a LOW line. **Remaining silent path:** a `saved` path that does not match the pattern while the pointer is valid. Example: pointer D1, saved `data/2026-11-03/news2.json`. No MED prints, and the report says "catch-up from last_marked_batch D1" but scanned only `saved`, so D2 is skipped without notice. `--mark` then stores the non-matching pointer, and the MED appears only on the next run, after D2 is already out of range. **Fix:** print MED when `saved` does not match the pattern, and have `--mark` refuse to store a non-matching pointer. |
| F7 test strength | FIXED | test_3 now asserts D3 is present, which the old newest-only code could not produce. test_2 asserts D1 is absent. New tests cover F1, F3, F4, F5 and F6. None of them covers the non-object batch, the rollback, or a non-matching `saved`. |

Minor: with no stored pointer and an unreadable newest batch, `--mark` writes no pointer and prints nothing about it. Catch-up then stays off until a mark lands on a readable batch. `--through` without `--mark` is ignored silently, which is harmless.

## Final check

FINAL: PASS

Scope of this read: `intake_scan_fixes2.diff` only. The four suites pass 47/47 (.venv python). Each point below was probed in a temporary lane.
- **Note 1, shared reader: FIXED.** `read_batch_items` now serves both the scan and `--mark`. The files `[]` and `{"items":null}` are now unreadable to both, and the pointer holds at D1. One deviation from the description: `{"x":1}`, an object with no `items` key, reads as an empty batch in both places. That matches the pre-repair `.get("items", [])`. The two paths agree, so it causes no loss.
- **Note 2, vanished pointer: FIXED.** Catch-up runs by date and prints a LOW line. It cannot replay anything already marked: the range is strictly later than the pointer's day (`lo < d`), and the never-backward rule means no batch after the stored pointer was ever marked. The rollback MED line now states the re-publish blind spot accurately.
- **Note 3, non-matching newest path: FIXED.** It now gets a MED line saying catch-up is OFF, so the skip is reported instead of silent.
- **Still open, with Will:** charter step 7e(e) still documents a bare `--mark`.
