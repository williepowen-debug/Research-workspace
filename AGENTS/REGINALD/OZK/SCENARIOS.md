# OZK — Scenario Analysis & Target Prices
**Created:** 2026-03-23 | **Last Updated:** 2026-03-25
**Current Price:** $44.70 (Finviz Mar 25) | **TBV:** $46.48 | **Book:** $52.46 | **P/TBV:** 0.96x
**Short Interest:** 13.81% float, 11.20 days to cover (KB-OZK-160)

> **Framing note:** Probabilities are scenario weights for position sizing. High-conviction directional thesis + 50% bear weight = expected value strongly favors the short even at coin-flip odds.

---

## EXPECTED VALUE SUMMARY

| Scenario | Prob | Price Range | Midpoint | Weighted |
|----------|------|-------------|----------|----------|
| Bear | **50%** | $28-35 | $31.50 | $15.75 |
| Base | **30%** | $37-44 | $40.50 | $12.15 |
| Bull | **15%** | $52-62 | $57.00 | $8.55 |
| Tail | **5%** | $16-24 | $20.00 | $1.00 |
| **Expected Value** | | | | **$37.45** |

**Current $44.70 → implied ~16% overvaluation vs EV of $37.45.**

---

## SCENARIO A: BEAR CASE (50%)

**Thesis:** Interest reserve depletion + 2022 vintage maturity wall forces nonaccrual wave Q1-Q3 2026. Charge-offs exceed provisioning. Market reprices to stressed bank multiple.

**Mechanics:**
1. Construction maturity wall hits Q1-Q3. Borrowers can't refi or stabilize. Interest reserves deplete.
2. Noncurrent rises to $600-800M by Q3 (from $341M). Plausible: $322M additions in last 6 months, wall hasn't fully arrived.
3. Charge-offs accelerate to $80-120M/quarter.
4. ACL consumed: $475.7M erodes to $300-350M.
5. EPS compresses from $6.18 to $3-4 range on provision catch-up.

**TBV Impact:**
- Cumulative excess charge-offs: $100-200M over 2-3 quarters
- TBV erosion: $46.48 → $42-43 (moderate) to $37-38 (if IQHQ partially written)
- IQHQ partial writedown ($100-150M) pushes TBV to ~$37-39

**Valuation:**
- Stressed CRE bank: 0.7-0.9x eroded TBV (~$37-43)
- **Bear target: $28-35**
- Deep bear (IQHQ + systemic): $25-28

**Why 50%:** 89.7% of construction on interest reserves is administered, not organic. Market reads "low construction noncurrent" as health — it's artifice. Q4 noncurrent spike was the leading edge. Maturity wall is mechanical, not probabilistic.

**Rate relief doesn't help much:** Stress is concentrated in office/life sci (75% of noncurrent) where the bottleneck is vacancy, not borrowing cost. Moderate rate cuts reduce bear probability by ~5% at most.

---

## SCENARIO B: BASE CASE (30%)

**Thesis:** Management provisions just enough to stabilize ACL. Charge-offs elevated but contained. No IQHQ resolution. Slow grind lower.

**Mechanics:**
1. Q1 charge-offs: $60-80M. Provision roughly matches.
2. Noncurrent rises to $400-500M then plateaus.
3. EPS compresses to $4.50-5.50.
4. Dividend maintained under scrutiny.
5. IQHQ extended to 2028 — deferred, not resolved.

**TBV Impact:** Minimal erosion, stays $44-47.

**Valuation:**
- Uncertain CRE bank: 0.85-0.95x TBV
- **Base target: $37-44**
- Current $44.70 = top of base range. Limited upside, limited downside.

---

## SCENARIO C: BULL CASE (15%)

**Thesis:** CRE stabilizes, management rebuilds ACL, short squeeze amplifies recovery.

**Mechanics:**
1. IQHQ lands significant tenant (unlikely at 25-29% SD vacancy)
2. Rate cuts enable construction loan refis — maturity wall softened
3. Charge-offs normalize to $30-40M/quarter
4. EPS recovers to $5.50-6.00

**Valuation:**
- Recovering bank: 1.1-1.3x TBV ($48-50 TBV)
- **Bull target: $52-62**
- Squeeze overshoot: $58-65 temporarily (13.81% SI, 11.2 days to cover)

**This is the loss scenario for puts.** Size to survive a squeeze to $55 without panic.

---

## SCENARIO D: TAIL — CAPITAL EVENT (5%)

**Thesis:** Cascading losses → rating downgrade → deposit flight → forced capital raise.

**Mechanics:**
1. Multiple large loans go nonaccrual simultaneously
2. ACL breached, provision surge crushes earnings to near-zero
3. KBRA/Moody's downgrade (KBRA already Negative outlook)
4. Uninsured deposit flight: $11.9B uninsured (35.8%), 2.2x Tier 1
5. Forced dilutive equity raise

**Valuation:**
- **Tail target: $16-24** (0.5-0.65x deeply eroded TBV)

---

## EPS SENSITIVITY — THE REAL TRADE

The thesis is earnings compression, not bank failure. Capital buffer is ~$2B+ above well-capitalized minimums.

| EPS | P/E 7x (current) | P/E 6x (stressed) | P/E 5x (crisis) |
|-----|-------------------|--------------------|--------------------|
| $6.18 | $43 | $37 | $31 |
| $5.00 | $35 (-22%) | **$30 (-33%)** | $25 (-44%) |
| $4.00 | $28 (-37%) | **$24 (-46%)** | $20 (-55%) |
| $3.00 | $21 (-53%) | $18 (-60%) | $15 (-66%) |

Bear case needs EPS ~$5.00 at 6x → **$30** (-33% from $44.70).

---

## PUT EXPECTED VALUE AT $44.70

### Aug $45 Put (4 contracts) — Core Position
| Scenario | Prob | Stock | Intrinsic | Weighted |
|----------|------|-------|-----------|----------|
| Bear ($31.50) | 50% | $31.50 | $13.50 | $6.75 |
| Base ($40.50) | 30% | $40.50 | $4.50 | $1.35 |
| Bull ($57.00) | 15% | $57.00 | $0.00 | $0.00 |
| Tail ($20.00) | 5% | $20.00 | $25.00 | $1.25 |
| **EV** | | | | **$9.35** |

At ~$4.05 cost basis (last add), **EV = 2.3x risk.** Positive EV with defined max loss.

### May $42.5 Put (2 contracts) — Catalyst Bet
| Scenario | Prob | Stock at Exp | Intrinsic | Weighted |
|----------|------|-------------|-----------|----------|
| Bear (partial by May) | 35% | $36 | $6.50 | $2.28 |
| Base | 35% | $42 | $0.50 | $0.18 |
| Bull | 20% | $50 | $0.00 | $0.00 |
| Tail | 10% | $30 | $12.50 | $1.25 |
| **EV** | | | | **$3.70** |

Tight timeline — needs Apr 16 earnings to catalyze. Positive EV but narrower margin.

### Aug $42.5 Put (1 contract) — Deep Bear
EV similar to Aug $45 but lower delta. Profits only in bear/tail. Pure downside bet.

---

## SQUEEZE RISK

- **13.81% short float, 11.20 days to cover** — heavily crowded
- Any positive catalyst (earnings beat, IQHQ tenant, rate cut signal) could trigger 10-15% squeeze
- Size positions to survive $50-55 without forced exit
- Aug expiry provides runway to survive squeeze and still catch maturity wall
- **Rule: don't add on green days.** Squeeze risk is highest when stock is already moving up.

---

## WHY MARKET IS MISPRICING

1. **Interest reserve artificiality invisible** — 89.7% administered, deep in Call Report, no analyst covers it
2. **Noncurrent spike read as one-off** — market doesn't see maturity wall pipeline behind it
3. **C&I reclassification flatters CRE ratios** — 37.6% MI3 not discussed by sellside
4. **Record EPS $6.18 anchors narrative** — earnings lag credit reality by 2-3 quarters
5. **"CIB diversification" narrative** — NDFI counterparties are overwhelmingly CRE debt funds
6. **Exit counterparty risk invisible** — Blue Owl gated, Affinius bonds at 81¢ with Oct 2026 deadline

---

## APRIL 16 DECISION FRAMEWORK

| Outcome | Action |
|---------|--------|
| Noncurrent >$450M + provision < charge-offs | Hold all, consider adding Aug. Bear accelerating. |
| Noncurrent $350-450M, provision ≈ charge-offs | Hold Aug, evaluate May. Base case grinding. |
| Noncurrent <$350M, charge-offs declining | Trim May, hold Aug with tighter stop. Watch for thesis break. |
| Positive surprise + squeeze to $50+ | DO NOT PANIC. Aug has runway. May is the risk — accept loss or roll. |
| IQHQ writedown announced | Add aggressively. This is the catalyst. |
| Management announces capital raise or div cut | Add aggressively. Tail risk confirming. |

---

*KB evidence: 160 rows | Thesis: `THESIS.md` | Weaknesses: `WEAKNESSES.md`*
