---
signal_id: SIG-W-20261001-033
date: 2026-10-01
timestamp: 2026-10-01T22:06:25Z
time_dispatched: 2026-10-01T22:06:25Z
timestamp_note: stamped from `date -u` at write, not typed
source: Will-Telegram
origin: ["Will via Telegram 2026-10-01 ~22:03Z, BM-20261001-08: item 5 @BabakTaghvaee1 4:45 PM 10/1 with a UKMTO 147-26 warning card; item 4 @bonzerbarry video watermarked Alfaqaar313 ('reportedly footage from Yanbu earlier today'); item 8 @MoloMonitor carrier thread", "WALTER search ~22:1xZ: Ship & Bunker, Times of Israel liveblog, investingLive, Arab Times all carry UKMTO 147-26 (report 1750 UTC 10/01). UKMTO primary NOT opened (403 to this box per the 10/01 sweep). Misbar fact-check 2026-09-27 read (a different, debunked Yanbu video)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
entities: ["UKMTO-147-26", "Strait-of-Hormuz", "Yanbu-crude-terminal", "Alfaqaar313", "USS-Theodore-Roosevelt", "USS-Makin-Island", "GATE-2", "FAL-01"]
confidence: 0.75
confidence_language: UKMTO 147-26 is four-outlet corroborated at the level of the warning text; the tanker, weapon and actor are unnamed. The Yanbu video is UNVERIFIED in place AND date. The carrier thread is one OSINT account
signal_type: pattern-match
safety_net: clear
verdict: "UKMTO 147-26 (Attack): third-party report at 1750 UTC 2026-10-01 of a tanker struck by an unknown projectile while transiting the Strait of Hormuz, causing a fire; crew reported safe; damage and environmental impact unknown. Tanker, projectile and actor not named by UKMTO. No sinking, no mine: GATE 2 untouched, losses stay 3. Separately, a video said to show a fire at the Yanbu crude export terminal 'earlier today' is UNVERIFIED in place and date."
precedence: PRIORITY
action: ["FALCON"]
info: ["HAWK", "BRENT", "SAM", "RED"]
dispatch_note: "Iran pre-dispatch guard: anchor read at boot (full sweep 10/01, UKMTO 146-26 of 9/30 unread there); GUARDS ADD#26 (UNKNOWN PROJECTILE is a recurring phrase: keyed here on report time 1750Z 10/01 and warning number 147-26), ADD#13 (a hit is not a sinking), ADD#22 (state-actor artefact class for the video), INTERCEPTED-to-STRUCK retelling class. IRGC anti-ship cruise missile attribution is the poster's, not UKMTO's: NOT carried as fact. RED pull-complete."
---

# UKMTO 147-26: a tanker hit by an unknown projectile in Hormuz at 17:50 UTC, fire, crew safe. Plus an UNVERIFIED Yanbu terminal-fire video

## 1. UKMTO 147-26 (corroborated)
**UKMTO Incident 147-26, "Attack":** a **third-party report at 1750 UTC on 2026-10-01** of an **oil tanker struck by an unknown projectile while transiting the Strait of Hormuz, causing a fire.** **Crew reported safe**; **damage and environmental impact unknown.** UKMTO did **not** name the tanker, the projectile or the party responsible. It's carried by Ship & Bunker, Times of Israel, investingLive and Arab Times. **WALTER did not open UKMTO's own page** (403 to this box).
- **Against the gates:** **no sinking, no mine. GATE 2 untouched; losses stay 3.** The hit series that resumed 9/28–9/29 (`-001`) continues.
- ⛔ **The "IRGC used an anti-ship cruise missile" attribution is the X poster's (@BabakTaghvaee1), not UKMTO's.** UKMTO says "unknown projectile." Not carried as fact.
- **ADD#26:** "unknown projectile, Hormuz" is a recurring UKMTO phrase. This one is keyed on **147-26 / 1750Z 10/01**. The anchor's sweep recorded **146-26 (9/30) as unread**, so 146 and 147 are distinct and both remain to be reconciled.

## 2. Yanbu crude terminal fire video: UNVERIFIED (place and date)
X @bonzerbarry: *"Reportedly footage from Yanbu earlier today. This is the crude export terminal."* The clip is watermarked **Alfaqaar313** (a Telegram channel) and shot from a vessel or pier. It shows a dark plume with flame at its top above a waterfront tank farm.
- **No wire, Saudi, Aramco or UKMTO report of a Yanbu incident on 10/01 was found.**
- **Precedent:** on 9/27 Misbar debunked a different "Yanbu attacked" video (actually a Puerto Rico power-plant fire, 9/23). This clip is not that one, but the class is live.
- **A flame atop a plume at a terminal is also what a flare looks like** (same trap as the 9/30 Bu Hasa claim, INDETERMINATE). ⛔ **Do not carry ATTACKED, DAMAGED or "terminal hit."** If it ever verifies, a terminal is **not** FAL-01 (production), but it would bear directly on the Yanbu export route that `-027` reports recovering.

## 3. Carrier thread (one OSINT account): consistent with relief, not a third carrier
@MoloMonitor: **USS Theodore Roosevelt (CVN-71) and USS Makin Island** are en route from San Diego, arriving in the Indian Ocean **around mid-October**. The account expects them to **relieve USS George Washington and USS Boxer**, not to add a third carrier. This is consistent with the relief reading in `-007` (third carrier vs relief CONTESTED); it is **one account, not a Navy statement**.
- ⛔ **NOT carried:** the same thread's claim that **"the 5th Fleet base in Manama, Bahrain, is no longer operational."** No primary. The anchor has **no executed Bahrain in-port hit**, so this would be a major state change asserted in passing.

## Requested action
FALCON: log 147-26 against the hit series (losses unchanged), reconcile it with 146-26, and decide whether the Yanbu video merits a check. HAWK, BRENT, SAM: information only.
