# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-25 (Claude Code Prome — morning sync, branch-reconciliation landing, full branch sweep)

## What Just Happened

- **Morning sync:** pulled master from origin — clean 10-commit fast-forward (was `329bb543`, WALTER 6/24 + BRENT 6/24 EIA + YEYOU SOUL/IDENTITY + 9 BOARD cards). Working tree was clean; no stash needed.
- **Scouted + deep-dove two unmerged `prome/*` branches**, then executed an approved **curated landing** on master (4 commits, isolated-worktree build, FF-landed).
- **Master now at `2ee22af4`.** Curated commits:
  - `02474316` — salvage `PROME/GIT_COORDINATION.md` + `WEEKLY_DECISION_CALENDAR_2026-06-22.md` (net-new; A is YEYOU's prereq).
  - `ca2fbb37` — salvage 7 HANS `research/*.md` modules + `REVIVAL_PLAN_2026-06-22.md` + revived HANS `CLAUDE.md` + pre-revival snapshot. **Master's newer Jun-22 22:42 PM HANS STATUS/workbook left UNTOUCHED.**
  - `ea8f2c17` — merge `reconcile-yeyou` = canonical YEYOU (REVIEW_CHECKLIST→`reviews/`, +CLOSEOUT/CROSS_SILO/COORDINATION).
  - `2ee22af4` — archive dead `AGENTS/PROME/` tree (30 files) → `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/`; updated `_INDEX`/`_SYNTHESIS_OPS` + PROME docs to new layout.
- **Deliberately dropped:** `pending-flush`'s stale HANS STATUS/ML/VX/FLOW (master authoritative) + its superseded YEYOU portion. `pending-flush` was 111 commits behind base; never raw-merged. Did NOT bring `memory/2026-06-22.md` (optional historical session note).
- **Branch sweep (Will-directed):** cleaned ALL stale branches — origin went **14 heads → 1 (`master` only)**. Deleted the 2 `prome/*` + 11 more (merged/redundant/superseded `claude/*` + `brent/may4-data-pull`). Before deleting `claude/todays-repo-commits-w96on7`, **salvaged** 2 Will-requested Jun-9 audit docs → `AUDITS/2026-06-09_{shared_state_design,signal_coherence_audit}.md` (commit `da495926`). Also deleted local-only backup `otto-backup-pre-rebase-20260415` (verified 100% redundant — post-rebase SHA-churn; all 15 commits' work confirmed present on master).

## Current Git State

- **PUSHED 2026-06-25.** Local + origin master both at **`da495926`** — `HEAD...origin/master = 0/0`, fully synced. (Curated-landing + reconcile-yeyou + closeout truth-up + auto-mem + AUDITS salvage.)
- Working tree clean. Staging worktree + branch removed.
- **Branch list fully clean: `master` only, both locally and on origin.** All `prome/*` + 11 stale `claude/*`/`brent/*` remotes + the local Apr-15 backup deleted.

## Open Follow-ups

1. ✅ **DONE 2026-06-25** — push (origin at `da495926`), full branch sweep (origin + local now `master`-only), 2 audit docs salvaged to `AUDITS/`.
2. **HANS dedup:** `AGENTS/HANS/archive/STATUS_PRE_REVIVAL_2026-06-22.md` duplicates master's `workbook/STATUS_archive_20260430.md` (same Apr-30 content, two paths) — HANS to reconcile to one. Kept so HANS `CLAUDE.md`/`REVIVAL_PLAN` refs resolve.
3. **HANS workbook hygiene** (old Jun-22 SCRATCH's "Batch D"): **moot for the branch versions** — master carries the newer Jun-22 PM workbook (ML 16 rows incl. Qatar/Lebanon/Jul-4). Any further HANS workbook work is HANS-owned against master's current state, not the salvaged branch. `SOVEREIGN_LDI_MONITOR_2026-06.md` is now present (was in the salvage set).

## Cautions

- **Do not push without Will's explicit coordination.**
- HANS STATUS/workbook on master = Jun-22 22:42 PM (authoritative). Salvaged `research/*.md` are durable scaffolding — cross-check against master STATUS before treating as live.
- Refresh dashboard/FRED before citing current market levels (HEARTBEAT is Fri-close orientation only).
- `git add` only specific PROME/ paths; never broad-add (per the newly-landed `PROME/GIT_COORDINATION.md`).
