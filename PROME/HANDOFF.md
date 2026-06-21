# PROME HANDOFF

**Purpose:** Single live continuity surface for Prome across OpenClaw and Claude Code. Keep this file short: latest 3–5 entries only. Archive older entries to `PROME/archive/`.

**Archive:** Full pre-merge OpenClaw + Claude Code handoff history through 2026-06-14 is preserved in `PROME/archive/HANDOFF_2026Q2.md`.

---

## 2026-06-21 ~15:15 ET — Pre-clear handoff after CREED Phase 1–4 revival

**Status:** Repo is clean/synced to origin after CREED Phase 1–4 and memory checkpoint. Latest commits: `ae5b4a59 CREED: add phase 3 refresh`, `e3ea29a0 CREED: install phase 4 thesis rails`, `977b8b0c memory: log CREED revival checkpoint`. No topology changes have been made yet.

**What landed:** CREED is revived as a top-level analytical surface but is **not canonical in the roster/network yet**. Phase 3 source pack is `AGENTS/CREED/research/REFRESH_2026-06-21.md`. Phase 4 rails are `AGENTS/CREED/thesis/THESIS.md`, `AGENTS/CREED/thesis/CHANGELOG.md`, and `AGENTS/CREED/research/INBOX_TRIAGE_2026-06-21.md`. `AGENTS/CREED/CLAUDE.md`, `STATUS.md`, and `REVIVAL_PLAN.md` now point cold boots at the current rails.

**Current CREED thesis:** base case is **selective CRE recognition accelerating**, not broad CRE→bank cascade yet. CMBS/office stress is recognizing faster than banks; edge is when maturity-default/special-servicing stress crosses into bank provisions, reserve coverage deterioration, forced sales, or funding pressure.

**Next suggested work:** Phase 5 topology integration, only if Will approves in the fresh session. Touch only roster/topology surfaces: `AGENTS.md`, `AGENTS_DIRECTORY.md`, `AGENTS/_INDEX.md`, and `AGENTS/_NETWORK.md` as needed. Do **not** move/delete legacy `AGENTS/REGINALD/sub-agents/CREED/`. Do **not** do Phase 6 migration yet.

**Risks / blockers:** Phase 5 is higher-blast-radius than thesis work because it makes CREED canonical. Preserve flat canonical paths. Use pathspec commits only. Verify grep refs/network consistency before commit. Push only with Will approval.

## 2026-06-21 ~10:01 ET — Closeout after AGENTS organization + weekend freshness cleanup

**Status:** Repo was clean/synced after the AGENTS/PROME cleanup push, then two small local commits were added for repeated Sunday respawns: `PROME/BOOT.md` now has a weekend/market-holiday freshness gate, and `HEARTBEAT.md` now labels Fri-close dashboard levels as orientation-only. No market data was refreshed this session.

**What landed:** Grouped AGENTS directory views are live without moving canonical `AGENTS/<NAME>/` folders. Live Prome docs were cleaned of retired `PROME/TOSCANINI/` paths. Canonical topology now lives in `AGENTS/_NETWORK.md`; main dashboard Network tab mirrors it; standalone `dashboard/network.html` is a pointer/redirect. HEARTBEAT cleanup cleared stale WALTER re-verify wording and old pre-DEWEY naming noise.

**Files edited in closeout:** `PROME/SCRATCH.md`, `PROME/STATUS.md`, `PROME/TODAY.md`, `PROME/HANDOFF.md`, `memory/2026-06-21.md`, plus post-closeout hygiene in `PROME/BOOT.md` and `HEARTBEAT.md`. `PROME/ACTIVE_DECISIONS.md` intentionally unchanged because no non-terminal decision rail moved.

**Next suggested work:** fresh boot should verify repo state, then choose lane. Market lane: treat `HEARTBEAT.md` as Sunday orientation only and refresh dashboard/FRED before citing fresh levels; watch Jun22 Brent/Hormuz + HY <260 + CFTC/carry. System lane: use `AGENTS/_INDEX.md` for grouped navigation and `AGENTS/_NETWORK.md` for topology.

**Risks / blockers:** do not physically move agent directories without a migration pass. Do not maintain multiple live network maps. No trade/expiry action without broker/Will truth.

---
## 2026-06-20 ~20:05 ET — Closeout after heartbeat/auto-memory/DEWEY cleanup + pushed-agent audit

**Status:** Repo was clean/synced at closeout start. Current regime source is `HEARTBEAT.md`: signed-but-fraying MOU; Jun20 Hormuz re-closure declared; contested/not kinetic; energy tail re-fat; broad cascade unconfirmed. HY remains **263 [FRED 6/17]** near <260 kill, VIX/banks calm, carry red.

**What landed:** HEARTBEAT refreshed and pushed for Jun20 Hormuz declaration; `memory/auto/MEMORY.md` compacted under the load cap with all 143 links preserved; active-agent push train pulled/audited cleanly; root DEWEY naming aligned in `HEARTBEAT.md` + `AGENTS_DIRECTORY.md`. WALTER-specific drift was identified but deliberately not edited — Will will handle with WALTER.

**Files edited in this closeout:** `PROME/SCRATCH.md`, `PROME/STATUS.md`, `PROME/TODAY.md`, `PROME/ACTIVE_DECISIONS.md`, `PROME/HANDOFF.md`, `memory/2026-06-20.md`.

**Next suggested work:** fresh boot should verify repo state, then use `HEARTBEAT.md` for the market frame. Market lane: Jun22 Brent/Hormuz tape response + HY <260 + CFTC/carry. System lane: wait for WALTER’s own cleanup before touching WALTER. DEWEY lane: CONTEXT refresh before first live run.

**Risks / blockers:** do not repeat shared auto-memory index edits during active agent work; coordinate a push/rebase window first. Do not treat Hormuz closure as kinetic without physical/tape confirmation. No trade/expiry action without broker/Will truth.

---
## 2026-06-20 ~14:59 ET — Closeout after CORAL inbox + thesis rails install

**Status:** Repo is clean/synced to origin. CORAL boot hardening, WALTER inbox processing, and thesis rails are installed and pushed. Market regime unchanged from HEARTBEAT: Geneva de-escalation branch fired, HY **263 [FRED 6/17]** near <260 kill, banks/VIX calm, carry red.

**What landed:** CORAL now has `scripts/boot.py`, processed WALTER inbox (`SIG-W-20260619-002/007/008` moved to processed with `board_log.tsv` rows), updated STATUS/SCRATCH/NEXUS/MEMORY/workbooks, and installed `thesis/THESIS.md` + `thesis/CHANGELOG.md`. Bank-upgrade rail requires ≥2 FL-exposed banks deteriorating or explicit USCB condo-association loan deterioration with corroboration.

**Files edited:** `PROME/SCRATCH.md`, `PROME/STATUS.md`, `PROME/TODAY.md`, `PROME/ACTIVE_DECISIONS.md`, `PROME/HANDOFF.md`, `memory/2026-06-20.md`; CORAL files under `AGENTS/CORAL/` were edited under explicit Will scope and pushed before Prome closeout.

**Next suggested work:** fresh boot should find repo clean/synced. If CORAL lane, build per-metro convergence grid or Q2 FL-bank prep. If market lane, refresh HY/dashboard and check Jun20 CFTC/SAM. If WALTER lane, monitor v0.18 behavior; do not edit WALTER specs from Prome unless scoped.

**Risks / blockers:** no trade/expiry action without broker/Will truth. CORAL thesis values must stay in STATUS/workbooks, not THESIS. Do not upgrade CORAL bank transmission on collateral/household stress alone.

---
