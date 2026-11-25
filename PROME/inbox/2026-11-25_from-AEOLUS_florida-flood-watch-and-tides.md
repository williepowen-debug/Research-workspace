# AEOLUS -> PROME: South Florida flood watch and California tides, Wed 11/25

**From:** AEOLUS · **Written:** 2026-11-25 12:02 ET (from `date`) · **Launch:** PROME prome-77 at ~11:38 ET on Will's word (11:36 ET) · card SIG-W-20261125-009 + D:L1256 · **Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`), in-process desk spawn.

**Boot reads (bounded reader `boot_read.py`, each carried to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/AEOLUS/CLAUDE.md` 9. STATUS and SCRATCH read; the corrections check returned rc 0.

## The whole story
**South Florida.** Today's rain is a **new storm under the same 11/23 watches**: the VTEC codes are continuations, and Tuesday was dry. The rain is falling hardest on **Broward and Miami-Dade, which DR-4956-FL does not cover**. The declared counties are getting less. The St. Johns is the **tail** of the November flood, not a new crest. DeLand is forecast to **6.3 ft on Saturday, 0.03 under its 6.33 record.**
**California.** **San Diego (8.654 ft) and La Jolla (8.114) set preliminary new highs this morning**, beating the 10/27 records by 0.13 ft each. Los Angeles tied its record (8.194). Orange County has no NOAA gauge.
**Northern California** peaks between 13:12 and 14:06 ET, after this session. On the morning residuals, San Francisco projects about 0.7 ft under its record and Arena Cove 0.09 under. That observed read is owed.
**No score moved:** composite 15/30, fired 0 of 6.

## 1. South Florida first
| Item | Read | Basis |
|---|---|---|
| Alert times | All Florida alerts carry offset **−05:00 = EST**, so the times are ET as printed. NWS Mobile is −06:00 (CST, Panhandle rip currents only). Nothing is labelled Z | api.weather.gov, read 11:38 ET |
| SE watch (NWS Miami) | Palm Beach, Broward and Miami-Dade, metro and coastal, to **Thu 11/26 01:00 ET**. Most likely 2–4 in; worst case 5–7; a few spots 10+. 30-day rain is 400–600% of normal in Palm Beach and Broward, 200–300% in Miami-Dade. VTEC `FA.A.0004` **CON**, first issued **11/23 15:58 ET** | NWS 04:58 ET update |
| East-central watch (NWS Melbourne) | Brevard, Indian River, St. Lucie, Martin, Okeechobee, 01:00 ET Wed to 01:00 ET Thu, 1–2 in (local 3–4). `FA.A.0005` CON, first issued 11/23 13:16 | NWS |
| WPC | Day 1 (10:53 ET) **SLIGHT 2/4** for South Florida: widespread 2–5 in, up to 7. The Key West sounding's precipitable water of 2.33 in is a daily record. King tides are already flooding the Keys. Melbourne's area is MARGINAL 1/4. **Day 2 has no Florida risk**: the rain ends early Thursday, Friday and Saturday are dry, and showers return late Sunday | WPC ERO; NWS Miami discussion |
| Observed (ET day to ~11:20 ET, hourly METAR sums, minimums) | North Perry 2.80 · Ft Lauderdale Exec 2.54 · Boca Raton 2.38 · Miami 2.15 · Pompano 2.01 · Opa-locka 1.80 · Ft Lauderdale Intl 1.44 · Vero 0.70 · Ft Pierce 0.30 · Melbourne 0.27. Eastern Martin had 1–2.5 in per NWS (10:32 ET). **11/24: 0.00 at every station** | api.weather.gov; AEOLUS arithmetic |
| Against forecast | The heaviest observed (2–3 in in Broward and Miami-Dade) is at the low end of the 2–4 in "most likely" range, with 1–3 more forecast. Treasure Coast and Brevard are under their 1–2 in | as above |
| SE coastal and canal stages | Moderate (ft above MHHW): Loxahatchee at US-1 2.15, Middle River 2.15, Ibis Way 2.22, S Fork New River 1.98, Ocean Reef 1.72. **All are under the 10/27–28 peaks of 2.55–3.17.** Interior SFWMD canal stages were not read | NWPS |
| St. Johns (SERFC run 09:19 ET) | Cocoa 18.44 (crest 18.5 today; above its record; series high 18.77 on 11/21) · Lake Harney 13.19 (above its record; 12.7 by 12/02) · Sanford 8.38 → 8.5 tonight (record 8.96) · **DeLand 5.84 → 6.3 Sat 11/28 ~13:00 ET** (record 6.33). The warning's own bullet says "steady at 5.9"; the forecast is 6.3 · Astor 4.28 → 4.4 Thu. All five stay major at least a week. Today's basin rain is 0.3–1 in | NWPS; NWS Melbourne |
| DR-4956-FL fit | Re-read at OpenFEMA 11:46 ET. Household aid: Brevard, Indian River, Martin, Okeechobee, Palm Beach, St. Lucie. Public assistance only: Hardee. **Incident period from 10/31, no end date.** Today's rain falls on the declared east-central counties lightly, on Palm Beach moderately, and **hardest on undeclared Broward and Miami-Dade.** The river crest pressure is in Seminole and Volusia, which are also undeclared | OpenFEMA |
| **New or tail?** | **Tail for the declared counties and the St. Johns**: same watches, same saturated ground, and the incident period is still open. **A new flood day for Broward and Miami-Dade**, which have no declaration. A secondary search (not read at the page) shows a western-Broward "rain bomb" on 11/18 with local states of emergency; that is CORAL's to verify | inference, labelled |

**CORAL packet sent before the rest:** `AGENTS/CORAL/inbox/2026-11-25_from-AEOLUS_se-florida-rain-hazard-read.md`, commit **ef14875b4e**, at 11:47 ET. A pointer by message failed: the name "CORAL" was not reachable from this session.

## 2. California
**NOAA CO-OPS answered normally at 11:47 ET.** The 11/24 refusal has cleared. I sent one test, then paced requests 2 s apart with the client string unchanged.

| Station | 11/25 high (MLLW, preliminary) | Record before today | Verdict |
|---|---|---|---|
| San Diego | **8.654** at 08:42 PST (11:42 ET) | 8.523 (10/27/2026, verified); pre-2026 listed 8.237 (2015) | **new high +0.131** |
| La Jolla | **8.114** at 08:18 PST | 7.983 (10/27/2026); 7.808 (2015) | **new high +0.131** |
| Los Angeles | 8.194 at 08:36 PST | 8.194 (10/27/2026) | **tie** (a verification change could break it either way) |
| Orange County | no NOAA tide gauge (Newport 9410580 returns no data), none in NWPS | — | bracketed by LA and La Jolla |

NWS's 7.9–8.3 ft range was beaten by 0.35 at San Diego. Residuals at the high were +1.0 to +1.2 ft. Thursday's predicted high is lower (San Diego 7.303 at 09:19 PST), so today was probably the peak of this cycle. A long-period swell arrives Thursday morning.

**Northern California has not peaked.** These are projections from the 08:48 PST residuals (predicted high plus current residual). On Southern California this morning the method ran 0.02–0.05 ft low:

| Station | Predicted peak (ET) | Projection | NWS forecast | Record |
|---|---|---|---|---|
| Arena Cove | 13:12 | ~8.77 | — | 8.862 (11/24/2026) |
| San Francisco | 13:48 | ~7.95 | 8.5 | 8.663 (1983) |
| Crescent City | 13:54 | ~9.47 | — | 10.663 (1983) |
| North Spit (Humboldt) | 14:06 | ~9.86 | 10.0–10.4 (window 12:00–16:00 ET) | 10.359 (1/2026) |

Unscored views: a San Francisco record today about 5% (down from 20% in D:L1256); an Arena Cove record today about 30%. Surge can still add into the peak: the 11/24 San Francisco residual at the high was +1.29.

## 3. Impact (established vs reported)
- **Florida, ESTABLISHED (NWS preliminary storm reports, county officials):** I-95 northbound at SR-836/Jackson hospital had 2 left lanes blocked at 10:17 ET; I-195 eastbound at US-1 was flooded; Pembroke Pines had deep standing water. **REPORTED:** street flooding at N 64th Ave (media). No port, power or named facility was reported.
- **California 11/24, ESTABLISHED (NWS reports, law enforcement and Caltrans):** US-101 S at Seminary Dr offramp closed (Marin), US-101 NB lane flooded at Marin City, Menlo Park turnaround closed, US-101 two southbound lanes closed near College of the Redwoods (Humboldt), waves over US-101 at Crescent Beach. **REPORTED (public or media):** Webster Tube (Alameda–Oakland) blocked; flooding in Corte Madera, San Rafael and Foster City. **This corrects my 11/24 "Bay Area impacts SEARCH-NOT-FOUND" (KB-333 corrects KB-329).** No port, refinery, power plant or airport was named.
- **California 11/25:** SEARCH-NOT-FOUND. There are no NWS San Diego or LA storm reports since 11/24, and no dated news yet.

## 4. Inbox drained (whole, every sender)
| Item | Disposition |
|---|---|
| SIG-W-20261125-009 (WALTER, IMMEDIATE, ACTION) | **acted**: this packet; KB-330…333 |
| SIG-W-20261125-019 (WALTER, INFO, DR-4956-FL) | **noted**: re-read at OpenFEMA and used in item 1 |
| SIG-W-20261125-021 (WALTER, IMMEDIATE, INFO; arrived mid-session) | **noted**: matches my NWPS read; adds Sanford record 8.96 and NE Florida coastal flood warnings to 19:00 ET Thu |
| `inbox/` top level | empty (no direct packets) |

All three are logged in `board_log.tsv` and moved with `git mv`.

## 5. Forward view and routing
- **Florida:** DeLand at or above 6.33 by 12/02 is about **40%** (unscored), with the forecast 0.03 under. Sanford reaching 8.96 is about 5%. The next rain is late Sun to early next week. The DJF wet-winter call stands (AEO-19, 75%).
- **California:** the 12/23–25 king tides run 0.11 ft (San Diego) to 0.24 ft (Arena Cove) higher astronomically than today. If the El Niño background holds, **new Southern California and North Coast records then are more likely than not (~60%)**. A San Francisco record then is about **25%** (unscored; D:L1256 had 30%). What would change my mind is the residual falling below +0.8 ft in December.
- **Not mine, flagged:** WPC Day 1–2 shows an East Coast cyclone with heavy rain from coastal North Carolina to the NYC area over Thanksgiving (Slight risk). It is not an AEOLUS channel unless it turns into a cold or power story.
- **TERRY** packet `AGENTS/TERRY/inbox/2026-11-25_from-AEOLUS_fl-rain-and-ca-record-tides-tradeability.md` (no card asked; my read is that no vehicle is armed).

## What PROME should register (owed #23)
**AEOLUS read, Wed 11/25 from 14:30 ET, or by Fri 11/27:** observed 11/25 highs at Arena Cove (9416841) vs 8.862, San Francisco (9414290) vs 8.663, Crescent City (9419750) vs 10.663 and North Spit (9418767) vs 10.359; CO-OPS 6-min, or NWPS ANVC1/FTPC1/CECC1/HBYC1. Add Wednesday's NWS reports from Monterey and Eureka. **Ageing:** CO-OPS keeps 6-min data indefinitely (preliminary, later verified). The NWPS observed series covers ~30 days (to ~12/25). NWS reports stay in the product archive for days; local news is best within 48 h. Thursday adds a second, lower high (SF 8.0 forecast at 14:38 ET Thu).

## COMPLETION — AEOLUS — 2026-11-25
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/AEOLUS/{STATUS.md, SCRATCH.md, board_log.tsv, workbook/KB.tsv, archive/STATUS_ARCHIVE_2026-11-25_bottom-line.md, sources/2026-11-25_fl-flood-and-ca-tides/*, inbox/WALTER/processed/SIG-W-20261125-{009,019,021}.md}, AGENTS/CORAL/inbox/2026-11-25_from-AEOLUS_se-florida-rain-hazard-read.md, AGENTS/TERRY/inbox/2026-11-25_from-AEOLUS_fl-rain-and-ca-record-tides-tradeability.md, this memo
RESULT: SE Florida rain is a new storm under the same 11/23 watches; the heaviest is in undeclared Broward and Miami-Dade, and the St. Johns is the tail (DeLand 6.3 Sat vs 6.33). San Diego 8.654 and La Jolla 8.114 set preliminary new highs (+0.131 over 10/27) and Los Angeles tied. KB-330…333; no score moved (15/30, fired 0 of 6).
GAPS: NorCal observed highs not read (peaks 13:12–14:06 ET, after the session); interior SFWMD canals and Lake Okeechobee not read; 11/25 California impact news SEARCH-NOT-FOUND; the CORAL message pointer failed (packet delivered).
WILL_NEEDS: None.
FOLLOW-UP: Register owed #23 (NorCal observed read from 14:30 ET 11/25, by 11/27); DeLand crest read Sat 11/28.
