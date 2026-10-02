---
signal_id: SIG-W-20261002-018
date: 2026-10-02
timestamp: 2026-10-02T18:11:07Z
time_dispatched: 2026-10-02T18:11:07Z
timestamp_note: stamped from the system clock at write, not typed
source: Will-Telegram (msg 4873, ZeroHedge X post 16:34Z 'Another Tanker Struck & Damaged By Iran In Strait Of Hormuz')
origin: ["SABC News 2026-10-02 17:57 SAST, quoting UKMTO verbatim: 'A tanker was struck by an unknown projectile while transiting outbound through the Strait of Hormuz, causing a small fire and a blackout onboard'", "Caspianpost 2026-10-02 20:58 (local): 1122 GMT, outbound, small fire and blackout, vessel resumed its journey; Times of Israel liveblog 10/02 18:53 (local); newsquawk headline", "ZeroHedge 'Update(1233ET)' citing @christankerfund 'Another tanker struck and damaged. 6th alert in last couple of days'; Axios 10/02 via ZeroHedge on Patriot batteries"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["UKMTO", "Strait-of-Hormuz", "SIG-W-20261002-017", "SIG-W-20261001-033"]
corrects: SIG-W-20261002-017
corrects_direction: "FLIPS -017's 'no separate tanker attack on 10/02 was found': a NEW hit occurred 10/02 1122Z (UKMTO). -017's naming of 147-26 as Kazimah III (10/01) is unaffected."
kill_strings: ["No separate tanker attack on 10/02 was found", "no-new-10-02-attack-found"]
confidence: 0.85
confidence_language: "reports"
signal_type: correction
safety_net: clear
verdict: "Correction to -017: there WAS a new Hormuz tanker hit on 10/02. UKMTO: a tanker struck by an unknown projectile at 1122 GMT 10/02 while transiting OUTBOUND, causing a small fire and a blackout; fire extinguished, no casualties or pollution, vessel resumed its journey; vessel unnamed (SABC, Caspianpost, Times of Israel, newsquawk). -017's 'no separate attack on 10/02' was wrong when written (reports were up by ~16:00Z). A second, Panama-flagged INBOUND tanker hit on 10/02 is UNCONFIRMED (one Riviera headline, unreachable). Not sunk: GATE 2 untouched, losses 3."
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK", "SAM", "RED", "PROME"]
dispatch_note: "Will surfaced it (ZeroHedge). WALTER's own -017 search returned only the 10/01 event and was written up as an absence (MEMORY #28 class, n=3). Iran guards: ADD#26 (keyed on EVENT date 10/02 1122Z, outbound; distinct from 147-26 = 10/01 1750Z), POTUS channel = tape. Date traps excluded: Ship & Bunker 'UKMTO reports new ship attack' = 2026-06-27; Gulf News 'mystery projectile, fire out' = 121-26, 2026-08-25."
---
# Correction to `-017`: there WAS a new tanker hit in Hormuz on 10/02, at 11:22 GMT, outbound. Small fire, blackout, crew safe, ship unnamed.

**What was wrong:** `-017` said *"No separate tanker attack on 10/02 was found."* **There was one.** UKMTO reported it, and outlets were carrying it by ~16:00Z, before `-017` went out at 16:39Z. WALTER's search came back with only Thursday's event, and WALTER wrote that up as an absence. **Will caught it** (ZeroHedge, 12:34 ET).

**The new event (UKMTO, via SABC / Caspianpost / Times of Israel / newsquawk):**

| | |
|---|---|
| When | **Fri 10/02, 11:22 GMT** (07:22 ET) |
| Where / direction | Strait of Hormuz, **OUTBOUND** transit |
| What | struck by an **unknown projectile**: **small fire + blackout** (loss of power) |
| Outcome | **fire extinguished; no casualties; no pollution; the vessel resumed its journey** |
| Vessel | **not named** |
| Gates | **not sunk: GATE 2 untouched, losses stay 3** |

**The week's count (keyed by event date, ADD#26):** *Al Funtas* 9/28 · 146-26 (9/30, unread) · **147-26 = *Kazimah III*, 10/01 17:50Z** (`-017`) · **the outbound tanker, 10/02 11:22Z (this signal)** · ⚠️ a **Panama-flagged INBOUND tanker on 10/02** is **UNCONFIRMED**: one Riviera headline ("Kuwait-flagged VLCC, Panama-flagged tanker reported hit... fires on board, crew evacuated") that this box cannot reach. Search summaries say "at least four vessels this week" (attributed to UKMTO, not seen at UKMTO). @christankerfund (via ZeroHedge): *"6th alert in last couple of days."*

**Also in Will's link (context, not graded):** ZeroHedge relays **Axios (10/02): one Patriot battery was sent last month to protect a key Saudi oil facility, and another to a Qatari gas plant.** Trump: *"either Iran signs the deal, or it won't exist any longer"*, reported as weighing a renewed bombing campaign in the coming weeks. ⛔ **POTUS channel = tape, not information** (guard). Weighing ≠ ordered.

## Caveats
- **"By Iran" is ZeroHedge's headline, not UKMTO's.** UKMTO says "unknown projectile." Attribution is not carried.
- No vessel name, flag or position. UKMTO's own page returns 403 to this box.
- ⛔ **Date traps found during the check and NOT carried:** Ship & Bunker "UKMTO reports new ship attack in Strait of Hormuz" is **6/27**; Gulf News "tanker struck by mystery projectile... fire out" is **UKMTO 121-26, 8/25**. Both read like today's event.

## Requested action
**FALCON:** log the 10/02 outbound hit in the series beside 146-26 and 147-26 (*Kazimah III*), and check whether a Panama-flagged inbound tanker was also hit on 10/02. BRENT, HAWK, SAM, RED, PROME: information.
