# PREDICTIONS MONITOR
**Purpose:** Falsifiable prediction ledger. Granular claim-level track. Includes HIT / MISS / TRUE-in-letter-FALSE-in-spirit / falsified — the falsification log is a discipline asset, not a stigma to hide.
**Last restructured:** 2026-06-06 (self-audit Phase B). Last *content* update before that: 4/4 (9 weeks stale at time of restructure).
**Format:** ID | Date | Source | Claim | Trigger | Status | Conf

---

## DISCIPLINE RUBRIC

Apply when entering, updating, or resolving any prediction. Came from real misses.

1. **Threshold vs Mechanism** — separately track whether the threshold sticks AND whether the mechanism claimed was actually the cause. Threshold-only resolution can be TRUE-in-letter, FALSE-in-spirit.
2. **Single-month skepticism** — single-print sub-component moves get tagged `[needs 2nd-print]` before load-bearing. Sustained 2-mo direction > sharp 1-mo magnitude.
3. **Catalyst vs Consequence** — P(consequence) = P(catalyst) × P(consequence | catalyst). Never transcribe catalyst-prob as consequence-prob without the conditional. Each prediction must specify which.
4. **Single-print prediction-market skepticism** — single Polymarket/Kalshi prints are not "holds"; require ≥3-day re-check + cross-source verify.

### Status taxonomy

- ✅ **HIT** — threshold + mechanism both confirmed.
- ✅L **TRUE-in-letter** — threshold confirmed, mechanism wrong/absent.
- ✅P **PARTIAL** — partial confirmation; specify which axis.
- ❌ **MISS** — threshold not reached by deadline.
- ❌F **FALSIFIED** — mechanism broken (independent of threshold).
- 🟡 **DEFERRED** — extended deadline (specify new date).
- 🔵 **PAST-TRIGGER / UNVERIFIED** — trigger date passed, resolution not yet verified against ground truth. Pending E-phase or future verification.
- 🔴 **ACTIVE** — forward-looking, trigger date not yet reached.

---

## ✅ CONFIRMED (preserved from March-April resolutions)

| ID | Date | Source | Prediction | Trigger | Status | Notes |
|----|------|--------|-----------|---------|--------|-------|
| PRED-01 | ~Feb 2026 | NEXUS/HAWK | Gas $4 behavioral breakpoint → consumer spending contraction | Gas ≥$4/gal sustained | ✅ HIT | Gas $3.983, +$1.01/mo (+34%). Promoted → CONFIRMED.md C-28. |
| PRED-02 | ~Feb 2026 | NEXUS | FL UI Wave 1 exhaustion → CC DQ spike ~May | FL WARN cohort Dec 2025 exhausts 12-wk | ✅P PARTIAL | Wave 1 fired Mar 24. Promoted partial → C-05. CC DQ spike resolution: see PRED-21. |
| PRED-03 | ~Feb 2026 | HENRY | FOMC holds, both mandates cited, 0-1 cuts | Mar FOMC | ✅ HIT | HEN-04. |
| PRED-04 | Mar 2026 | HENRY | Mar 16 relief rally = bull trap | Price action post-Mar 16 | ✅ HIT | HEN-07. |
| PRED-05 | Mar 2026 | HENRY | VIX gaps to 28+ | Escalation catalyst | ✅ HIT | VIX 30+ intraday Mar 23. HEN-08. |
| PRED-06 | Mar 2026 | HENRY | SPX tests 6,550-6,600 | Escalation pressure | ✅ HIT | 6,556 Mar 24. HEN-10. |
| PRED-07 | Mar 2026 | HENRY | Brent $110-115 | Supply disruption acceleration | ✅L EXCEEDED | Hit $119. HEN-09. |
| PRED-08 | ~Mar 2026 | NEXUS/LABOR | NFP Feb print negative | WARN→payroll | ✅ HIT | NFP -92K (Mar 6 BLS). r=0.78 WARN→payroll. Folded into C-19. |
| PRED-09 | ~Mar 2026 | NEXUS | Stagflation trap | NFP neg + oil high + Fed paralyzed | ✅ HIT | C-19. |
| PRED-10 | ~Mar 2026 | NEXUS | "Help with mortgage" ATH surpassing GFC | Consumer stress metric | ✅ HIT | C-24. |
| PRED-11 | Mar 2026 | NEXUS | UST demand destruction / petrodollar collapse | Gulf surplus breakdown | ✅ HIT | C-07/C-15 (now merged into C-34). Campbell "Strip vs Strait". |
| PRED-12 | ~Mar 2026 | NEXUS | BOJ/FOMC dual catalyst | Shunto + BOJ signal | ✅ HIT | C-23. Shunto 5.26%. |
| PRED-13 | Mar 2026 | HENRY | Iran "talks" rally = bull trap | Iran denial + combat resume | ✅P PARTIAL | HEN-11. Pattern repeating. Promote candidate → CONFIRMED.md (pending C-ID assignment). |

---

## 🔴 ACTIVE / FORWARD-LOOKING

| ID | Date | Source | Prediction | Trigger Date/Condition | Status | Conf |
|----|------|--------|-----------|----------------------|--------|------|
| PRED-20 | Mar 2026 | NEXUS/HENRY | HY OAS 320→500 in 2-4mo (2007 template) | OAS ≥350 = issuance freeze; ≥500 = 2008-style | 🔴 ACTIVE — **needs current OAS read** (5/21 anchor was 280-286); decay risk | TBD |
| PRED-24 | Mar 2026 | NEXUS | Private credit cascade Stage 2→3 transition | HY OAS ≥350 / bank↔shadow bank contagion | 🔴 ACTIVE — Stage 2 institutionalized; Stage 3 threshold not crossed by 5/21 | reduced |
| PRED-30 | Mar 2026 | NEXUS | Gulf surplus recycling collapse → structural UST/equity selling | Oil suppression + Gulf revenue decline | 🔴 ACTIVE — C-34. **Threshold-vs-mechanism caveat:** SIG-26060601 (BRENT MM-long unwind) may indicate the mechanism rotating; reassess in E. | 90% |
| PRED-32 | ~Mar 2026 | NEXUS | China buffer exhaustion → LGFV cascade (¥66T) | Mid-May to late June 2026 | 🔴 ACTIVE — trigger window currently live | 85% |
| PRED-35 | Mar 2026 | NEXUS | LGFV cascade: oil→margin→tax→LGFV | China oil buffer exhaustion | 🔴 ACTIVE — same window as PRED-32 | 85% |
| PRED-36 | Mar 2026 | BROCK | HY OAS >400bps | Jun-Jul 2026 | 🔴 ACTIVE — needs current OAS read | 85% |
| PRED-37 | Mar 2026 | BROCK | HY OAS >500bps | Aug-Sep 2026 | 🔴 ACTIVE | 70% |
| PRED-38 | Mar 2026 | BROCK | Bank writedowns visible in Q2-Q3 earnings | Apr-Jul 2026 | 🔴 ACTIVE — Q2 prints rolling | 85% |
| PRED-39 | Mar 2026 | BRENT/HANS | Phase 1 supply disruption extends to Q3 2026 | Infra rebuild 60-90d | 🔴 ACTIVE — **catalyst-vs-consequence caveat:** is this catalyst-prob (rebuild needed) or consequence-prob (price stays elevated)? Distinguish in E. | 90% |
| PRED-40 | Mar 2026 | BROCK/NEXUS | Bank loss exposure $73.4-137.6B | Q2-Q3 earnings | 🔴 ACTIVE | 80% |
| PRED-41 | Mar 2026 | OTTO/NEXUS | Mass-market consumer stress breaks Q4 2026 / Q1 2027 | 6-12mo lag from RV/auto destruction | 🔴 ACTIVE | 75% |
| PRED-43 | Mar 2026 | HANS/HAWK | Dimona→Fordow→Kharg sequence as main escalation path | Israeli nuclear retaliation to Dimona strike | 🔴 ACTIVE — **catalyst-vs-consequence caveat:** P(sequence) = P(Dimona strike) × P(Israeli nuclear retaliation \| Dimona strike). Reassess given HAWK 5/22 partial-thaw reframe (SIG-26060602). | 65% (likely reducing) |
| PRED-45 | Apr 2026 | NEXUS | Blue Owl arms-length fire sale triggers industry mark-down | First secondary at 85-90¢ or below | 🔴 ACTIVE | 90% |

---

## 🔵 PAST-TRIGGER / RESOLUTION UNVERIFIED

These items have passed their trigger date but were not formally resolved during the 5/21 reset. Mark and verify in E-phase against ground truth (don't restate from prior surface text — see `[[feedback_verify_counts_before_propagating]]`).

| ID | Date | Source | Prediction | Trigger | Lean (UNVERIFIED) | Resolution needs |
|----|------|--------|-----------|---------|-------------------|------------------|
| PRED-21 | Mar 2026 | NEXUS/CARL | FL UI Wave 1 → CC DQ spike ~May | ~May 2026 | UNVERIFIED — CC DQ data needed | CARL header refresh |
| PRED-22 | Mar 2026 | SAM | BOJ hike May 1 | BOJ meeting May 1 | LIKELY MISS — no May 1 hike referenced in 5/21 state | SAM header / Japan rates |
| PRED-23 | Mar 2026 | HENRY/NEXUS | Q1 quarter-end SOFR spike Mar 27-28 | Q1 close Mar 31 | ✅P PARTIAL (already marked) — spiked then normalized | LIQUID confirmation |
| PRED-25 | Mar 2026 | HAWK/NEXUS | HAWK Scenario D ≥80% | War escalation threshold | ✅ HIT (already marked 92% on 4/1) — **SUPERSEDED** by HAWK 5/22 reframe (SIG-26060602: D now 35%) → mechanism shifted | Promote HIT → CONFIRMED; flag mechanism-shift to RED |
| PRED-26 | Mar 2026 | RED | RED bear confidence ≥85% | Thesis integrity | UNVERIFIED — 6+ wks unmarked | RED header refresh |
| PRED-27 | Mar 2026 | NEXUS | BDC rating contagion: ARCC/OBDC/GBDC downgrades | Moody's post-FSK Ba1 | UNVERIFIED — outcome of 48-72hr catalyst (4/4) | BROCK / Moody's check |
| PRED-28 | Mar 2026 | HENRY | PCE Mar 28 hot (≥2.7% headline) | Mar 28 print | UNVERIFIED | HENRY header / PCE print |
| PRED-29 | Mar 2026 | HAWK/NEXUS | Yanbu strike → Brent $145-165 | Yanbu hit | **NOT TRIGGERED** — catalyst (Yanbu strike) did not fire to public knowledge. **Catalyst-vs-consequence reminder:** consequence-prob undefined until catalyst fires | Confirm Yanbu status |
| PRED-31 | Mar 2026 | NEXUS | FL UI Wave 2 peak → second DQ wave | Apr 26 peak | UNVERIFIED | LABOR/CARL refresh |
| PRED-33 | Mar 2026 | HENRY | Iran 5-day pause expires Mar 28 → escalation resumes | Mar 28 (extended to Apr 6) | LIKELY ❌F FALSIFIED — HAWK 5/22 partial-thaw reframe means mechanism (escalation resumes) inverted | Promote to FALSIFIED on HAWK confirm |
| PRED-34 | Mar 2026 | NEXUS | APO stock repricing as "Apollo gates Apollo" | News cycle absorption | UNVERIFIED — APO sustained >$130 per 5/21 STATUS suggests MISS on repricing thesis | APO mark verify |
| PRED-42 | Mar 2026 | ZHAO | Belgium TIC Jan 2026 >$500B | TIC Mar 19 print | UNVERIFIED | TIC data check |
| PRED-44 | Mar 2026 | OTTO/NEXUS | JEF "losses over time" → multi-lender markdowns Q1-Q2 | Q1 bank earnings Apr 20-29 | UNVERIFIED — Q1 prints past; not in 5/21 integrated | REGINALD / OZK refresh |
| PRED-46 | Apr 2026 | NEXUS/SAM | BOJ Apr 23-24 rate hike (pulled fwd from May) | Apr 23-24 BOJ | LIKELY MISS — USDJPY ~159 on 5/21 + 5/21 references "June BOJ path" implies no Apr hike | SAM header / BOJ statement |
| PRED-47 | Apr 2026 | NEXUS/HAWK | Iran pause expiry Apr 6 → escalation within 2 weeks | Apr 6 + 14d | LIKELY ❌F FALSIFIED — HAWK 5/22 partial-thaw reframe; Trump call-off | Promote to FALSIFIED on HAWK confirm |

---

## ❌ FALSIFIED / SUPERSEDED (preserved as discipline log)

| ID | Date | Source | Prediction | Why Falsified |
|----|------|--------|-----------|---------------|
| PRED-F01 | Feb 2026 | NEXUS | Soft landing scenario | NFP -92K, gas $4, stagflation confirmed (RED tombstone). |
| PRED-F02 | Mar 2026 | External | "Productive Iran talks" — Mar 23 rally narrative | Iran explicitly denied negotiations; active combat in Tehran + near Dimona simultaneous. T-14. |
| PRED-F03 | Mar 2026 | External (BofA) | BofA buy upgrade OWL/ARES/KKR (Mar 18) | Rejected by Mar 19 price action. T-11. |

---

## E-phase resolution priorities (pre-2026-06-09)

1. **Promote** PRED-13, PRED-25 to CONFIRMED.md with C-ID assignment.
2. **Falsify** PRED-33, PRED-47 on HAWK header confirm (likely confirmed by SIG-26060602).
3. **Resolve** PRED-22, PRED-46 on SAM header (BOJ outcomes).
4. **Apply Catalyst vs Consequence** review to PRED-29, PRED-39, PRED-43 (rewrite as conditional probs).
5. **Refresh** PRED-20, PRED-36 against current HY OAS read (5/21 anchor was 280-286; needs current).
