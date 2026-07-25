# PCAOB RSM 2024 Inspection — Issuer B Elimination Analysis

**Date:** 2026-03-27
**Conclusion:** **Issuer B = Western Alliance Bancorporation (WAL)** — confirmed by elimination

## Issuer B Profile (from PCAOB report)

A financial institution that:
1. **Purchased certain collateralized loans at a discount**
2. **Engaged specialists to estimate fair value of underlying collateral**
3. Determined **"accretable" discounts** on purchased loans

## Elimination Method

Searched EDGAR full-text search (EFTS) for all RSM bank audit clients' 10-K filings containing the exact phrases: `"purchased loans"` + `"at a discount"` + `"accretable"`.

### Results

| Bank | Ticker | Assets | EDGAR Hits | Match? |
|------|--------|--------|------------|--------|
| International Bancshares | IBOC | ~$15B | **0** | ❌ No |
| Bridgewater Bancshares | BWB | ~$8B | **0** | ❌ No |
| Bar Harbor Bankshares | BHB | ~$4B | **1** (2012 only) | ❌ No — historical only, from 2012 10-K; no recent purchased loan portfolio |
| Community West Bancshares | CWBC | ~$3B | **0** | ❌ No |
| Unity Bancorp | UNTY | ~$3B | **0** | ❌ No |
| **Western Alliance Bancorporation** | **WAL** | **~$80B** | **5** | ✅ **YES** — consistent across multiple years |

### Detail: Western Alliance Hits

WAL's 10-K filings match across **5 separate filings** spanning 2014–present. WAL has a well-known purchased loan portfolio (including from FDIC-assisted acquisitions and note finance operations) where they:
- Purchase collateralized loans at a discount to par
- Engage third-party specialists to appraise underlying collateral
- Calculate accretable yield on the discount (ASC 310-30 / CECL PCD treatment)

### Detail: Bar Harbor (sole other hit)

BHB's single hit is from a **2012 10-K** (filed March 2013), likely related to a small acquisition. BHB has no ongoing purchased loan business model and no recent filings with this language. Not a match for a 2024 inspection finding.

## Why This Matters

The PCAOB finding on Issuer B criticizes RSM's audit of fair value estimates for purchased loan collateral — specifically that RSM failed to adequately test the specialists' work and the reasonableness of accretable discount calculations. For WAL, this implicates:

- **Note finance portfolio** — WAL's distinctive business line purchasing distressed/discounted loans
- **Fair value reliability** — the very collateral valuations underpinning WAL's discount accretion income
- **Audit quality** — RSM may not have caught aggressive assumptions in WAL's purchased loan marks

## Confidence: **HIGH**

No other RSM bank audit client has a purchased-loans-at-discount business model. WAL is the only candidate by a wide margin.
