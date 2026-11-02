---
title: "Regional banks vs. big banks: KRE decoupling and Q3 2026 fundamentals"
subtitle: "Studies 1 + 2, single consolidated report — data through the 10/30/2026 close (prepared 11/02/2026)"
---

# 1. Summary

**Central question:** which types of regional banks are outperforming, and do improving financial fundamentals support that outperformance?

1. **The decoupling is real.** The KRE–KBWB 63-session correlation of daily returns was **0.719** on 10/30/2026, the **1.5th percentile** of 3,708 rolling windows since Feb 2012. The 2026-09-15 reading (0.632) is the lowest in that history.
2. **The "rally" is smaller than it sounds.** Over those 63 sessions KRE fell 6.0% and KBWB fell 8.4%. 78% of KRE stocks beat KBWB, but only 19% went up. The actual rally runs from the 10/14 low: KRE +5.1% vs KBWB +3.4%.
3. **This is not a handful of stocks and not mainly ETF construction.**
   - KRE decoupled from *everything*: KBWB, SPY, IWM and even KBWB's own regional banks.
   - Regional banks still move together normally among themselves (average pairwise correlation ~35th percentile).
   - Cap-weighting KRE's stocks lifts the correlation to 0.80, but that is still ~6th percentile of its own history.
4. **Drivers.**
   - (a) A capital-markets shock hit the big banks: Bank of America's 9/14 fee warning.
   - (b) Regional banks now trade **inversely to Treasury yields** during a Fed hiking cycle. KRE's rate beta flipped negative (4th percentile) and its S&P 500 beta collapsed (1.6th percentile).
   - (c) A low-volatility regime.
   - The 10/22 flight-to-quality bond rally (KRE +2.5%, SPY −1.2%) is the clearest example.
5. **Who did better.**
   - Size works like beta: large regionals fell more into 10/14 and rose more after it.
   - Fintech, banking-as-a-service and specialty lenders lagged.
   - The rally was broad: the top 10 contributors supplied 26% of it, and 67% of stocks beat KBWB.
6. **Fundamentals support the year's gains, not the recent rally.**
   - YTD returns track NIM and ROA improvement in the June call reports.
   - The 63-day and rally windows mostly don't.
   - Q3 results in a predetermined 17-bank size sample (16 reported) are mixed:
     - NIMs mostly up.
     - Deposit costs turning up after the September hike.
     - Credit drifting slightly worse.
     - Tangible book value down at 7 of 12 as bond losses grew.
     - 5 banks took losses to reposition their balance sheets.
7. **Hypothesis scorecard.**
   - **Broad market rotation:** weak.
   - **Interest-rate relief:** best-supported, but partial (~1.6 of 5 points in the rally), and HY spreads *widened* during the rally.
   - **Improving fundamentals:** true for the year to date, not shown for the late-October move.

**Implication:** investors are partly paying more for the same rate risk. If the December hike the market expects pushes yields back up, the same sensitivity works in reverse.

# 2. Data, sources and definitions

- **KRE holdings:** State Street daily holdings file, as of 30-Oct-2026 (167 stocks plus cash). <https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-kre.xlsx>
- **KBWB holdings:** 24 stocks — WFC JPM GS MS BAC USB TFC C COF FITB PNC MTB HBAN BNY NTRS STT CFG RF KEY EWBC PNFP FHN ZION WAL.
  - Source: stockanalysis.com/Finnhub list dated 10/16/2026, because Invesco's own file was blocked from this environment (aggregator, not primary).
  - 10 stocks are in both ETFs. **KeyCorp and Fifth Third are in KBWB but not in KRE's 10/30 file** (why was not checked).
- **Prices:** Yahoo Finance daily adjusted closes (dividend-adjusted).
- **Bank fundamentals:** FDIC BankFind call-report API, 6/30/2025 and 6/30/2026. 9/30/2026 data was not loaded yet.
  - Each ticker = sum of all its bank charters (e.g., Wintrust = 16 banks).
  - Ratios are computed from summed dollars. Some percentage ratios are asset-weighted.
- **Q3 2026:** company earnings releases — SEC 8-K Exhibit 99.1 for 14 banks; GlobeNewswire for TowneBank and Preferred Bank (FDIC filers).
- **Rates:** Treasury daily par yield curve; FRED BAMLH0A0HYM2 (ICE BofA US high-yield OAS).
- **Windows:**
  - "63d" = close 8/3 → close 10/30.
  - "Selloff" = 8/3 → 10/14 (KRE's low since Sept).
  - "Rally" = 10/14 → 10/30.
  - The breakpoint is chosen from the outcome, so treat the split as descriptive.
- **Pre-window betas:** estimated 8/1/2025–7/31/2026 so they don't use the test window.
- **KRE replication:** using 10/30 weights gives −5.3% vs KRE's actual −6.0% over 63d (weight drift and the September rebalance).

# 3. Study 1 — ETF-level decoupling

## 3.1 Returns by window (%)

|      |   8/3→10/30 (63d) |   8/3→10/14 |   10/14→10/30 |   YTD |   1 year |
|:-----|------------------:|------------:|--------------:|------:|---------:|
| KRE  |              -6.0 |       -10.5 |           5.1 |  13.0 |     23.3 |
| KBWB |              -8.4 |       -11.5 |           3.4 |   6.6 |     18.5 |
| IWM  |              -5.5 |        -8.1 |           2.9 |  14.2 |     14.3 |
| RSP  |               0.9 |        -1.9 |           2.9 |  15.3 |     17.8 |
| SPY  |              -0.0 |         1.8 |          -1.8 |  11.7 |     11.1 |
| IWN  |              -4.0 |        -7.1 |           3.3 |  19.7 |     22.5 |
| XLF  |              -1.2 |        -4.6 |           3.7 |   4.4 |     10.2 |
| KBE  |              -6.3 |       -10.9 |           5.1 |  10.1 |     19.1 |

63-day annualized volatility (%): KRE 15.6, KBWB 16.4, IWM 13.7, RSP 10.1, SPY 10.5, IWN 11.2, XLF 12.5, KBE 15.1.

## 3.2 How unusual is the correlation?

| KRE vs                 |   63d corr 10/30 |   hist. percentile |   hist. median |
|:-----------------------|-----------------:|-------------------:|---------------:|
| KBWB                   |            0.719 |              1.509 |          0.940 |
| KBWB regionals 12 (EW) |            0.894 |              0.081 |          0.972 |
| KBWB big 12 (EW)       |            0.616 |              1.805 |          0.885 |
| JPM/BAC/WFC/C          |            0.541 |              1.482 |          0.838 |
| GS/MS/BNY/STT/NTRS     |            0.465 |              2.290 |          0.823 |
| IWM                    |            0.501 |              2.937 |          0.789 |
| SPY                    |            0.219 |              1.644 |          0.665 |

*Percentile = share of historical 63-day windows since 2012 with a lower correlation.*

**Correlation matrix, last 63 sessions:**

|      |   KRE |   KBWB |   IWM |   RSP |   SPY |   IWN |   XLF |   KBE |
|:-----|------:|-------:|------:|------:|------:|------:|------:|------:|
| KRE  |  1.00 |   0.72 |  0.50 |  0.55 |  0.22 |  0.70 |  0.64 |  0.99 |
| KBWB |  0.72 |   1.00 |  0.54 |  0.59 |  0.53 |  0.59 |  0.82 |  0.76 |
| IWM  |  0.50 |   0.54 |  1.00 |  0.77 |  0.73 |  0.92 |  0.39 |  0.53 |
| RSP  |  0.55 |   0.59 |  0.77 |  1.00 |  0.64 |  0.83 |  0.72 |  0.62 |
| SPY  |  0.22 |   0.53 |  0.73 |  0.64 |  1.00 |  0.58 |  0.39 |  0.26 |
| IWN  |  0.70 |   0.59 |  0.92 |  0.83 |  0.58 |  1.00 |  0.53 |  0.72 |
| XLF  |  0.64 |   0.82 |  0.39 |  0.72 |  0.39 |  0.53 |  1.00 |  0.71 |
| KBE  |  0.99 |   0.76 |  0.53 |  0.62 |  0.26 |  0.72 |  0.71 |  1.00 |

**KRE–KBWB 63-day correlation by year:**

|   year |   min |   median |   max |
|-------:|------:|---------:|------:|
|   2012 | 0.832 |    0.917 | 0.954 |
|   2013 | 0.844 |    0.883 | 0.921 |
|   2014 | 0.827 |    0.874 | 0.916 |
|   2015 | 0.855 |    0.929 | 0.956 |
|   2016 | 0.938 |    0.974 | 0.989 |
|   2017 | 0.920 |    0.954 | 0.969 |
|   2018 | 0.803 |    0.925 | 0.961 |
|   2019 | 0.924 |    0.958 | 0.977 |
|   2020 | 0.945 |    0.980 | 0.991 |
|   2021 | 0.902 |    0.954 | 0.982 |
|   2022 | 0.921 |    0.946 | 0.957 |
|   2023 | 0.899 |    0.943 | 0.971 |
|   2024 | 0.845 |    0.891 | 0.976 |
|   2025 | 0.833 |    0.910 | 0.975 |
|   2026 | 0.632 |    0.814 | 0.926 |

**Episodes with KRE–KBWB correlation below 0.80** (gaps over 10 days split episodes):

| start      | end        |   min_corr |   days |
|:-----------|:-----------|-----------:|-------:|
| 2026-01-21 | 2026-01-22 |      0.793 |      2 |
| 2026-02-19 | 2026-02-20 |      0.790 |      2 |
| 2026-07-07 | 2026-10-30 |      0.632 |     81 |

## 3.3 ETF construction vs. a genuine regional-bank move

Correlation of portfolios built from KRE's current stocks with KBWB, measured against their own 5-year history:

| portfolio                       |   63d corr w/ KBWB |   pct (5y) |   median (5y) |   63d return |   10/14→10/30 |
|:--------------------------------|-------------------:|-----------:|--------------:|-------------:|--------------:|
| KRE names, size Q1 (smallest)   |              0.637 |      7.946 |         0.816 |       -3.300 |         3.500 |
| size Q2                         |              0.632 |      6.255 |         0.822 |       -3.900 |         3.500 |
| size Q3                         |              0.598 |      4.396 |         0.837 |       -5.200 |         4.200 |
| size Q4                         |              0.633 |      3.128 |         0.861 |       -5.600 |         5.500 |
| size Q5 (largest)               |              0.797 |      5.156 |         0.928 |       -6.000 |         5.900 |
| All 167 KRE names, equal-weight |              0.679 |      5.495 |         0.866 |       -4.800 |         4.500 |
| All 167 KRE names, cap-weight   |              0.797 |      6.171 |         0.929 |       -5.800 |         5.200 |
| KRE replica (10/30 weights)     |              0.708 |      5.325 |         0.887 |       -5.300 |         5.100 |
| KRE names NOT in KBWB (EW)      |              0.655 |      5.410 |         0.856 |       -4.600 |         4.500 |
| 10 names in both ETFs (EW)      |              0.888 |     12.595 |         0.948 |       -7.300 |         5.100 |
| KRE (actual)                    |              0.719 |      4.734 |         0.927 |       -6.000 |         5.100 |
| IWM                             |              0.540 |      3.719 |         0.776 |       -5.500 |         2.900 |

**Reading:**
- Equal weighting (a small-bank tilt) lowers the *level* of the correlation.
- Every construction — cap-weight, any size quintile, stocks outside KBWB — is at its own 3rd–13th percentile.
- The average pairwise correlation among the 167 KRE stocks is 0.643, ~35th percentile of 5 years (median 0.69). The regional group is cohesive. It is its link to big banks and the market that broke.

## 3.4 The divergence is concentrated in a few days

The 5 largest days account for **44%** of the summed squared daily KRE–KBWB gap over 63 sessions, and the top 10 for **62%**. Daily % moves:

|            |   KRE |   KBWB |   gap |   IWM |   SPY |   BAC |   JPM |   GS |   MS |
|:-----------|------:|-------:|------:|------:|------:|------:|------:|-----:|-----:|
| 2026-10-22 |   2.5 |    0.2 |   2.4 |   0.1 |  -1.2 |   0.6 |   0.4 | -1.5 | -1.6 |
| 2026-09-14 |   0.3 |   -1.9 |   2.2 |  -0.3 |  -0.4 |  -5.1 |  -1.7 | -4.0 | -3.6 |
| 2026-08-20 |  -0.4 |   -1.8 |   1.4 |  -1.3 |  -0.8 |  -2.1 |  -1.6 | -1.9 | -3.2 |
| 2026-10-28 |  -0.6 |    0.6 |  -1.3 |   0.4 |   0.3 |   0.3 |   1.0 |  1.5 |  1.7 |
| 2026-09-21 |  -0.5 |    0.8 |  -1.3 |   0.5 |   1.6 |   0.4 |   0.7 |  1.8 |  1.7 |
| 2026-10-09 |  -0.8 |    0.4 |  -1.2 |   0.5 |   0.6 |   1.3 |   0.5 |  1.4 |  1.4 |
| 2026-09-22 |  -1.1 |   -2.3 |   1.2 |   0.6 |  -0.0 |  -3.0 |  -3.4 | -1.0 | -2.9 |
| 2026-10-21 |   0.0 |    1.1 |  -1.1 |   0.3 |   0.5 |   0.3 |  -0.0 |  2.3 |  3.7 |
| 2026-09-16 |  -1.8 |   -2.9 |   1.1 |  -0.4 |  -0.4 |  -2.7 |  -1.0 | -4.0 | -1.9 |
| 2026-08-05 |  -0.6 |    0.3 |  -1.0 |  -0.6 |  -0.2 |   0.6 |   0.5 |  0.7 |  0.6 |
| 2026-10-01 |   0.7 |   -0.2 |   0.9 |   0.4 |   0.2 |  -1.3 |   0.7 | -0.4 | -0.0 |
| 2026-08-25 |  -0.6 |    0.3 |  -0.9 |   0.4 |   0.3 |   0.2 |   0.1 |  2.2 |  1.3 |

- **9/14:** Bank of America's CEO, at the Barclays conference, guided Q3 investment-banking fees to $1.6–1.8B vs $2.0B a year earlier. BAC fell 5.1%, GS −4%, MS −3%; KRE was +0.3%.
- **10/22:** the AI-stock rout (Meta), French fiscal stress and Mideast tensions drove Treasuries' biggest one-day rally in years. 10-year −17bp, 2-year −16bp; KRE +2.5%.

## 3.5 Rates, credit spreads and the rate regime

**Yields and HY spread at key dates (%):**

|            |   3m bill |   2y |   10y |   HY OAS |   2s10s |
|:-----------|----------:|-----:|------:|---------:|--------:|
| 2026-06-30 |      3.87 | 4.14 |  4.44 |     2.75 |    0.30 |
| 2026-08-03 |      3.91 | 4.25 |  4.70 |     2.78 |    0.45 |
| 2026-09-15 |      4.11 | 4.67 |  5.00 |     2.76 |    0.33 |
| 2026-09-30 |      4.20 | 4.88 |  5.29 |     3.12 |    0.41 |
| 2026-10-14 |      4.28 | 4.82 |  5.19 |     3.25 |    0.37 |
| 2026-10-22 |      4.22 | 4.65 |  4.96 |     3.40 |    0.31 |
| 2026-10-30 |      4.16 | 4.56 |  4.94 |     3.44 |    0.38 |

**Fed context:**
- The Fed hiked 25bp in September 2026 to 3.75–4.00% and held on 10/28 (vote 10–2; Cook and Hammack wanted a hike).
- Futures price a December hike.

**Daily, 10/14–10/30:**

|            |   KRE % |   KBWB % |   IWM % |   SPY % |   % KRE names up |   Δ2y bp |   Δ10y bp |   HY OAS |
|:-----------|--------:|---------:|--------:|--------:|-----------------:|---------:|----------:|---------:|
| 2026-10-14 |   -0.75 |    -1.48 |   -1.93 |   -1.08 |            10.18 |     3.00 |     -2.00 |     3.25 |
| 2026-10-15 |    1.77 |     1.31 |    1.37 |    0.28 |            99.40 |    -5.00 |     -9.00 |     3.23 |
| 2026-10-16 |    0.09 |     0.20 |   -1.69 |   -1.11 |            73.05 |    -3.00 |     -1.00 |     3.31 |
| 2026-10-19 |   -0.79 |    -1.07 |    0.31 |    0.42 |             2.99 |     3.00 |      6.00 |     3.29 |
| 2026-10-20 |    1.96 |     1.43 |    1.66 |    0.34 |            98.20 |     2.00 |     -3.00 |     3.33 |
| 2026-10-21 |    0.00 |     1.15 |    0.25 |    0.53 |            36.53 |     2.00 |      1.00 |     3.27 |
| 2026-10-22 |    2.53 |     0.16 |    0.07 |   -1.18 |            96.41 |   -16.00 |    -17.00 |     3.40 |
| 2026-10-23 |    0.07 |    -0.75 |   -0.33 |   -0.52 |            52.10 |     4.00 |      4.00 |     3.38 |
| 2026-10-26 |    0.37 |     0.73 |    0.45 |    0.71 |            64.07 |    -1.00 |      0.00 |     3.30 |
| 2026-10-27 |   -0.21 |     0.45 |    1.15 |    0.56 |            34.73 |     2.00 |     -1.00 |     3.18 |
| 2026-10-28 |   -0.65 |     0.63 |    0.40 |    0.34 |            19.76 |    -3.00 |      6.00 |     3.14 |
| 2026-10-29 |    1.04 |     1.05 |    0.97 |   -0.38 |            89.22 |    -6.00 |     -7.00 |     3.26 |
| 2026-10-30 |   -1.17 |    -1.86 |   -1.65 |   -1.77 |             7.78 |    -5.00 |     -4.00 |     3.44 |

**Rolling 63-day regression betas** (KRE or KBWB on SPY and the daily Δ10-year yield in pp; history since 2012):

|                |   latest |    pct |   median |
|:---------------|---------:|-------:|---------:|
| KRE d10y beta  |   -0.061 |  4.258 |    0.070 |
| KBWB d10y beta |   -0.030 |  4.670 |    0.065 |
| KRE SPY beta   |    0.213 |  1.648 |    0.985 |
| KBWB SPY beta  |    0.842 | 21.566 |    1.045 |

**Share of KRE's daily variance explained (R²):**

| KRE explained by   |   R² last 63d |   median R² prior 5y |
|:-------------------|--------------:|---------------------:|
| IWM                |         0.282 |                0.685 |
| SPY                |         0.067 |                0.380 |
| KBWB               |         0.525 |                0.865 |
| KBWB+IWM           |         0.548 |                0.892 |
| KBWB+IWM+d10       |         0.571 |                0.893 |

**63-day factor regressions and decomposition** (sum of daily returns, %):

|                     |   R2 |   beta_mkt |   t_mkt |   beta_d10y (per 1pp) |   t_d10y |   pre: actual |   pre: mkt part |   pre: rates part |   rally: actual |   rally: mkt part |   rally: rates part |
|:--------------------|-----:|-----------:|--------:|----------------------:|---------:|--------------:|----------------:|------------------:|----------------:|------------------:|--------------------:|
| ('KRE', 'SPY+d10')  | 0.17 |       0.28 |    1.58 |                 -0.06 |    -2.80 |        -10.41 |            0.94 |             -2.78 |            5.02 |             -0.49 |                1.58 |
| ('KRE', 'IWM+d10')  | 0.31 |       0.50 |    3.87 |                 -0.04 |    -1.62 |        -10.41 |           -3.14 |             -1.57 |            5.02 |              1.49 |                0.89 |
| ('KBWB', 'SPY+d10') | 0.32 |       0.78 |    4.66 |                 -0.03 |    -1.42 |        -11.33 |            2.64 |             -1.35 |            3.43 |             -1.38 |                0.77 |
| ('KBWB', 'IWM+d10') | 0.31 |       0.63 |    4.62 |                 -0.01 |    -0.34 |        -11.33 |           -3.94 |             -0.34 |            3.43 |              1.87 |                0.20 |

**Reading:**
- Rates explain about +1.6 points of the +5.0-point rally and about −2.8 of the −10.4-point selloff.
- Most of KRE's path is a regional-bank common factor that neither the market nor rates explain.

## 3.6 Volatility regime

KRE–KBWB correlation by KRE 63-day volatility quintile (2012–2026):

| bin         |   days | vol_range   |   mean_corr |   min_corr |   share_below_075 |
|:------------|-------:|:------------|------------:|-----------:|------------------:|
| lowest vol  |    742 | 11.7–17.5%  |       0.879 |      0.632 |             5.526 |
| 2           |    741 | 17.5–21.9%  |       0.913 |      0.687 |             3.374 |
| 3           |    742 | 21.9–24.8%  |       0.927 |      0.810 |             0.000 |
| 4           |    741 | 24.8–29.9%  |       0.932 |      0.840 |             0.000 |
| highest vol |    742 | 29.9–96.6%  |       0.961 |      0.832 |             0.000 |

KRE's current 63-day volatility of 15.6% is near the 9th percentile. Low volatility explains part of the low correlation, but even in the lowest-volatility quintile only 5.5% of days fell below 0.75.

# 4. Study 1 — which regional banks moved (cross-section of 167)

**Breadth:**
- 63d: 78% beat KBWB; 19% had positive returns.
- Rally: 67% beat KBWB; the top 10 contributors were 26% of KRE's rally.

All returns and ratios below are medians, in %, except n, assets ($bn), betas, CET1, P/B and P/E.

## 4.1 By size (FDIC June 2026 assets, quintiles)

| sizeq    |     n |   assets_med_bn |   ret_63d |   ret_pre |   ret_rally |   ret_ytd |   beat_KBWB_63d |   beat_KBWB_rally |   beta_kbwb |   dNIM_yoy_pp |   NPL |   NCO |   CRE_conc |   unreal_loss_T1 |   CET1 |   P_B |   fwd_PE |
|:---------|------:|----------------:|----------:|----------:|------------:|----------:|----------------:|------------------:|------------:|--------------:|------:|------:|-----------:|-----------------:|-------:|------:|---------:|
| Q1 small | 34.00 |            4.72 |     -2.78 |     -6.59 |        4.29 |     23.29 |           82.35 |             58.82 |        0.60 |          0.20 |  0.56 |  0.06 |       2.67 |            -6.46 |  13.13 |  1.41 |    10.49 |
| Q2       | 33.00 |            7.31 |     -3.23 |     -6.32 |        3.82 |     25.26 |           78.79 |             63.64 |        0.66 |          0.21 |  0.62 |  0.09 |       2.61 |            -8.49 |  12.72 |  1.38 |    10.10 |
| Q3       | 33.00 |           12.18 |     -2.93 |     -7.59 |        3.98 |     24.86 |           75.76 |             60.61 |        0.66 |          0.15 |  0.89 |  0.15 |       2.28 |            -9.50 |  12.98 |  1.36 |    10.95 |
| Q4       | 33.00 |           22.62 |     -6.14 |     -9.83 |        5.08 |     15.45 |           72.73 |             75.76 |        0.72 |          0.16 |  0.57 |  0.11 |       2.38 |            -9.63 |  12.95 |  1.26 |    10.69 |
| Q5 large | 34.00 |           65.80 |     -5.75 |    -11.60 |        5.81 |     12.75 |           82.35 |             76.47 |        0.87 |          0.06 |  0.57 |  0.23 |       1.68 |           -10.84 |  12.19 |  1.22 |    10.08 |

## 4.2 By business model

Classification is mine, from FDIC loan mix:
- **Fintech / BaaS / specialty:** a hand list (TBBK, CASH, CCB, LOB, TFIN, AX, CUBI, MCB, ESQ, NBN).
- **Thrift / residential:** 1–4 family loans >45% of loans.
- **CRE-heavy:** CRE >300% of total capital.
- **C&I-heavy:** C&I >30% of loans.

| model                          |      n |   assets_med_bn |   ret_63d |   ret_pre |   ret_rally |   ret_ytd |   beat_KBWB_63d |   beat_KBWB_rally |   beta_kbwb |   dNIM_yoy_pp |   NPL |   NCO |   CRE_conc |   unreal_loss_T1 |   CET1 |   P_B |   fwd_PE |
|:-------------------------------|-------:|----------------:|----------:|----------:|------------:|----------:|----------------:|------------------:|------------:|--------------:|------:|------:|-----------:|-----------------:|-------:|------:|---------:|
| C&I-heavy (>30% loans)         |  11.00 |           22.35 |     -6.14 |    -10.33 |        5.07 |     15.50 |           81.82 |             81.82 |        0.72 |          0.06 |  0.63 |  0.17 |       1.53 |            -9.96 |  12.29 |  1.38 |    10.58 |
| CRE-heavy (>300% of capital)   |  31.00 |            8.79 |     -3.08 |     -7.69 |        5.08 |     23.86 |           77.42 |             64.52 |        0.65 |          0.27 |  0.68 |  0.07 |       3.40 |            -6.14 |  12.95 |  1.22 |    10.27 |
| diversified community/regional | 106.00 |           15.31 |     -4.13 |     -8.27 |        4.52 |     19.93 |           81.13 |             66.98 |        0.68 |          0.14 |  0.62 |  0.12 |       2.35 |           -10.44 |  12.73 |  1.30 |    10.49 |
| fintech/BaaS/specialty         |  10.00 |            8.13 |     -9.54 |    -12.68 |        4.85 |      5.58 |           50.00 |             60.00 |        0.84 |         -0.17 |  1.12 |  0.58 |       2.04 |            -2.94 |  12.48 |  1.65 |     8.66 |
| thrift/residential             |   9.00 |            6.94 |     -2.54 |     -6.76 |        4.44 |     28.55 |           77.78 |             66.67 |        0.65 |          0.16 |  0.30 |  0.04 |       1.93 |           -12.23 |  13.92 |  1.55 |    11.11 |

## 4.3 By region (headquarters state of the lead bank)

| region         |     n |   assets_med_bn |   ret_63d |   ret_pre |   ret_rally |   ret_ytd |   beat_KBWB_63d |   beat_KBWB_rally |   beta_kbwb |   dNIM_yoy_pp |   NPL |   NCO |   CRE_conc |   unreal_loss_T1 |   CET1 |   P_B |   fwd_PE |
|:---------------|------:|----------------:|----------:|----------:|------------:|----------:|----------------:|------------------:|------------:|--------------:|------:|------:|-----------:|-----------------:|-------:|------:|---------:|
| Hawaii         |  3.00 |           23.65 |     -9.18 |    -12.21 |        6.03 |      4.85 |           33.33 |            100.00 |        0.72 |          0.12 |  0.30 |  0.12 |       1.84 |           -25.53 |  13.44 |  1.71 |    10.62 |
| Midwest/Plains | 38.00 |            9.23 |     -4.19 |     -8.31 |        4.61 |     24.73 |           86.84 |             71.05 |        0.65 |          0.10 |  0.67 |  0.16 |       2.09 |            -9.73 |  12.61 |  1.42 |    10.27 |
| Northeast      | 45.00 |            9.41 |     -2.79 |     -7.54 |        5.10 |     26.67 |           88.89 |             75.56 |        0.68 |          0.19 |  0.64 |  0.15 |       2.90 |            -7.41 |  12.73 |  1.30 |    10.15 |
| Puerto Rico    |  3.00 |           19.22 |     -9.05 |     -7.24 |       -1.79 |     27.83 |           33.33 |              0.00 |        0.87 |          0.23 |  1.59 |  0.83 |       1.07 |           -15.22 |  15.96 |  1.62 |     9.90 |
| Southeast      | 39.00 |           18.34 |     -6.31 |     -8.83 |        4.26 |     15.50 |           71.79 |             56.41 |        0.72 |          0.17 |  0.72 |  0.10 |       2.37 |            -6.63 |  12.43 |  1.29 |    10.70 |
| Texas          | 13.00 |           15.23 |     -6.11 |     -9.71 |        3.46 |      6.89 |           61.54 |             53.85 |        0.67 |          0.06 |  0.55 |  0.09 |       1.71 |           -10.64 |  13.39 |  1.35 |    12.46 |
| West           | 26.00 |           17.79 |     -2.69 |     -9.86 |        5.16 |     13.61 |           76.92 |             73.08 |        0.73 |          0.15 |  0.51 |  0.11 |       2.76 |           -10.44 |  12.82 |  1.25 |    10.41 |

## 4.4 Best and worst performers

**Top 12, 63d:**

|      | name                         |   assets $bn | region         | model                          |   63d % |   8/3→10/14 % |   rally % |   YTD % |   NPL % |   ΔNIM pp |
|:-----|:-----------------------------|-------------:|:---------------|:-------------------------------|--------:|--------------:|----------:|--------:|--------:|----------:|
| EGBN | EAGLE BANCORP INC            |         9.62 | Northeast      | diversified community/regional |   19.50 |         -1.40 |     21.20 |   55.50 |    2.10 |      0.15 |
| CBC  | CENTRAL BANCOMPANY           |        20.31 | Midwest/Plains | diversified community/regional |    8.80 |         -1.40 |     10.30 |   50.80 |    0.50 |      0.07 |
| FBIZ | FIRST BUSINESS FINANCIAL SER |         4.41 | Midwest/Plains | CRE-heavy (>300% of capital)   |    4.90 |         -3.60 |      8.80 |   41.20 |    1.10 |      0.08 |
| COFS | CHOICEONE FINANCIAL SVCS INC |         4.45 | Midwest/Plains | diversified community/regional |    4.50 |         -5.20 |     10.30 |   23.50 |    1.00 |     -0.12 |
| CUBI | CUSTOMERS BANCORP INC        |        26.50 | Northeast      | fintech/BaaS/specialty         |    4.50 |         -8.90 |     14.70 |   15.10 |    0.30 |     -0.18 |
| SBSI | SOUTHSIDE BANCSHARES INC     |         8.76 | Texas          | diversified community/regional |    4.30 |         -6.40 |     11.40 |   14.60 |    0.20 |      0.07 |
| CLBK | COLUMBIA FINANCIAL INC       |        12.17 | Northeast      | CRE-heavy (>300% of capital)   |    4.20 |          2.30 |      1.80 |   57.00 |    0.50 |      0.15 |
| MCB  | METROPOLITAN BANK HOLDING CO |         8.86 | Northeast      | fintech/BaaS/specialty         |    3.50 |         -6.80 |     11.10 |   26.70 |    0.90 |      0.28 |
| UCB  | UNITED COMMUNITY BANKS/GA    |        28.99 | Southeast      | diversified community/regional |    3.30 |         -6.80 |     10.80 |   20.40 |    0.50 |      0.19 |
| HBT  | HBT FINANCIAL INC/DE         |         6.72 | Midwest/Plains | diversified community/regional |    2.80 |         -1.70 |      4.60 |   44.60 |    0.20 |      0.20 |
| HIFS | HINGHAM INSTITUTION FOR SVGS |         4.56 | Northeast      | CRE-heavy (>300% of capital)   |    2.30 |         -2.60 |      5.10 |    7.00 |    0.80 |      0.50 |
| ACNB | ACNB CORP                    |         3.30 | Northeast      | diversified community/regional |    2.00 |         -2.50 |      4.60 |   39.50 |    0.40 |      0.37 |

**Bottom 12, 63d:**

|      | name                      |   assets $bn | region         | model                          |   63d % |   8/3→10/14 % |   rally % |   YTD % |   NPL % |   ΔNIM pp |
|:-----|:--------------------------|-------------:|:---------------|:-------------------------------|--------:|--------------:|----------:|--------:|--------:|----------:|
| TBBK | BANCORP INC/THE           |         9.21 | Midwest/Plains | fintech/BaaS/specialty         |  -34.20 |        -31.80 |     -3.40 |  -30.80 |    1.30 |     -0.65 |
| FLG  | FLAGSTAR BANK NA          |        87.71 | Northeast      | CRE-heavy (>300% of capital)   |  -26.00 |        -21.80 |     -5.40 |  -16.30 |    5.00 |      0.19 |
| LOB  | LIVE OAK BANCSHARES INC   |        15.96 | Southeast      | fintech/BaaS/specialty         |  -21.20 |        -21.30 |      0.10 |    0.60 |    4.00 |     -0.01 |
| WAFD | WAFD INC                  |        27.58 | West           | CRE-heavy (>300% of capital)   |  -20.90 |        -22.00 |      1.50 |   -6.20 |    0.60 |      0.18 |
| TFIN | TRIUMPH FINANCIAL INC     |         7.40 | Texas          | fintech/BaaS/specialty         |  -19.00 |        -20.10 |      1.40 |   -0.80 |    1.70 |     -0.17 |
| CARE | CARTER BANKSHARES INC     |         4.80 | Southeast      | CRE-heavy (>300% of capital)   |  -17.90 |        -15.00 |     -3.40 |   48.50 |    1.00 |      0.60 |
| CASH | PATHWARD FINANCIAL INC    |         7.31 | Midwest/Plains | fintech/BaaS/specialty         |  -17.00 |        -22.00 |      6.50 |    6.30 |    5.30 |     -0.79 |
| HBCP | HOME BANCORP INC          |         3.60 | Southeast      | diversified community/regional |  -15.90 |         -9.50 |     -7.20 |    6.40 |    1.00 |      0.18 |
| PRK  | PARK NATIONAL CORP        |        12.61 | Midwest/Plains | diversified community/regional |  -14.90 |        -14.90 |      0.00 |   17.50 |    0.90 |     -0.14 |
| FFIN | FIRST FINL BANKSHARES INC |        15.23 | Texas          | diversified community/regional |  -13.10 |        -12.20 |     -1.00 |    4.50 |    0.80 |      0.12 |
| AX   | AXOS FINANCIAL INC        |        28.87 | West           | fintech/BaaS/specialty         |  -12.80 |        -16.50 |      4.40 |    4.90 |    0.40 |     -0.17 |
| NBHC | NATIONAL BANK HOLD CL A   |        12.54 | West           | diversified community/regional |  -12.70 |        -13.40 |      0.80 |    0.80 |    0.60 |      0.08 |

**Top 12, rally (10/14→10/30):**

|      | name                         |   assets $bn | region    | model                          |   63d % |   8/3→10/14 % |   rally % |   YTD % |   NPL % |   ΔNIM pp |
|:-----|:-----------------------------|-------------:|:----------|:-------------------------------|--------:|--------------:|----------:|--------:|--------:|----------:|
| EGBN | EAGLE BANCORP INC            |         9.62 | Northeast | diversified community/regional |   19.50 |         -1.40 |     21.20 |   55.50 |    2.10 |      0.15 |
| TCBI | TEXAS CAPITAL BANCSHARES INC |        33.62 | Texas     | C&I-heavy (>30% loans)         |    0.70 |        -12.40 |     15.00 |   12.90 |    0.50 |     -0.08 |
| CUBI | CUSTOMERS BANCORP INC        |        26.50 | Northeast | fintech/BaaS/specialty         |    4.50 |         -8.90 |     14.70 |   15.10 |    0.30 |     -0.18 |
| VLY  | VALLEY NATIONAL BANCORP      |        66.23 | Northeast | CRE-heavy (>300% of capital)   |   -1.70 |        -13.70 |     13.90 |   24.10 |    0.90 |      0.20 |
| OCFC | OCEANFIRST FINANCIAL CORP    |        23.17 | Northeast | CRE-heavy (>300% of capital)   |   -7.80 |        -19.10 |     13.90 |    3.20 |    0.70 |     -0.09 |
| GBCI | GLACIER BANCORP INC          |        31.58 | West      | diversified community/regional |   -3.00 |        -14.70 |     13.70 |   12.60 |    0.40 |      0.67 |
| BBT  | BEACON FINANCIAL CORP        |        22.20 | Northeast | CRE-heavy (>300% of capital)   |   -3.10 |        -14.20 |     13.00 |   19.90 |    0.90 |      0.44 |
| OZK  | BANK OZK                     |        41.70 | Southeast | diversified community/regional |   -1.00 |        -12.20 |     12.70 |   14.50 |    0.90 |     -0.16 |
| SBSI | SOUTHSIDE BANCSHARES INC     |         8.76 | Texas     | diversified community/regional |    4.30 |         -6.40 |     11.40 |   14.60 |    0.20 |      0.07 |
| MCB  | METROPOLITAN BANK HOLDING CO |         8.86 | Northeast | fintech/BaaS/specialty         |    3.50 |         -6.80 |     11.10 |   26.70 |    0.90 |      0.28 |
| UCB  | UNITED COMMUNITY BANKS/GA    |        28.99 | Southeast | diversified community/regional |    3.30 |         -6.80 |     10.80 |   20.40 |    0.50 |      0.19 |
| DCOM | DIME COMMERCIAL BANCSHARES I |        15.03 | Northeast | CRE-heavy (>300% of capital)   |    2.00 |         -7.70 |     10.50 |   42.70 |    0.60 |      0.28 |

**Bottom 12, rally:**

|      | name                        |   assets $bn | region         | model                          |   63d % |   8/3→10/14 % |   rally % |   YTD % |   NPL % |   ΔNIM pp |
|:-----|:----------------------------|-------------:|:---------------|:-------------------------------|--------:|--------------:|----------:|--------:|--------:|----------:|
| HBCP | HOME BANCORP INC            |         3.60 | Southeast      | diversified community/regional |  -15.90 |         -9.50 |     -7.20 |    6.40 |    1.00 |      0.18 |
| CTBI | COMMUNITY TRUST BANCORP INC |         6.95 | Southeast      | diversified community/regional |  -11.80 |         -5.50 |     -6.60 |   25.30 |    0.60 |      0.13 |
| FLG  | FLAGSTAR BANK NA            |        87.71 | Northeast      | CRE-heavy (>300% of capital)   |  -26.00 |        -21.80 |     -5.40 |  -16.30 |    5.00 |      0.19 |
| MPB  | MID PENN BANCORP INC        |         7.04 | Northeast      | CRE-heavy (>300% of capital)   |  -11.40 |         -7.30 |     -4.40 |   11.70 |    0.50 |      0.51 |
| CARE | CARTER BANKSHARES INC       |         4.80 | Southeast      | CRE-heavy (>300% of capital)   |  -17.90 |        -15.00 |     -3.40 |   48.50 |    1.00 |      0.60 |
| TBBK | BANCORP INC/THE             |         9.21 | Midwest/Plains | fintech/BaaS/specialty         |  -34.20 |        -31.80 |     -3.40 |  -30.80 |    1.30 |     -0.65 |
| TCBX | THIRD COAST BANCSHARES INC  |         6.73 | Texas          | C&I-heavy (>30% loans)         |   -9.30 |         -6.30 |     -3.20 |    4.90 |    0.50 |     -0.41 |
| SMBK | SMARTFINANCIAL INC          |         6.11 | Southeast      | diversified community/regional |   -8.90 |         -6.40 |     -2.60 |   31.80 |    0.20 |      0.30 |
| UVSP | UNIVEST FINANCIAL CORP      |         8.17 | Northeast      | diversified community/regional |  -10.60 |         -8.80 |     -2.00 |   23.10 |    0.60 |      0.23 |
| FBP  | FIRST BANCORP PUERTO RICO   |        19.22 | Puerto Rico    | diversified community/regional |   -9.00 |         -7.20 |     -1.90 |   29.40 |    0.90 |      0.24 |
| OFG  | OFG BANCORP                 |        12.04 | Puerto Rico    | diversified community/regional |   -5.10 |         -3.40 |     -1.80 |   24.90 |    1.60 |      0.14 |
| NRIM | NORTHRIM BANCORP INC        |         3.40 | West           | diversified community/regional |  -11.90 |        -10.90 |     -1.10 |   -8.60 |    0.90 |      0.28 |

# 5. Study 2 — do fundamentals explain the moves?

## 5.1 FDIC June baseline (167 banks): Jun-2025 vs Jun-2026

| metric                                  |   median Jun-25 |   median Jun-26 |   p25 Jun-25 |   p25 Jun-26 |   p75 Jun-25 |   p75 Jun-26 |
|:----------------------------------------|----------------:|----------------:|-------------:|-------------:|-------------:|-------------:|
| NIM, Q2 (%)                             |            3.61 |            3.83 |         3.22 |         3.50 |         3.99 |         4.07 |
| ROA, Q2 (%)                             |            1.20 |            1.39 |         0.98 |         1.13 |         1.50 |         1.62 |
| Cost of deposits, H1 annualized (%)     |            1.95 |            1.75 |         1.57 |         1.40 |         2.37 |         2.08 |
| Net charge-offs, H1 annualized (%)      |            0.14 |            0.12 |         0.05 |         0.05 |         0.28 |         0.26 |
| Noncurrent loans / loans (%)            |            0.58 |            0.63 |         0.38 |         0.45 |         0.91 |         0.97 |
| Unrealized securities loss / Tier 1 (%) |          -11.72 |           -8.50 |       -18.54 |       -13.86 |        -6.29 |        -4.42 |

**Levels, June 2026 (median):**

|                                                          |   median |
|:---------------------------------------------------------|---------:|
| Uninsured deposits / deposits (%)                        |     37.8 |
| CRE (constr+multifam+non-owner-occ) / total capital (%)  |    237.4 |
| Loans / deposits (%)                                     |     89.2 |
| CET1 ratio (%)                                           |     12.7 |
| Leverage ratio (%)                                       |     10.3 |
| Deposit growth YoY (%)                                   |      4.7 |
| Asset growth YoY (%)                                     |      4.5 |
| Banks flagged merger-affected (asset growth >25%), count |     22.0 |

**Reading:**
- Before Q3, margins and profitability had genuinely improved and securities losses had shrunk.
- Credit was flat to slightly worse.

## 5.2 Spearman rank correlations: characteristic vs. return (n=167; |ρ| > ~0.15 ≈ p < 0.05)

|                              |   63d |   8/3→10/14 |   10/14→10/30 |   YTD |
|:-----------------------------|------:|------------:|--------------:|------:|
| log assets                   | -0.23 |       -0.48 |          0.23 | -0.35 |
| beta to KBWB (pre)           | -0.18 |       -0.39 |          0.23 | -0.34 |
| beta to IWM (pre)            |  0.14 |        0.04 |          0.08 |  0.05 |
| beta to Δ10y (pre)           | -0.17 |       -0.25 |          0.01 | -0.30 |
| uninsured deposit share      |  0.02 |       -0.04 |          0.11 | -0.02 |
| cost of deposits Q2          |  0.03 |        0.03 |          0.01 | -0.04 |
| NIM Q2                       | -0.00 |        0.16 |         -0.19 |  0.05 |
| ΔNIM YoY                     |  0.09 |        0.12 |         -0.01 |  0.24 |
| ROA Q2                       | -0.00 |        0.11 |         -0.08 |  0.05 |
| ΔROA YoY                     | -0.02 |       -0.01 |          0.05 |  0.18 |
| NCO H1                       | -0.06 |       -0.18 |          0.12 | -0.14 |
| ΔNCO YoY                     |  0.09 |        0.04 |          0.12 | -0.10 |
| noncurrent loans             | -0.24 |       -0.19 |         -0.14 | -0.17 |
| Δnoncurrent YoY              |  0.00 |       -0.04 |          0.07 | -0.11 |
| CRE / total capital          |  0.24 |        0.17 |          0.09 |  0.17 |
| loans / deposits             | -0.03 |        0.04 |         -0.10 |  0.13 |
| unrealized loss (AFS+HTM)/T1 | -0.08 |       -0.01 |         -0.16 | -0.11 |
| HTM unrealized loss/T1       | -0.06 |        0.10 |         -0.23 |  0.05 |
| securities / assets          | -0.01 |       -0.07 |          0.11 | -0.02 |
| CET1                         |  0.17 |        0.21 |         -0.08 |  0.17 |
| deposit growth YoY           |  0.08 |        0.05 |          0.05 | -0.11 |
| price / book                 |  0.05 |        0.14 |         -0.06 |  0.21 |
| forward P/E                  |  0.11 |        0.16 |         -0.06 |  0.24 |

## 5.3 Multivariate regression

Return (pp) on standardized characteristics; coefficient = pp per 1 standard deviation; HC3 robust t-statistics.

|                              |   ('8/3→10/14', 'coef') |   ('8/3→10/14', 't') |   ('10/14→10/30', 'coef') |   ('10/14→10/30', 't') |   ('63d', 'coef') |   ('63d', 't') |
|:-----------------------------|------------------------:|---------------------:|--------------------------:|-----------------------:|------------------:|---------------:|
| R²                           |                    0.39 |               nan    |                      0.25 |                 nan    |              0.28 |         nan    |
| beta to IWM (pre)            |                   -0.41 |                -0.69 |                      0.71 |                   1.48 |              0.25 |           0.29 |
| beta to KBWB (pre)           |                   -0.98 |                -1.72 |                      0.72 |                   1.21 |             -0.35 |          -0.37 |
| CET1                         |                    0.18 |                 0.58 |                      0.52 |                   1.04 |              0.69 |           1.28 |
| cost of deposits Q2          |                    1.15 |                 1.68 |                      0.32 |                   0.52 |              1.46 |           1.37 |
| const                        |                   -8.89 |               -26.19 |                      4.51 |                  13.88 |             -4.78 |          -9.76 |
| CRE / total capital          |                   -0.17 |                -0.38 |                      0.27 |                   0.64 |              0.08 |           0.11 |
| ΔNCO YoY                     |                    0.59 |                 1.35 |                      0.43 |                   1.20 |              0.97 |           1.72 |
| ΔNIM YoY                     |                    0.48 |                 1.16 |                     -0.25 |                  -0.53 |              0.26 |           0.43 |
| Δnoncurrent YoY              |                    0.38 |                 0.48 |                      0.50 |                   1.06 |              0.78 |           0.87 |
| ΔROA YoY                     |                   -0.32 |                -0.46 |                      0.28 |                   0.44 |             -0.04 |          -0.03 |
| deposit growth YoY           |                   -0.53 |                -2.05 |                      1.11 |                   4.75 |              0.40 |           1.07 |
| log assets                   |                   -1.52 |                -2.57 |                      0.67 |                   1.04 |             -0.96 |          -0.98 |
| merger                       |                    0.19 |                 0.44 |                     -0.65 |                  -1.82 |             -0.39 |          -0.70 |
| noncurrent loans             |                   -1.33 |                -2.22 |                     -0.99 |                  -1.47 |             -2.20 |          -2.37 |
| beta to Δ10y (pre)           |                    0.26 |                 0.54 |                     -0.47 |                  -1.08 |             -0.15 |          -0.23 |
| HTM unrealized loss/T1       |                    0.75 |                 1.37 |                     -0.59 |                  -1.40 |              0.22 |           0.26 |
| unrealized loss (AFS+HTM)/T1 |                   -0.88 |                -1.82 |                     -0.38 |                  -0.93 |             -1.25 |          -1.93 |
| uninsured deposit share      |                    0.85 |                 1.79 |                     -0.01 |                  -0.04 |              0.82 |           1.30 |

**Reading:**
- The noncurrent-loan level is the most consistent negative.
- HTM unrealized loss/T1 predicts a *bigger* rally — the only cross-sectional rate-relief evidence.
- June-quarter changes in NIM, ROA, NCO and deposits explain little of the 63d or rally moves, though they do line up with YTD returns.
- Deposit growth's rally coefficient is fragile: it loses significance after winsorizing and dropping merger-affected banks.

## 5.4 Q3 2026: predetermined size-stratified sample

**Rule:** sort the 167 stocks by June-2026 FDIC assets and take ranks 1, 11, 21, …, 161 (17 banks). The rule is mechanical, but it was fixed after the cross-sectional return patterns had been seen.

- **Earnings reaction:** 3-day return around the release date minus KRE.
- **"NPL basis"** differs by bank (NPL, nonaccrual or NPA) as each company reports it.

| ticker   |   assets $bn | release    |   deposits QoQ % |   deposit cost Q3 % |   Δ dep cost bp | dep cost basis     |   NIM Q3 % |   ΔNIM QoQ bp |   ΔNIM YoY bp |   NPL Q3 % |   NPL Q2 % | NPL basis                          |   NCO Q3 % |   NCO Q2 % |   TBV QoQ % |   CET1 Q3 |   CET1 Q2 | repositioning                                               |   3-day earnings reaction vs KRE % |   rally % |   63d % | notes                                                                 |
|:---------|-------------:|:-----------|-----------------:|--------------------:|----------------:|:-------------------|-----------:|--------------:|--------------:|-----------:|-----------:|:-----------------------------------|-----------:|-----------:|------------:|----------:|----------:|:------------------------------------------------------------|-----------------------------------:|----------:|--------:|:----------------------------------------------------------------------|
| TFC      |       548.30 | 2026-10-16 |             0.90 |                1.59 |            3.00 | total              |       3.00 |          2.00 |         -1.00 |       0.40 |       0.51 | NPL/loans                          |       0.77 |       0.50 |       -4.50 |     10.70 |     10.90 | Y: $1.4B AFS loss + RAC loan sale                           |                               0.17 |      7.10 |   -5.10 | NCO incl 39bp RAC; adj EPS +12% YoY                                   |
| FHN      |        84.10 | 2026-10-15 |            -0.50 |                1.88 |           10.00 | total              |       3.48 |         -1.00 |         -7.00 |       0.81 |       0.81 | NPL/loans                          |       0.22 |       0.20 |       -4.70 |     10.30 |     10.50 | Y: ~$4.5B mortgage sale (loss on HFS reclass)               |                              -0.93 |      2.60 |   -9.20 | IB deposit cost 2.45 (+12bp); brokered up                             |
| ASB      |        51.80 | 2026-10-22 |             1.10 |                2.46 |            1.00 | interest-bearing   |       3.20 |          3.00 |         16.00 |       0.50 |       0.41 | nonaccrual/loans                   |       0.19 |       0.25 |             |     10.38 |     10.47 | N                                                           |                               0.92 |      7.00 |   -2.70 | FY guide kept (NII +19-21%); bought back $100M                        |
| TCBI     |        33.60 | 2026-10-21 |            -4.10 |                2.45 |            5.00 | total              |       3.44 |         16.00 |         -3.00 |       0.51 |       0.50 | nonaccrual LHI                     |       0.24 |       0.26 |       -2.50 |     12.20 |     12.10 | N                                                           |                               5.94 |     15.00 |    0.70 | criticized loans +12% QoQ / +48% YoY; AOCI -251M vs -99M              |
| CUBI     |        26.50 | 2026-10-22 |             3.80 |                2.50 |            0.00 | total              |       3.19 |          2.00 |        -27.00 |       0.29 |       0.31 | NPL/loans                          |       0.28 |       0.34 |        0.70 |     12.60 |           | N                                                           |                               8.18 |     14.70 |    4.50 | FY guide raised; Sept NIM run-rate ~3.25                              |
| TOWN     |        22.60 | 2026-10-28 |            -1.40 |                1.51 |           -4.00 | total              |       3.89 |         21.00 |         41.00 |       0.26 |       0.21 | NPL/loans                          |       0.06 |       0.15 |       -1.30 |     12.47 |     12.16 | N                                                           |                              -0.55 |      4.30 |   -4.20 | AFS unrealized loss -187M vs -85M; Dogwood-acquired NPLs              |
| TRMK     |        19.20 | 2026-10-27 |            -0.10 |                1.67 |            8.00 | total              |       3.84 |          0.00 |          1.00 |       0.40 |            | NPA/loans                          |       0.03 |            |       -2.10 |     11.98 |           | Y: branch sale-leaseback gain offset $61.5M securities loss |                              -1.79 |      0.20 |   -7.40 | NPA +4% QoQ; ex-brokered deposits +1.2% QoQ                           |
| IBOC     |        16.40 |            |                  |                     |                 |                    |            |               |               |            |            |                                    |            |            |             |           |           |                                                             |                                    |     -0.40 |  -11.40 | not yet reported Q3 (Q2 reported Aug 6); moved listing to TXSE Oct 19 |
| HTH      |        12.70 | 2026-10-22 |             4.90 |                2.34 |                 | interest-bearing   |       3.33 |         12.00 |               |       0.54 |       0.57 | nonaccrual/loans                   |       0.06 |            |       -0.40 |     18.28 |           | N                                                           |                              -2.99 |      2.30 |   -6.10 | BVPS (not TBV); $10M provision build; PrimeLending loss               |
| STBA     |         9.90 | 2026-10-22 |            -0.30 |                2.46 |            3.00 | interest-bearing   |       4.06 |          7.00 |               |       0.45 |       0.50 | NPA/(loans+OREO)                   |       0.10 |       0.05 |        0.30 |     14.02 |     13.64 | N                                                           |                               0.79 |      5.40 |   -2.80 | record EPS                                                            |
| FMBH     |         9.10 | 2026-10-29 |             0.60 |                     |                 |                    |       3.76 |         -3.00 |               |       0.63 |       0.60 | NPL/loans                          |       0.01 |            |       -0.20 |     13.91 |           | Y: late-Oct securities sale $14.8M loss                     |                              -0.10 |      3.40 |   -3.50 | criticized -$45.9M; cost of funds up (rates + competition)            |
| PFBC     |         7.70 | 2026-10-23 |             1.20 |                3.06 |                 | total (Sept month) |       3.49 |        -24.00 |               |            |            | nonaccrual+90dpd $109.4M vs $98.9M |            |            |             |     11.26 |           | N                                                           |                              -2.77 |      3.60 |    0.30 | NIM 3.60 ex interest reversal; deposit competition into 2027          |
| MPB      |         7.00 | 2026-10-21 |             2.40 |                2.11 |            4.00 | total              |       3.92 |        -14.00 |         32.00 |            |            | NPA $47.0M vs $36.8M (+28%)        |       0.01 |       0.00 |        0.30 |           |           | N                                                           |                              -9.74 |     -4.40 |  -11.40 | accretion down; CRE nonaccrual +$7M                                   |
| TRST     |         6.50 | 2026-10-21 |             0.00 |                1.80 |                 | interest-bearing   |       2.95 |          8.00 |         16.00 |       0.39 |       0.40 | NPL/loans                          |            |            |             |           |           | N                                                           |                              -1.18 |      4.40 |   -1.00 | TCE/TA 9.71 vs 10.05 (buybacks)                                       |
| GSBC     |         5.50 | 2026-10-21 |            -5.40 |                     |                 |                    |       3.75 |         -1.00 |          3.00 |       0.03 |            | NPL/loans                          |       0.03 |            |             |     13.70 |     13.60 | N                                                           |                              -2.10 |      5.70 |    0.40 | brokered runoff -$300M YTD; AOCI -65M vs -32M; hedge accounting hit   |
| SFST     |         4.70 | 2026-10-20 |             1.90 |                2.97 |            1.00 | interest-bearing   |       3.02 |         15.00 |         40.00 |       0.30 |       0.27 | NPA/assets                         |       0.07 |            |        2.00 |     12.75 |     12.82 | N                                                           |                              -0.37 |      0.60 |   -6.10 | BVPS +2% QoQ; retail deposits +18% annualized                         |
| CBAN     |         3.60 | 2026-10-28 |            -0.50 |                2.12 |                 | interest-bearing   |       3.59 |          7.00 |         42.00 |            |            | NPA $25.0M vs $20.9M (+20%)        |       0.27 |       0.29 |        0.30 |     13.50 |           | Y: announced sale-leaseback + securities repositioning      |                              -0.29 |      3.20 |   -6.70 | one construction downgrade                                            |

**Tally (16 reporting):**
- NIM: 10 up, 1 flat, 5 down QoQ.
- Deposit cost: up at 8, flat 1, down 1 (of 10 with a QoQ figure).
- Deposits: up at 8 of 16.
- TBV/BV: down at 7 of 12.
- Loss-taking balance-sheet repositioning: 5 of 16.
- Earnings reaction: median −0.5%, positive at 31%.
- Spearman with the reaction: ΔNIM +0.34 (n=16); Δ deposit cost −0.42 (n=10). Neither is significant.

**Other notable Q3 items:**
- TCBI AOCI −$251M vs −$99M; criticized loans +12% QoQ.
- TowneBank AFS unrealized loss −$187M vs −$85M.
- Preferred Bank: reserves 0.75× nonperforming loans; management expects deposit competition "into 2027".
- Customers Bancorp raised full-year guidance.

# 6. Hypothesis scorecard

| Hypothesis | Evidence for | Evidence against | Verdict |
|---|---|---|---|
| Broad market rotation (small-cap / equal-weight) | Small and equal-weight indices also fell less than KBWB over 63d | IWM explains 28% of KRE's daily variance vs 69% normally; KRE's SPY beta at 1.6th percentile; on 10/22 KRE +2.5% while IWM was flat | Weak |
| Interest-rate relief | KRE's rate beta flipped to −0.06 (4th percentile); 10/22; bigger HTM losses → bigger rally; 5 of 16 sample banks repositioned securities | Rates explain only ~1.6 of 5 points in the rally; pre-window rate beta doesn't predict the rally; HY spreads widened during the rally | Best-supported, partial |
| Improving bank fundamentals | YTD returns track ΔNIM/ΔROA; small banks improved most and outperformed YTD; Q3 NIMs mostly up | June fundamentals ≈0 for the 63d/rally windows; Q3 deposit costs up, credit drifting, TBV down; median earnings reaction negative | Supports YTD, not the recent rally |

# 7. Confidence and gaps

- **High confidence:**
  - The correlation level and percentile.
  - The "KRE vs everything" pattern with normal internal cohesion.
  - Size-as-beta and breadth (direct computations from primary holdings and price data).
- **Medium confidence:** the rate-regime reading. It rests on 63 observations; R² of KRE on SPY + rates is only 0.17. The rates contribution is an in-sample fit.
- **Low confidence:**
  - The Q3 reaction correlations (n=10–16).
  - The business-model buckets (my thresholds).
  - The window split at the KRE low.
- **Secondary sources:**
  - KBWB holdings (aggregator).
  - The 9/14 BAC guidance and the 10/22 bond-rally narrative (news reports from Yahoo/TheStreet, Investing.com/Reuters, CNBC, Bloomberg, Globe and Mail — not company or market primary data).
- **Not done or not available:**
  - FDIC 9/30 call reports (re-run Sections 4–5 on Q3 for all 167 when loaded).
  - International Bancshares' Q3 report.
  - Why KeyCorp and Fifth Third are not in KRE.
- **Data caveats:**
  - FDIC data is bank-level, not holding-company.
  - Merger-affected growth rates (22 banks with asset growth >25% YoY) distort deposit growth.

# Appendix A. All 167 KRE stocks

Sorted by June-2026 assets.

**Definitions:**
- β KBWB = pre-window beta.
- NIM / ROA = Q2-2026 quarterly, %.
- ΔNIM = YoY, pp.
- cost dep = Q2-2026 annualized cost of deposits.
- NCO = H1-2026 annualized.
- NPL = noncurrent loans / loans.
- CRE/cap = CRE / total capital.
- unins = uninsured deposits / deposits.
- UL/T1 = unrealized securities loss (AFS + HTM) / Tier 1.
- dep g = deposit growth YoY (merger-affected for some).

|       | name                         |   wt % |   assets $bn |   mcap $bn | region         | model                          | KBWB   |   63d % |   8/3→10/14 % |   rally % |   YTD % |   β KBWB |   NIM Q2 |   ΔNIM |   ROA Q2 |   cost dep % |   NCO % |   NPL % |   ΔNPL pp |   CRE/cap % |   unins % |   UL/T1 % |   CET1 |   dep g % |   P/B |   fwd PE |
|:------|:-----------------------------|-------:|-------------:|-----------:|:---------------|:-------------------------------|:-------|--------:|--------------:|----------:|--------:|---------:|---------:|-------:|---------:|-------------:|--------:|--------:|----------:|------------:|----------:|----------:|-------:|----------:|------:|---------:|
| TFC   | Truist Financial Corp        |   1.1  |        548.3 |       58.5 | Southeast      | diversified community/regional | Y      |    -5.1 |         -11.4 |       7.1 |     2.2 |     1.04 |     3.14 |  -0.02 |     1.16 |         1.61 |    0.54 |    0.72 |      0.15 |          57 |        45 |     -24.6 |   12.1 |       0.4 |  1.07 |     10.2 |
| HBAN  | Huntington Bancshares Inc    |   1.07 |        283.1 |       31.8 | Midwest/Plains | diversified community/regional | Y      |    -8.2 |         -12.2 |       4.5 |    -6.4 |     1.1  |     3.39 |   0.1  |     1.13 |         1.85 |    0.24 |    1.06 |      0.26 |          83 |        32 |     -15.8 |   11.8 |      35.7 |  1.1  |      9.2 |
| CFG   | Citizens Financial Group     |   1.04 |        232.5 |       26.7 | Northeast      | diversified community/regional | Y      |   -11.5 |         -13.9 |       2.8 |    12.4 |     1.07 |     3.3  |   0.19 |     1.04 |         1.59 |    0.37 |    1.36 |     -0.07 |          95 |        47 |     -11.1 |   11.9 |       5.6 |  1.19 |     10   |
| MTB   | M + T Bank Corp              |   1.05 |        218.8 |       31.7 | Northeast      | diversified community/regional | Y      |   -11   |         -12.8 |       2.2 |    11.8 |     0.96 |     3.87 |   0.1  |     1.54 |         1.37 |    0.26 |    1.35 |     -0.17 |         104 |        49 |      -4.6 |   11.8 |       2.3 |  1.29 |     10.6 |
| RF    | Regions Financial Corp       |   1.08 |        159.8 |       24.3 | Southeast      | diversified community/regional | Y      |    -8.3 |         -13.7 |       6.2 |     8.5 |     1.05 |     3.74 |   0    |     1.47 |         1.16 |    0.46 |    0.93 |     -0.11 |          65 |        39 |      -5.9 |   11.6 |      -0.2 |  1.49 |     10.2 |
| PNFP  | Pinnacle Financial Partners  |   1.16 |        128.8 |       15.4 | Southeast      | diversified community/regional | Y      |    -5   |         -13.3 |       9.5 |     8.1 |     0.96 |     3.46 |   0.27 |     1.04 |         2.12 |    0.22 |    0.48 |      0.04 |         231 |        50 |      -4   |   10.7 |     125.9 |  1.14 |      9   |
| WAL   | Western Alliance Bancorp     |   1.08 |         98.6 |        8.2 | West           | diversified community/regional | Y      |    -7.4 |         -12.4 |       5.6 |    -7.9 |     1.27 |     3.51 |  -0.07 |     1.57 |         1.81 |    0.8  |    2.82 |      0.9  |         161 |        38 |     -10.7 |   11.6 |      15.3 |  1.15 |      7.4 |
| ZION  | Zions Bancorp Na             |   1.08 |         89   |        9.5 | West           | diversified community/regional | Y      |    -7.1 |         -12.2 |       5.8 |    14.1 |     1.23 |     3.32 |   0.11 |     2.05 |         1.49 |    0.04 |    0.47 |     -0.04 |         152 |        46 |     -14.2 |   11.8 |       3.5 |  1.27 |      9.6 |
| FLG   | Flagstar Bank Na             |   0.89 |         87.7 |        4.4 | Northeast      | CRE-heavy (>300% of capital)   |        |   -26   |         -21.8 |      -5.4 |   -16.3 |     0.54 |     2.17 |   0.19 |     0.16 |         2.52 |    0.58 |    4.97 |     -0.3  |         328 |        29 |      -8.7 |   13.2 |      -3.9 |  0.61 |     14.9 |
| EWBC  | East West Bancorp Inc        |   1.14 |         84.3 |       17.9 | West           | diversified community/regional | Y      |    -1   |          -5.7 |       5   |    18.7 |     0.92 |     3.45 |   0.06 |     1.77 |         2.06 |    0.13 |    0.38 |      0.12 |         205 |        52 |     -10.7 |   13.9 |       7.9 |  2.02 |     11.3 |
| FHN   | First Horizon Corp           |   1.07 |         84.1 |       11   | Southeast      | diversified community/regional | Y      |    -9.2 |         -11.5 |       2.6 |    -0.5 |     0.87 |     3.56 |   0.05 |     1.39 |         1.74 |    0.19 |    0.83 |     -0.13 |         143 |        40 |     -10   |   11.2 |       3.7 |  1.38 |     10.2 |
| BPOP  | Popular Inc                  |   1.07 |         78.4 |        9.8 | Puerto Rico    | diversified community/regional |        |    -9.3 |          -9.7 |       0.4 |    27.8 |     0.9  |     3.83 |   0.23 |     1.36 |         1.57 |    0.83 |    1.8  |      0.44 |         139 |        55 |     -15.2 |   16   |       4.1 |  1.62 |      9.2 |
| WTFC  | Wintrust Financial Corp      |   1.14 |         74.8 |       10.3 | Midwest/Plains | C&I-heavy (>30% loans)         |        |    -5.5 |         -12.5 |       8.1 |    10.2 |     0.87 |     3.39 |  -0.05 |     1.66 |         2.12 |    0.11 |    0.63 |     -0.05 |         153 |        36 |     -14.8 |   11.2 |       8.6 |  1.56 |     11.2 |
| ONB   | Old National Bancorp         |   1.11 |         73.9 |        9.5 | Midwest/Plains | diversified community/regional |        |    -6   |          -8.2 |       2.4 |    14.5 |     0.93 |     3.61 |  -0.13 |     1.46 |         1.67 |    0.25 |    0.92 |     -0.35 |         252 |        43 |     -18.4 |   11.3 |       3.9 |  1.21 |      9.2 |
| UMBF  | Umb Financial Corp           |   1.07 |         71.9 |       10.2 | Midwest/Plains | C&I-heavy (>30% loans)         |        |    -8.2 |         -12.1 |       4.4 |    18.1 |     0.78 |     3.28 |   0.29 |     1.39 |         1.98 |    0.17 |    0.34 |      0.06 |         164 |        64 |     -14.7 |   11.8 |      -0.7 |  1.4  |      9.9 |
| SSB   | Southstate Bank Corp         |   1.13 |         68.8 |       10.2 | Southeast      | diversified community/regional |        |    -1.9 |          -7.5 |       6.1 |    13.8 |     0.84 |     3.88 |  -0.24 |     1.42 |         1.74 |    0.07 |    0.54 |     -0.09 |         281 |        38 |     -11   |   12.2 |       4   |  1.15 |     10.4 |
| VLY   | Valley National Bancorp      |   1.16 |         66.2 |        7.8 | Northeast      | CRE-heavy (>300% of capital)   |        |    -1.7 |         -13.7 |      13.9 |    24.1 |     0.78 |     3.34 |   0.2  |     1.1  |         2.26 |    0.15 |    0.91 |      0.19 |         320 |        40 |      -7.9 |   12.3 |       7   |  1.07 |      9.5 |
| COLB  | Columbia Banking System Inc  |   1.16 |         65.4 |        8.7 | West           | diversified community/regional |        |    -1.4 |          -9.9 |       9.5 |    14   |     0.82 |     4.02 |   0.15 |     1.31 |         1.31 |    0.28 |    0.57 |      0.09 |         292 |        39 |      -5.9 |   12.2 |      24.8 |  1.22 |      9.4 |
| CFR   | Cullen/Frost Bankers Inc     |   1.1  |         54   |        9.8 | Texas          | diversified community/regional |        |    -6.1 |          -9.7 |       4   |    27.1 |     0.74 |     3.66 |   0.03 |     1.32 |         1.05 |    0.13 |    0.55 |      0.03 |         123 |        52 |     -24.7 |   14.4 |       3.5 |  2.59 |     13.2 |
| BOKF  | Bok Financial Corporation    |   1.09 |         53   |        7.9 | Texas          | C&I-heavy (>30% loans)         |        |    -9   |         -14   |       5.8 |    11.5 |     0.63 |     2.95 |   0.03 |     1.29 |         2.13 |    0.02 |    0.54 |     -0.04 |         131 |        53 |      -8   |   12.3 |       4   |  1.36 |     12.3 |
| ASB   | Associated Banc Corp         |   1.13 |         51.8 |        5.6 | Midwest/Plains | diversified community/regional |        |    -2.7 |          -9.1 |       7   |    20.7 |     0.9  |     3.33 |   0.3  |     1.04 |         2.15 |    0.16 |    0.42 |     -0    |         183 |        49 |     -11.1 |   10.2 |      17.3 |  1.09 |      9.2 |
| FNB   | Fnb Corp                     |   1.12 |         50.8 |        6.4 | Northeast      | diversified community/regional |        |    -5.2 |         -11.1 |       6.7 |     7.9 |     0.9  |     3.34 |  -0.01 |     1.23 |         1.73 |    0.19 |    0.38 |     -0.07 |         165 |        40 |      -6.5 |   11.4 |       1.2 |  0.95 |      9.8 |
| PB    | Prosperity Bancshares Inc    |   1.14 |         43.9 |        8.6 | Texas          | diversified community/regional |        |    -3.5 |         -10.6 |       7.9 |     6.9 |     0.63 |     3.51 |   0.3  |     1.57 |         1.3  |    0.35 |    0.48 |      0.01 |         171 |        43 |     -21.2 |   15.2 |      18.4 |  0.91 |      9.9 |
| OZK   | Bank Ozk                     |   1.17 |         41.7 |        5.5 | Southeast      | diversified community/regional |        |    -1   |         -12.2 |      12.7 |    14.5 |     0.71 |     4.15 |  -0.16 |     1.61 |         2.8  |    0.62 |    0.92 |      0.75 |         260 |        32 |      -0.6 |   11.8 |       1.4 |  0.97 |      8.6 |
| AUB   | Atlantic Union Bankshares Co |   1.12 |         38   |        5.5 | Southeast      | diversified community/regional |        |    -7.4 |         -11.7 |       4.9 |    14.4 |     0.88 |     4.03 |  -0.86 |     1.81 |         1.92 |    0.02 |    0.5  |     -0.24 |         264 |        36 |      -8.5 |   13   |      -1.6 |  1.13 |     10   |
| HWC   | Hancock Whitney Corp         |   1.09 |         36.3 |        5.8 | Southeast      | C&I-heavy (>30% loans)         |        |    -6.8 |          -7   |       0.2 |    15.5 |     0.85 |     3.66 |   0.1  |     1.44 |         1.39 |    0.17 |    0.57 |     -0.08 |         146 |        52 |     -12.4 |   12.9 |       1.9 |  1.39 |     10.1 |
| CBSH  | Commerce Bancshares Inc      |   1.07 |         35   |        7.8 | Midwest/Plains | diversified community/regional |        |    -7.3 |          -8.4 |       1.2 |     6.8 |     0.72 |     3.8  |   0.14 |     0.93 |         1.08 |    0.24 |    0.17 |     -0.08 |          93 |        39 |     -15.4 |   15.1 |       8.7 |  1.9  |     12.2 |
| BANC  | Banc Of California Inc       |   1.12 |         34.9 |        2.9 | West           | diversified community/regional |        |    -4.6 |         -11.2 |       7.4 |    -3.6 |     0.95 |     3.3  |   0.03 |    -2.68 |         1.79 |    1.39 |    2.34 |      1.06 |         291 |        29 |      -6.4 |   12.7 |       2   |  1.04 |      8.9 |
| BKU   | Bankunited Inc               |   1.07 |         34.9 |        3.1 | Southeast      | diversified community/regional |        |    -8   |         -12.2 |       4.8 |    -0.7 |     0.81 |     3.1  |   0.05 |     0.89 |         2    |    0.36 |    1.69 |     -0.69 |         194 |        58 |      -8.5 |   13   |      -0.5 |  1.1  |     10.3 |
| UBSI  | United Bankshares Inc        |   1.16 |         33.6 |        6.6 | Southeast      | diversified community/regional |        |    -0.6 |          -5.6 |       5.3 |    28.9 |     0.72 |     3.89 |   0.01 |     1.62 |         1.85 |    0.09 |    0.44 |      0.16 |         299 |        38 |      -5.7 |   13.7 |       3   |  1.23 |     12.5 |
| TCBI  | Texas Capital Bancshares Inc |   1.18 |         33.6 |        4.4 | Texas          | C&I-heavy (>30% loans)         |        |     0.7 |         -12.4 |      15   |    12.9 |     0.9  |     3.32 |  -0.08 |     1.09 |         2.29 |    0.27 |    0.5  |      0.02 |         105 |        38 |      -4.2 |   12.4 |      10.7 |  1.4  |     12.6 |
| FULT  | Fulton Financial Corp        |   1.13 |         32.6 |        4.5 | Northeast      | diversified community/regional |        |    -3.9 |         -10.5 |       7.4 |    24.6 |     0.93 |     3.67 |   0.11 |     1.36 |         1.75 |    0.3  |    0.71 |     -0.17 |         184 |        40 |     -12.5 |   13   |       3.9 |  1.31 |     10   |
| GBCI  | Glacier Bancorp Inc          |   1.2  |         31.6 |        6.3 | West           | diversified community/regional |        |    -3   |         -14.7 |      13.7 |    12.6 |     0.84 |     3.97 |   0.67 |     1.29 |         1.17 |    0.08 |    0.42 |      0.17 |         267 |        34 |     -14.6 |   13   |      14   |  1.51 |     14   |
| EBC   | Eastern Bankshares Inc       |   1.16 |         31.1 |        5.1 | Northeast      | diversified community/regional |        |    -2.4 |          -9.2 |       7.5 |    24.1 |     0.74 |     3.65 |   0.07 |     1.4  |         1.45 |    0.17 |    0.47 |      0.17 |         253 |        42 |     -12.4 |   12.1 |      22.4 |  1.18 |     10.7 |
| UCB   | United Community Banks/Ga    |   1.18 |         29   |        4.4 | Southeast      | diversified community/regional |        |     3.3 |          -6.8 |      10.8 |    20.4 |     0.83 |     3.71 |   0.19 |     1.63 |         1.63 |    0.18 |    0.51 |      0.08 |         216 |        39 |     -18   |   12.1 |      -1.3 |  1.29 |     10.9 |
| AX    | Axos Financial Inc           |   1.09 |         28.9 |        5.1 | West           | fintech/BaaS/specialty         |        |   -12.8 |         -16.5 |       4.4 |     4.9 |     1.05 |     4.64 |  -0.17 |     2.13 |         2.66 |    0.09 |    0.44 |     -0.18 |         188 |        21 |       1.1 |   10.9 |      18   |  1.66 |      8.8 |
| ABCB  | Ameris Bancorp               |   1.11 |         28.4 |        5.5 | Southeast      | diversified community/regional |        |    -6.3 |         -11.2 |       5.5 |    11.8 |     0.68 |     3.96 |   0.05 |     0.82 |         1.75 |    0.2  |    0.57 |      0.13 |         263 |        46 |      -1.1 |   13   |       2.6 |  1.37 |     12.1 |
| WSBC  | Wesbanco Inc                 |   1.08 |         27.7 |        3.7 | Southeast      | diversified community/regional |        |    -7.1 |         -12   |       5.6 |    19.5 |     0.81 |     3.73 |   0    |     1.42 |         1.76 |    0.09 |    0.86 |      0.3  |         268 |        32 |     -11.7 |   12.2 |       2.3 |  0.98 |     10.4 |
| WAFD  | Wafd Inc                     |   0.61 |         27.6 |        2.2 | West           | CRE-heavy (>300% of capital)   |        |   -20.9 |         -22   |       1.5 |    -6.2 |     0.67 |     2.89 |   0.18 |     0.99 |         2.33 |    0.02 |    0.63 |      0.23 |         332 |        31 |      -3.1 |   13   |      -2.1 |  0.83 |      7.5 |
| RNST  | Renasant Corp                |   0.98 |         27   |        3.6 | Southeast      | diversified community/regional |        |    -8.6 |         -10.9 |       2.6 |    15.4 |     0.8  |     3.98 |  -0.66 |     1.4  |         1.91 |    0.05 |    0.96 |      0.21 |         272 |        46 |      -6.6 |   12.4 |       1   |  0.97 |     10.7 |
| CUBI  | Customers Bancorp Inc        |   0.86 |         26.5 |        2.8 | Northeast      | fintech/BaaS/specialty         |        |     4.5 |          -8.9 |      14.7 |    15.1 |     0.92 |     3.16 |  -0.18 |     1.15 |         2.4  |    0.31 |    0.33 |      0.09 |         179 |        44 |      -5.3 |   13.6 |      14.6 |  1.33 |      8.9 |
| FIBK  | First Interstate Bancsys A   |   1.15 |         25.8 |        3.5 | West           | diversified community/regional |        |    -1.2 |          -9.8 |       9.5 |    13   |     0.79 |     3.59 |   0.16 |     1.4  |         1.14 |    0.17 |    1.12 |     -0.05 |         231 |        36 |     -20.2 |   14.3 |      -5.6 |  1.14 |     13.2 |
| PFS   | Provident Financial Services |   0.78 |         25.7 |        3   | Northeast      | CRE-heavy (>300% of capital)   |        |    -8   |         -11.9 |       4.5 |    19.8 |     0.75 |     3.63 |   0.1  |     1.33 |         1.89 |    0.05 |    0.55 |      0.02 |         422 |        54 |      -5.3 |   12.1 |       4.5 |  1.08 |      9.2 |
| INDB  | Independent Bank Corp/Ma     |   0.99 |         25   |        3.9 | Northeast      | diversified community/regional |        |    -1.9 |          -9.8 |       8.8 |    16   |     0.79 |     3.97 |   0.44 |     1.4  |         1.33 |    0.06 |    0.56 |      0.18 |         276 |        33 |      -5.9 |   14.9 |      26.8 |  1.16 |     10.2 |
| SFNC  | Simmons First Natl Corp Cl A |   1.03 |         24.7 |        3.3 | Southeast      | CRE-heavy (>300% of capital)   |        |    -2   |          -6.7 |       5.1 |    26.7 |     0.81 |     3.83 |   0.75 |     1.17 |         1.89 |    0.2  |    0.92 |      0    |         345 |        36 |     -19.7 |   10.4 |      -9.8 |  1.03 |     10.4 |
| CATY  | Cathay General Bancorp       |   1.03 |         24.6 |        4.3 | West           | diversified community/regional |        |     1.4 |          -7   |       9.1 |    35.8 |     0.75 |     3.53 |   0.21 |     1.57 |         2.36 |    0.04 |    0.54 |     -0.41 |         265 |        49 |      -2   |   14   |       5.4 |  1.43 |     10.7 |
| HOMB  | Home Bancshares Inc          |   1.13 |         24.6 |        5.9 | Southeast      | diversified community/regional |        |    -4.1 |          -8.9 |       5.2 |     9.6 |     0.68 |     4.72 |   0.18 |     2.1  |         1.85 |    0.07 |    0.55 |     -0.09 |         257 |        47 |     -11.3 |   14.8 |       8.8 |  1.34 |     11.8 |
| BOH   | Bank Of Hawaii Corp          |   0.93 |         23.8 |        2.7 | Hawaii         | thrift/residential             |        |   -12.2 |         -17.2 |       6   |     4.9 |     0.72 |     2.78 |   0.41 |     1.08 |         1.25 |    0.06 |    0.18 |     -0.03 |         179 |        47 |     -38.7 |   13.9 |       0.4 |  1.89 |     10.9 |
| FHB   | First Hawaiian Inc           |   1.11 |         23.6 |        3.1 | Hawaii         | diversified community/regional |        |    -9.2 |         -12.2 |       3.4 |     2.6 |     0.8  |     3.26 |   0.12 |     1.33 |         1.2  |    0.12 |    0.3  |      0.07 |         184 |        48 |     -25.5 |   13.2 |      -0.4 |  1.11 |     10.2 |
| OCFC  | Oceanfirst Financial Corp    |   0.65 |         23.2 |        1.8 | Northeast      | CRE-heavy (>300% of capital)   |        |    -7.8 |         -19.1 |      13.9 |     3.2 |     0.63 |     2.93 |  -0.09 |     0.08 |         1.87 |    0.03 |    0.66 |      0.34 |         384 |        52 |      -3.1 |   13   |      73.5 |  0.78 |      8.3 |
| TOWN  | Towne Bank                   |   0.73 |         22.6 |        3.4 | Southeast      | diversified community/regional |        |    -4.2 |          -8.1 |       4.3 |    13.4 |     0.56 |     3.74 |   0.53 |     3.44 |         1.53 |    0.1  |    0.22 |      0.15 |         249 |        48 |      -4.1 |   12.2 |      21.7 |  1.14 |     10.9 |
| WSFS  | Wsfs Financial Corp          |   1.12 |         22.6 |        4   | Northeast      | diversified community/regional |        |    -3.5 |          -7.5 |       4.3 |    43.2 |     0.67 |     3.96 |  -0.06 |     1.52 |         1.26 |    0.05 |    0.57 |     -0.41 |         225 |        46 |     -27.4 |   13.8 |      10.2 |  1.57 |     11.4 |
| FFBC  | First Financial Bancorp      |   1.05 |         22.4 |        3.4 | Midwest/Plains | C&I-heavy (>30% loans)         |        |    -4.5 |          -9.1 |       5.1 |    32.6 |     0.73 |     4.1  |  -0.08 |     1.55 |         1.76 |    0.27 |    0.7  |      0.05 |         169 |        42 |     -12.3 |   12.8 |      21.7 |  1.21 |      9.3 |
| BBT   | Beacon Financial Corp        |   0.82 |         22.2 |        2.6 | Northeast      | CRE-heavy (>300% of capital)   |        |    -3.1 |         -14.2 |      13   |    19.9 |     0.63 |     3.88 |   0.44 |     1.22 |         1.92 |    0.31 |    0.9  |     -0.38 |         336 |        38 |      -2.2 |   11.8 |     302   |  1.05 |      9.3 |
| SBCF  | Seacoast Banking Corp/Fl     |   1.06 |         21.3 |        3.2 | Southeast      | diversified community/regional |        |    -4.9 |          -8.8 |       4.4 |     7   |     0.77 |     3.85 |   0.2  |     1.14 |         1.5  |    0.1  |    0.66 |      0.05 |         230 |        36 |     -10.6 |   13.6 |      34.4 |  1.26 |     12.6 |
| FRME  | First Merchants Corp         |   0.56 |         21.3 |        2.5 | Midwest/Plains | C&I-heavy (>30% loans)         |        |    -6.1 |         -10.3 |       4.7 |    11.3 |     0.72 |     3.37 |   0.15 |     0.88 |         2.07 |    0.18 |    0.82 |      0.28 |         183 |        45 |     -20.8 |   11.5 |      12.9 |  0.99 |      9.5 |
| MCHB  | Mechanics Bancorp A          |   0.25 |         21.2 |        3.2 | West           | CRE-heavy (>300% of capital)   |        |   -12.6 |         -15.2 |       3.1 |     9.6 |     0.72 |     3.74 |   0.27 |     1.13 |         1.24 |    0.11 |    0.41 |      0.2  |         340 |        43 |      -9.6 |   15.5 |      29.5 |  1.36 |     13.2 |
| CVBF  | Cvb Financial Corp           |   1.09 |         21.2 |        4   | West           | diversified community/regional |        |    -0.3 |          -5.7 |       5.8 |    24.9 |     0.68 |     4.05 |   0.77 |     1.11 |         0.9  |    0    |    0.14 |     -0.17 |         281 |        54 |     -31.1 |   14.3 |      36.3 |  1.3  |     11.7 |
| CBC   | Central Bancompany           |   0.88 |         20.3 |        8.6 | Midwest/Plains | diversified community/regional |        |     8.8 |          -1.4 |      10.3 |    50.8 |     0.38 |     4.08 |   0.07 |     2.02 |         1.21 |    0.1  |    0.49 |      0.07 |         238 |        38 |      -7.1 |   12.7 |       8.9 |  2.3  |     18   |
| FBP   | First Bancorp Puerto Rico    |   1.06 |         19.2 |        4   | Puerto Rico    | diversified community/regional |        |    -9   |          -7.2 |      -1.9 |    29.4 |     0.87 |     4.99 |   0.24 |     1.99 |         1.35 |    0.56 |    0.9  |     -0.11 |         107 |        47 |     -16.4 |   16   |       1.8 |  2.13 |     10.5 |
| TRMK  | Trustmark Corp               |   0.57 |         19.2 |        2.6 | Southeast      | diversified community/regional |        |    -7.4 |          -7.6 |       0.2 |    15.5 |     0.66 |     3.89 |   0.06 |     1.4  |         1.56 |    0.12 |    1.14 |     -0.03 |         237 |        37 |      -1.8 |   12.4 |       6.6 |  1.26 |     10.6 |
| HOPE  | Hope Bancorp Inc             |   0.46 |         19   |        1.7 | West           | diversified community/regional |        |    -6   |          -6.1 |       0.1 |    24.5 |     0.73 |     3.02 |   0.12 |     0.79 |         2.57 |    0.26 |    0.88 |     -0.01 |         271 |        40 |     -10.9 |   12.7 |      -0.3 |  0.76 |     10.1 |
| SFBS  | Servisfirst Bancshares Inc   |   0.77 |         18.3 |        4.4 | Southeast      | CRE-heavy (>300% of capital)   |        |   -10.1 |         -15   |       5.8 |    14.4 |     0.74 |     3.62 |   0.54 |     1.89 |         2.19 |    0.17 |    1.18 |      0.64 |         307 |        66 |      -2.5 |   12   |       5   |  2.24 |     11.9 |
| BUSE  | First Busey Corp             |   0.81 |         18.1 |        2.4 | Midwest/Plains | diversified community/regional |        |    -7.1 |          -7.4 |       0.4 |    25.7 |     0.57 |     3.76 |   0.18 |     1.46 |         1.76 |    0.21 |    0.51 |      0.12 |         218 |        43 |     -12.8 |   14.7 |      -4.9 |  1.05 |     11   |
| TFSL  | Tfs Financial Corp           |   0.49 |         18.1 |        4.6 | Midwest/Plains | thrift/residential             |        |    -9.2 |         -10.6 |       1.5 |    29.9 |     0.57 |     1.9  |   0.12 |     0.68 |         2.83 |   -0.02 |    0.25 |      0.01 |           0 |         4 |      -1.3 |   15.7 |      -2.9 |  2.29 |     41.2 |
| CBU   | Community Financial System I |   0.56 |         17.4 |        3.3 | Northeast      | diversified community/regional |        |    -5.5 |         -10.6 |       5.6 |    11.1 |     0.61 |     3.53 |   0.17 |     1.21 |         1.06 |    0.11 |    0.5  |     -0    |         201 |        32 |     -29.1 |   11.7 |       7   |  1.66 |     12.4 |
| EFSC  | Enterprise Financial Service |   0.47 |         17.4 |        2.2 | Midwest/Plains | C&I-heavy (>30% loans)         |        |    -7   |         -11.7 |       5.4 |    16.4 |     0.66 |     4.34 |   0.08 |     1.02 |         1.52 |    0.3  |    0.98 |     -0.18 |         207 |        34 |      -8.3 |   12.1 |       9.5 |  1.23 |     10.6 |
| NWBI  | Northwest Bancshares Inc     |   0.54 |         17.2 |        2.2 | Northeast      | diversified community/regional |        |    -2.8 |          -6.4 |       3.9 |    32.4 |     0.61 |     3.91 |   0.18 |     1.35 |         1.4  |    0.15 |    0.69 |     -0.21 |         109 |        27 |     -13.7 |   12.8 |      15   |  1.21 |     10.8 |
| FBK   | Fb Financial Corp            |   0.66 |         16.8 |        2.6 | Southeast      | diversified community/regional |        |   -12   |         -17.3 |       6.3 |    -2.9 |     0.8  |     3.96 |   0.26 |     1.46 |         2.21 |    0.08 |    1.4  |      0.23 |         269 |        43 |      -3.1 |   11.3 |      25.5 |  1.41 |     10.9 |
| BANR  | Banner Corporation           |   0.7  |         16.6 |        2.5 | West           | diversified community/regional |        |    -1.2 |          -5.3 |       4.3 |    13.1 |     0.7  |     4.15 |   0.19 |     1.24 |         1.32 |    0.02 |    0.46 |      0.09 |         253 |        32 |     -22   |   12.7 |       2.1 |  1.22 |     10.8 |
| IBOC  | International Bancshares Crp |   0.84 |         16.4 |        4.2 | Texas          | diversified community/regional |        |   -11.4 |         -11   |      -0.4 |     2.7 |     0.65 |     4.43 |  -0.12 |     2.3  |         1.34 |    0.06 |    3.26 |      1.37 |         187 |        35 |     -10.6 |   23.3 |       2   |  1.26 |    nan   |
| NBTB  | N B T Bancorp Inc            |   0.62 |         16.1 |        2.7 | Northeast      | diversified community/regional |        |    -0.6 |          -4.4 |       4   |    28.8 |     0.68 |     3.81 |  -0.01 |     1.23 |         1.3  |    0.16 |    0.55 |      0.15 |         228 |        43 |     -11.3 |   11.8 |      -0.6 |  1.43 |     11.7 |
| LOB   | Live Oak Bancshares Inc      |   0.3  |         16   |        1.6 | Southeast      | fintech/BaaS/specialty         |        |   -21.2 |         -21.3 |       0.1 |     0.6 |     0.99 |     3.39 |  -0.01 |     1.03 |         3.21 |    0.65 |    4.01 |     -0.07 |         227 |        17 |      -5.6 |   10.5 |      16.2 |  1.36 |      8.5 |
| FSUN  | Firstsun Capital Bancorp     |   0.31 |         15.7 |        1.7 | Texas          | diversified community/regional |        |    -0.2 |          -4   |       4   |     4.1 |     0.68 |     5.27 |   1.09 |    -0.17 |         3.18 |    0.9  |    1.63 |      0.75 |         228 |        31 |      -2.6 |   13   |      87   |  1.02 |      9   |
| NIC   | Nicolet Bankshares Inc       |   1.13 |         15.4 |        3.6 | Midwest/Plains | diversified community/regional |        |    -0.9 |          -6.2 |       5.6 |    42.4 |     0.6  |     4.23 |   0.36 |     1.53 |         1.76 |    0.03 |    0.63 |      0.23 |         208 |        33 |      -3.6 |   11.1 |      68.6 |  1.63 |     12.8 |
| FFIN  | First Finl Bankshares Inc    |   0.92 |         15.2 |        4.4 | Texas          | diversified community/regional |        |   -13.1 |         -12.2 |      -1   |     4.5 |     0.71 |     3.83 |   0.12 |     1.77 |         1.46 |   -0.01 |    0.77 |     -0.01 |         107 |        45 |     -19.9 |   18.4 |       5.8 |  2.48 |     14.9 |
| DCOM  | Dime Commercial Bancshares I |   0.43 |         15   |        1.8 | Northeast      | CRE-heavy (>300% of capital)   |        |     2   |          -7.7 |      10.5 |    42.7 |     0.74 |     3.39 |   0.28 |     1.01 |         1.64 |    0.34 |    0.64 |      0.15 |         355 |        49 |      -5.8 |   14.8 |       7.7 |  1.34 |      9.8 |
| CNOB  | Connectone Bancorp Inc       |   0.52 |         14.4 |        1.6 | Northeast      | CRE-heavy (>300% of capital)   |        |    -3.5 |         -10.2 |       7.5 |    24.8 |     0.64 |     3.6  |   0.58 |     1.29 |         2.38 |    0.47 |    0.68 |      0.33 |         439 |        47 |      -4.3 |   12.3 |       3.4 |  1.12 |      8.9 |
| BANF  | Bancfirst Corp               |   0.56 |         14.3 |        3.7 | Texas          | diversified community/regional |        |    -2.8 |          -5.9 |       3.4 |     5.5 |     0.76 |     3.82 |   0.08 |     1.81 |         1.91 |    0.09 |    1.06 |      0.33 |         163 |        31 |      -0.7 |   17   |       6.7 |  1.95 |     13.9 |
| FBNC  | First Bancorp/Nc             |   0.46 |         13   |        2.6 | Southeast      | diversified community/regional |        |    -0.1 |          -6.9 |       7.3 |    26.7 |     0.8  |     3.85 |   0.35 |     1.61 |         1.29 |    0.05 |    0.49 |      0.07 |         280 |        41 |     -18.7 |   14.7 |       2.3 |  1.59 |     12.9 |
| HTH   | Hilltop Holdings Inc         |   0.33 |         12.7 |        2.1 | Texas          | diversified community/regional |        |    -6.1 |          -8.3 |       2.3 |    11.1 |     0.65 |     3.35 |   0.2  |     1.17 |         1.84 |    0.16 |    1.03 |     -0.14 |         255 |        54 |     -10.7 |   12.5 |       1.6 |  1.03 |     15.6 |
| PRK   | Park National Corp           |   0.57 |         12.6 |        3.2 | Midwest/Plains | diversified community/regional |        |   -14.9 |         -14.9 |       0   |    17.5 |     0.66 |     4.82 |  -0.14 |     1.91 |         1.19 |    0.11 |    0.86 |      0.04 |         197 |        22 |      -3.6 |   12.2 |      26.6 |  1.93 |     13.9 |
| NBHC  | National Bank Hold Cl A      |   0.54 |         12.5 |        1.7 | West           | diversified community/regional |        |   -12.7 |         -13.4 |       0.8 |     0.8 |     0.66 |     3.97 |   0.08 |     1.13 |         1.85 |    0.29 |    0.6  |      0.06 |         215 |        30 |     -10.3 |   12.3 |      25.9 |  1.04 |      9.7 |
| FCF   | First Commonwealth Finl Corp |   0.53 |         12.2 |        2   | Northeast      | diversified community/regional |        |    -2.8 |          -7.8 |       5.4 |    27.2 |     0.61 |     4.07 |   0.14 |     1.51 |         1.72 |    0.41 |    0.89 |     -0.16 |         205 |        28 |     -12   |   12.2 |       1.4 |  1.4  |     10.6 |
| CLBK  | Columbia Financial Inc       |   0.86 |         12.2 |        3   | Northeast      | CRE-heavy (>300% of capital)   |        |     4.2 |           2.3 |       1.8 |    57   |     0.46 |     2.4  |   0.15 |     0.52 |         2.05 |    0.03 |    0.51 |      0.01 |         350 |        46 |     -10.8 |   13.2 |      16.9 |  0.95 |     14.5 |
| OFG   | Ofg Bancorp                  |   0.5  |         12   |        2.1 | Puerto Rico    | diversified community/regional |        |    -5.1 |          -3.4 |      -1.8 |    24.9 |     0.68 |     5.59 |   0.14 |     1.88 |         1.34 |    1.21 |    1.59 |     -0.35 |          61 |        52 |      -7.1 |   13.2 |      -1.6 |  1.61 |      9.9 |
| BHRB  | Burke + Herbert Financial Se |   0.36 |         11   |        1.4 | Southeast      | CRE-heavy (>300% of capital)   |        |    -3.6 |          -6.3 |       2.9 |    15.9 |     0.52 |     4.49 |   0.22 |     0.66 |         1.83 |    0.03 |    1.19 |     -0.34 |         335 |        35 |      -6.1 |   13.3 |      40.7 |  1.27 |      8.2 |
| SYBT  | Stock Yards Bancorp Inc      |   0.46 |         10.4 |        2.4 | Southeast      | diversified community/regional |        |    -6.5 |         -10.3 |       4.2 |    22.4 |     0.63 |     3.92 |   0.33 |     1.72 |         1.81 |   -0    |    0.31 |      0.05 |         248 |        41 |      -9.7 |   12   |      13.1 |  2.12 |     13.9 |
| AMTB  | Amerant Bancorp Inc          |   0.32 |         10.3 |        1.2 | Southeast      | diversified community/regional |        |     1.2 |          -3.4 |       4.8 |    55.2 |     0.83 |     3.58 |  -0.29 |     0.93 |         2.2  |    0.25 |    2.49 |      1.34 |         218 |        47 |      -3.3 |   12.9 |       0.5 |  1.42 |     10.6 |
| OBK   | Origin Bancorp Inc           |   0.29 |         10.2 |        1.6 | Southeast      | diversified community/regional |        |    -3.6 |          -6.5 |       3.1 |    41.9 |     0.67 |     3.87 |   0.21 |     1.39 |         1.92 |    0.08 |    0.97 |     -0.14 |         227 |        49 |      -7   |   12.8 |       6.4 |  1.3  |     11.7 |
| STBA  | S + T Bancorp Inc            |   0.44 |          9.9 |        1.8 | Northeast      | CRE-heavy (>300% of capital)   |        |    -2.8 |          -7.7 |       5.4 |    31.6 |     0.65 |     3.98 |   0.07 |     1.47 |         1.73 |    0.07 |    0.5  |      0.23 |         309 |        36 |      -4.4 |   13.3 |       2   |  1.31 |     12.6 |
| TCBK  | Trico Bancshares             |   0.43 |          9.9 |        1.7 | West           | CRE-heavy (>300% of capital)   |        |    -8.9 |         -11.9 |       3.4 |    13.3 |     0.59 |     4.19 |   0.22 |     1.41 |         1.27 |    0.03 |    0.94 |      0.01 |         315 |        34 |     -14.1 |   13.7 |      -0.1 |  1.29 |     12.1 |
| BY    | Byline Bancorp Inc           |   0.39 |          9.9 |        1.7 | Midwest/Plains | C&I-heavy (>30% loans)         |        |    -2.9 |          -7.6 |       5.1 |    33.5 |     0.65 |     4.5  |   0.06 |     1.72 |         1.9  |    0.27 |    0.93 |      0.01 |         129 |        34 |     -10   |   14   |       0.8 |  1.38 |     11   |
| QCRH  | Qcr Holdings Inc             |   0.42 |          9.8 |        1.7 | Midwest/Plains | diversified community/regional |        |    -2.7 |          -6.7 |       4.3 |    22.2 |     0.64 |     3.24 |   0.08 |     1.74 |         2.4  |    0.2  |    0.56 |     -0.06 |         291 |        36 |      -9.5 |   13.3 |       3.8 |  1.47 |     11.4 |
| CFFN  | Capitol Federal Financial In |   0.23 |          9.7 |        1   | Midwest/Plains | thrift/residential             |        |    -6.5 |          -9.3 |       3.1 |    28.6 |     0.65 |     2.33 |   0.35 |     0.97 |         2.09 |    0    |    0.62 |      0.02 |         204 |        11 |       0.9 |    0   |       6.5 |  1.05 |     10   |
| EGBN  | Eagle Bancorp Inc            |   0.31 |          9.6 |        1   | Northeast      | diversified community/regional |        |    19.5 |          -1.4 |      21.2 |    55.5 |     0.75 |     2.86 |   0.15 |     0.38 |         2.93 |    2.21 |    2.05 |     -1.15 |         258 |        28 |     -13.5 |   14.9 |     -10.2 |  0.9  |     13.8 |
| PEBO  | Peoples Bancorp Inc          |   0.32 |          9.5 |        1.4 | Midwest/Plains | diversified community/regional |        |    -7.6 |         -14.3 |       7.8 |    33   |     0.67 |     4.34 |   0.11 |     1.28 |         1.46 |    0.35 |    0.6  |     -0.01 |         176 |        26 |     -17.4 |   12.3 |      -2.3 |  1.12 |      9.3 |
| AMAL  | Amalgamated Financial Corp   |   0.27 |          9.4 |        1.5 | Northeast      | diversified community/regional |        |     1.2 |          -5.9 |       7.6 |    58.2 |     0.73 |     3.85 |   0.25 |     1.53 |         1.46 |    0.25 |    1.99 |      1.25 |         235 |        57 |     -19.9 |   14.8 |       9.3 |  1.82 |     10.9 |
| SRCE  | 1St Source Corp              |   0.4  |          9.3 |        2.1 | Midwest/Plains | C&I-heavy (>30% loans)         |        |    -2.9 |          -6.4 |       3.7 |    42.3 |     0.57 |     4.43 |   0.28 |     2.15 |         1.88 |    0.12 |    0.99 |     -0.05 |          56 |        54 |      -4.8 |   14.8 |      -0.1 |  1.64 |     11.8 |
| TBBK  | Bancorp Inc/The              |   0.77 |          9.2 |        1.9 | Midwest/Plains | fintech/BaaS/specialty         |        |   -34.2 |         -31.8 |      -3.4 |   -30.8 |     0.9  |     5.52 |  -0.65 |     2.94 |         0.12 |    1.57 |    1.33 |      0.09 |         254 |         3 |      -0.5 |   14.3 |      -3.7 |  2.76 |      6.5 |
| FMBH  | First Mid Bancshares Inc     |   0.24 |          9.1 |        1.3 | Midwest/Plains | diversified community/regional |        |    -3.5 |          -6.7 |       3.4 |    31.4 |     0.63 |     3.83 |   0    |     1.09 |         1.76 |    0.08 |    0.58 |      0.23 |         271 |        17 |     -14.8 |   13.6 |      22.2 |  1.25 |     10.1 |
| BFST  | Business First Bancshares    |   0.26 |          8.9 |        1   | Southeast      | diversified community/regional |        |     0.1 |          -3.2 |       3.4 |    23.5 |     0.57 |     3.86 |   0.12 |     1.21 |         2.24 |    0.12 |    1.26 |      0.29 |         241 |        47 |      -4.7 |   12.3 |      13   |  1.14 |      9.9 |
| MCB   | Metropolitan Bank Holding Co |   0.43 |          8.9 |        1.2 | Northeast      | fintech/BaaS/specialty         |        |     3.5 |          -6.8 |      11.1 |    26.7 |     0.66 |     4.22 |   0.28 |     0.93 |         2.58 |    1.27 |    0.91 |      0.31 |         304 |        27 |     -10.6 |   12.9 |      13.9 |  1.23 |      8.8 |
| TMP   | Tompkins Financial Corp      |   0.34 |          8.8 |        1.4 | Northeast      | CRE-heavy (>300% of capital)   |        |    -0.7 |          -4.3 |       3.8 |    40.4 |     0.75 |     3.58 |   0.48 |     1.45 |         1.47 |    0.07 |    0.8  |     -0.05 |         323 |        41 |      -7.4 |   11.9 |       6   |  1.56 |     12.4 |
| SBSI  | Southside Bancshares Inc     |   0.15 |          8.8 |        1   | Texas          | diversified community/regional |        |     4.3 |          -6.4 |      11.4 |    14.6 |     0.67 |     3.03 |   0.07 |     1.38 |         1.86 |    0.02 |    0.19 |      0.09 |         289 |        43 |     -14.9 |   16.3 |      -7   |  1.25 |     10.2 |
| HFWA  | Heritage Financial Corp      |   0.3  |          8.4 |        1.2 | West           | diversified community/regional |        |    -4.3 |          -9.7 |       5.9 |    23.6 |     0.69 |     4.03 |   0.49 |     0.92 |         1.2  |    0.03 |    0.27 |     -0.12 |         295 |        39 |     -12.3 |   12.3 |      21.7 |  1.1  |     11.2 |
| CCNE  | Cnb Financial Corp/Pa        |   0.19 |          8.4 |        1.1 | Northeast      | diversified community/regional |        |     0.3 |          -5.3 |       5.9 |    38   |     0.57 |     3.96 |   0.35 |     1.39 |         2.02 |    0.05 |    0.84 |      0.24 |         269 |        29 |      -6.4 |   13.1 |      28.9 |  1.25 |      9.8 |
| UVSP  | Univest Financial Corp       |   0.3  |          8.2 |        1.1 | Northeast      | diversified community/regional |        |   -10.6 |          -8.8 |      -2   |    23.1 |     0.66 |     3.6  |   0.23 |     1.24 |         2.22 |    0.09 |    0.62 |      0.21 |         264 |        45 |      -5.6 |   10.8 |       4.7 |  1.18 |     10.5 |
| PGC   | Peapack Gladstone Finl Corp  |   0.28 |          8   |        0.8 | Northeast      | CRE-heavy (>300% of capital)   |        |    -2   |          -7.4 |       5.8 |    63.4 |     0.79 |     3.38 |   0.52 |     0.83 |         2.08 |    0.52 |    1.07 |     -0.91 |         406 |        36 |     -11.4 |   10.6 |      10.7 |  1.12 |      9.7 |
| HAFC  | Hanmi Financial Corporation  |   0.25 |          8   |        1   | West           | CRE-heavy (>300% of capital)   |        |     1.7 |          -4.7 |       6.8 |    23.9 |     0.73 |     3.45 |   0.3  |     1.31 |         2.2  |    0.12 |    0.15 |     -0.26 |         315 |        45 |      -7.2 |   13.4 |       3.4 |  1.21 |      9.7 |
| PFBC  | Preferred Bank/Los Angeles   |   0.38 |          7.7 |        1.3 | West           | CRE-heavy (>300% of capital)   |        |     0.3 |          -3.1 |       3.6 |    15.5 |     0.64 |     3.75 |  -0.09 |     1.74 |         3.05 |    0.17 |    1.57 |      0.66 |         357 |        50 |      -3.6 |   11.1 |       6.5 |  1.63 |      9.6 |
| EQBK  | Equity Bancshares Inc   Cl A |   0.18 |          7.7 |        1   | Midwest/Plains | diversified community/regional |        |    -4.1 |          -8.3 |       4.5 |    10.4 |     0.46 |     4.31 |   0.07 |     1.54 |         1.9  |    0.11 |    1.18 |     -0.03 |         237 |        27 |      -0.8 |   13.1 |      47.9 |  1.26 |      9.2 |
| KRNY  | Kearny Financial Corp/Md     |   0.17 |          7.7 |        0.6 | Northeast      | CRE-heavy (>300% of capital)   |        |    -4.9 |          -6.8 |       2   |    27.9 |     0.7  |     2.31 |   0.29 |     0.38 |         2.13 |    0.02 |    0.81 |      0.03 |         514 |        39 |     -16.2 |   13.4 |       0.6 |  0.78 |      9.9 |
| CPF   | Central Pacific Financial Co |   0.21 |          7.5 |        1   | Hawaii         | thrift/residential             |        |    -3.5 |         -10   |       7.3 |    25   |     0.72 |     3.68 |   0.07 |     1.22 |         0.88 |    0.19 |    0.3  |     -0.02 |         193 |        42 |     -20.3 |   13.4 |       2.1 |  1.71 |     10.6 |
| NBBK  | Nb Bancorp Inc               |   0.21 |          7.4 |        1   | Northeast      | CRE-heavy (>300% of capital)   |        |    -3.7 |          -4   |       0.3 |    13.1 |     0.48 |     3.95 |   0.21 |     1.2  |         2.62 |    0.45 |    0.43 |      0.15 |         314 |        28 |      -0.7 |   11.5 |      47.8 |  1.04 |      9   |
| TFIN  | Triumph Financial Inc        |   0.53 |          7.4 |        1.5 | Texas          | fintech/BaaS/specialty         |        |   -19   |         -20.1 |       1.4 |    -0.8 |     1.04 |     6.4  |  -0.17 |     0.74 |         1.61 |    0.13 |    1.65 |      0.06 |          94 |        26 |      -0.5 |   11.4 |      19.8 |  1.64 |     18.2 |
| CASH  | Pathward Financial Inc       |   0.62 |          7.3 |        1.6 | Midwest/Plains | fintech/BaaS/specialty         |        |   -17   |         -22   |       6.5 |     6.3 |     0.69 |     7.15 |  -0.79 |     1.65 |         0.01 |    0.84 |    5.28 |      3.8  |           5 |        13 |     -26.2 |   12   |      -0.9 |  1.95 |      7   |
| LKFN  | Lakeland Financial Corp      |   0.4  |          7.2 |        1.5 | Midwest/Plains | diversified community/regional |        |    -3.6 |          -9.4 |       6.3 |     9   |     0.63 |     3.49 |   0.07 |     1.69 |         2.32 |    0.08 |    0.36 |     -0.23 |         209 |        58 |     -17.9 |   14.1 |       2.7 |  2.09 |     13.4 |
| FMNB  | Farmers Natl Banc Corp       |   0.23 |          7.2 |        0.9 | Midwest/Plains | diversified community/regional |        |    -1   |          -5.5 |       4.8 |    21.7 |     0.49 |     3.62 |   0.47 |     1.28 |         1.76 |    0.17 |    0.93 |      0.09 |         198 |        35 |     -27.7 |   12.6 |      32.5 |  1.31 |      8.9 |
| RBCAA | Republic Bancorp Inc Class A |   0.3  |          7.1 |        1.6 | Southeast      | diversified community/regional |        |    -8.8 |          -8.3 |      -0.6 |    33.3 |     0.6  |     4.95 |   0.17 |     1.85 |         1.37 |    0.46 |    0.56 |      0.16 |         125 |        46 |      -1   |   16.5 |       4.6 |  1.56 |     12.9 |
| MPB   | Mid Penn Bancorp Inc         |   0.17 |          7   |        0.9 | Northeast      | CRE-heavy (>300% of capital)   |        |   -11.4 |          -7.3 |      -4.4 |    11.7 |     0.59 |     4.05 |   0.51 |     1.4  |         2.05 |    0.04 |    0.51 |      0.14 |         328 |        20 |      -5.7 |   12.6 |       8.4 |  0.97 |      9.3 |
| CTBI  | Community Trust Bancorp Inc  |   0.25 |          6.9 |        1.3 | Southeast      | diversified community/regional |        |   -11.8 |          -5.5 |      -6.6 |    25.3 |     0.67 |     3.87 |   0.13 |     1.69 |         1.93 |    0.09 |    0.58 |      0.06 |         165 |        30 |      -9.7 |    0   |       8.1 |  1.45 |     10.8 |
| CAC   | Camden National Corp         |   0.18 |          6.9 |        1   | Northeast      | thrift/residential             |        |    -2.5 |          -6.3 |       4   |    36.6 |     0.7  |     3.39 |   0.21 |     1.38 |         1.58 |    0.04 |    0.24 |     -0.12 |         261 |        24 |     -12.2 |   12.7 |       0.8 |  1.38 |     10.4 |
| OSBC  | Old Second Bancorp Inc       |   0.32 |          6.9 |        1.2 | Midwest/Plains | diversified community/regional |        |    -5.4 |          -4.5 |      -1   |    26.2 |     0.6  |     5.35 |   0.38 |     1.77 |         0.99 |    0.72 |    1.08 |      0.27 |         192 |        27 |      -5.9 |   13.7 |      12.3 |  1.4  |     10.5 |
| CHCO  | City Holding Co              |   0.56 |          6.8 |        2   | Southeast      | thrift/residential             |        |    -1.2 |          -3.8 |       2.7 |    23.1 |     0.48 |     3.99 |   0.01 |     1.99 |         1.1  |    0.05 |    0.22 |     -0.1  |         206 |        17 |     -16.5 |   15   |       2.1 |  2.62 |     15   |
| TCBX  | Third Coast Bancshares Inc   |   0.14 |          6.7 |        0.7 | Texas          | C&I-heavy (>30% loans)         |        |    -9.3 |          -6.3 |      -3.2 |     4.9 |     0.67 |     3.95 |  -0.41 |     1.46 |         3.04 |   -0.01 |    0.5  |      0.01 |         236 |        31 |       0.2 |   12.1 |      36.8 |  1.01 |      9.6 |
| HBT   | Hbt Financial Inc/De         |   0.17 |          6.7 |        1.3 | Midwest/Plains | diversified community/regional |        |     2.8 |          -1.7 |       4.6 |    44.6 |     0.59 |     4.48 |   0.2  |     1.68 |         1.19 |    0.03 |    0.19 |      0.02 |         262 |        24 |      -9.1 |   14.7 |      33.1 |  1.81 |     10.5 |
| MSBI  | Midland States Bancorp Inc   |   0.18 |          6.7 |        0.7 | Midwest/Plains | diversified community/regional |        |    -3.2 |          -6.1 |       3   |    60.6 |     0.71 |     4.06 |   0.32 |     1.26 |         1.76 |    0.9  |    1.43 |     -0.15 |         261 |        23 |     -13.6 |   13.6 |      -3.9 |  1.66 |      9.7 |
| WASH  | Washington Trust Bancorp     |   0.2  |          6.6 |        0.7 | Northeast      | thrift/residential             |        |    -1.1 |          -5.9 |       5   |    39.5 |     0.75 |     2.79 |   0.35 |     1.01 |         2.09 |    0    |    0.78 |      0.27 |         333 |        27 |     -16.7 |   12.2 |       6.3 |  1.43 |     11.1 |
| HBNC  | Horizon Bancorp Inc/In       |   0.44 |          6.5 |        1.1 | Midwest/Plains | diversified community/regional |        |     0.5 |          -7.8 |       9   |    26.4 |     0.68 |     4.47 |   1.21 |     1.71 |         1.49 |    0.05 |    0.7  |      0.17 |         235 |        26 |      -4.9 |   12.6 |      -5.2 |  1.55 |      9.4 |
| TRST  | Trustco Bank Corp Ny         |   0.26 |          6.5 |        1   | Northeast      | thrift/residential             |        |    -1   |          -5.2 |       4.4 |    39.3 |     0.62 |     2.89 |   0.16 |     1.05 |         1.54 |   -0    |    0.4  |      0.06 |          28 |        22 |      -3.5 |   14.5 |       3.5 |  1.52 |     20.2 |
| FISI  | Financial Institutions Inc   |   0.22 |          6.3 |        0.8 | Northeast      | diversified community/regional |        |    -6.8 |          -8.6 |       1.9 |    29.8 |     0.76 |     3.85 |   0.23 |     1.43 |         2.07 |    0.27 |    0.82 |      0.11 |         294 |        46 |      -8.5 |   12.7 |       2.2 |  1.3  |      9.3 |
| MBWM  | Mercantile Bank Corp         |   0.26 |          6.2 |        1   | Midwest/Plains | diversified community/regional |        |    -0.9 |          -4.4 |       3.7 |    27   |     0.61 |     3.6  |   0    |     1.7  |         1.88 |   -0.03 |    0.1  |     -0.11 |         222 |        57 |      -5.2 |   12.6 |       4.2 |  1.43 |     10.4 |
| THFF  | First Financial Corp         |   0.27 |          6.2 |        0.9 | Midwest/Plains | diversified community/regional |        |    -6.6 |         -10.9 |       4.8 |    31   |     0.68 |     4.33 |   0.18 |     1.51 |         1.46 |    0.19 |    0.61 |      0.35 |         264 |        36 |     -17.9 |   12.6 |       3.5 |  1.41 |      9.5 |
| SHBI  | Shore Bancshares Inc         |   0.17 |          6.1 |        0.7 | Northeast      | CRE-heavy (>300% of capital)   |        |    -8.3 |          -8.5 |       0.3 |    29.1 |     0.68 |     3.79 |   0.36 |     1.34 |         1.68 |    0.04 |    1.32 |      0.97 |         326 |        18 |      -7.7 |   12.3 |       2   |  1.23 |     10.1 |
| SMBK  | Smartfinancial Inc           |   0.17 |          6.1 |        0.8 | Southeast      | diversified community/regional |        |    -8.9 |          -6.4 |      -2.6 |    31.8 |     0.56 |     3.61 |   0.3  |     1.2  |         2.09 |    0.03 |    0.24 |      0.05 |         290 |        48 |      -5.3 |   11.4 |      10.6 |  1.46 |     11.9 |
| BFC   | Bank First Corp              |   0.45 |          5.9 |        1.7 | Midwest/Plains | diversified community/regional |        |    -3.6 |          -5.5 |       2   |    23.8 |     0.56 |     4.16 |   0.42 |     1.69 |         1.51 |    0.05 |    0.56 |      0.19 |         240 |        33 |      -2.4 |   10.9 |      38.6 |  2.05 |     12.6 |
| WABC  | Westamerica Bancorporation   |   0.33 |          5.8 |        1.4 | West           | diversified community/regional |        |     0.7 |          -2.7 |       3.5 |    30.3 |     0.49 |     3.9  |  -0.1  |     1.85 |         0.26 |    0.14 |    0.12 |     -0.54 |          55 |        50 |     -31   |   16.2 |       0.5 |  1.79 |     12.4 |
| IBCP  | Independent Bank Corp   Mich |   0.24 |          5.7 |        0.8 | Midwest/Plains | diversified community/regional |        |    -4.3 |          -9   |       5.2 |    15.1 |     0.54 |     3.74 |   0.06 |     1.42 |         1.48 |    0.03 |    0.99 |      0.74 |         174 |        24 |     -14   |   11.4 |       4.2 |  1.43 |      9.4 |
| ORRF  | Orrstown Finl Services Inc   |   0.19 |          5.6 |        0.9 | Northeast      | diversified community/regional |        |     1.2 |          -5.4 |       6.9 |    26.9 |     0.72 |     4.03 |  -0.13 |     1.7  |         1.88 |    0.1  |    0.6  |     -0.01 |         300 |        29 |      -4.5 |   12.1 |       2   |  1.46 |      9.9 |
| GSBC  | Great Southern Bancorp Inc   |   0.26 |          5.5 |        0.9 | Midwest/Plains | CRE-heavy (>300% of capital)   |        |     0.4 |          -5.1 |       5.7 |    34.3 |     0.59 |     3.89 |   0.03 |     1.2  |         1.61 |    0.04 |    0.02 |     -0.02 |         438 |        38 |      -9.1 |   13.3 |      -7.2 |  1.45 |     14   |
| CCB   | Coastal Financial Corp/Wa    |   0.28 |          5.5 |        0.7 | West           | fintech/BaaS/specialty         |        |     1.5 |          -3.6 |       5.3 |   -62.2 |     0.77 |     6.89 |  -0.64 |    -2.99 |         2.27 |    4.64 |    2.27 |      0.58 |         219 |        27 |       0   |   11   |      23.9 |  1.38 |      8.5 |
| PFIS  | Peoples Financial Services   |   0.13 |          5.4 |        0.7 | Northeast      | diversified community/regional |        |     1   |          -3   |       4.1 |    48.9 |     0.58 |     3.83 |   0.04 |     1.23 |         1.63 |    0.06 |    0.33 |     -0.11 |         290 |        31 |      -7.4 |   12.7 |       5.2 |  1.41 |     10.4 |
| SPFI  | South Plains Financial Inc   |   0.18 |          5.4 |        0.8 | Texas          | diversified community/regional |        |    -1.3 |          -4.6 |       3.5 |    14.8 |     0.66 |     4.38 |   0.06 |     1.6  |         2.15 |    0.05 |    0.25 |     -0.08 |         239 |        37 |     -11.7 |   13.4 |      22.6 |  1.35 |     10.7 |
| FSBC  | Five Star Bancorp            |   0.25 |          5.4 |        1.1 | West           | CRE-heavy (>300% of capital)   |        |    -5.1 |         -10.1 |       5.7 |    27.8 |     0.55 |     3.78 |   0.12 |     1.61 |         2.16 |    0.07 |    0.3  |      0.23 |         536 |        59 |      -2.4 |   11.1 |      23.2 |  1.82 |     12.3 |
| NBN   | Northeast Bank               |   0.5  |          5.2 |        1.1 | Northeast      | fintech/BaaS/specialty         |        |    -6.3 |          -6.5 |       0.3 |    19.4 |     0.71 |     4.84 |  -0.36 |     2.68 |         3.45 |    0.23 |    0.55 |     -0.37 |         464 |         4 |      -0.1 |   13.5 |       9.6 |  1.77 |      8.1 |
| SMBC  | Southern Missouri Bancorp    |   0.26 |          5.2 |        0.8 | Midwest/Plains | diversified community/regional |        |    -9.9 |         -12.3 |       2.7 |    20.9 |     0.61 |     3.74 |   0.22 |     1.62 |         2.41 |    0.21 |    0.63 |      0.07 |         288 |        19 |      -2.3 |   12.1 |       2.8 |  1.32 |     10.5 |
| CWBC  | Community West Bancshares    |   0.29 |          5   |        0.7 | West           | diversified community/regional |        |     1.7 |           0.8 |       0.9 |    16.3 |     0.51 |     5.3  |   1.02 |     0.51 |         1.51 |    0.31 |    0.56 |      0.28 |         298 |        33 |     -10.6 |   12.9 |      37.7 |  1.19 |      8.8 |
| CARE  | Carter Bankshares Inc        |   0.36 |          4.8 |        0.6 | Southeast      | CRE-heavy (>300% of capital)   |        |   -17.9 |         -15   |      -3.4 |    48.5 |     0.55 |     3.51 |   0.6  |     0.2  |         2.03 |   -0.83 |    1.01 |     -5.68 |         395 |        18 |      -7.3 |   14.3 |      -0.8 |  1.22 |     11.2 |
| BHB   | Bar Harbor Bankshares        |   0.14 |          4.7 |        0.7 | Northeast      | CRE-heavy (>300% of capital)   |        |     1.2 |          -4.9 |       6.5 |    33.9 |     0.59 |     3.69 |   0.37 |     1.5  |         1.51 |    0.19 |    0.32 |     -0.01 |         335 |        20 |      -9.5 |   12.7 |      17   |  1.3  |     10.7 |
| SFST  | Southern First Bancshares    |   0.26 |          4.7 |        0.6 | Southeast      | diversified community/regional |        |    -6.1 |          -6.7 |       0.6 |    15.6 |     0.81 |     2.97 |   0.44 |     1    |         2.34 |    0.01 |    0.28 |     -0.03 |         236 |        46 |      -2.5 |   11.6 |       9.5 |  1.26 |      9.9 |
| HIFS  | Hingham Institution For Svgs |   0.32 |          4.6 |        0.7 | Northeast      | CRE-heavy (>300% of capital)   |        |     2.3 |          -2.6 |       5.1 |     7   |     0.78 |     2.14 |   0.5  |     2.24 |         2.38 |    0    |    0.78 |     -0.02 |         525 |        36 |      -0   |   14.7 |       4.7 |  1.32 |    nan   |
| AROW  | Arrow Financial Corp         |   0.12 |          4.5 |        0.7 | Northeast      | diversified community/regional |        |    -4.1 |          -9.6 |       6   |    25.2 |     0.71 |     3.42 |   0.28 |     0.99 |         1.71 |    0.09 |    0.24 |      0.06 |         142 |        30 |      -5.3 |   12.7 |      -6.5 |  1.41 |      9.1 |
| COFS  | Choiceone Financial Svcs Inc |   0.11 |          4.5 |        0.5 | Midwest/Plains | diversified community/regional |        |     4.5 |          -5.2 |      10.3 |    23.5 |     0.64 |     3.75 |  -0.12 |     1.18 |         1.58 |    0.02 |    1    |      0.43 |         257 |        33 |     -22   |   11.8 |       0.4 |  1.16 |      9.6 |
| CCBG  | Capital City Bank Group Inc  |   0.15 |          4.4 |        0.9 | Southeast      | thrift/residential             |        |    -2.5 |          -6.8 |       4.5 |    21.6 |     0.47 |     4.37 |   0.04 |     1.53 |         0.72 |    0.12 |    0.4  |      0.15 |         122 |        48 |      -6.5 |   18.2 |       0.7 |  1.55 |     13.8 |
| HTB   | Hometrust Bancshares Inc     |   0.24 |          4.4 |        0.7 | Southeast      | diversified community/regional |        |    -9.3 |         -10.1 |       0.9 |     8.9 |     0.55 |     4.45 |   0.25 |     1.52 |         1.72 |    0.2  |    1.4  |      0.62 |         235 |        26 |      -0.1 |   13.7 |      -1.7 |  1.3  |     10.7 |
| FBIZ  | First Business Financial Ser |   0.13 |          4.4 |        0.6 | Midwest/Plains | CRE-heavy (>300% of capital)   |        |     4.9 |          -3.6 |       8.8 |    41.2 |     0.69 |     3.85 |   0.08 |     1.52 |         2.58 |    0.18 |    1.06 |      0.18 |         340 |        33 |      -3.8 |   11.2 |       8.6 |  1.65 |     11.1 |
| CIVB  | Civista Bancshares Inc       |   0.13 |          4.3 |        0.6 | Midwest/Plains | diversified community/regional |        |    -2.7 |          -8.8 |       6.7 |    29.7 |     0.55 |     4.07 |   0.31 |     1.43 |         1.81 |    0.05 |    0.92 |      0.19 |         261 |        18 |      -8.4 |   16.4 |       8.8 |  1.08 |      9.7 |
| BCAL  | California Bancorp           |   0.13 |          4   |        0.7 | West           | CRE-heavy (>300% of capital)   |        |     0.7 |           0.6 |       0   |    16.9 |     0.45 |     4.82 |   0.01 |     1.48 |         1.29 |    0.01 |    0.29 |     -0.33 |         313 |        50 |      -2.3 |   13.9 |       1.1 |  1.2  |     11.7 |
| BMRC  | Bank Of Marin Bancorp/Ca     |   0.15 |          3.9 |        0.5 | West           | CRE-heavy (>300% of capital)   |        |    -2.3 |         -10.1 |       8.6 |    12.1 |     0.68 |     3.54 |   0.51 |     1.06 |         1.25 |    0.7  |    0.4  |     -1.16 |         366 |        37 |     -11.1 |   13.7 |       3.6 |  1.24 |     12   |
| CBAN  | Colony Bankcorp              |   0.15 |          3.6 |        0.4 | Southeast      | diversified community/regional |        |    -6.7 |          -9.6 |       3.2 |    16.1 |     0.49 |     3.63 |   0.42 |     1.23 |         1.74 |    0.28 |    0.76 |      0.23 |         278 |        32 |     -17.6 |   13.6 |      16.1 |  1.12 |      8.6 |
| HBCP  | Home Bancorp Inc             |   0.18 |          3.6 |        0.5 | Southeast      | diversified community/regional |        |   -15.9 |          -9.5 |      -7.2 |     6.4 |     0.71 |     4.47 |   0.18 |     1.39 |         1.65 |    0.06 |    0.95 |      0.11 |         208 |        31 |      -5.9 |   14.4 |       5.7 |  1.07 |     10   |
| NRIM  | Northrim Bancorp Inc         |   0.12 |          3.4 |        0.5 | West           | diversified community/regional |        |   -11.9 |         -10.9 |      -1.1 |    -8.6 |     0.86 |     5.72 |   0.28 |     2.04 |         1.21 |    0.02 |    0.89 |      0.4  |         270 |        39 |      -0.8 |   12.4 |       4.2 |  1.53 |      9   |
| RRBI  | Red River Bancshares Inc     |   0.29 |          3.3 |        0.7 | Southeast      | diversified community/regional |        |     1.8 |          -1.4 |       3.2 |    45.8 |     0.56 |     3.67 |   0.23 |     1.45 |         1.41 |    0.01 |    0.11 |      0.05 |         155 |        32 |     -15.5 |   17.3 |       3.4 |  1.87 |     13.9 |
| ACNB  | Acnb Corp                    |   0.13 |          3.3 |        0.7 | Northeast      | diversified community/regional |        |     2   |          -2.5 |       4.6 |    39.5 |     0.55 |     4.63 |   0.37 |     1.86 |         1.04 |    0.01 |    0.4  |     -0.02 |         232 |        22 |      -9.3 |   14.3 |       0.3 |  1.62 |     11.8 |
| UNTY  | Unity Bancorp Inc            |   0.12 |          3.2 |        0.6 | Northeast      | diversified community/regional |        |    -2.8 |          -7.5 |       5.1 |    11.8 |     0.66 |     4.43 |   0.13 |     1.93 |         2.3  |   -0.01 |    1.23 |      0.45 |         237 |        42 |      -2.1 |   14.3 |      12.3 |  1.53 |      9.3 |
| ESQ   | Esquire Financial Holdings I |   0.56 |          2.5 |        1.5 | Northeast      | fintech/BaaS/specialty         |        |    -3   |          -8.5 |       6   |    23.1 |     0.66 |     6.13 |  -0.13 |     2.34 |         1.03 |    0.52 |    0.27 |     -0.32 |         166 |        34 |      -6.4 |   14.2 |      22.4 |  1.89 |     13.9 |

# Appendix B. Q3 sample source documents

- **SEC 8-K Ex 99.1 (accession numbers):**
  - TFC 0000092230-26-000108
  - FHN 0000036966-26-000178
  - ASB 0000007789-26-000257
  - TCBI 0001077428-26-000078
  - CUBI 0001488813-26-000100
  - TRMK 0001193125-26-434330
  - HTH 0001104659-26-118167
  - STBA 0000719220-26-000114
  - FMBH 0001171843-26-006956
  - MPB 0000879635-26-000058
  - TRST 0001140361-26-040403
  - GSBC 0001171843-26-006766
  - SFST 0001206774-26-000563
  - CBAN 0001104659-26-119632
- **GlobeNewswire:**
  - TowneBank (10/28/2026)
  - Preferred Bank (10/23/2026)
- **IBOC:** no Q3 release as of 10/30; it moved its listing to the Texas Stock Exchange on 10/19 (8-K 10/6/2026).
