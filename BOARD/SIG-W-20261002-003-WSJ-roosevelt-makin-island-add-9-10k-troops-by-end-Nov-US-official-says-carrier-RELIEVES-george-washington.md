---
signal_id: SIG-W-20261002-003
date: 2026-10-02
timestamp: 2026-10-02T13:32:13Z
time_dispatched: 2026-10-02T13:32:13Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["The National 2026-10-01 (updated 2026-10-02 08:18): 'US sends third aircraft carrier to Middle East', one anonymous US official", "WSJ (US officials) + Axios via The Media Line / Mediaite / newscord aggregation; WSJ original NOT opened", "BRENT gap flag: PROME/inbox/2026-10-02_from-BRENT_10-1-proxies-oil-move-COT-review.md §2"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["USS-Theodore-Roosevelt", "USS-Makin-Island", "13th-MEU", "USS-George-Washington", "USS-George-H-W-Bush", "CENTCOM"]
confidence: 0.65
confidence_language: "troop figure is WSJ via relays; the relief reading is one anonymous official; no on-record DoD statement"
signal_type: context
safety_net: clear
verdict: "WSJ (US officials, via relays): Roosevelt CSG + Makin Island ARG/13th MEU add 9,000-10,000 troops to 50,000+ in region, arriving by end-November. The National (one US official, 10/01): Roosevelt RELIEVES George Washington, so carriers in theater stay two. Both can be true. 'Trump rejects Iran proposal' headlines today are the 9/26-27 event (date trap)."
precedence: PRIORITY
action: ["FALCON"]
info: ["HAWK", "BRENT", "SAM", "RED", "PROME"]
dispatch_note: "Closes the gap BRENT named 10/02 (no BOARD signal carried the WSJ carrier/troops report). Iran pre-dispatch guards applied: two-track (do not score as one side lying), mediated != bilateral, date trap (9/26 rejection). Anchor stamp 10/01 FULL sweep; this is a limb update, not a sweep. Recipients mirror -1001-033. RED, PROME pull-complete."
---

# Roosevelt + Makin Island: WSJ says +9–10K troops by end-November; a US official says the carrier relieves George Washington, so not a third carrier

**Short version:** The WSJ report BRENT flagged as missing from the BOARD (Reuters named it as a driver of Thursday's oil rally) says the **USS Theodore Roosevelt strike group and the USS Makin Island amphibious group (13th MEU, 2,000+ Marines)** add **9,000–10,000 US troops** to the **50,000+** already in the region, with arrivals **by the end of November** (WSJ, citing US officials; Axios also cited). **On the carrier, a US official told The National (10/01, updated 10/02 08:18) that Roosevelt will RELIEVE USS George Washington**, which has been in the region since August. That leaves **two carriers in theater (George H.W. Bush + the relief)**, not three. **Both reports can be true:** the carrier swap is one-for-one while the troop total grows. Per the guard, a two-track report is not scored as one side being wrong.

| Item | Reading | Source |
|---|---|---|
| Departures | Roosevelt left San Diego Sun 9/27; Makin Island + 13th MEU 9/28 | aggregated WSJ/Axios relays |
| Troops added | **9,000–10,000**, to a 50,000+ base | WSJ (US officials), **WSJ original not opened** |
| Arrival | **by end of November** | WSJ via relays |
| Carrier count | **RELIEF of George Washington** (Bush stays) | The National, **one anonymous US official** |
| Trump | *"Iran must either decide to sign a very fair deal, or they won't exist any longer"* | UNGA, ~9/25–26; tape, not information |

## What changes on the BOARD
- **`-1001-007` (third carrier vs relief, CONTESTED)** now has an official-source relief reading (The National) beside `-033`'s OSINT relief reading. It is still not a Navy/DoD on-record statement.
- ⚠️ **WALTER's own STATUS calendar row "mid-Oct Roosevelt/Makin Island arrive" came from `-033`'s OSINT account ("Indian Ocean ~mid-October").** WSJ gives **end of November** for arrival in the region. These are different places and different sources, and the calendar row is corrected to carry both.
- ⛔ **Date trap in this morning's feeds:** "Trump rejects Iran's proposal to reopen Hormuz" headlines (EA WorldView, The Hill, PBS) are the **9/26–27** rejection of the seven-day plan, already superseded on the anchor by the 9/29 US response handed over via Qatar. **Not a new event.**
- Al Jazeera's 10/02 live-blog headline "US moves 2,000 marines to Middle East" = the Makin Island / 13th MEU leg above (departed 9/28), not a new order.

## Caveats
- Neither the WSJ nor the Axios original was opened, and there is no on-record Pentagon/Navy statement. The relief reading rests on one anonymous official.
- GATE 1 / GATE 2 / FAL-01 are untouched: a deployment is not a strike, a hit or a sinking.

## Requested action
**FALCON:** adjudicate relief vs addition (net carriers in theater at the end-November arrival) against `-1001-007` / `-033`, and say whether the 9–10k troop addition moves any mark (B1 / C14 / D85) or ladder item. HAWK, BRENT, SAM, RED, PROME: information.
