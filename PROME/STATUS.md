# PROME STATUS.md
**Updated:** 2026-06-16 16:44 ET (OpenClaw Prome — state correction before next work)

## Core State

**Operational priority:** get Prome’s own surfaces accurate before more agent/theory work. Current state is clean/synced repo, refreshed dashboard, WALTER partially repaired, NEXUS matrix review passed, and FOMC/HY kill-line as the live near gate.

**Current repo reality:** clean and synced with `origin/master` after pulling fresh WALTER + memory updates. Earlier Prome local commits were pushed; no local ahead/behind blocker remains. Continue **pathspec-only** staging/commits; push only when Will explicitly approves.

**Regime source:** `HEARTBEAT.md` now carries the current 6/16 dashboard/regime read. Refresh live before reusing prices/levels.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves. Agent files are read-only inputs for Prome unless that constraint changes.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Refreshed 6/16 ~16:44 ET; HY 266 / CCC 937 / Brent 79.49 / VIX 16.41. |
| `PROME/TODAY.md` | Operator card / immediate lane | Refreshed 6/16; objective is Prome state correction before next work. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | Updated for FOMC/HY kill-line and BOJ-done/expiry context; broker truth still required. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current state correction and next entry point. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Stale Jun14 map; read only as historical unless refreshed on demand. |
| `PROME/HANDOFF.md` | Live continuity surface | Current entry should say clean/synced + WALTER partially repaired. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow; repo state first remains mandatory. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Daily log should record Prome state correction if this pass commits. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **NEXUS synthesis** | ✅ passed review | ORC four-group read substantially corroborated matrix. No row overturned. Additions are tension/branch framing, not reversal. |
| **WALTER intake/routing** | 🟠 partially repaired | 6/16 WALTER anchor/registry/staleness sweep pushed. Still need routing receipts + cron/feed health before treating inbox completeness as reliable. |
| **LABOR pushed fixes** | ✅ landed | Functional fixes reviewed cleanly; later LABOR hygiene commit fixed stale handoff/push language. |
| **NEXUS/LABOR brief treatment** | 🟠 propagation/design | Auto-memory supports LABOR standing brief; NEXUS map/brief restructuring may still need follow-through. Not a Prome blocker. |
| **FOMC grading** | 🔴 near gate | HY 266 is only 6bp from <260 blended-credit kill. Use live proxy at event time, confirm via FRED T+1. |
| **SHADE artifact hygiene** | ✅ pushed | Raw PDFs stored outside Git; manifest/ignore work pushed. No current blocker. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Prome surface correction | 🔴 active | Refresh TODAY/HEARTBEAT/STATUS/SCRATCH/HANDOFF/ACTIVE_DECISIONS; commit/push after verification. |
| FOMC live grading | 🔴 near-term | Watch 2Y/front-end, HYG/intraday credit proxy, vol/gamma. Confirm HY OAS next day. |
| WALTER diagnosis continuation | 🟠 next ops lane | Confirm cron/feed state, routed-signal receipts, and whether BRENT/HAWK SIG-W-001/-002 drop is resolved. |
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

Finish this Prome surface correction, verify diffs, commit/push if Will wants GitHub current. Then choose between FOMC prep, WALTER routing-health diagnosis, or position reconciliation.
