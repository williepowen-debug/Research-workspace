# <Event / Decision> Action Card
**Created:** YYYY-MM-DD HH:MM ET
**State:** DRAFT / PROPOSED / WILL_APPROVED / BROKER_PENDING / ORDER_PLACED / FILLED / POSITION_UPDATED / LOGGED / COMPLETED / REJECTED / DEFERRED / EXPIRED / SUPERSEDED / CANCELLED
**Owner:** Prome / Will / <agent>
**Next:** <one literal next step>
**Window:** <date/time or condition>
**Backstop:** <date/time or condition>
**Default:** <hold / trim / roll / let expire / cancel / ask Will>
**Source:** `<pre-build / domain source path>`
**Position:** `PROME/POSITIONS.md` updated <date>
**Spec:** `PROME/EXECUTION_RAILS.md` + `PROME/DECISION_FLOW.md`

---

## Objective

<State the specific decision this card is meant to discipline.>

This card is **not** a trade order. It defines allowed/forbidden actions and the decision prompts to bring to Will. Any trade or external action requires Will’s approval.

**State rule:** use one canonical `State` from `PROME/EXECUTION_RAILS.md`. `WILL_APPROVED` is not complete; `BROKER_PENDING` means live operational risk until verified.

---

## Current Relevant Exposure

| Position / Bucket | Expiry | Qty | Current value | Read |
|---|---:|---:|---:|---|
| <position> | <date> | <qty> | <$> | <live risk / residual / hedge / structural> |

**Key implication:** <One sentence on what this exposure means for the decision.>

---

## Branch Inputs

| Metric / signal | Bull / benign | Mixed / watch | Bear / action | Strong bear / urgent |
|---|---:|---:|---:|---:|
| <metric> | <threshold> | <threshold> | <threshold> | <threshold> |

---

## Branch-to-Action Table

| Branch | Evidence | Allowed actions | Forbidden actions | Will decision needed |
|---|---|---|---|---|
| Bull / stabilization | <evidence> | <actions> | <forbidden> | <prompt or none> |
| Mixed / grind | <evidence> | <actions> | <forbidden> | <prompt or none> |
| Bear / weak tail breaking | <evidence> | <actions> | <forbidden> | <prompt> |
| Strong / Max Bear | <evidence> | <actions> | <forbidden> | <prompt> |

## Execution Rail

| Trigger | Evidence / threshold | Action | Forbidden action | Owner | Deadline |
|---|---|---|---|---|---|
| C1 | <condition> | <action> | <forbidden> | <owner> | <date/condition> |
| C2 | <condition> | <action> | <forbidden> | <owner> | <date/condition> |
| C3 Invalidation | <condition> | <cancel / reprice / ask Will> | <forbidden> | <owner> | <date/condition> |
| C4 Time backstop | No decisive trigger by <date> | <default action> | <forbidden> | <owner> | <date> |

---

## Execution Checklist

1. Pull actual event/source data.
2. Extract the decisive metrics.
3. Classify branch against pre-set thresholds.
4. Pull live tape/dashboard if markets are open.
5. Apply this Action Card.
6. If proposing action, give Will max 2 options and one recommendation.
7. If Will approves, immediately update Status / Owner / Next action; do not call it complete until verified.
8. Log final decision in `PROME/TRADE_DECISIONS.md`.
9. If trade-related, update position/source-of-truth files after fills.
10. Update `HEARTBEAT.md` if the regime, catalyst queue, or pending decisions changed.

---

## Forbidden Actions

- No changing thresholds after the event unless the pre-build is demonstrably invalid.
- No revenge-adds to repair losing positions.
- No trade execution without Will approval.
- No using this event to decide unrelated books unless explicitly linked.

---

## Verification / Completion

- Verification needed: <fill prices / screenshot / explicit Will confirmation / none>
- Files to update after action: `<paths>`
- Completion condition: <what makes this operationally done>

## Expiration / Supersession

This card expires after:
- <event is read and decision logged>, or
- <a stronger catalyst supersedes it>, or
- Will explicitly cancels the process.

If a decision is approved but not executed, the card remains live as `WILL_APPROVED` or `BROKER_PENDING`; it does **not** expire silently.
