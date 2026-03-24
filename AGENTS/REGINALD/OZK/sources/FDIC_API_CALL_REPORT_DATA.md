# OZK Call Report Data — FDIC API
**Source:** banks.data.fdic.gov/api/financials (CERT: 110)
**Pulled:** 2026-03-23 ~8:50 PM ET
**Note:** FDIC summary API. Does NOT include Memo Item 3 (RCON2746) or noncurrent by loan type (RC-N detail). Those require raw Call Report from FFIEC CDR.

---

## Loan Composition ($000s)

| Category | Q1 2024 | Q2 2024 | Q3 2024 | Q4 2024 | Q1 2025 | Q2 2025 | Q3 2025 | Q4 2025 | YoY Chg |
|----------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| **Construction** | 12,322,321 | 11,491,194 | 9,827,974 | 9,522,678 | 9,208,619 | 8,684,947 | 8,489,956 | 7,778,411 | **-18.3%** |
| **Nonfarm Nonres** | 5,590,632 | 6,479,286 | 7,924,453 | 7,842,692 | 7,997,142 | 8,599,886 | 8,912,407 | 8,417,455 | +7.3% |
| **Multifamily** | 2,408,875 | 2,359,446 | 3,058,056 | 3,272,635 | 3,865,580 | 4,336,103 | 3,791,814 | 3,680,059 | +12.4% |
| **C&I** | 1,355,125 | 1,499,489 | 1,503,411 | 1,728,801 | 2,066,290 | 2,330,142 | 2,870,535 | **3,431,585** | **+98.5%** |
| **Consumer/Other** | 3,155,050 | 3,406,194 | 3,552,189 | 3,647,842 | 3,759,224 | 4,011,644 | 4,222,679 | 4,258,482 | +16.7% |
| **1-4 Family** | 967,941 | 1,001,809 | 1,075,912 | 1,323,435 | 1,332,867 | 1,528,174 | 1,606,442 | 1,635,746 | +23.6% |
| **HELOC** | 137,011 | 153,541 | 174,005 | 196,243 | 215,463 | 238,268 | 258,787 | 276,917 | +41.1% |
| **Farmland/Ag** | 252,232 | 276,785 | 274,703 | 296,898 | 300,388 | 305,921 | 317,999 | 321,254 | +8.2% |
| **Total Loans Net** | 27,665,413 | 28,266,606 | 28,798,086 | 29,503,320 | 30,619,723 | 32,486,420 | 32,313,774 | 31,842,064 | +7.9% |

---

## 🔴 SMOKING GUN: C&I vs Construction Migration

| Quarter | Construction | C&I | Const Δ (QoQ) | C&I Δ (QoQ) | Net Shift |
|---------|-------------|-----|---------------|-------------|-----------|
| Q1 2024 | 12,322 | 1,355 | — | — | — |
| Q2 2024 | 11,491 | 1,499 | -831 | +144 | |
| Q3 2024 | 9,828 | 1,503 | -1,663 | +4 | |
| Q4 2024 | 9,523 | 1,729 | -306 | +225 | |
| Q1 2025 | 9,209 | 2,066 | -314 | +337 | |
| Q2 2025 | 8,685 | 2,330 | -524 | +264 | |
| Q3 2025 | 8,490 | 2,871 | -195 | +540 | |
| Q4 2025 | 7,778 | 3,432 | -712 | +561 | |

**Over 8 quarters:**
- Construction: -$4,544M (-36.9%)
- C&I: +$2,077M (+153.3%)
- ~46% of construction decline migrated to C&I

This is textbook **Memo Item 3 reclassification** — construction/CRE loans completing and moving to C&I "secured by real estate" to make the CRE concentration look lower.

---

## Credit Quality

### Noncurrent Loans ($000s)

| Quarter | Noncurrent | % of Loans | QoQ Change |
|---------|-----------|------------|------------|
| Q1 2024 | 61,197 | 0.22% | |
| Q2 2024 | 85,266 | 0.30% | +39% |
| Q3 2024 | 175,665 | 0.61% | +106% |
| Q4 2024 | 131,494 | 0.45% | -25% |
| Q1 2025 | 62,719 | 0.20% | -52% |
| Q2 2025 | 58,545 | 0.18% | -7% |
| Q3 2025 | 149,744 | 0.46% | +156% |
| **Q4 2025** | **341,223** | **1.07%** | **+128%** |

🔴 **Noncurrent spiked 2.3x in one quarter.** Worst level in the dataset. Ratio more than doubled from 0.46% → 1.07%.

### Past Due 30-89 Days (Q4 2025 only, $000s)
- Real Estate: $20,527
- C&I: $10,143
- Consumer: $11,068
- **Total: $41,738**
- Past Due 90+: **$0** across all categories (everything noncurrent is on nonaccrual, not just late)

### ACL & Charge-offs ($000s)

| Quarter | ACL Balance | QoQ Chg | NCOs (quarterly) | NCO Rate (ann.) |
|---------|------------|---------|-------------------|-----------------|
| Q1 2024 | 365,935 | | ~$10,600 | 0.15% |
| Q2 2024 | 407,079 | +41,144 | ~$12,700 | 0.18% |
| Q3 2024 | 420,058 | +12,979 | ~$46,400 | 0.64% |
| Q4 2024 | 465,547 | +45,489 | ~$37,200 | 0.50% |
| Q1 2025 | 488,150 | +22,603 | $38,417 | 0.50% |
| Q2 2025 | 518,634 | +30,484 | $35,215 | 0.43% |
| Q3 2025 | 532,341 | +13,707 | $48,313 | 0.60% |
| **Q4 2025** | **475,721** | **-56,620** | **$50,569** | **0.64%** |

🔴 **ACL cut $56.6M (-10.6%) while charge-offs accelerated to highest quarterly rate.** Noncurrent doubled same quarter. This is the "reserves cut while losses accelerated" pattern — provisioning in reverse.

### ACL Coverage Ratio

| Quarter | ACL | Noncurrent | Coverage |
|---------|-----|-----------|----------|
| Q3 2024 | 420,058 | 175,665 | 2.39x |
| Q4 2024 | 465,547 | 131,494 | 3.54x |
| Q1 2025 | 488,150 | 62,719 | 7.78x |
| Q2 2025 | 518,634 | 58,545 | 8.86x |
| Q3 2025 | 532,341 | 149,744 | 3.55x |
| **Q4 2025** | **475,721** | **341,223** | **1.39x** |

🔴 **Coverage collapsed from 8.86x → 1.39x in two quarters.** Below the 1.6x we had from management comments (difference likely due to FDIC vs company reporting definitions).

---

## Capital & Concentration

| Metric | Q4 2024 | Q4 2025 |
|--------|---------|---------|
| Total Assets ($000s) | 38,258,852 | 40,785,840 |
| Tier 1 Capital ($000s) | 5,115,692 | 5,488,755 |
| Total Equity ($000s) | 5,706,194 | 6,129,851 |
| Tier 1 Leverage Ratio | — | 11.72% |
| Tier 1 RBC Ratio | — | 13.64% |

### CRE Concentration (Q4 2025)
- CRE (Const + Nonres + Multi): $19,875,925
- CRE / Tier 1: **362%** (FDIC-derived, broad definition; management reports **358%** using their CRE scope — difference is definitional, ~$200M in loan classification)
- Total RE / Tier 1: **403%**
- Construction / Tier 1: **142%** (vs 100% guidance)

---

## FFIEC CDR CALL REPORT — Q4 2025 (Raw file pulled by Will, Mar 23)

### RCON2746 — MEMO ITEM 3: $1,289,437 ($000s) = $1.289 BILLION
**"Loans to finance commercial real estate, construction, and land development activities (not secured by real estate) included in Schedule RC-C, part I, items 4 and 9"**
- C&I total (RCON1766): $3,431,585
- **Memo Item 3 / C&I = 37.6%** ✅ Confirms prior estimate exactly
- Loans to NDFIs (RCONJ454): $2,742,514 — massive ($2.7B to non-bank financial institutions)

### RC-C Loan Composition Detail ($000s)
| Category | RCON | Amount |
|----------|------|--------|
| 1-4 fam construction | RCONF158 | 2,387,805 |
| Other construction/land | RCONF159 | 5,390,606 |
| Farmland | RCON1420 | 321,254 |
| HELOC | RCON1797 | 276,917 |
| 1-4 fam first lien | RCON5367 | 1,347,193 |
| 1-4 fam junior lien | RCON5368 | 11,636 |
| Multifamily | RCON1460 | 3,680,059 |
| Owner-occ nonfarm nonres | RCONF160 | 815,386 |
| **Other nonfarm nonres** | **RCONF161** | **7,602,069** |
| C&I | RCON1766 | 3,431,585 |
| Loans to NDFIs | RCONJ454 | 2,742,514 |
| Consumer other | RCONK207 | 4,258,482 |
| **Total** | RCON2122 | **32,317,785** |

### 🔴 RC-N — Noncurrent by Loan Type ($000s)
| Category | 30-89 Past Due | Noncurrent | Signal |
|----------|---------------|------------|--------|
| 1-4 fam construction | 1,176 | 130 | Clean |
| **Other construction/land** | **3,188** | **40,424** | 🔴 |
| Farmland | 10 | 611 | Clean |
| HELOC | 315 | 496 | Clean |
| 1-4 fam first lien | 11,581 | — | |
| 1-4 fam junior lien | 96 | — | |
| Multifamily | 0 | 576 | Clean |
| Owner-occ nonfarm nonres | 3,420 | 2,121 | Mild |
| **Other nonfarm nonres** | **741** | **256,727** | 🔴🔴🔴 |
| C&I | 10,143 | 2,703 | Low |
| All other loans | 0 | 0 | Clean |
| **TOTAL** | **41,738** | **341,223** | |

🔴🔴🔴 **OTHER NONFARM NONRESIDENTIAL = $256.7M of $341.2M noncurrent (75.2%)**
This is non-owner-occupied CRE — office, life sciences, retail. The same category where IQHQ, Pacific Center, Bioterra sit.
Construction noncurrent $40.4M is secondary driver (11.8%).

### Additional Key Fields
- Interest reserves on construction loans: $6,959,527 ($000s) — **$7.0B using interest reserves** (RCONG376). This means the majority of construction book ($7.0B of $7.8B) has interest reserves = borrowers aren't paying from cash flow
- Interest capitalized from reserves in Q4: $108,614 ($000s) = $108.6M (RIADG377)
- Pledged loans: $23,927,102 ($000s) = **$23.9B pledged** (74% of total loans)
- Loans to business credit intermediaries: $1,200,531 (RCONPV06)
- Loans to private equity funds: $772,151 (RCONPV07)
- Nonaccrual additions in prior 6 months: $322,199 ($000s) = $322M (RCONC410)

## What's Still Missing

1. **State-level breakdowns** — Not in this Call Report format. Need RC-C Part I geographic schedules or cross-reference with Summary of Deposits.
2. **Construction ACL breakdown** — Category-level ACL not in standard call report output. May need RC-R detail.

---

## Key Findings for Thesis

1. **C&I doubled (+98.5%) while construction fell 18.3%** — strongest quantitative evidence of Memo Item 3 reclassification at OZK specifically (not just industry-level H.8 data)
2. **Noncurrent exploded Q4 2025** — $341M, up from $150M, ratio 1.07%. Something big went nonaccrual.
3. **ACL cut INTO deterioration** — management released $56.6M reserves while charge-offs accelerated and noncurrent doubled. This is either confidence or recklessness.
4. **Coverage ratio collapsed to 1.39x** — one more bad quarter and ACL doesn't cover noncurrent loans
5. **Capital ratios look adequate** (Tier 1 13.6%) but CRE concentration remains 362% of Tier 1 — and that's AFTER the reclassification flatters the number
