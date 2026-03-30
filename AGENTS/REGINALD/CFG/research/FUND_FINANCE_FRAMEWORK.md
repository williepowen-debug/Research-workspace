# Fund Finance Facility Framework — Applied to CFG's $12.5B

**Created:** 2026-03-30 | **Source:** Industry research (Mayer Brown, Cadwalader, Dechert, PE Bro, market reporting)

---

## TWO PRODUCT TYPES, TWO RISK PROFILES

CFG's fund finance book splits into two structurally different products:

### Product 1: Capital Call Facilities ($8,579M) — LOWER RISK

**How they work:** Revolving credit lines to PE/VC funds secured by LP uncalled capital commitments. The bank lends against the contractual right to call capital from investors. If the fund defaults, the bank can step into the GP's shoes and issue capital calls directly.

**Borrowing base mechanics:**
- Advance rates: **50-90%** of eligible LP commitments, tiered by investor quality
  - Top tier (investment-grade insurers, sovereign wealth funds): highest advance rates
  - Mid tier (public pensions, rated endowments): moderate
  - Low tier (unrated family offices, HNW): lowest advance rates / excluded
- Single-investor concentration cap: **10-25%** of borrowing base
- Top-5 investor concentration target: **<60%** of borrowing base
- Minimum undrawn coverage covenant: **1.5x-3.0x** of outstanding borrowings

**What triggers impairment:**
- LP rated downgrade → borrowing base shrinks automatically (lower advance rate applied)
- LP invokes excuse rights (ESG, sanctions) → excluded from borrowing base → mandatory prepayment if over-drawn
- LP defaults on capital call → overcall mechanism (10-25% of commitments from other LPs)
- Correlated LP stress during macro shock → multiple downgrades/exclusions simultaneously → borrowing base collapse

**Default events:**
- Outstanding loans exceed borrowing base → **mandatory prepayment**
- Undrawn coverage falls below covenant → breach
- LPA amendment impairing call mechanics → breach
- Fund/GP insolvency

**Pricing:** SOFR + 135-175bps (top-tier) to SOFR + 175-275bps (mid-market)

**The risk is NOT the individual facility — it's correlation.** In normal times, LP defaults are uncorrelated. In a systemic stress event (PE liquidity crisis, LP cash flow constraints from private credit losses), multiple LPs across multiple funds can degrade simultaneously, shrinking borrowing bases across CFG's entire $8.6B capital call book.

---

### Product 2: Secured Private Credit Finance ($3,963M) — HIGHER RISK

**How they work:** NAV-based lending facilities where the collateral is the fund's existing portfolio assets (loans, debt instruments, equity interests in portfolio companies), NOT LP commitments. The bank lends against the value of what the fund already owns.

**NAV-based mechanics:**
- LTV minimums: **25-35%** customary (fund must maintain NAV well above loan amount)
- NAV-to-Cost covenant: maintain **100-110%** of aggregate cost basis (maximum ~10% NAV decline tolerated)
- Collateral: direct/indirect interests in portfolio companies, account pledges, distribution rights
- Valuation: quarterly or more frequent; lenders negotiate right to dispute valuations

**What triggers impairment:**
- Portfolio NAV declines below covenant threshold → **mandatory prepayment** from distributions/liquidations
- NAV marks are quarterly — impairment transmission is **QUARTERLY, not daily** (lag risk)
- If underlying borrowers enter distressed exchange → portfolio marks drop → NAV declines → collateral impairment
- Double-pledging risk: collateral pledged to multiple lenders (documented in MFS/Barclays scandal)

**Why this is the high-risk tranche:**
1. Collateral IS the thing under stress. Unlike capital calls (secured by LP commitments, a separate credit), NAV facilities are secured by the portfolio that's deteriorating.
2. Valuation lag. NAV marks are backward-looking. By the time a quarterly mark reflects stress, the actual decline may be worse.
3. Distressed exchange masking. 94% of private credit downgrades are distressed exchanges — not defaults. NAV marks may not reflect these as losses until the exchange terms fail.

---

## CURRENT MARKET STRESS — APPLIED TO CFG

| Signal | Current Level | Impact on CFG |
|--------|--------------|---------------|
| PCDR (default rate) | 5.8%, MS warns 8% | Impairs NAV collateral on $4.0B secured PC book |
| Distressed exchanges | 94% of all PC downgrades | Masks true losses in NAV marks — CFG's CECL model may undercount |
| Interest coverage | <1.0x for many mid-market firms | Fund borrowers can't service debt → portfolio marks decline |
| Gating (Ares 5%, Apollo 45¢/$1, Blue Owl halted) | 9+ funds restricted | LP liquidity stress → capital call reliability questioned |
| LP redemption pressure | 11%+ requests at multiple funds | If LPs can't redeem from gated funds, can they fund capital calls? |
| Goldman tightening credit lines | Active | G-SIBs reducing exposure = regionals like CFG left holding more |

---

## TRANSMISSION CHAIN — DETAILED

```
Stage 1: Portfolio Stress
  Private credit defaults rise (5.8% → 8%)
  Distressed exchanges mask losses (94% of downgrades)
  Interest coverage drops below 1.0x

Stage 2: NAV Decline
  Fund portfolio marks drop on quarterly valuations
  NAV-to-Cost breaches 100% threshold
  → CFG's $4.0B "secured PC finance" collateral impaired
  → Mandatory prepayment or additional collateral required
  → If fund can't pay → provisions or charge-offs

Stage 3: LP Liquidity Stress
  LPs locked in gated funds can't access capital
  LP cash flow constrained → capital call reliability questioned
  LP credit downgrades → borrowing base shrinks across capital call book
  → CFG's $8.6B capital call book availability declines
  → Multiple fund borrowing bases shrink simultaneously (correlation)

Stage 4: CFG Balance Sheet Impact
  Provisions increase on fund finance book (currently buried in C&I)
  RWA increases (already up $5.8B from C&I growth)
  Unfunded commitments ($105.9B) = contingent drain if funds draw
  FHLB dependency rises if liquidity tightens
```

**Speed estimate:**
- Secured PC (NAV-based): QUARTERLY lag (marks → covenant test → mandatory prepay)
- Capital call (LP-based): WEEKS to MONTHS (LP downgrades → borrowing base recalc)
- Combined: First provisions likely appear at Q1 or Q2 2026 earnings

---

## WHAT CFG'S CECL MODEL LIKELY MISSES

1. **No fund-finance-specific loss history.** Van Saun says "$0 losses" on Private Bank. Industry loss rates on subscription lines are near-zero historically. CECL models calibrated to this history will produce minimal reserves.

2. **Correlation not modeled.** CECL uses econometric models by loan pool. Capital call facilities are pooled in C&I. The model likely uses general C&I default/loss assumptions, NOT fund-finance-specific stress scenarios with correlated LP downgrades.

3. **Qualitative overlay.** CFG's CECL includes qualitative factors ("uncertainty related to economic forecasts, loan growth, backtesting results"). In theory, management COULD add a qualitative overlay for private credit stress. In practice, with 11 Strong Buy ratings and "zero losses," the incentive to do so is low.

---

## SOURCES

- [Mayer Brown: Subscription Credit Facilities — Understanding the Collateral](https://www.mayerbrown.com/en/insights/publications/2025/04/subscription-credit-facilities-understanding-the-collateral)
- [Dechert: Key Differences Between Sub-lines and NAV Facilities](https://www.dechert.com/knowledge/the-cred/2024/9/back-to-basics--key-differences-between-sub-lines-and-nav-facili.html)
- [Private Equity Bro: Subscription Credit Facilities — Structure, Pricing, Risks](https://privateequitybro.com/subscription-credit-facilities-structure-pricing-risks/)
- [Cadwalader: NAV Covenants and Subscription Lines](https://www.cadwalader.com/fund-finance-friday/index.php?eid=1312&nid=174&cont=93)
- [Business Story: Private Credit's 'Zero-Loss Illusion'](https://www.businessstory.org/2026/03/25/private-credits-zero-loss-illusion-is-reaching-its-conclusion-as-defaults-and-fund-withdrawals-increase/)
- [FinancialContent: The Sputtering Flywheel — US Private Credit Faces a Reckoning](https://markets.financialcontent.com/stocks/article/marketminute-2026-3-26-the-sputtering-flywheel-us-private-credit-faces-a-reckoning-as-distressed-exchanges-and-liquidity-gaps-explode)

---

*Parent: CFG/THESIS.md | Vectors: V1 (Fund Finance Collateral), V2 (FHLB Amplification)*
