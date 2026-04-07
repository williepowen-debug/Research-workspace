# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-04-07 09:33 ET

## What Just Happened
Morning session — agent check-ins, cron system discussion, handoff preparation.

**Key activities:**
1. **LABOR check-in** — No new data, monitoring mode until Thu Apr 10 claims (FL Wave 1 lag test)
2. **CARL check-in** — Skipped (persistent agent on Claude Code per AGENTS.md)
3. **MARCO check-in** — Spawned but timed out (2m0s, no output)
4. **Cron discussion** — User exploring dual OpenClaw/Claude Code agent spawning
5. **Calendar sync** — Token expired, flagged for re-auth

**Decisions deferred:**
- Dual agent spawning (OpenClaw + Claude Code) — hold for now
- Agent check-in routing — no changes

## Current State
- **Tuesday morning, 9:30 AM ET.**
- **Markets open.** HY OAS print today adjudicates RED debate.
- **APO:** Still below $113 stop ($107.04) — 4+ days, decision pending
- **Prome Zone:** Paused (user request)
- **Calendar:** Sync failed, needs manual re-auth

## QUICKSTART (Next Session)
1. **Review HY OAS print** — adjudicate RED debate R4
2. **APO decision** — Cut or hold? Below stop 4+ days
3. **KRE roll pricing** — LIQUID domain
4. **Signal Registry Draft A** — Review when ready
5. **Calendar re-auth** — `mv token.json token.json.bak && python3 sync_calendar.py`

## Handoff Block
**Last context:** Morning check-ins complete. HY OAS print today critical for RED debate. APO below stop.
**Next tide:** Market data review, position decisions
**Open:** Prome Zone paused, APO decision pending, calendar sync broken
**Files touched:** None new

## Pending / Unresolved
- APO position — below stop, decision needed
- HY OAS print — RED debate adjudication
- KRE Jun→Dec rolls — pricing
- Signal Registry Draft A — pending review
- Calendar sync — token expired
- RED/HANS check-ins — stale (persistent agents)
