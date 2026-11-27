# D:L1272 — HENRY broadening marker, 11/25 cell (graded 2026-11-27)

**Session:** henry, spawned by PROME prome-80 (Fri 11/27 ~12:42 ET wake); Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop. FRED CSVs read 12:39 ET and saved here at 12:42 ET (`fred_*_read1242.csv`).

## Marker rule (as registered, unchanged)

DOCKET L1272, from HENRY's 11/25 packet § 3 and § 6: the FRED high-yield cell (BAMLH0A0HYM2) for 11/25 **above 376**, **on a day the equal-weight S&P (RSP) fell** = credit-led broadening. Both legs on the same session. Also the FRED SP500 cell for 11/25 against the red line 7,037.04.

## Grade

| Leg | Value | Source, date | Result |
|---|---|---|---|
| HY OAS 11/25 | **377bp** (3.77) | FRED BAMLH0A0HYM2, read 12:39 ET 11/27 | **Level MET: over 376 by 1bp** (one unit of the series' reporting resolution) |
| RSP 11/25 | **+0.83%** (215.74) | vendor close, HENRY close check 11/25 16:36 ET | **Equity leg FAILED** |
| **Marker** | | | **NOT FIRED** (needs both legs the same day) |
| S&P 500 11/25 | **7,182.78** | FRED SP500, read 12:39 ET 11/27 (= vendor bar) | red 7,037.04 **NOT FIRED** (145.74 over); YELLOW (17.22 under 7,200). Provisional grade now FINAL |
| VIX 11/25 | **28.29** | FRED VIXCLS (= vendor 16:15:01 stamp) | ORANGE confirmed (VIOLET owns the broadcast) |

Context cells (FRED 11/25): CCC **1,417bp** (14.17; highest in the pull since 2025-01-01), BB **228bp**, CCC−BB **1,189**.

Superlative check (LESSONS: full-series query before the word): 377 is the **2026 high** (2026-01-01 to 11/25; next 376 on 11/20, 372 on 11/24). It is **not** a multi-year high: the pull since 2024-01-01 has 461 on 2025-04-07 (the April 2025 tariff shock).

## What 377 does and does not establish

- **Does:** junk-bond spreads kept widening through Wednesday's close (363 → 372 → 377 over 11/23–11/25) on a day the average stock rose. The two clocks (credit widening, equal-weight flat) persisted into 11/25. CCC widened further (1,405 → 1,417).
- **Does not:** establish broadening. The registered marker needs the average stock to fall the same day; it rose. And the 1bp margin is the series' rounding unit, so "over 376" is met with no cushion.
- **Cannot see:** Friday. At 12:40 ET 11/27 (vendor, not closes): S&P 7,278 (+1.3%), RSP +1.04%, IWM +1.4%, HYG 76.58 (+0.08%), JNK +0.13%, LQD −0.27%, VIX 24.4 (−13.6% against the 11/25 settle 28.29; fetch.py's −8.8% is against a VIXCLS cell dated 11/26, 26.80, on a NYSE holiday, origin not established, not used). Junk ETFs flat while the 10-year rose about 9bp implies spreads probably tightened on Friday, not widened.

## When next testable

- **11/27 cell** (FRED posts about Mon 11/30): equity leg almost certainly fails (RSP up at the close, see the close addendum below). Read for level only.
- **11/30 cell** (posts about Tue 12/1): first session where both legs can line up. Then each session through 12/4.

## Close addendum (13:00 ET half-day, vendor)

See `CLOSE_1127.md` in this folder (written after 13:12 ET).
