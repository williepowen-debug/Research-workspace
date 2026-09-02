# PROFILE — PROME (coordinator / chief of staff)

> ⚠️ **STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01):** spine re-based 8/20 (named trigger) · 35d since 7/28 body. Read the FLEET_MAP row (re-cut 2026-09-01) and `upgrades/PRODUCTION_REVIEW_2026-09-01.md` before this body. Refresh checkpoint: **2026-09-08**. *(Bannered by `scripts/profile_clock_check.py` + the PR#5 readers; a banner is a warning, not a fix — PAT-085.)*

**Built:** 2026-07-28 (from the same-day 4-reader full-directory audit — `upgrades/PROME_AUDIT_2026-07-28.md` + `_readers/`; graded into FLEET_MAP the same day, Will-ratified) · **Class:** Meta · **Home:** repo-root `PROME/` (NOT `AGENTS/` — deliberate; Will-scoped shared-doc steward) · **Refresh trigger:** after the 7/31-8/2 maintenance batch lands, or any re-base of the protocol spine, or ±2 surfaces added/removed from BOOT.md's read list.

## 1. What it is (charter, in its own shape)

Chief of staff, not universal analyst: prioritization, decision rails, state files, operational tasking, Will-facing synthesis. Signal/news routing is WALTER's (PROME consumes BOARD via cursor). Runs live near-daily — highest change-rate agent in the fleet (322 commits on roster, most active). **Everything downstream consumes PROME:** every agent reads its packets/rails; Will reads its dashboard + HEARTBEAT directly.

## 2. File anatomy — where the richness lives

| Layer | Surfaces | Character |
|---|---|---|
| **Always-loaded** | `CLAUDE.md` (76 ln) | Thin by design — boot-order summary + git ¶ (a named Mirror-Map row; historically the LAGGING mirror — check first on any canon change) |
| **Protocol spine** | `BOOT.md` (96) · `CLOSEOUT.md` (260, chunked+tiered) · `HANDOFF.md` · `SCRATCH.md` (session) · `STATUS.md` (standing; 100 ln but ~88K — density lives in long table rows) | ~1,200 ln across 12 docs — fleet's heaviest protocol layer. BOOT = the FAST surface (absorbs new gates in hours); CLOSEOUT = the SLOW one (symmetry table lags). NO labeled BOTTOM LINE on STATUS (substance in core-state header) |
| **Decision rails** | `DOCKET.tsv` (canonical ON DRIFT, its own line 3) · `GATES.tsv` (boot-blocking rows) · `ACTIVE_DECISIONS.md` · `ROSTER.md` (fleet classification truth) | The crown jewels. Honest per-row dates throughout — content-vintage, never mtime. GATES has a STATES vocabulary line; state cells must LEAD with an enumerated token |
| **Governance** | `SYSTEM.md` (216 — holds the **Mirror Map** :52-55) · `AUTONOMY.md` (tier grants) · `COMPLETION_SPEC.md` (spawn contract) · `ORCHESTRATION_PLAYBOOK.md` (current) · `ORCHESTRAL_LAYER_DESIGN.md` (decaying, roster-arithmetic stale) · `GIT_COORDINATION.md` · `MACHINE_LOCAL.md` | The self-knowledge layer — unique in fleet. Mirror Map is load-bearing for any cross-agent change |
| **Tools** | `tools/`: `board_scan.py` (BOARD cursor, every boot) · `fleet_dashboard.py` (Will-facing artifact, closeout) · `spine_audit.workflow.js` (self-audit, ~7d stamp cadence) + state files | All wired w/ real cadence homes (above fleet norm). Parsers key on HEARTBEAT FORMATTING — any re-base is a breaking change (PAT-069) |
| **Flow** | `inbox/` ("sole delivery surface"; processed/ flat ~80 files) · `packets/` `proposals/` `reports/` `cluster/` `drafts/` | Proposal-disposition write-back is the chronic gap class (PAT-032) |
| **Archive** | `archive/` (8.7M, 44 entries) — ⚠️ contains LIVE boot-read `HANDOFF_2026Q2.md` (212K, append-daily) | Boundary lies in both directions; no live index (index itself archived) |

## 3. How it expresses the meta-dimensions (its own forms)

- **Conformance checking:** `spine_audit.workflow.js` on ~7d cadence (GROUPS = 10 files; blind to HANDOFF/AUTONOMY/MACHINE_LOCAL/COMPLETION_SPEC — extension proposed) + a growing check-stack (claim_check, firetime_check, position_agreement_check, env_doctor, memory_index_check, ledger_staleness).
- **Records/learning:** rails-as-ledgers (DOCKET/GATES with honest dates), canon amendments with in-session Will approval, lessons named by KB-row (KB-VIO-110 "ledger not prose"), memory/auto contributions.
- **Falsification analog:** verify-before-fix discipline (fetched the live degraded artifact before believing the audit; re-verifies MY claims before amending BOOT — correct counterparty rigor both directions).
- **Delivery:** dashboard artifact (recorded URL, favicon-stable) + HEARTBEAT (re-base + numbered-amendment audit trail) + packets to agent inboxes (self-committed per carve-out ①).

## 4. DO-NOT-TOUCH (verified design decisions, not debt)

1. **Root-level placement** — false symmetry to force into `AGENTS/`; scanner blindness is the scanner's gap (noted in FLEET_MAP row), not a reason to move PROME.
2. **DOCKET-wins-on-drift** — the single best anti-rot rule in its design.
3. **AUTONOMY.md tiers** — explicit Will-delegation contract; enables fast action without scope creep.
4. **HEARTBEAT re-base + amendment ritual** — audit-trail pattern is right; needs a migration CHECKLIST (accepted into batch), never a redesign.
5. **`archive/HANDOFF_2026Q2.md` boot-read** — the defect is the BOUNDARY (live file under a dead-meaning name); fix is rotation + live index, never deletion (it's appended daily).
6. **codex lane** — dormant capability by design; needs a trigger line, not removal.

## 5. Known tensions + active program (grade-relevant)

**T1** mirror-heavy × highest change-rate · **T2** protocol mass > session execution capacity · **T3** no second reader on Will-facing outputs. Full statement: audit §7a; nine mechanisms §7b. **Live program:** small-four (mirror_walk, generate-at-n≥3, symmetry-registration, nonempty-assertions) ride PROME's 7/31-8/2 DOCKET'd batch; second wave = `prome_gate.py` BEFORE spine-prune, then mirror census. **L5 gate rides this program** (FLEET_MAP row). DAEDALUS-side: 21d external sweep (T3-a, pending Will green light) + PAT-069 blueprint line.

## 6. Reading protocol for future DAEDALUS sessions

Start: `STATUS.md` head + `SCRATCH.md` (session state) + `DOCKET.tsv`/`GATES.tsv` (the truth) — NOT the prose docs. On any canon change touching PROME: walk SYSTEM.md's Mirror Map + grep the old token (PAT-068). Never edit anything here — PROME is near-always live; packets only. Its self-reports are reliable but verify fixes AT TARGET (it fixed 5/5 cleanly on 7/28 — verified, zero misdiagnoses both directions).
