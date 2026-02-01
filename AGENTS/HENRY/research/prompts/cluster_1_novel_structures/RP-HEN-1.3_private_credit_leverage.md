# RP-HEN-1.3: Private Credit / Shadow Leverage

**Prompt ID:** RP-HEN-1.3
**Cluster:** Novel Market Structures
**Priority:** 6
**Created:** 2026-01-26

---

## Context for Research Assistant

HENRY is investigating potential sources of hidden systemic leverage, drawing parallels to 2007-08 when CDOs and SIVs contained leverage that wasn't visible until crisis. Private credit has grown explosively to $1.7T+, largely outside bank regulatory frameworks and public market visibility. This may be where today's "hidden leverage" resides.

Current HENRY findings for context:
- Public market leverage indicators (margin debt) at ~P75 percentile
- 2008 crisis was characterized by hidden leverage in structured products
- Current conditions show multiple valuation extremes - leverage could amplify any correction

---

## Research Questions

### 1. SCALE & GROWTH OF PRIVATE CREDIT
- Current size of US private credit market (total AUM)
- Growth rate: What was private credit AUM in 2015, 2020, today?
- Breakdown by type:
  - Direct lending
  - Business Development Companies (BDCs)
  - Mezzanine financing
  - Distressed debt
  - CLO equity tranches held privately
- Major players: Which firms dominate? (Apollo, Ares, Blackstone, etc.)
- Flow trends: Is capital still flowing in or has it peaked?

### 2. LEVERAGE WITHIN PRIVATE CREDIT
- Fund-level leverage: How much do private credit funds borrow?
  - Typical leverage ratios (debt/equity at fund level)
  - Subscription line facilities
- Borrower leverage: What are typical debt/EBITDA ratios for private credit borrowers?
- NAV lending: Explain NAV loans against PE/PC portfolios
  - How much NAV lending exists?
  - What happens if underlying valuations drop?
- Leverage on leverage: Are there layers of leverage stacking?

### 3. VALUATION & MARK-TO-MARKET PRACTICES
- How are private credit assets valued?
  - Frequency of marks
  - Who determines fair value?
- "Volatility laundering" - research on how private assets appear less volatile
- What is the typical lag between public market stress and private credit marks?
- Evidence of extend-and-pretend in private credit?
- Default rate discrepancies: Private credit reported defaults vs public market equivalents

### 4. INTERCONNECTIONS & CONTAGION PATHS
- Bank exposure to private credit:
  - Direct lending by banks
  - Credit facilities to private credit funds
  - Warehouse lines
- Insurance company exposure:
  - How much private credit do insurers hold?
  - Regulatory treatment of private credit on insurer balance sheets
- Pension fund exposure:
  - Public pension allocations to private credit
  - What assumptions are pensions using for returns?
- Wealth management exposure:
  - Retail access to private credit (interval funds, etc.)

### 5. COMPARISON TO 2007-08 STRUCTURES
- CDO/SIV characteristics in 2007:
  - Opacity
  - Leverage levels
  - Interconnections
  - Rating agency involvement
- Private credit today - similarities:
  - Opacity (limited disclosure)
  - Leverage (fund + borrower level)
  - Interconnections (banks, insurers, pensions)
- Private credit today - differences:
  - Floating rate (less duration risk)
  - Direct lending (less tranching complexity)
  - No AAA mispricing?
- Key question: Is private credit "2008-lite" or structurally different?

### 6. STRESS SCENARIOS
- What happens if defaults spike to 2008 levels?
  - Forced selling dynamics
  - Liquidity for redemptions
  - Mark-to-market cascades
- What happens if rates stay higher for longer?
  - Borrower distress (floating rate debt)
  - Refinancing walls
- Interconnection stress: Could private credit stress transmit to:
  - Regional banks (REGINALD's domain)
  - Insurance companies
  - Public credit markets

### 7. REGULATORY VISIBILITY & GAPS
- What do regulators (SEC, Fed, OFR) know about private credit?
- Data gaps and blind spots
- Recent regulatory statements or concerns
- FSB or international warnings about private credit

---

## Output Format Requested

```markdown
# Private Credit / Shadow Leverage - Research Output

## Executive Summary
[Key findings and risk assessment]

## 1. Market Scale
[Size, growth, composition]

## 2. Leverage Analysis
[Fund-level, borrower-level, NAV lending]

## 3. Valuation Practices
[Mark-to-market issues, volatility laundering]

## 4. Interconnection Map
[Banks → Private Credit → Insurers → Pensions]

## 5. 2008 Comparison
| Factor | 2007 CDO/SIV | 2025 Private Credit |
|--------|--------------|---------------------|

## 6. Stress Scenarios
[Default spike, rate shock, contagion paths]

## 7. Regulatory Gaps
[What's not being monitored]

## Risk Rating
[Overall assessment: Low/Medium/High systemic risk]

## Monitoring Recommendations
[What HENRY should track]

## Sources
[URLs and citations]
```

---

## Integration Notes for HENRY

After receiving this research:
- Assess if private credit warrants dedicated vector(s)
- Coordinate with REGINALD (regional bank exposure)
- Update FLOW.tsv with private credit transmission paths
- Consider cross-agent signal to REGINALD if bank exposure significant

---

*Prompt ready for external LLM research*
