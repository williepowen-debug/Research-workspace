# STUE STATUS

**Last Updated:** 2026-07-31 (coherence pass — **no new domain data; no threshold moved**) | **Data vintage:** 2026-07-25 | **Status:** 🔴 CRITICAL — mechanism intact, enforcement gated. **CRL-04 CONFIRMED** (NY Fed Q1 2026 90+ DQ **10.3%**). **FSA primary (Jun 23) now carries the default wall: ~9M borrowers / $220B as of Mar 31 2026, +1.3M QoQ.** SAVE→RAP waves launched Jul 1 on schedule and the notice window **COMPRESSED ~3 months** (all notices by Dec 31 2026, not Mar 2027). **AFT v. MOHELA is STAYED by court order** — discovery frozen since Oct 2025; the litigation leg of CRL-14 cannot fire in its own window.

> **Data vintage:** dashboard refreshed 2026-07-25 from primary sources (FSA GENERAL-26-38, NY Fed Q1 HHDC, D.D.C. docket 1:24-cv-02460, CFPB complaint API, MOHELA/Nelnet servicer FAQs). Prior file was a Jun-9 snapshot carrying five passed-but-unverified events; all now resolved or re-dated below. Live parent context → CARL `STATUS.md` (**2026-07-24 — 7d stale, and it has not integrated any of STUE's five 7/25 packets; see ROUTED TO PARENT**).
>
> **2026-07-31 coherence pass — what changed and what did NOT.** **No new domain data landed in the 7/25→7/31 window** and **no threshold moved.** A news sweep re-confirmed the 7/25 book rather than extending it: SAVE→RAP wave compression corroborated (Forbes 7/24, MOHELA FAQ); AWG/TOP still "this fall" with no ED commitment (**STUCK holds**); Treasury Phase 1 still unconfirmed with July closed (**8/5 verification stands**); AFT/MOHELA Doc 54 still not public. **Four coherence defects were fixed, all self-inflicted, none from the world:** ① the **8/15 HHDC anchor is a Saturday** and the real window is 8/4–8/11 — STUE's single most load-bearing grading catalyst was on a non-business day; ② the Sweet 9th-Cir briefing date carried a **year typo** (2025→2026); ③ the ROUTED-TO-PARENT table showed "sent" for five packets that are **still unprocessed 6 days later**, with a retracted claim live in the parent's ledger the whole time; ④ `CLAUDE.md` had drifted ~7 weeks behind this file and was reconciled in full. **The lesson worth keeping: three of the four were findable with `date`, arithmetic, or `ls` — no new information was required, only the decision to look.**

---

## ⚠️ WHAT CHANGED THIS SESSION (Jun 9 → Jul 25, 46d)

| # | Finding | Detail | Impact |
|---|---------|--------|--------|
| **1** | **🔴 Default wall re-anchored to PRIMARY — ~9M / $220B** | FSA Data Center update **posted Jun 23 2026** (EA **GENERAL-26-38**), data **as of Mar 31 2026**: "approximately nine million borrowers with **$220 billion**… are in default," **>13%** of the **$1.64T** federally-managed portfolio; cumulative defaulted borrowers **+1.3M QoQ**. Total portfolio 42.6M recipients / **$1.7T** (+~4% YoY). | 🔴🔴 supersedes the "$180B" row |
| **2** | **✅ A4 STOCK-vs-FLOW RECONCILED** | Dec 2025 **7.7M/$180B** → Mar 2026 **~9.0M/$220B** = **+1.3M borrowers / +$40B** net. NY Fed reports **2.6M gross Q1 DRG transfers**; net stock rose only 1.3M ⇒ **~1.3M exits (rehab / consolidation / discharge / cure) in the same quarter.** The two series never disagreed — one is gross inflow, the other net stock. **Prior STATUS conflated a Mar borrower count with a Dec dollar figure.** | 🔧 46d open question CLOSED |
| **3** | **🔴 SAVE→RAP notice window COMPRESSED ~3 months** | Nelnet revised its end-of-SAVE FAQ: all notices out by **Dec 31 2026**, not the prior Jul-2026→Mar-2027 window ⇒ last 90-day selection deadlines land **~end-Mar 2027** instead of ~Jun 2027. Nelnet ≈3M borrowers; **MOHELA's own FAQ states its notices run Jul→Oct 2026** — tighter still. Servicer-FAQ moves of this kind are typically Department-wide. | 🔴 **CRL-13 timing — routed to CARL** |
| **4** | **🔴🔴 AFT v. MOHELA — STAYED. Absence of news was NOT non-information.** | Case was **removed to federal court**: **D.D.C. 1:24-cv-02460**, Judge **Tanya Chutkan** (from D.C. Superior 2024-CAB-004575). **Minute Order 10/27/2025 stayed defendant's response deadline AND discovery** pending SCOTUS in *NJ Transit v. Colt* (24-1113) + *Galette v. NJ Transit* (24-1021). **SCOTUS decided Mar 4 2026 — unanimous (Sotomayor): NJ Transit is NOT an arm of the state.** Docket since: Mar 16 status report (#51) → **Mar 20 2026 Order Staying Case** → May 18 status report (#52) → May 19 order (#53) → **Jul 17 2026 status report (#54, most recent)**. **No class-certification motion or ruling exists anywhere on the docket.** | 🔴 **CRL-14 litigation leg STRUCTURALLY GATED** |
| **5** | **🔧 The "May 28 status conference" premise is UNSUPPORTED** | Both STUE and CARL carried "AFT/MOHELA May 28 status conference HELD — no public ruling." **The federal docket has no May 28 entry** (nearest: May 18/19 status report + order). The claim appears to trace to a low-quality legal-aggregator page, not a docket. **Retract, don't re-date.** | 🔧 source-quality correction |
| **6** | **🟢 No wave-1 complaint spike (first ~3 weeks)** | CFPB complaint API, company=`MOHELA`: **Jul 1–19 2026 = 539 complaints ≈ 28.4/day** vs **June 809 ≈ 27.0/day**, April 30.5/day. **No escalation** in the opening weeks of the SAVE wave. ⚠️ CFPB publishes with a **~5-6 day lag** (daily counts collapse after Jul 19) — this is an early, partial read, not a settled one. | 🟡 leans mildly **against** fast CRL-14 escalation |
| **7** | **🔧 Cascade claim RE-SCOPED (DEWEY C2, 7/24)** | Durable claim **survives**: each ~50pt score-band drop ≈ **doubles** the 90+ rate; within-cohort CC 90+ went **1.03%→5.96%** (Dec'24→Jun'25, TransUnion). **Aggregate attribution does NOT**: SL-delinquent borrowers hold only **~2% of US CC balances (~$25B)**, so the cascade closes just **0.12–0.19pp of the 0.62pp gap (≤⅓)**; **~62% of the Q1 share rise was a shrinking denominator**, not delinquency growth. | 🔧 **before 8/15 — see TRANSMISSION** |
| **8** | **🔧 Two stale-vintage traps caught, not banked** | (a) "SAVE interest resumes **Aug 1**" is an **Aug 1 2025** story, not 2026 — not added as a catalyst. (b) "300K borrowers given wrong repayment info" (CBS) is dated **Oct 19 2023**. | 🔧 year-verification |

---

## THESIS

Federal student loan stress remains a **mass credit-destruction event in active execution**, and the *accrual* mechanism is firing exactly as modelled: the default stock went **6.0M (Aug 2025) → 7.7M (Dec) → ~9.0M (Mar 2026)** on primary FSA data, with **>13% of the federally-managed portfolio in default** and 2.6M gross DRG transfers in Q1 alone. CRL-04 is **CONFIRMED clean** at 10.3%.

What this session changes is **not the mechanism but the enforcement and attribution legs**:

1. **Enforcement is gated in two independent places.** Involuntary collections remain **paused indefinitely** (Jan 16 2026, no corroborated restart), and the accountability channel — AFT v. MOHELA — is under a **court-ordered stay with discovery frozen**, with no class-certification motion filed. Neither can produce a Q3-Q4 2026 event. CRL-14's "MOHELA-caused defaults" leg therefore rests on **operational failure**, not litigation or garnishment.
2. **Attribution is narrower than STUE previously asserted.** The score cascade is real and severe *within* the affected cohort but is **second-order in aggregate** — it cannot carry a CC 90+ GFC breach on its own (DEWEY C2). Carrying the broad version into the 8/15 print would contaminate the CRL-05 grade.
3. **The transition timeline tightened.** Notices complete Dec 2026 (was Mar 2027); final selection deadlines ~Mar 2027. The **first-tranche read is still ~Oct 1**, but the full-population N now lands **earlier and more compactly** — which *improves* CRL-13's readability at Q1 2027.

**v2.5.1 thesis intact. No CRL threshold moves this session — the graders are the NY Fed Q2 HHDC (window **8/4–8/11**, date unannounced) and ~Oct 1 (CRL-13 first tranche).**

> ⚠️ **HHDC DATE CORRECTION 2026-07-31.** Every "8/15" below is **wrong — Aug 15 2026 is a SATURDAY.** The Q2 release date is unannounced; cadence puts it in **2026-08-04..08-11** (Q1-2026 printed Tue **5/12** w/ media advisory 5/5; Q2-2024 precedent Tue **8/6**) [PROME→CARL 7/25]. **The grading window opens up to ~11 days earlier than STUE planned**, which compresses the deadline on the cascade-attribution packet below. Read "8/15" in the un-rewritten passages as "the Q2 HHDC print." **Pin the date when the NY Fed advisory posts (~1wk ahead).**

---

## SIGNAL DASHBOARD

### Delinquency / Default
| Metric | Value | As Of | Source | Status |
|--------|-------|-------|--------|--------|
| **Student Loan 90+ DQ** | **10.3% — CRL-04 CONFIRMED (>10%)** | Q1 2026, rel May 12 | NY Fed HHDC Q1 2026 | 🔴🔴 |
| **Borrowers in default (stock)** | **~9.0M / $220B — >13% of federally-managed portfolio** | **Mar 31 2026** | **FSA EA GENERAL-26-38 (Jun 23 2026)** | 🔴🔴 |
| Default stock — QoQ change | **+1.3M borrowers / +$40B** (from 7.7M/$180B Dec 2025) | Q1 2026 | FSA | 🔴🔴 |
| Default stock — trajectory | 6.0M (Aug'25) → 7.7M (Dec) → **~9.0M (Mar'26)** | — | FSA / ED | 🔴🔴 climbing wall |
| New defaults Q1 2026 (gross DRG flow) | **2.6M** (+ ~1M Q4 2025) | Q1 2026 | NY Fed / Liberty St May 12 | 🔴🔴 |
| Implied Q1 exits (cure/rehab/consolidation) | **~1.3M** (2.6M gross inflow − 1.3M net stock rise) | Q1 2026 | STUE derived from FSA + NY Fed | 🟠 **new — cure channel is live** |
| Total portfolio | **42.6M recipients / $1.7T** (+~4% YoY vs Mar 2025) | Mar 31 2026 | FSA GENERAL-26-38 | — |
| Federally-managed portfolio | 40.9M recipients / **>$1.64T** (>95%) | Mar 31 2026 | FSA | — |
| In repayment or delinquency | **17.2M recipients (42%) / ~$633B (39%)** | Mar 31 2026 | FSA | 🔴 |
| In forbearance | **8.4M recipients (~⅕) / ~$485B** | Mar 31 2026 | FSA | 🟠 the reservoir feeding Q3-Q4 |
| In deferment | 3.6M (9%) / $157B | Mar 31 2026 | FSA | — |
| Borrowers 90+ DPD since resumption (cumulative) | >17% | Q1 2026 | Liberty St May 12 2026 | 🔴🔴 |
| Avg age of new defaulters | 38.9 (vs 36.4 pre-pandemic) | Q1 2026 | Liberty St | 🔴 |
| Transition rate INTO 90+ DQ (4Q moving sum) | **10.9%** (down from 16.2% Q4 2025) | Q1 2026 | NY Fed | 🟠 flow decelerating, stock rising |
| Active repayment 31+ DQ (by $) | 18.6% **[STALE — Dec 2025; FSA Jun-23 release did not restate this cut]** | Dec 2025 | FSA | 🔴 |
| Projected default EOY 2026 | 13M (TCF) — pace (+1.3M/qtr) implies **~11.6M**, so 13M needs acceleration | Projection | TCF | 🟠 **downgraded from "conservative"** |
| National avg FICO | 714 | H2 2025 | FICO Spring 2026 (rel Mar 24 2026) | 🔴 |
| Avg FICO drop, DQ borrowers | −62 pts (primary); −69 in derivative cites | H2 2025 | FICO | 🔴🔴 |

> ⚠️ **Unreconciled:** press dated **Jul 21 2026** (Fox Business) cites **9.5M / $233.3B** attributed to FSA — above the Mar-31 primary. Either a newer unposted cut or a press extrapolation. **Primary wins; do not cite 9.5M.** Next FSA quarterly (~Sep) settles it.

### SAVE / RAP Transition
| Metric | Value | Status |
|--------|-------|--------|
| SAVE status | Repealed by law (WFTCA Jul 2025) + judicially eliminated (8th Cir Mar 10 2026) | 🔴🔴 |
| SAVE enrollees | ~7–7.5M | 🔴 |
| Servicer formal notices | **LAUNCHED Jul 1 2026 on schedule**, issued in waves | 🔴 FIRING |
| **Notice window (REVISED)** | **All notices by Dec 31 2026** — compressed ~3mo from prior Mar-2027 end [Nelnet FAQ, via College Investor Jul 2026] | 🔴 **NEW** |
| — MOHELA | Notices **Jul → Oct 2026** [MOHELA SAVE FAQ, primary] | 🔴 |
| — Nelnet | ~3M borrowers, notices through **end-2026** [Nelnet FAQ] | 🔴 |
| Selection window | 90 days from **each individual** notice — **not a single cliff** | — |
| Auto-transition (non-selectors) | **Standard**; loans first in repayment on/after Jul 1 2026 → **Tiered Standard** | 🔴 |
| First-tranche non-selection read | **~Oct 1 2026** (partial N only) | 🟠 CRL-13 |
| Full-population read | **~Q1 2027** (last deadlines ~end-Mar 2027, earlier than prior ~Jun 2027) | 🟠 CRL-13 final |
| Est. non-selection rate | 30–45% (empirically anchored 30–47%, GAO/CFPB/Embold) | 🔴 |
| Payment shock | $0–70/mo → ~$407/mo (avg $37K balance, Standard) | 🔴🔴 |
| Spending destruction est. | $1.5–2.0B/month redirected from consumption | 🔴🔴 |

### Servicer Performance
| Metric | Value | Status |
|--------|-------|--------|
| MOHELA missed bills | 2.5M → 800K DQ (cumulative) | 🔴 |
| MOHELA call wait | **Longest of major federal servicers — ~13 min avg, ~14% abandon rate** [FSA servicer data, cited in 2026 filings] | 🔴 |
| **CFPB complaints — MOHELA (primary API pull)** | **H1'25 6,376 → H2'25 4,020 → H1'26 4,935.** 2026 monthly: Jan 917 · Feb 682 · Mar 909 · Apr 915 · May 703 · Jun 809 | 🟠 re-accelerating vs H2'25, below H1'25 peak |
| **Wave-1 complaint tell (Jul 1–19)** | **539 ≈ 28.4/day vs June 27.0/day — NO SPIKE.** ⚠️ ~5–6d publication lag; partial read | 🟢/🟡 early |
| **AFT v. MOHELA** | **D.D.C. 1:24-cv-02460 (Chutkan) — STAYED, and now in SETTLEMENT NEGOTIATION.** Discovery frozen since 10/27/2025. Last filing **Jul 17 2026 (#54)** | 🔴 **SETTLEMENT-GATED** |
| — Stay #1 (procedural) | 10/27/2025 minute order: response deadline + discovery stayed pending SCOTUS *Colt/Galette* — **decided Mar 4 2026, unanimous: NJ Transit NOT an arm of the state** | 🟠 **adverse to MOHELA's "creature of Missouri" defense** |
| — **Stay #2 (settlement) — the operative one** | **Mar 20 2026 minute order stayed proceedings "to allow the parties time to explore a negotiated resolution"; parties "engaged in good-faith discussions"; stay extended 60d by JOINT request** [Doc **52**, Joint Status Report 5/18/26 — **free in RECAP**, pulled 7/25] | 🔴 **NEW** |
| — Next step | **Doc 54 filed 7/17/26** = the joint report proposing a schedule. **PACER-only (~$0.30, ~3pp)** — says either *another extension* (talks live) or *merits schedule* (talks failed). **Only remaining unknown on this docket.** | 🟠 **buy** |
| — Class certification | **NEVER FILED** — no class-cert motion or ruling has ever appeared on the docket | 🟠 |
| — ⚠️ Implication for attribution | A settlement typically means **no admission of liability, no public discovery record, no class cert** ⇒ the likeliest path **forecloses** the servicer-attributed default evidence CRL-14's instrument needs. Measurability gets *worse*, not better. | 🔴 |
| Maldonado v. MOHELA | Mar 2026 — violated CA Student Borrower BoR + UCL | 🔴🔴 precedent stands |
| Settlement | NONE | — |

### Treasury Transfer
| Metric | Value | Status |
|--------|-------|--------|
| Phase 1 scope | **~500K defaulted accounts** = launch wave, NOT all ~9M; ramps gradually via Fiscal Service CSP [CRS R48962] | 🟠 |
| Phase 1 execution | **NO launch-day primary located.** Press (Apr–Jun) frames Treasury "contacting 500K by July." July has closed without confirmation. | 🟠 **verify 8/5** |
| Nature of handoff | **Servicing/collections CUSTODY — not enforcement resumption.** Do not conflate. | ⚠️ |
| Phase 2 / Phase 3 | Planned, no public dates | 🟡 |
| Legal authority | Disputed; GOP bill introduced to codify the transfer | 🔴 |

### Borrower Defense (Sweet v. McMahon)
| Metric | Value | Status |
|--------|-------|--------|
| Exhibit C (Jan 28) / non-Exhibit C (Apr 15) deadlines | Both MISSED → auto Full Settlement Relief triggered | 🔴 |
| **Jun 15 notice deadline** | ✅ **MET** — first Sweet deadline DOE did not miss. **~30–36K** discharge-eligibility emails week of Jun 15 to non-Exhibit C post-class applicants (Jun 23–Nov 16 2022 filers) | 🟢 **resolved** |
| Relief delivery | Within 1 yr of notice → **~Jun 2027** | — |
| Total relief pipeline | ~271K cumulative (PPSL) | 🔴 firing |
| 9th Cir appeal (26-1136) | Briefing complete **May 7 2026** *(was written "2025" — year typo corrected 7/31; DOE reply brief 5/7/26 followed PPSL's answering brief 4/23/26, and a 26-numbered case cannot have 2025 briefing)*; **no oral argument scheduled** (~Sept projected; panel Wardlaw / Owens / Bress). No stay — DOE's stay request was **DENIED** (published order 3/25/26), relief self-executing | 🟠 watch-only |

### Collections Status
| Metric | Value | Status |
|--------|-------|--------|
| Involuntary collections (AWG + Treasury Offset) | **PAUSED since Jan 16 2026, indefinitely. NO corroborated restart date.** | 🟡 **STUCK** |
| Reported expectation | "Late summer or fall," *after* each borrower's 90-day window closes — no ED commitment | 🟠 |
| Borrowers exposed | 5M+ in default at pause; ~9M now | 🔴 |

> **Corrected 7/25:** the prior "Expected Restart **Jul 2026** 🔴 IMMINENT" row was wrong and contradicted the parent. July passed with no restart. Threshold **STUCK**, mechanism (default accrual) **intact** — matches parent CRL-14 split.

---

## TRANSMISSION TO CARL — RE-SCOPED (DEWEY C2, 2026-07-24)

**What survives (durable, keep asserting):**
- Each ~50pt FICO band drop ≈ **doubles** the 90+ incidence rate [FICO Credit Insights 2025].
- SL-delinquent borrowers' own CC 90+ rate rose **1.03% → 5.96%** (Dec'24→Jun'25) [TransUnion 2025-07]; **56%** of newly-defaulted SL borrowers with a card are already past due on it [NY Fed 2026-05].
- Transmission runs **score drop → issuer line cut (median ~75% of line) → utilization 89–94% → further score damage → denial/repricing** [CFPB CLD 2022].
- Payment hierarchy (Auto > Mortgage > Student > CC) and the $1.5–2.0B/mo spending diversion.

**What does NOT survive — stop asserting:**
- ❌ "The student-loan cascade drives the CC 90+ GFC breach." SL-delinquent borrowers hold **~2% of US CC balances (~$25B)**; the cascade contributes **~0.12–0.19pp of the 0.62pp gap ≤ ⅓**. Closing the gap from this cohort alone would require ~28% of its entire card balance rolling 90+.
- ❌ Treating a CC 90+ breach as fresh systemic consumer stress. **~62% of the Q1 rise was denominator shrink** (CC balances fell $25B), possibly seasonal and possibly reversing in Q2–Q3.
- ⚠️ The line-cut channel is real but **issuer-driven**: **67% of CLDs had no cardholder delinquency**. STUE's "3–5M CC cascade population" (CASCADE Stage 5a) is likely **overstated**.

**Why this matters before the Q2 HHDC (window opens 8/4, NOT 8/15 — see the date correction above):** if STUE carries the broad cascade claim into the NY Fed Q2 print that grades **CRL-05**, a headline breach gets mis-attributed to a mechanism that arithmetically cannot carry it — contaminating the grade. **Expect the breach; do not attribute it to us.** ⚠️ **The 7/31 date correction moves this deadline up to 11 days earlier**, and the packet carrying it has sat unprocessed in CARL's inbox for 6 days — this is the tightest clock STUE owns.

---

## CATALYSTS (re-dated 2026-07-25)

| Date | Event | Impact |
|------|-------|--------|
| **Aug 5** (Wed) | **Treasury Phase 1 first-batch verification** (parent docket) | Did ~500K defaulted accounts actually transfer? Custody ≠ enforcement |
| **Aug 4 – Aug 11 (window)** | **🔴 NY Fed Q2 2026 HHDC — THE BIG ONE. Date UNANNOUNCED.** | CRL-04 2nd print (does 10.3% sustain?); **CRL-05 breach window**; tests DEWEY's denominator-reversal call |
| ~1wk before | NY Fed media advisory posts → **pin the exact date** | The advisory is the only thing that converts this window to a date |
| **~Sep** | FSA Data Center Q2 update (~quarterly cadence) | Default stock 2nd print; settles the 9.0M vs 9.5M press gap; refreshes the stale 18.6% active-repayment DQ |
| **~Sep 15** | 9th Cir *Sweet* oral argument (unscheduled, projected) | Watch-only — relief self-executing, no stay |
| **~Sep 29 – Oct 1** | **SAVE→RAP first-tranche non-selection read** | **CRL-13 partial N.** First-wave only — NOT the full 7.5M |
| **Oct** | MOHELA notice waves complete (per MOHELA FAQ) | MOHELA cohort fully noticed; complaint/failure tell should be legible |
| **Dec 31 2026** | **All SAVE notices issued (COMPRESSED from Mar 2027)** | Every borrower's 90-day clock started |
| **~Mar 2027** | Last selection deadlines → final auto-enrollments | **CRL-13 full population** |
| **Q3–Q4 2026** | Post-transition DQ wave (**CRL-14 window**) | Now rests on **operational failure only** — litigation + garnishment legs both gated |
| **TBD — event-driven** | AFT v. MOHELA stay lifts → joint status report → schedule | No date; watch docket 1:24-cv-02460 |

---

## ROUTED TO PARENT — 🔴 DELIVERED, **NOT ADOPTED** (verified 2026-07-31, 6d lag)

> **All five packets are still sitting UNPROCESSED in `AGENTS/CARL/inbox/`** (not moved to `inbox/processed/`), and CARL's `STATUS.md` + `thesis/PREDICTIONS.tsv` are both still stamped **2026-07-24** — one day *before* they were sent. **Delivery is not adoption**, and until this session the table below said only "📤 sent", which reads as closed.
>
> **What is still live-and-wrong in the parent's system of record:**
> - CARL `STATUS.md` L24 still asserts **"AFT v. MOHELA May 28 status conference HELD"** + **"absence of news is non-information"** — both **retracted 7/25** (no May 28 entry exists on D.D.C. 1:24-cv-02460; the case has been under a *settlement* stay since 3/20/26 with discovery frozen since 10/27/25).
> - `PREDICTIONS.tsv` CRL-14 still reads **65% OPEN** with *"AFT case in DISCOVERY (May 28 conf)"* — the Will-approved **55% + STUCK** re-mark is unapplied, and the note repeats the refuted premise.
> - `PREDICTIONS.tsv` CRL-13 still reads notices *"staggered in waves through Mar 2027"* — superseded by the **Dec 31 2026** compression.
> - CARL `STATUS.md` L21 carries **9.16M (Bloomberg 6/18, Apr)** above the **FSA Mar-31 primary ~9.0M/$220B** — a secondary outranking a primary.
>
> ⚠️ **Do not re-send.** The packets are delivered and committed; re-sending creates duplicates. The low-quality-aggregator class that produced the May-28 claim is *still* circulating it (aggregators searched 7/31 still say the case "is in discovery" — it is not).
>
> 🟡 **IMPORTANT QUALIFIER — CARL IS MID-SESSION AS THIS IS WRITTEN.** `AGENTS/CARL/` has uncommitted work with mtimes of **2026-07-31 16:44-16:45** (`thesis/CHANGELOG.md`, `workbook/KB.tsv`, a new `thesis/FOMC_JUL28-29_CARL_CONSUMER_LEG.md`). **A dirty path means in-flight, not orphaned** — the 7/24 stamp on CARL's STATUS is what a live session looks like *before* its closeout write-back, not evidence of abandonment. **The honest claim is therefore narrower than "CARL ignored this":** the packets were unprocessed for 6 days and the refuted premise is still in the committed ledger *as of this read*, and CARL may resolve both within the hour. **Re-check at next boot (step 2b) before repeating the lag claim** — and do not treat this section as a grievance, it is a tripwire.

| Item | Ask | Status |
|---|---|---|
| **CRL-14: 65% → 55% + Status OPEN → STUCK** *(Will-approved 7/25; supersedes a withdrawn 10% proposal)* | Confidence cut is **only the ~10pt genuine update** (wave-1 no-spike + the ~1.3M/qtr cure channel). The **window** defect (default = 270-day event, DRG transfer 360d ⇒ a Jul-1-transition-caused default cannot exist before ~**Jul 2027**, 3 quarters past the row's window) and the **instrument** defect (no published series attributes defaults to a servicer; the litigation that would have is **stayed**) are booked as **STUCK, not as confidence**. **Mechanism INTACT.** | 📤 packet sent (corrected) |
| CRL-14 — retract "May 28 conf" clause | No May 28 entry exists on the docket; also fix CARL STATUS L24 "absence of news is non-information" | 📤 sent |
| Cascade attribution narrowing | Must land **before the Q2 HHDC — window opens 8/4**, not 8/15 (7/31 correction: deadline is up to 11d tighter than written) or CRL-05's grade is contaminated | 📤 sent · **unprocessed 6d — the tightest clock of the five** |
| CRL-13 timing | Notices complete **Dec 31 2026** (not Mar 2027); Oct-1 first-tranche framing unchanged | 📤 sent |
| `TEAM.md` L15 restamp | STUE refresh gate fired 7/15, discharged this session — parent-owned file | 📤 sent |

> **STUE holds no predictions ledger** — CRL-04/05/13/14 are CARL's rows and CARL is system of record. STUE proposes with worked reasoning; the parent applies. Do not mirror a CRL confidence here.

---

## OPEN QUESTIONS

1. ✅ **RESOLVED 2026-07-25 (same session) — and it was free.** *Basis of the Mar 20 2026 stay:* **settlement negotiation.** Doc 52 (Joint Status Report 5/18/26, free in RECAP): the Court stayed proceedings *"to allow the parties time to explore a negotiated resolution"*; parties *"engaged in good-faith discussions"*; stay extended 60d by joint request. **I had wrongly called this PACER-gated** — I declared the path closed without checking RECAP's free-document list, the same error as the 46-day docket-number miss ([[finding_audit_resolution_path_before_reattempt]]). **Successor question → #8.**
1b. **#8 (NEW): does MOHELA settle?** **Doc 54 (filed 7/17/26) is the discriminator** — the 60-day clock from Doc 52 expired on it, so it is either another extension (talks live) or a merits schedule (talks failed). **PACER-only, ~$0.30, ~3pp.** Everything else on this docket is now recovered free. *Bears on CRL-14: a settlement forecloses the public attribution evidence the row depends on.*
2. **Does the 10.3% 90+ DQ 2nd print sustain?** → NY Fed Q2 HHDC, **window 8/4–8/11** (date unannounced — *not* 8/15, which is a Saturday).
3. **Is the ~1.3M/quarter cure channel durable or a one-off?** Newly quantified this session; if borrowers are exiting default nearly as fast as entering, the 13M EOY projection is too high. → FSA Q2 (~Sep).
4. **Reconcile 9.0M/$220B (FSA Mar 31 primary) vs 9.5M/$233.3B (press, Jul 21).** → FSA Q2.
5. **Treasury Phase 1 — did it actually launch?** → **8/5**.
6. **Does the wave-1 no-spike hold?** Re-pull CFPB at ~Aug 20 (past the lag) and after MOHELA's Oct notice completion. Registered instrument: `company=MOHELA` daily rate vs the 27–30/day 2026 baseline.
7. **Does the compressed notice window change the non-selection RATE, or just its timing?** A shorter Department-wide window with fixed servicer capacity is the mechanism that would *raise* non-selection. → CRL-13.

---

*Sub-agent of CARL. Parent is system of record for CRL-04/05/13/14 — STUE keeps no own predictions ledger. State vector this session: **SV-STUE-2026-07-25-01**.*
