---
signal_id: SIG-W-20261002-017
date: 2026-10-02
timestamp: 2026-10-02T16:39:00Z
time_dispatched: 2026-10-02T16:39:00Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER (Will asked 10/02: 'I just read something about a tanker attack today')
origin: ["arabnews.com 'Tanker attacked in Strait of Hormuz: UK maritime agency' 2026-10-02 01:54 UTC, read via WebFetch (vessel NOT named by UKMTO)", "TradeWinds 'Fire burns on Kuwait Oil Tanker Co VLCC after attack in Strait of Hormuz' + Seatrade 'Tanker catches fire after first Hormuz attack in October' + Splash247 10/02: headlines and search summaries only (403/paywall)", "vesseltracker.com: Kazimah III, IMO 9329693, MMSI 447152000, flag Kuwait"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["Kazimah-III", "KOTC", "UKMTO-147-26", "Al-Funtas", "SIG-W-20261001-033"]
confidence: 0.75
confidence_language: "reports"
signal_type: context
safety_net: clear
verdict: "UKMTO 147-26 (tanker struck by an unknown projectile in Hormuz, 1750Z Thu 10/01, fire, crew safe; carried unnamed in -1001-033) is named by trade press on 10/02 as the Kuwait-flagged VLCC KAZIMAH III (Kuwait Oil Tanker Co). That makes it KOTC's second VLCC hit in four days after AL FUNTAS on 9/28. No KOTC or Kuwaiti statement found. No separate tanker attack on 10/02 was found; Arab News's 'Thursday, October 2' is a mislabel (Thursday = 10/01)."
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK", "SAM", "RED"]
dispatch_note: "Will-prompted check. Additive to -1001-033 section 1. Iran guards: ADD#26 (key on event date 10/01 and UKMTO number, not report date), ADD#13/GATE 2 (not sunk, losses 3). Two search-summary figures withheld as probable merges (see Caveats). RED pull-complete."
---
# Update to `-1001-033`: the Hormuz tanker hit on Thursday 10/01 is named by trade press as the Kuwaiti VLCC *Kazimah III*. No separate attack on 10/02 was found.

**Short version:** `-1001-033` carried **UKMTO 147-26**: a tanker struck by an unknown projectile in the Strait of Hormuz at **17:50 UTC on Thursday 10/01**, with a fire and the crew safe. UKMTO did **not** name the ship. On 10/02 the shipping trade press named it as the **Kuwait-flagged VLCC *Kazimah III*, operated by Kuwait Oil Tanker Co (KOTC)** (TradeWinds headline: *"Fire burns on Kuwait Oil Tanker Co VLCC after attack in Strait of Hormuz"*; Seatrade; Splash247). That makes it **KOTC's second VLCC hit in four days**, after *Al Funtas* on 9/28.

| | Status |
|---|---|
| Event | UKMTO 147-26, **Thu 10/01 17:50Z**, Strait of Hormuz, unknown projectile, fire, crew safe |
| Vessel | ***Kazimah III***, Kuwait flag, IMO 9329693 (vesseltracker), KOTC: **trade-press identification, not UKMTO's** |
| Pattern | second KOTC VLCC in four days (*Al Funtas*, 9/28, north of Khasab) |
| Damage | unknown |
| Claim | none found |
| Gates | **not sunk, no mine: GATE 2 untouched, losses stay 3** |
| A new attack on 10/02? | **none found.** Arab News (published 10/02 01:54Z) says "Thursday, October 2". **Thursday was 10/01.** It is the same event, published the next day |

## Caveats, including two figures deliberately NOT carried
- **The vessel name comes from trade press,** reachable here only as headlines and search summaries (403/paywall). **No KOTC or Kuwaiti government statement was found.**
- ⛔ **"Carrying ~2 million barrels of crude": NOT carried.** That figure appears in search summaries, but the same searches return the **March 2026 *Al-Salmi* story** ("Kuwaiti tanker carrying 2 million barrels ... Dubai port"). It is a probable merge.
- ⛔ **"Fire extinguished, continued underway to a port of refuge" (attributed to Vanguard): NOT carried for *Kazimah III*.** That exact wording is Riviera's line for ***Al Funtas*** on 9/28. It is a probable merge.
- ⛔ **"About eight kilometres off Oman" and "several projectiles":** search-summary only, and they conflict with UKMTO's "an unknown projectile". Not carried as fact.
- ⚠️ **Name-collision trap:** a ***Kazimah*** (KOTC) was attacked by an Iranian helicopter in the 1980s tanker war. Do not merge.

## Requested action
**FALCON:** fold the name into the 146/147-26 reconcile. BRENT, HAWK, SAM, RED: information.
