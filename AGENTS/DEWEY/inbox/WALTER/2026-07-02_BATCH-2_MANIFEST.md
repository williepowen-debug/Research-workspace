# DEWEY BATCH 2 — queue manifest (13 prompts, Will-approved 2026-07-02)

**From:** PROME (Will-directed) · **For:** DEWEY (execute, loop mode) + Will (launch/oversight) · **WALTER:** logs ledger rows + routes outputs (packet: `AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md`)

**Provenance:** fleet-wide mining sweep 7/1 late — 22 readers over every active agent's state files + DEWEY's own Process Reports + the coverage-gap analysis → 108 raw candidates → merged/ranked → adversarially verified (already-answered? cheap-verifiable? decision real? primaries exist?) → these 13 survived. Full slate + the ~60-item next-batch bench: `PROME/proposals/2026-07-01_dewey-prompt-slate.workflow.json`. Every prompt cites the owning agent's own flagged gap as originating evidence.

## Loop protocol (DEWEY)

Will approved running the WHOLE queue. **Process in the PRIORITY ORDER in the "Queue at a glance" table below — NOT filename order** (re-prioritized 2026-07-04; see the revision note under the table — the filename numbers `07`–`18` are stable identifiers only, they no longer encode run order). Per prompt:
1. Run the paste-and-go `/deep-research` prompt (Thesis mode; one workflow at a time — do NOT run research workflows concurrently, `[[finding_workflow_concurrency_529]]`).
2. Layer DEWEY discipline on the return: independent primary-source pass on load-bearing numbers, citations, counter-evidence, Process Report.
3. Archive to `output/`, append the `INDEX.tsv` row (note the REQ flag ID), write the create-only handoff to `AGENTS/WALTER/inbox/DEWEY/`.
4. `git mv` the consumed prompt to `processed/` and **commit (pathspec) after EACH report** — checkpoints make the queue crash/relaunch-safe; don't batch commits to the end.
5. Take the next file. Ending the session mid-queue is fine — the queue is durable; the next DEWEY session resumes at the first unprocessed prompt (boot step 4 surfaces it).

**Session sizing suggestion:** ~3-5 reports per session, then closeout (safe-push) and let Will relaunch — keeps context fresh and ships results to origin incrementally. 13 runs ≈ 3-4 DEWEY sessions over ~2 weeks, which matches the deliver_by ladder.

## Queue at a glance — PRIORITY ORDER (re-prioritized 2026-07-04)

**Delivered (do not re-run):** **05** hy-ccc-widening-decomposition + **06** hormuz-reopening-scorecard — DEWEY delivered 7/2, WALTER routed the outputs, both in `processed/`.

**Live queue = 12 prompts. Run top-to-bottom (this order, NOT the filename numbers):**

| Order | File (stable ID) | Deliver by | Why here / gates |
|---|------|-----------|-------|
| 1 | **18** coreweave-neocloud-credit *(NEW 7/4)* | ASAP | **The live AI-credit canary** — feeds the Mon 7/6 HY-index cohort discriminator (the fleet's #1 watch). Issuer-side capital-structure + transmission map. → LIQUID/HENRY |
| 2 | **07** funding-seizure-x1-gate *(reframed 7/4)* | ASAP | X1 validity + the CoreWeave "stress-real-but-index-doesn't-print" pre-emption question; LIQUID funding-plumbing mandate |
| 3 | **08** jgb-superlong-demand-sign *(REVISED 7/4)* | **7/6** (30Y auction 7/7) | Meiji Yasuda demand-floor banked → now announcement-vs-flow; SAM carry-tail SIGN, SAM-32 FALSE/SAM-33 |
| 4 | **09** ust-demand-rotation | **7/7** (refunding 7/7-9) | BOND BND-11 (30Y reopen 7/9 decisive); TLT add-gate; NEXUS PRED-30 |
| 5 | **11** food-supply-cpi-fork | **7/9** (CPI 7/14) | CARL CRL-10; MARCO ES-MARCO-08; NEXUS S-26060701 (prefers Jul-10 WASDE if reached ≥7/10) |
| 6 | **12** mechanical-selling-stack | 7/10 (opex 7/17) | M-09 AI-positioning-unwind live (CoreWeave adds to it); HENRY HEN-35; VIOLET hedge sizing |
| 7 | **13** criticized-credit-migration | 7/14 (prints 7/16) | *Hotter* (OZK deed-in-lieu + S2 realized); CHG-RED-040; REG-24/25; RED beat/miss tree |
| 8 | **14** bank-private-credit-exposure | 7/14 (prints 7/16) | *Hotter* (CoreWeave/XPV + S2/Benefit Street); NEXUS PRED-24 Stage-3; WAL V3; APO Dec $95P |
| 9 | **15** fha-va-loss-waterfall | 7/14 (prints 7/16) | REGINALD Path C leg live-or-dies |
| 10 | **16** bdc-rating-actions-print-hunt | 7/22 (marks 7/25-28) | BROCK BRK-25 → BIZD Sep $12P; NEXUS PRED-27/45 |
| 11 | **17** insurer-lender-double-jeopardy | 7/22 (see governance_note in file) | SHADE/BROCK named-entity map; TERRY pre-stage |
| 12 | **10** energy-hy-oas-unblind *(DEPRIORITIZED 7/4)* | slack only | Energy DE-ESCALATED → stress-hunt moot; run for the durable free-monitoring-source deliverable only |

### ★ 2026-07-04 revision note (PROME, Will-directed)
Re-prioritized after the 7/4 developments materially shifted the slate:
- **05 + 06 DELIVERED** (7/2) — dropped from the queue.
- **18 coreweave-neocloud-credit ADDED** — the CoreWeave junk-bond slide (SIG-704-001) is now the #1 live watch and the Mon 7/6 discriminator; not covered by 05 (index-level) or 14 (bank-syndicate). **WALTER: log a NEW ledger row for REQ-DEWEY-20260704-018 at next boot (QUEUED).**
- **08 REVISED** — SAM's 7/2 Meiji Yasuda demand-floor (SAM-32 FALSIFIED) partially answered the sign question; the prompt now asks announcement-vs-flow so DEWEY doesn't re-derive it.
- **07 reframed** — "5bp-from-280" urgency softened (HY receded to 275), but CoreWeave makes the single-name-pre-emption angle live; added to the closing judgment.
- **10 DEPRIORITIZED** — energy de-escalated (Iran re-stamp, record oil-on-water, Houston premium→$0); moved to the bottom, run for the monitoring-source deliverable only.
- **09/11/12/13/14/15/16/17 unchanged** (13/14 flagged *hotter* by the credit-substance firming); all their gating catalysts remain on `PROME/DOCKET.tsv`, unfired.

**Freshness rules:** if a prompt's deliver_by has PASSED when you reach it, still run it but re-read its docket anchor first (the decision may have re-marked — note that in the report). Prompt 11 prefers the Jul-10 WASDE if you reach it on/after 7/10.
