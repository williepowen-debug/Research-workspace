# PROME STATUS.md
**Updated:** 2026-06-19 21:15 ET (OpenClaw Prome — CORAL Phase 1 pushed; Geneva heartbeat local)

## Core State

**Operational priority:** CORAL Phase 1 maturity scaffold is now on origin: `SCRATCH.md`, `NEXUS_BRIEF.md`, `board_log.tsv`, and CLAUDE boot/write-back/WALTER-consumption protocol. WALTER deep-research candidate flag remains active as **CHECKLIST v0.18**; Prome monitors behavior and does not edit WALTER specs directly.

**Market priority:** Geneva de-escalation branch fired: U.S.–Iran MOU / Hormuz reopening / ceasefire framework defers the immediate oil-shock tail but leaves a 60-day fuse. HY OAS **263 [FRED 6/17]** remains 3bp above the <260 kill line; VIX/banks do not confirm cascade; carry remains red (USD/JPY **161.28**, FXY **$56.85** on Jun19 dashboard). Next market lane is HY <260 monitoring + SAM/CFTC carry read + bank/PC re-weakening.

**Current repo reality:** CORAL Phase 1 is pushed; heartbeat + this closeout are local-only unless/until Will asks to push. Continue **pathspec-only** commits; future pushes remain Will-coordinated.

**Regime source:** `HEARTBEAT.md` was updated after the Geneva gate and is the current regime source locally; verify origin if another runtime needs it.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves/scopes it. WALTER deep-research flag tuning is WALTER-owned; Prome monitors behavior after landing.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Geneva MOU defers oil shock; HY 263 near kill; cascade unconfirmed; carry red. |
| `PROME/TODAY.md` | Operator card / immediate lane | Updated for Geneva/de-escalation + HY/CFTC/CORAL next gates. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | WALTER row now includes deep-research flag ratification as Full-WALTER-owned. FOMC row remains HY 263 monitor. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current closeout entry point: heartbeat local; CORAL Phase 1 pushed; HY/SAM/CORAL gates next. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Stale Jun14 map; read only as historical unless refreshed on demand. |
| `PROME/HANDOFF.md` | Live continuity surface | Top entry reflects final synced closeout and WALTER v0.18 landed. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow; repo state first remains mandatory. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Jun19 daily log created for SAM/HAWK audit + WALTER flag design session. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **WALTER Routing v2** | ✅ real path proven | Full path works; Quick mode restricted to registered triggers/backfill only. |
| **WALTER deep-research flag** | ✅ landed / active | CHECKLIST v0.18 ratified and verified: Full-only Phase 2.8, materiality gate, ledger `prompt_ref`+`deadline`, no FORMAT_SPEC header, `walter_doctor` overdue check in v1. |
| **WALTER consumption rollout** | 🟡 OpenClaw progressed / CC pending | CORAL now has board-log intake; next CORAL session should consume pending WALTER handoffs. CC self-apply still pending for some persistent agents. |
| **WALTER cron/feed health** | 🟠 stale upstream feeds | Doctor still flags stale `news-sweep`, `filing-watch`, `SIGNALS/inbound`; not caused by Routing v2. |
| **SAM v1.6** | 🟡 draft / CFTC-gated | Audit fixes incorporated; convexity EV table supports hold-small-stub, not add size. Jun20 CFTC is the next real gate. |
| **HAWK energy-strike framing** | ✅ audit fixes landed | Brent math/reference fixes, product/crack → Brent flip triggers, and BRENT handoff delivery all look clean. |
| **FOMC / Geneva grading** | 🟡 mixed confirmation | Energy shock deferred; HY 263 near kill; VIX/banks benign; carry red. Need HY <260/CFTC-FXY/bank-PC follow-through. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Fresh-window closeout hygiene | ✅ closing out | Core Prome surfaces updated; heartbeat/closeout commit remains local-only unless pushed. |
| HY <260 / post-FOMC confirmation | 🔴 next market lane | Latest HY 263; watch <260, TIC/FXY/carry, and bank/PC re-weakening. |
| WALTER deep-research candidate flag | ✅ active | WALTER landed v0.18; next work is only behavior monitoring / future tuning if noisy or missed flags appear. |
| WALTER Quick-boundary / Full-WALTER standard | ✅ settled | Quick paused for fresh news; Full WALTER routes novel signals and owns research-flag judgment. |
| WALTER Phase 2 consumption rollout | 🟡 mechanical follow-through | CORAL now has mature board-log intake; next CORAL session should consume two pending WALTER signals. CC agents self-apply on next Claude Code spawn after pull. |
| SAM v1.6 CFTC gate | 🟡 next SAM lane | Jun20 CFTC decides whether carry-convexity frame survives, weakens, or strengthens while USD/JPY >161. |
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

Next: fresh-session boot from HEARTBEAT/SCRATCH/TODAY. First verify git state: heartbeat + closeout may be local-only. If market lane, monitor HY <260 / CFTC-FXY / banks-PC; if CORAL lane, consume pending WALTER signals; if WALTER lane, monitor v0.18 behavior/doctor. Do not touch positions without Will/broker truth.
