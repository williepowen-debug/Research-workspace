# PROME STATUS.md
**Updated:** 2026-06-20 14:59 ET (OpenClaw Prome — CORAL inbox + thesis rails installed/pushed)

## Core State

**Operational priority:** CORAL is now through the first maturity pass: boot situational card, WALTER board-log intake, processed WALTER inbox, NEXUS brief, and installed thesis rails are all on origin. Next CORAL work is analytical, not plumbing: per-metro convergence grid and Q2 FL-bank earnings prep.

**Market priority:** Geneva de-escalation branch remains the current regime source in `HEARTBEAT.md`: immediate Hormuz/oil-shock tail deferred, HY OAS **263 [FRED 6/17]** still near the <260 kill line, VIX/banks not confirming cascade, carry remains red (USD/JPY/FXY). Next market lane is HY <260 monitoring + SAM/CFTC carry read + bank/PC re-weakening.

**Current repo reality:** clean and synced to origin as of closeout. All today’s CORAL/Prome changes were committed and pushed.

**Regime source:** `HEARTBEAT.md` remains current enough (<48h) and should not be rewritten just for CORAL system-work hygiene.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves/scopes it. Today’s CORAL edits were explicitly scoped. WALTER deep-research flag tuning remains WALTER-owned; Prome monitors behavior and coordinates.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Geneva MOU defers oil shock; HY 263 near kill; cascade unconfirmed; carry red. |
| `PROME/TODAY.md` | Operator card / immediate lane | Updated for Jun20 closeout: CORAL thesis rails installed; repo synced; market gates unchanged. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | CORAL row now reflects inbox processed + thesis rails installed; next work is per-metro/Q2 prep. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current closeout entry point: CORAL complete through thesis rails; repo clean/synced. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Stale Jun14 map; read only as historical unless refreshed on demand. |
| `PROME/HANDOFF.md` | Live continuity surface | Top entry reflects CORAL boot/inbox/thesis work pushed. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow; repo state first remains mandatory. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Jun20 daily log created for CORAL boot/inbox/thesis installation. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **CORAL maturity** | ✅ boot/inbox/thesis rails installed | Boot card, WALTER processed lane, NEXUS brief, thesis/changelog, and closeout rules are on origin. |
| **CORAL next work** | 🟡 analytical follow-through | Per-metro convergence grid + Q2 FL-bank earnings prep; do not confuse household stress with bank-loss confirmation. |
| **WALTER Routing v2** | ✅ real path proven | Full path works; Quick mode restricted to registered triggers/backfill only. |
| **WALTER deep-research flag** | ✅ landed / active | CHECKLIST v0.18 ratified and verified: Full-only Phase 2.8, materiality gate, ledger `prompt_ref`+`deadline`, no FORMAT_SPEC header, `walter_doctor` overdue check in v1. |
| **WALTER consumption rollout** | 🟡 OpenClaw progressed / CC pending | CORAL consume path now completed; CC recipient self-apply still pending for some persistent agents. |
| **WALTER cron/feed health** | 🟠 stale upstream feeds | Doctor still flags stale `news-sweep`, `filing-watch`, `SIGNALS/inbound`; not caused by Routing v2. |
| **SAM v1.6** | 🟡 draft / CFTC-gated | Audit fixes incorporated; convexity EV table supports hold-small-stub, not add size. Jun20 CFTC is the next real gate. |
| **HAWK energy-strike framing** | ✅ audit fixes landed | Brent math/reference fixes, product/crack → Brent flip triggers, and BRENT handoff delivery all look clean. |
| **FOMC / Geneva grading** | 🟡 mixed confirmation | Energy shock deferred; HY 263 near kill; VIX/banks benign; carry red. Need HY <260/CFTC-FXY/bank-PC follow-through. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| CORAL boot/inbox/thesis hardening | ✅ complete | All today’s CORAL changes committed/pushed; WALTER inbox 0 pending; thesis v1.0 installed. |
| CORAL per-metro convergence grid | 🟡 next CORAL lane | Miami/Tampa/Orlando/Jax/SW-FL grid using condo/SF/migration/tourism/negative-equity/bankruptcy/insurance vectors. |
| CORAL Q2 FL-bank prep | 🟡 next CORAL lane | Focus diagnostic: synchronized deterioration across ≥2 FL-exposed banks or explicit USCB condo-association loan deterioration with corroboration. |
| HY <260 / post-FOMC confirmation | 🔴 next market lane | Latest HY 263; watch <260, TIC/FXY/carry, and bank/PC re-weakening. |
| WALTER deep-research candidate flag | ✅ active | WALTER landed v0.18; next work is behavior monitoring / future tuning only if noisy or missed flags appear. |
| WALTER Quick-boundary / Full-WALTER standard | ✅ settled | Quick paused for fresh news; Full WALTER routes novel signals and owns research-flag judgment. |
| WALTER Phase 2 consumption rollout | 🟡 mechanical follow-through | CORAL is done; remaining CC agents self-apply on next Claude Code spawn after pull. |
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

Next: fresh-session boot from HEARTBEAT/SCRATCH/TODAY. First verify git state, expected clean/synced. If CORAL lane, build the per-metro convergence grid or Q2 bank prep. If market lane, monitor HY <260 / CFTC-FXY / banks-PC. If WALTER lane, monitor v0.18 behavior/doctor. Do not touch positions without Will/broker truth.
