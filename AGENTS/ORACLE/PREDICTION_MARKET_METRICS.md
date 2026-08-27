# ORACLE Prediction Market Metrics

**Created:** 2026-06-21 · **Implementation added 2026-08-27: `tools/metrics.py`** (`entropy` | `collapse` | `kl` | `verify`)  
> ⚠️ **This document specified a measurement layer for 67 days with NO code behind it.** Every σ ORACLE published in that window was hand-computed, therefore unauditable — and when the tool was finally built and pointed at ORACLE's own record, **three of five published σ turned out to be unreachable at any rolling window** and two threshold classifications were withdrawn (KB-ORC-064 → `CORRECTED`, KB-ORC-074). The dH and entropy figures reproduced exactly; only the significance scores failed. **Do not publish a derived score from this document without running `tools/metrics.py`.** Reproduce the audit: `python3 tools/metrics.py verify`.
> ⚠️ **σ here RANKS unusualness within one series. It is not a p-value.** ORACLE's pull cadence is irregular (1–9 days), so a rolling std over mixed intervals is not a frequentist object. The tool prints its interval spread, annotates each σ with the gap-days behind its dH, and refuses to quote σ below n=8.  
**Purpose:** reusable measurement layer for prediction-market monitoring. These are research/triage tools, not auto-trading rules.

---

## Core Rule

ORACLE measures crowd pricing, dislocations, liquidity, and anomalies. ORACLE does **not** execute trades.

If a market looks actionable:

1. ORACLE flags the market and evidence.
2. Domain agent / NEXUS assesses reality.
3. TERRY evaluates tradeability, sizing, and execution blockers.
4. Will approves/rejects. No auto-trading.

---

## 1. Required Fields For Any Market Read

| Field | Meaning |
|---|---|
| Platform | Polymarket, Kalshi, etc. |
| Market name / slug | exact contract identity |
| Resolution criteria | exact event definition; ambiguity risk noted |
| p_market | market-implied probability, adjusted for spread/fees when possible |
| Price timestamp | when odds were pulled |
| Volume | total / recent volume if available |
| Liquidity / order book depth | whether edge is executable or fake |
| Δ1d / Δ7d | recent probability movement |
| Thesis owner | domain agent or NEXUS if comparing to our view |
| p_model / p_thesis | our probability estimate, if one exists |
| Gap | p_model - p_market |
| Metrics | entropy, KL bits, anomaly flags where applicable |

If liquidity/resolution criteria are unclear, mark the read as **diagnostic only**.

---

## 2. Entropy — Uncertainty Score

For a binary market:

```text
H(p) = -p log2(p) - (1-p) log2(1-p)
```

Interpretation:

| Entropy | Meaning |
|---|---|
| ~1.0 bit | maximum uncertainty; market near 50/50 |
| falling entropy | market becoming more certain |
| near 0 | market almost resolved / one-sided |

Use:
- identify markets where new information still matters.
- detect sudden certainty shifts.
- avoid overinterpreting markets already priced near 0/100 unless liquidity is deep and resolution risk is low.

Caveat:
- low entropy is not itself edge; it may simply mean the crowd is right or the market is stale.

---

## 3. KL Divergence — Dislocation / Attention Score

For binary market comparison between our estimate `P` and market estimate `Q`:

```text
D_KL(P || Q) = p_model * log2(p_model / p_market)
             + (1-p_model) * log2((1-p_model) / (1-p_market))
```

Use KL as an **attention ranking**, not a profit estimate.

| KL bits | Read |
|---|---|
| <0.03 | probably noise / too small |
| 0.03–0.10 | worth watching if liquidity/depth is real |
| 0.10–0.20 | meaningful dislocation; needs source/liquidity check |
| >0.30 | either huge edge or bad p_model / bad market / resolution mismatch; audit before routing |

Critical caveats:
- KL is not EV.
- KL is asymmetric; use `D_KL(our_estimate || market_price)` for our-dislocation scoring.
- Clip probabilities away from 0/1 for math stability.
- A large KL in a dead/thin/ambiguous market is not tradeable edge.

ORACLE should report both:

```text
gap_pp = p_model - p_market
kl_bits = D_KL(p_model || p_market)
```

---

## 4. Tradeable Edge Requires Discounts

Before ORACLE routes anything toward TERRY, apply these sanity filters:

```text
raw_gap = p_model - p_market
tradeable_gap = raw_gap
                - spread_cost
                - fee_cost
                - liquidity_discount
                - resolution_risk_discount
                - model_uncertainty_discount
```

If `tradeable_gap <= 0`, route as **interesting diagnostic**, not trade candidate.

ORACLE should not size. TERRY sizes.

---

## 5. Entropy Collapse / Anomaly Alert

A sudden drop in entropy can indicate:

- information leakage / informed order flow
- whale positioning
- delayed public-news ingestion
- manipulation in a thin book
- resolution/market-criteria confusion

Compute:

```text
H_t = entropy(price_t)
dH = H_t - H_(t-1)
alert if abs(dH) > k * rolling_std(dH)
```

Default:
- interval: 5–15 minutes if available, otherwise use available pulls.
- threshold: `k = 3` as watch, `k = 5` as urgent.

Alert template:

```text
ENTROPY_COLLAPSE_ALERT
Market: [platform / slug]
Price: [from → to]
Entropy: [from → to]
Move: [Δpp over time]
Volume/liquidity: [values]
Public news found? [yes/no/unknown]
Read: [informed flow / whale / thin-market noise / news reaction]
Route: [PROME / WALTER / domain agent / TERRY]
```

Guardrail:
- entropy collapse is an alert, not proof of insiders.
- require public-news check and liquidity context before escalating as informed-flow signal.

---

## 6. Signal Fusion — Keep It Humble

Weighted signal fusion is useful, but do not over-market it as magic “max entropy.”

Practical approach:

```text
p_fused = weighted average of signals
weights = source reliability / freshness / directness / historical calibration
```

Required disclosure:

| Component | Example |
|---|---|
| base rate | historical event frequency |
| market price | current p_market |
| domain-agent view | HAWK/BRENT/REGINALD/etc. estimate |
| recent news | WALTER/domain update |
| liquidity quality | confidence haircut |

Output:

```text
p_fused = X%
confidence = low/medium/high
biggest driver = [source]
biggest uncertainty = [source]
```

Do not pretend a weighted blend is proof. It is a disciplined estimate.

---

## 7. Routing Rules

| Condition | Route | Priority |
|---|---|---|
| KL >0.10 bits and liquidity real | NEXUS + relevant domain agent | 🟠 |
| KL >0.20 bits and thesis owner has high confidence | NEXUS + RED + domain agent | 🔴 |
| entropy collapse >3σ with real volume | PROME + WALTER + domain agent | 🔴 |
| entropy collapse >5σ and no public news | PROME urgent triage | 🔴🔴 |
| p_market moves >10pp in 48h | existing ORACLE rule: PROME triage | 🔴 |
| tradeable_gap positive after discounts | TERRY for tradeability review | 🟠/🔴 depending on size |

---

## 8. TERRY Handoff Packet

When routing to TERRY, include:

```markdown
# ORACLE → TERRY Prediction Market Review

**Market:** [platform / slug / exact title]
**Resolution criteria:** [exact wording]
**p_market:** [price, timestamp]
**Liquidity / spread:** [values]
**Volume:** [values]
**p_model / thesis owner:** [estimate + source]
**Gap:** [pp]
**KL bits:** [value]
**Entropy:** [current H]
**Entropy anomaly:** [none / watch / alert]
**Tradeable-gap adjustment:** [spread/fees/liquidity/resolution/model uncertainty]
**Why this may matter:** [one paragraph]
**Why this may be fake edge:** [one paragraph]
**Request:** TERRY tradeability review only; no execution.
```

---

## 9. Minimal Python Reference

```python
import math

EPS = 1e-6

def clip(p):
    return min(max(float(p), EPS), 1 - EPS)

def entropy_bits(p):
    p = clip(p)
    q = 1 - p
    return -(p * math.log2(p) + q * math.log2(q))

def kl_bits(p_model, p_market):
    p = clip(p_model)
    m = clip(p_market)
    q = 1 - p
    qm = 1 - m
    return p * math.log2(p / m) + q * math.log2(q / qm)
```

---

## 10. Anti-Patterns

Do not:

- treat KL bits as profit.
- trade top-K dislocations automatically.
- ignore spread, fees, liquidity, and resolution ambiguity.
- call every entropy collapse “insider trading.”
- size from full Kelly.
- use stale p_model estimates without source/date.
- let prediction markets override domain evidence without RED/NEXUS adjudication.

Prediction markets are a signal surface, not an oracle despite the agent name.
