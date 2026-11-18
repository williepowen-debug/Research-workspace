# November 18: Kuwait and Bahrain attacks, the ADNOC hull, EIA week 11/13, Crimea and Krasnodar

**Session:** BRENT live session for PROME prome-6e, launched on Will's word (12:51 ET). Started 12:52 EST; times are from `date`.
**Scope:** one bounded session. No line, gate, band, prediction letter or probability changes in this note.

## 1. Summary

- **The Gulf attacks moved nothing on my board.**
  - Iran fired drones at Kuwait (Ali Al Salem air base) and at Bahrain early 11/18. Both states confirm the attacks. Damage is NOT ESTABLISHED. The claimant is unsettled: the army per IRIB, the IRGC per Tasnim. These are FALCON's grades (cards 001 and 006).
  - An ADNOC ship was struck in Hormuz on the evening of 11/17: 1 missing, 11 injured, crew evacuated. FALCON grades it PROBABLY distinct from TARA GAS. It is unnamed (Seatrade's NAVIG8 MESSI is unverified). FALCON's confirmed-loss census stays at 7.
  - Brent January (BZF27) fell about 2.2% on the day. The curve shape did not change: M1−M3 was about +5.00 at 12:43 ET, against +5.09 at the 11/17 window.
  - The market is not pricing a supply loss from these attacks. It added at most about $0.30 at the evening reopen, and that had faded by 03:00 ET.
- **EIA week 11/13: BRT-31 week six QUALIFIES (−1.7848%), streak 1.**
  - The precondition can no longer fire.
  - MET now depends on one print. The week to 11/20 (released about 11/25) must come in at or under **8,263.66 kb/d**. The last three weeks were 8,767 to 8,808.
  - BRT-34's second print was 104,901, not below 95,000.
- **Crimea bridge and the Krasnodar refineries move nothing.**
  - OSPREY: Kerch shipping has been shut since 7/10, so the bridge adds no new flow loss. The refinery strikes are capacity, not barrels, and no halt is reported.
  - The diesel crack fell on the day. This item is logged on combo:diesel-buffer.

## 2. The tape against the news [vendor one-minute bars, EST, not settles; CME is IP-blocked from this box]

| Time (ET) | Event | BZF27 | Note |
|---|---|---|---|
| 11/17 16:59 | 11/17 close of day session | 93.07 | vendor daily row 93.14 |
| 11/17 18:00 | evening reopen. Reuters title "Iran fires at Kuwait after US strike" 23:15Z = 18:15 ET | 93.39 (hour high 93.47) | **+0.32: the only visible bid** |
| 11/18 01:00–03:00 | Asia and early London; Kuwait and Bahrain interceptions reported | low 91.15 (03:00 hour) | the bid faded and price fell through it |
| 11/18 07:00–08:00 | London morning | high 93.37 | a rebound, on no news I can attach to it |
| 11/18 09:00–10:00 | | 91.63–92.97 | |
| 11/18 10:30 | EIA WPSR release: crude +3.380M, gasoline +5.193M, distillate +1.571M | 11:00 hour 92.02 → 90.80 | the steepest hour of the day |
| 11/18 12:43 | capture | **91.13** (day low 90.43) | −2.01 against the vendor daily 93.14 (−2.2%) |

| 12:43 ET read | Value | 11/17 window [14:28,14:30) |
|---|---|---|
| BZF27 / BZG27 / BZH27 | 91.13 / 88.33 / 86.13 | 93.1479 / 90.3817 / 88.0559 |
| M1−M2 | +2.80 | +2.7662 |
| **M1−M3 (BRT-33 pair)** | **+5.00** | +5.0920 |
| CLF27 (WTI January) | 81.69 (−3.5% against 84.65) | 84.66 |
| Brent minus WTI, January against January | +9.44 | +8.49 |
| HOF27 × 42 − BZF27 (diesel crack) | +71.50 | +73.45 |
| RBF27 × 42 − BZF27 | +10.99 | +11.97 |
| January 3:2:1 | +31.16 | +32.46 |
| HOZ26 × 42 − CLZ26 (December crack) | +83.35 | |

**Reading (assessment):**

1. **Spreads held.** Flat price fell about $2 and both front spreads held. A supply loss is priced front-first, with M1 bid over M3. Today did the opposite: the whole curve moved down together.
   - My invalidation item 4 (M1−M3 above about +6.3 while flat prices rise) is NOT met.
   - This is the third Gulf escalation in a week that the curve has shrugged off: 11/16 hulls, 11/17 Bahrain and Qeshm, 11/18 Kuwait, Bahrain and ADNOC.
2. **WTI fell more than Brent, and Brent's premium widened about $0.95.** That fits a US crude build alongside a jump in US crude exports (+1.033 mb/d to 4.488), which means US barrels are being pulled abroad. I have not established why.
   - ⚠️ CLZ26 is in its last days, so WTI December is a thin contract.
3. **Products fell with crude.** The diesel crack fell about $2 and gasoline about $1. Neither the Russian refinery strikes nor the Gulf news is being priced into products.
4. **Equities were firm and VIX fell 5.4%** [fetch.py, vendor]. This was not a risk-off day. I do not know the cause of the selloff beyond the timing of the EIA release.
   - Summit headlines (Trump, Putin and Xi in Shenzhen) and ORACLE's lower pause odds (42.0, −14.5) point in opposite directions. Neither is established as a cause.

⚠️ **The vendor continuous contract rolled to February today.** `BZ=F` now quotes BZG27 (88.33). That is why `fetch.py` prints Brent −5.16% and boot prints 88.44, −2.14%: each mixes contracts. The January move is −2.2%. Quote named contracts only.

**Physical market:**
- FRED's newest Dated Brent is still 11/11 ($92.14, under BZF27 by $0.62), so I have no fresh Dated read.
- Flow floors (WALTER card 007; FALCON grades the theater):
  - PortWatch: 16 Hormuz transits 11/9–11/15, 2.6% of 88 a day, against 27 the week before. WALTER re-pulled this at the primary. My own probe at 12:57 EST still returns `Token Required` (error 499), so I cannot reproduce it.
  - Kpler: Hormuz clearance 8,553 kb/d for the 7 days to 11/16, against the 10.5 mb/d "since 10/1" relayed on 11/11. This is a helper read, not re-checked by WALTER or me. Different windows; not netted.
- If true, the Kpler figure is a flow fall the curve is not pricing. It is relayed and unverified, so it goes on combo:gulf-flow-basis and combo:paper-physical-gap, not into a test.

## 3. EIA week 11/13 (released Wed 11/18 10:30 ET) [CONF EIA primary]

Own capture: `ir.eia.gov/wpsr/psw01.xls` (via the EIA signed redirect) at 12:5x EST, plus `table9.csv`. The headline stocks come from the routine (`demand_destruction/data/eia_2026-11-18.md`) and WALTER card 008, which read the same EIA tables and agree on every figure.

| Series | Week 11/13 | Week 11/6 | Change |
|---|---|---|---|
| Commercial crude | 417.797M | 414.417M | +3.380M |
| Cushing | 26.147M | 27.356M | −1.209M (boundary 3 not met) |
| SPR | 276.361M | 279.535M | −3.174M |
| Gasoline stocks | 215.949M | 210.757M | +5.193M |
| Distillate stocks (WDISTUS1) | **104,901** | 103,330 | +1,571 (BRT-34: not below 95,000) |
| Refinery utilization | 95.7% | 95.2% | +0.5 points (TRACKER line 3 stays crossed) |
| Crude exports | 4,488 kb/d | 3,455 | +1,033 |
| Gasoline supplied, weekly (WGFUPUS2) | 8,790 | 8,767 | +23 |

### BRT-31 week six: owner grade

The letter's basis is the unrounded value computed from the weekly series as first published. Every earlier window week was graded this way.

- Current four weeks: 8,358, 8,808, 8,767, 8,790. Average 8,680.75.
- The same four weeks a year earlier (to 2025-11-14): 8,924, 8,874, 9,028, 8,528. Average 8,838.5.
- **Year on year: −1.784805113989929%, at or below −1.5%: QUALIFYING.**
- The prior week (−1.0346%) did not qualify, so the **streak is 1**. No terminal event.
- No revisions: 8,767, 8,808 and 8,358 match the 11/12 capture, and so do the year-ago base weeks.
- ⚠️ The routine's −1.7989% divides EIA's rounded four-week averages (`Data 3`: 8,680 against 8,839). That is not the letter's basis. It is on the same side of every line, and the grade figure is −1.7848%.

**Price leg.** GASREGW on 11/16 was $3.805 against $3.062 on 2025-11-17, a rise of **+24.27%** [FRED, read 12:54 EST; matches the routine's EIA page read]. That is above +20%, so the counter stays at **0 of 3**. Two window weeks remain (11/20 and 11/27), so a third week under +20% cannot happen. **NOT-FIRED-PRECONDITION is no longer reachable.**

**What can still happen:**
- **MET:** this requires week 11/20 to qualify. Its four-week window is 8,808, 8,767, 8,790 and the new week. The base is 8,874, 9,028, 8,528 and 8,726, which averages 8,789.0. So the 11/20 week qualifies only at or under **8,263.66 kb/d**. Week 11/27 cannot rescue a miss at 11/20: it would need 11/20 to qualify too.
- **NO-VERDICT:** this is the likely end state if the 11/20 week prints above that. The 11/12 print already ruled out NOT MET.
- **NO-VERDICT-CONTAMINATED:** only if a federal or large-state gasoline tax cut takes effect.

**My judgment (not a re-mark):**
- A single week at about 8,264 means a fall of about 530 kb/d from the latest week (8,790). The lowest week in the window so far was 8,358 (10/23).
- The 40% registered call stays as registered.
- **Reading:** retail prices fell 19¢ in a week while measured volume held near 8,790. That is weakening against a high year-ago base, not a fresh fall in volume.
- Label per the letter: MET would mean "weakening measured", never "destruction confirmed".

## 4. Crimea bridge and the Krasnodar refineries (OSPREY packet 26196c889d; YURI via WALTER card 009)

- **Crimea bridge.** The road span fell overnight 11/16–17 and rail runs on one track. Kerch passage has been stopped since 7/10 (Reuters, three grain-trade sources, unconfirmed officially). PortWatch shows 0 ships a day to 11/8. No oil volume via Azov was found.
  - **For oil:** this extends an existing closure. It is not a new barrel loss. Nothing on my board reads Azov flows.
- **Refinery strikes.** Ilsky 11/16 (a General Staff claim), Salavat 11/17 ("no critical damage"), Ilsky and Afipsky 11/18 (fires). OSPREY counts 12 November refinery rows: capacity, not barrels, and no halts reported.
  - YURI: Russia's government admits local fuel deficits and continued product imports while its export bans run to 31.01.2027.
  - **For oil:** this leans toward a thinner diesel buffer outside the US (YURI's line). The market did not price it today: the diesel crack fell about $2, and US distillate built +1.571M.
  - Logged on combo:diesel-buffer. No INCIDENTS row: these are Russian capacity strikes, OSPREY's domain rows, with no halt and no primary operator statement.

## 5. Against the four items of the 11/17 note (§5)

| Item | 11/18 state |
|---|---|
| Laden crude loss confirmed | NOT MET: the ADNOC hull is unnamed, its cargo is not stated, nothing sank; census 7 (FALCON) |
| Gulf-ally production loss stated | NOT MET: no Gulf-ally oil facility hit or claimed (FALCON; FAL-08 not engaged) |
| US-facilitated transits fall after 11/16 | NOT MEASURED: the PortWatch fall (27 to 16) is for 11/9–11/15, before the warning |
| M1−M3 above about +6.3 while flat prices rise | NOT MET: about +5.00 while flat fell |

**BG-02** is NOT MET. TARA GAS was abandoned after a second attack. It is an LPG carrier, and the perimeter question stays with PROME and Will. Nothing sank.

## 6. Trade-read handoff (WQ-696)

**Gulf:**
- **What the evidence implies.** For now, the oil market treats Iran's widening attacks on Gulf states and hulls as noise in flat price, not as a supply loss. Three escalations in three days left the Brent curve shape unchanged. The day's fall came with a bearish US stock print.
- **Horizon:** the next one to two weeks, up to the OPEC+ January decision on 11/29.
- **Invalidated by:** any of the four items in §5. Above all: a confirmed laden crude loss, a stated Gulf-ally production or export outage, or M1−M3 bid above about +6.3 while flat price rises.
- **Unknown:**
  - who fired at the ADNOC ship, what it carried, and its name;
  - whether the Kpler 8.55 mb/d clearance read (relayed) is real;
  - why the 08:00 ET rebound happened;
  - the cause of the selloff beyond the EIA timing.
- **Investment implication: none new.**

**BRT-31:**
- **What the evidence implies.** US gasoline volume is weakening against last year's high base while retail prices fall.
- **Horizon:** one print, 11/25.
- **Invalidated by:** a week-11/20 print above 8,263.66 kb/d. That ends the MET path, and NO-VERDICT then follows.
- **Unknown:** the 11/20 print; any holiday-week distortion falls on 11/27, not 11/20.
- **Investment implication: none.** This is a forecast-row event, not a price signal. Gasoline cracks already fell (January RBOB crack about $11).

**Routing:** this is a short TERRY packet saying "no card". Will has asked that material findings reach TERRY unasked, and the Gulf non-reaction is material to anyone holding Gulf-risk optionality.

## 7. Coverage limits

- No official CME or ICE settle (IP block). No window observation today (Friday's row). No Dated Brent after 11/11.
- PortWatch is token-gated from this box. The Kpler figures are relayed.
- The ADNOC hull's name and cargo are unknown.
- The IEA October Saudi 9.99 mb/d is a snippet only (iea.org 403), WALTER card 007. Not read; it stays with the 11/29 spare-capacity question.
