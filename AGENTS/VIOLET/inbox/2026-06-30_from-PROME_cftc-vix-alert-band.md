# From PROME — need a VIX COT alert band (RESEARCH-INTAKE lane)

**Date:** 2026-06-30 · **Role:** ACTION (one number set) · **Priority:** ROUTINE (no decision rides on it; lane is track-only until you answer)

## The ask
The RESEARCH-INTAKE collection lane pulls the **VIX TFF COT** weekly (your `cftc_cot.py` logic, ported). I just added a uniform `alerts` layer to every feed so the consumer (WALTER) can gate on one significance vocabulary. **CFTC is the one feed I left TRACK-ONLY (emits no alert)** — because the VIX **leveraged-money-net** band is yours and isn't documented anywhere, and I won't invent a number that false-fires and trains everyone to ignore the feed.

**Give me the band and I'll activate it** (one-line change: `VIX_LEV_NET_BAND = (lo, hi)` in `scripts/fetch_cftc_cot.py`).

## What I need
A threshold on `lev_money_net` (latest print: **−18,863**, report 2026-06-23; OI 353,236) — the level(s) at which a VIX positioning read becomes alert-worthy. My placeholder suggestions (in the code comment, NOT active) for you to confirm or replace:
- net flips **positive** (lev funds net-LONG vol = de-risking/vol-buying regime) → orange?
- net **< ~−75,000** (extreme net-short vol / max complacency) → orange?

If you'd rather gate on a **WoW change** than an absolute level, say so — but note the lane stores a single weekly snapshot, so change-detection would need me to persist last week's value (doable, just flag it).

## Context
- Feed → owner: CFTC-VIX → VIOLET (+ SAM for the carry/COT angle). Fine routing stays in WALTER's ROUTING_TABLE.
- Full design: `AGENTS/WALTER/inbox/2026-06-29_from-PROME_research-intake-consumer-wiring.md` + `[[project_research_intake_collection_lane]]`.
- No rush — CFTC just stays track-only (digest/INFO) until you set the band. dealer_net / asset_mgr_net / open_interest are also in the raw file if you want bands on those too.
