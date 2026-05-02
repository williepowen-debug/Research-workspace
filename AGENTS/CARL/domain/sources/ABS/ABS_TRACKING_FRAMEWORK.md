# ABS TRUSTEE REPORTS TRACKING FRAMEWORK

**Purpose:** Real-time consumer payment stress monitoring via ABS monthly performance data (30-45 day lag vs NY Fed's 2-3 month lag)

**Last Updated:** 2026-02-11  
**Owner:** CARL  
**Status:** ACTIVE

---

## THESIS

ABS trustee reports provide the **earliest publicly available** read on consumer payment behavior:

- **30-45 day lag** from payment activity (vs NY Fed's 60-90 day lag)
- **Monthly frequency** (vs NY Fed's quarterly)
- **Granular vintage tracking** — can isolate 2024/2025 originations vs 2019 baseline
- **Payment Rate = Leading Indicator** — drops 1-2 months BEFORE delinquencies rise

**Strategic Value:**
1. Detect stress **before** it appears in NY Fed data
2. Confirm/refute LABOR→CARL transmission hypothesis in near real-time
3. Geographic stress signals (issuer-specific concentrations)
4. Early warning for REGINALD (bank portfolio deterioration)

---

## DATA SOURCES

### Primary Source: SEC EDGAR Form 10-D
**What:** Monthly/quarterly ABS distribution reports  
**Where:** https://www.sec.gov/cgi-bin/browse-edgar  
**How to Search:**
1. Go to EDGAR Company Search
2. Enter trust name (e.g., "Discover Card Master Trust I")
3. Filter by form type: "10-D"
4. Most recent filing shows latest performance data

**Key Disclosures in Form 10-D:**
- Principal Payment Rate (%)
- Delinquency buckets (30+, 60+, 90+ days)
- Charge-off Rate (%)
- Pool balance and composition
- Vintage performance tables
- Geographic concentration (if disclosed)

### Secondary Source: Issuer Investor Relations Sites
Many issuers post monthly performance data directly:

| Issuer | Trust Name | IR Website |
|--------|------------|-----------|
| **Discover** | Discover Card Master Trust I | investor.discover.com → ABS Performance |
| **American Express** | American Express Credit Account Master Trust | ir.americanexpress.com → Fixed Income |
| **Capital One** | Capital One Multi-asset Execution Trust | investors.capitalone.com → Credit Card ABS |
| **Synchrony** | Synchrony Credit Card Master Note Trust | investors.synchrony.com → ABS |
| **Santander** | Santander Drive Auto Receivables Trust | santanderconsumerusa.com/investor-relations |
| **Ally** | Ally Auto Receivables Trust | ally.com/about/investor |
| **Exeter** | Exeter Finance auto trusts | sec.gov/edgar (CIK: 0001567338) |

**Advantage of IR sites:** Often post before SEC filing deadline (within 5-10 days of month-end)

---

## KEY METRICS TO TRACK

### 1. Payment Rate (% of balance paid monthly) — **LEADING INDICATOR**

**What it measures:** % of outstanding balance that borrowers pay down each month  
**Why it leads:** Consumers reduce payments BEFORE missing them entirely  
**Typical baseline:**
- Credit Card: 20-25% (healthy), <18% (stress)
- Auto: 4-5% (healthy), <3.5% (stress)

**Alert Thresholds:**
- 🟡 YELLOW: Payment rate drops >2% MoM
- 🟠 ORANGE: Payment rate <18% (CC) or <3.5% (auto)
- 🔴 RED: Payment rate declining 3+ consecutive months

### 2. 30+ Day Delinquency Rate

**What it measures:** % of accounts 30+ days past due  
**Why it matters:** Early-stage stress before charge-offs  
**Typical baseline:**
- Prime Credit Card: 2-3%
- Subprime Credit Card: 6-8%
- Prime Auto: 1-2%
- Subprime Auto: 8-12%

**Alert Thresholds:**
- 🟡 YELLOW: >4.5% (prime CC), >10% (subprime CC)
- 🟠 ORANGE: >6% (prime CC), >12% (subprime CC)
- 🔴 RED: Rising for 3+ consecutive months above threshold

### 3. Charge-off Rate (annualized %)

**What it measures:** % of balances written off as uncollectible  
**Why it matters:** Final confirmation of credit deterioration  
**Typical baseline:**
- Prime Credit Card: 2-4%
- Subprime Credit Card: 8-12%
- Prime Auto: 0.5-1.5%
- Subprime Auto: 6-10%

**Alert Thresholds:**
- 🟡 YELLOW: >6% (prime CC), >12% (subprime CC)
- 🟠 ORANGE: >8% (prime CC), >15% (subprime CC)
- 🔴 RED: Exceeds 2019 peak by >2pp

### 4. Vintage Performance (2024/2025 vs 2019 baseline)

**What it measures:** Performance of recent originations vs pre-pandemic baseline  
**Why it matters:** Identifies underwriting quality deterioration  
**Key comparison:** 2024/2025 originations should perform BETTER than 2019 if underwriting standards held

**Alert Thresholds:**
- 🟡 YELLOW: 2024/2025 vintage DQ rate >1.5x 2019 at same age
- 🟠 ORANGE: 2024/2025 vintage DQ rate >2x 2019
- 🔴 RED: 2024/2025 vintage DQ accelerating vs prior month

---

## WATCHLIST

### Credit Card ABS (Target: 5-6 trusts)

| Trust | Issuer | CIK | Asset Type | Priority | Notes |
|-------|--------|-----|------------|----------|-------|
| **Discover Card Master Trust I** | Discover Bank | 0000894329 | CC | 🔴 CRITICAL | Large issuer, broad borrower base |
| **American Express Credit Account Master Trust** | AmEx | 0001393612 | CC | 🔴 CRITICAL | Prime/super-prime benchmark |
| **Capital One Multi-asset Execution Trust** | Capital One | 0000927628 | CC | 🔴 CRITICAL | Mix of prime/subprime |
| **Synchrony Credit Card Master Note Trust** | Synchrony | 0001601712 | CC | 🟠 HIGH | Retail card exposure (store cards) |
| **Citibank Credit Card Issuance Trust** | Citibank | 0001131579 | CC | 🟠 HIGH | Major bank issuer |
| **Bank of America Credit Card Trust** | BofA | 0001067983 | CC | 🟡 MEDIUM | Cross-reference with REGINALD |

**Selection Criteria:**
- Size (>$10B outstanding)
- Monthly reporting frequency
- Consistent vintage disclosure
- Mix of prime/subprime exposure

### Auto ABS (Target: 5-6 trusts)

| Trust | Issuer | CIK | Asset Type | Priority | Notes |
|-------|--------|-----|------------|----------|-------|
| **Santander Drive Auto Receivables Trust** | Santander Consumer | 0001567338 | Auto (subprime) | 🔴 CRITICAL | Subprime bellwether |
| **Exeter Finance auto trusts** | Exeter Finance | 0001567338 | Auto (deep subprime) | 🔴 CRITICAL | S&P elevated loss expectations |
| **Ally Auto Receivables Trust** | Ally Financial | 0001613666 | Auto (prime/near-prime) | 🟠 HIGH | Large captive lender |
| **CarMax Auto Owner Trust** | CarMax | 0001170010 | Auto (used, near-prime) | 🟠 HIGH | Used car indicator |
| **Toyota Auto Receivables Owner Trust** | Toyota Financial | 0000908838 | Auto (prime) | 🟡 MEDIUM | Prime baseline comparison |
| **GM Financial Auto Leasing Trust** | GM Financial | 0001489669 | Auto lease | 🟡 MEDIUM | Lease vs retail comparison |

**Selection Criteria:**
- Coverage across credit spectrum (prime → deep subprime)
- Manufacturer captive vs independent lender
- New vs used car exposure
- Monthly reporting

---

## MONITORING PROTOCOL

### Monthly Cycle

**Week 1 (First 5 business days of month):**
- Check issuer IR sites for early performance data
- Look for press releases or investor updates

**Week 2-3 (Day 6-15 of month):**
- Pull Form 10-D filings from EDGAR (due within 15 days of distribution date)
- Extract key metrics (Payment Rate, 30+ DQ, Charge-off, Vintage)
- Update VX.tsv with current values and status

**Week 3-4 (Day 16-30):**
- Compare ABS data to prior month and 2019 baseline
- Check for threshold breaches
- Cross-reference with LABOR data (UI claims, temp employment)
- Update ML.tsv with significant findings
- Flag divergences to PROME if status change

### What to Check Every Month

For **each trust** in watchlist:

1. **Principal Payment Rate** — Compare to 3-month moving average
2. **30+ Day Delinquency** — MoM change and absolute level
3. **Charge-off Rate** — Annualized rate vs 2019/2024 baseline
4. **Vintage Tables** — 2024/2025 originations vs 2019 at same age
5. **Pool Composition** — Any shifts in FICO distribution or geography

### Trigger Conditions for ALERT

**Immediate escalation to PROME if:**
- Payment Rate drops >2% MoM across 3+ trusts
- 30+ DQ breaches ORANGE threshold on 2+ major trusts (e.g., Discover + Capital One)
- Subprime auto DQ >15% (Santander or Exeter)
- 2024/2025 vintage DQ accelerates vs prior month across multiple issuers
- ABS data shows stress that NY Fed data does NOT yet show (divergence signal)

---

## THRESHOLDS

### Credit Card ABS

| Metric | GREEN | YELLOW | ORANGE | RED |
|--------|-------|--------|--------|-----|
| Payment Rate | >20% | 18-20% | 15-18% | <15% |
| 30+ Day DQ | <4% | 4-5% | 5-7% | >7% |
| Charge-off Rate | <5% | 5-7% | 7-10% | >10% |
| Vintage (2024/2025 vs 2019) | <1.2x | 1.2-1.5x | 1.5-2x | >2x |

### Auto ABS (Subprime)

| Metric | GREEN | YELLOW | ORANGE | RED |
|--------|-------|--------|--------|-----|
| Payment Rate | >4% | 3.5-4% | 3-3.5% | <3% |
| 30+ Day DQ | <10% | 10-12% | 12-15% | >15% |
| Charge-off Rate | <8% | 8-10% | 10-12% | >12% |
| Vintage (2024/2025 vs 2019) | <1.3x | 1.3-1.6x | 1.6-2x | >2x |

**Notes:**
- Subprime auto thresholds are higher than prime by design
- Payment rate thresholds calibrated to 2019 baseline
- Vintage comparison uses "months on book" to normalize

---

## INTEGRATION WITH OTHER SIGNALS

### 1. LABOR → CARL (Leading Indicator)

**Cross-reference:**
- LABOR: UI exhaustion calendar (FL.tsv from LABOR)
- CARL: ABS payment rate should drop 30-60 days AFTER exhaustion begins

**Test Case: Florida**
- LABOR shows FL WARN notices +76% YoY (Q4 2025)
- CARL shows FL foreclosures +190% YoY (Q4 2025)
- **Hypothesis:** ABS payment rate for FL-concentrated issuers should drop in Q1 2026

**How to track:**
- Identify issuers with high FL exposure (if disclosed in 10-D geographic tables)
- Compare FL-heavy trusts vs national trusts
- Flag divergence: FL stress showing first = confirms LABOR→CARL transmission

### 2. ABS vs NY Fed (Divergence Detection)

**NY Fed Quarterly Household Debt Report:**
- Released ~45 days after quarter-end
- Q4 2025 data released Feb 10, 2026
- Next: Q1 2026 data expected ~May 15, 2026

**ABS Advantage:**
- January 2026 data available ~Feb 15 (30 days earlier)
- February data available ~Mar 15 (45 days earlier)
- March data available ~Apr 15 (30 days earlier than NY Fed Q1 report)

**Divergence Signals to Watch:**
- ABS shows accelerating DQ but NY Fed lags (confirms ABS leading value)
- ABS shows stress in specific segments (e.g., subprime auto) before aggregate data reflects it
- Geographic stress (FL) visible in ABS before national data

### 3. CARL → REGINALD (Bank Portfolio Impact)

**Timeline:**
- ABS stress detected at T+0
- Banks report consumer loan NCOs at earnings (45-90 days lag)
- Stock reprices when guidance cuts occur

**How to use:**
- If Discover ABS shows stress in Jan 2026, expect Discover Bank (DFS) to report elevated NCOs in Q1 earnings (late April)
- If Capital One ABS deteriorates, expect COF Q1 earnings impact
- Cross-reference ABS signals with REGINALD bank watchlist

**Early Warning:**
- ABS stress in Jan-Feb 2026 → Bank earnings warnings in Apr-May 2026 → Stock repricing

---

## BASELINE DATA (To Be Established)

### Target: Pull 2-3 Major Trusts for Baseline

**Trusts to baseline first:**
1. **Discover Card Master Trust I** (CIK: 0000894329)
2. **Capital One Multi-asset Execution Trust** (CIK: 0000927628)
3. **Santander Drive Auto Receivables Trust** (CIK: 0001567338)

**Data to capture:**
- Latest month performance (Jan 2026 if available)
- 3-month trend (Oct-Dec 2025)
- 2019 baseline (same months)
- Vintage tables for 2024/2025 originations

**Where baseline data will be stored:**
- Raw data: `domain/sources/ABS/` (PDF/Excel downloads)
- Extracted metrics: `domain/workbook/VX.tsv`
- Analysis: `domain/workbook/ML.tsv` entries

---

## DELIVERABLES STATUS

- [x] **Framework document created** (this file)
- [ ] **VX.tsv vectors added** (ABS-specific vectors)
- [ ] **ML.tsv master log created**
- [ ] **STATUS.md updated** (ABS monitoring section)
- [ ] **Baseline data pulled** (Discover, Capital One, Santander)
- [ ] **Monthly monitoring protocol tested** (first cycle)

---

## RESEARCH NOTES

### Why Payment Rate is a Leading Indicator

1. **Behavioral economics:** Consumers reduce discretionary spending → pay down less debt BEFORE missing payments
2. **Cash flow squeeze:** When liquidity tightens, borrowers make minimum payments (or less) but stay current
3. **Observable lag:** Payment rate drops 1-2 months before 30+ DQ rises

**Evidence:**
- 2008-2009: Payment rates dropped Q3 2008, DQ spiked Q4 2008-Q1 2009
- 2020: Payment rates surged (stimulus), DQ dropped with 2-month lag
- 2023-2024: Payment rates softening preceded current DQ rise

### Why ABS Data Beats Aggregate Sources

1. **Granularity:** Can track specific vintages, issuers, geographies
2. **Frequency:** Monthly vs quarterly
3. **Timeliness:** 30-45 day lag vs 60-90 day lag
4. **Transparency:** Standardized Form 10-D disclosures

**Limitation:**
- Only covers securitized portfolios (~40-60% of total consumer credit)
- Issuers may retain worse credits (selection bias)
- Not all issuers disclose same level of detail

**Mitigation:**
- Track multiple issuers to triangulate
- Compare ABS data to issuer's total portfolio (from earnings calls)
- Use ABS as **directional signal**, not absolute truth

---

## CALENDAR INTEGRATION

**Add to FL.tsv:**
- Monthly: First 15 days of each month → Check for Form 10-D filings
- Quarterly: NY Fed Household Debt Report → Compare to ABS trend
- Quarterly: Major bank earnings → Confirm ABS signals in bank NCO data

**Sample FL.tsv entries:**

```
ID: FL-CARL-ABS-001 | Date: 2026-02-15 | Event: ABS Jan 2026 Data Release | Domain: CREDIT-ABS | Expected Impact: Payment rate trend update | Priority: HIGH | Status: PENDING

ID: FL-CARL-ABS-002 | Date: 2026-03-15 | Event: ABS Feb 2026 Data Release | Domain: CREDIT-ABS | Expected Impact: Confirm/refute Jan trend | Priority: HIGH | Status: PENDING

ID: FL-CARL-ABS-003 | Date: 2026-05-15 | Event: NY Fed Q1 2026 Report | Domain: CREDIT | Expected Impact: Compare to ABS Jan-Mar trend | Priority: CRITICAL | Status: PENDING
```

---

*Framework established 2026-02-11. Begin baseline data collection.*
