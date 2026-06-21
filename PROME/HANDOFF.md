# PROME HANDOFF

**Purpose:** Single live continuity surface for Prome across OpenClaw and Claude Code. Keep this file short: latest 3–5 entries only. Archive older entries to `PROME/archive/`.

**Archive:** Full pre-merge OpenClaw + Claude Code handoff history through 2026-06-14 is preserved in `PROME/archive/HANDOFF_2026Q2.md`.

---

## 2026-06-21 ~19:40 ET — Closeout after CREED/REITS/TRADES/TERRY/ORACLE cleanup

**Status:** Repo was clean/synced after rebasing over newer WALTER/SAM commits and pushing four system-cleanup commits. Closeout now updates Prome live-state surfaces. If committed after this entry, local may be ahead by one Prome closeout commit until Will pushes.

**What landed:** REITS was archived/demoted and its useful public REIT equity-market tape moved into CREED. TRADES was archived/demoted and its useful verification pattern moved into TERRY. TERRY gained risk scoring/calibration tooling. ORACLE gained prediction-market metrics (entropy, KL bits, entropy-collapse alerts, liquidity/resolution discounts, TERRY handoff packet). Claude Code command reference now has no REITS/TRADES launch commands.

**Pushed commits:** `9cf41161 CREED: absorb REIT equity tape`; `cdd6ce96 TERRY: archive legacy TRADES playbook`; `6219553f TERRY: add risk scoring module`; `0ad1def6 ORACLE: add prediction market metrics`.

**Current ownership truth:** CREED owns national CRE/CMBS + REIT tape. REITS is source archive only. TERRY owns live trade construction and the old TRADES playbook. TRADES is source archive only. ORACLE measures prediction-market diagnostics; TERRY evaluates tradeability; Will approves. No auto-trading.

**Next suggested work:** fresh boot should verify repo state, then either refresh market data for Jun22 gates or continue dormant-agent cleanup only after inspecting actual files/value. If ORACLE implementation resumes, metrics doc exists but script integration is still future work.

**Risks / blockers:** HEARTBEAT remains Fri-close/weekend orientation; refresh dashboard/FRED before current levels. No trade/position action without broker/Will truth. Do not launch archived REITS/TRADES unless Will explicitly revives.

## 2026-06-21 ~15:55 ET — Post-CREED topology closeout / no-push session rule

**Status:** Repo was clean/synced after pushed CREED topology closeout and memory closeout. Latest pushed commit: `670ae6b6 memory: log CREED topology closeout`. Will then approved updating Prome live boot surfaces and said local commits are allowed, but **do not push to GitHub until he coordinates**.

**What landed:** CREED is canonical as **National CRE / CMBS** market-stress agent. Pushed closeout commits: `8eb56e66 CREED: integrate phase 5 topology`, `94c01c15 CREED: add legacy pull-forward map`, `34552d9e CREED: tighten cold-boot readiness`, `670ae6b6 memory: log CREED topology closeout`.

**Current CREED state:** CREED feeds `REGINALD`, `CORAL`, `LIQUID`, and `CARL`. CREED is Claude Code roster / explicit-permission only; do not casually spawn. Current thesis remains **selective CRE recognition accelerating**, not broad CRE→bank cascade yet. Legacy `AGENTS/REGINALD/sub-agents/CREED/` remains source archive only; do not move/delete.

**Current rails:** `AGENTS/CREED/CLAUDE.md`, `AGENTS/CREED/README.md`, `AGENTS/CREED/STATUS.md`, `AGENTS/CREED/research/REFRESH_2026-06-21.md`, `AGENTS/CREED/thesis/THESIS.md`, `AGENTS/CREED/thesis/CHANGELOG.md`, `AGENTS/CREED/research/INBOX_TRIAGE_2026-06-21.md`, `AGENTS/CREED/archive/LEGACY_PULL_FORWARD_2026-06-21.md`.

**Next suggested work:** Finish/verify Prome live-state refresh (`HANDOFF`, `SCRATCH`, `TODAY`, `STATUS`) and commit locally only. If CREED analytical lane resumes, start with monthly CMBS/special-servicing tracker design, handoff thresholds to REGINALD/CORAL/LIQUID/CARL, then Q2/Q3 bank-filing convergence questions. Do not do full legacy migration unless Will explicitly approves.

**Risks / blockers:** No GitHub push until Will coordinates. Market levels in `HEARTBEAT.md` are weekend/Fri-close orientation only; refresh dashboard/FRED before citing current levels. No trade/position action without broker/Will truth.

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
