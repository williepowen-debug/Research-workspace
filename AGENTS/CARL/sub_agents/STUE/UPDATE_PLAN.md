# STUE → CARL Update Plan
**Generated:** 2026-04-13
**Based on:** STUE refresh Apr 13 (STATUS.md updated with fresh web data)
**Next available KB ID:** KB-CARL-180
**Next available VX ID:** No new SL vectors needed — check notes below

---

## UPDATES TO EXISTING ENTRIES

### VX.tsv — Student Loan Vectors

| File | Entry ID | Field | Old Value | New Value | Source |
|------|----------|-------|-----------|-----------|--------|
| VX.tsv | VX-CARL-SL-05 | Current_Value | 7.7M | **9.2M** | ED/FSA (via press, early Mar 2026) |
| VX.tsv | VX-CARL-SL-05 | Last_Updated | 2026-04-04 | 2026-04-13 | — |
| VX.tsv | VX-CARL-SL-05 | Notes | "$180B. +2.5M since Sep 2025. <40% in repayment. 18.6% active DQ by $. NEW VECTOR." | "$180B. +1.5M in ~90 days (Dec→Mar). Treasury Transfer Phase 1 (Mar 19) based on this count. 2.4M additional in late-stage DQ (not yet defaulted). <40% in repayment. 18.6% active DQ by $." | ED/FSA Mar 2026 |
| VX.tsv | VX-CARL-SL-04 | Current_Value | 9M+ | **11.6M+** | FICO Spring 2026 Credit Insights + FSA |
| VX.tsv | VX-CARL-SL-04 | Notes | "13M projected default EOY 2026. MOHELA caused 800K manufactured DQ via missed bills. Credit report duplication errors. Upgraded ORANGE→RED." | "9.2M in default + 2.4M late-stage DQ = 11.6M in active distress. FICO avg score dropped to 714 (from 716). 7M+ new DQ reports in 2025. Near-prime (680+) cohort: -100 pts for 2M borrowers. Gen Z 14.4% saw -50pt+ drops. 13M projected EOY 2026. MOHELA caused 800K DQ via missed bills + credit errors." | FICO Spring 2026 / FSA / TCF |
| VX.tsv | VX-CARL-SL-04 | Last_Updated | 2026-04-04 | 2026-04-13 | — |
| VX.tsv | VX-CARL-SL-07 | Notes | "800K became DQ from missed bills alone. Wait times 7x-50x peers. ~2M credit report errors. $7.2M penalty. NEW VECTOR." | "800K became DQ from missed bills alone. Wait times 7x-50x peers. ~2M credit report errors. $7.2M penalty. MOHELA abandon rate 14%+ (no other servicer exceeds 5%). AFT case in DISCOVERY phase — next status conf May 28. Maldonado ruling (Mar 2026): violated CA Student Borrower Bill of Rights + Unfair Competition Law." | AFT/court docket/Maldonado ruling Mar 2026 |
| VX.tsv | VX-CARL-SL-07 | Last_Updated | 2026-04-04 | 2026-04-13 | — |
| VX.tsv | VX-CARL-SL-03 | Notes | "REPEALED by Working Families Tax Cuts Act (Jul 2025). ... Non-selectors → Standard or Tiered Standard (payment shock $0→$407/mo). RAP available." | "REPEALED by Working Families Tax Cuts Act (Jul 2025). Legislative, not administrative — no legal path to reinstate. ED final guidance Mar 31, 2026. Jul 1: servicer notices begin in waves (every 2 weeks). Non-selectors auto-transition to Standard OR Tiered Standard (NOT direct default — RAP clarification Mar 31). Payment shock $0→$407/mo avg. RAP: 1-10% AGI, $50/mo per-dependent deduction, 30-yr forgiveness." | ED Mar 31 guidance |
| VX.tsv | VX-CARL-SL-03 | Last_Updated | 2026-04-06 | 2026-04-13 | — |
| VX.tsv | VX-CARL-SL-06 | Current_Value | PHASE 1 ACTIVE | **PHASE 1 ACTIVE — 9.2M / $180B transferred Mar 19** | ED/FSA Mar 19 2026 |
| VX.tsv | VX-CARL-SL-06 | Notes | "~9M defaulted borrowers transferred to Treasury. Legal authority disputed. Operational capacity unproven. NEW VECTOR." | "9.2M / $180B (11% of $1.7T portfolio) transferred to Treasury (Mar 19). Phase 1: collections to private default resolution agencies via Treasury. Phase 2 (non-defaulted) planned. Phase 3 (FAFSA) planned. Legal authority disputed — 5 Senate committee ranking members demanding rescission. Operational contradiction: Phase 1 active but ED paused collections Jan 16 that Treasury would execute; restart expected July 2026." | ED/FSA Mar 19 / Senate |
| VX.tsv | VX-CARL-SL-06 | Last_Updated | 2026-04-04 | 2026-04-13 | — |

### KB.tsv — Student Loan Entries

| File | Entry ID | Field | Old Value | New Value | Source |
|------|----------|-------|-----------|-----------|--------|
| KB.tsv | KB-CARL-145 | Fact | "7.7M borrowers in default on $180B (11% of $1.61T portfolio). Up ~2.5M since Sep 2025. Active repayment 31+ DQ rate: 18.6% by dollar..." | Append note: "UPDATED Apr 13: Default count rose to 9.2M (early Mar 2026, +1.5M in ~90 days from Dec 2025). See KB-CARL-180 for Mar 2026 data." | ED/FSA Mar 2026 |
| KB.tsv | KB-CARL-145 | Status | ACTIVE | SUPERSEDED (by KB-CARL-180) | — |
| KB.tsv | KB-CARL-147 | Notes | "CRITICAL CATALYST: Jul 1 forces 7.5M into action. Non-selectors face payment shock. RAP may cushion IF enrollment is high..." | Append: "Mar 31 ED guidance clarified: non-selectors auto-transition to Standard OR Tiered Standard (NOT direct default). Reduces immediate cliff but does not eliminate payment shock. RAP per-dependent deduction is $50/mo." | ED Mar 31 2026 |
| KB.tsv | KB-CARL-150 | Notes | "Servicer failure is AMPLIFYING delinquency. 800K borrowers DQ because bills weren't sent..." | Append: "Apr 13 update: AFT case in DISCOVERY phase (next conf May 28, 2026). No settlement. MOHELA abandon rate >14% vs 5% max for any other servicer. Maldonado ruling (Mar 2026) confirmed MOHELA violated CA Student Borrower Bill of Rights and Unfair Competition Law — creates legal precedent for other states. See KB-CARL-174 (Maldonado), KB-CARL-175 (collections pause)." | AFT/court docket/Maldonado |

### STATUS.md — Dashboard Values

| Row | Old Value | New Value | Source |
|-----|-----------|-----------|--------|
| Student Loan Defaults | **7.7M / $180B** (+2.5M since Sep 2025) [Dec 2025, FSA] | **9.2M / $180B** (+1.5M Dec→Mar) [Mar 2026, FSA/ED press] | ED/FSA Mar 2026 |
| Convergence Matrix Row 4 label | "7.7M default, ~25% DQ, SAVE ending Jul 1, MOHELA 800K manufactured DQ." | "**9.2M default** (+1.5M in 90 days), 2.4M late-stage DQ, ~25% DQ rate, SAVE ending Jul 1, MOHELA 800K manufactured DQ. FICO avg: 714. Credit cascade EXECUTING." | — |

---

## NEW ENTRIES NEEDED

### KB.tsv

| File | Proposed ID | Content Summary | Source |
|------|-------------|-----------------|--------|
| KB.tsv | **KB-CARL-180** | FSA Mar 2026 default count: 9.2M borrowers in default (up from 7.7M Dec 2025, +1.5M in ~90 days). Additional 2.4M in late-stage DQ (not yet defaulted). Total at-risk: 11.6M. This was the basis for Treasury Transfer Phase 1 on Mar 19. Default trajectory: 13M EOY 2026 projection. [ED official/Inside Higher Ed/CNBC, Mar 2026] | ED/FSA (via press), Mar 2026 |
| KB.tsv | **KB-CARL-181** | FICO Spring 2026 Credit Insights: National avg FICO dropped to 714 (from 716 in 2024). 7M+ borrowers reported new DQ in 2025 — student loan DQ is primary driver. Avg score drop for DQ borrowers: -62 pts. Near-prime cohort (680+): -100 pts for 2M borrowers (680→580). Gen Z (18-29): 14.4% of cohort saw -50pt+ drop, triple prior rate. Lifetime cost consequence: +$64K mortgage, +$8,800 auto (680→580 repricing). National FICO declining = systemic signal beyond individual borrowers. [FICO Spring 2026 Credit Insights, released Mar/Apr 2026] | FICO Spring 2026 Credit Insights |
| KB.tsv | **KB-CARL-182** | Credit cascade confirmed executing (Apr 13): Student loan DQ is amplifying CC, auto, and mortgage DQ through credit score destruction. Mechanism: 9.2M defaults + 2.4M late-stage DQ → FICO avg 714 (primary driver per FICO) → -62 pts avg for DQ borrowers → near-prime band (680→580) → mortgage denial/repricing + auto repricing → est. +0.5-1.0pp to CC 90+ DQ rate (CARL's CRL-05 pathway). This is not a future risk — cascade is NOW EXECUTING. [FICO Spring 2026 + TCF, Apr 13 synthesis] | STUE synthesis from FICO/TCF data |
| KB.tsv | **KB-CARL-183** | Sweet v. McMahon non-Exhibit C deadline: Apr 15, 2026 (2 days). DOE must issue decisions for non-Exhibit C post-class applicants OR automatic full relief triggers (discharge + refunds + credit corrections). As of Apr 13, no public record that DOE issued non-Exhibit C notices. New judge assigned (Judge Alsup retired). Pattern from Jan 28: DOE missed Exhibit C deadline → auto full relief ordered. Ninth Circuit merits appeal ongoing but NO stay in effect — deadlines remain binding. High probability of same pattern repeating Apr 15. [PPSL/tateesq.com/Cullen Dykman, Apr 2026] | PPSL/tateesq.com/Cullen Dykman Apr 2026 |

### VX.tsv

No new SL vector IDs needed — the Apr 13 data populates into existing SL-01 through SL-07. However, one new vector is recommended:

| File | Proposed ID | Content Summary | Source |
|------|-------------|-----------------|--------|
| VX.tsv | **VX-CARL-SL-08** | National Avg FICO Score — new vector to track the credit score destruction pathway at the population level. Current_Value: 714. Prior: 716 (2024). Status: RED (below 715 = systemic distress signal). Green: >735. Yellow: <730. Orange: <720. Red: <715. Last_Updated: 2026-04-13. Source: FICO Spring 2026 Credit Insights. Notes: Student loan DQ is primary driver per FICO. -62 pts avg for 7M+ DQ borrowers; near-prime (680→580) cohort = 2M borrowers with lifetime mortgage cost +$64K. Gen Z 14.4% saw -50pt+ drops. This is the transmission bridge between student loan stress (STUE) and CC/auto/mortgage stress (CARL). | FICO Spring 2026 Credit Insights |

---

## PREDICTION CHANGES

| ID | Field | Old | New | Reason |
|----|-------|-----|-----|--------|
| CRL-04 | Notes | "FSA confirms 7.7M default/$180B, ~25% of borrowers w/payment due behind. 18-29 cohort already at 21%. SAVE ending Jul 1 forces 7.5M into repayment. MOHELA failures manufacturing DQ. Near-certain on next NY Fed release..." | Update to: "UPDATED Apr 13: Default count now 9.2M (Mar 2026, +1.5M in 90 days). 2.4M in late-stage DQ. FICO avg: 714. 7M+ new DQ reported 2025. Near-certain. Only risk: methodology change or forgiveness intervention. Next read: NY Fed Q1 2026 QHDC (~May-Jun)." | Default count update from STUE refresh |
| CRL-04 | Confidence | 95% | **97%** | 9.2M default + FICO confirmation eliminates most remaining uncertainty. Only scenario for miss: DOE mass forgiveness or methodology change. |
| CRL-05 | Notes | "Apr 6 upgrade: STUE cascade analysis identifies student loan credit score destruction (-87 to -171 pts) as additional pathway to GFC breach. 10-12M borrowers face score damage → 3-5M cascade into CC DQ → est. +0.5-1.0pp to CC 90+ rate." | Update score range: "-62 pts avg (FICO Spring 2026 confirmed). Near-prime cohort: -100 pts for 2M borrowers. National avg FICO already at 714 (from 716). 9.2M default + 2.4M late-stage DQ = 11.6M in active distress. Cascade NOW EXECUTING per FICO Spring 2026 data. Combined with multi-vector cost squeeze." | FICO Spring 2026 quantifies what was previously estimated |
| CRL-05 | Confidence | 82% | **85%** | FICO Spring 2026 confirms the cascade is already executing (not projected). National FICO declining now. |
| CRL-13 | Notes | "Based on Oct 2023 forbearance-end precedent (20-30% failed to resume) + MOHELA operational failures..." | Append: "RAP clarification (Mar 31 ED guidance): non-selectors auto-transition to Standard OR Tiered Standard (NOT direct default). Per-dependent deduction $50/mo reduces payment shock for some. However, est. non-selection rate 30-45% still holds because affirmative opt-in required and MOHELA capacity near-zero for transition volume." | RAP clarification from Mar 31 ED guidance |
| CRL-14 | Notes | "MOHELA services ~16.5M accounts (largest servicer). Already failed to deliver bills to 2.5M, manufactured 800K DQ." | Append: "Apr 13: AFT case in DISCOVERY (May 28 conf). MOHELA abandon rate >14% vs 5% max peers. Maldonado ruling (Mar 2026) confirmed legal violations. Legal exposure now: Maldonado + AFT + class action + state AGs + CFPB = 5+ concurrent. Operational capacity deteriorating INTO Jul 1 transition." | STUE Apr 13 refresh |

---

## STATUS.md DASHBOARD CHANGES

| Row | Old Value | New Value | Source |
|-----|-----------|-----------|--------|
| Student Loan Defaults | `**7.7M / $180B** (+2.5M since Sep 2025)` with `Dec 2025, FSA` | `**9.2M / $180B** (+1.5M in 90 days, Dec→Mar) + **2.4M late-stage DQ**` with `Mar 2026, ED/FSA (via press)` | ED/FSA Mar 2026 |
| Header summary line | "Student loan cascade + JOLTS 0.91." | "Student loan cascade 9.2M default, FICO 714, credit cascade EXECUTING. JOLTS 0.91." | — |
| Convergence Matrix Row 4 | "**7.7M default, ~25% DQ, SAVE ending Jul 1, MOHELA 800K manufactured DQ.** Max." | "**9.2M default (+1.5M in 90 days), 2.4M late-stage DQ, FICO 714 (primary driver), credit cascade EXECUTING. SAVE ending Jul 1, MOHELA 800K manufactured DQ.** Max." | — |
| Next catalysts footer | "Apr 15: Sweet v. McMahon notices" | "**Apr 15: Sweet v. McMahon non-Exhibit C deadline** (DOE compliance unconfirmed as of Apr 13 — high probability of miss → auto full relief for non-Exhibit C cohort)" | STUE Apr 13 |

---

## FLOW.tsv CHANGES

| File | Entry ID | Field | Old Value | New Value | Source |
|------|----------|-------|-----------|-----------|--------|
| FLOW.tsv | FLOW-CARL-4.01 | Current Position | "Hierarchy: Auto > Mortgage > Student > CC" | "Hierarchy: Auto > Mortgage > Student > CC. **CONFIRMATION Apr 13:** Student loan cascade EXECUTING. 9.2M default + 2.4M late-stage DQ → FICO 714 (student loans = primary driver per FICO) → -62 pts avg DQ borrowers → near-prime 680→580 (-100 pts, 2M borrowers) → CC/auto/mortgage repricing. Est. +0.5-1.0pp to CC 90+ DQ." | FICO Spring 2026 |
| FLOW.tsv | FLOW-CARL-4.01 | Notes | (existing) | Append: "FICO Spring 2026 confirms student loan → FICO destruction → CC/auto cascade is NOW EXECUTING, not projected." | FICO Spring 2026 |

A new FLOW entry should be considered for the credit score destruction cascade pathway (STUE → CC/Auto/Mortgage), but CARL should decide whether to create FLOW-CARL-12.01 or amend 4.01. Not enough to mandate without CARL's call.

---

## NOTES

1. **Most urgent action (Apr 15 — 2 days):** STATUS.md and KB need the Sweet v. McMahon non-Exhibit C deadline flagged as imminent. If DOE misses → auto relief. CARL should flag this in its outbox to PROME as a time-sensitive catalyst to watch.

2. **9.2M default: single most important number to propagate.** This is the number that underpins Treasury Transfer Phase 1 and the 13M EOY projection. It updates the core dashboard metric and VX-CARL-SL-05. KB-CARL-145 should be superseded by KB-CARL-180.

3. **FICO Spring 2026 data is NEW and not yet in CARL's system at all.** The -62 pts avg, 714 national avg, Gen Z 14.4% at -50pt+ drop, and the near-prime 680→580 destruction for 2M borrowers are all unrepresented in CARL's KB/VX. This is the highest-priority NEW data class.

4. **VX-CARL-SL-08 (National FICO) is a recommended new vector** — it bridges the student loan domain and the CC/auto/mortgage DQ domains. CARL should decide if it wants this or prefers to track via KB notes only.

5. **RAP clarification matters for CRL-13.** The Mar 31 ED guidance confirmed non-selectors go to Standard OR Tiered Standard (not direct default). This slightly reduces the immediate default cliff but the non-selection rate estimate (30-45%) is unchanged because the affirmative opt-in requirement and MOHELA capacity failures still dominate.

6. **AFT case discovery (May 28 conf) is a new near-term catalyst** not yet visible in CARL's DANGER WINDOW table. It should be added as a monitoring item.

7. **CARL's CRL-05 CC 90+ DQ prediction** references "-87 to -171 pts" credit score destruction in its notes — this appears to be an earlier STUE estimate. FICO Spring 2026 now gives the confirmed number: **-62 pts avg** (and -100 pts for near-prime cohort). The notes should be updated to use the empirically confirmed FICO figure, not the older estimate.

8. **No new FLOW entry created here** — CARL should decide whether to create a dedicated FLOW entry for the student loan → credit score → CC/auto cascade or amend FLOW-CARL-4.01. Recommending amendment of 4.01 as the simpler path.

9. **Collections restart (July 2026)** is already in KB-CARL-175 but is NOT in CARL's DANGER WINDOW table. It should be added as a July 2026 item (compounds with SAVE transition simultaneously).
