# FALCON SOURCES

> **Reference index — NOT boot-read.** Consulted ad hoc when running a theater scan; not part of the BOOT sequence (STATUS/SCRATCH/LESSONS/predictions). Sources below are evergreen monitoring endpoints — refreshed, not rebuilt.
> **Inherited/split from `AGENTS/HAWK/SOURCES.md` at spinout 2026-07-12** (build spec §2 SOURCES.md three-way split: generic sections copied to all three of FALCON/OSPREY/HAWK; Iran/ME regional → FALCON; Russia/Ukraine regional → OSPREY; China-Taiwan + Venezuela/LatAm regional → HAWK). HAWK's original (all-theater) index frozen at `AGENTS/HAWK/SOURCES.md`.
> **Oil handoff (Mar 6 2026, inherited):** oil prices / storage / tanker *markets* are **BRENT's** lane. FALCON owns military ops, chokepoint *transit* tracking, escalation indicators, and geopolitical catalysts for the Iran/Gulf theater — see the Energy/Commodity section for the split.

Monitored sources for geopolitical and military risk, Iran/Gulf theater.

---

## Military Tracking

| Source | URL | Type | Signal Quality |
|--------|-----|------|-----------------|
| ADSB Exchange | https://globe.adsbexchange.com | Flight tracking | High |
| FlightRadar24 | https://www.flightradar24.com | Flight tracking | High |
| MarineTraffic | https://www.marinetraffic.com | Naval tracking | High |
| Aircraft Spots (X) | @AircraftSpots | Military air movements | High |
| US Naval Institute | https://news.usni.org | Fleet positions | High |
| Janes | https://www.janes.com | Defense intelligence | Very High |

---

## Diplomatic / Government

| Source | URL | Type | Signal Quality |
|--------|-----|------|-----------------|
| State Dept Briefings | https://www.state.gov/press-releases | Official US position | High |
| Pentagon Briefings | https://www.defense.gov/News | Military posture | High |
| White House Statements | https://www.whitehouse.gov/briefing-room | Policy signals | High |
| UN Security Council | https://www.un.org/securitycouncil | International response | Medium |

---

## Think Tanks & Analysis

| Source | URL | Focus | Signal Quality |
|--------|-----|-------|-----------------|
| ISW | https://www.understandingwar.org | Russia-Ukraine, Iran | Very High |
| CSIS | https://www.csis.org | Broad geopolitical | High |
| CFR | https://www.cfr.org | Foreign policy | High |
| Atlantic Council | https://www.atlanticcouncil.org | NATO, Europe | High |
| RAND | https://www.rand.org | Defense policy | High |

---

## News Wires (Breaking)

| Source | URL | Speed | Reliability |
|--------|-----|-------|-------------|
| Reuters | https://www.reuters.com/world | Fast | High |
| AP | https://apnews.com/world-news | Fast | High |
| AFP | https://www.afp.com | Fast | High |

---

## Defense Journalism

| Source | URL | Focus | Signal Quality |
|--------|-----|-------|-----------------|
| Defense One | https://www.defenseone.com | US defense policy | High |
| Breaking Defense | https://breakingdefense.com | Industry + policy | High |
| War on the Rocks | https://warontherocks.com | Strategic analysis | Very High |
| The War Zone | https://www.thedrive.com/the-war-zone | Military tech + ops | High |

---

## OSINT Community (X/Twitter)

Key accounts for real-time military tracking:
- @IntelCrab — OSINT aggregator
- @AircraftSpots — Military flight tracking
- @MT_Anderson — Naval movements
- @AuroraIntel — Global military activity
- @sentdefender — Conflict monitoring

*(@RALee85 — Russia/Ukraine-focused — moved to OSPREY's SOURCES.md.)*

---

## Energy/Commodity Impact — **BRENT-owned (defer)**

> Oil pricing, storage, tanker-market rates → **BRENT** owns these; reference BRENT's values, don't re-derive (Mar 6 2026 handoff). FALCON's use of the flow trackers below is narrow: **chokepoint military-transit monitoring** (Hormuz/Bab-al-Mandab vessel counts, AIS dark-transit, naval blockade status) — not oil-price formation.

| Source | URL | Focus | FALCON use |
|--------|-----|-------|------------|
| TankerTrackers | https://tankertrackers.com | Oil shipping / AIS | Chokepoint transit counts only |
| Kpler | https://www.kpler.com | Commodity flows | Hormuz throughput / dark-transit |
| MarineTraffic | https://www.marinetraffic.com | Vessel AIS | Naval + transit tracking (also Military) |
| S&P Global Platts | https://www.spglobal.com/platts | Energy pricing | → BRENT (reference only) |

---

## Regional Focus

### Iran/Middle East
- Al-Monitor: https://www.al-monitor.com
- Iran International: https://www.iranintl.com
- Middle East Eye: https://www.middleeasteye.net

*(China/Taiwan and Venezuela/LatAm regional sources moved to HAWK's SOURCES.md — dormant book. Russia/Ukraine regional sources moved to OSPREY's SOURCES.md.)*

---

## Scan Frequency

| Status | Frequency |
|--------|-----------|
| 🟢 GREEN | Weekly |
| 🟡 YELLOW | 2x/week |
| 🟠 ORANGE | Daily |
| 🔴 RED | Continuous / multiple daily |

**Current posture (spinout, 2026-07-12):**
- **Iran / Gulf — 🔴 RED** (war at highest kinetic intensity yet — 3rd US strike round, broadest Gulf retaliation, formal enforced Hormuz closure; continuous scans warranted). Canonical tier truth lives in `STATUS.md`, not here — this footer is a quick-reference snapshot, refresh at closeout if posture shifts a tier.

---

## ADDED 2026-07-30 — primaries that carried decision-weight and were NOT in this index

> ⚠️ **This file had not been touched since spinout (2026-07-12) while the sourcing base changed materially.** Every entry below was load-bearing in a real adjudication — several resolved or killed a registered prediction — and none of them was findable here. **An un-updated source index quietly re-routes the next session back to the sources that were already failing.**

**Refinery / plant outage status (the gap that mattered most)**
- **IIR Energy (via Reuters)** — refinery outage and restart data. **This is the source that produced the Jazan shutdown** (400 kbpd, shut 7/27, restart tent. 8/15) after Aramco itself stayed silent and did not reply to Reuters. **Registered in FAL-04 route (b) (carried into FAL-05 route (b)) as an acceptable "named-source trade primary."** ⚠️ It is a *trade primary, not the operator* — cite it as such.
- **Aramco direct** — has issued **no** statement on Jazan. **Operator silence is the norm here, which is exactly why the resolvability guard exists** (silence must never auto-confirm a negative prediction).

**LNG / gas — the molecule with no coverage before 7/30**
- **Bloomberg** (7/22, 7/28) · **CNBC** (7/1) · **AGBI** · **LNG Prime** · **Al Jazeera** (2026-03-24 declaration) — the QatarEnergy Ras Laffan force-majeure chain. ⚠️ **No FALCON source line existed for gas at all before this, which is half of why a four-month supply loss went unseen.**
- **NOT HELD, and needed:** an authoritative **JKM / TTF** series. `TTF=F` on Yahoo is a thin, unvalidated proxy — **do not make it load-bearing.** Gas pricing is SAM's / the macro agents' lane; route rather than adjudicate.

**Saudi export volumes / loadings**
- **AGBI** — pinned the **4.7 mb/d Mar-Jun baseline as *Red Sea exports* (TOTAL LIQUIDS)**, which closed the GATE-FALCON-001 leg-3 commodity-basis question and killed a false −42.6% crude-only read. **Also the source for Petroline OPERATIONAL, ~5 mb/d available.**
- **Goldman Sachs GIR via Kpler** (routed by WALTER) — Yanbu 7DMA loadings. Estimates (vessel count × avg volume), not measurements.
- **Bloomberg Intelligence** (Salih Yilmaz) — useful framing discipline: *"a serious escalation in RISK rather than a confirmed large-scale supply outage."*

**Military / theater**
- **`centcom.mil` official public releases** — ⚠️ **has 403'd on direct WebFetch before; `globalsecurity.org` mirrors CENTCOM releases** and is a reliable fallback. The 7/29 "heavy wave" target list came through this route.
- **NASA FIRMS** (MODIS/Aqua) — independent thermal-anomaly confirmation of fires, with coordinates, FRP and a DAYNIGHT flag. **Claimant-independent, and it corrected me once** (Abqaiq: interception and fire are not mutually exclusive).
- **CTP / ISW Iran Update (daily)** + **Shafaq** — the **PRIMARY** Iraq/PMF read. ⚠️ **`baghdad_watch.py`'s embassy feed is a DEAD false-quiet channel** — it printed `QUIET, 0 new` on 7/30, three days after Iraq-launched drones hit Abqaiq and one day after the US struck Iraq. **Positive-alert backstop only.**
- **UKMTO / JMIC advisory notes** — vessel incidents, mine status. ⚠️ **Stamped in UTC**; date kinetic maritime events in **LOCAL theater time (UTC+4)** and cite the clock (a one-day correction is a clock collision until proven otherwise).
- **IMF PortWatch ArcGIS FeatureServer** — the official series behind the unscrapable Hub page; drives all three transit/bypass/kharg scripts. Lags ~5-8d; each script reports its own print age.

**Insurance**
- **Marcus Baker, Marsh (global head of marine) via S&P Global Platts** — the anchor Hormuz hull-premium quote. ⚠️ **Publishes infrequently: re-pulled 7/30 and the 7/22 figure was still the newest in existence.** See `workbook/WARRISK.tsv`'s three-clock header — *old because nothing newer was published* ≠ *old because nobody looked.*


---

## ADDED 2026-09-08 — primaries that carried decision-weight in the 9/5–9/8 tanker war and the 9/7–9/8 Saudi salvo

**Vessel strikes / shadow fleet**
- **CENTCOM public releases via NBC / CBS / ABC live blogs** — `centcom.mil` still 403s from this box (documented since 9/1); the three networks relay the release text within the hour. ⚠️ **Grade the OPERATIVE phrase** ("rendered inoperable") not the headline verb ("destroyed") — see the false-fire register.
- **TankerTrackers.com** (via search-layer relays) — dark-immune hull identification and laden state (Derya empty; Kylo empty; the five 9/8 hulls' export history). **The only route that saw the 8/12 Kharg loading my AIS instrument missed.** Primary not directly reachable; relays cite it by name.
- **Kpler via WSJ / Reuters** — Iranian crude afloat outside the blockade (90M→29M), Kharg monthly loadings (251 kb/d Aug), Hormuz commodity-ship counts (~10/day). BRENT's lane; cite, never maintain. ⚠️ Three different denominators in one week (Kpler ships/day · PortWatch 88 · Reuters 130-140 norm) — never blend.
- **IRNA via Malay Mail / Middle East Eye / Al Bawaba** — IRGC Navy statements verbatim (the Kuwait/Bahrain in-port warning). Iranian state media = D-tier for INTENT, B-tier for the FACT that a statement was issued.

**Saudi strikes**
- **Saudi Ministry of Energy statements via Al Arabiya English / Arab News / Al Jazeera** — the operator-of-record voice for "fires… temporary halt in some operations"; **never names units, durations or volumes** — the absence is structural, not a gap to close by re-pulling. Reuters (streetinsider mirror) 403s and `apnews.com` is unfetchable from this box.
- **The War Zone (TWZ) + NASA FIRMS** — thermal-anomaly geolocation at facility resolution (Jazan refinery vs Jazan Bulk Plant vs King Abdullah Airport). Claimant-independent.
- **Shafaq News relaying the FT** — the only route to the FT's 9/7 Jazan report from this box (FT paywalled).
- **Houthi Yahya Saree statements (Telegram, via relays)** — target list + weapon class; claim-tier only.

**Iran internal / diplomacy**
- **CTP-ISW Iran Update (daily)** — now also the primary read on the RESTRICTED ZONE, the blockade's economic bite (gasoline price, floating-stock drawdown) and Iranian decision-maker statements (Rezaei, Qalibaf, Khatam al-Anbiya HQ). Iraq section stays the PMF primary.
- **Iran International / AP (via Asharq Al-Awsat, Africanews)** — gasoline price hike and security deployment. **NCRI / Shabtabnews = advocacy** (opposition-aligned); flag, do not make load-bearing.

**Unreachable / trap notes this week:** CNN returns HTTP 451 to this box; Kurdistan24's "three F-35s destroyed" item is 7/30-vintage and surfaces beside 9/8 Jordan claims (register row); Wikipedia's ship-attack list stops in July and explicitly flags its September gap.
