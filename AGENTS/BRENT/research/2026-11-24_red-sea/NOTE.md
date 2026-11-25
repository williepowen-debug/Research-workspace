# BRENT — Red Sea threat, Hodeidah strike and the bypass (2026-11-24 night, written from 23:42 EST)

Session brent-desk-agent-2026-11-24, woken by PROME prome-77 on Will's word (23:34 ET). Delivery packet: `PROME/inbox/2026-11-24_from-BRENT_red-sea-bypass-price-and-barrels.md` (same analysis, plain-words section first). Raw bars: `raw/c1_*.json` (23:39 EST capture) and `raw/c2_*.json` (23:41 EST), five-day one-minute vendor bars; script `pull.py`.

## 1. Price reaction (vendor one-minute bars, about 10 minutes behind; not settles; cmegroup.com IP-blocked, no ICE page read)

| Contract | 11/24 day session (window VWAP [14:28,14:30) ET) | Secondhand settle 11/24 | Evening, last traded (ET) | Change vs window |
|---|---|---|---|---|
| Brent Jan BZF27 (M1) | 91.4165 | 91.40, +2.27% (The Nation Thailand via WALTER card 006) | 90.15 at 23:29 | −1.27 (−1.4%) |
| Brent Feb BZG27 (M2) | 88.7864 | — | 87.54 at 23:28 | −1.25 |
| Brent Mar BZH27 (M3) | 86.6034 | — | 85.59 at 22:26 (thin) | −1.01 |
| WTI Jan CLF27 | 82.0556 | 82.05 (same source) | 80.76 at 23:30 | −1.30 (−1.6%) |
| Heating oil Jan HOF27 | 3.6593 | — | 3.6183 at 23:28 | −1.1% |
| Gasoline Jan RBF27 | 2.4413 | — | 2.4089 at 23:32 | −1.3% |

Evening session = the 11/25 session (vendor overwrites the 11/24 daily bar after the 18:00 ET reopen; the daily bar labelled 11/24 is NOT the 11/24 settle).

**News-minute read (CLF27, the liquid leg):** 80.74 at 22:15 → 80.94 at 22:22–22:25 (+0.20) → 80.74 by 22:40. The rise began a few minutes before Reuters 03:26Z (22:26 ET). BZF27 90.02 at 22:09 → 90.25 at 22:24 → 90.08 at 22:50. **The fall of about $1 from 20:00 to 21:45 ET came before the news,** alongside Asian risk-off posts (KOSPI sidecar, SoftBank −10%, copper −3.5%, per WALTER card 018 item 20, posts, unverified).

**Curve:** M1−M2 evening 2.61 vs 2.63 at the window (flat). M1−M3 about +4.56 on a stale March last trade vs +4.81 at the window. Flat price fell, the curve did not move: **no prompt tightening priced.** Diesel crack HO−CL Jan 71.21 evening vs 71.64 window vs 79.73 on 11/19 window: diesel premium still unwinding.

## 2. BRT-33 windows (pinned pair BZF27 − BZH27, [14:28,14:30) ET VWAP, capture c1)

| Session | M1−M3 | M1−M2 | Valid | Note |
|---|---|---|---|---|
| 11/19 (control) | +4.8513 | +2.5548 | yes | reproduces the 11/20 note to four decimals |
| 11/20 | none | +2.6124 | NO OBSERVATION | BZH27 no bar (reproduces) |
| 11/23 | +4.8917 | +2.6841 | yes | BZF27 89.3464, BZH27 84.4547 |
| 11/24 | +4.8131 | +2.6301 | yes | BZF27 91.4165, BZH27 86.6034 |

Valid 11, none under +3.5000. Remaining sessions 11/25 and 11/27 (11/26 Thanksgiving; 11/27 hours unread). Grade NO at the first read after 11/27 unless a window crosses. My unregistered projection: about 3% (from about 10% on 11/20); tonight's news pushes the spread the other way.

Other window figures 11/24: WTI M1−M3 +2.0756; HO−CL Jan 71.635; 3-2-1 Jan vs CL 37.531.

## 3. Barrels on the Red Sea side (sources and dates; vendors disagree)

| Quantity | Figure | Source, date | Weight |
|---|---|---|---|
| East-West pipeline (Petroline) capacity | 7 mb/d | Bloomberg 2026-03-28 (title: hits 7 million barrel goal) | wire, title read |
| Petroline throughput | 5.8 mb/d "as of this morning" | Energy Minister Prince Abdulaziz, Manama, 2026-10-06 (Al Jazeera with Reuters, page read) | state, secondary of a primary |
| Of Petroline, feeding west-coast refineries | about 2 mb/d (about 5 mb/d for export) | Aramco CEO, May 2026 (search summary only) | unverified at page |
| Yanbu / Red Sea crude exports, October | Vortexa about 2.5 mb/d (2.4 Sep) | Gulf News 2026-10-31 (page read) | secondary of vendor |
| Yanbu loadings | Kpler about 3.07 mb/d October, about 2.7 mb/d November to date; about 450 kb/d of it south via Bab el-Mandeb | WALTER card 20261123-022 item 3 (relayed, Kpler page not read) | relay |
| Yanbu, Kpler, Oct 1–25 | 2.21 mb/d (2.54 Sep) | search summary (low-weight sites) | low |
| Saudi total exports, October | Kpler 5.4 · Vortexa 6.5 · TankerTrackers 6.99 mb/d | Gulf News 2026-10-31 | secondary of vendors |
| Ras Tanura (Gulf side) | 2.95 mb/d Oct 1–25 vs 4.16 Sep (Kpler via Asharq) | Gulf News 2026-10-31 | secondary |
| Saudi west-coast product exports | 970 kb/d 2025 average; under 1.0 mb/d July 2026; Jizan refinery 400 kb/d capacity, about 200 kb/d exports June–July | Kpler blog (about early August 2026, undated page) | vendor, stale |
| Hormuz clearance (all origins) | 9,947 kb/d, 58% of 17,148, 7 days to 11/21 | Kpler via WALTER card 022 item 8 | relay; floor (recent days settle higher) |
| World production Q4 2026 | 105.14 mb/d | EIA STEO November (BRENT pull 11/10) | primary |
| OPEC surplus capacity | 0.01 mb/d through Q1 2027 | EIA STEO November (BRENT pull 11/10, CATALYSTS row 24) | primary |
| World stock change Q4 2026 | build 1.47 mb/d | same | primary |

**Read:** about 2.5 to 3.1 mb/d of Saudi crude leaves through Yanbu (about 40% of Saudi crude exports, about 2.4 to 2.9% of world output), plus up to about 1 mb/d of west-coast products (stale basis). A Red Sea outlet shut for days would put about 3 to 4 mb/d gross at risk. **Most Yanbu crude goes north to Suez/SUMED; only about 450 kb/d passes Bab el-Mandeb, so the port itself, not the strait, is the exposure.** Jeddah and King Abdullah Port are container and general-cargo ports (Jeddah also an Aramco product-import and distribution terminal) [EST, domain knowledge, not re-verified tonight]: a Jeddah hit is an import and civil-logistics shock, not a crude-export loss. **The offset is thin:** EIA's surplus capacity is about zero because the spare sits behind Hormuz; re-routing Yanbu crude back to Ras Tanura sends it into the strait where three hulls were struck 11/22 (UKMTO 219-26). The stock build (1.47 mb/d Q4, EIA) is the real cushion.

## 4. What is and is not established tonight

| Item | State |
|---|---|
| Coalition says it struck "operational capabilities" at Hodeidah, early Wed 11/25 local | COALITION STATEMENT (Reuters 03:26Z via WALTER 006); damage and port status not stated |
| Houthi threat to Jeddah and all Saudi Red Sea ports if Hodeidah were struck | THREAT; condition now met; shipping-office emails name Jeddah (The National 11/23 via WALTER 025) |
| Riyadh financial-district tower, drone, 11 wounded, 11/24 | STRUCK, state-confirmed (civil defence) |
| Three ships struck eastbound in Hormuz | UKMTO 219-26: 22 Nov 20:25 UTC, verified, time-late, all continued, crews accounted for. A Sunday event, already in Monday and Tuesday prices |
| ADNOC PPA notice JDR/MN/023/2026 (11/23): tankers barred from ADNOC-PPA waters unless calling at its ports, 90 days | image of the notice via WALTER 017; original not on adnoc.ae; does not name Fujairah |
| Any hit on Saudi crude or product export infrastructure after the threat | NOT FOUND (WALTER search 22:40 ET; my searches 23:4x). Rabigh 11/22 claim only; Jizan 11/20 intercepted |
| Any Yanbu loading halt | NOT FOUND (BRT-32 letter not met) |

**ADNOC ban:** it clears third-party tankers from waiting, STS and transit in Abu Dhabi's western waters; it does not stop ADNOC's own loadings at Ruwais, Jebel Dhanna, Das, Zirku or Mubarraz. Volume effect UNSTATED; it is a security measure that removes anchorage and STS space inside the Gulf, not a supply cut.

## 5. Rows and gates (letters unchanged)
- BRT-33: valid 11, none under; OPEN; grade after 11/27.
- BRT-32 (Yanbu halt ≥24h, 11/6–12/31, 20% registered): letter not met; my unscored current view for the next two weeks alone about 8 to 10%.
- COT-FUEL-35B: no print tonight; #16 as-of Tue 11/24 (before the Hodeidah strike) releases Mon 11/30.
- BG-02 frame-breaker: NOT MET (no R1 statement, no named quantity).
- JWC listing: Southern Red Sea (Yanbu inside) and Saudi Arabia already listed; KILL-LEG2-JWC-LISTING not fired; no new circular read tonight.
- Energy arm RETIRED 8/7 (ACTIVE_DECISIONS), WQ-192 stand-down: unchanged and still fits tonight's facts (see packet § finding).
- D:L1224: WPSR week 11/20 released Wed 11/25 10:30 ET (EIA schedule page read 23:4x EST: no exception listed for 11/25); second read owed after 10:30 ET and again at the 14:28 ET BRT-33 window.
