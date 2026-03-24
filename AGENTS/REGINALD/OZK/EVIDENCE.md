# OZK — Evidence Database
**Last Updated:** 2026-03-23

This file contains all current data supporting the OZK short thesis. Updated as new evidence arrives.

---

## FDIC GEOGRAPHIC — District-Level CRE Stress (Q4 2025)

OZK is HQ'd in Dallas (AR) but lends primarily in NY and FL/GA. District data by HQ, not loan origination.

### Nonfarm Nonresidential CRE Noncurrent by District
| District | Rate | vs National | OZK Relevance |
|----------|------|------------|---------------|
| NY | 1.57% | +27bps | **Primary origination market** |
| Atlanta | 1.36% | +6bps | **FL/GA loan book** |
| National | 1.30% | — | benchmark |
| Dallas (HQ) | 0.89% | -41bps | False clean signal — OZK counted here |

### 30-89 Day Pipeline (Leading Indicator — converts in 60-90 days)
| District | 30-89d | Noncurrent | PDNA Total | Signal |
|----------|--------|-----------|-----------|--------|
| **NY** (OZK loans) | **0.41%** | 1.57% | 1.98% | **Highest pipeline in country** |
| Atlanta (OZK loans) | 0.28% | 1.36% | 1.64% | Low pipeline = stress already noncurrent |
| National | 0.33% | 1.30% | 1.63% | benchmark |
| Dallas (OZK HQ) | 0.33% | 0.89% | 1.22% | Suppressed by E&P |

**NY 0.41% = 24% above national.** This is the pipeline feeding Wave 2 (Q2 2026).
**Atlanta 0.28% low but 1.36% noncurrent** = Wave 1 stress already impaired (Apr earnings).

### Extend-and-Pretend Gap (PDNA minus NCO)
| District | PDNA | NCO | Gap | Signal |
|----------|------|-----|-----|--------|
| **Dallas** (OZK HQ) | 1.88% | 0.19% | **1.69pts** | **Largest in country** — maximum deferred loss recognition |
| NY (OZK loans) | 1.56% | 0.40% | 1.16pts | Second worst |
| National | 1.56% | 0.62% | 0.94pts | benchmark |

### Community Bank Data
| District | 30-89d | Noncurrent | PDNA Est. |
|----------|--------|-----------|----------|
| Dallas (OZK HQ) | **0.42%** | 0.86% | 1.28% |
| CB National | 0.39% | 0.80% | 1.19% |

Dallas CB 30-89 pipeline tied for highest = hot at OZK's home district too.

**Source:** FDIC QBP Q4 2025, Tables V-A, III-B, VI-B. Full analysis → `sources/FDIC_QBP_Q4_GEOGRAPHIC_ANALYSIS.md`

---

## SPECIFIC DISTRESSED LOANS

| Loan | Amount | Status | Timeline |
|------|--------|--------|----------|
| **IQHQ RaDD (San Diego)** | $915M / ~$555M funded | 97% vacant (1 tenant: J. Craig Venter, 50K/1.7M SF). Cole est: worth ~$500M = underwater. SD life sci vacancy 25-29%. IQHQ under pressure (markdowns 4-23%, PIK loans 13.5-14%). **Two-year extension reported (Bisnow Oct 2024), +$87M equity injection.** Not disclosed in OZK filings — all from external sources. | **~Aug 2028** (extended from 2026) |
| Pacific Center (Sorrento Mesa) | $265M | Sold to Strategic Value Partners (distressed debt) Jan 5. Mgmt claims "par" and "one-off." | Done |
| Bioterra (Sorrento Mesa) | $202M | Vacant, facing distress. 5 miles from Pacific Center. | Active |
| Boston office | $72.4M | Charged off Q4 | Done |
| Lincoln Yards (Chicago) | $9M | Life sciences, charged off Q4 | Done |
| LA land parcel | $54.45M | Foreclosed | Done |

**IQHQ is the whale.** $300M writedown would exceed Q4 provision and consume ~half remaining ACL.

---

## INSIDER ACTIVITY — ALL SELLS, ZERO BUYS (Score 13)

| Date | Insider | Role | Action | Signal |
|------|---------|------|--------|--------|
| Feb 24 '26 | **Majumdar** | **CRO** | Sold 10.78% of holdings (419 shares), NO 10b5-1 plan | 🔴 Discretionary — the risk officer reducing exposure |
| Oct '24 + Jan '25 | Hicks | CFO | ~$944K across tranches (~22% of holdings) | 🔴 Material, staged |
| Various | Whipple | Director | $5.2M sold at $51.50 (stock now ~$42-44) | 🔴 Timed near high |
| — | Gleason | CEO (~10% owner) | Zero selling | 🟡 Position too large to sell — captive, not confident |
| 12 months | All insiders | — | **Zero buying** | 🔴 No one stepped in during drawdown |

**CRO selling discretionarily while bank cuts reserves = strongest single insider signal in screen.**

Full detail → `sources/INSIDER_SCAN_OZK.md`

---

## INDUSTRY CONTEXT (FDIC QBP Q4 2025)

| Metric | Industry | Community Banks | OZK Comparison |
|--------|---------|----------------|---------------|
| Reserve coverage | 171.2% (declining) | 154.3% (-2.9pts QoQ) | ACL/Ann. NCOs = 1.6x — lowest in peer group |
| Problem banks | 60 (+69% from '22 trough) | — | Not on list (yet) but metrics worse than some that are |
| Nondep financial lending | +24.5% YoY | — | Banks feeding private credit at peak stress |
| Uninsured deposits | $8.14T (+7% YoY) | — | Flight risk if stress event hits concentrated CRE lender |
| Net charge-off rate | 0.63% (+15bps vs pre-pandemic) | — | OZK at 1.18% = nearly 2x industry |

Full data → `sources/FDIC_QBP_Q4_2025.md`

---

## CAPITAL RATIOS (Dec 2025, from Q4 Mgmt Comments + Financial Supplement)

**Note:** Bank OZK files with FDIC, not SEC — there is no 10-K. Primary filings are FFIEC Call Reports and 8-K equivalents.

| Ratio | Dec 2025 | Dec 2024 | Threshold | Status |
|-------|----------|----------|-----------|--------|
| CET1 | **11.70%** | 11.34% | 6.50% | OK on surface |
| Tier 1 | **12.50%** | 12.15% | 8.00% | OK on surface |
| Total RBC | **14.80%** | — | 10.00% | OK |
| TCE/TA | **12.79%** | — | — | |
| CRE/Tier 1 | **~358%** | ~415% | 300% ⚠️ | Improved but still 1.2x red line |
| CRE/TCE | **~387%** | — | — | |
| CRE/Total RBC | **~302%** | — | 300% ⚠️ | Barely above regulatory threshold |
| CRE + unfunded / Tier 1 | **~682%** | — | — | ~~900% unverifiable~~ |

TCE: $5,130M | TBV/share: $46.48 | Book/share: $52.46

### Adjusted CRE Concentration (Including Shadow NDFI + Memo Item 3)
| Metric | Reported | + Shadow CRE + MI3 |
|--------|---------|-------------------|
| CRE / Tier 1 | 358% | **405-416%** |
| Basis | On-balance CRE only | + $1.0-1.6B shadow CRE via NDFI + $1.289B Memo Item 3 |

OZK's $2.74B NDFI book (loans to bridge lenders, PE funds, BDCs) is positively correlated with CRE stress — wrong-way risk. CEO Gleason confirmed on Q3 2025 earnings call: **"a chunk of our NDFI loans that show up on our call report are actually RESG loans. And this goes back to our long-standing relationships with a lot of the debt funds that do commercial real estate lending."** Management's own admission: NDFI ≈ CRE debt fund exposure. Full analysis → `research/NDFI_SHADOW_CRE_ANALYSIS.md`

---

## FDIC API — CREDIT QUALITY TREND (Primary, Mar 23)

### Noncurrent Loans ($000s)
| Quarter | Noncurrent | % of Loans | QoQ | ACL Balance | ACL Coverage |
|---------|-----------|------------|-----|-------------|-------------|
| Q1 2024 | 61,197 | 0.22% | | 365,935 | 5.98x |
| Q2 2024 | 85,266 | 0.30% | +39% | 407,079 | 4.77x |
| Q3 2024 | 175,665 | 0.61% | +106% | 420,058 | 2.39x |
| Q4 2024 | 131,494 | 0.45% | -25% | 465,547 | 3.54x |
| Q1 2025 | 62,719 | 0.20% | -52% | 488,150 | 7.78x |
| Q2 2025 | 58,545 | 0.18% | -7% | 518,634 | 8.86x |
| Q3 2025 | 149,744 | 0.46% | +156% | 532,341 | 3.55x |
| **Q4 2025** | **341,223** | **1.07%** | **+128%** | **475,721** | **1.39x** |

🔴 Noncurrent 2.3x in one quarter. Coverage collapsed 8.86x → 1.39x in two quarters. ACL cut $56.6M while charge-offs accelerated.

### Charge-offs (YTD cumulative → quarterly implied)
| Quarter | YTD NCOs ($000s) | Quarterly | Ann. Rate |
|---------|-----------------|-----------|-----------|
| Q1 2025 | 38,417 | 38,417 | 0.50% |
| Q2 2025 | 73,632 | 35,215 | 0.43% |
| Q3 2025 | 121,945 | 48,313 | 0.60% |
| Q4 2025 | 172,514 | 50,569 | 0.64% |

Source: FDIC API (banks.data.fdic.gov), CERT 110, pulled Mar 23 2026. Full data → `sources/FDIC_API_CALL_REPORT_DATA.md`

### RC-N Noncurrent by Loan Type (Q4 2025, from FFIEC Call Report)
| Category | 30-89 Past Due ($000s) | Noncurrent ($000s) | % of Total NC |
|----------|----------------------|-------------------|--------------|
| **Other nonfarm nonres** | **741** | **256,727** | **75.2%** |
| **Other construction/land** | **3,188** | **40,424** | **11.8%** |
| Owner-occ nonfarm nonres | 3,420 | 2,121 | 0.6% |
| C&I | 10,143 | 2,703 | 0.8% |
| All other categories | 24,246 | 39,248 | 11.5% |
| **TOTAL** | **41,738** | **341,223** | |

🔴 **75% of all noncurrent loans are in "other nonfarm nonresidential"** — non-owner-occupied CRE (office, life sciences, retail). This is where IQHQ, Pacific Center, Bioterra sit. The stress is concentrated in the exact category the thesis targets.

### 🔴 Interest Reserves — Construction Book Artificiality
- $7.0B of $7.8B construction loans use interest reserves (RCONG376) — **89.7%**
- Q4 interest capitalized from reserves: $108.6M (RIADG377)
- Borrowers are NOT paying from cash flow. The bank is lending to itself to keep loans current. When reserves deplete or loans mature, these convert to nonaccrual.

### RCON2746 — Memo Item 3 CONFIRMED: $1.289 BILLION
- C&I total: $3,431,585 ($000s)
- Memo Item 3 / C&I = **37.6%** ✅ (matches prior estimate)
- Additional: $2.74B in loans to NDFIs (non-depository financial institutions) — debt-on-debt risk

Source: FFIEC Call Report (RSSD 107244), Q4 2025, pulled Mar 23 2026.

### Deposit Composition — Uninsured Exposure (FDIC API, 8 quarters)
| Quarter | Total Dep ($M) | Insured ($M) | Uninsured ($M) | Uninsured % | Brokered ($M) |
|---------|---------------|-------------|----------------|-------------|---------------|
| Q1 2024 | 29,406 | 19,538 | 9,922 | 33.7% | 609 |
| Q2 2024 | 29,944 | 19,785 | 10,483 | 35.0% | 621 |
| Q3 2024 | 30,572 | 20,330 | 10,778 | 35.3% | 636 |
| Q4 2024 | 31,043 | 20,462 | 11,214 | 36.1% | 638 |
| Q1 2025 | 31,926 | 21,019 | 11,591 | 36.3% | 652 |
| Q2 2025 | 33,522 | 21,772 | 12,446 | 37.1% | 657 |
| Q3 2025 | 33,985 | 22,805 | 12,012 | 35.3% | 667 |
| **Q4 2025** | **33,385** | **22,402** | **11,939** | **35.8%** | **662** |

**$11.9B uninsured = 35.8% of deposits.** This is the flight-risk pool in a stress scenario. For context, SVB was ~94% uninsured; First Republic was ~68%. OZK's 35.8% is moderate but not benign — $11.9B is 2.2x Tier 1 capital. A 20% run on uninsured ($2.4B) would require significant FHLB/discount window borrowing against already-74%-pledged loan book.

Uninsured deposits grew from $9.9B → $12.4B (peak Q2 2025) then declined $500M in H2 2025. Early outflow signal? Or seasonal. Worth watching.

Source: FDIC API (CERT 110), fields DEP/DEPINS/DEPUNA/DEPSMB/DEPLGB.

---

## KEY RISK METRICS (Dec 2025, primary sourced)

| Risk | Amount | Notes |
|------|--------|-------|
| Total Real Estate Loans | **$21,828M** | 67.5% of total |
| Construction/Land Dev | **$7,778M** | 24.1% (down from $9.52B — payoffs + curtailments) |
| Other CRE | **$8,412M** | Noncurrent: $258.8M (highest category) |
| Life Science (total commitment) | **$3.1B** | 10.7% of RESG. Funded split not disclosed. |
| Office (total commitment) | **$3.7B** | 12.8% of RESG. LTV 55% avg. |
| **Unfunded Commitments** | **$18.0B** | Down from $19.08B but still massive vs capital |
| NPLs | **$341M** | **1.07%** — doubled from $150M in Q3 (FDIC: $341,223 / $31,842,064) |
| NPAs | **$402M** | **0.99%** — doubled from $228M in Q3 |
| Classified/Criticized | **$984M** | Substandard non-accrual $341M, accrual $161M, special mention $421M |
| RESG FY2025 NCOs | **$130.5M** | 0.68% — 3.6x the 23-year avg of 0.19% |

### Q4 Substandard Non-Accrual Credits (Fig. 26)
| Location | Type | Balance | Q4 Charge-off | LTV | Notes |
|----------|------|---------|---------------|-----|-------|
| Boston, MA | Office | $156.4M | $72.4M | 95% | Equity partners can't agree. Bank moving to acquire title. |
| Santa Monica, CA | Office | $50.1M | $5.7M | 100% | 15% leased. Sponsor unwilling to support. |
| Chicago, IL | Life Science | $50.0M | $9.0M | 68% | Sponsor negotiating short sale at $50M. |
| Baltimore, MD | Land | $40.0M | — | 53% | $4.6M additional charge-off. Active buyer discussions. |

### Office Stress Signal
Two office loans reappraised in Q4: LTV jumped from 52.9% → 98.9% (+46pts) and 93.2% → 111.5% (+18pts, **underwater**). Both rated Special Mention.

Construction ACL: ~~"$85M" and "$139M" discrepancy~~ — category-level ACL not disclosed in Mgmt Comments. Need Call Report (RC-R / RI-C) to verify.

---

## MEMO ITEM 3 — HIDDEN CRE + RECLASSIFICATION EVIDENCE

| Metric | OZK | WAL | Metropolitan (failed) |
|--------|-----|-----|-----------------------|
| Memo3/C&I ratio | **37.6%** | 24.2% | 39.6% |
| Trend | ↓ Structural | ↑ GROWING | — |
| True CRE (on-B/S) | 71.5% | ~59% | — |
| Hidden in "Other" | $1.06B (RESG to NDFIs) | — | — |

FFIEC field: RCON2746. Screen: RC-C Part I → Item 4 (C&I) → Memo Item 3 → ratio >20% = flag.

### 🔴 FDIC API Confirms Reclassification at OZK (Mar 23, 2026)

**C&I doubled while construction fell — textbook Memo Item 3 migration:**

| Quarter | Construction ($M) | C&I ($M) | Const QoQ | C&I QoQ |
|---------|-------------------|----------|-----------|---------|
| Q1 2024 | 12,322 | 1,355 | — | — |
| Q2 2024 | 11,491 | 1,499 | -831 | +144 |
| Q3 2024 | 9,828 | 1,503 | -1,663 | +4 |
| Q4 2024 | 9,523 | 1,729 | -306 | +225 |
| Q1 2025 | 9,209 | 2,066 | -314 | +337 |
| Q2 2025 | 8,685 | 2,330 | -524 | +264 |
| Q3 2025 | 8,490 | 2,871 | -195 | +540 |
| Q4 2025 | 7,778 | 3,432 | -712 | +561 |

- **Construction: -$4,544M (-36.9%) over 8 quarters**
- **C&I: +$2,077M (+153%) over 8 quarters**
- ~46% of construction decline migrated to C&I
- This is OZK-specific evidence (not just industry H.8 data)

**✅ RCON2746 confirmed from FFIEC CDR:** $1.289B = 37.6% of C&I. See RC-N/RC-C section above.

---

*Raw sources → `sources/` | Deep analysis → `research/`*
