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
| NPLs | **$341M** | **1.06%** — doubled from $150M in Q3 |
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

## MEMO ITEM 3 — HIDDEN CRE

| Metric | OZK | WAL | Metropolitan (failed) |
|--------|-----|-----|-----------------------|
| Memo3/C&I ratio | **37.6%** | 24.2% | 39.6% |
| Trend | ↓ Structural | ↑ GROWING | — |
| True CRE (on-B/S) | 71.5% | ~59% | — |
| Hidden in "Other" | $1.06B (RESG to NDFIs) | — | — |

FFIEC field: RCON2746. Screen: RC-C Part I → Item 4 (C&I) → Memo Item 3 → ratio >20% = flag.

---

*Raw sources → `sources/` | Deep analysis → `research/`*
