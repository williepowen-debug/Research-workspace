# SHARED VOCABULARY

**Purpose:** Common terminology across all agents. Ensures syntactic boundary crossing—everyone uses the same words to mean the same things.

**Last Updated:** 2026-01-19

---

## Status Levels

All agents use these status levels consistently:

| Status | Definition | Action Implication |
|--------|------------|-------------------|
| **NORMAL** | Below threshold, no concern | Routine monitoring |
| **ELEVATED** | Approaching threshold, notable | Increased attention |
| **CRITICAL** | At or near threshold, high concern | Active monitoring, prepare response |
| **BREACHED** | Tripwire crossed | Immediate attention, escalate |

---

## Recommended Action Levels (State Vectors)

When subordinates report to CARL:

| Action | Definition | CARL Response |
|--------|------------|---------------|
| **IGNORE** | Signal noted but not relevant to current focus | Log receipt, no integration |
| **WATCH** | Signal worth monitoring, not yet actionable | Add to watch list, note in ML |
| **INCORPORATE** | Signal should factor into assessment | Integrate into thesis evaluation |
| **ESCALATE** | Signal is urgent or contradicts thesis | Immediate review, confidence reassessment |

---

## Phase Model (CARL)

```
Stage 1: Inflation Squeeze    → Cost shock exceeds income growth
Stage 2: Credit Exhaustion    → Savings depleted, credit buffers used
Stage 3: Collateral Default   → Cannot service debt, assets liquidate
Stage 4: Banking Transmission → Consumer losses hit financial institutions
```

---

## Confidence Levels

| Range | Interpretation |
|-------|----------------|
| 90-95% | Near certain (never claim 100%) |
| 75-89% | High confidence |
| 50-74% | Moderate confidence |
| 25-49% | Low confidence |
| <25% | Highly uncertain |

Always include **reasoning** with confidence scores.

---

## Diagnostic Value

How much evidence discriminates between hypotheses:

| Level | Definition | Example |
|-------|------------|---------|
| **HIGH** | Strongly favors one hypothesis over others | "Subprime accelerating while prime stable" |
| **MEDIUM** | Somewhat favors one hypothesis | "Delinquency rising" |
| **LOW** | Weakly discriminates | "Consumer spending flat" |
| **ZERO** | Consistent with all hypotheses equally | "Fed watching data carefully" |

**Prioritize HIGH diagnostic value evidence.**

---

## Core Concepts

### K-Shape Bifurcation
Economic divergence where upper-income households maintain spending/stability while lower-income households deteriorate. **Masks aggregate stress** — headline numbers look stable while foundation crumbles.

### Zombie Borrower
A borrower making only minimum payments—technically current but functionally insolvent. At high APRs, minimum payments cover almost no principal. Will transition to default when liquidity fully exhausted.

### Cockroach Thesis
"When you see one cockroach, there are probably more." Applied to lender failures—visible failures indicate broader hidden deterioration in the sector.

### Front-Loading Paradigm
The thesis that consumer stress LEADS economic downturns (inverted from traditional sequence where recession → unemployment → consumer stress).

### Buffer Exhaustion
When financial buffers (savings, credit availability, gig income, family support) are depleted, leaving no cushion before default.

---

## Domain-Specific Terms

### CARL (Consumer Credit)
- **DQ:** Delinquency
- **60+ DQ:** 60+ days delinquent (serious delinquency)
- **Charge-off:** Debt written off as uncollectible
- **Utilization:** Credit used / credit available

### POLLY (Insurance)
- **Combined Ratio:** (Losses + Expenses) / Premiums — over 100% = unprofitable
- **Loss Ratio:** Claims paid / Premiums earned
- **Lapse Rate:** Policies cancelled for non-payment

### DOC (Healthcare)
- **Medical Debt:** Healthcare costs converted to debt (collections, credit cards, loans)
- **Care Avoidance:** Skipping/delaying care due to cost
- **OOP:** Out-of-pocket costs

### NICK (Shadow Credit)
- **BNPL:** Buy Now Pay Later
- **Stacking:** Multiple simultaneous BNPL/loan obligations
- **Shadow Credit:** Lending outside traditional bank/credit bureau visibility

### POP (Small Business)
- **Personal Guarantee:** Owner personally liable for business debt
- **MCA:** Merchant Cash Advance (high-cost business financing)
- **Zombie Business:** Operating but unable to invest or grow

### GIG (Gig Economy)
- **Saturation:** Worker supply exceeds demand, depressing earnings
- **Multi-Apping:** Working multiple gig platforms simultaneously
- **Buffer Function:** Gig work as supplemental income safety net

---

## Log Types

| Log | Question Answered | Persistence |
|-----|-------------------|-------------|
| **VX** | What are we measuring? | Permanent (structural) |
| **ML** | What do we know now? | Permanent (observations) |
| **FL** | What should we watch for? | Until date passes (then retire) |
| **FLOW** | If X breaks, what breaks next? | Until relationship changes |

---

## State Vector Fields

Required fields for subordinate → CARL communication:

```yaml
# IDENTITY
id: "SV-[AGENT]-[DATE]-[##]"
from_agent: "[Reporting agent]"
to_agent: "CARL"
timestamp: "[ISO 8601]"

# SYNTACTIC (shared vocabulary)
domain: "[Agent's domain]"
metric: "[What's being measured]"
value: "[Current value]"
status: "NORMAL | ELEVATED | CRITICAL | BREACHED"

# SEMANTIC (local interpretation)
interpretation: "[What it means]"
confidence: [XX]%
confidence_reasoning: "[Why this confidence]"
translation_flags: ["[Concepts that may not transfer cleanly]"]

# PRAGMATIC (recommendation)
recommended_action: "IGNORE | WATCH | INCORPORATE | ESCALATE"
action_rationale: "[Why this recommendation]"

# VALIDITY
sources: ["[Data sources]"]
invalidation_conditions: ["[What would change this]"]
```

---

## Abbreviations

| Abbrev | Meaning |
|--------|---------|
| ACH | Analysis of Competing Hypotheses |
| ALCOA | Attributable, Legible, Contemporaneous, Original, Accurate |
| ABS | Asset-Backed Securities |
| APR | Annual Percentage Rate |
| C2 | Command and Control |
| DQ | Delinquency |
| FL | Future Log |
| FLOW | Cascade Map |
| ML | Master Log |
| OOP | Out of Pocket |
| P&C | Property & Casualty (insurance) |
| SECI | Socialization, Externalization, Combination, Internalization |
| SV | State Vector |
| VX | Vector Registry |

---

*Use these terms consistently. If you need a new term, propose adding it here.*
