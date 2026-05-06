# WALTER Design + Infra State

*Reference doc — current version state of every WALTER design spec, scaffolding file, active policy, and infrastructure layer. Read **on demand** when checking what's shipped at what version. **NOT in WALTER boot sequence** — live operational state lives in `STATUS.md` (lead paragraph + FILTER POSTURE + SESSION LOG).*

*Created 2026-05-04 (Pass 2 of STATUS.md refactor — moved out of STATUS.md OPERATIONAL STATE table, which had grown to 24 rows mixing static design completeness with stale live-state).*

*Maintenance: this file follows the canonical-source rule (CLAUDE.md). When a spec version bumps in its own file, update the corresponding row here. Don't store the version-history narrative here — point to the spec's own version section.*

---

## 1. Active design specs

| Spec | Current | Notes |
|------|---------|-------|
| `design/SIGNAL_FORMAT_SPEC.md` | **v0.6** | v0.6 (Apr 20 — Filter v2 Seg B) added Multi-Origin Signals section codifying same-theme combine rule (same domain + same event/sub-theme + each origin adds value; pre-dispatch any-arrival-path, post-dispatch immutable). `origin` field now accepts array form. v0.5 (Apr 20 — Seg A) added `thesis-frame` signal_type. v0.4 (Apr 14) added ASIA_CONTAGION + UST_FOREIGN codes. v0.3 (Apr 11 PM) canonical Domain Vocabulary. v0.2 added `dispatched`/`dispatch_note` + `confidence_language`. |
| `design/ROUTING_TABLE.md` | **v0.7** | v0.7 (May 6 PM — JOINT_PROPOSAL_2026-05-06_red_walter §3 Will sign-off) added "By Tag/By Verdict" section after By Signal Type — three rules (cluster_mediating auto-cc to RED, CORRECTED-FRAMING auto-cc to RED, falsification_trigger auto-fire from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`) + de-dupe + interim prose-tag discipline pre-v0.8. v0.6 (May 6 AM) Iran-cluster CARL-info override + boundary-trigger threshold-cross sub-rule per CARL ↔ WALTER LIAISON Q3. v0.5 (Apr 20) thesis-frame row + Residential-housing exception. v0.4 (Apr 14) ASIA_CONTAGION + UST_FOREIGN rows. v0.3 (Apr 11) canonical Domain Vocabulary. |
| `design/FILTER_SPEC.md` | **v0.4** | v0.4 (Apr 20 evening — Filter v2 Seg C) added Verify-Research Trigger (Phase 1.5 — reference) subsection between Gate 1b and Credibility; points to CHECKLIST v0.8 Phase 1.5 as canonical. No filter-logic change; insertion point only. v0.3 (Seg A) retired "START LOOSE" → BALANCED; Pre-Apr-21 bypass reaffirmation. v0.2 (Apr 11) unified filter model v1 provisional. |
| `design/SIGNAL_PROCESSING_CHECKLIST.md` | **v0.10** | v0.10 (May 6 PM — JOINT_PROPOSAL §3 Will sign-off) Phase 2 routing-augmentation steps 5-7 added: step 5 cluster_mediating auto-cc to RED (with interim prose-tag discipline pre-v0.8), step 6 CORRECTED-FRAMING auto-cc to RED, step 7 FALSIFICATION_TRIGGERS auto-fire scan with sustain-window suppression and parallel ledger at `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` preserving Critical Rule #2. v0.9 (May 5) cluster assignment step + `cluster:` header per CLUSTER_TAXONOMY.md v0.1. v0.8 (Apr 20) Phase 1.5 verify-research framing audit codified. v0.7 (Apr 20) Phase 1b combine check. v0.6 (Apr 11 PM) canonical Domain Vocabulary. |
| `design/SIGNAL_INTAKE_TEMPLATE.md` | **v0.1** | v0.1 (Apr 9). Template for per-agent subscription specs. **Agent rollout 4/14 Tier 1: SAM, BRENT, VIOLET, CARL.** CARL (Apr 19 22:21 UTC) is the richest reference — Active Thresholds, 3-tier keywords, explicit NOT-TO-SEND. Recommend as primary reference for HENRY / RED next. |
| `design/BOARD_CONSUMPTION_SPEC.md` | **v0.1** | v0.1 (Apr 20 late-evening). Per-agent `AGENTS/<NAME>/board_log.tsv` (4 cols: timestamp_read / signal_id / disposition / notes; 5-value disposition enum). Boot-step template included for agent CLAUDE.md propagation. No retention cap. Will approved defaults via Telegram msg 938. **Propagation to 14 Tier 1 agent CLAUDE.md files pending — WALTER does not edit other agents' CLAUDE.md (git isolation rule); each agent or Will applies the boot block.** |
| `design/FILTER_V2_PLAN.md` | **Living plan** | Tracks 4-segment Filter v1→v2 review (A/B/C complete Apr 20; D confidence asymmetry deferred — needs design round-trip with Will on 3 mechanic candidates). Archive to `design/history/` once Segment D ships. |
| `design/V0_9_STACK.md` | **v0.1** (May 6 PM) | Tracker doc for FORMAT_SPEC v0.9 candidates — `unanimity_state` 4-val enum + `event_anchored: true` sub-tag + closeout-level `network_uncertainty_peak` flag. Will-approved 2026-05-06 per JOINT_PROPOSAL_2026-05-06_red_walter §5. Implementation gated on FORMAT_SPEC v0.8 land + CARL/BRENT calibration cycle 1 fire (ETA 2026-05-19 to 2026-05-27). |

## 2. Deferred / draft design

| Item | State | Notes |
|------|-------|-------|
| `design/SIGNAL_REGISTRY_DRAFT_A.md` | 📋 Draft A | Architecture only — SQLite / superevent system deferred to v2. |
| `queue/` directory | ❌ Not created | Deferred until MINIMIZE mode needed (no FLASH-batched scenarios to date). |
| FORMAT_SPEC v0.8 | 🟡 Pending Will sign-off | 4 fields + 9-value `transmission_intensity` enum from JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2a. Must land before V0_9_STACK candidates. |
| FORMAT_SPEC v0.9 | 🟡 Tracked | Per `design/V0_9_STACK.md` — gated on v0.8 land + calibration cycle 1 fire. |

## 3. Research milestones

| Item | State | Notes |
|------|-------|-------|
| Research Corpus | ✅ 10 prompts | ESI, military, ATC, pub/sub, IC dissemination, emergency dispatch, scientific alerts, open output, newsroom editorial, trading desk. |
| Distilled Principles | ✅ 10/10 | All prompts distilled. Source for COP architecture decisions Apr 7. |

## 4. File scaffolding

| Path | State | Notes |
|------|-------|-------|
| `outbox/` | ✅ Created Apr 10 | Drafts in flight only. Cleared once signal dispatches to BOARD (Apr 14 architecture change). |
| `routed/route_log.tsv` | ✅ Created Apr 11 | FILTER_SPEC schema. Append-only audit trail of every dispatched signal. |
| `filtered/kill_log.tsv` | ✅ Created Apr 11 | FILTER_SPEC schema. Append-only audit trail of every kill verdict. |
| `MEMORY.md` | ✅ Created Apr 14 | Feedback / Findings / References / Session Notes — matches SAM pattern. Boot-read every session. |
| `LAST_COMPLETION.md` | ✅ Created Apr 14 | Structured closeout record — STATUS / CHANGED / RESULT / GAPS / WILL_NEEDS / FOLLOW-UP. Overwritten each session, not appended. Boot-read every session. |
| `SESSION_LOG.md` | ✅ Created 2026-05-04 | Full per-session history archive (Pass 1 of STATUS.md refactor). Older entries flow here as STATUS.md SESSION LOG section keeps only last 5. Newest first. Append-only. |
| `design/STATE.md` | ✅ Created 2026-05-04 | This file. Pass 2 of STATUS.md refactor. |
| `anchors/IRAN_WAR.md` | ✅ Created 2026-05-04 | Network-wide macro anchor pulled out of STATUS.md (Pass 3) — explicit verified-as-of stamp + re-verify trigger. WALTER owns; refresh at boot if state-change OR every 7d min OR pre-dispatch on Iran-cluster signals. |
| `registry/FALSIFICATION_FIRED_LOG.tsv` | ✅ Created 2026-05-06 PM | WALTER-side parallel ledger for RED's pre-registered falsification triggers. 5-col schema (trigger_id / fired_date / metric_value_at_fire / dispatched_signal_id / sustain_confirmation). Preserves Critical Rule #2 — fire history lives in WALTER tree, not RED tree. Spec at JOINT_PROPOSAL_2026-05-06_red_walter §2.4. README at `registry/README.md`. Empty at scaffold; appends one row per WALTER auto-dispatch from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`. |
| `registry/README.md` | ✅ Created 2026-05-06 PM | Operational pattern doc for the registry/ directory + FALSIFICATION_FIRED_LOG schema + cross-references. |

## 5. Active policies

| Policy | State | Detail |
|--------|-------|--------|
| **Delivery policy** | ✅ Active since 2026-04-14 | BOARD-only for IMMEDIATE / PRIORITY / ROUTINE. FLASH = BOARD + Telegram-alert-to-Will only (no inbox push). Other-agent boot-sequence rollout pending — recipient agents will pull from BOARD at their own boot once `BOARD_CONSUMPTION_SPEC` propagation lands. Codified as RULE 10 in CLAUDE.md. |
| **Domain Vocabulary** | ✅ v0.4 (Apr 14) | 15 canonical codes (LABOR, MACRO_INFLATION, TARIFF_TRADE, CONSUMER_CREDIT, BANK_CRE, FUNDING_LIQUIDITY, PRIVATE_CREDIT, INSURANCE_SHADOW, OIL_ENERGY, GEOPOL_ENERGY, GEOPOL_NON_ENERGY, JAPAN_BOJ, MARKET_VOL, ASIA_CONTAGION, UST_FOREIGN). v0.4 added ASIA_CONTAGION + UST_FOREIGN. ROUTING_TABLE v0.4 propagated. Canonical source: `SIGNAL_FORMAT_SPEC.md`. |
| **Boot Sequence** | ✅ Updated 2026-04-14 (BOARD), 2026-05-04 (Pass 1+2 trim) | CLAUDE.md boot order. Apr 14: scan `/BOARD/INDEX.md` (was `signals/INDEX.md`); git steps stage BOARD/ explicitly. May 4: STATUS.md trimmed in Pass 1 (older session log archived) and Pass 2 (design state moved here). |
| **Filter posture (live)** | See STATUS.md FILTER POSTURE section | Not duplicated here — `STATUS.md` is the canonical source for current filter mode. |

## 6. /COP.md status

| Field | Value |
|-------|-------|
| Location | Repo root: `/COP.md` |
| Owner | WALTER (writes + commits; lives at repo root for network-shared read access) |
| Current version | **v0.3 — last refreshed 2026-04-13** |
| State | **🟡 LIVE BUT PAUSED** — refresh deprioritized by Will on 2026-04-14 to focus on signal-routing throughput. Resume trigger: Will's call. |
| Staleness | 22+ days. Content still references Islamabad collapse / OZK Apr 16 / WAL Apr 21 / Apr 22 ceasefire — all moot. **Reading the current file at boot is actively misleading until refreshed or until paused state is honored.** |
| Boot read note | `STATUS.md` FILTER POSTURE includes the "COP refresh: PAUSED" flag so the active state is visible without opening COP.md. |
| Template | `design/COP_TEMPLATE.md` |

## 7. /BOARD/ status

| Field | Value |
|-------|-------|
| Location | Repo root: `/BOARD/` (relocated from `AGENTS/WALTER/signals/` on 2026-04-14 via `git mv`) |
| Owner | WALTER (all writes); pull point for all agents |
| Index | `/BOARD/INDEX.md` — discovery table, one row per dispatched signal, chronological |
| Current count | See `STATUS.md` lead paragraph — live count is the canonical source (this file would go stale if it stored the count). |
| Filename pattern | `SIG-W-YYYYMMDD-NNN-slug.md` |
| Append-only | Yes — never delete, never rename |

## 8. Agent SIGNAL_INTAKE.md rollout (subscription specs)

| Agent | State | Notes |
|-------|-------|-------|
| SAM | ✅ Has SIGNAL_INTAKE.md | Prototype reference. |
| BRENT | ✅ Has SIGNAL_INTAKE.md | |
| VIOLET | ✅ Has SIGNAL_INTAKE.md | |
| CARL | ✅ Has SIGNAL_INTAKE.md (Apr 19) | Richest reference yet (8.4KB; Active Thresholds w/ specific levels, 3-tier keyword confidence, explicit NOT-TO-SEND, earnings pre-staged). Recommend as primary reference for HENRY / RED next. |
| HENRY | ⏳ Pending | Prompt drafted Apr 19 transcript-only, not saved to disk. |
| RED | ⏳ Pending | Prompt drafted Apr 19 transcript-only, not saved to disk. |
| REGINALD / BROCK / LIQUID / LABOR / HAWK / NEXUS / OZK / ATHENA / VIOLET (others) | ⏳ Pending | 14 Tier 1 total target; 4/14 done. |

## 9. BOARD_CONSUMPTION rollout

| Agent | `board_log.tsv` exists | CLAUDE.md boot block applied |
|-------|-----------------------|------------------------------|
| WALTER | n/a (writes BOARD, doesn't consume) | n/a |
| **CARL** | ✅ `AGENTS/CARL/board/BOARD_LOG.tsv` (9-col schema since 2026-05-05; new `Post_Hoc_Conf` column shipped commit `d26aaab2` per LIAISON Turn 3) | ✅ CARL has BOARD-pull at boot (CARL self-applied; **correction to prior STATE that said all-other-agents-pending — CARL was further along than WALTER's MEMORY tracked**) |
| All other Tier 1 agents | ⏳ Pending | ⏳ Pending — Will or each agent applies; WALTER does not edit other agents' CLAUDE.md per git isolation rule. |

## 10. LIAISON channels (paired-agent architectural-alignment scaffolding)

*Created 2026-05-06 per Phase 1 scaffolding. Generic naming convention: `AGENTS/{TARGET}/handoff_WALTER/LIAISON.md` for any WALTER-paired channel. Glob-discovery at boot step 9. Manifest with last_turn_date + DORMANT auto-flag (30-day threshold) lives in STATUS.md "Active LIAISON channels + countdowns" subsection. Calibration cycle trigger: 14-day calendar primary; N=20 BOARD dispositions early-fire. **Only artifacts that exist now are listed; aspirational rows added when shipped.***

| Channel | File state | Notes |
|---------|------------|-------|
| WALTER ↔ CARL | ✅ `AGENTS/CARL/handoff_WALTER/LIAISON.md` (6 turns 2026-05-05 → 06; thread converged) | First active LIAISON. README at same path. Cycle 1 calibration ETA 2026-05-19 calendar primary. |
| WALTER ↔ RED | ⏳ Pending RED revival | CARL has staged `handoff_RED/` (transitional layer ready to convert when RED operational). |
| WALTER ↔ HENRY | ⏳ Pending RED first | Second priority. CC-side, file-mediated works. |
| WALTER ↔ BRENT | ⏳ Deferred | OC-platform crossing makes file-mediated slow. |

## 11. Outbox queue files (active requests to other agents via Prome)

*Naming: `AGENTS/WALTER/outbox/REQ-{TARGET}-{YYYYMMDD}-{slug}.md`. Persist as durable record even if Prome degraded. Boot step 9 scans for files older than 14d → flag for retry/escalation.*

| Path | Created | Status | Target | Topic |
|------|---------|--------|--------|-------|
| `outbox/REQ-HAWK-20260505-geopolitical-driver-rebuild-post-may4-break.md` | 2026-05-05 | Open | HAWK | Geopolitical-driver framing rebuild post-5/4-break. HAWK-proxy synthesis available as starting framework. |
| `outbox/REQ-NEXUS-20260505-cluster-classification-iran-hormuz-confluence-consumer-stagflation-breakdown.md` | 2026-05-05 | Open | NEXUS | 5-vector IRAN_HORMUZ + 5-axis CONSUMER_STAGFLATION classification. |
| `outbox/REQ-RED-20260505-wirth-1970s-analog-steelman-falsification.md` | 2026-05-05 | Open | RED | Wirth 1970s-analog 5-track adversarial framework. |

## 12. One-shot artifacts in flight

| Path | Purpose | State |
|------|---------|-------|
| `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-05_walter_sections.md` | WALTER's drafted sections of joint WALTER+CARL proposal from 6-turn LIAISON 2026-05-05 — covers FORMAT_SPEC v0.8 (4 fields) + scheduled-scan budget + ROUTING_TABLE v0.6 + design/CROSS_REFS/CARL.md. | ✅ Shipped 2026-05-06; awaiting CARL's parallel sections + Will-mediated stitch into repo-root `design/JOINT_PROPOSAL_2026-05-05.md`. |
| `AGENTS/WALTER/design/LIAISON_PLAYBOOK.md` | Generic process doc — captures CARL pilot pattern as repeatable LIAISON channel process. Reusable for BRENT, RED, HENRY, future. | ✅ Shipped 2026-05-06. Update if new lessons land from BRENT dialog. |
| `AGENTS/WALTER/design/BRENT_LIAISON_PREP.md` | One-shot prep doc — boot-ready handle for next-session BRENT LIAISON setup. Q1-Q8 prepared, Q9-Q14 anticipated, cross-platform options α/β/γ, bridge concept candidate `energy_transmission` enum. | ✅ Shipped 2026-05-06. Archive to `design/history/` after BRENT dialog converges. |
