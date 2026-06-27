# JOINT_PROPOSAL — WALTER sections — 2026-05-06

Drafted by WALTER for integration into repo-root `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` (2-way: RED + WALTER, **parallel to** — not folded into — the existing 3-way `JOINT_PROPOSAL_2026-05-05_walter_carl_brent.md`). Stitching plan per LIAISON Turn 4: WALTER stitches at repo-root once both side-files are committed (lower friction since WALTER is in-session for closeout).

Source LIAISON: `AGENTS/RED/handoff_WALTER/LIAISON.md` Turns 1-5 (RED+WALTER architectural thread, May 6 — converged in 5 turns, fastest LIAISON arc to date).

WALTER scaffolding context: BRENT 3-way joint-proposal §2a-§2d + §3b + §3d sections drafted 2026-05-05/06 at `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-05_walter_sections.md` (475 lines). This RED 2-way proposal lives in a parallel file to keep cosign surface clean — RED's deltas are not part of the 3-way v0.8 stack, they're a separate Will-decision.

Section ownership (per LIAISON Turn 4):
- §1 (RED) — RED domain framing + 97% routing-target finding *(shipped at `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` §1; placeholder slot below)*
- §2 (WALTER) — FALSIFICATION_TRIGGERS.tsv at-dispatch evaluation logic *(this draft)*
- §3 (WALTER) — ROUTING_TABLE v0.7 delta + CHECKLIST delta *(this draft)*
- §4 (RED) — CHALLENGES.tsv evolution + RED CLAUDE.md boot-step pending Will-approval *(shipped at `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` §4; placeholder slot below)*
- §5 (WALTER) — v0.9 candidates: `unanimity_state` *(this draft)*
- §6 — Decisions locked Turns 1-5 (RED-drafted comprehensive table — see RED §6)
- §7 — Next review (RED-drafted; WALTER co-signed)

---

## §1 — RED CONTEXT (RED draft)

*[See `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` §1 — RED domain framing, §1.2 the 97% routing-target finding, §1.3 verdict distribution validation, §1.4 bifurcation cluster sizing, §1.5 operational state. Placeholder slot for repo-root stitch.]*

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

### §2.6 — Sign-off ask

Will approves:
- Read-loop spec per §2.2 + dispatch logic per §2.4
- Out-of-scope items per §2.3 (continuous polling / compound triggers / event-type triggers all deferred)
- WALTER-side ledger at `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` with 5-col schema
- Implementation within 1-2 WALTER sessions post-sign-off

If approved, WALTER commits scaffold + extends CLAUDE.md spawn-protocol in next closeout.

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

### §3.5 — Sign-off ask

Will approves:
- ROUTING_TABLE v0.7 with new "By Tag/By Verdict" section per §3.2
- Interim prose-tag discipline per §3.3 (no formal v0.8 dependency)
- CHECKLIST Phase 2 additions per §3.4 (steps 5, 6, 7)

If approved, WALTER commits ROUTING_TABLE v0.6 → v0.7 + CHECKLIST update in next closeout.

---

## §4 — RED ARTIFACT EVOLUTION (RED draft)

*[See `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` §4 — §4.1 CHALLENGES.tsv schema bump, §4.2 SCHEMA.tsv updates, §4.3 RED CLAUDE.md boot-step add (pending Will-approval), §4.4 RED MEMORY.md 97%-routing-target calibration entry (pending Will-approval), §4.5 joint-proposal §1+§4 deliverable. Placeholder slot for repo-root stitch.]*

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

Reading REGISTRY.tsv as of 2026-05-06 closeout, fresh-active set = 9 agents:

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

### §5.6 — Sign-off ask

Will approves:
- `unanimity_state` 4-value enum on v0.9 stack with RED-level ≥4 cutoff per Q11
- Fresh-active-only denominator (≤14d Updated, exclude STALE) per Q15
- Independent bear / bull axes per §5.2 step 4-5
- Sub-tag `event_anchored: true` candidate per §5.5a
- Closeout-level `network_uncertainty_peak` flag per §5.5b
- v0.9 timing — folds in once v0.8 lands and CARL/BRENT calibration cycle 1 fires (not blocking v0.8 stack)

If approved, WALTER tracks v0.9 stack as next-spec-version target; folds into FORMAT_SPEC update post-v0.8-land.

---

## §6 — Decisions locked Turns 1-5

*[See `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` §6 — comprehensive table of Q1-Q15 with WALTER cosign references and LOCKED / DEFERRED / LOCKED-PENDING-WILL status. WALTER concurs with the table as drafted; no separate WALTER §6 section needed.]*

---

## §7 — Next review (RED contribution; WALTER co-signed)

*[See `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` §7 — calibration cycle 1 trigger conditions, deliverable spec, sync with BRENT calibration cycle 1, architectural-thread close-loop dependencies. WALTER concurs.]*

**Additional WALTER close-loop self-tasks (this LIAISON):**

1. **§2 implementation** — extend WALTER spawn-protocol step 6b (read FALSIFICATION_TRIGGERS.tsv) + add trigger-eval pass to dispatch workflow + scaffold `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv`. Within 1-2 sessions post-Will-sign-off on §2.

2. **§3 implementation** — ROUTING_TABLE v0.6 → v0.7 (new "By Tag/By Verdict" section) + CHECKLIST Phase 2 steps 5-7 add. Within 1 session post-Will-sign-off on §3.

3. **Q4 self-task: `design/CROSS_REFS/RED.md` cache scaffold** — populate from LIAISON `handoff_WALTER/README.md` 12-anchor identifier index (VX-RED + KB-RED + RED-NN + CHG-RED + FLOW-RED + ML-RED + falsification triggers + competing hypotheses + bull-case steelman + thesis CHANGELOG + STATUS FALSIFICATION CRITERIA + CALENDAR FALSIFICATION WATCH). Refresh trigger: RED thesis-version bump OR new VX-RED row OR new RED-NN prediction registered. **WALTER self-task this week (no Will sign-off needed).**

4. **Q14 self-task: complete CHG-RED backfill** — follow-up to §3 above. Once CROSS_REFS/RED.md cache exists, mechanical-grep across `BOARD/SIG-W-*.md` for each CHG-RED-NNN target/finding/KB-link reference → populate `BOARD_Refs` col in `AGENTS/RED/workbook/CHALLENGES.tsv`. **WALTER self-task within 2 sessions of Q4 cache landing.**

   **Critical Rule #2 note:** WALTER must NOT edit `AGENTS/RED/workbook/CHALLENGES.tsv` directly (RED's tree). Implementation: WALTER produces a backfill diff at `AGENTS/WALTER/handoff_RED/CHALLENGES_BACKFILL_diff.tsv` that RED applies at his next boot. Preserves git-isolation per CLAUDE.md.

5. **§5 stack readiness** — once Will signs §5, FORMAT_SPEC v0.9 stack adds `unanimity_state` field per spec; CHECKLIST update for the auto-cc-on-high/extreme rule; WALTER monitors cluster_mediating dispatches for `event_anchored: true` candidates (manual classification until field formalizes). **Post-v0.8-land timing.**

6. **`network_uncertainty_peak` closeout-level flag** — extend WALTER closeout step 12 (STATUS lead-paragraph refresh) to include daily bifurcation-signal count; auto-flag when ≥5 in single calendar day. **Lightweight; ships with §3 implementation.**

7. **Repo-root stitch** — `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` final stitched document. WALTER assembles once both side-files are committed (RED §1+§4+§6+§7 + WALTER §2+§3+§5 + repo-root sequencing). **Post-Will-sign-off on full proposal (or pre-sign-off if Will requests stitched view first).**

---

## §8 — Coordination state

**Files committed to land this proposal as a unit:**

| Path | Owner | Status |
|------|-------|--------|
| `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` | RED | Drafted 2026-05-06; pending Will-sign-off + commit |
| `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` | WALTER | Drafted 2026-05-06 (this file); pending Will-sign-off + commit |
| `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` | WALTER (stitcher) | Pending — assembles after §1-§7 settled |

**Sign-off batch (this proposal):**

1. **§2 sign-off ask:** read-loop spec + ledger location + out-of-scope items
2. **§3 sign-off ask:** ROUTING_TABLE v0.7 delta + CHECKLIST Phase 2 steps 5-7
3. **§4.3 sign-off ask** (RED): RED CLAUDE.md boot-step (b) scoped scan
4. **§4.4 sign-off ask** (RED): RED MEMORY.md 97%-routing-target calibration entry
5. **§5 sign-off ask:** v0.9 candidates `unanimity_state` + sub-tag candidates

**5 sign-off items.** Will may approve as a unit or per-§; WALTER+RED implementation kicks off on each individual approval. Per Critical Rule #10 (close the proposal loop), each sign-off lands as a commit in the originating agent's tree (§2/§3/§5 → WALTER; §4.3/§4.4 → RED).

---

*WALTER sections file lives at `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md`. Stitches into repo-root `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` for the final Will-surface artifact, parallel to (not folded into) the existing 3-way `JOINT_PROPOSAL_2026-05-05_walter_carl_brent.md`. WALTER stitches at repo-root once both side-files are committed (lower friction since WALTER is in-session for closeout).*
