# PROME STATUS.md
**Updated:** 2026-06-17 11:05 ET (OpenClaw Prome — closeout before clear; WALTER direct-routing next)

## Core State

**Operational priority:** next system-work lane is WALTER delivery architecture: keep BOARD as canonical archive, but move operational delivery to recipient-local `AGENTS/{AGENT}/inbox/WALTER/` handoff files. FOMC/HY kill-line remains today's market gate.

**Current repo reality:** pulled WALTER's latest GitHub updates cleanly. WALTER self-audit tooling is now present; closeout edits are local until committed. Continue **pathspec-only** staging/commits; push only when Will explicitly approves.

**Regime source:** `HEARTBEAT.md` carries the current pre-FOMC regime read. Refresh dashboard/proxies before reusing levels and refresh HEARTBEAT after FOMC if regime changes.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves/scopes it. For WALTER architecture changes, prefer spawning/instructing WALTER to edit its own domain.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Pre-FOMC regime file; refresh after FOMC or before citing live levels. Latest dashboard pull during session: HY 271 [6/16] / CCC 944 [6/16] / Brent 80.72 / VIX 16.55. |
| `PROME/TODAY.md` | Operator card / immediate lane | Needs post-clear refresh if market/FOMC work starts; WALTER direct-routing is next system-work lane. |
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
| **WALTER intake/routing** | 🟠 improved tooling; architecture change pending | 6/16–17 WALTER self-audit tools landed (`version_drift_check.py`, `walter_doctor.py`). Doctor passes spec/BOARD checks but flags stale upstream feeds. Delivery policy still BOARD-only; next change should add recipient-local `inbox/WALTER/` handoffs. |
| **LABOR pushed fixes** | ✅ landed | Functional fixes reviewed cleanly; later LABOR hygiene commit fixed stale handoff/push language. |
| **NEXUS/LABOR brief treatment** | 🟠 propagation/design | Auto-memory supports LABOR standing brief; NEXUS map/brief restructuring may still need follow-through. Not a Prome blocker. |
| **FOMC grading** | 🔴 today | HY 271 [FRED 6/16] remains above the <260 blended-credit kill line. Use live proxy at event time, confirm via FRED T+1. |
| **SHADE artifact hygiene** | ✅ pushed | Raw PDFs stored outside Git; manifest/ignore work pushed. No current blocker. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Prome closeout / clear-window handoff | 🔴 active | SCRATCH/HANDOFF/STATUS/memory updated for WALTER-direct-routing next session; commit locally if desired, push Will-gated. |
| FOMC live grading | 🔴 today | Watch 2Y/front-end, HYG/intraday credit proxy, vol/gamma. Confirm HY OAS next day. |
| WALTER direct-routing architecture | 🟠 next ops lane | Instruct/spawn WALTER to supersede BOARD-only with BOARD-first + recipient-local handoffs; include `.venv` command fix and SIG-W-20260610-001/-002 backfill/audit. |
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

After clear/new window: pull/verify repo, then either (a) continue WALTER direct-routing architecture work by spawning/instructing WALTER, or (b) refresh dashboard/proxies for FOMC grading. Do not trade or touch positions without Will/broker truth.
