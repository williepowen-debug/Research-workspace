# HENRY STATUS

**Signal Status:** 🟡 COMPLACENCY TRAP — **VIX 17.76, Brent $90.67, HY OAS 285 (stale)** | Hormuz "completely open" Apr 17 AM → oil closed off lows (-8.8% Brent vs -11% intraday) | **Last Updated:** 2026-04-17 EOD (~16:00 ET)

---

## MARKET DATA — Apr 17, 2026 EOD

| Metric | EOD | Δ vs Apr 16 close | Δ vs AM (10:40) | Source | Status |
|--------|-----|-------------------|-----------------|--------|--------|
| SPX | **7,123.77** | +1.17% | flat | yfinance | 🟡 |
| VIX | **17.76** | -1.00% | +0.10 | yfinance | 🟡 No further compression |
| VIX3M | 20.68 | — | +0.25 | yfinance | Term structure slightly wider |
| SKEW | 140.74 | flat | flat | yfinance | 🟠 Holds >140 — FADE_RERAMP active (VIOLET) |
| Brent | **$90.67** | **-8.77%** | **+$2.51** | yfinance | 🟡 Partial retrace — skepticism on unilateral |
| WTI | **$83.18** | **-12.16%** | +$2.16 | yfinance | 🟡 Same — off intraday lows |
| Gas (AAA) | **$4.076** | -$0.047 | — | AAA | 🔴 Still >$4 |
| 10Y Yield | 4.25% | -1bp | +1bp | yfinance | 🟡 |
| USD/JPY | **158.55** | -0.16% | +0.84 | yfinance | 🟠 Yen gave back |
| HY OAS | 285bps (Apr 16) | — | — | FRED (1-day lag) | 🟢 Apr 17 print tomorrow AM |
| CCC OAS | 924bps (Apr 2) | — | — | FRED | 🟡 |
| KRE | **$70.38** | +2.24% | **-$0.55** | yfinance | 🟡 Gave back — AM bid was Hormuz beta |
| APO | **$124.28** | +2.87% | -$2.20 | yfinance | 🟡 Faded |
| TLT | $87.04 | +0.88% | -$0.07 | yfinance | — |
| HYG | $80.62 | +0.34% | — | yfinance | 🟢 Risk-on |
| LQD | $110.04 | +0.56% | — | yfinance | 🟢 Bid |

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
| VIX | 17.76 | >23 | >28 | **>30 sustained** | → ALL (risk-off regime) |
| SPX | 7,123.77 | <6,800 | <6,707 | **<6,494** | → CTA layer 4 (long-term) |
| KRE | $70.38 | <$65 | <$62 | **<$60** | → REGINALD, PROME |
| ISM Mfg | 52.7 | <50 | <48 | **<47** | → LABOR, PROME |
| 10Y Yield | 4.25% | >4.5% | >4.8% | **>5.0%** | → LIQUID (term premium crisis) |
| HY OAS | 285bps (Apr 16) | >320 | >400 | **>500** | → credit-equity transmission |
| CCC-BB Spread | ~800bps (Apr 2) | >750 | >900 | **>1100** | → dispersion canary (pre-Apr 21) |
| USD/JPY | 158.55 | >160 | >162 | **>165** | → SAM (carry unwind) |

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

**Complacency trap intact into weekend.** Apr 17 EOD: SPX closed +1.17% at 7,123.77 (within 4pts of AM highs), VIX 17.76 (did NOT break 17), SKEW 140.74 (holds >140), Brent +$2.51 off intraday lows (closed -8.77% vs -11.3% AM), KRE gave back $0.55 from AM peak, APO faded $2.20. **Three EOD tells:** (1) VIX refused to compress below 17 — complacency hasn't deepened, (2) Brent partial retrace = oil market itself pricing skepticism on unilateral Iranian declaration, (3) KRE/APO gave back most of the AM Hormuz beta — consistent with LESSONS rule on regional-bank margin vs credit trade distinction. **Invalidation criteria NOT triggered** (required VIX <15 + HY OAS <260 + SPX >7,100 for 5 sessions — only SPX piece qualifies). **Counter-counter still holds:** oil-shock-removed does not fix CPI 3.3% / UMich 3.8% / ISM Services Employment 45.2 — stagflation trap survives a clean oil unwind. **April 21–30 catalyst window fully intact:** OZK+WAL Q1 (Tue AMC), BOJ (Wed-Thu), FOMC (Tue-Wed following), PCE+GDP (Thu). Positioning asymmetry into Apr 21 unchanged (HF whipsaw, DB financials -2z). **Monday watch:** (a) Apr 17 HY OAS settle print (tomorrow AM FRED) — sub-280 = compression continuing, (b) Brent weekend gap — any fresh escalation/de-escalation headline repricing, (c) tanker-tracking signal (HAWK/BRENT) on whether physical flow is actually moving vs just announced.
