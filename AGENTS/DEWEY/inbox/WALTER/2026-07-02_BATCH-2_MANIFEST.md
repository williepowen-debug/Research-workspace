# DEWEY BATCH 2 — queue manifest (13 prompts, Will-approved 2026-07-02)

**From:** PROME (Will-directed) · **For:** DEWEY (execute, loop mode) + Will (launch/oversight) · **WALTER:** logs ledger rows + routes outputs (packet: `AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md`)

**Provenance:** fleet-wide mining sweep 7/1 late — 22 readers over every active agent's state files + DEWEY's own Process Reports + the coverage-gap analysis → 108 raw candidates → merged/ranked → adversarially verified (already-answered? cheap-verifiable? decision real? primaries exist?) → these 13 survived. Full slate + the ~60-item next-batch bench: `PROME/proposals/2026-07-01_dewey-prompt-slate.workflow.json`. Every prompt cites the owning agent's own flagged gap as originating evidence.

## Loop protocol (DEWEY)

Will approved running the WHOLE queue. Process in **filename order** (05→17 — docket-driven: the deliver_by dates are monotone). Per prompt:
1. Run the paste-and-go `/deep-research` prompt (Thesis mode; one workflow at a time — do NOT run research workflows concurrently, `[[finding_workflow_concurrency_529]]`).
2. Layer DEWEY discipline on the return: independent primary-source pass on load-bearing numbers, citations, counter-evidence, Process Report.
3. Archive to `output/`, append the `INDEX.tsv` row (note the REQ flag ID), write the create-only handoff to `AGENTS/WALTER/inbox/DEWEY/`.
4. `git mv` the consumed prompt to `processed/` and **commit (pathspec) after EACH report** — checkpoints make the queue crash/relaunch-safe; don't batch commits to the end.
5. Take the next file. Ending the session mid-queue is fine — the queue is durable; the next DEWEY session resumes at the first unprocessed prompt (boot step 4 surfaces it).

**Session sizing suggestion:** ~3-5 reports per session, then closeout (safe-push) and let Will relaunch — keeps context fresh and ships results to origin incrementally. 13 runs ≈ 3-4 DEWEY sessions over ~2 weeks, which matches the deliver_by ladder.

## Queue at a glance

| # | File | Deliver by | Gates |
|---|------|-----------|-------|
| 05 | hy-ccc-widening-decomposition | ASAP (Gate A ~7/2; Bin-A 7/6-7/10) | VIOLET Gate A + Bin-A; LIQUID X1 composition check |
| 06 | hormuz-reopening-scorecard | **7/4** (HAW-13) | HAWK HAW-13; BRENT BRT-07/17, re-arm line |
| 07 | funding-seizure-x1-gate | ASAP (HY 5bp from 280) | X1 validity; LIQUID funding-plumbing mandate |
| 08 | jgb-superlong-demand-sign | **7/6** (30Y auction 7/7) | SAM carry-tail trigger SIGN; SAM-32/33 |
| 09 | ust-demand-rotation | **7/7** (refunding 7/7-9) | BOND BND-11; TLT add-gate; NEXUS PRED-30 |
| 10 | energy-hy-oas-unblind | ASAP (blind 64d) | LIQUID >300 trip; BRENT >400; BOND VX-11 |
| 11 | food-supply-cpi-fork | **7/9** (CPI 7/14) | CARL CRL-10; MARCO ES-MARCO-08; NEXUS S-26060701 |
| 12 | mechanical-selling-stack | 7/10 (opex 7/17) | HENRY HEN-35; VIOLET hedge sizing |
| 13 | criticized-credit-migration | 7/14 (prints 7/16) | CHG-RED-040; REG-24/25; RED beat/miss tree |
| 14 | bank-private-credit-exposure | 7/14 (prints 7/16) | NEXUS PRED-24 Stage-3; WAL V3; APO Dec $95P |
| 15 | fha-va-loss-waterfall | 7/14 (prints 7/16) | REGINALD Path C leg live-or-dies |
| 16 | bdc-rating-actions-print-hunt | 7/22 (marks 7/25-28) | BROCK BRK-25 → BIZD Sep $12P; NEXUS PRED-27/45 |
| 17 | insurer-lender-double-jeopardy | 7/22 (see governance_note in file) | SHADE/BROCK named-entity map; TERRY pre-stage |

**Freshness rules:** if a prompt's deliver_by has PASSED when you reach it, still run it but re-read its docket anchor first (the decision may have re-marked — note that in the report). Prompt 11 prefers the Jul-10 WASDE if you reach it on/after 7/10.
