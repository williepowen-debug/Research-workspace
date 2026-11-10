# D:L342: acceptance condition, written BEFORE the fix (2026-11-10 11:3x ET)

Fix scope: `scripts/thresholds.py` `append_daily_log()`, the only VIOLET writer that can create a VX_DAILY row on a weekday NYSE holiday. It skips Sat/Sun only. `backfill.py` already refuses to create an orphan-VIX row (MEMORY: orphan ^VIX = phantom, 13/13 exact at source).

Rule: refuse to write a row when VIX is present and VIX9D, VIX3M, VIX6M and VVIX are all empty (an orphan VIX). Return the status `skip-orphan-vix`. A refused row is recoverable, because backfill.py creates any real session's row from Cboe History. A written phantom row is not removed by anything.

PASS requires all of:
- **A1:** a row dated 2026-09-07 built from Cboe History (VIX 15.30; no 9/07 bar in VIX9D, VIX3M, VIX6M or VVIX) returns `skip-orphan-vix`, and the ledger copy is byte-identical afterwards.
- **A2:** a row dated 2026-09-08 built from Cboe History (all companions present) returns `appended` on a ledger copy with its 9/08 row removed. A real session still writes.
- **A3, cross-check:** SPY (yfinance daily) has no bar on 2026-09-07 and has one on 2026-09-08. Cboe VIX_History has 9/07 = 15.30, while VIX3M, VIX9D, VIX6M, VVIX and SKEW History all lack 9/07. The companion rule and the SPY rule agree on the test day.
- **A4:** `run_tests.py --quiet` passes, and the closeout guard stays green.
