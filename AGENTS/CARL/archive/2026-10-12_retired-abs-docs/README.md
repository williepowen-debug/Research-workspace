# ABS Data Sources Directory

This directory stores raw and extracted data from Asset-Backed Securities (ABS) trustee reports.

## Purpose
- Track monthly consumer payment stress via ABS Form 10-D filings
- 30-45 day earlier signal than NY Fed quarterly data
- Monitor payment rates (leading indicator) and delinquency rates

## Directory Structure

```
ABS/
├── README.md                          # This file
├── ABS_EXTRACTED_BASELINE.tsv         # Cleaned, tabulated baseline data
├── Discover_YYYY-MM.xlsx              # Raw Discover Card Master Trust data
├── CapitalOne_YYYY-MM.xlsx            # Raw Capital One MAET data
├── Santander_YYYY-MM.xlsx             # Raw Santander Drive auto data
└── [Other trust data files]
```

## Data Collection Protocol

**Monthly Cycle (15th of each month):**
1. Check SEC EDGAR for Form 10-D filings (due 15 days after distribution date)
2. Download raw data (Excel/HTML/PDF) from SEC or issuer IR site
3. Extract key metrics to ABS_EXTRACTED_BASELINE.tsv
4. Update VX.tsv with current values
5. Flag threshold breaches in STATUS.md

**Priority Trusts (Phase 1):**
- Discover Card Master Trust I (CIK: 0000894329)
- Capital One Multi-asset Execution Trust (CIK: 0000927628)
- Santander Drive Auto Receivables Trust (CIK: 0001567338)

**Key Metrics:**
- Principal Payment Rate (% of balance paid monthly) — LEADING INDICATOR
- 30+ Day Delinquency Rate
- 60+ Day Delinquency Rate
- 90+ Day Delinquency Rate
- Charge-off Rate (annualized)
- Pool Balance
- Average FICO (if disclosed)

## Data Sources

### Primary: SEC EDGAR
https://www.sec.gov/edgar/searchedgar/companysearch.html
- Search by trust name or CIK
- Filter form type: "10-D"
- Look for Exhibit 99.1 or Servicer's Certificate

### Secondary: Issuer Investor Relations Sites
- **Discover:** investor.discover.com → Fixed Income → ABS Performance
- **American Express:** ir.americanexpress.com → Fixed Income
- **Capital One:** investors.capitalone.com → Credit Card ABS
- **Synchrony:** investors.synchrony.com → ABS
- **Santander:** santanderconsumerusa.com/investor-relations
- **Ally:** ally.com/about/investor

## Threshold Validation

After baseline collection, validate VX.tsv thresholds match reality:

**Credit Card:**
- Payment Rate: GREEN >20%, YELLOW 18-20%, ORANGE 15-18%, RED <15%
- 30+ DQ: GREEN <4%, YELLOW 4-5%, ORANGE 5-7%, RED >7%

**Subprime Auto:**
- Payment Rate: GREEN >4%, YELLOW 3.5-4%, ORANGE 3-3.5%, RED <3%
- 30+ DQ: GREEN <10%, YELLOW 10-12%, ORANGE 12-15%, RED >15%

Adjust if baseline data suggests different appropriate levels.

## Integration

**Cross-Reference:**
- LABOR: UI exhaustion calendar → should predict ABS payment rate drops 30-60 days later
- NY Fed: Quarterly household debt report → ABS should lead by 30-60 days
- REGINALD: Bank earnings → ABS stress predicts bank NCO warnings 60-90 days later

**Test Case:**
- LABOR shows FL stress (WARN +76%, foreclosures +190%)
- ABS should show FL-concentrated trusts deteriorating first
- Confirms LABOR→CARL transmission chain

## Reference Documents

- **Framework:** `domain/sources/ABS/ABS_TRACKING_FRAMEWORK.md`
- **Protocol:** `domain/sources/ABS/ABS_BASELINE_PROTOCOL.md`
- **Implementation Summary:** `domain/sources/ABS/ABS_IMPLEMENTATION_SUMMARY.md`
- **Quick Reference:** `domain/sources/ABS/ABS_QUICK_REFERENCE.md`
- **Vectors:** `domain/workbook/VX.tsv` (VX-CARL-ABS-01 through ABS-14)
- **Calendar:** `domain/workbook/FL.tsv` (FL-CARL-ABS-001 through ABS-008)
- **Status:** `domain/STATUS.md` (ABS Monitoring section)

---

*Directory created 2026-02-11 as part of ABS tracking framework implementation.*
