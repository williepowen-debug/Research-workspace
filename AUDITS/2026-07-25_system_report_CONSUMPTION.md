# System Report v2 — PROME Consumption Memo
**Date:** 2026-07-25 (Sat evening) · **Author:** PROME (Will in-session; intake + analysis Will-directed)
**Subject:** `AUDITS/2026-07-22_system_analysis_v2.md` (external system review, snapshot 7/22, v2 pass 7/23)
**Companion:** `AUDITS/2026-07-25_system_report_DISPOSITIONS.md` — per-recommendation ledger (canonical for adoption state; this memo is the analysis).

## Verdict

Best external read of the system produced to date; trustworthy as a planning input. Every repo-facing claim PROME could check from the inside verified accurate (KB-VIO-110 7-day orphan → GATES.tsv origin, 2-route messaging cohort, OZK transition lag, PSEC 8.6%-vs-35% behind Critical Rule 3, LABOR Brier scoreboard 7/10, HAWK sunset-armed at snapshot). The v2 revision layer is substantive, not cosmetic (§6.1 REGINALD softening; §9.1 ACH caveat).

**Central thesis independently confirmed:** the report's "analytical institution ahead of the operational control plane" (§6.1/§6.2) and PROME's own 7/25 closeout theme — "the checks were present and correct; INVOCATION is what failed" — are the same diagnosis, reached independently 3 days apart (report snapshot 7/22; PROME theme written 7/25 with no knowledge of the report). Strongest possible validation of the finding.

## Hardest hits (accepted)

1. **State-recovery cost (§6.3, P2).** PROME/STATUS.md = 95 lines / 55.7k chars; at the 7/25 evening boot the harness truncated it at line 41 against a 25k-token cap — live proof of the report's point. Line caps are being satisfied by line *density*; the real contract is bounded-budget recovery of thesis/gates/predictions/freshness by a fresh session.
2. **Transition-propagation lag (§3.1).** "The registered condition was right; the completion of the state change across surfaces was not automatic." Re-confirmed AFTER the snapshot on the same agent: OZK had no AGENTS.md row for 3 months post-promotion; the 7/25 WAL sweep found AGENTS.md *wrong, not stale*.
3. **Adjudication queue, never a dashboard (§6.8, v2).** Passive green-state dashboards are the mechanism by which oversight becomes procedural (automation-bias literature). Adopted as a standing design constraint for the Fleet-Ops dashboard and any exception view: operator-cleared, never auto-green. Converges with `finding_mechanize_the_cap_not_the_ritual`.
4. **Task-structure argument (§8.2, v2).** The workload (parallel-by-domain, tool-heavy, context-exceeding, PROME-centralized) sits in the regime where controlled studies favor multi-agent (centralized orchestration = 4.4× error amplification vs 17.2× independent). MAST mapping: observed fleet failures are coordination/verification class; the specification class (41.8% elsewhere) is suppressed by per-agent contract investment — first external quantification of what the CLAUDE.md/boot/closeout discipline buys.

## Refinements / push-backs (PROME inside-view)

1. **The dates exception-class already has the P5 machinery, working.** `firetime_check.py` + DOCKET.tsv + `scripts/firetime_allowlist.tsv` = a generated, boot-gated exception check with expiry-dated suppressions (cleared flags re-flag themselves), rc=1-always-means-act, and a full-logic-re-read rule. 14→6 flags on 7/25 via owner-routed dispositions = an adjudication queue in miniature. **P1+P5 should be built as an extension of the firetime pattern to the other exception classes** (overdue predictions, unacknowledged messages, incomplete transitions, stale briefs), not greenfield.
2. **The auto-memory layer is the report's biggest blind spot.** §10.3 credits "repeated conversion of incidents into new controls" but never names the mechanism: `memory/auto/` findings + auto-injected index + compaction discipline. It is the "lossy-by-design, contradiction-resolving consolidation" the report's own memory literature calls for — already built, ~150 findings. Deserves its own section in any case-study writeup.
3. **P6 Arm-B/C equivalence test = right question, hardest experiment.** Outcome leakage + evaluator blinding are near-intractable on reconstructed tasks. The cheap high-yield slices: RED harmful-revision ledger (V1.6 raw material exists) and blind NEXUS brief-tests. Mini-precedent in-repo: the blind 3-analyst workflow that triple-validated BROCK's X1 adjudication (7/4).
4. **Git-regime defense (§3.5).** Not a durable runtime — correct — but the serial-multi-machine + pathspec + ff-gated-push regime is deliberately cheap and its measured failure rate is now very low (zero index races across ~10 concurrent writers on recent heavy days). P7's own reframe (cron + exception view covers the first loop; workflow engine maybe never) is the right conclusion.

## What changed between the 7/22 snapshot and 7/25 (deltas the reviewer couldn't see)

- **HAWK** (the §6.1 "starkest rot case," sunset-armed): cc'd on GATE-FALCON-001 7/23, ran a full session 7/25 (Jazan refinery-vs-crude, 6 commits, inbox processed). Caught by the fleet's own machinery (DAEDALUS scan) → revived by routing. §6.4's general point stands; the named worst case is closed.
- **Orphan detector adopted fleet-wide 7/23** (`scripts/orphan_check.sh` + root carve-out ①, then ② on 7/25) — attacks the ~12% orphaned-packet class; one exception class mechanized before the recommendation was read.
- **The 7/25 calendar-correction day** = the report's thesis live, both directions: 5th fleet date error in 8 days (canonical state authoritative-and-wrong, §6.2), AND the correction loop worked (NEXUS/RED catches → independent re-verification → same-session propagation to DOCKET/HEARTBEAT/owners).
- **AEOLUS + WATT** ran in the 7/22 catch-up wave (softens the §6.1 examples; the deeper point — a *human-triggered* wave was required — stands).
- **Confirmed still-open at 7/25:** `MESSAGING/README.md` header still said "NOT YET LIVE" against a live, proven cohort (§3.2's exact example) — **fixed 2026-07-25 this session** (Will-approved), see DISPOSITIONS row H1.

## Bigger-picture (proof-of-work narrative)

Two v2 additions sharpen Will's case-study pitch: **FRI superforecaster-parity** (if raw LLM forecasting commoditizes, the defensible edge is exactly the institutional layer this repo demonstrates — converts "unproven incremental value" from weakness to thesis statement) and **CIA co-workers convergence** (the agents-monitor / WALTER-triages / Will-decides doctrine predates the IC's public adoption of the same division, with a fuller audit trail — "convergent, not idiosyncratic").

## Standing guards adopted from the report

- §13 preservation list endorsed verbatim (preserve failures · no-action is output · no new top-level agents without a demonstrated gap · no dashboards over unreliable state · threshold-vs-mechanism survives any schema).
- §9.1 ACH corollary → note for DAEDALUS: if a competing-hypotheses-matrix proposal ever surfaces, the empirical literature says build more RED instead.
