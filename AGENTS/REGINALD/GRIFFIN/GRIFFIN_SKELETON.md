# GRIFFIN Domain Skeleton

**Agent:** GRIFFIN (Growth & Risk In Private Finance Networks)
**Parent:** REGINALD
**Domain:** BDC & Private Credit Monitoring
**Version:** 1.0
**Created:** 2026-02-03

---

## QUICK START

GRIFFIN monitors Business Development Companies (BDCs) and private credit vehicles — redemption pressure, PIK income trends, sector exposures, leverage ratios, and NAV dynamics. REGINALD consumes GRIFFIN's output to assess credit intermediary stress that may transmit to banks and broader markets.

**Primary Question:** When does private credit stress transmit to forced selling and broader credit contagion?

**Core Method:**
1. Track redemption rates across major BDCs (normal <5%, stress >5%, crisis >10%)
2. Monitor PIK income as shadow default proxy
3. Map sector exposures (tech/software concentration risk)
4. Track NAV discounts/premiums as market sentiment
5. Assess leverage ratios and liquidity buffers
6. Watch for redemption gate triggers and fund mergers (liquidity stress signals)

---

## ENTITY TYPES

### Vectors (VX)
Quantifiable BDC/private credit metrics tracked over time.

**Naming Convention:** VX-GRIF-[Domain].[Number]
- Domain 1: RED (Redemptions)
- Domain 2: PIK (Payment-in-Kind / Credit Quality)
- Domain 3: EXP (Sector Exposure)
- Domain 4: LEV (Leverage & Liquidity)
- Domain 5: NAV (Valuation)
- Domain 6: FLO (Fund Flows)

### BDC Watchlist

| Ticker | Name | AUM | Focus | Current Status |
|--------|------|-----|-------|----------------|
| **ARCC** | Ares Capital | ~$25B | Diversified | 🟢 Largest, most stable |
| **MAIN** | Main Street Capital | ~$8B | Lower middle market | 🟢 High quality |
| **ORCC** | Owl Rock (Blue Owl Credit Income) | ~$33B | Upper middle market | 🟠 5.2% redemptions |
| **OBDC** | Blue Owl Capital Corp | ~$13B | Tech-focused | 🟠 Merger-related |
| **OTIC** | Blue Owl Technology Income | ~$3B | Tech/Software | 🔴 15.4% redemptions |
| **TRIN** | Trinity Capital | ~$2B | Venture lending | 🟡 Tech exposure |
| **HTGC** | Hercules Capital | ~$4B | Venture/Tech | 🟡 Tech exposure |
| **GBDC** | Golub Capital | ~$8B | Sponsor-backed | 🟠 PIK elevated |
| **FSCO** | FS KKR Capital | ~$15B | Diversified | 🟡 Watch |
| **BXSL** | Blackstone Secured Lending | ~$10B | Senior secured | 🟢 Quality focus |

---

## THRESHOLDS (Tripwires)

### Redemption Domain (RED)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED |
|--------|--------|-------|--------|--------|-----|
| VX-GRIF-1.01 | Quarterly Redemption Rate | <3% | 3-5% | 5-10% | >10% |
| VX-GRIF-1.02 | Redemption Gate Triggers | 0 | 1-2 funds | 3-5 funds | >5 funds |
| VX-GRIF-1.03 | Fund Mergers (liquidity-driven) | 0 | 1 | 2-3 | >3 |

### PIK Domain (Credit Quality)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED |
|--------|--------|-------|--------|--------|-----|
| VX-GRIF-2.01 | PIK Income % of Total | <8% | 8-12% | 12-18% | >18% |
| VX-GRIF-2.02 | Non-Accrual Rate | <1.5% | 1.5-3% | 3-5% | >5% |
| VX-GRIF-2.03 | PIK YoY Growth | <20% | 20-50% | 50-100% | >100% |

### Exposure Domain (EXP)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED |
|--------|--------|-------|--------|--------|-----|
| VX-GRIF-3.01 | Software/Tech Concentration | <20% | 20-30% | 30-40% | >40% |
| VX-GRIF-3.02 | Top 10 Holdings % | <15% | 15-25% | 25-35% | >35% |

### Leverage Domain (LEV)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED |
|--------|--------|-------|--------|--------|-----|
| VX-GRIF-4.01 | Debt/Equity Ratio | <0.90x | 0.90-1.05x | 1.05-1.20x | >1.20x |
| VX-GRIF-4.02 | Liquidity Buffer (% of assets) | >15% | 10-15% | 5-10% | <5% |

### NAV Domain (Valuation)

| Vector | Metric | GREEN | YELLOW | ORANGE | RED |
|--------|--------|-------|--------|--------|-----|
| VX-GRIF-5.01 | Price/NAV (Traded BDCs) | >0.95x | 0.85-0.95x | 0.75-0.85x | <0.75x |
| VX-GRIF-5.02 | NAV Decline (QoQ) | <2% | 2-5% | 5-10% | >10% |

---

## TRANSMISSION PATHS

### 1. Redemption Cascade
```
Rising defaults / PIK
    ↓
Investor unease → Redemption requests
    ↓
BDC honors redemptions (sells assets)
    ↓
Forced selling depresses loan prices
    ↓
Other BDCs mark down → More redemptions
    ↓
Feedback loop until gates trigger
```

### 2. Tech Exposure Contagion
```
Software/tech downturn
    ↓
Portfolio company stress
    ↓
PIK spikes, non-accruals rise
    ↓
NAV declines
    ↓
Retail/Asian investors flee
    ↓
Sector-wide BDC selloff
```

### 3. BDC → Bank Transmission
```
BDC forced selling
    ↓
CLO/loan market prices drop
    ↓
Bank loan books marked down
    ↓
REGINALD bank stress escalates
    ↓
Credit tightening → Corporate defaults
    ↓
Loop back to BDC portfolio stress
```

---

## CURRENT SITUATION (Feb 2026)

### Blue Owl Stress Event
- **OTIC:** 15.4% redemptions ($527M) — largest ever for Blue Owl
- **ORCC:** 5.2% redemptions (~$1B)
- Leverage elevated to 1.05x post-redemption
- Asian wealthy investors pulling out
- Class action lawsuit alleging hidden redemption surge

### Sector-Wide Concerns
- Tech/software exposure across BDC portfolios
- PIK income elevated (Golub +173% YoY spike noted)
- BDC stocks hitting multi-year lows
- Growing regulatory scrutiny

### Signal Status
| Metric | Reading | Status |
|--------|---------|--------|
| OTIC Redemptions | 15.4% | 🔴 RED |
| ORCC Redemptions | 5.2% | 🟠 ORANGE |
| PIK Income (sector) | ~12-13% | 🟠 ORANGE |
| NAV Discounts | Widening | 🟡 YELLOW |
| Sector Sentiment | Negative | 🟠 ORANGE |

**Composite:** 🟠 ORANGE — Active stress in tech-focused BDCs, contagion risk to broader sector

---

## KEY DATES

| Date | Event | Priority |
|------|-------|----------|
| Q4 Earnings | Major BDC reports (ARCC, MAIN, etc.) | 🟠 HIGH |
| Mar 2026 | Blue Owl Q4 earnings + redemption update | 🔴 CRITICAL |
| Ongoing | Lawsuit developments (Blue Owl) | 🟡 MEDIUM |

---

## CROSS-AGENT CONNECTIONS

| Agent | Connection | Signal |
|-------|------------|--------|
| **REGINALD** | Parent — BDC stress → loan price impact → bank marks | Primary transmission |
| **CARL** | PIK income as consumer credit proxy | Cross-reference |
| **LIQUID** | CLO market stress from BDC forced sales | Secondary transmission |
| **SAM** | Japan investor repatriation from US private credit | Asian redemption driver |

---

## DATA SOURCES

| Source | URL | Frequency |
|--------|-----|-----------|
| SEC EDGAR | BDC 10-Q/10-K filings | Quarterly |
| BDC Buzz | bdcbuzz.com | Weekly commentary |
| Seeking Alpha | BDC coverage | Daily |
| Bloomberg | BDC pricing, news | Real-time |
| Pitchbook/LCD | Private credit data | Subscription |

---

## GLOSSARY

**BDC:** Business Development Company — closed-end fund providing credit to middle-market companies
**PIK:** Payment-in-Kind — borrower pays interest with more debt instead of cash (stress signal)
**NAV:** Net Asset Value — fair value of portfolio minus liabilities
**Non-Accrual:** Loan where interest is no longer being recognized (default proxy)
**Redemption Gate:** Limit on withdrawals (typically 5% quarterly) to prevent runs
**Middle Market:** Companies with $10M-$1B EBITDA — too small for public markets, too big for traditional banks

---

*GRIFFIN Domain Skeleton v1.0*
*Created: 2026-02-03*
*Parent: REGINALD*
