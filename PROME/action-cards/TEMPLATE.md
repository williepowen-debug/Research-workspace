# <Event / Decision> Action Card
**Created:** YYYY-MM-DD HH:MM ET  
**Status:** Draft / Active / Expired / Superseded  
**Event / Decision Window:** <date/time or condition>  
**Pre-build / Domain source:** `<path>`  
**Position snapshot:** `PROME/POSITIONS.md` updated <date>  
**Decision-flow spec:** `PROME/DECISION_FLOW.md`

---

## Objective

<State the specific decision this card is meant to discipline.>

This card is **not** a trade order. It defines allowed/forbidden actions and the decision prompts to bring to Will. Any trade or external action requires Will’s approval.

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

---

## Execution Checklist

1. Pull actual event/source data.
2. Extract the decisive metrics.
3. Classify branch against pre-set thresholds.
4. Pull live tape/dashboard if markets are open.
5. Apply this Action Card.
6. If proposing action, give Will max 2 options and one recommendation.
7. Log final decision in `PROME/TRADE_DECISIONS.md`.
8. Update `HEARTBEAT.md` if the regime, catalyst queue, or pending decisions changed.

---

## Forbidden Actions

- No changing thresholds after the event unless the pre-build is demonstrably invalid.
- No revenge-adds to repair losing positions.
- No trade execution without Will approval.
- No using this event to decide unrelated books unless explicitly linked.

---

## Expiration / Supersession

This card expires after:
- <event is read and decision logged>, or
- <a stronger catalyst supersedes it>, or
- Will explicitly cancels the process.
