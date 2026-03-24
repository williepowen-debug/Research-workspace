# OZK NDFI Exposure — Shadow CRE Analysis
**Created:** 2026-03-23 | **Sources:** FFIEC Call Report Q4 2025, OZK Q3 2025 Earnings Call Transcript

---

## NDFI Breakdown (FFIEC Call Report, $000s)

| RCON | Category | Amount | % of NDFI | Likely CIB Sub-Group |
|------|----------|--------|-----------|---------------------|
| RCONPV06 | Business credit intermediaries | $1,200,531 | 43.8% | ABLG (asset-based lending) + CBSF (sponsor finance) |
| RCONPV07 | Private equity funds | $772,151 | 28.2% | Fund Finance (subscription lines, bridge loans) |
| RCONPV08 | Consumer credit intermediaries | $48,285 | 1.8% | Small — consumer lenders |
| RCONPV09 | Other NDFIs | $721,546 | 26.3% | Likely BDCs, mortgage REITs, specialty finance |
| **Total** | **RCONJ454** | **$2,742,514** | **100%** | |

---

## What Are These? (From OZK's Own Definitions)

OZK's Q3 2025 earnings call glossary explicitly defines:
- **NDFI** = "lender-finance or loan-to-lender exposures, such as **BDCs and similar entities**"
- **Fund Finance** = "lending exposures to investment funds, including **subscription facilities, bridge loans**"
- **CBSF** = "targeting **leveraged and sponsored borrowers**"

This is debt-on-debt: OZK lends to entities that themselves lend to or invest in real estate and leveraged corporate borrowers.

### 🔴 CEO CONFIRMS NDFI = RESG (CRE) LOANS

**George Gleason, Q3 2025 Earnings Call (Oct 17, 2025):**
> "I'm -- you were talking about the NDFI loans, Jake, from your CIB group. But **a chunk of our NDFI loans that show up on our call report are actually RESG loans.** And this goes back to our long-standing relationships with a lot of the debt funds that do commercial real estate lending."

The CEO just told us: the NDFI line on the Call Report contains CRE exposure that is managed by RESG, not CIB. These are loans to **CRE debt funds** — entities OZK has "long-standing relationships" with. This is not a thesis inference; it's management's own admission. The NDFI bucket is partially CRE by OZK's own classification.

This significantly narrows the uncertainty in our shadow CRE estimate. If Gleason calls it "a chunk" and specifically ties it to CRE debt funds, the 50-75% CRE correlation on business credit intermediaries ($1.2B) is likely conservative for that sub-category.

---

## Shadow CRE Assessment

### $1.2B Business Credit Intermediaries (RCONPV06)
These are loans to companies whose business IS lending — bridge lenders, specialty finance, non-bank CRE lenders. If their borrowers default (e.g., CRE sponsors can't pay bridge loans), the intermediary can't repay OZK.

**CRE linkage: HIGH.** OZK is the largest US construction lender. Their network of borrowers includes CRE bridge lenders and specialty finance firms. The ecosystem is self-referential — OZK lends to the construction borrower AND to the bridge lender who might provide mezzanine or takeout financing.

### $772M Private Equity Funds (RCONPV07)
Subscription line facilities — secured by LP capital commitments, not by underlying assets. In theory, low risk (LP commitments are the collateral). In practice:
- If LPs are themselves stressed (capital calls during a downturn), subscription lines become harder to call
- If the underlying fund holds CRE assets (real estate PE funds), the fund's NAV and LP willingness to fund are both CRE-correlated
- OZK's own relationship base skews heavily CRE — their PE fund clients likely include real estate-focused funds

**CRE linkage: MODERATE-HIGH.** Not directly CRE-collateralized, but counterparty and LP base likely CRE-correlated given OZK's network.

### $722M Other NDFIs (RCONPV09)
This is the black box. Could be BDCs (like ARCC, OBDC — our BROCK thesis targets), mortgage REITs, CLO managers, or other specialty finance. OZK's own glossary says NDFI = "BDCs and similar entities."

**CRE linkage: MODERATE.** BDCs are mostly corporate middle-market lending, not CRE. But some hold real estate debt. Mortgage REITs are directly CRE-linked. Without knowing the specific names, we estimate 30-50% CRE correlation.

### $48M Consumer Credit (RCONPV08)
Consumer lenders. Minimal CRE linkage. Immaterial.

---

## True CRE Exposure Estimate (Including Shadow NDFI)

### Conservative Estimate (Low CRE assumption for NDFI)
| Category | Amount | CRE % | Shadow CRE |
|----------|--------|-------|------------|
| Business credit intermediaries | $1,201M | 50% | $600M |
| PE funds | $772M | 30% | $232M |
| Other NDFIs | $722M | 30% | $217M |
| Consumer credit | $48M | 0% | $0 |
| **Total shadow CRE** | | | **$1,049M** |

### Aggressive Estimate (High CRE assumption)
| Category | Amount | CRE % | Shadow CRE |
|----------|--------|-------|------------|
| Business credit intermediaries | $1,201M | 75% | $900M |
| PE funds | $772M | 50% | $386M |
| Other NDFIs | $722M | 50% | $361M |
| Consumer credit | $48M | 0% | $0 |
| **Total shadow CRE** | | | **$1,647M** |

### Adjusted CRE Concentration

| Metric | Reported | + Shadow CRE (Conserv.) | + Shadow CRE (Aggr.) |
|--------|---------|------------------------|---------------------|
| CRE exposure | $19,876M | $20,925M | $21,523M |
| CRE / Tier 1 | 362% | **381%** | **392%** |
| + Memo Item 3 ($1.289B) | — | **405%** | **416%** |

🔴 **Including shadow NDFI + Memo Item 3, true CRE/Tier 1 is 405-416%** — not the reported 358%.

---

## Key Risk: Correlation in Stress

The critical issue isn't just the dollar amount — it's **correlation**. In a CRE stress scenario:
1. OZK's direct CRE loans go nonaccrual (already happening — $256.7M)
2. Bridge lenders OZK lent to ($1.2B) can't collect from the same stressed CRE borrowers
3. PE funds OZK lent to ($772M) face NAV declines and LP reluctance to fund capital calls
4. BDCs/specialty finance ($722M) face their own credit stress

All four channels are hit by the same macro shock. This is **wrong-way risk** — OZK's NDFI exposure is positively correlated with its direct CRE exposure when it should be diversifying.

OZK management characterizes CIB as "diversification away from RESG." The data suggests it's partial diversification at best — $2.74B in NDFI loans to entities whose businesses depend on the same credit cycle OZK's RESG is exposed to.

---

## What We Don't Know (And Can't Get From Public Data)

1. **Specific NDFI counterparty names** — Are these real estate bridge lenders or tech-focused BDCs? The CRE correlation estimate swings widely.
2. **Collateral on NDFI loans** — Are they secured by the intermediary's loan portfolio? By LP commitments? Unsecured?
3. **Overlap** — Does OZK lend to a CRE borrower directly via RESG AND to a bridge lender who also lent to that same borrower? This would be double exposure to the same credit.
4. **NDFI noncurrent status** — The $2,703 of C&I noncurrent (RC-N) is tiny vs $3.4B C&I book. But NDFI defaults tend to be sudden (fund gate, margin call), not gradual.

---

*Source: FFIEC Call Report RSSD 107244, Q4 2025. OZK Q3 2025 Earnings Call (Motley Fool transcript, Oct 17 2025).*
