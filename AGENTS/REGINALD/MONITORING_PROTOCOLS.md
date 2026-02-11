# MONITORING PROTOCOLS

**Created:** February 11, 2026  
**Agent:** REGINALD  
**Purpose:** Standardized weekly and monthly monitoring routines for new tracking frameworks

---

## Weekly Monitoring Routine (Every Friday)

### 1. FHLB Advance Check (~4:30pm ET, Post-H.8 Release)

**Data Source:** Federal Reserve H.8 "Assets and Liabilities of Commercial Banks"  
**Release Time:** Fridays ~4:15pm ET  
**URL:** https://www.federalreserve.gov/releases/h8/current/

**Steps:**
1. Navigate to H.8 current release page
2. Find Table 2 or detailed breakdown showing "Borrowings from Federal Home Loan Banks"
3. Extract current week's value (use NOT seasonally adjusted for raw signal)
4. Update `domain/workbook/VX.tsv` → VX-REG-7.01:
   - Current_Value = [new reading]
   - Status = GREEN (<$700B) / YELLOW ($700-750B) / ORANGE ($750-800B) / RED (>$800B)
   - Last_Updated = [current date]
5. Calculate changes:
   - Week-over-week change
   - Month-over-month change  
   - % change from 2023 crisis peak ($675B)

**Alert Thresholds:**
- 🟡 **YELLOW**: Advances cross $700B → Note in ML.tsv, flag in STATUS.md
- 🟠 **ORANGE**: Advances cross $750B → Immediate note to main agent, update STATUS
- 🔴 **RED**: Advances cross $800B → URGENT alert, major thesis validation

**Cross-Check When Spike Detected:**
- VX-REG-7.02: FHLB collateral haircuts (tightening?)
- VX-REG-7.03: Banks shifting to Delivery Status? (forensic audit stress)
- VX-REG-4.01: Deposit flight accelerating?
- Fed Discount Window usage (if both spike = severe)

**Update Files:**
- `domain/workbook/VX.tsv` (Vector VX-REG-7.01)
- `domain/STATUS.md` (FHLB Dashboard section)  
- `domain/workbook/ML.tsv` (if threshold crossed or significant change)

**Time Required:** 10-15 minutes

---

### 2. BDC Monthly Report Check (Every Monday Morning)

**Purpose:** Catch newly released monthly reports from 5 BDCs that report monthly

**BDCs to Check:**
1. **PSEC** (Prospect Capital): ~20th of month → https://www.prospectstreet.com/investor-relations/monthly-portfolio-statistics
2. **FSK** (FS KKR Capital): ~15th of month → https://www.fskkcapital.com/investor-relations
3. **TCPC** (TCP Capital): Mid-month → https://ir.tcgbdc.com/financial-information/monthly-stockholder-reports
4. **MFIC** (MidCap Financial): ~20th of month → https://ir.midcapfinancial.com/financial-information  
5. **BXSL** (Blackstone Secured): ~15th of month → https://ir.bxsl.com/financial-information/monthly-reports

**Quick Scan:**
- Check investor relations pages for new monthly reports  
- Note which BDCs have released (most release mid-to-late month)
- Flag any dividend announcements or warnings

**If New Report Found → Proceed to Data Extraction (see below)**

**Time Required:** 5 minutes (just scanning)

---

## Monthly Deep Dive (First Friday of Month)

### BDC Cash Coverage Analysis

**Purpose:** Full update of all BDC cash coverage ratios

**Steps:**

#### 1. Data Collection (30-45 minutes)
For each BDC that reported, extract from monthly report:
- **Total NII** (Net Investment Income)
- **PIK Interest Income** (or calculate: Total Interest Income - Cash Interest Income)
- **Cash NII** = Total NII - PIK Income
- **Dividend Declared** (monthly amount)
- **Cash Coverage Ratio** = Cash NII / Dividend

**Extraction Template:**
```
BDC: [Ticker]
Report Month: [Month Year]
Total NII: $[X]M
PIK Income: $[Y]M  
Cash NII: $[X-Y]M
Monthly Dividend: $[Z]M
Coverage Ratio: [Cash NII / Dividend]x
Status: GREEN/YELLOW/ORANGE/RED
```

#### 2. Update Tracking File (10 minutes)
Update `domain/workbook/BDC_CASH_COVERAGE.tsv`:
- Fill in Cash_NII, Cash_Coverage_Ratio for each BDC
- Update Status based on thresholds:
  - 🟢 GREEN: >1.00x
  - 🟡 YELLOW: 0.90-1.00x
  - 🟠 ORANGE: 0.75-0.90x  
  - 🔴 RED: <0.75x or dividend cut
- Update Last_Updated date
- Add notes for any significant changes

#### 3. Trend Analysis (15 minutes)
Calculate month-over-month changes:
- Is coverage improving or deteriorating?
- Which BDCs crossed thresholds?
- Are PSEC/FSK (canaries) showing stress?
- Is ARCC (quality benchmark) stable?

#### 4. ML.tsv Logging (10 minutes)
If significant findings, log to `domain/workbook/ML.tsv`:
```
Entry_ID: ML-REG-[next number]
Date: [current date]
Category: BDC_Cash_Flow
Title: [e.g., "PSEC Cash Coverage Drops to 0.87x"]
Summary: [Key finding and implication]
Source: [BDC monthly report URL]
Diagnostic_Value: [HIGH/MEDIUM/LOW]
Vector_Link: VX-REG-2.03, BROCK vectors
Tags: BDC, PSEC, cash_coverage, dividend_risk
```

**Log if:**
- Any BDC crosses threshold (e.g., YELLOW → ORANGE)
- PSEC or FSK coverage <0.90x (canary signal)
- ARCC shows deterioration (quality benchmark failing)
- Sector-wide pattern emerges

#### 5. STATUS.md Update (10 minutes)
Update `domain/STATUS.md` → BDC Cash Flow Dashboard:
- Update coverage table with current ratios
- Update Status indicators  
- Note any threshold crossings
- Update "What Would Change Our View" if needed

#### 6. Cross-Reference Bank Exposure (5 minutes)
Check related bank vectors for correlation:
- VX-REG-6.05 (CFG): Fund finance exposure
- VX-REG-6.04 (WAL): Fund finance + multi-channel stress
- VX-REG-2.03: BDC NAV discount widening?

**Total Time Required:** 80-90 minutes (once per month)

---

## Alert Triggers (Check Immediately When Detected)

### FHLB Advance Alerts
- **YELLOW** (>$700B): Notable but not urgent, monitor closely  
- **ORANGE** (>$750B): Alert main agent, exceeds 2023 peak  
- **RED** (>$800B): URGENT, systemic stress, major thesis validation

### BDC Cash Coverage Alerts  
- **YELLOW** (<1.00x): Flag in weekly update, watch closely
- **ORANGE** (<0.90x): Alert main agent, dividend cut risk high
- **RED** (<0.75x or cut announced): URGENT, canary has fallen

### Immediate Actions for RED Alerts
1. Update STATUS.md immediately  
2. Log to ML.tsv with HIGH diagnostic value
3. Note in response to main agent (flag prominently)
4. Cross-check related vectors for correlation
5. Review bank watchlist for transmission (especially CFG, WAL, VLY)

---

## Quarterly Reviews

### FHLB Advance Quarterly Review
- Compare to same quarter prior year
- Analyze seasonal patterns  
- Review individual FHLB bank filings (when released)
- Check for changes in collateral requirements (VX-REG-7.02)

### BDC Sector Quarterly Review  
- ARCC earnings (quarterly reporter, sector benchmark)
- GSBD earnings (quarterly, quality check)
- Sector-wide trends: Is PIK still rising?
- Bank call reports: Fund finance / NDFI loan trends

---

## Data Sources Reference

### FHLB Data
- **Primary:** Fed H.8 (weekly) → https://www.federalreserve.gov/releases/h8/current/
- **Detailed:** FRED → Search "FHLB" series
- **System-Wide:** FHLB Office of Finance → https://www.fhlb-of.com/ (quarterly reports)

### BDC Data
**Monthly Reporters:**
- PSEC: https://www.prospectstreet.com/investor-relations/monthly-portfolio-statistics
- FSK: https://www.fskkcapital.com/investor-relations
- TCPC: https://ir.tcgbdc.com/financial-information/monthly-stockholder-reports
- MFIC: https://ir.midcapfinancial.com/financial-information
- BXSL: https://ir.bxsl.com/financial-information/monthly-reports

**Quarterly Reporters:**
- ARCC: https://ir.arescapitalcorp.com
- GSBD: https://www.goldmansachsbdc.com/investor-relations

**Sector Data:**
- CEF Connect (NAV discounts): https://www.cefconnect.com/
- BDC Investor (sector coverage): https://seekingalpha.com/instablog/bdc-investor

---

## Files to Maintain

### Weekly Updates
- `domain/workbook/VX.tsv` → VX-REG-7.01 (FHLB)
- `domain/STATUS.md` → FHLB Dashboard section

### Monthly Updates  
- `domain/workbook/BDC_CASH_COVERAGE.tsv` → All BDC data
- `domain/STATUS.md` → BDC Dashboard section
- `domain/workbook/ML.tsv` → Significant findings

### As Needed
- `domain/workbook/ML.tsv` → Alert triggers, threshold crossings
- `domain/STATUS.md` → Status level changes, thesis updates

---

## Success Metrics

### FHLB Monitoring Success
- ✅ VX-REG-7.01 updated every Friday (within 24 hours of H.8 release)
- ✅ No missed threshold crossings  
- ✅ Alert escalation protocol followed

### BDC Monitoring Success
- ✅ All monthly reports captured within 1 week of release
- ✅ BDC_CASH_COVERAGE.tsv fully updated by 5th of month
- ✅ Trend analysis completed monthly
- ✅ Cross-reference with bank vectors maintained

### Overall Success  
- ✅ Early warning signal if FHLB advances spike (weeks ahead of public recognition)
- ✅ Early warning signal if BDC dividends crack (quarters ahead of bank losses)
- ✅ Validated transmission paths from BDC stress → Bank stress

---

## Next Immediate Actions

### Week of Feb 11-17, 2026
- [ ] Friday Feb 14: First FHLB advance check from H.8
- [ ] Monday Feb 17: Check for BDC monthly reports (FSK ~Feb 15, BXSL ~Feb 15)

### Week of Feb 17-24, 2026  
- [ ] Monday Feb 17: Continue BDC report scanning
- [ ] ~Feb 20: PSEC, TCPC, MFIC monthly reports expected
- [ ] Friday Feb 21: Second FHLB advance check

### First Week of March 2026
- [ ] Friday March 7: First full monthly BDC deep dive
- [ ] Update STATUS.md with initial baseline coverage ratios
- [ ] Establish trend direction for each BDC

---

**This protocol ensures systematic monitoring of two high-signal stress indicators. FHLB advances = liquidity stress. BDC cash coverage = credit stress. Both lead KRE by quarters.**
