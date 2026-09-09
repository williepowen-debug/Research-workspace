# September 11 positioning review — prepared September 9

**PENDING RELEASE.** September 11 at 15:30 ET is the carried CFTC publication cadence for September 8 positions. The September 9 fetch still reports September 1. No post-rally covering verdict exists yet.

Sources: [CFTC legacy futures-only](https://www.cftc.gov/dea/newcot/deafut.txt), [TFF futures-only table](https://www.cftc.gov/dea/futures/financial_lf.htm), saved raw files and [calculation](../research/outputs/2026-09-09_followthrough/analysis.json). Contract market code **097741**. Both sources have OI **411,882** on September 1, +27,666 week-on-week; the TFF categories plus spreading/non-reportables reconcile on both sides.

| September 1 baseline | Long | Short | Net | Weekly Δ long | Weekly Δ short |
|---|---:|---:|---:|---:|---:|
| Legacy non-commercial | 117,169 | 209,396 | −92,227 | −11,171 | +17,758 |
| TFF dealer | 116,682 | 37,361 | +79,321 | +16,690 | −19,693 |
| TFF asset manager | 70,419 | 94,940 | −24,521 | −1,002 | +3,403 |
| TFF leveraged funds | 58,529 | 160,717 | −102,188 | −7,999 | +17,147 |
| TFF other reportables | 55,035 | 2,313 | +52,722 | −5,380 | +657 |

These populations differ; do not equate leveraged funds with legacy non-commercials or sum overlapping taxonomies. September 1 is a **short build before the rally**. Current normalization is 49.0% of |−188,077|; the historical TSV's 180K-based column remains legacy data.

At release:

1. Save the new primary publication with retrieval time/hash. Require **as-of September 8**, market code 097741 and futures-only scope before describing it as the new print. If still September 1, report delayed/unavailable and stop the inference.
2. Compute gross long/short/net changes and OI against this baseline; verify built-in change columns and check revisions. For covering percentage use `−Δshort / prior short`, never current short as denominator. Decompose new longs, short covering and two-sided liquidation; a net change alone cannot identify which occurred.
3. Reconcile TFF populations and spreading to OI. Report cohort disagreement; do not force a common carry-unwind story or identify OTC swaps from exchange positions.
4. Compare the weekly snapshot with the rally's actual window and matched FX observations. It covers through September 8, not September 9–11 activity. FX direction and position changes can disagree without either being false.
5. Write a sourced research verdict and update STATUS. Retired −108K/−140K/−153K gates remain retired. Do not revive entry rules or add a hindsight deadband. Original SAM-28/31 terms govern the September 18 review separately.

US August CPI is separately scheduled September 11 **08:30 ET** ([BLS calendar](https://www.bls.gov/schedule/2026/09_sched.htm)); record actual/core/base and consensus provenance before policy interpretation. A CPI surprise alone is not the frozen Fed **dot-walk-back** trigger.
