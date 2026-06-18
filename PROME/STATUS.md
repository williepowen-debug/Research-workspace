# PROME STATUS.md
**Updated:** 2026-06-17 21:32 ET (OpenClaw Prome — WALTER delivery-model closeout)

## Core State

**Operational priority:** WALTER Routing v2 real path is proven and BRENT/HAWK loops are durable. Next system-work lane is delivery/push policy design for Will’s real workflow: Prome on VPS routes/signals, while domain-agent work usually happens in Claude Code on desktop/laptop and therefore needs origin visibility.

**Market priority:** Post-FOMC update is done: hawkish-of-pricing branch fired, broad cascade not confirmed. Next market-work lane is 6/18 confirmation: FRED HY OAS, claims, TIC/FXY, and persistence in VIX/HYG/KRE/WAL.

**Current repo reality:** clean working tree, **ahead of origin** with local WALTER/OpenClaw consume rollout + Prome operating-model correction commits. Continue **pathspec-only** commits; push only when Will explicitly approves or when a scoped delivery policy is explicitly adopted.

**Regime source:** `HEARTBEAT.md` is post-FOMC as of 17:15 ET. Latest dashboard snapshot is in `HEARTBEAT.md` / `PROME/TODAY.md`.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves/scopes it. Current exception already used: Will scoped WALTER/OpenClaw consume-step rollout. Future recipient changes need fresh scope or owner self-apply.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Post-FOMC hawkish re-arm / unresolved divergence. |
| `PROME/TODAY.md` | Operator card / immediate lane | Updated for WALTER v2 landed + post-FOMC next rails. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | WALTER row moved to Phase-1 shipped / Phase-2 pending. FOMC row remains monitor-only pending T+1 HY/post-event synthesis. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current closeout entry point: brainstorm WALTER/Prome push/delivery options. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Stale Jun14 map; read only as historical unless refreshed on demand. |
| `PROME/HANDOFF.md` | Live continuity surface | Top entry should reflect WALTER v2 shipped and next PROME-side work. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow; repo state first remains mandatory. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Daily log appended for WALTER v2 and FOMC chart-learning session. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **WALTER Routing v2** | ✅ real path proven | Real `agentId=walter` Quick gate passed, Case B Iran guard fired, BOARD reconciles, delivery/consumption telemetry works. |
| **WALTER consumption rollout** | 🟡 OpenClaw progressed / CC pending | BRENT + HAWK consumed backfills; doctor shows zero in-flight. Remaining OpenClaw consume capability installed locally for BROCK/LIQUID/HENRY/LABOR/NEXUS/VIOLET/SHADE; CC agents self-apply after pull. |
| **WALTER cron/feed health** | 🟠 stale upstream feeds | Doctor still flags stale `news-sweep`, `filing-watch`, `SIGNALS/inbound`; not caused by Routing v2. |
| **NEXUS synthesis** | ✅ pre-FOMC review-passed | ORC four-group read upheld matrix. Needs post-FOMC synthesis if market lane resumes. |
| **LABOR pushed fixes** | ✅ landed | Functional fixes reviewed cleanly; claims 6/18 remains live. |
| **FOMC grading** | ✅ initial post-event update done; confirmation pending | Hawkish-of-pricing branch fired; broad cascade not confirmed. Need 6/18 HY/claims/TIC + persistence. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Post-closeout / fresh window boot | 🔴 active | Pull/verify repo; read SCRATCH/TODAY/ACTIVE_DECISIONS. |
| Post-FOMC confirmation | 🔴 next market lane | Confirm with 6/18 FRED HY OAS, claims, TIC/FXY, VIX/HYG/KRE/WAL persistence. |
| WALTER delivery/push policy | 🔴 next system lane | Brainstorm and choose how Prome commits/pushes routed WALTER signals for Claude Code visibility: immediate, urgency-tiered, or explicit flush queue. |
| WALTER Phase 2 consumption rollout | 🟡 mechanical follow-through | OpenClaw consume capability mostly installed locally; CC agents self-apply on next Claude Code spawn after pull. |
| Quick-WALTER acceptance test | ✅ done | Real `agentId=walter` route-only test validated BOARD + delivery file + delivery_log + Case B Iran guard. |
| IMMEDIATE/FLASH → CC push behavior | 🟠 pending operational rail | Because Will’s agents run mainly in Claude Code, origin push is the real delivery boundary; needs explicit policy/automation. |
| Position-state reconciliation | 🟠 pending | Needed for expiry/trade hygiene; broker/Will truth required. |
| Separate-clones migration | 🟠 deferred | Post-FOMC calm-window decision packet; do not do halfway. |
| Execution-rails design | 🔵 design debt | HYG Jun→Dec failure remains canonical: thesis needs pre-registered ladders and triggers. |

---

## Rules of Engagement

- **No agent edits** unless Will explicitly changes the constraint.
- **No trade execution without Will approval.**
- **No trade recommendations unless explicitly requested.**
- **No external/public messages without approval.**
- **Old trade rails are verification-required** until broker/Will reconciliation.
- **WALTER routes signals/news; Prome maintains state, tasking, rails, and Will-facing synthesis.**
- **Pathspec commits only;** never `git add .`, `git add -A`, broad reset/stash, force-push, or stash/reset unknown work.
- **Push is Will-coordinated** — commit locally when scoped; push only on Will's explicit call.
- Read current files before editing; verify after edits.

---

## Next Best Action

Next: brainstorm WALTER/Prome delivery-push policy from the corrected operating model: Prome routes on VPS, but Claude Code agents need origin visibility. Do not touch positions without Will/broker truth.
