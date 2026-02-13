# RQ-CREED-001: Bank CRE DQ Series Reconciliation

**Date:** 2026-01-27 | **Status:** COMPLETE

---

## RESOLUTION

The 1.56% vs 4.18% discrepancy is explained by **three simultaneous filters**:

### Series Definitions

| Series | Value (Q3 2025) | Scope | Bank Size | Property Type | DQ Definition |
|--------|-----------------|-------|-----------|---------------|---------------|
| **FRED DRCRELEXFACBS** | **1.56%** | All commercial banks | All banks | All CRE excl farmland (includes owner-occupied) | 30+ days or nonaccrual |
| FRED DRCRELEXFT100S | ~1.86% | Top 100 banks | >~$10B | Same as above | Same |
| FRED DRCRELEXFOBS | 1.14% | Banks outside top 100 | <~$10B | Same as above | Same |
| **FDIC QBP** | **4.18%** | Large banks | >$250B assets | **Non-owner-occupied only** | Past due + nonaccrual |

- **DRCRELACBS does not exist.** Likely confusion with DRCRELEXFACBS.

### Why They Differ

1. **Property scope**: FRED includes owner-occupied CRE (lower risk, repaid from business cash flows). FDIC 4.18% is non-owner-occupied only (repaid from rents — closer to CMBS universe).
2. **Bank size**: FRED blends all banks. Large banks (>$250B) show 4.18%. Small banks drag average down (1.14%).
3. **Mix effect**: Small banks have lowest DQ but highest CRE concentration relative to capital.

### Which Is the Right Comparator for CMBS?

**4.18% is the most methodologically appropriate** comparator to CMBS (11.31% office), because:
- CMBS is also non-owner-occupied
- CMBS originates from large institutions
- Both measure similar property risk profiles

The masking gap is **7.1pp** (11.31% vs 4.18%), not 9.75pp (11.31% vs 1.56%).

### Trend (4.18% series)
- Q3 2024: 4.99% (peak)
- 4th consecutive quarterly decline
- Pre-pandemic average: 0.59%
- Still 7x pre-pandemic

### Modification Impact
- Modifications suppress bank DQ (banks can modify freely; CMBS servicers cannot)
- St. Louis Fed: 66% increase in CRE modifications through Q2 2025
- Modified loan balance: $39.3B (Mar 2025), up 86% from $21.1B (Mar 2024)
- Impact on DQ suppression not separately quantifiable with public data

### Gaps Remaining
- Property-type breakdown within bank portfolios (FRED does NOT separate office from MF from retail)
- 60+ vs 90+ day sub-buckets (Call Report has them; FRED may not publish separately)
- Exact modification-suppression effect on DQ count

### CREED Action
- VX-CREED-1.02 updated to 4.18% ORANGE (confirmed)
- Note: 4.18% is declining (from 4.99% peak) — trend is improving even as level is elevated
- The masking gap is real but smaller than initially modeled

---

*RQ-CREED-001 Complete | Source: FRED, FDIC QBP, FFIEC Call Reports*
