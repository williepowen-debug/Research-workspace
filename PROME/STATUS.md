# PROME STATUS.md
**Updated:** 2026-06-16 16:12 ET (OpenClaw Prome — NEXUS/WALTER/LABOR review closeout)

## Core State

**Operational priority:** preserve Will’s attention by running Prome as chief-of-staff / reviewer: coordinate agent pushes, verify consistency, surface system-health defects, and keep trade-facing rails honest. Current highest operational lane is **WALTER intake/routing integrity**, not a new market-thesis rewrite.

**Current repo reality:** local branch is behind origin after LABOR/NEXUS pushed updates and still has unpushed Prome commits. Push/rebase remains Will-coordinated. Continue **pathspec-only** staging/commits; no broad git ops.

**Regime source:** use `HEARTBEAT.md` for market/regime dashboard, but refresh live before citing prices/levels. Current review used HY OAS 266 [FRED 6/15] as a load-bearing FOMC/R3 kill proximity fact; confirm next day because FRED HY OAS is T+1.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves. Agent files are read-only inputs for Prome unless that constraint changes.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Needs live refresh if used for fresh market levels. |
| `PROME/TODAY.md` | Operator card / immediate lane | Older boot card; use with current SCRATCH until next full boot refresh. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | Verification-required until broker/Will reconciliation. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current NEXUS/WALTER/LABOR review closeout and next entry point. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Read on demand; not mandatory boot context. |
| `PROME/HANDOFF.md` | Live continuity surface | Current entry points to WALTER diagnosis and FOMC grading. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow before new session / closeout; push remains Will-gated. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Daily log updated with NEXUS/WALTER/LABOR review state. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **NEXUS synthesis** | ✅ passed review | ORC four-group read substantially corroborated NEXUS matrix. No row overturned. Additions are tension/branch framing, not matrix reversal. |
| **WALTER intake/routing** | 🔴 degraded / diagnose next | Evidence suggests stale content and possible silent dispatch drop to BRENT/HAWK. Treat WALTER/NEXUS inbox completeness as degraded until receipt trail is verified. |
| **LABOR pushed fixes** | ✅ merge-safe with cleanup nits | Boot/scripts tested from origin temp worktree. Remaining issues are stale STATUS language and NEXUS `BRIEFS_MAP` alignment if LABOR brief becomes standing surface. |
| **NEXUS BRIEFS_MAP** | 🟠 needs propagation | Map still treats LABOR as Tier-2 / brief not required despite new LABOR `NEXUS_BRIEF.md` and Will’s apparent standing-brief intent. |
| **FOMC grading** | 🔴 near gate | HY 266 is only 6bp from <260 blended-credit kill. Grade sustained move; use intraday proxy live and FRED confirmation next day. |
| **SHADE artifact hygiene** | 🟠 local Prome commits only | Raw PDFs stored outside Git; manifest/ignore work local. Push only with Will approval. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; do not infer execution from rails. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| WALTER diagnosis-first repair | 🔴 next operational lane | Confirm dormant vs cron/feed vs dispatch-path bug vs running-not-committing. Trace SIG-W-20260610-001/-002 to BRENT/HAWK inbox write. Add health/receipt discipline. |
| FOMC live grading | 🔴 near-term | Watch 2Y/front-end, HYG/intraday credit proxy, vol/gamma. Confirm HY OAS next day. |
| LABOR/NEXUS cleanup | 🟠 small | LABOR stale STATUS lines; NEXUS `BRIEFS_MAP.md` LABOR brief treatment. Read-only review unless Will scopes edits. |
| Local Prome push decision | 🟠 Will-gated | Decide whether/when to push local Prome commits: SHADE recovery/closeout/raw-artifact-store work plus current closeout. |
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
- **Push is Will-coordinated** — commit locally only; push only on Will's explicit call.
- Read current files before editing; verify after edits.

---

## Next Best Action

Run a WALTER diagnosis-first pass unless Will pivots: verify freshness, cron/feed state, and routing receipts before relying on WALTER/NEXUS inbox completeness for FOMC/post-FOMC synthesis.
