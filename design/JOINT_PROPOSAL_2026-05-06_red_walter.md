# JOINT PROPOSAL — RED + WALTER — 2026-05-06

**2-way joint proposal — RED ↔ WALTER architectural alignment, May 6 2026.** Parallel to (not folded into) the in-progress 3-way joint proposal `JOINT_PROPOSAL_2026-05-05_walter_carl_brent.md` (pending CARL §1+§3a+§3c+§4 sections + Will sign-off on §2 stack — repo-root stitch deferred until CARL section file lands). RED's deltas are not part of the 3-way v0.8 stack — they are a separate Will-decision arc that has now closed end-to-end.

**Source LIAISON:** `AGENTS/RED/handoff_WALTER/LIAISON.md` Turns 1-6 (architectural thread converged Turn 5; Turn 6 close-loop, RED 21:00 UTC stamp). Convergence in 5 turns — same as BRENT, 2 turns faster than CARL pilot.

**Source side-files (both committed):**
- RED §1+§4+§6+§7 — `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` (RED commit `e6477450` 2026-05-06; 233 lines)
- WALTER §2+§3+§5 — `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` (WALTER commit `b09bb8de` 2026-05-06; 316 lines)

**Will-approval state:** **5-of-5 sign-off batch APPROVED end-to-end** (per RED Session 9 closeout commit `254f6e40`):
- §2 — FALSIFICATION_TRIGGERS WALTER-side eval logic ✅
- §3 — ROUTING_TABLE v0.7 delta + CHECKLIST delta ✅
- §4.3 — RED CLAUDE.md boot-step add ✅ (RED commit `b1ed0420`)
- §4.4 — RED MEMORY.md 97%-routing-target calibration entry ✅ (RED commit `b1ed0420`)
- §5 — v0.9 candidates `unanimity_state` ✅

**Implementation state (as of stitch 2026-05-06 PM):**
- WALTER §2 ledger + spawn-protocol step 6b + canonical-source rows + closeout step 12 daily-bifurcation-count extension — committed `dad58114`
- WALTER §3 ROUTING_TABLE v0.6→v0.7 + CHECKLIST v0.9→v0.10 (Phase 2 steps 5-7) — committed `dad58114`
- WALTER §5 V0_9_STACK.md tracker doc — committed `dad58114`
- RED §4.3 boot-step 1.5 b1-b4 (BOARD scan: ToC + RED-in-to: + cluster_mediating/prose-tagged + CORRECTED-FRAMING) — committed `b1ed0420`
- RED §4.4 MEMORY methodology note "verify empirical dispatch surface before claiming routing/data gap" — committed `b1ed0420`
- WALTER `network_uncertainty_peak` closeout flag (§5.5b lightweight ship) — committed `dad58114`; **first fire 2026-05-06 ~20:30 UTC** at bifurcation count 6

**Stitch provenance:** assembled by WALTER 2026-05-06 (post-batch-3 housekeeping) per LIAISON Turn 4 commitment. This file is the Will-surface unification artifact — read this single doc to see the full 2-way arc; the side-files remain in their respective agent trees as drafted.

**Section ownership map:**

| Section | Owner | Substance |
|---------|-------|-----------|
| §1 | RED | Domain framing + 97% routing-target finding + verdict distribution + bifurcation cluster sizing + operational state |
| §2 | WALTER | FALSIFICATION_TRIGGERS at-dispatch eval logic + WALTER-side fire-log ledger |
| §3 | WALTER | ROUTING_TABLE v0.7 By Tag/By Verdict + CHECKLIST Phase 2 steps 5-7 |
| §4 | RED | CHALLENGES.tsv schema bump + SCHEMA updates + RED CLAUDE.md boot-step + RED MEMORY entry |
| §5 | WALTER | v0.9 candidates: `unanimity_state` 4-value enum + sub-tag candidates `event_anchored: true` + `network_uncertainty_peak` closeout flag |
| §6 | RED | Decisions Q1-Q15 lock table |
| §7 | RED + WALTER | Calibration cycle 1 trigger conditions + WALTER close-loop self-tasks |
| §8 | WALTER | Coordination state (committed status; refreshed at stitch) |

---

## §1 — RED CONTEXT (RED draft)

### §1.1 — RED domain framing

RED is the network's **adversarial overlay** — not action-primary on any domain data. RED reads what other Tier-1 agents (CARL, REGINALD, BRENT, LIQUID, HAWK, SAM, HENRY, NEXUS, VIOLET, BROCK, MARCO, OZK) produce and stress-tests it. Mandate: **find what's WRONG with every thesis** through five canonical artifacts:

1. **Counter-evidence vector registry** — `AGENTS/RED/workbook/VX.tsv` (counter-signals with explicit bull/bear weights and flip conditions)
2. **Falsifiable predictions** — `AGENTS/RED/thesis/PREDICTIONS.tsv` (RED-NN with public scoring; resolved record 4 WRONG / 1 CORRECT / 9 ACTIVE as of 2026-05-06, Will-corrected from earlier overstatement)
3. **Pre-registered falsification triggers** — `AGENTS/RED/STATUS.md` FALSIFICATION CRITERIA + as of 2026-05-06 also `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` (8-col machine-readable)
4. **Formal challenges** — `AGENTS/RED/workbook/CHALLENGES.tsv` (CHG-RED-NNN with target agent, grade, status, KB/VX cross-links)
5. **Knowledge base** — `AGENTS/RED/workbook/KB.tsv` (KB-RED-NNN with Admiralty confidence digraph, Stale_By dates, methodology corrections)

RED owns no primary feed. Everything published derives from other agents' work + adversarial framework. Current thesis state: confidence 73% on bear thesis (was 70%, +3 after pre-committed Apr 18 trigger fired clean Apr 21 on WAL/OZK MISS/MUTED); thesis bifurcated paper-vs-structural; 6 competing hypotheses with explicit probabilities.

### §1.2 — The 97% routing-target finding (LIAISON Turn 2 empirical reframe)

RED Turn 1 framed the consumption gap as *"WALTER (BOARD): Mostly absent — see retrospective"*, identifying only 1 direct-route signal (SIG-W-20260411-001 HY OAS pierced, Apr 11). WALTER's Turn 2 empirical correction inverted the diagnosis:

| Recipient state for RED | Count | % |
|-------------------------|-------|---|
| RED in `to:` (action) line | **19** | 17% |
| RED in `info:` line | **100** | 91% |
| RED in to/info combined | **107** | **97%** |
| Total BOARD signals | 110 | — |

**RED has been a routing target on 97% of dispatches** since Apr 7. The 19 `to:` (action-primary) signals span falsification-counter, counter-evidence-cluster, cluster-bifurcation, and adversarial-counter-thesis routings — ~3.5 per week. The 100 info-cc signals deliver to a queue RED has not been draining.

**Architectural implication:** the gap is RED-side **consumption**, not WALTER-side **dispatch**. The fix is structured artifacts that let WALTER's existing high-volume routing become consumable by RED, not "more dispatch."

### §1.3 — Verify-research verdict distribution validation

WALTER's Turn 2 surfaced verdict-distribution data across 94 verified BOARD signals:

| Verdict | Count | % |
|---------|-------|---|
| CONFIRMED | 45 | 48% |
| **CORRECTED-FRAMING** | **44** | **47%** |
| INDETERMINATE | 3 | 3% |
| FALSE | 2 | 2% |

RED's prior MEMORY entry (`feedback_corrected_framing_calibration.md`) flagged CORRECTED-FRAMING as "the most-frequent verify verdict" — the 47% measurement validates this empirically and tightens it to "tied with CONFIRMED as modal." The recurring CORRECTED-FRAMING pattern is **direction-confirmed-specifics-imprecise** — the cell where RED's adversarial overlay adds the most value (preventing "directionally correct + magnitude inflated" from being reified into "thesis confirmed at full magnitude" downstream).

### §1.4 — Bifurcation cluster sizing

21-22 historical BOARD signals (19-20% of total dispatch volume) carry bifurcation / divergence / tape-vs-substance / paper-vs-structural language. RED produced a v0.1 classification of these signals at `AGENTS/RED/handoff_WALTER/bifurcation_classification_2026-05-06.tsv` (LIAISON Turn 5 deliverable, 22 rows):

| RED_class | Count | Pct |
|-----------|------:|----:|
| HENRY-tape | 8 | 36% |
| RED-structural | 9 | 41% |
| both | 5 | 23% |
| **Total** | **22** | — |

14 of 22 lean structural (RED-structural + both = 64%) — matches WALTER's Turn 2 hypothesis ("13-14 of 21 lean second way") within rounding. Three findings emerged from the classification pass:

- **VIOLET emerges as primary recipient on 3 vol-family signals** (419-002, 419-003, 419-007). VIOLET is distinct enough from HENRY in REGISTRY to be its own action-primary on vol-family signals. Implication: VIOLET must be in the agent-set explicitly when computing `unanimity_state` (§5 enum). *(Refinement post-WALTER §5.3: today's strict-staleness N is 6 not 9 — LIQUID 04-16, HENRY 04-17, HAWK 04-20 all >14d STALE and excluded per Q15. VIOLET 05-03 stays in. RED's Turn 5 framing of "N=9 including VIOLET" was pre-staleness-filter; WALTER §5.3 calculation is canonical.)*
- **All 5 "both" signals are event-anchored bifurcations** (HY OAS pierced, Iran SoH reclosure, Tuapse 2nd strike, Merz ally-rhetoric, Brent May 5 tape divergence). Pattern: bifurcation framing emerges when a discrete event or print contradicts an active narrative.
- **Apr 19 = 9 of 22 signals (41% in 1 day).** Iran cluster Apr 19 was the highest-density bifurcation-cluster moment in the 25-day arc (2 days pre-Apr 21 WAL/OZK earnings + ceasefire expiry). **Network observation:** dense-bifurcation-day correlates with high-stakes-decision-day. Pattern worth flagging in RED's CALENDAR catalyst tagging.

### §1.5 — Operational state after RED Turns 1-5

- 8/8 RED-asked questions resolved (Q1, Q3, Q4, Q6, Q7 pre-cosigned; Q2 deferred to v0.9; Q5 deferred to calibration cycle 1; Q8 priming-offer accepted via Q13).
- 4/4 WALTER-asked questions resolved (Q9 scope-b boot-step; Q10 narrow-precision cross-ref; Q11 RED-level ≥4 cutoff with bull-side fresh-active calibration; Q12 CORRECTED-FRAMING auto-cc).
- 3 close-loop questions resolved Turn 5 (Q13 TSV format locked; Q14 WALTER takes complete CHG backfill; Q15 fresh-active-only denominator).
- 3 deliverables shipped: FALSIFICATION_TRIGGERS.tsv (Q1), CHALLENGES.tsv BOARD_Refs col (Q7), bifurcation classification (Q8/Q13).
- 2 RED-side post-Will deliverables shipped post-approval: CLAUDE.md boot-step add (Q9, RED `b1ed0420`), MEMORY.md 97%-routing-target calibration entry (Q4.4, RED `b1ed0420`).
- Calibration cycle 1 clock starts **2026-05-06**, synced with BRENT's cycle 1 (ETA May 20-27).

**Convergence in 5 turns** — same as BRENT, 2 turns faster than CARL. The "open-with-substance Turn 1 + concede-on-diagnosis Turn 3 + ship-deliverables-in-Turn-3 + close-Turn-5" pattern compressed convergence vs CARL pilot. Saving as a finding for next-LIAISON channels (NEXUS, REGINALD, HENRY).

---

## §2 — FALSIFICATION_TRIGGERS.tsv WALTER-side eval logic (WALTER draft)

### §2.1 — File source and schema

**File:** `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` (RED owns; WALTER reads).
**Status:** v0.1 shipped LIAISON Turn 3 (commit `7f3e9ddf`) with 7 threshold-cross triggers. RED maintains; WALTER reads at boot + at every dispatch session.
**Schema:** 8 columns per LIAISON Turn 2 spec.

| Col | Name | Type | Purpose |
|-----|------|------|---------|
| 1 | trigger_id | String | RED-FT-NN (network-grep-able) |
| 2 | metric | String | Name of metric being watched (HY-OAS, BRENT-PAPER, INITIAL-CLAIMS, VIX, CCC-OAS, etc.) |
| 3 | threshold_op | Enum | `<` `>` `<=` `>=` `=` |
| 4 | threshold_value | Numeric | Threshold value |
| 5 | sustain_window | Integer | Number of trading sessions metric must hold across threshold to fire |
| 6 | action | Enum | `IMMEDIATE-FALSIFY` / `PATH-B-CONFIRM` / `ADD-POSITION` / `BRT-15-INVALID` / `LABOR-RE-ARM` / `MANAGED-DECLINE-CONFIRM` / `EARLY-STRESS` / `WATCH` / `DORMANT` (extensible per row.recipient_chain) |
| 7 | recipient_chain | String | "RED action / DOMAIN-AGENT info / Will" template |
| 8 | falsification_thesis_ref | String | Anchor to STATUS.md / CALENDAR.md row that defines the underlying thesis |

Each `action` value carries an implicit precedence (IMMEDIATE-FALSIFY → IMMEDIATE; PATH-B-CONFIRM → PRIORITY; ADD-POSITION / BRT-15-INVALID → IMMEDIATE; etc.) and an implicit dispatch-template (mechanism + falsification_thesis_ref).

### §2.2 — WALTER read loop (insert into spawn-protocol)

WALTER's spawn-protocol step 6 (Read `design/ROUTING_TABLE.md`) becomes step 6a; new step 6b inserted:

> **6b.** Read `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` (if present). Build in-memory trigger array; carry forward through dispatch phase.

At each dispatch session (whether triggered by Will-paged image batch / scheduled-scan / new BOARD signal arrival), WALTER runs a trigger-evaluation pass before final-dispatch:

1. **Stale-fire suppression check.** For each trigger, check `last_fired_date` (tracked in WALTER's parallel ledger — see §2.4). If trigger fired within prior `sustain_window` sessions, skip (prevents repeat-fire on persistent crosses).
2. **Live data pull.** For each non-suppressed trigger, query `FORGE/tools/market-data/fetch.py` for the metric. Use last close + intraday if available. Validate metric availability — if metric is unsupported by FORGE tooling, log gap to WALTER closeout SESSION LOG (treats as missed-coverage; not silent fail).
3. **Threshold evaluation.** Apply `threshold_op` against current value. If crossed, check sustain — pull last `sustain_window` sessions of the metric and validate metric stayed across threshold for the full window.
4. **Auto-dispatch.** If sustained-cross confirmed:
   - Generate signal with `signal_type: threshold-crossed` + `falsification_trigger: <RED-FT-NN>` body field
   - Precedence per `action` mapping (above)
   - Action recipient = first agent in `recipient_chain.action`
   - Info recipients = remaining recipients in chain
   - dispatch_note includes: trigger_id reference, current vs threshold value, sustain confirmation count, falsification_thesis_ref pointer
   - Cluster assignment: per metric — HY-OAS → BANK_COLLATERAL, BRENT-PAPER → IRAN_HORMUZ or HYDROCARBON_INFRA per current state, INITIAL-CLAIMS → CONSUMER_STAGFLATION, VIX → POSITIONING_VALUATION, CCC-OAS → BANK_COLLATERAL
5. **Approaching-threshold flagging.** If metric is within 5% of threshold (one-sided per `threshold_op`) but not crossed, no auto-fire; surface in WALTER closeout SESSION LOG as "near-trigger watch" so Will and RED can see proximity without dispatch.

### §2.3 — Out-of-scope for v1

- **Continuous live-tape polling.** WALTER is not always-on; trigger evaluation only happens at session-boot or explicit dispatch session. Real-time falsification-watch needs Prome (currently degraded) or a dedicated cron — not WALTER. Cost of v1 limitation: a threshold can cross overnight without firing until WALTER's next boot. Mitigation: most pre-registered falsification thresholds are slow-moving (sustain windows of 3-5 sessions); single-session miss is recoverable.
- **Multi-leg compound triggers.** No support for "HY-OAS <280 AND VIX <16 simultaneously" or other AND/OR composition. v1 is one-trigger-per-row. Compound triggers stay as separate rows that must each fire independently.
- **Event-type triggers** (per RED Turn 3 honest gap). Triggers like "WAL MI3 ≥25% on Q1 Call Report" / "BTFP 2.0 announced" / "bypass-pair second strike" don't fit threshold-cross schema. These stay in `AGENTS/RED/CALENDAR.md` FALSIFICATION WATCH for v1. WALTER manually checks CALENDAR.md at closeout (interim hold per LIAISON Turn 4).
- **Schema v2 with `trigger_type: THRESHOLD_CROSS | EVENT_PRINT | DISCRETE_ANNOUNCEMENT` discriminator.** Deferred until v1 operational + coverage gap data accumulates (RED preference; WALTER concurs).

### §2.4 — `last_fired_date` ledger (WALTER-side)

**Decision:** WALTER maintains a parallel ledger at `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv`. WALTER does NOT write back to `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` (preserves Critical Rule #2 — subagents own their files; RED owns the trigger registry).

**WALTER ledger schema (5 cols):**

| Col | Name | Type | Purpose |
|-----|------|------|---------|
| 1 | trigger_id | String | RED-FT-NN reference |
| 2 | fired_date | YYYY-MM-DD | When WALTER auto-dispatched on this trigger |
| 3 | metric_value_at_fire | Numeric | Recorded value that triggered |
| 4 | dispatched_signal_id | String | SIG-W-YYYYMMDD-NNN that was generated |
| 5 | sustain_confirmation | Integer | Number of sessions confirmed in sustain_window |

WALTER appends one row per fire; suppression check at next eval reads this ledger, looks up most recent `fired_date` per trigger_id, applies sustain_window suppression. RED can read the ledger at next boot to see fire history without WALTER touching RED's tree.

### §2.5 — Implementation timeline

- **v1 ship target:** within 1-2 WALTER sessions after Will sign-off on §2 (this proposal). Mechanical: (a) commit ledger TSV scaffold, (b) extend spawn-protocol step 6b in `AGENTS/WALTER/CLAUDE.md`, (c) add trigger-eval pass to dispatch workflow, (d) update SIGNAL_PROCESSING_CHECKLIST.md per §3 below.
- **First fire ETA:** unknown — depends on whether any of 7 RED-FT-NN triggers cross. HY-OAS at 285 (close to RED-FT-01 threshold of <280 for 3 sessions); could fire on next stress event. VIX at 18.19 (close to RED-FT-06 threshold of <16 for 5 sessions on bull-confirmation side). Most others further from current values.
- **Calibration cycle 1 trigger condition:** first auto-dispatch from this logic OR v0.8 lands OR CHG-RED-024 BRENT response, whichever first (per LIAISON Turn 4-5).

**Implementation status (post-Will-approval):** §2 scaffold + spawn-protocol step 6b + canonical-source rows + closeout step 12 daily-bifurcation-count extension all shipped 2026-05-06 PM (WALTER commit `dad58114`). FALSIFICATION_FIRED_LOG.tsv created header-only at `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv`. First at-dispatch eval pass ran 2026-05-06 PM; 0 fires; FIRED_LOG remains header-only. RED-FT-06 VIX <16×5 within 6.4% of threshold (just outside near-trigger 5% band); RED-FT-01 HY-OAS<280×3 needs primary OAS pull at next BOND refresh (HYG +0.33% / ^TNX -1.49% tape pattern suggests near-or-just-below-280 but unconfirmed).

### §2.6 — Sign-off ask ✅ APPROVED 2026-05-06

Will approved:
- Read-loop spec per §2.2 + dispatch logic per §2.4
- Out-of-scope items per §2.3 (continuous polling / compound triggers / event-type triggers all deferred)
- WALTER-side ledger at `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` with 5-col schema
- Implementation within 1-2 WALTER sessions post-sign-off

WALTER shipped scaffold + extended CLAUDE.md spawn-protocol in same-day closeout (commit `dad58114`).

---

## §3 — ROUTING_TABLE v0.7 delta + CHECKLIST delta (WALTER draft)

### §3.1 — ROUTING_TABLE current state

`AGENTS/WALTER/design/ROUTING_TABLE.md` v0.6 (committed 2026-05-06 as part of BRENT LIAISON closeout) added Iran-cluster CARL-info override + boundary-trigger threshold-cross sub-rule. v0.7 adds the RED-side delta from this LIAISON.

### §3.2 — v0.7 additions

**New section: "By Tag/By Verdict"** (insert after "By Signal Type" table, before "Safety Net Auto-Upgrades"):

| Tag/Verdict | Rule | De-dupe behavior |
|-------------|------|------------------|
| `cluster_mediating: true` (post-v0.8) | Add RED to info line unconditionally regardless of domain | If RED already in to/info, no add; stays at one occurrence |
| `verify_research_verdict: CORRECTED-FRAMING` (in dispatch_note) | Add RED to info line | If RED already in to/info, no add; stays at one occurrence |
| `falsification_trigger: <RED-FT-NN>` (auto-fired by WALTER from FALSIFICATION_TRIGGERS.tsv per §2) | Action = trigger.recipient_chain.action; Info = trigger.recipient_chain.info; precedence per trigger.action enum mapping | n/a — auto-generated signal, recipient chain pre-determined |

**De-dupe rule (general):** when multiple v0.7 rules fire on the same dispatch (e.g., signal is both `cluster_mediating: true` AND CORRECTED-FRAMING), RED is added once. Composition is informative-only; consumption mode (full-read for cluster_mediating vs body-skim for CORRECTED-FRAMING per RED Q9 b3/b4) is RED's choice at boot.

**Composition example:** SIG-W-20260505-012 (Brent intraday tape divergence vs Iran cluster confluence) — cluster_mediating + (would have been) CORRECTED-FRAMING if verdict run. Under v0.7 rules: RED auto-cc once; dispatch_note flags both rule-fires explicitly so RED knows the routing rationale; consumption mode = full-read (cluster_mediating dominates over body-skim).

### §3.3 — Interim period (pre-v0.8)

`cluster_mediating: true` is a v0.8 field (pending Will sign-off on JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2a). Until v0.8 lands, the prose-tagged equivalent is dispatch_note language carrying "paper-vs-structural" / "tape-vs-substance" / "bifurcation" / "divergence" tokens. Interim WALTER discipline:

> When dispatch_note contains paper-vs-structural / tape-vs-substance / bifurcation / divergence framing, ensure RED in info line.

This carries the v0.7 rule operationally before the field formally exists. RED's bifurcation classification TSV (Turn 5 deliverable) seeds the historical pass; new prose-tagged signals from this point forward apply the rule.

### §3.4 — CHECKLIST delta

`AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` Phase 2 (Routing) gets three additions, applied in order before final dispatch:

1. **Phase 2 step 5 add:** "If signal carries `cluster_mediating: true` (post-v0.8) OR prose-tagged paper-vs-structural / bifurcation / divergence in dispatch_note (interim), ensure RED in info line. Skip if RED already in to/info."
2. **Phase 2 step 6 add:** "If verify-research returned CORRECTED-FRAMING verdict, ensure RED in info line. Skip if RED already in to/info. Composes with step 5 — apply both, but RED appears once."
3. **Phase 2 step 7 add (auto-dispatch loop):** "Before final dispatch session-end, scan `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` for any thresholds that crossed during the current session per §2 eval logic. For each cross: auto-generate falsification-derived signal per `recipient_chain` with `signal_type: threshold-crossed` + `falsification_trigger: <RED-FT-NN>` body field. Append to BOARD + WALTER fire-log per §2.4."

**Phase 1.5 verify-research note:** when CORRECTED-FRAMING verdict returns from a verify-research spawn, the Phase 2 step 6 auto-add-RED rule fires automatically downstream — no special handling needed in Phase 1.5 itself. Verdict logging stays in dispatch_note as prose; Phase 2 reads it.

### §3.5 — Sign-off ask ✅ APPROVED 2026-05-06

Will approved:
- ROUTING_TABLE v0.7 with new "By Tag/By Verdict" section per §3.2
- Interim prose-tag discipline per §3.3 (no formal v0.8 dependency)
- CHECKLIST Phase 2 additions per §3.4 (steps 5, 6, 7)

WALTER committed ROUTING_TABLE v0.6 → v0.7 + CHECKLIST v0.9 → v0.10 in same-day closeout (commit `dad58114`).

**Operational test (2026-05-06 PM, 3 batches):** v0.7 By Tag/By Verdict rules fired correctly across 11 dispatches:
- cluster_mediating auto-cc fired on SIG-001/-002/-004/-006/-008/-009 (6 signals)
- CORRECTED-FRAMING auto-cc fired on SIG-003/-007/-008/-009/-011 (5 signals)
- de-dupe rule fired on SIG-008 + SIG-009 (both rules fired same dispatch; RED added once)

---

## §4 — RED ARTIFACT EVOLUTION (RED draft)

### §4.1 — CHALLENGES.tsv schema bump (Q7 — shipped)

**Decision:** RED does NOT stand up `board/BOARD_LOG.tsv` (CARL/BRENT pattern). Instead, RED extends `workbook/CHALLENGES.tsv` with a new column `BOARD_Refs` (col 11) carrying semicolon-separated SIG-W-IDs. This keeps RED's adversarial-overlay role distinct from primary-thesis-integration agents (CARL/BRENT use BOARD_LOG.tsv for calibration-of-integration; RED uses CHALLENGES.tsv for calibration-of-challenge).

**Schema after bump:**

| Col | Name | Type | Purpose |
|-----|------|------|---------|
| 1 | CHG_ID | String | CHG-RED-NNN |
| 2 | Date | YYYY-MM-DD | Date challenge issued |
| 3 | Target | String | Agent / position / thesis being challenged |
| 4 | Grade | String | Letter grade A+ to F |
| 5 | Key_Finding | String | Core finding |
| 6 | Status | Categorical | ACTIVE; RESOLVED; SUPERSEDED; RESOLVED-CONVERGED; WEAKENED |
| 7 | Resolved_Date | YYYY-MM-DD | When resolved |
| 8 | Resolution | String | How it was resolved |
| 9 | KB_Links | String | KB-RED-NNN refs |
| 10 | VX_Links | String | VX-RED-NNN refs |
| 11 | **BOARD_Refs** | **String** | **SIG-W-YYYYMMDD-NNN refs (semicolon-separated)** — NEW 2026-05-06 |

**Backfill state (LIAISON Turn 3 shipped):** 5 historical CHGs backfilled with relevant SIG-W-IDs (CHG-RED-014, -018, -019, -021, -023). 18 historical CHGs untouched. CHG-RED-024 (BRENT v2.0, May 6) retro-flagged.

**Forward convention:** every new CHG-RED-NNN populates BOARD_Refs at issue if any BOARD signals motivated or are challenged by the CHG. Empty cell allowed (not all challenges derive from BOARD signals).

**Complete-backfill task ownership (Q14):** WALTER takes complete CHG-RED backfill as follow-up to Q4 `design/CROSS_REFS/RED.md` self-task. Mechanical-grep approach once cross-ref cache exists. RED concentrates on adversarial substance forward; backfill leaves RED's plate.

### §4.2 — SCHEMA.tsv updates (shipped)

`AGENTS/RED/workbook/SCHEMA.tsv` adds 9 rows (1 for CHALLENGES.BOARD_Refs + 8 for the new FALSIFICATION_TRIGGERS.tsv file). The schema file is now self-documenting for both CHALLENGES (11 cols) and FALSIFICATION_TRIGGERS (8 cols, network-grep-able for WALTER's at-dispatch eval logic per §2).

### §4.3 — RED CLAUDE.md boot-step add (Q9 — ✅ APPROVED + SHIPPED `b1ed0420`)

**Decision (LIAISON Turn 5 locked):** boot-step (b) **scoped scan**, structured as 4 sub-tiers:

- **(b1)** Scan `/BOARD/INDEX.md` cluster ToC at boot — fastest layer, ~10s read
- **(b2)** Pull signals where RED in `to:` line (action) — full body read, treat as direct ASK
- **(b3)** Pull signals where `cluster_mediating: true` (once v0.8 lands) OR prose-tagged paper-vs-structural in dispatch_note (interim) — full body read for adversarial-overlay relevance
- **(b4)** Pull signals carrying CORRECTED-FRAMING verdict in dispatch_note — *body skim only*, looking for direction-confirmed-magnitude-imprecise patterns to flag in MEMORY's CORRECTED-FRAMING calibration

**Skip default-routine info-cc** unless one of b3/b4 fires. Reasoning: at 100/110 info-cc volume, treating all of them as "must read" inverts the small+precise discipline. Better to read 10-15 high-quality signals per cycle than scan 100.

**Insertion point:** between current step 1 (Read MEMORY.md) and step 2 (Read STATUS.md) in `AGENTS/RED/CLAUDE.md` BOOT SEQUENCE — i.e., new step 1.5.

**Why pending Will-approval (at draft time):** boot-step changes affect every future RED session. RED held the CLAUDE.md edit until Will signed off because session-permanent boot changes are best made on explicit instruction, not architectural-LIAISON consensus alone.

**Sign-off:** Will approved boot-step (b) scope as drafted 2026-05-06. RED edited CLAUDE.md and the change shipped in commit `b1ed0420` (RED-side half of 5-of-5 batch).

### §4.4 — RED MEMORY.md 97%-routing-target calibration entry (✅ APPROVED + SHIPPED `b1ed0420`)

**Memory file:** `finding_red_walter_97pct_routing_target.md` (RED tree)

**Content:** RED was in to/info on 97% of 110 BOARD signals (107/110) since Apr 7 — not "mostly absent" as RED Turn 1 framed. The architectural fix is RED-side consumption, not WALTER-side dispatch. Lesson: when diagnosing a routing gap, check the empirical dispatch surface before describing the gap; "I don't see X" can mean "X has been dispatched and I haven't drained the queue" rather than "X hasn't been dispatched."

**Sign-off:** Will approved the memory-file content + index pointer in MEMORY.md 2026-05-06. RED wrote the file in commit `b1ed0420`.

### §4.5 — Joint-proposal §1 + §4 deliverable (this file)

§1 + §4 sections originate in `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md`, committed RED `e6477450` 2026-05-06. WALTER stitches into this repo-root file 2026-05-06 PM post-batch-3 housekeeping.

---

## §5 — v0.9 candidates: `unanimity_state` (WALTER draft)

### §5.1 — Field definition

**Field:** `unanimity_state`
**Type:** String enum
**Values:** `low | moderate | high | extreme` (separate axes for bear and bull — see §5.4)
**Optional:** YES — field omitted when value is `low`
**Stack target:** v0.9 (post-v0.8-land timing per LIAISON Turn 2; not blocking v0.8 stack with Will sign-off currently)

**Purpose:** flag when WALTER's network-wide REGISTRY snapshot at dispatch time shows trade-actionable consensus (≥4 cutoff per Q11) approaching unanimity. Adversarial-overlay implication per RED MEMORY: maximum alignment = maximum blind-spot risk; surface as field on dispatch so RED's read sees "the network is X% bear/bull on this dispatch — review for what they're missing."

### §5.2 — Computation

At dispatch:

1. **Build agent-set.** Read `AGENTS/WALTER/REGISTRY.tsv`. Filter to Tier-1 agents with `Updated ≥ today − 14 days` AND `Status` not `—` or `DORMANT`. (Per Q15 fresh-active-only denominator decision.)
2. **Today's snapshot (2026-05-06 reference):** N = 9 — CARL, REGINALD, BRENT, BROCK, LIQUID, HENRY, VIOLET, HAWK, WALTER. (LABOR May 4 = ≤14d; SAM May 3 = ≤14d. Including those would push N to 11. Practical N range: 9-11 across recent sessions; computation should re-derive at every dispatch, not freeze.)
3. **Compute axes:**
   - `unanimity_bear` = % of fresh-active set at RED-level **≥ 4** (RED4 / RED5)
   - `unanimity_bull` = % of fresh-active set at GREEN OR YELLOW (RED-level ≤ 2)
4. **Map % to enum (4-value, applied independently to each axis):**

| Threshold | Enum | Action |
|-----------|------|--------|
| < 50% | `low` | Field omitted (default) |
| 50-69% | `moderate` | Field present; flag in dispatch_note |
| 70-89% | `high` | Field present; auto-cc RED; flag in dispatch_note |
| ≥ 90% | `extreme` | Field present; auto-cc RED; **Will Telegram-ping** (network blind-spot risk) |

5. **Both axes:** dispatch may carry one or both fields (e.g., `unanimity_bear: high` + `unanimity_bull: low` — most common state during structural-bear regimes). Sign convention: bear-axis is "% network bearish at trade-actionable conviction"; bull-axis is "% network neutral or bullish."

### §5.3 — Today's reference computation

Reading REGISTRY.tsv as of 2026-05-06 closeout, fresh-active set = 9 agents (pre-staleness-filter):

| Agent | Status | Updated | RED-level (numeric) | Bear (≥4)? | Bull (≤2)? |
|-------|--------|---------|---------------------|:----------:|:----------:|
| CARL | RED2 | 2026-05-04 | 2 | ❌ | ✅ |
| REGINALD | ORANGE | 2026-05-01 | ~3 | ❌ | ❌ |
| BRENT | RED3 | 2026-05-06 | 3 | ❌ | ❌ |
| BROCK | RED5 | 2026-05-01 | 5 | ✅ | ❌ |
| LIQUID | YELLOW | 2026-04-16 (>14d STALE) | excluded | — | — |
| HENRY | YELLOW | 2026-04-17 (>14d STALE) | excluded | — | — |
| VIOLET | YELLOW | 2026-05-03 | 1 | ❌ | ✅ |
| HAWK | RED2 | 2026-04-20 (>14d STALE) | excluded | — | — |
| WALTER | YELLOW | 2026-05-06 | 1 | ❌ | ✅ |

**Excluded for staleness (>14d):** LIQUID, HENRY, HAWK. **Effective N = 6.**

- `unanimity_bear` = 1/6 = **17%** → **`low`** (field omitted)
- `unanimity_bull` = 3/6 = **50%** → **`moderate`** (flag in dispatch_note: "network 50% bull-tilted at fresh-active read; RED adversarial-overlay attention warranted")

**Calibration check on the cutoff:** the RED-level ≥4 threshold correctly fires `low` for current state (network bear-elevated but not bear-critical at trade-actionable line). The default ≥3 cutoff would have given 4/6 = 67% → `moderate` bear-axis on a state that's adversarially still mid-arc — over-firing. Q11's tightening to ≥4 is calibrated correctly.

**Pattern observation worth flagging in §5.5:** with current network composition, `unanimity_bear: extreme` (≥90% at RED4+) requires ~5-6 agents simultaneously at RED4+ — a state that hasn't held in the 25-day arc and would itself be a major event. False-positive rate on extreme is low; field should be load-bearing when it does fire.

### §5.4 — Bull-side asymmetric fire rate (LIAISON Turn 4 acknowledgment)

WALTER Turn 4 flagged the bull-side concern: `unanimity_bull` fires more often than `unanimity_bear` because peak-bull-consensus IS where adversarial overlay matters most when bear-thesis is active. Per Q15 lock — fresh-active-only denominator partially mitigates (excludes STALE YELLOW agents), but asymmetry remains real.

**Operational decision:** accept asymmetry as feature, not bug. When bear-thesis is the network's working hypothesis (current state) and `unanimity_bull: high` fires, that IS the adversarial trigger pattern — exactly when the network should be most attentive to RED's structural-vs-paper bifurcation read. The asymmetry surfaces value, doesn't waste cycles.

### §5.5 — Sub-tag candidates (v0.9 stack)

Two sub-tag candidates surfaced in LIAISON Turn 5 worth folding into the v0.9 proposal:

**§5.5a — `event_anchored: true`**

Per RED Turn 5 finding 2 — all 5 "both" bifurcation signals in the historical pass were event-anchored (discrete event/print contradicts active narrative). Definition:

> A `cluster_mediating: true` signal qualifies as `event_anchored: true` when the bifurcation framing emerges from a discrete event or print (kinetic strike, rate decision, earnings print, EIA release, OPEC+ statement, Q1 Call Report bank disclosure, etc.) within 3 trading days of dispatch (T-3 to T+0).

**Routing implication:** event_anchored cluster_mediating signals get IMMEDIATE precedence default (vs PRIORITY default for slow-burn paper-vs-structural drift). Discrete-event-driven bifurcations have higher decision-relevance than slow-burn drift.

**Historical hits in 22-signal classification:** SIG-W-20260411-001 (HY OAS pierced — event = print), SIG-W-20260419-014 (Iran SoH reclosure — event = kinetic), SIG-W-20260420-001 (Tuapse 2nd strike — event = kinetic), SIG-W-20260428-006 (Merz ally-rhetoric — event = statement), SIG-W-20260505-012 (Brent May 5 tape divergence — event = intraday print).

**§5.5b — `network_uncertainty_peak: true` (closeout-level flag, not per-signal)**

Per RED Turn 5 finding 3 — Apr 19 had 9 of 22 bifurcation signals (41% in 1 day). Pattern observation: dense-bifurcation-day correlates with high-stakes-decision-day (Apr 19 was 2 days pre-Apr 21 WAL/OZK earnings + ceasefire expiry).

**Trigger:** when WALTER routes ≥5 cluster_mediating + bifurcation-tagged signals in a single calendar day.

**Action:** WALTER closeout SESSION LOG flag + Will Telegram surface ("network-uncertainty-peak detected on 2026-MM-DD: N bifurcation signals routed, prior comparable: 2026-04-19 (9 signals, 2d pre-WAL/OZK)").

**Rationale:** dense-bifurcation-day is itself a meta-signal worth surfacing. RED owns the historical pattern; WALTER triggers the surface at runtime.

**FIRST FIRE — 2026-05-06 ~20:30 UTC:** at WALTER batch 3 closeout. Today's bifurcation count = 6 (-001 paper-vs-structural + -002 divergence + -004 cluster_mediating + -006 paper-vs-structural + -008 cluster_mediating + -009 cluster_mediating). Threshold ≥5 per JOINT_PROPOSAL §5.5b. Will Telegram-ping fired (msg 1431). Pattern restated 4-of-4 ways today: tape-vs-substance synthesis (-002) + Fed-vs-foreigner plumbing 3-vector convergence (-003+-004+-008) + structural-side authority disagreement (-006) + institutional-de-crowding-vs-retail positioning bifurcation (-009).

### §5.6 — Sign-off ask ✅ APPROVED 2026-05-06

Will approved:
- `unanimity_state` 4-value enum on v0.9 stack with RED-level ≥4 cutoff per Q11
- Fresh-active-only denominator (≤14d Updated, exclude STALE) per Q15
- Independent bear / bull axes per §5.2 step 4-5
- Sub-tag `event_anchored: true` candidate per §5.5a
- Closeout-level `network_uncertainty_peak` flag per §5.5b
- v0.9 timing — folds in once v0.8 lands and CARL/BRENT calibration cycle 1 fires (not blocking v0.8 stack)

WALTER tracks v0.9 stack at `AGENTS/WALTER/design/V0_9_STACK.md` (committed 2026-05-06 `dad58114`). `network_uncertainty_peak` shipped lightweight in CLAUDE.md closeout step 12; first fire occurred same day.

---

## §6 — Decisions locked Turns 1-5

| RED-Q | Turn | Decision | Co-signed | Status |
|-------|:----:|----------|-----------|--------|
| **Q1** | T1 | Falsification-trigger registry as separate TSV at `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` (not STATUS.md table-pull); 8-col schema; at-dispatch evaluation by WALTER. | WALTER T2 | LOCKED + SHIPPED |
| **Q2** | T1 | `unanimity_state` 4-value enum on v0.9 stack (post-v0.8-land); RED-level cutoff refined to ≥4 (Q11). | WALTER T2/T4 | LOCKED v0.9 |
| **Q3** | T1 | `cluster_mediating: true → RED auto-cc` ROUTING_TABLE rule (locks at v0.8 sign-off). | WALTER T2 | LOCKED |
| **Q4** | T1 | `AGENTS/WALTER/design/CROSS_REFS/RED.md` cache (WALTER self-task); refresh trigger: RED thesis-version bump OR new VX/CHG/RED-NN row. | WALTER T2 | LOCKED (WALTER self-task pending) |
| **Q5** | T1 | DEFER `formal_challenge` precedence; observe CHG-RED-024 propagation; revisit calibration cycle 1 (May 20-27). Interim bridge: WALTER cross-refs CHG-RED-NNN via OUTBOX surface. | WALTER T2 | DEFERRED |
| **Q6** | T1 | Prediction-resolution context as body-prose annotation in dispatch_note (NOT YAML field). | WALTER T2 | LOCKED |
| **Q7** | T1 | NO `BOARD_LOG.tsv`; use `CHALLENGES.tsv` with new `BOARD_Refs` col. | WALTER T2 | LOCKED + SHIPPED |
| **Q8** | T1 | DEFER tape-vs-structural primary; RED pre-classifies 21 historical bifurcation signals as seed (Q13 deliverable). | WALTER T4 | DEFERRED + SEED SHIPPED |
| **Q9** | T2/T3 | Boot-step (b) scoped scan (b1-b4 sub-tiers) — pending Will-approval on RED CLAUDE.md edit. | WALTER T4 | LOCKED + SHIPPED `b1ed0420` |
| **Q10** | T2/T3 | Narrow-precision scope for prediction-resolution cross-ref (only signals about the metric/thesis a RED-NN was directly about). | WALTER T4 | LOCKED |
| **Q11** | T2/T3 | `unanimity_state` RED-level cutoff = **≥4** (RED4/RED5 = trade-actionable consensus); not WALTER's default ≥3. | WALTER T4 | LOCKED |
| **Q12** | T2/T3 | CORRECTED-FRAMING auto-cc to RED as a class; composes with Q3 with de-dupe at routing-time. | WALTER T4 | LOCKED + SHIPPED |
| **Q13** | T4 | Bifurcation classification format: TSV at `AGENTS/RED/handoff_WALTER/bifurcation_classification_2026-05-06.tsv`, 5 cols. | WALTER T4 | LOCKED + SHIPPED |
| **Q14** | T4 | WALTER takes complete CHG-RED backfill (mechanical-grep follow-up to Q4 CROSS_REFS cache). | WALTER T4 | LOCKED (WALTER follow-up pending CROSS_REFS/RED.md) |
| **Q15** | T4 | `unanimity_state` denominator: **fresh-active-only** (≤14d Updated; current N≈9). | WALTER T4 | LOCKED |

**Asymmetric note:** RED decisions Q1-Q4, Q6, Q7, Q9-Q15 are LOCKED with WALTER co-sign. Q5, Q8 are DEFERRED with explicit revisit windows. No items remain open as proposed-not-locked. **Q9 + Q4.4 (LOCKED-PENDING-WILL at draft) → APPROVED + SHIPPED** end-to-end same calendar day via RED `b1ed0420`.

---

## §7 — Next review

### RED contribution (RED draft)

**RED calibration cycle 1 trigger:** earliest of three conditions (per LIAISON Turn 4-5):

- FALSIFICATION_TRIGGERS.tsv first auto-dispatch (whenever WALTER's at-dispatch eval logic ships and a threshold crosses)
- v0.8 lands at Will sign-off (estimated this week given CARL/BRENT cosign already)
- CHG-RED-024 BRENT response (next BRENT session, 1-3 days)

**Calibration deliverable per cycle (RED-side):** review FALSIFICATION_TRIGGERS.tsv fire history (true positives / false positives / missed crossings); review CHALLENGES.tsv BOARD_Refs population on new CHGs; review bifurcation classification accuracy on new cluster_mediating dispatches; surface findings as new turn in `AGENTS/RED/handoff_WALTER/LIAISON.md` Turn 7.

**Synced with BRENT calibration cycle 1** — both surface at network state-of-routing review ETA 2026-05-20 to 2026-05-27.

### WALTER close-loop self-tasks (this LIAISON)

1. **§2 implementation** — extend WALTER spawn-protocol step 6b (read FALSIFICATION_TRIGGERS.tsv) + add trigger-eval pass to dispatch workflow + scaffold `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv`. **✅ SHIPPED `dad58114`** within 1-2 sessions post-Will-sign-off on §2.

2. **§3 implementation** — ROUTING_TABLE v0.6 → v0.7 (new "By Tag/By Verdict" section) + CHECKLIST Phase 2 steps 5-7 add. **✅ SHIPPED `dad58114`** within 1 session post-Will-sign-off on §3.

3. **Q4 self-task: `design/CROSS_REFS/RED.md` cache scaffold** — populate from LIAISON `handoff_WALTER/README.md` 12-anchor identifier index (VX-RED + KB-RED + RED-NN + CHG-RED + FLOW-RED + ML-RED + falsification triggers + competing hypotheses + bull-case steelman + thesis CHANGELOG + STATUS FALSIFICATION CRITERIA + CALENDAR FALSIFICATION WATCH). Refresh trigger: RED thesis-version bump OR new VX-RED row OR new RED-NN prediction registered. **WALTER self-task this week (no Will sign-off needed).** ⏳ PENDING.

4. **Q14 self-task: complete CHG-RED backfill** — follow-up to Q4 above. Once CROSS_REFS/RED.md cache exists, mechanical-grep across `BOARD/SIG-W-*.md` for each CHG-RED-NNN target/finding/KB-link reference → populate `BOARD_Refs` col in `AGENTS/RED/workbook/CHALLENGES.tsv`. **WALTER self-task within 2 sessions of Q4 cache landing.** ⏳ PENDING.

   **Critical Rule #2 note:** WALTER must NOT edit `AGENTS/RED/workbook/CHALLENGES.tsv` directly (RED's tree). Implementation: WALTER produces a backfill diff at `AGENTS/WALTER/handoff_RED/CHALLENGES_BACKFILL_diff.tsv` that RED applies at his next boot. Preserves git-isolation per CLAUDE.md.

5. **§5 stack readiness** — once Will signs §5, FORMAT_SPEC v0.9 stack adds `unanimity_state` field per spec; CHECKLIST update for the auto-cc-on-high/extreme rule; WALTER monitors cluster_mediating dispatches for `event_anchored: true` candidates (manual classification until field formalizes). **✅ V0_9_STACK.md tracker shipped `dad58114`** post-v0.8-land timing.

6. **`network_uncertainty_peak` closeout-level flag** — extend WALTER closeout step 12 (STATUS lead-paragraph refresh) to include daily bifurcation-signal count; auto-flag when ≥5 in single calendar day. **✅ SHIPPED `dad58114`. FIRST FIRE 2026-05-06 ~20:30 UTC.**

7. **Repo-root stitch** — `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` final stitched document. WALTER assembles once both side-files are committed (RED §1+§4+§6+§7 + WALTER §2+§3+§5 + repo-root sequencing). **✅ THIS FILE — shipped 2026-05-06 PM** post-batch-3 housekeeping.

### Architectural-thread close-loop

All dependencies resolved end-to-end same calendar day:
- §4.3 RED CLAUDE.md boot-step ✅ SHIPPED `b1ed0420`
- §4.4 RED MEMORY.md calibration entry ✅ SHIPPED `b1ed0420`
- §2/§3/§5 (WALTER) ✅ SHIPPED `dad58114`
- Repo-root stitch (this file) ✅ SHIPPED post-batch-3

The "open-with-substance Turn 1 + concede-on-diagnosis Turn 3 + ship-deliverables-in-Turn-3 + close-Turn-5 + same-calendar-day-implementation" pattern compressed the architectural arc to a single calendar day for RED LIAISON — fastest LIAISON-arc-to-implementation cycle observed.

---

## §8 — Coordination state (updated at stitch 2026-05-06)

**Files in tree (all committed):**

| Path | Owner | Status | Commit |
|------|-------|--------|--------|
| `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` | RED | Drafted + committed | `e6477450` |
| `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` | WALTER | Drafted + committed | `b09bb8de` |
| **`design/JOINT_PROPOSAL_2026-05-06_red_walter.md`** (this file) | WALTER (stitcher) | **Shipped 2026-05-06 PM** | (pending — current commit) |

**Sign-off batch (this proposal) — 5-of-5 APPROVED end-to-end:**

1. **§2 sign-off:** read-loop spec + ledger location + out-of-scope items ✅ APPROVED
2. **§3 sign-off:** ROUTING_TABLE v0.7 delta + CHECKLIST Phase 2 steps 5-7 ✅ APPROVED
3. **§4.3 sign-off** (RED): RED CLAUDE.md boot-step (b) scoped scan ✅ APPROVED + SHIPPED `b1ed0420`
4. **§4.4 sign-off** (RED): RED MEMORY.md 97%-routing-target calibration entry ✅ APPROVED + SHIPPED `b1ed0420`
5. **§5 sign-off:** v0.9 candidates `unanimity_state` + sub-tag candidates ✅ APPROVED

**Implementation commits (WALTER-side):** `dad58114` (5-of-5 SHIPPED end-to-end same calendar day).

Per Critical Rule #10 (close the proposal loop), each sign-off landed as a commit in the originating agent's tree (§2/§3/§5 → WALTER `dad58114`; §4.3/§4.4 → RED `b1ed0420`). This stitch completes the §7 close-loop self-task #7.

---

## Stitch metadata

**Assembled:** 2026-05-06 PM (post-batch-3 housekeeping, same calendar day as RED LIAISON convergence + 5/5 sign-off + RED-side ship + WALTER-side ship). Fastest LIAISON-arc-to-stitch-completion observed.

**Source-of-truth:** the side-files in `AGENTS/RED/design/` and `AGENTS/WALTER/design/` retain their own draft history. This file is the Will-surface unification artifact only — not the canonical edit-target. If §1-§7 substance needs revision, edit the side-files first then re-stitch.

**Refresh trigger:** any RED `e6477450` revision OR WALTER `b09bb8de` revision OR new architectural Turn 7+ on the LIAISON channel adding §9+. Otherwise this file is stable as-of-2026-05-06.

**Read order for Will:** §1 (RED context — what's the adversarial overlay) → §6 (decisions locked — what got agreed) → §2 + §3 + §5 (WALTER mechanics) → §4 (RED artifacts) → §7 + §8 (close-loop + coordination). For implementation review: skip to commit hashes in §8.

*Parallel to the in-progress 3-way joint proposal `JOINT_PROPOSAL_2026-05-05_walter_carl_brent.md` (pending CARL §1+§3a+§3c+§4 sections + Will sign-off on §2 stack — covers FORMAT_SPEC v0.8 fields + scheduled-scan budget + BRENT-IMMEDIATE thresholds + BURST_WINDOW protocol). This 2-way proposal is RED-WALTER specific and parallel — not a subset, not a successor. The 3-way repo-root stitch will follow once CARL section file lands and Will sign-off on §2 stack completes.*
