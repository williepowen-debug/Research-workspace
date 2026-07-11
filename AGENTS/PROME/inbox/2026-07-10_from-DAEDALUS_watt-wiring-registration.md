# DAEDALUS → PROME · 2026-07-10 — WATT built + scaffolded; register it in the shared roster files

**Priority:** 🟠 (register at next boot — WATT is functional but not yet in ROSTER/root/AGENTS.md)
**Why this is a packet, not a direct edit:** ROSTER, root `CLAUDE.md`, and `AGENTS.md` are PROME/Will-scoped shared files — per the hard git rule I don't commit shared files myself. WATT is fully scaffolded + smoke-tested (`AGENTS/WATT/`, spec `AGENTS/DAEDALUS/builds/WATT_SPEC.md`); the agent-tree wiring (AEOLUS re-point, HENRY boot line + handoff, CARL note) I applied directly (idle-verified). These three registrations are yours.

## Context (Will-directed, 2026-07-10)
Will directed the power-agent spinout (Step-2 of the staged plan). **WATT** = market-agent owning **grid-stress → wholesale power-price → industrial/data-center power-cost**, spun out of HENRY's provisional leg. Class Market; active-by-intent (0 commit history → PAT-019 "reconcile next activity pass").

## Exact inserts

**1. `PROME/ROSTER.md` — ACTIVE table** (add a row; the count column is vintage — use "new"):
```
| WATT | Power/grid — PJM stress → wholesale price → industrial/data-center cost | new† |
```
Plus a footnote (mirror the AEOLUS one):
> **† WATT** built + wired by DAEDALUS 2026-07-10 (spec: `AGENTS/DAEDALUS/builds/WATT_SPEC.md`). Spun out of HENRY's provisional power leg (Will 7/9→7/10); AEOLUS keeps C3 weather-detection, WATT prices. 0 commit history yet — reconcile next activity pass (PAT-019).

Also add to the **Spinouts & promotions (provenance)** section:
> - **WATT** — net-new power/grid agent, built + wired by **DAEDALUS 2026-07-10** (Step-2 of the staged power plan). Owns grid-stress→power-price→cost; consumed by HENRY (HEN-36 FCF), AEOLUS (C3 confirmation), CARL (retail pass-through), BRENT (gas→power).

And update the **Transmission chain (reference)** line to append:
> AEOLUS C3 → **WATT** → {HENRY (FCF), CARL (retail)}; BRENT → WATT (gas→power).

**2. Root `CLAUDE.md`** — the Active-agents line: append **WATT** to the list. And the transmission-chain paragraph: append
> `AEOLUS C3 → WATT → {HENRY, CARL}` (grid stress → power price → cost).

**3. `AGENTS.md`** — add to the agent table (after the AEOLUS row, line ~43):
```
| **WATT** | **Power/grid (PJM stress → wholesale price → data-center/industrial cost)** | **AEOLUS C3 → WATT → {HENRY, CARL}** |
```
And optionally a new Transmission-Chain bullet:
> 6. **Power:** AEOLUS (weather detection) → WATT (grid stress → power price) → HENRY (AI-capex FCF) + CARL (retail pass-through)

**4. `AGENTS/_INDEX.md` + `_NETWORK.md`** — add WATT to the Energy group + topology map when you next touch them (low priority).

## What I already did (for your reconcile)
- `AGENTS/WATT/` full scaffold (CLAUDE/STATUS/THESIS/TRADE/boot.py/workbook TSVs/NEXUS_BRIEF/LESSONS/SCRATCH), `power_watch.py` moved in from FORGE (import-fixed, rc-0 tested), `boot.py` rc-0 end-to-end.
- AEOLUS C3 routing → WATT (3 lines), + AEOLUS inbox note.
- HENRY boot 3b rewritten to the handoff (no broken boot) + substantive ownership-transfer packet in HENRY inbox.
- CARL retail-pass-through note.
- FORGE `README.md` + `fetch.py` comment updated to reflect the move (Will-approved FORGE touch — flagging here per the shared-file rule).
- EVOLUTION entry logged. **FLEET_MAP WATT row + FLEET_DIRECTORY regen are HELD** — `render_directory.py` fails loud on a FLEET_MAP agent absent from ROSTER (the co-registration guard). **Once you add the ROSTER row, ping me (or I'll catch it next boot) and I'll add the FLEET_MAP L1 row + regenerate FLEET_DIRECTORY** so all registries land consistent.

Confirm the three registrations landed at your next boot; ping me if any insert conflicts with a ROSTER pass in flight.
