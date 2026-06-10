# WALTER Design + Infra State

*Reference doc — current version state of every WALTER design spec, scaffolding file, active policy, and infrastructure layer. Read **on demand** when checking what's shipped at what version. **NOT in WALTER boot sequence** — live operational state lives in `STATUS.md` (lead paragraph + FILTER POSTURE + SESSION LOG).*

*Created 2026-05-04 (Pass 2 of STATUS.md refactor — moved out of STATUS.md OPERATIONAL STATE table, which had grown to 24 rows mixing static design completeness with stale live-state).*

*Maintenance: this file follows the canonical-source rule (CLAUDE.md). When a spec version bumps in its own file, update the corresponding row here. Don't store the version-history narrative here — point to the spec's own version section.*

---

## 1. Active design specs

| Spec | Current | Notes |
|------|---------|-------|
| `design/SIGNAL_FORMAT_SPEC.md` | **v0.8** | **v0.8 (May 8 — JOINT_PROPOSAL §2a + §2d.5 Will sign-off 2026-05-08)** added 5 optional header fields: `cluster_secondary` / `signal_role` (4-val) / `consumer_transmission` (9-val, CARL-on-routing-line only) / `consumer_lens` (4-val, consumer-cluster + CARL only) / `event_window` (boolean, canonical state in EVENT_WINDOW_STATE.md). All optional, backwards-compatible, forward-only adoption from 2026-05-08; no retro-fit. v0.7 cluster_mediating prose-tag interim discipline RETIRED; v0.7-era `cluster_mediating: true` boolean reads equivalently to v0.8 `signal_role: cluster_mediating`. v0.7 (May 5) added `cluster:` field. v0.6 (Apr 20) Multi-Origin Signals. v0.5 (Apr 20) thesis-frame. v0.4 (Apr 14) ASIA_CONTAGION + UST_FOREIGN. v0.3 (Apr 11 PM) Domain Vocabulary. |
| `design/ROUTING_TABLE.md` | **v0.8** | **v0.8 (May 8 — JOINT_PROPOSAL §2c Will sign-off 2026-05-08)** added "By Boundary Threshold" section after By Tag/By Verdict — 8-row BRENT-IMMEDIATE threshold-cross dispatch list (Brent ≥$120/3sess / ≤$75/3sess / Cushing <20Mbbl single / HY Energy OAS >400bps / VLCC ≥2× 30d-median / Gasoline crack re-cross-≥$30 OR ≥$50 / US oil rigs +50 / 3:2:1 crack >$50). Cadence: single-day=watch / 2-3 sess sustained=dispatch / single-print operational minima dispatch on print / re-fire on boundary re-cross only. BRENT-fire-as-primary; WALTER-fire-as-fallback >5d. By Tag/By Verdict cluster_mediating row updated to v0.8 canonical `signal_role: cluster_mediating`. v0.7 (May 6 PM) By Tag/By Verdict section. v0.6 (May 6 AM) Iran-cluster CARL-info override. v0.5 (Apr 20) thesis-frame row + Residential-housing. v0.4 (Apr 14) ASIA_CONTAGION + UST_FOREIGN. v0.3 (Apr 11) canonical Domain Vocabulary. |
| `design/FILTER_SPEC.md` | **v0.5** | **v0.5 (May 8 — JOINT_PROPOSAL §2d Will sign-off 2026-05-08)** added "OPEN-window dispatch posture" sub-section under Tuning Rules. When EVENT_WINDOW_STATE.md state = OPEN: Phase-2-cluster signals dispatch FLASH; cross-cluster stay normal precedence; verify-research mandatory on extreme-claim items; Will-Telegram threading under master message; daily 00:00 UTC roll-up; close-of-window summary at OPEN→CLOSED transition; `event_window: open` header on all dispatches. State transitions BRENT-led on CLOSED→OPEN (Path A 4/4 met OR Path B EIA triggers fire) and WALTER-led on OPEN→CLOSED (≥48h stable). LESSONS #18 disambiguation early-close retroactive-tags in-window signals. Composes with BALANCED default — does not replace. v0.4 (Apr 20 evening) Verify-Research Trigger reference. v0.3 (Apr 20) BALANCED posture. v0.2 (Apr 11) unified filter model v1 provisional. |
| `design/SIGNAL_PROCESSING_CHECKLIST.md` | **v0.11** | **v0.11 (May 8 — JOINT_PROPOSAL §2a + §2d.5 + §2d.6 Will sign-off 2026-05-08)** added Phase 2 step 4.5 v0.8 routing-augmentation tagging (cluster_secondary / signal_role / consumer_transmission / consumer_lens / event_window field-tagging discipline at dispatch time, with CARL-on-routing-line + consumer-cluster gating rules) + Phase 2.5 event-window state check (reads EVENT_WINDOW_STATE.md once per session; if OPEN, overrides precedence to FLASH for Phase-2-cluster signals while leaving cross-cluster at Phase 2 precedence; daily roll-up + close-of-window summary requirements; 7d stale-check). Step 5 updated to reference v0.8 canonical `signal_role: cluster_mediating` form retiring v0.7 prose-tag and `cluster_mediating: bool` interim discipline. Phase 3 header example refreshed with all v0.8 fields. v0.10 (May 6 PM) Phase 2 routing-augmentation steps 5-7. v0.9 (May 5) cluster assignment + cluster header. v0.8 (Apr 20) Phase 1.5 verify-research codified. v0.7 (Apr 20) Phase 1b combine check. v0.6 (Apr 11 PM) Domain Vocabulary. |
| `design/SIGNAL_INTAKE_TEMPLATE.md` | **v0.1** | v0.1 (Apr 9). Template for per-agent subscription specs. **Agent rollout 4/14 Tier 1: SAM, BRENT, VIOLET, CARL.** CARL (Apr 19 22:21 UTC) is the richest reference — Active Thresholds, 3-tier keywords, explicit NOT-TO-SEND. Recommend as primary reference for HENRY / RED next. |
| `design/BOARD_CONSUMPTION_SPEC.md` | **v0.1** | v0.1 (Apr 20 late-evening). Per-agent `AGENTS/<NAME>/board_log.tsv` (4 cols: timestamp_read / signal_id / disposition / notes; 5-value disposition enum). Boot-step template included for agent CLAUDE.md propagation. No retention cap. Will approved defaults via Telegram msg 938. **Propagation to 14 Tier 1 agent CLAUDE.md files pending — WALTER does not edit other agents' CLAUDE.md (git isolation rule); each agent or Will applies the boot block.** |
| `design/FILTER_V2_PLAN.md` | **Living plan** | Tracks 4-segment Filter v1→v2 review (A/B/C complete Apr 20; D confidence asymmetry deferred — needs design round-trip with Will on 3 mechanic candidates). Archive to `design/history/` once Segment D ships. |
| `design/V0_9_STACK.md` | **v0.1** (May 6 PM) | Tracker doc for FORMAT_SPEC v0.9 candidates — `unanimity_state` 4-val enum + `event_anchored: true` sub-tag + closeout-level `network_uncertainty_peak` flag. Will-approved 2026-05-06 per JOINT_PROPOSAL_2026-05-06_red_walter §5. Implementation gated on FORMAT_SPEC v0.8 land + CARL/BRENT calibration cycle 1 fire (ETA 2026-05-19 to 2026-05-27). |

## 2. Deferred / draft design

| Item | State | Notes |
|------|-------|-------|
| `design/SIGNAL_REGISTRY_DRAFT_A.md` | 📋 Draft A | Architecture only — SQLite / superevent system deferred to v2. |
| `queue/` directory | ❌ Not created | Deferred until MINIMIZE mode needed (no FLASH-batched scenarios to date). |
| FORMAT_SPEC v0.8 | ✅ SHIPPED 2026-05-08 | 5 optional fields landed per JOINT_PROPOSAL §2a + §2d.5; Will-approved 2026-05-08; CARL+BRENT pre-cosigned via 5/5-5/6 LIAISON. Forward-only adoption; no retro-fit. v0.7 prose-tag interim discipline RETIRED. |
| FORMAT_SPEC v0.9 | 🟡 Tracked | Per `design/V0_9_STACK.md` — gated on calibration cycle 1 fire (May 19-27). v0.8 prerequisite SATISFIED. |
| §2b Scheduled scan workflow | 🟡 Will-approved infra-build pending | Cost budget approved 2026-05-08 ($25-50/yr). Build awaiting Phase 2 dependencies: CARL DATA_RELEASE_CALENDAR.md (CARL self-task this week per LIAISON Turn 7) + BRENT DATA_RELEASE_CALENDAR.md (BRENT self-task post-back-disposition). First scan target: BLS April CPI Tuesday 5/13 8:30 AM ET. Hard cap $1.50/wk. Kill-trigger: cost >2× budget OR FP-rate >20% OR 3+ INFO_ONLY-or-REFERRED dispositions on auto-pushed. |

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
| `design/EVENT_WINDOW_STATE.md` | ✅ Created 2026-05-08 | Live BURST_WINDOW state file per JOINT_PROPOSAL §2d. Default state = CLOSED; read at WALTER boot (spawn-protocol step 7b). State machine + verification gates documented inside. WALTER + BRENT have write access (BRENT-led on CLOSED→OPEN; WALTER-led on OPEN→CLOSED). State Transition Log table appends one row per declaration. Cross-refs: FILTER_SPEC v0.5 OPEN-window posture sub-section + CHECKLIST v0.11 Phase 2.5 precedence-override + FORMAT_SPEC v0.8 `event_window` field. |
| WALTER spawn-protocol step 7c (cron-driven feed read) | ✅ Added 2026-05-08 PM (Will direction msg 1597) | Reads 3 external-feed scrapers at boot for triage of novel items: `FORGE/tools/news-sweep/latest.md` (15 Google News RSS thesis-queries M-F 8:30 ET cron) + `FORGE/tools/filing-watch/latest.md` (PROME EDGAR MVP, 10-K/10-Q/8-K/NT/Form-4/SC-13D/SC-13G watched-companies) + `SIGNALS/inbound.md` (SENTRY-owned RSS/Atom EIA + EDGAR getcurrent + more, GitHub Action twice daily 10:00 + 22:00 UTC). Surfaces NOVEL items in Will-Telegram boot reply (one-line triage). Dedupe priority: URL > headline-string > company-CIK against BOARD INDEX + kill_log. NOT auto-dispatched (Will-curated loop preserved). $0 cost (read-only). 24h staleness flag for cron-down detection. Resolves long-pending OPEN DESIGN DECISION "Autonomous news-scan policy". |

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
| VIOLET | ✅ Rebuilt to template 2026-06-10 (first conformant version) | Prior ✅ reflected file-existence only — the Apr 12 original predated the 4/14 rollout and never had template structure. VIOLET self-rebuilt 6/10 (CARL-pattern: live-source map + boot-self-pull rule + 3 priority tiers + exclusions-with-redirects + 4 durable threshold lines; old file archived). Re-read at next routing-rules pass. Appendix A flag drove ROUTING_TABLE v0.10 MARKET_VOL split (Will approved 6/10). |
| CARL | ✅ Has SIGNAL_INTAKE.md (Apr 19) | Richest reference yet (8.4KB; Active Thresholds w/ specific levels, 3-tier keyword confidence, explicit NOT-TO-SEND, earnings pre-staged). Recommend as primary reference for HENRY / RED next. |
| HENRY | ⏳ Pending | Prompt drafted Apr 19 transcript-only, not saved to disk. |
| RED | ⏳ Pending | Prompt drafted Apr 19 transcript-only, not saved to disk. |
| REGINALD / BROCK / LIQUID / LABOR / HAWK / NEXUS / OZK / ATHENA / VIOLET (others) | ⏳ Pending | 14 Tier 1 total target; 4/14 done. |

## 9. BOARD_CONSUMPTION rollout

| Agent | `board_log.tsv` exists | CLAUDE.md boot block applied |
|-------|-----------------------|------------------------------|
| WALTER | n/a (writes BOARD, doesn't consume) | n/a |
| **CARL** | ✅ `AGENTS/CARL/board/BOARD_LOG.tsv` (9-col schema since 2026-05-05; new `Post_Hoc_Conf` column shipped commit `d26aaab2` per LIAISON Turn 3) | ✅ CARL has BOARD-pull at boot (CARL self-applied; **correction to prior STATE that said all-other-agents-pending — CARL was further along than WALTER's MEMORY tracked**) |
| VIOLET | ⏳ Pending — no `board_log.tsv` yet | 🟠 Self-adoption announced 2026-06-10 (SIGNAL_INTAKE Appendix A flag): VIOLET will apply the boot block in her own CLAUDE.md residue pass. Delivery-side status tracked here per her request. |
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
