# STUE STATUS

**Last Updated:** 2026-08-10 (inbox processing · Treasury/MOHELA verification sweep — **no threshold moved; three inbox packets applied; verdicts INCONCLUSIVE on both catalyst checks**) | **Data vintage:** 2026-07-25 core dashboard, w/ *Sweet* 9th Cir at 7/17, Treasury row re-checked 2026-08-10 (still inconclusive, new Aug-7 development logged) | **Status:** 🔴 CRITICAL — mechanism intact, enforcement gated. **CRL-04 CONFIRMED** (NY Fed Q1 2026 90+ DQ **10.3%**). **FSA primary (Jun 23) now carries the default wall: ~9M borrowers / $220B as of Mar 31 2026, +1.3M QoQ.** SAVE→RAP waves launched Jul 1 on schedule and the notice window **COMPRESSED ~3 months** (all notices by Dec 31 2026, not Mar 2027). **AFT v. MOHELA is STAYED by court order** — discovery frozen since Oct 2025. ⚠️ **CRL-14 was RETIRED 2026-07-31, superseded by CRL-28** (frozen 55/day CFPB-complaint threshold, window Oct 1 2026–Sep 30 2027); mentions of "CRL-14" below the fold are historical record of the 7/25→7/31 session that produced that retirement, not the live row — corrected fleet-wide 2026-08-10, PROME round-2 audit.

> ## 📌 SESSION CLOSEOUT 2026-08-10 — NEXT-SESSION HANDOFF (read first)
>
> **Three inbox packets processed** (CARL VASP/monotone-law hand-down 7/31; PROME round-2 audit CRL-14→CRL-28 residue 7/31; PROME U3/inbox-layer ruling 8/2) — all applied, moved to `inbox/processed/`. **Tomorrow (8/11) is the Q2 HHDC's fallback Tuesday** (modal was 8/4, which passed with no advisory found in this session's scope — not re-checked tonight, out of task scope) — **do not let a stale STATUS read as current going into that print.**
>
> **Both spawn-tasked catalyst checks came back INCONCLUSIVE, not confirmed clean:**
> - **Treasury Phase 1 (docketed 8/13):** the original "500K by July" wave is still unconfirmed at the primary level — but a **NEW Aug 7 2026 development** (Treasury "Default Resolution Hub" + vendor-partnership announcement, secondary-sourced) shifts the shape of the question. **Recommend re-scoping the 8/13 row, not pruning it** — see § Treasury Transfer.
> - **AFT v. MOHELA docket (8/14):** CourtListener returned **403 to WebFetch on every attempt** (2 docket-ID variants + a search page) — the free-RECAP route this row depends on was unreachable this session, not confirmed-quiet. Web search found no news of Doc 54's content. **Do not prune 8/14 on tonight's null** — it's an access failure, not a resolved docket. See § Servicer Performance.
>
> ## 📌 SESSION CLOSEOUT 2026-07-31 — NEXT-SESSION HANDOFF (archival, prior session)
>
> **Domain: nothing moved. Architecture: a lot did.** No threshold, no confidence, no thesis change all session. Nine defects were found and fixed — **five traced to one root cause: mutable data duplicated across files with no declared owner.**
>
> **🔴 DO THIS FIRST NEXT SESSION — the NY Fed Q2 HHDC advisory.** Base rate says **Tue Aug 4** (Q2 printed on the 1st or 2nd Tuesday of August four years running; 3 of 4 = first). The advisory posts **T-5 to T-7** and had **NOT posted** as of CARL's 7/31 evening check — so **it is overdue by pattern and may be the first thing waiting.** It sets whether CRL-05's grading window opens in days. `newyorkfed.org/newsevents/mediaadvisory/2026/` — ⚠️ **403s WebFetch; reach it via search.**
>
> **What changed structurally (all shipped + verified, nothing pending on STUE's side):**
> - **📬 STUE HAS AN INBOX** — `inbox/`, Will-ruled. **First sub-agent in the fleet that can receive.** Read at every boot **including spawned mode**; packet **age is a finding** (>~30d ⇒ tell the sender).
> - **Scope EXTENDED (Will-ruled):** **+ SLABS** (collateral-transmission question only) and **+ higher-ed institutional stress**. Both had zero fleet coverage. Fiscal read-through **declined** — no edge.
> - **Spawned-mode boot card** — this file's `CLAUDE.md` never auto-loads when CARL spawns STUE. That was the highest-value gap of the day.
> - **Doc Ownership table**, **two-clock ledger headers** (caught a 7-day freshness overstatement STUE created itself), **unrepresentable-shock register** (S1-S6), **expected-signals register** (ES-01..06), **BOTTOM LINE**.
> - **Enforcement: 44 ledgers now graded, was 7.** CARL shipped both `LEDGER_GLOB` fixes same-day and **processed all four STUE packets** — nothing owed in either direction.
>
> **Still with others (not STUE's to chase):** CARL — consistency-check sub-agent coverage (Fix B, backlogged). PROME — whether the *other six* sub-agents get inboxes, and the unowned fiscal read-through.
>
> **The lesson worth carrying:** almost everything found today was findable with `date`, arithmetic, or `ls`. **No new information was required — only the decision to look.** Both structural gaps had the same shape: **two individually-correct decisions combining into a blind spot, failing as silence rather than as error.**
>
> ---
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
| **Total portfolio (THE DENOMINATOR — S3 check)** | **42.6M recipients / $1.7T, GROWING +~4% YoY** vs Mar 2025 | Mar 31 2026 | FSA GENERAL-26-38 | ✅ **DENOMINATOR CHECK PASSES** |
| ↳ *what that rules out* | **The default-stock rise is NOT a denominator artifact.** The base is **expanding**, so 7.7M→9.0M is a genuine numerator move — if anything the *rate* understates it. **Run this check every FSA print** (register S3): a shrinking base would inflate every rate STUE cites with zero change in borrower behaviour, and ~62% of the Q1 CC 90+ rise was exactly that | Mar 31 2026 | STUE derived | 🟢 |
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
| — ⚠️ Implication for attribution | A settlement typically means **no admission of liability, no public discovery record, no class cert** ⇒ the likeliest path **forecloses** the servicer-attributed default evidence CRL-28's instrument needs (attribution question is unchanged by the CRL-14→CRL-28 retire+replace). Measurability gets *worse*, not better. | 🔴 |
| 🆕 **2026-08-10 free-check attempt (Will declined the PACER $0.30 buy, per 7/31)** | **NO CHANGE FOUND — but ⚠️ this is a blocked-mirror result, not a confirmed-quiet docket.** `courtlistener.com` returned **HTTP 403 to WebFetch on 3 separate URL attempts** (two docket-ID variants + a search-results page) — the exact free-RECAP-text route this row's docket asks for was unreachable this session. Web search surfaced **no news of Doc 54's content, a settlement, or any post-7/17 filing** — but a null search result is weaker evidence than a blocked primary being reachable-but-silent. **Doc 54 remains the only unknown; status unchanged (STAYED, settlement negotiation, last confirmed filing 7/17).** Do not read tonight's null as "confirmed still stayed" — it's "couldn't check the primary, and secondary is silent too." | ⚠️ **inconclusive — try RECAP via a different route next session** |
| Maldonado v. MOHELA | Mar 2026 — violated CA Student Borrower BoR + UCL | 🔴🔴 precedent stands |
| Settlement | NONE | — |

### Treasury Transfer
| Metric | Value | Status |
|--------|-------|--------|
| Phase 1 scope | **~500K defaulted accounts** = launch wave, NOT all ~9M; ramps gradually via Fiscal Service CSP [CRS R48962] | 🟠 |
| Phase 1 execution — "500K by July" wave | **STILL NO launch-day primary located.** Secondary reporting (Forbes 4/22, College Investor, Yahoo) uniformly frames it as "expected by July" / future tense — none pins a completed-transfer date. **INCONCLUSIVE, not confirmed either way**, as of this check. | 🟠 **re-verified 2026-08-10, still open** |
| 🆕 **Aug 7 2026 — Treasury announced NEW steps (not the July wave's confirmation)** | Yahoo News (dated Fri 8/7/26; via search) + corroborating secondary coverage: Treasury unveiled a **"Default Resolution Hub"** — centralized borrower point-of-contact — and is **"seeking to partner with vendors"** for collections/rehab support. Language is **prospective** ("moving forward," "new plans"), describing **infrastructure build-out that PRECEDES actual collections activity**, not evidence the July batch already moved. [Yahoo News 2026-08-07, via WebSearch — primary Treasury.gov release not located; WebFetch 403s courtlistener.com AND could not confirm a distinct treasury.gov press release URL] | 🟠 **NEW — changes the shape of the 8/13 verification, does not resolve it** |
| Nature of handoff | **Servicing/collections CUSTODY — not enforcement resumption.** Do not conflate. | ⚠️ |
| Phase 2 / Phase 3 | Planned, no public dates | 🟡 |
| Legal authority | Disputed; GOP bill introduced to codify the transfer | 🔴 |

> ⚠️ **2026-08-10 verdict on Phase 1 launch: INCONCLUSIVE.** Free web search found no primary confirming the ~500K account wave actually transferred/borrowers were contacted in July as originally framed. **But the question itself may now be the wrong one to close on 8/13**: the Aug 7 "Default Resolution Hub" + vendor-partnership announcement suggests Treasury's own framing has shifted from a discrete "500K by July" batch toward an ongoing operational build-out — a July yes/no answer may never surface cleanly. **Recommend CARL do NOT prune the 8/13 row outright; re-scope it** to "has the Default Resolution Hub gone live / have vendor partnerships been named?" rather than continuing to chase the original July figure. AWG/TOP involuntary collections still show no restart signal in this sweep — custody-build-out ≠ enforcement, unchanged.

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

⚠️ **CORRECTED 2026-08-10 (PROME audit item 2, CARL hand-down — inbox packet processed): the "monotone law" claim below is WRONG and is struck.** The **−91** defaulter figure reflects a **worse-cohort mechanism** (defaulters vs. merely-delinquent) — the *opposite* axis from "better starting score falls further" — and **−57** was omitted from the ordering entirely. **These are not points on one monotone scale.** The table above is correct; read each row's own cohort/window on its own terms and do not construct a cross-cohort ranking from them. **A spread of figures here is EXPECTED. What was wrong was presenting them unlabelled** — but the generalization that followed compounded the error rather than fixing it.

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
- ⚠️ **CORRECTED 2026-08-10 (CARL hand-down, PROME audit item 1 — inbox packet processed) — struck, was a CATEGORY ERROR.** The prior claim that the VASP termination gap is "a confound of similar size in the same series" was wrong on **both halves**, at its own cited source (DEWEY `2026-07-24_fha-va-loss-waterfall.md`): the **11.88%** figure is **FHA-only** MBA NDS (the ~900bps FHA-vs-conventional spread is only computable if so), while **VASP is a VA program** — different series, not an in-series confound at all. And the VA leg is **much milder**, not similar size: DEWEY `:69` — PFSI VA 60+ **1.7%** vs FHA **8.0%**. **Candidate REAL in-series confound:** HUD ML 2025-06 mandatory partial-claim waterfall (defers loss as an MMI receivable — genuinely distorts the FHA series). Data hook: HUD FHA Neighborhood Watch geographic cut (DEWEY `:89` items 3-4, scoped, never pulled — coordinate with HOMER).
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
| **Q3–Q4 2026** | Post-transition DQ wave (**CRL-28 window opens Oct 1** — CRL-14's successor, retired+replaced 7/31) | Now rests on **operational failure only** — litigation + garnishment legs both gated |
| **TBD — event-driven** | AFT v. MOHELA stay lifts → joint status report → schedule | No date; watch docket 1:24-cv-02460 |

---

## ROUTED TO PARENT — ✅ **ALL ADOPTED** (closed 2026-07-31 PM)

> ⚠️ **Post-dated 2026-08-10:** the CRL-14 row below is now doubly-superseded — adopted as 55%+STUCK on 7/25, then **RETIRED and replaced by CRL-28** later the same evening (7/31, Will-ruled opt-a "yes register"). The table is left as the historical record of the 7/25 exchange; do not read "✅ 55% + Status STUCK" as CRL-14's current state — CRL-14 no longer has a current state, CRL-28 does (frozen 55/day, window Oct 1 2026–Sep 30 2027).
>
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

## 🕳️ UNREPRESENTABLE-SHOCK REGISTER (added 2026-07-31 — DAEDALUS blueprint §6b.2, the "★" test)

**The test:** *"Name a shock in this domain that NONE of the seeded rows has a row-shape for."*
**Why it is the strongest check in the blueprint:** *a file with no row-shape for a class of event is silent about it in a way **indistinguishable from that event not happening** — so "that belongs to another agent" and "I am blind to it" look identical from outside, and only one is safe.*

**This test predicted today's FHA defect exactly.** STUE had `0/0/0` FHA mentions; nothing in the file could tell blindness from scope. Run properly, it finds **six** more — and **three of them have no owner anywhere in the fleet.**

### SEEDED — in scope, STUE is the right owner, row-shape now exists

| # | Shock with no row-shape | Why it matters | Watch instrument |
|---|---|---|---|
| **S1** | **🔴 Mass forgiveness / broad cancellation / policy reversal** | **The single fastest way this thesis DIES**, and STUE tracked it nowhere. Sweet is bounded (~170K); this is the unbounded version — a new administration, a court, or Congress discharging at scale. **A bear thesis with no surface for its own kill-shot is not a thesis, it is a position.** *(CRL-04's invalidation criterion names "broader forgiveness" — but naming a risk in an invalidation clause is not tracking it.)* | ED/White House announcements · reconciliation-bill text · any successor to the SAVE litigation. **Direction: UPSIDE for borrowers, FATAL for the thesis** |
| **S2** | **Servicer contract LOSS / transition** (≠ servicer failure) | STUE tracks MOHELA *failing*. It has no shape for MOHELA *exiting, being replaced, or losing its contract* — and **a servicer transition is itself a mass-DQ event** (the 2023-24 transitions proved it). Would fire *through* CRL-14's population without touching its stated mechanism | FSA servicer contract awards/terminations · ED announcements |
| **S3** | **Denominator shock — origination / enrollment collapse** | ⚠️ **This is the CRL-09 failure class inside STUE's own domain.** Every headline STUE cites is a RATE. If the portfolio shrinks (fewer originations, enrollment decline), **DQ rates rise with zero change in borrower behaviour** — and STUE would read it as deterioration. **We already got burned by exactly this once** (~62% of the Q1 CC 90+ rise was denominator shrink) | FSA quarterly *originations* + total-portfolio recipient count — **STUE already receives both and was only reading the numerator** |
| **S4** | **Publisher / methodology shock** | STUE depends on ~4 publishers (FSA, NY Fed, CFPB, court dockets). **NY Fed already changed methodology once** (Equifax 3.0 → VantageScore 4.0, and it took a session to establish the headline rate was unaffected). A publisher ceasing, delaying, or restating is an **instrument** failure that looks like a **world** change | Release-cadence slips · methodology notes in each release · **treat a missing release as a signal, not as silence** |

### EXCLUDED — out of scope, owner named and verified

| Domain | Owner |
|---|---|
| Overall consumer stress / K-shape synthesis | **CARL** |
| Bank & lender exposure | **REGINALD** |
| Housing / mortgage market as an asset market | **HOMER** *(the FHA channel reaches STUE as received evidence only — § CHANNEL 5)* |
| Employment | **LABOR** |

### ✅ ABSORBED — Will-ruled 2026-07-31: STUE takes two of the three unowned domains

**Both had ZERO fleet coverage.** Seeded as watch-rows — a row-shape, not a build.

| # | Now owned | Row-shape / instrument | Registered prior |
|---|---|---|---|
| **S5** | **Student-loan ABS / SLABS — the COLLATERAL question** | FFELP trusts (Navient, Nelnet) + private SL trusts (SLM, Navient private, College Ave, Earnest). Watch: **CNL · 90+ DQ · forbearance % · parity ratio · tranche CE · rating actions · spreads.** Sources: trustee/servicer reports, EDGAR ABS-EE / 10-D filings, rating-agency actions | ⚠️ **TRANSMISSION IS PROBABLY WEAK — register this BEFORE looking, so a null result is a finding and not a disappointment.** FFELP carries a **~97% federal guarantee** ⇒ its risk is **extension / prepay / liquidity, NOT credit.** Private SLABS sit on a **different, largely cosigned, better-credit pool** — not the ~9M defaulted cohort. **"9M in default ⇒ SLABS blow up" is the naive read and it is likely WRONG.** The value is in *settling* that, not assuming it |
| **S6** | **Higher-ed institutional stress** | College closures · enrollment (IPEDS/NSC) · **Title IV heightened cash monitoring** · the 150+ flagged schools | **Near-zero acquisition cost — STUE already pulls the file that carries it.** The FSA Data Center quarterly (GENERAL-26-38 class) publishes Title IV heightened-cash-monitoring institutions **alongside** the portfolio data. Feeds two rows STUE already owns: borrower-defense claim generation + the S3 origination denominator |

> **Scope guard on S5:** STUE owns the **collateral/transmission** question. **Pricing, tranche analysis and positioning route OUT** — LIQUID (structured credit) / REGINALD (lender exposure) / TERRY (construction). **If SLABS proves large, that is a DAEDALUS spinout question, not a quiet expansion.**
>
> ⚠️ **CAPACITY CONDITION, recorded as a condition and not a courtesy.** STUE is the largest sub-agent (27 files, ~1.6× the next) and was **invisible to both fleet coherence enforcers until today.** **Adding domains without adding capability is precisely how the rot this session spent a day fixing comes back.** The CARL `LEDGER_GLOB` fix is requested and should land **before** either of these grows past a watch-row.

### ✅ FORMERLY UNOWNED — declined by STUE, all now dispositioned (U1/U2 absorbed 7/31, U3 ruled 8/2)

> ⚠️ **U1 and U2 were ABSORBED by STUE on Will's 7/31 ruling — see the block above.** **U3 (below) was RULED 2026-08-02 — BOND-conditional watch-row — closing the last open row in this table.** Checked at the counterparty standard rather than assumed (`[[finding_scope_negative_needs_the_counterparty_standard]]` — *"it's absent/undefined" is the claim that stops anyone looking*). **Writing "X owns it" here would have been fiction** at the time this table was built; it no longer is.

| # | Gap | Evidence of the gap | Why it matters |
|---|---|---|---|
| **U3** | **Mass forgiveness as a fleet-level policy risk** | Only hits are **2 retired STUE archive files** + an unrelated OTTO doc | ✅ **RULED 2026-08-02 (PROME) — BOND-conditional watch-row, not unowned anymore.** BOND holds a row that activates only on STUE's S1 trigger (forgiveness happens); BOND-decline → declared blind spot either way. Fiscal/rates read-through (≥$220B of defaulted principal) is a BOND/MARCO-scale question, not STUE's |

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
11. **🆕 🔴 Is the FHA delinquency rise student-loan-CAUSED, or co-moving?** The single highest-value open question STUE has, because it decides whether **CASCADE Stage 6 (mortgage) re-dates from Apr-Dec 2027 to ALREADY UNDERWAY** — a ~9-18 month pull-forward of the thesis's most consequential stage. **What would settle it:** an FHA-isolated cut — DQ rates for FHA borrowers *with* vs *without* student debt, same vintage, same LTV band. **CORRECTED 2026-08-10: the VASP precondition was a false blocker (category error — VASP is a VA program, not an in-series FHA confound, and the VA leg is much milder, not similar size — see § CHANNEL 5 above) and is REMOVED.** The real in-series confound to net out first is **HUD ML 2025-06's mandatory partial-claim waterfall** (unpulled — HUD FHA Neighborhood Watch geographic cut). **Do not treat "FHA is rising and student debt is concentrated there" as causation — that is the same co-movement error that produced the over-sized CC cascade claim.** Owner: CARL/DEWEY hold the evidence; STUE holds the student-debt side. → § CHANNEL 5.
12. **🆕 Source the score-drop band properly.** Pull the **NY Fed Liberty Street Mar 2025** piece behind the **−87 to −171** figure and check whether a post-on-ramp update exists — it is the oldest and largest number in the score set and it anchors the top of the cascade. → § SCORE-DROP RECONCILIATION.

---

---

## BOTTOM LINE (blueprint §8 — rewrite EVERY session, plain language, no jargon)

**Where the domain is now:** The student-loan default wall is real, primary-sourced and still climbing — **~9.0M borrowers / $220B, over 13% of the federally-managed portfolio**, with **8.4M more sitting in forbearance** that has not yet converted. The upstream deterioration is not in question.

**The single most important thing:** **The downstream consequences are quieter than the upstream would predict, and that decomposes into four different situations that need opposite responses — only ONE of which is a genuine "not yet."** The forbearance conversion is truly just lagging (a Jul-1-transition default cannot exist before ~Jul 2027). Enforcement is *switched off*, not delayed. The servicer-accountability channel is *settlement-stayed and getting less measurable, not more*. And the credit-card cascade was simply **over-modelled** — that cohort holds ~2% of card balances and can never carry a national breach. Meanwhile a consequence **is** firing, into **FHA mortgages**, a series STUE was not reading until 7/31.

**What's next:** The **NY Fed Q2 HHDC — modal Tuesday Aug 4** — is not another datapoint; it is the discriminator. Q2 issuer earnings all improved (0 of 4 confirming), and the only way to tell "the consumer is healing" from "issuer books are survivor-biased" is a bureau-wide print that cannot be survivor-filtered. **If it prints benign too, the survivor-bias defence has been offered twice and refuted twice**, and the pre-registered falsifiers bite.

**What would change my mind:** a forbearance reservoir that does not drain on the ~Sep FSA print (ES-STUE-01) — that would mean the conversion is being administratively **deferred** rather than delayed, and the whole Q3-Q4 thesis slides a year. Second falsifier, cheaper and sooner: a **second** null on the MOHELA complaint tell through October (ES-STUE-02) would leave CRL-14 with **no working mechanism** rather than a stalled threshold — a STUCK→MISSED question, not a confidence trim.

*(Rewritten 2026-07-31 closeout. **Rewrite this block every session** — a carried-forward BOTTOM LINE reads as a current judgement when it is a stale one.)*

---

*Sub-agent of CARL. Parent is system of record for CRL-04/05/13/28 (CRL-14 retired 7/31, superseded by CRL-28) — STUE keeps no own predictions ledger. Latest state vector: **SV-STUE-2026-08-10-01**. Expected-signals register: `workbook/EXPECTED_SIGNALS_TRACKER.md`.*
