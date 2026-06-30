# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-30 (Prome, PM-2) — **★ TRACK B (history scrub) DONE + verified.** Repo on GitHub is now provably clean of all secrets/private data, full 3,465-commit / 5-month history intact. **Repo is SAFE TO FLIP PUBLIC** (Will's action, when ready). Public-prep is essentially complete pending the flip.

## ⏰ NEXT-SESSION ENTRY POINT — repo is clean; only the public-flip remains
**Target:** Will applying to **Anthropic Fellows — Economics & Policy** (job 5183053008); this repo = centerpiece artifact. Durable context → [[project_public_prep_anthropic_fellows]]. Full scrub record → `PROME/public-prep/HISTORY_SCRUB_PLAN.md`.

## ✅ This session (PM-2) — Track B history scrub COMPLETE
- **Method:** `git filter-repo` from a pristine mirror backup; sidecar-rewrite → verify → ONE force-push (Landing A — repo preserved, NOT delete/recreate) → re-sync live → fresh-clone proof. Done while PRIVATE.
- **Removed from ALL history:** `WILL/trading-journal/` (private financial), `tools/calendar/` (Google OAuth `GOCSPX` secret + pickled tokens), `.venv/` + `*.pyc`/`__pycache__` (bloat 225M→131M), dead telegram token (id+secret), gateway token, **WALTER live bot-ID** (Will opted in).
- **★ The double-check earned its keep:** pass 1 scrubbed the bot-**ID** but left the dead token's **35-char secret half** (old `cron_sweep.sh` hardcode). Caught by reading edited content + a blob-level secret enumeration over kept history. Pass 2 (corrected, fresh from backup) scrubbed the whole credential. Lesson → [[finding_history_scrub_verify_by_content_not_pickaxe]].
- **Final state:** origin == local == fresh-clone = `b01c0346`; all targets 0; broad credential sweep 0; CASCADE research image byte-identical (a base64 coincidence, correctly NOT scrubbed); fsck clean; README+essay intact.
- **WALTER/fleet Telegram UNAFFECTED** — live tokens are off-repo (`~/.claude/channels/telegram-*`), never in repo; scrub only edited 7 `.md` docs.

## ⭐ REMAINING for going public
1. **Will flips repo → Public** (GitHub Settings → Visibility). Nothing else gates it. *(Accepted Landing-A residue: GitHub may keep old commits reachable only by exact 40-char SHA until its GC — harmless, repo never public, secrets dead.)*
2. After Will confirms public looks right → delete the mirror backup `~/Research-workspace-PRESCRUB-BACKUP-20260630.git` (the rollback net).

## Also pending (lower)
- **Essay** (`PROME/drafts/essay_conservation_of_cost.md`) — Will reviewing/editing; revise on his edits.
- `BOARD/` (live, ~416 files) — route to WALTER to thin consumed entries (same pattern as processed/).
- Phase-2 archives — ref-surgery to cut ~370 referenced archives if going deeper on declutter.
- root `MEMORY.md` lines 45–46 OpenClaw-vestige — refresh pass.

## Git / repo state
Clean. Track-B force-pushes done (`bec24b60 → 9b7d3290 → b01c0346`). Live working dir synced + gc'd (.git 133M). Closeout commit = PROME/public-prep artifacts + state docs + daily log + 1 auto-memory.

## Cautions
- **Position truth OFF-repo** (`WILL/trading-journal` gone from tree AND history now).
- **Refresh dashboard/FRED before citing levels** — no market read since 6/30 AM (HY OAS ~280 at-line tightening, VIX ~17, Brent ~$74, USD/JPY ~162).
- Mirror backup still on disk = rollback until Will confirms; don't delete prematurely.
