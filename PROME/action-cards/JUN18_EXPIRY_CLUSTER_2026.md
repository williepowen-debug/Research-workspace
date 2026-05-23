# 6/18 Expiry Cluster Action Card
**Created:** 2026-05-23 17:00 ET
**State:** `DRAFT`
**Owner:** Prome
**Next:** Consolidate BROCK + REGINALD calibration replies or apply 2026-05-24 EOD default-pass, then present v0.2 to Will.
**Window:** Now → 2026-06-18 expiry; hard operational backstop 2026-06-16 16:00 ET.
**Backstop:** 2026-06-16 16:00 ET post-FOMC close.
**Default:** If no pre-registered trigger fires, let theta-killer positions expire mechanically.
**Source:** `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md`
**Position:** `FORGE/STATUS.md` 2026-05-21 rehab + source trigger set marks.
**Spec:** `PROME/EXECUTION_RAILS.md` + `PROME/DECISION_FLOW.md`

---

## Objective

Promote the existing FORGE 6/18 trigger set into Prome's standardized action-card / active-decision system without duplicating the source logic.

This card is the **Will-facing wrapper and operational state tracker**. The trigger-set source remains the detailed rail.

This card is **not** a trade order. Any roll, close, or fresh trade requires Will approval.

---

## Source-of-Truth Relationship

| Layer | File | Owns |
|---|---|---|
| Source trigger set | `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` | Detailed R1-R4 triggers, position-specific triggers, dropped positions, calibration tracking |
| Prome wrapper | this file | State, owner, next action, Will-facing summary, promotion into `ACTIVE_DECISIONS.md` |
| Decision log | `PROME/TRADE_DECISIONS.md` | Will approvals/rejections/state changes/outcomes |
| Live cockpit | `PROME/ACTIVE_DECISIONS.md` | Boot-readable state row |

**Rule:** update the FORGE trigger set for trigger details. Update this card for operational state.

---

## Current Cluster Read

The 6/18 problem is not thesis discovery. It is **theta and decision drift**.

Most positions are down ~87–94% and should not be rescued unless a pre-registered regime break or position-specific trigger fires. The default is intentionally harsh: **no trigger = let expire**.

This implements the lesson from the missed HYG Jun→Dec roll: a framework without pre-registered execution rails is only a hypothesis.

---

## Covered Positions

### Theta-killer rail positions

| Position | Source trigger-set ID | Current posture | Default |
|---|---|---|---|
| HYG $75P ×8 | A1 | Public-credit contagion lottery; BROCK-owned calibration pending/default-pass | Let expire unless R2 / sub-90¢ BDC / bank-PC loss trigger fires |
| EGBN $25P ×1 margin | A2 | REGINALD single-name bank residual | Let expire unless R3 + EGBN <$26 or material disclosure fires |
| WAL $65P ×1 | A4 | WAL deep OTM residual | Let expire unless WAL breaks $73 close |
| WAL $67.5P ×2 | A5 | WAL closer residual | Let expire unless WAL breaks $73 close |
| KRE $60P ×1 | A6 | Regional-bank sector residual | Let expire unless R3 or MI3/FFIEC PDD material trigger fires |

### Dropped / mechanical let-expire in source trigger set

| Position | Reason |
|---|---|
| AAL $10P ×2 Jun 18 | No thesis owner; no fake trigger |
| CF $130C ×1 Jun 18 | No active ag-domain owner supporting roll; bigger loss but no rail support |
| AAL Jul 17 $10P ×1 | Standalone; defer until Jun 18 sweep clears |

### Separate logic, not bundled

| Position | Handling |
|---|---|
| TLT Jun 18 $85P ×3 | Separate action card: `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md`; currently `BROKER_PENDING` |
| WAL $85P ×1 | Source trigger set says separate full-premium logic: hold/trim/roll-up based on WAL levels |
| WAL $77.5P ×1 / IWM $257P ×1 / FITB $45P ×2 | Source trigger set: near-money losers, 6/13 EOD review |

---

## Regime-Break Triggers — Summary

Full definitions live in the source trigger set. Summary:

| ID | Condition | Current calibration status |
|---|---|---|
| R1 | VIX ≥ 22 for 2 sessions | Pending HENRY calibration / default-pass |
| R2 | HY OAS ≥ 290 for 2 sessions | Pending BROCK calibration / default-pass |
| R3 | KRE breaks $63 close | Pending REGINALD calibration / default-pass |
| R4 | HY OAS ≥ 320 single close | Pending BROCK calibration / default-pass |

Any one trigger arms cluster-wide review. Two triggers escalate to roll-default unless thesis-state contradicts.

---

## Open Calibration

| Agent | Asked | Due | Status | Prome action |
|---|---|---|---|---|
| BROCK | R2/R4, HYG roll target, sub-90¢ / bank-PC trigger language | 2026-05-24 EOD | No local outbox reply seen at 5/23 boot | Default-pass if no reply; do not spawn BROCK unless Will requests |
| REGINALD | R3, WAL break-zone, WAL/KRE/EGBN roll targets | 2026-05-24 EOD | No local outbox reply seen at 5/23 boot | Default-pass if no reply; persistent agent, do not spawn |
| HENRY | R1/R4-VIX calibration + TLT decision | 2026-05-24 EOD | TLT reply landed and became separate card | Fold TLT result separately; use default R1 if no further reply |

---

## Branch-to-Action Table

| Branch | Evidence | Allowed actions | Forbidden actions | Will decision needed |
|---|---|---|---|---|
| No trigger / vol floor persists | R1-R4 not fired; position-specific triggers not fired | Let theta-killers expire; keep monitoring until backstop | Rolling residual premium to “feel better” | No, unless Will wants to override default |
| One regime trigger fires | Any one of R1-R4 fires | Cluster-wide review; validate affected roll targets; present max 2 options | Automatic size-up; rolling unrelated orphan theses | Yes, if any trade proposed |
| Two regime triggers fire | Two of R1-R4 fire | Escalate toward roll-default for thesis-owned lines unless domain contradiction | Ignoring source trigger set; adding new contracts without approval | Yes |
| Position-specific trigger fires | e.g. WAL <$73; KRE <$63; sub-90¢ BDC loan; bank PC loss disclosure | Act only on affected line(s); request Will approval for roll/close | Bundling unrelated lines into one emotional trade | Yes |
| Hard backstop | 2026-06-16 16:00 ET and no trigger | Apply default: untriggered theta-killers expire mechanically | Reopening debate after backstop without new catalyst | No, unless Will overrides |

---

## Execution Rail

| Trigger | Evidence / threshold | Action | Forbidden action | Owner | Deadline |
|---|---|---|---|---|---|
| C1 Default-pass consolidation | BROCK/REGINALD no reply by 2026-05-24 EOD | Promote source trigger set to v0.2 with pending language removed; present to Will | Waiting indefinitely for calibration | Prome | 2026-05-25 |
| C2 Regime break | Any R1-R4 fires | Run cluster-wide review; validate affected roll targets; ask Will if trade action needed | Silent roll / size-up | Prome + domain owner | Same session if market open |
| C3 Position trigger | Any position-specific trigger in FORGE source fires | Prepare line-specific action prompt for Will | Rolling entire cluster | Prome | Same session if market open |
| C4 Time backstop | No trigger by 2026-06-16 16:00 ET | Apply default let-expire for untriggered theta-killers; log decision | Last-minute rescue trade | Prome | 2026-06-16 close |
| C5 Supersession | New domain file or Will instruction replaces source trigger set | Mark this card `SUPERSEDED`; update `ACTIVE_DECISIONS.md` | Maintaining two conflicting rails | Prome | Same day |

---

## Verification / Completion

- Verification needed: Will approval only if any roll/close/fresh trade is proposed; otherwise backstop/default can be logged by Prome.
- Files to update after action: `PROME/ACTIVE_DECISIONS.md`, `PROME/TRADE_DECISIONS.md`, `FORGE/JOURNAL.md`, and if fills occur `FORGE/STATUS.md` / `PROME/POSITIONS.md` as applicable.
- Completion condition: all 6/18 theta-killer lines are either expired, closed/rolled with fills logged, or explicitly superseded.

---

## Current Recommendation

Keep state as `DRAFT` until calibration deadline/default-pass. Then move to `PROPOSED` and present Will one simple approval packet:

> Adopt the 6/18 trigger set as execution rail v0.2: no trigger = let expire; trigger = named review/roll action; hard backstop 6/16 close.

This is deliberately conservative. It prevents revenge-rolling dead premium while preserving the right to act if the regime actually breaks.
