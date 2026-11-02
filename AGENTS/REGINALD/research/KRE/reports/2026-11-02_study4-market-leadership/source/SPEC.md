# Study 4 (market leadership vs regional-bank decoupling): spec fixed BEFORE computing any study-4 statistic
Written 2026-11-02 (session 12 continued), after downloading data only.

## Data
- Daily adjusted closes (Yahoo v8 chart, period2=1800000000): KRE KBWB SPY RSP IWM IWN IWO QQQ XLF KBE IWD IWF MTUM XLK
  + predetermined nonbank set: XLU (utilities, rate-sensitive), IYR (REITs, rate-sensitive), ITB (homebuilders, rate+cycle),
  XLI (industrials, cyclical), XLB (materials, cyclical), IYT (transports, cyclical), KIE (insurance, non-bank financial).
  Set chosen before looking at any 2025–26 statistic; no additions/removals afterwards.
- Kenneth French Data Library daily: Mkt-RF, SMB, HML, RF (3-factor) and Mom. Available through 2026-09-30 only.
- ETF factor proxies to extend to 10/30: MKT_p = SPY − RF; SMB_p = IWM − SPY; HML_p = IWD − IWF; MOM_p = MTUM − SPY (from 2013-04).
  RF after 9/30 = Treasury 3m par yield/252. Proxy quality reported vs French over 2013-05..2026-09.
- Rates: Treasury 10y par yield daily change (pp). Credit: ΔBAA10Y (FRED, via study-3 master.csv).
- Last observation: 2026-10-30.

## Windows and reference distributions
- Recent windows: 21, 63, 126 sessions ending 2026-10-30 (and ending 2026-09-30 for exact French factors).
- Percentiles: vs all rolling windows; reference period stated each time (KBWB-based: since 2012-02; KRE-only: since 2006-12).
  For Q2 "collapse" tests the reference is fixed to windows ending 2012-02..2024-12 (pre-2025), so 2025–26 is out-of-reference.
- Any count/test uses non-overlapping windows.

## Q1 metrics
- 63d corr and univariate beta of KRE and of KBWB vs SPY RSP IWM IWN QQQ XLF KBE; percentile vs own history.
- Leadership metrics: corr(SPY,RSP), corr(SPY,QQQ), beta of RSP and IWN on SPY; CONC = r_SPY − r_RSP.
- KRE ~ RSP + CONC (does KRE load on the equal-weight market normally?).

## Q2
- 63d univariate SPY beta for each nonbank ETF + IWN + KBWB + KRE: pct vs own pre-2025 history; "collapse" = below own pre-2025 10th pct.
  Dates of collapse episodes in 2025–26 (runs ≥ 10 sessions).
- Same with RSP as the market.

## Q3 models (daily OLS, same spec in every window)
- M0: SPY. M1: MKT. M2: MKT+SMB+HML+MOM. M3: M2 + Δ10y. M4: M3 + CONC + ΔBaa.
- Recent exposures (21/63/126) vs historical median and percentile (rolling, same window length).
- Unexplained: R², residual vol, residual corr(KRE_resid, KBWB_resid) under M2/M3, partial corr — vs history.
- Volatility-matched: reference = the 10% of historical 63d windows (since 2012-02) closest to current in (log KRE vol, log SPY vol).
- Out-of-sample: non-overlapping 21-day blocks since 2013-11; fit on prior 126 sessions, predict block; OOS R² = 1 − SSE/Σ(r − train mean)².
  Compare M0..M4 historically vs recent blocks (2025, 2026H1, Jul–Oct 2026). Rank by OOS, not in-sample.

## Q4 timing
- Rolling 63d series + non-overlapping 21d blocks since 2024-01: KRE beta (SPY, RSP), corr KRE–IWN, KRE–KBWB, KRE HML beta, KRE Δ10y beta,
  corr SPY–RSP, nonbank SPY betas. Onset = first date a series stays below its pre-2025 10th pct for ≥10 consecutive sessions, per year (2025, 2026).

## Hypotheses (fixed now, with what each predicts)
- H1 Market leadership/composition (SPY driven by AI/mega-cap): KRE's beta/corr to RSP/IWN/XLI ~normal; SPY–RSP corr low; other value/cyclical ETFs also lose SPY beta; KRE fine vs equal-weight factors.
- H2 Style rotation (value/small): KRE keeps normal HML/SMB loadings; problem is style factors decoupled from market.
- H3 Rate regime (bank-wide): adding Δ10y restores much of the fit; KBWB shares it.
- H4 Regional-bank-specific repricing: KRE decoupled from RSP/IWN/XLI/KBWB too; large residual unexplained after factors; nonbank sectors show no comparable collapse.
- H5 Low-vol attenuation: vol-matched history makes current values unremarkable.

## Change log
(append with reason)
- Factor series for windows ending 10/30 = French through 9/30 spliced with ETF proxies for 10/1–10/30 (French data end 9/30); pure-French windows ending 9/30 reported alongside. Decided before results.
- Added after first results (diagnostic, labelled in report): beta decomposition into loading vs structure terms (q3b, q4b), KRE–KBWB correlation decomposition (q3b), sector 5-factor R²/OOS (q3b), value-factor rate beta and 63d alphas (q3c), frozen-loading next-test calibration (q5). No hypothesis, ETF set or threshold was changed.
