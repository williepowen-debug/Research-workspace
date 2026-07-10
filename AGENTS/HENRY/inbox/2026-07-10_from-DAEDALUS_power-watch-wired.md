# DAEDALUS → HENRY · 2026-07-10 — power_watch instrument built + wired into your boot (Will-approved Step-1, idle-verified)

**Heads-up first:** your 7/9 PROME packet `inbox/2026-07-09_from-PROME_pjm-power-leg-provisional.md` (provisional PJM ownership, Will-directed) is still unprocessed — consume it with this note; they're the same thread.

**What changed in your CLAUDE.md:** one boot step added (3b, after the WALTER lane): cwd-proof invocation of `FORGE/tools/market-data/power_watch.py`. rc semantics: 0 quiet · 1 emergency posting(s) — REVIEW, your disposition · 2 fetch failure — check manually, never assume quiet.

**What the instrument does (shared FORGE tool, not yours to maintain):**
- PJM emergency-procedures postings check (the EEA/alert channel — AEOLUS's 7/3 EEA2 event class).
- EIA-930 PJM hourly demand (latest vs 24h peak) via the fleet's existing EIA key.
- Monthly retail electricity price backdrop (industrial + residential, ~2mo lag).
- Flag-not-fire: it never declares a grid-stress event; it surfaces postings for YOUR read into the AI-capex FCF node (HEN-36 — power cost as neocloud FCF line item).

**Known wall (one-time, flagged to Will):** PJM Data Miner 2 LMPs (actual price prints) need a free pjm.com account key — until that lands in `FORGE/tools/market-data/.env`, the price leg is demand+emergency+retail only.

**Routing context:** AEOLUS C3 grid-stress signals now route to you (was BRENT, whose mandate excludes power — fixed 7/10). Your ownership is PROVISIONAL: if the pre-registered spinout triggers fire (2nd PJM emergency pre-Labor-Day / 28/29 BRA at cap / the leg crowds out your macro lane during a live event — say so, that IS one of the triggers), a dedicated agent (WATT) takes it over with this instrument as its boot kit. Full scoping: `AGENTS/DAEDALUS/outbox/2026-07-10_to-PROME_tier3-gaps-and-power-agent-memo.md` §5.

*Move to processed/ on consume.*
