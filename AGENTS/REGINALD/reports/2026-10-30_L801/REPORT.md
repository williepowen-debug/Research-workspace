# DOCKET L801 — the Q3 cohort pattern re-read against DEWEY's base rate

**Written:** 2026-10-30T09:14:16-04:00 (from `date`). **Desk:** REGINALD, PROME-spawned (WQ-184 Tier 1, due row). **Row:** `PROME/DOCKET.tsv` line 801 (PROME-owned; this file is REGINALD's decision record, the row itself is not edited here).
**Inputs:** DEWEY `AGENTS/DEWEY/output/2026-10-22_reserve-coverage-decline-base-rate.md` (REQ-DEWEY-20261022-003) · REGINALD cohort reads `reports/2026-10-22_catchup/REPORT.md` §1d and `reports/2026-10-23_boot/REPORT.md` §2e · FLG desk `AGENTS/FLG/NEXUS_BRIEF.md` (pinned 10/28, commit a12f81587) · `BANK_EXPOSURE_MATRIX.md` §1 channel 2 · `reports/2026-10-23_ranking-test_FROZEN_protocol.md` (sha256 `06e37edad2d583074a20f0ca70d0f84079a3eed95fba891204060662bcd00672`, re-verified 10/30).

## 1. Decision (REGINALD's letter)

| Leg of the Q3 cohort pattern (my answer to SIG-W-20261022-005) | Decision | Base rate written beside it |
|---|---|---|
| **Problem loans rising** (nonaccrual / NPL / criticized up quarter on quarter) | **KEEP** as the leg that carries predictive weight. Current count **7 of 10 read names** [10/23], not the 6 of 6 the row quotes [10/22]: AMTB, CUBI and First Citizens (secondary) moved the other way. | 2007–10 cross-section, n = 373 banks ≥$1B: rise in problem-loan ratio vs later 8-quarter charge-offs **ρ = +0.464, p < 0.0001** (DEWEY Table 3a). |
| **Reserve coverage falling** (allowance ÷ problem loans down) | **DROP as a predictor** (weight zero). Kept only as a descriptive line and a question about specific loans (§3). Never cited without the base rate in the next column. | Joint pattern (problem loans up AND coverage down, year on year, $10–100B band, 1984–2026): charge-off jump ≥25bp within 4 quarters in **2 of 10 episodes vs 41 of 166 quarters (25%) unconditional**, so no lift at 2–4 quarters. Cross-section 2007–10: coverage change vs later charge-offs **ρ = −0.064, p ≈ 0.21**; adding it after the problem-loan rise moves R² **0.088 → 0.094** (t = −1.35); in the failure model a bigger decline went with *lower* failure risk (t = +3.31). |

**Why drop rather than re-weight.** A re-weight needs a positive weight the data support, and DEWEY's data give none at the horizon the row asks about: the joint pattern hit 20% against a 25% base. The only lift is at 8 quarters (5 of 10 vs 36% for charge-offs; 7 of 10 vs 49% for provisions), every hit is pre-2020, the post-2020 sample has nothing to predict (0 of 22 unconditional), and in the cross-section that lift belongs to the problem-loan half: once the problem-loan rise is in the model, coverage change adds nothing or carries the wrong sign. A weight of zero is a drop. The row offered either; I take the drop.

**Caveats that travel with the decision (DEWEY's, kept in substance):** about 3 real loss cycles; one episode moves a rate by 8–10 points; episodes overlap and no significance test is reported. The current episode has been on since 2024Q1 with band charge-offs flat (0.35% → 0.36%) and is unresolved. CECL (2020) lifts every post-2020 coverage level, so today's coverage looks safer against old history than it is. "Collateral covers it" has a poor record at failed banks (construction loans lost ~53% weighted, 2008–13), and those are failed-bank figures that likely overstate going-concern losses. Charge-off data exclude losses the FDIC absorbed at failed banks, so the base rate's outcome is a lower bound in the cycles that mattered.

## 2. What does not change

- **No score, threshold, prediction or probability moves.** REG-29 (cohort Q4 NCO rise, 45%) rests on the appraisal-refresh mechanism and an 8-transition base rate, not on coverage (`workbook/PREDICTIONS.tsv` row REG-29); untouched. REG-30 (VLY non-accrual ≥ $511.4M, 60%) is a problem-loan line and stays.
- **The matrix's coverage POINT is a different object and stays frozen.** Channel 2 adds 1 when allowance ÷ nonaccrual is below 100% (a LEVEL, not a change). Its justification was already corrected 10/23 to "untested warning indicator", and whether it adds information is tested on 11/07 by the frozen protocol (S1 with the point vs S2 without). DEWEY's post-hoc level result (coverage level sorted 2008 failures, 34.7% failed below 45%, but added little once the problem-loan level was controlled: failure-model R² 0.321 → 0.324) is a prior for that test, not a reason to re-score before it. Re-scoring now would change what the frozen test measures.
- **Which banks are concerning does not change:** FLG, EGBN and OZK stay the CRE top three; the concentration claim was already carried by the problem-loan leg and the CRE concentration channel, not by coverage.

## 3. What the coverage line is still good for: a question about specific loans

DEWEY's Table 6b is the reason the ratio cannot predict: when a collateral-dependent loan's shortfall is charged off, the remaining balance sits at collateral value with little reserve, so coverage falls whether losses are already recognised (benign) or new problem loans are being called well-secured on old appraisals (adverse). Only the loss on exit, loan by loan, separates them. So the cohort line becomes: **which nonperforming loans carry no specific reserve on a collateral claim, and what did the ones that left actually lose against carrying value?**

| Name | No-reserve-on-collateral claim | Exit evidence to grade it | When |
|---|---|---|---|
| FLG | $1,571M of non-accrual carries no allowance; specific reserve $163M = 5.8% of non-accrual [6/30, 10-Q]; ACL flat $869M while non-accrual rose to $2,817M, coverage 30.85% [Q3 release, derived] | FLG desk roll-forward (13 filings): **cure share 59.5% (2023H1) → 1.6% (2026H1); 87.5% of outflow by payoff/disposition**; management says exits clear at 1–5% of the mark (SECONDARY via the call, loss vs carrying value, not par). The book churns rather than drains: H1-2026 formation $780M replaced 81.7% of outflow. | FLG Q3 10-Q ~Nov 6–9 (roll-forward, formation vs outflow) |
| VLY | $30.1M construction loan "well-secured … did not require a specific reserve" (8-K 10/22); LTVs on appraisals seasoned ~2.5 years | Appraisal date and resolution of that loan; REG-30 grades total non-accrual at Q4 | 10-Q ~11/10; Q4 release |
| EGBN | $56.0M Prince George's multifamily to nonaccrual, re-extended to 12/21/26, no cash; two pass-rated construction loans on 2022–23 appraisals | REG-28 Q4 maturity outcomes | Q4 release ~late Jan 2027 |

**FLG as a cohort input (the row's ask):** the roll-forward says FLG's exits now run almost entirely through payoff and disposition, not cure. That makes FLG's low coverage exactly the case DEWEY's Table 6b describes: the reading depends on the loss at exit, and the exit channel is the market for the collateral, not borrower recovery. The FLG desk notes the roll-forward is an FR Y-14Q item and not public for peers, so **no cohort base rate for cure share can be built**; FLG cannot be ranked against peers on this flow, and I do not infer one. FLG's coverage level (30.85%, company basis) sits below DEWEY's <45% bucket from 2008Q2; that comparison is post-hoc, cross-regime (CECL) and on a different basis (company release vs Call Report), so it is recorded and not adopted.

## 4. Data state on 10/30 and the re-run

- **Q3 Call Reports: not yet loaded at FDIC BankFind** (`REPDTE:20260930` → 0 rows, checked 2026-10-30 09:09 ET; evidence `WAL-KRE-settled_and_FDIC-Q3-check.txt` in this folder). Most banks' filing deadline is 10/30; FFIEC public release ~11/14 per the spawn brief. Not waited for (brief).
- **Re-reads already on the calendar, not new monitors:** 11/04 FFIEC short-list re-run before the JWT lapses 11/05 (WQ-495.CDR, Will's hands) · 11/07 Call Report run + frozen ranking test (S1 vs S2 settles the coverage POINT question on this cohort) · DEWEY re-runs its base rate after the Q3 call reports (its own row).
- **What would change this decision:** a post-2020 episode in which the joint pattern is followed by a ≥25bp charge-off rise while the problem-loan rise alone is not, or the 11/07 test showing S1 beating S2 on Q3 deterioration. Either re-opens the coverage leg; neither exists today.

## 5. Plain-language version (for PROME's synthesis)

The Q3 bank prints showed two things together: more bad loans at most of the names I read, and reserves covering a smaller share of them. History says only the first one has predicted losses. Banks whose reserve coverage fell most in 2008 did not lose the most, and the combined pattern was followed by a jump in charge-offs in 2 of 10 past episodes, no better than a random quarter. So I keep the bad-loan rise as the signal and stop treating falling coverage as a warning on its own. What coverage still tells us is where to look: loans the banks say are safe because of collateral, chiefly at Flagstar, whose bad loans now leave almost only by payoff or sale rather than by recovering. Whether those exits lose more than the banks expect is the thing to watch, and the next evidence is Flagstar's 10-Q in early November. Nothing about positions, scores or thresholds changes.

## 6. Inbox drain, 10/30 (13 packets, every sender)

| Lane | Item | Disposition |
|---|---|---|
| general | CYPHER 10/29 Jack Henry + Sharetec | INFO_ONLY: no core or processing disruption at a cohort bank; Sharetec is credit unions |
| general | CYPHER 10/29 N-central MSP route | INFO_ONLY: route revised to "some traffic"; the small NY savings bank is outside the cohort and its vendor link is unconfirmed |
| general | CYPHER 10/29 wave re-check | ACTED: rows 3 and 8 NOT-FIRED noted; the 10/22 boundary ask answered → `AGENTS/CYPHER/inbox/2026-10-30_from-REGINALD_boundary-confirmed.md` (CONFIRMED, credit-union-only items amended to P3) |
| WALTER | SIG-W-20261029-016 ECB hold | INFO_ONLY (HANS) |
| WALTER | SIG-W-20261029-017 HY 314 [10/28] | INTEGRATED: STATUS HY, CCC/HY (4.16×, HY-tightening-led, no escalation) rows refreshed; REG-T-03 exit run 0; REG-T-04 not fired |
| WALTER | SIG-W-20261029-019 ARCC/MFIC | INFO_ONLY (BROCK): an equity price, not a loan mark |
| WALTER | SIG-W-20261029-024 four CRE cases, office CMBS payoff 12.79% | INFO_ONLY (CREED action): bank holders unknown |
| WALTER | SIG-W-20261029-028 housing investors, Canada, Australia | INFO_ONLY (HOMER) |
| WALTER | SIG-W-20261029-036 DEWEY cyber 008R (REGINALD action) | Graded NO-BANK-CONSEQUENCE: no named bank or core-vendor victim |
| WALTER | SIG-W-20261029-038 / -039 / -044 vendor incidents | INFO_ONLY: no cohort bank, no core or processing hit |
| WALTER | SIG-W-20261029-043 correction to 039 | NO-OP receipt COR-20261029-43 (no REGINALD surface cites the dead line) |

BOARD scan backstop: SIG-W-20261029-026 (CCC two indices) logged BACKFILL; my CCC/HY row is on the ICE basis. Rows in `board/BOARD_LOG.tsv`. Peer channels (OZK, WAL): 0 entries above my last ACK.

Levels refreshed at the same pass: WAL $77.80 and KRE $72.86 [10/29 settled, Yahoo and Nasdaq agree]; REG-T-02 exit log rows for 10/28 and 10/29 (run 0-of-3). FLG ladder RED, $10.47 [10/29], 16 settled closes below RED.
