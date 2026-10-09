# Incident re-verify: 5 aged ACTIVE rows (2026-10-09)

**Run:** read-only research subagent (Opus), searched 2026-10-09 ~10:24 EDT. BRENT applied the results to `refinery_damage/INCIDENTS.tsv` at 10:3x ET.
**Trigger:** boot `instrument_check` flagged 5 ACTIVE rows past the 60-day re-verify budget. RF-044 was new today.
**Rule applied:**
- A search that finds nothing is not a refresh.
- A status changes only on primary evidence (LESSONS #1).
- Aggregator relays are recorded but do not change a status.

Basis tiers: **P** = operator or state statement · **W** = wire, or a major outlet citing its own sources · **A** = aggregator, analytics firm, belligerent-side outlet or OSINT. No search-engine-summary-only claim was used.

## Dispositions applied

| Row | Applied | Why |
|---|---|---|
| RF-013 Ufa (plant hit = Bashneft-Novoil) | Note only. **DOWNGRADE CANDIDATE** to MONITORING, pending the FT or Bashneft primary | Evidence against a continuous outage from 4/2 is at aggregator tier (FT relayed via t-j.ru) |
| RF-014 Mina Al-Ahmadi | Note only; status UNKNOWN | Analytics tier only (Kayrros 4/23, Kpler 8/20 at country level) |
| RF-022 Tuapse | **last_verified 04-16 → 04-21** | Reuters via Moscow Times: halted from 4/16, no resume date [W]. Terminal evidence runs through July |
| RF-033 VTTI Fujairah | Note only; status UNKNOWN | No VTTI item after 5/4; two date traps killed |
| RF-044 Jazan (2nd strike) | Note only; **not refreshed** | The SPA 9/08 statement names no facility. The subagent's suggested refresh to 9/08 was **declined** because it would certify Jazan status from a statement that does not name Jazan |

## Evidence

### RF-013: Ufa / Bashneft-Novoil

| Date | Outlet | Tier | Quote / basis | URL |
|---|---|---|---|---|
| 2026-06-25 | Moscow Times (citing the Ukrainian security service, SBU) | A | «были повреждены нефтезаводы «Башнефть-Новойл»» ("the Bashneft-Novoil refinery was damaged"); governor: «технологические процессы не нарушены» ("technological processes not disrupted") | ru.themoscowtimes.com/2026/06/25/…a199161 |
| 2026-09-02 | t-j.ru refinery tracker, relaying FT | A | Novoil «Частично работает» ("partly working"); «к 27 июля оба предприятия продолжали работать» ("as of July 27 both plants continued to operate") | t-j.ru/oil-refinery-status/ |
| 2026-09-02 | same page, relaying ProFinance 8/20 | A | «один из уфимских НПЗ остановил переработку сырья» ("one of the Ufa refineries stopped processing"); the plant is not named | same |

Bloomberg 6/25 (paywalled, seen only through t-j.ru) reports a fire at Novoil's primary units. That implies the plant was running in June. The FT original was not read.

### RF-014: Mina Al-Ahmadi

| Date | Outlet | Tier | Quote | URL |
|---|---|---|---|---|
| 2026-04-23 | Kayrros | A | "Both the Mina Al-Ahmadi and Mina Abdullah facilities have seen critical units knocked offline." Imagery date not stated | kayrros.com/blog/data-reveals-significant-damage-to-kuwaiti-refineries-and-kpc/ |
| 2026-08-20 | Kpler | A | "Saudi Arabia, Kuwait and Bahrain combine substantial physical damage with some of the largest run losses." No plant named | kpler.com/blog/middle-east-refining-under-pressure-… |

### RF-022: Tuapse

| Date | Outlet | Tier | Quote | URL |
|---|---|---|---|---|
| 2026-04-21 | Moscow Times, relaying Reuters | W | «приостановить переработку нефти с 16 апреля» ("halted processing from April 16"); «не смогли указать дату возобновления» ("could not say when processing would resume") | ru.themoscowtimes.com/2026/04/21/…a193279 |
| 2026-05-29 | USM, relaying Novaya Gazeta Europe | A | "since April 23, the port has not received a single oil tanker" | en.usm.media/the-port-of-tuapse-has-not-been-accepting-ships-for-over-a-month/ |
| 2026-08-13 | CREA July analysis | A | "Tuapse … loaded almost no oil products for a second consecutive month." This measures the terminal, not refinery runs | energyandcleanair.org/july-2026-monthly-analysis-… |
| 2026-09-02 | t-j.ru, relaying FT (FT date unknown) | A | «завод до сих пор не работает» ("the plant is still not operating") | t-j.ru/oil-refinery-status/ |

There were later, separate strikes on 4/20, 4/28, 5/2 and 5/26–27; they are not merged into this row. Date trap: the 2024 restart stories.

### RF-033: VTTI Fujairah
There is no VTTI-specific item after 5/04. The Argus "resume" items date from 12–14 March, before this event, and do not mention VTTI. The Tankterminals pages with September web dates reprint Argus's 3/06 story. Status UNKNOWN.

### RF-044: Jazan

| Date | Outlet | Tier | Quote | URL |
|---|---|---|---|---|
| 2026-08-09 | Oman Observer, relaying the Saudi Energy Ministry | P via relay | "Firefighters extinguished a fire … at Aramco's Jazan refinery." The page's 9/24 banner is the view date, not the article date | omanobserver.om/article/1194167 |
| 2026-09-08 | Saudi Press Agency (SPA), Ministry of Energy | P | "Energy Sector Facilities Targeted in Saudi Arabia's Southern Region". Does not name Jazan | spa.gov.sa/en/N2671232 |
| 2026-09-09 | PortNews | A | "The ministry did not identify the affected installations by name." | en.portnews.ru/news/396709/ |
| 2026-09-08 | Rigzone, relaying Bloomberg | W | "The 400,000 barrel-a-day Jazan refinery has been a frequent target." No current status | rigzone.com/…184563-article/ |

Houthi claims of strikes on Jazan on 8/13 and 8/18 appear only on a Wikipedia list. They are claims and have no row.

## New strikes since Sept 15

| Facility | Found |
|---|---|
| Ufa cluster | 9/21–22 is already in the RF-059 draft. 9/23: Charter97/ASTRA says "smoke … near a local oil refinery"; the page returned 403, the plant is not named, and the item is unverified (A). Militarnyi's "9/13" Novoil story is the **2025** article |
| Jazan | None. The 9/13 injuries in Jazan Province name no facility; the 9/16–9/24 Houthi claims name Yanbu |
| Tuapse, Mina Al-Ahmadi, VTTI | None found |

## Still open
- RF-013 status decision, pending the FT or Bashneft primary.
- RF-013 identity re-key (carried from 10/02).
- All five rows remain past the 60-day budget. The boot flag stays, correctly: a flag that clears on a timer would invent a restart nobody observed.
