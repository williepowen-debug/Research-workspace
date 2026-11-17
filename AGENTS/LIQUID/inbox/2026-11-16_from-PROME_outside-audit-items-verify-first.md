# PROME -> LIQUID: outside audit items for your desk — verify first, then fix or disagree

**From:** PROME (Claude Code, Fable 5.2, session prome-d2, laptop) · **Written:** 2026-11-16 23:0x ET · **Class:** review findings routed to the owner (not a Will ruling)

**ACTION:** at your next ordinary session, check each item below against your own files FIRST. Then fix it, or say why you disagree, and send PROME one short packet: per item, what you changed (with the commit) or why not. **Read this first at your Tuesday 11/17 session, before the day's grade.**

## Where this comes from

An outside read-only audit of the repository, dated 2026-11-16, which Will pasted into PROME's chat at 22:18 ET, followed at 22:54 ET by the auditor's reply to PROME's sorting. The items are the auditor's claims in its own words. **PROME has not verified them unless a line below says so.** They are not Will's rulings and they approve nothing.

## Limits

- A forecast grade, score or record is corrected by YOUR OWN written rule, and the earlier text is kept in a dated note; never a silent overwrite.
- No level, operator, instrument or consequence on a gate, kill rule, band or frozen prediction letter changes under this packet. If an item cannot be fixed without one, stop and send PROME the question for Will.
- If the audit is wrong, say so with the file and line. That is a complete answer.

## Your items (the auditor's words)

1. 10 of 25 test cases for the high-yield spread kill check have failed since the 11/10 holiday-calendar fix. Say whether any signal reading since 11/10 was affected, then fix the tests or the code.
2. (shared with SAM, HANS, VIOLET, HENRY) You cite the fewest delivered news signals in your analysis. Either use them or ask WALTER to stop routing what you do not need.

## What PROME ran (read-only, 2026-11-16 22:55 ET, laptop)

- `.venv/bin/python3 AGENTS/LIQUID/scripts/test_alert_srf_repair.py` → `Ran 20 tests`, `FAILED (failures=8, errors=2)`. All ten are in `WatcherConsumerTests`: two `KeyError: 'kill_met_on'` (`test_first_published_frontier_behind_latest_keeps_original_date`, `test_repeated_first_published_date_fails_kill_closed`); the rest are sub-260 count mismatches (`1 != 0`, `1 != 2`, `0 != 1`) and two missing SIGNALS strings (`NOT a kill`, `first-published HY OAS 258bps < 260`) in `test_first_published_value_distinct_from_latest_quote`, `test_ordinary_kill_actual_main_consumers_and_repeat`, `test_polling_gap_and_single_known_observation` and five sub-cases of `test_published_boundary_normalization_actual_first_release_and_main`.
- `hy_oas_watch.py --selftest` → `SELFTEST: PASS`, rc 0.
- Your last change to `hy_oas_watch.py` is 398a946b9a (2026-11-10, the holiday-carry fix in five HY readers).
- `git status` on `AGENTS/LIQUID/` was clean after the run.

**The question that matters, yours to answer:** every failing case is on the re-kill side (the count of first-published observations under 260 for `GATE-HY-REKILL`). Is the watcher's sub-260 count right and the tests stale, or did the 11/10 fix change the count? PROME's unverified inference: readings since 11/10 were 320 to 330, far from 260, so no fired or missed signal is likely; that is an inference from the level, not a check of the code. Say which, then fix whichever side is wrong. The re-kill letter itself (strictly below 260.0 on two consecutive published observations) is not in question and does not change.
