# Research Prompt: Treasury Auction Health Indicators

## Objective

Research US Treasury auction mechanics and health indicators — specifically bid-to-cover ratios, indirect bids (foreign demand proxy), and tail analysis. This supports LIQUID's monitoring of Treasury market absorption capacity.

---

## Context

**Current Situation (as of Jan 2026):**
- Treasury auction BTC (bid-to-cover) averaging ~2.5x (considered healthy)
- Indirect bid percentage ~68% (foreign/institutional demand)
- No recent auction "failures" but elevated supply from fiscal deficits

**Why This Matters:**
Treasury auctions are how the US government funds itself. Auction health indicates:
- Demand for US government debt
- Foreign buyer appetite (indirect bids proxy foreign officials + large institutions)
- Market's ability to absorb supply
- Potential funding stress if auctions weaken

**LIQUID's Thresholds:**
- BTC: <2.3x Yellow, <2.0x Orange, <1.8x Red
- Indirect Bid: <65% Yellow, <60% Orange, <55% Red

---

## Research Questions

### 1. Auction Mechanics
- How do Treasury auctions work? (competitive vs. non-competitive bids)
- What are direct, indirect, and dealer bids?
- How is bid-to-cover calculated?
- What is a "tail" and what does it indicate?
- What is the difference between bills, notes, and bonds auctions?

### 2. Historical Auction Data
- What are typical BTC ratios by security type?
- What are typical indirect bid percentages?
- Have there been any "failed" or severely distressed auctions in recent history?
- What happened during COVID (March 2020)?
- What happened during other stress periods?

### 3. Foreign Demand (Indirect Bids)
- Who are the "indirect bidders"?
- How reliable is indirect bid % as a proxy for foreign demand?
- What drives foreign demand for Treasuries?
- TIC data — what does it show about foreign holdings trends?
- Are there specific countries to watch? (Japan, China holdings)

### 4. Auction Stress Signals
- What does a weak auction look like?
- What BTC level is considered distressed?
- What tail size indicates demand weakness?
- Have any auctions had BTC below 2.0x? When, why?
- What happens if an auction "fails"?

### 5. Supply Dynamics
- What is the current Treasury issuance pace?
- How does supply affect auction metrics?
- Is there a "supply indigestion" threshold?
- Relationship between T-bill supply and money market rates?

---

## Data Sources to Check

**Primary (Official):**
- TreasuryDirect auction results: https://www.treasurydirect.gov/auctions/announcements-data-results/
- Treasury auction calendar
- TIC data (Treasury International Capital): https://home.treasury.gov/data/treasury-international-capital-tic-system
- FRED Treasury auction data

**Analysis:**
- Treasury Borrowing Advisory Committee (TBAC) reports
- CBO projections on Treasury issuance
- Primary dealer research (publicly available)
- Financial press coverage of notable auctions

**Historical:**
- March 2020 Treasury market stress
- Historical auction results database

---

## Deliverables

### A. Narrative Analysis

1. **Auction Mechanics Primer**
   - How auctions work
   - What each metric means
   - Normal ranges by security type

2. **Historical Baseline**
   - Typical BTC, indirect bid, tail by security type
   - What "normal" looks like
   - Seasonal patterns (quarter-end, year-end)

3. **Stress Episode Analysis**
   - Catalog of weak/distressed auctions
   - What caused them
   - How markets reacted

4. **Foreign Demand Assessment**
   - Who are the major foreign holders?
   - Trend in foreign holdings (growing/shrinking?)
   - Risks to foreign demand

5. **Supply Pressure**
   - Current issuance pace
   - Projected supply
   - Absorption capacity concerns

### B. Key Numbers

| Metric | Current | Normal Range | Stress Level | Source |
|--------|---------|--------------|--------------|--------|
| 10Y BTC | ? | ? | ? | TreasuryDirect |
| 10Y Indirect | ? | ? | ? | TreasuryDirect |
| 30Y BTC | ? | ? | ? | TreasuryDirect |
| Foreign holdings | ? | ? | ? | TIC |
| ... | ... | ... | ... | ... |

### C. Threshold Validation

LIQUID's current thresholds:
- BTC: <2.3x Yellow, <2.0x Orange, <1.8x Red
- Indirect: <65% Yellow, <60% Orange, <55% Red

Based on research:
- Are these appropriate?
- Should they vary by security type?
- What historically triggered concern?

### D. Upcoming Auctions

Provide the auction calendar for the next 30 days, highlighting:
- Large settlement dates
- Refunding auctions
- Any unusually large issuance

---

## Output Format

```
# Treasury Auction Health Research Results

## Executive Summary
[Key findings]

## 1. Auction Mechanics
[How it works]

## 2. Historical Baselines
[Normal ranges, typical patterns]

## 3. Stress Episodes
[Weak auctions and what happened]

## 4. Foreign Demand Analysis
[Indirect bid trends, TIC data]

## 5. Supply Dynamics
[Issuance pace, absorption concerns]

## 6. Key Data Points
[Table of current values and sources]

## 7. Threshold Assessment
[Evaluation of LIQUID's thresholds]

## 8. Upcoming Calendar
[Next 30 days of auctions]

## 9. Data Gaps
[What couldn't be found]

## Sources
[Full list]
```

---

## Notes

- Treasury auction health is tracked via VX-LIQUID-2.01 (BTC) and VX-LIQUID-2.02 (Indirect Bid)
- Foreign demand is particularly important given Japan repatriation risk (SAM's domain, but LIQUID sees auction impact)
- Focus on 10Y and 30Y auctions as these are most closely watched
- Note: "Failed auction" in US context is extremely rare — focus on "weak" auctions

---

*LIQUID Research Prompt 03 | Treasury Auction Health*
