# FORMAT_SPEC v0.9 stack — candidate tracker

*Tracking doc — what's queued for the v0.9 release of `SIGNAL_FORMAT_SPEC.md` once v0.8 lands and CARL/BRENT calibration cycle 1 fires. Not a spec itself — points back at the canonical source documents below. Created 2026-05-06 PM after Will sign-off on JOINT_PROPOSAL_2026-05-06_red_walter §5.*

*Maintenance: when a candidate ships into FORMAT_SPEC v0.9, mark **SHIPPED** with the FORMAT_SPEC version + commit ref. When deferred to v0.10+, move to deferred section. Don't duplicate spec — point at it.*

---

## 1. Implementation gating

**Pre-conditions:**
1. **FORMAT_SPEC v0.8 lands.** v0.8 stack is the 3-way CARL/BRENT/WALTER joint proposal at `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-05_walter_sections.md` §2a (4 fields + 9-value `transmission_intensity` enum). Will sign-off pending.
2. **CARL or BRENT calibration cycle 1 fires.** ETAs: CARL ~2026-05-19 (14d cal), BRENT/RED 2026-05-20 to 2026-05-27 (N=15 forward OR 21d, whichever first).

**Why gating:** v0.9 candidates are downstream of v0.8 architecture decisions (cluster_mediating field, transmission_intensity enum, BURST_WINDOW state machine). Shipping v0.9 before v0.8 lands would force re-architecture; calibration cycle 1 likely surfaces additional v0.9 candidates worth folding in same release.

**Once gating clears:** WALTER drafts FORMAT_SPEC v0.9 update + CHECKLIST + ROUTING_TABLE deltas + commits in single closeout (similar to v0.8 stack mechanics).

---

## 2. Candidate fields (Will-approved 2026-05-06 per JOINT_PROPOSAL §5)

### 2.1 — `unanimity_state` (header field, optional)

**Source:** `JOINT_PROPOSAL_2026-05-06_red_walter §5` (canonical spec).

| Attribute | Value |
|-----------|-------|
| Field name | `unanimity_state` |
| Type | String enum |
| Values | `low | moderate | high | extreme` |
| Optional | YES — field omitted when value is `low` (default state) |
| Axes | Two independent: `unanimity_bear` + `unanimity_bull` (one or both may be present per dispatch) |
| Cutoff | RED-level **≥ 4** for bear-axis; RED-level **≤ 2** (GREEN/YELLOW) for bull-axis |
| Denominator | Fresh-active-only (`Updated ≥ today − 14 days` AND `Status` not `—` or `DORMANT`) per Q15 LIAISON lock |
| Mapping | <50% → low | 50-69% → moderate | 70-89% → high (auto-cc RED) | ≥90% → extreme (auto-cc RED + Will Telegram-ping) |

**Today's reference computation** (effective N=6 after Q15 staleness filter): `unanimity_bear` = 1/6 = 17% LOW (field omitted); `unanimity_bull` = 3/6 = 50% MODERATE (flagged in dispatch_note). Calibration: ≥4 cutoff fires correctly; default ≥3 would have over-fired 4/6=67% MODERATE on bear-axis at trade-actionable line.

**Implementation work (post-v0.8-land):**
- FORMAT_SPEC v0.9: add field schema + mapping table.
- CHECKLIST: extend Phase 2 step 4 (Confidence) with sister sub-step "Compute unanimity_state from REGISTRY snapshot per fresh-active denominator; add field if value > low; auto-cc RED if high|extreme; Telegram-ping Will if extreme".
- ROUTING_TABLE: extend "By Tag/By Verdict" section with `unanimity_state: high|extreme` row → auto-cc RED.
- WALTER spawn-protocol: extend at-dispatch logic to pull REGISTRY snapshot (already done at boot step 8/13) into in-memory unanimity computation per dispatch.

### 2.2 — `event_anchored: true` (sub-tag of cluster_mediating, optional)

**Source:** `JOINT_PROPOSAL_2026-05-06_red_walter §5.5a`.

| Attribute | Value |
|-----------|-------|
| Field name | `event_anchored` |
| Type | Boolean |
| Optional | YES — only present when value is `true` |
| Pre-condition | Signal must already carry `cluster_mediating: true` (post-v0.8) |
| Trigger | Bifurcation framing emerges from a discrete event or print (kinetic strike, rate decision, earnings print, EIA release, OPEC+ statement, Q1 Call Report bank disclosure, etc.) within 3 trading days of dispatch (T-3 to T+0) |
| Routing implication | event_anchored cluster_mediating signals get **IMMEDIATE precedence default** (vs PRIORITY default for slow-burn paper-vs-structural drift) |

**Historical hits in 22-signal classification (RED Turn 5 deliverable):** SIG-W-20260411-001 (HY OAS pierced — print), SIG-W-20260419-014 (Iran SoH reclosure — kinetic), SIG-W-20260420-001 (Tuapse 2nd strike — kinetic), SIG-W-20260428-006 (Merz ally-rhetoric — statement), SIG-W-20260505-012 (Brent May 5 tape divergence — intraday print).

**Interim manual classification** (pre-v0.9): WALTER monitors cluster_mediating dispatches and tags `event_anchored: true` in dispatch_note prose when 3-day-event-anchor matches; field formalizes at v0.9.

### 2.3 — `network_uncertainty_peak` (closeout-level flag, NOT a per-signal field)

**Source:** `JOINT_PROPOSAL_2026-05-06_red_walter §5.5b`.

| Attribute | Value |
|-----------|-------|
| Scope | Closeout-level flag, NOT a per-signal header field |
| Trigger | WALTER routes ≥5 cluster_mediating + bifurcation-tagged signals in a single calendar day |
| Action | WALTER closeout SESSION LOG flag + Will Telegram surface ("network-uncertainty-peak detected on 2026-MM-DD: N bifurcation signals routed; prior comparable: 2026-04-19 (9 signals, 2d pre-WAL/OZK)") |
| Rationale | Dense-bifurcation-day correlates with high-stakes-decision-day (Apr 19 reference: 9/22 = 41% in 1 day, 2 days pre-Apr 21 WAL/OZK earnings + Iran ceasefire expiry) |

**Implementation status (2026-05-06 PM):** **shipped lightweight with §3 implementation** — extend STATUS.md lead-paragraph closeout step 12 to include daily bifurcation-signal count; auto-flag when ≥5 in single calendar day. Pre-v0.8 uses prose-tag detection (paper-vs-structural / tape-vs-substance / bifurcation / divergence in dispatch_note); post-v0.8 switches to `cluster_mediating: true` count.

**Empirical refinement candidate (RED Turn 6 callout):** ≥5 starting threshold may be over-firing or under-firing — RED to monitor over calibration cycle 1; if false-positive rate is high, refine ≥5 → ≥7 at Turn 7 calibration retro May 20. Threshold adjustment is a one-line edit.

---

## 3. Future v0.9 candidates (NOT yet proposed)

### 3.1 — `sponsor_strategy` enum (header field, optional) — PARKED 2026-05-21

**Origin:** Will-mediated decision 2026-05-22 00:11 UTC re: SPONSOR_BIFURCATION sub-cluster spawn question. 5-instance crystallization surfaced via SIG-W-20260521-019 (KKR-doubles-down / Apollo-cashes-out / Blackstone-counter-inflows / Blue-Owl-gates / NEW WAL-sponsor-walk-away bank-side). Decision: status quo cluster_secondary tagging is sufficient at 5 instances; defer header-sub-tag promotion until pattern grows or surfaces outside PC_STRESS / BANK_COLLATERAL domain.

| Attribute | Value |
|-----------|-------|
| Field name | `sponsor_strategy` |
| Type | String enum |
| Values | `defend | cash_out | counter | gate | walk_away` |
| Optional | YES — only set when signal substance is about how an alt-asset sponsor responded to PC/BDC/bank-loan stress |
| Domain | PC_STRESS + BANK_COLLATERAL primary; cross-cluster eligible |

**Re-evaluation trigger:** calibration cycle 1 close 2026-05-25 OR pattern reaches 8-10 instances OR pattern surfaces in non-PC non-bank domain. If none fires by 6/15, defer to v0.10 stack.

**Why parked not shipped:**
1. WAL bank-side instance just crystallized 2026-05-21 — premature to spawn structure for a pattern only just locked in at 5 instances.
2. Existing `cluster_secondary` already accommodates the cross-cluster bifurcation (SIG-W-20260521-019 demonstrates the mechanic works).
3. Signal density is in the LENS not standalone events — header sub-tag adds queryability but not classification value the current tags don't capture.

Calibration cycle 1 (CARL/BRENT/RED) likely surfaces additional candidates 2026-05-19 to 2026-05-27. Add rows here as they emerge.

---

## 4. Cross-references

- **JOINT_PROPOSAL §5 spec (canonical):** `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` §5
- **RED side context (FALSIFICATION_TRIGGERS as v0.9 cousin):** `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md` §1 + §4
- **v0.8 stack pending sign-off:** `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-05_walter_sections.md` §2a-§2d
- **REGISTRY for unanimity computation:** `AGENTS/WALTER/REGISTRY.tsv` (RED-level + Updated columns load-bearing)
- **Calibration cycle 1 trigger conditions:** LIAISON Turn 4-5 of CARL/BRENT/RED LIAISON files

---

*This file lives in `design/` not `design/history/` because the v0.9 stack is still active; archive once v0.9 ships.*
