# NEXUS Self-Audit — Machinery, Not Worldview
**Date:** 2026-06-06
**Scope:** Audit NEXUS's own files, spawn protocol, frameworks, and lifecycle hygiene — independent of refreshing any domain-agent inputs.
**Anchor:** Last write 2026-05-21 (16 days stale). Will: "fix NEXUS itself before worrying about the other agents."

---

## DOCUMENT INVENTORY

| File | Lines | Last write | Role | Status |
|---|---:|---|---|---|
| `CLAUDE.md` | 181 | (unknown) | Identity + spawn + frameworks | Drift vs reality (see §1) |
| `STATUS.md` | 137 | 5/21 | Active convergence matrix, tensions, thresholds, narrative gap | 16d stale; structural bloat |
| `SIGNALS.md` | 61 | 5/21 | Live unresolved cross-agent signals | Broken — duplicates STATUS, misses actually-live signals (see §2) |
| `CONFIRMED.md` | 24 | March | Thesis scorecard (convergence-level) | Neglected since March; April→May convergences not posted |
| `PREDICTIONS_MONITOR.md` | 75 | 4/4 | Falsifiable prediction tracker | 9 weeks stale; ~15+ items unresolved past trigger dates |
| `LAST_COMPLETION.md` | 59 | 5/21 | Last-run output + files-touched | Current; duplicated by STATUS "Last Run Output" section |
| `inbox/` | 2 unprocessed | 5/14, 5/22 | Incoming signals | Stalled; integration broken |
| `outbox/` | 1 (not moved to delivered) | 5/21 | Outgoing to PROME | OK |
| `archive/` | 2 STATUS snapshots | — | Historical | OK |
| `signals_archive/` | 2 SIGNALS snapshots | — | Historical | OK |
| `research/` | 3 March docs | — | Deep-dive synthesis | Context-only |
| `recon/` | 2 docs (5/21, 3/15) | — | Audit/recon | OK |

---

## §1 SPAWN PROTOCOL DRIFT (CLAUDE.md)

**HIGH IMPACT — changes what NEXUS does at boot.**

| # | Drift | Reality |
|---|---|---|
| 1 | Step 4 numbered twice (typo) — two `4.` lines | Should be 4 (SIGNALS) then 5 (agent headers); steps 5-7 shift to 6-8 |
| 2 | "Write to `OUTBOX.md`" | Actual is `outbox/` directory with dated files (`YYYY-MM-DD_to-TARGET_topic.md`) |
| 3 | "WHAT YOU READ" table lists `INBOX.md` (file) | Actual is `inbox/` (directory of dated signal files) |
| 4 | "WHAT YOU READ" table lists `PROME/PREDICTIONS_MONITOR.md` | File lives at `AGENTS/NEXUS/PREDICTIONS_MONITOR.md` (NEXUS-owned, per "WHAT YOU OWN" table — internal contradiction) |
| 5 | No closeout-as-write-back-tail framing | Per memory [[finding_closeout_as_writeback_tail]]: spawn protocol should explicitly end with: write STATUS, update LAST_COMPLETION, move processed inbox files to `inbox/processed/`, move delivered outbox to `outbox/delivered/`, archive consumed signals to `signals_archive/` |
| 6 | No live-event override | Per memory [[finding_boot_protocol_live_event_override]]: live event should short-circuit closeout/integration steps, do minimum-viable synthesis first |
| 7 | No predictions-resolve scan at boot | Per memory [[finding_boot_predictions_scan]]: first run after gap should scan PREDICTIONS_MONITOR for trigger dates passed; would catch the ~15 stale Apr items currently rotting |
| 8 | "WHEN TO RUN" assumes daily AM/EOD check-in rounds via PROME | PROME degraded per memory [[project_openclaw_prome_degraded]]; this trigger cadence is dead |
| 9 | "You receive from: ALL agents via HERMES" | Messaging system being overhauled per memory [[project_messaging_overhaul]]; HERMES routing unreliable |
| 10 | OUTPUT FORMAT prescribes CONVERGENCE/CONTRADICTION report templates | Never used — STATUS uses table format. Template is dead text. Either use it or delete it. |

---

## §2 SIGNALS.md IS BROKEN

**HIGH IMPACT — affects what NEXUS considers "live."**

**Design intent (per CLAUDE.md):** "Live unresolved cross-agent signals only. If absorbed into STATUS.md, keep only a short reference here until next pass. If still developing, keep active."

**Reality:** SIGNALS.md currently contains SIG-M01 through SIG-M08, each of which is a 1:1 restatement of STATUS matrix rows M-01..M-07 plus the FORGE no-trade-rails guardrail. The mapping column literally says "M-01 / T-01" etc. **It is a second copy of the matrix, not a tracker of unresolved signals.**

Meanwhile, the **actually-unintegrated** signals are:
- HAWK 5/22 partial-thaw reframe (inbox, not yet in matrix — should update M-06)
- Gamma surge 5/14 (inbox, partly aligned to M-04 but never logged)
- BRENT 5/15 Path B Trigger #3 CFTC distribution (in `AGENTS/SIGNALS.md`, not absorbed)

**Fix direction:** Empty SIGNALS.md of duplicates. Keep ONLY signals waiting on next pass. The 3 above are candidates.

---

## §3 CONFIRMED.md NEGLECTED

**MEDIUM IMPACT — thesis scorecard integrity.**

Last update March 2026. PREDICTIONS_MONITOR shows multiple April confirmations that never made it into CONFIRMED:
- PRED-25 HAWK Scenario D ≥80% → confirmed at 92% (4/1)
- PRED-13 Iran "talks" rally = bull trap (3/23)
- PRED-08 NFP Feb negative (3/6)
- PRED-23 SOFR Q1 spike partial-confirmed
- C-34 Gulf Surplus Recycling Collapse (March, mentioned in CONFIRMED merged-dedup row but no entry)

Either CONFIRMED.md is the live scorecard (then it's missing entries) or PREDICTIONS_MONITOR is (then CONFIRMED is redundant). Currently both are stale and unclear.

**Question for Will:** Do we need both? My read: PREDICTIONS_MONITOR is *prediction-level* (granular, falsifiable), CONFIRMED is *convergence-level* (thesis-track). Different unit. But the line-drawing isn't enforced and both rot. Consider merging or assigning one as canonical.

---

## §4 PREDICTIONS_MONITOR STALE + UNDISCIPLINED

**HIGH IMPACT — predictions are NEXUS's contract with reality.**

**Staleness:** 47 entries, last touch 4/4. Items with trigger dates past:
- PRED-21 (CC DQ spike ~May) — past, status unupdated
- PRED-22 (BOJ May 1 hike) — past
- PRED-26 (RED bear conf) — 6+ weeks unmarked
- PRED-27 (ARCC/OBDC downgrades) — 48-72hr catalyst from 4/4
- PRED-28 (PCE Mar 28 hot) — past
- PRED-31 (FL UI Wave 2 Apr 26) — past
- PRED-33 (Iran pause Apr 6) — past
- PRED-42 (Belgium TIC Jan) — past
- PRED-44 (Q1 bank earnings Apr 20-29) — past
- PRED-46 (BOJ Apr 23-24 hike) — past
- PRED-47 (Iran pause expiry Apr 6) — past

**Discipline gaps (recent memory not yet absorbed):**
- [[finding_threshold_vs_mechanism]]: predictions don't separate "threshold sticks" from "mechanism intact" — a fired threshold on wrong mechanism still resolves TRUE-in-letter, FALSE-in-spirit. Recent CARL examples (SAM-25/26) validate this twice.
- [[feedback_single_month_subcomponent_skepticism]]: single-month sub-component moves (1-print) shouldn't load-bear predictions; require 2nd-print.
- [[finding_catalyst_vs_consequence_conflation]]: P(consequence) = P(catalyst fires) × P(consequence | catalyst). PRED-29 (Yanbu→Brent $145-165) inflates if transcribed as consequence-prob without the conditional.

**Fix direction:** Resolve all past-trigger items honestly (HIT / MISS / TRUE-in-letter-FALSE-in-spirit). Add discipline rubric at top of file. Prune to active/pending forward predictions only.

---

## §5 STATUS.md STRUCTURAL BLOAT

**LOW-MEDIUM IMPACT — cosmetic, but affects future-NEXUS clarity at boot.**

| Section | Lines | Verdict |
|---|---:|---|
| Header + Executive Read | ~20 | Earns |
| Active Convergence Matrix M-01..M-07 | ~10 | Earns |
| Contradictions/Tensions T-01..T-07 | ~12 | Earns |
| Threshold Proximity | ~14 | Earns; could split breached vs proximate visually |
| Narrative Gap | ~5 | Earns |
| Next Evidence Checklist | ~15 | Earns but should be tagged stale (June 9-11 auctions still ahead, R11 5/28-6/02 window passed) |
| **STALE/RETIRED APR 4 ITEMS** | ~12 | **Dead weight.** One-time janitorial from 5/21 reset. Belongs in recon, not STATUS. |
| **DATA GAPS BEFORE NEXT FULL NEXUS PASS** | ~5 | **Pass-specific.** Belongs in LAST_COMPLETION. |
| **LAST RUN OUTPUT** | ~6 | **Duplicates** LAST_COMPLETION.md. Pointer suffices. |

Removing the 3 bottom sections nets ~23 lines, gives STATUS more room for live matrix detail. Per OUTPUT RULES "Max 200 lines" — we're at 137 not at cap, but signal density matters more than space.

---

## §6 FRAMEWORKS — EARNED VS DEAD

| Framework | Used in STATUS? | Verdict |
|---|---|---|
| Convergence Detection (3/4/5+ agents) | Yes — M-01..M-07 | Earns |
| Contradiction Scoring (surface/real/temporal) | Partial — tensions table doesn't tag surface/real/temporal | Earns but taxonomy invisible |
| Transmission Chain Validation (LABOR→CARL→REGINALD) | **No live row** | Defined but not surfaced. Should appear as STATUS dashboard row with link-by-link status |
| Threshold Proximity Matrix | Yes — 12-row table | Earns |
| Narrative Gap Analysis | Yes | Earns but missing market-verdict counter-signal anchor per [[finding_thesis_loadbearing_sweep_scope]] |

**Missing frameworks** (memory entries not yet absorbed):
- Catalyst-vs-consequence conditional discipline
- Single-month skepticism on sub-components
- Threshold-vs-mechanism split on falsifiable claims
- Market-verdict counter-signal as required row in narrative gap

---

## §7 INBOX/OUTBOX HYGIENE

- `inbox/` has 2 unprocessed files (5/14 gamma, 5/22 HAWK). Last processed batch: April. Per memory [[project_messaging_overhaul]], partly expected — but at minimum, current run should process or explicitly defer.
- `outbox/2026-05-21_to-PROME_stage2late_divergence_reset.md` not moved to `outbox/delivered/`. Implies the closeout step was skipped on 5/21. Pattern would repeat without a write-back tail.

---

## FINDINGS RANKED BY BEHAVIORAL IMPACT

**Per memory [[feedback_audit_behavioral_ranking]]: rank by what makes NEXUS DO something different, not by line-count.**

### Tier 1 — Changes spawn behavior
1. **Spawn protocol drift** (§1, items 1-10). Fix typos, file-path drift, add write-back tail, live-event override, predictions-scan-at-boot, catalyst-docket scan. Net: ~30 line CLAUDE.md edit.
2. **SIGNALS.md broken** (§2). Empty duplicates. Repopulate with the 3 actually-unintegrated signals.
3. **PREDICTIONS_MONITOR stale + undisciplined** (§4). Resolve past-trigger items. Add discipline rubric (threshold-vs-mechanism, single-month skepticism, catalyst-vs-consequence).

### Tier 2 — Changes synthesis output
4. **Transmission chain not surfaced** (§6). Add live STATUS row.
5. **Narrative gap missing market-verdict counter-signal** (§6). Add as required column.
6. **CONFIRMED.md missing April→May entries** (§3). Either populate or declare PREDICTIONS_MONITOR canonical and step CONFIRMED down to summary.

### Tier 3 — Cosmetic / line-trim
7. STATUS bloat removal (§5): drop "STALE/RETIRED APR 4," "DATA GAPS," "LAST RUN OUTPUT" sections.
8. Threshold table: split breached vs proximate visually.
9. CLAUDE.md: delete unused CONVERGENCE/CONTRADICTION report templates OR enforce them.

### Tier 4 — Worldview (after machinery sound)
10. Refresh all 11 agent-header inputs to current data.
11. Re-grade Break/Grind/Divergence split (currently 25/35/40 from 5/21).
12. Process inbox signals into matrix.

---

## RECOMMENDED ORDER OF OPERATIONS

Per memory [[feedback_front_load_planning]]: surface decisions first, execute mechanically second.

**Phase A — Spawn protocol fix (one CLAUDE.md edit, ~10min):**
- Renumber steps, fix INBOX/OUTBOX path drift, add write-back tail, predictions-scan, live-event override.

**Phase B — Lifecycle housekeeping (mechanical, ~15min):**
- Empty SIGNALS.md of duplicates; populate with 3 unintegrated signals.
- Resolve all past-trigger PREDICTIONS items honestly.
- Move 5/21 outbox file to `outbox/delivered/`.
- Move processed inbox files to `inbox/processed/` after integration.

**Phase C — STATUS structural cleanup (~10min):**
- Drop 3 bloat sections.
- Add transmission chain row.
- Add market-verdict counter-signal anchor to narrative gap.

**Phase D — Frameworks rubric (CLAUDE.md edit, ~10min):**
- Codify threshold-vs-mechanism, single-month skepticism, catalyst-vs-consequence as synthesis disciplines.
- Decide CONFIRMED vs PREDICTIONS canonicalization.

**Phase E — Worldview refresh (separate session, larger):**
- Read 11 agent headers, re-grade matrix, integrate 3 inbox signals, ship updated STATUS.

A-D = NEXUS machinery sound. E = NEXUS worldview current. Will's instinct was right that A-D blocks E from being durable.

---

## OPEN DECISIONS FOR WILL

1. **CONFIRMED.md vs PREDICTIONS_MONITOR.md** — keep both with clear unit-distinction (convergence-level vs prediction-level), merge into one, or declare PREDICTIONS canonical and step CONFIRMED down to a summary table?
2. **WHEN TO RUN** — PROME-driven daily cadence is dead. New trigger model: on Will request, on inbox arrival via WALTER, on PROME revival, or pre-event only?
3. **HERMES dependency** — "You receive from ALL agents via HERMES" is stale. Replace with current routing reality (inbox + AGENTS/SIGNALS.md scan only, until messaging overhaul lands)?
4. **OUTPUT FORMAT templates** — keep the CONVERGENCE/CONTRADICTION report templates and enforce them, or delete (current behavior uses tables)?

Once these are answered, A-D can be executed in one batched session.
