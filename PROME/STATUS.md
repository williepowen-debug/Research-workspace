# PROME STATUS.md
**Updated:** 2026-06-17 16:20 ET (OpenClaw Prome — WALTER Routing v2 shipped; post-FOMC handoff)

## Core State

**Operational priority:** WALTER Routing v2 Phase 1 is shipped. Next system-work lane is PROME-side follow-through: Phase 2 recipient consumption rollout, Quick-WALTER live acceptance test, and clean-tree push behavior for IMMEDIATE/FLASH deliveries to Claude Code recipients.

**Market priority:** FOMC happened; do not update regime from the first impulse alone. Next market-work lane is post-FOMC synthesis with fresh dashboard/proxies and FRED T+1 HY confirmation.

**Current repo reality:** WALTER pushed to GitHub and Prome pulled cleanly. Repo was clean/synced before this closeout. Prome closeout edits are local until committed. Continue **pathspec-only** commits; push only when Will explicitly approves.

**Regime source:** `HEARTBEAT.md` is still pre-FOMC. Refresh after a proper post-FOMC synthesis if regime changed. Latest dashboard snapshot is in `PROME/SCRATCH.md` / `TODAY.md`.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves/scopes it. WALTER owns WALTER-domain edits; recipient agents own their own consume-step integration.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Pre-FOMC. Needs update only after proper post-FOMC regime read. |
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
| **FOMC grading** | 🔴 post-event synthesis pending | Initial QQQ reaction was risk-off/whipsaw with absorption bounce. Need fresh cross-asset read and HY OAS T+1 before regime conclusion. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Post-closeout / fresh window boot | 🔴 active | Pull/verify repo; read SCRATCH/TODAY/ACTIVE_DECISIONS. |
| Post-FOMC synthesis | 🔴 next market lane | Use fresh 2Y/HYG/VIX/USDJPY/TLT/credit proxy; confirm HY OAS via FRED 6/18. |
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

After `/new`: boot clean, then choose lane: (a) post-FOMC synthesis with T+1 HY confirmation discipline, or (b) WALTER Phase 2 / Quick-WALTER acceptance test. Do not touch positions without Will/broker truth.
