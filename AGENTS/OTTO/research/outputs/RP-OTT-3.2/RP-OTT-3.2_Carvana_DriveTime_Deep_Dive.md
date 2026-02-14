# RP-OTT-3.2 — Carvana/DriveTime Fraud Allegations Deep Dive

**Source:** Gemini Deep Research  
**Date:** 2026-02-14  
**Prompt:** RP-OTT-3.2

## Executive Summary

Allegations surfaced in late January 2026 that Carvana significantly overstated earnings (~$1 billion) by hiding losses in related-party deals with entities owned by CEO Ernest Garcia III's father (Ernest Garcia II). The short-seller Gotham City report (Jan 28) claimed Carvana booked sale revenues via DriveTime Automotive Group (a large used-car dealer owned by Garcia II) and loan manager Bridgecrest, but funneled nearly all the cash back to those related entities. In response, Carvana denied any fraud, but investors panicked: the stock plunged ~15–20% the first day and fell a further ~10% on Feb. 12, erasing its 2026 gains.

Concurrently, a federal magistrate judge (John Z. Boyle, D. Ariz.) granted a plaintiffs' motion to compel production of DriveTime-related documents (previously withheld as "attorneys-eyes-only") in the ongoing Carvana securities lawsuit. This order (entered Feb. 11–12) implicitly lends credibility to the allegations by forcing disclosure of internal DriveTime communications.

---

## Corporate Structure

**Critical distinction:** DriveTime is NOT a Carvana subsidiary – it's a separate company controlled by the Garcia family.

```
Carvana Co. (Public - Class A)
    │
    └── Carvana Group, LLC (Operating units)
            │
            ├── Retail Platform
            ├── Financing Subsidiaries  
            └── [Related-party transactions with...]
                    │
                    ▼
        DriveTime Automotive Group (SEPARATE)
        └── Owned by Ernest Garcia II (CEO's father)
            └── Bridgecrest (loan servicer)
```

- **Carvana Co.**: Public Class A stock; Class B held by Garcia family (virtually all voting power)
- **DriveTime**: Independently owned by Ernest Garcia II; Carvana's filings treat it as "related party"
- **Bridgecrest**: Loan servicer owned by Garcia II; services loans sold to Ally and ABS trusts

### Intercompany Transactions (Per 10-K)
| Transaction Type | 2024 Amount | Notes |
|-----------------|-------------|-------|
| Wholesale sales to DriveTime | $12M | DriveTime bids on Carvana inventory |
| VSC/Warranty commissions | $193M | Carvana sells, DriveTime administers |
| Facility leases | Undisclosed | Inspection centers, offices |
| Total disclosed related-party | <$250M | vs $13.67B total revenue |

**Key concern:** Are undisclosed costs (huge loan losses, cash burn) being kept off Carvana's books at DriveTime?

---

## Fraud Allegation Timeline

| Date | Event | Impact |
|------|-------|--------|
| **Jan 28, 2026** | Gotham City Research publishes $1B+ fraud allegations | Stock -15-20% |
| Early Feb 2026 | Law firms announce investigations (Block & Leviton, Kirby McInerney) | Litigation risk rises |
| **Feb 11-12, 2026** | Judge Boyle grants motion to compel DriveTime documents | Stock -10% additional |
| **Feb 18, 2026** | Q4/FY2025 earnings release | **CRITICAL CATALYST** |
| TBD | Plaintiffs receive DriveTime documents under attorneys'-eyes-only | Discovery continues |

---

## Subprime Auto Exposure

### Loan Origination Profile
- **~$8-9B** annual loan originations
- **~44%** to nonprime borrowers (FICO 601-660) — far higher than typical lenders
- Most loans sold immediately to Ally Bank or ABS trusts (non-recourse)
- Balance sheet held only **$612M** finance receivables (end 2024, down from $807M)

### Credit Performance (DETERIORATING)
| Metric | Carvana | Industry Average |
|--------|---------|------------------|
| Prime 61+ DQ | **1.3%** | 0.3% |
| Overall 30+ DQ | ~12-13% (unverified) | ~3-4% |

### Warehouse/Financing Structure
| Facility | Capacity | Drawn | Rate |
|----------|----------|-------|------|
| Floorplan (inventory) | $1.5B | $67M | — |
| Revolving (loan financing) | $2.7B | $0 | 7-7.4% |
| Warehouse lenders | Ally, Citi, JPM | — | — |

### Double-Pledging Risk
- No direct evidence of double-pledging (unlike Tricolor)
- Loan sales are non-recourse with 5% risk retention
- Cash collections held in restricted accounts
- **BUT:** If collateral is overstated, warehouse lenders face losses

---

## Financial Exposure Assessment

### Revenue Breakdown (2024)
| Segment | Revenue | YoY |
|---------|---------|-----|
| Retail vehicle sales | $9.68B | +29% |
| Wholesale sales | $2.84B | +14% |
| Other (financing, fees) | $1.15B | — |
| **Total** | **$13.67B** | — |

### The $1B Gap Question
- **Reported net income 2023+2024:** ~$550M
- **Gotham's claim:** Should have been losses (~-$450M)
- **Disclosed related-party income:** <$250M (far below alleged $1B gap)
- **Implication:** If true, hidden losses reside at DriveTime/Bridgecrest

### Balance Sheet (End 2024)
| Item | Amount |
|------|--------|
| Cash (incl. restricted) | $1.76B |
| Senior secured debt | $4.38B |
| Warehouse borrowings | $354M |
| Finance receivables (net) | $612M |
| Inventory | ~$5.2B |

---

## Market Impact

### Stock Price
- Pre-Gotham (late Jan): ~$480/share
- Post-Gotham (Jan 28): -15-20%
- Post-court order (Feb 12): additional -10%
- **Total decline:** ~35% from late-Jan high
- Short interest: ~7% of float

### ABS/Credit Market
- Subprime auto ABS spreads widened modestly in Feb 2026
- Warehouse lenders (Ally, Citi, JPM) will reassess during renewals
- Revolving facilities recently renewed into 2026 — no cuts yet

---

## Conclusion: Assessment

**Is this a major fraud case or overblown?**

| Factor | Assessment |
|--------|------------|
| Allegation seriousness | **HIGH** — $1B+ would dwarf Tricolor/PrimaLend |
| Evidence in public filings | **LIMITED** — only small-dollar disclosed transactions |
| Court action significance | **MATERIAL** — judge forcing DriveTime document production |
| Loan performance | **CONCERNING** — DQ rates 4x industry average |
| Smoking gun? | **NOT YET** — no definitive proof in public domain |

**Confidence Level:** MODERATE

The drop in stock and court action indicate material risk, but without the newly ordered documents it is not fully confirmed. Multiple red flags (short-seller reports, insider selling, demand for documents, deteriorating metrics) make it hard to dismiss as rumor.

**Key Watch:** Feb 18 earnings — Will management address the allegations? Any auditor commentary? 10-K delay or GT resignation = RED flag.

---

## Cross-Agent Implications

| Agent | Finding | Implication |
|-------|---------|-------------|
| **OTTO** | Carvana = "largest cockroach candidate" | Feb 18 is DECISIVE |
| **OTTO** | 44% nonprime, 1.3% prime DQ (4x industry) | Validates subprime stress thesis |
| **OTTO/Ally** | $19B sold to Ally, Bridgecrest services | Contagion path mapped |
| **BROCK** | If fraud confirmed = largest case since FTX | Systemic implications |
| **HENRY** | Stock -35%, ABS spreads widening | Market structure stress |

---

## Sources
- Carvana SEC filings (2024 10-K, Q1 2025 10-Q)
- Gotham City Research report (Jan 28, 2026)
- Hindenburg Research (prior)
- Court filings: In re Carvana Co. Securities Litigation (D. Ariz., No. 2:22-cv-02126)
- Bloomberg, Reuters, Yahoo Finance, Investopedia, 24/7 Wall St.
