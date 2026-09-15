# VIOLET workbook state register

Reviewed September 14, 2026. Raw TSV schemas remain intact; do not prepend banners that would break their readers.

| Surface | State / use | Refresh contract |
|---|---|---|
| VX_DAILY | LIVE; all six spot columns through September 14 | Cboe confirm; row and SKEW-cell completeness; both futures symbols/date |
| MOVE, JPY_VOL, OVX, CHEAP_TAIL, IMPLIED_CORR | LIVE | Boot, actual observation dates; IV/prev-close caveats in STATUS |
| COT_VIX | LIVE; September 8 report | Actual CFTC publication and cadence/grace |
| VIX_OPTIONS | LIVE but September 14 OI unusable | Regular-hours chain required; retain bad rows as labelled source artifacts |
| CATALYSTS | LIVE future events | Official dates and twin check |
| PREDICTIONS | LIVE navigation index, six entries | Frozen source always wins; no new authority or copied full branch rules |
| KB | DATED EVIDENCE | Historical empirical facts are not today's state. Past Stale_By alone does not refute a finding; validator explains this. Current-live claims are revalidated separately. |
| FLOW / board_log / corrections receipts | EVENT LOGS | Append only on actual send/read/receipt; no daily market cadence; exact-ID lookup, never a truncated whole-read |
| VX_M1_HISTORY | FROZEN research sample through July 29 | Not a pure M1 series: DTE composition defect KB-VIO-212; do not use as live curve |
| VX_TERM_HISTORY | FROZEN research corpus through August 3 | Historical calibration only; fresh study requires dated rebuild and its own validation |
| DIET_COILED_SPRING.csv | FROZEN study output | Not a live signal ledger; thesis owns its conditional base rates |
| SCHEMA | STATIC parser contract | Change only with intentional schema migration |

The root staleness tool does not consume this Markdown state register and may still report historical-table age. That is a declared limitation, not a claim of mechanized freezing. `LEDGER_GLOB` broadens coverage; it does not certify content correctness.
