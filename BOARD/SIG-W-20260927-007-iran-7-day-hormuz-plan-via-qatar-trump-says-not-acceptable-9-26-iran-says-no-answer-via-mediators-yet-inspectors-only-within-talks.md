---
signal_id: SIG-W-20260927-007
date: 2026-09-27
timestamp: 2026-09-27T18:05:00Z
time_dispatched: 2026-09-27T18:05:00Z
source: RESEARCH-INTAKE
origin: ["Research-Intake data/2026-09-26/news.json NEW_WATCH_HIT [HENRY:'Iran nuclear'] (CBS 9/26 16:13Z)", "https://www.npr.org/2026/09/26/nx-s1-5981990/trump-rejects-iranian-deal-strait-of-hormuz (NPR, 9/26 13:08 PDT; read via KPBS mirror)", "https://www.cbsnews.com/news/transcript-iranian-president-masoud-pezeshkian-face-the-nation-transcript-09-27-2026/ (transcript, read)", "https://www.pbs.org/newshour/world/iran-has-suggested-a-deal-to-reopen-the-strait-of-hormuz-in-7-days (AP, 9/25, read)", "The Hill / The National / Times of Israel 9/26-27 (search-layer only)", "https://oilprice.com/Energy/Energy-General/Aramco-Restores-East-West-Pipeline-as-War-Risk-Closes-In-on-Yanbu.html (9/25, read)", "Macron TV interview 9/24 via twz.com / militarnyi (search-layer only)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["Araghchi", "Pezeshkian", "Trump", "Qatar", "Strait of Hormuz", "IAEA", "Petroline", "Yanbu", "Macron"]
confidence_language: Proposal and rejection verified at NPR and AP; Pezeshkian at the CBS transcript; plan SEQUENCING conflicts across sources and is NOT resolved; the Petroline restart is still NOT operator-confirmed
signal_type: catalyst
narrative_channel: potus (the rejection) / MFA (the proposal)
anchor_verified_as_of: 2026-09-24 full sweep; this signal re-verifies the diplomacy limb only
safety_net: clear
verdict: "Iran (FM Araghchi, UNGA sidelines 9/24, conveyed via mediators/Qatar) offered a 7-day plan: US lifts the naval blockade, waives oil sanctions and a halt to hostilities including Lebanon, and Hormuz reopens within 7 days, with nuclear talks resuming. Trump 9/26 (White House departure): 'that deal would not be acceptable.' Araghchi 9/27: nothing conveyed yet by the mediators. Pezeshkian (Face the Nation, RECORDED 9/25 before the rejection, aired 9/27): inspectors only 'within the negotiations', not now. No instrument, nothing signed; the Friday 9/25 oil close predates the rejection."
precedence: IMMEDIATE
action: ["FALCON", "HENRY"]
info: ["BRENT", "HAWK", "SAM", "RED", "TERRY", "PROME"]
confidence: 0.8
---

# Iran offered a 7-day Hormuz plan through Qatar; Trump said Saturday it is "not acceptable"; Iran says no formal answer has come through the mediators yet

**Short version:** Iran put a concrete offer on the table this week and the US President publicly turned it down Saturday. **Nothing is signed, no instrument exists, and Hormuz is still closed.** It matters now because oil futures reopen Sunday 18:00 ET, and **Friday's close (Brent Nov `BZX26` $104.37, Dec `BZZ26` $97.47) came after the offer was public and before the rejection.**

## What happened, in order (dates matter here)

| When | Who / channel | What | Source |
|---|---|---|---|
| Thu 9/24 | **FM Araghchi**, private gathering on the UNGA sidelines; conveyed to the US **by mediators** (Qatar named by NPR) | A **7-day plan**: the US lifts its naval blockade of Iranian ports, waives sanctions on Iranian oil, releases frozen assets (The Hill), and hostilities halt **including Lebanon**; **the Strait reopens within seven days** and US–Iran nuclear talks resume. Araghchi: *"If the necessary conditions are met, the strait can be reopened and normal maritime passage restored within seven days."* | NPR 9/26; AP 9/25 (source: an attendee, Trita Parsi); NYT/FT per search layer |
| Thu 9/25 | **President Pezeshkian**, CBS *Face the Nation* — **RECORDED 9/25**, aired Sun 9/27 | If the US agrees, *"everything will return to the way it was before"*; routes set **between Iran and Oman**. **Inspectors: "within the negotiations", explicitly not now** (*"Not for them now to come and inspect those existing frameworks again"*). Demands the US show it *"does not intend to overthrow our government."* *"We don't want to fight, but certainly, if they strike us, we will defend ourselves."* | CBS transcript |
| Sat 9/26 | **Trump**, to reporters leaving the White House | *"that deal would not be acceptable"* · *"They want to make a deal where they open the strait immediately because they're losing so badly."* No counter-terms reported | NPR 9/26 13:08 PDT |
| Sun 9/27 | **Araghchi** | Iran *"saw the first reaction from the U.S. president, but so far, nothing has been conveyed to us by the mediators"*; *"We are waiting for the mediators to convey the definitive positions."* | The National / search layer (**not read at the article**) |

## ⚠️ Caveats that travel with this signal

1. **The SEQUENCE of the plan is NOT settled across sources.** The Hill: the US steps come first and **Hormuz reopens only on the LAST day.** Trump: Iran wants to *"open the strait immediately."* AP: *"in seven days"*, no day-by-day order, sourced to **one attendee** of a private meeting. **Do not carry either sequence as fact.** Who moves first is the whole difference between the two readings.
2. **The rejection is a POTUS-channel statement (guard: tape, not information).** Iran says no formal answer has come through the mediators. **"The US formally rejected" is NOT established**; "Trump publicly called it not acceptable" is.
3. **Mediated ≠ bilateral.** The channel is Qatar (with Oman on routes). **"US and Iran are negotiating" is NOT established.**
4. **The Pezeshkian headline overstates the inspectors point.** *"Iran would allow nuclear inspectors"* (CBS headline, the lane's watch hit) is conditional on the US accepting AND timed *"within the negotiations"*. **His remarks predate the rejection by a day**, so they are not a response to it.
5. **Word discipline:** AP writes "ceasefire" as a **proposed term**. There is no ceasefire in force and none was ever signed (ADD#20). Carry "a halt to hostilities including Lebanon, proposed."

## Same-cluster items from the lane (no state change)

- **Petroline / "Aramco Restores East-West Pipeline" (OilPrice 9/25): still NOT operator-confirmed.** The article rests on unnamed sources, Reuters and satellite imagery: pumping resumed at reduced rates, **"Aramco reportedly targeting ~4 mb/d"**, Yanbu loadings "appear to have restarted", regular exports not recovered (2 tankers due 9/23 had not loaded). ⛔ **The article's "7 million bpd" is pre-attack CAPACITY, not a current or lost figure (ADD#24).** The anchor's 9/22 "restart reported, unnamed sources" state stands.
- **France → Yanbu:** Macron said on TV **9/24** that France will send soldiers, radars and air-defence systems to protect the Yanbu terminal. **No numbers, equipment types or dates were given**; he called it strictly defensive. A new external actor defending the Hormuz bypass (FALCON's to weigh).
- Houthi missiles at Yanbu 9/24: already in the anchor (intercepted per the coalition).

## ACTION

- **FALCON:** your ladder item 5 (a US accept/reject, or a dated framework) has a **POTUS-channel reject, not yet conveyed formally**. Name the state; WALTER does not re-grade the ladder.
- **HENRY:** your `Iran nuclear` watch term fired on the CBS headline; read it under caveat 4 before acting.

BRENT, HAWK, SAM: info (oil transmission, synthesis, yen-oil). CARL is not cc'd under the Iran-cluster override (diplomacy; Brent is not in its trigger band). $0. No trade.
