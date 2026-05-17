# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-16 21:23 ET

## What Just Happened

Will wanted the git work made safe before clearing context.

Completed:
- Local dirty work was chunked, committed, rebased on top of remote agent commits, dry-run verified, and pushed.
- Remote now includes Prome commits through `da7242c2 PROME: refresh heartbeat May 16 evening`.
- Rebase/push preserved Claude Code agents' remote work; no conflicts during final rebase.
- After push, a fresh automated/news-sweep batch dirtied the tree. It is not pushed yet.
- `PROME/HANDOFF.md` was rewritten for clear-ready fresh-session pickup.

## Current Dirty Batch

Modified:
- `FORGE/tools/news-sweep/.cache/seen.json`
- `FORGE/tools/news-sweep/latest.json`
- `FORGE/tools/news-sweep/latest.md`
- `HEARTBEAT.md`

Untracked:
- `AGENTS/BROCK/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/CARL/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/HENRY/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/LABOR/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/LIQUID/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/OTTO/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/REGINALD/inbox/sweep_2026-05-16_2306.md`
- `AGENTS/SAM/inbox/sweep_2026-05-16_2306.md`

Do not pull/rebase/stash/reset while this is dirty. Inspect and commit safely if Will approves.

## Current Working Model

- BDC/private-credit mark/income stress confirmed by FSK Q1.
- Broad public-credit cascade still unconfirmed: HY OAS 276bps, VIX 18.43.
- Stress concentrated in Brent/gas, USDJPY, BIZD, WAL/KRE.
- Latest HEARTBEAT: 2026-05-16 19:06 ET; news sweep routed 12 alert-level items + 1 WATCH_FOR hit internally.

## Next Best Action

Fresh session should:
1. Read `PROME/HANDOFF.md` and run `PROME/BOOT.md`.
2. Inspect dirty news-sweep/heartbeat batch and remote overlap.
3. Commit it as a small sweep batch only if safe.
4. Then move to Monday decision prep: APO/ARES/BDC and regional-bank Call Report triage.

## Cautions

- No trades without Will approval.
- No external messages without approval.
- Do not spawn CARL/REGINALD/SAM/RED/BRENT.
- Use explicit path staging only; no broad `git add .`.
- Protect remote Claude Code agents' work.
