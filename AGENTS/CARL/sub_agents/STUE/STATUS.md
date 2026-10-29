# STUE STATUS

**Last Updated:** 2026-10-28 ~21:00 ET (**53-day dark gap closed: FSA FY2026 Q3 graded (ES-01/04/06), ES-02 boundary rule's first out-of-sample run, news sweep, 2 CARL inbox packets processed**) | **Data vintage:** FSA `PortfoliobyLoanStatus` + companion files **Last-Modified Fri 18 Sep 2026** (data as of **Jun 30 2026** = FY2026 Q3; MD5 `d443da74…` matches CARL's 9/24 copy); CFPB `company=MOHELA` settled through **Oct 16 2026** (pulled 10/28, vintage 2026-10-28); Treasury release sb0639 **Sep 30 2026**; AFT v. ED docket (CourtListener) through **Oct 15 2026**; Sweet via PPSL/secondaries through **Oct 15 2026**; NY Fed 2026:Q3 HHDC **not yet posted** (data URL 302 on 10/28) | **Status:** 🔴 CRITICAL, unchanged. **No registered threshold fired.** The default stock is still rising but slowed to roughly a quarter of the prior quarter's pace, and the servicer-complaint signal stays well below its bands inside CRL-28's now-open window.

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

> 📌 **[ROTATED 2026-10-28 → `archive/STUE_STATUS_ARCHIVE_2026-10.md` §C1, 14310 B, CRC32 `1c2ff88e`]** The 9/5 session block (23-day gap closed; ES-02 second null; FSA not yet posted; the ED/Treasury IAA read at primary; Sweet contempt motion). Every figure still live is in § SIGNAL DASHBOARD.


> ⛔ **[ROTATED 2026-09-05 → `archive/STUE_STATUS_ARCHIVE_2026-09.md` §B1]** The 8/13 🔴→🟠 downgrade that was written and withdrawn within the same session after Will challenged the baseline. **Superseded by § #17 ANSWERED, which is still here.** Status stayed 🔴 and still is.

>
> 📌 **[ROTATED 2026-09-05 → archive §B2]** The 8/13 session narrative (Q2 HHDC folded on an independent pull; Treasury + AFT catalysts both closed; the S4 Pg-14/Pg-28 divergence). **All of its live figures are carried in § SIGNAL DASHBOARD** — 10.60% stock, 7.83% flow (Pg 14, never 7.44%).
> 📌 **[ROTATED 2026-09-05 → archive §B3]** The 8/10 closeout — three inbox packets processed; both catalyst checks returned INCONCLUSIVE. Both were closed on 8/13.
> 📌 **[ROTATED 2026-09-05 → archive §B4]** The 7/31 closeout, news sweep and coherence pass — nine defects fixed, five tracing to one root cause (mutable data duplicated with no declared owner). **The durable outputs of that session are still live here and in `CLAUDE.md`:** the inbox, the spawned-mode boot card, the Doc-Ownership table, the two-clock ledger headers, the unrepresentable-shock register and the expected-signals register.

---

## ⚠️ WHAT CHANGED — Jun 9 → Jul 25 2026

**[ROTATED 2026-09-05 → `archive/STUE_STATUS_ARCHIVE_2026-09.md` §B5]** The 8-row session-diff table for the 46-day Jun-9→Jul-25 window (default wall re-anchored to ~9M/$220B; stock-vs-flow reconciled; SAVE notice window compressed; AFT stay discovered; the May-28-conference retraction; wave-1 no-spike; cascade re-scope; two stale-vintage traps). **Every value it established that is still current lives in § SIGNAL DASHBOARD.**

---

## THESIS

Federal student loan stress remains a **mass credit-destruction event in active execution**, and the *accrual* mechanism is firing exactly as modelled: the default stock went **6.0M (Aug 2025) → 7.7M (Dec) → 9.0M (Mar 2026) → 9.3M (Jun 2026)** on primary FSA data, with 2.6M gross DRG transfers in calendar Q1 alone. ⚠️ **10/28: the accrual is decelerating hard** (+1.3M then +0.3M net per quarter), consistent with the cohort-exhaustion reading on the NY Fed flow. CRL-04 is **CONFIRMED clean** at 10.3%.

---

### ⚑ WHY THE DOWNSTREAM LOOKS QUIET — four-channel decomposition

**[ROTATED 2026-09-05 → archive §B8 — already marked ⛔ SUPERSEDED on 8/13.]** Will's framing that only ONE of four channels is genuinely "not firing yet": **forbearance→default conversion is a real lag (earliest ~Jul 2027); enforcement is BLOCKED not pending; servicer attribution gets WORSE via settlement; the CC cascade was arithmetically too small (~2% of card balances) to ever carry it.** ⚠️ **That decomposition is still the right map and is retained verbatim in the archive** — it was superseded only as a *discriminator*, because the Q2 print it pointed at contains zero post-transition borrowers. **First readable cascade signal is 2027:Q1 HHDC (~May 2027).** See also § CHANNEL 5 (FHA/mortgage), which is live and stays here.

---

What the 7/25 session changed is **not the mechanism but the enforcement and attribution legs**:

1. **Enforcement is gated in two independent places.** Involuntary collections remain **paused indefinitely** (Jan 16 2026, no corroborated restart), and the accountability channel — AFT v. MOHELA — is under a **court-ordered stay with discovery frozen**, with no class-certification motion filed. Neither can produce a Q3-Q4 2026 event. CRL-14's "MOHELA-caused defaults" leg therefore rests on **operational failure**, not litigation or garnishment.
2. **Attribution is narrower than STUE previously asserted.** The score cascade is real and severe *within* the affected cohort but is **second-order in aggregate** — it cannot carry a CC 90+ GFC breach on its own (DEWEY C2). Carrying the broad version into the 8/15 print would contaminate the CRL-05 grade.
3. **The transition timeline tightened.** Notices complete Dec 2026 (was Mar 2027); final selection deadlines ~Mar 2027. The **first-tranche read is still ~Oct 1**, but the full-population N now lands **earlier and more compactly** — which *improves* CRL-13's readability at Q1 2027.

**v2.5.1 thesis: ⚠️ INTACT AS OF 7/31, but see § THE BASELINE PROBLEM (8/13) — the level claim underneath it is contested in BOTH directions and is not settled.** The Q2 HHDC grader **has fired (Tue Aug 11)**; ~Oct 1 (CRL-13 first tranche) is the next.

> ⛔ **[ROTATED 2026-09-05 → archive §B6]** The Q2-HHDC advisory-watch blockquote, already marked SPENT — the event it forecast happened Tue Aug 11 2026. **The two lessons that outlived it are kept:** with 3-of-N support publish the BAND and treat the mode as colour; and **poll the deterministic data URL (`HHD_C_Report_<YYYY>Q<N>.xlsx`, curl + browser UA), never hunt for a media advisory.**

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
| Transition rate INTO 90+ DQ (4Q moving sum) | ⛔ **SUPERSEDED by the two flow rows above** — this row was the Pg-28 by-age cut. At Q1 it was indistinguishable from Pg 14 (10.86 vs 10.8609); at Q2 the two diverge, so the series is no longer a safe stand-in. **Do not refresh this row; read Pg 13/14.** | Q1 2026 (last valid) | NY Fed Pg 28 | ⛔ retired 8/13 |
| Active repayment 31+ DQ (by $) | **15.7%** (Dec 2025 was 18.6%) | Jun 30 2026 | FSA GENERAL-26-57 + FM delinquency sheet | 🔴 |
| Projected default EOY 2026 | 13M (TCF). **The current pace (+0.3M/qtr) and the 0.66M late pipeline imply ~10M, so 13M looks unreachable without a new inflow** (SAVE auto-enrolment defaults cannot arrive before ~2027) | Projection | TCF / STUE | 🟢 **TCF figure looks too high** |
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
| — MOHELA | Notices **Jul → Oct 2026** [MOHELA SAVE FAQ, primary] | 🔴 |
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
| MOHELA missed bills | **2.5M missed → 800K DQ** (cumulative, 2025) | 🔴 |
| MOHELA call wait / abandon | **~13 min avg wait, ~14% abandon** — longest of the major federal servicers; no peer exceeds ~5% [FSA servicer data] | 🔴 |
| **CFPB complaints — MOHELA, monthly 2026** | Jan **912** · Feb **681** · Mar **905** · Apr **909** · May **704** · Jun **815** · Jul **895** · Aug **709** · Sep **682**. YoY: Jul 2025 771 · Aug 602 · Sep 651 · Oct 652. ⚠️ **VINTAGE 2026-10-28**, a revisable series (Jul was 883 at the 9/5 vintage); re-pull and re-locate the cliff before comparing vintages | 🟢 at or below baseline |
| **MOHELA daily rate — the ES-02 / CRL-28 instrument** | **CRL-28 window Oct 1–16 (settled, D = Oct 16 by the rule): 396 = 24.8/day.** Sep 22.7/day. Bands **Y >35 · O >45 · R ≥55** (CRL-28 frozen) ⇒ the print is **45% of R**. Interim in-window read; **the grade is ~Nov 13/16** | 🟢 **below Y** |
| ⚠️ Instrument note | The **"5–6 day lag" rule is RETIRED**. The pre-registered completeness test **passed its first out-of-sample run on 10/28**: it chose Oct 16 against an eyeball cliff at Oct 18, so it was conservative, and the band was unchanged at D±3. Cliff distance was ~10 days (vs ~14 on 9/5) | 🟡 **n=1 out-of-sample** |
| **AFT v. MOHELA** | **D.D.C. `1:24-cv-02460` (Chutkan) — STAYED, in settlement negotiation, discovery frozen since 10/27/2025.** Last filing **Doc 54, Jul 17 2026**; MTD denied + remand denied **Sep 29 2025**; **no class cert ever filed** | 🔴 **settlement-gated** |
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
| Vendor build-out (OQ#14 leg b) | **Not re-run 10/28.** 9/5 null (USAspending, target terms n=0, controls fire). Press (Washington Sun 10/19, via IBTimes) reports Treasury plans to hire private collectors "possibly November", so **re-run USAspending at the next session** | 🟠 |
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
| **9th Cir appeal (26-1136) — ✅ DECIDED Fri Jul 17 2026, DOE LOST, UNANIMOUS** | **STUE MISSED THIS IN THE 7/25 REFRESH — it fired 8 days before that session.** Panel **Wardlaw / Owens / Bress** unanimously rejected DOE's appeal to delay relief for **>170,000 post-class applicants**, affirming the district court: DOE **failed to show the "changed circumstances"** legally required to modify a settlement it signed in 2022, and "knew exactly what it was signing up for." Prior STATUS carried *"no oral argument scheduled, ~Sept projected, watch-only"* — the court ruled without one. Briefing had completed **May 7 2026** *(also corrected 7/31 from a "2025" year typo)*. Earlier published order **3/25/26** denied DOE's stay bid; this is the merits loss. | 🟢🔴 **RESOLVED — DOE lost** |
| — scale, disaggregated | **>500K** borrowers / **≥$23B** = the **whole 2022 settlement** · **~200K** = original settlement class · **>170K (DOE knew of >205K by Feb 2023)** = **post-class applicants, the cohort THIS ruling covers** · **>210K** = a *separate* borrower-defense backlog · **>1,000** class members still awaiting relief already owed. ⚠️ **Headlines say "500,000" — that is the settlement total, NOT this ruling's cohort. Do not cite 500K as the 7/17 number.** | ⚠️ figure-conflation trap |
| — what's left | ~~**DOE has not said whether it will appeal; the only remaining stop is SCOTUS.** No stay in place → **automatic discharges are proceeding.**~~ 🔧 **QUALIFIED 2026-09-05 — entitlement is settled, DELIVERY is now formally contested.** No cert petition found in any source this sweep (PPSL's own page reports none) ⇒ **leaning NO but unresolved — no deadline stated.** **The live action has moved from the appellate tail to district-court ENFORCEMENT** | 🟠 **re-opened** |
| 🆕🔴 **Aug 18 2026 — PPSL moved to ENFORCE the settlement AND to hold ED in CONTEMPT with sanctions** | Verified at the PPSL primary (the search summary that surfaced it was truncated — resolved at source per STUE's own rule). **At least 807 Sweet CLASS members are still awaiting discharges or refunds ED was legally required to provide by deadlines "that have long since passed"; some "more than a year and a half" overdue.** ⚠️ **PERIMETER — this file has a standing conflation trap on this case: 807 = original-CLASS members with OVERDUE relief.** NOT the **>170K** post-class cohort of the 7/17 ruling, NOT the **~200K** class, NOT the **>500K / ≥$23B** settlement. **Small in count, large in legal significance — a contempt predicate, not a population estimate** | 🔴 **NEW — ED compliance contested** |
| — status 10/28 | **Fully briefed** (plaintiffs' replies Oct 15 2026); **hearing Thu Nov 5 2026**; no ruling [PPSL case page via search, docket not read] | 🟠 **ruling pending** |
| — ⚠️ date-conflict note | Forbes 7/21 (Minsky) dates the ruling **"Friday, July 18"** — **July 18 2026 is a SATURDAY.** PPSL (7/23 release) and The College Investor both say **July 17**, which **is** a Friday. **7/17 is correct**; the weekday check broke the tie. *(Second time in two sessions the same `date` check caught a bad date — see the 8/15 HHDC catch.)* | 🔧 |

### SLABS / ES-STUE-05 — 🆕 **FIRST CHECK EVER (2026-09-05).** Registered prior CONFIRMED
*(VALUES + POINTERS. Working → § DASHBOARD BODY §D3.)*

| Metric | Value | Status |
|--------|-------|--------|
| **Instrument** | **SLM Student Loan Trust 2014-2 (Navient), Form 10-D filed 2026-09-04**, collection period **Jul 1–31 2026**, distribution date 8/25/2026 [SEC EDGAR primary] | ✅ **live route found** |
| **Credit loss — the registered question** | **Cumulative non-reimbursable losses $4.16M on a $964.9M original pool = 0.43%.** Period losses **$23,560** | 🟢 **DID_NOT_APPEAR — prior CONFIRMED** |
| Credit enhancement | **Parity ratio 1.00999** (prior 1.01010) · overcollateralisation **$1.79M** · **reserve funds utilised $0.00** | 🟢 **no CE breach, no draw** |
| ⚠️ **But the pool IS deeply stressed — in CASH-FLOW terms, not credit** | Only **63.83% current**. **31+ delinquent 13.50%** · **forbearance 16.47%** · deferment 5.62% · claims in process 0.49% ⇒ **~36% of the pool is not paying normally** | 🟠 |
| ✅ **The registered MECHANISM is confirmed, not just the direction** | **Since-issued CPR −40.02%** — *negative* prepayment, i.e. **EXTENSION.** STUE registered FFELP exposure as *"extension / prepayment / liquidity, NOT credit"* **before looking. That is exactly what the tape shows** | 🟢 **mechanism confirmed** |
| 🔧 **Bucket shape — AGING WITH NO CURE. ⚠️ NOT an exhaustion test (claim DOWNGRADED 2026-09-05)** | 31–60 DPD fell **4.204% → 2.978%** while 61–90 rose **2.814% → 3.279%** and 91–120 rose **1.410% → 1.932%** — **the early bucket drained INTO the aged buckets.** ⛔ **This is CONSISTENT WITH delinquency aging and an absence of cure. It is NOT independent corroboration of COHORT EXHAUSTION** — that needs an **inflow / cohort-flow** measure, and a bucket-mix shift over **one month** is not one. ⚠️ **And the populations differ:** this is a **legacy FFELP pool**, not the ~9M defaulted federal cohort — **STUE's own scope note says exactly that**, so using it to corroborate a federal-cohort finding is a **population mismatch**. *(I wrote "independent corroboration… on a completely independent instrument." The INSTRUMENT is independent; the POPULATION is not the subject. Caught by Codex.)* | 🔧 **downgraded** |

### Collections Status
| Metric | Value | Status |
|--------|-------|--------|
| Involuntary collections (AWG + Treasury Offset) | **PAUSED since Jan 16 2026; no restart verified at any primary** (re-checked 10/28, 4th consecutive STUCK). Press reports collections "in 2027"; a MoneyWise 10/27 "garnishment next month" claim is unsupported and conflicts with it | 🟡 **STUCK** |
| 🆕 **STRUCTURAL CORROBORATION — the restart switch stays with ED even after custody moves** | ED/Treasury IAA (Mar 19 2026), read at primary 9/5: *"The Cross-Servicing program will use **only the tools authorized by Education**, as specified in the Cross-Servicing Agency Profile(s)."* ⇒ **a Treasury custody transfer does NOT itself restart AWG/TOP.** ⚠️ **But the plumbing is specified and being built with the switch off** — the IAA lays out the full AWG process (NOI letter → hearing → AWG order *"generally between 31 and 60 days after sending the NOI letter"*). **When ED authorizes it, that 31–60 day NOI→order gap is the usable lead time.** | ⚠️ **watch the AUTHORIZATION, not the custody** |
| Reported expectation | **Press: private collectors possibly from Nov 2026, involuntary collections in 2027** (Washington Sun 10/19 via IBTimes). No ED/Treasury commitment | 🟠 |
| Borrowers exposed | 5M+ in default at pause; ~9M now | 🔴 |

> **Corrected 7/25:** the prior "Expected Restart **Jul 2026** 🔴 IMMINENT" row was wrong and contradicted the parent. July passed with no restart. Threshold **STUCK**, mechanism (default accrual) **intact** — matches parent CRL-14 split.

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

## ⚠️ THE BASELINE PROBLEM — a base-rate check, and its partial retraction (2026-08-13, both halves same session)

> **Read this section as a corrected finding, not a finding.** The original claim — *"student 90+ DQ has not exceeded its pre-pandemic level, it is BELOW it"* — **rested on a baseline that does not hold up.** Will asked whether the comparison years were themselves elevated. **They were.** What follows keeps the original working, then the correction, then what actually survives.

### 🔴 THE CORRECTION — the 2015–19 baseline is a contaminated PEAK, not a norm

**The series roughly DOUBLED and then plateaued. I compared today against the plateau and called it "normal."**

| Window | Student 90+ share | What it is |
|---|---:|---|
| 2003–2007 | **6.66%** | before the for-profit boom |
| 2008–2011 | **8.42%** | GFC + enrollment surge climbing |
| 2012–2019 | **11.01%** | ⚠️ **the plateau — the top of a decade-long climb** |
| *2015–2019 (the window I chose)* | *11.12%* | ⚠️ **the highest sub-window available** |
| **26:Q2 (now)** | **10.60%** | **+3.94pp vs 2003–07 · +2.18pp vs 2008–11 · −0.52pp vs 2015–19** |

**Same number, three baselines, opposite conclusions. That is window selection driving a headline.**

**The structural cause is documented, not speculative.** For-profit college enrollment peaked in **2010 at ~2.4M (~11% of all students)** and **fell ~50% by 2020**; for-profits enrolled **~10% of students but accounted for ~50% of all defaults**, with ~14.7% three-year default rates. Those cohorts entered repayment **2012–2016** — exactly the climb-and-plateau window. Corinthian collapsed 2015, ITT 2016. **The 2012–19 level embeds a high-risk cohort that no longer exists at anything like that size**, so it is the wrong counterfactual for a 2026 portfolio. [NCES/Digest via search; PPSL; Senate HELP for-profit report]

### ❌ WITHDRAWN — the trend-extrapolation claim

**"The default count is −16.2% below its pre-pandemic trend" is withdrawn.** I fitted a line to FY2016 Q4–FY2020 Q2 and pushed it 24 quarters forward. **Two things make that invalid:** (a) that slope was itself produced by the for-profit cohort accumulating into the default stock — **extrapolating a one-time cohort's wash-through for six more years is exactly the wrong operation**; and (b) **the slope was already decelerating** when I fitted it — **+0.120 → +0.100 → +0.090 M/qtr** across FY2017/18/19, YoY increments **+0.50 → +0.50 → +0.40M**. A decelerating series extrapolated linearly overstates the counterfactual by construction. **The direction may survive; the number does not, and the false precision of "−16.2%" was the worst thing in the original write-up.**

### ✅ WHAT ACTUALLY SURVIVES

1. **The FLOW comparison is the most robust leg, because flow is not contaminated by accumulated stock.** New 90+ delinquencies: **7.83%** today vs **10.10%** (2012–14 peak), **9.51%** (2015–19), **8.11%** (2008–11), **6.94%** (2004–07). **Today sits at roughly 2008–2011 levels — below every year from 2010 to 2019, and above the mid-2000s.** ⚠️ **But "below the entire pre-pandemic range" was still cherry-picked** — it was below the *2015–19* range; against 2004–07 it is **+0.89pp**.
2. **The pre-pandemic flow was already declining** — 2012–19 trend **−0.037pp/qtr** — consistent with the for-profit cohort washing out. **A falling pre-COVID trend makes today's low flow less surprising, not more.**
3. **The instrument identification stands** (FSA Federally Managed *Cumulative in Default* = 9.00M/$220.3B, matching the cited headline) and **so does the perimeter error** — the "~5M ⇒ 1.8×" framing really does mix Direct Loan against Federally Managed.
4. **The SPEED finding is untouched by any of this**: +3.8M in two quarters, ~16× the pre-pandemic pace, off a stock drained to 5.2M.

### 🧭 WHERE THAT LEAVES THE LEVEL QUESTION: **genuinely open**

**There is no clean baseline, and that is the actual finding.** Every candidate window is contaminated: 2012–19 by the for-profit boom; 2003–07 by a much smaller, less-indebted portfolio; and *all* pre-2020 windows by the fact that **income-driven repayment, PSLF, and Fresh Start have since changed the mechanics of how a struggling borrower shows up in these series at all.**

**So: today's 10.60% is clearly far above the mid-2000s and clearly at-or-just-below the for-profit-era plateau. Whether that constitutes "crisis" requires a composition-adjusted counterfactual that has not been built.** → open question **#17**, now the highest-value analytical work in the domain.

> ### 🔴 CLOSING NOTE — **the fleet was told in May. It was logged, marked INTEGRATED, and not acted on.**
>
> Found 2026-08-13 while running the publisher-side consumer check before commit — i.e. **by a routine closeout step, not by insight.**
>
> **`BOARD/SIG-W-20260513-002` (WALTER, 2026-05-13) says it in its own HEADLINE:** *"NY Fed Q1 2026 HHDC — **Student-Loan 90+d 10.3% Back to Pre-Pandemic**…"*, and again in the body: *"Student loan 90+d: 10.3% — **back to pre-pandemic level**."* **`AGENTS/CARL/board/BOARD_LOG.tsv:139` dispositions it `INTEGRATED` on 2026-05-22 and transcribes the phrase verbatim into the disposition text.**
>
> ⚠️ **So this was never an information gap. It was a REASONING gap.** The datum arrived, was recorded accurately, was marked integrated — **and for three months both STUE and CARL went on treating `>10%` as a breach threshold while their own ledger held the sentence that undercuts it.**
>
> **The transferable failure: `INTEGRATED` means TRANSCRIBED, not REASONED ABOUT.** A descriptive phrase in an inbound signal — *"back to pre-pandemic"* — was copied into a log and never converted into the obvious question it implies: *then why is our threshold set below that level?* **Nothing in the disposition workflow asks whether an integrated fact CONTRADICTS a standing threshold.** `[[finding_record_of_an_action_is_not_the_action]]`
>
> 🔧 **This also corrects my own framing from earlier today.** I wrote that this was a check "nobody ran" and that the comparison "was one arithmetic step away the whole time." **The stronger and truer version: it was ZERO steps away — it was already written down, in a signal we had marked integrated.** Credit where due: **WALTER's signal had it right in May.**

> **The lesson, logged against myself:** the morning's finding came from asking *"compared to what?"* — which was the right question. **The afternoon's correction came from asking it one level deeper: "and was THAT period normal?"** I stopped one step short, and the stopping point happened to be the window that made the finding strongest. **A baseline that makes your result dramatic deserves the same scrutiny as a result that makes your baseline dramatic.**

**Student 90+ balance share, full NY Fed history (2003–2026, n=94 quarters):**

| Era | Student 90+ stock | Note |
|---|---:|---|
| 2015–2019 mean | **11.12%** | the pre-pandemic normal regime |
| 2019 mean | **10.91%** | last clean pre-COVID year |
| **All-time max** | **11.83%** (13:Q3) | — |
| 2023–2024 mean | **~0.6%** | ⚠️ **the ANOMALY** — reporting pause / on-ramp, not borrower behaviour |
| **26:Q2 (now)** | **10.60%** | **below 2019, below the 2015–19 mean, 1.23pp below the all-time high** |

**The series sat continuously above 10% for 31 consecutive quarters — 12:Q3 through 20:Q1.** Only **3** quarters since 2025 are above 10% (25:Q2, 26:Q1, 26:Q2). Current level is at the **66th percentile** of its own 23-year history.

**The flow tells the same story.** Pre-pandemic 2015–19 flow into 90+: **mean 9.51%, range 8.59–10.27%.** Now: **7.83% — below the entire pre-pandemic range.**

**And in dollars, the "wall" is smaller than 2019 in real terms:**

| | 19:Q4 | 26:Q2 | change |
|---|---:|---:|---:|
| Student balances | $1.508T | $1.651T | **+9.5%** |
| 90+ balances | **$166.8B** | **$175.0B** | **+4.9% nominal** |

**90+ dollars grew HALF as fast as the book over 6.5 years — i.e. materially DOWN in real terms.**

### ✅ **OPEN QUESTION #15 RESOLVED SAME SESSION — the default COUNT does not rescue the level claim either** (2026-08-13, FSA archives pulled)

**Instrument identified exactly.** FSA `PortfoliobyLoanStatus.xls`, **Federally Managed** tab, *"Cumulative in Default"* — official definition: **loans more than 360 days delinquent**, quarterly by federal fiscal year (FY2026 Q2 = quarter ending **Mar 31 2026**). **It reads 9.00M recipients / $220.3B — matching STUE's cited "~9.0M / $220B" exactly.** Same file's forbearance column reads **8.40M**, also matching. **This is definitively the series behind the headline claim.**

| Measure (Federally Managed) | Pre-pandemic PEAK (FY2020 Q2 = Mar 31 2020) | **Now (FY2026 Q2)** | Ratio |
|---|---:|---:|---:|
| Borrowers in default | **7.90M** | **9.00M** | **1.14×** |
| Dollars in default | **$171.5B** | **$220.3B** | **1.28×** |

⛔ **THE TREND-EXTRAPOLATION CLAIM THAT STOOD HERE IS WITHDRAWN — see § THE BASELINE PROBLEM.** It read: *"the series rose linearly at +0.119M/quarter through FY2016 Q4–FY2020 Q2, so the counterfactual for today is **10.7M / $295.4B**, making actual **−16.2% / −25.4% below trend** — had the pandemic never happened there would be MORE borrowers in default today than there are."*

**Why it is withdrawn:** that slope was **produced by the for-profit cohort accumulating into the default stock**, and it was **already decelerating** when fitted (+0.120 → +0.100 → +0.090 M/qtr across FY2017/18/19). Extrapolating a decelerating, one-time-cohort-driven slope 24 quarters forward is invalid. **The 1.14× / 1.28× ratios above are measurements and stand. The counterfactual was a construction and does not — do not carry −16.2%.** *(Direct-Loan-only tab: the **1.24× ratio** — 5.80M → 7.20M — stands as a measurement. ⚠️ **Its companion "−18.2% vs trend" is WITHDRAWN on the identical grounds** and was missed in the first retraction pass, caught at closeout: **a retraction has to sweep every sibling figure the same construction produced, not just the one that was quoted in the headline.**)*

> 🔧 **MY REGISTERED PRIOR WAS WRONG, AND THE ERROR IS THE USEFUL PART.** I registered *"pre-pandemic defaults ran ~5M and rising, so ~9M may be a genuine ~1.8×."* **The ~5M is the DIRECT LOAN series; the 9.0M is FEDERALLY MANAGED (Direct Loans + ED-held FFEL).** Setting a 9.0M numerator against a ~5M baseline is a **perimeter error** — and it manufactures a "defaults nearly doubled" headline out of two different populations. **Like-for-like it is 7.9M → 9.0M.** `[[finding_cross_entity_comparison_needs_same_perimeter]]`. **This is the confound I predicted definitionally and then walked into anyway** — which is why the prior gets written down *before* the pull.

### ⚠️ What DOES survive, and it is real: **the SPEED, not the level**

**The stock was drained, then refilled.** Payment pause + Fresh Start cures pulled it from **7.90M (Mar 2020) down to 5.20M (Sep 2025)** — a monotonic 22-quarter decline. Then: **5.2M → 7.7M → 9.0M in two quarters (+3.8M).**

**That two-quarter rate is genuinely without precedent in the series.** Pre-pandemic the stock moved **+0.12M/quarter**; the last two quarters ran **~+1.9M/quarter — roughly 16×**. ⚠️ **But it is mechanically a catch-up pulse, not a new regime:** the 360-day clock makes everyone who stopped paying when the on-ramp expired cross the threshold *together*. **A reservoir refilling fast is not the same as a reservoir overflowing.**

### 🔮 The two instruments now make ONE dated, falsifiable prediction — proposed to CARL

The NY Fed **flow into 90+** is a **leading indicator** of the FSA default count, because default = 360 days delinquent ≈ **~9 months after** a loan hits 90+. That flow **peaked at 16.19% in 25:Q4** and has since collapsed to **7.83%**.

⇒ **The FSA default count should PEAK around FY2026 Q4 (quarter ending Sep 30 2026) — roughly 10.5–11M — and then DECLINE.** *(9.0M now + a decaying inflow, with the 25:Q4 flow peak landing ~Sep 2026.)*

**This is the cleanest falsifier the domain has.** If the count keeps compounding past ~11.5M into 2027, cohort exhaustion is wrong on both instruments and the level claim revives. If it rolls over near ~10–11M on schedule, **the entire episode resolves as a large, fast, one-time normalization** — severe for the individuals caught in it, and not a systemic consumer break. → **next read: FSA FY2026 Q3 (quarter ended Jun 30 2026), due ~Sep.**

### ⚠️ What this does to CRL-04 — routed to CARL, parent decides

**CRL-04 is "Student 90+ DQ >10%", carried at 98% CONFIRMED.** The threshold **does not discriminate between crisis and the pre-pandemic norm** — the series was above it for 31 straight quarters ending Q1 2020. **A prediction that it returns above 10% after an artificial suppression ends is close to a certainty that carries almost no information about consumer stress.** The 98% was arguably right for the wrong reason: near-certain because **the reporting pause was ending and the series had to revert**, not because the consumer was breaking. `[[finding_base_rate_the_threshold_before_building_it]]` · `[[finding_threshold_level_is_a_measurement_not_a_constant]]`.

### ✅ What SURVIVES — stated fully, because the finding is easy to over-read

1. **The credit-score destruction is real, large, and already banked.** It is a **FLOW** event, not a level event: going 0.53% → 10.60% in five quarters means an enormous number of borrowers had a delinquency **newly reported**. The −62pt average drop (FICO) happened. **Whether the resulting level is historically normal has no bearing on whether those borrowers were damaged** — and they were.
2. ~~**The borrower-count default stock (~9.0M, FSA) is a DIFFERENT metric** and has not been base-rated.~~ ✅ **RESOLVED SAME SESSION — and it does NOT rescue the level claim.** Like-for-like, **7.90M (pre-pandemic peak) → 9.00M = 1.14×** — but ⚠️ **that baseline is contaminated too** (see § THE BASELINE PROBLEM), and the *"−16.2% below trend"* claim that sat here is **WITHDRAWN**. **What survives is the SPEED (+3.8M in two quarters, ~16× the pre-pandemic pace) — a refilling reservoir, not an overflowing one.**
3. **8.4M in forbearance have not converted.** The level can still rise; nothing here says the ceiling is in.
4. **Composition differs** — average new-defaulter age 38.9 vs 36.4 pre-pandemic. Same rate, different people.

### ❌ What must STOP being asserted without this context

- ❌ **"90+ DQ has breached its GFC/historic level."** It has not. It is **below** 2013–2019 and below the 2013 peak.
- ❌ Presenting **10.60%** as evidence of unprecedented stress **without stating the 2015–19 mean of 11.12%** beside it. A number this close to its own normal cannot be quoted bare.
- ❌ Reading the **flow collapse** as merely "decelerating." It has **undershot** the pre-pandemic range — which strengthens cohort exhaustion considerably beyond what the 8/11 packet claimed.

> **Why this went unseen for months:** every STUE surface compared Q2 to **Q1**, and Q1 to **Q4**, against thresholds set in **2026**. **Nothing ever compared the level to the era before the anomaly** — and the 2020–2024 near-zero was so obviously abnormal that it quietly became the mental baseline. **The comparison that mattered was to 2019, and it was in the same file, one column over.**

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
| **~Oct 31** | MOHELA notice waves complete — **this is the EVENT, not the grade** | The condition ES-02's third look is waiting on. ⚠️ **Do NOT pull on this date.** *(Weekday check, per standing rule: **Oct 31 2026 is a SATURDAY** — fine for a completion milestone, but it is not a release date and must never be treated as one.)* |
| **~Fri 2026-11-13 / Mon 11-16** | 🔴 **ES-02 THIRD AND FINAL LOOK — the actual GRADE date** (DOCKET L150) | ⚠️ **CORRECTED 2026-09-05 (PROME/Codex):** the surfaces previously called **Oct 31 itself** the "third and final look." **Wrong, and wrong by STUE's own cliff finding** — the settled boundary runs **~14 days behind the pull**, so a pull on Oct 31 reads data settled only to ~Oct 17 and **cannot see notice completion at all.** The boundary reaches Oct 31 around **~Nov 14**. **Grading a completion event before the data covering it is settled is exactly the error the lag work exists to prevent** — and it very nearly propagated into the row that decides CRL-28's STUCK→MISSED question |
| **(see re-dated FSA row above)** | *(the ~Sep row moved up and is now header-triggered, not calendar-triggered)* | Default stock 2nd print; settles the 9.0M vs 9.5M press gap; refreshes the stale 18.6% active-repayment DQ |
| ~~**Sep 30 2026**~~ **→ Dec 31 2026 (EXTENDED 9/29 by ED; read by CARL 10/01, KB-CARL-500)** | RAP auto-pay enrollment deadline — **1% interest-rate reduction through Jun 30 2028** for borrowers enrolled in auto-pay by this date [ED; Edfinancial page PRIMARY 10/01: 'on or before 11:59 PM ET on 12/31/2026', Direct Loans originated on or after 7/1/2012; ~2M new enrolments per ED 9/29] | 🆕 *added 7/31.* Marginally **relieving** on payment burden; a partial offset to the $0→~$407/mo shock. Small, but it is the only easing mechanism in the transition |
| ~~**~Sep 29 – Oct 1**~~ **READ 10/01 by CARL: NO GRADEABLE DATA** | **SAVE→RAP first-tranche non-selection read** | **CRL-13 partial N — no wave-level count exists in public (KB-CARL-501); CRL-13 OPEN 75% unchanged. Notice windows are servicer-specific (Edfinancial 7/1–8/15, MOHELA Jul–Oct), so the 'Department-wide 12/31' inference is withdrawn. First proxy: FSA Data Center 9/30-data refresh ~mid/late Dec 2026; AFT v. ED status conference 10/14.** |
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
| MOHELA missed bills | 2.5M → 800K DQ (cumulative) | 🔴 |
| MOHELA call wait | **Longest of major federal servicers — ~13 min avg, ~14% abandon rate** [FSA servicer data, cited in 2026 filings] | 🔴 |
| **CFPB complaints — MOHELA (primary API pull)** | **2026 monthly, VINTAGE 2026-09-05:** Jan **913** · Feb **681** · Mar **908** · Apr **910** · May **704** · Jun **815** · Jul **883** · **Aug (d1–22 settled) 475**. ⚠️ **WQ-175 stamp — this series IS revisable:** the same months read 917/682/909/915/703/809 at their 8/13 vintage (deltas −4/−1/−1/−5/+1/+6, all <1%). **Recompute:** re-pull `company=MOHELA` by month and re-locate the settled cliff; do not diff against a prior vintage without re-pulling both | 🟠 at baseline, not accelerating |
| **MOHELA daily rate — the ES-02 / CRL-28 instrument** | **Aug 1–22 (settled) = 21.6/day** · **SAVE wave to date Jul 1 – Aug 22 = 25.6/day** vs the **27–30/day 2026 baseline**. Bands Y >35 · O >45 · **R ≥55 (CRL-28 frozen)** ⇒ **nearest band is 62% above the print**. ⚠️ **YoY like-for-like is mildly UP, not down** (Aug d1–22 **21.6 vs 20.6** in 2025; Jul **30.7 vs 25.5**) — **the Aug fall is largely seasonal, the same July→August drop appears in 2025.** VINTAGE 2026-09-05 | 🟢 **NO SPIKE — 2nd DID_NOT_APPEAR** |
| 🔴 **INSTRUMENT DEFECT — the registered 5–6 day lag rule is WRONG and fails toward a FAKE COLLAPSE** | Settled boundary is a **CLIFF at ~Aug 22 (≈14 days back)**, not a 5–6d taper: Aug 22 = **17**, Aug 23 = **6**, Aug 27 = **3**, Aug 29 = **0**, **Sep 1–5 = 0**. **Applying the documented 5–6d rule on 9/5 reads through Aug 30 and yields 3.3/day — an 85% "collapse" that does not exist.** Backfill is NOT the cause and was measured, not assumed (STUE's own Jul 1–19 window: **539 recorded → 556 today, +3.2%**; settled months <1%) ⇒ it is a **publication BOUNDARY**, not a decay curve. ✅ **FIX: never subtract a fixed N — print dailies and locate the cliff empirically on every pull.** Routed to CARL as a wiring item | 🔴 **fix registered** |
| **Wave-1 complaint tell (Jul 1–19)** | **539 ≈ 28.4/day vs June 27.0/day — NO SPIKE.** ⛔ **The "~5–6d publication lag" qualifier on this row is SUPERSEDED (2026-09-05) — that rule is the one proved defective.** ✅ **Re-derived on fully-settled data: 556 = 29.3/day, still 16% below the >35/day Y band. The null HOLDS** — but it holds on MARGIN (~3% bias vs 16% headroom), **not because the rule was harmless.** *(This row's window was itself selected by the defective rule — pull date minus 5–6d. Flagged by CARL, re-derived, kept.)* | 🟢 **re-derived, holds** |
| **AFT v. MOHELA** | **D.D.C. 1:24-cv-02460 (Chutkan) — STAYED, and now in SETTLEMENT NEGOTIATION.** Discovery frozen since 10/27/2025. Last filing **Jul 17 2026 (#54)** | 🔴 **SETTLEMENT-GATED** |
| — Stay #1 (procedural) | 10/27/2025 minute order: response deadline + discovery stayed pending SCOTUS *Colt/Galette* — **decided Mar 4 2026, unanimous: NJ Transit NOT an arm of the state** | 🟠 **adverse to MOHELA's "creature of Missouri" defense** |
| — **Stay #2 (settlement) — the operative one** | **Mar 20 2026 minute order stayed proceedings "to allow the parties time to explore a negotiated resolution"; parties "engaged in good-faith discussions"; stay extended 60d by JOINT request** [Doc **52**, Joint Status Report 5/18/26 — **free in RECAP**, pulled 7/25] | 🔴 **NEW** |
| — Next step | **Doc 54 filed 7/17/26** = the joint report proposing a schedule. **PACER-only (~$0.30, ~3pp)** — says either *another extension* (talks live) or *merits schedule* (talks failed). **Only remaining unknown on this docket.** | 🟠 **buy** |
| — Class certification | **NEVER FILED** — no class-cert motion or ruling has ever appeared on the docket | 🟠 |
| — ⚠️ Implication for attribution | A settlement typically means **no admission of liability, no public discovery record, no class cert** ⇒ the likeliest path **forecloses** the servicer-attributed default evidence CRL-28's instrument needs (attribution question is unchanged by the CRL-14→CRL-28 retire+replace). Measurability gets *worse*, not better. | 🔴 |
| ✅ **2026-08-13 — DOCKET RECOVERED IN FULL. The 8/10 "inconclusive" is CLOSED: CONFIRMED QUIET.** | **Nothing has been filed since Doc 54 (Jul 17 2026).** CourtListener's own `Date of Last Known Filing` field reads **July 17, 2026**, and the entry list ends there. Status unchanged and now *positively verified*: **STAYED, in settlement negotiation, discovery frozen since 10/27/2025.** **Working route (record it — the 8/10 session lost a check to this):** `curl` + browser User-Agent → `courtlistener.com/docket/69090685/`. WebFetch **403s**; the REST API demands auth; **searching the docket NUMBER does not resolve the case, searching the case NAME does.** The 8/10 read was right to refuse to call a blocked mirror "quiet" (`[[finding_unfetched_is_not_unavailable]]`) — the fix was the path, not the data | ✅ **confirmed quiet through 8/13** |
| 🔧 **CORRECTION — Doc 53 was mis-numbered on the NARRATIVE surfaces, and the LEDGER had it right all along** | STATUS (§ WHAT CHANGED #4) and `SV-STUE-2026-07-25-01` both recorded *"May 19 order (**#53**)"*. **Wrong** — #53 is a **Notice of Withdrawal of Appearance filed May 27 2026**; the May 19 order is an **unnumbered minute order**. **`workbook/SERVICER.tsv` row 18 records it correctly** ("May 27 notice of counsel withdrawal (#53)"). ⚠️ **Note the direction: the machine ledger was accurate and the prose retelling degraded it** — the usual assumption is the reverse. **When a ledger and a narrative disagree, the ledger is not automatically the stale one.** SVs are immutable → corrected here, not there | 🔧 |
| 🔴 **GAP — STUE never recorded the Sep 29 2025 dispositive ruling, and it is the most consequential order on this docket** | **Doc 47 (Memorandum Opinion) + Doc 48 (Order), both Sep 29 2025, Chutkan, both FREE:** **MOHELA's motion to dismiss DENIED without prejudice** *and* **AFT's motion to remand DENIED.** ⇒ the case **survived dismissal** and **stays in federal court**. STUE's live files contain zero mention of either; the only "MTD denied" string anywhere is an **April 2025** line in a retired archive file. **This reframes the stay:** the case is not merely procedurally parked — it is parked *after* clearing a dispositive motion, which is why settlement talks are the live path | 🔴 **new to the record** |
| 🟠 **The Amended Complaint (Doc 50, Jan 15 2026) is FREE and STUE has never read it** | STUE sources **280K borrowers overcharged**, the **~7×/>50× wait-time ratio** and the call-centre **"deflection"** claim to *Protect Borrowers / NCLC* summaries — i.e. **advocacy secondaries paraphrasing a primary that is one free download away** (CourtListener + Internet Archive; $3.00 only if bought on PACER). STUE's own source-quality rule says resolve procedural claims on the docket itself. **Highest-value free pull available in this lane** — it would let three advocacy-attributed figures be re-sourced to the pleading | 🟠 **backlogged → open question #13** |
| Doc 54 + Doc 51 | **Still PACER-only** (0 RECAP requests on each) — unchanged. Doc 52 and 53 are free and already pulled | 🟠 |
| Maldonado v. MOHELA | Mar 2026 — violated CA Student Borrower BoR + UCL | 🔴🔴 precedent stands |
| Settlement | NONE | — |



### §D2 — Treasury Transfer, full detail
*Verbatim. 8,936 B · CRC32 `61383f2f`*

### Treasury Transfer
| Metric | Value | Status |
|--------|-------|--------|
| Phase 1 scope | **~500K defaulted accounts** = launch wave, NOT all ~9M; ramps gradually via Fiscal Service CSP [CRS R48962] | 🟠 |
| Phase 1 execution — "500K by July" wave | ⛔ **QUESTION RETIRED 2026-08-13 — it is not answerable and no longer the right question.** Four months of coverage never produced a launch-day primary, and Treasury's Aug-7 framing moved from a discrete batch to an ongoing build-out (Hub + vendor procurement), so **a clean July yes/no will likely never surface.** Chasing it further is a sunk-cost check. **Replaced by the two instrumented rows below.** | ⛔ retired |
| 🆕 **Aug 7 2026 — Treasury announced PLANS. Read at source 8/13: entirely future tense.** | Article read directly (not via search summary): Treasury "**released plans** to assume management of defaulted student-loan accounts," incl. a **"Default Resolution Hub"** and **vendor partnerships** for collections/counselling; Bessent quoted on "transforming the way defaulted loans are serviced." **The transfer "is set to occur in phases." No completion date, no deadline, and no statement that any accounts have moved.** [Yahoo News 2026-08-07, read in full 8/13] | 🟠 **plans, not execution** |
| 🔴 **THE ANSWER TO THE 8/13 ROW — Treasury's OWN operational primary says the handoff has not happened** | `fiscal.treasury.gov/debt-management/resources/federal-student-loans`, **Last Updated May 18 2026**, still describes the role as: *"The U.S. Department of the Treasury **helps** the U.S. Department of Education, Federal Student Aid **collect** defaulted loans."* That is the **long-standing assisting role** (Cross-Servicing / Treasury Offset / AWG), **not custody or management.** A genuine Phase-1 custody transfer is a change this page would have to reflect, and as of its last update it does not. ⚠️ ~~**Page vintage (May 18) predates the July wave, so this is strong negative evidence, NOT proof.**~~ ✅ **THAT HEDGE IS RETIRED 2026-09-05 — the page now reads `Last Updated: September 4, 2026`** (`<time datetime="2026-09-04T20:19:22+00:00">`) **and the language is UNCHANGED**: still *"Treasury **helps** ED… **collect**"*, still the Default Resolution **Group** at 1-800-621-3115. **It was touched YESTERDAY — 4 weeks after the Aug-7 'Hub' announcement — and still describes the assisting role.** ⚠️ **One honest limit: a CMS `changed` field can move on a trivial edit, so this kills the 'merely stale' explanation without proving an affirmative review.** **Registered as the standing instrument for this question** — a dated, primary, binary surface, which is what the last four months of press-chasing never produced | 🟠 **best available primary read: NOT TRANSFERRED** |
| ⚠️ **NAME TRAP — "Default Resolution HUB" ≠ "Default Resolution GROUP"** | The **Group** is ED/FSA's decades-old default unit, live today with a phone number on the Fiscal Service page (1-800-621-3115). The **Hub** is the *proposed* Aug-7 thing. **The names differ by one word and the evergreen explainer articles are about the Group.** Do not let a piece about the Group be banked as evidence the Hub launched | ⚠️ |
| 🔧 **"Treasury posted it to the Federal Register" — NOT SUPPORTED; do not carry it** | The claim appeared **twice in WebSearch's generated summaries** and is **absent from the article those summaries drew on**. A Federal Register full-text search for **"Default Resolution Hub" across all of 2026 returns ZERO documents**; the Treasury/Fiscal-Service notice lists for Jul–Aug carry nothing on point. **A search-engine summary is not a source** — this one manufactured a specific, checkable, false provenance claim, which is worse than vagueness because it *invites* the reader to stop checking (`[[finding_exact_level_authenticates_a_wrong_direction]]`) | 🔧 **retracted before it entered the record** |
| ⚠️ **Press default-count creep — the secondaries are drifting UP and away from the primary** | Primary (FSA, Mar 31 2026): **~9.0M / $220B / >13%**. Press: 9.2M (ED official, Mar) → **9.5M** (Fox, Jul 21) → **10M** (Yahoo, Aug 7). **Meanwhile the same Aug-2026 secondaries still recycle "$180 billion / 11%" — which are the DEC 2025 figures.** So current coverage simultaneously *overstates* borrowers and *understates* dollars. **Cite the primary; next FSA print (~Sep) settles it.** | ⚠️ **unchanged rule: primary wins** |
| 🆕🔑 **THE GOVERNING PRIMARY, READ 2026-09-05 — ED/Treasury Interagency Agreement, Mar 19 2026 (free on ed.gov)** | **Four months of this lane were worked through press and a webpage while the contract sat unopened.** It settles the shape of the question: **Phase 1 = Treasury REVOKES Education's Cross-Servicing exemption** (granted **May 11 2001** under **31 U.S.C. § 3711(g)(2)(B)**) and integrates FSA's **Default Resolution Group** into Cross-Servicing. Phase 2 = non-defaulted servicing. Phase 3 = FAFSA / eligibility / oversight | 🔑 **new instrument** |
| 🆕🔑 **THE TRIGGER IS A CAPABILITY, NOT A DATE — and this is why the July question was unanswerable** | *"Education understands that it is Treasury's intent to **revoke the existing exemption once full operational capacity has been reached**."* **The agreement contains NO phase dates** (effective on last signature, runs until terminated, 90-day termination clause). ✅ **Retroactively vindicates the 8/13 retirement of the "500K by July" row** — the contract never contemplated a dated wave | ✅ **OQ#5 retirement justified at primary** |
| 🆕⚠️ **AND IT DISSOLVES THE CONTRADICTION: two claims STUE had fused** | Pre-revocation, *"Education may refer exempted debts to Cross-Servicing, if agreed to by Treasury"* — **discretionary referral.** ⇒ **accounts CAN move without revocation and without any change to Treasury's public page.** So the page evidence is strong against **CUSTODY** and is **NOT** evidence against *some accounts having moved*. **Keep those separate** | ⚠️ **scope correction** |
| 🆕⚠️ **A THIRD PERIMETER — and Phase 1's object is SMALLER than every figure in circulation** | IAA: *"The DRG operates and maintains the Default Management and Collections System (DMCS)… It serves nearly **six million** student and parent borrowers with a current outstanding loan value of over **$120 billion**."* **That is what Phase 1 takes over — not 9.0M/$220B.** ⚠️ STUE already tracks **Federally Managed 9.00M ≠ Direct Loan 7.20M**; **DMCS/DRG ~6M/$120B is a THIRD perimeter.** It explains the press scatter (7.8M/$179B · 9.2M · 9.5M · 10M): **they are mixing perimeters.** **State the perimeter on every default figure** | ⚠️ **perimeter discipline** |
| ✅ **NAME TRAP SETTLED AT PRIMARY** | The IAA says **Default Resolution GROUP (DRG)** throughout; **"Default Resolution Hub" appears NOWHERE in it.** The "Hub" is press framing over DRG/Cross-Servicing integration. **The registered trap was correct** | ✅ |
| ✅ **OQ#14 leg (b) — vendor awards: NULL, and the null is VALIDATED** | USAspending, Treasury awarding, actions Mar–Sep 2026: **"default resolution" n=0 · "student" n=0**, while **controls FIRE** ("debt collection" n=10, "cross-servicing" n=1, "call center" n=7) ⇒ **real null, not a broken query.** ⚠️ Latest PCA capacity action is a **bridge contract dated 2025-05-18** — a stopgap, the **opposite shape** of a build toward "full operational capacity." *(SAM.gov is a JS shell and defeats fetching; **USAspending is the workable route**)* | 🟠 **no build-out visible** |
| Nature of handoff | **Servicing/collections CUSTODY — not enforcement resumption.** Do not conflate. ✅ **Now a CONTRACT CITATION, not an assertion:** *"The Cross-Servicing program will use only the tools **authorized by Education**"* ⇒ the AWG/TOP switch stays with ED post-custody | ⚠️ |
| Phase 2 / Phase 3 | Planned, no public dates | 🟡 |
| Legal authority | Disputed; GOP bill introduced to codify the transfer | 🔴 |

> ⚠️ **2026-08-10 verdict on Phase 1 launch: INCONCLUSIVE.** Free web search found no primary confirming the ~500K account wave actually transferred/borrowers were contacted in July as originally framed. **But the question itself may now be the wrong one to close on 8/13**: the Aug 7 "Default Resolution Hub" + vendor-partnership announcement suggests Treasury's own framing has shifted from a discrete "500K by July" batch toward an ongoing operational build-out — a July yes/no answer may never surface cleanly. **Recommend CARL do NOT prune the 8/13 row outright; re-scope it** to "has the Default Resolution Hub gone live / have vendor partnerships been named?" rather than continuing to chase the original July figure. AWG/TOP involuntary collections still show no restart signal in this sweep — custody-build-out ≠ enforcement, unchanged.



---

## ROUTED TO PARENT — ✅ ALL ADOPTED (closed 2026-07-31)

**[ROTATED 2026-09-05 → `archive/STUE_STATUS_ARCHIVE_2026-09.md` §B7]** The 7/25–7/31 routing table, closed with nothing owed in either direction, verified against the parent's committed files. **The two procedural lessons are kept and are live in boot step 2b:** check adoption against the parent's FILES, not against a claim of processing — and check whether the parent is mid-session before reading a stale stamp as neglect.

### 🔵 LIVE — routed 2026-09-05, delivered to CARL + PROME (`SV-STUE-2026-09-05-01`)

> **Boot step 2b reads THIS table.** Verify each against the parent's committed files — **delivery is not adoption.**

| Item | Ask | Status |
|---|---|---|
| **ES-02 mechanism warning** (2nd DID_NOT_APPEAR) | **NOT a re-price.** CRL-28's window opens Oct 1 2026, so a pre-window null cannot grade it. Registered decision point = MOHELA notice completion **~Oct 31** | ✅ **INTEGRATED** — CARL 9/5: KB-CARL-425; no confidence touched |
| **ES-02 instrument DEFECT** (5–6d lag rule → fake 85% collapse) | Wiring item: never subtract a fixed N; locate the cliff empirically | ✅ **ADOPTED + ROUTED ONWARD** — CARL → PROME, recommended to DAEDALUS as a candidate fleet rule. **Promoted to fleet auto-memory as `finding_dormant_instrument_is_a_query_plus_unexercised_reading_rules`** |
| **FSA release NOT posted** (MD5-verified) | Leave CARL's default-stock figures untouched at their Mar-31-2026 as-of | ✅ **INTEGRATED** — KB-CARL-424 |
| **DMCS/DRG third perimeter** (~6M / $120B) | New KB row; bears on the denominator work | ✅ **INTEGRATED** — KB-CARL-423 |
| **Sweet contempt motion** (Aug 18; 807 class members) | Qualify the "discharges are proceeding" read | ✅ delivered |
| **OQ#19 — SAVE notice-window conflict** | Aug-15 secondary would pull CRL-13's full-population read to ~Nov 13 2026 vs carried Q1-2027 | 🟠 **OPEN — carried framing STANDS.** CARL 9/5: settle on a **servicer primary before Oct 1**; decide on evidence, not a secondary |
| **STATUS read-cap** | Ruling requested | ✅ **RULED 9/5 — rotate, do not split.** Executed same session; see § below |
| **10/28 delivery** (`SV-STUE-2026-10-28-01` + packet `AGENTS/CARL/inbox/2026-10-28_from-STUE_FSA-Q3-grades-AFT-collections.md`) | ES-01 NO VERDICT (straddles Y) · ES-04 not gradeable · ES-06 access gap · ES-02 interim 24.8/day · AFT v. ED date correction (10/14, not 10/28; no new count) · collections still paused. **No CRL change proposed** | 📤 **sent 10/28; adoption unverified** |

> ⚠️ **Historical routing table (7/25–7/31, all adopted, nothing owed) → `archive/STUE_STATUS_ARCHIVE_2026-09.md` §B7.**

> **STUE holds no predictions ledger** — CRL-04/05/13/28 are CARL's rows and CARL is system of record. STUE proposes with worked reasoning; the parent applies. **Do not mirror a CRL confidence here.**

---

## 🗃️ READ-CAP ROTATION 2026-09-05 (CARL-ruled: rotate, do not hot/cold split)

**8 resolved/closed blocks moved VERBATIM to `archive/STUE_STATUS_ARCHIVE_2026-09.md`** (§B1–B8), each byte- and CRC32-stamped and **verified byte-identical against the pre-rotation source in git**. One-line pointers left at every original location. **No canonical value moved** — a safety test confirmed every live figure survives outside the rotation set *before* any block was cut.

⚠️ **THE AGGREGATE, NOT THE HEADLINE — and measured in BYTES, it is not a win.** *(CARL's constraint, and it bites here exactly as he warned. ⚠️ A first pass of this table was written in CHARACTER counts and understated every figure — a file this heavy in emoji runs ~2.3% larger in bytes than in characters, and the read cap is a BYTE cap. Corrected against `git show` before it stood.)*

| Measure (BYTES) | Session start (`ef46d42b`) | After this session's writes (`4fdc62e3`) | After rotation |
|---|---:|---:|---:|
| `STATUS.md` | 104,420 | 130,882 | **112,983** |
| `CLAUDE.md` (untouched) | 45,035 | 45,035 | 45,035 |
| **BOOT-READ TOTAL** | **149,455** | 175,917 | **158,018** |
| `STATUS.md` vs 32,550 B budget | 3.21× | 4.02× | **3.47×** |

**The rotation removed ~17,900 B net and absorbed ~68% of this session's own 26,462 B of growth — but the boot path still ends the day +8,563 B (+5.7%) ABOVE where it started, and STATUS is 3.47× budget versus the 3.21× I inherited.** *(These are the post-write figures and they INCLUDE this measurement block itself — writing the measurement moved it, which is the smaller version of the same problem.)*

🔴 **Stated plainly because the flattering version is available and wrong: I left this surface WORSE than I found it.** "Rotated 24,959 B" is a true sentence that describes a net increase. **The rotation did not pay for the session.**

🔴 **And the structural finding underneath it: rotation alone cannot fix this surface.** After removing everything closed, **the LIVE content is still ~106 KB = 3.27× the 32,550 B budget.** The problem is not accumulated dead weight; it is that STATUS carries dense live analysis a boot is told to read whole. **Flagged to CARL — not acted on, because the remedy is a design question and the last one was ruled, not assumed.**

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
1b. **#8 (NEW): does MOHELA settle?** **Doc 54 (filed 7/17/26) is the discriminator** — the 60-day clock from Doc 52 expired on it, so it is either another extension (talks live) or a merits schedule (talks failed). **PACER-only, ~$0.30, ~3pp.** Everything else on this docket is now recovered free. *Bears on CRL-14: a settlement forecloses the public attribution evidence the row depends on.* **⏸ UPDATE 2026-08-13: docket CONFIRMED QUIET through today — nothing filed since Doc 54 (Jul 17). So the discriminator has NOT resolved and is NOT overdue; a 4-week gap after a status report is unremarkable on a stayed docket. Doc 54 remains PACER-only (0 RECAP requests). ⚠️ Do not re-check this weekly — it is EVENT-driven, and the 8/10 session burned a check on it. Free route if ever needed: `curl` + browser UA → `courtlistener.com/docket/69090685/`.**
2. ✅ **RESOLVED 2026-08-13 (Q2 HHDC, rel Aug 11) — YES, and the flow answer is the bigger one.** Stock **10.34% → 10.60%**, so CRL-04 holds on a 2nd consecutive >10% print and is not a single-print artifact. **The stock-up/flow-down ambiguity flagged at registration resolves to COHORT EXHAUSTION**: flow into 90+ went 16.19 → 10.86 → **7.83%**, halving twice while the stock rose. On-ramp slack and seasonality are both refuted by the repetition across two quarters. ES-STUE-03 logged **APPEARED (Y)**.
3. **Is the ~1.3M/quarter cure channel durable or a one-off?** Newly quantified this session; if borrowers are exiting default nearly as fast as entering, the 13M EOY projection is too high. → FSA Q2 (~Sep). 🔧 **10/28: STILL OPEN.** FY2026 Q3 net default growth was only +0.3M, but no gross-flow figure exists for Apr–Jun (FSA `DLEnteringDefaults.xls` frozen since Aug 2023; no Liberty Street update), so the cure share is unmeasurable. ES-04 not gradeable.
4. ✅ **LARGELY RESOLVED 2026-09-05 — and the mechanism is named, not just the discrepancy.** Parsed the FSA primary directly: **9.57M / 9.5M / 10M appear at NO perimeter in the file.** The sheets carry **five** perimeters at FY2026 Q2, and two were not previously on STUE's register:
   | Perimeter | Default recipients | Dollars |
   |---|---:|---:|
   | **Federally Managed** *(the correct combined figure — STUE's primary)* | **9.00M** | **$220.3B** |
   | Direct Loan | 7.20M | $175.3B |
   | 🆕 **ED-Held FFEL** | **2.46M** | $45.0B |
   | 🆕 **FFEL (incl. commercially held)** | **3.20M** | $67.5B |
   | *naive SUM of Direct Loan + ED-Held FFEL* | *9.66M* | — |
   **⇒ The naive sum-of-parts is 9.66M against a correct 9.00M — a 0.66M DOUBLE-COUNT of borrowers holding both loan types.** **Every press figure in circulation (9.2M · 9.5M · 9.57M · 10M) sits inside the 9.00–9.66M band.** ⚠️ **The double-count is structural, not default-specific** — it appears in every category (Repayment +0.71M, Forbearance +0.54M), so anyone adding the sheets gets it everywhere. ⚠️ **Stated at its true strength: this is a MECHANISM THAT EXACTLY REPRODUCES THE OBSERVED BAND, not a proof of how any particular outlet got its number** — I have not seen their working. **Rule unchanged: cite Federally Managed 9.00M, and name the perimeter every time.**
5. ⛔ **RETIRED 2026-08-13 — unanswerable as posed, and superseded.** No launch-day primary exists after four months; Treasury's Aug-7 framing shifted from a discrete "500K by July" batch to an ongoing build-out. **Best primary read is that custody has NOT transferred** (Fiscal Service page, last updated May 18 2026, still says Treasury *"helps ED collect"*). **Successor → #14.**
6. ✅ **RESOLVED 2026-09-05 (~16d late) — YES, THE NO-SPIKE HOLDS. Second DID_NOT_APPEAR.** Aug 1–22 settled **21.6/day**, SAVE wave to date (Jul 1–Aug 22) **25.6/day**, both **below** the 27–30/day baseline and **~2.5× below** CRL-28's frozen 55/day. ⚠️ **Do not read the August fall as improvement — it is largely seasonal** (2025 showed the same Jul→Aug drop); **YoY like-for-like is mildly UP** (+4.9% Aug, +20% Jul). 🟠 **Mechanism warning routed to CARL, NOT a re-price:** CRL-28's window (Oct 1 2026–Sep 30 2027) has not opened, so this is a pre-window read. **The registered third look is MOHELA's ~Oct 31 notice completion — that is the STUCK→MISSED decision point, not this one.** 🔴 **And the instrument itself was found defective — see the 9/5 session block: the registered 5–6d lag rule fails toward a fake 85% collapse; fixed to locate-the-cliff-empirically.**
7. **Does the compressed notice window change the non-selection RATE, or just its timing?** A shorter Department-wide window with fixed servicer capacity is the mechanism that would *raise* non-selection. → CRL-13.
8. ✅ **RESOLVED — Tue Aug 11, the FALLBACK Tuesday.** The base rate's *band* (1st or 2nd Tuesday of August) held for a 5th year; its *point estimate* (Aug 4, on 3-of-4 support) was wrong. **Calibration lesson, kept because it is cheap and repeatable: with 3-of-4 support, publish the band and treat the mode as colour.** A 75%-confidence point estimate that misses is not a broken method — but STUE wrote "modal Tue Aug 4" into a 🔴 DO-THIS-FIRST line and a BOTTOM LINE, which reads as a date. **Next quarter: poll `HHD_C_Report_2026Q3.xlsx` directly rather than watching for an advisory.**
9. **🔧 UPDATED + RE-FRAMED 2026-09-05 — the question moved from the appellate tail to district-court ENFORCEMENT, and that is the live gate now.** **No cert petition found in any source this sweep**, and PPSL's own case page reports none ⇒ **leaning NO, but unresolved** (no deadline is stated — *"no petition found"* is not *"DOE declined"*). **What actually happened in the gap: on Aug 18 2026 PPSL moved to ENFORCE the settlement and to hold ED in CONTEMPT with sanctions**, stating **at least 807 CLASS members** still await discharges/refunds past deadlines *"that have long since passed,"* some **>1.5 years** overdue. ⚠️ **Perimeter: 807 = original-class members with overdue relief — NOT the >170K post-class cohort, NOT ~200K, NOT >500K.** **Entitlement is settled; DELIVERY is contested.** → watch the D.C. district docket for a ruling on the enforce/contempt motions. 🔧 **10/28: enforce + contempt motions fully briefed (replies Oct 15); hearing Thu Nov 5 2026.** Still no cert petition found.
10. **🆕 Harvest the TCF/Protect Borrowers study STUE already half-cites.** *"Trump's Student Loan Delinquency Crisis, Unmasked"* (Granville, TCF + PB, **published Feb 20 2026**, nationally-representative credit panel, data = first 3 quarters of 2025) is where STUE's carried **25% DQ rate** and **13M EOY projection** come from — **but its cohort-severity and demographic cuts were never harvested**: **−57pt** avg score drop, **three-quarters of delinquent borrowers pushed into "deep subprime,"** **7.9M entered delinquency** in 3 quarters, **Black and Native borrowers ~50%** DQ, **Pell recipients 27%**. ⚠️ **NOT new** — a 5-month-old study, flagged so it is not mistaken for a July datum. The **−57pt** figure is a *third* score-drop number alongside FICO's **−62** (H2 2025) and the **−69** derivative cite: **different sources, windows and panels — reconcile before citing any of them as "the" number.** *Backlog item, not a threshold move.*
11. **🆕 🔴 Is the FHA delinquency rise student-loan-CAUSED, or co-moving?** The single highest-value open question STUE has, because it decides whether **CASCADE Stage 6 (mortgage) re-dates from Apr-Dec 2027 to ALREADY UNDERWAY** — a ~9-18 month pull-forward of the thesis's most consequential stage. **What would settle it:** an FHA-isolated cut — DQ rates for FHA borrowers *with* vs *without* student debt, same vintage, same LTV band. **CORRECTED 2026-08-10: the VASP precondition was a false blocker (category error — VASP is a VA program, not an in-series FHA confound, and the VA leg is much milder, not similar size — see § CHANNEL 5 above) and is REMOVED.** The real in-series confound to net out first is **HUD ML 2025-06's mandatory partial-claim waterfall** (unpulled — HUD FHA Neighborhood Watch geographic cut). **Do not treat "FHA is rising and student debt is concentrated there" as causation — that is the same co-movement error that produced the over-sized CC cascade claim.** Owner: CARL/DEWEY hold the evidence; STUE holds the student-debt side. → § CHANNEL 5.
12. **🆕 Source the score-drop band properly.** Pull the **NY Fed Liberty Street Mar 2025** piece behind the **−87 to −171** figure and check whether a post-on-ramp update exists — it is the oldest and largest number in the score set and it anchors the top of the cascade. → § SCORE-DROP RECONCILIATION.
13. **🆕 Pull the AFT Amended Complaint (Doc 50, Jan 15 2026) — it is FREE and has never been read.** Three servicer figures STUE cites (**280K overcharged**, the **~7×/>50× wait-time ratio**, the call-centre **"deflection"** pattern) are currently sourced to *Protect Borrowers / NCLC* summaries of this pleading. The pleading itself is downloadable from CourtListener/Internet Archive at no cost. **This is a source-quality upgrade, not new information** — but STUE's own rule says resolve claims on the docket, and it has been paraphrasing an advocacy paraphrase for months. *Also free and unread: Doc 47, the Sep-29-2025 Memorandum Opinion denying dismissal.*
14. **🔑 RE-INSTRUMENTED 2026-09-05 ON THE GOVERNING PRIMARY — and the new instrument is far better than the two it replaces.** Reading the **ED/Treasury Interagency Agreement (Mar 19 2026)** for the first time gives a **binary legal event**: **has Treasury REVOKED Education's May-11-2001 Cross-Servicing exemption** (31 U.S.C. § 3711(g)(2)(B); I TFM 3-5280; 31 CFR 285.12(d)(5))? **That is custody.** Its stated trigger is *"once **full operational capacity** has been reached"* — **a capability, not a date, which is exactly why #5 was unanswerable.**
   - **(a) OLD page-wording test → DEMOTED to corroboration.** Checked 9/5: page now stamped **`Last Updated: September 4, 2026`** with the *"helps ED collect"* language **unchanged** ⇒ consistent with **exemption NOT revoked**, and the old "page is stale" hedge is dead.
   - **(b) Vendor awards → NULL, VALIDATED** (USAspending: target terms n=0, controls n=10/1/7). Latest PCA capacity action is a **2025-05-18 bridge contract** — a stopgap, the opposite of a capacity build. **This is now the LEADING indicator for (a)**, since revocation is gated on operational capacity.
   - ⚠️ **CRITICAL SCOPE SPLIT the old framing got wrong:** pre-revocation, ED **may refer debts discretionarily** with Treasury's approval ⇒ **accounts can move WITHOUT revocation and without any public-page change.** Evidence against **custody** is **not** evidence against **any accounts having moved.**
   - ⚠️ **Custody ≠ enforcement, and now at primary:** *"the Cross-Servicing program will use only the tools **authorized by Education**."* AWG/TOP remain paused; **re-confirmed 9/5, 3rd consecutive STUCK.**
19. **🆕 Which SAVE notice-completion date is right — Dec 31 2026, or Aug 15 2026?** A secondary asserts servicer notices ran **"between July 1 and August 15, 2026."** **If true, the CRL-13 FULL-POPULATION read lands ~Nov 13 2026 — a full quarter earlier than the carried Q1-2027**, which would materially re-date CARL's docket. **Against it:** ED's own Mar-27-2026 release states **no end date**, and two servicer primaries contradict it (Nelnet → **Dec 31 2026**; MOHELA → **Jul–Oct 2026**). **Servicers send the notices, so servicer FAQs are the right evidence level.** ✅ **Arithmetic corroborates the carried framing at BOTH ends:** Jul 1 + 90d = **Tue Sep 29 2026** (matches the reported "no borrower moves off SAVE before Sep 29" exactly and matches the first-tranche catalyst); Dec 31 + 90d = **Wed Mar 31 2027** (matches "last deadlines ~end-Mar 2027"). **Carried framing STANDS; the Aug-15 claim is logged unverified, not banked.** → settle on a servicer primary (Nelnet/MOHELA FAQ re-read) before the Oct-1 first-tranche read. 🔧 **10/28: the frame shifted again.** Notices are servicer-specific (Edfinancial 7/1–8/15, MOHELA Jul–Oct, Nelnet to year-end; CARL KB-501), and ED reportedly added a **final 30-day notice** after a missed window (secondary). **The last auto-enrolments may land ~end-Apr 2027.** Still unsettled at primary.
15. ✅ **RESOLVED 2026-08-13, same session it was opened — FSA archives pulled, and the count does NOT rescue the level claim.** Like-for-like **7.90M → 9.00M = 1.14×**. The registered "~5M ⇒ ~1.8×" prior was a **perimeter error** (Direct-Loan baseline against a Federally-Managed numerator) — **that part stands.** ⚠️ **But the accompanying "−16.2% below trend" figure is WITHDRAWN, and the 7.90M baseline is itself for-profit-contaminated** (§ THE BASELINE PROBLEM), so **this question is only PARTLY resolved: the down-market K-shape hypothesis is not supported on a like-for-like ratio, but the counterfactual it was measured against does not hold. Real resolution needs #17.** What survives is the **speed** — +3.8M in two quarters, ~16× the pre-pandemic pace — which is a catch-up pulse off a stock that had been drained to 5.2M, not accumulation to new highs. Full working → § THE BASE-RATE CHECK. **Successor → #16.**
16. **🆕 Does the FSA default count PEAK on schedule? — the one dated falsifier both instruments now agree on.** NY Fed flow into 90+ **leads** the FSA count by ~9 months (default = 360 days delinquent). That flow peaked **25:Q4 at 16.19%** and has collapsed to **7.83%** ⇒ **the count should top out ~FY2026 Q4 (quarter ending Sep 30 2026) near 10–11M, then decline.** **Compounding past ~11.5M into 2027 refutes cohort exhaustion on BOTH instruments and revives the level claim; rolling over on schedule resolves the episode as a large, fast, one-time normalization.** → next read **FSA FY2026 Q3** (quarter ended Jun 30 2026), due ~Sep. ⚠️ **Pull the archive file directly** — `studentaid.gov/sites/default/files/fsawg/datacenter/library/PortfoliobyLoanStatus.xls`, *Federally Managed* tab, *Cumulative in Default* — **do not wait for a press release or an EA announcement.** 🔧 **10/28: FY2026 Q3 = 9.30M (+0.3M); 271–360-day pipeline 0.66M ⇒ Sep-30 count roughly 9.5–10.0M, below the 10–11M band.** Rolling over looks earlier and lower than projected. Grade on the FY2026 Q4 file (~Dec).
17. ✅ **ANSWERED 2026-08-13, same session it was opened — and the answer REVERSES the morning's reading.** **The dominant composition effect is the DENOMINATOR, not cohort quality:** the share of portfolio dollars in active repayment (the only balances that *can* be delinquent) fell **53.8% → 38.5%** while forbearance rose **10.0% → 29.5%**. Exposure-adjusted, 90+ among those actually in repayment went **7.97% (2015–19) → 10.95% (FY2026 Q2) = 1.37×**, cross-checked at **1.31×** by an independent route. **Registered prior CONFIRMED — today's 10.60% IS elevated — but by a mechanism I did not anticipate.** ⚠️ **The for-profit cohort adjustment this question originally specified is STILL NOT DONE** (it would push the baseline lower still and make today look worse — unmeasured, so unclaimed). Full working → § #17 ANSWERED. **Residual threat → #18.**
18. **🆕 🔴 Is the in-repayment population SELECTED? — the main threat to #17's answer, and the reason #17 is not fully closed.** The exposure adjustment assumes the ~38.5% still in active repayment is comparable to the ~53.8% of 2015–19. **It may not be.** ⚠️ **Argument it is FINE:** the 2024–26 forbearance block is largely **SAVE *litigation* forbearance** — borrowers parked administratively when the plan was enjoined, **not** selected for distress — so the residual should not be adversely selected. ⚠️ **Argument it is NOT fine:** the residual may be **positively** selected (borrowers who kept paying while others were parked), which would inflate the 10.95% relative to a like-for-like 2015–19 population and shrink the 1.37×. **Both directions are live and I cannot currently separate them.** **What would settle it:** the FSA repayment-plan file (`DLPortfoliobyRepaymentPlan.xls`, pulled and unexamined) shows plan mix over time — if the in-repayment residual is disproportionately **IDR**, that is evidence of *administrative* sorting rather than borrower quality; a shift toward **Level/Graduated** would suggest the opposite. ⚠️ **Register the prior: I expect selection to be MODEST and not to overturn a 1.3–1.4× gap — but I expected the wrong mechanism this morning too, so treat that expectation as weak.** Until #18 is worked, quote **#17's finding with its selection caveat attached**, never bare.

---

---

## BOTTOM LINE (blueprint §8 — rewrite EVERY session, plain language, no jargon)

**Where the domain is now:** The number of federal borrowers in default is still rising, but much more slowly. It reached **9.3 million ($234.1 billion) on June 30**, up 0.3 million in the quarter after 1.3 million the quarter before. The pipeline behind it is thinning: about **0.66 million** borrowers were 271–360 days late on June 30 and are the most that can default by September. That points to a **September count near 9.5–10 million**, below the 10–11 million peak I projected in August. This is consistent with the "one big cohort working through" reading; it is not proof of it.

**The single most important thing:** **The mass SAVE transition has not yet reached any data I can see.** The June 30 FSA snapshot was taken the day before the first notices went out. MOHELA complaints are running about **25 a day in October**, well under the 35/day yellow line and under half of the 55/day level CRL-28 needs, now that its window is open. The real tests are the **NY Fed third-quarter report (~Nov 4–5)**, the **final MOHELA complaint grade (~Nov 13–16)**, and the **FSA September-30 file (~December)**.

**Where my own instruments fell short tonight:** The forbearance check landed on its yellow line and the published rounding cannot say which side, so I report **no verdict** rather than pick one. The cure-channel check **cannot be graded at all** this quarter, because nobody published a gross count of new defaults, and the substitute I tried failed a consistency check. The school-closure list is still unreadable. The complaint-boundary rule **did pass its first test on fresh data**, but that is one test.

**What changed outside the data:** Treasury and Education opened an online **Defaulted Loans Support Center on Sep 30**, which is a rehabilitation portal, not a collections restart. **Wage garnishment and tax-refund offsets remain paused**, and reports of private collectors coming in November are plans, not announcements. Borrowers who miss their 90-day SAVE window reportedly now get a **final 30-day notice**, which would push the last forced switches from roughly end-March to end-April 2027. That comes from news reports, not the Education Department's own page. The **Sweet contempt hearing is Nov 5**.

**What would change my mind:** If the September-30 default count comes in **above ~10.5 million**, or the NY Fed flow into 90+ stops falling, the exhaustion reading is wrong. If MOHELA complaints jump toward 45–55 a day as auto-enrolments land in November, the servicer-failure mechanism I have been close to calling dead is alive.

*(Rewritten 2026-10-28. Prior version 2026-09-05.)*

---

*Sub-agent of CARL. Parent is system of record for CRL-04/05/13/28 (CRL-14 retired 7/31, superseded by CRL-28) — STUE keeps no own predictions ledger. Latest state vector: **SV-STUE-2026-10-28-01**. Expected-signals register: `workbook/EXPECTED_SIGNALS_TRACKER.md`.*
