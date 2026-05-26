# ACTIVE_DECISIONS.md
**Created:** 2026-05-23 15:20 ET
**Owner:** Prome
**Purpose:** Boot-readable index of live decisions that are not terminal. Full logic stays in action cards / execution rails.

---

## Rules

- Include decisions in non-terminal states: `DRAFT`, `PROPOSED`, `WILL_APPROVED`, `BROKER_PENDING`, `ORDER_PLACED`, `FILLED`, `POSITION_UPDATED`, `LOGGED`, `DEFERRED`.
- Remove or archive when terminal: `COMPLETED`, `REJECTED`, `EXPIRED`, `SUPERSEDED`, `CANCELLED`.
- Keep this file short. It is an index, not a thesis document.
- Every row must name an owner, next action, backstop, and source file.

---

## Live Decision Index

| Decision | State | Owner | Next | Backstop | Source |
|---|---|---|---|---|---|
| TLT Jun 18 $85P ×3 2/1 roll | `BROKER_PENDING` | Will → broker; Prome → post-fill files | Tue 5/27 open: place sell 3× Jun18 $85P / buy 1× Sep19 $85P if invalidation has not fired | 2026-06-06 EOD | `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` |
| 6/18 theta-killer cluster | `WILL_APPROVED` | Prome (daily monitor); Will (approval at any trigger fire) | Daily dashboard scan of R1-R4 + position-specific WAL/KRE/EGBN levels; on fire, spawn named domain agent → fresh Will approval for any roll | Hard operational backstop 2026-06-16 16:00 ET | `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` + `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` (v0.2 WILL_APPROVED) + `PROME/action-cards/JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md` (§ Decision Log) |

---

## Next Candidate Rows

Add these when their rails/action cards become concrete enough:

- SAM Sep-18 $60C × 5-10 contracts — pending post-CPI cheaper entry.
- FXY $58C reconciliation — SAM v1.4 says held; missing from 5/21 CSV.
- TLT $88P May 15 disposition unknown.
- VIOLET 4/15 VIX/SKEW trade adjudication — 60d window closes ~6/12.
- APD long thesis tag unassigned.
- WAL Sep $67.5P × N — fresh Q2-print exposure (REGINALD V2.2 Bear-medium 30% dominant, EV $67.98, Q2 print late-July). Decision window opens at 6/13 EOD review or paired with 6/16 backstop sweep, whichever fires first. v0.2 6/18 cluster rail explicitly silent on this gap (disclosed in `PROME/action-cards/JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md` § "Outside this rail").
- AAL Jul 17 $10P × 1 — standalone orphan, decision deferred until 6/18 cluster sweep clears. No domain owner (airline). Surface post-6/16 backstop.
