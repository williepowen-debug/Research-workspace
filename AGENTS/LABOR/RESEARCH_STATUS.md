# LABOR Research Status

**Last Updated:** 2026-02-01
**Agent:** LABOR (Labor Market Stress Monitor)
**Session:** Research Session 1

---

## Current Status

**LABOR research in progress.** Key findings:
1. layoffs.fyi has DOGE tracker with federal departure data
2. **CRITICAL INSIGHT:** Claims data has structural blind spot for gig economy workers

### ⚠️ Methodological Note: Claims Undercount Real Stress

Traditional UI claims miss ~15% of workforce (gig-dependent workers):
- 1099 contractors don't qualify for UI
- Platform workers (Uber, DoorDash, etc.) invisible to claims data
- When gig work deteriorates, no signal appears in Thursday numbers
- COVID's PUA covered them temporarily — that's gone

**Implication:** Claims could stay "healthy" at 220K while millions experience real income stress. Must cross-reference GIG sub-agent for complete picture.

---

## Research Priorities

### PRIORITY 1: Federal Employment / DOGE Impact (CRITICAL GAP)

**Why:** Federal employment cuts are direct, immediate, and completely untracked in the current system. DOGE is actively cutting agencies.

**Questions:**
- [ ] How many federal civilian employees by agency? (Baseline)
- [ ] What has DOGE actually cut so far? (USAID, CFPB, others)
- [ ] Estimated federal contractor employment? (Often 2-3x direct)
- [ ] Which metros have highest federal employment concentration?
- [ ] What are the multiplier effects of federal job cuts?

**Sources to Research:**
- OPM (Office of Personnel Management) FedScope data
- GAO reports on federal workforce
- News reporting on DOGE actions
- BARON agent (policy tracking)

**Status:** NOT STARTED

---

### PRIORITY 2: Leading Indicator Baseline

**Why:** Need current values for all leading indicators to assess employment break probability.

**Data Needed:**
- [ ] Indeed job postings index (current, YoY change)
- [ ] Temp employment (last 3 months MoM change)
- [ ] NFIB hiring plans (latest reading)
- [ ] Challenger job cuts (YoY comparison)
- [ ] ISM employment indices (manufacturing + services)

**Sources:**
- Indeed Hiring Lab (public data)
- BLS Employment Situation archives
- NFIB monthly reports
- Challenger, Gray & Christmas releases
- ISM monthly reports

**Status:** NOT STARTED

---

### PRIORITY 3: Small Business → Employment Transmission

**Why:** POP (via CARL) identifies 3-6 month lag from small business revenue stress to employment. Need to validate and refine.

**Questions:**
- [ ] What's the historical correlation between Fed SBCS revenue and subsequent employment?
- [ ] Which sectors show tightest transmission?
- [ ] What's the current state of small business hiring intentions?

**Sources:**
- Fed Small Business Credit Survey (SBCS)
- NFIB Job Openings and Hiring Plans
- Academic research on small business employment dynamics

**Status:** NOT STARTED

---

### PRIORITY 4: Hidden Unemployment Sizing

**Why:** Official unemployment undercounts true labor market stress. Need to size hidden categories.

**Data Needed:**
- [ ] Part-time for economic reasons (current, trend)
- [ ] Multiple jobholders (current, trend)
- [ ] Discouraged workers (current, trend)
- [ ] U-6 vs U-3 spread (current, historical context)

**Sources:**
- BLS Household Survey (monthly)
- BLS Alternative Measures of Labor Underutilization

**Status:** NOT STARTED

---

### PRIORITY 5: Tech Layoff Aggregation

**Why:** Tech layoffs are high visibility and lead sentiment. Need aggregate tracking.

**Questions:**
- [ ] Total tech layoffs Q4 2025?
- [ ] Total tech layoffs Jan 2026?
- [ ] Which companies? What sectors within tech?
- [ ] Comparison to 2022-2023 tech layoff wave?

**Sources:**
- layoffs.fyi (crowdsourced tracker) — **CONFIRMED AVAILABLE** with DOGE tracker
- Challenger monthly reports
- Company announcements

**Status:** IN PROGRESS — layoffs.fyi accessible

---

## Completed Research

*None yet — agent newly created*

---

## Research Prompts (For Future Sessions)

### RP-LAB-001: Federal Employment Deep Dive
```
Research the current state of US federal civilian employment:
1. Total headcount by major agency (2024 baseline)
2. DOGE actions to date — which agencies targeted, estimated cuts
3. Federal contractor employment estimates
4. Geographic concentration of federal workers
5. Historical precedents for large federal workforce reductions
6. Multiplier effects on local economies
```

### RP-LAB-002: Leading Indicator Composite
```
Build a composite leading indicator for US employment:
1. Compile current values for: Indeed postings, temp employment, NFIB hiring plans, ISM employment, Challenger cuts
2. Calculate YoY and MoM changes
3. Assess historical lead times for each indicator
4. Create weighted composite score
5. Assess current composite status (GREEN/YELLOW/ORANGE/RED)
```

### RP-LAB-003: Employment Break Scenario Analysis
```
Model what happens when employment breaks:
1. Define "employment break" thresholds (claims, NFP, unemployment)
2. Map transmission to consumer stress (timeline, magnitude)
3. Map transmission to bank stress (timeline, magnitude)
4. Map transmission to market stress (timeline, magnitude)
5. Identify which current "latent" stresses would convert
```

---

## Session Log

| Date | Session | Focus | Outcome |
|------|---------|-------|---------|
| 2026-02-01 | Init | Agent creation | Skeleton, signals, research priorities established |

---

*LABOR Research Status v1.0*
*Employment is the master variable — track it comprehensively*
