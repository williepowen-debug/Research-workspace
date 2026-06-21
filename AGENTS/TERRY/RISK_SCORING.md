# TERRY Risk Scoring + Calibration

**Created:** 2026-06-21  
**Purpose:** turn thesis conviction into disciplined trade sizing, risk gates, and postmortem learning without giving TERRY execution authority.

---

## Core Rule

TERRY may estimate edge and propose structure. TERRY never executes.

Every actionable output still ends with:

> **APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## 1. Pre-Trade Risk Checklist

Before a trade card can be marked `PROPOSED`, answer these:

| Gate | Question | Required answer |
|---|---|---|
| Thesis owner | Who owns the underlying truth? | NEXUS/domain agent/Will, with file/source |
| Edge | What is mispriced or mistimed? | explicit edge claim, not vibes |
| Catalyst | What forces repricing before time stop? | date/event/threshold |
| Entry | Where is entry acceptable? | trigger + no-chase level |
| Structure | Why this instrument/expiry/strike/spread? | structure beats alternatives |
| Max loss | What is the maximum acceptable loss? | $ / % portfolio / R unit |
| Invalidation | What proves the trade wrong? | price, thesis, time, or event |
| Liquidity | Can we enter/exit without stupid spread cost? | bid/ask, OI/volume, or [CHAIN_NEEDED] |
| Event risk | What gap/catalyst risk can bypass stops? | known and sized |
| Position truth | Does existing exposure matter? | broker/Will truth or `[POSITION_STATE_UNKNOWN]` |

If any gate is missing, output `CONDITIONAL` or `NO TRADE`, not `PROPOSED`.

---

## 2. Edge Score

For directional trades:

```text
edge_score = expected_return / max_loss
```

For probability / prediction-market style trades:

```text
edge = p_model - p_market
EV = p_model * payoff_if_right - (1 - p_model) * loss_if_wrong
```

For options:

```text
edge must beat spread + theta + event-vol risk
```

TERRY should state edge qualitatively unless inputs are real:

| Score | Meaning | Action |
|---|---|---|
| Negative / unclear | no measurable edge | NO TRADE |
| Small | edge exists but fragile | watch / tiny only |
| Moderate | edge + catalyst + structure align | possible proposed card |
| Strong | edge + catalyst + cheap structure + clear invalidation | high-quality setup, still approval required |

Never invent a precise p_model. If probability is subjective, label it subjective.

---

## 3. Fractional Kelly Reference

Kelly is a sizing reference, not an instruction.

Binary approximation:

```text
f* = (p*b - q) / b
where:
p = probability of win
q = 1 - p
b = payoff odds net of stake
```

TERRY policy:

- never recommend full Kelly.
- default cap: **0.25x Kelly or lower**.
- final size is the smaller of:
  1. fractional Kelly estimate,
  2. max loss budget,
  3. liquidity/spread capacity,
  4. event-risk cap.

If edge estimate is uncertain, shrink sizing aggressively or mark `NO TRADE`.

Suggested language:

> Kelly-implied size is X, but because edge confidence is low and event risk is high, Terry caps this at Y max loss.

---

## 4. Execution Block

TERRY should explicitly block action when any of these are missing:

```text
EXECUTION BLOCKED unless:
- Will approves
- max loss is defined
- invalidation is defined
- entry/no-chase rule is defined
- liquidity/option chain is acceptable or explicitly verified by Will
- position truth is known if existing exposure matters
```

If the setup involves prediction markets or on-chain venues, add:

```text
- venue/liquidity/resolution rules checked
- fees/slippage included
- counterparty/oracle/resolution risk understood
```

---

## 5. Calibration / Brier Tracking

For probability-like calls, record the forecast before outcome:

| Field | Meaning |
|---|---|
| Setup ID | ticker/market/date |
| Forecast | p_model or subjective probability |
| Market price | p_market if applicable |
| Outcome | 1 if event occurred, 0 if not |
| Brier | `(forecast - outcome)^2` |
| Lesson | overconfident, underconfident, right thesis/wrong timing, etc. |

Brier score:

```text
Brier = (p_forecast - outcome)^2
```

Lower is better. This is for humility and calibration, not leaderboard theater.

Possible future file if used often:

`AGENTS/TERRY/CALIBRATION.tsv`

Do not create a calibration row unless a probability was stated before the outcome.

---

## 6. Postmortem Taxonomy

Every closed/dead trade review should classify the failure or success:

| Dimension | Questions |
|---|---|
| Thesis | Was the underlying thesis right? Was owner-agent evidence good? |
| Timing | Did repricing happen inside the selected window? |
| Structure | Was the instrument/expiry/strike/spread appropriate? |
| Sizing | Was max loss appropriate? Did position size cause bad behavior? |
| Entry | Did we chase? Did entry violate plan? |
| Exit | Did we follow invalidation/target/time stop? |
| Liquidity | Did spread/slippage matter? |
| Vol/theta | Did IV crush or theta kill the trade? |
| Process | Was approval, source verification, or position truth missing? |

Loss cause tags:

```text
BAD_THESIS
BAD_TIMING
BAD_STRUCTURE
OVERSIZED
CHASED_ENTRY
MISSED_EXIT
LIQUIDITY_COST
IV_CRUSH
THETA_DECAY
POSITION_TRUTH_MISSING
RULE_VIOLATION
GOOD_LOSS_PROCESS_WORKED
```

---

## 7. Prediction Market / ORACLE-Specific Add-On

ORACLE owns the prediction-market metric layer:

- `AGENTS/ORACLE/PREDICTION_MARKET_METRICS.md`

If TERRY reviews ORACLE/prediction-market ideas, require ORACLE’s handoff packet or equivalent data:

Require:

- exact market question and resolution criteria
- market price / order book / liquidity
- modeled probability and source confidence
- time to resolution
- fees/slippage
- maximum stake
- dispute/oracle/resolution risk

Mispricing template:

```text
p_market = market price adjusted for fees/spread
p_model = thesis-owner probability estimate
edge = p_model - p_market
kl_bits = ORACLE dislocation / attention score
tradeable_edge = edge - spread_cost - fee_cost - liquidity_discount - resolution_risk_discount - model_uncertainty_discount
```

If `tradeable_edge <= 0`, no trade. KL bits can prioritize review, but cannot make a trade executable by itself.

Entropy / anomaly guardrail:

- entropy collapse may indicate informed flow, whale activity, delayed public news, manipulation, or resolution confusion.
- TERRY must not treat an entropy-collapse alert as tradeable without liquidity, public-news, and resolution checks.

Guardrail:

> Prediction-market prices are not dumb money by default. Treat “mispricing” as a hypothesis requiring evidence, not a discovered fact.

---

## 8. TERRY Output Standard

For any actionable proposal include:

```text
Terry verdict: CLEAN / CONDITIONAL / NO TRADE
Edge: [qualitative or quantified]
Sizing: [max loss and Kelly-informed cap if applicable]
Execution status: BLOCKED until Will approval
```

TERRY should prefer a clean `NO TRADE` over a clever but underspecified idea.
