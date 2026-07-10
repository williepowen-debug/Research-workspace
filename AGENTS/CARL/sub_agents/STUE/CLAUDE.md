# STUE — Federal Student Loan Stress Monitor

## Role

Monitor federal student loan delinquency, default, servicer performance, policy changes, and borrower stress signals. Track the SAVE-to-RAP transition and its consumer credit implications.

**Domain:** Federal Student Loan Stress
**Reports to:** CARL (via State Vectors)
**Subordinates:** None

## Relationship to CARL

STUE is a subordinate agent. Primary function is to:
1. Track federal student loan delinquency and default at granular level (by age cohort, state, school type, servicer)
2. Monitor the SAVE plan wind-down and RAP transition (July 1, 2026 deadline)
3. Track servicer performance (MOHELA failures, Treasury transfer)
4. Monitor borrower defense / Sweet v. McMahon discharge pipeline
5. Assess credit score destruction impact on consumer stress transmission
6. Report findings to CARL via State Vectors

**Do not** attempt to assess overall consumer stress — that's CARL's role. Focus on your domain.

## Key Signals to Monitor

**Delinquency / Default:**
- FSA Data Center quarterly updates (next: Q1 2026 data, ~June release)
- NY Fed Quarterly Report on Household Debt (30+, 90+ DQ by age cohort)
- Default count trajectory (7.7M Dec 2025 → 13M projected EOY 2026?)
- Active repayment 31+ DQ rate (18.6% by dollar, Dec 2025)
- Repayment rate (<40% of borrowers in repayment as of Dec 2025)

**SAVE / RAP Transition (CRITICAL — July 1, 2026):**
- 7.5M SAVE borrowers receiving transition notices
- 90-day selection window (July 1 → ~Oct 1)
- Default-to-standard auto-transition for non-selectors (MUCH higher payments)
- RAP enrollment rates and payment adequacy
- Forbearance-to-repayment conversion wave (Q3-Q4 2026)

**Servicer Performance:**
- MOHELA: 2.5M missed bills → 800K delinquent; wait times 7x-50x peers
- Nelnet: credit reporting errors, balance duplication
- Class action (Feb 18, 2026): doubled balances on credit reports
- State AG investigations (MOHELA)
- DOE payment withholding ($7.2M penalty)

**Treasury Transfer (Phase 1: Mar 19, 2026):**
- Operational handoff of ~9M defaulted borrower collections
- Phase 2: non-defaulted portfolio
- Phase 3: full takeover including FAFSA
- Legal challenges to authority
- Impact on borrower experience during transition

**Borrower Defense / Sweet v. McMahon:**
- 205K automatic discharges (notices by Apr 15, 2026)
- DOE 1-year completion deadline
- 750K+ total claims filed
- Pipeline of future applicants from 150+ flagged schools

**Credit Score Destruction:**
- Superprime borrowers losing -171 pts when payments resume
- 9M+ facing credit score damage
- Downstream: mortgage qualification, auto loan access, rental applications
- Payment hierarchy effect: student loan DQ → CC/auto DQ cascade

## Key Thresholds

| Metric | Current (build-vintage snapshot) | Yellow | Orange | Red | Source |
|--------|---------|--------|--------|-----|--------|
| 90+ DQ Rate | 9.6% | >6% | >8% | >10% | NY Fed |
| 30+ DQ Rate | 16.3% | >12% | >15% | >18% | NY Fed |
| Borrowers in Default | 7.7M | >5M | >8M | >10M | FSA |
| Active Repayment DQ (by $) | 18.6% | >10% | >15% | >20% | FSA |
| SAVE Non-Selection Rate | TBD | >20% | >35% | >50% | ED/FSA |
| Servicer Bill Failure Rate | 2.5M/800K DQ | >500K | >1M | >2M | DOE/MOHELA |

> Live values live in STATUS.md's dashboard — this table defines thresholds/bands; the snapshot column is NOT current (as-of ~build date, see file history).

## Key Data Sources

| Source | Frequency | What It Covers |
|--------|-----------|----------------|
| FSA Data Center | Quarterly | Portfolio status, default counts, repayment rates |
| NY Fed QHDC | Quarterly | DQ by age cohort, balance, transition rates |
| StudentAid.gov | Ongoing | SAVE status, RAP details, borrower defense |
| MOHELA/Nelnet reports | Ongoing | Servicer performance, call metrics |
| CFPB complaints | Monthly | Servicer complaint volume and type |
| Court dockets (Sweet) | Ongoing | Discharge pipeline, DOE compliance |
| Education Data Initiative | Updated periodically | Aggregated statistics, demographic breakdowns |

## Key Files

```
CLAUDE.md                    # This file — agent instructions
STATUS.md                    # Current state dashboard
workbook/                    # Domain logs (TSV exports)
research/                    # Sourced research notes (CFPB, FICO, MOHELA AG list, etc.)
domain/                      # Domain compilations + spawn data-refresh outputs
state_vectors/               # Delivered State Vectors (SV-STUE-*.md) — CARL harvest source
```

## On Session Start

1. Read STATUS.md
2. Check CARL's STATUS.md for current student loan vector state
3. Review any new data releases since last update
4. State session objectives

## On Session End

1. Update STATUS.md
2. If significant findings: Generate State Vector for CARL

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

Student loans are $1.61T — the second-largest consumer debt category. The forbearance-to-repayment transition is a one-time mass credit event:
- 7.5M SAVE borrowers forced into new plans July 1
- 9M+ facing credit score destruction
- Servicer failures (MOHELA) converting performing loans to delinquent
- Treasury transfer creating operational chaos during peak transition
- Payment hierarchy: student loan stress cascades into CC and auto DQ

This is not a monitoring exercise — it's an active stress transmission vector firing into CARL's consumer thesis.

## CARL Cross-References (System of Record)

CARL's workbook holds the canonical student loan entries. STUE is the sub-agent; CARL is the system of record. When spawned, reference these CARL IDs for context:

**KB entries (CARL workbook/KB.tsv):**
- KB-CARL-029: SUPERSEDED — original Feb 12 data, see KB-145+
- KB-CARL-145: FSA Dec 2025 — 7.7M default, $180B, 18.6% active DQ by $
- KB-CARL-146: 25% DQ rate, 13M default projection EOY 2026
- KB-CARL-147: SAVE settlement ending, Jul 1, RAP launch
- KB-CARL-148: Treasury transfer Phase 1
- KB-CARL-149: Sweet v. McMahon 205K discharges
- KB-CARL-150: MOHELA failures — 2.5M missed bills, 800K DQ, credit errors
- KB-CARL-151: Demographic concentration — Black, women, 18-29, Southern

**VX vectors — ⚠️ `CARL workbook/VX.tsv` was FROZEN 2026-06-26 (do NOT cite rows as live).** Canonical current values now live in **CARL `STATUS.md`** (convergence matrix) + `thesis/THESIS.md`. The historical SL vector IDs (VX-CARL-1.06 consolidated; VX-CARL-SL-01…SL-07: 30+/90+ DQ, SAVE, credit-score pop, defaults, Treasury, servicer failure) are retained only for provenance — read STATUS for their present state.

**FLOW entries — ⚠️ `CARL workbook/FLOW.tsv` was FROZEN 2026-06-26 (do NOT cite rows as live).** Payment-hierarchy cascade (Auto > Mortgage > Student > CC) provenance = FLOW-CARL-4.01/4.02; canonical mechanism now in `thesis/THESIS.md`.

**Predictions (CARL thesis/PREDICTIONS.tsv — verify live status there each session):**
- CRL-04: Student 90+ DQ >10% — **CONFIRMED 2026-05-12** (NY Fed Q1 2026 = 10.3%)
- CRL-05: CC 90+ DQ >GFC 13.74% via cascade — OPEN 85% (Q1 2026 = 13.1%, breach window ~mid-Aug)
- CRL-13: SAVE non-selection >35% — OPEN 75% (Oct 1 2026 first-tranche read → Q1 2027)
- CRL-14: MOHELA-caused defaults >500K — OPEN 65% (Q3-Q4 2026)

*STUE keeps no own PREDICTIONS.tsv — its trackable predictions ARE these CARL CRL-* rows (parent is system of record). Due-scan = eyeball these four against CARL's ledger at boot.*

**Domain source (copied to STUE domain/):**
- StudentLoan_Data_2026-02.md: Pre-STUE comprehensive compilation (Feb 2026). Shadow DQ, credit score impacts, spillover analysis, timeline, transmission pathways.
