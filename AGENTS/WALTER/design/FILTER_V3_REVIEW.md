# FILTER v3 Review — Empirical filter-health review

**Status:** review conducted **2026-07-04** (WALTER Full, holiday-weekend catch-up). This is the live filter-review doc; it supersedes `FILTER_V2_PLAN.md` (v2 COMPLETE 7/3 → archived to `design/history/`).
**Owner:** `FILTER_SPEC.md` owns the filter model; this doc is the periodic empirical review that feeds it (Tuning-Rules discipline, FILTER_SPEC §"Tuning Rules").
**Trigger:** the last *empirical* filter review was the **Apr 11–20 window** (51 dispatches → FILTER_V2). **~390 dispatches have run since with no formal review** (BOARD now 442). The v2→v3 trigger (10+ dispatches OR 30 days) is long-passed. *(Note: v2's implementation debt — Segment D `confidence_note` — cleared 7/3, but that was implementation, not a review.)*
**Scope:** empirical review of `route_log.tsv` + `kill_log.tsv` over a representative recent window, checking (1) false-positive kills, (2) routing/precedence calibration, (3) emerged informal practice worth codifying, (4) filter-architecture gaps.

---

## Diagnostic Headline

**The v1/v2 filter is structurally healthy. No architecture change needed. BALANCED posture holds.**

Empirical review of the recent window — **last ~30 dispatches (SIG-W-20260628-011 → 20260704-008)** + **last 25 kills (6/28–7/4)**:

- **Zero false-positive kills.** Every kill in the window has a clean, correct, auditable reason (evidence below). Nothing was killed that should have routed.
- **Routing well-calibrated.** Dispatches land on the correct domain owner; RED is auto-cc'd on essentially every dispatch per the 97%-routing-target design; precedence is calibrated (no FLASH/IMMEDIATE was warranted in a calm-tape / markets-closed window, and none was forced).
- **Confidence calibrated.** Scores span 0.55–0.90; CORRECTED-FRAMING items land 0.72–0.85; the 0.30 floor was not spuriously tripped.

This mirrors the v2 diagnostic ("zero obvious false positives, routes calibrated, no need to rewrite the filter architecture") — **the filter has held its calibration across ~10× the dispatch volume** (51 → ~440). The architecture is not the constraint.

### Empirical kill audit (last 25, 6/28–7/4) — all correct

| Kill class (emerged) | Count (approx) | Representative | Verdict |
|---|---|---|---|
| **stale-to-owner** (Novelty — owner holds it, often *more* currently) | ~14 | crack-spread ×4 + Kemp SPR (BRENT ahead+contrary); USD/JPY 40yr-low ×2 (SAM live mark); CC-90+DQ 13.1% ×2 (CARL w/ NY-Fed context); NFP-revisions + LFPR (LABOR/MARCO); API-6/30 (superseded by EIA); Broken-Moats PC-insurer (SHADE docket-depth) | correct |
| **advocacy / opinion / TA-narrative, no observable datum** | ~5 | Gundlach coupon-cut op-ed; Gordon-Johnson Fed-MBS opinion; gold-dips-before-crash advocacy; JustDario JPY-oil TA; $USO overnight-manipulation TA | correct |
| **immaterial** (Relevance) | ~2 | Merrill $7.5M SAR fine ×2 | correct |
| **off-topic/accidental** (Relevance) | 1 | cannabis/sperm-count health query (flagged Will) | correct |
| **stale recirculation** (Novelty — real-but-OLD event re-surfaced) | 1 | Metropolitan Capital "first US bank failure of 2026" = a **5-mo-stale Feb event** re-surfaced by the intake-lane keyword matcher | correct |
| **re-send dedup** (Novelty) | ~2 batches | 7/4 batch-2 (10/10 dups) + batch-3 (9/10 dups) | correct |

---

## What v3 addresses — 4 emerged practices worth codifying

Per the v2 pattern, the review's value is **codifying informal practice that's emerged in use.** Four candidates, ranked by recurrence × leverage:

### ① Image-batch dedup by file-id-stem → content-grep  —  **RECURRED (6/28 + 7/4) · recommend CODIFY**

Multi-image Will-Telegram drops are now the **dominant intake modality**, and later batches in a stream are heavily duplicative (6/28: batch-4 was 8/10 re-sends; 7/4: batch-2 = 10/10, batch-3 = 9/10). Two mechanics, used in sequence:
1. **Fast path — file-id stem.** On a re-send, Telegram often re-uses the same `file_id` stem → compare stems against the prior batch; identical stem = exact re-send → dedup-skip with one audit note, **no re-OCR / re-grep** (6/28 batch-4 caught this way).
2. **Fallback — content-grep.** A re-send can arrive with a *fresh* stem (7/4 batch-2: "NEW file-id stem but content identical") → when stems differ, content-grep each image against BOARD INDEX + kill_log before processing.

**Proposed edit — CHECKLIST Phase 1b (append a note; → v0.25):**
> **Multi-image batch dedup (fast path).** On a multi-image drop, before running Phase-1 gates per image: (a) compare each image's Telegram `file_id` stem against the prior batch — an identical stem = exact re-send → dedup-skip with one audit note (no re-OCR); (b) if stems differ, a re-send can still carry a *fresh* stem, so content-grep each image against BOARD INDEX + `kill_log` before processing. Log a consolidated `re-send dedup` kill row for a fully-duplicative batch (log_reconcile counts unique signal_ids, so a dedup row is free). *(Recurred 6/28 batch-4, 7/4 batches 2–3.)*

### ② Three emergent kill sub-classes — name them in FILTER_SPEC Gate 1  —  **RECURRING · recommend CODIFY**

The kill-gate taxonomy (Novelty / Relevance) is correct, but the *rich free-text qualifiers* in the kill log reveal 3 stable sub-patterns the spec doesn't name. Naming them makes the discipline explicit + trains future-WALTER:

- **(a) stale-to-owner** *(Novelty sub-class)* — the domain owner already holds the datum, often *more currently*. **The dominant kill class now (~55–60% of the window).** Correct behavior (defers to domain owners per `board_lags_agents`), but it depends on a domain-STATUS check to confirm owner-ahead → worth naming so the check is explicit, not implicit.
- **(b) advocacy / opinion / TA-narrative with no observable datum** *(Relevance/Novelty hybrid)* — op-eds, motivated-reasoning long-form, chart-divergence "warnings." **NO-ROUTE the narrative; route the eventual ACTUAL policy-action / datapoint if one appears.** (Gundlach, Gordon-Johnson, gold-dips advocacy, JustDario TA — all 7/2–7/4.) This is the deployed form of MEMORY findings `[2026-06-21] advocacy→extract-falsifiable-core` + the Schiff/Gundlach "route an ACTUAL policy action" kill-note.
- **(c) stale recirculation** *(Novelty sub-class)* — a real-but-OLD event re-surfaced as fresh; **date-check before killing/routing.** **NEWLY AMPLIFIED by the RESEARCH-INTAKE lane:** its `newssweep` onset-dedup flags a new *headline-appearance*, not event-age, so a months-old event can surface as a "NEW" breach (the Metropolitan Capital 5-mo-stale kill 7/4 is the prototype). This is a **new systematic intake risk** the lane introduced — worth an explicit spec note now that the lane is live.

**Proposed edit — FILTER_SPEC Gate 1 (add a short "Recognized kill sub-patterns" subsection; → v0.6).** Draft text ready; does not change gate logic, only names the emerged sub-classes + the date-check discipline for the intake lane.

### ③ Distressed-CRE $ figure — origination vs current-UPB vs realized-loss  —  **1 instance, but systematic · DECIDE**

A headline `$` on a defaulted / foreclosed / deed-in-lieu / REO credit is routinely the **origination** amount, not the current UPB or the realized loss — trade-press reposts conflate them. OZK Seattle 7/4: the "$196M default" was the **2022 origination**; current exposure ≈ **$126M** (routing the origination overstates the loss ~55%). Generalizes MEMORY `[[finding_number_carries_threshold_unit_source]]` to distressed-CRE figures.

**Status:** *first explicit instance* (the "promote if it recurs" gate has fired once), but the pattern is **systematic** — this book has four CRE agents (REGINALD/CREED/CORAL/OZK) and the conflation is standard in the source material. **Decision for Will:** codify now as a CHECKLIST Phase 1.5 figure-verify sub-bullet, OR watch-for-a-2nd-instance. WALTER lean: **codify now** (high leverage, cheap, clearly systematic).

### ④ HOLD — single instance, re-evaluate next review

- **trigger-vs-structural-amplifier attribution** [7/4 PJM: heat=trigger, AI/data-center=amplifier] — clean, but 1 instance.
- **fold-primary-arrives-later verdict-upgrade** [6/28 NWS heat SIG-011: SKIP-VERIFY 0.65 → OFFICIAL-PRIMARY 0.85] — clean, but 1 instance.

Both are already deployed correctly; hold codification until a 2nd instance confirms them as stable practice (avoids over-fitting the spec to one-offs).

---

## Also surfaced — review-cadence recalibration (meta)

The empirical-review trigger (**10+ dispatches OR 30 days**) is now mis-scaled: at 442 dispatches it would fire almost continuously, and in practice the cadence stretched from 30 days to **~2.5 months** (Apr → Jul). Same class as the `network_uncertainty_peak` recalibration watch (MEMORY `[2026-05-11]`). **Recommend resetting the v3→v4 trigger to: a quarterly pulse (~Oct 4) OR the next filter-behavior surprise (first real FP kill / a mis-route / a new intake modality), whichever first** — a surprise-driven review beats a volume-counter that never gets read.

---

## Landed / pending

**Landed this review (all Will-greenlit 2026-07-04):**
- Registry-lag refresh (CREED, DAEDALUS).
- This review doc; `FILTER_V2_PLAN.md` archived → `design/history/`; STATE §1 + CLAUDE.md refs repointed.
- **① image-batch dedup → CHECKLIST Phase 1b (v0.25)** — LANDED.
- **② 3 kill sub-classes → FILTER_SPEC Gate 1 (v0.6)** — LANDED.
- **③ distressed-CRE figure-verify → CHECKLIST Phase 1.5 (v0.25)** — LANDED (Will greenlit codify-now; flagged as 1-instance-but-systematic → re-check for a 2nd at v4).
- **meta: review-cadence reset to quarterly-or-surprise** — LANDED in FILTER_SPEC v0.6 Tuning Rules.

**Next review (v4):** ~2026-10-04 OR next filter-behavior surprise, whichever first.

---

## Log

| Date | Action |
|------|--------|
| 2026-07-04 | v3 review conducted (WALTER Full, holiday catch-up). Empirical audit of last ~30 dispatches + 25 kills = zero FP kills, routes/precedence/confidence calibrated, BALANCED holds. 4 emerged practices identified (2 codify / 1 decide / 1 hold-for-2nd) + review-cadence recalibration. FILTER_V2_PLAN archived. Spec edits staged for Will greenlight. |
