# PROME STATUS.md
**Updated:** 2026-06-17 17:15 ET (OpenClaw Prome — post-FOMC regime update)

## Core State

**Operational priority:** WALTER Routing v2 Phase 1 is shipped. Next system-work lane is PROME-side follow-through: Phase 2 recipient consumption rollout, Quick-WALTER live acceptance test, and clean-tree push behavior for IMMEDIATE/FLASH deliveries to Claude Code recipients.

**Market priority:** Post-FOMC update is done: hawkish-of-pricing branch fired, broad cascade not confirmed. Next market-work lane is 6/18 confirmation: FRED HY OAS, claims, TIC/FXY, and persistence in VIX/HYG/KRE/WAL.

**Current repo reality:** WALTER pushed to GitHub and Prome pulled cleanly. Repo was clean/synced before this closeout. Prome closeout edits are local until committed. Continue **pathspec-only** commits; push only when Will explicitly approves.

**Regime source:** `HEARTBEAT.md` is post-FOMC as of 17:15 ET. Latest dashboard snapshot is in `HEARTBEAT.md` / `PROME/TODAY.md`.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves/scopes it. WALTER owns WALTER-domain edits; recipient agents own their own consume-step integration.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Post-FOMC hawkish re-arm / unresolved divergence. |
| `PROME/TODAY.md` | Operator card / immediate lane | Updated for WALTER v2 landed + post-FOMC next rails. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | WALTER row moved to Phase-1 shipped / Phase-2 pending. FOMC row remains monitor-only pending T+1 HY/post-event synthesis. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current closeout entry point. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Stale Jun14 map; read only as historical unless refreshed on demand. |
| `PROME/HANDOFF.md` | Live continuity surface | Top entry should reflect WALTER v2 shipped and next PROME-side work. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow; repo state first remains mandatory. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Daily log appended for WALTER v2 and FOMC chart-learning session. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **WALTER Routing v2** | ✅ Phase 1 shipped | BOARD-first archive + recipient-local `inbox/WALTER/` handoffs landed. `delivery_log.tsv`, Quick/Full mode, Iran-anchor guard, git-derived written-but-undelivered telemetry, and narrow BRENT/HAWK backfills reviewed. |
| **WALTER consumption rollout** | 🟠 pending / PROME-side coordination | Phase 2 consume boot-step not rolled out. Expect delivered-but-unconsumed nags after 2d if not addressed; that is intended anti-rot telemetry. |
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
| WALTER Phase 2 consumption rollout | 🟠 next system lane | Coordinate recipient consume-step rollout; OpenClaw agents first; do not directly edit recipient docs unless scoped. |
| Quick-WALTER acceptance test | 🟠 pending | PROME-spawned route-only test to validate BOARD + delivery file + delivery_log + anchor guard. |
| IMMEDIATE/FLASH → CC push behavior | 🟠 pending operational rail | PROME owns clean-tree scoped commit + normal push behavior when urgent delivery to Claude Code recipient requires origin. |
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

Next: either monitor 6/18 post-FOMC confirmation data or continue WALTER Phase 2 / Quick-WALTER acceptance test. Do not touch positions without Will/broker truth.
