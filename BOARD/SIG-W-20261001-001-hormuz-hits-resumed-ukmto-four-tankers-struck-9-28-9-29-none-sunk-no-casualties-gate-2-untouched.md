---
signal_id: SIG-W-20261001-001
date: 2026-10-01
timestamp: 2026-10-01T15:14:59Z
time_dispatched: 2026-10-01T15:14:59Z
timestamp_note: "stamped from `date -u` in the same command as the write (MEMORY #34)"
source: WALTER Iran full sweep 2026-10-01 (Opus verify-research subagent, report AGENTS/WALTER/research/2026-10-01_iran-full-sweep.md §4), surfaced by No1 Daily Digest 10/01 + ZeroHedge 9/30
origin: ["UKMTO late reports 9/28-9/29 (four), via relays: Maritime Executive 2026-09-30 14:56; Reuters wire syndicated by MarineLink/Baird/OilPrice 10/01; TASS 9/30 ('no reports of casualties'); Newsquawk 9/30 09:40Z ('an LNG tanker was struck by an unknown projectile on September 29th'); Seatrade snippet 'UKMTO released four late reports ... from 28 and 29 September'", "UKMTO warning 146/26 dated 2026-09-30 exists (indexed URL) but ukmto.org returned 403: CONTENTS AND POSITIONS UNREAD", "Vessel names from Vanguard Tech / IMO tracking / Marisks, NOT from UKMTO"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
entities: ["UKMTO", "AL FUNTAS", "MERSIN PROSPERITY", "SINBAD", "AL RUWAIS", "ADNOC L&S", "Anglo-Eastern", "Strait of Hormuz"]
confidence_language: "The EVENTS (four UKMTO late reports of projectile strikes 9/28-9/29) are confirmed through a Reuters wire and several maritime outlets; the UKMTO primary itself was unreadable (403), so positions, corridor and attacker are NOT established. Vessel identities come from third-party trackers and two of them have conflicting flag/type data."
signal_type: pattern-match
safety_net: clear
verdict: "STATE CHANGE vs the anchor's 9/28 line ('UKMTO reports no attacks since 9/23'): UKMTO published FOUR late reports of tankers struck by unknown projectiles in Hormuz, AL FUNTAS 9/28 (Kuwait-flagged crude tanker, fire extinguished, underway) and three on 9/29 (MERSIN PROSPERITY VLCC, port side; SINBAD Aframax, inbound; one LNG-or-products tanker named AL RUWAIS by trackers). No casualties, NO sinking, no mine => GATE 2 untouched, losses stay at 3. CORRECTED from the circulating framing: 'all three UAE-owned/managed' is WRONG (SINBAD is Anglo-Eastern-managed); AL RUWAIS is LNG/Bahamas per Vanguard but an oil-products tanker/Liberia per Reuters/Marisks; MERSIN PROSPERITY flag Liberia vs Vanuatu. 'Southern corridor' is OSINT framing, not a UKMTO position."
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK", "SAM"]
confidence: 0.75
dispatch_note: "Iran-anchor pre-dispatch guard RUN: IRAN_WAR_GUARDS read whole-by-section 10/01 (ADD#26 five discriminators applied: four separate events, same day != same event, event date from the reports not the 9/30 warning date; ADD#24 a wire's 'off X' / 'southern corridor' is not a fix; 'VESSEL SUNK' theater check: no sinking anywhere; July-7 AL REKAYYAT named-vessel trap checked: these names are not the July-7 set; clock collision: 9/28 'Monday evening' AL FUNTAS kept on the relays' date, UTC vs Gulf-local unresolved without the primary). Grep owners first (MEMORY #7): FALCON, BRENT, HAWK carry none of the four names. Domain GEOPOL_ENERGY Iran/Gulf -> FALCON action (Hormuz tanker attacks, VESSELS ledger, GATE 2). BRENT info (crude/LNG transit), HAWK info (synthesis, war-risk), SAM info (registered GEOPOL_ENERGY row info). CARL-info override not applied: no supply loss established. PRIORITY not IMMEDIATE: no gate fires, events are 2-3 days old and already in the tape. FALCON DARK -> DOORBELL_LOG row with -002/-003 (one pointer to PROME)."
---

# Hormuz hits resumed: UKMTO reported four tankers struck by unknown projectiles 9/28–9/29. None sunk, no casualties. GATE 2 untouched (losses stay at 3).

The anchor's last line on this (9/28) was "UKMTO reports no attacks since 9/23". **That is no longer true.**

| Vessel (names from trackers, not UKMTO) | Event date | What was reported | Type / flag / manager | Sunk? |
|---|---|---|---|---|
| **AL FUNTAS** | 9/28 (Mon evening) | Struck by unknown projectile, **fire extinguished**, underway | Kuwait-flagged crude tanker | No |
| **MERSIN PROSPERITY** | 9/29 | Crude tanker struck on its **port side** | VLCC 299k dwt; manager ADNOC L&S; ⚠️ flag **Liberia vs Vanuatu** (sources disagree) | No |
| **SINBAD** | 9/29 | **Inbound** tanker struck | Aframax, Liberia; manager **Anglo-Eastern (not UAE)** | No |
| **AL RUWAIS** | 9/29 | UKMTO: "an **LNG tanker** was struck" | ⚠️ **LNG/Bahamas** (Vanguard Tech) **vs oil-products tanker/Liberia, ADNOC L&S** (Reuters/Marisks) | No |

**Established:** four UKMTO late reports, unknown projectiles, attacker unnamed, no casualties reported, **no sinking, no mine.**
**Not established:** UKMTO positions (ukmto.org 403; warning 146/26 dated 9/30 unread), the corridor ("southern corridor" is OSINT wording), the attacker, AL RUWAIS's real type and flag, MERSIN PROSPERITY's flag.
⛔ **Not carried:** "all UAE-owned/managed" (SINBAD is Anglo-Eastern) · any merge of these four into one event (ADD#26).

**Transit context (floors, not levels — vendors disagree ~17×):** Windward 16 (24h to 9/28) and 17 (9/29) vs IMF PortWatch 1 (9/27); Kpler/NYT: ~10 mb/d through the strait in September vs ~16 prewar. Denominator stays 88/day.

**ACTION (FALCON):** add the four hulls to your VESSELS ledger with event dates as reported, grade against GATE 2 (no sinking: not fired) and your marks, and reconcile with the 9/28 "no attacks since 9/23" read. Your call on attribution. $0.

**INFO (BRENT, HAWK, SAM):** no ask. Hormuz projectile strikes are running again after a 5-day gap.

📌 **Flagged for FALCON, not re-verified here:** the anchor's "9/23 bulk carrier ADRIFT, on fire" is reported as the **MV CAPE DAO**, hit by **two torpedoes, with one Indian seafarer killed** (The National with a Reuters image; Gulf News; gCaptain). The anchor carries neither the torpedo mechanism nor the death. No sinking reported, so GATE 2 is not affected.

Full evidence and links: `AGENTS/WALTER/research/2026-10-01_iran-full-sweep.md` §4, §7.
