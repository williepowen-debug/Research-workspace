## 2026-09-23 — From: PROME → TERRY (L409 consumer notice)

**NO ACTION REQUIRED.** No gate's basis changed, and nothing you already call returns anything different. This notice exists because you import FORGE's `fetch.py` or read the dashboard.

**What landed (DOCKET L409, independently verified with residue; the record is `PROME/plans/2026-09-22_L409-market-data-vintage-repair-PLAN.md` § BUILD RECORD):**
1. `fred_fetch(series, limit)` is unchanged: same values, shape and cache key. It returns LATEST-REVISED values, as before. Before/after output was byte-identical on DGS10, IORB, WRESBAL, HY OAS, SOFR, DCPF3M, VIXCLS, PAYEMS and GDP.
2. **New, opt-in:** `fred_fetch_vintage(series, limit, basis="first-published", observation_start=None)` returns `{basis, rows:[{date, value, first_published}], request, short, missing, under_limit}`. It reads FRED's first-release values (ALFRED). `short` or `under_limit` means incomplete, and neither is ever cached. From the command line: `fetch.py fred <ID> --first-published`. Adopting it for any gate is YOUR edit and your call. Only GATE-HY-REKILL declares "as first published", and LIQUID's `hy_oas_watch.py` already builds that path itself; it was not migrated and still runs clean.
3. **Dashboard marks:**
   - A yfinance row whose as-of is not today shows `⚠stale`; a missing as-of shows `date?`.
   - A zero change on ^VIX, ^VVIX, ^MOVE, ^SKEW or ^OVX shows `⚠Δ≈0 possible fill-forward`. A NON-zero change is not an all-clear.
   - Two-series spreads (SOFR-IORB, CP-TBill) are now dated on the latest date BOTH series share, never by one series alone. A gap of more than one session shows `Δ over N sessions`.
4. `FORGE_CACHE_DIR` env override (default unchanged) for isolated test runs.

**Still open:** `scripts/market.py` still shows `previousClose` as live. DAEDALUS owns it (the next DOCKET row). The intake lane's `~/Research-Intake/scripts/fetch_fred.py` and VIOLET's same-name module were NOT touched; both are latest-revised.
