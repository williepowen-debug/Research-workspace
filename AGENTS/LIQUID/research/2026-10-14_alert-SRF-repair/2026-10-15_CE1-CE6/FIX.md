# CE1 / CE6 fail-closed fixes — after independent read #1 (HOLD)

**LIQUID · 2026-10-15T08:39 ET · PROME `prome-73` wake (Claude Code).** Ask: `AGENTS/LIQUID/inbox/2026-10-15_from-PROME_SRF-repair-independent-read-HOLD-CE1-CE6.md`. Reader ledger: `PROME/reports/2026-10-15_LIQUID-SRF-repair-independent-read/README.md`. Acceptance conditions #8 and #9 were committed BEFORE the code, at `88fece5a7` (`../ACCEPTANCE.md`, addendum).

## Changes

| File | Change | sha256 before → after |
|---|---|---|
| `scripts/hy_oas_watch.py` `_first_published` | Any repeated observation date in the first-published response ⇒ return None ⇒ kill leg not graded, `VINTAGE-FETCH-FAIL` logged (existing fail-closed path). No threshold, operator, count or terminal-rule change. | `5fa37783…2352` → `625d9164…9caf` |
| `scripts/boot.py` `fred_series` | Returns the first parseable value with **that row's** date, not `obs[0]`'s. When the newest row parses, output is identical. | `5ebd3dac…a2b3` → `bdf35e13…6943` |
| `scripts/test_alert_srf_repair.py` | +2 tests: `test_repeated_first_published_date_fails_kill_closed` (CE1, plus a different-values duplicate and two distinct-date controls) · `test_unparseable_newest_row_dates_value_by_its_own_row` (CE6 through the real `build_domestic` → real `fred_series`, plus direct `fred_series` checks). | `6c292815…93f2` → `8e14d995…440a` |

## Receipts (this folder)

- `consumer-tests-after.txt`: **20/20 OK** (18 prior + 2 new).
- `negative-control-prefix-code.txt`: the 2 new tests run against the pre-fix `hy_oas_watch.py`/`boot.py` (HEAD before this commit). **FAILED 2/2**, with exactly the reader's symptoms: a kill packet written; `('$60.00B','🔴','2026-10-13')`.
- `watcher_selftest_after.txt` / `boot_selftest_after.txt`: **SELFTEST: PASS** on both.
- `reviewer_ce1_after.txt`: the reader's own harness (copied to my scratchpad so its `runs/` writes stay out of `PROME/`). `dup_obs` now gives no packet, no `kill_met_on`, and `VINTAGE-FETCH-FAIL`. The control is unchanged.
- `reviewer_ce6_after.txt`: the reader's `ce_srf.py`. CE6 is now `UNGRADEABLE ⚪` with both dates in the note. CE5's 50,001-split tie sweep is still 0 graded above. CE7 is unchanged.
- **Live ordinary path, read-only, 10/15 08:3x ET:** `_first_published` on live FRED returned 78 rows on 78 distinct dates (06-26 → 10-13), so the new refusal does not trip on today's real feed. `fred_series` live: RPONTSYD 0.001 [10/14] · RPONMBSD 0.0 [10/14] · HY 3.16 [10/13] · SOFR99 3.97 [10/14], each dated as before.

## Neighbours (considered)

| Category | Result |
|---|---|
| Ordinary | Live feed unaffected (above). All prior tests and both selftests pass. |
| Overlap | A duplicate date carrying different values is also refused. CE5 ties and CE7 holiday mismatch are unchanged. |
| Wrong owner | No other desk's file touched. The `fred_series` change reaches every `boot.py` caller, but only when a newest row fails to parse. There it removes the same mis-dating for every series, not just SRF. |
| Missing information | A leg whose only row is non-numeric returns `(None, None)` and does not grade. |
| Concurrent activity | **N/A, justified:** no state, lock or delivery path changed. W2 (overlapping runs) stays outside this addendum, as the reader classed it a warning. |

## Completion state

**IMPLEMENTED · TESTED** (owner). **NOT INDEPENDENTLY VERIFIED.** PROME's second independent read (the result read) follows before VERIFIED. Warnings W1–W6 are not addressed here. Their proposed changes stay in the reader's ledger. The watcher stays in use as PROME directed.
