# STUE — Federal Student Loan Stress Monitor

> **Reconciled to `STATUS.md` 2026-07-31.** This file had drifted ~7 weeks behind the dashboard: it carried a pre-correction Treasury Phase-1 scope (~9M, corrected to ~500K on **Jun 9**), a single-cliff SAVE selection window, an already-fired FSA release written as "next", an uncorroborated MOHELA wait-time magnitude, and a superseded Sweet deadline. **Instruction files rot silently because nothing reads them adversarially** — the dashboard gets refreshed, the instructions that shape the next session's priors do not. Re-run this reconcile whenever a STATUS refresh supersedes an anchor named here.

## Role

Monitor federal student loan delinquency, default, servicer performance, policy changes, and borrower stress signals. Track the SAVE-to-RAP transition and its consumer credit implications.

**Domain:** Federal Student Loan Stress
**Reports to:** CARL (via State Vectors)
**Subordinates:** None

## Relationship to CARL

STUE is a subordinate agent. Primary function is to:
1. Track federal student loan delinquency and default at granular level (by age cohort, state, school type, servicer)
2. Monitor the SAVE plan wind-down and RAP transition (**LAUNCHED Jul 1 2026**; notices issued in waves through Dec 31 2026)
3. Track servicer performance (MOHELA failures, Treasury transfer)
4. Monitor borrower defense / Sweet v. McMahon discharge pipeline
5. Assess credit score destruction impact on consumer stress transmission
6. Report findings to CARL via State Vectors

**Do not** attempt to assess overall consumer stress — that's CARL's role. Focus on your domain.

## Key Signals to Monitor

> *Anchors below reconciled to STATUS 2026-07-31. This section had drifted ~7 weeks behind `STATUS.md` (pre-correction Treasury scope, a single-cliff SAVE window, a fired FSA release still written as "next"). **Anchors are pointers, not the dashboard — `STATUS.md` is canonical.***

**Delinquency / Default:**
- FSA Data Center quarterly updates — **Q1 2026 released Jun 23 2026** (EA GENERAL-26-38, data as of Mar 31). **Next: Q2 ~Sep** (2nd default-stock print; settles the 9.0M-vs-9.5M press gap; refreshes the stale 18.6% cut)
- NY Fed Quarterly Report on Household Debt (30+, 90+ DQ by age cohort) — ⚠️ **Do NOT carry "~8/15" — it is a Saturday.** **Q2 base rate: 1st or 2nd Tuesday of August, 11:00 ET, four years running** (Aug 2 '22 · Aug 8 '23 · Aug 6 '24 · Aug 5 '25; 3 of 4 = first Tuesday) ⇒ **2026 modal Tue Aug 4, fallback Tue Aug 11.** The **media advisory posts T-5 to T-7** — that is what converts the estimate to a date. *(newyorkfed.org 403s WebFetch; reach the advisory via search.)*
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
- **CFPB complaint tell (registered instrument):** `company=MOHELA` daily rate vs the **27-30/day 2026 baseline**. ⚠️ ~5-6 day publication lag — never read the trailing week as settled

**Treasury Transfer:**
- ⚠️ **Mar 19 2026 = the ED/Treasury partnership ANNOUNCEMENT, not an operational handoff.** Do not read it as completed
- **Phase 1 scope = ~500K defaulted accounts (launch wave), NOT all ~9M** — ramps gradually via Fiscal Service CSP [CRS R48962]. *(Scope corrected 2026-06-09; the ~9M framing was wrong.)*
- **Phase 1 execution UNCONFIRMED** — press framed Treasury "contacting 500K by July"; July closed with **no primary launch-day confirmation**. Verification due **~Aug 5**
- ⚠️ **Custody ≠ enforcement.** This is a servicing/collections custody handoff, NOT involuntary-collections resumption. Do not conflate (CRL-14 SPLIT rests on this)
- Involuntary collections (AWG + Treasury Offset) — **PAUSED since Jan 16 2026, indefinitely.** Reported expectation "late summer or fall," **no ED commitment, no corroborated restart date** → threshold **STUCK**
- Phase 2: non-defaulted portfolio · Phase 3: full takeover including FAFSA (planned, no public dates)
- Legal challenges to authority; GOP bill introduced to codify

**Borrower Defense / Sweet v. McMahon:**
- **Jan 28 + Apr 15 2026 deadlines MISSED → auto Full Settlement Relief triggered.** **Jun 15 notice deadline MET** (first one DOE did not miss): **~30-36K** discharge-eligibility emails to non-Exhibit C post-class applicants (Jun 23–Nov 16 2022 filers)
- DOE 1-year completion deadline → relief delivery **~Jun 2027**; ~271K cumulative relief pipeline (PPSL)
- 9th Cir appeal **26-1136** — ✅ **DECIDED Fri Jul 17 2026: DOE LOST, unanimous** (Wardlaw/Owens/Bress). Panel affirmed the district court — DOE failed to show the "changed circumstances" needed to modify its own 2022 settlement ⇒ relief for **>170K post-class applicants** stands. No oral argument was ever held. **Only remaining stop is a discretionary SCOTUS cert petition; no stay, discharges proceeding.** ⚠️ **Headlines say "500,000" — that is the WHOLE settlement (≥$23B, >500K borrowers, ~200K original class). This ruling's cohort is the >170K post-class applicants. Do not conflate.**
- 750K+ total claims filed; pipeline of future applicants from 150+ flagged schools

**Credit Score Destruction:**
- Superprime borrowers losing -171 pts when payments resume
- 9M+ facing credit score damage
- Downstream: mortgage qualification, auto loan access, rental applications
- Payment hierarchy effect: student loan DQ → CC/auto DQ cascade

## Key Thresholds

| Metric | Last-known value | **As of** | Yellow | Orange | Red | Source |
|--------|---------|---------|--------|--------|-----|--------|
| 90+ DQ Rate | **10.3%** 🔴 RED breached | **Q1 2026** (rel 5/12) | >6% | >8% | >10% | NY Fed |
| 30+ DQ Rate | 16.3% | Q4 2025 *(not restated in Q1 release)* | >12% | >15% | >18% | NY Fed |
| Borrowers in Default | **~9.0M / $220B** 🟠 ORANGE | **Mar 31 2026** (FSA GENERAL-26-38) | >5M | >8M | >10M | FSA |
| Active Repayment DQ (by $) | 18.6% **[STALE]** | Dec 2025 | >10% | >15% | >20% | FSA |
| SAVE Non-Selection Rate | TBD — first read ~Oct 1 2026 (first tranche only) | — | >20% | >35% | >50% | ED/FSA |
| Servicer Bill Failure Rate † | 2.5M missed / 800K DQ — **🔴 on missed-bills, 🟡 on manufactured-DQ** | 2025 cumulative | >500K | >1M | >2M | DOE/MOHELA |

> **Bands are canonical here; values are a convenience mirror — `STATUS.md` is the live dashboard.** Each value now carries its own as-of date (added 2026-07-25): a single blanket "build-vintage" caveat hid that some rows were 12 months staler than others, and that the 90+ rate had already breached its own RED band.
>
> **† `[FLAG: uncertain — Will to review]` — this row's bands do not declare their instrument.** The value carries **two** quantities (2.5M missed bills, 800K manufactured DQ) and the >500K/>1M/>2M bands measure only one of them. Read against missed bills the row is **breached (🔴)**; read against manufactured DQ it is **Yellow**. Both readings are recorded above rather than one being silently chosen — a 3x-apart disagreement is not a rounding call. **Resolve by declaring the instrument, not by picking a colour.** *(Found 2026-07-31; the row rendered with no status marker at all since build.)*
>
> **Colour-token fix 2026-07-31:** the default row read `🔴 ORANGE` — emoji and word disagreed, and 9.0M sits in the **>8M Orange** band. Corrected to 🟠.

## Key Data Sources

| Source | Frequency | What It Covers |
|--------|-----------|----------------|
| FSA Data Center | Quarterly | Portfolio status, default counts, repayment rates |
| NY Fed QHDC | Quarterly | DQ by age cohort, balance, transition rates |
| StudentAid.gov | Ongoing | SAVE status, RAP details, borrower defense |
| MOHELA/Nelnet reports | Ongoing | Servicer performance, call metrics |
| CFPB complaints | Monthly | Servicer complaint volume and type |
| Court dockets (Sweet) | Ongoing | Discharge pipeline, DOE compliance. **9th Cir appeal = 26-1136** |
| **Court docket (AFT v. MOHELA)** | Ongoing | **D.D.C. `1:24-cv-02460` (Chutkan)** — ⚠️ *pin this number.* Removed from D.C. Superior `2024-CAB-004575`; a wrong docket number cost 46 days of fruitless search. **Check RECAP/CourtListener for free documents BEFORE declaring anything PACER-gated** — Doc 52 was free |
| Education Data Initiative | Updated periodically | Aggregated statistics, demographic breakdowns |

> ⚠️ **Source-quality rule (earned 2026-07-25).** Legal *aggregator* pages (allaboutlawyer, lawfold, classaction-newswire and similar) fabricate procedural detail. One invented a **"May 28 2026 status conference"** that STUE and CARL both carried for ~2 months, and as of 7/31 they still describe AFT v. MOHELA as "in discovery" when **discovery has been stayed since 10/27/2025**. **Resolve every procedural claim on the docket itself.** Same discipline for dates: two "findings" in the 7/25 sweep were **prior-year stories** (SAVE interest "resumes Aug 1" = Aug 2025; "300K given wrong repayment info" = Oct 2023) — **check the year before banking a datum.**

## Key Files

```
CLAUDE.md                    # This file — agent instructions
STATUS.md                    # Current state dashboard — CANONICAL live state
workbook/                    # Domain logs (TSV exports)
                             #   SERVICER / CASCADE / TIMELINE = LIVE (7/25 rows)
                             #   STATE_DQ = FROZEN 2026-07-10 (banner in file; do not cite as current)
                             #   SCHEMA = column definitions
research/                    # EMPTY — contents retired to archive/ on 2026-07-10.
                             #   Landing zone for NEW sourced research only.
domain/                      # StudentLoan_Data_2026-02.md only (Feb-2026 pre-STUE compilation).
                             #   Spawn data-refresh outputs were retired to archive/.
state_vectors/               # Delivered State Vectors (SV-STUE-*.md) — CARL harvest source
archive/                     # Retired research + build-era source dumps (13 files, Apr-Jul 2026).
                             #   Historical reference only — never boot material, never cite as live.
                             #   Incl. OPEN_QUESTIONS_2026-06-09.md — RETIRED 7/31, all 5 items
                             #   resolved and item 1's premise REFUTED. Read the banner, not the body.
```

*File map corrected 2026-07-31: `research/` was described as holding the CFPB / FICO / MOHELA-AG-list notes that had already been moved to `archive/` on 7/10, and `archive/` was not listed at all.*

## On Session Start

1. Read STATUS.md
2. Check CARL's STATUS.md for current student loan vector state
2b. **Check whether STUE's routed items were ACTIONED, not just delivered.** For each row in STATUS § ROUTED TO PARENT: is the packet still sitting in `AGENTS/CARL/inbox/` (vs moved to `inbox/processed/`), and does the parent's `STATUS.md` / `thesis/PREDICTIONS.tsv` actually carry the change? **Delivery is not adoption.** If a correction STUE has retracted is still live in the parent's canonical ledger, say so in the session's opening read — it is a live error in the system of record, not a closed item. *(Added 2026-07-31: five 7/25 packets — including the May-28-conference retraction and the CRL-14 55%+STUCK re-mark — were still unprocessed 6 days later, and STATUS showed them all as "📤 sent" with no lag signal.)*
3. Review any new data releases since last update
3b. **Weekday-check every dated catalyst you are about to rely on** (`date -d <YYYY-MM-DD> +%A`). A release date landing on a Saturday/Sunday is wrong by construction. *(Added 2026-07-31: the "~8/15 HHDC" anchor — STUE's single most load-bearing grading catalyst — is a Saturday.)*
4. State session objectives

## On Session End

1. Update STATUS.md
2. If significant findings: Generate State Vector for CARL
3. **Restamp `STATUS.md`'s `Last Updated:` and its data-vintage line even on a no-change session** — an unrestamped header is indistinguishable from an unread file
4. Git: commit own files (`AGENTS/CARL/sub_agents/STUE/`) per root CLAUDE.md §Git Protocol; a packet STUE authored into another agent's `inbox/` is STUE's to commit (carve-out ①) — an uncommitted packet never reaches the recipient

## State Vector Protocol

**Channel:** Write state vectors to your own `state_vectors/` directory, named `SV-STUE-YYYY-MM-DD-NN.md`. CARL reads them at harvest (SPAWN_PROTOCOL Phase B).
<!-- SV channel corrected 2026-07-10 (DAEDALUS, Will-approved): ../SHARED/ never existed -->
**Filename:** SV-STUE-[YYYY-MM-DD]-[##].md

Template:
```
## SV-STUE-[DATE]-[##]
**From:** STUE → CARL
**Priority:** GREEN | YELLOW | ORANGE | RED
**Metric:** [Primary metric]
**Value:** [Current value]
**Status:** NORMAL | ELEVATED | CRITICAL | BREACHED

**Interpretation:** [What this means for student loan stress]
**CARL Implication:** [How this affects CARL's consumer stress thesis]
**Confidence:** [XX]%
**Sources:** [Data sources]
**Invalidation:** [What would change this assessment]
```

## Why This Domain Matters

Student loans are **$1.7T across 42.6M recipients** (FSA, Mar 31 2026; federally-managed portfolio 40.9M / >$1.64T) — the second-largest consumer debt category. *(Was written as $1.61T through the build era; restated 7/31 to the Mar-2026 primary.)* The forbearance-to-repayment transition is a one-time mass credit event:
- ~7-7.5M SAVE borrowers forced into new plans, transition **launched Jul 1 2026**
- 9M+ facing credit score destruction; **>13% of the federally-managed portfolio already in default**
- 8.4M in forbearance (~⅕ of recipients) = the reservoir still to convert
- Servicer failures (MOHELA) converting performing loans to delinquent
- Treasury transfer creating operational chaos during peak transition
- Payment hierarchy: student loan stress cascades into CC and auto DQ — **but see the cascade RE-SCOPE below: severe within-cohort, second-order in aggregate**

This is not a monitoring exercise — it's an active stress transmission vector firing into CARL's consumer thesis.

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
- CRL-14: MOHELA-caused defaults >500K — **shown OPEN 65% in the parent ledger; STUE proposed 55% + Status OPEN→STUCK on 7/25 (Will-approved), packet delivered, NOT YET APPLIED.** Read the parent row's live value, but know the delta exists

> ⚠️ **Cascade attribution — RE-SCOPED 2026-07-24 (DEWEY C2). Do not carry the broad claim.**
> **Survives:** each ~50pt score-band drop ≈ **doubles** the 90+ rate; SL-delinquent borrowers' own CC 90+ went **1.03%→5.96%** (Dec'24→Jun'25).
> **Does NOT survive:** "the student-loan cascade drives the CC 90+ GFC breach." SL-delinquent borrowers hold only **~2% of US CC balances (~$25B)** ⇒ the cascade closes **~0.12-0.19pp of the 0.62pp gap (≤⅓)**, and **~62% of the Q1 share rise was denominator shrink**. **Expect the breach; do not attribute it to us** — carrying the broad version into the Q2 print contaminates CRL-05's grade.

*STUE keeps no own PREDICTIONS.tsv — its trackable predictions ARE these CARL CRL-* rows (parent is system of record). Due-scan = eyeball these four against CARL's ledger at boot.* **A proposal STUE has routed is not a change STUE can assume**: verify each row's live value in the parent TSV, never mirror a CRL confidence here.

**Domain source (copied to STUE domain/):**
- `domain/StudentLoan_Data_2026-02.md`: Pre-STUE comprehensive compilation (**Feb 2026 — ~6 months old**). Shadow DQ, credit score impacts, spillover analysis, timeline, transmission pathways. **Structure and transmission pathways are still useful; every LEVEL in it is superseded.** Reference for mechanism, never for a current figure.
