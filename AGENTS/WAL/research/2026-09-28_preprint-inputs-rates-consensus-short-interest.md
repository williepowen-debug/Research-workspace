# WAL pre-print inputs: rate sensitivity · dated consensus · short interest (2026-09-28)

**Written:** Mon 2026-09-28 ~17:1x ET, WAL session #10. **Asked by:** Will (pasted recommendation, 9/28): *"Take the three cheap ones now, in one WAL session: #3, #2, #4 … they give the new §10.2 non-credit rule real numbers to grade against."* and *"WAL should pull its own table now, then hand REGINALD the figure so both desks grade off one number."*
**Scope:** three pulls that must exist **before** the Q3 print (unannounced; pattern ~10/20–10/28). No score, weight, EV, PT, grading cell or trade moved. The results feed the print frame as **benchmarks / non-gating records** (§9 annotation, 9/28), not as new rules.

---

## 1. WAL's own rate sensitivity (Q2 10-Q, Item 3) — A1

**Source:** Q2-26 10-Q, filed 2026-07-31, acc **0001628280-26-051418**, `wal-20260630.htm` pp. 88-89, pulled raw from EDGAR 9/28 17:12 ET. Q1 comparison: Q1-26 10-Q acc 0001628280-26-033054, `wal-20260331.htm`, same section.

**Net interest income sensitivity (% change vs a forward-curve base; DYNAMIC balance sheet; horizon = next 12 months):**

| Scenario | Down 200 | Down 100 | Up 100 | Up 200 |
|---|---|---|---|---|
| **Parallel shock, 6/30/26** | **(8.6)%** | **(5.2)%** | **+5.9%** | **+11.8%** |
| Parallel shock, 3/31/26 | (7.1)% | (4.2)% | +6.0% | +11.6% |
| **Gradual ramp (over 12 months), 6/30/26** | **(5.1)%** | **(2.7)%** | **+3.2%** | **+6.3%** |
| Gradual ramp, 3/31/26 | (4.6)% | (2.4)% | +3.6% | +6.8% |

**Economic value of equity (instantaneous parallel shock):**

| Scenario | Down 200 | Down 100 | Up 100 | Up 200 |
|---|---|---|---|---|
| **6/30/26** | **+4.4%** | **+2.7%** | **(4.4)%** | **(10.5)%** |
| 3/31/26 | +5.2% | +3.1% | (4.4)% | (10.5)% |

**Assumptions the company states (carry them with the numbers — Will's WQ-318 rider: "inputs, not verdicts"):**

| Assumption | 6/30/26 | 3/31/26 |
|---|---|---|
| Non-term deposit beta (NII model) | product range **45%–86%**, **average 53%** | 46%–87%, average 55% |
| ECR-eligible deposit beta (Earnings-at-Risk model) | **70%** | 74% |
| All non-maturity deposits incl. ECRs, weighted beta (EaR) | **59%** | 62% |
| Balance sheet | **dynamic** (shock and ramp) | dynamic |
| Horizon | **12 months** | 12 months |
| Base | forward yield curves | forward yield curves |
| Limits | EaR and EVE "within the Company's current limits" | same |

**Read (factual, then labelled inference):**
- **WAL is asset-sensitive on NII**: rates up ⇒ NII up; rates down ⇒ NII down, and the **downside sensitivity grew Q1→Q2** (−200 shock −7.1% → −8.6%) while the upside was flat. Modelled deposit betas fell (53% vs 55%; ECR 70% vs 74%).
- **EVE falls when rates rise** (−4.4% at +100, −10.5% at +200) — the long-rate channel the AOCI mark sits on. With the 10Y at 5.24% intraday on 9/28 (5.11% on 9/23), this is the rate channel that can hurt at the print.
- *Inference, labelled:* the Fed's +25bp on 9/16 is, on the gradual-ramp line, roughly **+0.8% of 12-month NII** (¼ of +3.2%, linear) — a tailwind the Q2 guide already assumed (KB-117). It is **not** a forecast of the Q3 number.
- **Use at the print (§10.2):** N1 (NIM ≤ 3.47%) and N2 (deposit cost ≥ 1.88%) remain the registered tests. This table does not change them; it tells the grader which direction rates *should* push NII and EVE, so an NII/NIM miss in a rising-short-rate quarter is harder to blame on rates.

**Handed to REGINALD** (WQ-318 column 7) the same day, so both desks grade off one figure and one vintage — packet `AGENTS/REGINALD/inbox/2026-09-28_from-WAL_WQ-318-rate-sensitivity-figure.md`.

---

## 2. Dated consensus snapshot (before the print) — B-tier vendor data

**Taken:** Mon **2026-09-28 17:13 ET** (both pulls within one minute). ⛔ Vendor consensus is not a filing datum; it is recorded **dated, before the print**, because Q2 showed it cannot be reconstructed afterwards (KB-139: three contested figures).

| Item (quarter ending 9/30/26) | Nasdaq (`api.nasdaq.com/api/analyst/WAL/earnings-forecast`) | Yahoo (via yfinance `earnings_estimate` / `revenue_estimate`) |
|---|---|---|
| **EPS consensus** | **$2.43** (8 estimates; high $2.71, low $2.22) | **$2.44** (2.44476; 13 analysts; high $2.71, low $2.18) |
| EPS revisions | last 4 weeks: 0 up, **1 down** | last 30 days: 1 up, **10 down** (last 7 days: 1 up, 8 down) |
| EPS trend | — | **$2.63 (90 days ago) → $2.49 (60) → $2.45 (30, 7) → $2.44 now: −7.2% over 90 days** |
| Year-ago EPS (Q3-25) | — | $2.15 |
| **Revenue consensus** | not shown | **$989.0M** (12 analysts; $967.6M–$1,005.9M); year-ago $938.2M |
| FY2026 EPS | $9.16 (6 est.) | $8.90 (13) |
| Next quarter (Dec-26) EPS | $2.65 (7) | $2.59 (13) |
| **Charge-offs, NPLs, NIM consensus** | **UNAVAILABLE** (no free vendor publishes them) | **UNAVAILABLE** |
| Earnings date | not shown | **10/21/2026 — a VENDOR estimate, NOT an announcement** (WAL has not announced; EDGAR/IR re-checked 9/28) |

**Read:** the two vendors agree on EPS within $0.01 ($2.43/$2.44); they disagree on revision counts (their panels differ — record both, cite neither alone). The trend is **down** into the print. Q2 printed $2.36 (GAAP = adjusted, KB-149), so **$2.43-2.44 implies ~+3% QoQ**. EPS basis (GAAP vs "adjusted") is **not stated** by either vendor — the Q2 lesson (KB-149) says grade the release's own GAAP and adjusted figures against it and record the basis gap, never infer it.

---

## 3. Short interest — FINRA consolidated, A1

**Source:** FINRA Consolidated Short Interest API (`api.finra.org/data/group/otcMarket/name/consolidatedShortInterest`, symbolCode WAL), pulled 9/28 ~17:1x ET. **Reconciles to the stale row:** the 6/30 settlement (5,218,885 shares, +27.75%) is exactly KB-126's source figure.

| Settlement | Shares short | Change | Avg daily volume | Days to cover |
|---|---|---|---|---|
| 6/15 | 4,085,239 | +5.48% | 871,466 | 4.69 |
| 6/30 | 5,218,885 | +27.75% | 1,212,801 | 4.30 |
| 7/15 | 5,570,519 | +6.74% | 992,186 | 5.61 |
| 7/31 | **6,302,163** (period high) | +13.13% | 1,071,912 | 5.88 |
| 8/14 | 5,355,526 | −15.02% | 878,379 | 6.10 |
| 8/31 | 5,650,274 | +5.50% | 1,043,423 | 5.42 |
| **9/15** | **5,974,409** | **+5.74%** | 933,316 | **6.40** (series high) |

**Ratios (state the basis):** 9/15 short interest = **5.48% of shares outstanding** (÷ 109,100,864, the 7/28 10-Q cover, KB-200) · ≈ **5.62% on KB-126's float basis** (≈106.3M, *derived* as 5,218,885 ÷ 4.91% — the float figure itself was never recorded) · **+14.5% vs 6/30**. **Next settlement: 9/30 (published ~10/9).**

**Read:** shorts rose into Q2, peaked 7/31, dipped mid-August, and have rebuilt for two straight settlements. **Days to cover 6.4 is the highest in the series** — more crowded than at the Q2 print (4.30). That feeds WEAKNESSES' squeeze/crowding row (a benign print meets more shorts). Not a thesis signal on its own.

---

## 4. One-line strike map for the Dec-18 $70P (in the print frame §9, non-gating)

v2.4 ranges (SCENARIOS §EV SUMMARY): the $70 strike is **in the money** in Bear-fast ($52-62), Bear-medium ($58-66) and Tail ($35-45) = **25% combined weight**, and **out of the money** across Base ($74-82) and Bull ($86-94) = 75%. *The scenarios are thesis-horizon states, not a Dec-18 forecast.* No position action — TERRY/Will lane (exit letter on TERRY's card; time stop 12/04; the $4.40 GTC is cancelled).

---

## Raw captures (for reproducibility)

- **Nasdaq JSON (quarterly row):** `{"fiscalEnd":"Sep 2026","consensusEPSForecast":2.43,"highEPSForecast":2.71,"lowEPSForecast":2.22,"noOfEstimates":8,"up":0,"down":1}` · Dec 2026 2.65/2.86/2.43/7 · FY Dec 2026 9.16/10.05/8.45/6.
- **yfinance `earnings_estimate` 0q:** avg 2.44476 · low 2.18080 · high 2.710 · yearAgoEps 2.15170 · n 13. `revenue_estimate` 0q: avg 989,029,160 · low 967,643,470 · high 1,005,900,000 · n 12 · yearAgo 938,200,000. `eps_trend` 0q: current 2.44476 · 7d 2.45099 · 30d 2.45099 · 60d 2.49266 · 90d 2.63361.
- **FINRA rows:** as tabled above (fields: settlementDate, currentShortPositionQuantity, changePercent, averageDailyVolumeQuantity, daysToCoverQuantity; revisionFlag null on all).
- **10-Q text:** the two tables and the beta sentences are quoted from Item 3 as printed.
