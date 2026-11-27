---
signal_id: "SIG-W-20261126-008"
date: "2026-11-27"
timestamp: "2026-11-27T03:54:04Z"
dispatched: "2026-11-27T03:54:04Z"
source: "web search summaries 2026-11-26 between 22:52 ET and 03:53:19Z (Reuters via investing.com, thereader.ai, piqmarkets; Al Jazeera; tafs.uz, newscord on Araghchi; Arab News Japan, Shipping Herald, Tehran Times titles); FORGE/tools/market-data fetch.py 2026-11-27T03:53:19Z"
origin: ["web searches between 22:52 ET and 03:53:19Z", "FORGE fetch.py 03:53:19Z"]
action: ["BRENT", "FALCON"]
info: ["HAWK", "HENRY", "SAM", "VIOLET", "HANS", "RED", "PROME"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.7
confidence_language: "reports: search summaries of named wires; vendor prices are last trades, not settles"
resources: 1
safety_net: "clear"
cluster: "IRAN_HORMUZ"
domain: "OIL_ENERGY"
entities: ["Brent", "BZF27", "IRGC Navy", "Strait of Hormuz", "Araghchi", "Qatar", "Pakistan", "Ras Tanura"]
word_count: 409
dispatch_note: "ROUTINE sweep card on Will's word. ACTION BRENT (settle and price), FALCON (claims). Iran pre-dispatch guard read this session. RED, PROME by BOARD diff."
event_window: "open"
---
# Night sweep Nov 26: Brent January settled $96.57, +2.1%, on the Jazan refinery hit and mine reports (Reuters via summaries), heading for its first weekly gain of November; IRGC Navy says two tankers on an 'unauthorized route' hit mines Nov 25 and Iran won't restore normal Hormuz shipping until its demands are met; Araghchi says Qatar and Pakistan mediation continues; ES 7,304.75 and BZF27 96.48 vendor at 03:53Z

# Night news sweep, Thu 11/26 from 22:52 ET (window after the collector's 18:55 ET run)

| # | Item | Read | Owner |
|---|---|---|---|
| 1 | **Brent January (BZF27) settled $96.57, +2.1%, on 11/26** (ICE traded; US closed), Reuters linking the move to the Jazan refinery attack and mined-tanker reports; Asia: Brent above $96, 'first weekly gain in November', still about 20% lower for the month (Investing.com) | search summaries; settle not read at ICE. Vendor BZF27 96.48, CLF27 85.66 at 03:53Z (last trade, non-session flag) | BRENT |
| 2 | **IRGC Navy (state media):** two oil tankers hit mines and caught fire 11/25 after trying an 'unauthorized route'; separate Army statement of a tanker in a 'restricted zone' (card 20261126-004 item 3). Tehran: no normal shipping until demands are met (blockade lifted, war ended on all fronts). Tehran Times title: 'downs US drones' in the strait | search summaries; Tehran Times page not read; vessels unnamed, no UKMTO or US confirmation found; US officials reported rejecting the mine account (tracker site, weak) | FALCON |
| 3 | **Araghchi 11/26:** Qatar and Pakistan mediation with the US continues; 'ideas were presented'; demands must be met before Hormuz opens (blockade, safe passage, sanctions, oil-export exemptions, frozen assets) | search summaries of several outlets; no direct US-Iran meeting found | FALCON, HAWK |
| 4 | **Ras Tanura (card 20261125-008):** Saudi authorities say four drones downed, no hit confirmed; Aramco and the government did not answer Reuters on damage | search summary | FALCON, BRENT |
| 5 | **Markets, vendor at 03:53Z (not closes):** ES 7,304.75 (11/25 evening 7,239.75), NQ 26,713.50, USD/JPY 159.22, Nikkei 58,435 (+1.63%), Hang Seng 22,395 (+0.76%), gold GC 3,657 | FORGE fetch.py; holiday non-session flags on futures | HENRY, SAM |

- **Searched, nothing new found by my search:** Jazan restart (none published; ministry calls the stoppage temporary); Yanbu, Rabigh or Jeddah hits on 11/26; Kuwait follow-up from Italy; Russia-Ukraine strikes or talks dated 11/26 to 11/27; a MOFCOM countermeasure; a bank cyber outage; CoreWeave news; St. Johns evacuations.
- **Guards (IRAN_WAR_GUARDS):** item 2 is an IRGC claim; a mine claim does not fire GATE 2 on relay. Item 3 is MEDIATED, not bilateral.
- **So what:** oil is pricing the Saudi Red Sea hits and the mine claims together (Brent up more than 6% in two sessions per Reuters summaries); OPEC+ meets Sun 11/29. Friday's US session closes 13:00 ET.
