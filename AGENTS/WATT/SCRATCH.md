# WATT — SCRATCH (next-session pickup)

**2026-07-10 — BUILD SESSION (DAEDALUS scaffold, Will-approved spinout).**

WATT is live. Spun out of HENRY's provisional power leg. Step-1 instruments (`power_watch.py`) moved in from FORGE and re-import-pathed; smoke-tested rc 0 with live data. Matrix seeded: P1 live (quiet-but-armed, demand 88.9% peak), P2 live (🔴 structural — both BRAs at cap), **P3 + P4 are GAPS carrying inherited/no reads.**

**▶ PICK UP HERE (next session, in priority order):**
1. **Run `boot.py`** first — confirm power_watch + staleness + predictions-due all green.
2. **Close P3 gap** — pull interconnection-queue depth (LBNL Queued Up 2026 edition) + IPP load-growth guidance (VST/CEG/NRG/TLN latest earnings). Re-score VX-WATT-P3, update STATUS.
3. **Close P4 gap** — ask BRENT for Henry Hub; compute spark spread vs PJM power price. Re-score VX-WATT-P4.
4. **Process inbox** — HENRY ownership-handoff packet (integrate the HEN-36 coupling detail), AEOLUS C3 routing-confirmation.
5. **PJM_API_KEY** — if Will has registered it, wire the LMP leg into `power_watch.py` (upgrades P1 from demand-proxy to actual price).
6. Resolve/extend PREDICTIONS (WATT-01 28/29 BRA Dec; WATT-02 EEA2 recurrence by 9/7) at boot.

**Open dependencies (not WATT's to do):** Will → PJM_API_KEY registration (~5min); HENRY → drop its provisional-owner role + power_watch boot line (packet routed); PROME → confirm ROSTER row.
