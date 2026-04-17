# HENRY STATUS

**Signal Status:** 🟡 COMPLACENCY TRAP — **VIX 17.66, Brent $88.16, HY OAS 285 (stale)** | Hormuz declared "completely open" Apr 17 AM → oil -11% to -14% intraday | **Last Updated:** 2026-04-17 ~10:40 ET

---

## MARKET DATA — Apr 17, 2026 (intraday ~10:40 ET)

| Metric | Value | Δ vs Apr 16 close | Source | Status |
|--------|-------|-------------------|--------|--------|
| SPX | **7,127** | +1.21% | yfinance | 🟡 |
| VIX | **17.66** | -1.45% | yfinance | 🟡 Compressed further |
| Brent | **$88.16** | **-11.3%** | yfinance | 🟢 Shock removed |
| WTI | **$81.02** | **-14.4%** | yfinance | 🟢 Shock removed |
| Gas (AAA) | **$4.076** | -$0.047 | AAA | 🔴 Still >$4 |
| 10Y Yield | 4.24% | -2bps | yfinance | 🟡 |
| USD/JPY | **157.71** | -0.67% | yfinance | 🟠 Away from 160 |
| HY OAS | 285bps (Apr 16) | — | FRED (1-day lag) | 🟢 Refresh pending |
| CCC OAS | 924bps (Apr 2) | — | FRED | 🟡 |
| KRE | **$70.93** | +3.06% | yfinance | 🟡 Bid into FITB/RF |
| APO | **$126.48** | +4.69% | yfinance | 🟡 |
| TLT | $87.11 | +0.96% | yfinance | — |

---

## VOL REGIME

*VIX/term structure/VVIX/SKEW owned by VIOLET — values below are `[CONF VIOLET Apr 17]` from her `workbook/VX_DAILY.tsv` 14:32 UTC pull. Do not duplicate-track; pull from her file.*

- **VIX:** 17.62 | **VIX3M:** 20.43 | **VIX6M:** 22.47 | **VIX3M/VIX:** 1.160 (steepening, further from inversion)
- **VVIX:** 94.26 (compressed from 100.09 Apr 16; well below 120 stress threshold) — dealer vol-of-vol premium collapsing on Hormuz reopen
- **SKEW:** 140.74 (**bounced** from 139.23 Apr 16; back above 140) — reverses VIOLET's Apr 16 "peaceful resolution" watch; re-activates FADE_RERAMP path (69% historical) if holds
- **Term structure:** VX M1 (K6) / M2 (M6) **+2.54% contango, roll-adjusted** (below 5.6% avg; flat-ish but normal, not backwardation)
- **Regime (VIOLET):** LOW_VOL — credit-vol correlation weak (~0.06), credit leads vol 6-16 weeks in this regime
- **Vol-control layer:** VIX <23 = mechanical buying; INACTIVE-BUYING (compression = flow-in)
- **0DTE SPX share:** *PENDING* — HENRY domain, SpotGamma/Barchart wire-up needed
- **GEX regime:** *PENDING* — HENRY domain, SpotGamma gated
- **MOVE / HY OAS bracket (LIQUID Apr 10):** HY OAS <300 = squeeze path (Apr 16 @ 285); >340 = stress path. Hormuz reopen should compress further — sub-260 sustained would trip thesis invalidation.
- **VIOLET tactical trigger (not armed):** HY OAS +100bps from Jan 22 trough (264) → VIX 15-26 regime = 2-6wk lead to VIX >10pt spike. Currently only +20bps from trough.

*Next refresh: HENRY to wire 0DTE + GEX via SpotGamma/Barchart; fresh HY OAS Apr 17 close via FRED tomorrow AM.*

---

## ACTIVE THRESHOLDS

| Metric | Current | Yellow | Orange | Red | Cross-Agent Trigger |
|--------|---------|--------|--------|-----|---------------------|
| VIX | 17.66 | >23 | >28 | **>30 sustained** | → ALL (risk-off regime) |
| SPX | 7,127 | <6,800 | <6,707 | **<6,494** | → CTA layer 4 (long-term) |
| KRE | $70.93 | <$65 | <$62 | **<$60** | → REGINALD, PROME |
| ISM Mfg | 52.7 | <50 | <48 | **<47** | → LABOR, PROME |
| 10Y Yield | 4.24% | >4.5% | >4.8% | **>5.0%** | → LIQUID (term premium crisis) |
| HY OAS | 285bps (Apr 16) | >320 | >400 | **>500** | → credit-equity transmission |
| CCC-BB Spread | ~800bps (Apr 2) | >750 | >900 | **>1100** | → dispersion canary (pre-Apr 21) |
| USD/JPY | 157.71 | >160 | >162 | **>165** | → SAM (carry unwind) |

---

## APRIL CATALYST STACK

| Date | Event | HENRY Lens |
|------|-------|------------|
| **Apr 21 AMC** | **OZK Q1 + WAL Q1** (same day) | First real test of CRE marks. REGINALD thesis convergence. Binary vol event. |
| Apr 21 | Retail Sales Mar (rescheduled) | First consumer print post-CPI 3.3%. Control group is the GDP feed. |
| Apr 23-24 | **BOJ Policy Meeting** | Carry unwind catalyst. USD/JPY 159 → >160 or <157 either way. |
| Apr 28-29 | **FOMC Meeting** (no SEP) | Powell presser into CPI 3.3% + UMich inflation exp 3.8% = hawkish lock-in. |
| Apr 29 | Housing Starts Mar (rescheduled) | — |
| Apr 30 | **March PCE + GDP Q1 Advance** | First war-energy-inclusive PCE. Core expected hot vs Feb 3.0%. |

---

## ACTIVE PREDICTIONS

| ID | Prediction | Resolves |
|----|------------|----------|
| HEN-22 | CPI 3.3% + VIX 19 = complacency trap forming | Apr 30 |
| HEN-23 | Gas $4+ = consumer demand destruction begins | Apr 30 |
| HEN-24 | OZK Q1: provision spike / MI3 acceleration, stock gaps >5% | Apr 22 |
| HEN-25 | WAL Q1: fund-finance/CRE exposure, stock gaps >5% | Apr 22 |
| HEN-26 | BOJ: USD/JPY moves >2 handles; base case HOLD → yen weakens past 160 | Apr 25 |
| HEN-27 | March PCE: core YoY >3.0% OR MoM >0.3% (energy passthrough) | Apr 30 |
| HEN-28 | Labor cliff: claims >240K or 4-wk avg >230K | May 1 |

*Full log: workbook/PREDICTIONS.tsv (24 rows, 23 resolved, 7 active)*

---

## THESIS STATE

**COMPLACENCY TRAP (primary working thesis — Apr 2026):**

*Confirmed/amplifying signals:*
- ✅ CPI 3.3% + Core PCE 3.0% = Fed trap LOCKED (cuts repriced to H2 2027)
- ✅ UMich 1-yr inflation expectations 3.4% → 3.8% (largest jump since Apr 2025)
- ✅ ISM Services Employment 45.2 (lowest since Dec 2023) + JOLTS hiring 3.1% (lowest since Apr 2020) = **LABOR internals breaking under surface**
- ✅ ISM Mfg Prices Paid 78.3 (highest since Jun 2022) = stagflation, not expansion
- ✅ Gas $4.12 + consumer sentiment 53.3 = consumer double-bind
- ✅ March PPI +4.0% YoY headline (highest since Feb 2023), Core +3.8% — Fed-can't-cut print, though core-core +0.2% MoM cooler (goods/energy shock, not broad)

*Counter-signals / invalidation watch:*
- ⚠️ VIX 18.6 + HY OAS 285 = credit NOT confirming stress yet (but CCC-BB dispersion vertical: 700→800bps Jan→Apr 2, mask effect)
- ⚠️ SPX 7,038 above Feb high = structural bid intact (buybacks + passive flows)
- ⚠️ KRE $68.93 = regional banks have NOT cracked
- 🕒 Econ Surprise 0.338 (Apr 2, highest since late 2023) = longer lag before stress shows, sharper break when it does — April data prints are the test
- **Invalidates if:** HY OAS <260 sustained + VIX <15 + SPX >7,100 held 5+ sessions

---

## APR 21 SETUP — POSITIONING ASYMMETRY

- **HF short-cover whipsaw (GS Prime):** Week ending Apr 4, HFs covered single-stock + macro shorts fastest pace since 2020. Prior week was fastest *sold* in 13 years — violent reversal, not conviction. Trigger = Trump Iran ceasefire, now dead (Islamabad collapsed Apr 12, Hormuz blockade). Funds covered into optimism that evaporated = wrong-footed into Apr 21.
- **Financials positioning gap (DB/ISABELNET):** High-freq financials positioning at multi-year lows (-1.5 to -2z) while consensus earnings growth +20-40% YoY. Widest divergence since 2020. Resolves OZK + WAL + ZION Apr 21 AMC.
- **Binary magnitude:** Both tails fatten. Beat → short-squeeze (HFs still underweight financials). Miss → deeper crack (positioning correct, covered broad shorts re-risk into weakening tape).

---

## CROSS-AGENT DEPENDENCIES

| From | Signal | HENRY Impact |
|------|--------|-------------|
| LABOR | claims >300K | Structural bid breaks → cascade accelerates |
| LIQUID | HY OAS >320 | Credit transmission confirmed → H4 validates |
| SAM | Yen strengthens past 155 | Carry unwind Phase 2 → systematic deleveraging |
| REGINALD | KRE <$60 OR OZK/WAL earnings miss | Credit-equity transmission, bank-stress cascade |
| HAWK | Hormuz escalation | Oil >$100 → Fed hold locked → stagflation regime |
| BRENT | Brent sustained <$85 | Energy-deflation = CPI cools = Fed cuts return = thesis weakens |

---

## BOTTOM LINE

**The complacency trap is the story — but Hormuz reopen is a material counter-signal.** Apr 17 AM: Iranian FM declared Hormuz "completely open" for Israel-Lebanon ceasefire duration → Brent -11%, WTI -14%, SPX +1.2%, VIX 17.66. US blockade technically remains in force, so it's a *unilateral Iranian concession*, not a signed deal. Thesis amber watch: if this holds 5+ sessions with HY OAS drifting sub-260 and VIX sub-17, invalidation criteria triggered. **Counter-counter:** (1) blockade language says tankers still can't reach Iranian ports, so global flow effect may be asymmetric; (2) oil-shock-removed does not fix CPI 3.3% already printed, UMich 3.8% exp, or ISM Services Employment 45.2 — stagflation trap survives even a clean oil unwind; (3) positioning asymmetry into Apr 21 unchanged (HF whipsaw, DB financials -2z). **Watch today:** (a) does VIX print <17 on close, (b) does HY OAS Apr 17 settle print <280, (c) FITB + RF AMC — regional-bank bid today may just be Hormuz beta, not credit-quality conviction. **April 21–30 window intact**, but if Hormuz reopen sticks, the macro shock variable gets subtracted and the thesis becomes "labor + credit only" rather than "stagflation."
