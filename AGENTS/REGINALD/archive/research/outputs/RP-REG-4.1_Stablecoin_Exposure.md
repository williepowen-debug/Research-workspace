# RP-REG-4.1: Stablecoin/Crypto Banking Exposure

**Research Prompt:** Regional Bank Exposure to Stablecoin Reserves and Digital Asset Banking

**Completed:** 2026-02-05

**Status:** ✅ COMPLETE

---

## Executive Summary

**Standard Chartered projects $500 billion in deposit outflows from U.S. banks to stablecoins by 2028.** Regional banks are disproportionately vulnerable because Net Interest Margin (NIM) comprises up to 80% of their revenue, versus <30% for diversified/investment banks. The GENIUS Act (signed July 2025) creates a regulatory framework for bank-issued stablecoins, but also legitimizes nonbank competitors.

**Key Finding:** This is a **systemic threat to regional banks** rather than a concentrated single-name exposure. Unlike other REGINALD channels, stablecoin deposit flight affects the entire sector rather than specific banks with identifiable concentration risk.

---

## 1. Stablecoin Reserve Holdings at Banks

### Circle (USDC) Reserve Composition (Aug 2025)

| Asset Class | % of Reserves |
|-------------|---------------|
| U.S. Treasuries | 33.59% |
| Repurchase Agreements | 50.79% |
| **Bank Deposits** | **14.24%** |
| Other | 1.38% |

**Primary Custodians:**
- **BNY Mellon** — Primary custodian for USDC reserves since April 2022
- **BlackRock** — Manages Circle Reserve Fund (Treasuries)
- **Customers Bank** — Settlement flows for USDC operations

**Historical Context (SVB Crisis):**
- March 2023: Circle had $3.3B deposited at SVB (~8% of total reserves)
- USDC depegged to $0.86 when Circle couldn't access funds over weekend
- Federal backstop announcement restored peg within 24 hours
- Circle has since restructured: doubled Treasury allocation, reduced bank deposit exposure

### Tether (USDT) Reserve Composition (Feb 2025)

| Asset Class | % of Reserves |
|-------------|---------------|
| U.S. Treasuries | ~85% ($113B) |
| **Bank Deposits** | **~0.02%** |
| Other | ~15% |

**Primary Custodian:** Cantor Fitzgerald (holds 99% of Treasury reserves as of late 2024)

**Key Difference:** Tether holds virtually no reserves in bank deposits, meaning it does NOT recycle deposits back into the banking system.

### Implication for Banks

**The redepositing cushion is minimal:**
- If $100 flows from bank deposits → stablecoins
- Tether recycles: $0.02
- Circle recycles: $14.24
- Remaining ~$85-$100 leaves banking system entirely (goes to Treasuries/MMFs)

This is **net disintermediation** — money permanently leaving regional bank balance sheets.

---

## 2. Standard Chartered Deposit Outflow Projections

### Headline Numbers

| Market | Projected Outflow by 2028 |
|--------|---------------------------|
| Developed Markets (US) | **$500 billion** |
| Emerging Markets | $1 trillion |
| **Total** | **$1.5 trillion** |

### Why Regional Banks Are Most Vulnerable

**Net Interest Margin (NIM) Dependency:**

| Bank Type | NIM as % of Revenue | Exposure Level |
|-----------|---------------------|----------------|
| Regional Banks | 60-80% | 🔴 CRITICAL |
| Diversified Banks | 40-60% | 🟠 ELEVATED |
| Investment Banks | <30% | 🟢 LOW |

**Four Risk Channels (Standard Chartered):**

1. **NIM Compression** — Deposits funding loans at spread evaporate
2. **Limited Redepositing** — Only 0.02-14.5% of stablecoin reserves return to banks
3. **Geographic Concentration** — 95%+ of stablecoins are USD-denominated, hitting US banks
4. **Retail vs Wholesale Shift** — FDIC-insured deposits (low cost) replaced by wholesale funding (high cost)

---

## 3. GENIUS Act: Opportunity or Threat?

**Signed into law:** July 17, 2025

### What the Law Allows

| Entity | Permitted Activities |
|--------|---------------------|
| **Bank Subsidiaries** | Issue payment stablecoins (backed 100% by HQLA) |
| **Federal Nonbank Issuers** | Issue stablecoins (>$10B requires federal regulation) |
| **State-Regulated Issuers** | Issue stablecoins (≤$10B can use state regulation) |

### Key Provisions

- **No interest payments** on stablecoins (protects bank deposits somewhat)
- **100% reserve backing** required (Treasuries, deposits, high-quality liquid assets)
- **Monthly audited reserve reports** mandatory
- **BSA/AML compliance** required (gives banks advantage over nonbanks)
- **Stablecoin holders first in line** in bankruptcy (ring-fenced reserves)

### Bank Positioning Under GENIUS Act

| Bank | Status | Notes |
|------|--------|-------|
| **JPMorgan Chase** | 🟢 Active | Launched JPMD (tokenized deposit) alongside stablecoin pilot (July 2025) |
| **Bank of America** | 🟡 Announced | CEO confirmed readiness; expected 2025-2026 launch |
| **Citibank** | 🟡 Announced | Exploring stablecoin issuance via consortium |
| **BNY Mellon** | 🟢 Active | Primary custodian for Circle; infrastructure provider |
| **Customers Bank (CUBI)** | 🟠 Constrained | Fed enforcement action (Aug 2024); capped crypto deposits |
| **Bank of North Dakota** | 🟢 Pilot | "Roughrider coin" pilot with Fiserv (blockchain payments) |

### Regional Bank Dilemma

**Option A: Issue own stablecoin**
- Requires significant tech investment
- Regulatory compliance cost high
- May only partially offset deposit flight

**Option B: Be infrastructure/custody provider**
- Lower capital intensity
- Fee income opportunity
- Requires specialized expertise (BSA/AML for crypto)

**Option C: Partner with fintechs/issuers**
- White-label offerings
- Maintain customer relationships
- Depends on partner health

**Most regional banks are choosing Option C or doing nothing.** This leaves them exposed to deposit flight without offsetting revenue streams.

---

## 4. Regional Bank Crypto/Digital Asset Exposure

### Banks with Material Crypto Banking Exposure

| Bank | Ticker | Exposure Type | Status | Risk Level |
|------|--------|---------------|--------|------------|
| **Customers Bank** | CUBI | Crypto deposits (CBIT platform) | Fed enforcement (Aug 2024); deposits capped | 🟠 ELEVATED |
| **Metropolitan Commercial** | MCB | Crypto client banking | Reduced exposure post-2023 | 🟡 MODERATE |
| **Provident Bancorp** | PVBC | Crypto banking partnerships | Small scale | 🟡 MODERATE |
| **Cross River Bank** | Private | Fintech/crypto partnerships | Active but diversified | 🟡 MODERATE |

### Customers Bank (CUBI) — Key Case Study

**Background:**
- Launched CBIT (Customer Bank Instant Token) — real-time blockchain payments for crypto firms
- Clients included: Galaxy Digital, Coinbase, Circle
- Post-SVB/Signature, became one of few banks serving crypto industry

**Fed Enforcement Action (August 2024):**
- Cited "significant deficiencies" in AML/risk management for digital asset clients
- Required prior approval for any new crypto initiatives
- Bank capped deposits in CBIT platform
- Debanked some digital asset hedge funds

**Current Status:**
- Actively reducing crypto concentration
- But still meaningful exposure to Circle settlement flows
- Stock trades at discount to peers due to regulatory overhang

### Former Crypto Banks (Cautionary Tales)

| Bank | What Happened | Lesson |
|------|---------------|--------|
| **Silvergate Bank** | Voluntary liquidation (Mar 2023) | Crypto deposit concentration → run when industry crashed |
| **Signature Bank** | Seized by regulators (Mar 2023) | Signet network popular with crypto; concentrated deposit base |
| **Silicon Valley Bank** | Seized by regulators (Mar 2023) | $3.3B Circle exposure revealed interconnection risk |

---

## 5. KRE Constituent Analysis

### Stablecoin/Crypto Exposure Assessment

**Methodology:** Reviewed 10-K/10-Q filings, earnings calls, news coverage for crypto banking mentions

| Bank | Ticker | Crypto Exposure | Stablecoin Risk | Notes |
|------|--------|-----------------|-----------------|-------|
| **Customers Bancorp** | CUBI | 🔴 HIGH | 🟠 ELEVATED | Circle settlement partner; Fed enforcement |
| **Provident Financial** | PVBC | 🟡 MODERATE | 🟡 MODERATE | Small crypto banking unit |
| **Metropolitan Commercial** | MCB | 🟡 MODERATE | 🟡 MODERATE | Reduced post-2023 |
| **Western Alliance** | WAL | 🟡 LOW | 🟠 ELEVATED | Innovation banking (fintech, not pure crypto) |
| **Most other KRE names** | — | 🟢 MINIMAL | 🟠 SYSTEMIC | No direct crypto, but all face deposit flight risk |

### Key Insight: Systemic vs Idiosyncratic

**The stablecoin threat to regional banks is primarily SYSTEMIC, not idiosyncratic:**
- $500B deposit outflow affects ALL regional banks proportionally
- No single KRE constituent has SVB-level stablecoin reserve concentration
- The "concentration risk" that existed at SVB/Silvergate/Signature has not reformed at scale
- CUBI is the exception, but it's actively de-risking

**This means stablecoin deposit flight:**
- Supports the KRE short thesis (sector-wide NIM compression)
- Does NOT identify specific single-name short targets
- Is a **tailwind for existing convergence thesis** rather than new channel

---

## 6. Transmission Mechanism to Regional Banks

```
                    ┌─────────────────────────┐
                    │  Stablecoin Adoption    │
                    │  ($2T market by 2028)   │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  $500B Deposit Outflow  │
                    │  (Developed Markets)    │
                    └───────────┬─────────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
   ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
   │ NIM         │      │ Funding     │      │ Credit      │
   │ Compression │      │ Cost Rise   │      │ Contraction │
   └─────────────┘      └─────────────┘      └─────────────┘
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  Regional Bank Earnings │
                    │  Pressure (2026-2028)   │
                    └─────────────────────────┘
```

### Timeline

| Date | Event |
|------|-------|
| July 2025 | GENIUS Act signed |
| Jan 2027 | GENIUS Act regulations take effect |
| 2027-2028 | Major bank stablecoin launches expected |
| End 2028 | Standard Chartered $500B outflow target date |

---

## 7. Implications for REGINALD Thesis

### Does This Change Convergence Scores?

**No — but it strengthens the macro thesis.**

This channel doesn't identify *which* banks break first. Instead, it:
- Compresses NIM across ALL regional banks
- Accelerates deposit cost pressures
- Creates structural headwind for sector recovery

### Watch Items to Add

| Signal | What to Monitor | Trigger |
|--------|-----------------|---------|
| **Stablecoin market cap** | CoinMarketCap total stablecoin supply | Acceleration beyond $200B growth/year |
| **Bank deposit data** | Fed H.8 weekly deposit releases | Regional bank deposit outflows |
| **CUBI earnings** | Customers Bancorp quarterly reports | Crypto deposit trends, regulatory updates |
| **Major bank stablecoin launches** | JPM/BAC/C announcements | Accelerates legitimization of stablecoin rails |
| **Tether US expansion** | USAt launch timeline | Tether entering US market increases competitive pressure |

---

## 8. Research Gaps

1. **Quantifying per-bank NIM exposure** — Need to model which specific regionals have highest NIM dependency
2. **GENIUS Act implementation timeline** — Regulations due by July 2026, actual launches unclear
3. **Institutional vs retail stablecoin adoption** — Which deposit categories are most vulnerable?
4. **Cross-border vs domestic flows** — Is foreign dollar demand actually backfilling some outflows?

---

## Key Takeaways

1. **$500B deposit threat is real** — Standard Chartered analysis credible, Fed research confirms mechanisms
2. **Regional banks most vulnerable** — NIM dependency = existential exposure to deposit flight
3. **No SVB-level concentration** — Individual bank crypto exposure is manageable (CUBI is watchable but de-risking)
4. **Systemic channel, not single-name** — Supports KRE basket short, doesn't identify new single-name targets
5. **2026-2028 timeline** — Pressure builds over next 2-3 years as GENIUS Act implementations roll out
6. **Bank stablecoin issuance may partially offset** — But requires investment and won't fully recapture lost deposits

---

## Sources

- Federal Reserve FEDS Notes: "Banks in the Age of Stablecoins" (Dec 2025)
- Federal Reserve FEDS Notes: "In the Shadow of Bank Runs" (Dec 2025)
- Standard Chartered Digital Assets Research (Jan 2026)
- CoinDesk: "Standard Chartered says U.S. regional banks most at risk" (Jan 2026)
- DL News: "Four risks from stablecoins that drain $1.5tn from banks" (Jan 2026)
- Bank Director Magazine (Q1 2026)
- Circle Transparency Reports
- GENIUS Act text (S.394, S.1582)
- Grant Thornton, Gibson Dunn, Sidley Austin regulatory analyses
