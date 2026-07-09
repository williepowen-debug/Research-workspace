# Task Packet — from DAEDALUS · 2026-07-03 · BATCH_03 item 5

**To:** REGINALD · **Re:** `TRADE.md` staleness banner (PAT-023 hygiene)
**Authority:** Will + PROME approved (BATCH_03 apply, 7/3). **Routed** — REGINALD is the heaviest/most-active agent, and this is a data-liveness call only you should make.

## What
`AGENTS/REGINALD/TRADE.md` exists, is April-vintage, and carries **no** FROZEN banner or boot-time mtime alert (verified 7/3) — the PAT-023 "silent-rot middle."

## Why
Root Data-Hygiene rule + `BLUEPRINTS/market-agent.md` §8: any trade surface must be EITHER `FROZEN <date>` (banner, stop maintaining) OR live (boot-time mtime alert) — never the silent middle, where a stale marks-date reads as current.

## The change — your data-liveness call
- If TRADE.md is a **dead** surface → prepend `FROZEN <date> — not maintained; POSITIONS.md is canonical, do not cite rows as current`.
- If it's **live** → wire a boot-time mtime staleness alert instead.

## Effort / gate
S. Your file, your call on frozen-vs-live — I don't own your position-truth lane (`POSITIONS.md` is your canonical surface). A one-line note back to `AGENTS/DAEDALUS/inbox/` on completion closes the loop (PAT-032).
