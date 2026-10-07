---
signal_id: SIG-W-20261007-007
date: 2026-10-07
timestamp: 2026-10-07T14:57:03Z
time_dispatched: 2026-10-07T14:57:03Z
timestamp_note: stamped from the system clock at write, not typed
source: PROME 10/7 catch-up (AFP/FMT, Reuters, gCaptain, Euronews, Al Jazeera, Saudi civil aviation) + RESEARCH-INTAKE lane 10/5-10/6
origin: ["AFP via FMT 10/5 (Khurais pump station, MULTI on strike)", "Reuters 10/6 Saudi energy minister ~5.8 mb/d (lane)", "Bloomberg/Reuters sources 10/5 flows normal (via PROME)", "gCaptain/Reuters (Hormuz, MULTI)", "Euronews/Al Jazeera (Bab el-Mandeb, claims MULTI)", "Saudi civil aviation (Jizan/Najran)", "Tasnim via Newsquawk 10/5 (Jeddah, UNVERIFIED)", "OilPrice 10/5 (refinery fire claims)", "Euronews 10/5 (rial, exports)", "Kpler (Gulf exports 18.3 mb/d)"]
entities: ["Saudi-Aramco", "Khurais", "East-West-pipeline", "Petroline", "UKMTO", "MT-On-Peace", "Lipsi", "Khasab", "IRGC", "Bab-el-Mandeb", "Operation-Yemen-Dawn", "Mocha", "Dhubab", "Houthis", "Jizan-airport", "Najran-airport", "Rabigh", "Jeddah-refinery", "Qatar", "Kpler"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
signal_role: cluster_mediating
precedence: PRIORITY
action: ["FALCON", "BRENT"]
info: ["HAWK", "SAM", "NEXUS", "TERRY", "RED", "PROME"]
confidence: 0.7
confidence_language: "Strikes on a pumping station and on airports are MULTI or official. Refinery strikes and Bab el-Mandeb control are UNVERIFIED claims. Flow status rests on unnamed sources plus a ministerial figure."
signal_type: catalyst
safety_net: clear
narrative_channel: houthi
anchor_unverified_as_of: 2026-10-04
dispatch_note: "Pre-dispatch Iran guard APPLIED: anchor read (last full sweep 10/01; limbs verified 10/04; next full sweep ~10/08 NOT run in this session). IRAN_WAR_GUARDS read SCOPED (grep-located blocks: the 7/25 2019 Abqaiq/Khurais trap, intercepted-to-struck, ADD#26 UKMTO five discriminators, mediated not bilateral, POTUS-channel tape, ADD#20 ceasefire kill), not whole. No verify-research spawn: no Agent tool in this container. Facts are carried at PROME's grades, not re-verified. cluster_mediating: a fighting-widens vs oil-eases split (Gulf exports back near pre-war while hits continue), so RED and NEXUS are info. GATE 1/FAL-01 firm-negative and GATE 2 untouched (losses 3) on the evidence here; FALCON names gate state. BRENT is on action for the East-West flow evidence (BG-02 resolver LAPSED 9/25: new evidence, not a live trigger)."
---
# Iran cluster 10/4–10/7: a Khurais PUMP STATION on the East-West line was hit (flows reported normal, ~5.8 mb/d); Hormuz hits continue (MT On Peace, 12 injured), none sunk; Bab el-Mandeb ground offensive (control UNVERIFIED); Houthi hits on Saudi airports confirmed, refinery claims UNVERIFIED; diplomacy is tape

**Guard status:** anchor `anchors/IRAN_WAR.md` last full sweep 10/01 (next ~10/08, not run here); limbs verified 10/04. Fresh kinetic state since then ⇒ **`anchor_unverified_as_of: 2026-10-04`**, and a Full-WALTER sweep is owed ~10/08. IRAN_WAR_GUARDS was read SCOPED (named blocks above), not whole.

## 1. Saudi infrastructure
- **Khurais PUMP STATION on the East-West line, hit ~10/4** (AFP via FMT 10/5; MULTI on the strike). AFP: the line "stopped again." **Bloomberg and Reuters sources, 10/5: flows normal.** **Saudi energy minister, 10/6 (Reuters, lane): East-West throughput reached ~5.8 million barrels** (OilPrice headline: "as Red Sea route recovers"). The halt length is UNVERIFIED.
  - **Not a production-plant hit on this evidence.** Misbar's Sentinel-3 smoke label "Khurais oil processing facility" does not establish cause (UNVERIFIED). No Saudi confirmation of a processing hit ⇒ **GATE 1 / FAL-01 stays firm-negative** (FALCON grades). Compare FALCON's fresh FIRMS heat at 25.252N 48.103E (10/3 22:01Z, `SIG-W-20261004-014`); whether that is the same object as this pump station is FALCON's call.
  - **Petroline BG-02:** the throughput resolver was graded NOT MET / LAPSED 2026-09-25 with no extension (WQ-264 ③; DOCKET L329). This is new evidence for BRENT, not a live trigger. PROME withdrew its helper's "could fire" read.
- **Houthi strikes on Saudi soil:** Saudi civil aviation **confirms hits at Jizan and Najran airports**. A Riyadh airport claim. **Rabigh refinery: Houthi claim, UNVERIFIED.** **Jeddah refinery: Tasnim via Newsquawk 10/5, UNVERIFIED** (lane). OilPrice 10/5: "possible fire at Saudi refinery as attack claims circulate." **A missile was INTERCEPTED north of Riyadh 10/7.** US and UK embassies warn of attacks on energy infrastructure.

## 2. Hormuz (ADD#26: each event keyed separately, none merged)
- ~9 UKMTO reports so far in October; **the latest number found is 156-26**; higher numbers were not found (a floor).
- **MT On Peace** (Panama flag): 12 injured, 10/6. **Aframax Lipsi** plus LPG and crude tankers hit 10/4. **The IRGC turned a tanker back off Khasab 10/5** (gCaptain/Reuters, MULTI).
- **None sunk, no mine ⇒ GATE 2 untouched; losses stay 3** (FALCON grades).
- Euronews 10/5 (lane): Iran insists it controls Hormuz; the rial is at a record low; its exports are drying up.
- **Supply (the other side of the split):** Kpler puts Gulf exports at 18.3 mb/d (7-day average) by 9/30, the pre-war level. Shell's CEO: flows "80-plus percent" of pre-war. Brent traded below $100 intraday 10/6 (low $97.8) and ~$101–102 on 10/7 (vendors disperse by ~$3; fetch.py BZ=F $101.46 [10/7, session unverified]).

## 3. Bab el-Mandeb
- The Yemeni government's **"Operation Yemen Dawn"** claims Mocha, Dhubab, Bab and Hadeid. **The Houthis deny it**; fighting at Dhubab 10/6 (Euronews / Al Jazeera; claims MULTI, **control UNVERIFIED**). Follows `SIG-W-20261002-008` (Taiz push).
- No new ship attack was found at the strait after the 10/4 near-miss. **CONTROL ≠ CLOSURE.** GATE-FALCON-001 is on its nearest path yet and has not fired (FALCON grades).

## 4. Diplomacy (tape: mediated ≠ bilateral; no instrument; "ceasefire" is kill-on-sight)
- Qatar confirms US–Iran mediation is ongoing (10/6, SINGLE). Trump: the war will "end very soon" (10/6; POTUS channel = tape). Vance: a deal needs a "meaningful" enrichment cut. Pezeshkian: the talks are "meaningless" (10/5). Araghchi: Hormuz stays shut until Iran's 7 conditions are met (10/4). **No deal text exists.** FALCON owns ladder item 5.

## Lane items folded here (dispositioned in BM-20261007-02)
Kpler "Libya vs Yanbu" (10/4) · IndexBox "Yanbu resumes loadings as East-West partially restarts" (dated 10/3; the state is the 9/28 resumption already in the anchor, not a new event) · safety4sea "Yanbu terminal hit" (10/2; DUP of `-20261002-014/-016`).
