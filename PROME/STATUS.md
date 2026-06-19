# PROME STATUS.md
**Updated:** 2026-06-19 14:53 ET (OpenClaw Prome — SAM/HAWK audits + WALTER deep-research flag greenlight)

## Core State

**Operational priority:** WALTER deep-research candidate flag is greenlit for **WALTER-owned ratification**. Prome should verify the actual landed specs after WALTER implements: CHECKLIST v0.18, 11-col TSV ledger, prompt embed, dispatch_note convention, Quick/Full one-liners, `walter_doctor` overdue check, STATE sync, version-drift check. Prome should not edit WALTER specs directly.

**Market priority:** Post-FOMC confirmation is mixed. HY OAS **263 [FRED 6/17]** remains 3bp above the <260 kill line; claims/VIX/banks do not confirm cascade; carry remains red (USD/JPY **161.27**, FXY **$56.85** on Jun19 dashboard). Next market lane is HY <260 monitoring + TIC/FXY + bank/PC re-weakening.

**Current repo reality:** closeout edits are intended to be **local-only** until Will approves push. Continue **pathspec-only** commits; do not push this closeout per Will's instruction.

**Regime source:** `HEARTBEAT.md` is current as regime source; Jun19 dashboard refresh is in `PROME/TODAY.md` and did not change the regime read.

**Standing constraint:** **do not edit `AGENTS/*`** unless Will explicitly approves/scopes it. WALTER deep-research flag ratification is WALTER-owned; Prome reviews after it lands.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | HY 263 near kill; broad cascade unconfirmed; carry worse. |
| `PROME/TODAY.md` | Operator card / immediate lane | Updated for Jun19 dashboard + WALTER deep-research flag lane. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | WALTER row now includes deep-research flag ratification as Full-WALTER-owned. FOMC row remains HY 263 monitor. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current closeout entry point: WALTER flag verification or HY/SAM gates. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Stale Jun14 map; read only as historical unless refreshed on demand. |
| `PROME/HANDOFF.md` | Live continuity surface | Top entry reflects WALTER deep-research flag greenlight and local-only closeout. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow; repo state first remains mandatory. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Jun19 daily log created for SAM/HAWK audit + WALTER flag design session. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **WALTER Routing v2** | ✅ real path proven | Full path works; Quick mode restricted to registered triggers/backfill only. |
| **WALTER deep-research flag** | 🟢 greenlit / WALTER ratifies | v0.3 proposal approved: Full-only Phase 2.8, materiality gate, ledger `prompt_ref`+`deadline`, no FORMAT_SPEC header, `walter_doctor` overdue check in v1. |
| **WALTER consumption rollout** | 🟡 OpenClaw progressed / CC pending | BRENT + HAWK consumed backfills; OpenClaw consume steps pushed; CC agents self-apply after pull. |
| **WALTER cron/feed health** | 🟠 stale upstream feeds | Doctor still flags stale `news-sweep`, `filing-watch`, `SIGNALS/inbound`; not caused by Routing v2. |
| **SAM v1.6** | 🟡 draft / CFTC-gated | Audit fixes incorporated; convexity EV table supports hold-small-stub, not add size. Jun20 CFTC is the next real gate. |
| **HAWK energy-strike framing** | ✅ audit fixes landed | Brent math/reference fixes, product/crack → Brent flip triggers, and BRENT handoff delivery all look clean. |
| **FOMC grading** | 🟡 mixed confirmation | HY 263 near kill; claims/VIX/banks benign; carry red. Need HY <260/TIC/FXY/bank-PC follow-through. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Post-closeout / fresh window boot | 🔴 active | Pull/verify repo; read HEARTBEAT/SCRATCH/TODAY/ACTIVE_DECISIONS. Note local closeout may be ahead until Will approves push. |
| HY <260 / post-FOMC confirmation | 🔴 next market lane | Latest HY 263; watch <260, TIC/FXY/carry, and bank/PC re-weakening. |
| WALTER deep-research candidate flag | 🟡 WALTER-owned implementation next | After WALTER lands it, inspect actual CHECKLIST/ledger/doctor diff and version-drift output. |
| WALTER Quick-boundary / Full-WALTER standard | ✅ settled | Quick paused for fresh news; Full WALTER routes novel signals and owns research-flag judgment. |
| WALTER Phase 2 consumption rollout | 🟡 mechanical follow-through | OpenClaw consume capability mostly installed locally; CC agents self-apply on next Claude Code spawn after pull. |
| SAM v1.6 CFTC gate | 🟡 next SAM lane | Jun20 CFTC decides whether carry-convexity frame survives, weakens, or strengthens. |
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
- **Push is Will-coordinated** — commit locally when scoped; push only on Will's explicit call. Current closeout specifically stops short of pushing.
- Read current files before editing; verify after edits.

---

## Next Best Action

Next: fresh-session boot from HEARTBEAT/SCRATCH/TODAY. If system lane, verify WALTER's deep-research flag ratification after he lands it; if market lane, monitor HY <260/TIC/FXY/banks; if SAM lane, check Jun20 CFTC against v1.6 convexity survival. Do not touch positions without Will/broker truth.
