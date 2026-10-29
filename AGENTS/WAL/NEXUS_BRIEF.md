# WAL — NEXUS Brief

**As of:** October 28 2026 22:50 ET. **STATUS commit `66c884cf7814a6d3276de3555e5c26cd550a6635`**. Will-interactive session (Claude Opus 5.5, laptop): catch-up and data refresh — no 10-Q yet, Q3 Call Report not yet filed, KB expiry review, short interest, EDGAR sweep, First Eagle NDFI joinder, inbox drain. *Prior pin:* October 22 12:31 ET, STATUS `1d4d4210a`.
**Status:** nothing graded since 10/22. Q3 print (10/19) and call (10/20) are graded on the frozen frames; the Q3 10-Q is **still not on EDGAR** (10/28 ~22:40 ET; statutory Mon 11/9) and is the single carrier for what remains open. Live price → `STATUS.md` (10/28 close $75.96 = EV).
**Thesis:** v2.4 (dated 2026-08-20); Bear-fast 2% / Bear-medium 16% / Base 45% / Bull 30% / Tail 7%; **EV $75.96 / PT $52–76**; composite 13/25 (V1a 1, V1b-broadening 2, V1b-magnitude 4, V3 3, V4 3; V2 5/5 historical, excluded). **Unchanged.** The re-score is owed right after the 10-Q grade.
**Domain:** issuer evidence and frozen grading. Funding/cohort/severity and the price guards are REGINALD's; structure and position management are TERRY's and Will's.

## What Q3 showed (8-K acc 0001628280-26-066286; call B2)

| Item | Q3 result | Read |
|---|---|---|
| WAL-02 (ex-fraud NCO > 40bps) | NCO $45.8M = **30bps** ⇒ **INVALIDATED** (10-Q confirm pending) | Against the bear |
| WAL-01 (Office classified > $500M) | **$272.75M** (25% × $1,091M, slide 13) ⇒ **INVALIDATED, provisional** (10-Q cross-check: classified loans ~$926M + OREO $165M expected) | Against the bear |
| Office migrations | 0 identified ⇒ **DP2 of 3 DISCONFIRM, final**; RETIRE broadening counter 2 of 3 | Against the bear |
| $99M life-science appraisal | Not mentioned in the release, deck or call ⇒ **PENDING-10-Q**, never benign | Gates the Bear-medium kill (leg b) |
| Reserves | ACL $574.4M = **118% of nonaccrual** (Q2 96%); RETIRE coverage leg MET | Against the bear |
| Problem-loan mix | Nonaccrual $562M → $485M, but OREO $126M → $165M and special mention $316M → $397M | The live residual |
| Earnings | EPS $2.45 vs $2.36; NIM 3.57% (+4bp); NII guide cut 12–14% → 11–12%; fees guide up; consistent-basis profit ~flat | Mixed; slight drag on the bull's NII leg |
| Capital | AOCI −$786M; TBV $62.22 (from $63.24); parent CET1 10.9% preliminary; buyback $92.1M | Mixed |
| Tape | 10/20 WAL +2.27% vs KRE +1.96% ⇒ non-credit falsifier NOT TRIGGERED | Neutral |

**Judgment:** Q3 runs against the credit bear and slightly against the bull's NII engine. What remains of the bear rests on the $99M appraisal and the OREO/special-mention build. No re-mark until the 10-Q, because the Bear-medium kill needs both of its legs and only one is in. **Pre-registered 10/22:** a cure moves Bear-medium 16 → 8 (kill fires); still non-paying or unmentioned 16 → 12; a partial write-down holds 16; a majority loss 16 → 20.

## Since the print (through 10/28)

- **NDFI (new 10/28):** First Eagle Private Credit Fund SPV amendment dated 10/1 (8-K 10/5): Western Alliance Bank joins as a lender with a **$100M commitment** — the second private-credit SPV joinder in two weeks after Crestline 9/18. A commitment, not a funded balance; exposure direction, not stress; V3 stays 3/5 until the 10-Q NDFI table (KB-260).
- **Q3 Call Report (MI3, bank NDFI):** not filed as of 10/28 (RSSD absent from FFIEC's 2,643-filer list); due Fri 10/30; FFIEC token expires Thu 11/5.
- **Insiders / ownership:** 9/24 → 10/28 no Form 144, 13D/G or open-market trade; 10/19 Form 4s routine RSU settlements (KB-252/259).
- **Short interest:** FINRA 10/15 settlement 6.35M shares, +2.15%, third straight rise; days-to-cover 4.68 (KB-258). Dated observation, no score read.
- **Cantor courts:** remand + stay relief GRANTED 8/24; WAL §523 suit vs the Stupins, **hearing Wed 12/9**. Procedural, no recovery → `research/2026-10-22_court-checks.md`.
- **Jefferies:** FQ3 10-Q never mentions WAL; NY index numbers still unknown.
- **Sell-side:** Stephens PT $94 → $88 on the NII guide (B2, single source, KB-253).

## Next carriers

1. **Q3 10-Q** — frozen frame verbatim ($99M §4 first after subsequent events; WAL-01/02; full NPL; OREO; NDFI 25.9%; Cantor; hotel), then the post-Q3 re-score.
2. **Q3 Call Report / MI3** — retry from Sat 10/31, before the JWT expires Thu 11/5; REGINALD cohort screen due 11/7.
3. **12/9** WAL §523 hearing; **11/30** Makhijani status conference (unverified; CourtListener now refuses anonymous access).

## Delivery

Desk commit `27ee3ed4a` (KB 260 rows / 20 groups; 9 expired rows judged; STATUS/MEMORY/INDEX; inbox drained) + stamp fix `66c884cf7`. PROME packet: `PROME/inbox/2026-10-28_from-WAL_catchup-data-refresh.md` (`e03d97e7b`, stamp fix `54071b1bc`). Exact-path commits, pushed through `scripts/safe-push.sh`. This brief is the session's last write, committed after its STATUS pin.
