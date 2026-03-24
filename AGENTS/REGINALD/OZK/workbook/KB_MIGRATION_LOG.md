# KB Migration Log — OZK
**Date:** 2026-03-24 | **Migrated by:** Prome (subagent)

## Summary
- **Total rows:** 63 (+ header)
- **ID range:** KB-OZK-001 → KB-OZK-063
- **All rows verified:** 13 columns each

## Group Distribution
| Group | Rows | Notes |
|-------|------|-------|
| CRE_CONCENTRATION | 12 | Core thesis — geographic, type, adjusted ratios |
| DISTRESSED_LOANS | 9 | IQHQ, Bioterra, Pacific Center, 4 Q4 substandard credits |
| SHADOW_CRE | 7 | NDFI, counterparties, Blue Owl exit risk |
| CAPITAL_LIQUIDITY | 6 | Ratios, deposits, FHLB, pledged collateral |
| ACL_THINNING | 6 | Coverage collapse, NCOs, NPAs |
| MGMT_CREDIBILITY | 5 | CRO/CFO/Director selling, zero buying |
| GAP | 5 | State RC-C, Bioterra source, Pacific par, NCO mislabel, IQHQ vacancy |
| BULL_COUNTER | 5 | Capital buffer, rate relief, thin edge, zero wholesale, IQHQ deferred |
| MEMO_ITEM_3 | 3 | RCON2746 confirmed, C&I migration, peer comparison |
| MATURITY_WALL | 5 | Interest reserves, construction decline, vintage, DBRS, nonaccrual flow |

## Sources
- **Primary (A2):** 42 rows — FDIC API, FFIEC Call Report, Q4 Mgmt Comments, Form 4
- **Secondary (B2):** 10 rows — Commercial Observer, Bisnow, deep research
- **Derived (C3):** 3 rows — adjusted ratios, scenario estimates
- **Gap (F6):** 5 rows — known unknowns from audit

## Issues Found
1. **NCO rate mislabeling** (KB-OZK-059): "1.18%" labeled as Q4 rate throughout THESIS.md — actually FY2025 annualized. Q4 quarterly: 0.64%. Flagged as GAP row.
2. **Bioterra sourcing** (KB-OZK-057): $203M figure has no primary source. Needs CoStar/EDGAR verification.
3. **CRE/Tier 1 variance**: 358% (Mgmt Comments) vs 362% (FDIC API derived). 4pt gap likely scope/rounding — noted in KB-OZK-007.
4. **IQHQ vacancy date**: "97% vacant" from Oct 2024 — 5 months old, potentially stale (KB-OZK-060).
5. **Dallas PDNA gap** (KB-OZK-050): Methodologically problematic — OZK counted in Dallas stats but lends in NY/FL/GA. Noted in row.
6. **Maturity wall underrepresented**: Originally only 2 rows. Added 3 more (KB-OZK-061-063) on Mar 25. Two key claims ($13.8B vintage, DBRS 63%) rated D4 — sourced from Temple 8/THESIS.md with NO primary verification. Nonaccrual flow ($322M/6mo) is A2 from Call Report.

## Post-Migration Fixes (Mar 25, Prome direct)
- **KB-OZK-059:** Status changed ACTIVE → CORRECTED. NCO mislabeling was fixed in THESIS.md same day.
- **KB-OZK-061 (Vintage_2022):** Added as D4/ESTIMATE. $13.8B from Temple 8 — 10K extract explicitly says "not verifiable from Q4 filings." Flagged for historical Call Report verification.
- **KB-OZK-062 (DBRS_Vintage):** Added as D4/ESTIMATE. No primary source citation found anywhere in sources/ folder. Needs DBRS report link/date.
- **KB-OZK-063 (Nonaccrual_Flow):** Added as A2/EMPIRICAL. RCONC410 from FFIEC Call Report — verified primary data.

## Audit Report Integration
All 8 Priority 1 gaps (B1-B8) from AUDIT_REPORT_MAR23.md were reviewed. Five converted to GAP rows. Three were incorporated as notes on existing evidence rows (CRE ratio inconsistency, NDFI analysis gap, FHLB/pledged collateral).

All 5 weaknesses (C1-C5) noted in relevant rows via Notes field.
