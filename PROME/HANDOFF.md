# PROME HANDOFF

**Purpose:** Single live continuity surface for Prome across OpenClaw and Claude Code. Keep this file short: latest 3–5 entries only. Archive older entries to `PROME/archive/`.

**Archive:** Full pre-merge OpenClaw + Claude Code handoff history through 2026-06-14 is preserved in `PROME/archive/HANDOFF_2026Q2.md` (older 2026-06 entries appended there as they roll off).

---

## 2026-06-25 — Morning sync + curated two-branch reconciliation landed on master

**Status:** Pulled master clean (10-commit FF to `329bb543`), deep-dove and landed a curated reconciliation of two unmerged `prome/*` branches, refreshed Prome state, and **pushed — origin master at `da495926`, fully synced (`0/0`).** Branch list fully swept to **`master`-only (local + origin)**. Working tree clean; staging worktree/branch removed.

**What landed (4 curated commits):** (A) `02474316` salvage `PROME/GIT_COORDINATION.md` + `WEEKLY_DECISION_CALENDAR_2026-06-22.md`. (B) `ca2fbb37` salvage 7 HANS `research/*.md` modules + `REVIVAL_PLAN_2026-06-22.md` + revived HANS `CLAUDE.md` — **master's newer Jun-22 22:42 PM HANS STATUS/workbook preserved untouched.** (C) `ea8f2c17` merge canonical YEYOU from `reconcile-yeyou` (REVIEW_CHECKLIST→`reviews/`, +CLOSEOUT/CROSS_SILO/COORDINATION). (D) `2ee22af4` archive dead `AGENTS/PROME/` tree (30 files) → `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/`; `_INDEX`/`_SYNTHESIS_OPS`/PROME docs updated to new layout.

**Deliberately dropped:** `pending-flush`'s stale HANS STATUS/ML/VX/FLOW (master authoritative) + its superseded YEYOU portion. `pending-flush` was 111 commits behind base; never raw-merged. Build was done in an isolated git worktree — main tree never left master until the verified FF-land.

**Resolved this session (2026-06-25):** coordinated push completed (origin master at `da495926`). **Full branch sweep:** origin **14 heads → 1 (`master` only)** — deleted both `prome/*` + 11 stale `claude/*`/`brent/may4-data-pull` remotes (all merged/redundant/superseded) + the local-only `otto-backup-pre-rebase-20260415` (verified 100% redundant: post-rebase SHA-churn, all 15 commits' work confirmed on master). Before deleting `claude/todays-repo-commits-w96on7`, salvaged 2 Will-requested Jun-9 audit docs → `AUDITS/2026-06-09_{shared_state_design,signal_coherence_audit}.md`.

**Risks / blockers / open:** HANS `archive/STATUS_PRE_REVIVAL_2026-06-22.md` duplicates `workbook/STATUS_archive_20260430.md` (same Apr-30 content) — HANS to dedup. Refresh dashboard/FRED before citing market levels.

**Next suggested work:** continue normal Prome boot (BOOT/SYSTEM/CLAUDE_CODE_PROME docs, scan `AGENTS/*/outbox/` for to-PROME signals). HANS workbook hygiene is now HANS-owned vs master's current state, not the salvaged branch.

## 2026-06-22 ~10:14 ET — HANS revival checkpoint before clear

**Status:** Local HANS revival commit exists and is **not pushed**: `94b2e475 HANS: revive Europe monitoring baseline`. Repo was clean/ahead 1 after that commit before this closeout write-back. Push remains gated by Will coordination. *(Note 6/25: this work was reconciled onto master via the curated landing above — master's later Jun-22 PM HANS state is authoritative; the salvaged research modules landed at `ca2fbb37`.)*

**What landed:** HANS stale Apr30 war-regime baseline was archived; HANS `CLAUDE.md`/`STATUS.md` now warn not to boot from old assumptions (Hormuz closed/mined, Qatar permanent loss, Brent $111, Scenario D 85%, HY 350+). Revival plan and research packets are in `AGENTS/HANS/REVIVAL_PLAN_2026-06-22.md` and `AGENTS/HANS/research/`. Completed packets: Batch A current snapshot + PMI scaffold, B1 ECB/Fed divergence, B2 Europe TIC/UST custody, C1 EU energy/storage, C2 EU bank/private-credit/CRE bridge. Weekly decision calendar created at `PROME/WEEKLY_DECISION_CALENDAR_2026-06-22.md`.

**Current HANS read:** Europe is mixed/stagflationary; ECB/Fed divergence/funding is monitor-only; Europe UST demand is neutral/noisy; EU energy is **CONDITIONAL** not active; EU bank/private-credit/CRE is **MONITOR** not active. No HANS outbox threshold fired.

**Unfinished / next entry point:** (1) HANS Phase 7 / Batch C3 — sovereign spread + UK LDI monitor. (2) Jun23 flash PMI mini-update after actuals print. (3) Batch D workbook hygiene: update or mark stale HANS `VX.tsv`, `ML.tsv`, `FLOW.tsv`; set `FLOW-HANS-8` to CONDITIONAL. (4) Optional stale March HANS inbox archive after Batch D.

**Risks / blockers:** HANS workbook is not current yet; research docs + STATUS are current. Do not push without Will. Do not treat HANS old inbox/archived status as live. Refresh market/FRED before citing current prices/levels.

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
