# October 28 close bundle

Will-directed catch-up, retrieved about 23:52 ET October 28, 2026 (03:52 UTC October 29). Same method as `../2026-10-26_close/`: `capture.py` (END moved to 2026-10-29 04:00 UTC) saves raw public responses with hashes in `access.json`; `calculate.py` (TARGET 2026-10-28) applies the unchanged band arithmetic and guard to produce `summary.json`.

- Fund closes: MIRROR Yahoo raw unadjusted daily closes; GLD matched to the PRIMARY SPDR archive (`GLD_issuer_archive.xlsx`, `GLD_latest_issuer.csv`).
- Futures: the October 27 rows are guard-qualified. The October 28 rows are the newest rows, excluded, and retrieved after the evening reopen. Live appended rows are listed separately in `summary.json`.
- PRIMARY Treasury real yield curve: `treasury_real.csv` (October 28 = 2.67%).
- LME copper: Westmetall MIRROR tables, columns identified by header.
- Two-day crossing path (October 26→27→28) was checked separately from the script's last-pair test: no crash or upside crossing; PPLT recovered above −20% on October 27.
- Not a certified settlement; no CME endpoint probed; no new cadence.

Report: `../../research/2026-10-28_catch-up.md`.
