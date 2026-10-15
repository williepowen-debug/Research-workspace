---
signal_id: SIG-W-20261011-007
date: 2026-10-11
timestamp: 2026-10-11T21:10:45Z
time_dispatched: 2026-10-11T21:10:45Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["UKMTO incident page 'Suspicious Activity UKMTO #28082036, 11 October 2026' (screenshot in Will X-bookmark @MenchOsint 2026-10-11 19:31Z, read)", "Reuters via Devdiscourse 2026-10-11 23:52 IST (UKMTO: tanker incident near Sohar anchorage; crew and damage unknown)", "ANI via The Tribune, Muscat 2026-10-12, updated 01:10 IST (India's Shipping Minister Sonowal + Indian Embassy Oman)", "Will X-bookmarks BM-20261011-03 items 2-5"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["MT-Petro-Dolphin", "Sohar", "Oman", "Gulf-of-Oman", "drone", "MT-Valthera", "GEM-NO-2", "UKMTO", "Sonowal", "Aramco"]
precedence: IMMEDIATE
action: ["FALCON", "BRENT"]
info: ["HAWK", "SAM", "HENRY", "CARL", "TERRY", "PROME"]
confidence: 0.8
confidence_language: "the Sohar incident is in UKMTO's own record and Reuters; the vessel name, drone cause and crew figures come from India's shipping minister and embassy (ANI); attacker not identified; Valthera's match to a UKMTO number is not established"
signal_type: catalyst
safety_net: clear
event_window: closed
word_count: 453
dispatch_note: "Addendum to SIG-W-20261011-006 (same desks, same referent: the 18:00 ET CME reopen; covered by the 2313bf2b2 doorbell to PROME). FALCON/BRENT action; HAWK/SAM/HENRY info; CARL via BOARD ID-diff (pull-complete; Iran-cluster override met: vessel strike); TERRY/PROME via ID-diff. Guards: ADD#26 (same day is not same event), maritime-date clock collision (IST vs UTC), anti-merge."
---

# Gulf of Oman, Sun 10/11: the tanker MT Petro Dolphin (Nicaragua flag) was hit by a drone at Sohar anchorage, Oman, and 2 of its 11 Indian crew are missing (India's shipping minister). UKMTO logged it as a "suspicious activity" incident. India also names the Valthera as a 10/11 Hormuz hit

**1. Sohar (outside the strait, in the Gulf of Oman).**
- **UKMTO's own record:** "Suspicious Activity #28082036, 11 October 2026". UKMTO received a report of an incident involving a tanker near Sohar anchorage, Oman; crew, damage and environmental impact were unknown at the time. It is classed **suspicious activity, not attack**. Reuters carried the same.
- **India's account:** Shipping Minister Sarbananda Sonowal (ANI, Muscat, updated 01:10 IST 10/12) names the ship as the **Nicaragua-flagged MT Petro Dolphin**, "subjected to a **drone attack** at Sohar Anchorage on October 11". Of 11 Indian crew, **9 are rescued and safe and 2 are missing**; the Indian Embassy in Oman gives the same count. The Coast Guard is searching.
- **Attacker: not identified.** The drone cause is the minister's word; UKMTO has not stated a mechanism.
- Two more facts: this is a hit in **Oman**, the mediator, and it is **outside Hormuz**, so the GATE 2 sea-check applies. **No sinking is reported; losses stay at 3.**

**2. A name for one weekend Hormuz hit, unmatched.** Sonowal: the **Marshall Islands-flagged M/T Valthera** (11 Indian crew, all safe) was hit by an unknown projectile in the Strait of Hormuz "on October 11", causing a fire.
- UKMTO **162-26** (Sat 10/10 1920Z, fire) falls on 10/11 on India's clock (00:50 IST). **164-26** (Sun 10/11 1200Z) states damage but no fire. **Which one Valthera is, is INDETERMINATE.** Never merge it on the date alone (clock collision guard).
- Sonowal also calls the 10/9 GEM NO. 2 hit a drone attack at **Sharjah** anchorage; UKMTO 160-26 said "13NM west of Al Jazeera, UAE". Carry both descriptions.

**3. Other bookmarks folded here:**
- ZeroHedge's "several tankers on fire" videos add nothing beyond `-006`.
- A reader's note that **Aramco has published no damage acknowledgment since August** is an unverified count, but the limit it points at is real: GATE 1 cannot wait on an Aramco statement (cf. the anchor: the Aramco CEO's 10/05 "restoring damaged infrastructure" names no asset).

**FALCON (action):** grade the Sohar drone hit (Oman, outside the strait; missing crew) and match Valthera to 162-26 or 164-26. **BRENT (action):** the Gulf of Oman is now hit too, so fold it into the transit and war-risk read for the 18:00 ET reopen. **Info:** HAWK · SAM · HENRY · CARL via ID-diff · TERRY via ID-diff (Will's 37 USO shares, VLO ×1; no trade proposed) · PROME via ID-diff.
