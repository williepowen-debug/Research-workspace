# Prome Decision Flow
**Created:** 2026-05-08 21:05 ET
**Owner:** Prome
**Purpose:** Turn research into decisions without mixing event analysis, portfolio exposure, proposed actions, and learning records.

---

## Why This Exists

Prome’s job is not just to find signals. Prome has to help Will make disciplined decisions under time pressure.

The failure modes this flow prevents:

1. **Stale exposure** — acting on old positions or expired contracts.
2. **Moving goalposts** — redefining bullish/bearish after an event lands.
3. **Domain/action confusion** — research files deciding portfolio actions without current sizing.
4. **Panic analysis** — rebuilding the framework during the event window.
5. **No learning loop** — decisions happen, but the reason/outcome is not recorded.

This flow is intentionally lightweight. It should help cold-boot Prome orient fast, not create bureaucracy.

---

## The Six Layers

```text
Event Pre-Build
→ Position Snapshot
→ Action Card / Execution Rail
→ Live Event Read
→ Decision State Tracking
→ Decision Log
→ HEARTBEAT update
```

### 1. Event Pre-Build

**Question:** What does the event mean?

**Owner:** Relevant domain agent / research file.
**Location:** `AGENTS/<DOMAIN>/domain/sources/*_PREBUILD_*.md`

**Contains:**
- Baseline numbers before the event.
- Thresholds set before the print lands.
- Branch definitions: Bull / Mixed / Bear / Strong Bear.
- Read order: first 5 minutes, first 15 minutes, first 30 minutes.
- Cross-agent routing triggers.

**Does not contain:**
- Current portfolio sizing.
- Specific trade instructions.
- Will’s final decision.

**Example:** `AGENTS/BROCK/domain/sources/FSK_PREBUILD_MAY11.md`

---

### 2. Position Snapshot

**Question:** What do we actually own right now?

**Owner:** Prome.
**Location:** `PROME/POSITIONS.md`

**Contains:**
- Current account size and cash.
- Position values, expiries, cost basis, P/L.
- Exposure by theme.
- Which positions are live risk vs residual/lottery tickets.
- OCR/source caveats when pulled from screenshots.

**Does not contain:**
- Full event framework.
- Branch logic.
- Detailed action permissions.

**Rule:** Any serious Action Card requires a fresh or explicitly accepted Position Snapshot.

---

### 3. Action Card / Execution Rail

**Question:** Given current exposure, what actions are allowed by event branch — and what happens if no trigger fires?

**Owner:** Prome.
**Location:** `PROME/action-cards/` and `PROME/EXECUTION_RAILS.md`

**Contains:**
- Link to the relevant Event Pre-Build.
- Link/date of the Position Snapshot used.
- Branch-to-action table.
- Allowed actions.
- Forbidden actions.
- Execution checklist.
- Exact decision status vocabulary.
- Owner / next action / time backstop.
- Default action if no new information arrives.
- “Ask Will” decision prompts when a trade/public action is involved.

**Does not contain:**
- Full 10-Q extraction.
- Permanent thesis narrative.
- Final decision/outcome record.

**Rule:** Action Cards are event-specific. Execution Rails are the state/trigger layer that prevents limbo. A card or rail with no time backstop is incomplete.

---

### 4. Live Event Read

**Question:** Which branch fired?

**Owner:** Prome + relevant domain context.
**Location:** Usually a concise chat answer first; optionally a dated note if complex.

**Contains:**
- Actual event numbers.
- Branch classification.
- Deviation from pre-build expectations.
- Immediate implications for the Action Card.

**Does not contain:**
- A trade execution unless Will explicitly approves.

**Rule:** First classify the event. Then consult the Action Card. Do not invent new thresholds live unless data invalidates the pre-build, and if that happens, say so explicitly.

---

### 5. Decision State Tracking

**Question:** Where exactly is the decision in the chain from proposal to completion?

**Owner:** Prome.
**Location:** Action-card header, execution rail, and `PROME/TRADE_DECISIONS.md` entry.

**State vocabulary:**

```text
DRAFT → PROPOSED → WILL_APPROVED → BROKER_PENDING → ORDER_PLACED → FILLED → POSITION_UPDATED → LOGGED → COMPLETED
```

**Terminal / alternate states:**

```text
REJECTED / DEFERRED / EXPIRED / SUPERSEDED / CANCELLED
```

**Rule:** `WILL_APPROVED` is not execution. `BROKER_PENDING` is live risk. A decision is not `COMPLETED` until broker/public action is verified, position files are updated, and the decision log reflects the outcome or pending follow-up.

---

### 6. Decision Log

**Question:** What did Will decide, why, and what happened later?

**Owner:** Prome.
**Location:** `PROME/TRADE_DECISIONS.md`

**Contains:**
- Date/time.
- Decision requested.
- Options considered.
- Will’s decision.
- Rationale at the time.
- Follow-up/outcome field.

**Does not contain:**
- Full position table.
- Domain research detail.

**Rule:** Log decisions, not every thought. If no decision was made, log only when the non-decision matters.

---

## HEARTBEAT’s Role

`HEARTBEAT.md` is the cold-boot orientation layer.

It should summarize:
- Current regime.
- Key dashboard levels.
- Top catalysts.
- Pending decisions.
- Which docs are stale.
- Current active Action Cards.

For live operational state, HEARTBEAT should point to `PROME/ACTIVE_DECISIONS.md` rather than duplicating every next step.

It should not hold full action logic. HEARTBEAT points to action cards; it does not replace them.

---

## Standard Workflow

### Before an Event

1. Confirm or create Event Pre-Build.
2. Refresh Position Snapshot if any action might be taken.
3. Create Action Card.
4. Add the event/action card to HEARTBEAT if it is top priority.

### During an Event

1. Pull actual event data.
2. Classify branch against the pre-build.
3. Consult Action Card.
4. Give Will the smallest decision needed.
5. Do not execute external/trade actions without approval.

### After a Decision

1. Mark the action card / rail with the exact state: `WILL_APPROVED`, `BROKER_PENDING`, `ORDER_PLACED`, etc.
2. Record Will’s decision in `PROME/TRADE_DECISIONS.md`.
3. If execution is pending, name the owner, next action, and verification needed.
4. After fills/actions, update position/source-of-truth files before calling the decision complete.
5. Update HEARTBEAT if the regime, catalyst queue, or pending decisions changed.
6. Update domain files only if the fact belongs there.
7. Mark action card expired, superseded, or completed when no live step remains.

---

## Ownership Rules

| File type | Owns | Does not own |
|---|---|---|
| Event Pre-Build | Event meaning, thresholds, read order | Portfolio actions |
| Position Snapshot | Current exposure, sizing, P/L | Event interpretation |
| Action Card | Branch-to-action permissions | Permanent history |
| Execution Rail | Triggers, owner, deadline, default action, status | Full research thesis |
| Live Event Read | Actual result + branch | Long-term memory unless promoted |
| Decision State | Current operational state and next owner | Thesis justification |
| Decision Log | Will decision + rationale + outcome | Research detail |
| HEARTBEAT | Current regime + pointers | Full action logic |

---

## Minimal Templates

### Event Pre-Build Reference Block

```md
## References
- Pre-build: `AGENTS/<DOMAIN>/domain/sources/<EVENT>_PREBUILD_<DATE>.md`
- Position snapshot: `PROME/POSITIONS.md` updated <date/time>
- Action card: `PROME/action-cards/<EVENT>_ACTION_CARD.md`
```

### Action Card Skeleton

```md
# <EVENT> Action Card
**Event:** <event/date>
**Pre-build:** <path>
**Position snapshot:** <path + timestamp>
**State:** <one canonical state from `PROME/EXECUTION_RAILS.md`>
**Owner:** <Prome / Will / agent>
**Next:** <literal next step>
**Backstop:** <date/condition>
**Default:** <action>

## Objective
What decision this card supports.

## Current Exposure
Only the positions relevant to the event.

## Branch Actions
| Branch | Evidence | Allowed | Forbidden | Will decision needed |
|---|---|---|---|---|
| Bull | ... | ... | ... | ... |
| Mixed | ... | ... | ... | ... |
| Bear | ... | ... | ... | ... |
| Strong Bear | ... | ... | ... | ... |

## Execution Checklist
- Pull live data.
- Classify branch.
- Check spreads/pricing if trade-related.
- Ask Will for approval before action.
```

### Decision Log Entry Skeleton

```md
## YYYY-MM-DD HH:MM ET — <Decision Title>

**Context:**
**Options:**
**Recommendation:**
**Decision state:** <one canonical state from `PROME/EXECUTION_RAILS.md`>
**Will decision:** Approved / Rejected / Deferred / Modified
**Action taken:**
**Next owner / verification needed:**
**Follow-up date:**
**Outcome:** Pending
```

---

## First Implementation: FSK May 11

Use FSK as the first test case because the pre-build and position snapshot already exist.

Files:
- Pre-build: `AGENTS/BROCK/domain/sources/FSK_PREBUILD_MAY11.md`
- Position snapshot: `PROME/POSITIONS.md` updated 2026-05-08 14:17 ET
- Action card: `PROME/action-cards/FSK_MAY11_ACTION_CARD.md`
- Decision log: `PROME/TRADE_DECISIONS.md`

The key architectural point: FSK should classify the event, but the Action Card should decide how that classification maps to Will’s actual portfolio and cash.
