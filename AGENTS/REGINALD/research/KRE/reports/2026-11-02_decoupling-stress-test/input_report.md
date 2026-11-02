# Stress-Testing the KRE Decoupling (data through the 30 Oct 2026 close)

**Question.** Is the low KRE–KBWB correlation a lasting change in how regional-bank stocks behave, or is it mostly a handful of unusual trading days?

**Short answer.**
1. **Removing the unusual days does not make the rarity go away.** Taking out the 10 largest gap days lifts the correlation from 0.719 to 0.854. But the same deletion applied to every historical window lifts those windows too. Against that matched benchmark, the current value still sits at about the 1st percentile at every trim level.
2. **The low correlation is lasting, and it started earlier than the original report implies.** It began around **June 2026**, before both 14 Sep and 22 Oct, and an earlier episode ran from September 2025 to February 2026. Before 2025, low-correlation episodes almost always ended within one 63-session window. This one has not.
3. **"KRE decoupled from KBWB" is mostly KRE decoupling from the stock market as a whole.** Once SPY's effect is removed, the KRE–KBWB correlation is only at the **11th percentile**. The extreme number comes mainly from KRE's market beta falling to 0.33 (1.3rd percentile). About half of the gap from normal comes from low volatility (the Forbes–Rigobon effect). The other half comes from a gap in daily returns between the two ETFs that is wider than usual.
4. **The R² column in the original report is wrong.** On the stated sample, R² should be 0.517, 0.251 and 0.048. No single calculation reproduces all three reported values, so they appear to come from mixed calculations. One of them, 0.525, is exactly what a degrees-of-freedom mismatch produces.

A *rare* reading is not the same as a *significant* one, and neither proves a lasting *regime change*. My overall confidence is in §6.

---

## 0. Data and methods (applies to everything below unless a section says otherwise)

| Item | Definition |
|---|---|
| Prices | Yahoo Finance v8 chart API, `adjclose` (adjusted for splits and dividends). I checked the adjustment by hand on KRE's ex-dividend dates: 21 Sep 2026 gives −0.481% on adjclose versus −0.478% computed manually from close plus the $0.412 dividend, while the price-only return is −1.045%. 22 Jun 2026 checks out the same way. |
| Cross-check against the issuer | SSGA KRE daily NAV history (navhist xlsx). The NAV-based total-return correlation with KBWB over the same window is **0.714**, against 0.719 on market prices. KBWB has no issuer cross-check because Invesco's holdings and NAV downloads are blocked or JavaScript-only. |
| Returns | Simple daily total returns, close to close. Sessions are the US trading days on which both series trade. |
| Main window | **63 returns, 4 Aug → 30 Oct 2026** (base price 3 Aug). Prices for 2 Nov 2026 were downloaded but are excluded. |
| Historical benchmark | Every 63-session window ending from 2 Feb 2012 to 30 Oct 2026: **3,708 overlapping windows**. Non-overlapping grid: 59 windows anchored on 30 Oct (step 63). |
| Percentile | Share of historical windows with a strictly lower value. |
| Yields (§3 only) | US Treasury daily par-yield-curve CSVs for 2011–2026, 2-year and 10-year. On bond-market holidays the prior value is carried forward. |
| Trim rule | Within each window, rank days by \|r_KRE − r_KBWB\| and delete the top k. **The same rule is applied to every historical window**, so each trimmed result is compared with a trimmed benchmark. |
| Scripts | `scripts/fetch.sh` downloads the raw inputs. The `data/` folder holds the processed ETF price panels and the issuer and Treasury files as of 2 Nov 2026. Then run in `scripts/`, in this order: `panel.py`, `sens.py`, `sens_pairs.py`, `horizons.py`, `path.py`, `vol.py`, `factor.py`, `partial_rates.py`, `persist.py`, `boot_nav.py`, `seqtrim.py`, `lowfreq.py`, `r2recon*.py`). Outputs are in `out/`. |

The original headline figures replicate exactly: KRE–KBWB 0.7193, KRE–SPY 0.2193, KRE–IWM 0.5010, KRE–KBE 0.9880, percentile 1.51–1.54. The top five gap days account for 43.8% of the summed squared gaps (43.1% if the gaps are demeaned first), and the top ten for 62.2%.

---

## 1. Does the low correlation survive removing the unusual days?

### 1a. Removing specific days, and the matched historical benchmark (63 sessions)

| Test | n | Correlation | Change vs full | Hist. median (same rule) | Percentile (overlapping) | Rank among 59 non-overlapping | Lowest value before 2026 (same rule) |
|---|---|---|---|---|---|---|---|
| Full window | 63 | **0.719** | – | 0.940 | 1.5% | 1 | 0.803 (Sep 2018) |
| Drop 14 Sep | 62 | 0.749 | +0.030 | 0.943 (rule: drop the 2nd-largest gap day) | 1.7% | 2 | 0.805 |
| Drop 22 Oct | 62 | 0.753 | +0.034 | 0.943 (rule: drop the largest) | 1.3% | 1 | 0.819 |
| Drop both | 61 | **0.785** | +0.066 | 0.946 | 1.6% | 2 | 0.831 |
| Drop top 5 | 58 | **0.821** | +0.102 | 0.953 | 1.3% | 1 | 0.857 |
| Drop top 10 | 53 | **0.854** | +0.134 | 0.962 | 1.1% | 2 | **0.845 (Nov 2025)** |

Where the rank is 2, the one lower non-overlapping window is the one immediately before (May–Jul 2026), which belongs to the same episode. At the top-10 trim, one window from late 2025 is lower than today's value.

### 1b. How much each day moves the correlation

Cumulative effect of deleting the largest gap days one at a time:

| Day | KRE % | KBWB % | Gap (pp) | Correlation after deletion | Change |
|---|---|---|---|---|---|
| 22 Oct | +2.53 | +0.16 | +2.38 | 0.753 | +0.034 |
| 14 Sep | +0.28 | −1.89 | +2.17 | 0.785 | +0.033 |
| 20 Aug | −0.39 | −1.79 | +1.41 | 0.797 | +0.012 |
| 28 Oct | −0.65 | +0.63 | −1.28 | 0.809 | +0.012 |
| 21 Sep | −0.48 | +0.80 | −1.28 | 0.821 | +0.012 |
| 9 Oct | −0.83 | +0.41 | −1.25 | 0.834 | +0.013 |
| 22 Sep | −1.11 | −2.33 | +1.22 | 0.838 | +0.003 |
| 21 Oct | 0.00 | +1.15 | −1.15 | 0.848 | +0.010 |
| 16 Sep | −1.77 | −2.88 | +1.11 | 0.844 | **−0.004** |
| 5 Aug | −0.64 | +0.35 | −0.99 | 0.854 | +0.010 |

Leave-one-out influence, dropping each of the 63 days separately (`out/loo.csv`): 30 of the 63 days would raise the correlation if removed. After 22 Oct (+0.034) and 14 Sep (+0.029), the effects are small and spread out. **Negative finding for the "a few days" story:** after the top two days, the effect is a long tail of ordinary-sized gaps, not a few outliers.

### 1c. Other robustness checks
- **Rank (Spearman) correlation:** 0.717, at the 1.43rd percentile. The lowest value before 2026 was 0.718, so the current figure only ties the earlier low and does not beat it.
- **Lower-frequency returns** (log, non-overlapping): 2-day returns over 126 sessions give 0.663 (0.1st percentile); 5-day returns over 126 sessions give 0.691 (0.1st percentile, n=25). This rules out stale small-bank closing prices as the explanation.
- **Block bootstrap** (stationary, mean block length 5, 10,000 draws) of the 63-day correlation: 95% interval **[0.61, 0.81]**. Fisher interval: [0.57, 0.82].

**Rarity vs significance.** The 1.5th percentile is a rank among overlapping windows. There are only about 59 independent 63-day windows, so being lowest of 59 means p ≈ 1/59 at best. That figure ignores that this pair and this moment were picked *because* they looked unusual, and that many pairs were examined. The bootstrap interval sits entirely below the historical 10th percentile (0.863). That says the *within-window* correlation is genuinely low. It does not say the low correlation will last.

---

## 2. Is the divergence sustained?

### 2a. Different window lengths (all ending 30 Oct; percentiles since Feb 2012)

| Pair | 21d | 42d | 63d | 126d | 126d rank among non-overlapping windows |
|---|---|---|---|---|---|
| KRE–KBWB | 0.672 (1.2%) | 0.708 (1.2%) | 0.719 (1.5%) | **0.730 (0.1%)** | 1/29 |

The 126-session window, which starts around 1 May 2026, is the lowest on record. That window reaches back well before 14 Sep.

### 2b. Gradual or sudden?
Non-overlapping 21-session blocks, oldest first (full table in `out/path_blocks.csv`):

| Block (21 sessions) | 2 Feb–3 Mar | 4 Mar–1 Apr | 2 Apr–1 May | 4 May–2 Jun | **3 Jun–2 Jul** | **6 Jul–3 Aug** | 4 Aug–1 Sep | 2 Sep–1 Oct | 2–30 Oct |
|---|---|---|---|---|---|---|---|---|---|
| KRE–KBWB | 0.933 | 0.902 | 0.872 | 0.890 | **0.677** | **0.640** | 0.793 | 0.742 | 0.672 |
| KRE ann. vol % | 30.0 | 18.7 | 20.2 | 20.0 | 21.3 | 19.0 | 12.9 | 15.9 | 17.7 |

- The sharp step down happened in **June–July 2026**, before either flagged event. The current 63-session window is *not* the low point: 15 Sep 2026 was (0.632).
- Of the last 18 blocks (since May 2025), 16 are below the historical median block correlation (0.927) and 9 are below its 10th percentile (0.836). **In the last 12 blocks, 7 are below the 10th percentile. No earlier 12-block stretch had more than 3.**
- Episodes with the 63-day correlation below 0.863 (the 10th percentile), merged when gaps are under 63 sessions: 2012-02, 2012-11, 2013-06→2014-02, 2014-06, 2014-10→2015-01, 2018-07→10, 2024-05→07, **2025-09→2026-02 (85 days below)**, **2026-06→now (96 of 100 days below)**. Share of days below the threshold by year: 2025 19%, **2026 64%**.
- **Persistence check:** before 2025, after a 63-day window below the 10th percentile, the *next* 63-day window was also below it only **0.5%** of the time (median next value 0.911). The 2025–26 period breaks that pattern.
- **Counterpoint:** the Fisher-z correlation on the non-overlapping grid has an AR(1) of 0.67, so low windows naturally cluster. And the 2025–26 episode *did* recover, back to about 0.91 by May 2026, before falling again.

### 2c. Comparison with similarly low-volatility periods
The current KRE 63-day volatility is 15.6%, at the 9th percentile. KBWB is at 16.4% (20th percentile).

| Historical subset | Windows | Median corr | 10th pct | Share of windows ≤ 0.719 | Lowest before 2026 |
|---|---|---|---|---|---|
| All | 3,708 | 0.940 | 0.863 | 1.5% | 0.803 |
| KRE vol in bottom quintile | 741 | 0.884 | 0.836 | 5.1% | 0.803 |
| KRE vol within ±2 pts of current | 733 | 0.886 | 0.840 | 5.2% | 0.816 |
| KRE and KBWB vol both in bottom quartile | 746 | 0.888 | 0.843 | 2.7% | 0.803 |

Every low-volatility window below 0.719 falls in 2026 itself. A regression of Fisher-z correlation on log KRE volatility, using 58 non-overlapping windows, predicts **0.90** at current volatility; the current value is about **2.2 standard deviations below** that prediction. **Volatility explains part of the low reading, but not all of it.**

The mechanics, writing the gap volatility as σ(K−B): corr = (σK² + σB² − σ(K−B)²) / (2σKσB).
- σ(K−B), the volatility of the daily KRE-minus-KBWB return gap, is 12.0% annualised, at the **82nd percentile** (median 8.9%).
- Current volatilities with a *median* gap give 0.849.
- *Median* volatilities with the *current* gap give 0.859.
- Both conditions are needed to reach 0.72. This is the Forbes–Rigobon point: correlation depends on the level of volatility ([Forbes & Rigobon, J. Finance 2002](https://doi.org/10.1111/0022-1082.00494)). Here it works in reverse: calm markets push measured correlation down.

---

## 3. Is this specific to KRE versus KBWB?

### 3a. Other pairs (63 days; percentile; rank among non-overlapping windows; trim rule applied to each pair's own gaps)

| Pair | Full | Drop top 2 | Drop top 5 | Drop top 10 |
|---|---|---|---|---|
| KRE–KBWB | 0.719 (1.5%) | 0.785 (1.6%) | 0.821 (1.3%) | 0.853 (1.1%) |
| **KBE–KBWB** | 0.763 (1.1%) | 0.827 (1.5%) | 0.844 (0.7%) | 0.882 (0.3%) |
| **QABA–KBWB** | 0.649 (2.2%) | 0.722 (2.7%) | 0.768 (2.2%) | 0.825 (3.4%) |
| IAT–KBWB | 0.886 (3.6%) | 0.915 (3.5%) | 0.927 (3.4%) | 0.926 (1.9%) |
| KRE–SPY | 0.219 (1.6%) | 0.356 (3.0%) | 0.383 (2.3%) | 0.467 (4.0%) |
| KRE–IWM | 0.501 (2.9%) | 0.584 (3.6%) | 0.653 (4.6%) | 0.733 (5.0%) |
| KRE–IAT | 0.898 (0.1%) | 0.915 (0.1%) | 0.937 (0.4%) | 0.951 (0.6%) |
| KRE–KBE | 0.988 (29.5%) | 0.991 | 0.992 | 0.995 (48%) |
| KBWB–SPY | 0.525 (**14.3%**) | 0.569 (14.7%) | 0.622 (16.0%) | 0.729 (25.2%) |

### 3b. Constituent baskets (63 days; percentiles from 2021 onward only, because constituent prices start in 2021; baskets use **current** members, so there is survivorship bias)

| Pair | Corr | Percentile since 2021 |
|---|---|---|
| KRE vs KRE members weighted by SSGA weights (30 Oct) | 0.998 | 99% (the ETF tracks its holdings) |
| KRE vs the 10 KRE∩KBWB large regionals (TFC MTB HBAN CFG RF EWBC PNFP FHN ZION WAL), equal-weighted | 0.900 | **0.2%** |
| Those 10 large regionals vs the rest of KRE | 0.845 | **1.0%** |
| Those 10 large regionals vs 14 KBWB megabanks/super-regionals, equal-weighted | 0.846 | 12% |
| Megabank basket vs SPY | 0.543 | 22% |
| GS+MS vs SPY | 0.720 | 65% |

### 3c. Removing the market and rates factors (KRE and KBWB each regressed on the controls; residuals correlated over 63 days, history from 2012)

| Partial correlation of KRE and KBWB, controlling for | Value | Median | Percentile |
|---|---|---|---|
| Nothing (raw) | 0.719 | 0.940 | 1.5% |
| SPY | **0.728** | 0.874 | **11.1%** |
| SPY + Δ10y | 0.719 | 0.858 | 12.6% |
| SPY + IWM | 0.713 | 0.872 | 10.1% |
| Δ10y only | 0.697 | 0.917 | 1.6% |

| 63-day beta to SPY | Value | Median | Percentile |
|---|---|---|---|
| KRE | **0.33** | 1.11 | **1.3%** |
| KBWB | 0.83 | 1.16 | 10.1% |

**Reading.** KRE, KBE and QABA move almost identically (correlations around 0.99), and all three separate from KBWB to a similar degree. So this is a **small/mid regional-bank factor**, not a quirk of the KRE wrapper or its index. Supporting points:
- Prices against NAV and against the member basket rule out an ETF artefact.
- The split follows bank size: KRE's smaller names separate even from the large regionals inside KBWB, and those large regionals still track the megabanks normally.
- KBWB itself looks fairly ordinary. It tracks its megabanks, and its SPY correlation is only at the 14th percentile, so **large-bank-specific shocks are not the main driver**. 14 Sep is a real large-bank shock, but it is one day.
- It is **not a broad-market effect** in the sense of everything decoupling: IWM–SPY is at about the 10th percentile, which is not extreme.

The most extreme part of the reading is **KRE's collapsed equity-market beta**. With SPY controlled, the bank-specific comovement is below normal but not unprecedented (11th percentile). Controlling for the 10-year yield does not restore the correlation, so a simple linear rate-sensitivity story is **not** what separates them day to day.

---

## 4. Reconciling correlation and R²

On the identical 63-return sample, a single-variable OLS with an intercept gives R² = r² **exactly**: KBWB **0.517**, IWM **0.251**, SPY **0.048**. The reported values (0.525 / 0.282 / 0.067) are *not* from that calculation. I tested return type (simple, log, unadjusted), window length (50–79 returns), end date (20–30 Oct, and 2 Nov), with and without an intercept, extra regressors (SPY, Δ10y, Δ2y) and a variance-normalisation (ddof) mismatch:

| Reported | Candidates that match within 0.0015 on this data |
|---|---|
| KBWB 0.525 | **Degrees-of-freedom (ddof) mismatch** on the stated sample: 1 − var(residual, ddof=0)/var(y, ddof=1) = r² + (1−r²)/63 = **0.5251**. A 64-return (off-by-one) window gives 0.527. Several 2-factor variants on 60–67-return windows also match. |
| IWM 0.282 | **KRE ~ IWM + Δ10y** on the stated sample = **0.2824**. Not reproduced by the ddof mismatch (0.263) or the 64-return window (0.272). |
| SPY 0.067 | No match on the stated sample. Univariate on 65 returns = 0.066. The ddof mismatch gives 0.063. |

**Conclusion.** No single spec reproduces all three values, so they come from **at least two different calculations**: a ddof or window error, and probably a regression with an added rate term. Too many combinations fit each number individually to name *the* cause with certainty. The prior working notes do show that the earlier study ran KRE ~ X + Δ10y regressions in this same window (its "R² 0.15–0.17" for KRE ~ SPY + Δ10y matches my 0.153 / 0.167). **Fix:** report R² = r² (0.517 / 0.251 / 0.048), or label multi-factor R² explicitly. None of the conclusions depend on this.

---

## 5. Answers to the deliverable questions

**How much of the decoupling survives removing the unusual days?** In *level*, deleting 14 Sep and 22 Oct recovers 0.066 of the 0.221 gap to the median, and the top 10 days recover 0.134. In *rarity*, none of it goes away: every trimmed value is at about the 1st percentile of identically trimmed history. A rank-based measure and 2-day and 5-day returns give the same result.

**Is there evidence of a sustained change?** Yes, in persistence. Low correlation has been the usual state for much of the 14 months since September 2025, the 126-day window is the lowest on record, and the step down predates the flagged events. What the evidence does *not* show is a change in how banks relate to *each other*: with the market controlled, bank-to-bank comovement is only at the 11th percentile. The persistent change is mainly that **small and mid-sized regional banks have stopped moving with the equity market** (beta 0.33). In calm markets that mechanically shows up as low correlation with every equity series, KBWB included.

**Which alternative explanations remain plausible?**
1. **Low volatility mechanically lowers correlation.** This explains roughly half of the gap from normal.
2. **A market-beta collapse rather than a bank regime.** The regionals no longer co-move with a market whose leadership is elsewhere (earlier work noted AI-stock sell-offs on regional-bank up-days). The low partial correlation given SPY fits this.
3. **Ordinary clustering of low-correlation states.** AR(1) is 0.67, and the 2025–26 episode reverted once already.
4. **Large-bank capital-markets news.** Real (BAC, 14 Sep), but it explains about 0.03 of correlation.
5. **Rate sensitivity.** 22 Oct was a rates day, but a linear Δ10y control does not restore the correlation. A nonlinear or event-driven rate effect is not ruled out.
6. **Selection effects.** The pair and the moment were chosen because they looked odd.

Wrapper or index artefacts and stale-price microstructure are **largely ruled out**.

**What would most convincingly disprove the regime-change idea?** The next non-overlapping 63-session window, from 2 Nov 2026 to about 2 Feb 2027, showing a KRE–KBWB correlation **back above about 0.86** (the historical 10th percentile, close to the low-volatility median) **while KRE volatility stays low** (below about 20%) **and KRE's SPY beta recovers toward about 0.8 or higher**. A recovery during a stress spike would *not* count, because high volatility pushes correlations up for everyone. Before 2025, this kind of reversion happened after essentially every low window (99.5%). If it happens now in a calm market, the "regime" was a normal, if prolonged, episode.

---

## 6. Confidence and gaps

| Claim | Confidence | Why |
|---|---|---|
| The headline numbers replicate, and the R² column is wrong | **High** | Exact replication; the arithmetic is mechanical. |
| The rarity survives deleting the top 1, 2, 5 or 10 gap days against matched benchmarks | **High** | Consistent across rules, pairs, rank correlation and return frequency. |
| The low correlation began around June 2026, before the flagged events, with an earlier episode in 2025 | **High** | Visible in every window length and in non-overlapping blocks. |
| The extreme reading mainly reflects KRE's collapse in market beta plus low volatility, not bank-to-bank decoupling | **Medium** | Partial correlation and the volatility identity support it; the factor choice (SPY) affects the split. |
| This is a *lasting regime* | **Low–medium** | Persistence is unusual, but there are only about 9 independent episodes since 2012, one of which already reverted, and the forward test has not happened yet. |
| Which calculation produced each wrong R² | **Low** | Many specifications fit each number individually. |

**Gaps and caveats.**
- KBWB prices are vendor data with no issuer NAV cross-check, because Invesco's pages and downloads could not be retrieved.
- KBWR (Invesco KBW Regional Banking ETF) returned "no data" from the price source, so I could not use it as a second issuer-defined regional basket; IAT and QABA were used instead.
- QABA is very small and thinly traded (about $86M, a few thousand shares a day).
- The constituent baskets use 30 Oct 2026 membership, so they carry survivorship bias and their history starts only in 2021.
- The trim rule (largest absolute gaps) is one of several possible rules. Deleting the days that most *raise* the correlation would give slightly higher trimmed values, again against a matched benchmark.
- These are sensitivity tests, not unbiased significance estimates.

## Sources
- SSGA KRE fund page (index; modified equal weight): https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-regional-banking-etf-kre
- SSGA KRE factsheet (linked benchmark: KBW Regional Banking Index until 24 Oct 2011, so every window here uses the S&P index): https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-kre.pdf
- SSGA KRE daily holdings (30 Oct 2026): https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-kre.xlsx
- SSGA KRE NAV history: https://www.ssga.com/library-content/products/fund-data/etfs/us/navhist-us-en-kre.xlsx
- S&P DJI, S&P Regional Banks Select Industry Index: https://www.spglobal.com/spdji/en/indices/equity/sp-regional-banks-select-industry-index/
- Invesco KBWB page (no usable content; methodology text taken from the prospectus summary as quoted by Yahoo Finance): https://www.invesco.com/us/en/financial-products/etfs/invesco-kbw-bank-etf.html ; https://finance.yahoo.com/quote/KBWB/profile/
- iShares IAT (Dow Jones U.S. Select Regional Banks Index): https://www.ishares.com/us/products/239521/ishares-us-regional-banks-etf
- First Trust QABA: https://www.ftportfolios.com/retail/etf/etfsummary.aspx?Ticker=QABA
- US Treasury daily par yield curve (2Y/10Y; 22 Oct 2026: 2Y 4.81→4.65, 10Y 5.13→4.96): https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv
- 14 Sep BAC guidance (verbal, at a conference; no SEC filing found): CNBC https://www.cnbc.com/2026/09/14/bank-of-america-bac-q3-investment-banking-fees.html ; Quartz https://qz.com/bank-of-america-ceo-investment-banking-fees-trading-revenue-091526
- Forbes, K. & Rigobon, R. (2002), "No Contagion, Only Interdependence," *Journal of Finance* 57(5): https://doi.org/10.1111/0022-1082.00494
- Price data: Yahoo Finance v8 chart API (vendor, secondary; KRE cross-checked against the SSGA NAV).
