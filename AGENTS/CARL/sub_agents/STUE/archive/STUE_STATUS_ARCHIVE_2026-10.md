# STUE STATUS ARCHIVE — 2026-10

Verbatim rotations out of `STATUS.md`. Each section carries a byte count and CRC32 of the moved text, computed before the cut. Historical only; never cite as current.

## §C1 — 📌 SESSION 2026-09-05 block (rotated 2026-10-28)

**Bytes 14310 · CRC32 `1c2ff88e`** · Its live figures were superseded or carried into § SIGNAL DASHBOARD on 2026-10-28 (CFPB series re-pulled, FSA FY2026 Q3 posted, Treasury rows updated). The IAA reading and the ES-02 lag-rule correction remain live in the dashboard, `CLAUDE.md` and the ES tracker.

> ## 📌 SESSION 2026-09-05 — 23 DAYS DARK. BOTH DATED CHECKS RUN: ONE REAL NULL, ONE NON-EVENT. AND THE TREASURY QUESTION FINALLY HAS A PRIMARY.
>
> **⚠️ First, the gap itself: STATUS was last written 2026-08-13. That is 23 days, not "a couple."** In that window the one dated item (ES-02, ~Aug 20) went ~16 days overdue and was flagged externally — PROME's 9/4 DOCKET reconcile named it **the single genuinely-missed item out of 32 overdue rows (DOCKET L150)**. **STUE did not catch its own overdue instrument; the parent-fleet audit did.** That is the finding about process, and it is worth more than either number below.
>
> ### ✅ ASK 1 / ES-STUE-02 — **the wave-1 "no spike" HOLDS. Second DID_NOT_APPEAR.**
>
> | Window (settled) | Complaints | Per day | vs 27–30/day baseline |
> |---|---:|---:|---|
> | Jun 2026 (full) | 815 | 27.2 | at baseline |
> | Jul 2026 (full) | 883 | 28.5 | at baseline |
> | **Aug 1–22 2026** | **475** | **21.6** | **BELOW** |
> | **SAVE wave to date (Jul 1 – Aug 22, 53 d)** | **1,358** | **25.6** | **BELOW** |
>
> **Bands: Y >35/day · O >45/day · R ≥55/day (= CRL-28's frozen absolute). Nearest band is 62% above the print. Nothing is close to firing.**
>
> ⚠️ **Do NOT read the August decline as improvement — it is largely seasonal.** The same July→August drop appears in 2025 (25.5 → 20.6/day, −19%); 2026 is −30%, same direction. **On a YoY like-for-like the series is mildly UP:** Aug d1–22 **21.6 vs 20.6** (+4.9%), Jul d1–22 **30.7 vs 25.5** (+20%). **The honest reading is FLAT-TO-SLIGHTLY-UP against last year and BELOW its own 2026 baseline — and ~2.5× below CRL-28's threshold, two months into the SAVE wave.**
>
> 🟠 **Consequence for CRL-28, stated carefully because its window has NOT opened.** CRL-28 runs **Oct 1 2026 – Sep 30 2027**; this is a **pre-window mechanism read, not a grade.** Per the ES register, a second null means *"CRL-28 has no working mechanism, not merely a stalled threshold — that is a STUCK→MISSED question."* **The mechanism has now had two months of the largest servicing event in the portfolio's history to arm itself and has not moved.** ⚠️ **Not proposing a confidence cut** — the window is not open and the Oct notice-completion check is the registered third look. **Routed to CARL as a mechanism warning, not a re-price.**
>
> ### 🔴 ASK 2 — **THE WAKE-MECHANISM VERDICT: the query woke clean, the LAG RULE did not. Half the instrument had rotted.**
>
> **(a) Runnable exactly as written? ✅ YES.** `company=MOHELA` against the CFPB complaint API returned valid JSON first try, no auth, no 403, no endpoint drift, historical months reproducible. **A dormant instrument was woken cold after 3 weeks and produced a clean verdict.**
>
> **(b) But the instrument's LAG CHARACTERISATION IS WRONG, and it is wrong in the direction that manufactures a spectacular false finding.** The register says *"~5–6 day publication lag — never read the trailing week."* **Measured today, the settled boundary is a CLIFF at ~Aug 22 — a 14-day gap — not a 5–6 day taper:** Aug 22 = 17 complaints, Aug 23 = 6, Aug 27 = 3, Aug 29 = **0**, and **Sep 1–5 = 0**. **A reader applying the registered 5–6 day rule on 9/5 would treat data through Aug 30 as settled and read 3.3/day — an 85% collapse off baseline that does not exist.** ⚠️ **That is not a small miscalibration: on this instrument the documented rule produces a fake ORANGE-adjacent crash in the *quiet* direction, i.e. it would have been banked as "MOHELA complaints have collapsed."**
> - **Backfill is NOT the explanation and I checked rather than assumed:** re-pulling STUE's own recorded Jul 1–19 window gives **556 today vs 539 recorded = +3.2%**, and settled months move by <1% (Jan −4, Feb −1, Mar −1, Apr −5, May +1, Jun +6). **So data goes ~97% complete within days of a batch, then the batch boundary sits ~2 weeks back.** It is a publication *boundary*, not a decay curve.
> - ✅ **FIX, and it is the generalizable form: stop subtracting a fixed N. LOCATE THE CLIFF EMPIRICALLY ON EVERY PULL** — print dailies, find the step-change, discard everything after it. Registered into the ES-02 row.
> - `[[finding_instrument_cadence_cannot_resolve_the_claims_window]]` · `[[finding_dated_carry_item_has_no_expiry_check]]` — **the query was tested when written and the lag figure never was.** A number written beside a working query inherits its credibility.
>
> ### ⛔ ASK 3 — **the FSA release has NOT posted. This is a NON-EVENT, recorded as one.**
>
> **`studentaid.gov/.../PortfoliobyLoanStatus.xls` pulled 9/5: `last-modified: Thu 18 Jun 2026 21:05 GMT`, and MD5 `4732c453bc281433b6417304b919d007` is BYTE-IDENTICAL to STUE's own 8/13 archived copy.** The Jun-23 release (EA GENERAL-26-38, data as of Mar 31 2026 = FY2026 Q2) is still the newest. **⇒ ES-01 / ES-04 / ES-06 remain UNRESOLVED; open questions #3, #4 and #16 cannot be graded.**
> ⚠️ **Per the register's own rule this is NOT a signal** — absence of a publication is not absence of stress. **Next-look trigger: poll the same URL's `last-modified` header weekly; act on the header changing, NOT on a calendar date and NOT on an EA announcement.** *(Naming the RELEASE not the quarter, per the 8/13 cadence-bug fix: the next release carries **FY2026 Q3**, quarter ended Jun 30 2026.)* ⚠️ **Note the registered single point of failure is now live: this one delayed release is blinding four questions at once.**
>
> ### 🆕🔴 THE SESSION'S REAL FIND — **the ED/Treasury INTERAGENCY AGREEMENT (Mar 19 2026), read at primary for the first time. It names the custody trigger, and it is not a date.**
>
> ⚠️ **Scope note: this is NOT the retired ~500K-July question** (PROME's guardrail, correctly set). It is the **registered successor instrument, open question #14** — and the answer arrived from a document STUE had never opened. **For four months this lane was worked entirely through press and a webpage's wording while the governing contract sat free on ed.gov.** `[[finding_a_named_unchecked_fallback_makes_an_absence_closable]]`
>
> - **🔑 THE MECHANISM IS EXEMPTION REVOCATION — binary, legal, and checkable.** Under **31 U.S.C. § 3711(g)(2)(B)**, *"On **May 11, 2001**, Treasury granted Education's request for an exemption for delinquent and defaulted student loans."* Phase 1 = Treasury **revokes** it. **This is the custody event, and it replaces "does a webpage change its wording" as the instrument.**
> - **🔑 AND THE TRIGGER IS A CAPABILITY, NOT A DATE:** *"Education understands that it is Treasury's intent to **revoke the existing exemption once full operational capacity has been reached**."* **The governing document contains NO phase dates at all** (effective on last signature, runs until terminated, 90-day termination notice). ✅ **This retroactively VINDICATES the 8/13 decision to retire the July-wave question as unanswerable — it was unanswerable because the contract never contemplated a dated wave.**
> - **🔑 IT ALSO DISSOLVES THE APPARENT CONTRADICTION.** Pre-revocation, *"Education may refer exempted debts to Cross-Servicing"* — **discretionary referral, with Treasury's approval.** ⇒ **accounts CAN move without the exemption being revoked and without any change to Treasury's public page.** So "Treasury's page still says *helps* ED collect" is strong evidence **against CUSTODY** and is **NOT** evidence against *some accounts having moved*. **Those are two different claims and STUE had them fused.**
> - **⚠️ A THIRD PERIMETER, and it is smaller than everything being quoted.** *"The DRG operates and maintains the Default Management and Collections System (DMCS)… It serves nearly **six million** student and parent borrowers with a current outstanding loan value of over **$120 billion**."* **That — not 9.0M/$220B — is the object Phase 1 actually takes over.** ⚠️ **STUE already tracks Federally-Managed (9.00M) ≠ Direct-Loan (7.20M); DMCS/DRG-serviced (~6M/$120B) is now a THIRD.** It explains why press figures scatter (7.8M/$179B · 9.2M · 9.5M · 10M): **they are mixing perimeters.** **State the perimeter on every default figure, every time.**
> - **✅ "CUSTODY ≠ ENFORCEMENT" IS NOW A CONTRACT CITATION, NOT AN ASSERTION.** *"The Cross-Servicing program will use only the tools **authorized by Education**, as specified in the Cross-Servicing Agency Profile(s)."* ⇒ **the AWG/TOP restart decision stays with ED even after custody moves.** ⚠️ **But note the other half: the IAA specifies the full AWG plumbing** (NOI letter → hearing → AWG order *"generally between 31 and 60 days after sending the NOI letter"*). **The machinery is being built with the switch off — so when ED does authorize it, there is a usable 31–60 day lead between NOI and garnishment.**
> - ✅ **NAME-TRAP SETTLED AT PRIMARY:** the agreement says **Default Resolution GROUP (DRG)** throughout and the phrase **"Default Resolution Hub" appears nowhere in it.** The "Hub" is press framing over DRG/Cross-Servicing integration. **The registered trap was right.**
> - ✅ **270-day default clock CONFIRMED at primary** (*20 U.S.C. § 1085(l)*, quoted in the IAA) — the arithmetic under CRL-28's window and the "no transition-caused default before ~Jul 2027" line now rests on statute, not inference.
>
> **🔧 And the old instrument's caveat is GONE — in the direction that strengthens the negative.** `fiscal.treasury.gov/debt-management/resources/federal-student-loans` now reads **`Last Updated: September 4, 2026`** (`<time datetime="2026-09-04T20:19:22+00:00">`) — it moved past May 18 — **and the language did NOT change:** still *"The U.S. Department of the Treasury **helps** the U.S. Department of Education, Federal Student Aid **collect** defaulted loans,"* still routing to the Default Resolution **Group** at 1-800-621-3115. **The 8/13 read was hedged as "strong negative evidence, not proof, because the page predates the July wave." That hedge no longer applies: the page was touched YESTERDAY and still describes the assisting role.** ⚠️ **One honest limit: a CMS `changed` field can move on a trivial edit, so this kills the "the page is merely stale" explanation without proving an affirmative review.**
> - **✅ OQ#14 leg (b) — vendor awards: checked properly, and the NULL IS VALIDATED.** USAspending, Treasury as awarding agency, actions Mar–Sep 2026: **"default resolution" n=0, "student" n=0** — but the controls FIRE (**"debt collection" n=10, "cross-servicing" n=1, "call center" n=7**), so the query works and the null is real. ⚠️ **Most recent PCA capacity action is a *bridge contract* dated 2025-05-18 — a stopgap, which is the OPPOSITE shape of a build-out toward "full operational capacity."** *(SAM.gov is a JS shell and defeats fetching; USAspending is the workable route — record it.)*
>
> ### 🆕🔴 SWEET v. McMAHON — **ED IS FACING A CONTEMPT MOTION. STUE's "discharges are proceeding" read needs qualifying.**
>
> **Aug 18 2026: PPSL filed a motion to ENFORCE the settlement *and* a motion to hold the Department in CONTEMPT and impose sanctions** [PPSL case page, verified at the primary — the search summary that surfaced it was truncated]. **At least 807 Sweet CLASS members are still awaiting discharges or refunds ED was legally required to provide by deadlines "that have long since passed" — some "more than a year and a half" overdue.**
> - ⚠️ **PERIMETER, because this file has a standing figure-conflation trap on this case: 807 = original-CLASS members with OVERDUE relief.** Not the **>170K** post-class applicants (the 7/17 ruling's cohort), not the **~200K** class, not the **>500K / ≥$23B** whole settlement. **807 is small in count and large in legal significance — it is a contempt predicate, not a population estimate.**
> - **🔧 What this changes:** STATUS carried *"no stay → automatic discharges are proceeding."* **Directionally still true for the 7/17 cohort, but ED's compliance is now formally contested in district court.** Relief *delivery* is the failing leg, not relief *entitlement*.
> - **OQ#9 (does DOE seek cert?) — no petition found in any source this sweep; PPSL's own page reports none.** ⚠️ **Not the same as "DOE declined"** — no deadline is stated. Leaning NO, unresolved. **The live action has moved from the appellate tail to district-court enforcement.**
>
> ### Other lanes — checked, nothing moved
> - **AWG / Treasury Offset: STILL PAUSED, no restart, no ED commitment. 🟡 STUCK holds** (3rd consecutive check). Now corroborated structurally by the IAA's "tools authorized by Education" clause.
> - **SAVE→RAP: ✅ first-tranche date CONFIRMED BY ARITHMETIC AT PRIMARY.** ED's Mar-27-2026 release: notices start **Jul 1**, **90 days** each, auto-enroll to Standard/Tiered Standard, **7.5M** borrowers. **Jul 1 + 90d = Tue Sep 29 2026** — matching the reported *"no borrower required to move off SAVE until September 29, 2026 at the earliest"* **exactly**, and matching STUE's `~Sep 29 – Oct 1` catalyst. **Dec 31 notice + 90d = Wed Mar 31 2027** — matching the carried "last deadlines ~end-Mar 2027." **The carried framing is internally consistent; both ends check out.**
> - ⚠️ **ONE UNRESOLVED SECONDARY CLAIM, FLAGGED NOT BANKED:** a secondary asserts notices ran **"between July 1 and August 15, 2026."** **If true, the full-population CRL-13 read lands ~Nov 13 2026, a full quarter earlier than the carried Q1-2027.** **But ED's own release states NO end date**, and two servicer primaries (Nelnet → Dec 31 2026; MOHELA → Jul-Oct 2026) contradict it. **Servicers send the notices, so servicer FAQs are the right evidence level. Carried framing STANDS; the Aug-15 claim is logged as unverified.** → open question #19.
> - **AFT v. MOHELA: ⚠️ ACCESS FAILURE, NOT A FINDING.** `courtlistener.com/docket/69090685/` returned **HTTP 404** to the curl+UA route that worked on 8/13. **Do not record this as "quiet"** (`[[finding_unfetched_is_not_unavailable]]`). **The 8/13 session paid to find that route and it has since rotted — recorded so the next session does not assume it works.** This row is **event-driven**; not re-chased, per STUE's own standing rule.

## §C2 — THE BASELINE PROBLEM section (8/13 episode, superseded by § #17 ANSWERED) (rotated 2026-10-28)

**Bytes 16041 · CRC32 `e957e453`** · original STATUS.md lines 234–358 at commit before this rotation.

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
> 🔧 **10/28 update to this projection:** FY2026 Q3 printed **9.3M (+0.3M)** and the 271–360-day pipeline at Jun 30 is **0.66M**, so the Sep-30 count looks like roughly **9.5–10.0M**, below the 10.5–11M written above (the bucket undercounts gross inflow). The falsifier thresholds (~11.5M compounding into 2027) are unchanged. Current read: § OPEN QUESTIONS #16.

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


## §C3a — DASHBOARD BODY §D1: superseded CFPB rows (9/5 vintage) + AFT docket-history rows (rotated 2026-10-28)

**Bytes 5808 · CRC32 `7f83d943`** · original STATUS.md lines 460–474 (non-contiguous: 460,461,462,463,465,466,467,470,471,472,474) at commit before this rotation.

| **CFPB complaints — MOHELA (primary API pull)** | **2026 monthly, VINTAGE 2026-09-05:** Jan **913** · Feb **681** · Mar **908** · Apr **910** · May **704** · Jun **815** · Jul **883** · **Aug (d1–22 settled) 475**. ⚠️ **WQ-175 stamp — this series IS revisable:** the same months read 917/682/909/915/703/809 at their 8/13 vintage (deltas −4/−1/−1/−5/+1/+6, all <1%). **Recompute:** re-pull `company=MOHELA` by month and re-locate the settled cliff; do not diff against a prior vintage without re-pulling both | 🟠 at baseline, not accelerating |
| **MOHELA daily rate — the ES-02 / CRL-28 instrument** | **Aug 1–22 (settled) = 21.6/day** · **SAVE wave to date Jul 1 – Aug 22 = 25.6/day** vs the **27–30/day 2026 baseline**. Bands Y >35 · O >45 · **R ≥55 (CRL-28 frozen)** ⇒ **nearest band is 62% above the print**. ⚠️ **YoY like-for-like is mildly UP, not down** (Aug d1–22 **21.6 vs 20.6** in 2025; Jul **30.7 vs 25.5**) — **the Aug fall is largely seasonal, the same July→August drop appears in 2025.** VINTAGE 2026-09-05 | 🟢 **NO SPIKE — 2nd DID_NOT_APPEAR** |
| 🔴 **INSTRUMENT DEFECT — the registered 5–6 day lag rule is WRONG and fails toward a FAKE COLLAPSE** | Settled boundary is a **CLIFF at ~Aug 22 (≈14 days back)**, not a 5–6d taper: Aug 22 = **17**, Aug 23 = **6**, Aug 27 = **3**, Aug 29 = **0**, **Sep 1–5 = 0**. **Applying the documented 5–6d rule on 9/5 reads through Aug 30 and yields 3.3/day — an 85% "collapse" that does not exist.** Backfill is NOT the cause and was measured, not assumed (STUE's own Jul 1–19 window: **539 recorded → 556 today, +3.2%**; settled months <1%) ⇒ it is a **publication BOUNDARY**, not a decay curve. ✅ **FIX: never subtract a fixed N — print dailies and locate the cliff empirically on every pull.** Routed to CARL as a wiring item | 🔴 **fix registered** |
| **Wave-1 complaint tell (Jul 1–19)** | **539 ≈ 28.4/day vs June 27.0/day — NO SPIKE.** ⛔ **The "~5–6d publication lag" qualifier on this row is SUPERSEDED (2026-09-05) — that rule is the one proved defective.** ✅ **Re-derived on fully-settled data: 556 = 29.3/day, still 16% below the >35/day Y band. The null HOLDS** — but it holds on MARGIN (~3% bias vs 16% headroom), **not because the rule was harmless.** *(This row's window was itself selected by the defective rule — pull date minus 5–6d. Flagged by CARL, re-derived, kept.)* | 🟢 **re-derived, holds** |
| — Stay #1 (procedural) | 10/27/2025 minute order: response deadline + discovery stayed pending SCOTUS *Colt/Galette* — **decided Mar 4 2026, unanimous: NJ Transit NOT an arm of the state** | 🟠 **adverse to MOHELA's "creature of Missouri" defense** |
| — **Stay #2 (settlement) — the operative one** | **Mar 20 2026 minute order stayed proceedings "to allow the parties time to explore a negotiated resolution"; parties "engaged in good-faith discussions"; stay extended 60d by JOINT request** [Doc **52**, Joint Status Report 5/18/26 — **free in RECAP**, pulled 7/25] | 🔴 **NEW** |
| — Next step | **Doc 54 filed 7/17/26** = the joint report proposing a schedule. **PACER-only (~$0.30, ~3pp)** — says either *another extension* (talks live) or *merits schedule* (talks failed). **Only remaining unknown on this docket.** | 🟠 **buy** |
| ✅ **2026-08-13 — DOCKET RECOVERED IN FULL. The 8/10 "inconclusive" is CLOSED: CONFIRMED QUIET.** | **Nothing has been filed since Doc 54 (Jul 17 2026).** CourtListener's own `Date of Last Known Filing` field reads **July 17, 2026**, and the entry list ends there. Status unchanged and now *positively verified*: **STAYED, in settlement negotiation, discovery frozen since 10/27/2025.** **Working route (record it — the 8/10 session lost a check to this):** `curl` + browser User-Agent → `courtlistener.com/docket/69090685/`. WebFetch **403s**; the REST API demands auth; **searching the docket NUMBER does not resolve the case, searching the case NAME does.** The 8/10 read was right to refuse to call a blocked mirror "quiet" (`[[finding_unfetched_is_not_unavailable]]`) — the fix was the path, not the data | ✅ **confirmed quiet through 8/13** |
| 🔧 **CORRECTION — Doc 53 was mis-numbered on the NARRATIVE surfaces, and the LEDGER had it right all along** | STATUS (§ WHAT CHANGED #4) and `SV-STUE-2026-07-25-01` both recorded *"May 19 order (**#53**)"*. **Wrong** — #53 is a **Notice of Withdrawal of Appearance filed May 27 2026**; the May 19 order is an **unnumbered minute order**. **`workbook/SERVICER.tsv` row 18 records it correctly** ("May 27 notice of counsel withdrawal (#53)"). ⚠️ **Note the direction: the machine ledger was accurate and the prose retelling degraded it** — the usual assumption is the reverse. **When a ledger and a narrative disagree, the ledger is not automatically the stale one.** SVs are immutable → corrected here, not there | 🔧 |
| 🔴 **GAP — STUE never recorded the Sep 29 2025 dispositive ruling, and it is the most consequential order on this docket** | **Doc 47 (Memorandum Opinion) + Doc 48 (Order), both Sep 29 2025, Chutkan, both FREE:** **MOHELA's motion to dismiss DENIED without prejudice** *and* **AFT's motion to remand DENIED.** ⇒ the case **survived dismissal** and **stays in federal court**. STUE's live files contain zero mention of either; the only "MTD denied" string anywhere is an **April 2025** line in a retired archive file. **This reframes the stay:** the case is not merely procedurally parked — it is parked *after* clearing a dispositive motion, which is why settlement talks are the live path | 🔴 **new to the record** |
| Doc 54 + Doc 51 | **Still PACER-only** (0 RECAP requests on each) — unchanged. Doc 52 and 53 are free and already pulled | 🟠 |

## §C3b — DASHBOARD BODY §D2: closed Treasury rows (Phase-1 ~500K question, Aug-7 plans, 8/13 answer, name trap dup, Federal Register trap, press creep, 8/10 verdict) (rotated 2026-10-28)

**Bytes 5347 · CRC32 `ac9c3ccf`** · original STATUS.md lines 486–503 (non-contiguous: 486,487,488,489,490,491,492,503) at commit before this rotation.

| Phase 1 scope | **~500K defaulted accounts** = launch wave, NOT all ~9M; ramps gradually via Fiscal Service CSP [CRS R48962] | 🟠 |
| Phase 1 execution — "500K by July" wave | ⛔ **QUESTION RETIRED 2026-08-13 — it is not answerable and no longer the right question.** Four months of coverage never produced a launch-day primary, and Treasury's Aug-7 framing moved from a discrete batch to an ongoing build-out (Hub + vendor procurement), so **a clean July yes/no will likely never surface.** Chasing it further is a sunk-cost check. **Replaced by the two instrumented rows below.** | ⛔ retired |
| 🆕 **Aug 7 2026 — Treasury announced PLANS. Read at source 8/13: entirely future tense.** | Article read directly (not via search summary): Treasury "**released plans** to assume management of defaulted student-loan accounts," incl. a **"Default Resolution Hub"** and **vendor partnerships** for collections/counselling; Bessent quoted on "transforming the way defaulted loans are serviced." **The transfer "is set to occur in phases." No completion date, no deadline, and no statement that any accounts have moved.** [Yahoo News 2026-08-07, read in full 8/13] | 🟠 **plans, not execution** |
| 🔴 **THE ANSWER TO THE 8/13 ROW — Treasury's OWN operational primary says the handoff has not happened** | `fiscal.treasury.gov/debt-management/resources/federal-student-loans`, **Last Updated May 18 2026**, still describes the role as: *"The U.S. Department of the Treasury **helps** the U.S. Department of Education, Federal Student Aid **collect** defaulted loans."* That is the **long-standing assisting role** (Cross-Servicing / Treasury Offset / AWG), **not custody or management.** A genuine Phase-1 custody transfer is a change this page would have to reflect, and as of its last update it does not. ⚠️ ~~**Page vintage (May 18) predates the July wave, so this is strong negative evidence, NOT proof.**~~ ✅ **THAT HEDGE IS RETIRED 2026-09-05 — the page now reads `Last Updated: September 4, 2026`** (`<time datetime="2026-09-04T20:19:22+00:00">`) **and the language is UNCHANGED**: still *"Treasury **helps** ED… **collect**"*, still the Default Resolution **Group** at 1-800-621-3115. **It was touched YESTERDAY — 4 weeks after the Aug-7 'Hub' announcement — and still describes the assisting role.** ⚠️ **One honest limit: a CMS `changed` field can move on a trivial edit, so this kills the 'merely stale' explanation without proving an affirmative review.** **Registered as the standing instrument for this question** — a dated, primary, binary surface, which is what the last four months of press-chasing never produced | 🟠 **best available primary read: NOT TRANSFERRED** |
| ⚠️ **NAME TRAP — "Default Resolution HUB" ≠ "Default Resolution GROUP"** | The **Group** is ED/FSA's decades-old default unit, live today with a phone number on the Fiscal Service page (1-800-621-3115). The **Hub** is the *proposed* Aug-7 thing. **The names differ by one word and the evergreen explainer articles are about the Group.** Do not let a piece about the Group be banked as evidence the Hub launched | ⚠️ |
| 🔧 **"Treasury posted it to the Federal Register" — NOT SUPPORTED; do not carry it** | The claim appeared **twice in WebSearch's generated summaries** and is **absent from the article those summaries drew on**. A Federal Register full-text search for **"Default Resolution Hub" across all of 2026 returns ZERO documents**; the Treasury/Fiscal-Service notice lists for Jul–Aug carry nothing on point. **A search-engine summary is not a source** — this one manufactured a specific, checkable, false provenance claim, which is worse than vagueness because it *invites* the reader to stop checking (`[[finding_exact_level_authenticates_a_wrong_direction]]`) | 🔧 **retracted before it entered the record** |
| ⚠️ **Press default-count creep — the secondaries are drifting UP and away from the primary** | Primary (FSA): **9.3M / $234.1B at Jun 30 2026** (was ~9.0M / $220B / >13% at Mar 31 — the figure this row was written against). Press: 9.2M (ED official, Mar) → **9.5M** (Fox, Jul 21) → **10M** (Yahoo, Aug 7). **Meanwhile the same Aug-2026 secondaries still recycle "$180 billion / 11%" — which are the DEC 2025 figures.** So current coverage simultaneously *overstates* borrowers and *understates* dollars. **Cite the primary; next FSA print (~Sep) settles it.** | ⚠️ **unchanged rule: primary wins** |
> ⚠️ **2026-08-10 verdict on Phase 1 launch: INCONCLUSIVE.** Free web search found no primary confirming the ~500K account wave actually transferred/borrowers were contacted in July as originally framed. **But the question itself may now be the wrong one to close on 8/13**: the Aug 7 "Default Resolution Hub" + vendor-partnership announcement suggests Treasury's own framing has shifted from a discrete "500K by July" batch toward an ongoing operational build-out — a July yes/no answer may never surface cleanly. **Recommend CARL do NOT prune the 8/13 row outright; re-scope it** to "has the Default Resolution Hub gone live / have vendor partnerships been named?" rather than continuing to chase the original July figure. AWG/TOP involuntary collections still show no restart signal in this sweep — custody-build-out ≠ enforcement, unchanged.

## §C4 — OPEN QUESTIONS: bodies of resolved/retired questions #1, #2, #4 (+table), #5, #6, #8, #15, #17 (rotated 2026-10-28)

**Bytes 6236 · CRC32 `b7fee8a2`** · original STATUS.md lines 603–633 (non-contiguous: 603,605,607,608,609,610,611,612,613,614,615,616,617,619,631,633) at commit before this rotation.

1. ✅ **RESOLVED 2026-07-25 (same session) — and it was free.** *Basis of the Mar 20 2026 stay:* **settlement negotiation.** Doc 52 (Joint Status Report 5/18/26, free in RECAP): the Court stayed proceedings *"to allow the parties time to explore a negotiated resolution"*; parties *"engaged in good-faith discussions"*; stay extended 60d by joint request. **I had wrongly called this PACER-gated** — I declared the path closed without checking RECAP's free-document list, the same error as the 46-day docket-number miss ([[finding_audit_resolution_path_before_reattempt]]). **Successor question → #8.**
2. ✅ **RESOLVED 2026-08-13 (Q2 HHDC, rel Aug 11) — YES, and the flow answer is the bigger one.** Stock **10.34% → 10.60%**, so CRL-04 holds on a 2nd consecutive >10% print and is not a single-print artifact. **The stock-up/flow-down ambiguity flagged at registration resolves to COHORT EXHAUSTION**: flow into 90+ went 16.19 → 10.86 → **7.83%**, halving twice while the stock rose. On-ramp slack and seasonality are both refuted by the repetition across two quarters. ES-STUE-03 logged **APPEARED (Y)**.
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
8. ✅ **RESOLVED — Tue Aug 11, the FALLBACK Tuesday.** The base rate's *band* (1st or 2nd Tuesday of August) held for a 5th year; its *point estimate* (Aug 4, on 3-of-4 support) was wrong. **Calibration lesson, kept because it is cheap and repeatable: with 3-of-4 support, publish the band and treat the mode as colour.** A 75%-confidence point estimate that misses is not a broken method — but STUE wrote "modal Tue Aug 4" into a 🔴 DO-THIS-FIRST line and a BOTTOM LINE, which reads as a date. **Next quarter: poll `HHD_C_Report_2026Q3.xlsx` directly rather than watching for an advisory.**
15. ✅ **RESOLVED 2026-08-13, same session it was opened — FSA archives pulled, and the count does NOT rescue the level claim.** Like-for-like **7.90M → 9.00M = 1.14×**. The registered "~5M ⇒ ~1.8×" prior was a **perimeter error** (Direct-Loan baseline against a Federally-Managed numerator) — **that part stands.** ⚠️ **But the accompanying "−16.2% below trend" figure is WITHDRAWN, and the 7.90M baseline is itself for-profit-contaminated** (§ THE BASELINE PROBLEM), so **this question is only PARTLY resolved: the down-market K-shape hypothesis is not supported on a like-for-like ratio, but the counterfactual it was measured against does not hold. Real resolution needs #17.** What survives is the **speed** — +3.8M in two quarters, ~16× the pre-pandemic pace — which is a catch-up pulse off a stock that had been drained to 5.2M, not accumulation to new highs. Full working → § THE BASE-RATE CHECK. **Successor → #16.**
17. ✅ **ANSWERED 2026-08-13, same session it was opened — and the answer REVERSES the morning's reading.** **The dominant composition effect is the DENOMINATOR, not cohort quality:** the share of portfolio dollars in active repayment (the only balances that *can* be delinquent) fell **53.8% → 38.5%** while forbearance rose **10.0% → 29.5%**. Exposure-adjusted, 90+ among those actually in repayment went **7.97% (2015–19) → 10.95% (FY2026 Q2) = 1.37×**, cross-checked at **1.31×** by an independent route. **Registered prior CONFIRMED — today's 10.60% IS elevated — but by a mechanism I did not anticipate.** ⚠️ **The for-profit cohort adjustment this question originally specified is STILL NOT DONE** (it would push the baseline lower still and make today look worse — unmeasured, so unclaimed). Full working → § #17 ANSWERED. **Residual threat → #18.**

## §C5 — READ-CAP ROTATION 2026-09-05 log section (rotated 2026-10-28)

**Bytes 2324 · CRC32 `68803cf7`** · original STATUS.md lines 534–552 at commit before this rotation.

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


## §C6 — ROUTED TO PARENT: 9/5 rows, all integrated/ruled (rotated 2026-10-28)

**Bytes 1167 · CRC32 `4820ddff`** · original STATUS.md lines 519–525 (non-contiguous: 519,520,521,522,523,525) at commit before this rotation.

| **ES-02 mechanism warning** (2nd DID_NOT_APPEAR) | **NOT a re-price.** CRL-28's window opens Oct 1 2026, so a pre-window null cannot grade it. Registered decision point = MOHELA notice completion **~Oct 31** | ✅ **INTEGRATED** — CARL 9/5: KB-CARL-425; no confidence touched |
| **ES-02 instrument DEFECT** (5–6d lag rule → fake 85% collapse) | Wiring item: never subtract a fixed N; locate the cliff empirically | ✅ **ADOPTED + ROUTED ONWARD** — CARL → PROME, recommended to DAEDALUS as a candidate fleet rule. **Promoted to fleet auto-memory as `finding_dormant_instrument_is_a_query_plus_unexercised_reading_rules`** |
| **FSA release NOT posted** (MD5-verified) | Leave CARL's default-stock figures untouched at their Mar-31-2026 as-of | ✅ **INTEGRATED** — KB-CARL-424 |
| **DMCS/DRG third perimeter** (~6M / $120B) | New KB row; bears on the denominator work | ✅ **INTEGRATED** — KB-CARL-423 |
| **Sweet contempt motion** (Aug 18; 807 class members) | Qualify the "discharges are proceeding" read | ✅ delivered |
| **STATUS read-cap** | Ruling requested | ✅ **RULED 9/5 — rotate, do not split.** Executed same session; see § below |

## §C7 — CATALYSTS: two closed rows (rotated 2026-10-28)

**Bytes 736 · CRC32 `1e194dc8`** · original STATUS.md lines 435–437 (non-contiguous: 435,437) at commit before this rotation.

| ~~(see re-dated FSA row above)~~ | ⛔ **CLOSED 2026-10-28** | The FSA release posted 9/18 (FY2026 Q3: 9.3M / $234.1B; 15.7% of repayment dollars 31+ late). The 9.0M vs 9.5M press gap is settled in § SIGNAL DASHBOARD. Kept as a one-line marker for the next rotation |
| ~~**~Sep 29 – Oct 1**~~ **READ 10/01 by CARL: NO GRADEABLE DATA** | **SAVE→RAP first-tranche non-selection read** | **CRL-13 partial N — no wave-level count exists in public (KB-CARL-501); CRL-13 OPEN 75% unchanged. Notice windows are servicer-specific (Edfinancial 7/1–8/15, MOHELA Jul–Oct), so the 'Department-wide 12/31' inference is withdrawn. First proxy: FSA Data Center 9/30-data refresh ~mid/late Dec 2026; AFT v. ED status conference 10/14.** |

## §C8 — Head pass: rotation-pointer stack, 7/25 thesis narrative, closed dashboard rows (rotated 2026-10-28)

**Bytes 7909 · CRC32 `09bbed30`** · original STATUS.md lines 35–189 (non-contiguous: 35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,100,162,164,167,179,189) at commit before this rotation.

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
### ⚑ WHY THE DOWNSTREAM LOOKS QUIET — four-channel decomposition

**[ROTATED 2026-09-05 → archive §B8 — already marked ⛔ SUPERSEDED on 8/13.]** Will's framing that only ONE of four channels is genuinely "not firing yet": **forbearance→default conversion is a real lag (earliest ~Jul 2027); enforcement is BLOCKED not pending; servicer attribution gets WORSE via settlement; the CC cascade was arithmetically too small (~2% of card balances) to ever carry it.** ⚠️ **That decomposition is still the right map and is retained verbatim in the archive** — it was superseded only as a *discriminator*, because the Q2 print it pointed at contains zero post-transition borrowers. **First readable cascade signal is 2027:Q1 HHDC (~May 2027).** See also § CHANNEL 5 (FHA/mortgage), which is live and stays here.

---

What the 7/25 session changed is **not the mechanism but the enforcement and attribution legs**:

1. **Enforcement is gated in two independent places.** Involuntary collections remain **paused indefinitely** (Jan 16 2026, no corroborated restart), and the accountability channel — AFT v. MOHELA — is under a **court-ordered stay with discovery frozen**, with no class-certification motion filed. Neither can produce a Q3-Q4 2026 event. CRL-14's "MOHELA-caused defaults" leg therefore rests on **operational failure**, not litigation or garnishment.
2. **Attribution is narrower than STUE previously asserted.** The score cascade is real and severe *within* the affected cohort but is **second-order in aggregate** — it cannot carry a CC 90+ GFC breach on its own (DEWEY C2). Carrying the broad version into the 8/15 print would contaminate the CRL-05 grade.
3. **The transition timeline tightened.** Notices complete Dec 2026 (was Mar 2027); final selection deadlines ~Mar 2027. The **first-tranche read is still ~Oct 1**, but the full-population N now lands **earlier and more compactly** — which *improves* CRL-13's readability at Q1 2027.

**v2.5.1 thesis: ⚠️ INTACT AS OF 7/31, but see § THE BASELINE PROBLEM (8/13) — the level claim underneath it is contested in BOTH directions and is not settled.** The Q2 HHDC grader **has fired (Tue Aug 11)**; ~Oct 1 (CRL-13 first tranche) is the next.

> ⛔ **[ROTATED 2026-09-05 → archive §B6]** The Q2-HHDC advisory-watch blockquote, already marked SPENT — the event it forecast happened Tue Aug 11 2026. **The two lessons that outlived it are kept:** with 3-of-N support publish the BAND and treat the mode as colour; and **poll the deterministic data URL (`HHD_C_Report_<YYYY>Q<N>.xlsx`, curl + browser UA), never hunt for a media advisory.**
| Transition rate INTO 90+ DQ (4Q moving sum) | ⛔ **SUPERSEDED by the two flow rows above** — this row was the Pg-28 by-age cut. At Q1 it was indistinguishable from Pg 14 (10.86 vs 10.8609); at Q2 the two diverge, so the series is no longer a safe stand-in. **Do not refresh this row; read Pg 13/14.** | Q1 2026 (last valid) | NY Fed Pg 28 | ⛔ retired 8/13 |
| **9th Cir appeal (26-1136) — ✅ DECIDED Fri Jul 17 2026, DOE LOST, UNANIMOUS** | **STUE MISSED THIS IN THE 7/25 REFRESH — it fired 8 days before that session.** Panel **Wardlaw / Owens / Bress** unanimously rejected DOE's appeal to delay relief for **>170,000 post-class applicants**, affirming the district court: DOE **failed to show the "changed circumstances"** legally required to modify a settlement it signed in 2022, and "knew exactly what it was signing up for." Prior STATUS carried *"no oral argument scheduled, ~Sept projected, watch-only"* — the court ruled without one. Briefing had completed **May 7 2026** *(also corrected 7/31 from a "2025" year typo)*. Earlier published order **3/25/26** denied DOE's stay bid; this is the merits loss. | 🟢🔴 **RESOLVED — DOE lost** |
| — what's left | ~~**DOE has not said whether it will appeal; the only remaining stop is SCOTUS.** No stay in place → **automatic discharges are proceeding.**~~ 🔧 **QUALIFIED 2026-09-05 — entitlement is settled, DELIVERY is now formally contested.** No cert petition found in any source this sweep (PPSL's own page reports none) ⇒ **leaning NO but unresolved — no deadline stated.** **The live action has moved from the appellate tail to district-court ENFORCEMENT** | 🟠 **re-opened** |
| — ⚠️ date-conflict note | Forbes 7/21 (Minsky) dates the ruling **"Friday, July 18"** — **July 18 2026 is a SATURDAY.** PPSL (7/23 release) and The College Investor both say **July 17**, which **is** a Friday. **7/17 is correct**; the weekday check broke the tie. *(Second time in two sessions the same `date` check caught a bad date — see the 8/15 HHDC catch.)* | 🔧 |
| 🔧 **Bucket shape — AGING WITH NO CURE. ⚠️ NOT an exhaustion test (claim DOWNGRADED 2026-09-05)** | 31–60 DPD fell **4.204% → 2.978%** while 61–90 rose **2.814% → 3.279%** and 91–120 rose **1.410% → 1.932%** — **the early bucket drained INTO the aged buckets.** ⛔ **This is CONSISTENT WITH delinquency aging and an absence of cure. It is NOT independent corroboration of COHORT EXHAUSTION** — that needs an **inflow / cohort-flow** measure, and a bucket-mix shift over **one month** is not one. ⚠️ **And the populations differ:** this is a **legacy FFELP pool**, not the ~9M defaulted federal cohort — **STUE's own scope note says exactly that**, so using it to corroborate a federal-cohort finding is a **population mismatch**. *(I wrote "independent corroboration… on a completely independent instrument." The INSTRUMENT is independent; the POPULATION is not the subject. Caught by Codex.)* | 🔧 **downgraded** |
> **Corrected 7/25:** the prior "Expected Restart **Jul 2026** 🔴 IMMINENT" row was wrong and contradicted the parent. July passed with no restart. Threshold **STUCK**, mechanism (default accrual) **intact** — matches parent CRL-14 split.

## §C9 — 10/28 session block + closed catalyst, routing and Sweet rows (rotated 2026-10-28 22:20 EDT)

**Bytes 14020 · CRC32 `5ba2e6c1`** · original STATUS.md lines 5–374 (non-contiguous: 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,149,150,296,297,301,303,361,369,370,371,372,374) at commit before this rotation.

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
>
> ### ✅ CLOSEOUT 2026-10-28 22:09 EDT — run to the DOC/CARL standard by hand (STUE's own step list is under-specified; proposal sent to CARL)
> | Check | Result |
> |---|---|
> | Inbox | empty (2 CARL packets processed, `git mv` to `processed/`) |
> | ES tracker | ES-01/04/06 graded on FY26 Q3; ES-02 interim logged; CARL ruling recorded |
> | State vectors | SV-STUE-2026-10-28-01, -02 |
> | Ledgers (`ledger_staleness`) | CASCADE / SERVICER / TIMELINE ok; STATE_DQ FROZEN |
> | Weekday (`claim_check`) | 1 flag, false positive ("Washington Sun" read as Sunday) |
> | Orphans (`orphan_check.sh CARL`) | no STUE items |
> | Read cap (`--agent STUE`) | ⏳ **rc=2 CANNOT-EVALUATE** (re-run 22:2x): STATUS is now registered in READS.tsv as a *scoped* read (bounded head), so the whole-file failure is gone; the check waits on **STUE's own attestation**, sent to PROME (`PROME/inbox/2026-10-28_from-STUE_READS-attestation.md`), which also declares two previously unregistered scoped reads (CARL STATUS grep, CARL PREDICTIONS lookup) |
> | Memory | extended `finding_scan_keyed_on_naming_reads_local_form_as_absence` (n+1); `--slug` check rc=0; index 71% of cap |
> | 60-day retirement | no candidates (`domain/StudentLoan_Data_2026-02.md` is >60d but cited live by `CLAUDE.md`; retained) |
> | Next run docketed | ✅ CARL CATALYSTS + CALENDAR now carry the **ES-02 grade (11/13)**, HHDC 11/05, Sweet 11/05, AFT 11/23 11:00 ET (corrected), FSA ~12/18 (CARL `2f6c64bd3`, verified) |
> | ⇒ | **PARTIAL closeout, one item left:** read-cap evaluation awaits PROME's transcription of STUE's attestation. The closeout-protocol upgrade is **done**: Will authorized STUE to edit its card (22:1x), but CARL had already applied the proposal verbatim in `2f6c64bd3` (§ On Session End steps 0, 3c–3e, 4b, 5, 6), so no STUE card edit was made |
| Exhibit C (Jan 28) / non-Exhibit C (Apr 15) deadlines | Both MISSED → auto Full Settlement Relief triggered | 🔴 |
| **Jun 15 notice deadline** | ✅ **MET** — first Sweet deadline DOE did not miss. **~30–36K** discharge-eligibility emails week of Jun 15 to non-Exhibit C post-class applicants (Jun 23–Nov 16 2022 filers) | 🟢 **resolved** |
| ⛔ **7 FIRED/CLOSED catalyst rows ROTATED 2026-09-05 PM** → `archive/STUE_STATUS_ARCHIVE_2026-09.md` **§B9** (2,677 B, CRC32 `cb276a5c`) | Treasury Phase-1 verification · AFT docket check · the Q2 HHDC print · the NY Fed advisory-watch · the ~Aug-20 CFPB re-pull · the ~Sep FSA release row (now header-triggered) · the ~Sep-15 *Sweet* oral argument that never happened. **Two figures carried forward here because the safety test flagged they would otherwise leave STATUS entirely: the Q2 CC 90+ print was 12.92%, and CARL cut CRL-05 85→20 on it.** ⚠️ *Both are CARL's, not STUE's — recorded as context, and STUE still does not mirror a CRL confidence as its own state.* | ⛔ **rotated** |
| ~~Fri 2026-09-11~~ **FIRED 9/18, graded 10/28** | FSA FY2026 Q3 release (LM Fri 18 Sep 2026; CARL caught it 9/24) | ES-01 NO VERDICT (straddles Y) · ES-04 not gradeable · ES-06 access gap. **Next: FY2026 Q4 (Sep 30 data), expected ~mid/late Dec 2026. Poll the `last-modified` header weekly from ~Dec 1** |
| ~~**~Oct 31**~~ **→ done by Sep 30** | MOHELA notice waves complete — **its FAQ now says notices went out July–September 2026** (primary, 10/28) | ⇒ MOHELA's 90-day windows close by **~Dec 29 2026**; first auto-enrolments from ~Sep 29 (+ ~30-day final notice ⇒ ~Oct 29). **The complaint window that matters is Oct 2026 – Jan 2027.** The ES-02 grade date (~Nov 13/16) is unchanged |
| ⛔ **2 closed rows ROTATED 2026-10-28** → archive §C7 (736 B, CRC32 `1e194dc8`) | The superseded FSA "see re-dated" marker and the 10/01 first-tranche read (no gradeable data; CARL KB-CARL-501) | ⛔ |
**[ROTATED 2026-09-05 → `archive/STUE_STATUS_ARCHIVE_2026-09.md` §B7]** The 7/25–7/31 routing table, closed with nothing owed in either direction, verified against the parent's committed files. **The two procedural lessons are kept and are live in boot step 2b:** check adoption against the parent's FILES, not against a claim of processing — and check whether the parent is mid-session before reading a stale stamp as neglect.
| ⛔ **6 closed 9/5 rows ROTATED 2026-10-28** → archive §C6 (1167 B, CRC32 `4820ddff`) | ES-02 mechanism warning, lag-rule defect, FSA not-posted, DMCS perimeter, Sweet contempt, read-cap ruling — all integrated or ruled by CARL | ✅ closed |
| **OQ#19 — SAVE notice-window conflict** | Aug-15 secondary would pull CRL-13's full-population read to ~Nov 13 2026 vs carried Q1-2027 | 🟠 **OPEN — carried framing STANDS.** CARL 9/5: settle on a **servicer primary before Oct 1**; decide on evidence, not a secondary |
| **10/28 delivery** (`SV-STUE-2026-10-28-01` + packet `AGENTS/CARL/inbox/processed/2026-10-28_from-STUE_FSA-Q3-grades-AFT-collections.md`) | ES-01 NO VERDICT (straddles Y) · ES-04 not gradeable · ES-06 access gap · ES-02 interim 24.8/day · AFT v. ED date correction (10/14, not 10/28; no new count) · collections still paused. **No CRL change proposed** | ✅ **ADOPTED 10/28** — CARL KB-568/569, STATUS Student/FSA row; ES-02 placement reading AFFIRMED (carl-6f) |
| **10/28 research pass** (`SV-STUE-2026-10-28-02` + packet `…/2026-10-28_from-STUE_research-items-treasury-pilot-SAVE-windows.md`; `research/README_2026-10-28_research-items.md`) | Treasury Education PCA pilot (awarded, then terminated Jun 3); SAVE windows servicer-specific (MOHELA Jul–Sep); score-drop band sourced; AFT Doc 50 figures checked; 13M attribution unverified; 3 card fixes | ✅ **ADOPTED 10/28** — CARL KB-CARL-573 + STATUS wording; card fixes applied in STUE `CLAUDE.md` (lines 95, 109, 130 verified); PROME DOCKET L154 resolved |
> ⚠️ **Historical routing table (7/25–7/31, all adopted, nothing owed) → `archive/STUE_STATUS_ARCHIVE_2026-09.md` §B7.**
