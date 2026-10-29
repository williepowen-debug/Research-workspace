# STUE STATUS

**Last Updated:** 2026-10-28 ~21:45 ET (**53-day dark gap closed: FSA FY2026 Q3 graded (ES-01/04/06), ES-02 boundary rule's first out-of-sample run, news sweep, 2 CARL inbox packets processed; then a file sweep, a rotation pass, and five research items — the Treasury Education collections pilot, SAVE windows, score-drop sources, AFT Doc 50, TCF — with the workbook reconciled to them**) | **Data vintage:** FSA `PortfoliobyLoanStatus` + companion files **Last-Modified Fri 18 Sep 2026** (data as of **Jun 30 2026** = FY2026 Q3; MD5 `d443da74…` matches CARL's 9/24 copy); CFPB `company=MOHELA` settled through **Oct 16 2026** (pulled 10/28, vintage 2026-10-28); Treasury release sb0639 **Sep 30 2026**; AFT v. ED docket (CourtListener) through **Oct 15 2026**; Sweet via PPSL/secondaries through **Oct 15 2026**; NY Fed 2026:Q3 HHDC **not yet posted** (data URL 302 on 10/28) | **Status:** 🔴 CRITICAL, unchanged. **No registered threshold fired.** The default stock is still rising but slowed to roughly a quarter of the prior quarter's pace, and the servicer-complaint signal stays well below its bands inside CRL-28's now-open window.

> ## 📌 SESSION 2026-10-28 — 53 DAYS DARK. THE FSA RELEASE IS GRADED, THE COMPLAINT RULE PASSED ITS FIRST OUT-OF-SAMPLE RUN, AND THE AFT v. ED DATE CARL CARRIED WAS WRONG.
>
> ⚠️ **The gap first: last STUE session 2026-09-05; the FSA file posted 9/18 and sat ungraded for 40 days.** CARL noticed and graded nothing on STUE's behalf (correct). **For the second consecutive dark period, the parent noticed the posting before STUE did.**
>
> ### ES-STUE-01 — forbearance drain, FSA FY2026 Q3 (Jun 30 2026): ⚖️ **NO VERDICT ON THE REGISTERED BASIS. It straddles the −5% Yellow edge.**
> | Basis | Q2 (Mar 31) | Q3 (Jun 30) | QoQ | vs −5% Y edge |
> |---|---:|---:|---:|---|
> | **Federally Managed recipients (REGISTERED)** | 8.4M | 8.0M | **−4.76% as printed; rounding range −3.6% to −5.9%** | **straddles; cannot settle** |
> | Federally Managed dollars | $484.6B | $459.2B | **−5.24%** | just past Y |
> | Direct Loan recipients, sum of the forbearance-type report (2 decimals) | 8.43M | 8.04M | **−4.63%** | just short of Y |
> **Composition is the finding, not the band:** *administrative* forbearance (the SAVE-litigation pool) **7.74M → 7.26M (−6.2%)**, while *discretionary* hardship forbearance **rose 0.59M → 0.65M (+10%), $34.6B → $39.5B (+14%)** [FSA `DLbyForbearanceType.xls`, LM 9/18]. **Destination changed:** last quarter both feeder pools drained into default; this quarter repayment **+0.2M**, default **+0.3M**, deferment **−0.3M**. ⚠️ **The Jun-30 snapshot predates the first SAVE notice (Jul 1)**, so the SAVE drain proper starts in the FY2026 Q4 (Sep 30) file, due ~mid/late December. SAVE enrolment was already **6.99M → 6.52M** in the quarter, with IBR **2.92M → 3.31M**, so leavers are choosing IDR plans [FSA `DLPortfoliobyRepaymentPlan.xls`].
>
> ### ES-STUE-04 — cure channel: ⛔ **NOT GRADEABLE. The gross-flow leg does not exist for this quarter.**
> **Stock leg:** Federally Managed cumulative default **9.0M / $220.3B → 9.3M / $234.1B** (+0.3M / +$13.8B, vs +1.3M / +$39.8B the prior quarter). **Gross leg:** the registered instrument is the NY Fed/Liberty Street gross DRG flow; **no calendar-Q2 figure has been published.** FSA's own entering-defaults report (`DLEnteringDefaults.xls`) is **frozen at Aug 2023**. ⚠️ **I tried a substitute and rejected it:** the 271–360-day bucket (1.10M at Dec 31) cannot explain the following quarter's +1.3M net default rise, so it **undercounts gross inflow** (FSA counts recipients at loan level) and cannot back out exits. **Cure durability (OQ#3) stays open; the slowdown in the stock cannot say whether cures rose or inflow fell.**
>
> ### ES-STUE-06 — HCM list: ⚠️ **ACCESS GAP again, not a null.** The page's `Last-Modified` moved **Jul 31 → Wed 14 Oct 2026**, so it *was* updated, but the list is still JS-rendered and no data file is linked in the HTML. **No major-chain closure found in the sweep.**
>
> ### OQ#16 — does the default count peak on schedule? **Tracking the exhaustion reading, and probably lower than the 10–11M band.**
> FSA delinquency pipeline (Federally Managed recipients, Jun 30): 31–90 days **1.18M**, 91–180 **0.86M**, 181–270 **0.77M**, **271–360 0.66M** (= the most that can default in Jul–Sep). Pre-pandemic Q3 the 271–360 bucket ran **0.30–0.37M**, so the pipeline is still ~2× normal but no longer 3×. ⚠️ **The 31–90 uptick (1.00M → 1.18M) is seasonal:** the same Q2→Q3 rise appears in 2017 (+13%) and 2018 (+57%), and the level is below every 2017–19 Q3 (1.36–1.63M). **Arithmetic: 9.3M + ≤~0.7M gross ⇒ roughly 9.5–10.0M at Sep 30**, *with the undercount caveat above*. The FY2026 Q4 file is the grade.
>
> ### ES-STUE-02 / CRL-28 — **inside the window now (opened Oct 1). 24.8/day, below Yellow. The boundary rule passed its first out-of-sample run.**
> Pre-registered completeness test on the 10/28 pull **selected D = Fri Oct 16**. The visible cliff is **Oct 18/19** (Oct 18 = 11, ratio 1.10; Oct 19 = 1, ratio 0.04). The rule stopped 2 days early because Sat Oct 17 read 0.58. **It picked a boundary inside the settled region, never past the cliff.** Clause 4(b): **24.0 / 24.8 / 22.1 per day at D−3 / D / D+3, all below Y (>35).** CRL-28 window Oct 1–16 = **396 complaints = 24.8/day**, which is **45% of the frozen 55/day**. Sep 2026 = **682 (22.7/day)** vs Sep 2025 **651** (+4.8% YoY); Oct 1–16 is +18% on Oct 2025's 21.0/day, but at a low level. ⚠️ **This is an interim in-window read, NOT the grade.** The grade is still **~Fri Nov 13 / Mon Nov 16**. The cliff now sits **~10 days** behind the pull (it was ~14 on 9/5), which confirms that a fixed lag offset is the wrong rule.
>
> ### News sweep, Sep 5 → Oct 28 (primaries where stated)
> - **Treasury/collections:** ED + Treasury launched the **Defaulted Loans Support Center on Sep 30** (rehabilitation and consolidation applications online) [Treasury release sb0639, **primary**]. **The release says nothing about revoking ED's exemption, new collector contracts, or garnishment/offset timing.** It counts **>5M borrowers in default >6 years and another 5M who defaulted in under a year.** **Involuntary collections: still PAUSED, no restart verified at any primary.** Private-collector hiring "possibly November" and collections "in 2027" are **press-reported plans only**; a MoneyWise 10/27 claim that garnishment "begins next month" conflicts with them and is unsupported. **OQ#14 custody event (exemption revocation): not observed.**
> - **SAVE→RAP:** ED added a **"final 30-day notice"** after a missed 90-day window (secondary, College Investor 10/15 and Newsweek; **StudentAid.gov page not read at primary** because it is JS-rendered and the article 403'd). **If it holds, each auto-enrolment slips ~30 days: earliest ~Oct 29, and the last deadlines move from ~end-Mar to ~end-Apr 2027**, which pushes CRL-13's full-population read with them. Notices continue roughly every two weeks through year-end. **No wave-level selection or non-selection count exists anywhere public.**
> - **AFT v. ED (D.D.C. `1:25-cv-00802`, Walton):** ⚠️ **The conference CARL carried as 10/28 was held on Wed 10/14** [CourtListener minute entry]. **Next: Mon 11/23 11:00 ET.** Doc 70 (10/15) is an order. **The last ED status report is Doc 65 (May 19); none has been filed since.** ⇒ **no post-April IDR/RAP count is public: UNAVAILABLE.** ⚠️ This case's reports cover the IDR/PSLF processing backlog, **not SAVE non-selection**, so even a new report would not directly feed CRL-13.
> - **Sweet v. McMahon:** the enforce + contempt motions (filed Aug 18) are **fully briefed** (plaintiffs' replies Oct 15); **hearing Thu Nov 5 2026** [PPSL, via search; docket not read]. No ruling yet.
> - **NY Fed 2026:Q3 HHDC:** not posted; last year's Q3 came out Wed Nov 5 2025. **Poll `HHD_C_Report_2026Q3.xlsx`.**
>
> ### 🆕 Later 10/28: five research items worked (Will-directed) → `research/README_2026-10-28_research-items.md`
> - 🔴 **Treasury built and cancelled an Education collections pilot.** Fiscal Service awarded "PCA SERVICES - EDUCATION PILOT" task orders to **5 private collectors, $8M each (May 19–29 2026)**, and **terminated all five on Jun 3 2026** [USAspending/FPDS primary]. **STUE's 9/5 "validated null" missed it** because it searched "student" and "default resolution". Collections remain paused; no custody transfer observed.
> - **SAVE notice windows settled (OQ#19):** servicer-specific; **MOHELA finished noticing by Sep 30** (primary), so its auto-enrolments run ~Oct 2026 – Jan 2027. Final notice confirmed at primary.
> - **Score-drop band sourced (OQ#12):** −87…−171 is a 2016–19 historical estimate; the observed Q1-2025 update averages ≈ −105.
> - **AFT complaint read (OQ#13):** two of three cited figures confirmed; the **7×/>50× wait ratio is not in the pleading**; the 2.5M/800K figures are **Oct 2023**, not 2025.
> - **TCF study harvested (OQ#10):** its projection is **17M in distress**, not the **13M in default** STUE attributed to it.

> 🗂️ **ROTATION INDEX** — older session blocks and closed sections live verbatim in `archive/STUE_STATUS_ARCHIVE_2026-09.md` §B1–B9 and `archive/STUE_STATUS_ARCHIVE_2026-10.md` §C1–C8 (each byte + CRC32 stamped). §C8 (7909 B, CRC32 `09bbed30`) holds the pointer stack and closed head rows collapsed into this line on 2026-10-28.

## THESIS

Federal student loan stress remains a **mass credit-destruction event in active execution**, and the *accrual* mechanism is firing exactly as modelled: the default stock went **6.0M (Aug 2025) → 7.7M (Dec) → 9.0M (Mar 2026) → 9.3M (Jun 2026)** on primary FSA data, with 2.6M gross DRG transfers in calendar Q1 alone. ⚠️ **10/28: the accrual is decelerating hard** (+1.3M then +0.3M net per quarter), consistent with the cohort-exhaustion reading on the NY Fed flow. CRL-04 is **CONFIRMED clean** at 10.3%.

---

**Mechanism status (10/28):** enforcement is still gated (AWG/TOP paused since Jan 16 2026; AFT v. MOHELA stayed in settlement talks); the CC cascade is second-order in aggregate (~2% of card balances); the level claim is contested in both directions (§ #17 ANSWERED, open question #18). v2.5.1 thesis intact. The 7/25 framing and the four-channel decomposition are in archive §C8 / §B8.

---

## SIGNAL DASHBOARD

### Delinquency / Default
| Metric | Value | As Of | Source | Status |
|--------|-------|-------|--------|--------|
| **Student Loan 90+ DQ (stock)** | **10.60% — CRL-04 holds on a 2nd consecutive >10% print** (10.34% Q1 → 10.60% Q2, +26bps) | **Q2 2026, rel Tue Aug 11** | **NY Fed HHDC 2026:Q2, Pg 12 — STUE direct pull 8/13** | 🔴🔴 |
| **Flow INTO 30+ (student)** | **7.83%** — 16.35% (Q4) → 11.03% (Q1) → **7.83%** | Q2 2026 | NY Fed HHDC Pg 13 | 🟢 **decelerating hard** |
| **Flow INTO 90+ (student)** | **7.83%** — 16.19% (Q4) → 10.86% (Q1) → **7.83%**, i.e. **more than halved in two quarters** | Q2 2026 | NY Fed HHDC Pg 14 | 🟢 **decelerating hard** |
| ↳ *the shape, and what it settles* | **Stock UP while flow COLLAPSES, two quarters running = COHORT EXHAUSTION.** On-ramp slack and seasonality are both refuted by the repetition. The newly-defaulting pool is draining; the stock is aging on reports. **This is the resolution of open question #2** — and it independently corroborates the ≤⅓ cascade cap *from the other direction*: a decaying flow cannot drive forward consumer-credit deterioration | Q2 2026 | STUE + CARL packet 8/11 | 🔧 **impulse fading, mechanism intact** |
| ⚠️ *instrument caveat on the flow series* | Pg 28 (by age, 4Q moving sum) prints **7.44%** for the same Q2 concept — the two series agreed to **±0.01pp for 5 quarters** then split **+0.39pp** in 26:Q2 alone. **Cite Pg 14's 7.83%; do not silently switch.** Register **S4** instance | Q2 2026 | STUE derived | 🟡 **watch next release** |
| **Borrowers in default (stock)** | **9.3M / $234.1B** (Federally Managed, *Cumulative in Default*), up from 9.0M / $220.3B | **Jun 30 2026** (FY2026 Q3) | FSA `PortfoliobyLoanStatus.xls` LM Fri 18 Sep 2026 (STUE pull 10/28) | 🔴🔴 |
| Default stock — QoQ change | **+0.3M / +$13.8B**, vs +1.3M / +$39.8B the prior quarter (**net growth slowed ~¾**) | FY2026 Q3 | FSA | 🔴 **decelerating** |
| Default stock — trajectory | 6.0M (Aug'25) → 7.7M (Dec) → 9.0M (Mar'26) → **9.3M (Jun'26)**. Pipeline at Jun 30: 271–360 days **0.66M** (pre-pandemic Q3 0.30–0.37M) ⇒ Sep-30 count roughly **9.5–10.0M** (OQ#16; bucket undercounts gross inflow) | — | FSA + `DLPortfoliobyDelinquencyStatus.xls` | 🔴 climbing, slower |
| New defaults Q1 2026 (gross DRG flow) | **2.6M** (+ ~1M Q4 2025) | Q1 2026 | NY Fed / Liberty St May 12 | 🔴🔴 |
| Implied exits (cure/rehab/consolidation) | Q1 2026 **~1.3M** (2.6M gross − 1.3M net). **FY2026 Q3: UNKNOWN**, because no gross-flow figure is published for Apr–Jun (ES-04 not gradeable 10/28) | Q1 2026 | STUE derived | 🟠 **open (OQ#3)** |
| **Total portfolio (THE DENOMINATOR — S3 check)** | **42.6M recipients / $1.7T, GROWING +~4% YoY** vs Mar 2025 | Mar 31 2026 | FSA GENERAL-26-38 | ✅ **DENOMINATOR CHECK PASSES** |
| ↳ *what that rules out* | **The default-stock rise is NOT a denominator artifact.** The base is **expanding**, so 7.7M→9.0M is a genuine numerator move — if anything the *rate* understates it. **Run this check every FSA print** (register S3): a shrinking base would inflate every rate STUE cites with zero change in borrower behaviour, and ~62% of the Q1 CC 90+ rise was exactly that | Mar 31 2026 | STUE derived | 🟢 |
| Federally-managed portfolio | 40.9M recipients / **>$1.64T** (>95%) | Mar 31 2026 | FSA | — |
| In repayment or delinquency | **17.4M recipients / $658.5B** (Q2: 17.2M / $632.8B). **31+ days late: 3.54M recipients / $103.2B = 15.7% of repayment dollars** (my sum of the FM delinquency sheet matches FSA GENERAL-26-57) | Jun 30 2026 | FSA | 🔴 |
| In forbearance | **8.0M recipients / $459.2B** (Q2 8.4M / $484.6B). Administrative (SAVE-litigation) DL **7.26M**; discretionary hardship DL **0.65M / $39.5B, rising** | Jun 30 2026 | FSA + `DLbyForbearanceType.xls` | 🟠 reservoir draining slowly, pre-notice |
| In deferment | 3.6M (9%) / $157B | Mar 31 2026 | FSA | — |
| Borrowers 90+ DPD since resumption (cumulative) | >17% | Q1 2026 | Liberty St May 12 2026 | 🔴🔴 |
| Avg age of new defaulters | 38.9 (vs 36.4 pre-pandemic) | Q1 2026 | Liberty St | 🔴 |
| Active repayment 31+ DQ (by $) | **15.7%** (Dec 2025 was 18.6%) | Jun 30 2026 | FSA GENERAL-26-57 + FM delinquency sheet | 🔴 |
| Projected default EOY 2026 | 13M — ⚠️ **source UNVERIFIED** (10/28: the TCF/PB release carries **17M "in distress"**, a different quantity, not 13M; the full report was not readable). Pace (+0.3M/qtr) and the 0.66M late pipeline imply ~10M | Projection | unverified / STUE | 🟢 **looks too high** |
| National avg FICO | 714 | H2 2025 | FICO Spring 2026 (rel Mar 24 2026) | 🔴 |
| Score drop from SL delinquency | **−62 pts = the canonical average** (FICO primary). ⚠️ **FIVE other figures exist and measure DIFFERENT COHORTS — see § SCORE-DROP RECONCILIATION before citing any of them** | H2 2025 | FICO Spring 2026 | 🔴🔴 |

> ✅ **Settled 10/28:** the Jul-21 press figure **9.5M / $233.3B** was never at the Mar-31 perimeter. Jun 30 prints **9.3M / $234.1B** (Federally Managed); the dollar figure is close, the count is not. Per OQ#4, 9.5M-type counts come from summing perimeters (DL + ED-Held FFEL double-counts ~0.66M). **Still cite the FSA Federally Managed figure.**

### SAVE / RAP Transition
| Metric | Value | Status |
|--------|-------|--------|
| SAVE status | Repealed by law (WFTCA Jul 2025) + judicially eliminated (8th Cir Mar 10 2026) | 🔴🔴 |
| SAVE enrollees | **6.52M / $354.3B** at Jun 30 (Q2 6.99M; peak 7.73M at Q3 2025); IBR rose 2.92M → 3.31M in the same quarter [FSA `DLPortfoliobyRepaymentPlan.xls`] | 🔴 |
| Servicer formal notices | **LAUNCHED Jul 1 2026 on schedule**, issued in waves | 🔴 FIRING |
| **Notice window (REVISED)** | **All notices by Dec 31 2026** — compressed ~3mo from prior Mar-2027 end [Nelnet FAQ, via College Investor Jul 2026] | 🔴 **NEW** |
| — MOHELA | Notices **"between July and September 2026"** [MOHELA SAVE FAQ, primary, re-read 10/28; was Jul–Oct]; non-selectors get a **final notice** (confirmed at primary) | 🔴 **noticing complete** |
| — Nelnet | ~3M borrowers, notices through **end-2026** [Nelnet FAQ] | 🔴 |
| Selection window | 90 days from **each individual** notice — **not a single cliff** | — |
| Auto-transition (non-selectors) | **Standard**; loans first in repayment on/after Jul 1 2026 → **Tiered Standard** | 🔴 |
| First-tranche non-selection read | **NO GRADEABLE DATA**: no wave-level count is published (CARL 10/01, KB-CARL-501; re-checked 10/28). AFT v. ED reports do not carry it either | 🟠 CRL-13 |
| Full-population read | **~end-Apr 2027 if the "final 30-day notice" holds** (Dec 31 notice + 90 + 30 days), was ~end-Mar 2027. ⚠️ Secondary-sourced (College Investor 10/15, Newsweek); StudentAid.gov not read at primary | 🟠 CRL-13 final |
| Est. non-selection rate | 30–45% (empirically anchored 30–47%, GAO/CFPB/Embold) | 🔴 |
| Payment shock | $0–70/mo → ~$407/mo (avg $37K balance, Standard) | 🔴🔴 |
| Spending destruction est. | $1.5–2.0B/month redirected from consumption | 🔴🔴 |

### Servicer Performance
*(VALUES + POINTERS. Full analysis — AFT docket history, the CFPB instrument defect, the litigation record — → § DASHBOARD BODY below `## CATALYSTS`.)*

| Metric | Value | Status |
|--------|-------|--------|
| MOHELA missed bills | **2.5M missed bills → >800K DQ** — ⚠️ **an Oct 30 2023 ED figure**, not "2025 cumulative" (AFT Doc 50 ¶¶4, 120, read at primary 10/28) | 🔴 |
| MOHELA call wait / abandon | **13:28 avg speed to answer, 14.12% abandon** (peers 0:13–1:57 and 0.55–4.72%) — ✅ **VERIFIED at ED primary 10/28, but vintage Jul–Sep 2024** (FSA Loan Servicer Performance FY2024 Q4, the last report published). The 7×/50× ratio is derivable from it (6.9× Edfinancial; 48–62× Nelnet/CRI/Aidvantage). **No current figure is public** | 🔴 (2024 data) |
| **CFPB complaints — MOHELA, monthly 2026** | Jan **912** · Feb **681** · Mar **905** · Apr **909** · May **704** · Jun **815** · Jul **895** · Aug **709** · Sep **682**. YoY: Jul 2025 771 · Aug 602 · Sep 651 · Oct 652. ⚠️ **VINTAGE 2026-10-28**, a revisable series (Jul was 883 at the 9/5 vintage); re-pull and re-locate the cliff before comparing vintages | 🟢 at or below baseline |
| **MOHELA daily rate — the ES-02 / CRL-28 instrument** | **CRL-28 window Oct 1–16 (settled, D = Oct 16 by the rule): 396 = 24.8/day.** Sep 22.7/day. Bands **Y >35 · O >45 · R ≥55** (CRL-28 frozen) ⇒ the print is **45% of R**. Interim in-window read; **the grade is ~Nov 13/16** | 🟢 **below Y** |
| ⚠️ Instrument note | The **"5–6 day lag" rule is RETIRED**. The pre-registered completeness test **passed its first out-of-sample run on 10/28**: it chose Oct 16 against an eyeball cliff at Oct 18, so it was conservative, and the band was unchanged at D±3. Cliff distance was ~10 days (vs ~14 on 9/5) | 🟡 **n=1 out-of-sample** |
| **AFT v. MOHELA** | **D.D.C. `1:24-cv-02460` (Chutkan) — STAYED for settlement talks.** **Doc 54 (Jul 17 2026, free on archive.org) asked for a 60-day continuation and a joint status report due Sep 15 2026.** That report is not in the free archive and the CourtListener page still 404s ⇒ **status after 9/15 = ACCESS GAP, not quiet.** No class cert ever filed | 🔴 **settlement-gated** |
| — retrieval | ⚠️ **The 8/13 curl+UA route to `courtlistener.com/docket/69090685/` returned HTTP 404 on 9/5 — ACCESS FAILURE, not a quiet docket.** Event-driven; do not re-check weekly | ⚠️ |
| Maldonado v. MOHELA | Mar 2026 — violated CA Student Borrower BoR + UCL | 🔴🔴 precedent stands |
| Settlement (AFT) | NONE | — |

### Treasury Transfer
*(VALUES + POINTERS. Full analysis — the IAA reading, the three traps, the press-creep record — → § DASHBOARD BODY below `## CATALYSTS`.)*

| Metric | Value | Status |
|--------|-------|--------|
| **Custody status — the headline** | **NOT TRANSFERRED as far as any primary shows.** The **Defaulted Loans Support Center launched Sep 30 2026** on StudentAid.gov (rehabilitation and consolidation online) [Treasury sb0639, primary]. **The release is silent on exemption revocation, collector contracts and garnishment/offset timing.** Fiscal Service page last read 9/5 (*"helps ED collect"*); not re-read 10/28 | 🟠 |
| **🔑 THE CUSTODY TRIGGER (OQ#14 instrument)** | **Treasury REVOKES Education's May 11 2001 Cross-Servicing exemption** (31 U.S.C. § 3711(g)(2)(B)). Stated trigger: *"once **full operational capacity** has been reached"* — **a capability, not a date; the governing IAA carries no phase dates at all** | 🔑 **binary, legal, checkable** |
| ⚠️ Scope split that is easy to get wrong | Pre-revocation, ED **may refer debts discretionarily** with Treasury's approval ⇒ **accounts can move without revocation and without any public-page change.** Evidence against **custody** is **not** evidence against *some accounts having moved* | ⚠️ |
| **Phase 1 scope — ⚠️ THREE PERIMETERS** | **~500K** launch wave [CRS R48962] · the IAA's own object is **DMCS/DRG: "nearly six million" borrowers / over "$120 billion"** · vs **Federally Managed 9.0M / $220B** and **Direct Loan 7.20M**. **State the perimeter on every default figure** — mixing them is why press counts scatter (7.8M/$179B · 9.2M · 9.5M · 10M) | ⚠️ |
| Vendor build-out (OQ#14 leg b) | 🔴 **9/5 "validated null" was WRONG (query missed the agency's wording).** Fiscal Service awarded **"PCA SERVICES - EDUCATION PILOT"** task orders to **5 collectors (CBE, Coast, ConServe, Pioneer, Transworld), $8M each, signed May 19–29 2026**, then **terminated all five for convenience effective Jun 3 2026** and deobligated ($24,527.95 kept by Pioneer) [USAspending/FPDS, primary, 10/28]. Parent BPAs **2033H625A00007–11**: a re-award would show there. Separate all-agency PCA orders ($12M each, Jan 2026 – Jan 2027) also exist. Detail: `research/README_2026-10-28_research-items.md` | 🟠 **pilot built and cancelled; watch the BPAs** |
| Nature of handoff | **Servicing/collections CUSTODY, not enforcement resumption.** Now a contract citation: *"only the tools **authorized by Education**"* ⇒ the AWG/TOP switch stays with ED post-custody | ⚠️ |
| ⚠️ Name trap | **"Default Resolution HUB" ≠ "Default Resolution GROUP."** The IAA says **GROUP** throughout; **"Hub" appears nowhere in it** — it is press framing | ⚠️ |
| Phase 2 / Phase 3 | Non-defaulted servicing; then FAFSA / eligibility / oversight. Planned, no public dates | 🟡 |
| Legal authority | Disputed; GOP bill introduced to codify | 🔴 |

### Borrower Defense (Sweet v. McMahon)
| Metric | Value | Status |
|--------|-------|--------|
| Exhibit C (Jan 28) / non-Exhibit C (Apr 15) deadlines | Both MISSED → auto Full Settlement Relief triggered | 🔴 |
| **Jun 15 notice deadline** | ✅ **MET** — first Sweet deadline DOE did not miss. **~30–36K** discharge-eligibility emails week of Jun 15 to non-Exhibit C post-class applicants (Jun 23–Nov 16 2022 filers) | 🟢 **resolved** |
| Relief delivery | Within 1 yr of notice → **~Jun 2027** | — |
| Total relief pipeline | ~271K cumulative (PPSL) | 🔴 firing |
| 9th Cir appeal 26-1136 | ✅ **DOE LOST, Fri Jul 17 2026, unanimous** (Wardlaw/Owens/Bress): relief stands for **>170K post-class applicants**. Detail + the Jul-18 weekday tie-break → archive §C8 | 🟢 resolved |
| — scale, disaggregated | **>500K** borrowers / **≥$23B** = the **whole 2022 settlement** · **~200K** = original settlement class · **>170K (DOE knew of >205K by Feb 2023)** = **post-class applicants, the cohort THIS ruling covers** · **>210K** = a *separate* borrower-defense backlog · **>1,000** class members still awaiting relief already owed. ⚠️ **Headlines say "500,000" — that is the settlement total, NOT this ruling's cohort. Do not cite 500K as the 7/17 number.** | ⚠️ figure-conflation trap |
| 🆕🔴 **Aug 18 2026 — PPSL moved to ENFORCE the settlement AND to hold ED in CONTEMPT with sanctions** | Verified at the PPSL primary (the search summary that surfaced it was truncated — resolved at source per STUE's own rule). **At least 807 Sweet CLASS members are still awaiting discharges or refunds ED was legally required to provide by deadlines "that have long since passed"; some "more than a year and a half" overdue.** ⚠️ **PERIMETER — this file has a standing conflation trap on this case: 807 = original-CLASS members with OVERDUE relief.** NOT the **>170K** post-class cohort of the 7/17 ruling, NOT the **~200K** class, NOT the **>500K / ≥$23B** settlement. **Small in count, large in legal significance — a contempt predicate, not a population estimate** | 🔴 **NEW — ED compliance contested** |
| — status 10/28 | **Fully briefed** (plaintiffs' replies Oct 15 2026); **hearing Thu Nov 5 2026**; no ruling [PPSL case page via search, docket not read] | 🟠 **ruling pending** |

### SLABS / ES-STUE-05 — 🆕 **FIRST CHECK EVER (2026-09-05).** Registered prior CONFIRMED
*(VALUES + POINTERS. Working → § DASHBOARD BODY §D3.)*

| Metric | Value | Status |
|--------|-------|--------|
| **Instrument** | **SLM Student Loan Trust 2014-2 (Navient), Form 10-D filed 2026-09-04**, collection period **Jul 1–31 2026**, distribution date 8/25/2026 [SEC EDGAR primary] | ✅ **live route found** |
| **Credit loss — the registered question** | **Cumulative non-reimbursable losses $4.16M on a $964.9M original pool = 0.43%.** Period losses **$23,560** | 🟢 **DID_NOT_APPEAR — prior CONFIRMED** |
| Credit enhancement | **Parity ratio 1.00999** (prior 1.01010) · overcollateralisation **$1.79M** · **reserve funds utilised $0.00** | 🟢 **no CE breach, no draw** |
| ⚠️ **But the pool IS deeply stressed — in CASH-FLOW terms, not credit** | Only **63.83% current**. **31+ delinquent 13.50%** · **forbearance 16.47%** · deferment 5.62% · claims in process 0.49% ⇒ **~36% of the pool is not paying normally** | 🟠 |
| ✅ **The registered MECHANISM is confirmed, not just the direction** | **Since-issued CPR −40.02%** — *negative* prepayment, i.e. **EXTENSION.** STUE registered FFELP exposure as *"extension / prepayment / liquidity, NOT credit"* **before looking. That is exactly what the tape shows** | 🟢 **mechanism confirmed** |
| Bucket shape (31–60 → 61–120 DPD) | Aging with no cure; **NOT an exhaustion test** (downgraded 9/5; legacy FFELP pool ≠ the federal defaulted cohort). Detail → archive §C8 | 🔧 downgraded |

### Collections Status
| Metric | Value | Status |
|--------|-------|--------|
| Involuntary collections (AWG + Treasury Offset) | **PAUSED since Jan 16 2026; no restart verified at any primary** (re-checked 10/28, 4th consecutive STUCK). Press reports collections "in 2027"; a MoneyWise 10/27 "garnishment next month" claim is unsupported and conflicts with it | 🟡 **STUCK** |
| 🆕 **STRUCTURAL CORROBORATION — the restart switch stays with ED even after custody moves** | ED/Treasury IAA (Mar 19 2026), read at primary 9/5: *"The Cross-Servicing program will use **only the tools authorized by Education**, as specified in the Cross-Servicing Agency Profile(s)."* ⇒ **a Treasury custody transfer does NOT itself restart AWG/TOP.** ⚠️ **But the plumbing is specified and being built with the switch off** — the IAA lays out the full AWG process (NOI letter → hearing → AWG order *"generally between 31 and 60 days after sending the NOI letter"*). **When ED authorizes it, that 31–60 day NOI→order gap is the usable lead time.** | ⚠️ **watch the AUTHORIZATION, not the custody** |
| Reported expectation | **Press: private collectors possibly from Nov 2026, involuntary collections in 2027** (Washington Sun 10/19 via IBTimes). No ED/Treasury commitment | 🟠 |
| Borrowers exposed | 5M+ in default at pause; ~9M now | 🔴 |


---

## ✅ #17 ANSWERED — **THE DENOMINATOR IS PADDED. Exposure-adjusted, distress is ~31–37% ABOVE pre-pandemic, not below it.** (2026-08-13)

> **This reverses the morning's headline reading and confirms the prior registered before the pull.** It also answers #17 by a mechanism I did **not** anticipate — I expected the adjustment to come from for-profit cohort quality; **the dominant effect is far simpler and far larger: the share of the portfolio that CAN be delinquent has collapsed.**

### The mechanism, in one line
**The NY Fed headline divides delinquent balances by ALL student debt — including balances that structurally cannot be delinquent.** That protected block has nearly tripled.

| Federally Managed portfolio, share of **dollars** | 2015–2019 avg | **2026 Q2** | Δ |
|---|---:|---:|---:|
| **In active repayment** *(exposed to delinquency)* | **53.8%** | **38.5%** | **−15.3pp** |
| **Forbearance** *(cannot be delinquent)* | 10.0% | **29.5%** | **+19.5pp** |
| In-school + grace | 14.3% | 8.4% | −5.9pp |
| Cumulative in default | 10.9% | 13.4% | +2.5pp |

### The answer, on FSA's own internally-consistent measure
Delinquency **as a share of the in-repayment base** — same source, same portfolio, no cross-source mixing:

| | 2015–19 avg | **2026 Q2** | Δ |
|---|---:|---:|---:|
| **90+ (of those in repayment)** | **7.97%** | **10.95%** | **+2.98pp = 1.37×** |
| 31+ (of those in repayment) | 14.19% | 15.53% | +1.34pp |

### Cross-checked by an independent route
Applying the FSA exposure share to the **NY Fed** headline (different source for the numerator) gives **20.55% → 26.82% = 1.31×**. **Two routes, ~1.3–1.4×, same direction.** *(FSA fiscal Q2 ends Mar 31, i.e. calendar Q1 — mapping applied, not assumed.)*

### ⚠️ Why this is CONSERVATIVE, not inflated
**The in-repayment base EXCLUDES the defaulted stock**, and that stock grew **5.2M → 9.0M in the two quarters immediately before this reading.** The worst loans were removed from the denominator right before it was measured. **A cleaner base should print a LOWER rate — it printed a higher one.**

### What this does and does not settle

**Settles:** the headline NY Fed rate **is not comparable across the pandemic** without an exposure adjustment. **Every "back to pre-pandemic" comparison — including WALTER's May signal, CARL's framing, and my own this morning — is measuring a ratio whose denominator changed underneath it.** The composition-adjusted baseline is **below** 11.12%, so **today's 10.60% is elevated.** Registered prior: **CONFIRMED**, wrong mechanism.

**Does NOT settle — stated so this isn't over-read in the new direction:**
1. ⚠️ **The for-profit cohort adjustment I originally set out to do is STILL NOT DONE.** It would push the pre-pandemic baseline *lower still* (2015–19's 7.97% includes for-profit borrowers at their peak), making today look worse — **but it is unmeasured, so it is not claimed.**
2. ⚠️ **Selection into forbearance is NOT controlled for and could cut either way.** The 2024–26 forbearance block is largely the **SAVE litigation forbearance** — administrative, not distress-selected — so the remaining in-repayment population is not obviously adversely selected. **But it may be positively selected** (people who kept paying while others were parked). **Unresolved; it is the main threat to this finding.** → open question #18.
3. This says nothing about the **cascade**, which remains pre-test until 2027:Q1.

> **The through-line of the whole day:** the morning asked *"compared to what?"* and got the wrong window. The afternoon asked *"was that window normal?"* and retracted. **This asked "is the RATIO even measuring the same thing in both periods?" — and it was not.** The first two were about the numerator's context; **this one is about the denominator, and it is the one that mattered.**

---

## ⚠️ THE BASELINE PROBLEM — ⛔ ROTATED 2026-10-28 → `archive/STUE_STATUS_ARCHIVE_2026-10.md` §C2 (16041 B, CRC32 `e957e453`)

The 8/13 base-rate check and its same-day partial retraction. **What survives, and is carried live elsewhere:** the 2015–19 baseline is a contaminated peak, so **quote 10.60% with a RANGE of baselines, never one** (`CLAUDE.md` band-provenance block); exposure-adjusted distress is **~31–37% above pre-pandemic** (§ #17 ANSWERED, open question #18 caveat); the **speed** finding (+3.8M in two quarters) and the dated peak falsifier (open question #16). Full working, including what was withdrawn, is in the archive.

## TRANSMISSION TO CARL — RE-SCOPED (DEWEY C2, 2026-07-24)

### 📐 SCORE-DROP RECONCILIATION (added 2026-07-31) — six figures, one concept, **they do not conflict**
> 🆕 **10/28 additions (primary, see open question #12):** the −87…−171 band is Liberty Street Mar 26 2025, a **pre-pandemic (2016–19) by-prior-score-band** estimate. A **post-on-ramp observed** update exists (Liberty Street May 13 2025, Q4'24→Q1'25 new-90+ cohort, Equifax 3.0): **−74 / −140 / −177 by band, ≈ −105 weighted**. TCF/PB **−57** (Q1–Q3 2025 credit panel) is now sourced to its release. **Default stays −62 (FICO).**

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
| FHA total DQ | **11.79%** (−9bps QoQ, **+122bps YoY**) — **SECOND-highest since Q2-2021; Q1-2026's 11.88% remains the peak.** ⛔ **NOT RELIEF — MIGRATION.** MBA NDS total DQ **excludes loans in foreclosure**, so a borrower moving delinquent→foreclosure leaves the numerator and the measure improves while nothing about their situation does. Same release: **FC inventory +3bps to 0.67%, 90-day +1bp to 1.43%** (MBA: *"more loans moved into later stages"*). Declines uniform across conventional/FHA/VA (−3/−9/−10bps) = seasonality, not FHA relief. ⚠️SECONDARY (mba.org 403s; HousingWire 8/13). **Standing rule: never read an FHA DQ decline as relief without checking FC inventory AND the 90-day bucket in the same release.** | MBA NDS **Q2-2026** (CARL hand-down 8/15, from HOMER 8/13; prior 11.88% Q1-2026) |
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
| ⛔ **7 FIRED/CLOSED catalyst rows ROTATED 2026-09-05 PM** → `archive/STUE_STATUS_ARCHIVE_2026-09.md` **§B9** (2,677 B, CRC32 `cb276a5c`) | Treasury Phase-1 verification · AFT docket check · the Q2 HHDC print · the NY Fed advisory-watch · the ~Aug-20 CFPB re-pull · the ~Sep FSA release row (now header-triggered) · the ~Sep-15 *Sweet* oral argument that never happened. **Two figures carried forward here because the safety test flagged they would otherwise leave STATUS entirely: the Q2 CC 90+ print was 12.92%, and CARL cut CRL-05 85→20 on it.** ⚠️ *Both are CARL's, not STUE's — recorded as context, and STUE still does not mirror a CRL confidence as its own state.* | ⛔ **rotated** |
| ~~Fri 2026-09-11~~ **FIRED 9/18, graded 10/28** | FSA FY2026 Q3 release (LM Fri 18 Sep 2026; CARL caught it 9/24) | ES-01 NO VERDICT (straddles Y) · ES-04 not gradeable · ES-06 access gap. **Next: FY2026 Q4 (Sep 30 data), expected ~mid/late Dec 2026. Poll the `last-modified` header weekly from ~Dec 1** |
| **~Wed 2026-11-04 / Thu 11-05** | 🔴 **NY Fed 2026:Q3 HHDC** (2025:Q3 released Wed Nov 5; no advisory yet on 10/28) | Third stock print (CRL-04) and flow into 90+ (cohort exhaustion). **Poll `HHD_C_Report_2026Q3.xlsx` (curl + browser UA); returned 302 on 10/28** |
| **Thu 2026-11-05** | **Sweet v. McMahon hearing**: motions to enforce and for contempt (fully briefed 10/15) | Relief DELIVERY leg; 807 class members overdue. Event-driven read after the hearing |
| **Mon 2026-11-23 11:00 ET** | **AFT v. ED (`1:25-cv-00802`) status conference** (10/14 conference held; set by minute entry) | IDR/PSLF backlog reports, **not** SAVE non-selection. Check for any new ED status report (none since Doc 65, May 19) |
| ~~**~Oct 31**~~ **→ done by Sep 30** | MOHELA notice waves complete — **its FAQ now says notices went out July–September 2026** (primary, 10/28) | ⇒ MOHELA's 90-day windows close by **~Dec 29 2026**; first auto-enrolments from ~Sep 29 (+ ~30-day final notice ⇒ ~Oct 29). **The complaint window that matters is Oct 2026 – Jan 2027.** The ES-02 grade date (~Nov 13/16) is unchanged |
| **~Fri 2026-11-13 / Mon 11-16** | 🔴 **ES-02 THIRD AND FINAL LOOK — the actual GRADE date** (DOCKET L150) | ⚠️ **CORRECTED 2026-09-05 (PROME/Codex):** the surfaces previously called **Oct 31 itself** the "third and final look." **Wrong, and wrong by STUE's own cliff finding** — the settled boundary runs **~14 days behind the pull**, so a pull on Oct 31 reads data settled only to ~Oct 17 and **cannot see notice completion at all.** The boundary reaches Oct 31 around **~Nov 14**. **Grading a completion event before the data covering it is settled is exactly the error the lag work exists to prevent** — and it very nearly propagated into the row that decides CRL-28's STUCK→MISSED question |
| ⛔ **2 closed rows ROTATED 2026-10-28** → archive §C7 (736 B, CRC32 `1e194dc8`) | The superseded FSA "see re-dated" marker and the 10/01 first-tranche read (no gradeable data; CARL KB-CARL-501) | ⛔ |
| ~~**Sep 30 2026**~~ **→ Dec 31 2026 (EXTENDED 9/29 by ED; read by CARL 10/01, KB-CARL-500)** | RAP auto-pay enrollment deadline — **1% interest-rate reduction through Jun 30 2028** for borrowers enrolled in auto-pay by this date [ED; Edfinancial page PRIMARY 10/01: 'on or before 11:59 PM ET on 12/31/2026', Direct Loans originated on or after 7/1/2012; ~2M new enrolments per ED 9/29] | 🆕 *added 7/31.* Marginally **relieving** on payment burden; a partial offset to the $0→~$407/mo shock. Small, but it is the only easing mechanism in the transition |
| **TBD — event-driven** | **Treasury revokes ED's May-11-2001 Cross-Servicing exemption** = THE custody event (OQ#14, re-instrumented 9/5) | Stated trigger is *"once full operational capacity has been reached"* — **no date exists.** Leading indicator = Treasury vendor/procurement build-out (USAspending); currently **null, with the last PCA action a 2025 bridge contract** |
| **Dec 31 2026** | **All SAVE notices issued (COMPRESSED from Mar 2027)** | Every borrower's 90-day clock started |
| **~Mar 2027 → possibly ~end-Apr 2027** | Last selection deadlines → final auto-enrollments (+30 days if the "final 30-day notice" holds; secondary-sourced 10/28) | **CRL-13 full population** |
| **Q3–Q4 2026** | Post-transition DQ wave (**CRL-28 window opens Oct 1** — CRL-14's successor, retired+replaced 7/31) | Now rests on **operational failure only** — litigation + garnishment legs both gated |
| **TBD — event-driven** | AFT v. MOHELA stay lifts → joint status report → schedule | No date; watch docket 1:24-cv-02460 |

---

---

## 📚 DASHBOARD BODY — the analysis behind the Servicer and Treasury rows

> **Moved here 2026-09-05 under the (c) rule: THE DASHBOARD HOLDS VALUES AND POINTERS.** These blocks are **verbatim**; nothing was rewritten. They sit **below `## CATALYSTS` and are therefore GREP/ON-DEMAND, not a boot whole-read.** ⚠️ **A safety test was run BEFORE the line was moved** and caught six live figures that would otherwise have left the bounded head entirely (`913`, `STAYED`, `2.5M`, `800K`, `14%`, `~13 min`) — all six were written into the compact dashboard rows above before this cut was made.

### §D1 — Servicer Performance, full detail
*Verbatim. 7,604 B · CRC32 `ef471ec9`*

### Servicer Performance
| Metric | Value | Status |
|--------|-------|--------|
| MOHELA missed bills | 2.5M → 800K DQ — ⚠️ Oct 30 2023 ED figure (corrected 10/28, AFT Doc 50 ¶120) | 🔴 |
| MOHELA call wait | **Longest of major federal servicers — ~13 min avg, ~14% abandon rate** [FSA servicer data, cited in 2026 filings] | 🔴 |
| ⛔ **ROTATED 2026-10-28** → archive §C3a (5808 B, CRC32 `7f83d943`) | 11 rows: the 9/5-vintage CFPB rows (superseded by the 10/28 vintage in § SIGNAL DASHBOARD and `workbook/SERVICER.tsv`), the retired 5–6-day-lag defect row (rule now in `CLAUDE.md` + ES tracker), and the AFT v. MOHELA docket history through 8/13 (stays #1/#2, Doc 53 numbering fix, the Sep-29-2025 ruling back-fill). Current case status: § SIGNAL DASHBOARD | ⛔ |
| **AFT v. MOHELA** | **D.D.C. 1:24-cv-02460 (Chutkan) — STAYED, and now in SETTLEMENT NEGOTIATION.** Discovery frozen since 10/27/2025. Last filing **Jul 17 2026 (#54)** | 🔴 **SETTLEMENT-GATED** |
| — Class certification | **NEVER FILED** — no class-cert motion or ruling has ever appeared on the docket | 🟠 |
| — ⚠️ Implication for attribution | A settlement typically means **no admission of liability, no public discovery record, no class cert** ⇒ the likeliest path **forecloses** the servicer-attributed default evidence CRL-28's instrument needs (attribution question is unchanged by the CRL-14→CRL-28 retire+replace). Measurability gets *worse*, not better. | 🔴 |
| 🟠 **The Amended Complaint (Doc 50, Jan 15 2026) is FREE and STUE has never read it** | STUE sources **280K borrowers overcharged**, the **~7×/>50× wait-time ratio** and the call-centre **"deflection"** claim to *Protect Borrowers / NCLC* summaries — i.e. **advocacy secondaries paraphrasing a primary that is one free download away** (CourtListener + Internet Archive; $3.00 only if bought on PACER). STUE's own source-quality rule says resolve procedural claims on the docket itself. **Highest-value free pull available in this lane** — it would let three advocacy-attributed figures be re-sourced to the pleading | 🟠 **backlogged → open question #13** |
| Maldonado v. MOHELA | Mar 2026 — violated CA Student Borrower BoR + UCL | 🔴🔴 precedent stands |
| Settlement | NONE | — |



### §D2 — Treasury Transfer, full detail
*Verbatim. 8,936 B · CRC32 `61383f2f`*

### Treasury Transfer
| Metric | Value | Status |
|--------|-------|--------|
| ⛔ **ROTATED 2026-10-28** → archive §C3b (5347 B, CRC32 `ac9c3ccf`) | 8 closed rows: the retired "~500K by July" Phase-1 question, Treasury's Aug-7 future-tense plans, the 8/13 Fiscal Service reading, the Federal-Register non-source, the press count-creep record and the 8/10 inconclusive verdict. **Standing traps stay live in `CLAUDE.md` § Treasury Transfer** | ⛔ |
| 🆕🔑 **THE GOVERNING PRIMARY, READ 2026-09-05 — ED/Treasury Interagency Agreement, Mar 19 2026 (free on ed.gov)** | **Four months of this lane were worked through press and a webpage while the contract sat unopened.** It settles the shape of the question: **Phase 1 = Treasury REVOKES Education's Cross-Servicing exemption** (granted **May 11 2001** under **31 U.S.C. § 3711(g)(2)(B)**) and integrates FSA's **Default Resolution Group** into Cross-Servicing. Phase 2 = non-defaulted servicing. Phase 3 = FAFSA / eligibility / oversight | 🔑 **new instrument** |
| 🆕🔑 **THE TRIGGER IS A CAPABILITY, NOT A DATE — and this is why the July question was unanswerable** | *"Education understands that it is Treasury's intent to **revoke the existing exemption once full operational capacity has been reached**."* **The agreement contains NO phase dates** (effective on last signature, runs until terminated, 90-day termination clause). ✅ **Retroactively vindicates the 8/13 retirement of the "500K by July" row** — the contract never contemplated a dated wave | ✅ **OQ#5 retirement justified at primary** |
| 🆕⚠️ **AND IT DISSOLVES THE CONTRADICTION: two claims STUE had fused** | Pre-revocation, *"Education may refer exempted debts to Cross-Servicing, if agreed to by Treasury"* — **discretionary referral.** ⇒ **accounts CAN move without revocation and without any change to Treasury's public page.** So the page evidence is strong against **CUSTODY** and is **NOT** evidence against *some accounts having moved*. **Keep those separate** | ⚠️ **scope correction** |
| 🆕⚠️ **A THIRD PERIMETER — and Phase 1's object is SMALLER than every figure in circulation** | IAA: *"The DRG operates and maintains the Default Management and Collections System (DMCS)… It serves nearly **six million** student and parent borrowers with a current outstanding loan value of over **$120 billion**."* **That is what Phase 1 takes over — not 9.0M/$220B.** ⚠️ STUE already tracks **Federally Managed 9.00M ≠ Direct Loan 7.20M**; **DMCS/DRG ~6M/$120B is a THIRD perimeter.** It explains the press scatter (7.8M/$179B · 9.2M · 9.5M · 10M): **they are mixing perimeters.** **State the perimeter on every default figure** | ⚠️ **perimeter discipline** |
| ✅ **NAME TRAP SETTLED AT PRIMARY** | The IAA says **Default Resolution GROUP (DRG)** throughout; **"Default Resolution Hub" appears NOWHERE in it.** The "Hub" is press framing over DRG/Cross-Servicing integration. **The registered trap was correct** | ✅ |
| ✅ **OQ#14 leg (b) — vendor awards: NULL, and the null is VALIDATED** | USAspending, Treasury awarding, actions Mar–Sep 2026: **"default resolution" n=0 · "student" n=0**, while **controls FIRE** ("debt collection" n=10, "cross-servicing" n=1, "call center" n=7) ⇒ **real null, not a broken query.** ⚠️ Latest PCA capacity action is a **bridge contract dated 2025-05-18** — a stopgap, the **opposite shape** of a build toward "full operational capacity." *(SAM.gov is a JS shell and defeats fetching; **USAspending is the workable route**)* | 🟠 **no build-out visible** |
| Nature of handoff | **Servicing/collections CUSTODY — not enforcement resumption.** Do not conflate. ✅ **Now a CONTRACT CITATION, not an assertion:** *"The Cross-Servicing program will use only the tools **authorized by Education**"* ⇒ the AWG/TOP switch stays with ED post-custody | ⚠️ |
| Phase 2 / Phase 3 | Planned, no public dates | 🟡 |
| Legal authority | Disputed; GOP bill introduced to codify the transfer | 🔴 |




---

## ROUTED TO PARENT — ✅ ALL ADOPTED (closed 2026-07-31)

**[ROTATED 2026-09-05 → `archive/STUE_STATUS_ARCHIVE_2026-09.md` §B7]** The 7/25–7/31 routing table, closed with nothing owed in either direction, verified against the parent's committed files. **The two procedural lessons are kept and are live in boot step 2b:** check adoption against the parent's FILES, not against a claim of processing — and check whether the parent is mid-session before reading a stale stamp as neglect.

### 🔵 LIVE — routed 2026-09-05, delivered to CARL + PROME (`SV-STUE-2026-09-05-01`)

> **Boot step 2b reads THIS table.** Verify each against the parent's committed files — **delivery is not adoption.**

| Item | Ask | Status |
|---|---|---|
| ⛔ **6 closed 9/5 rows ROTATED 2026-10-28** → archive §C6 (1167 B, CRC32 `4820ddff`) | ES-02 mechanism warning, lag-rule defect, FSA not-posted, DMCS perimeter, Sweet contempt, read-cap ruling — all integrated or ruled by CARL | ✅ closed |
| **OQ#19 — SAVE notice-window conflict** | Aug-15 secondary would pull CRL-13's full-population read to ~Nov 13 2026 vs carried Q1-2027 | 🟠 **OPEN — carried framing STANDS.** CARL 9/5: settle on a **servicer primary before Oct 1**; decide on evidence, not a secondary |
| **10/28 delivery** (`SV-STUE-2026-10-28-01` + packet `AGENTS/CARL/inbox/processed/2026-10-28_from-STUE_FSA-Q3-grades-AFT-collections.md`) | ES-01 NO VERDICT (straddles Y) · ES-04 not gradeable · ES-06 access gap · ES-02 interim 24.8/day · AFT v. ED date correction (10/14, not 10/28; no new count) · collections still paused. **No CRL change proposed** | ✅ **ADOPTED 10/28** — CARL KB-568/569, STATUS Student/FSA row; ES-02 placement reading AFFIRMED (carl-6f) |
| **10/28 research pass** (`SV-STUE-2026-10-28-02` + packet `…/2026-10-28_from-STUE_research-items-treasury-pilot-SAVE-windows.md`; `research/README_2026-10-28_research-items.md`) | Treasury Education PCA pilot (awarded, then terminated Jun 3); SAVE windows servicer-specific (MOHELA Jul–Sep); score-drop band sourced; AFT Doc 50 figures checked; 13M attribution unverified; 3 card fixes | ✅ **ADOPTED 10/28** — CARL KB-CARL-573 + STATUS wording; card fixes applied in STUE `CLAUDE.md` (lines 95, 109, 130 verified); PROME DOCKET L154 resolved |

> ⚠️ **Historical routing table (7/25–7/31, all adopted, nothing owed) → `archive/STUE_STATUS_ARCHIVE_2026-09.md` §B7.**

> **STUE holds no predictions ledger** — CRL-04/05/13/28 are CARL's rows and CARL is system of record. STUE proposes with worked reasoning; the parent applies. **Do not mirror a CRL confidence here.**

---

## 🗃️ READ-CAP ROTATION LOG — ⛔ ROTATED 2026-10-28 → archive §C5 (2324 B, CRC32 `68803cf7`)

The 9/5 rotation record (byte table, "rotation alone cannot fix this surface"). The 10/28 passes are recorded in the archive header and commit messages.

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

1. ✅ RESOLVED 2026-07-25 (stay basis = settlement negotiation) → archive §C4.
1b. **#8 (NEW): does MOHELA settle?** **Doc 54 (filed 7/17/26) is the discriminator** — the 60-day clock from Doc 52 expired on it, so it is either another extension (talks live) or a merits schedule (talks failed). **PACER-only, ~$0.30, ~3pp.** Everything else on this docket is now recovered free. *Bears on CRL-14: a settlement forecloses the public attribution evidence the row depends on.* **⏸ UPDATE 2026-08-13: docket CONFIRMED QUIET through today — nothing filed since Doc 54 (Jul 17). So the discriminator has NOT resolved and is NOT overdue; a 4-week gap after a status report is unremarkable on a stayed docket. Doc 54 remains PACER-only (0 RECAP requests). ⚠️ Do not re-check this weekly — it is EVENT-driven, and the 8/10 session burned a check on it. Free route if ever needed: `curl` + browser UA → `courtlistener.com/docket/69090685/`.**
2. ✅ RESOLVED 2026-08-13 (Q2 HHDC: stock up, flow halved = cohort exhaustion) → archive §C4.
3. **Is the ~1.3M/quarter cure channel durable or a one-off?** Newly quantified this session; if borrowers are exiting default nearly as fast as entering, the 13M EOY projection is too high. → FSA Q2 (~Sep). 🔧 **10/28: STILL OPEN.** FY2026 Q3 net default growth was only +0.3M, but no gross-flow figure exists for Apr–Jun (FSA `DLEnteringDefaults.xls` frozen since Aug 2023; no Liberty Street update), so the cure share is unmeasurable. ES-04 not gradeable.
4. ✅ LARGELY RESOLVED 2026-09-05 (9.5M-type counts = DL + ED-Held FFEL sum-of-parts, a ~0.66M double-count) → archive §C4.
5. ⛔ RETIRED 2026-08-13 (Phase-1 "500K by July"; successor = #14) → archive §C4.
6. ✅ RESOLVED 2026-09-05 (ES-02 2nd DID_NOT_APPEAR) → archive §C4.
7. **Does the compressed notice window change the non-selection RATE, or just its timing?** A shorter Department-wide window with fixed servicer capacity is the mechanism that would *raise* non-selection. → CRL-13.
8. ✅ RESOLVED (HHDC Q2 printed Tue Aug 11, the fallback Tuesday) → archive §C4.
9. **🔧 UPDATED + RE-FRAMED 2026-09-05 — the question moved from the appellate tail to district-court ENFORCEMENT, and that is the live gate now.** **No cert petition found in any source this sweep**, and PPSL's own case page reports none ⇒ **leaning NO, but unresolved** (no deadline is stated — *"no petition found"* is not *"DOE declined"*). **What actually happened in the gap: on Aug 18 2026 PPSL moved to ENFORCE the settlement and to hold ED in CONTEMPT with sanctions**, stating **at least 807 CLASS members** still await discharges/refunds past deadlines *"that have long since passed,"* some **>1.5 years** overdue. ⚠️ **Perimeter: 807 = original-class members with overdue relief — NOT the >170K post-class cohort, NOT ~200K, NOT >500K.** **Entitlement is settled; DELIVERY is contested.** → watch the D.C. district docket for a ruling on the enforce/contempt motions. 🔧 **10/28: enforce + contempt motions fully briefed (replies Oct 15); hearing Thu Nov 5 2026.** Still no cert petition found.
10. **🆕 Harvest the TCF/Protect Borrowers study STUE already half-cites.** *"Trump's Student Loan Delinquency Crisis, Unmasked"* (Granville, TCF + PB, **published Feb 20 2026**, nationally-representative credit panel, data = first 3 quarters of 2025) is where STUE's carried **25% DQ rate** and **13M EOY projection** come from — **but its cohort-severity and demographic cuts were never harvested**: **−57pt** avg score drop, **three-quarters of delinquent borrowers pushed into "deep subprime,"** **7.9M entered delinquency** in 3 quarters, **Black and Native borrowers ~50%** DQ, **Pell recipients 27%**. ⚠️ **NOT new** — a 5-month-old study, flagged so it is not mistaken for a July datum. The **−57pt** figure is a *third* score-drop number alongside FICO's **−62** (H2 2025) and the **−69** derivative cite: **different sources, windows and panels — reconcile before citing any of them as "the" number.** *Backlog item, not a threshold move.* ✅ **HARVESTED 2026-10-28** (release text; report page 403): 25% DQ vs 9.2% (2019), 7.9M entered DQ Q1–Q3 2025, −57 pts, 2M near-prime 680→580, Pell 27% vs 15%, LA 40% / MS 39%, 328K IDR rejections Aug 2025, 734K unprocessed Dec. ⚠️ **It projects 17M "in distress", NOT 13M in default — STUE's 13M attribution is unverified.** → `research/README_2026-10-28_research-items.md` §4.
11. **🆕 🔴 Is the FHA delinquency rise student-loan-CAUSED, or co-moving?** The single highest-value open question STUE has, because it decides whether **CASCADE Stage 6 (mortgage) re-dates from Apr-Dec 2027 to ALREADY UNDERWAY** — a ~9-18 month pull-forward of the thesis's most consequential stage. **What would settle it:** an FHA-isolated cut — DQ rates for FHA borrowers *with* vs *without* student debt, same vintage, same LTV band. **CORRECTED 2026-08-10: the VASP precondition was a false blocker (category error — VASP is a VA program, not an in-series FHA confound, and the VA leg is much milder, not similar size — see § CHANNEL 5 above) and is REMOVED.** The real in-series confound to net out first is **HUD ML 2025-06's mandatory partial-claim waterfall** (unpulled — HUD FHA Neighborhood Watch geographic cut). **Do not treat "FHA is rising and student debt is concentrated there" as causation — that is the same co-movement error that produced the over-sized CC cascade claim.** Owner: CARL/DEWEY hold the evidence; STUE holds the student-debt side. → § CHANNEL 5.
12. **🆕 Source the score-drop band properly.** Pull the **NY Fed Liberty Street Mar 2025** piece behind the **−87 to −171** figure and check whether a post-on-ramp update exists — it is the oldest and largest number in the score set and it anchors the top of the cascade. → § SCORE-DROP RECONCILIATION. ✅ **RESOLVED 2026-10-28 at primary.** −87…−171 = Mangrum & Wang, Liberty Street **Mar 26 2025**: by prior score band (<620 −87 … 760+ −171), **first new 90+ events 2016–2019**, Equifax 3.0 ⇒ historical, not an uncertainty range. **Post-on-ramp update exists:** Liberty Street **May 13 2025**, observed Q4'24→Q1'25: <620 −74 (3.2M), 620–719 −140 (2.0M), >720 −177 (0.4M), ≈ −105 weighted. −62 (FICO) stays the default. → `research/README_2026-10-28_research-items.md` §3.
13. **🆕 Pull the AFT Amended Complaint (Doc 50, Jan 15 2026) — it is FREE and has never been read.** Three servicer figures STUE cites (**280K overcharged**, the **~7×/>50× wait-time ratio**, the call-centre **"deflection"** pattern) are currently sourced to *Protect Borrowers / NCLC* summaries of this pleading. The pleading itself is downloadable from CourtListener/Internet Archive at no cost. **This is a source-quality upgrade, not new information** — but STUE's own rule says resolve claims on the docket, and it has been paraphrasing an advocacy paraphrase for months. *Also free and unread: Doc 47, the Sep-29-2025 Memorandum Opinion denying dismissal.* ✅ **READ 2026-10-28 at primary.** 280K excessive payments ✅ (Oct 2023, ¶4); 2.5M bills / >800K DQ ✅ but **Oct 2023**, not 2025 (¶120); call deflection ✅ (¶¶161–164); **~7×/>50× wait-time ratio ❌ NOT in the pleading** (cites ED Q4-2024 metrics only qualitatively). Doc 54 is free; JSR was due Sep 15 (unread, access gap). → `research/README_2026-10-28_research-items.md` §5.
14. **🔑 RE-INSTRUMENTED 2026-09-05 ON THE GOVERNING PRIMARY — and the new instrument is far better than the two it replaces.** Reading the **ED/Treasury Interagency Agreement (Mar 19 2026)** for the first time gives a **binary legal event**: **has Treasury REVOKED Education's May-11-2001 Cross-Servicing exemption** (31 U.S.C. § 3711(g)(2)(B); I TFM 3-5280; 31 CFR 285.12(d)(5))? **That is custody.** Its stated trigger is *"once **full operational capacity** has been reached"* — **a capability, not a date, which is exactly why #5 was unanswerable.** 🔧 **10/28: leg (b) REVERSED** — Treasury stood up and terminated (Jun 3) an Education PCA pilot with 5 collectors; the 9/5 null missed it on vocabulary. Exemption revocation still not observed. → `research/README_2026-10-28_research-items.md` §1.
   - **(a) OLD page-wording test → DEMOTED to corroboration.** Checked 9/5: page now stamped **`Last Updated: September 4, 2026`** with the *"helps ED collect"* language **unchanged** ⇒ consistent with **exemption NOT revoked**, and the old "page is stale" hedge is dead.
   - **(b) Vendor awards → NULL, VALIDATED** (USAspending: target terms n=0, controls n=10/1/7). Latest PCA capacity action is a **2025-05-18 bridge contract** — a stopgap, the opposite of a capacity build. **This is now the LEADING indicator for (a)**, since revocation is gated on operational capacity.
   - ⚠️ **CRITICAL SCOPE SPLIT the old framing got wrong:** pre-revocation, ED **may refer debts discretionarily** with Treasury's approval ⇒ **accounts can move WITHOUT revocation and without any public-page change.** Evidence against **custody** is **not** evidence against **any accounts having moved.**
   - ⚠️ **Custody ≠ enforcement, and now at primary:** *"the Cross-Servicing program will use only the tools **authorized by Education**."* AWG/TOP remain paused; **re-confirmed 9/5, 3rd consecutive STUCK.**
19. **🆕 Which SAVE notice-completion date is right — Dec 31 2026, or Aug 15 2026?** A secondary asserts servicer notices ran **"between July 1 and August 15, 2026."** **If true, the CRL-13 FULL-POPULATION read lands ~Nov 13 2026 — a full quarter earlier than the carried Q1-2027**, which would materially re-date CARL's docket. **Against it:** ED's own Mar-27-2026 release states **no end date**, and two servicer primaries contradict it (Nelnet → **Dec 31 2026**; MOHELA → **Jul–Oct 2026**). **Servicers send the notices, so servicer FAQs are the right evidence level.** ✅ **Arithmetic corroborates the carried framing at BOTH ends:** Jul 1 + 90d = **Tue Sep 29 2026** (matches the reported "no borrower moves off SAVE before Sep 29" exactly and matches the first-tranche catalyst); Dec 31 + 90d = **Wed Mar 31 2027** (matches "last deadlines ~end-Mar 2027"). **Carried framing STANDS; the Aug-15 claim is logged unverified, not banked.** → settle on a servicer primary (Nelnet/MOHELA FAQ re-read) before the Oct-1 first-tranche read. 🔧 **10/28: the frame shifted again.** Notices are servicer-specific (Edfinancial 7/1–8/15, MOHELA Jul–Oct, Nelnet to year-end; CARL KB-501), and ED reportedly added a **final 30-day notice** after a missed window (secondary). **The last auto-enrolments may land ~end-Apr 2027.** Still unsettled at primary. ✅ **RESOLVED 2026-10-28: servicer-specific, and "Aug 15" is Edfinancial's window** (Edfinancial 7/1–8/15 primary; **MOHELA Jul–Sep primary**; Nelnet to end-2026, secondary). Final notice confirmed at primary (MOHELA); its 30-day length is secondary ⇒ last auto-enrolments ~end-Apr 2027. → `research/README_2026-10-28_research-items.md` §2.
15. ✅ RESOLVED 2026-08-13 (count 7.90M → 9.00M like-for-like = 1.14×; does not rescue the level claim) → archive §C4.
16. **🆕 Does the FSA default count PEAK on schedule? — the one dated falsifier both instruments now agree on.** NY Fed flow into 90+ **leads** the FSA count by ~9 months (default = 360 days delinquent). That flow peaked **25:Q4 at 16.19%** and has collapsed to **7.83%** ⇒ **the count should top out ~FY2026 Q4 (quarter ending Sep 30 2026) near 10–11M, then decline.** **Compounding past ~11.5M into 2027 refutes cohort exhaustion on BOTH instruments and revives the level claim; rolling over on schedule resolves the episode as a large, fast, one-time normalization.** → next read **FSA FY2026 Q3** (quarter ended Jun 30 2026), due ~Sep. ⚠️ **Pull the archive file directly** — `studentaid.gov/sites/default/files/fsawg/datacenter/library/PortfoliobyLoanStatus.xls`, *Federally Managed* tab, *Cumulative in Default* — **do not wait for a press release or an EA announcement.** 🔧 **10/28: FY2026 Q3 = 9.30M (+0.3M); 271–360-day pipeline 0.66M ⇒ Sep-30 count roughly 9.5–10.0M, below the 10–11M band.** Rolling over looks earlier and lower than projected. Grade on the FY2026 Q4 file (~Dec).
17. ✅ ANSWERED 2026-08-13 (denominator padded; see § #17 ANSWERED) → archive §C4.
18. **🆕 🔴 Is the in-repayment population SELECTED? — the main threat to #17's answer, and the reason #17 is not fully closed.** The exposure adjustment assumes the ~38.5% still in active repayment is comparable to the ~53.8% of 2015–19. **It may not be.** ⚠️ **Argument it is FINE:** the 2024–26 forbearance block is largely **SAVE *litigation* forbearance** — borrowers parked administratively when the plan was enjoined, **not** selected for distress — so the residual should not be adversely selected. ⚠️ **Argument it is NOT fine:** the residual may be **positively** selected (borrowers who kept paying while others were parked), which would inflate the 10.95% relative to a like-for-like 2015–19 population and shrink the 1.37×. **Both directions are live and I cannot currently separate them.** **What would settle it:** the FSA repayment-plan file (`DLPortfoliobyRepaymentPlan.xls`, pulled and unexamined) shows plan mix over time — if the in-repayment residual is disproportionately **IDR**, that is evidence of *administrative* sorting rather than borrower quality; a shift toward **Level/Graduated** would suggest the opposite. ⚠️ **Register the prior: I expect selection to be MODEST and not to overturn a 1.3–1.4× gap — but I expected the wrong mechanism this morning too, so treat that expectation as weak.** Until #18 is worked, quote **#17's finding with its selection caveat attached**, never bare.

---

---

## BOTTOM LINE (blueprint §8 — rewrite EVERY session, plain language, no jargon)

**Where the domain is now:** The number of federal borrowers in default is still rising, but much more slowly. It reached **9.3 million ($234.1 billion) on June 30**, up 0.3 million in the quarter after 1.3 million the quarter before. The pipeline behind it is thinning: about **0.66 million** borrowers were 271–360 days late on June 30 and are the most that can default by September. That points to a **September count near 9.5–10 million**, below the 10–11 million peak I projected in August. This is consistent with the "one big cohort working through" reading; it is not proof of it.

**The single most important thing:** **The mass SAVE transition has not yet reached any data I can see.** The June 30 FSA snapshot was taken the day before the first notices went out. MOHELA complaints are running about **25 a day in October**, well under the 35/day yellow line and under half of the 55/day level CRL-28 needs, now that its window is open. The real tests are the **NY Fed third-quarter report (~Nov 4–5)**, the **final MOHELA complaint grade (~Nov 13–16)**, and the **FSA September-30 file (~December)**.

**Where my own instruments fell short tonight:** The forbearance check landed on its yellow line and the published rounding cannot say which side, so I report **no verdict** rather than pick one. The cure-channel check **cannot be graded at all** this quarter, because nobody published a gross count of new defaults, and the substitute I tried failed a consistency check. The school-closure list is still unreadable. The complaint-boundary rule **did pass its first test on fresh data**, but that is one test.

**What changed outside the data:** Treasury and Education opened an online **Defaulted Loans Support Center on Sep 30**, which is a rehabilitation portal, not a collections restart. **Wage garnishment and tax-refund offsets remain paused**, and reports of private collectors coming in November are plans, not announcements. Borrowers who miss their 90-day SAVE window reportedly now get a **final 30-day notice**, which would push the last forced switches from roughly end-March to end-April 2027. That comes from news reports, not the Education Department's own page. The **Sweet contempt hearing is Nov 5**.

**Added later 10/28, from the research pass:** Treasury did start building student-loan collections. It hired five private collection agencies for an "Education pilot" in late May 2026 (about $40 million obligated), then **cancelled all five contracts on June 3** before they ran. My September check had called that search clean; it was looking for the wrong words. Collections are still paused, but the contracting machinery exists and can be re-used quickly, so a restart would most likely show up first as new orders under those same five agreements.

**What would change my mind:** If the September-30 default count comes in **above ~10.5 million**, or the NY Fed flow into 90+ stops falling, the exhaustion reading is wrong. If MOHELA complaints jump toward 45–55 a day as auto-enrolments land in November, the servicer-failure mechanism I have been close to calling dead is alive.

*(Rewritten 2026-10-28. Prior version 2026-09-05.)*

---

*Sub-agent of CARL. Parent is system of record for CRL-04/05/13/28 (CRL-14 retired 7/31, superseded by CRL-28) — STUE keeps no own predictions ledger. Latest state vector: **SV-STUE-2026-10-28-01**. Expected-signals register: `workbook/EXPECTED_SIGNALS_TRACKER.md`.*
