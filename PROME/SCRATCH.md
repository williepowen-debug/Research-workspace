# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-04-03 11:15 ET (Session handoff)

## What Just Happened
Built the News Sweep tool from scratch. Full session with Will designing, researching, building, testing, and deploying a thesis-tagged news monitoring system. Also: LABOR check-in (NFP 178K), MARCO DHS deal logged, multiple agent cron check-ins handled (Good Friday — light touch).

## Immediate State
- **NEWS SWEEP v1 IS LIVE.** `FORGE/tools/news-sweep/` — sweep.py + config.py fully operational. First live run completed, 9 agent inboxes received files. Cron set for M-F 8:30 AM ET with Telegram push. Dashboard endpoint `/api/news` active.
- **Monday Apr 7 is the real test.** First automated sweep → agent check-in → inbox processing cycle. Watch for: agents reading sweep files, dedup cache behavior, Google News rate limits.
- **Good Friday.** Markets closed. Most agents not spawned today. LABOR got NFP check-in (178K, healthcare-driven). MARCO got DHS deal news (shutdown may end today).

## Key Signals to Track
1. 🔴🔴 **Blue Owl $5.4B redemptions** — 10+ sources confirming. BROCK domain. Sweep correctly classified and routed.
2. 🔴🔴 **Kuwait refinery drone strike** — new Gulf infrastructure attack. HENRY WATCH_FOR hit.
3. 🔴🔴 **Subprime auto cluster** — 8 articles, Tricolor fraud charges, Chapter 7 filing. CARL/OTTO domain.
4. 🔴 **Apollo SEC class action (Epstein ties)** — DEVELOPMENT on known entity. BROCK.
5. 🔴 **NFP 178K** — headline beat but internals weak (healthcare 43%, Feb revised down to -133K). LABOR logged.
6. 🔴 **DHS shutdown deal reached** — may resolve today via pro forma session. MARCO inbox.
7. 🔴 **Carry trade unwind risk building** — SAM WATCH_FOR hit. UBS calling USD/JPY 175.

## News Sweep — Maintenance Notes for Next Prome
- **Config:** `FORGE/tools/news-sweep/config.py` has ENTITY_INDEX and WATCH_FOR lists. Update after major STATUS changes.
- **Known friction:** LIQUID inbox can be large (34 items first run, should be smaller after query tightening). Some watch keyword false positives in compact output (minor).
- **V2 considerations (NOT YET — wait 1 week):** Auto entity index generation, push WATCH_FOR to agents, NEXUS integration, embedding-based matching. Will agreed to evaluate after 1 full week of v1 data.
- **Full docs:** `FORGE/tools/news-sweep/README.md`

## Pending / Unresolved
- **Monday Apr 7:** APO reassess (stop $113, at ~$107 — already blown through), KRE Jun→Dec roll, HYG roll
- **Monday Apr 7:** First automated news sweep cycle. Monitor.
- **Apr 10:** FL Wave 1 lag test (claims print — critical given Fed breakeven = zero research)
- **Apr 6 (Sun):** Iran pause expiry — HAWK deadline
- **BOJ Apr 23-24 meeting**
- ORACLE agent inaugural sweep — still never spawned
- Calendar sync broken (Google OAuth)
- Cliffwater 219% and BDC NAV table still need primary source verification
- BROCK batches 2-3 unprocessed (in inbox from Apr 2)
- CLAUDE.md needs local machine pickup (Will: `mv CLAUDE.md CLAUDE_OLD.md && git pull`)
- **NEXUS and RED both 8 days stale** (last updated 3/26). Should get check-ins soon.
- **Agent inbox backlog:** REGINALD (8+sweep), CARL (7+sweep), HENRY (6+sweep), LABOR (5+sweep)

## Don't Forget
- WTI at $109+. Brent $107-108. Gas $3.99 (hair below $4 breakpoint).
- Account ~$55.7K (+111.5%)
- Eric Jackson timeline: May-Aug = thesis confirms or breaks
- Fed breakeven job growth = ZERO (structural fragility)
- APO below stop — decision needed Monday
