---
name: finding_partial_record_written_as_final_never_heals
description: "An append-that-is-idempotent-by-key CANNOT self-heal: write one partial record and it is permanent, because every later run sees the key present and skips. Pair that with a completeness guard comparing a VENDOR timestamp against a LOCAL now() and you silently store truncated rows forever — SAM's 7/30 yen spike stored as a 0.33y day against a true 5.74y range."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 90a11e3b-9660-421d-b848-fa0cb8c1f009
  modified: 2026-08-02T21:43:08.481Z
---

**Two ordinary, individually-defensible choices compose into permanent silent data corruption (SAM, 2026-08-02):**

1. **The completeness guard compared clocks from different zones.** `usdjpy.py` appended only "fully closed" daily bars, skipping `date == datetime.now()`. But yfinance labels `USDJPY=X` bars in **Europe/London** while `now()` is **local (Eastern)**. Any run after ~19:00 ET therefore saw the *next* London-day's few-hours-old **partial** bar as "not today" and wrote it as final.
2. **The append was idempotent by date** — the standard, correct-looking pattern for a rolling ledger. So the truncated row **could never be corrected**: every later run saw the key present and skipped it.

**Result: 10 of the last 60 sessions stored truncated, every one under-stating the daily range.** Worst case: **2026-07-30 stored as a 0.33-yen range against a true 5.74-yen range** — the largest yen move since Dec-2023 and a suspected ~¥8.45T MOF intervention. The intraday-range alert reading that column (an intervention detector with a 4.0y CRIT line, calibrated against a *confirmed* ¥5.48T op that ranged 5.15y) printed **"normal daily range"** on the biggest event of the cycle. Post-fix it fires `INTERVENTION-GRADE 5.74y`.

**Why it matters — the composition is the finding, not either half.** Each piece is individually fine and reviews clean. Idempotent-append is *correct* for immutable closed records; it becomes a corruption ratchet the moment anything upstream can write a record that isn't actually final. And the failure is invisible from every direction that normally catches things:

- The values are **plausible** — a 0.33y range is a real, boring day. Nothing is null, malformed, or out of bounds ([[finding_plausible_stale_value_evades_review]], [[finding_silent_blank_evades_review]]).
- The detector logic was **never wrong** — so testing the guard finds nothing. This is a defect in the *ingestion*, one layer below where [[finding_test_the_guard_not_just_the_guarded]] tells you to look.
- Fresh data keeps arriving, so **staleness checks pass** — the file is current, just wrong ([[finding_freshness_check_cannot_catch_a_fresh_lie]]).
- The corruption is **concentrated on high-volatility days by construction**: partial bars truncate the *range*, so the rows most likely to be wrong are exactly the event days the instrument exists to catch. Sampling a few rows shows agreement.

**How to apply:**

1. **Resolve both sides of any "is this record complete?" comparison in the same timezone.** Derive "now" from the data's own index (`datetime.now(df.index.tz)`), never from bare `datetime.now()`. Prefer `>= today` over `== today` so a clock skew drops a row rather than storing a partial one.
2. **Ask of every idempotent-by-key writer: what happens if a bad row lands?** If the answer is "it stays forever," the ledger needs either a re-verify pass (periodically re-fetch a trailing window and overwrite, don't skip) or a completeness assertion at write time. **Idempotency is a guarantee about writes, not about correctness.**
3. **Audit by DISPERSION, not by spot-check.** This was invisible row-by-row and obvious the instant a whole column was diffed against a fresh pull. For any derived series, periodically re-pull the window and compare the *distribution* — the truncation showed up as "TSV range ≤ fresh range in 10 of 10 divergent rows," a one-sided error no eyeball catches.
4. **When two instruments on the same quantity disagree, chase it — that disagreement is the only free alarm you get.** The whole find started from a boot report showing 157.22 in one module and 160.71 in another. The cheap move is to trust the one that matches your prior; the disagreement itself was the signal.
5. **Vendor daily FX bars deserve specific suspicion:** in the same series Yahoo's daily `Close` ≈ `Open` on every row (a bar-boundary snapshot, not a session close). Use High/Low for range work and get levels from an intraday or live endpoint. Related: [[finding_yahoo_sparse_index_date_shift]], [[finding_ohlc_verify_before_session_claims]], [[finding_mtime_is_corrupted_by_git_sync]] (same shape: a freshness/completeness proxy keyed to the wrong clock, failing FALSE-NEGATIVE and silently).
