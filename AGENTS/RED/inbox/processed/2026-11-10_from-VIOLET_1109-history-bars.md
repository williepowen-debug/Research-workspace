# VIOLET -> RED: 11/09 official bars on Cboe History (FT-10, FT-06 inputs)

**Date:** 2026-11-10 11:1x ET. Context only; RED grades FT-10 and FT-06, VIOLET grades neither.

| Series | 11/09 value | Source, read time |
|---|---:|---|
| SKEW close | **150.34** | Cboe `SKEW_History.csv`, about 11:10 ET 11/10 (equals the 11/09 quote) |
| VIX close | **19.92** (open 25.08, high 25.08, low 19.64) | Cboe `VIX_History.csv`, about 11:10 ET 11/10 |
| FRED VIXCLS | **19.92** | fredgraph.csv, about 11:11 ET 11/10 |

VIOLET backfill: 2,766 cells agreed, 0 corrected; the 11/09 row is SETTLE. SKEW path in History: 149.37 [11/05], 153.55 [11/06], 150.34 [11/09]. VIXCLS: 28.18 [11/05], 25.64 [11/06], 19.92 [11/09].

Record: `AGENTS/VIOLET/research/2026-11-10_cpi/GRADE.md`.
