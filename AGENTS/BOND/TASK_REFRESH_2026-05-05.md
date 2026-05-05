# BOND Refresh Task — May 5, 2026

## Objective
Full domain refresh after 40-day staleness. Update STATUS.md with current bond market structure data.

## Sub-Tasks (spawn separately)

### SUB-1: Auction Data Pull
**Agent:** BOND-SUB-AUCTION
**Task:** 
- Pull Treasury auction results for Apr 1-May 5, 2026
- Focus: 2Y, 5Y, 7Y, 10Y, 30Y auctions
- Metrics: Bid-to-cover, tail, dealer absorption %
- Compare to Mar 26 baseline (5Y worst BTC in 4yr)
- Check if eSLR reform (Apr 1) improved demand

**Sources:** TreasuryDirect, FiscalData.treasury.gov, Bloomberg if available
**Output:** `auction_refresh.md` with table + trend analysis

### SUB-2: Issuance & Credit Data Pull
**Agent:** BOND-SUB-ISSUANCE
**Task:**
- HY new issue volume for Apr 2026
- IG new issue volume for Apr 2026
- Pulled deals, repricings, any freeze signals
- CDX.HY levels vs cash spreads (basis)
- Compare to Mar 26 baseline (Janus Henderson scrapped, $2.6B pulled)

**Sources:** LCD, LevFin Insights, Bloomberg, FRED
**Output:** `issuance_refresh.md` with volume data + trend

### SUB-3: Dealer Capacity & Positioning
**Agent:** BOND-SUB-DEALER
**Task:**
- Primary dealer net Treasury positions (latest FR 2004)
- eSLR reform impact: are dealers expanding Treasury books?
- SLR levels post-reform
- Any dealer restructuring (MS $85B transfer follow-up)

**Sources:** FR 2004, NY Fed, dealer 10-Qs
**Output:** `dealer_refresh.md` with positioning data

## BOND Main Agent Task
After sub-agents complete:
1. Read all sub-agent outputs
2. Update STATUS.md with fresh dashboard
3. Update convergence matrix (score current vectors)
4. Revise falsification criteria
5. Write HEADLINES block
6. Flag any signals for LIQUID/ZHAO/HENRY

## Context for BOND
- Last update: Mar 26, 2026
- HY OAS was 319bps, now 278bps (tightened 41bps)
- Thesis: auction deterioration, issuance freeze, credit-equity lead
- Current reality: opposite direction on HY, SOFR normalized, dealer capacity expanded
- Need honest reassessment — don't anchor to old thesis
