# PROME STATUS.md
**Updated:** 2026-06-21 10:04 ET (OpenClaw Prome — post-closeout hygiene: BOOT/HEARTBEAT freshness + HANDOFF tighten)

## Core State

**Operational priority:** AGENTS/PROME organization pass is complete and pushed. Grouped AGENTS indexes are live, canonical topology lives in `AGENTS/_NETWORK.md`, dashboard network rendering is updated, standalone dashboard network is demoted to a pointer, live Prome docs no longer point at retired `PROME/TOSCANINI/`, and repeated Sunday respawns now have an explicit market-freshness gate in `PROME/BOOT.md`.

**Market priority:** unchanged from `HEARTBEAT.md`: signed-but-fraying MOU; Hormuz re-closure declared; official/declaratory/contested, not yet kinetic. Energy tail is re-fat, broad cascade still unconfirmed. Next market lane is Jun22 Brent/vol/traffic response, HY <260 monitoring, SAM/CFTC carry read, and bank/PC re-weakening.

**Current repo reality:** clean and synced to origin after pushed cleanup and closeout commits. Latest pushed sequence: grouped AGENTS indexes, Prome path/network cleanup, closeout log, BOOT weekend freshness gate, HEARTBEAT weekend hygiene, and HANDOFF tighten.

**Regime source:** `HEARTBEAT.md` is current as orientation. Jun21 hygiene added a weekend freshness note; no fresh Sunday market data was pulled.

**Standing constraint:** **do not edit `AGENTS/*` domain files** unless Will explicitly approves/scopes it. Index/topology docs under `AGENTS/_*.md` are Prome/system surfaces, but domain agents still own their folders.

---

## Live Surfaces / Ownership

| Surface | Role | Current note |
|---|---|---|
| `HEARTBEAT.md` | Regime, dashboard, thresholds, near gates | Hormuz re-closure declared; contested/not kinetic; energy tail re-fat; cascade unconfirmed. Jun21 hygiene labels Fri-close levels as orientation-only. |
| `PROME/TODAY.md` | Operator card / immediate lane | Updated for Jun21 closeout: organization pass complete; no fresh market refresh. |
| `PROME/ACTIVE_DECISIONS.md` | Safety index for trade/expiry rails | No decision moved in AGENTS/PROME organization pass; leave existing trade/system rails unchanged. |
| `PROME/SCRATCH.md` | Working notes / latest session entry | Current closeout entry point: grouped views + path cleanup + canonical network map pushed. |
| `PROME/FLEET_SCAN.md` | Conditional fleet map | Stale Jun14 map; read only as historical unless refreshed on demand. |
| `PROME/HANDOFF.md` | Live continuity surface | Tightened to 3 live entries; top entry reflects AGENTS cleanup + weekend freshness hygiene. |
| `AGENTS/_INDEX.md` | Grouped directory view | Live navigation layer; canonical paths remain flat. |
| `AGENTS/_NETWORK.md` | Canonical topology map | Live source for agent network/transmission topology. |
| `dashboard/index.html` | Visual dashboard | Network tab mirrors `AGENTS/_NETWORK.md`; standalone `dashboard/network.html` is pointer/redirect only. |
| `PROME/BOOT.md` / `PROME/CLOSEOUT.md` | Start/end procedures | Follow; repo state first remains mandatory. |
| `MEMORY.md` / `memory/YYYY-MM-DD.md` | Durable kernels / daily logs | Jun21 daily log captures organization/path/network cleanup. |

---

## Agent / System Health Watch

| Lane | Status | Prome read |
|---|---|---|
| **AGENTS directory organization** | ✅ pushed | Grouped indexes are live; no physical agent-folder moves. |
| **Canonical network map** | ✅ pushed | `AGENTS/_NETWORK.md` is source of truth; dashboard is rendering. |
| **Dashboard network drift** | ✅ reduced | `dashboard/network.html` demoted to pointer; main dashboard tab updated. |
| **PROME stale path refs** | ✅ cleaned | Live Prome docs no longer reference retired Toscanini paths; path checks clean before push. |
| **BOOT freshness gate** | ✅ codified | Weekends/market holidays: HEARTBEAT is orientation only; refresh dashboard/FRED before citing current levels. |
| **HEARTBEAT / regime** | ✅ refreshed Jun20 + hygiene Jun21 | Hormuz re-closure declared Jun20; contested/not kinetic; Jun22 tape is next confirmation; Fri-close dashboard levels labeled orientation-only. |
| **HANDOFF live surface** | ✅ tightened | Reduced to 3 entries; stale push-state and pre-DEWEY wording cleared. |
| **Auto-memory load cap** | ✅ compacted Jun20 | `memory/auto/MEMORY.md` under cap with all 143 links preserved; future compaction should be coordinated. |
| **DEWEY root naming** | ✅ aligned | HEARTBEAT + `AGENTS_DIRECTORY.md` now use DEWEY; WALTER-specific follow-up belongs to WALTER. |
| **CORAL maturity** | ✅ boot/inbox/thesis rails installed | Boot card, WALTER processed lane, NEXUS brief, thesis/changelog, and closeout rules are on origin. |
| **WALTER Routing / DEWEY loop** | 🟡 WALTER-owned cleanup pending | Prome found stale push/registry wording Jun20; Will will pass directly to WALTER. Prome should not edit WALTER unless scoped. |
| **SAM v1.6 / carry** | 🟡 CFTC-gated | Juneteenth-delayed CFTC read tests carry-convexity frame while USD/JPY >161. |
| **Hormuz / energy tail** | 🟠 re-fat, unconfirmed | Declaratory closure is not physical escalation until behavior/tape confirms. |
| **Position/broker reconciliation** | 🟠 pending | Keep separate from repo/doc cleanup; no expiry action without broker/Will truth. |

---

## Current Work Queue

| Lane | Priority | Status / owner note |
|---|---:|---|
| Jun22 Brent / Hormuz tape test | 🔴 next market lane | First real test of whether Jun20 declaration stays coercive/non-physical or reprices energy/vol. |
| HY <260 / post-FOMC confirmation | 🔴 next market lane | Latest HEARTBEAT HY 263; watch <260, CFTC/FXY/carry, and bank/PC re-weakening. |
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

- **No agent domain edits** unless Will explicitly changes the constraint.
- **No trade execution without Will approval.**
- **No trade recommendations unless explicitly requested.**
- **No external/public messages without approval.**
- **Old trade rails are verification-required** until broker/Will reconciliation.
- **WALTER routes signals/news; Prome maintains state, tasking, rails, and Will-facing synthesis.**
- **Canonical paths remain flat:** do not move `AGENTS/<NAME>/` without migration tooling and tests.
- **One live network map:** `AGENTS/_NETWORK.md` is canonical; dashboard is rendering only.
- **Pathspec commits only;** never `git add .`, `git add -A`, broad reset/stash, force-push, or stash/reset unknown work.
- **Push is Will-coordinated** — commit locally when scoped; push only on Will's explicit call.
- Read current files before editing; verify after edits.

---

## Next Best Action

Fresh boot should verify git state, expected clean/synced after the latest hygiene push, then choose lane. Market lane = treat HEARTBEAT as Sunday orientation only, refresh dashboard/FRED before citing current levels, and watch Jun22 Brent/Hormuz + HY <260 + CFTC/carry. System lane = use `AGENTS/_INDEX.md` and `AGENTS/_NETWORK.md`; do not create a second live map. Position lane remains blocked on broker/Will truth.
