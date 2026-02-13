# LABOR DOMAIN SKELETON v1.0

# Purpose: Structural scaffold for LABOR agent operations
# Domain:  US Labor Markets, Employment Dynamics, Workforce Stress, DOGE Impacts
# Agent:   LABOR (Labor Market Stress Monitor)
#
# Version: 1.0
# Created: 2026-02-01
# Author:  Prome (System Synthesis)
#
# Usage:
#   - Load this file at the start of any LABOR session
#   - Provides vocabulary, entities, vectors, and thresholds for employment monitoring
#   - Employment is the MASTER VARIABLE — transmission mechanism for all other stress

---

## 0. QUICK START

### About This Agent

LABOR monitors the full US employment picture as the primary transmission mechanism for systemic stress. When employment breaks, latent stress across all domains converts to active crisis.

**Key Insight:** Employment breaks in a SEQUENCE. Leading indicators move first. LABOR's value is seeing the break BEFORE NFP confirms it.

### Current Status

| Metric | Value | Status | Threshold |
|--------|-------|--------|-----------|
| Initial Claims | ~220K | GREEN | >280K = ORANGE |
| Continuing Claims | ~1.9M | GREEN | >2.3M = ORANGE |
| NFP (last) | +200K+ | GREEN | <50K = ORANGE |
| Unemployment | 4.1% | GREEN | >4.8% = ORANGE |
| JOLTS Openings | 7.5M | YELLOW | <6.5M = ORANGE |
| Quits Rate | 2.0% | YELLOW | <1.6% = ORANGE |
| Part-Time Econ | ~4.5M | YELLOW | >5.5M = ORANGE |

**Overall Assessment:** GREEN with YELLOW leading indicators. No active transmission. Monitoring mode.

### Session Type Routing

| Session Type | Load Sections | Purpose |
|--------------|---------------|---------|
| Weekly Update | 0, 4 | Thursday claims processing |
| Monthly Update | 0, 4, 5 | NFP and full employment review |
| Analysis | 0, 3, 4, 5 | Deep dive on specific sector/signal |
| Crisis | All | Employment break — full cascade assessment |
| Handoff | Full skeleton | Explicit knowledge transfer |

---

## 1. ENTITY TYPES

### Data Sources

| Source | Frequency | Release | Key Metrics |
|--------|-----------|---------|-------------|
| BLS Employment Situation | Monthly | 1st Friday 8:30am | NFP, unemployment, hours, wages |
| BLS JOLTS | Monthly | ~40 days lag | Openings, quits, layoffs, hires |
| DOL Initial Claims | Weekly | Thursday 8:30am | Initial claims, continuing claims |
| ADP Employment | Monthly | 2 days before NFP | Private payrolls (preview) |
| Challenger Job Cuts | Monthly | 1st Thursday | Announced layoffs by sector |
| Indeed Job Postings | Weekly | Wednesday | Postings index, sector breakdown |
| NFIB Survey | Monthly | 2nd Tuesday | Small business hiring plans |
| Conference Board | Monthly | Various | Help wanted, employment trends |
| Fed Regional Surveys | Monthly | Various | Employment sub-indices |

### Sector Categories

| Sector | Sensitivity | Lead/Lag | Key Signals |
|--------|-------------|----------|-------------|
| Temp/Staffing | LEADING | 3-6 months ahead | First cut, first hired |
| Tech | EARLY CYCLE | 1-3 months ahead | High visibility, sentiment driver |
| Retail/Hospitality | EARLY CYCLE | 1-2 months ahead | Consumer-facing |
| Construction | RATE-SENSITIVE | Coincident | Housing/infrastructure |
| Manufacturing | TRADE-SENSITIVE | Coincident | Goods economy |
| Healthcare | DEFENSIVE | Lagging | Last to cut |
| Government/Federal | POLICY-DRIVEN | Variable | DOGE = direct shock |
| Financial Services | CYCLE-SENSITIVE | Coincident | Bank stress transmission |

### Hidden Employment Categories

| Category | Definition | Why It Matters |
|----------|------------|----------------|
| Part-Time for Economic Reasons | Want full-time but can't find | Hidden unemployment |
| Discouraged Workers | Stopped looking (not in labor force) | Not counted in headline |
| Marginally Attached | Want work but not actively searching | Not in labor force |
| Multiple Jobholders | 2+ jobs to make ends meet | Stress indicator |
| Gig-Dependent | Primary income from gig work | Not traditional employment |
| Underemployed | Overqualified for current job | Wage stress, turnover risk |

### ⚠️ METHODOLOGICAL CAVEAT: The Gig Economy Claims Blind Spot

**Claims data structurally undercount true employment stress.** Traditional UI requires:
- W-2 employment (not 1099 contractors)
- Sufficient wage history with one employer
- Involuntary separation

**Who falls through the cracks:**
- Uber/Lyft drivers who get deactivated
- DoorDash/Instacart couriers whose orders dry up
- Freelancers who lose clients
- Platform workers of all types

**Scale of blind spot:**
- ~36% of US workers participate in gig economy (some capacity)
- ~15% rely on it as primary income (~5M+ workers)
- COVID's PUA temporarily covered them — that program is gone

**Implication:** Claims could stay "healthy" at 220K while millions of gig workers experience real income stress. They're invisible to the legacy measurement system.

**This connects to CARL's thesis:** The 25-40% "hidden stressed" population overlaps heavily with gig-dependent workers. When traditional employment weakens, workers flee TO gig work, but gig earnings are ALSO compressing due to saturation. This creates a doom loop where both escape routes are blocked.

**Cross-Reference:** GIG sub-agent (under CARL) tracks this population in detail. LABOR should treat GIG signals as LEADING indicators that won't appear in claims data.

---

## 2. TRANSMISSION PATHS (FLOW)

### FLOW-LAB-1.01 — Employment → Consumer Stress

```
Speed: 1-3 MONTHS
Status: LATENT — Awaiting employment break

Pathway:
  Layoffs/Hours Cut
    → Income loss
    → Savings drawdown (already low — CARL)
    → Missed payments (credit card, auto, mortgage)
    → Delinquency acceleration
    → Default spike
    → Bank NCO increase

Trigger: NFP <50K OR Claims >280K sustained
Current Position: LATENT — Claims ~220K
Cross-Agent: Signals to CARL when triggered
```

### FLOW-LAB-1.02 — Employment → Bank Stress

```
Speed: 3-6 MONTHS
Status: LATENT — Awaiting employment break

Pathway:
  Layoffs
    → Depositors withdraw savings (need cash)
    → Deposit flight accelerates (especially uninsured)
    → Consumer NCOs rise
    → Bank earnings decline
    → Stock price falls
    → Confidence loss → More deposit flight
    → [REGINALD ORANGE banks → RED]

Trigger: Unemployment >4.8% OR Claims >300K
Current Position: LATENT
Cross-Agent: Signals to REGINALD when triggered
Note: Per REGINALD — "If ANY employment metric reaches RED → all ORANGE banks escalate simultaneously"
```

### FLOW-LAB-1.03 — Employment → Market Stress

```
Speed: 1-6 MONTHS (flows fast, earnings slower)
Status: LATENT — Awaiting employment break

Pathway:
  Layoffs
    → 401(k) contributions stop (payroll-deducted)
    → 401(k) hardship withdrawals increase (already at ATH)
    → Passive inflows decline → outflows possible
    → Structural bid weakens
    → Consumer spending collapses
    → Corporate earnings revisions down
    → Multiple compression
    → Market repricing

Trigger: Unemployment >5.0% (HENRY Structural Bid break scenario)
Current Position: LATENT
Cross-Agent: Signals to HENRY when triggered
```

### FLOW-LAB-2.01 — Small Business → Employment

```
Speed: 3-6 MONTHS
Status: MONITORING — POP showing stress

Pathway:
  Small business revenue decline (POP monitors)
    → Owner absorbs losses first (personal guarantee)
    → Hiring freeze
    → Hours reduction
    → Layoffs / business closure
    → Employment impact

Trigger: Fed SBCS revenue drops > increases sustained
Current Position: MONITORING — SBCS showing stress, employment not yet
Cross-Agent: Receives signals from POP/CARL
Key Insight: This is the 3-6 month LEADING pathway
```

### FLOW-LAB-2.02 — Federal Employment Shock (DOGE)

```
Speed: IMMEDIATE (direct cut) + MONTHS (multiplier)
Status: ACTIVE — DOGE cutting agencies

Pathway:
  DOGE targets agency
    → Direct federal job cuts
    → Contractor job losses (often larger than direct)
    → Local economy impact (DC metro, agency regions)
    → Multiplier effects (services to federal workers)
    → Housing market impact in federal regions

Trigger: Executive orders, agency "reorganization"
Current Position: ACTIVE — USAID, CFPB, others targeted
Cross-Agent: Receives signals from BARON
Key Insight: UNTRACKED in current system. 2.2M federal employees + millions of contractors.
```

### FLOW-LAB-3.01 — Leading Indicator Cascade

```
Speed: SEQUENCE (months)
Status: REFERENCE — This is the detection framework

Sequence:
  1. Job postings decline (6+ months ahead)
  2. Temp employment declines (3-6 months ahead)
  3. Hours worked decline (1-3 months ahead)
  4. Initial claims rise (weeks ahead)
  5. NFP misses / goes negative (coincident)
  6. Unemployment rate rises (1-3 months lag)
  7. Continuing claims plateau (3-6 months lag)
  8. Long-term unemployment rises (6+ months lag)

Current Position: Stage 1-2 possibly starting (watching)
Key Insight: Track the SEQUENCE, not just the headline
```

---

## 3. THRESHOLDS (Consolidated Tripwires)

**Color Coding:** GREEN = Normal | YELLOW = Watch | ORANGE = Alert | RED = Critical

### VX-LAB-1.XX — Weekly Indicators (Fastest)

| Vector | Metric | Current | GREEN | YELLOW | ORANGE | RED |
|--------|--------|---------|-------|--------|--------|-----|
| VX-LAB-1.01 | Initial Claims | ~220K | <230K | 230-250K | 250-300K | >300K |
| VX-LAB-1.02 | Continuing Claims | ~1.9M | <2.0M | 2.0-2.1M | 2.1-2.5M | >2.5M |
| VX-LAB-1.03 | Claims 4-Week Avg | ~220K | <230K | 230-250K | 250-300K | >300K |
| VX-LAB-1.04 | Indeed Postings YoY | TBD | >0% | -5% to 0% | -10% to -5% | <-10% |

### VX-LAB-2.XX — Monthly Indicators (Headline)

| Vector | Metric | Current | GREEN | YELLOW | ORANGE | RED |
|--------|--------|---------|-------|--------|--------|-----|
| VX-LAB-2.01 | NFP (MoM) | +200K+ | >150K | 50-150K | 0-50K | <0 |
| VX-LAB-2.02 | Unemployment Rate | 4.1% | <4.3% | 4.3-4.5% | 4.5-5.0% | >5.0% |
| VX-LAB-2.03 | Labor Force Participation | 62.5% | >62.5% | 62.0-62.5% | 61.5-62.0% | <61.5% |
| VX-LAB-2.04 | U-6 Underemployment | ~7.5% | <7.5% | 7.5-8.0% | 8.0-9.0% | >9.0% |
| VX-LAB-2.05 | Avg Weekly Hours | 34.3 | >34.3 | 34.0-34.3 | 33.5-34.0 | <33.5 |
| VX-LAB-2.06 | Avg Hourly Earnings YoY | 4.0% | 3-4% | 2-3% | <2% | <0% (deflation) |

### VX-LAB-3.XX — JOLTS / Turnover

| Vector | Metric | Current | GREEN | YELLOW | ORANGE | RED |
|--------|--------|---------|-------|--------|--------|-----|
| VX-LAB-3.01 | Job Openings | 7.5M | >8.0M | 7.0-8.0M | 6.0-7.0M | <6.0M |
| VX-LAB-3.02 | Quits Rate | 2.0% | >2.2% | 2.0-2.2% | 1.6-2.0% | <1.6% |
| VX-LAB-3.03 | Layoffs Rate | 1.0% | <1.0% | 1.0-1.2% | 1.2-1.5% | >1.5% |
| VX-LAB-3.04 | Openings/Unemployed Ratio | 1.1 | >1.2 | 1.0-1.2 | 0.7-1.0 | <0.7 |

### VX-LAB-4.XX — Leading Indicators

| Vector | Metric | Current | GREEN | YELLOW | ORANGE | RED |
|--------|--------|---------|-------|--------|--------|-----|
| VX-LAB-4.01 | Temp Employment MoM | flat | >0% | -0.5% to 0% | -1% to -0.5% | <-1% |
| VX-LAB-4.02 | Challenger Cuts YoY | +30%? | <+20% | +20-50% | +50-100% | >+100% |
| VX-LAB-4.03 | NFIB Hiring Plans | net +10 | >+10 | 0 to +10 | -10 to 0 | <-10 |
| VX-LAB-4.04 | ISM Employment Index | 50+ | >52 | 48-52 | 45-48 | <45 |

### VX-LAB-5.XX — Hidden Unemployment

| Vector | Metric | Current | GREEN | YELLOW | ORANGE | RED |
|--------|--------|---------|-------|--------|--------|-----|
| VX-LAB-5.01 | Part-Time Econ Reasons | ~4.5M | <4.5M | 4.5-5.0M | 5.0-6.0M | >6.0M |
| VX-LAB-5.02 | Multiple Jobholders | ~8.5M | <8.5M | 8.5-9.0M | 9.0-10.0M | >10.0M |
| VX-LAB-5.03 | Discouraged Workers | ~0.4M | <0.5M | 0.5-0.7M | 0.7-1.0M | >1.0M |
| VX-LAB-5.04 | Long-Term Unemployed (27w+) | ~1.3M | <1.5M | 1.5-2.0M | 2.0-2.5M | >2.5M |

### VX-LAB-6.XX — Sectoral Stress

| Vector | Metric | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| VX-LAB-6.01 | Tech Layoffs (Challenger) | Elevated | YELLOW | High visibility, leads sentiment |
| VX-LAB-6.02 | Federal Employment | 2.2M | GAP | DOGE impact untracked |
| VX-LAB-6.03 | Retail Employment MoM | TBD | TBD | Consumer-facing |
| VX-LAB-6.04 | Construction Employment | TBD | TBD | Rate-sensitive |
| VX-LAB-6.05 | Manufacturing Employment | TBD | TBD | Trade-sensitive |
| VX-LAB-6.06 | Healthcare Employment | TBD | TBD | Defensive sector |

### VX-LAB-7.XX — Federal Employment (DOGE Impact) — NEW

| Vector | Metric | Baseline | Current | Change | Status |
|--------|--------|----------|---------|--------|--------|
| VX-LAB-7.01 | Total Federal Civilian | 2.2M | TBD | TBD | GAP |
| VX-LAB-7.02 | USAID Headcount | ~10K | Eliminated? | -100%? | CRITICAL |
| VX-LAB-7.03 | CFPB Headcount | ~1,700 | Gutted | -80%? | CRITICAL |
| VX-LAB-7.04 | DOE Headcount | ~14K | Targeted | TBD | WATCH |
| VX-LAB-7.05 | EPA Headcount | ~15K | Targeted | TBD | WATCH |
| VX-LAB-7.06 | IRS Headcount | ~90K | Targeted | TBD | WATCH |
| VX-LAB-7.07 | Federal Contractor Est. | ~5M+ | Unknown | Unknown | GAP |
| VX-LAB-7.08 | DC Metro Employment Impact | TBD | TBD | TBD | GAP |

---

## 4. VECTOR REGISTRY (Detailed)

### VX-LAB-1.01 — Initial Claims

```yaml
id: VX-LAB-1.01
name: Initial Unemployment Claims
description: Weekly first-time unemployment insurance filings
source: DOL (weekly, Thursday 8:30am ET)
frequency: Weekly
current_value: ~220K
current_status: GREEN

thresholds:
  green: <230K
  yellow: 230-250K
  orange: 250-300K
  red: >300K

history:
  pre_covid_normal: 200-220K
  covid_peak: 6.9M (Apr 2020)
  2023_average: ~220K
  
interpretation: |
  Fastest weekly signal. Initial claims are filed immediately upon job loss.
  Rising claims = layoffs accelerating. 
  4-week moving average smooths noise.
  >300K historically associated with recession.

cross_agent:
  - "If >280K sustained → signal CARL, REGINALD"
  - "If >300K → signal ALL agents — employment RED"
```

### VX-LAB-2.01 — Nonfarm Payrolls

```yaml
id: VX-LAB-2.01
name: Nonfarm Payrolls (NFP)
description: Monthly change in total nonfarm employment
source: BLS Employment Situation (1st Friday 8:30am ET)
frequency: Monthly
current_value: +200K+
current_status: GREEN

thresholds:
  green: >150K
  yellow: 50-150K
  orange: 0-50K
  red: <0 (negative)

history:
  2024_average: +180K/month
  covid_trough: -20.5M (Apr 2020)
  recession_signal: 3 consecutive negative prints
  
interpretation: |
  Headline employment number. High visibility, market-moving.
  Subject to revisions (watch for benchmark revisions annually).
  Negative print = recession signal historically.
  
cross_agent:
  - "If <100K → signal CARL, HENRY"
  - "If <0 → signal ALL agents — recession confirmed"
```

### VX-LAB-3.02 — Quits Rate

```yaml
id: VX-LAB-3.02
name: JOLTS Quits Rate
description: Percentage of employed workers voluntarily leaving jobs
source: BLS JOLTS (monthly, ~40 day lag)
frequency: Monthly
current_value: 2.0%
current_status: YELLOW

thresholds:
  green: >2.2%
  yellow: 2.0-2.2%
  orange: 1.6-2.0%
  red: <1.6%

history:
  great_resignation_peak: 3.0% (Nov 2021)
  pre_covid_normal: 2.3%
  recession_trough: 1.3% (2009)
  
interpretation: |
  Worker confidence indicator. High quits = workers confident in finding new jobs.
  Falling quits = workers scared to leave, labor market weakening.
  Leading indicator — workers sense trouble before layoffs hit.
  
cross_agent:
  - "Quits <2.0% = labor market cooling significantly"
  - "Quits <1.6% = recession-level worker fear"
```

### VX-LAB-4.01 — Temp Employment

```yaml
id: VX-LAB-4.01
name: Temporary Help Services Employment
description: BLS series for temp/staffing industry employment
source: BLS Employment Situation (monthly)
frequency: Monthly
current_value: declining
current_status: YELLOW

thresholds:
  green: >0% MoM
  yellow: -0.5% to 0% MoM
  orange: -1% to -0.5% MoM
  red: <-1% MoM (sustained)

history:
  note: "Temp employment leads headline employment by 3-6 months"
  pre_recession_pattern: "Temp declines before headline NFP"
  
interpretation: |
  LEADING INDICATOR. Companies cut temps before permanent staff.
  Sustained temp employment decline = layoffs coming in 3-6 months.
  Track MoM change, not level.
  
cross_agent:
  - "Temp -1% MoM sustained → signal ALL — leading indicator flashing"
```

---

## 5. DATA CALENDAR

### Weekly (Every Thursday)
- **8:30am ET:** Initial Claims, Continuing Claims

### Monthly
| Release | Timing | Key Metrics |
|---------|--------|-------------|
| NFP/Employment Situation | 1st Friday 8:30am | Payrolls, unemployment, hours, wages |
| ADP Employment | 2 days before NFP | Private payrolls preview |
| Challenger Job Cuts | 1st Thursday | Announced layoffs |
| JOLTS | ~40 days after reference month | Openings, quits, layoffs |
| NFIB Survey | 2nd Tuesday | Small business hiring plans |

### Quarterly
- BLS Benchmark Revisions (annual, but watch for interim)
- Fed Senior Loan Officer Survey (SLOOS) — credit conditions affecting hiring

---

## 6. GLOSSARY

| Term | Definition |
|------|------------|
| Initial Claims | First-time unemployment insurance filings |
| Continuing Claims | Ongoing unemployment insurance recipients |
| NFP | Nonfarm Payrolls — headline monthly employment change |
| JOLTS | Job Openings and Labor Turnover Survey |
| Quits Rate | % of employed voluntarily leaving jobs |
| U-3 | Official unemployment rate (unemployed / labor force) |
| U-6 | Broad unemployment (includes part-time econ + marginally attached) |
| LFPR | Labor Force Participation Rate |
| Temp Employment | Temporary help services — leading indicator |
| Challenger Cuts | Announced layoffs tracked by Challenger, Gray & Christmas |
| DOGE | Department of Government Efficiency — Musk-led agency cutting federal workforce |
| Part-Time Econ | Working part-time because can't find full-time |
| Discouraged Workers | Want work but stopped looking (not in labor force) |

---

## 7. CROSS-AGENT CONNECTIONS

### LABOR → CARL
- Employment is transmission mechanism for consumer stress
- Claims >280K → accelerate consumer default timeline
- Signal: VX-LAB-1.01 thresholds

### LABOR → REGINALD
- Employment RED → ALL ORANGE banks escalate simultaneously
- This is REGINALD's documented catalyst
- Signal: VX-LAB-2.02 (unemployment) crossing 4.8%

### LABOR → HENRY
- Employment break → 401(k) outflows → structural bid reverses
- Unemployment >5.0% is HENRY's scenario trigger
- Signal: VX-LAB-2.02 crossing 5.0%

### LABOR → LIQUID
- Recession → Fed policy pivot → rate trajectory changes
- Employment break → flight to quality → funding dynamics shift
- Signal: NFP negative 3 consecutive months

### LABOR → SAM
- US recession → global demand shock → Japan export collapse
- US unemployment spike → Fed easing → dollar weakness → yen strength
- Signal: Recession confirmation

### LABOR ← BARON
- DOGE federal employment cuts
- Policy changes affecting labor (overtime rules, contractor classification)
- Receive: BARON signals on federal workforce actions

### LABOR ← POP (via CARL)
- Small business revenue stress → 3-6 month employment lag
- This is the LEADING pathway
- Receive: Small business stress escalation

### LABOR ← GIG (via CARL)
- Gig saturation = buffer exhausted
- Gig workers are hidden unemployment
- Receive: GIG saturation critical

---

## 8. RESEARCH PRIORITIES

### Immediate
1. **Federal employment baseline** — How many federal employees by agency? Contractor estimates?
2. **DOGE impact quantification** — What's actually been cut so far?
3. **Indeed postings trend** — Current YoY change?
4. **Temp employment trend** — Last 3 months MoM?

### Near-Term
1. **Regional concentration** — Which metros most exposed to federal cuts?
2. **Tech layoff tracker** — Aggregate Q4 2025 / Q1 2026 tech cuts
3. **Small business → employment lag** — Validate 3-6 month transmission

### Medium-Term
1. **Leading indicator model** — Weight indicators for composite score
2. **Sector rotation analysis** — Which sectors lead in this cycle?
3. **Hidden unemployment deep dive** — Part-time econ + gig-dependent sizing

---

*LABOR Skeleton v1.0 — The Master Variable Monitor*
*Created: 2026-02-01 by Prome*
