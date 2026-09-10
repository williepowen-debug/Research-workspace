# STUE — CLAUDE.md PROVENANCE COMPANION
> ## ⛔ Nothing here is an instruction. The CARD (`CLAUDE.md`) holds the rules; this file holds the STORY BEHIND THEM.
**Created 2026-09-05** (Will-authorised card rotation). Blocks are **VERBATIM** from `CLAUDE.md`, byte- and CRC32-stamped. ⛔ **GREP THIS FILE — never read it whole.** On grep terms it carries no read-cap budget claim (`READ_CAP.md` rule-8 mode ruling).
**Why the split:** the card is read WHOLE at every boot, and it had grown to **1.58× the read-cap budget**. The rule stays in the card; the incident narrative that produced the rule moves here. ⚠️ **A card that carries live VALUES also goes stale silently — one figure moved here (the Fiscal Service page's "Last Updated May 18 2026") had already been superseded by September 4 2026 while sitting in the card as fact.**

---

## Manifest

| § | Block | Bytes | CRC32 |
|---|---|---:|---|
| **P1** | Key Signals to Monitor — full prior text (values + provenance) | 13,107 | `5d920412` |
| **P2** | CARL Cross-References — KB/VX/FLOW ids and CRL history | 4,400 | `ee0935af` |
| **P3** | Why This Domain Matters — full narrative | 1,034 | `d4e34a9d` |
| **P4** | The 2026-07-31 reconcile preamble | 606 | `bb09663a` |

**Total moved out of the card: 19,147 B.**

---


## §P1 — Key Signals to Monitor — full prior text (values + provenance)

*Verbatim. 13,107 B · CRC32 `5d920412`*

---

## Key Signals to Monitor

> *Anchors below reconciled to STATUS 2026-07-31. This section had drifted ~7 weeks behind `STATUS.md` (pre-correction Treasury scope, a single-cliff SAVE window, a fired FSA release still written as "next"). **Anchors are pointers, not the dashboard — `STATUS.md` is canonical.***

**Delinquency / Default:**
- FSA Data Center quarterly updates — **Q1 2026 released Jun 23 2026** (EA GENERAL-26-38, data as of Mar 31). **Next: Q2 ~Sep** (2nd default-stock print; settles the 9.0M-vs-9.5M press gap; refreshes the stale 18.6% cut)
- NY Fed Quarterly Report on Household Debt (HHDC) — **Q2 2026 PRINTED Tue Aug 11 2026** (the *fallback* Tuesday; the band held, the modal Aug-4 point estimate missed). **Base rate now 5 years: Q2 lands on the 1st or 2nd Tuesday of August, 11:00 ET** (Aug 2 '22 · Aug 8 '23 · Aug 6 '24 · Aug 5 '25 · **Aug 11 '26**) — **3 of 5 first Tuesday, so publish the BAND and treat the mode as colour.** ⚠️ **Retrieval, learned the hard way — do not repeat the advisory-watch:** `newyorkfed.org` **403s WebFetch**, but the data files are on a **deterministic URL** and need no advisory at all: `curl` + browser User-Agent → `newyorkfed.org/medialibrary/interactives/householdcredit/data/xls/HHD_C_Report_<YYYY>Q<N>.xlsx`. **Poll that path; do not hunt for a media advisory.** *(STUE spent two sessions watching for an advisory it never found, and the print landed anyway.)*
  - **Which sheet is canonical** (register **S4** — settled 2026-08-13): **Pg 12** = 90+ *stock* share by loan type · **Pg 13** = new delinquent (30+) by loan type · **Pg 14** = new seriously delinquent (90+) by loan type ⇐ **cite Pg 13/14 for flow.** ⚠️ **Pg 28** (student transition by age, 4Q moving sum) tracked Pg 14 within ±0.01pp for five quarters and then **diverged +0.39pp in 26:Q2** — it is **not** an interchangeable stand-in. **Never silently substitute one for the other.**
- Default count trajectory — **~9.0M / $220B as of Mar 31 2026** (FSA primary; 6.0M Aug'25 → 7.7M Dec → ~9.0M Mar, **+1.3M QoQ**). The **13M EOY-2026** (TCF) projection needs *acceleration*: current pace implies ~11.6M
- **Cure channel (track the offset, not just the inflow):** 2.6M gross Q1 DRG transfers vs +1.3M net stock rise ⇒ **~1.3M/qtr exits** (rehab / consolidation / discharge / cure). Durability is an open question
- Active repayment 31+ DQ rate — 18.6% by dollar, **Dec 2025 [STALE — not restated in the Jun-23 release]**
- Repayment status — **17.2M recipients (42%) / ~$633B in repayment-or-delinquency; 8.4M (~⅕) / ~$485B in forbearance** (Mar 31 2026, FSA). Forbearance is the reservoir feeding Q3-Q4

**SAVE / RAP Transition (FIRING — launched Jul 1 2026):**
- ~7–7.5M SAVE borrowers receiving transition notices, **issued in WAVES**
- ⚠️ **NOT a single cliff.** The 90-day selection clock runs from **each individual borrower's notice**. **~Oct 1 2026 = FIRST-TRANCHE read only (partial N)**; full population resolves ~Q1 2027. Treating Oct 1 as the full-population read is the CRL-09 denominator-mismatch trap
- **Notice window COMPRESSED ~3mo (7/25):** all notices by **Dec 31 2026** (was Mar 2027) ⇒ last selection deadlines ~end-Mar 2027. MOHELA's own window is tighter: **Jul → Oct 2026**
- Auto-transition for non-selectors → **Standard**, or **Tiered Standard** for loans first in repayment on/after Jul 1 2026 (MUCH higher payments; $0-70/mo → ~$407/mo avg)
- RAP enrollment rates and payment adequacy
- Forbearance-to-repayment conversion wave (Q3-Q4 2026)

**Servicer Performance:**
- MOHELA: 2.5M missed bills → 800K delinquent; **280K borrowers overcharged** (wrong calculation guidelines); systematic call-centre "deflection" to self-help channels [AFT amended complaint 1/15/26, via Protect Borrowers / NCLC]
- **Call metrics — two different instruments, both valid, do not merge them:**
  - **Abandon / wait level [FSA servicer performance data, cited in 2026 filings]:** ~13 min avg wait, **~14% abandon**, longest of the major federal servicers; no other major peer exceeds ~5%. *Use this for level comparisons.*
  - **Wait-time RATIO [AFT complaint via PB/NCLC]:** MOHELA borrowers wait **~7×** EdFinancial and **>50×** Aidvantage / CRI / Nelnet. *Plaintiff-sourced and advocacy-framed — attribute it, don't launder it as neutral.*
  - ⚠️ *Correction to a 7/31 correction: this pass first struck "7x-50x" as uncorroborated, then found the source the same session. It is **sourced**, and it measures **wait time**, where the FSA figure measures **abandon rate** — different quantities, not a contradiction. **"I can't find it in my preferred source" is not "it is unsupported"** — name the source you checked before declaring a claim unsupported.*
- Nelnet: credit reporting errors, balance duplication
- Class action (Feb 18, 2026): doubled balances on credit reports *[not re-verified since build — treat as unrefreshed]*
- State AG investigations (MOHELA) — 9-state CID working group
- DOE payment withholding ($7.2M penalty) *[not re-verified since build]*
- **CFPB complaint tell (registered instrument):** `company=MOHELA` daily rate vs the **27-30/day 2026 baseline**.
  - 🔴 **THE OLD RULE HERE — *"~5-6 day publication lag — never read the trailing week"* — IS RETIRED AS PROVEN FALSE (2026-09-05). Do not reinstate it.** Measured: the settled boundary is a **CLIFF ~14 days back**, not a taper. **Applying the retired rule on 2026-09-05 would have read 3.3/day — a fake 85% collapse.** Backfill was measured, not assumed (a settled window re-pulls +3.2%; settled months <1%) ⇒ it is a publication **BOUNDARY**, not a decay curve.
  - ✅ **THE RULE: never subtract a fixed N. Print the dailies and locate the boundary with the pre-registered completeness test** ⚠️ **(marked PROVISIONAL — validated IN-SAMPLE on the very cliff it was built to explain.)**
    - **Out-of-sample test = the NEXT CFPB `company=MOHELA` PULL.** ⚠️ **NOT the FSA `PortfolioByLoanStatus` poll (DOCKET L281)** — that is a `last-modified` header check on a different source and **cannot test a daily-series boundary algorithm at all.** *(Mislabel corrected 2026-09-05; it originated upstream and STUE propagated it without checking that the named test could actually exercise the rule — `[[finding_guard_correctness_and_wiring_are_independent]]`.)*
    - ⛔ **IF THE TEST AND AN EYEBALL READ DISAGREE, THE ANSWER IS NO VERDICT — not the eyeball.** *(Corrected 2026-09-05: this line first read "believe the eyeball," which **directly contradicted** the NO-VERDICT clause three lines above it, since believing the eyeball IS the analyst-selected cutoff that clause exists to forbid. Both were written the same session, hours apart, in two files.)* **The eyeball's ONLY role is to diagnose and REVISE the algorithm afterwards — never to convert a NO VERDICT into a call in the moment.** in `workbook/EXPECTED_SIGNALS_TRACKER.md` § ES-STUE-02 — same-weekday normalisation (weekends run ~half of weekdays and an un-normalised test reads a Sunday as a cliff); a day is COMPLETE at **ratio ≥ 0.70** of its same-weekday median over the prior 4 weeks; **boundary `D` = the most recent date where `D`, `D−1`, `D−2` are all complete.**
  - ⛔ **NO VERDICT — report no rate at all — if (a) no qualifying `D` exists within 30 days of the pull, or (b) the BAND COLOUR changes when `D` moves ±3 days.** An ambiguous boundary yields **NO VERDICT**, never an analyst-selected cutoff.
  - ⚠️ **And the caveat that makes this worth fixing rather than noting:** both MOHELA nulls survived this defect on **margin** (~3% bias against 16-40% headroom), **not because the rule was harmless.** A series sitting near its band would have been decided by it.

**Treasury Transfer:**
- ⚠️ **Mar 19 2026 = the ED/Treasury partnership ANNOUNCEMENT, not an operational handoff.** Do not read it as completed
- **Phase 1 scope = ~500K defaulted accounts (launch wave), NOT all ~9M** — ramps gradually via Fiscal Service CSP [CRS R48962]. *(Scope corrected 2026-06-09; the ~9M framing was wrong.)*
- ⛔ **Phase 1 execution — QUESTION RETIRED 2026-08-13 as unanswerable.** Four months produced no launch-day primary, and Treasury's Aug-7 framing moved from a discrete batch to an ongoing build-out (a "Default Resolution Hub" + vendor procurement, all future tense), so a clean July yes/no will likely never surface. **Best primary read: NOT transferred** — `fiscal.treasury.gov/debt-management/resources/federal-student-loans` (**Last Updated May 18 2026**) still says Treasury *"**helps** the U.S. Department of Education, Federal Student Aid **collect** defaulted loans"* = the standing assisting role, not custody. ⚠️ Page vintage predates the July wave ⇒ strong negative evidence, not proof.
  - **The two registered successor instruments** (dated, primary, binary — which press-chasing never gave us): ① does that Fiscal Service page move past **May 18 2026** and change its "helps…collect" language to custody/management? ② do **vendor awards** appear (USAspending / SAM.gov / Fiscal Service procurement) and does a real borrower-facing **"Default Resolution Hub"** exist? → STATUS open question #14.
  - ⚠️ **THREE TRAPS, all live:** **(a) "Default Resolution HUB" ≠ "Default Resolution GROUP"** — the *Group* is ED/FSA's decades-old default unit with a live phone number on that same page; evergreen explainers about it read exactly like evidence the Hub launched. **(b) "Treasury posted plans to the Federal Register" is NOT SUPPORTED** — it appeared only in **WebSearch-generated summaries**, is absent from the underlying article, and an FR full-text search for the phrase across all of 2026 returns **zero**. *A search summary is not a source, and a fabricated-but-checkable provenance claim is worse than vagueness because it stops people checking.* **(c) Press count creep** — 9.2M (Mar) → 9.5M (Jul) → 10M (Aug 7), while the same Aug-2026 articles still recycle **"$180B / 11%"** (*Dec 2025* figures). **Primary wins: 9.00M / $220.3B / >13%.**
- ⚠️ **Custody ≠ enforcement.** This is a servicing/collections custody handoff, NOT involuntary-collections resumption. Do not conflate (the enforcement/attribution split originally reasoned through CRL-14 — retired 7/31, superseded by CRL-28 — still governs)
- Involuntary collections (AWG + Treasury Offset) — **PAUSED since Jan 16 2026, indefinitely.** Reported expectation "late summer or fall," **no ED commitment, no corroborated restart date** → threshold **STUCK**
- Phase 2: non-defaulted portfolio · Phase 3: full takeover including FAFSA (planned, no public dates)
- Legal challenges to authority; GOP bill introduced to codify

**Borrower Defense / Sweet v. McMahon:**
- **Jan 28 + Apr 15 2026 deadlines MISSED → auto Full Settlement Relief triggered.** **Jun 15 notice deadline MET** (first one DOE did not miss): **~30-36K** discharge-eligibility emails to non-Exhibit C post-class applicants (Jun 23–Nov 16 2022 filers)
- DOE 1-year completion deadline → relief delivery **~Jun 2027**; ~271K cumulative relief pipeline (PPSL)
- 9th Cir appeal **26-1136** — ✅ **DECIDED Fri Jul 17 2026: DOE LOST, unanimous** (Wardlaw/Owens/Bress). Panel affirmed the district court — DOE failed to show the "changed circumstances" needed to modify its own 2022 settlement ⇒ relief for **>170K post-class applicants** stands. No oral argument was ever held. **Only remaining stop is a discretionary SCOTUS cert petition; no stay, discharges proceeding.** ⚠️ **Headlines say "500,000" — that is the WHOLE settlement (≥$23B, >500K borrowers, ~200K original class). This ruling's cohort is the >170K post-class applicants. Do not conflate.**
- 750K+ total claims filed; pipeline of future applicants from 150+ flagged schools

**Credit Score Destruction:**
- ⚠️ **SIX score-drop figures exist across STUE and CARL and they measure DIFFERENT COHORTS — read `STATUS.md` § SCORE-DROP RECONCILIATION before citing any of them.** Default to **−62 pts** (FICO Spring 2026, average borrower with a new SL delinquency, H2 2025).
- **Corrected 2026-07-31:** this line previously read *"superprime borrowers losing −171 pts when payments resume."* The source (**NY Fed Liberty Street, Mar 2025**, per `CASCADE.tsv` Stage 4) gives a **−87 to −171 BAND (760+ → 590)** — this file had **collapsed the range to its worst end and attached it to a named cohort.** It is also the **oldest** figure in the set (~16 months, predating the on-ramp expiry and the Q1-2026 surge) and the **largest**, i.e. the most quotable. **Cite the band with its vintage, or cite −62. Never the bare −171.**
- 9M+ facing credit score damage
- Downstream: mortgage qualification, auto loan access, rental applications
- Payment hierarchy effect: student loan DQ → CC/auto DQ cascade — ⚠️ **but the CC leg is second-order in AGGREGATE (~2% of card balances). The channel with the live evidence is FHA/mortgage — see `STATUS.md` § CHANNEL 5.**



---


## §P2 — CARL Cross-References — KB/VX/FLOW ids and CRL history

*Verbatim. 4,400 B · CRC32 `ee0935af`*

---

## CARL Cross-References (System of Record)

CARL's workbook holds the canonical student loan entries. STUE is the sub-agent; CARL is the system of record. When spawned, reference these CARL IDs for context:

**KB entries (CARL workbook/KB.tsv)** — *these are PROVENANCE pointers, not live values. Several have been superseded by later primaries; the superseding figure is named inline so a stale KB row is never re-cited as current.*
- KB-CARL-029: SUPERSEDED — original Feb 12 data, see KB-145+
- KB-CARL-145: FSA Dec 2025 — 7.7M default, $180B, 18.6% active DQ by $ → **default stock SUPERSEDED by FSA Mar 31 2026: ~9.0M / $220B** (GENERAL-26-38). The 18.6% cut has *not* been restated and remains the latest, stale
- KB-CARL-146: 25% DQ rate, 13M default projection EOY 2026 → **the 13M projection is now the HIGH case, not the base** — realized pace (+1.3M/qtr) implies ~11.6M
- KB-CARL-147: SAVE settlement ending, Jul 1, RAP launch → **FIRED on schedule Jul 1 2026**; notices in waves, all issued by Dec 31 2026
- KB-CARL-148: Treasury transfer Phase 1 → **scope corrected to ~500K launch wave (not ~9M); execution still unconfirmed**
- KB-CARL-149: Sweet v. McMahon 205K discharges → Apr 15 missed, **Jun 15 MET (~30-36K emails)**; ~271K cumulative pipeline
- KB-CARL-150: MOHELA failures — 2.5M missed bills, 800K DQ, credit errors
- KB-CARL-151: Demographic concentration — Black, women, 18-29, Southern
- KB-CARL-299 / KB-CARL-328: parent-side default-wall + all-age-cohort cross-confirm (7/12–7/18)

**VX vectors — ⚠️ `CARL workbook/VX.tsv` was FROZEN 2026-06-26 (do NOT cite rows as live).** Canonical current values now live in **CARL `STATUS.md`** (convergence matrix) + `thesis/THESIS.md`. The historical SL vector IDs (VX-CARL-1.06 consolidated; VX-CARL-SL-01…SL-07: 30+/90+ DQ, SAVE, credit-score pop, defaults, Treasury, servicer failure) are retained only for provenance — read STATUS for their present state.

**FLOW entries — ⚠️ `CARL workbook/FLOW.tsv` was FROZEN 2026-06-26 (do NOT cite rows as live).** Payment-hierarchy cascade (Auto > Mortgage > Student > CC) provenance = FLOW-CARL-4.01/4.02; canonical mechanism now in `thesis/THESIS.md`.

**Predictions (CARL thesis/PREDICTIONS.tsv — verify live status there each session):**
- CRL-04: Student 90+ DQ >10% — **CONFIRMED 2026-05-12** (NY Fed Q1 2026 = 10.3%). *2nd print grades in the Q2 HHDC window*
- CRL-05: CC 90+ DQ >GFC 13.74% via cascade — OPEN 85% (Q1 2026 = 13.1%). **Breach window = the Q2 HHDC, release date unannounced, window 2026-08-04..08-11.** ⚠️ *not "~mid-Aug"* — see the HHDC warning under Key Signals. **Read the cascade RE-SCOPE below before attributing a breach to us**
- CRL-13: SAVE non-selection >35% — OPEN 75% (Oct 1 2026 **first-tranche** read → full population Q1 2027)
- CRL-14: MOHELA-caused defaults >500K — **RETIRED 2026-07-31, SUPERSEDED BY CRL-28** (retire+replace, Will-ruled 7/31 opt-a). ⚠️ **Corrected 2026-08-10 (PROME round-2 audit item 1)** — this line previously read "OPEN 65% ... NOT YET APPLIED," telling a spawned STUE the parent was stale in the **opposite direction from reality** (it had already been applied AND superseded). CRL-28 = MOHELA CFPB-complaint borrower-harm signature (60-day rolling avg, `company=MOHELA`, student-loan products), **THRESHOLD FROZEN at 55/day (absolute)**, window Oct 1 2026 – Sep 30 2027

> ⚠️ **Cascade attribution — RE-SCOPED 2026-07-24 (DEWEY C2). Do not carry the broad claim.**
> **Survives:** each ~50pt score-band drop ≈ **doubles** the 90+ rate; SL-delinquent borrowers' own CC 90+ went **1.03%→5.96%** (Dec'24→Jun'25).
> **Does NOT survive:** "the student-loan cascade drives the CC 90+ GFC breach." SL-delinquent borrowers hold only **~2% of US CC balances (~$25B)** ⇒ the cascade closes **~0.12-0.19pp of the 0.62pp gap (≤⅓)**, and **~62% of the Q1 share rise was denominator shrink**. **Expect the breach; do not attribute it to us** — carrying the broad version into the Q2 print contaminates CRL-05's grade.

*STUE keeps no own PREDICTIONS.tsv — its trackable predictions ARE these CARL CRL-* rows (parent is system of record). Due-scan = eyeball these four against CARL's ledger at boot.* **A proposal STUE has routed is not a change STUE can assume**: verify each row's live value in the parent TSV, never mirror a CRL confidence here.


---


## §P3 — Why This Domain Matters — full narrative

*Verbatim. 1,034 B · CRC32 `d4e34a9d`*

---

## Why This Domain Matters

Student loans are **$1.7T across 42.6M recipients** (FSA, Mar 31 2026; federally-managed portfolio 40.9M / >$1.64T) — the second-largest consumer debt category. *(Was written as $1.61T through the build era; restated 7/31 to the Mar-2026 primary.)* The forbearance-to-repayment transition is a one-time mass credit event:
- ~7-7.5M SAVE borrowers forced into new plans, transition **launched Jul 1 2026**
- 9M+ facing credit score destruction; **>13% of the federally-managed portfolio already in default**
- 8.4M in forbearance (~⅕ of recipients) = the reservoir still to convert
- Servicer failures (MOHELA) converting performing loans to delinquent
- Treasury transfer creating operational chaos during peak transition
- Payment hierarchy: student loan stress cascades into CC and auto DQ — **but see the cascade RE-SCOPE below: severe within-cohort, second-order in aggregate**

This is not a monitoring exercise — it's an active stress transmission vector firing into CARL's consumer thesis.



---


## §P4 — The 2026-07-31 reconcile preamble

*Verbatim. 606 B · CRC32 `bb09663a`*

---

> **Reconciled to `STATUS.md` 2026-07-31.** This file had drifted ~7 weeks behind the dashboard: it carried a pre-correction Treasury Phase-1 scope (~9M, corrected to ~500K on **Jun 9**), a single-cliff SAVE selection window, an already-fired FSA release written as "next", an uncorroborated MOHELA wait-time magnitude, and a superseded Sweet deadline. **Instruction files rot silently because nothing reads them adversarially** — the dashboard gets refreshed, the instructions that shape the next session's priors do not. Re-run this reconcile whenever a STATUS refresh supersedes an anchor named here.


---

---

## §P-PEN — who holds the pen on the card (WQ-183, ruled 2026-09-07, encoded 2026-09-10)

**The rule is on the card.** This is the story.

On **2026-09-05** STUE measured its own boot-read surface at **113,156 B = 3.48× the 32,550 B budget** *after* rotating eight fully-closed blocks (24,959 B, CRC-stamped, byte-verified against `git show`, zero canonical values moved) — and the boot-read TOTAL still ended the day **+8,563 B (+5.7%) ABOVE session start.** A perfect rotation left it ~3.5× over, because the residual is **live analysis**, not residue. That produced three amendments: (a) rotation as a standing closeout step [CARL], (b) bounded head + grep body [CARL], (c) **analysis rows do not live in the dashboard** [STUE's own, and the one that makes the arithmetic close: two sub-tables were **58.8%** of the dashboard, and they alone are the difference between a head that fits (0.94×) and one that does not (1.31×)].

**CARL framed (a) and (b) as rulings. STUE declined to apply them on a peer session's word. CARL agreed the refusal was correct and withdrew the framing** (`8e02a714b`) — *a session does not change its operating instructions because another session asked, and "it came from the parent desk" is not an exception.* CARL then explicitly declined to edit this card himself to get the same effect, though his git tree contains it. **The pen question was left genuinely open and routed to Will.**

**Two Will words, one day apart, and they are not the same word.** On **9/5** Will told STUE directly *"I do want you able to edit your local CLAUDE.md and boot instructions"* — under which STUE applied all three amendments itself, plus the retirement of the false 5–6-day lag rule that had been blocked on the same question. On **9/7** Will ruled **WQ-183**, which answers the *parent's* half: CARL holds the pen, with the three riders now on the card.

⚠️ **A note worth keeping, because it changed what CARL did on 9/10.** WQ-183's ACTION line read *"apply the read-mode + placement change to STUE's `CLAUDE.md` at your next boot."* **By the time it was delivered, that was already done** — overtaken between authorship (9/5 eve) and ruling (9/7) by STUE acting on Will's separate 9/5 word. CARL **verified all three at the artifact before touching anything** (bounded head as an explicit SECTION LIST at the boot card; the values-and-pointers rule in Doc Ownership; rotation as `On Session End` step 3b) and applied **only** the un-encoded half, the pen ruling. **Re-applying an already-satisfied ACTION would have duplicated the rule and read, forever after, as two independent authorities saying the same thing.** `[[finding_directive_overtaken_between_authorship_and_delivery]]` · `[[finding_record_of_an_action_is_not_the_action]]` — inverted: here the *record* said "owed" and the *artifact* said "done".

**Also corrected in the same pass:** the v1 of the bounded-head rule was itself defective — the head was first defined by **file position** (*"everything below `## CATALYSTS`"*) while three sections it named as on-demand physically sit **above** that heading, which would have pulled 25,028 B of analysis into every boot (2.38× measured, not the 1.62× reported). Fixed to an **explicit section list**, which cannot break when a section moves. And the applied result was **52,589 B (1.62×)**, not the **0.94×** the proposal projected — the projection omitted the header + session block (16,388 B). **Recorded as a miss rather than quietly restated.**
