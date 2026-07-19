# DEWEY BATCH 2 — queue manifest (13 prompts, Will-approved 2026-07-02)

**From:** PROME (Will-directed) · **For:** DEWEY (execute, loop mode) + Will (launch/oversight) · **WALTER:** logs ledger rows + routes outputs (packet: `AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md`)

**Provenance:** fleet-wide mining sweep 7/1 late — 22 readers over every active agent's state files + DEWEY's own Process Reports + the coverage-gap analysis → 108 raw candidates → merged/ranked → adversarially verified (already-answered? cheap-verifiable? decision real? primaries exist?) → these 13 survived. Full slate + the ~60-item next-batch bench: `PROME/proposals/2026-07-01_dewey-prompt-slate.workflow.json`. Every prompt cites the owning agent's own flagged gap as originating evidence.

## Loop protocol (DEWEY)

Will approved running the WHOLE queue. **Process in the PRIORITY ORDER in the "Queue at a glance" table below — NOT filename order** (re-prioritized 2026-07-04; see the revision note under the table — the filename numbers `07`–`18` are stable identifiers only, they no longer encode run order). Per prompt:
1. Run the paste-and-go `/deep-research` prompt (Thesis mode; one workflow at a time — do NOT run research workflows concurrently, `[[finding_workflow_concurrency_529]]`).
2. Layer DEWEY discipline on the return: independent primary-source pass on load-bearing numbers, citations, counter-evidence, Process Report.
3. Archive to `output/`, append the `INDEX.tsv` row (note the REQ flag ID), write the create-only handoff to `AGENTS/WALTER/inbox/DEWEY/` — **AND (NEW 2026-07-19, constrained-B) deliver a create-only POINTER stub into each named recipient's inbox at write-time** (pointer to the `output/` report + the per-recipient action block + REQ ID; main session only, reviewed, pathspec — see the inbox change-packet `AGENTS/DEWEY/inbox/2026-07-19_from-PROME_constrained-B-routing-change.md`). WALTER now owns the ledger/audit + backstop, not primary routing.
4. `git mv` the consumed prompt to `processed/` and **commit (pathspec) after EACH report** — checkpoints make the queue crash/relaunch-safe; don't batch commits to the end.
5. Take the next file. Ending the session mid-queue is fine — the queue is durable; the next DEWEY session resumes at the first unprocessed prompt (boot step 4 surfaces it).

**Session sizing suggestion:** ~3-5 reports per session, then closeout (safe-push) and let Will relaunch — keeps context fresh and ships results to origin incrementally. 13 runs ≈ 3-4 DEWEY sessions over ~2 weeks, which matches the deliver_by ladder.

## Queue at a glance — PRIORITY ORDER (re-prioritized 2026-07-08, supersedes 7/04 ordering on item 10 only)

**Delivered (do not re-run):** **05** hy-ccc-widening-decomposition + **06** hormuz-reopening-scorecard — DEWEY delivered 7/2, WALTER routed the outputs, both in `processed/`.

**Live queue = 12 prompts. Run top-to-bottom (this order, NOT the filename numbers):**

| Order | File (stable ID) | Deliver by | Why here / gates |
|---|------|-----------|-------|
| 1 | **18** coreweave-neocloud-credit *(NEW 7/4)* | ASAP | **The live AI-credit canary** — feeds the Mon 7/6 HY-index cohort discriminator (the fleet's #1 watch). Issuer-side capital-structure + transmission map. → LIQUID/HENRY |
| 2 | **10** energy-hy-oas-unblind *(RE-PRIORITIZED UP 7/8 — was #12/DEPRIORITIZED)* | **ASAP** (sustain test through Fri 7/10) | **The 7/4 "energy de-escalated" premise this was deprioritized on REVERSED overnight 7/7→7/8**: US-Iran truce collapsed (US struck 80+ targets, Treasury revoked ceasefire oil relief wind-down 7/17, Iran hit 3 neutral tankers + fired on Gulf bases), Brent +6.3% to $78.82. BRENT/HAWK/SAM adjudicated the re-arm tonight (energy tail RE-ARM, ACTIVE, sustain test through Fri 7/10); LIQUID tasked tonight with energy-OAS re-state + pre-registering the HY path under an oil-sustained week — this prompt's HY-OAS-by-energy-exposure decomposition directly feeds that pre-registration. Run now, not for the monitoring-source deliverable only. → LIQUID |
| 3 | **07** funding-seizure-x1-gate *(reframed 7/4)* | ASAP | X1 validity + the CoreWeave "stress-real-but-index-doesn't-print" pre-emption question; LIQUID funding-plumbing mandate |
| 4 | **08** jgb-superlong-demand-sign *(REVISED 7/4)* | **7/6** (30Y auction 7/7, PASSED — re-read docket anchor on pickup) | Meiji Yasuda demand-floor banked → now announcement-vs-flow; SAM carry-tail SIGN, SAM-32 FALSE/SAM-33 |
| 5 | **09** ust-demand-rotation | **7/7** (refunding 7/7-9, PASSED — re-read docket anchor on pickup) | BOND BND-11 (30Y reopen 7/9 decisive); TLT add-gate; NEXUS PRED-30 |
| 6 | **11** food-supply-cpi-fork | **7/9** (CPI 7/14) | CARL CRL-10; MARCO ES-MARCO-08; NEXUS S-26060701 (prefers Jul-10 WASDE if reached ≥7/10) |
| 7 | **12** mechanical-selling-stack | 7/10 (opex 7/17) | M-09 AI-positioning-unwind live (CoreWeave adds to it); HENRY HEN-35; VIOLET hedge sizing |
| 8 | **13** criticized-credit-migration | 7/14 (prints 7/16) | *Hotter* (OZK deed-in-lieu + S2 realized); CHG-RED-040; REG-24/25; RED beat/miss tree |
| 9 | **14** bank-private-credit-exposure | 7/14 (prints 7/16) | *Hotter* (CoreWeave/XPV + S2/Benefit Street); NEXUS PRED-24 Stage-3; WAL V3; APO Dec $95P |
| 10 | **15** fha-va-loss-waterfall | 7/14 (prints 7/16) | REGINALD Path C leg live-or-dies |
| 11 | **16** bdc-rating-actions-print-hunt | 7/22 (marks 7/25-28) | BROCK BRK-25 → BIZD Sep $12P; NEXUS PRED-27/45 |
| 12 | **17** insurer-lender-double-jeopardy | 7/22 (see governance_note in file) | SHADE/BROCK named-entity map; TERRY pre-stage |

### ★ 2026-07-19 revision note (PROME, Will-directed) — delivery protocol, not ordering
- **Constrained-B write-time delivery ADOPTED** (Will 2026-07-19): DEWEY now delivers create-only POINTER stubs directly to each named recipient's inbox at report write-time (loop step 3, amended above), killing the async latency gap that stranded prompts 11+13 unrouted on 7/10. WALTER shifts primary-router → ledger/audit owner + backstop (verify stubs landed, deliver any missed, liveness-flag). Guardrails preserved: main session only, create-only, pointer-not-resynthesis, pathspec, sub-agents never route/commit. Durable spec (for batch 3): `AGENTS/DEWEY/inbox/2026-07-19_from-PROME_constrained-B-routing-change.md` (DEWEY applies to its own CLAUDE.md at next boot). WALTER backstop packet: `AGENTS/WALTER/inbox/2026-07-19_from-PROME_dewey-routing-backstop-A.md`. **Queue order below is UNCHANGED.**

### ★ 2026-07-08 revision note (WALTER, per PROME tasking — reverses the 7/04 note's item-10 call only)
- **10 energy-hy-oas-unblind RE-PRIORITIZED UP** (was #12/bottom, "run for the monitoring-source deliverable only"): the "energy de-escalated" premise it was deprioritized on has REVERSED — US-Iran truce collapsed 7/7→7/8 (US struck 80+ targets; Treasury revoked ceasefire oil-sales relief, wind-down 7/17; Iran hit 3 neutral tankers in Hormuz + fired on Gulf bases; Brent +6.3% to $78.82). Fleet adjudicated tonight: BRENT = energy tail RE-ARM (ACTIVE, sustain test through Fri 7/10); HAWK = ladder B12/C42/D46; SAM = JGB 30Y FIRM. LIQUID tasked tonight with energy-OAS re-state + pre-registering the HY path under an oil-sustained week — this prompt directly feeds that. Moved to #2 (right after the still-live CoreWeave AI-credit canary).
- All other ordering/notes below are the unchanged 2026-07-04 PROME revision (item 10's entry there is superseded by this note):

### 2026-07-04 revision note (PROME, Will-directed) — retained for history; item 10 above supersedes
Re-prioritized after the 7/4 developments materially shifted the slate:
- **05 + 06 DELIVERED** (7/2) — dropped from the queue.
- **18 coreweave-neocloud-credit ADDED** — the CoreWeave junk-bond slide (SIG-704-001) is now the #1 live watch and the Mon 7/6 discriminator; not covered by 05 (index-level) or 14 (bank-syndicate). **WALTER: log a NEW ledger row for REQ-DEWEY-20260704-018 at next boot (QUEUED).**
- **08 REVISED** — SAM's 7/2 Meiji Yasuda demand-floor (SAM-32 FALSIFIED) partially answered the sign question; the prompt now asks announcement-vs-flow so DEWEY doesn't re-derive it.
- **07 reframed** — "5bp-from-280" urgency softened (HY receded to 275), but CoreWeave makes the single-name-pre-emption angle live; added to the closing judgment.
- ~~**10 DEPRIORITIZED** — energy de-escalated~~ **REVERSED 7/8, see note above.**
- **09/11/12/13/14/15/16/17 unchanged** (13/14 flagged *hotter* by the credit-substance firming); all their gating catalysts remain on `PROME/DOCKET.tsv`, unfired.

**Freshness rules:** if a prompt's deliver_by has PASSED when you reach it, still run it but re-read its docket anchor first (the decision may have re-marked — note that in the report). Prompt 11 prefers the Jul-10 WASDE if you reach it on/after 7/10.
