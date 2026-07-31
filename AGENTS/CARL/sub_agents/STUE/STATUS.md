# STUE STATUS

**Last Updated:** 2026-07-31 (coherence pass **+ full news/data sweep** — **no threshold moved; one MISSED event recovered**) | **Data vintage:** 2026-07-25, w/ *Sweet* 9th Cir refreshed to 7/17 | **Status:** 🔴 CRITICAL — mechanism intact, enforcement gated. **CRL-04 CONFIRMED** (NY Fed Q1 2026 90+ DQ **10.3%**). **FSA primary (Jun 23) now carries the default wall: ~9M borrowers / $220B as of Mar 31 2026, +1.3M QoQ.** SAVE→RAP waves launched Jul 1 on schedule and the notice window **COMPRESSED ~3 months** (all notices by Dec 31 2026, not Mar 2027). **AFT v. MOHELA is STAYED by court order** — discovery frozen since Oct 2025; the litigation leg of CRL-14 cannot fire in its own window.

> **Data vintage:** dashboard refreshed 2026-07-25 from primary sources (FSA GENERAL-26-38, NY Fed Q1 HHDC, D.D.C. docket 1:24-cv-02460, CFPB complaint API, MOHELA/Nelnet servicer FAQs). Prior file was a Jun-9 snapshot carrying five passed-but-unverified events; all now resolved or re-dated below. Live parent context → CARL `STATUS.md` (**2026-07-31 — CURRENT. CARL closed out later the same day and adopted all five 7/25 packets plus the 7/31 *Sweet* finding; CRL-14 is now 55% + STUCK. Nothing owed in either direction** — see ROUTED TO PARENT).
>
> **2026-07-31 SWEEP RESULT — read this before the tables.** A full news/data sweep across all eight STUE lanes returned **no threshold-moving data in the 7/25→7/31 window**, **but recovered one event STUE MISSED in its own 7/25 refresh: the *Sweet* 9th Cir appeal was DECIDED Fri 7/17 (DOE lost, unanimous, >170K post-class applicants) — 8 days before that session, and it sat one search away throughout it.** The Borrower Defense row and the ~Sep-15 catalyst were both wrong until now. Second finding: the Q2 HHDC has a **4-year base rate making Tue Aug 4 the modal print**, with the media advisory **due today or within days** — the single highest-value check available this week. Lanes that returned nothing: FSA (no update since 6/23, next ~Sep), SAVE→RAP (compression re-corroborated), servicers (no new event), Treasury Phase 1 (still unconfirmed, 8/5 stands), AWG/TOP (still "fall," no ED commitment → **STUCK holds**), AFT/MOHELA (Doc 54 still not public). **CFPB complaints deliberately NOT re-pulled** — the registered instrument sets ~Aug 20, past the 5-6d lag; pulling now would read the trailing week as settled, which the instrument exists to prevent. Both new findings routed to CARL (packet + `SV-STUE-2026-07-31-01`). *(Original coherence-pass note follows.)*
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

---

### ⚑ WHY THE DOWNSTREAM LOOKS QUIET — the four-channel decomposition (added 2026-07-31, Will's framing)

**The upstream is loud and the aggregate consumer-credit prints have not broken.** That gap is real, and the standing question is whether downstream consequences are *"not firing yet."* **"Yet" is right for only one of four channels** — and treating the other three as pending is how a thesis stays alive without evidence.

| Channel | Why it isn't visible | Is "yet" the right word? |
|---|---|---|
| **Forbearance → default conversion** (8.4M / ~$485B still parked) | **Genuine timing.** Transition launched Jul 1; default is a **270-day** event (+360d to DRG transfer) ⇒ **earliest possible ~Jul 2027** | ✅ **YES — real lag. Keep waiting.** |
| **Enforcement** (AWG + Treasury Offset) | **Switched off by policy** — paused Jan 16 2026, indefinitely, no ED commitment | ❌ **NO — blocked, not pending** |
| **Servicer attribution** (AFT v. MOHELA) | **Settlement stay**; discovery frozen 10/27/25; class cert never filed. A settlement **forecloses** the record | ❌ **NO — and measurability gets WORSE, not better** |
| **Credit-card cascade** | **Arithmetically too small.** Cohort holds **~2% of US card balances**; closes **≤⅓** of the gap | ❌ **NO — it was never going to carry it** |

⚠️ **And the premise needs one correction: a downstream consequence IS firing — into a series STUE was not reading.** See **§ CHANNEL 5 — FHA/MORTGAGE** below. "Nothing downstream is firing" was partly **the wrong instrument pointed at the wrong series.**

**The live discriminator is the Q2 HHDC (~Aug 4).** Q2 issuer prints (SYF/ALLY/COF/AXP) all improved — 0 of 4 confirming. Either the consumer is healing, **or** issuer books are survivor-biased by construction (worst borrowers already charged off). **The HHDC is bureau-wide and therefore cannot be survivor-filtered** — it is the test, not another datapoint. **If it prints benign too, the survivor-bias defence has been offered twice and refuted twice**, and CARL's pre-registered falsifiers bite.

---

What the 7/25 session changed is **not the mechanism but the enforcement and attribution legs**:

1. **Enforcement is gated in two independent places.** Involuntary collections remain **paused indefinitely** (Jan 16 2026, no corroborated restart), and the accountability channel — AFT v. MOHELA — is under a **court-ordered stay with discovery frozen**, with no class-certification motion filed. Neither can produce a Q3-Q4 2026 event. CRL-14's "MOHELA-caused defaults" leg therefore rests on **operational failure**, not litigation or garnishment.
2. **Attribution is narrower than STUE previously asserted.** The score cascade is real and severe *within* the affected cohort but is **second-order in aggregate** — it cannot carry a CC 90+ GFC breach on its own (DEWEY C2). Carrying the broad version into the 8/15 print would contaminate the CRL-05 grade.
3. **The transition timeline tightened.** Notices complete Dec 2026 (was Mar 2027); final selection deadlines ~Mar 2027. The **first-tranche read is still ~Oct 1**, but the full-population N now lands **earlier and more compactly** — which *improves* CRL-13's readability at Q1 2027.

**v2.5.1 thesis intact. No CRL threshold moves this session — the graders are the NY Fed Q2 HHDC (window **8/4–8/11**, date unannounced) and ~Oct 1 (CRL-13 first tranche).**

> ⚠️ **HHDC DATE CORRECTION 2026-07-31.** Every "8/15" below is **wrong — Aug 15 2026 is a SATURDAY.** Read "8/15" in the un-rewritten passages below as "the Q2 HHDC print." **SHARPENED 7/31 PM with a 4-year base rate** — the window from [PROME→CARL 7/25] was right but wider than it needs to be:
>
> | Q2 report | Released | Which Tuesday of August |
> |---|---|---|
> | 2022 | Tue **Aug 2** | 1st |
> | 2023 | Tue **Aug 8** | 2nd |
> | 2024 | Tue **Aug 6** | 1st |
> | 2025 | Tue **Aug 5** | 1st |
>
> **Every Q2 HHDC for four years has printed on the 1st or 2nd Tuesday of August at 11:00 ET, with a background press call at 9:30 ET. Three of four were the FIRST Tuesday.** August 2026's Tuesdays are **4 · 11 · 18 · 25** ⇒ **modal estimate Tue Aug 4, fallback Tue Aug 11.** (Q1-2026 also printed on a Tuesday, 5/12.)
>
> 🔴 **THE ADVISORY IS DUE RIGHT NOW.** The Q2-2025 advisory posted **Jul 31 2025 — T-5** (`newyorkfed.org/newsevents/mediaadvisory/2025/0731-2025`); the Q1-2026 advisory posted 5/5 for a 5/12 print — **T-7**. **Today is Jul 31 2026 — one year to the day from the Q2-2025 advisory.** Expect it today or within days: watch `newyorkfed.org/newsevents/mediaadvisory/2026/`. ⚠️ *WebFetch gets **403** from newyorkfed.org — the advisories have been reachable via web search, not direct fetch.*
>
> **Consequence: the grading window may open ~4 days from now**, up to 11 days earlier than the retired 8/15 anchor — which compresses the cascade-attribution packet's deadline to almost nothing.

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
| Score drop from SL delinquency | **−62 pts = the canonical average** (FICO primary). ⚠️ **FIVE other figures exist and measure DIFFERENT COHORTS — see § SCORE-DROP RECONCILIATION before citing any of them** | H2 2025 | FICO Spring 2026 | 🔴🔴 |

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
| **9th Cir appeal (26-1136) — ✅ DECIDED Fri Jul 17 2026, DOE LOST, UNANIMOUS** | **STUE MISSED THIS IN THE 7/25 REFRESH — it fired 8 days before that session.** Panel **Wardlaw / Owens / Bress** unanimously rejected DOE's appeal to delay relief for **>170,000 post-class applicants**, affirming the district court: DOE **failed to show the "changed circumstances"** legally required to modify a settlement it signed in 2022, and "knew exactly what it was signing up for." Prior STATUS carried *"no oral argument scheduled, ~Sept projected, watch-only"* — the court ruled without one. Briefing had completed **May 7 2026** *(also corrected 7/31 from a "2025" year typo)*. Earlier published order **3/25/26** denied DOE's stay bid; this is the merits loss. | 🟢🔴 **RESOLVED — DOE lost** |
| — scale, disaggregated | **>500K** borrowers / **≥$23B** = the **whole 2022 settlement** · **~200K** = original settlement class · **>170K (DOE knew of >205K by Feb 2023)** = **post-class applicants, the cohort THIS ruling covers** · **>210K** = a *separate* borrower-defense backlog · **>1,000** class members still awaiting relief already owed. ⚠️ **Headlines say "500,000" — that is the settlement total, NOT this ruling's cohort. Do not cite 500K as the 7/17 number.** | ⚠️ figure-conflation trap |
| — what's left | **DOE has not said whether it will appeal; the only remaining stop is SCOTUS (cert, discretionary).** No stay in place → **automatic discharges are proceeding.** Relief within 1yr of notice. | 🟡 residual tail |
| — ⚠️ date-conflict note | Forbes 7/21 (Minsky) dates the ruling **"Friday, July 18"** — **July 18 2026 is a SATURDAY.** PPSL (7/23 release) and The College Investor both say **July 17**, which **is** a Friday. **7/17 is correct**; the weekday check broke the tie. *(Second time in two sessions the same `date` check caught a bad date — see the 8/15 HHDC catch.)* | 🔧 |

### Collections Status
| Metric | Value | Status |
|--------|-------|--------|
| Involuntary collections (AWG + Treasury Offset) | **PAUSED since Jan 16 2026, indefinitely. NO corroborated restart date.** | 🟡 **STUCK** |
| Reported expectation | "Late summer or fall," *after* each borrower's 90-day window closes — no ED commitment | 🟠 |
| Borrowers exposed | 5M+ in default at pause; ~9M now | 🔴 |

> **Corrected 7/25:** the prior "Expected Restart **Jul 2026** 🔴 IMMINENT" row was wrong and contradicted the parent. July passed with no restart. Threshold **STUCK**, mechanism (default accrual) **intact** — matches parent CRL-14 split.

---

## TRANSMISSION TO CARL — RE-SCOPED (DEWEY C2, 2026-07-24)

### 📐 SCORE-DROP RECONCILIATION (added 2026-07-31) — six figures, one concept, **they do not conflict**

A grep found **six** different "score drop from student-loan delinquency" figures across STUE and CARL. **They are not competing estimates of one quantity — they measure different cohorts over different windows.** Nothing said so, which made them read as contradictory. **This is load-bearing:** the entire cascade rests on "each ~50pt band drop doubles the 90+ rate," so *which* drop, for *whom*, IS the mechanism.

| Drop | Cohort measured | Window | Source | Standing |
|---|---|---|---|---|
| **−62 pts** | **Average borrower with a NEW SL delinquency** | H2 2025 | **FICO Spring 2026 (primary)** | ✅ **CANONICAL — cite this one by default** |
| −69 pts | same as above | H2 2025 | derivative cites of the same FICO doc | ⚠️ **Do not cite — it is the −62 figure, restated wrong** |
| −57 pts | Borrowers with delinquent SLs, **nationally-representative credit panel** | first 3 qtrs 2025 | TCF/Protect Borrowers, pub **Feb 20 2026** | ✅ valid, **different panel + window** — not a rival to −62 |
| −91 pts | **Defaulters** (not merely delinquent) | Q1 2026 | via DEWEY 7/24 | ✅ valid — **a worse cohort, so a bigger drop.** CARL-side |
| −100 pts | **Near-prime** (~2M borrowers) | H2 2025 | FICO | ✅ valid — **cohort-specific**, in TIMELINE.tsv |
| **−171 pts** | ⚠️ **NOT a cohort figure — it is the TOP of a −87 to −171 RANGE** (760+ → 590) | **Mar 2025** | **NY Fed Liberty Street Mar 2025** (per `CASCADE.tsv` Stage 4) | 🟠 **sourced, but see below** |

**The pattern is monotone and it is the mechanism, not noise:** the better the starting score, the further there is to fall — superprime-end **−171** > near-prime **−100** > defaulters **−91** > average **−62**. **A spread of figures here is EXPECTED. What was wrong was presenting them unlabelled.**

⚠️ **The −171 defect is narrower and more specific than "unsourced" — I checked and my first read of it was wrong.** `CASCADE.tsv` Stage 4 carries it correctly as **"−87 to −171 pts, 760+→590"** attributed to **NY Fed Liberty Street Economics, Mar 2025**. The figure is sourced. **The actual defects are two:**
1. **Range collapse.** `CLAUDE.md` states it as *"Superprime borrowers losing −171 pts when payments resume"* — **a single point estimate for a named cohort, when the source gives a −87 to −171 BAND.** The file quotes the worst end as if it were the finding.
2. **Vintage.** The source is **Mar 2025 — ~16 months old**, predating the on-ramp expiry, the Q1-2026 default surge, and every FICO/TCF figure above it in this table. It is the **oldest** number in the set and the **largest**.

**Rule: cite the band (−87 to −171) with its Mar-2025 vintage, or cite −62 (FICO, H2 2025). Never the bare −171.** *(Logged against myself: this session's first pass called it "unsourced, never re-verified" and would have retired a real, attributable NY Fed figure. **Verify the number that makes you retract as hard as the one that makes you commit.**)*

---

**What survives (durable, keep asserting):**
- Each ~50pt FICO band drop ≈ **doubles** the 90+ incidence rate [FICO Credit Insights 2025]. ⚠️ **Pair this with the reconciliation table above** — the band that applies depends on the cohort's *starting* score.
- SL-delinquent borrowers' own CC 90+ rate rose **1.03% → 5.96%** (Dec'24→Jun'25) [TransUnion 2025-07]; **56%** of newly-defaulted SL borrowers with a card are already past due on it [NY Fed 2026-05].
- Transmission runs **score drop → issuer line cut (median ~75% of line) → utilization 89–94% → further score damage → denial/repricing** [CFPB CLD 2022].
- Payment hierarchy (Auto > Mortgage > Student > CC) and the $1.5–2.0B/mo spending diversion.

**What does NOT survive — stop asserting:**
- ❌ "The student-loan cascade drives the CC 90+ GFC breach." SL-delinquent borrowers hold **~2% of US CC balances (~$25B)**; the cascade contributes **~0.12–0.19pp of the 0.62pp gap ≤ ⅓**. Closing the gap from this cohort alone would require ~28% of its entire card balance rolling 90+.
- ❌ Treating a CC 90+ breach as fresh systemic consumer stress. **~62% of the Q1 rise was denominator shrink** (CC balances fell $25B), possibly seasonal and possibly reversing in Q2–Q3.
- ⚠️ The line-cut channel is real but **issuer-driven**: **67% of CLDs had no cardholder delinquency**. STUE's "3–5M CC cascade population" (CASCADE Stage 5a) is likely **overstated**.

---

### 🔴 CHANNEL 5 — FHA / MORTGAGE: the bridge STUE was not carrying (added 2026-07-31)

> **This is a RECEIVED channel, not a STUE finding.** Evidence is CARL/DEWEY's (`AGENTS/DEWEY/output/2026-07-24_fha-va-loss-waterfall.md`). It is recorded here because **STUE's transmission section had ZERO FHA mentions** while being 100% credit-card — i.e. STUE was documenting the channel that is **second-order** and silent on the one that appears to be **live**. Do not let it become load-bearing before it earns it.

| Datum | Value | Source |
|---|---|---|
| FHA total DQ | **11.88%** — highest since Q2-2021, **+126bps YoY** | MBA NDS Q1-2026 |
| FHA serious DQ | **+212bps YoY**; foreclosure inventory highest since Q4-2018 | MBA NDS |
| FHA-vs-conventional spread | **~900bps** | MBA NDS |
| Student-debt concentration in FHA | **~30% of FHA borrowers carry student debt** — >10pp above non-FHA | DEWEY 7/24 |
| Relative risk | SL-delinquent borrowers **~4× more likely** to be mortgage-delinquent | DEWEY 7/24 |

**Why it is mechanically plausible where the CC cascade was not:** the CC channel fails on **balance weight** (~2% of card balances — the cohort is too small to move a national series). FHA fails no such test: student-debt-carrying borrowers are **over-concentrated** in the FHA book, so the same cohort is a **large share of the denominator** rather than a trivial one. **Same cohort, different denominator — that is the whole difference.**

⚠️ **Caveats, carried verbatim rather than smoothed:**
- **Aggregate-corroborated, NOT FHA-isolated-proven.** Nobody has shown the FHA DQ rise is student-loan-*caused* rather than co-moving.
- **A confound of similar size sits in the same series:** the **VASP termination gap** — VA's foreclosure-avoidance program ended 5/1/25, its replacement (PCP) didn't open until 6/15/26 = a **~13-14 month backstop gap** (>10K veterans lost homes, ~90K seriously past due). **Do not attribute the whole move to student loans.**
- **Urban Institute reads the same data as "back to 2017-18 levels"**, with the thin-equity framing only partly supported (95%+ LTV FHA share actually *declined*).

**Consequence for the CASCADE ladder:** Stage 6 (mortgage) is modelled as **Apr–Dec 2027, 0.5–1M, +0.1–0.3pp — a projection.** The FHA data suggests it may already be **underway**, ~9-18 months earlier than the ladder says. **That is a re-dating question STUE cannot settle alone** — it needs the isolation test above. Logged as open question #11, **not** applied to the ladder.

---

**Why this matters before the Q2 HHDC (window opens 8/4, NOT 8/15 — see the date correction above):** if STUE carries the broad cascade claim into the NY Fed Q2 print that grades **CRL-05**, a headline breach gets mis-attributed to a mechanism that arithmetically cannot carry it — contaminating the grade. **Expect the breach; do not attribute it to us.** ⚠️ **The 7/31 date correction moves this deadline up to 11 days earlier**, and the packet carrying it has sat unprocessed in CARL's inbox for 6 days — this is the tightest clock STUE owns.

---

## CATALYSTS (re-dated 2026-07-25)

| Date | Event | Impact |
|------|-------|--------|
| **Aug 5** (Wed) | **Treasury Phase 1 first-batch verification** (parent docket) | Did ~500K defaulted accounts actually transfer? Custody ≠ enforcement |
| **Tue Aug 4 (modal) — else Tue Aug 11** | **🔴 NY Fed Q2 2026 HHDC — THE BIG ONE. Date still UNANNOUNCED but the cadence is tight.** | CRL-04 2nd print (does 10.3% sustain?); **CRL-05 breach window**; tests DEWEY's denominator-reversal call |
| **NOW – ~Aug 4** | **🔴 NY Fed media advisory — WATCH DAILY, it is due** | See the base rate below. **This is the single highest-value check STUE can run this week** |
| **~Sep** | FSA Data Center Q2 update (~quarterly cadence) | Default stock 2nd print; settles the 9.0M vs 9.5M press gap; refreshes the stale 18.6% active-repayment DQ |
| **Sep 30 2026** | RAP auto-pay enrollment deadline — **1% interest-rate reduction through Jun 30 2028** for borrowers enrolled in auto-pay by this date [ED] | 🆕 *added 7/31.* Marginally **relieving** on payment burden; a partial offset to the $0→~$407/mo shock. Small, but it is the only easing mechanism in the transition |
| ~~**~Sep 15** — 9th Cir *Sweet* oral argument~~ | ~~unscheduled, projected~~ | ⛔ **PRUNED 7/31 — never happened and never will. The appeal was DECIDED 7/17/26 without oral argument.** Row was carried on a projection that the event had already overtaken |
| **~Sep 29 – Oct 1** | **SAVE→RAP first-tranche non-selection read** | **CRL-13 partial N.** First-wave only — NOT the full 7.5M |
| **Oct** | MOHELA notice waves complete (per MOHELA FAQ) | MOHELA cohort fully noticed; complaint/failure tell should be legible |
| **Dec 31 2026** | **All SAVE notices issued (COMPRESSED from Mar 2027)** | Every borrower's 90-day clock started |
| **~Mar 2027** | Last selection deadlines → final auto-enrollments | **CRL-13 full population** |
| **Q3–Q4 2026** | Post-transition DQ wave (**CRL-14 window**) | Now rests on **operational failure only** — litigation + garnishment legs both gated |
| **TBD — event-driven** | AFT v. MOHELA stay lifts → joint status report → schedule | No date; watch docket 1:24-cv-02460 |

---

## ROUTED TO PARENT — ✅ **ALL ADOPTED** (closed 2026-07-31 PM)

> **CARL closed out on 7/31 and integrated everything. Nothing is owed in either direction.** Verified against the parent's committed files, not against a claim of processing:
>
> | Routed item | Parent state now |
> |---|---|
> | CRL-14 re-mark | ✅ **55% + Status STUCK** in `PREDICTIONS.tsv` |
> | "May 28 conference" retraction | ✅ CARL STATUS now carries the **retraction**, incl. the sharper form — *"absence of news is non-information" was affirmatively WRONG: the silence is a COURT ORDER* |
> | Cascade attribution narrowing | ✅ landed **before** the HHDC — the deadline held |
> | CRL-13 timing (Dec 31 2026) | ✅ adopted |
> | `TEAM.md` restamp | ✅ |
> | *Sweet* 9th Cir DECIDED 7/17 (sent today) | ✅ **already in CARL STATUS** the same day |
>
> 🔎 **The tripwire earned its keep, and so did the qualifier.** This section spent part of today reading **"DELIVERED, NOT ADOPTED — 6d lag"**, which was true *at that read*. It was then qualified on the observation that `AGENTS/CARL/` had **dirty paths at 16:44** — i.e. **a dirty path means in-flight, not orphaned**, and the 7/24 stamp was what a live session looks like *before* its closeout write-back. **That qualifier was correct and the un-qualified version would have been unfair.** Keep both moves: **check adoption against the parent's files** (boot step 2b), **and check whether the parent is mid-session before reading a stale stamp as neglect.**

| Item | Ask | Status |
|---|---|---|
| **CRL-14: 65% → 55% + Status OPEN → STUCK** *(Will-approved 7/25; supersedes a withdrawn 10% proposal)* | Confidence cut is **only the ~10pt genuine update** (wave-1 no-spike + the ~1.3M/qtr cure channel). The **window** defect (default = 270-day event, DRG transfer 360d ⇒ a Jul-1-transition-caused default cannot exist before ~**Jul 2027**, 3 quarters past the row's window) and the **instrument** defect (no published series attributes defaults to a servicer; the litigation that would have is **stayed**) are booked as **STUCK, not as confidence**. **Mechanism INTACT.** | 📤 packet sent (corrected) |
| CRL-14 — retract "May 28 conf" clause | No May 28 entry exists on the docket; also fix CARL STATUS L24 "absence of news is non-information" | 📤 sent |
| Cascade attribution narrowing | Must land **before the Q2 HHDC — window opens 8/4**, not 8/15 (7/31 correction: deadline is up to 11d tighter than written) or CRL-05's grade is contaminated | 📤 sent · **unprocessed 6d — the tightest clock of the five** |
| CRL-13 timing | Notices complete **Dec 31 2026** (not Mar 2027); Oct-1 first-tranche framing unchanged | 📤 sent |
| `TEAM.md` L15 restamp | STUE refresh gate fired 7/15, discharged this session — parent-owned file | 📤 sent |
| **🆕 *Sweet* 9th Cir 26-1136 DECIDED 7/17 — DOE lost, unanimous** | CARL STATUS L22 still reads *"no docket movement since Jun 9, ~Sept hearing projected"*. **Correct to: decided, no oral argument ever held, >170K post-class applicants, SCOTUS-cert-only tail.** ⚠️ Do not cite the "500,000" headline as this ruling's cohort. **STUE missed this in its own 7/25 refresh — the event predates that session by 8 days** | 📤 **sent 7/31** |
| **🆕 Q2 HHDC modal date = Tue Aug 4** | 4-year base rate (1st/2nd Tuesday of August; 3 of 4 = first). **Advisory due now** (T-5 to T-7; Q2-2025's posted 7/31/25). Bears on the frozen grading card + RED's pre-registered test — **and compresses the cascade-attribution deadline from 8/15 to possibly 8/4** | 📤 **sent 7/31** |

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
8. **Which Tuesday does the Q2 HHDC land on — Aug 4 or Aug 11?** Base rate says 4 (3 of 4 prior Q2s = first Tuesday) but no advisory had posted as of 7/31. **Resolves itself within days**; check `newyorkfed.org/newsevents/mediaadvisory/2026/` daily. *The answer sets the deadline on the un-processed cascade-attribution packet.*
9. **🆕 Does DOE seek cert in *Sweet*?** The 7/17 loss leaves only a discretionary SCOTUS petition, and DOE has not said. **No stay → discharges are proceeding regardless**, so this is a tail-risk watch, not a live gate. → watch PPSL / 9th Cir docket 26-1136.
10. **🆕 Harvest the TCF/Protect Borrowers study STUE already half-cites.** *"Trump's Student Loan Delinquency Crisis, Unmasked"* (Granville, TCF + PB, **published Feb 20 2026**, nationally-representative credit panel, data = first 3 quarters of 2025) is where STUE's carried **25% DQ rate** and **13M EOY projection** come from — **but its cohort-severity and demographic cuts were never harvested**: **−57pt** avg score drop, **three-quarters of delinquent borrowers pushed into "deep subprime,"** **7.9M entered delinquency** in 3 quarters, **Black and Native borrowers ~50%** DQ, **Pell recipients 27%**. ⚠️ **NOT new** — a 5-month-old study, flagged so it is not mistaken for a July datum. The **−57pt** figure is a *third* score-drop number alongside FICO's **−62** (H2 2025) and the **−69** derivative cite: **different sources, windows and panels — reconcile before citing any of them as "the" number.** *Backlog item, not a threshold move.*
11. **🆕 🔴 Is the FHA delinquency rise student-loan-CAUSED, or co-moving?** The single highest-value open question STUE has, because it decides whether **CASCADE Stage 6 (mortgage) re-dates from Apr-Dec 2027 to ALREADY UNDERWAY** — a ~9-18 month pull-forward of the thesis's most consequential stage. **What would settle it:** an FHA-isolated cut — DQ rates for FHA borrowers *with* vs *without* student debt, same vintage, same LTV band. **The confound that must be netted out first is the VASP gap** (VA backstop absent 5/1/25 → 6/15/26), which sits in the same series and is of similar size. **Do not treat "FHA is rising and student debt is concentrated there" as causation — that is the same co-movement error that produced the over-sized CC cascade claim.** Owner: CARL/DEWEY hold the evidence; STUE holds the student-debt side. → § CHANNEL 5.
12. **🆕 Source the score-drop band properly.** Pull the **NY Fed Liberty Street Mar 2025** piece behind the **−87 to −171** figure and check whether a post-on-ramp update exists — it is the oldest and largest number in the score set and it anchors the top of the cascade. → § SCORE-DROP RECONCILIATION.

---

*Sub-agent of CARL. Parent is system of record for CRL-04/05/13/14 — STUE keeps no own predictions ledger. State vector this session: **SV-STUE-2026-07-25-01**.*
