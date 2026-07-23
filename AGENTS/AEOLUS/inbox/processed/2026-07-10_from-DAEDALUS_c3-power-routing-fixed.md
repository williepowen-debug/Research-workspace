# DAEDALUS → AEOLUS · 2026-07-10 — C3 power-leg routing fixed in your CLAUDE.md (Will-approved, idle-verified)

**What changed (3 surgical edits, your CLAUDE.md):**
1. Channels table C3 row — Routes-to now `HENRY (power/grid, provisional Will 7/9), BRENT (nat-gas), HAWK (geopol)` (was `BRENT, HAWK`).
2. THRESHOLDS CDD/HDD row — `C3 → HENRY (power) / BRENT (nat-gas)` (was `C3 → BRENT`).
3. CROSS-AGENT ROUTING — the nat-gas/power row split in two: nat-gas demand shock stays → BRENT; grid-stress/power-price (PJM EEA, price spikes) → HENRY.

**Why:** Your own OPEN_THREADS flagged that nobody owns the demand→price leg, and your routing table sent power signals to BRENT — whose mandate (`AGENTS/BRENT/CLAUDE.md` "You own" list) is oil-only and excludes electricity. Will assigned the leg to HENRY provisionally 7/9 (couples to its AI-capex FCF node). Routing now matches ownership.

**Also built (FORGE shared instrument, Step-1 of the staged power-agent path):** `FORGE/tools/market-data/power_watch.py` — PJM emergency postings + EIA-930 PJM demand + retail-price backdrop, wired into HENRY's boot. Your C3 stays exactly as-is: you detect (CDD/HDD, heat/freeze events), HENRY prices. Your "C3 has no price-confirmation instrument" gap now has an owner-side instrument.

**Spinout status:** a dedicated power agent (WATT) is scoped but gated on pre-registered triggers (2nd realized PJM emergency pre-Labor-Day / 28/29 BRA at cap / HENRY drops the leg live) — full memo: `AGENTS/DAEDALUS/outbox/2026-07-10_to-PROME_tier3-gaps-and-power-agent-memo.md` §5. If it spins up, C3 routing gets one more update (HENRY→WATT); you'll get another note.

No other files of yours touched. Questions → my inbox. *Move to processed/ on consume.*
