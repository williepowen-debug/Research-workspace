---
signal_id: SIG-W-20260930-005
date: 2026-09-30
timestamp: 2026-10-01T00:50:19Z
time_dispatched: 2026-10-01T00:50:19Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram image (msg 4789, batch BM-20260930-01 item 5) of an X post (text matches @HormuzLetter status 2105318283024961949, posted 9/30 11:26 AM on Will's clock) + WALTER verification 2026-09-30 ~23:5xZ
origin: ["X @HormuzLetter 9/30: 'Yemen's Houthis appear to have struck the Abqaiq oil processing facility ... EUMETSAT Meteosat imagery shows a black smoke plume roughly 90 km long trailing from the site for at least seven hours, from 06:45 UTC'", "sh1n.org relay of @hey_itsmyturn, 2026-09-30 15:34 UTC: 'Aramco pumping station WEST of Abqaiq reported on fire at ~0700Z today, no statements by the Houthis'", "WALTER extended web searches ~23:5xZ: NO Saudi MoD, SPA, Aramco, CENTCOM or wire report of a 9/30 Abqaiq-area strike or fire found; the Bloomberg 'Houthis attack Saudi Arabia, claim to target Aramco facilities' item surfaced by search is dated 2026-09-24 (Yanbu/Taif intercepts, no Abqaiq)", "Tape: BZZ26 +1.7% on 9/30 (BRENT 10:17 ET intraday 98.20 vs 96.12 prior settle-window proxy)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
entities: ["Abqaiq", "Aramco", "Houthis", "EUMETSAT Meteosat", "East-West pipeline (Petroline)"]
confidence_language: "OSINT only. The imagery is described, not authenticated by WALTER (ADD#22: provenance raises status, it does not settle it). The object is contested between the posts: 'the Abqaiq processing facility' vs 'a pumping station WEST of Abqaiq'. No attribution evidence: 'appear to have' in the original, 'no Houthi statement' in the relay. No operator, state or wire confirmation found at ~23:5xZ, ~17h after the claimed start."
signal_type: pattern-match
safety_net: clear
verdict: "HYPOTHESIS, NOT AN EVENT. OSINT accounts report a large smoke plume on Meteosat imagery from ~06:45 UTC 9/30 at an Aramco site in the Abqaiq area; one relay places it at a PUMPING STATION WEST of Abqaiq, which is where the East-West line (Petroline) starts. NOTHING establishes that the Abqaiq stabilization plant was hit, that anything was struck rather than burning, or who did it. Carried so FALCON can grade it against its imagery tools and the half-rate Petroline restart; KILLED from the claim: 'Houthis struck the Abqaiq plant' and '5-7% of global oil supply' (a capacity figure quoted as a loss: KILL-ON-SIGHT ①, ADD#24)."
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK"]
confidence: 0.3
dispatch_note: "Iran-anchor pre-dispatch guard RUN: IRAN_WAR_GUARDS read (KILL-ON-SIGHT ① Abqaiq, 7/25 2019-Abqaiq trap, 'intercepted -> struck' retelling, ADD#15 FIRMS-unconfirmed, ADD#22 image authentication, ADD#24 shut/hit/capacity, METHOD NOTE 'check the world, not the guard'). Resolved on the world, not the guard: no primary found; the tape does not show an Abqaiq-scale shock (Dec Brent +1.7% on a day that also carried the Russia diesel-ban extension); but a real plume at an unconfirmed site cannot be dismissed. Domain GEOPOL_ENERGY Iran/Gulf -> FALCON action (owns FAL-01, the Gulf theater and the Petroline grade; same lane as -0929-011 pump-station claim). BRENT info (crude/Petroline), HAWK info (theater parent). CARL-info override not applied: no confirmed supply event. Precedence PRIORITY, not IMMEDIATE: a hypothesis, not a state change; confidence 0.3 = the filter floor. FALCON DARK -> DOORBELL_LOG row, NOT doorbelled: WALTER's own Iran FULL sweep is due 10/01 and re-checks this first; a primary confirming a hit at ANY time re-triggers IMMEDIATE."
---

# HYPOTHESIS: OSINT reports a smoke plume at an Aramco site west of Abqaiq from ~06:45 UTC 9/30. No Saudi, Aramco or wire confirmation. "Abqaiq plant hit" is NOT established.

**Will passed the X post by Telegram.**

| Claimed | Status at ~23:5xZ 9/30 |
|---|---|
| A ~90 km black smoke plume on EUMETSAT Meteosat imagery from ~06:45 UTC for 7+ hours | **Described by OSINT accounts, not authenticated here** |
| Location: "the Abqaiq oil processing facility" | ⚠️ **Contested:** a relay says a **pumping station WEST of Abqaiq**, where the East-West line (Petroline) starts |
| "Houthis appear to have struck" | **No attribution evidence**; the relay says no Houthi statement |
| "5 to 7% of global oil supply" | ⛔ **KILLED:** Abqaiq's nameplate capacity quoted as a loss (KILL-ON-SIGHT ①, ADD#24) |
| Saudi MoD / SPA / Aramco / CENTCOM / wires | **Nothing found** (two extended searches); the Bloomberg "Houthis attack Saudi Arabia" item is dated **9/24** (Yanbu/Taif intercepts), not today |
| Market | Dec Brent **+1.7%** on 9/30, on a day that also carried Russia's diesel export-ban extension. **Not an Abqaiq-scale shock** (2019: 5.7 mb/d offline; Brent settled about +15% on the next trading day) |

⚠️ **Why it is carried at all:** the guard file's own method note says a standing guard against the 2019 Abqaiq trap is itself a false-negative risk. A real plume at an unidentified Aramco site, next to the Petroline restart (`SIG-W-20260928-019/-020`) and the pump-station damage hypothesis (`SIG-W-20260929-011`), is worth FALCON's grade. **The claim that the Abqaiq plant was struck is not.**

**ACTION (FALCON):** grade the hypothesis: is there a fire at an Aramco site west of Abqaiq on 9/30 (your imagery / FIRMS tools; FIRMS needs coordinates, per ADD#15), is it on the East-West line, and does it bear on the Petroline restart or `-0929-011`. **Gate 1 / FAL-01 is NOT fired by this signal.** Your call. $0.

**INFO (BRENT, HAWK):** no ask. WALTER re-checks this first at the Iran full sweep due 10/01; **a primary confirming a hit re-routes as IMMEDIATE.**
