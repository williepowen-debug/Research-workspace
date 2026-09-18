# PROME — updated CATO review and action brief

Prepared September 18, 2026, at Will's request to update the review for PROME. **This supersedes the earlier action brief's priority/status summary, not its evidence or detailed A1–A7 acceptance conditions.** Prepared for Will to share, consistent with his earlier delivery preference; no peer message or inbox packet sent.

Review receipt: `ea3b65b5a`, confirmed pushed. Follow-up HEAD: `c7284ddeb`; all 13 inspected finding-related source files are unchanged from the review receipt, including live working bytes. Later BRENT archive/Friday-routine commits and active AEOLUS work are outside the reviewed perimeter. Do not assume owner inactivity or expand this into a full fleet audit.

## PROME: what to do first

1. **Have SAM reconcile the oil-price interpretation and correct its proposed benchmark before using those conclusions or implementing the plan** (R1–R3 below).
2. **Keep the earlier high-priority findings visible:** BOND's success-rate population before WQ-157 decision use; its publication-cutoff/vintage defects before BND-26 finalization; the shared FRED lesson and its consumers (A1–A4).
3. **Disposition the bounded control failures at their existing owners** (R4–R6, A5–A7). Use WQ-263 for the existing hook-convergence choice; this handoff does not authorize another unbounded series of repair/read rounds or alter the hook policy.

Use existing task records where available. Route domain corrections to their owners, preserve active work, and use existing approval/spawn boundaries. This brief requests disposition and evidence; it does not authorize new capital decisions, changed thresholds, a fleet rollout, or taking over another active desk's files.

## New findings: owners, exact asks and closure evidence

### R1 · HIGH · SAM — continuous Brent roll mistaken for an economic move

**Where:** `AGENTS/SAM/NEXUS_BRIEF.md:11`; `STATUS.md:49,84,89`. Comparison evidence: TERRY's `setups/BRENT_refiner-distillate-strong-leg_2026-08-27.md`, matched-contract block at lines 491–504 of the reviewed revision.

**Ask:** reconcile the claim “Brent −7.5% in three sessions despite Petroline shut.” SAM uses continuous quotes; TERRY identifies a November→December discontinuity on that series the same day. Reconstruct the interval on one named contract or a documented adjusted series. Correct the inference in NEXUS_BRIEF and affected live consumers, not just the quote label.

**Close only when:** timestamped prices, contract identities and the consistent-basis comparison are shown, with the resulting interpretation. Until then, the economic-direction inference is unestablished. **Do not replace it with “the entire decline was a roll” or “crude stayed up all day”: CATO did not establish either.** SAM withheld a fresh registered oil-in-yen count; no wrong gate firing was demonstrated.

### R2 · HIGH · SAM — diagnostic arithmetic passes; causal rejection does not

**Where:** `research/outputs/2026-09-18_oil-in-yen-rebenchmark-plan.md`, §§0–3 (`2f674c8c4`).

**Ask:** withdraw ELIMINATED/REJECTED for the lag-window hypothesis. A 0.069 correlation on 16 pairs does not rule out a material timing contribution. Keep the reproducible figures: n=17 monthly rows; high-ME residual 7.7314%/$5.4538, n=13; low-ME 17.1488%/$16.15, n=4; wedge-level correlation 0.83538. The last correlation does not identify proportional freight/insurance costs when price, war and slate regimes coincide.

**Close only when:** the plan distinguishes measured residuals from attributed causes; timing remains unresolved unless an adequately specified test resolves it; plausible cargo/pricing windows and uncertainty are addressed before changing the diagnostic band. A narrower honest diagnostic is a valid disposition—no new research programme is required just to retract an overclaim. Gate rescaling remains separately governed.

### R3 · MEDIUM · SAM — proposed Dubai identity ignores producer effective dates

**Where:** same plan, Phase 2.

**Ask:** correct the blanket assertion that the listed Middle East grades all price off Dubai/Oman over the historical sample. ADNOC announced on July 31 that its Murban-based method transitions to Dubai **November 1, 2026**, including Murban and Das. [Producer announcement](https://adnoc.ae/en/news-and-media/press-releases/2026/adnoc-announces-update-to-its-crude-pricing-methodology).

**Close only when:** the plan maps grade, delivery/loading month, destination and applicable pricing convention, including the November transition. If a single Dubai series is a proxy, state and test the approximation. This is a proposed-method defect, not an implemented gate change.

### R4 · MEDIUM · PROME — plain echo fixed; wrapped prose still falsely blocked

**Where:** `PROME/tools/hooks/commit_subject_guard.py`, `_commit_arg_lists`.

**Ask:** disposition these new v6 counterexamples with a 101-character literal message: `command -v git commit -m ...`; `env printf %s git commit -m ...`; `timeout 1 echo git commit -m ...`. All return BLOCK, although none executes Git.

**Close only when:** supported wrappers resolve to the actual child command, or uncertain cases produce the approved declared UNKNOWN behavior; lookup/printing cases pass without blocking; real short/long commits remain correctly classified. Preserve the fixed plain-echo regression. **A8 is closed narrowly; R4 is a new neighboring defect.** Keep WQ-263's policy choice distinct from implementation repairs; retain applicable convergence limits.

### R5 · MEDIUM · PROME — invalid calendar dates and terminal-state disagreement

**Where:** `willq_view.parse_open`, `decision_deck.parse_open`, `will_brief.parse_actions`, `prome_gate.check_will_queue`.

**Ask:** validate actual dates, not just YYYY-MM-DD-shaped strings. `2026-02-30` is accepted by three consumers and raises ValueError in the gate's queue check. Use the existing per-row failure channels. Also align terminal vocabulary: plain `CLOSED old item` disappears from willq_view but stays visible in Deck/brief; this is the lower-priority parity subitem.

**Close only when:** invalid month/day and leap-day fixtures are handled by name, neighboring valid asks remain usable under each surface's intended policy, and terminal-row visibility agrees. No malformed live row or wrong current count was observed; these are reproducible failure fixtures, not proof of a live outage.

### R6 · MEDIUM · BRENT — broken vintage history permits an ordinary successful grade

**Where:** `AGENTS/BRENT/scripts/cot_grade.py`, `read_ledger` / `main`.

**Ask:** separate current-print grading from revision-watch availability. A healthy historical shorts value of 107,229 versus fixture live 107,230 returns rc 4. Replacing that stored value with `BAD` makes the loader ignore the baseline and returns rc 0. A missing ledger likewise becomes empty history.

**Close only when:** corrupt/unavailable history is declared and cannot silently become a new baseline; deliberate initial seeding is distinguishable; changed/unchanged, malformed, duplicate and missing-record cases are tested. No actual corrupted ledger or missed CFTC revision was found. Current-file comparison is not a complete audit of older archive revisions.

## Earlier findings: retained, not duplicated

The [original detailed brief](2026-09-18_1102_prome-action-brief.md) retains exact surfaces, original evidence and acceptance cases. Use it for these items:

| ID | Owner | Required disposition now |
|---|---|---|
| A1 HIGH | WALTER / LIQUID; PROME coordinates shared consumers | Withdraw the automatic “derived FRED cell newer than component pages = unsupported” inference; retain actual observation-date alignment; reconcile shared memory and affected consumers. Source unchanged. |
| A2 HIGH | BOND; PROME checks WQ-157 summary | Separate all I-prime fires from the 68% subgroup. Verify actual numerators/denominators before publishing the implied 23/52 = 44.2%. Do not change a trade condition on this correction. Source unchanged. |
| A3 HIGH | BOND | Respect the September 30, 17:00 ET publication cutoff before finalizing unresolved BND-26 outcomes; preserve the registered observation window and grading branches. Source unchanged. |
| A4 MEDIUM | BOND | Establish first-publication evidence or withhold that certification; today's revised CSV does not establish the original vintage. Source unchanged. |
| A5 MEDIUM | DAEDALUS | Normal logging must not invalidate its own newly written receipt. Runner unchanged. |
| A6 MEDIUM | DAEDALUS | Fingerprint the actual checked dependencies, including external-owner and during-check changes. Runner unchanged. |
| A7 MEDIUM | DAEDALUS | Preserve unexpected child failures and native return codes as UNKNOWN, not CLEAN. Runner unchanged. |
| A8 | PROME | Original plain echo counterexample now passes; CLOSED narrowly. Track R4 separately. |
| A9 | CATO | Recovery provenance correction remains CLOSED. No repeat recovery. |

Unchanged source is evidence that the recorded defect remains, not evidence that an owner received and ignored an assignment. No owner acknowledgment of this updated brief is claimed.

## What passed — preserve these gains

Queue parity 26/26; renderer 32/32; subject hook 76/76; pipeline hook 36/36; live SCRATCH queue projection agreed at review. TERRY records one VLO share filled at $412 and two staged with account/time unknown; BROCK records the public-silence limit and related-fund counting rule. SAM's descriptive calculations reproduce. These checks do not close the new counterexamples or certify every domain source.

## Return to Will

For each A/R identifier above, return one disposition: **fixed and verified**, **open with named next step**, **deferred with reason and existing authority**, or **disputed with contrary evidence**. Include owner, exact repair revision, test/evidence, residual limitations and affected-consumer disposition where relevant. A packet sent is not a repaired source; implemented, tested and independently verified remain separate states.

Recheck current revisions before acting. Both CATO probe scripts intentionally load historical Git revisions and assert historical defects: **their exit 0 is not repair acceptance.** Adapt equivalent cases to the new candidate. Full reasoning and limits: [afternoon review](2026-09-18_1354_progress-review.md), [probes](2026-09-18_1354_progress-review-probe.py), [results](2026-09-18_1354_progress-review-probe.txt), and the original linked brief.

This update delivers instructions for disposition, not implementation. No owner files, queue rulings, settings or trades changed. CATO resumes by orienting and awaiting Will; further review/repair is not automatically assigned.
