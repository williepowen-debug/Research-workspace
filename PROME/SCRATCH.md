# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-04-11 15:30 ET

## What Just Happened
Weekend session — Research review, git protocol discussion, agent workflow cleanup.

**Key activities:**
1. **Reviewed old PC contagion research** — Verified $1.57T NDFI vs $85-95B PC-specific exposure (different metrics, both in system)
2. **Git protocol discussion** — Confirmed agents commit their own work, Prome does not auto-commit
3. **Spawn policy clarified** — LABOR, BRENT, BROCK, LIQUID now persistent on Telegram/Claude Code (do not spawn)
4. **HEARTBEAT.md flagged stale** — Multiple updates needed (Brent $91 not $109, claims 219K, APO 9+ days below stop)

**Decisions made:**
- AGENTS.md updated with persistent agent list
- Git protocol documented in docs/GIT_PROTOCOL.md
- HERMES spawns paused (cron job still running but Prome won't act on reminders)
- All scheduled Prome spawns stopped unless explicitly requested

## Current State
- **Saturday afternoon, 3:30 PM ET.**
- **Markets closed.** Weekend analysis mode.
- **APO:** ~$104 (was $104.28 in Friday snapshot) — still below $113 stop, 9+ days, decision still pending
- **Brent:** ~$91 post-ceasefire
- **Claims:** 219K (week ending Apr 4), shadow adjustment +70K confirmed
- **Portfolio:** Down ~5-7.5% this week per Friday snapshot

## QUICKSTART (Next Session)
1. **APO decision** — Still unresolved. Cut, hold, or hybrid?
2. **Update HEARTBEAT.md** — Stale since Apr 3-4
3. **KRE roll pricing** — Jun→Dec rolls on any rally
4. **TIC data Apr 15** — 4 days
5. **OZK earnings Apr 16** — 5 days

## Handoff Block
**Last context:** Git protocol stabilized. Persistent agents on Telegram/Claude Code. Prome spawns stopped unless requested. HEARTBEAT.md needs update.
**Next tide:** TIC Apr 15, OZK Apr 16, potential ceasefire developments
**Open:** APO cut/hold, KRE rolls, HEARTBEAT update
**Files touched:** `AGENTS.md` (updated persistent list), `docs/GIT_PROTOCOL.md` (created)

## Pending / Unresolved
- APO position — below stop 9+ days, decision needed
- KRE Jun→Dec rolls — pricing
- HEARTBEAT.md update — stale data
- HERMES cron job — still running but Prome won't spawn
- RED/HANS check-ins — stale (persistent agents)
