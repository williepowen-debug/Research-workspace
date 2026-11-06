# November 6 window read, BRT-33 first session

**Captured:** c1 2026-11-06 14:45 EST, c2 15:05 EST, `pull.py`, raw bars in `raw/`. Vendor one-minute bars, proxies, not settlements. No exchange page read.

## Result

| Row | Value, [14:28,14:30) ET | Basis |
|---|---|---|
| BRT-33 M1−M3, BZF27 − BZH27 | **NO OBSERVATION** | BZH27 has no bar in the window in either capture |
| BZF27 | 98.3500, 2 bars, 411 lots | [EST vendor proxy] |
| BZH27 | none | last bars 14:25 (93.45, 1,066 lots), then nothing until a zero-volume 14:53 |
| BZG27 | 95.6800, 2 bars, 572 lots | [EST vendor proxy] |
| M1−M2 | +2.6700 | record only |
| CLZ26 | 90.8551 | [EST vendor proxy] |
| January 3:2:1, boundary #8 | $37.1868, count 0, line $50 | (2×RBF27 2.7279 + HOF27 4.2254) × 42/3 − BZF27 |
| December crack | $91.1225 | HOZ26 4.3328 × 42 − CLZ26, record only |

**F-a:** window NOT MEASURABLE, same as 11/5. Same-minute 14:25 read, BZF27 98.49 less BZH27 93.45, is +5.04, not an observation and never a substitute under the row. Not near +$3.50.

## BRT-33 count

Valid sessions 0 of 1. Row needs at least 8 valid sessions, otherwise NO-VERDICT.

BZH27 printed a positive-volume bar in the window on 5 of the last 7 sessions (10/29, 10/30, 11/2, 11/3, 11/4 yes; 11/5, 11/6 no), from `yf` 1-minute bars pulled 15:0x ET 11/6. Both misses are the last two sessions. Small sample.

Sessions left: 14 if Thanksgiving 11/26 has no window session, 15 if it does (the holiday schedule was not read). Chance of fewer than 8 valid sessions, binomial: at the 5/7 rate 7.4% on 14 left, 3.8% on 15; at a 50% rate 60.5% on 14 left, 50.0% on 15. Own arithmetic, independent-sessions assumption, guide only. March volume should rise as January nears expiry; that is reasoning, not measured.

This is a NO-VERDICT risk for the row, not an amendment. The row stands as registered. No change from BRENT without Will.

## Settles and rigs

November 6 settles not found on one search at 15:0x ET (too early for indexing). Baker Hughes not found on one search. Friday Close routine, 16:15 ET, carries both.
