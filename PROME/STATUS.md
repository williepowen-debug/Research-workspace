# PROME STATUS.md
**Updated:** 2026-06-18 14:05 ET (OpenClaw Prome — closeout before fresh session)

## Core State

**Operational priority:** Quick-WALTER boundary is settled. Prome/Quick-WALTER is paused for fresh news/signals and may only execute pre-registered RED-FT / REG-T / safety-net triggers or delivery repair/backfill. Full WALTER owns signal-desk judgment.

**Market priority:** Post-FOMC confirmation is mixed. HY OAS **263 [FRED 6/17]** is 3bp above the <260 kill line; claims/VIX/banks do not confirm cascade; carry stress worsened. Next market lane is HY <260 monitoring + TIC/FXY + bank/PC re-weakening.

**Current repo reality:** clean and synced to origin. Continue **pathspec-only** commits; push only when Will explicitly approves or when a scoped delivery policy is explicitly adopted.

**Regime source:** `HEARTBEAT.md` is current as of 2026-06-18 12:26 ET. Latest dashboard snapshot is in `HEARTBEAT.md` / `PROME/TODAY.md`.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves/scopes it. Current exception already used: Will scoped WALTER/OpenClaw consume-step rollout. Future recipient changes need fresh scope or owner self-apply.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | HY 263 near kill; broad cascade unconfirmed; carry worse. |
| `PROME/TODAY.md` | Operator card / immediate lane | Updated for Jun18 HY/claims gate + Quick-WALTER pause. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | WALTER row moved to Quick-news-paused / Full-WALTER standard. FOMC row updated to HY 263 monitor. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current closeout entry point: fresh session; HY kill-line + possible VERIFY/CONTEXT helper design. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Stale Jun14 map; read only as historical unless refreshed on demand. |
| `PROME/HANDOFF.md` | Live continuity surface | Top entry should reflect WALTER v2 shipped and next PROME-side work. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow; repo state first remains mandatory. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Daily log appended for WALTER v2 and FOMC chart-learning session. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **WALTER Routing v2** | ✅ real path proven | Full path works; Quick mode restricted to registered triggers/backfill only. |
| **WALTER consumption rollout** | 🟡 OpenClaw progressed / CC pending | BRENT + HAWK consumed backfills; OpenClaw consume steps pushed; CC agents self-apply after pull. |
| **WALTER cron/feed health** | 🟠 stale upstream feeds | Doctor still flags stale `news-sweep`, `filing-watch`, `SIGNALS/inbound`; not caused by Routing v2. |
| **NEXUS synthesis** | ✅ pre-FOMC review-passed | ORC four-group read upheld matrix. Needs post-FOMC synthesis if market lane resumes. |
| **LABOR pushed fixes** | ✅ landed | Functional fixes reviewed cleanly; claims 6/18 remains live. |
| **FOMC grading** | 🟡 mixed confirmation | HY 263 near kill; claims/VIX/banks benign; carry worse. Need HY <260/TIC/FXY/bank-PC follow-through. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Post-closeout / fresh window boot | 🔴 active | Pull/verify repo; read HEARTBEAT/SCRATCH/TODAY/ACTIVE_DECISIONS. |
| HY <260 / post-FOMC confirmation | 🔴 next market lane | Latest HY 263; watch <260, TIC/FXY/carry, and bank/PC re-weakening. |
| WALTER Quick-boundary / Full-WALTER standard | ✅ settled | Quick paused for fresh news; Full WALTER routes novel signals. Future work: VERIFY/CONTEXT helper concept. |
| WALTER Phase 2 consumption rollout | 🟡 mechanical follow-through | OpenClaw consume capability mostly installed locally; CC agents self-apply on next Claude Code spawn after pull. |
| Quick-WALTER acceptance test | ✅ superseded by boundary decision | Mechanism worked; use now restricted to registered triggers/backfill. |
| Group-chat VERIFY/CONTEXT helper | 🟡 design idea | Potential helper researches/fact-packs surrounding facts; WALTER still owns routing. |
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

Next: fresh-session boot from HEARTBEAT/SCRATCH. If system lane, design VERIFY/CONTEXT helper; if market lane, monitor HY <260/TIC/FXY/banks. Do not touch positions without Will/broker truth.
