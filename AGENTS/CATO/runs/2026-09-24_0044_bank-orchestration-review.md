# Regional-bank orchestration round — September 24, 2026

**Current disposition: useful delivery, with bounded corrections required before treating every new instrument and conclusion as complete.** CATO reviewed the four-bank turn at `6b51442c3c1e33d42afb89045251b80b1bbb2006`. RB1–RB3 are the principal content/tool findings; RB4 is incomplete required rotation, RB5 a smaller monitoring-description error. No owner files were edited and no messages or launches were made. This review is delivered; orient and await Will's chosen follow-up.

## Assignment, perimeter and delivery evidence

Will: “Okay a turn of work just finished. Can you read through?” Context: PROME orchestrating his regional-bank desks, with CATO helping assess instructions and work. Inspected the latest four-bank delegation and its deliveries, not the whole prior catch-up session or PROME's still-running operational session. The later VIOLET/OSPREY spawns at `6b51442c3` are outside scope.

Startup tree was clean; `git pull --rebase` returned up to date. VIOLET later acquired unrelated working changes; preserved. Core commits: delegation `0ad8fc4df`; WAL frame `52304eeae`; REGINALD rotation `34e08ee49` and frame/memo `91e6d9ca3`; FLG `164f04067`; OZK `212fad817`; PROME consumption `939d7ca95` and `e9c04912d`.

**VERIFIED at records:** `PROME/state/ORCH_LOG.tsv` has four September 24 DOORBELL rows with named task briefs, delivery artifacts and structured ASKED_RECEIPT records. Each records the closeout ask in the original brief and a reply received at 00:31–00:35 ET. All four completion memos exist under `PROME/inbox/processed/2026-09-24_from-{WAL,REGINALD,FLG,OZK}_...`. This verifies PROME's durable accounting; CATO did not independently inspect the live SendMessage transcript and does not recertify runtime presence. PROME's full-session closeout is not yet the subject of this review.

The desk-to-coordinator correction loop worked in two important cases. WAL rejected the stale request for P2/P3 approval: row 32b of `PROME/proposals/2026-08-12_rule-batch-RULED.md` and repair `df87ac3f4` support its objection; PROME recorded the brief defect. OZK corrected the interest-drag input and identified an unarmed filing watch; PROME registered interim boot reads and the October 2 owner read. No trade recommendation or new approval follows from this review.

## RB1 — Medium: REGINALD's frozen frame lacks a deterministic bank-level verdict

**Source / VERIFIED:** `AGENTS/REGINALD/reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md:23–61`. The tables define metric-level TRANSMITS/HOLDS branches, while the aggregate counts **banks** (two TRANSMITS or three HOLDS). The file never explicitly combines a bank's disagreeing metrics into its single class. Labeling one metric “primary” does not settle whether it overrides, needs corroboration, or merely receives more weight.

**Counterexamples:** BKU can have its primary delinquency row HOLDS, 90+ TRANSMITS, and criticized HOLDS. “Primary controls,” “any adverse metric controls,” and “disagreement means MIXED” generate different outcomes. SBCF's primary row also leaves $13M in 30–89 days with $2M in 60–89 days in neither branch: it fails the ≥$3M seasoning limb but is not below $12.48M. AMTB classified growth attributed to acquired pools likewise meets neither stated branch. MIXED exists as a class, but the mapping to it is not specified. SBCF's residential row is inside its table while §3 excludes the residential sub-read from the aggregate; the combiner must honor that exclusion.

**Consequence:** the same filing can support different bank counts and change the CORAL/PROME signal after the data arrives, despite the FROZEN label.

**Correction / close when:** REGINALD adds a dated pre-print clarification covering per-name combination, boundary/missing-disclosure outcomes, excluded residential metrics and provisional versus final grades. Demonstrate the conflicting-metric and uncovered-branch cases. Preserve the existing baselines and thresholds unless a separate authorized change is intended. Do not let CATO choose the bank thesis rule. The already disclosed SSB/AMTB baseline rereads remain owed before grading.

## RB2 — Medium: OZK's categorical exclusion of reclassification exceeds its evidence

**Source / VERIFIED:** `AGENTS/OZK/MI3_2025Q3_ADJUDICATION.md` §§6.1b–6.2; the September 24 completion memo; `PROME/DOCKET.tsv` L181 at `e9c04912d`. The new FDIC 10-Q evidence is useful: locally stored Q2/Q3 2025 PDFs, PDF p.37 (and the p.38 classification footnote), support management's named debt-on-debt balance declining from approximately $1.20B to $0.77B and the Q3 NDFI breakdown. The repo's five-quarter table includes later quarters not independently re-extracted in this review. Public web opens of the two FDIC attachment URLs were unavailable; CATO inspected the locally stored primary PDFs, not a freshly authenticated download.

**Defect:** “no within-9.a relabel” follows from other sub-buckets growing only $68M; §6.2 further says relabeling “would leave item 9.a flat.” These are net endpoint comparisons, not loan-flow evidence. A within-container transfer can coexist with repayments or originations in the recipient and other buckets.

**Concrete counterexample ($K; hypothetical, not an allegation):** transfer 432,181 from PV09 to PV06 and allow PV06 other net runoff of 409,544. PV06 rises by the reported 22,637, while PV09 falls by the reported 432,181. Keep PV07 −212,636 and PV08 +45,729 as reported. All four endpoints and the total −576,451 fit exactly. Therefore the observed balances cannot refute that branch. The unchanged definition of the remaining reported book does not independently identify loans that left it. The report correctly retains loan-level exit UNKNOWN and C&I migration unfalsified; these limits should also constrain its categorical branch table and PROME's “relabel ... ruled out” summary.

**Consequence:** PROME can carry a plausible repayment inference as an exclusion proven by data. This does **not** establish reclassification occurred or overturn the named-book decline. It also does not justify reviving the already withdrawn claim that these loans stayed in item 4.

**Correction / close when:** OZK separates observed reported-book decline from inferred economic runoff, qualifies the categorical exclusion of within-NDFI reclassification, and supplies discriminating evidence if it wants to retain REFUTED. PROME propagates that narrower disposition to L181 and affected current summaries/recipients (the new REGINALD and BROCK verdict packets are in scope). The owner may retain repayment as the favored inference. No compulsory transcript chase, new loan-level investigation or trade follows.

## RB3 — Medium: the new FDIC watch can turn missing data into QUIET

**Source / VERIFIED by isolated execution:** `AGENTS/OZK/scripts/flng_watch.py:26–43`. Only fetching/JSON decoding is inside the error handler; row shape and historical baseline coverage are not validated before the no-new-filings result.

Pinned-code fixtures returned: known baseline → rc0; valid new filing → rc1; network failure → rc2; **empty JSON list → rc0 QUIET; empty JSON object → rc0 QUIET; row missing `instFlngId` → uncaught KeyError / process rc1**, which collides with the documented NEW result. No live API malfunction is asserted. These are independent counterexamples to the watch's missing-information contract, beyond the author's successful old-baseline test.

**Consequence:** both OZK CALENDAR's October 1 row and PROME's new October 2 row instruct rc0 → record the reprice as happened. An incomplete/invalid response can therefore advance a real-world event claim instead of leaving it UNKNOWN. Even a valid quiet response establishes only no newer returned filing; the contractual event inference must remain distinct from affirmative event confirmation.

**Correction / close when:** OZK validates the response schema and sufficient historical coverage/known baseline, maps malformed or incomplete data to rc2, keeps genuine new filings rc1, and tests normal, missing-information and failure paths. Preserve the baseline and owner cadence unless explicitly changed. PROME retains the scheduled watch but qualifies the rc0 consumer wording to the evidence it actually supplies. Use existing repair-review controls; no new service or monitoring framework is needed.

## RB4 — Low, required process completion: REGINALD's rotation is still partial

**VERIFIED:** rerunning `python3 -B scripts/read_cap_check.py --agent REGINALD` reproduced over_budget=0, rotation_due=3. STATUS 31,201 B, MEMORY 27,195 B, CALENDAR 26,357 B remain above the rotation trigger; ROADMAP, just rotated in `34e08ee49`, is 24,119 B. `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md:11` requires stopping below 22,785 B, not merely below the budget. The tool explicitly identifies the just-rotated 70–75% case.

PROME discloses the three rotate-tier files, which is good, but its L350 “REGINALD DONE” and the owner task-DONE token should distinguish the passed size check from unfinished mandatory rotation. ROADMAP is an additional unfinished rotation despite not contributing to rotation_due=3. CATO did not verify every archive CRC or the before/after obligation census and does not allege lost content.

**Correction / close when:** retain PARTIAL until the four rotated surfaces satisfy the prescribed stop condition and preservation checks, or accurately carry an explicit authorized deferral. No indiscriminate deletion or immediate broad archival batch is recommended by this review.

## RB5 — Low: FLG's check timing was compressed into an incorrect latency claim

**VERIFIED:** FLG T-12 says September 30 is “1 business day before T-08.” That is a lead time. Its completion memo and PROME GATES's T08 addendum describe a stay arriving September 26–29 as an accepted “at most one business day” gap. A Monday September 28 stay first found Wednesday September 30 waits two business days; WALTER intake is explicitly best-effort. The primary docket remains inaccessible/SEARCH-NOT-FOUND, and WQ-279 correctly presents the browser check as optional.

**Correction / close when:** distinguish the September 30 check's one-day lead before October 1 from the potentially multi-day detection lag after the September 25 check. Explicitly retain that gap or choose closer reads; no automatic daily-watch build. This review does not independently establish the case's latest legal status, overturn the source grades, or require Will to perform the optional browser task.

## Checks, limits and suggested instruction

Reproduction: `python3 -B AGENTS/CATO/runs/2026-09-24_0044_bank-orchestration-repro.py`; output stored alongside as `2026-09-24_0044_bank-orchestration-evidence.json`. The code pins the reviewed Git revision and uses mocked HTTP responses only. All six reproduced exit states and the balance counterexample matched the recorded assertions. CATO authored this reproduction; it is independent testing of OZK's implementation, not a new owner repair. Closeout: exact-path diff whitespace check passed; weekday claim check passed on DOCKET, GATES, WILL_QUEUE and this report. Orphan advisory identified only other owners' work outside CATO, including newer WAL/VIOLET/OSPREY work excluded from this snapshot. Foreign staged VIOLET inbox moves were observed and preserved; CATO's commit uses four exact paths.

WAL's new print frame distinguishes not-disclosed from zero, provisional Office grades from the later cross-check, and primary versus B2 management benchmarks. Its coverage-denominator pin is consistent with the historical v2.3 96% basis inspected in `df87ac3f4^`; no demonstrated basis-change finding here. No full external baseline, live price, broker, litigation docket or all-bank source audit was conducted. Previously closed CATO reviews and publication approvals remain untouched. No hosted output was inspected or published.

Suggested instruction to PROME: “Keep this round's useful deliveries. Route RB1–RB3 from CATO's September 24 report to REGINALD and OZK for bounded corrections: make the bank-level grades deterministic, qualify what the OZK evidence excludes, and make the FDIC watch return UNKNOWN on unusable data. Update your consumed summaries to match. Carry REGINALD's remaining rotation as partial and describe FLG's actual monitoring gap. Return the exact changes, tests and remaining limits; do not reopen settled WAL approvals or expand the research.”

This is proposed wording for Will, not an instruction CATO has sent. CATO's only authored repo paths are this report, its reproduction/evidence and CONTINUITY. Commit and fresh-fetch push receipt will be delivered in-session. Resume: await Will/owner disposition or an assigned bounded recheck.
