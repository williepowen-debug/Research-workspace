# ABS BASELINE DATA COLLECTION PROTOCOL

**Purpose:** Establish baseline performance metrics for ABS watchlist trusts  
**Status:** READY FOR MANUAL EXECUTION (SEC blocks automated tools)  
**Created:** 2026-02-11

---

## WHY BASELINE IS CRITICAL

Baseline data provides:
1. **Comparison point** for detecting deterioration
2. **Threshold calibration** — are current thresholds appropriate?
3. **Trend establishment** — 3-month moving averages
4. **2019 vintage comparison** — underwriting quality assessment

Without baseline, ABS monitoring is just raw numbers. With baseline, it's actionable signal.

---

## DATA TO COLLECT

For each trust in watchlist, capture:

### Monthly Performance (Latest Available — Likely Jan 2026)
- **Principal Payment Rate** (%)
- **30+ Day Delinquency Rate** (%)
- **60+ Day Delinquency Rate** (%)
- **90+ Day Delinquency Rate** (%)
- **Charge-off Rate** (annualized %)
- **Pool Balance** ($)
- **Average FICO** (if disclosed)
- **Geographic Concentration** (if disclosed)

### 3-Month Trend (Oct-Dec 2025)
- Same metrics as above for prior 3 months
- Calculate: Month-over-month change
- Calculate: 3-month moving average

### Vintage Tables (If Available)
- 2019 originations: DQ rate at 12 months, 24 months, 36 months on book
- 2024 originations: DQ rate at 12 months on book
- 2025 originations: DQ rate at 6 months on book (if available)
- **Comparison:** 2024/2025 vs 2019 at same months-on-book

---

## PRIORITY TRUSTS FOR BASELINE (Phase 1)

### 1. Discover Card Master Trust I (CIK: 0000894329)
**Why First:** Largest credit card ABS issuer, transparent reporting, monthly data  
**Where to Find:**
- Primary: SEC EDGAR → Search company "Discover Card Master Trust I" → Filter Form 10-D
- Secondary: investor.discover.com → Fixed Income → ABS Performance

**Expected Data Location:**
- Most recent 10-D filing: ~15 days after month-end distribution
- Look for: Exhibit 99.1 or "Servicer's Certificate" attachment
- Key table: "Master Trust Performance Statistics"

**Manual Steps:**
1. Go to https://www.sec.gov/edgar/searchedgar/companysearch.html
2. Search: "Discover Card Master Trust I" or CIK "0000894329"
3. Filter form type: "10-D"
4. Click most recent filing (should be Jan 2026 data, filed ~Feb 10-15)
5. Open Exhibit 99.1 or similar (usually HTML or Excel)
6. Extract metrics to `domain/sources/ABS/Discover_YYYY-MM.xlsx` or `.txt`
7. Update VX.tsv with current values

### 2. Capital One Multi-asset Execution Trust (CIK: 0000927628)
**Why Second:** Mix of prime/subprime, large issuer, comparison to Discover  
**Where to Find:**
- Primary: SEC EDGAR → "Capital One Multi-asset Execution Trust"
- Secondary: investors.capitalone.com → Credit Card ABS

**Expected Data:** Similar structure to Discover (Servicer's Certificate)

### 3. Santander Drive Auto Receivables Trust (CIK: 0001567338)
**Why Third:** Subprime auto bellwether, critical for auto stress monitoring  
**Where to Find:**
- Primary: SEC EDGAR → "Santander Drive Auto Receivables Trust"
- Secondary: santanderconsumerusa.com/investor-relations

**Expected Data:** Auto ABS reports typically include:
- Payment Rate
- 30/60/90+ DQ rates
- Net Loss Rate (charge-offs)
- Static pool performance (vintage tables)

---

## DATA STORAGE STRUCTURE

```
domain/
└── sources/
    └── ABS/
        ├── Discover_2026-01.xlsx          # Raw data from SEC/IR site
        ├── Discover_2025-12.xlsx
        ├── Discover_2025-11.xlsx
        ├── CapitalOne_2026-01.xlsx
        ├── CapitalOne_2025-12.xlsx
        ├── Santander_2026-01.xlsx
        └── ABS_EXTRACTED_BASELINE.tsv     # Cleaned, tabulated data
```

**ABS_EXTRACTED_BASELINE.tsv Format:**

```
Trust	Month	Payment_Rate	DQ_30	DQ_60	DQ_90	Chargeoff_Rate	Pool_Balance	Avg_FICO	Notes
Discover_CC	2026-01	22.5%	3.8%	2.1%	1.9%	5.2%	$12.5B	720	Jan 2026 baseline
Discover_CC	2025-12	23.1%	3.6%	2.0%	1.8%	5.0%	$12.3B	721	Dec 2025
Discover_CC	2025-11	22.8%	3.5%	1.9%	1.7%	4.9%	$12.1B	722	Nov 2025
CapitalOne_CC	2026-01	20.3%	4.2%	2.5%	2.2%	6.1%	$18.2B	698	Mix prime/subprime
Santander_Auto	2026-01	3.8%	11.2%	7.8%	6.1%	9.5%	$8.5B	620	Subprime auto
```

---

## THRESHOLD VALIDATION

Once baseline collected, validate thresholds:

### Credit Card Payment Rate
- **Discover Jan 2026:** If 22.5%, then:
  - GREEN: >20% ✅ (baseline confirms)
  - YELLOW: 18-20%
  - ORANGE: 15-18%
  - RED: <15%

**Action:** If baseline significantly different from expected, adjust thresholds in VX.tsv

### Credit Card 30+ DQ
- **Discover Jan 2026:** If 3.8%, then:
  - GREEN: <4% ✅ (baseline confirms threshold is appropriate)
  - YELLOW: 4-5%
  - ORANGE: 5-7%
  - RED: >7%

### Subprime Auto 30+ DQ
- **Santander Jan 2026:** If 11.2%, then:
  - GREEN: <10%
  - YELLOW: 10-12% ⚠️ (Santander at YELLOW)
  - ORANGE: 12-15%
  - RED: >15%

---

## EXECUTION CHECKLIST

**Phase 1: Baseline Collection (Target: Feb 11-15, 2026)**
- [ ] Create `domain/sources/ABS/` directory
- [ ] Pull Discover Jan 2026 data from EDGAR or investor.discover.com
- [ ] Pull Discover Oct-Dec 2025 data (3-month trend)
- [ ] Pull Capital One Jan 2026 data
- [ ] Pull Capital One Oct-Dec 2025 data
- [ ] Pull Santander Jan 2026 data
- [ ] Pull Santander Oct-Dec 2025 data
- [ ] Create `ABS_EXTRACTED_BASELINE.tsv` with cleaned data
- [ ] Update VX.tsv Current_Value for VX-CARL-ABS-01 through ABS-12
- [ ] Log findings to ML.tsv (ML-CARL-ABS-002)

**Phase 2: Threshold Calibration (Target: Feb 16, 2026)**
- [ ] Compare baseline to expected thresholds
- [ ] Adjust VX.tsv Yellow/Orange/Red thresholds if needed
- [ ] Document rationale in ML.tsv (ML-CARL-ABS-003)

**Phase 3: First Monthly Cycle (Target: Mar 15, 2026)**
- [ ] Pull Feb 2026 data (released ~Mar 10-15)
- [ ] Compare Feb vs Jan (MoM change)
- [ ] Update VX.tsv with Feb values
- [ ] Check for threshold breaches
- [ ] Update STATUS.md if status changes
- [ ] Log to ML.tsv (ML-CARL-ABS-004)

---

## TROUBLESHOOTING

### Issue: Can't find Form 10-D filing
**Solution:** 
- Check if trust reports quarterly instead of monthly
- Try searching by issuer parent company (e.g., "Discover Financial Services")
- Check issuer IR site directly — often posts before SEC filing

### Issue: Data format inconsistent across trusts
**Solution:**
- Focus on core metrics that all trusts report: Payment Rate, DQ rates, Charge-offs
- Document differences in Notes column of ABS_EXTRACTED_BASELINE.tsv
- Some trusts call "Payment Rate" as "Principal Payment Rate" or "Monthly Payment Rate"

### Issue: Vintage tables not available
**Solution:**
- Not all trusts provide detailed vintage analysis
- Prioritize trusts that DO provide it (Discover, Capital One typically do)
- Vintage comparison is "nice to have" — Payment Rate and DQ trends are must-haves

### Issue: Geographic concentration not disclosed
**Solution:**
- Most trusts don't disclose state-level data
- Use issuer-level geography as proxy (e.g., Discover has broad national footprint)
- Focus on trusts where we can infer concentration (e.g., regional banks/lenders)

---

## SAMPLE EXTRACTION (Discover Card Master Trust I)

**Example 10-D Filing Structure:**

```
Form 10-D
├── Cover Page
├── Item 1: Distribution and Pool Performance
│   └── Exhibit 99.1: Servicer's Certificate
│       ├── Table 1: Master Trust Performance Statistics
│       │   ├── Principal Payment Rate: 22.5%
│       │   ├── 30+ Day Delinquency: 3.8%
│       │   ├── 60+ Day Delinquency: 2.1%
│       │   ├── 90+ Day Delinquency: 1.9%
│       │   ├── Net Charge-off Rate: 5.2% (annualized)
│       │   └── Pool Balance: $12.5B
│       ├── Table 2: Vintage Performance (if available)
│       │   ├── 2019 Originations at 36 months: 2.5% DQ
│       │   ├── 2024 Originations at 12 months: 3.1% DQ
│       │   └── 2025 Originations at 6 months: 1.8% DQ
│       └── Table 3: Geographic Distribution (if available)
└── Signatures
```

**What to Extract:**
- From Table 1: All performance metrics → to ABS_EXTRACTED_BASELINE.tsv
- From Table 2: Vintage comparison → note in ML.tsv if 2024/2025 > 2019
- From Table 3: Any state >10% concentration → note in ML.tsv (e.g., FL exposure)

---

## INTEGRATION WITH VX.tsv

After extracting data, update vectors:

**Example:**

```
Vector_ID: VX-CARL-ABS-01
Name: ABS CC Payment Rate (Discover)
Current_Value: 22.5%  ← UPDATE THIS
Status: GREEN  ← UPDATE THIS (22.5% > 20% threshold)
Last_Updated: 2026-02-11  ← UPDATE THIS
Source: EDGAR Form 10-D, Jan 2026 Servicer Certificate  ← UPDATE THIS
Notes: Baseline established; 3-mo avg: 22.8% (stable)  ← ADD THIS
```

---

## NEXT STEPS FOR PROME

Once baseline collected:
1. **Validate framework** — Does ABS data match expectations? Any surprises?
2. **Set calendar** — Monthly check-ins (FL.tsv entries for Feb 15, Mar 15, etc.)
3. **First comparison** — When Feb data arrives (~Mar 15), compare to baseline
4. **Divergence test** — When NY Fed Q1 2026 report releases (~May 15), compare ABS Jan-Mar trend to NY Fed aggregates

**This framework is now OPERATIONAL.** Baseline data collection is the final step before live monitoring begins.

---

*Protocol ready for execution. SEC blocks automated tools — manual extraction required.*
