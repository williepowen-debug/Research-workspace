# POLLY STATUS
**Last real data refresh:** 2026-08-10 | **This is POLLY's FINAL STANDING REFRESH — dossier-mode gate fired.** Will-approved refresh-then-demote sequencing (flagged 2026-04-29, executed at Q2 P&C prints). CARL ratifies POLLY's move to dossier-mode after this session closes. Going forward POLLY does not boot on a normal cadence — spawn on-demand only; treat this file and `state_vectors/SV-POLLY-2026-08-10-01.md` as the handoff snapshot. **DOSSIER CARRY LIST → bottom of `state_vectors/SV-POLLY-2026-08-10-01.md`.**

> ⚠️ **VINTAGE MAP.** Q2-2026-vintage this session (2026-08-10): P&C combined ratios (ALL/PGR/TRV), CA FAIR Plan count, FL Citizens count, UNH/ELV MCR/BCR mirror, ML-17/18 repair, all 8 predictions checked (P02/P03/P05 re-scored). **NOT refreshed this session** (Apr-2026 vintage, historical only from here): auto insurance CPI, uninsured motorist rate, homeowners premium growth (national/CA), health deductibles, ACA enrollment, medical debt prevalence — parent **CARL STATUS.md** carries any live figure that supersedes these. Full per-row vintage in each workbook TSV's header banner.

**Phase:** Phase 2-3 (Premium Pressure → Coverage Erosion) nationally; Phase 3-4 in CA specifically. **FL reclassified this session: CA/FL are now DIVERGING more sharply than April's read — CA deceleration is a new finding, FL's decline is confirmed steeper than believed.**

---

## Q2 2026 FINAL REFRESH — THRESHOLD BREACHES AND STATUS CHANGES — 2026-08-10

| Item | Prior (Apr-2026) | New (Q2-2026) | Direction | CARL-Relevant? |
|------|-----|-----|-----------|----------------|
| Allstate auto CR | 81.9% (Q1) | **83.3% (Q2)** | Still deeply profitable, +1.4pp QoQ | POLLY-P05 test |
| Allstate P-L consolidated CR | — | **86.6%** (HO 94.6%) | Strong; HO still relative laggard of the 3 majors | Context |
| Progressive CR | 86.4% (Q1) | **87.3% (Q2)** | +1.1pp YoY, still 8pp under 95% threshold | POLLY-P05 test |
| Travelers consolidated CR | 88.6% (Q1) | **83.6% (Q2)** | IMPROVED further (auto 82.8%, HO 76.7%) | Context |
| UNH consolidated MCR | 83.9% (Q1) | **86.7% (Q2)**; FY guide IMPROVED 88.8%→88.1%±25bps | -270bps YoY; NO BREACH | YES — culling confirms, margin improving |
| ELV consolidated BCR | 86.8% (Q1) | **89.7% (Q2)**, +80bps YoY WORSEN | Medicaid trough -1.75% op margin | YES — diverging from UNH |
| CA FAIR Plan policies | 684,388 (Mar) | **696,562 (Jun)** | +8% since Sept-2025, but net-add pace DECELERATING 3rd straight qtr | YES — POLLY-P02 confidence CUT |
| CA FAIR Plan exposure | $750B (Mar) | **$768B (Jun)** | +11% since Sept-2025 | YES |
| FL Citizens policies | 336K (Mar) → 293,772 (May) | **278,196 (Jul-31)** | Near-flat Jun→Jul — may be approaching a floor, far under threshold | YES — POLLY-P03 confidence RAISED |
| POLLY-P02 confidence | 72% | **55%** | LOWERED — first cut on this vector since inception | Deceleration finding |
| POLLY-P03 confidence | 60% | **85%** | RAISED — decisively on track | — |
| POLLY-P05 confidence | 82% | **90%** | RAISED — H1 complete, wide margin of safety | — |
| ML-POLLY-17/18 merge defect | Broken since 2026-04-29 | **REPAIRED** | Row split, 17 reconstructed | Housekeeping (Task 3) |

**POLLY NOTE (headline finding this session):** The CA FAIR Plan growth-rate deceleration is the single most load-bearing new fact — it **reverses the direction of travel** on POLLY-P02 (>750K by EOY 2026). At the observed pace (6.0K/mo → 5.5K/mo → 4.1K/mo net adds over the last 3 quarters), FAIR Plan lands ~705-716K by Dec-2026, **below** the 750K threshold, absent a wildfire-driven enrollment spike in the Jul-Oct window that hasn't shown up in the June read yet. This does **not** mean the CA market crisis is resolving — $768B exposure and a still-record policy count are real — but the specific "accelerating toward 750K" claim from April no longer holds on trend.

---

## THESIS

Insurance is both INDICATOR and AMPLIFIER of consumer financial stress. As indicator: premium lapses and uninsured rates signal strain before credit metrics. As amplifier: coverage gaps convert incidents into catastrophes. **CA and FL are diverging, not converging:** CA's structural failure persists (696K FAIR Plan policies, $768B exposure) even as its growth RATE decelerates; FL's recovery is confirmed steeper than April's read (278K Citizens, 30% under the P03 threshold with 4 months of hurricane season still to run). National auto/HO carrier profitability (ALL/PGR/TRV all comfortably under stress thresholds through H1) continues to support the "hard market is over" read for auto specifically — but this is a NARROWING, not resolution, of POLLY's original 2026 thesis: national auto relief + FL recovery vs. CA deepening + health-cost re-acceleration split (UNH improving, ELV worsening) are simultaneously true.

**Thesis confidence: 76%** (down 2pp from 78% — the CA-P02 deceleration is a genuine partial disconfirmation, offset by the FL-P03 and auto-P05 strengthening) | Status: VALIDATED WITH SHARPER GEOGRAPHIC AND CARRIER-LEVEL DIVERGENCE

---

## SIGNAL DASHBOARD

| Vector | ID | Current | Threshold | Status | Trend | Last Updated |
|--------|-----|---------|-----------|--------|-------|--------------|
| Auto Insurance CPI YoY | VX-POLLY-2.01 | 0.8% (Mar 2026) `[FROZEN — Mar 2026, BLS blocked WebFetch this session]` | >8% Yellow | 🟢 GREEN | last known: SHARPLY MODERATING | 2026-04-17 |
| Uninsured Motorist Rate | VX-POLLY-2.03 | 15.4% (2023) `[FROZEN — 2023 IRC, annual series]` | >14% Yellow | 🟡 YELLOW | RISING | 2026-04-09 |
| CA FAIR Plan Enrollment | VX-POLLY-1.03 | **696,562 (Jun 2026)** | Largest carrier | 🔴 RED | RISING BUT DECELERATING (new finding) | **2026-08-10** |
| CA FAIR Plan Exposure | VX-POLLY-1.03 | **$768B (Jun 2026)** | — | 🔴 RED | RISING | **2026-08-10** |
| FL Citizens Policy Count | VX-POLLY-1.03 | **278,196 (Jul 31 2026)** | Growth resuming? NO — still declining | 🟢 GREEN | DECLINING, NEARING FLOOR | **2026-08-10** |
| Homeowners Premium Growth | VX-POLLY-1.01 | 4% nat'l (2026 proj) `[FROZEN — 2026-04-09]` | >8% Yellow | 🟡 YELLOW | last known: STABLE/RISING | 2026-04-09 |
| Auto P&C Combined Ratio | VX-POLLY-2.02 | **ALL 83.3% / PGR 87.3% / TRV 82.8% (Q2 2026)** | >100% Red | 🟢 GREEN | SOLIDLY PROFITABLE, H1 COMPLETE | **2026-08-10** |
| P&C Combined Ratio (broader) | VX-POLLY-4.01 | **TRV 83.6% / ALL 86.6% / PGR 87.3% (Q2)** | >102% Yellow (HO) | 🟢 GREEN | IMPROVING further vs Q1 | **2026-08-10** |
| ACA Marketplace Enrollment | VX-POLLY-3.03 | 23.1M (-4.9% YoY) [Jan 2026] `[FROZEN — Jan 2026; see CARL/DOC for live effectuated-enrollment reads]` | <22M Yellow | 🟠 ORANGE | last known: DECLINING | 2026-04-09 |
| Health Uninsured Rate | VX-POLLY-3.03 | 8% / 27.1M `[FROZEN — 2026-04-09]` | >9% Yellow | 🟡 YELLOW | last known: RISING (policy) | 2026-04-09 |
| Avg Employer Deductible | VX-POLLY-3.02 | $1,886 avg `[FROZEN — 2026-04-09, annual survey]` | >$2,000 Yellow | 🟡 YELLOW | last known: RISING | 2026-04-09 |
| Medical Debt Prevalence | VX-POLLY-3.04 | ~20% / $195B `[FROZEN — 2026-04-09]` | >20% Yellow | 🟡 YELLOW | last known: RISING | 2026-04-09 |
| MA MLR / MCR (UNH consolidated) | VX-POLLY-3.01 | **86.7% Q2 2026; FY guide IMPROVED 88.1%±25bps** | >88% Yellow | 🟡 YELLOW — no breach; FY guide improving | IMPROVING YoY (-270bps) | **2026-08-10** |
| BCR (ELV consolidated) | VX-POLLY-3.01 | **89.7% Q2 2026**; Medicaid op margin trough -1.75% | >88% Yellow | 🟠 ORANGE — Medicaid worsening | WORSENING YoY (+80bps) — diverging from UNH | **2026-08-10** |

*(See parent CARL `thesis/PREDICTIONS.tsv` CRL-22 v3 for the CARL-owned K-shape Selection consumer-coverage-loss test — POLLY mirrors the UNH/ELV inputs above but does not independently score CRL-22.)*

---

## KEY FINDINGS (this session)

| Finding | Source | Date | Significance |
|---------|--------|------|---------------|
| **[NEW] CA FAIR Plan growth DECELERATING 3rd consecutive quarter (6.0K→5.5K→4.1K net adds/mo); trend lands ~705-716K by EOY, below the 750K P02 threshold** | CA FAIR Plan Key Statistics, 2026-06-30, accessed 2026-08-10 | 2026-06 | Reverses April's "accelerating toward 750K" read. P02 confidence cut 72%→55%. Wildfire season (May-Oct) not yet reflected. |
| **[NEW] FL Citizens 278,196 (Jul-31-2026) — 30% below the 400K P03 threshold; Jun→Jul nearly flat, may be approaching a floor** | Citizens FL policies-in-force, accessed 2026-08-10 | 2026-07 | P03 confidence raised 60%→85%. FL recovery confirmed steeper than believed. |
| **[NEW] Allstate/Progressive/Travelers all comfortably profitable through H1 2026 — auto CRs 82.8-87.3%, HO CRs 76.7-94.6%** | ALL/PGR/TRV Q2 2026 earnings, Jul-Aug 2026 | 2026-06/08 | P05 confidence raised 82%→90%. Margin of safety to 95% breach: 8-13pp. |
| **[NEW] UNH and ELV MCR/BCR now DIVERGING — UNH improving YoY (-270bps), ELV worsening YoY (+80bps), Medicaid the differentiator** | UNH/ELV Q2 2026 8-Ks, Jul 2026 | 2026-06 | Confirms K-shape Selection (culling) mechanism is carrier-specific in near-term optics even as CARL's CRL-22 v3 test (consumer-side coverage loss) is unaffected by this divergence. |
| **[NEW] ML-POLLY-17/18 physical-line merge defect repaired** — 17 was truncated mid-sentence into 18's ID field since 2026-04-29, flagged 2026-07-11, never fixed until this session | Own workbook audit, 2026-08-10 | 2026-08 | Housekeeping (Task 3) — content reconstructed from cross-verified CARL STATUS + CARRIER.tsv, no new claims introduced. |
| ELV Q2 2026 actually reported 2026-07-15, not 2026-07-22 as POLLY's 2026-07-18 watch-card assumed | Cross-check vs CARL CRL-22 v3 Notes ("SPEC DEFECT #2") + ELV 8-K | 2026-08 | Both POLLY's SV and CARL's docket carried the wrong date; both already corrected at parent level — no action needed, logged for the record. |

*(Prior-session findings from Apr-2026 archived — see git history / prior STATUS revisions for the full April dashboard; not restated here to keep this file current and under length.)*

---

## GEOGRAPHIC STATUS

| State | Status | Key Metric (Q2 2026) | Key Issue | Outlook |
|-------|--------|------------|-----------|---------|
| CA | 🔴 CRISIS, decelerating | FAIR Plan **696,562** / $768B exposure; ~30% avg rate hike approved eff Oct-15-2026 | Private market structural failure persists; growth RATE now slowing 3 straight quarters | Mixed — base case likely misses 750K by EOY; wildfire season (peaks through Oct) is the swing factor |
| FL | 🟢 RECOVERING, confirmed | Citizens **278,196** (Jul-31), -79% from Oct-2023 peak | 2022 reforms holding; depopulation may be nearing a floor | Positive; 2026 season below-normal so far (2 named storms, 0 hurricanes through Aug 10) — durability still untested against a major landfall |
| LA / TX | 🟡 unchanged this session | `[FROZEN — Apr-2026 read]` | No acute new crisis | Not refreshed — see `[[dossier note]]` |
| National | 🟡 ELEVATED, unchanged this session | `[FROZEN — Apr-2026 read for CPI/uninsured/ACA]` | ACA cliff + OBBBA pipeline still building (parent CARL/DOC own the live read) | Not refreshed here |

---

## PREDICTIONS (summary — see workbook/PREDICTIONS.tsv for full detail; this session's re-scores marked)

| Pred_ID | Prediction | Confidence | Timeframe | Status |
|---------|-----------|------------|-----------|--------|
| POLLY-P01 | OBBBA Medicaid cuts push uninsured rate >9% by end of 2027 | 70% (unchanged) | 2026-2027 | TRACKING |
| POLLY-P02 | CA FAIR Plan >750K policies by Q4 2026 | **55%** (CUT from 72%) | 2026-Q4 | TRACKING — TREND BELOW PACE |
| POLLY-P03 | FL Citizens remains <400K through 2026 hurricane season | **85%** (RAISED from 60%) | 2026-Q4 | TRACKING — STRONG |
| POLLY-P04 | ACA enrollment drops below 22M for 2027 plan year | 75% (unchanged) | 2026-Q4 OE | TRACKING |
| POLLY-P05 | Auto CR below 95% full-year 2026 (ALL/PGR) | **90%** (RAISED from 82%) | 2026-Q4 | TRACKING — STRONG, H1 COMPLETE |
| POLLY-P06 | Bankruptcy filings >600K in 2026 | 55% (unchanged) | 2026-Q4 | TRACKING |
| POLLY-P07 | CA private re-entry <50K net new policies in 2026 | 60% (unchanged — FAIR Plan deceleration is ambiguous evidence, not directly attributable to re-entry vs. reduced demand) | 2026-Q4 | TRACKING |
| POLLY-P08 | Uninsured+underinsured auto >35% next IRC study | 65% (unchanged) | 2027 | TRACKING |

None of the 8 predictions are past their resolution Timeframe as of 2026-08-10 — no formal resolutions this session, only confidence/notes refresh per above.

---

## SEASONAL WATCH (as of 2026-08-10)

- **Hurricane season:** Jun 1-Nov 30, 2026 (ACTIVE, ~half elapsed). Through Aug-10: 2 named storms (Arthur, Bertha — both Gulf, LA landfall), **0 hurricanes**. NOAA holds **75% below-normal probability** (7-13 named storms, 2-6 hurricanes, 0-2 major through Nov). No FL landfall this season; August FL landfalls are historically rare (4 in 150+ yrs, last Idalia 2023). Directly supports POLLY-P03.
- **CA wildfire season:** May-Oct 2026 (ACTIVE, peak still ahead — Jul-Oct historically the worst window). FAIR Plan at $768B exposure; June read does not yet reflect any peak-season fire event. This is the key swing factor for POLLY-P02 — a major fire (as in Jan-2025) could still reverse the deceleration finding.
- **UNH/ELV:** Both reported Q2 (UNH 7/16, ELV 7/15 — corrected). Next: Q3 2026 earnings expected ~Oct-Nov 2026 (not in POLLY's scope going forward — dossier-mode; CARL/DOC own forward tracking).
- **OBBBA implementation:** 6-month redeterminations + work requirements begin Dec 30-31, 2026 (per CMS interim final rule, ML-POLLY-20). Not in this session's refresh scope.

---

*Full workbook detail in `workbook/`. This STATUS.md and `state_vectors/SV-POLLY-2026-08-10-01.md` are the terminal artifacts of POLLY's standing-refresh era — see the SV's DOSSIER CARRY LIST for what survives into dossier-mode.*
