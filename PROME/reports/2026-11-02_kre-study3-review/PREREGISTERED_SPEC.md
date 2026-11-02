# Study 3 — classification rules fixed BEFORE computing any forward return
Written 2026-11-02 ~20:50 UTC, before regime.py was run. Not changed afterwards
(any later change is logged at the bottom with its reason).

## Sample
- Daily adjusted closes (Yahoo v8 chart, adjclose): KRE from 2006-06-22, KBWB from 2011-10-20, IWM, SPY, HYG, IEF.
- Yields: US Treasury daily par yield curve, 2Y and 10Y. Bond-market holidays when stocks trade: carry the prior yield forward.
- Last observation used: 2026-10-30 close.

## Window grids
- Non-overlapping windows of W = 20 and W = 63 sessions, anchored so the last window ENDS on 2026-10-30, stepping back in blocks of W.
- Forward returns are measured from the window's end close: next 20 and next 60 sessions.
- W=63: forward 20 and 60 never overlap across windows (60 < 63).
- W=20: forward 20 never overlaps. Forward 60 WOULD overlap, so for that combination only every third window is used
  (3 phases; phase 0 = the one containing the latest window is primary; the other two phases are reported as a range).

## Conditioning (window-level, measured over the window itself)
Falling yields: change in the 2Y (or 10Y, reported separately) over the window < 0.
(a) KRE up: KRE total return over the window > 0.
(b) Credit spread widening: change in spread > 0.
    - Primary credit measure: Moody's Baa − 10Y (FRED BAA10Y), because the free FRED HY OAS (BAMLH0A0HYM2) only starts 2023-11-03.
    - Cross-check: HYG − IEF total-return difference < 0 counts as "widening" (from 2007-04).
    - HY OAS itself is used only for the current episode and to check proxy agreement 2023-11 → 2026-10.
(c) Curve steepening: change in (10Y − 2Y) > 0.
(d) KRE beats KBWB: KRE return − KBWB return over the window > 0 (only windows starting after 2011-10-20).

## Alternative thresholds (robustness, one set)
- Falling yields: Δy ≤ −10bp (W=20) / ≤ −20bp (W=63).
- Dead-bands; windows inside the band are dropped from that dimension:
  (a) |KRE ret| > 2% (W=20) / 4% (W=63); (b) |ΔBAA10Y| > 5bp / 10bp; (c) |Δ2s10s| > 5bp / 10bp; (d) |KRE − KBWB| > 1% / 2%.

## Outcomes
- Forward KRE return (absolute), KRE − KBWB, KRE − IWM (simple return differences), for 20 and 60 sessions.
- Each cell: n (independent windows), mean, median, hit rate (share > 0).
- Baseline: ALL windows on the same grid with a forward return available (unconditional).
- Report cell mean − baseline mean. Welch t of cell vs its complement only if n ≥ 10 in the cell; label cells with n < 10 "too thin".
- No t-stats on overlapping windows anywhere.

## Rate beta
- Rolling 63-session OLS: r_KRE = a + b_mkt · r_SPY + b_rate · Δy10 (Δy in percentage points, return in decimal) + e.
  Same with Δy2 as a variant.
- "Negative regime" = b_rate < 0 (primary); alternative b_rate < −0.03.
- Episodes: runs of negative b_rate merged if separated by < 63 sessions.
- Forward test: on the non-overlapping 63-session grid, condition on b_rate at window end; forward 20/60 KRE absolute and vs KBWB/IWM, plus forward 60-session max drawdown; compare with all grid points.

## Labels
- "Constructive" (descriptive label, defined in advance): falling-yield window with KRE up AND credit narrowing.
- "Stress rebound" : falling-yield window with KRE up AND credit widening.
- "Stress" : falling-yield window with KRE down AND credit widening.
- "Benign/other" : falling-yield window with KRE down AND credit narrowing.
Whether any of these labels is followed by better or worse returns is the empirical question, not assumed.

## Change log
- Primary rules above were NOT changed after forward returns were seen.
- Added AFTER seeing primary results (exploratory, labelled as such in the report):
  (1) ex-GFC variant (drop windows touching 2007-07..2009-06) - added because 2008 dominated some cells;
  (2) phase robustness for W=20/h=60 extended to the HYG proxy;
  (3) exclusion of forward windows overlapping COVID (2020-02..04) and SVB (2023-03..05) for the KRE-vs-KBWB result;
  (4) 12-session pattern scan matching 10/14->10/30 (10y <= -15bp, KRE >= +3%, Baa wider AND HYG<IEF), rule written before its forward returns were printed;
  (5) nearest-neighbour analogs on z-scored W=20 features; (6) rate-beta-sign x falling-yield interaction;
  (7) real-yield vs breakeven split (FRED DFII10, T10YIE).
- Cross-section (xs/crosssection.py): spec written in the script docstring before first run; CRE denominator fallback to Tier 1
  added after the first run crashed on banks that report no total risk-based capital (CBLR filers) - a data fix, not a result-driven change.
