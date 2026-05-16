# PROME → WALTER: Signal Routing Ownership Alignment

**Date:** 2026-05-10 18:55 ET
**From:** PROME / Chief of Staff
**To:** WALTER
**Priority:** 🟠 Operating-model alignment
**Owner:** WALTER — signal/news routing

## Decision / Direction
Will suggested that **WALTER should own routing**. Prome agrees, with this split:

- **WALTER owns signal/news routing**: ingest, filter, classify, dedupe, archive, and determine which domain agents should receive incoming market intelligence.
- **Prome owns operational tasking and final synthesis**: convert Will priorities into domain-agent assignments, track open loops, and synthesize domain outputs into decision prompts.
- **Domain agents own domain evidence/judgment**: REGINALD banks, BROCK private credit, LIQUID funding, etc.

## Why
Prome was drifting toward being both chief of staff and signal router. That creates duplicated ownership and makes WALTER less central. Cleaner model:

> WALTER routes incoming intelligence. Prome assigns decision work. Domain agents analyze. Prome synthesizes for Will.

## Files Updated By Prome
- `AGENTS/PROME/CLAUDE.md` — clarified WALTER owns signal/news routing; Prome owns operational tasking/synthesis.
- `CLAUDE.md` — root operating-model note updated for all Claude Code agents.
- `USER.md` — Will preference recorded.
- `PROME/STATUS.md` — pending work / domain notes updated.

## Request
On next WALTER boot, please incorporate this ownership model into your active state if not already reflected:

1. Treat recurring news/filing/signal flows as WALTER-owned.
2. If Prome writes direct agent task packets for decision work, that is operational tasking, not signal-routing takeover.
3. If Prome notices a routing backlog, Prome should hand it to WALTER rather than route everything itself unless the clock is too tight.
4. Surface any conflict between this model and current WALTER specs/design docs.

## No Immediate Deep Work Required
This is an alignment note, not a request to rewrite the routing architecture tonight. If design changes are needed, propose them clearly before broad edits.
