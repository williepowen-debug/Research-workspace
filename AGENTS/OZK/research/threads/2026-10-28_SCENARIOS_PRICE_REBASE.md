# SCENARIOS price-range re-base on Q3-26 EPS/TBV — PROPOSED (P-OZK-9)

**Date:** 2026-10-28 (OZK, Will-approved work item "1 2 3 all approved go ahead", 22:44 ET; the resulting EV goes back to Will before it is encoded in `SCENARIOS.md`).
**Owed since:** 2026-10-22 (P-OZK-8 re-weighted the scenarios on the unchanged 4/23 price midpoints $34 / $43 / $56 / $21.50; `SCENARIOS.md` line 31 marked the re-base as a separate step).
**Scope:** inputs only. Weights (Bear 20 / Base 50 / Bull 28 / Tail 2, P-OZK-8) and each scenario's own valuation multiple band are **unchanged**. OZK-09 (45%), A30/B45/C8/D17 and ~$129M EL are untouched.

## 1. Inputs (all Q3-26 primary, FDIC FLNG 12022 unless stated)

| Input | Value | Source |
|---|---|---|
| Diluted EPS Q3-26 | $1.50 (≈$6.00 annualized, DERIVED) | MC p.3 / press release |
| Net income to common Q3 | $164.3M | Appendix A |
| PPNR Q3 / 9M | $261.4M / $774.4M (run rate ≈$1,030–1,045M/yr, DERIVED) | Appendix A |
| Provision Q3 | $47.8M | Appendix A |
| Preferred dividends | $4.05M/qtr ($16.2M/yr) | Appendix A |
| Effective tax rate | 21.2% Q3; **22–23% guided for FY26–27** (model uses 22.5%) | MC "Effective Tax Rate" |
| Common dividend | $0.48 Q3; rises each quarter (65 straight) → model $1.96 next 12 months | Equity statement; MC "Dividends" |
| Shares outstanding | 108,398K at 9/30; buybacks 0.65M in Q3 + 0.52M Oct 1–19 → model 107.5M average | Appendix A; MC "Stock Repurchase" |
| TBV per share | **$47.50** (BV $53.59) | Appendix A |
| Q3 tie-out | (261.4 − 47.8) × (1 − 0.212) − 4.05 = **$164.3M** = reported NI to common ✓ | DERIVED |

## 2. Method

For each scenario, over a **12-month horizon (to ~Q3-27)**:

`EPS = ((PPNR − provision − OREO marks) × (1 − 22.5%) − $16.2M) ÷ 107.5M`
`End TBV = $47.50 + EPS − $1.96 dividends` (AOCI held flat; buybacks near 1.0× TBV treated as neutral)
`Price = the scenario's own multiple band (unchanged from the scenario body) × end TBV`

The old ranges mixed horizons (Bull on then-current TBV, Base/Bear on an end-state TBV). The re-base uses one horizon for all four; the today's-TBV figures are shown beside them so the horizon effect is visible.

## 3. Scenario assumptions and results

| Scenario | Credit path (12 mo) | EPS | End TBV | Multiple (unchanged) | **Price range** | **Mid** | On today's TBV |
|---|---|---|---|---|---|---|---|
| **Bear** | NCO $80–120M/qtr + $100–200M reserve build (provision $420–680M) + OREO sold/marked down $80–130M (≈20–30% of $420M) | $1.22–3.78 | $46.76–49.32 | 0.70–0.90× | **$33–44** | **$38.56** | $33–43 |
| **Base** | NCO $40–70M/qtr ("elevated through 2027", MC p.21; Q3 $44.5M), provision $180–300M | $5.04–6.09 | $50.58–51.63 | 0.85–0.95× | **$43–49** | **$46.02** | $40–45 |
| **Bull** | NCO $30–50M/qtr, provision $120–200M | $5.94–6.52 | $51.48–52.06 | 1.10–1.30× | **$57–68** | **$62.15** | $52–62 |
| **Tail** | $1.0–1.5B pre-tax losses beyond what earnings absorb; dilutive raise ignored (would lower further) | ~0 | $36.69–40.29 | 0.50–0.65× | **$18–26** | **$22.00** | — |

## 4. Expected value

| | Old (P-OZK-8, 4/23 midpoints) | **Re-based (proposed)** |
|---|---|---|
| Bear 20% | $34.00 | $38.56 |
| Base 50% | $43.00 | $46.02 |
| Bull 28% | $56.00 | $62.15 |
| Tail 2% | $21.50 | $22.00 |
| **EV** | **$44.41** | **$48.56** |
| vs 10/28 close $50.51 | price 13.7% above EV | **price 4.0% above EV** |

**What moved it:** four quarters of retained earnings (~$4/share in Base and Bull) on a TBV that is already $0.35 above the Q1 base ($47.15), plus the Base EPS band rising from $4.75–5.75 to $5.04–6.09 because Q3 printed $6.00 annualized with NCO already at the "elevated" level. **What did not move it:** the weights and every multiple band.

## 5. Separate judgement NOT folded in (flag for Will, no change proposed)

The **Base multiple band 0.85–0.95× TBV sits below the market's own range for OZK** over the last 12 months: price ~$41–53 (KB-214 range) on TBV $45.23 (Q3-25) → $48.41 (Q2-26) is roughly **0.9–1.15×**, and 1.06× today. If Base used 0.95–1.05×, Base mid → $51.13 and **EV → $51.12** (price ~1% below EV). Changing a multiple is a method change, not a re-base, so it is shown as sensitivity only.

## 6. Limits

- Every scenario is a desk model on management's own run rate; PPNR could drift with NIM (sub-notes reset ≈+$12.0M/yr cost from Q4, already inside the PPNR range).
- OREO marks in the Bear path are a desk assumption (Boston 10 Prospect took a $37.3M charge-off on the way into OREO at 80% of its Sept as-is value; no OREO sale was priced in Q3).
- Tail ignores the dilution of a forced raise; the range is a ceiling for that branch.
- Nothing here is a trade view. Trades are TERRY → Will (root rule #5).
