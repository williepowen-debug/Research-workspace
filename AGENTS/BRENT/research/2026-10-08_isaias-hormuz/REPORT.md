# BRENT — Thursday 2026-10-08 oil read: Hormuz hull war + Hurricane Isaias

**Written 2026-10-08 08:43 ET** (`date` run with the figure computation). Session: Claude Code, Opus 5.5 (`claude-opus-5-5`), PROME `prome-fc` spawn under WQ-391 item 1 (Will 08:30 ET). Laptop `WilliePOwen`; sole BRENT writer. **$0 capital; no trade proposal, threshold move, prediction grade or gate re-open.** Evidence files in this directory: `snapshot.json` (named-contract vendor pull 12:34:38Z), `pull.py` (same script as the 10/7 report), `warning_zone_refineries.tsv` + `eia_refcap26.xlsx` (EIA Refinery Capacity 2026, operable as of 2026-01-01).

⚠️ **Every futures figure below is a single-vendor (Yahoo) quote or an estimate derived from one. None is a CME/ICE settlement.** Pre-market equity/ETF figures are vendor pre-market prints, not closes.

## 1. Tape — named contracts, vendor quote timestamp 12:24Z (08:24 ET)

| Contract | Quote 10/8 08:24 ET [CONF vendor quote] | Vendor prior-session value | Δ | My 10/7 16:15–17 ET capture |
|---|---|---|---|---|
| Brent Dec `BZZ26` | **$105.22** (bid 105.21 / ask 105.22) | $100.20 | **+$5.02 (+5.0%)** | $101.04 |
| Brent Jan `BZF27` | $101.84 (12:23Z) | $97.45 | +$4.39 | — |
| WTI Nov `CLX26` | **$92.64** | $88.28 | **+$4.36 (+4.9%)** | $89.10 |
| WTI Dec `CLZ26` | $91.59 | $87.55 | +$4.04 | $88.22 |
| ULSD Nov `HOX26` | $4.8168/gal | $4.6227 | +4.2% | — |
| ULSD Dec `HOZ26` | $4.6547/gal | $4.4766 | +4.0% | — |
| RBOB Nov `RBX26` | $3.3579/gal | $3.2342 | +3.8% | — |

Corroboration (relays, same order of magnitude, not independent settlements): fetch.py `BZ=F` $105.27 (12:24Z; continuous ticker, contract UNKNOWN by its own label) · AEOLUS 08:24 ET $105.02 · WALTER ~$104.70 at ~12:00Z · OilPrice 05:46 CDT $105.02 · CNN "shortly after 7 a.m. ET" $105.46.

**Structure [EST, derived from the quotes above]:** Dec WTI−Brent **−$13.63** (vendor prior basis −$12.65; widened ~$0.98) · Brent Dec−Jan **+$3.38** (prior basis +$2.75; widened $0.63) · WTI Nov−Dec **+$1.05**. Brent Dec−Feb **NOT MEASURABLE** (BZG27 quote >30 min old at pull). No F-a grade.

**Equities/ETF pre-market [vendor pre-market, 08:34–08:41 ET; not closes]:** USO **$149.10** (10/7 close $143.91, −0.69%) · VLO $430.49 (10/7 close $424.10) · XLE $64.53 (10/7 close $63.36).

## 2. Driver — both, and the tape leans Hormuz for the level

**Facts (dated, sourced):**
- **Hormuz hull war escalated in rate and geography.** UKMTO 158-26, 10/07 ~1900Z, ~51 nm north of Madinat ash Shamal, Qatar, multiple projectiles, crew casualties (WALTER sweep relay; Al Jazeera 10/8; UKMTO primary 403). Kpler: 10 tankers struck 9/28–10/04 (prior weekly high 6); 7 commodity vessels transited Tue 10/06, lowest since 7/23 (CNN/ABC17 10/8 relay of Kpler). No sinking; FALCON's losses stay 3; GATE 1 holds firm-negative (SIG-W-20261008-014).
- **US posture:** Axios 10/07 (anonymous): CENTCOM told to conclude preparations; no date, no decision (SIG-W-20261008-014).
- **Isaias:** MMA (BSEE) 10/07 11:00 CDT — **511,619 b/d oil = 25.08%; 350.25 MMcf/d gas = 16.37%**; 8 of 371 manned platforms evacuated (read at primary today). NHC Intermediate Advisory 7A, 07:00 CDT 10/8: 80 mph, 23.7N 90.6W, ENE 9 mph; Hurricane Warning Ocean Springs MS – Bay/Gulf County line FL (read at primary today).
- **IEA 10/07:** accelerate the ~100 mb still undelivered from the March 400 mb pledge; **no new volume** (CNN 10/8 relay; IEA 403). Wires: European gasoil closed +6% Wednesday on it.
- **Wire attribution of today's move:** CNN 10/8: "Oil prices climbed Thursday on continued worries about global supply" after record tanker attacks, with "concerns about further supply losses as Hurricane Isais [sic] heads towards America's refining hub." OilPrice 10/8 05:46 CDT ties it to the Iran attacks. Neither splits the move.

**Assessment [INFERRED — a one-session inference from structure, not a measured decomposition]:**
1. **Brent outran WTI.** Dec WTI−Brent widened ~$0.98 and Brent Dec−Jan widened $0.63 on the vendor prior basis. A US-offshore crude loss alone tightens US-delivered crude and would tend to NARROW WTI−Brent; the observed widening and the prompt Brent spread point at the seaborne Gulf/Hormuz channel for the level.
2. **The storm's crude loss is small against the move.** Earth Science Associates' GOMsmart mean expected loss **9.55 M bbl oil** (down from 11.17 M on Wednesday; Rigzone 10/8 07:02 ET relay). Enki Research (Watson): outages "would likely last no more than a week if the forecast track holds" (ZeroHedge relay). 511.6 kb/d × 7 days ≈ 3.6 M bbl [EST].
3. **Products did not lead.** HOX +4.2% and RBX +3.8% vs CLX +4.9% in percent terms; a refinery-hit premium would show RBOB/ULSD leading. The Nov diesel crack still rose ~$3.8 in dollars because the product base is larger (§3).
- **Persistence judgement:** **Hormuz component = persistent until a measured change** — strikes rising, transits at a floor, US preparations reported, Iran's final reply via Qatar pending. It can unwind fast on a diplomatic or escort headline (two-sided). **Isaias component = transient** — offshore restart begins after inspection once the storm clears (landfall late Fri 10/9 – early Sat 10/10; post-tropical over the Tennessee Valley by 10/10 18Z per NHC #7 via AEOLUS). The tail that would make it persistent is DAMAGE: refinery hits at Pascagoula/Mobile or damage to eastern deepwater hubs (Mars/Olympus/Ursa/Appomattox), on the stronger east side of the track (AEOLUS PWS #7: 29N 87W 64-kt odds 35%).

## 3. Crack estimate and VLO leg-A distance (GATE-TERRY-VLO-HELD-01; November governs through 10/14)

| Basis | Nov `HOX26×42−CLX26` | Dec `HOZ26×42−CLZ26` | Status under WQ-386 source order |
|---|---|---|---|
| **10/8 08:24 ET intraday matched quotes [EST single vendor]** | **$109.67** | $103.91 | **Diagnostic only — not a leg-A observation** (order is CME settle → accepted vendor daily row → 14:28–30 ET one-minute VWAP proxy) |
| Vendor prior-session values [EST single vendor] | $105.87 | $100.47 | agrees within $0.06 of the 10/7 proxy |
| 10/7 14:28–30 ET one-minute VWAP proxy [EST single vendor, prior report] | $105.82 | $100.42 | last proxy produced |

**Leg-A distance (November governs):** intraday $109.67 is **$19.51 above the $90.16 SELL-recommendation line** and **$14.67 above the $95 notice line**. On the last settlement-window proxy (10/7, $105.82) the distance is **$15.66**. December (diagnostic until 10/15): $103.91 intraday, $13.75 above $90.16. **TERRY grades; this desk does not.** Today's 14:28–30 ET proxy was **not produced** — this session closes before that window (no wait for a print).

## 4. Gulf shut-in path, restart risk and refining in the warning zone

**Path:** shut-ins are precautionary (8 of 371 platforms evacuated). MMA: after the storm passes, facilities are inspected, "production from undamaged facilities will be brought back online immediately"; damaged facilities "may take longer". **10/8 MMA update: NOT FOUND** (release index access-denied to AEOLUS 08:23 ET; no 10/8 figure in sources read). The 10/7 figure is a floor for a storm still strengthening (NHC 7A: 80 mph; NHC #7 forecast peak 95 kt 10/9 06Z) and will likely rise before landfall. Restart window: from ~10/10–10/11 for undamaged facilities [INFERRED from NHC timing + MMA procedure + Enki ≤1-week view].

**WTI/products:** offshore Gulf barrels are mostly medium-sour (Mars class). A short outage tightens US Gulf sour crude for days, absorbed by commercial stocks at 424.134M bbl (EIA WPSR week 10/2). The products risk is refining, not offshore.

**Refining in the warning zone** (EIA Refinery Capacity 2026, operable atmospheric crude capacity, barrels per calendar day; NHC 7A zones):

| Refinery | Capacity | NHC 7A zone | 10/8 status |
|---|---|---|---|
| Chevron Pascagoula MS | 356,440 | **Hurricane Warning** | **No shutdown reported** in the sources read (ZeroHedge/Rigzone/CNN 10/8; the wire summary calls it at risk only on a westward shift). **GAP, not a clear.** |
| Vertex Saraland AL (Mobile Bay) | 88,000 | Hurricane Warning coast; surge 5–7 ft Mobile Bay | Not read. **GAP.** |
| PBF Chalmette LA | 190,000 | TS Warning coastal segment (parish coast); plant inland on the river | Not read. **GAP.** |
| Valero Meraux LA | 125,000 | Same as Chalmette | Not read. **GAP.** (Valero-owned; relevance to the held VLO share is TERRY's card, not graded here) |

Hurricane-warning capacity **444,440 b/cd = 2.4%** of US operable (18.16 mb/cd row sum); with the TS-warning edge **759,440 = 4.2%** [EST arithmetic on EIA rows; the TS-zone placement of Chalmette/Meraux is INFERRED from parish geography]. Major Mississippi River refineries (Garyville, Norco, Baton Rouge) and Lake Charles sit west of the warning segments in Advisory 7A.

## 5. Diesel balance — netting releases against losses (SIG-W-20261008-015 ask)

| Item | Volume | New barrels? | Source |
|---|---|---|---|
| IEA acceleration | ~100 mb remaining of the March 400 mb | **No** — timing only | IEA 10/7 via CNN/Reuters relays |
| G7 diesel (10/2) | "up to 100 mb" headline | **Mostly no** — France/Germany: largely already-committed March reserves; Germany none new; France maybe ~2 mb | Politico 10/7 via relay |
| Cardón (Venezuela) | 310 kb/d nameplate, full shutdown after diesel-hydrotreater fire | New loss; **pre-fire run rate not reported** | Reuters 10/6 (8 sources) via relay |
| Volgograd (Russia) | ~280 kb/d nameplate, halted since 10/2 | New loss; run rate before strike not reported | Reuters 10/6 via relay |
| Isaias refining | 0 reported (gap) | Risk, not a loss | §4 |

**Net [INFERRED, direction only]:** release headlines add ~0–2 mb of NEW barrels, while ~590 kb/d of nameplate refining is newly down. ⛔ Nameplate is not lost runs; no diesel-volume net is computed. **Direction: tighter than headlines; magnitude NOT MEASURABLE today.** The tape agrees on direction: Nov diesel crack +$3.8 intraday vs the prior-session basis. **Forties >$140** (Kemp 10/6) vs Dec Brent futures ~$105 is physical spot against a deferred future; Kemp's own war high was $147 on 4/09. Not verified at an assessment publisher. **Not carried as a figure.**

## 6. Freight → WTI → USO (SIG-W-20261008-004 ask)

TD3C ~$1.33M/day on a chart point with no printed observation date, against $1,221,893/day WS1145 verified 10/2. **No change to the 10/7 read: no measured freight-to-WTI beta.** One mechanism cuts against USO: dearer long-haul freight widens the discount US crude needs to clear export, i.e. WTI underperforms Brent. Today's WTI−Brent widening (~$0.98) is consistent with that but does not prove it. ZeroHedge's "$40/bbl" stays unverified.

## 7. Petroline restart-date conflict — RECORD ONLY

| Claim | Date implied | Source class |
|---|---|---|
| Strike on the East-West line | **2026-09-10 ~17:56 UTC** | BRENT 9/11 adjudication |
| "Restarted, pumping at a low rate"; 4 mb/d = target | **9/22** | Reuters, 3 unnamed sources (SIG-W-20260924-002) |
| Minister Abdulaziz bin Salman, Manama 10/06: "within five or six days, we began using the pipeline again after the major attack" | **~9/15–9/16** from 9/10; WALTER computes ~9/16–17 from 9/11 | Named minister via Reuters/Al Jazeera relays (WALTER sweep §107) |
| Same speech: "back up to 5.8 million barrels" | 10/06 | **No daily unit** in the quote; 7 mb/d is nameplate, never flow or loss |

**Disposition:** conflict recorded. "Began using" and "restarted at a low rate" may describe different stages; no operator time series exists to settle it. **Graded nothing. BG-02 instance (4) stays LAPSED / NOT MET (9/25). Nothing re-opened.** FAL-05 shut-duration is FALCON's. The successor resolver still registers only after the WQ-264 shadow run (10/24).

## 8. Event-class arm — one line

**Not a new event-class arm:** no confirmed destroyed capacity (no sinking, no FAL-01 hit, precautionary storm shut-ins, an anonymous CENTCOM report). BG-02's head clause reads zero. The 8/7 rule binds; the deploy question stays CLOSED; WQ-192 STAND DOWN holds.

## 9. Armed / dated

- **COT-35B #9** (as-of 10/6): prints Fri 10/9 ~15:30 ET. **ARMED, not graded today**; raw `f_disagg.txt` primary + `cot_grade.py --expect 2026-10-06`.
- **USO Oct-09 $150C:** TERRY's Fri 15:00 ET stop stands (WQ-366 DECLINE). Pre-market USO $149.10 is $0.90 below the strike. Scaling 10/7's $143.91 by CLX26's +4.9% gives ~$151.0 [EST; current USO weights UNKNOWN]. TERRY re-marks; no desk view on the option.
- **Isaias:** landfall grade belongs to AEOLUS (10/9–10); BRENT's restart/refinery read follows at the next session with MMA's post-storm releases.
- **China product-export guidance** (CATALYSTS ~10/8, modeled): October halt per anonymous sources; **post-holiday guidance NOT FOUND** — UNKNOWN, row stays open.

## Sources read this session
NHC Intermediate Advisory 7A (nhc.noaa.gov, read 08:3x ET) · MMA/BSEE release "MMA monitors Gulf response, Isaias" (bsee.gov) · EIA Refinery Capacity 2026 `refcap26.xlsx` (eia.gov) · Rigzone 10/8 07:02 ET · ZeroHedge Isaias/refineries (undated page) · OilPrice 10/8 05:46 CDT · CNN 10/8 via ABC17 syndication · Yahoo Finance 10/7 08:26 ET (Wednesday context) · China export halt: The Standard / Yahoo relays (pre-holiday) · WALTER `research/2026-10-08_iran-full-sweep.md` · AEOLUS packet 2026-10-08 08:34 ET (`b154f4231`).

---

## §10 — Isaias transmission channels and weekend scenarios

**Added 2026-10-08 11:06 EDT, second BRENT session (WQ-391 follow-on; Claude Code Opus 4.8, laptop `WilliePOwen`, sole writer).** $0; no trade, threshold, grade or gate change. Web search returns only the 2020 Atlantic storm of the same name — NOT this event — and was deliberately NOT used as evidence. Built entirely on the §1–9 primaries above (NHC #7/7A, MMA 10/7, AEOLUS theater packet, EIA refcap26/WPSR). **This is the explicit grading basis for the CATALYSTS 10/10 Isaias row.**

**Live-tape confirm [CONF vendor, 09:09 ET]:** `fetch.py` BZ=F $104.39 (+4.18%), CL=F `CLX26` $92.11 (+4.34%) — the overnight jump holds, ~$0.8 off the 08:24 highs; no material change to §1. Boot threshold monitor flagged `DCOILBRENTEU` 125.44 (FRED, 10/6) as a structural breach — **a feed artifact, not a real level**: it contradicts our own 10/6 front-month (~$101) by ~$21. Advisory only; flagged for data review, not acted on.

### The crack asymmetry (why this is not a simple bullish-crude story)
Isaias acts on two physically separate things that push the **crack** in opposite directions:
- **Offshore (crude):** platforms shut in → less crude produced → crude-bullish.
- **Onshore (refining):** refineries shut/damaged → less crude *consumed* AND less product *made* → crude-bearish locally, product-bullish ⇒ **the crack WIDENS**.

So the governing question is *offshore story vs refining story*, because those have near-opposite signatures for the refiner leg (VLO) and the diesel crack we actually track.

### Channel A — offshore crude (real, small, transient)
25.08% Gulf oil shut in = 511,619 b/d [CONF MMA 10/7 11:00 CDT]; Gulf ~2.04 MMb/d ≈ 14% of US crude. Magnitude trivial vs stocks: 511 kb/d × ~7 d ≈ 3.6 MMbbl [EST]; GOMsmart mean expected loss 9.55 MMbbl [CONF ESA via Rigzone 10/8] — ~0.85%–2.3% of commercial crude (424.1 MMbbl, WPSR wk 10/2). **The tape confirms this is not the driver:** a US-offshore loss should NARROW WTI−Brent, but it WIDENED ~$0.98 [EST] ⇒ Hormuz, not the storm, owns the level. Grade = Mars-class medium-sour; a few-day tightening only.

### Channel B — onshore refining (the channel that touches the book); status = GAP
Warning-zone atmospheric crude capacity [CONF EIA refcap26; zones NHC 7A]: Chevron Pascagoula 356,440 (inside Hurricane Warning) · Vertex Saraland 88,000 (Hurricane Warning + 5–7 ft Mobile Bay surge) · PBF Chalmette 190,000 and **Valero Meraux 125,000** (TS-warning edge, inland on river). Hurricane-warning sum **444,440 b/cd ≈ 2.4%** of US operable; with the TS edge **759,440 ≈ 4.2%** [EST]. **No shutdown reported = GAP, not a clear.** The market is NOT yet pricing a refinery hit — products LAG crude today (ULSD +4.2%, RBOB +3.8% vs WTI +4.9%); today's crack firmness is the *other* diesel story (Cardón, Volgograd, Russia ban), not Isaias.

### Storm geometry — where the damage tail lives
[CONF NHC #7/7A via AEOLUS, ~09Z] 70 kt now; **forecast peak 95 kt 10/9 06Z** (Cat 2, one notch below Cat 3), then 90 kt to the coast, inland ~10/10 06Z near the AL/NW-FL line. Opposing caveats: RI possible (+35 kt/24h) vs 40–50 kt shear pre-landfall (could knock to TS). **Core tracks EAST of 89°W:** eastern deepwater hubs (Mars/Olympus/Ursa/Appomattox, ~29N 87W) carry **35% odds of 64-kt winds**; central-Gulf platforms (28N 89W) only **14%**. The strong side threatens the deepwater complex and the Pascagoula/Mobile coast — the high-value crude infrastructure and the biggest refinery.

### Weekend scenarios (the fork the 10/10 row grades against)
| | Trigger | Crude | Crack / refiner leg | Durability |
|---|---|---|---|---|
| **1. Base (most likely)** | Track holds, precautionary shut + clean restart, no major damage | Premium fades ~1 wk | Little Isaias effect | Transient |
| **2. Damage tail** | RI to Cat 3 + eastern track hits deepwater hubs and/or Pascagoula/Saraland | Durable sour loss (deepwater restarts slow) | **Cracks WIDEN → refiner-leg bullish** | Weeks |
| **3. Bust** | Shear wins, weakens to TS pre-landfall | Premium unwinds fully | Removes a support | — |

### What to watch, and when
1. **Fri 10/9 — refinery precautionary-shutdown headlines** (the GAP closing): Pascagoula/Saraland/Chalmette/Meraux; MMA ~11:00 CDT update (shut-in likely RISES into landfall).
2. **Fri night–Sat — landfall intensity/location** (AEOLUS grades): resolves deepwater-hub damage.
3. **Sat–Mon — restart data:** MMA restart %, BSEE, company damage statements (undamaged back immediately; damaged longer).
4. **The tell for the book: watch the CRACK, not crude.** Cracks widening faster than crude on shutdown news = Scenario 2, the refiner-leg-bullish path.

### Position implications (stand-down holds; TERRY owns construction)
- **No arm:** precautionary shut-ins and an un-landed storm are not destroyed capacity; BG-02 head clause reads zero, WQ-192 stand-down holds (consistent with §8).
- **VLO double-edged if Meraux shuts:** lost throughput is near-term equity-negative, but a refinery outage is a crack-*widener* (margin-positive); net depends on severity/duration. BRENT supplies the refinery read; TERRY grades the card.
- **WQ-386 not at risk from this:** November crack is $19.51 above the $90.16 SELL line (§3) — whether Isaias widens or compresses cracks, no near-term exit pressure.
