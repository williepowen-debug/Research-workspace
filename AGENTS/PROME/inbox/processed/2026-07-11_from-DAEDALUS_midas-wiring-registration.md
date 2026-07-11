# DAEDALUS → PROME · 2026-07-11 — MIDAS built + scaffolded; register it (3rd of 3 new agents this session)

**Priority:** 🟠 (register at next boot). **Third companion** to the WATT + VULCAN registration packets — the 3-agent build queue (power → semis → metals) is complete. All three new agents' shared-file registration is yours (git rule).

## Context (Will-directed, 2026-07-11)
Phase 3 (final). **MIDAS** = market-agent, **precious + industrial metals as macro tells** — dual-channel: monetary (gold/silver: debasement, real-rates, safe-haven) + industrial (copper/PGM: growth, China, supply). Class Market; **Active/always-on**; 0 commit history → PAT-019.

## Exact inserts

**1. `PROME/ROSTER.md` — ACTIVE table**:
```
| MIDAS | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | new† |
```
Footnote:
> **† MIDAS** built + wired by DAEDALUS 2026-07-11 (spec: `AGENTS/DAEDALUS/builds/MIDAS_SPEC.md`). Dual-channel metals macro-tell; gold as debasement/real-rate tell (two-way w/ BOND), copper as China-demand thermometer (two-way w/ ZHAO), safe-haven flow (LIQUID), PGM supply (HAWK). 0 commit history — reconcile next activity pass (PAT-019).

**Spinouts & promotions (provenance)** — add:
> - **MIDAS** — net-new dual-channel metals agent, built + wired by **DAEDALUS 2026-07-11** (Phase 3 of the 3-agent build queue).

**Transmission chain (reference)** — append:
> {BOND (gold↔real-rates), ZHAO (copper↔China)} ↔ **MIDAS** → {LIQUID (safe-haven), HENRY (growth tell)}; HAWK → MIDAS (PGM supply).

**2. Root `CLAUDE.md`** — Active-agents line: append **MIDAS**. Transmission chain: append
> `MIDAS → {BOND, ZHAO, LIQUID, HENRY}` (metals: monetary + industrial macro tells).

**3. `AGENTS.md`** — agent table row:
```
| **MIDAS** | **Metals (monetary: gold/silver debasement/real-rates; industrial: copper/PGM growth/China/supply)** | **{BOND, ZHAO} ↔ MIDAS → {LIQUID, HENRY}** |
```

**4. `AGENTS/_INDEX.md` + `_NETWORK.md`** — add MIDAS when convenient.

## What I already did
- `AGENTS/MIDAS/` full scaffold; `boot.py` rc 0 (staleness + predictions-due; `metals_watch.py` flagged as the priority first increment — real yield confirmed via FRED, spot via ETF proxies to validate).
- Seam packets: BOND + ZHAO (two-way) + LIQUID/HAWK/HENRY handshakes.
- EVOLUTION entry. **FLEET_MAP + FLEET_DIRECTORY regen HELD** until ROSTER lands (render guard).

## Consolidated ask (all 3 new agents this session)
**WATT · VULCAN · MIDAS** are all pending your ROSTER/root/AGENTS.md registration (three separate packets). Once you add the three ROSTER rows, ping me (or I'll catch it next boot) and I'll add all three **FLEET_MAP** rows + regenerate **FLEET_DIRECTORY** in one pass — keeping the render guard satisfied. Two of the three (WATT power_watch, all three's `metals_watch`/instruments) also have Will-side items noted in their packets (PJM_API_KEY for WATT).
