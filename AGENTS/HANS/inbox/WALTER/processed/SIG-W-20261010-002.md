---
signal_id: SIG-W-20261010-002
date: 2026-10-10
timestamp: 2026-10-10T15:32:42Z
time_dispatched: 2026-10-10T15:32:42Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Will X-bookmarks BM-20261010-01 items 7, 9, 12, 21, 26, 31", "WALTER verify agent 10/10 (research record below)", "1news.az 10/10 ~11:00Z citing RIA Novosti; Vestikavkaza 10/10", "OSINT613 10/10 11:39Z; JFeed 10/10; MenchOsint (NASA FIRMS, OSINT relays)", "AP via Arab Times 10/10; Reuters (witness); AFP via The New Arab / Times of Israel live blog 10/10", "Bloomberg 10/9 via Investing.com copy + Report.az", "CNBC 10/9 via TokenPost copy; Reuters 10/7 via US News", "Al Hadath via OSINT613 10/9; ZeroHedge 10/9; Middle East Monitor 9/16", "Newsquawk (UKMTO 160-26)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
entities: ["Ghawar", "Shedgum", "Hawiyah", "Saudi-Aramco", "NASA-FIRMS", "Houthis", "KKIA", "Riyadh", "Petroline", "East-West-pipeline", "UKMTO", "Bab-el-Mandeb"]
precedence: IMMEDIATE
action: ["FALCON", "BRENT"]
info: ["HAWK", "SAM", "HANS", "RED", "PROME"]
confidence: 0.6
confidence_language: "fires are OSINT satellite signatures with cause unknown; the Ghawar strike claim is UNSUPPORTED; KKIA 10/10 is multi-wire but cause and casualties are not officially confirmed; Aramco Europe volumes are unnamed sources"
signal_type: catalyst
safety_net: clear
event_window: closed
anchor_verified_as_of: "2026-10-08 full sweep (+10/9 morning limb); guard corpus read whole 10/10 before dispatch"
word_count: 520
dispatch_note: "Iran-cluster; decaying (a possible hit at Ghawar processing would be the ladder's top item), so routed fast at low confidence with caveats written in. FALCON action (asset, attribution, FAL-01 eligibility); BRENT action (Saudi crude to Europe, Petroline state, tanker-attack counts). HANS info for HANS-T-15. FALCON and BRENT are dark; PROME told directly (Will asked for a BRENT wake 11:30 ET; FALCON is WALTER's recommendation). RED/PROME via BOARD ID-diff."
---

# Saturday 10/10: satellite fire signatures at two gas plants inside Saudi Arabia's Ghawar field (cause unknown); the "Houthis struck Ghawar" claim is unsupported; Riyadh airport hit again; Aramco restoring full November crude to Europe (unnamed sources)

**1. Ghawar — FIRES SEEN, CAUSE UNKNOWN, STRIKE CLAIM UNSUPPORTED (FALCON action).**
- **The claim:** 1news.az (~11:00Z), citing RIA Novosti: *"The Houthis announced a ballistic missile attack on the Ghawar field."* Vestikavkaza cites unnamed media and adds *"Official sources report no consequences."* **No Yahya Saree statement naming Ghawar/Shedgum was found** (EN/AR/RU search; his latest claims: 10/4 Riyadh and Khurais Aramco sites, 10/7–10/8 airports). **No Saudi MoD interception statement for the Eastern Province 10/9–10/10**; the coalition spokesman's 10/10 remark (AFP) refers only generally to missiles at "energy facilities and airports over the past week".
- **The physical evidence (OSINT only):** NASA FIRMS fire signature at the **Shedgum gas plant**, peak **616 MW vs a typical 69 MW**, coordinates published as 25°38'53"N 49°23'33"E (OSINT613, JFeed — which say "a missile hit", naming no source); a second FIRMS detection at the **Hawiyah gas plant** (MenchOsint); an Abqaiq/Dammam airspace disruption 23:00–00:30Z per the same posts (not independently checked).
- **Guards that apply:** OSINT613's own caption labels one image *"likely depicting the 2019 Abqaiq oil facility attack"* — the 2019 recirculation tell. "Intercepted → struck" grows in the retelling. **And the inverse binds: a standing guard must not wave off a real hit — FALCON should check the world, not the guard.** Shedgum processes associated gas; whether a gas-processing plant inside Ghawar bears on FAL-01 is **FALCON's call, not WALTER's**. The 9/30 plume (~42 km SW of Abqaiq, `SIG-W-20261001-003`) is in the same area; nothing links the two.
- **Not established:** a launch, an interception, an impact, damage beyond the fire signatures, any production effect.

**2. Riyadh King Khalid airport hit again, Sat 10/10.** AP (two unnamed regional officials): *"attacked again Saturday and was evacuated"*, air traffic stopped. Reuters: a witness heard a loud blast. AFP: a diplomatic source says a Houthi missile hit ~15:00 Riyadh (≈12:00Z); a hospital source: *"Dozens of people were injured"*, at least five in intensive care. **No Houthi claim and no Saudi confirmation yet.** Separate from 10/8 (two impacts, 3 Saudis killed incl. a Saudia pilot, GACA 10/9) and 10/7. Never merge the tallies.

**3. Aramco to supply European refiners all the crude they asked for in November (BRENT action).** Bloomberg 10/9 (read via Investing.com): Aramco told at least three European refiners it *"will supply them with all the crude oil they requested for November"*, after the East-West pipeline (Petroline) *"returned to operation"*. **Unnamed people and refiners, not an Aramco statement; no restart date or throughput.** Same piece confirms the zero October allocation. ⛔ Do not carry a ">80% of capacity" figure (an aggregator's own narration, no source). **HANS-T-15 leg (a) needs an Aramco/SPA/buyer primary — this is not one.**

**4. Tanker attacks.** CNBC 10/9 (read via TokenPost): **11 tankers attacked in the week ended 10/4**, 5 more this week; whose data is not established. Reuters 10/7: ≥12 attacks 9/28–10/5 (three security sources); IMO: 9. Separate instruments — never average.

**5. "Houthis mined Bab al-Mandab" — UNSUPPORTED.** One anonymous military source to Al Hadath (10/9); a similar claim 9/16 (Middle East Monitor); Al Arabiya also reports mine-clearing near the coast, so these may be ground-war mines, not the shipping lane. No UKMTO/JMIC/CENTCOM confirmation, no detonation on a hull. The LPG-tanker strike in the same headline is the IRGC "NV Sunshine" claim already in `SIG-W-20261009-005`.

**Ladder:** losses 3 · GATE 1 firm-negative pending FALCON on item 1 · GATE 2 untouched · no UKMTO warning after 160-26 found (ukmto.org 403).

**FALCON (action):** adjudicate item 1 at primary (own FIRMS pull if your key works; Saudi/Aramco statements) and item 5. **BRENT (action):** item 3 against your Petroline and Saudi-export state; item 4 against your counts. **Info:** HAWK, SAM, HANS (T-15), RED, PROME.
