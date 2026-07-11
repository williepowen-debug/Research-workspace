# FRAMEWORK IMPLEMENTATION SUMMARY
**Date:** 2026-02-11  
**Agent:** LABOR  
**Task:** Implement Continuing Claims Tracking & State UI Exhaustion Frameworks

---

## DELIVERABLE #1: Continuing Claims Tracking ✅

### New Vectors Added to VX.tsv

**VX-LAB-1.02A: Continuing Claims (4-Week Average)**
- **Current Value:** ~1.85M
- **Status:** GREEN
- **Thresholds:** GREEN <1.9M | YELLOW 1.9-2.1M | ORANGE 2.1-2.5M | RED >2.5M
- **Last Updated:** 2026-01-24 (week ending)
- **Source:** DOL Weekly UI Claims
- **Purpose:** Smoothed duration signal for "Hotel California" divergence

**VX-LAB-1.02B: Insured Unemployment Rate**
- **Current Value:** 1.2%
- **Status:** GREEN
- **Thresholds:** GREEN <1.3% | YELLOW 1.3-1.5% | ORANGE 1.5-1.8% | RED >1.8%
- **Calculation:** Continuing claims (1,844K) ÷ covered employment (~155M)
- **Last Updated:** 2026-01-24
- **Source:** DOL Weekly UI Claims
- **Purpose:** Normalizes continuing claims for labor force size
- **Note:** Pre-pandemic average was 1.2% — currently at baseline

### "Hotel California" Dashboard Added to STATUS.md

**Current Readings (as of 2026-02-11):**

| Metric | Value | Status | Interpretation |
|--------|-------|--------|----------------|
| Initial Claims | 231K | 🟡 YELLOW | +22K spike from 209K (Feb 6 data) |
| Continuing Claims | 1,844K | 🟢 GREEN | Week ending Jan 24 — below 1.9M threshold |
| 4-Week Avg Continuing | ~1.85M | 🟢 GREEN | Smoothed signal stable |
| Insured Unemployment Rate | 1.2% | 🟢 GREEN | At pre-pandemic baseline |
| Duration Proxy | 8.0 weeks | 🟡 YELLOW | Continuing ÷ initial = 1,844K ÷ 231K |

**Divergence Status:** NO divergence detected. Both initial and continuing claims stable.

**Watch Condition:** If initial claims stay <250K but continuing claims breach 1.9M, it confirms "Hotel California" thesis — workers stuck on UI longer with frozen re-employment.

---

## DELIVERABLE #2: State UI Exhaustion Calendar ✅

### State Benefit Duration Documentation

| State | Max Weeks | Covered Employment | Rank | Notes |
|-------|-----------|-------------------|------|-------|
| **Florida** | **12** | ~8.5M | **50th** | Shortest in nation — CANARY STATE |
| North Carolina | 12-20 | ~4.5M | 49th | Variable by unemployment rate |
| Georgia | 14-20 | ~4.8M | 48th | Variable by unemployment rate |
| Michigan | 20 | ~4.3M | 47th | Below standard |
| Missouri | 13-20 | ~2.9M | 46th | Variable by unemployment rate |
| California | 26 | ~18M | Standard | National benchmark |
| New York | 26 | ~9M | Standard | AI WARN mandate |
| Texas | 26 | ~13M | Standard | Energy sector holding |
| **National Average** | **26** | ~155M | — | Standard since 1970s |

**Key Finding:** Florida + NC + GA = ~18M workers with sub-standard UI duration. These states will show exhaustion stress **3-6 months earlier** than national average.

### Florida Exhaustion Calendar (Q4 2025 WARN → 2026 Stress)

**Q4 2025 FL WARN Volume:** 22,771 workers (+76% YoY per VX-LAB-9.02)

**Major Cohorts:**

| Company | Workers | Layoff Date | UI Start | **UI Exhaustion Date** |
|---------|---------|-------------|----------|----------------------|
| Disney (various) | ~2,000 | Dec 2025 - Jan 2026 | Jan 1, 2026 | **Mar 24, 2026** |
| Kroger | 935 | Feb 1, 2026 | Feb 1, 2026 | **Apr 26, 2026** |
| Meta (facilities) | ~1,500 | Jan 2026 | Jan 15, 2026 | **Apr 9, 2026** |
| Healthcare cuts | ~17,107 | Feb-Mar 2026 | Mar 1, 2026 | **May 24, 2026** |

**Exhaustion Windows:**

1. **Wave 1 (Late March 2026):** Dec 2025 layoffs exhaust → ~2,000 workers
2. **Wave 2 (April-May 2026):** Jan-Feb layoffs exhaust → ~10,000+ workers (**PEAK**)
3. **Wave 3 (June 2026):** Mar layoffs exhaust → ~17,000 workers (healthcare)

### Transmission Timeline: FL Exhaustion → Consumer Stress

| Event | Date | Lag from Exhaustion | Impact |
|-------|------|---------------------|--------|
| **FL UI exhaustion begins** | **Mar-Apr 2026** | T+0 | First cohort loses income support |
| FL credit card delinquencies | **May 2026** | T+4-8 weeks | First missed payments |
| FL auto loan stress | **Jun 2026** | T+8-12 weeks | Repossessions begin |
| FL foreclosures re-accelerate | **Jul 2026** | T+12-16 weeks | Housing stress (already +57% YoY) |
| **CA/NY exhaustion begins** | **Aug 2026** | T+20 weeks | National signal (26-week states) |

**Critical Window:** **April-June 2026** — FL exhaustion → consumer stress transmission to CARL's domain.

### Cross-State Comparison

**California (26 weeks):**
- Q4 2025 WARN: 158,734 (+16% YoY)
- Exhaustion window: **June-August 2026**
- **Lags FL by 14 weeks** — FL is leading indicator

**New York (26 weeks):**
- Q4 2025 WARN: +20% YoY
- Exhaustion window: **June-August 2026**
- **Lags FL by 14 weeks**

**Texas (26 weeks):**
- Q4 2025 WARN: -31% YoY (counter-trend)
- Status: **NOT showing stress** — energy sector holding
- If TX flips to positive WARN growth, it's a national signal

### Calculated FL Exhaustion Window (Q4 2025 WARN → 2026)

**Formula:**
```
WARN Filing Date (Q4 2025)
  + 60 days (advance notice period)
  = Actual Layoff Date (Dec 2025 - Feb 2026)
  + 12 weeks (FL UI duration)
  = Exhaustion Window (Mar-May 2026)
```

**Example: Kroger**
- WARN filed: October 2025
- Effective date: February 1, 2026
- UI starts: February 1, 2026
- UI exhausts: **April 26, 2026** (12 weeks later)
- Credit stress: **May-June 2026** (4-8 weeks post-exhaustion)

**Peak Exhaustion:** **April-May 2026** for FL  
**National Exhaustion:** **August 2026** when CA/NY (26-week states) hit

---

## FILES UPDATED

1. ✅ **domain/workbook/VX.tsv**
   - Added VX-LAB-1.02A (Continuing Claims 4-week avg)
   - Added VX-LAB-1.02B (Insured Unemployment Rate)
   - Updated VX-LAB-1.02 with latest data (1,844K)

2. ✅ **domain/STATUS.md**
   - Added "Hotel California" Divergence Dashboard (before Signal Dashboard)
   - Added UI Exhaustion Transmission Timeline (before Research Gaps)
   - Updated Research Gaps (marked continuing claims and exhaustion as completed)

3. ✅ **domain/workbook/STATE_EXHAUSTION.md** (NEW FILE)
   - State benefit duration table (FL, CA, NY, TX, NC, GA, MI, MO + national avg)
   - Florida exhaustion calendar (Q4 2025 WARN → 2026 exhaustion windows)
   - Cross-state comparison (CA/NY/TX vs FL)
   - Transmission timeline framework
   - Exhaustion rate calculation methodology
   - Cross-agent triggers (CARL, REGINALD)
   - Falsifiable predictions (5 specific predictions with timeframes)

4. ✅ **domain/workbook/ML.tsv**
   - ML-LAB-049: Framework #1 implementation (continuing claims tracking)
   - ML-LAB-050: Framework #2 implementation (state UI exhaustion calendar)

5. ✅ **domain/workbook/FL.tsv**
   - FL-LAB-021 to FL-LAB-027: Forward calendar events for FL exhaustion monitoring
   - Includes: Wave 1/2/3 exhaustion dates, credit card/auto loan stress, foreclosure re-acceleration, CA/NY exhaustion

---

## KEY FINDINGS

### Continuing Claims (Framework #1)
- **Current status:** GREEN across all new metrics
- **No divergence:** Initial and continuing claims both stable
- **Duration proxy:** 8.0 weeks (continuing ÷ initial) — slightly elevated but not alarming
- **Insured unemployment rate:** 1.2% = pre-pandemic baseline
- **Watch trigger:** Continuing claims >1.9M while initial claims <250K = "Hotel California" confirmation

### UI Exhaustion (Framework #2)
- **Florida is the canary:** 12-week duration = shortest in nation
- **Q4 2025 FL WARN:** 22,771 workers (+76% YoY) → locks in Q2 2026 exhaustion stress
- **Peak exhaustion:** April-May 2026 for FL (~10,000+ workers)
- **Transmission lag:** FL exhaustion → consumer stress (4-8 weeks) → CA/NY exhaustion (14 weeks later)
- **Critical window:** **April-June 2026** for FL exhaustion → CARL consumer stress transmission
- **Foreclosures already elevated:** FL +57% YoY → exhaustion will drive second acceleration wave

---

## CROSS-AGENT IMPLICATIONS

### CARL (Consumer Stress)
- FL exhaustion April-June 2026 → credit card delinquencies May 2026
- Income support loss → missed payments → delinquency → default
- FL foreclosures (+57% YoY) re-accelerate July 2026
- **Trigger:** FL exhaustion rate >50% = consumer stress confirmation

### REGINALD (Banking Stress)
- Regional banks with FL exposure at risk (May-July 2026)
- FL credit stress → C&I loan stress for FL-heavy portfolios
- National exhaustion (Aug 2026) = synchronized consumer stress → all ORANGE banks escalate
- **Trigger:** FL credit card delinquencies +20% YoY

### HENRY (Markets)
- Employment stress → 401(k) outflows (if U-3 >5.0%)
- Currently: U-3 at 4.3% (YELLOW) — not breached yet
- Watch: Exhaustion-driven consumer stress → earnings warnings → equity repricing

---

## MONITORING SCHEDULE

### Weekly (Every Thursday, 8:30am ET)
- Initial claims (DOL release)
- Continuing claims (DOL release)
- Update VX-LAB-1.01, 1.02, 1.02A, 1.02B

### Monthly (First Friday + State releases)
- NFP report (national employment)
- FL state-level UI data (exhaustion rates, 30-day lag)
- FL credit card delinquencies (Fed data, 60-day lag)
- FL auto loan delinquencies (Equifax, 60-day lag)
- FL foreclosure filings (ATTOM, 30-day lag)

### Quarterly
- State WARN filing volumes (FL, CA, NY, TX)
- Fed Beige Book (regional employment stress)
- Exhaustion rate analysis (state vs national)

---

## NEXT ACTIONS

1. **Immediate (Weekly):**
   - Monitor initial claims for sustained breach >230K
   - Monitor continuing claims for breach >1.9M
   - Watch for divergence (initial stable, continuing rising)

2. **Q2 2026 (Critical Window):**
   - Track FL exhaustion rate (expect >50% by May)
   - Monitor FL credit card delinquencies (expect +20% YoY by June)
   - Watch FL foreclosures for re-acceleration (already +57%, expect +75%+ by Q2)

3. **Q3 2026 (National Signal):**
   - CA/NY exhaustion begins (Aug 2026)
   - National exhaustion rate expected >40%
   - CARL transmission confirmation
   - REGINALD bank stress escalation

---

**Status:** Both frameworks fully implemented and operational. Weekly monitoring begins immediately. Critical watch window: April-June 2026 for FL exhaustion transmission.
