# OSPREY SOURCES

> **Reference index — NOT boot-read.** Consulted ad hoc when running a theater scan; not part of the BOOT sequence (STATUS/SCRATCH/LESSONS/predictions). Sources below are evergreen monitoring endpoints — refreshed, not rebuilt.
> **Spun out of HAWK 2026-07-12.** Generic sections (Military/Diplomatic/Think-tank/News-wire/Defense-journalism/OSINT) copied verbatim from HAWK's `SOURCES.md` (last refreshed there 2026-06-26) — theater-agnostic. Regional Focus below is Russia/Ukraine-only (HAWK's Iran/ME + China/Taiwan + Venezuela/LatAm regional subsections went to FALCON / stayed HAWK-dormant respectively). Frozen HAWK original: `AGENTS/HAWK/SOURCES.md`.
> **Oil handoff (inherited, Mar 6 2026):** oil prices / storage / tanker *markets* are **BRENT's** lane. OSPREY owns military ops, crude-vs-products channel tracking, and geopolitical catalysts for the Russia/Ukraine theater — see the Energy/Commodity section for the split.

Monitored sources for the Russia/Ukraine energy-war theater.

---

## Military Tracking

| Source | URL | Type | Signal Quality |
|--------|-----|------|----------------|
| ADSB Exchange | https://globe.adsbexchange.com | Flight tracking | High |
| FlightRadar24 | https://www.flightradar24.com | Flight tracking | High |
| MarineTraffic | https://www.marinetraffic.com | Naval tracking | High |
| Aircraft Spots (X) | @AircraftSpots | Military air movements | High |
| US Naval Institute | https://news.usni.org | Fleet positions | High |
| Janes | https://www.janes.com | Defense intelligence | Very High |

---

## Diplomatic / Government

| Source | URL | Type | Signal Quality |
|--------|-----|------|----------------|
| State Dept Briefings | https://www.state.gov/press-releases | Official US position | High |
| Pentagon Briefings | https://www.defense.gov/News | Military posture | High |
| White House Statements | https://www.whitehouse.gov/briefing-room | Policy signals | High |
| UN Security Council | https://www.un.org/securitycouncil | International response | Medium |

---

## Think Tanks & Analysis

| Source | URL | Focus | Signal Quality |
|--------|-----|-------|-----------------|
| ISW | https://www.understandingwar.org | Russia-Ukraine (primary theater fit) | Very High |
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
- @RALee85 — Russia/Ukraine (theater-primary)
- @AuroraIntel — Global military activity
- @sentdefender — Conflict monitoring

---

## Energy/Commodity Impact — **BRENT-owned (defer)**

> Oil pricing, storage, tanker-market rates → **BRENT** owns these; reference BRENT's values, don't re-derive. OSPREY's use of the flow trackers below is narrow: **crude-export-terminal / tanker-campaign monitoring** (Baltic/Black-Sea port throughput, shadow-fleet AIS, loadings status) — not oil-price formation.

| Source | URL | Focus | OSPREY use |
|--------|-----|-------|----------|
| TankerTrackers | https://tankertrackers.com | Oil shipping / AIS | Baltic/Black-Sea crude-terminal + shadow-fleet transit tracking |
| Kpler | https://www.kpler.com | Commodity flows | Russian seaborne-crude liftings / loadings |
| MarineTraffic | https://www.marinetraffic.com | Vessel AIS | Naval + transit tracking (also Military) |
| S&P Global Platts | https://www.spglobal.com/platts | Energy pricing | → BRENT (reference only) |

---

## Regional Focus

### Russia/Ukraine
- ISW daily updates
- Kyiv Independent: https://kyivindependent.com
- Meduza: https://meduza.io/en
- Moscow Times: https://www.themoscowtimes.com
- Euromaidan Press: https://euromaidanpress.com

*(Iran/Middle East, China/Taiwan, and Venezuela/LatAm regional subsections are not OSPREY's scope — see FALCON's SOURCES.md and HAWK's dormant-book SOURCES.md respectively.)*

---

## Scan Frequency

| Status | Frequency |
|--------|-----------|
| 🟢 GREEN | Weekly |
| 🟡 YELLOW | 2x/week |
| 🟠 ORANGE | Daily |
| 🔴 RED | Continuous / multiple daily |

**Current posture (2026-07-12, at spinout):**
- **Russia/Ukraine — 🔴 RED** (active industrial-scale campaign on both refineries and crude-export terminals/tankers as of 7/12; see STATUS.md).
> Canonical tier truth lives in `STATUS.md`, not here — this footer is a quick-reference snapshot, refresh at closeout if posture shifts a tier.

---

## Maritime security, war-risk & tanker tracking — OSPREY-owned tripwires (added 2026-09-08)

> These are OSPREY's **Channel-3 and war-risk instruments**, not price sources. The standing rule from LESSONS 8: **run the dated-window bulletin FIRST**, then name queries. The war-risk source set lives in `workbook/WARRISK.tsv`'s header (10 outlets as of 9/8) — a starting set, never the scope.

| Source | URL | OSPREY use | Notes |
|--------|-----|-----------|-------|
| Palaemon Maritime weekly report | https://www.palaemonmaritime.com/blog | **Channel-3 sweep instrument** — Black Sea / Azov / Baltic / Med incidents by date | Publishes Mondays for the prior week; direct-fetchable |
| Windward blog | https://windward.ai/blog | AIS-derived vessel lists with IMO, flag, laden state | Found the 8/1 Yanina/Bourda gap |
| Baltic Exchange TD6 (via The Edge Malaysia / The DCN) | weekly relays | **AWRP tripwire** (CPC→Augusta freight) | Baltic's own site is challenge-blocked; use relays |
| Noah Intelligence / Gibson tanker report | https://noah-news.com | War-risk premium prints + market-structure statements | Carried the 8/21 print two canvasses missed |
| The Insurer · Lloyd's List · Insurance Day · Insurance Business · Insurance Journal | trade press | AWRP prints | Lloyd's List paywalled; headline only |
| Athens News (en.rua.gr) · Splash247 · TradeWinds · Maritime Executive | trade press | Greek-operated / Western tonnage in the Russian trade | Athens News carries AIS voyage histories |
| Militarnyi · Ukrinform · Ukrainska Pravda · RBC-Ukraine · NV · Kyiv Post | Ukrainian outlets | Strike reporting with FIRMS/ASTRA geolocation | Belligerent-side; C-tier unless corroborated |
| ASTRA (Telegram OSINT) | via relays | Geolocation of refinery fires | Independent Russian outlet; used for Saratov 9/8 |
| War & Sanctions portal (HUR) | https://war-sanctions.gur.gov.ua | Vessel/owner listings in the Russian trade | A database, NOT the NSDC sanctions list |
| censor.net · UNN · United24 | Ukrainian relays | Discovery only | ⚠️ censor.net recirculates hard — date-verify by article ID (trap #14) |

## Russian primary and legal-database sources (added 2026-09-08)

| Source | URL | Use | Notes |
|--------|-----|-----|-------|
| government.ru | http://government.ru/docs/ , /news/ | Decree announcements (e.g. No. 1097, /news/59723) | Fetch has failed from this desk and from BRENT — try before citing |
| publication.pravo.gov.ru | https://publication.pravo.gov.ru | Official publication of decrees | Not yet retrieved for No. 954 or 1097 (OWED-17) |
| GARANT · ConsultantPlus | garant.ru · consultant.ru | Decree TEXT transcriptions | TRANSCRIBED tier, not primary |
| Alta-Soft customs news · Kommersant · Interfax | alta.ru · kommersant.ru · interfax.com | Decree coverage with product codes and dates | Kommersant 8/29 carried the 9/1-exemption cancellation |
| EA Analytics (via Bloomberg / Moscow Times / Meduza) · Kpler blog | relays | Monthly refinery-runs anchors for the offline band | July 3.6, August 3.8 M bpd |

**Posture footer refreshed 2026-09-08:** Russia/Ukraine — 🔴 RED unchanged; canonical tier truth remains `STATUS.md`.
