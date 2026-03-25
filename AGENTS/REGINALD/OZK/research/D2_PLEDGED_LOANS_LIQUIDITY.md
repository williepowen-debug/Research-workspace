# D2: Pledged Loans, Liquidity Analysis & Depositor Subordination

**Created:** 2026-03-24
**Sources:** OZK Q4 2025 Management Comments, FDIC API (CERT 110), FFIEC Call Report Q4 2025
**KB Rows:** 042–047 | **Group:** `CAPITAL_LIQUIDITY` | **Nav:** `../workbook/KB_INDEX.md`
**Status:** COMPLETE

---

## The Data Point

**$23.9B in loans pledged as collateral — 74% of the total loan book.**

Three-quarters of OZK's loans are already committed. This is the sleeping number.

---

## Liquidity Sources (Q4 2025 — Management Comments)

| Source | Q4 2025 | Q3 2025 | Change |
|--------|--------:|--------:|-------:|
| Cash & equivalents | $2.8B | $3.1B | -$0.3B |
| Unpledged securities | $1.6B | $1.9B | -$0.3B |
| **FHLB borrowing capacity** | **$8.8B** | **$8.8B** | Flat |
| Unsecured lines of credit | $1.2B | $1.2B | Flat |
| Fed discount window | ~$0.7B | $0.6B | +$0.1B |
| **Total liquidity sources** | **$15.1B** | **$15.6B** | **-$0.5B** |

### Key Observations
1. **Liquid assets shrank** — cash (-$300M) and unpledged securities (-$300M) both declined Q3→Q4
2. **FHLB capacity is the backstop** — $8.8B = 58% of total liquidity. This is collateral-dependent
3. **Zero FHLB borrowings outstanding** — they haven't tapped it. Yet. When they do, it's a signal
4. **$4.13B FHLB standby LOCs** already in place (from Call Report) — available but undrawn

---

## The Collateral Trap

### What's Pledged vs. What's Left

| Category | Amount | % of Total Loans |
|----------|-------:|:----------------:|
| **Pledged loans** | $23.9B | **74%** |
| Unpledged loans | ~$8.4B | 26% |
| **Total loans** | $32.3B | 100% |

### Who Holds the Pledged Collateral?

OZK doesn't break this out, but the structure is inferrable:

| Likely Counterparty | Estimated Pledged | Basis |
|--------------------|------------------:|-------|
| **FHLB (Dallas)** | ~$15-18B | $8.8B capacity implies ~$15-18B collateral at 50-60% advance rates |
| **Fed discount window** | ~$3-5B | $0.7B capacity at typical haircuts |
| **Public deposits / state pledging** | ~$2-4B | Banks must pledge collateral for state/municipal deposits |
| **Total** | ~$20-27B | Roughly reconciles to $23.9B |

### The Math Problem

The $8.8B FHLB capacity requires collateral already pledged. If OZK's CRE collateral values decline (per D1 — office values down 30-47%), the FHLB can:
1. **Increase haircuts** — reducing borrowing capacity on the same collateral
2. **Reject declining collateral** — CRE loans migrating to substandard may become ineligible
3. **Mark to market** — construction loans on interest reserves aren't generating cash flow

**FHLB capacity is not fixed. It erodes as credit quality deteriorates.**

---

## Depositor Subordination — The Structural Angle

### The Hierarchy in Stress

When 74% of loans are pledged to secured creditors (FHLB, Fed), depositors' claims are effectively subordinated:

```
Secured creditors (FHLB, Fed)    → $23.9B in collateral (first claim)
FDIC-insured depositors          → $21.5B (covered by FDIC fund)
Uninsured depositors             → $11.9B (LAST in line for recovery)
```

### The Uninsured Depositor Problem

| Metric | Value |
|--------|------:|
| Uninsured deposits | $11.9B |
| As % of total deposits | 35.8% |
| Uninsured / Tier 1 capital | 2.2x |
| **Unpledged assets available to cover uninsured** | **~$8.4B loans + $1.6B securities = ~$10.0B** |
| **Shortfall if ALL uninsured flee** | **~$1.9B** |

In a deposit flight, OZK's first move is drawing the FHLB line ($8.8B). But:
- FHLB draws against **already-pledged** collateral — no new encumbrance
- If FHLB capacity shrinks (collateral downgrades), the gap widens
- Fed discount window ($0.7B) is emergency-only and stigmatized

### Comparison: SVB / First Republic / OZK

| Metric | SVB (pre-fail) | First Republic (pre-fail) | **OZK (Q4 2025)** |
|--------|:--------------:|:-------------------------:|:------------------:|
| Uninsured % | 94% | 68% | **35.8%** |
| Pledged as % of loans | ~60% | ~55% | **74%** |
| FHLB drawn at failure | $15B (maxed) | $92B (record) | **$0** |
| Liquid assets / uninsured | ~15% | ~20% | **~38%** |

OZK is better on uninsured concentration but **worse on pledge ratio**. 74% pledged is extremely high — it means in a stress scenario, the bank has very little free collateral to raise additional liquidity.

---

## Scenario Analysis: Deposit Stress

### Scenario 1: Mild Stress (10% uninsured outflow = $1.2B)
- Draw FHLB: $1.2B → capacity drops to $7.6B
- Manageable. No crisis signal.

### Scenario 2: Moderate Stress (25% uninsured outflow = $3.0B)
- Draw FHLB: $3.0B → capacity drops to $5.8B
- Cash reserves depleted ($2.8B → ~$0)
- FHLB draws become **public information** via quarterly reports
- Analyst coverage turns negative on liquidity

### Scenario 3: Severe Stress (50% uninsured outflow = $5.95B)
- Draw FHLB: $5.95B → capacity drops to $2.85B
- Cash + liquid securities exhausted
- Approaching the point where FHLB is the ONLY liquidity source
- Fed discount window ($0.7B) = emergency signal
- **This is where SVB and FRC were in the days before intervention**

### Scenario 4: Tail (Run — 75%+ uninsured outflow = $8.9B+)
- FHLB capacity exhausted ($8.8B)
- Fed emergency facilities required
- Regulatory intervention likely
- **OZK would need $0.1B+ beyond all available sources**

---

## Why This Matters for the Thesis

### Near-Term (Earnings Compression — Base Case)
The pledged loan ratio doesn't matter directly. But it constrains OZK's ability to:
- Sell loans to raise capital (pledged loans can't be sold without releasing collateral)
- Restructure the balance sheet under stress
- Respond to rating downgrades (higher collateral requirements)

### Tail Scenario (Capital Event — 5% probability)
74% pledged + $11.9B uninsured + CRE collateral declining = the ingredients for a liquidity crisis. Not today, but:
- A bad earnings report (Apr 16) + CRO discretionary selling + social media amplification → rational depositor response
- OZK's depositor base is more sophisticated than SVB's (fewer tech startups, more institutional) — which means they monitor CRE metrics and act faster

### The Monitoring Signal
**Watch for FHLB advances moving from $0 to any positive number.** That's the tripwire. OZK has been entirely deposit-funded — any FHLB draw signals the liquidity cushion is being tested.

---

## Position Sizing Implication

This analysis doesn't change the base case (earnings compression, Aug $45 put). It **validates the tail scenario** (Scenario D in SCENARIOS.md, 5% probability, $15-20 target). The pledge ratio means OZK has less room to maneuver than the headline capital ratios suggest. CET1 11.70% is strong — but capital and liquidity are different things. SVB had 15.3% CET1 the quarter before it failed.

---

## Outstanding Data Needs

1. **Pledged loan composition** — What types of loans are pledged? If heavily CRE, FHLB haircuts could increase
2. **FHLB advance rate history** — Has OZK ever drawn? When was the last time? (10-K historical data)
3. **Brokered deposits** — Any growth in brokered? That's a deposit quality signal (Call Report: RCONHK04)

---

## Cross-References
- EVIDENCE.md: Funding & Liquidity section (lines 108-122), Deposit composition (line 244)
- SCENARIOS.md: Tail scenario (Scenario D)
- sources/FDIC_API_CALL_REPORT_DATA.md: Pledged loans data
- Q4 2025 Management Comments: ir.ozk.com/4Q25_Management_Comments
