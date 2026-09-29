---
signal_id: SIG-W-20260929-011
date: 2026-09-29
timestamp: 2026-09-29T19:04:18Z
time_dispatched: 2026-09-29T19:04:18Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34); every WALTER read below precedes this stamp"
source: Will-Telegram image (@EGYOSINT X posts) + WALTER Iran pre-dispatch guard
origin: ["Will-Telegram BM-20260929-05 item 9: @EGYOSINT \"A third pumping station, PS-8 (24.4778, 43.3772), also appears to have been hit in the drone attack on Saudi Arabia's East-West Crude Oil Pipeline, with a possible burn scar ...\" quoting @EGYOSINT (~5h earlier) \"Extensive damage is visible in today's sat imagery at Pump Station 9 ... following the Sept. 10 drone attack launched from Iraq\"", "anchors/IRAN_WAR.md (Petroline: ATTACKED / SHUT / DAMAGED NOT ESTABLISHED; 9/14 imagery pumping-station fire damage; FALCON holds Al Mesba'ah / Al Dhekra at C3; exports reported resumed 9/28 at ~3.5 mb/d vs ~7 capacity, -019/-020)", "anchors/IRAN_WAR_GUARDS.md scoped read (2019 Petroline recirculation trap; \"burn scars\" 2019 description flag; ADD#22 authenticate-not-dismiss tell; ADD#24 SHUT != HIT; capacity-as-loss KILL)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
entities: ["East-West (Petroline) pipeline", "Pump Station 8", "Pump Station 9", "Saudi Aramco", "EGYOSINT", "FALCON", "BRENT"]
confidence_language: "One OSINT account's reading of satellite imagery (provider, resolution and capture date not stated in the screenshot); hedged in its own words (\"appears\", \"possible burn scar\"). No operator, ministry or wire confirmation. Iran guard corpus read SCOPED (the 66,781 B file is over the read cap), not whole."
signal_type: research
safety_net: clear
verdict: "An OSINT account (@EGYOSINT) says satellite imagery shows EXTENSIVE damage at Pump Station 9 and a possible burn scar at Pump Station 8 (24.4778N, 43.3772E) on Saudi Arabia's East-West crude pipeline, attributing both to the 9/10 drone attack \"launched from Iraq\". It calls PS-8 a THIRD station hit. On the anchor's three states this is ATTACKED (per imagery) and SHUT (per the MoE); DAMAGED is still per nobody, since no operator has confirmed or quantified damage. Why it may matter: Yanbu exports were reported resumed 9/28 at ~3.5 mb/d vs ~7 mb/d capacity (-020). Damaged pump stations are one possible mechanism for a half-rate restart. This is NOT established; it is a hypothesis for FALCON to grade."
precedence: ROUTINE
action: ["FALCON"]
info: ["BRENT", "RED"]
confidence: 0.4
dispatch_note: "Iran-cluster pre-dispatch guard run: anchor read (9/29, current); IRAN_WAR_GUARDS.md read SCOPED (the file is 66,781 B, 205% of the read cap, so a whole read is not possible in one pass; blocks read: the 2019 Petroline recirculation trap, the 2019 \"burn scars\" flag, ADD#22, ADD#24 incl. capacity-as-loss). Applied: carried ATTACKED / SHUT / DAMAGED separately (never \"destroyed/disabled\"); date-checked (the claim ties to the 9/10 attack, not 2019); attribution \"from Iraq\" carried as the poster's and CONTESTED per anchor; PS-8/PS-9 NOT merged with FALCON's C3 station names (Al Mesba'ah / Al Dhekra) because they may be the same sites under numeric names; \"7 mb/d\" appears only as CAPACITY. ADD#22 tell: independent confirmation would be an operator statement or a named imagery provider with a date, and neither exists here. FALCON ACTION: owns the asset and the basis (anchor). FALCON is DARK -> DOORBELL_LOG row. BRENT INFO (flow vs capacity)."
---
# OSINT imagery claims Petroline pump stations 8 and 9 were damaged in the 9/10 attack. That would be attacked per imagery, damaged per nobody, and it could explain the half-rate restart

**Short version:** one OSINT account (@EGYOSINT) says satellite imagery shows **extensive damage at Pump Station 9** and a **possible burn scar at Pump Station 8** on Saudi Arabia's East-West crude pipeline, from the **9/10** attack. It calls PS-8 a **third** station hit. **No operator, ministry or wire has confirmed damage.**

**Why FALCON should look:** Yanbu exports were reported resumed 9/28 at **~3.5 mb/d flow vs ~7 mb/d capacity** (`-020`, Bloomberg, one source). Damaged pump stations would be **one possible mechanism** for a half-rate restart. **This is a hypothesis, not a finding.**

| State (anchor discipline) | Per whom |
|---|---|
| **ATTACKED** | wires + imagery (9/10) |
| **SHUT** | Saudi MoE (9/11), restart reported 9/22, exports reported 9/28 |
| **DAMAGED** | **nobody yet.** This OSINT imagery is a claim, not an operator statement |

## Guards applied (Iran pre-dispatch; guard file read in scope, not whole)

1. **Date-checked.** The claim ties to the 9/10 attack. It's not the May-2019 Petroline recirculation, though that attack's description (drones, East-West line, pumping stations) is near-identical, which is exactly why the date matters.
2. **Not merged:** FALCON already holds two pumping stations at C3 by name (**Al Mesba'ah, Al Dhekra**). PS-8/PS-9 may be the **same** sites under numbers, or different ones. Unresolved.
3. **Attribution "launched from Iraq" is the poster's.** The anchor carries it as **contested** (Houthi and Iraq-corridor reads both live).
4. **"7 mb/d" is CAPACITY only.** Never a loss figure (KILL-ON-SIGHT ①).
5. **Independent confirmation absent** (ADD#22 tell): no named imagery provider, capture date or resolution, and no operator statement. **Authenticate, don't dismiss.**

**ACTION (FALCON):** grade whether PS-8/PS-9 damage is established, and whether it bears on the restart rate. $0.
