# MARCO Data Source Implementation Checklist

**Created:** 2026-02-24
**Purpose:** Track implementation of new tourism data sources

---

## ✅ COMPLETED

### Florida Tourism Baseline (Feb 24, 2026)
- [x] Visit Florida 2025 preliminary data pulled
- [x] Canadian decline confirmed: -14.7% YoY (2.9M visitors)
- [x] CTI validated: 0.72 (2.9M / 4.0M baseline)
- [x] Filed: `baselines/FL_TOURISM_BASELINE_2026-02.md`

---

## 🔄 IN PROGRESS

### Google Trends
- [ ] Set up tracking for "flights to Florida" (Canada filter)
- [ ] Set up tracking for "Florida vacation" (Canada filter)
- [ ] Establish YoY baseline
- **Issue:** Google Trends rate-limiting API access; need manual browser pull

### Nevada Gaming
- [ ] Pull NV Gaming Control Board ARR (Dec 2025, Jan 2026)
- [ ] Pull UNLV Gaming Research 6-month summary
- **Source:** https://gaming.nv.gov/about-us/abbreviated-revenue-release-arr/
- **Source:** https://gaming.library.unlv.edu/reports/6_month_NV_25_12.pdf

### Airport Enplanements
- [x] **FLL December 2024 (FULL YEAR)** ✅ Added 2026-02-24
  - Total: 35.2M (+0.3% YoY)
  - Domestic: 27.9M (+2.4% YoY)
  - **International: 7.3M (-7.2% YoY) — H2 COLLAPSED**
  - H2 2024: -7.3% Jun → -23.6% Nov (peak stress)
  - **Filed:** `baselines/FLL_AIRPORT_DATA_2024.md`
- [x] **MIA 2024 + 2025 + Feb 2026 Daily** ✅ Added 2026-02-24
  - 2024: 55.9M (+6.85% YoY) — strong
  - **2025: 55.3M (-1.09% YoY) — FLIPPED NEGATIVE**
  - International 2025: -1.25%
  - **Feb 2026 Daily: -6.24% passengers, -8.26% flights (PEAK SNOWBIRD)**
  - **Filed:** `baselines/MIA_AIRPORT_DATA_2024-2025.md`
- [x] **MCO CYE 2024 vs 2025 + International O&D** ✅ Added 2026-02-24
  - Total: 57.7M (+0.8% YoY) — **OUTLIER, holding**
  - Domestic: 49.2M (-0.4%) — first weakness
  - International: 8.5M (+8.2%) — UK/Caribbean offsetting
  - **Theme park anchor effect:** Disney/Universal = must-go
  - **Budget Canadian collapsing:** Hamilton -75.7%, Winnipeg -14.2%
  - **Filed:** `baselines/MCO_AIRPORT_DATA_2024-2025.md`
- [ ] LAS December 2024 / January 2025
- [ ] PHX December 2024 / January 2025
- **Note:** PDF reports from airport authority websites

### FLORIDA AIRPORT TRIFECTA COMPLETE ✅

| Airport | Total | Intl | Canadian Exposure | Status |
|---------|-------|------|-------------------|--------|
| FLL | +0.3% | **-7.2%** | HIGH | 🔴 COLLAPSED |
| MIA | -1.09% | -1.25% | MEDIUM | 🟡 FLIPPING |
| MCO | +0.8% | +8.2% | MEDIUM | 🟢 HOLDING (theme parks) |

**Key Finding:** Canadian boycott hitting DISCRETIONARY travel (FLL beach, MIA cruise), not ANCHOR destinations (MCO theme parks). Budget routes collapsing first.

---

## 📋 TODO (This Week)

### Manual Browser Tasks
1. **Google Trends** — Open browser, manually pull:
   - "flights to Florida" filtered by Canada, last 12 months
   - "Florida vacation" filtered by Canada, last 12 months
   - Screenshot or export CSV

2. **Nevada Gaming** — Download PDFs:
   - ARR from gaming.nv.gov
   - UNLV summary reports

3. **Airport Data** — Find monthly passenger reports:
   - MIA: miami-airport.com/statistics
   - MCO: goaa.org/statistics
   - LAS: harryreidairport.com
   - PHX: skyharbor.com/statistics

---

## 🎯 Quick Reference: What We Added Tonight

### VX.tsv (New Vectors)
- VX-MARCO-STR-01: STR Hotel Performance
- VX-MARCO-APT-01: Airport Net Passenger Flow
- VX-MARCO-GTR-01: Google Trends Tourism Intent
- VX-MARCO-TAX-01: State Tourism Tax Receipts
- VX-MARCO-CTI-01: Canada Tourism Index (0.72)
- VX-MARCO-SBMD-01: Sun Belt Migration Delta (-534K)
- VX-MARCO-TX-04: Texas Net Domestic Migration (+67K)

### ML.tsv (Methodology)
- ML-STR-01: STR implementation plan
- ML-APT-01: Airport enplanement plan
- ML-GTR-01: Google Trends methodology
- ML-TAX-01: State tax receipts plan
- ML-CTI-01: CTI calculation methodology
- ML-SBMD-01: SBMD calculation methodology
- ML-MIG-06: Texas migration analysis

### FL.tsv (Catalysts)
- 7 new Priority 1 catalysts (STR, Airport, GTR, Tax)
- 2 new migration catalysts (Census 2026, CTI monthly)

---

## 📊 Data Sources by Lag Time

| Source | Lag | Frequency | Cost |
|--------|-----|-----------|------|
| Google Trends | ~1 week | Weekly | FREE |
| Airport PDFs | 30-45 days | Monthly | FREE |
| NV Gaming ARR | ~30 days | Monthly | FREE |
| Visit Florida | ~90 days | Quarterly | FREE |
| Census Migration | ~12 months | Annual | FREE |
| STR Hotel Data | ~2 weeks | Monthly | $500-2K/mo |

---

**Next Session:** Pull manual data or use browser automation for Google Trends
