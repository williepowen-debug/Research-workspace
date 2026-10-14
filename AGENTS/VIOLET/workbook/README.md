# VIOLET workbook state register

Reviewed October 14, 2026. Raw TSV schemas remain intact; do not prepend banners that would break their readers. Current observations and source frontiers live in STATUS; this register describes use and refresh contracts.

| Surface | State / use | Refresh contract |
|---|---|---|
| VX_DAILY | LIVE daily record plus explicitly labelled current TICK | Cboe exact-date daily closes certify SETTLE; incomplete publication stays TICK; futures retain their own date |
| MOVE, JPY_VOL, OVX, CHEAP_TAIL, IMPLIED_CORR | LIVE | Boot, actual observation dates; IV/prev-close caveats in STATUS |
| COT_VIX | LIVE weekly positioning | Actual published CFTC report date and cadence/grace; never assume the next release exists |
| VIX_OPTIONS | LIVE dated chain snapshots | Regular-hours/source-quality checks; retain bad rows as labelled artifacts; gross OI is not initiated net flow |
| CATALYSTS | LIVE future events | Official dates and twin check |
| PREDICTIONS | Navigation index, six resolved entries | Frozen source and dated grade always win; no new authority or copied full branch rules |
| KB | DATED EVIDENCE | Historical empirical facts are not today's state. Past Stale_By alone does not refute a finding; validator explains this. Current-live claims are revalidated separately. |
| FLOW / board_log / corrections receipts | EVENT LOGS | Append only on actual send/read/receipt; no daily market cadence; exact-ID lookup, never a truncated whole-read |
| VX_M1_HISTORY | FROZEN research sample through July 29 | Not a pure M1 series: DTE composition defect KB-VIO-212; do not use as live curve |
| VX_TERM_HISTORY | FROZEN research corpus through August 3 | Historical calibration only; fresh study requires dated rebuild and its own validation |
| DIET_COILED_SPRING.csv / FEB2018_VOLMAGEDDON_M1M2.csv | STATIC DERIVED study outputs | See README_STATIC_ARTIFACTS.md; not live ledgers; thesis owns conditional base rates |
| SCHEMA | STATIC parser contract | Change only with intentional schema migration |

The root staleness tool does not consume this Markdown state register and may still report historical-table age. That is a declared limitation, not a claim of mechanized freezing. `LEDGER_GLOB` broadens coverage; it does not certify content correctness.
