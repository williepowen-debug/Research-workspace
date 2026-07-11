# MIDAS — SCRATCH (next-session pickup)

**2026-07-11 — BUILD SESSION (DAEDALUS scaffold, Will-approved; Phase 3 / final of the 3-agent queue).**

MIDAS is live. Dual-channel metals agent — monetary (gold/silver) + industrial (copper/PGM). No day-1 spot instrument; the value at birth is the dual-channel structure + clean seams. M1 (gold) carries the confirmed real-yield read (DFII10 2.31, FRED 7/9); M2/I1/I2 are honest GAPS awaiting spot pulls. `boot.py` = staleness + predictions-due only.

**▶ PICK UP HERE (next session, priority order):**
1. **Build `metals_watch.py`** (THE priority first increment) — real yield (FRED DFII10, confirmed working) + gold/silver/copper/Pt/Pd spot (ETF proxies GLD/SLV/CPER/PPLT/PALL via shared FORGE `fetch.py` — futures GC=F errored on test, validate the proxies) + gold/silver ratio. Wire into boot.py as leg 0 (PAT-041: durable cadence at build time, same session).
2. **M1 quantification** — gold spot vs real-yield divergence = the debasement premium (the live signal). Route to BOND (real rates) + LIQUID (safe-haven). Resolve MIDAS-01 by 9/30.
3. **I1 first pull** — copper spot + LME/COMEX inventory + China imports = the Dr.-Copper/China thermometer. Route to ZHAO. Resolve MIDAS-02 by 9/30.
4. **M2 / I2 pulls** — silver + GSR; Pt/Pd + SA/Russia supply.
5. **Process inbox** — BOND + ZHAO seam packets (the two-way ones), LIQUID/HAWK/HENRY handshakes.

**Discipline reminder (LESSONS L-01):** keep the monetary and industrial channels SEPARATE — gold up + copper down is a coherent risk-off read, not a contradiction. Don't collapse to "metals up/down."

**Open dependencies (not MIDAS's to do):** PROME → ROSTER/root/AGENTS.md registration; BOND/ZHAO → integrate the two-way seams.
