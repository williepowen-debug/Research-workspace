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
- [ ] MIA December 2025 / January 2026
- [ ] MCO December 2025 / January 2026  
- [ ] LAS December 2025 / January 2026
- [ ] PHX December 2025 / January 2026
- **Note:** PDF reports from airport authority websites

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
