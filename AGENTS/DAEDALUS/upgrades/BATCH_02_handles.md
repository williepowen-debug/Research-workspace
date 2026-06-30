# Batch Changelist 02 — the 7 firmed L4 agents (REGINALD/CARL/BRENT/HAWK/LABOR/BOND/ORACLE)

**By:** DAEDALUS · **Date:** 2026-06-28 · **Status:** 🟡 DRAFT — routed to PROME (+Will) for review; **NOT applied.**
**Source:** firm-next7 workflow (14 agents: 7 grade + 7 adversarial verify). Same gate as BATCH_01 (assess → propose → PROME review → apply; never auto-apply).

> **↳ Re-validated 2026-06-29 (firm7-profiles-cards profile/card pass).** Two items changed since drafting: **item 7 (BRENT TRADE.md) is now OBSOLETE — strike it** (BRENT migrated TRADE.md to a live boot/closeout-wired surface 6/29, PAT-023 resolved; freezing a live surface would be wrong). **§D utility-agent.md is DONE** (built + ACTIVE 6/28). All other items stand. The pass also surfaced **net-new handles for a candidate BATCH_03** (catalogued in each agent's `upgrades/<A>_CARD.md`): REGINALD §5 If-Falsified ACTION + TRADE.md banner/refresh · CARL/LABOR/BRENT §2 Independence col · BOND/LABOR §5 ACTION col · HAWK 2nd dangling ref `CEASEFIRE_FADE_PROTOCOL.md` · BRENT CLAUDE threshold-drift line 168 · ORACLE §2 CONTRACT block. Plus **domain-lane drifts routed to owners via PROME** (not DAEDALUS edits): HAWK STATUS un-absorbed REMARK_20260628 (HAW-14 breached) · BOND unprocessed Will-approved coverage-extension SIG · LABOR spine-date + imminent Jun-30/Jul-2 catalyst cluster.

---

## The headline (PAT-024): the mechanical scan systematically UNDER-rated mature agents

**All 7 graded L4; all 7 confirmed by adversarial verify; zero downgrades.** Six were under-rated by the 6/27 mechanical scan — **BRENT & HAWK by two levels (L2→L4)**, CARL/LABOR/BOND by one (L3→L4), ORACLE by two (L2→L4, utility). Combined with BROCK, the *entire* provisional-L4 cohort was under-rated. **The fleet is materially more mature than the map said (was 2×L4 → now ≥9×L4).** FLEET_MAP rows corrected this session (my files); patterns PAT-024/025/026 banked. The L0–L2 floor is reliable; the L3+ ceiling is not, until read — the firming pass is essential, not optional.

### Several FLEET_MAP "gaps" were false-negatives (now fixed)
| Agent | The scan said | The read found |
|---|---|---|
| **BRENT** | "no exit-rules" | BRENT is the blueprint's **named source** for §4 bidirectional-flip; rules exemplary |
| **HAWK** | "no exit-rules / missing falsification rails" | **definitive false-negative** — rails in 5 distinct places |
| **CARL** | "no prediction track; thin falsification" | 25 preds (CRL-01..25); **deepest** falsification loop in fleet |
| **BOND** | "build prediction track (it's thin)" | already built + mature (BND-01..10, resolved w/ post-mortems) |
| **LABOR** | "2 pred resolved" | 6 resolved; cadence gate already cleared (44/30d) |
| **ORACLE** | "confirm output consumed → L3" | output IS consumed (NEXUS/LIQUID/TERRY) — gate satisfied, L4 |
| **REGINALD** | "79d stale" | "79" = **79 commits/30d** (freshest agent); scanner-column misread |

---

## The changelist (gated) — grouped by type

### A. Encode-existing-reasoning handles (additive — same class as BATCH_01)
| # | Agent | File · change | Encodes | Effort |
|---|---|---|---|---|
| 1 | **REGINALD** | STATUS 8-channel table — add `Score(1-5)` + `Independence/Cluster` + `Upgrade Trigger` cols *(Independence sub-part → folded into `HANDLE_SWEEP_independence-action.md`; Score+Upgrade-Trigger stay here)* | the 4-cluster independence analysis already in thesis/THESIS.md §1 | S |
| 2 | **REGINALD** | add `NEXUS_BRIEF.md` writeback each closeout (1-para digest + 8-channel 5-pt + freshest deltas) | the convergence hub everyone needs to read without spawning | M |
| 3 | **REGINALD** | STATUS — add trailing labeled `## BOTTOM LINE` (substance exists in lead-summary + "Macro read") | existing top/'Macro read' synthesis | S |
| 4 | **CARL** | STATUS — add trailing labeled `## BOTTOM LINE` (the one real floor gap) | 52/70 composite + NEXUS_BRIEF.VIEW already exist | S |
| 5 | **BOND** | STATUS convergence matrix — add `Independence` column *(→ folded into `HANDLE_SWEEP_independence-action.md`; review the handle there)* | the VX-08..16 sub-vector "not double-counted" note already in the composite | S |
| 6 | **LABOR** | re-pin `NEXUS_BRIEF.md` each closeout (declared standing brief, not re-pinned 6/26) | existing brief, just stale | S |

### B. Hygiene (PAT-023/025 — the staleness rule I own)
| # | Agent | File · change | Effort |
|---|---|---|---|
| 7 | ~~**BRENT** `TRADE.md` FROZEN banner~~ | **OBSOLETE — STRIKE.** BRENT migrated TRADE.md to a LIVE boot/closeout-wired surface 6/29 (commit 6b4f99ef); PAT-023 RESOLVED. Freezing a live surface would be wrong — no replacement. | — |
| 8 | **HAWK** | `TRADE.md` — FROZEN banner (vestigial; oil handed to BRENT Mar-6) | S |
| 9 | **HAWK** | fix dangling boot ref: `scripts/ledger_staleness.py` absent (CLAUDE boot step 5a calls it) — copy the working REGINALD one or remove the call | S |
| 10 | **LABOR** | re-home the durable Green/Yellow/Orange/Red threshold bands (orphaned when VX.tsv was FROZEN — now only in a do-not-cite frozen ledger / Feb-stale EXPECTED_SIGNALS) into a live durable doc | M |

*Items 7–9 touch other agents' data/config; for the FROZEN-vs-refresh data-liveness call, prefer routing a task-packet to the owner (as with BROCK item 5) unless it's an unambiguous banner.*

### C. HELD for round-two justification (builds — not in this batch)
- **ORACLE** calibration / resolution scoreboard (`workbook/RESOLVED.tsv` + Brier) — a real build; its own EXIT RULES promise accuracy-tracking, but justify the upkeep first.
- **BOND** build + wire `NEXUS_BRIEF.md` (its pending Packet 7) — more than a re-pin; it's net-new infra. Justify vs the messaging-overhaul (don't build dead channel infra — auto-memory `messaging_overhaul`).

### D. DAEDALUS's own lane (not a per-agent edit) — surfaced by ORACLE
- ✅ **DONE — `BLUEPRINTS/utility-agent.md` built + ACTIVATED 6/28** (Will+PROME approved; PAT-026 closed). ORACLE was then graded against the live standard in the 6/29 profile/card pass.
- **Fleet-wide TRADE.md/ledger staleness sweep** (PAT-025) — separate proposal; promote `ledger_staleness.py` to a fleet-shared script (REGINALD's works; HAWK refs a missing copy).

## Per-agent DO-NOT-TOUCH (comprehension preserved; full grades in firm-next7 output)
- **REGINALD:** `POSITIONS.md` is the single canonical position truth — STATUS deliberately does NOT re-list strikes (the 6/19 desync lesson); never re-add them. thesis/THESIS.md's slow-moving date is by-design (CHANGELOG-gated) — don't "freshen" it. The 8→4 cluster-independence analysis is its core contribution. The bespoke closeout drift-grep protocol is load-bearing. **Heavily active — route a task-packet, don't edit live.**
- **CARL:** TRADE.md is RETIRED by design (transmission-middle, no book) — do not "restore" it; L4 trade-criterion is met via routing. Don't flatten the intermediate/outer masking-window falsification loop.
- **BRENT:** KB.tsv FROZEN-banner is model compliance — leave as-is. The PREDICTIONS calibration header (calibration-findings/directional-failures/pre-flight) exceeds the blueprint — don't trim.
- **HAWK:** light-end single-channel agent — don't impose multi-channel scaffolding. The VOIDED-disposition + Admiralty-conf prediction discipline is a strength.
- **LABOR:** head-of-chain — its NEXUS_BRIEF currency matters most. Kill A/B session-count discipline + live fired-state intact.
- **BOND:** the DUE-scan→resolve / never-OPEN-but-stale prediction discipline is among its strongest — preserve. mechanism-vs-thermometer per-row.
- **ORACLE (utility):** market constructs are correctly N/A — do not impose convergence matrix/TRADE/predictions. The crowd-signal read is the role.

## Application protocol (after approval) — unchanged from BATCH_01
Idle-check each target immediately before editing (REGINALD is heavily active → task-packet, not live edit); re-read the live file (PAT-009); pathspec commit; record in FLEET_MAP + card. Route a task-packet to inbox if any target is live.

> **Fast-follow — ✅ DONE 2026-06-29:** durable per-agent `profiles/{REGINALD,CARL,LABOR,BOND,HAWK,BRENT,ORACLE}.md` + `upgrades/{…}_CARD.md` written (workflow `firm7-profiles-cards`). Each card carries the section-by-section work queue + net-new handles; FLEET_MAP rows re-scored 6/29; this doc re-validated against the live re-read (item 7 struck, §D done).
