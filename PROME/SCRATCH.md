# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-25 (Claude Code Prome — morning sync + branch-reconciliation landing)

## What Just Happened

- **Morning sync:** pulled master from origin — clean 10-commit fast-forward (was `329bb543`, WALTER 6/24 + BRENT 6/24 EIA + YEYOU SOUL/IDENTITY + 9 BOARD cards). Working tree was clean; no stash needed.
- **Scouted + deep-dove two unmerged `prome/*` branches**, then executed an approved **curated landing** on master (4 commits, isolated-worktree build, FF-landed).
- **Master now at `2ee22af4`.** Curated commits:
  - `02474316` — salvage `PROME/GIT_COORDINATION.md` + `WEEKLY_DECISION_CALENDAR_2026-06-22.md` (net-new; A is YEYOU's prereq).
  - `ca2fbb37` — salvage 7 HANS `research/*.md` modules + `REVIVAL_PLAN_2026-06-22.md` + revived HANS `CLAUDE.md` + pre-revival snapshot. **Master's newer Jun-22 22:42 PM HANS STATUS/workbook left UNTOUCHED.**
  - `ea8f2c17` — merge `reconcile-yeyou` = canonical YEYOU (REVIEW_CHECKLIST→`reviews/`, +CLOSEOUT/CROSS_SILO/COORDINATION).
  - `2ee22af4` — archive dead `AGENTS/PROME/` tree (30 files) → `PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/`; updated `_INDEX`/`_SYNTHESIS_OPS` + PROME docs to new layout.
- **Deliberately dropped:** `pending-flush`'s stale HANS STATUS/ML/VX/FLOW (master authoritative) + its superseded YEYOU portion. `pending-flush` was 111 commits behind base; never raw-merged. Did NOT bring `memory/2026-06-22.md` (optional historical session note).

## Current Git State

- Local master at **`2ee22af4`, +6 / origin, NOT pushed.** Push is Will-coordinated.
- Working tree clean. Staging worktree + branch removed.
- Remote branches `origin/prome/pending-flush-2026-06-25` and `origin/prome/reconcile-yeyou-2026-06-25` still exist — delete on origin **after** the push (reconcile-yeyou fully merged; pending-flush salvaged+superseded).

## Open Follow-ups

1. **Coordinated push** of the +6 local commits to origin (Will window).
2. **Remote branch cleanup** post-push (the two `prome/*` branches above).
3. **HANS dedup:** `AGENTS/HANS/archive/STATUS_PRE_REVIVAL_2026-06-22.md` duplicates master's `workbook/STATUS_archive_20260430.md` (same Apr-30 content, two paths) — HANS to reconcile to one. Kept so HANS `CLAUDE.md`/`REVIVAL_PLAN` refs resolve.
4. **HANS workbook hygiene** (old Jun-22 SCRATCH's "Batch D"): **moot for the branch versions** — master carries the newer Jun-22 PM workbook (ML 16 rows incl. Qatar/Lebanon/Jul-4). Any further HANS workbook work is HANS-owned against master's current state, not the salvaged branch. `SOVEREIGN_LDI_MONITOR_2026-06.md` is now present (was in the salvage set).

## Cautions

- **Do not push without Will's explicit coordination.**
- HANS STATUS/workbook on master = Jun-22 22:42 PM (authoritative). Salvaged `research/*.md` are durable scaffolding — cross-check against master STATUS before treating as live.
- Refresh dashboard/FRED before citing current market levels (HEARTBEAT is Fri-close orientation only).
- `git add` only specific PROME/ paths; never broad-add (per the newly-landed `PROME/GIT_COORDINATION.md`).
