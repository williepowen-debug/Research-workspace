# EXECUTION_RAILS.md
**Created:** 2026-05-23 15:15 ET
**Owner:** Prome
**Purpose:** Convert trade/research conviction into pre-registered action rules so good frameworks do not die in limbo.

---

## Why This Exists

The recurring failure mode is not lack of research. It is the gap between:

```text
research conclusion → Will approval → broker action → position update → decision log → later review
```

If that chain is not explicit, positions drift into theta cliffs, approvals sit unexecuted, and Prome has to reconstruct state after crashes or clears.

Execution rails solve this by forcing every live decision to answer:

1. **What exactly is being decided?**
2. **What evidence changes the answer?**
3. **What action is allowed under each branch?**
4. **Who owns the next step?**
5. **What happens if nothing new happens by the deadline?**
6. **How do we verify the action actually happened?**

---

## Artifact Taxonomy

Full inventory lives at `PROME/DECISION_ARTIFACTS_INDEX.md`. Use this taxonomy to avoid rewriting existing agent work.

| Type | Purpose | Prome handling |
|---|---|---|
| **Action Card** | Will-facing decision artifact: objective, exposure, branches, checklist | Lives in `PROME/action-cards/`; use when Will action/approval is possible |
| **Execution Rail** | Trigger/default/owner/backstop logic | Can live inside an action card or source trigger set; must be indexed if non-terminal |
| **Decision Memo** | Agent/domain recommendation with mark context and rationale | Reference as source; promote only when action/state/default matters |
| **Trigger Set** | Cluster-level rail across multiple positions/catalysts | Keep source-of-truth in the relevant FORGE thesis/research path (for example `FORGE/timing/thesis/` or `FORGE/research/`); create Prome wrapper for Will-facing state |
| **Trade Decision Log** | Permanent Will decision + execution/outcome record | `PROME/TRADE_DECISIONS.md`; update on approval and state changes |
| **Active Decision Index** | Boot-readable cockpit of non-terminal decisions | `PROME/ACTIVE_DECISIONS.md`; no full logic, just state/owner/next/backstop/source |

**Promotion rule:** agents may write domain-native memos. Prome promotes to standardized rails when Will action is needed, expiry is within 30 days, multiple agents feed one decision, or the default action matters if nobody acts.

---

## Rail Standard

Every rail should fit this block. If it cannot, the decision is not concrete enough yet.

```md
## <Decision / Position / Cluster>

**State:** <canonical state; see vocabulary below>
**Owner:** Prome / Will / <agent>
**Next:** <one literal next step>
**Window:** <date/time or condition>
**Backstop:** <default deadline>
**Default:** <hold / roll / trim / let expire / cancel / ask Will>

### Exposure
| Position | Expiry | Qty | Current read | Why it matters |
|---|---:|---:|---|---|

### Inputs to Monitor
| Input | Source | Bull / benign | Mixed | Bear / action | Invalidate |
|---|---|---|---|---|---|

### Branch Rules
| Trigger | Evidence | Allowed action | Forbidden action | Owner | Deadline |
|---|---|---|---|---|---|
| C1 | <specific condition> | <specific action> | <specific forbidden> | <owner> | <date/condition> |
| C2 | ... | ... | ... | ... | ... |
| C3 | ... | ... | ... | ... | ... |
| C4 Time backstop | No decisive trigger by <date> | <default action> | <forbidden> | <owner> | <date> |

### Verification
- Broker/fill proof needed: <yes/no + what>
- Files to update after action: <paths>
- Completion condition: <what makes this rail done>
```

---

## Decision Status Vocabulary

Use these exact states across Action Cards, rails, logs, and `PROME/ACTIVE_DECISIONS.md`.

For headers, use the compact field name `State:` and one state only. Do not paste the full vocabulary into every card; link back here instead.

| State | Meaning | Next owner usually |
|---|---|---|
| `DRAFT` | Framework being built; not ready for Will. | Prome / agent |
| `PROPOSED` | Ready for Will; no approval yet. | Will |
| `WILL_APPROVED` | Will approved the action, but no broker/public action confirmed. | Will / Prome |
| `BROKER_PENDING` | Approval exists; order still needs to be placed. | Will |
| `ORDER_PLACED` | Order entered; fill not confirmed. | Will |
| `FILLED` | Broker fill reported; files not fully updated. | Prome |
| `POSITION_UPDATED` | Position/source-of-truth updated; decision log may still need finalization. | Prome |
| `LOGGED` | Decision log complete; outcome may remain pending. | Prome |
| `COMPLETED` | No next operational step remains. | None |
| `DEFERRED` | Will or Prome explicitly paused; requires future trigger/date. | Named owner |
| `REJECTED` | Will rejected proposal. | None unless follow-up specified |
| `EXPIRED` | Window passed; no longer actionable. | Prome for cleanup |
| `SUPERSEDED` | Replaced by newer rail/card. | Prome |
| `CANCELLED` | Actively cancelled before completion. | None unless cleanup specified |

**Important:** `WILL_APPROVED` is not completion. `BROKER_PENDING` is live risk.

---

## Active Decision Index

`PROME/ACTIVE_DECISIONS.md` is the live dashboard for unfinished decisions. It should stay short enough to read at boot.

Include any decision that is not terminal:

```text
DRAFT / PROPOSED / WILL_APPROVED / BROKER_PENDING / ORDER_PLACED / FILLED / POSITION_UPDATED / LOGGED / DEFERRED
```

Remove or archive decisions when they become:

```text
COMPLETED / REJECTED / EXPIRED / SUPERSEDED / CANCELLED
```

Minimum columns:

| Decision | State | Owner | Next | Backstop | Source |
|---|---|---|---|---|---|

`ACTIVE_DECISIONS.md` does **not** hold full logic. It points to action cards / rails.

---

## Required Fields for Live Trade Rails

A trade-related rail is incomplete unless it has:

- Current exposure source and timestamp.
- At least one action trigger and one invalidation trigger.
- A time backstop.
- A default action if no new info arrives.
- Named owner for the next step.
- Post-action file list.
- Verification requirement: fill price, screenshot, broker statement, or explicit Will confirmation.

---

## Default Rules

1. **No open-ended “watch.”** Watch until what date, which level, and what default?
2. **No approval without execution state.** If Will approves, immediately mark `WILL_APPROVED` or `BROKER_PENDING` and name the next owner.
3. **No silent expiry.** Every option expiring within 30 calendar days needs a rail or an explicit “let expire” decision.
4. **No threshold edits after the event** unless the pre-build is invalid; if changed, record why.
5. **No revenge-adds.** Losing premium can only be rolled or replaced if the rail says the thesis is still live and the vehicle mismatch is the issue.
6. **Default beats drift.** If no trigger fires by the backstop, execute the default or ask Will if the default itself requires judgment.

---

## Cluster Rails

Use a cluster rail when multiple positions share one catalyst/window, e.g. the 6/18 theta-killer group.

Cluster rail output should include:

| Position | Current state | Roll/add trigger | Trim/exit trigger | Let-expire trigger | Time backstop | Default |
|---|---|---|---|---|---|---|

Cluster rails are for **triage and synchronization**. If one line becomes decision-grade, promote it to its own Action Card.

---

## First Production Test

**Test case:** 6/18 expiry cluster.

Known live pieces from current Prome state:
- TLT Jun 18 $85P × 3 — already has an action card; `WILL_APPROVED / BROKER_PENDING` pending Tuesday 5/27 broker execution.
- HYG ×8, EGBN, AAL ×2, WAL $65P + $67.5P ×2, KRE $60P — still need cluster rail treatment after BROCK + REGINALD calibration/default-pass.

Success condition for v1: cold-boot Prome can answer for every 6/18 line:

```text
roll, trim, hold, let expire, or ask Will — by what date, based on what evidence, and who owns the next step.
```
