# Real Wage & MOF Flow Framework Implementation
**Date:** February 11, 2026  
**Agent:** SAM  
**Status:** ✅ COMPLETE

---

## EXECUTIVE SUMMARY

Two new tracking frameworks implemented to monitor **Japan's policy collision** and **UST repatriation transmission**:

1. **Real Wage Growth vs Inflation Dashboard** — Tracks BOJ normalization constraint
2. **MOF Weekly Portfolio Flow Monitor** — Early warning system for insurer repatriation

**Current Status:**
- **Real Wages:** 🟠 **ORANGE** (0.0%) — BOJ TRAPPED, April collision risk HIGH
- **MOF Flows:** 🟢 **GREEN** (+¥366B/mo) — Normal outflow, no repatriation yet

**Key Finding:** Real wage stagnation creates **Takaichi-Ueda collision** at April BOJ meeting if Shunto 2026 (late March) delivers weak wage growth (<2.5%).

---

## FRAMEWORK #1: REAL WAGE GROWTH vs INFLATION DASHBOARD

### Current Readings (Feb 11, 2026)

| Metric | Value | Status | Source |
|--------|-------|--------|--------|
| **Tokyo CPI (Core)** | 2.0% YoY | 🟢 GREEN | Jan 2026, Stats Bureau (lead indicator) |
| **National CPI (Core-core)** | 2.4% YoY | 🟡 YELLOW | Jan 2026, Stats Bureau |
| **Nominal Wage Growth** | 2.40% YoY | 🟡 YELLOW | Dec 2025, Monthly Labor Survey |
| **Real Wage Growth** | **0.0%** | 🟠 **ORANGE** | 2.40% - 2.4% = 0.0% |

**Formula:** Real Wage Growth = Nominal Wage Growth - Core-core CPI

### Thresholds

| Real Wage Growth | Status | BOJ Policy Space | Interpretation |
|------------------|--------|------------------|----------------|
| **≥ +1.0%** | 🟢 **GREEN** | Can normalize freely | Consumption supported, Ueda can hike to 1.0%+ |
| **0% to +1.0%** | 🟡 **YELLOW** | Cautious hikes only | BOJ proceeds slowly, Takaichi tolerates |
| **-0.5% to 0%** | 🟠 **ORANGE** | **TRAPPED — cannot hike** | Current: BOJ stuck, hike = consumption collapse |
| **< -0.5%** | 🔴 **RED** | Forced to cut or YCC return | Crisis: D2 scenario (monetary dominance) |

### Shunto 2026 Catalyst (Late March)

**Shunto** = Japan's annual coordinated wage negotiations. Results announced **late March 2026**.

**Scenarios:**

| Shunto Result | Nominal Wages | Real Wages (vs 2.4% CPI) | BOJ April Response | Collision Risk |
|---------------|---------------|--------------------------|--------------------| ---------------|
| **Strong (≥3.5%)** | +3.5%+ | +1.1%+ (GREEN) | Hike to 0.50%, bullish | **LOW (20%)** |
| **Moderate (2.5-3.5%)** | +2.5-3.5% | +0.1% to +1.1% (YELLOW) | Hold, cautious | **MEDIUM (50%)** |
| **Weak (<2.5%)** | <2.5% | Negative (RED) | **TRAPPED** | **HIGH (70%+)** |

**Current probability distribution:**
- Strong: 20%
- Moderate: 55%
- Weak: 25%

### April BOJ Collision Probability

**Base case (Moderate Shunto):** 50%
- Real wages barely positive (+0.1% to +0.5%)
- Ueda signals **slow normalization** (no April hike)
- Takaichi "concerned" but tolerates
- Collision deferred to July

**Stress case (Weak Shunto):** 70%+
- Real wages turn **NEGATIVE** (RED threshold)
- Ueda faces impossible choice: hike (political suicide) OR pause (credibility death)
- **Takaichi escalation:** Katayama summons Ueda, Aida publicly criticizes BOJ
- **Market impact:** JGBs rally short-term → yen selloff resumes → import inflation worsens → vicious cycle

**Bull case (Strong Shunto):** 20%
- Real wages clearly positive (+1.0%+)
- Ueda hikes to 0.50% in April, signals more
- Takaichi tolerates (still below 0.75% ceiling)
- Collision deferred until Ueda pushes past 0.75%

**CURRENT ASSESSMENT (Feb 11):**  
**April Collision Probability: 50-55%** (weighted average of scenarios)

**Key catalyst:** Shunto results (last week of March) determine trajectory. If weak (<2.5%), collision probability jumps to 70%+.

---

## FRAMEWORK #2: MOF WEEKLY PORTFOLIO FLOW TRACKING

### Data Source

**URL:** https://www.mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/index.htm

**Direct data:**
- **Latest PDF:** .../week.pdf (released every Thursday, 8:50am JST)
- **Historical CSV:** .../week.csv

**Target metric:** "Residents transactions in foreign securities — **Bonds**" (¥ billions)

**Sign convention:**
- **Positive (+)** = Buying foreign bonds (capital outflow, normal)
- **Negative (-)** = Selling foreign bonds (**REPATRIATION**, stress signal)

### Current Readings (Jan 2026)

| Week Ending | Foreign Bond Flow (¥B) | Status |
|-------------|------------------------|--------|
| Jan 10 | +¥104,243 | 🟢 Buying (normal) |
| Jan 17 | +¥77,749 | 🟢 Buying (normal) |
| Jan 24 | +¥79,240 | 🟢 Buying (normal) |
| Jan 31 | +¥104,882 | 🟢 Buying (normal) |
| **Monthly Total** | **+¥366B** | **🟢 GREEN** |

**Interpretation:** Japanese investors (primarily life insurers) are still **NET BUYING** foreign bonds. No repatriation detected. Consistent with **base case** ($10-15B/mo gradual).

**Baseline:** January 2026 = +¥366B/mo net buying (normal capital outflow).

### Thresholds

| 4-Week Rolling Sum | Annualized Rate | Status | Phase | Market Impact |
|--------------------|-----------------|--------|-------|---------------|
| **> ¥0 (buying)** | Normal outflow | 🟢 **GREEN** (NOW) | Base case | Business as usual |
| **¥0 to -¥500B** | $40-70B/yr selling | 🟡 **YELLOW** | Early repatriation | Gradual UST supply |
| **-¥500B to -¥1T** | $70-140B/yr selling | 🟠 **ORANGE** | Accelerated stress | **LIQUID alert**, KRE risk |
| **< -¥1T** | >$140B/yr selling | 🔴 **RED** | Crisis liquidation | Global contagion |

**Conversion (at USD/JPY 156):** ¥100B/mo ≈ $640M/mo ≈ $7.7B/yr

### Monitoring Protocol

**WEEKLY (Every Thursday):**
1. Check MOF release (8:50am JST)
2. Extract "Residents transactions in foreign securities — Bonds"
3. Calculate 4-week rolling sum
4. Compare to thresholds
5. Watch for sign flip (positive → negative)

**ESCALATION TRIGGERS:**
- **YELLOW:** 4-week sum -¥500B to -¥1T → Notify LIQUID
- **ORANGE:** 4-week sum < -¥1T → LIQUID red alert, HENRY/REGINALD notified
- **RED:** Single week < -¥1T → Global contagion protocols

### Link to LIQUID Vector

**Current repatriation rates:**
- **Base case:** $80-120B/12-24mo ($7-10B/mo)
- **Stress case:** $150-250B/6-12mo ($20-40B/mo) ← **MOF ORANGE**
- **Crisis case:** $300-500B/3-6mo ($100-165B/mo) ← **MOF RED**

**MOF flow as leading indicator:** 1-4 week advance warning before quarterly IIP data.

**For LIQUID:** When MOF crosses -¥500B/mo (YELLOW), escalate to "repatriation acceleration confirmed."

---

## VECTORS ADDED TO VX.TSV

**Real Wage Tracking:**
- VX-SAM-8.01: Tokyo CPI (Core) — 2.0% YoY (GREEN)
- VX-SAM-8.02: National CPI (Core-core) — 2.4% YoY (YELLOW)
- VX-SAM-8.03: Nominal Wage Growth — 2.40% YoY (YELLOW)
- VX-SAM-8.04: Real Wage Growth — 0.0% (ORANGE) ← **KEY VECTOR**

**MOF Portfolio Flow:**
- VX-SAM-9.01: MOF Weekly Foreign Bond Flow — ¥366B/mo buying (GREEN)
- VX-SAM-9.02: MOF Monthly Repatriation Rate — ¥0B/mo (GREEN)

---

## STATUS.MD UPDATES

Added two comprehensive sections:

1. **REAL WAGE GROWTH vs INFLATION DASHBOARD**
   - Current readings (all components)
   - Threshold table with BOJ implications
   - Shunto 2026 catalyst analysis
   - April BOJ collision probability scenarios
   - Formula and interpretation

2. **MOF PORTFOLIO FLOW TRACKING — Weekly Repatriation Monitor**
   - Data source and navigation (exact URLs)
   - Sign convention explanation (critical!)
   - Current readings (Jan 2026 monthly total)
   - Threshold table with market impacts
   - Weekly monitoring protocol
   - Escalation triggers for PROME
   - Link to LIQUID vector (base/stress/crisis cases)
   - What drives repatriation (5 key triggers)

---

## KEY INSIGHTS

### Real Wage Constraint on BOJ

**The fundamental problem:**
- Nominal wages (2.40%) barely keeping pace with inflation (2.4%)
- Real wages effectively **zero** (ORANGE threshold)
- BOJ **cannot hike** in this environment without crushing consumption
- Ueda caught between normalization mandate and economic reality

**The collision:**
- Takaichi fiscal expansion → weak yen → import inflation → erodes real wages
- Ueda wants to hike → would strengthen yen → but real wages too weak to tolerate higher rates
- **April BOJ meeting** (after Shunto results late March) = decision point
- If Shunto weak (<2.5%), **collision probability 70%+**

**Implications:**
- BOJ likely **on hold through Q2** unless Shunto surprises strongly
- D2 scenario (monetary dominance) probability stays elevated (30-35%)
- Yen remains weak (USD/JPY 155-160 range)
- JGB yields capped by "BOJ cannot hike" narrative

### MOF Flow as Leading Indicator

**Current state:**
- **No repatriation detected** (Jan 2026: +¥366B buying)
- Consistent with **base case** ($10-15B/mo gradual)
- Life insurers still deploying capital abroad normally

**Why it matters:**
- **Weekly frequency** = real-time detection (vs quarterly IIP lag)
- **Institutional flows** = major investors (life insurers, pension funds)
- **Sign flip** (positive → negative) = clear repatriation signal
- **Magnitude** = phase identification (gradual vs stress vs crisis)

**Forward look:**
- Feb 19 20Y auction = next inflection point
- If auction **FAILS** (BTC <2.3x) → MOF flows likely turn negative within 2-4 weeks
- **First negative 4-week sum** = YELLOW alert to LIQUID
- **Sustained negative** (2+ months) = stress case confirmed

---

## APRIL BOJ COLLISION ASSESSMENT

**Probability: 50-55%** (as of Feb 11, 2026)

**Scenario breakdown:**

### BULL CASE (20% probability) — NO COLLISION
**Catalyst:** Strong Shunto (≥3.5% wage growth)
- Real wages turn positive (+1.0%+)
- Ueda hikes to 0.50% in April
- Takaichi tolerates (below 0.75% ceiling)
- JGBs sell off, yen strengthens moderately
- Collision deferred to July (when Ueda pushes toward 0.75%)

### BASE CASE (55% probability) — MODERATE TENSION
**Catalyst:** Moderate Shunto (2.5-3.5% wage growth)
- Real wages barely positive (+0.1% to +0.5%)
- Ueda signals **slow normalization**, holds in April
- Takaichi "concerned" but does not escalate
- JGBs range-bound, yen weak but stable
- **Collision probability shifts to July** (next decision point)

### STRESS CASE (25% probability) — HIGH COLLISION RISK
**Catalyst:** Weak Shunto (<2.5% wage growth)
- Real wages turn **NEGATIVE** (RED threshold)
- Ueda faces impossible choice: hike (economic damage) OR pause (credibility loss)
- **Takaichi escalation:** Katayama summons Ueda, Aida publicly criticizes
- **Market chaos:** JGBs whipsaw, yen selloff resumes, import inflation accelerates
- **Collision probability: 70%+**

**Key dates:**
- **Late March:** Shunto 2026 results announced (likely last week of March)
- **April 23-24:** BOJ Policy Meeting — Ueda must respond
- **Early May:** Market repricing based on BOJ decision

**If collision occurs (Stress case):**
- **Scenario D2 probability jumps to 50%+** (monetary dominance)
- **Scenario B probability falls to 30%** (controlled chaos harder to maintain)
- **Yen selloff accelerates** (USD/JPY toward 165-170)
- **JGB yields spike** (30Y toward 4.0%, 40Y toward 4.5%)
- **Feb 19 auction stress** re-emerges (insurers panic)
- **MOF flows turn negative** within 4-8 weeks (repatriation begins)

---

## MONITORING PRIORITIES (Next 60 Days)

**PRIORITY 1 — Shunto 2026 Watch (Feb 15 - March 31)**
- **Mid-Feb:** Early hints from major employers (Toyota wage offer, etc.)
- **Late March:** Rengo announces aggregate results
- **Action:** Update VX-SAM-8.03 (nominal wage forecast), recalculate real wage status

**PRIORITY 2 — Feb 19 20Y JGB Auction**
- **Watch:** BTC <2.3x = immediate crisis risk
- **If fails:** MOF flows likely turn negative within 2-4 weeks
- **Action:** Escalate to PROME, prepare for MOF YELLOW alert

**PRIORITY 3 — MOF Weekly Flow (Every Thursday)**
- **Check:** 8:50am JST release
- **Calculate:** 4-week rolling sum
- **Trigger:** First negative sum = YELLOW alert
- **Action:** Update VX-SAM-9.01, notify LIQUID if threshold breach

**PRIORITY 4 — April BOJ Meeting (April 23-24)**
- **After Shunto results:** Recalculate collision probability
- **Watch:** Ueda statement language ("data-dependent" = hold, "gradual normalization" = hike coming)
- **Action:** Update VX-SAM-6.01 (BOJ rate), VX-SAM-6.03 (Takaichi pressure), collision assessment

**PRIORITY 5 — USD/JPY Correlation Breakdown**
- **Track:** 5-day rolling correlation with UST 10Y
- **Alert:** Correlation goes negative = repatriation confirmed
- **Action:** Cross-reference with MOF flow data, escalate if both signals align

---

## DELIVERABLES COMPLETE ✅

1. ✅ **Updated VX.tsv** — Added 6 new vectors (8.01-8.04 real wage, 9.01-9.02 MOF flow)
2. ✅ **Updated STATUS.md** — Two comprehensive dashboard sections (3,500+ words)
3. ✅ **Current readings provided:**
   - Real wages: 0.0% (ORANGE)
   - MOF flows: +¥366B/mo (GREEN, no repatriation)
4. ✅ **April BOJ collision probability assessed:** 50-55% (base), 70%+ if weak Shunto

**Files modified:**
- `domain/workbook/VX.tsv`
- `domain/STATUS.md`
- `domain/workbook/FRAMEWORK_IMPLEMENTATION_FEB11.md` (this document)

**Cross-references:**
- Real wage vectors: VX-SAM-8.01 through VX-SAM-8.04
- MOF flow vectors: VX-SAM-9.01, VX-SAM-9.02
- Existing vectors: VX-SAM-6.03 (Takaichi pressure), VX-SAM-1.03 (JGB 30Y), VX-SAM-3.03 (20Y auction)
- Deep dive: `workbook/LIFE_INSURER_UST_DEEP_DIVE.md`

---

**END OF IMPLEMENTATION REPORT**
