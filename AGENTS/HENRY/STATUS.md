# HENRY STATUS

**Signal Status:** 🟡 COMPLACENCY TRAP — **VIX 18.60, Brent $98.71, HY OAS 285** | CPI 3.3% YoY locks Fed | **Last Updated:** 2026-04-17 ET

---

## MARKET DATA — Apr 16, 2026

| Metric | Value | Δ vs Prior | Source | Status |
|--------|-------|------------|--------|--------|
| SPX | 7,038 | — | Live | 🟡 |
| VIX | **18.6** | — | Live | 🟡 Compressed |
| Brent | **$98.71** | — | Live | 🟡 |
| Gas (AAA) | **$4.123** | — | Live | 🔴 |
| 10Y Yield | 4.26% | — | Live | 🟡 |
| USD/JPY | **159.18** | — | Live | 🔴 |
| HY OAS | **285.0bps** | — | FRED | 🟢 |
| CCC OAS | **924.0bps** | — | FRED | 🟡 |
| KRE | $68.93 | — | Live | 🟡 |
| APO | $122.35 | — | Live | 🟡 |

---

## VOL REGIME

- **VIX:** 18.6 (compressed; bull-market regime)
- **Term structure:** *PENDING LIVE PULL* (last known: contango, normal)
- **Vol-control layer:** VIX <23 = mechanical buying; currently INACTIVE (sellers, not selling-pressure)
- **0DTE share:** *PENDING LIVE PULL* (baseline ~60% SPX volume)
- **GEX regime:** *PENDING LIVE PULL* (above gamma flip ~6,902 = dealer-long-gamma, suppressive)

*Next refresh: pull VIX1D/VX1M/VX2M from fetch.py; SpotGamma GEX via WebSearch.*

---

## ACTIVE THRESHOLDS

| Metric | Current | Yellow | Orange | Red | Cross-Agent Trigger |
|--------|---------|--------|--------|-----|---------------------|
| VIX | 18.6 | >23 | >28 | **>30 sustained** | → ALL (risk-off regime) |
| SPX | 7,038 | <6,800 | <6,707 | **<6,494** | → CTA layer 4 (long-term) |
| KRE | $68.93 | <$65 | <$62 | **<$60** | → REGINALD, PROME |
| ISM Mfg | 52.7 | <50 | <48 | **<47** | → LABOR, PROME |
| 10Y Yield | 4.26% | >4.5% | >4.8% | **>5.0%** | → LIQUID (term premium crisis) |
| HY OAS | 285bps | >320 | >400 | **>500** | → credit-equity transmission |
| USD/JPY | 159.18 | >160 | >162 | **>165** | → SAM (carry unwind) |

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

*Counter-signals / invalidation watch:*
- ⚠️ VIX 18.6 + HY OAS 285 = credit NOT confirming stress yet
- ⚠️ SPX 7,038 above Feb high = structural bid intact (buybacks + passive flows)
- ⚠️ KRE $68.93 = regional banks have NOT cracked
- **Invalidates if:** HY OAS <260 sustained + VIX <15 + SPX >7,100 held 5+ sessions

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

**The complacency trap is the story.** VIX 19 with Hormuz still closed, CPI 3.3%, and UMich at record lows is mispricing. The market has priced ceasefire as resolution, but the structural risks (Fed trap, consumer exhaustion, credit stress) are unchanged. Oil at $98-99 now, but Brent is Fed-exogenous; services disinflation underneath PPI headline gives Powell an ambient "transitory" narrative he cannot pivot on into 3.3% CPI. Regional bank earnings **converge Apr 21** (OZK AMC + WAL same day; call OZK Apr 22) — first real test of credit stress marks, same-day binary on both thesis shorts. BOJ Apr 23-24 is the carry unwind catalyst. **April 21–30 is the 10-day window where every catalyst resolves.** Watch HY OAS 300 — if it breaks lower with VIX sub-17, the thesis weakens materially.
