# DECISION_ARTIFACTS_INDEX.md
**Created:** 2026-05-23 16:58 ET
**Owner:** Prome
**Purpose:** Inventory decision artifacts so Prome promotes existing work into standard rails instead of reinventing it.

---

## Taxonomy

| Type | Purpose | Owner | Typical location | Prome action |
|---|---|---|---|---|
| **Action Card** | Will-facing decision artifact: objective, exposure, branches, execution checklist | Prome | `PROME/action-cards/` | Create / maintain when Will action may be needed |
| **Execution Rail** | Trigger/default/owner/backstop logic that prevents drift | Prome | inside action cards, `PROME/EXECUTION_RAILS.md`, or source trigger sets | Standardize and index in `ACTIVE_DECISIONS.md` |
| **Decision Memo** | Domain-native recommendation with mark/context/rationale | Agent / domain | `AGENTS/<NAME>/...`, `FORGE/...` | Reference; promote only if action needed |
| **Trigger Set** | Cluster-level rail across multiple positions/catalysts | Prome / FORGE / domain | `FORGE/trigger-sets/`, `PROME/action-cards/` wrapper | Use as source-of-truth; wrap for Will-facing state |
| **Trade Decision Log** | Permanent record of Will decision, execution state, outcome, lesson | Prome | `PROME/TRADE_DECISIONS.md` | Update on approval/state changes/outcome |
| **Active Decision Index** | Boot-readable cockpit of non-terminal decisions | Prome | `PROME/ACTIVE_DECISIONS.md` | Keep short; no full logic |

---

## Promotion Rule

Agents can keep writing domain-native memos. Prome promotes an artifact into standardized rails when any of these are true:

- Will approval/action is needed.
- A position expires within 30 calendar days.
- A decision has multiple operational states: approved, broker pending, filled, logged, etc.
- Multiple agents feed one position/cluster decision.
- The default action matters if nobody acts.

Promotion means:

1. Add / update a Prome action-card wrapper if Will-facing.
2. Ensure a rail exists with trigger, invalidation, owner, backstop, and default.
3. Add a row to `PROME/ACTIVE_DECISIONS.md` if non-terminal.
4. Log Will decisions / state changes in `PROME/TRADE_DECISIONS.md`.

---

## Existing Decision Artifacts

### Prome action cards

| Artifact | Type | State | Notes |
|---|---|---|---|
| `PROME/action-cards/TEMPLATE.md` | Action Card template | Active spec | Updated 2026-05-23 with compact state header + execution rail section |
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | Action Card | Historical / active reference | First private-credit branch-to-action card |
| `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md` | Action Card | Historical / superseded by later bank work | Strong precursor: buckets May scraps vs June salvage vs thesis runway |
| `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` | Action Card + rail | `BROKER_PENDING` | Will-approved 2/1 roll; broker execution still pending |
| `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` | Action Card wrapper | `DRAFT` | Created 2026-05-23; wraps FORGE trigger set |

### FORGE trigger sets / decision cards

| Artifact | Type | State | Notes |
|---|---|---|---|
| `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` | Trigger Set / cluster rail | v0.1 DRAFT | Source-of-truth for 6/18 theta-killer cluster; pending BROCK/REGINALD/HENRY calibration/default-pass |
| `FORGE/research/commodity-disruptions/helium/APD_DECISION_CARD.md` | Decision Card | Existing domain card | APD long-thesis tag/decision-card precursor; not yet promoted into Active Decisions |

### Agent/domain decision memos

| Artifact | Type | State | Notes |
|---|---|---|---|
| `AGENTS/REGINALD/MAY15_DECISIONS.md` | Decision Memo + trigger ladder | Historical | May 15 WAL/SSB expiry memo; strong pre-registered trigger example |
| `AGENTS/BROCK/domain/sources/POSITION_DECISIONS_MAY21.md` | Decision Memo + trigger ladder | Active reference | BROCK per-position decisions; explicitly calls HYG Jun let-expire and execution-rails lesson |
| `AGENTS/RED/research/APO_ROLL_DECISION_MAR26.md` | Decision Memo | Historical | RED adversarial roll work; useful for pattern audit if needed |
| `AGENTS/RED/research/POSITION_TIMELINE_STRESS.md` | Decision Memo | Historical | Timeline stress / position-pressure style precursor |
| `AGENTS/LIQUID/archive/research_tactical_resolved/KRE_HYG_ROLL_ANALYSIS.md` | Decision Memo | Historical/resolved | HYG/KRE roll analysis precursor |
| `AGENTS/TRADES/JUNE_2026_CANDIDATES.md` | Candidate list | Legacy | Candidate source, not a rail by itself |

---

## Live Promotions

| Source artifact | Prome wrapper / index | Promotion status | Next action |
|---|---|---|---|
| `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` | `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` + `ACTIVE_DECISIONS.md` | Promoted as wrapper 2026-05-23 | Consolidate BROCK/REGINALD calibration or default-pass; move DRAFT → PROPOSED for Will approval |
| `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` | `ACTIVE_DECISIONS.md` + `TRADE_DECISIONS.md` | Active | Tue 5/27 broker execution / fill verification |

---

## Non-Goals

- Do not force every agent into Prome's template.
- Do not duplicate full domain analysis in action cards.
- Do not make `ACTIVE_DECISIONS.md` a journal.
- Do not promote artifacts just because they exist; promote when action/state/default matters.
