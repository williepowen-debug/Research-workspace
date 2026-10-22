---
request_id: REQ-DEWEY-20261022-003
from: WALTER (discovery under Will's standing direction in the WALTER terminal, 2026-10-22 12:01 ET: "discovering valuable/significant research tasks/threads and assigning them to DEWEY")
to: DEWEY
created: 2026-10-22 (UTC stamp in the commit)
state: NEW
flag_trigger: T4 thesis pivot (whether a cross-bank Q3 pattern is a lead indicator for Will's bank view) + T3 load-bearing but thin (the pattern is six banks, one quarter, no base rate)
originating_evidence: SIG-W-20261022-012 (REGINALD's Q3 caveat for Will, 10/22: problem loans rose at 6 of 6 banks read, SSB VLY HBAN EGBN BKU ZION; reserve coverage of problem loans fell at 5 of 5 computed, e.g. EGBN 109% to 73%, VLY about 131% to 117%; banks cite collateral; "descriptive, not evidence of misstatement") + SIG-W-20261022-011 (HBAN and VLY allowance ratios fell as bad loans rose)
clusters: BANK_COLLATERAL
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261022-003
kill_condition: At intake, grep AGENTS/REGINALD and AGENTS/GIBBS for an existing historical study of coverage-ratio declines (search "coverage", "ACL/NPL", "allowance to nonperforming"). If one exists and covers at least two downturns, stop and report its location to WALTER. Also stop if the FDIC/FFIEC history needed for leg 2 cannot be retrieved, and say so.
deliver_by: no hard date; useful before the Q3 10-Qs (about 11/10) and well before Q4 prints (mid-January 2027)
---

# DEEP-RESEARCH REQUEST — When regional banks' bad loans rise while reserve coverage falls, how often do losses follow?

**Why now:** in the Q3 prints read so far, problem loans rose at every regional bank REGINALD checked and reserve coverage of those loans fell at every one it computed. The banks say collateral covers the gap. REGINALD reports this as a pattern only. Nobody in the fleet knows whether this pattern has historically come before rising charge-offs, or whether banks that said "collateral covers it" were usually right.

**Decision question:** in past US bank credit cycles, when a broad group of regional banks reported rising nonperforming loans together with falling reserve coverage (allowance divided by nonperforming loans) in the same quarter, (a) how often did net charge-offs and provisions rise materially over the next 2 to 4 quarters, (b) by how much, and (c) did the banks whose coverage fell most take the largest later losses?

**What changes with the answer:** if the pattern reliably led losses, REGINALD has grounds to propose a registered cross-bank indicator before the Q4 prints, and the 6-of-6 reading becomes evidence for Will's bank view. If it usually did not (collateral held), the pattern should not move Will's view, and the fleet stops citing it as a warning. Either answer is decision-useful.

## Scope (in bounds)

1. **Episodes.** At minimum: 1990–91 (New England CRE), 2007–10, 2015–16 (energy loans), 2020, and 2023–25 (office CRE). For each, identify the quarter(s) when the regional-bank aggregate showed rising NPLs with falling coverage.
2. **Aggregate base rate.** From FDIC Quarterly Banking Profile history and FRED bank-size series (for example charge-off and delinquency rates for banks outside the 100 largest), measure what followed over 1, 2, 4 and 8 quarters: net charge-off rate, provision expense, and allowance build. Report the hit rate with the count of episodes. Small n must be stated, not hidden.
3. **Cross-section.** Using call report data (FFIEC; allowance, nonaccrual and 90+ day past due, net charge-offs), test within one or two episodes whether banks with the largest coverage declines had larger subsequent charge-offs. Control crudely for loan mix (CRE share) if feasible.
4. **The collateral defense.** Find evidence on loss-given-default for CRE and construction loans in those episodes, and on how often banks' "well-secured" calls held. Note appraisal lag.
5. **Today's group placed in history.** Put the six Q3-2026 banks' coverage levels (from SIG-W-20261022-012 and REGINALD's report) against the historical distribution: is 73% coverage low, normal or high relative to past pre-loss quarters?
6. **Counter-evidence, required.** Periods when coverage fell because banks charged off reserved loans (coverage falls mechanically and is a good sign), and the CECL change in 2020 that altered how reserves relate to nonperforming loans. Say how CECL limits comparison with pre-2020 data.

## Out of bounds

Grading REGINALD's thesis or any bank's rank; stock calls or position sizing (TERRY); registering a threshold (REGINALD proposes, Will decides).

## Deliverable

Tables over prose, every cell sourced and dated: (1) episode table with the trigger quarter and outcomes at 1/2/4/8 quarters; (2) hit rate with n; (3) cross-section result for at least one episode; (4) today's six banks against the historical range; (5) counter-evidence and the CECL break; (6) explicit UNKNOWNs.

**On return:** archive to AGENTS/DEWEY/output/, then hand back via a create-only handoff in AGENTS/WALTER/inbox/DEWEY/ naming REQ-DEWEY-20261022-003. WALTER routes it as a research-output signal: REGINALD action; GIBBS, CREED, WAL, OZK, FLG, RED and PROME info.
