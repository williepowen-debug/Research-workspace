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
| **Independence** | **How many of the supporting legs are genuinely independent?** | **`N_eff` stated, with the shared antecedent named — see §2b** |
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

## 2b. EFFECTIVE-N — the independence discount

**Adopted 2026-07-26, Will-approved.** Source grade: `research/SIGNAL_COMBINATION_2026-07-26.md` **SC-03**. Fleet sibling: **NEXUS's Discipline F** (same insight, reached independently).

**The rule:**

> **Size to the number of *independent* views, never to the number of reasons you can list.**

Every actionable card states three things before sizing:

```text
N_claimed          = how many separate legs/reasons support this
shared antecedent  = the ONE event or fact that kills more than one at once
N_eff              = the honest independent count (+ one line of reasoning)
```

**Why it binds.** The Fundamental Law of Active Management gives combined risk-adjusted edge as `IR = IC × √N` — but **N is the *effective independent* count, not the signal count.** Legs that die to the same falsifier are one view wearing several hats. Sizing as though they were several is the specific mechanism behind *"I was right about the direction and still lost badly."*

**The worked example is our own book, not a textbook.** The regional-bank put basket — KRE ≈ −$2,225, OZK ≈ −$1,641, WAL ≈ −$1,425, **≈ −$5,291 total** — is three legs sharing **one** falsifier (regional-bank credit doesn't crack). `N_claimed = 3`, `N_eff ≈ 1.2`, sized as 3.

**Two honest limits on the rule, so it isn't over-applied:**
1. **Multi-leg expression of one thesis can be legitimate** — it diversifies idiosyncratic timing and single-name defense. The error is not owning three legs; it is **sizing three legs as three views.**
2. **This is not the only mechanism.** That same basket's loss came primarily from the 7/17 tenor/depth diagnosis (a slow-grind thesis in deep-OTM crash instruments). **Correlation set the size; tenor set the decay.** Both were live. Do not let `N_eff` become the single explanation for every loss.

**Applies to the book, not just the card:** before sizing, ask whether this card shares a falsifier with a position already on. If it does, the *combined* exposure is the number that matters — state it as one number, not as separate trades.

**Practical consequence for this desk:** we are **low-breadth by design** (~10–15 independent decisions a year). The Law says our IR is structurally capped by breadth regardless of process quality — so **our edge must come from payoff asymmetry (cheap convexity on dated catalysts), not from stacking more signals.** Adding correlated inputs raises `N_claimed` while leaving `N_eff` flat. **The productive direction is auditing independence, not manufacturing signals.**

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
- 🔴 **REJECTED variant — do not adopt `f = f_kelly × (1 − CV_edge)`** ("empirical Kelly", graded **SC-05** 2026-07-26). Its shrinkage *direction* is right and already ours, but its *level* is looser than our cap: at a plausible `CV_edge = 0.5` it yields **0.5× Kelly = twice our ceiling**, and it only becomes more conservative than 0.25× above `CV_edge > 0.75`. **Monte-Carlo framing makes a more aggressive rule read as a more rigorous one.** The 0.25× cap stands and takes precedence over any externally-sourced Kelly adjustment.
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
