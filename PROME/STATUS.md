# PROME STATUS.md
**Updated:** 2026-06-20 20:05 ET (OpenClaw Prome — heartbeat/automemory/DEWEY cleanup + pushed-agent audit)

## Core State

**Operational priority:** Jun20 push train is clean from Prome’s side: HEARTBEAT refreshed for Hormuz re-closure, auto-memory index compacted under cap, active-agent commits audited after pull, and root DEWEY naming aligned. Remaining WALTER-specific drift is Will→WALTER, not Prome-owned.

**Market priority:** current regime source is `HEARTBEAT.md`: signed-but-fraying MOU; Hormuz re-closure declared; official/declaratory/contested, not yet kinetic. Energy tail is re-fat, broad cascade still unconfirmed. Next market lane is Jun22 Brent/vol/traffic response, HY <260 monitoring, SAM/CFTC carry read, and bank/PC re-weakening.

**Current repo reality:** clean and synced to origin after closeout push; latest pushed Prome/root work aligned DEWEY naming, fixed HEARTBEAT’s stale RESEARCHER path, and closed out the Jun20 push-train cleanup.

**Regime source:** `HEARTBEAT.md` is current. Boot from it rather than old Geneva-only TODAY/HANDOFF text.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves/scopes it. WALTER-specific cleanup is being handled directly by Will/WALTER; Prome should monitor only unless scoped.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Hormuz re-closure declared; contested/not kinetic; energy tail re-fat; cascade unconfirmed. |
| `PROME/TODAY.md` | Operator card / immediate lane | Updated for Jun20 end-of-thread closeout: push audit, DEWEY cleanup, near gates. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | Updated for Hormuz re-fat + DEWEY/auto-memory/audit state; trade rows remain verification-required. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current closeout entry point: heartbeat/automemory/DEWEY cleanup complete; repo expected clean/synced. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Stale Jun14 map; read only as historical unless refreshed on demand. |
| `PROME/HANDOFF.md` | Live continuity surface | Top entry reflects Jun20 heartbeat/automemory/DEWEY cleanup + audit. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow; repo state first remains mandatory. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Jun20 daily log includes CORAL work plus later heartbeat/automemory/DEWEY/audit session. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **HEARTBEAT / regime** | ✅ refreshed | Hormuz re-closure declared Jun20; contested/not kinetic; Jun22 tape is next confirmation. |
| **Auto-memory load cap** | ✅ compacted | `memory/auto/MEMORY.md` under cap with all 143 links preserved; future compaction should be coordinated. |
| **Active-agent push audit** | ✅ clean enough | 15 commits pulled clean; WALTER/version/TSV/script checks passed; issues are state drift, not breakage. |
| **DEWEY root naming** | ✅ aligned | HEARTBEAT + `AGENTS_DIRECTORY.md` now use DEWEY; WALTER-specific follow-up belongs to WALTER. |
| **CORAL maturity** | ✅ boot/inbox/thesis rails installed | Boot card, WALTER processed lane, NEXUS brief, thesis/changelog, and closeout rules are on origin. |
| **CORAL next work** | 🟡 analytical follow-through | Per-metro convergence grid + Q2 FL-bank earnings prep; do not confuse household stress with bank-loss confirmation. |
| **WALTER Routing / DEWEY loop** | 🟡 WALTER-owned cleanup pending | Prome found stale push/registry wording; Will will pass directly to WALTER. Prome should not edit WALTER unless scoped. |
| **WALTER cron/feed health** | 🟠 stale upstream feeds | Doctor still flags stale `news-sweep`, `filing-watch`, `SIGNALS/inbound`; Scout/VPS-track, not a Prome closeout fix. |
| **SAM v1.6 / carry** | 🟡 CFTC-gated | Juneteenth-delayed CFTC read tests carry-convexity frame while USD/JPY >161. |
| **Hormuz / energy tail** | 🟠 re-fat, unconfirmed | Declaratory closure is not physical escalation until behavior/tape confirms. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Jun22 Brent / Hormuz tape test | 🔴 next market lane | First real test of whether Jun20 declaration stays coercive/non-physical or reprices energy/vol. |
| HY <260 / post-FOMC confirmation | 🔴 next market lane | Latest HY 263; watch <260, CFTC/FXY/carry, and bank/PC re-weakening. |
| SAM v1.6 CFTC gate | 🟡 next SAM lane | Delayed CFTC read decides whether carry-convexity frame survives, weakens, or strengthens while USD/JPY >161. |
| WALTER follow-up | 🟡 Will→WALTER | WALTER-specific push/registry/DEWEY drift found by Prome audit; Will will handle personally. |
| DEWEY first live run | 🟡 pending | Phase 2 wiring shipped; first live run requires CONTEXT refresh first. |
| CORAL per-metro convergence grid | 🟡 next CORAL lane | Miami/Tampa/Orlando/Jax/SW-FL grid using condo/SF/migration/tourism/negative-equity/bankruptcy/insurance vectors. |
| CORAL Q2 FL-bank prep | 🟡 next CORAL lane | Focus diagnostic: synchronized deterioration across ≥2 FL-exposed banks or explicit USCB condo-association loan deterioration with corroboration. |
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

Next: fresh-session boot from HEARTBEAT/SCRATCH/TODAY. First verify git state, expected clean/synced. If market lane, watch Jun22 Brent/Hormuz tape response + HY <260 + CFTC/carry. If system lane, wait for WALTER’s own cleanup rather than editing WALTER. If DEWEY lane, refresh CONTEXT before first live run. Do not touch positions without Will/broker truth.
