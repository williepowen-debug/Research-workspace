# BROCK — Signal Interpretation Guide

**Purpose:** Defines what metrics mean and when to act. Thresholds only — no live data here.
**Live data:** STATUS.md dashboard + workbook/VX.tsv
**Last reviewed:** 2026-03-06

---

## Quarterly Signals (Earnings Season)

### PIK % of Investment Income
PIK = borrowers paying interest with more debt, not cash. Single most important BDC health metric.

| Reading | Interpretation | Action |
|---------|----------------|--------|
| <9% | Healthy, sustainable | GREEN |
| 9-15% | Elevated, watch trend | YELLOW, track QoQ |
| 15-25% | Distressed, cash flow impaired | ORANGE, update watchlist |
| >25% | Crisis, dividend unsustainable | RED, alert REGINALD |

**Key question:** Is PIK rising or stable? Rising PIK = deteriorating credits.

### Dividend Coverage (NII / Distribution)

| Reading | Interpretation | Action |
|---------|----------------|--------|
| >1.15x | Strong, building spillover | GREEN |
| 1.05-1.15x | Adequate, thin buffer | YELLOW |
| 0.95-1.05x | Burning reserves | ORANGE, dividend cut risk |
| <0.95x | Unsustainable, cut imminent | RED, signal REGINALD |

**Key question:** How many quarters at <1.00x? Two+ = dividend cut coming.

### NAV Change (Quarter-over-Quarter)

| Reading | Interpretation | Action |
|---------|----------------|--------|
| >-2% | Normal volatility | GREEN |
| -2% to -5% | Elevated markdowns | YELLOW |
| -5% to -10% | Significant stress | ORANGE, identify problem names |
| -10% to -15% | Severe distress | RED, signal REGINALD |
| >-15% | Crisis | RED, check bank exposure |

**Key question:** Concentrated (1-2 names) or broad-based? Concentrated = idiosyncratic. Broad = systemic.

### Non-Accrual Rate (at Fair Value)

| Reading | Interpretation | Action |
|---------|----------------|--------|
| <1.5% | Healthy | GREEN |
| 1.5-2.5% | Slightly elevated | YELLOW |
| 2.5-4.0% | Concerning | ORANGE |
| >4.0% | Distressed | RED |

Compare to shadow default rate (~6-7%). The gap = PIK masking stress.

---

## Monthly/Continuous Signals

### Redemption Requests (Non-Traded BDCs)

| Reading | Interpretation | Action |
|---------|----------------|--------|
| <5% quarterly | Normal | GREEN |
| 5-10% | Elevated, manageable | YELLOW |
| 10-15% | Gate risk | ORANGE |
| >15% | Gate imminent | RED |
| **GATED** | Redemptions halted | 🔴 CRISIS |

### Market Price to NAV Discount (Listed BDCs)

| Reading | Interpretation | Action |
|---------|----------------|--------|
| <-10% | Normal range | GREEN |
| -10% to -15% | Elevated skepticism | YELLOW |
| -15% to -20% | Significant doubt | ORANGE |
| >-20% | Market calling BS on NAV | RED |

### Software/Tech Sector Concentration

| Reading | Interpretation | Action |
|---------|----------------|--------|
| <20% | Diversified | GREEN |
| 20-25% | Elevated | YELLOW |
| 25-30% | High concentration | ORANGE |
| >30% | Dangerous | RED |

---

## AI Infrastructure Signals

### Neocloud Credit Events

| Signal | Interpretation | Action |
|--------|----------------|--------|
| Customer loss | Revenue concentration risk | YELLOW |
| Covenant waiver | Credit stress beginning | ORANGE |
| Rating downgrade | Institutional concern | ORANGE |
| Missed payment / restructuring | Credit event | RED |
| Bankruptcy | Transmission to BDCs | RED, check bank exposure |

**Key names:** CoreWeave ($12.7B), Crusoe ($11.6B), Lambda ($2.3B)

### Big Tech Capex Guidance

| Signal | Interpretation | Action |
|--------|----------------|--------|
| Raised | Tailwind continues | GREEN |
| Flat | Stabilizing | YELLOW |
| Cut 10-20% | Stress emerging | ORANGE |
| Cut >30% | 2001 telecom parallel | RED |

---

## Cross-Agent Signal Rules

### → REGINALD (bank transmission)
1. Any BDC with >$2B bank revolver + NAV decline >15%
2. Multiple BDCs mark down same portfolio company
3. Redemption gate at non-traded BDC with bank sub-lines
4. PIK >20% at FSK or ARCC (largest syndicates)
5. Software sector broad markdown >5%

### → LABOR (employment)
1. Portfolio company layoff announcements spike
2. Sponsor portfolio stress emerges (Thoma Bravo, Vista)

### → LIQUID (funding)
1. BDC revolving facility draws spike
2. NAV facility LTV breaches trigger margin calls
3. CLO forced selling begins

---

## Status Levels

| Status | Meaning | Action |
|--------|---------|--------|
| 🟢 GREEN | Healthy | Monitor normally |
| 🟡 YELLOW | Watch closely | Update VX, flag trend |
| 🟠 ORANGE | Elevated stress | Update STATUS.md, consider cross-signal |
| 🔴 RED | Crisis | Signal agents, update PREDICTIONS |

---

*This file defines WHAT signals mean. STATUS.md tracks WHERE we are. VX.tsv stores the numbers.*
