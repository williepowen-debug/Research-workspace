# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-27 (Claude Code Prome — Sat agent-build-out day: **auto-push migration COMPLETED + roster refresh + pre-closeout staleness audit + archive sweep**. Supersedes the 6/26 LATE-NIGHT SCRATCH.)

## What happened this session
Boot + a full agent-infrastructure day (4 threads, all closed). **ORACLE/TERRY/WALTER live in separate windows throughout** — coordination file-based; all my commits pathspec-scoped → zero index race despite 3 live windows. No market trigger fired, no capital deployed (standing rule held).

1. **Auto-push migration — COMPLETE (the 6/26 headline leftover).**
   - Swept 8 agent CLAUDE.md to auto-push-at-closeout: BOND/CARL/CORAL/DEWEY/HENRY/LABOR/MARCO/OZK (commit `07d04796`). **OZK got a full git-block rehab** — it still taught forbidden `git reset HEAD` ×2 (63d-cold, pre-pathspec-reform); both fixed. HENRY stale interim-note corrected.
   - **ORACLE self-flipped its own block mid-session** (commit `824a713e`) — lazy-sweep design working as intended; confirmed why we skip live agents.
   - Tier-2: **LIQUID/CLOSEOUT.md flipped** + bookkeeping refreshed (`24fd1ef2`).
   - **Net: 18/21 CLAUDE.md on auto-push.** 3 holdouts all deliberate: TERRY (live/self-sweep), WALTER (architectural, BOARD_CONSUMPTION_SPEC §7), YEYOU (manual/branch). **Migration thread RETIRED.**

2. **Roster refresh — verified-active pass (commit `bc35fdc4`).** Built a commit-activity map (the real "is it running" signal). Corrections vs the old prose roster: **VIOLET slotted Active** (118 commits/30d — was unslotted!); **OZK Active→Dormant** (0/60d, Q2-gated); **DARWIN removed** (phantom — already in `_archive`); BOND/TERRY→Active; MARCO/ORACLE/SHADE promoted; CREED/DEWEY→Tier-2. **Retired 4 scaffolds** (BUFFER/DOC/EARNINGS/FOREX — skeleton, never launched) → `AGENTS/_archive/`. Wrote root CLAUDE.md (Active=20, Tier-2=4) + new **`PROME/ROSTER.md`** (durable verified classification + activity evidence).

3. **Pre-closeout staleness audit (commits `7aff8de0` + `0299c267`).** Fixed durable boot/closeout docs: ACTIVE_DECISIONS top row + preamble (stale `HY 263 [6/17]` → now references HEARTBEAT; "Hormuz re-fattened energy tail" → deflated); CLOSEOUT.md (auto-push status → complete 18/21; de-OpenClaw); HANDOFF.md (de-OpenClaw). Session-state files refreshed in this closeout.

4. **Archive sweep (this closeout).** `CLEANUP_PLAN_2026-05-07` → `PROME/archive/` (clean, no refs). **`PREDICTIONS_MONITOR.md` NOT archived** — reference check found it's **NEXUS's LIVE boot-read prediction ledger** (NEXUS/CLAUDE.md boot step 3 + doc-ownership table), mislocated in PROME/. Flagged for NEXUS.

## Repo state
Clean; all PROME work committed + pushed via the train (ORACLE's mid-session safe-push swept the first two commits earlier; closeout safe-push sweeps the rest). Only working-tree dirt = `WILL/trading-journal/` (Will's).

## Next planned work / open threads
- **PREDICTIONS_MONITOR.md → NEXUS:** flag that its prediction ledger is stale (April rows) AND cross-dir-located in PROME/; NEXUS should refresh + consider migrating it into `AGENTS/NEXUS/`.
- **Auto-push remainder (optional):** TERRY/YEYOU CLOSEOUT.md (TERRY self-sweeps; YEYOU manual-by-design = arguably correct as-is).
- **Energy (BRENT's lane):** BRENT processes the RED SIG on Jul-1 EIA WPSR / Jul-3 COT (downgrade "STRUCTURAL settled"→"structural LEAN"; re-derive curve).
- **Still pending (prior):** OZK revival gated on broker book (Q2 ~Jul-16); HEN-35 AI-capex Mon transmission test (MU/SMH/SOX + VIX vs 23); bank-put reshape card fires only on HY>280 sustained / WAL Jul-16.

## Forward docket
Mon MU/SMH/SOX (HEN-35) · VIX vs 23 · HY vs 280 (auto-watched) · 10Y 6/30 · JOLTS 6/30 · EIA 7/1 · NFP 7/3 · SPR re-auth ~7/3 · CFTC COT 7/3 (BRENT 2nd-week test) · STEO 7/8 · OZK+WAL+CFG Jul-16 · CPI 7/14 · late-Jul Q2 hyperscaler FCF + BDC marks ~7/25.

## Cautions
- Position/broker truth = Will/FORGE. Refresh dashboard/FRED (venv) before any level — **weekend; levels are 6/25 Fri-close orientation.**
- Standing rule held: deploy only on a fired trigger, $500/card. Nothing fired — pure agent-infrastructure day.
- Auto-push at closeout is canonical (`safe-push.sh`). Non-ff abort = 2nd machine → flag Will, do NOT force.
- 3 live windows (ORACLE/TERRY/WALTER) were active this session — they self-manage; don't assume warm next session.
