# News catch-up — Fri 10/2 16:00 ET → Wed 10/7 ~09:30 ET

**Owner:** PROME · **Written:** 2026-10-07 09:3x ET (Claude Code cloud session, Will-directed: *"there has been a lot of news we need to catch up on"*). **Status:** READ-ONLY sweep — five web-research helpers (Opus; read-only, no repo writes) + PROME's own read of the RESEARCH-INTAKE lane (`data/2026-10-05`, `data/2026-10-06`; last collector run 2026-10-06 19:56Z) + PROME level pulls (`fetch.py price` via Yahoo; FRED cache-busted CSV — the API key is absent in this container).
**What this is NOT:** a signal record, a route, or a grade. WALTER owns ingest/dedupe/routing (packet `AGENTS/WALTER/inbox/2026-10-07_from-PROME_news-catchup-for-routing.md`); every gate below is graded by its OWNER. "Could fire / does not reach" lines are PROME consumer reads.
**Why the gap:** the fleet's last BOARD signal is SIG-W-20261005-006 (WALTER Codex session, 10/5 ~10:38 ET); no desk committed on Tue 10/6.

⚠️ **Coverage:** all five helpers exhausted the shared web-search budget part-way. Items marked SEARCH-NOT-FOUND are UNSEARCHED or unfound, NOT confirmed quiet (list in § Gaps). Grades: PRIMARY (official text read) · MULTI (≥2 independent outlets) · SINGLE · UNVERIFIED (OSINT/social).

---

## 1. Headline

The global long-bond selloff resumed this morning in the US, UK and Japan. On primary data, the US 30-year real yield set a new cycle high of 3.37% [10/5 Treasury]. European bank stocks fell about 3.5% this morning on France contagion fears [Reuters, SINGLE]. Middle East fighting widened:
- More Hormuz tanker hits. The latest UKMTO report number found is 156-26; the MT On Peace attack injured 12 crew.
- A pump station on the East-West pipeline at Khurais was hit.
- A ground offensive is under way on the Bab el-Mandeb coast.
- Houthi strikes hit Saudi airports.

Oil nonetheless eased, because Gulf exports are back near pre-war levels (Kpler) and the pipeline is running about 5.8 mb/d (Saudi minister).

**Tropical Storm Isaias** is forecast to become a Category 2 hurricane and make landfall at Mobile Bay / the western Florida Panhandle late Fri 10/9 to early Sat 10/10 [NHC, PRIMARY]. That ground took 10–14 inches of rain on 10/2–10/5, and Florida has declared an emergency in 25 counties.

Credit paused rather than broke: HY OAS 324 → 310 → 312. Underneath, quality is eroding:
- US loans priced below 60c: $65B, the most since March 2020 (JPM).
- CMBS delinquency 8.02%, the highest since 2020 (Trepp).
- Private-credit valuation lawsuits.

AI financing news pointed to MORE spending: an OpenAI $30B raise at $1.4T (in talks), a Google–Constellation 3.59 GW deal, and Marvell's FY28 target raised to $20B. Stocks closed at records on 10/6.

## 2. What touches a live line (PROME consumer reads — owners grade)

| Line (owner) | Read | Evidence (dated, basis) |
|---|---|---|
| **HANS T-13 UK 30Y gilt 6.00%** | **COULD FIRE on today's close** | 6.026% intraday 10/7 [Trading Economics, SINGLE vendor]. On 10/1 it went above 6% intraday and closed ~5.9%, so only the close counts. |
| **SAM USD/JPY ¥158.054** | **Basis question — SAM's to settle** | Investing.com close 158.31 [10/6]; Yahoo 158.28 [10/7 ~09:15 ET, vendor]. Official Fed H.10: 157.81 [10/2]; the 10/5–10/6 H.10 prints are due 10/13. The same vendor also shows 10/1 at 158.07 vs H.10 157.63, so vendor and official disagree. |
| **WQ-365 QQQ Dec-18 put-spread card (TERRY; NOT approved)** | **Kill leg HY ≤312 TOUCHED on FRED** | HY OAS 310 [10/2] · 312 [10/5] (FRED `BAMLH0A0HYM2`, cache-busted CSV pulled 09:0x ET 10/7). Whether the card reads this series/basis is TERRY's call. Buy leg not met: QQQ has not closed back below $748.65 (759.66 [10/6c]). Needed-by 10/6 has passed. |
| HY >320 sustained-3 (RED FT-02 / REGINALD T-03) | Does not reach | 324 [10/1] → 310 [10/2] → 312 [10/5]. The count resets on the owners' rules. The fastest path to a fire needs three consecutive prints >320 from the 10/6 cell on. X1 stays CLOSED. |
| GATE-HY-REKILL (<260 ×2) | Does not reach | 312, 52bp above. |
| GATE-LIQ-072 (IG >94) | Does not reach | IG 84 [10/5 FRED]. |
| GATE-LIQ-069 (CoreWeave CDS) | No new print found | SEARCH-NOT-FOUND for ISDA-converted DTCC prints after 9/26. Bloomberg Tax 10/6: data-center debt selling off and hyperscaler 5Y CDS "nearing widest levels this year" (no figures, SINGLE). Review 10/15. |
| GATE-BRK-R2 (private-credit redemption) | Candidate for BROCK | **Blue Owl OTIC (~$5B fund): 39% of shares ($1.1B) asked to redeem vs a 5% cap** [Reuters 10/2 12:16 via KSL/Investing, MULTI]. Same release as the OCIC leg; whether it was counted is BROCK's to say. Cox Capital's secondary bid for OCIC at $7.31 = 20% below the 8/31 NAV of $9.14 [PRIMARY release, 10/5] is a price, not a gate. |
| **VLO-HELD-01 leg A (crack <$90.16)** | Does not reach | Nov crack HOX26×42−CLX26 ≈ $103.2 [10/6 close, vendor]; ≈$107.5–108 [10/7 pre-market, vendor; HO +3%]. PROME consumer read recorded on GATES 10/7. |
| VLO-HELD-01 leg B1 (signed export restriction) | Does not reach | Trump EO "Emergency Tax Relief on Diesel Fuel" (10/5 20:57 ET) defers the dyed-diesel highway excise tax through 12/31; 9 sections, the word "export" never appears [whitehouse.gov, PRIMARY]. Federal Register: no export rule since 10/2. Trump: "No diesel export ban" (10/5, Fence Post via intake). ⚠️ The threat is not dead: National Interest 10/6 "How Europe can talk Trump out of a diesel export ban"; FT 10/5 calls it "diesel export coercion". |
| USO Oct-09 $150 call (Will; TERRY stop Fri 10/09 15:00 ET) | No line; time-critical | USO $144.91 [10/6c] needs ~+3.5% by Friday. WTI ~$89.8–90 [10/7 vendor]. **PROME interpretation, not a grade:** Isaias crosses the central-Gulf production area Thu–Fri, and pre-storm offshore shut-ins are the one scheduled-looking catalyst before the stop. Size and timing are unmodeled (BRENT/AEOLUS). |
| FALCON D 85→92 (Khurais production plant) | Does not reach | The named target is a Khurais PUMPING STATION on the East-West line [AFP via FMT 10/5, MULTI on the strike]. Misbar's Sentinel-3 smoke labels the "Khurais oil processing facility" but "does not establish cause" [UNVERIFIED]. No Saudi confirmation of a production-plant hit. |
| GATE-FALCON-001 (Bab el-Mandeb) | Nearest path yet; not fired | Yemeni government "Operation Yemen Dawn" claims Mocha/Dhubab/Bab/Hadeid; Houthis deny; fighting at Dhubab 10/6 [Euronews/Al Jazeera, claims MULTI, control UNVERIFIED]. No new ship attack found at the strait after the 10/4 near-miss. |
| BRENT vessel-sunk frame-breaker | Does not reach | Hormuz hulls damaged, none sunk. CENTCOM's 13 destroyed are interdicted Iran-blockade trade, excluded by the capacity floor. Black Sea: Alfa Watan sank ~70nm off Bulgaria; type unstated, 2 dead [Al Jazeera, MULTI]. Recheck if confirmed a tanker. |
| BRENT Petroline (BG-02) | **Registered resolver LAPSED 9/25 — nothing to fire** | The helper flagged a "could fire" from the 10/4 halt (AFP: "pipeline stopped again"; Bloomberg/Reuters sources 10/5: flowing normally; minister 10/6: "around 5.8 million barrels"). ⛔ The BG-02 throughput resolver was GRADED NOT MET / LAPSED 2026-09-25 with no extension (WQ-264 ③; DOCKET L329). This is new evidence for BRENT, not a live trigger. The deploy question stays CLOSED regardless (needs BG-02 MET + WQ-192 lifted + [Approve]). |
| Cushing <20.0M | Does not reach | API week to 10/2: Cushing +0.87M [vendor]. EIA 10:30 ET today. |
| HENRY 30Y nominal 5.50% | Already through, deeper | 30Y 5.66% [10/5 H.15], 5.64% [10/6 Treasury]; ~5.72% pre-open 10/7 [CNBC/Yahoo vendor]. |
| HANS T-10 France | Stays FIRED | OAT–Bund spread 143 [10/5] → 127 [10/6] → 134bp [10/7] [single vendor with internal inconsistencies]. |
| CORAL MSI-01 (grade 10/09) · bank rail | Does not reach | Nothing in the window feeds the MSI. Isaias lands AFTER the 10/09 grade. No Florida-bank or condo-loan deterioration found (under-searched). |
| HOMER thesis-kill (0 of 5) | Does not reach | Everything moved the thesis's way: MBA 30Y 7.49% (wk to 10/2, ~3-yr high), applications −4.2%. Lennar −5.3% [10/5] on a Hunterbrook short report (Millrose bought 700+ Lennar homes ~13% above retail). Berkshire Form 4: bought 2.42M LEN shares 10/1–10/2 [SEC, PRIMARY]. |
| FERT G5 (review 10/07) · India IPL urea tender | Pending | Tender closed 10/7 02:00; offer prices SEARCH-NOT-FOUND at ~09:15 ET. Pre-tender: China added >1.5 Mt of export quota; prilled ~$380/t fob [9/23]. World Bank Pink Sheet (Oct ed.): urea $407.5/t Sept avg (+4.5% m/m) [PRIMARY]. |
| MIDAS gold de-crowding | Does not reach (no new COT) | Gold ~$4,089–4,118 [10/7, −1.8% d/d, ~−6% m/m, vendor]; silver ~$60 (−1.9%). Next COT Fri 10/9 15:30. |
| VULCAN breadth RED | Does not reach | Helper's own calculation: RSP−SPY 63d −4.34pp [10/6] (allow ~0.15pp basis vs VULCAN's −5.07 [10/1]); mostly start-date roll-off. Mag-7 share SEARCH-NOT-FOUND. |
| HBAN Oct-16 $16P ×2 (WQ-302, by 10/14) | Information | HBAN $15.33 [10/6c] = $0.67 in the money; **expires before HBAN's Thu 10/22 earnings**. |

## 3. By theater (top items; full sourcing in the helper ledgers, held in-session)

**Rates / macro**
- **ISM services Sept (10/5 10:00):** headline 54.9; **prices 74.0, highest since Jul 2022**; employment 50.1. Respondents cite diesel costs and "possible tariff reinstatement" [ISM via PR Newswire, PRIMARY].
- **Official curve 10/5:** 10Y 5.31 · 30Y 5.66 · 30Y real **3.37 (cycle high)**. **10/6:** 10Y 5.27 · 30Y 5.64 · 30Y real 3.35 [Fed H.15 + Treasury, PRIMARY]. The 10/6 dip is attributed to an oil dip and Bessent's debt reassurance [Bloomberg, SINGLE on cause].
- **3Y auction 10/6:** $58B at 4.932%, about 0.2bp through when-issued. Bid-to-cover 2.62. **Indirects 57.6% vs 65.9% average** [vendors, MULTI; Treasury release not fetched; intake lane rates it "avg"].
- **Fed:** October-hike odds ~20–22% [CME via vendors]. Logan said 10/1 that ≥50bp more is needed (before the window). Speaker remarks 10/6: SEARCH-NOT-FOUND.
- **Funding calm:** SOFR 3.90% [10/6]; standing repo facility take-up $0–2M/day [NY Fed, PRIMARY]. This is a term-premium move, not plumbing.
- **Japan:** 10Y JGB new-issue coupon 3% for the first time in ~30 years, yields still rose (10Y 3.11%, 30Y 4.243% [10/6]) [Nikkei, MULTI]. BOJ October-hike odds fell to 12% from 40% [SINGLE]; BOJ meets 10/30.
- **Europe:** UK 30Y 6.026% intraday; BoE's Mann says labour "isn't weak enough". STOXX banks −3.5% 10/7 (SocGen −5.2%, Deutsche −4.5%), France contagion cited [Reuters via Investing, SINGLE].
- **China:** FX reserves −1.11% in September; markets reopen 10/8. Fifth Plenum date SEARCH-NOT-FOUND.

**Middle East / energy / Russia**
- **Hormuz:** about 9 UKMTO reports so far in October (156-26 is the latest number found). MT On Peace (Panama flag), 12 injured, 10/6. LPG and crude tankers hit 10/4 (Aframax Lipsi). IRGC turned a tanker back off Khasab on 10/5 [gCaptain/Reuters, MULTI].
- **Supply:** Kpler puts Gulf exports at 18.3 mb/d (7-day average) by 9/30, pre-war level. Shell CEO: flows "80-plus percent" of pre-war. Brent below $100 intraday 10/6 (low $97.8); ~$101–102 on 10/7 [vendors; one quotes $104.74, a ~$3 dispersion — §2R defect class 2].
- **Saudi:** Houthi claims on the Rabigh refinery [UNVERIFIED] and Riyadh airport. Saudi civil aviation confirms hits at Jizan and Najran airports. Missile intercepted north of Riyadh 10/7. US and UK embassies warn of attacks on energy infrastructure. Intake: a Jeddah refinery attack reported by Tasnim via Newsquawk 10/5 [UNVERIFIED].
- **Diplomacy (the book's main downside risk):**
  - Qatar confirms US–Iran mediation is ongoing (10/6, SINGLE).
  - Trump: the war will "end very soon" (10/6).
  - Vance: a deal needs a "meaningful" enrichment cut.
  - Pezeshkian calls the talks "meaningless" (10/5).
  - Araghchi: Hormuz stays shut until Iran's 7 conditions are met (10/4).
  - No deal text exists.
- **US supply measures:** SPR exchange of up to 40M bbl offered 10/5, part of the March 172M commitment and not the G7 100M [Rigzone, SINGLE]. G7 country shares and timing: SEARCH-NOT-FOUND.
- **Russia:** Ukraine's MoD claims 51% of Russian refining is out [unverified claim]. ~650 drones flew at the Moscow region. Trump blamed Ukraine's strikes for US fuel prices (10/5). Black Sea drone hits inside NATO waters (Bulgaria). Intake: the Russian diesel export ban may be lifted for some companies in October (Interfax via Newsquawk 10/6). Russia's MFA warned diplomats in Kyiv of "mortal danger"; the EU says no embassy is leaving.

**Credit / banks / private credit**
- **JPM:** US loans priced below 60c at $65B vs $40B a year ago, the most since March 2020; tech is the largest sector [Bloomberg headline, SINGLE].
- **Trepp September CMBS delinquency 8.02%** (+17bp). Office 12.16%. Multifamily 8.04%, above the overall rate for the first time since Covid [MULTI, via Trepp].
- **Private-credit valuation:** Semafor 10/6–7 reports Woolery suits against FS KKR, Ares and Blue Owl over inflated marks and incentive fees on PIK interest. One loan (Kellermeyer) is marked ~100c by one lender and ~10c by another. PIK is more than 1/3 of income in Blue Owl's tech fund. An SEC warning to auditors. A Fed probe of bank collateral vetting. Intake 10/6: NY Fed reportedly investigating major banks' private-credit loans [Yahoo; date of review SEARCH-NOT-FOUND].
- **Redemptions easing:** OCIC+OTIC $4.2B vs $4.7B; GS Credit Fund 2% vs 3.2%. Blue Owl flags a 2028 refinancing wall.
- **Apollo 8-K (10/5):** preliminary Q3 alt NII ≈ $375M (~10% annualized); earnings 11/3 [PRIMARY]. A near-term headwind to the APO put.
- **Supply:** SoftBank's $11.1B junk deal, 7-year at 9.75%; Paramount Skydance $52B; global spreads +5bp on the week to 10/3 [SINGLE].
- **CRMT:** no 8-K 10/2–10/7. The lender waiver and facility termination date is **10/8** (8-K 10/1, PRIMARY). DOCKET L480/L585 are BROCK's.
- **Quiet:** FDIC failed-bank list last updated 9/25 (Nano Banc). Hertz: no 8-K since 10/1.

**AI capex / tech**
- **OpenAI** in talks to raise ≥$30B at $1.4T pre-money; UAE (MGX) anchor; BlackRock in separate talks [Bloomberg, SINGLE].
- **Google–Constellation:** 3,590 MW in PJM (890 MW new nuclear uprates, 20-year; 2,700 MW existing, 15-year). CEG +12% [MULTI].
- **Marvell** FY28 target ~$20B (from $18B) [MULTI].
- **CME / Silicon Data compute futures did NOT list:** the CFTC extended its review 45 days to 11/9; comments close 10/20 [MULTI]. DOCKET L250's premise has slid.
- **Micron Taoyuan union** authorized a strike (99% of voters); no date set; Taipei rally 10/19 [MULTI].
- **CoreWeave × AdaniConneX** 240 MW India; financing not disclosed. CoreWeave insiders sold ~$17.6M to cover taxes.
- **Samsung** preliminary Q3 due Thu 10/8 (KST); consensus operating profit ~106T won. Memory price increases slowing to single digits in Q4.
- **Closes:** S&P 7,818.93 · Nasdaq 27,599.79 · QQQ 759.66 [10/6, records]. Only ~25% of S&P members are above their 50-day average. VIX rose on the record day (15.76).

**Florida / housing / climate / commodities**
- **Isaias:** NHC Advisory 3 (10/7 05:00): 40 mph at 22.0N 94.1W. Forecast 95 kt Fri 05:00 at 25.5N 88.5W, inland SW Alabama Sat 05:00. Hurricane watches likely later today; rain 3–6 in, up to 10 in, LA to FL Panhandle [PRIMARY]. A DeepMind ensemble put Cat-3+ at 43% [Yale CC, SINGLE]. Artemis: a Cat 2 is "not an event of note" for cat bonds; losses land on primary insurers and Citizens.
- **FL EO 26-202:** emergency in 25 counties; soils "saturated" [PRIMARY].
- **Actual rain 10/2–10/5:** Navarre 13.96 in, Eglin 11.09, Pensacola up to 10.93, Apalachicola 11.84 [NWS, PRIMARY]. The forecast "20+" tail did not occur. Damage and rescue counts SEARCH-NOT-FOUND.
- **Rhine at Kaub:** 1 cm [10/7 09:00]; it read −6 cm on 10/1 [WSV PEGELONLINE, PRIMARY].
- **El Niño:** ⚠️ **fleet figure stale.** CPC (9/10) put >90% on a very strong event and 75% on record strength (>+2.5°C) for Oct–Dec; NOAA 10/6 says Jul–Sep was the second-largest anomaly on record. The fleet carries "81%" (NOAA 7/25). CPC update Thu 10/8.
- **Copper** ~$6.5–6.6/lb; Antofagasta workers voted to strike; Chile output at its lowest since Feb 2011 [SINGLE].
- **Gold:** central banks continued buying in August (WGC, via intake).

## 4. Next 48h (ET)
- **Wed 10/7:**
  - EIA petroleum 10:30
  - NHC Isaias advisories 11:00 / 17:00 / 23:00
  - Fed: Waller 10:00 · Jefferson 13:30 · **10Y reopening $39B 13:00** · **FOMC minutes 14:00** · Bowman (eSLR) 15:00 · G.19
  - IPL urea offer prices (time unknown)
  - Samsung preliminary Q3 (~evening ET)
- **Thu 10/8:**
  - **Claims 08:30** (consensus 200K)
  - CPC ENSO ~09:00
  - Bowman 10:45
  - Freddie Mac PMMS 12:00 (prior 7.28%)
  - **30Y reopening $22B 13:00**
  - H.4.1 16:30
  - **CRMT waiver/termination date**
  - ECB account; Bailey and Waller speak; China markets reopen
- **Fri 10/9:**
  - Isaias at ~95 kt in the central Gulf
  - TSMC September revenue (expected)
  - UMich 10:00
  - Rig count 13:00
  - **USO 150C stop 15:00**
  - COT 15:30 (as of 10/6)
  - H.8 16:15
  - CORAL MSI grade
  - DOCKET 10/09 cluster
- **Sat 10/10:** Isaias landfall, Mobile Bay / western Panhandle (forecast).
- **Mon 10/12:** Columbus Day; bond market closed, no HY print.
- **Tue 10/13:** JPM / WFC / C earnings.
- **Wed 10/14:** BAC / MS earnings · Beige Book · WQ-302 / WQ-357 / WQ-360 decision dates.

## 5. Corrections to the fleet record surfaced by this sweep
1. El Niño probability: CPC 9/10 says >90% very strong / 75% record, not the 81% (7/25) carried by the fleet. Owner AEOLUS.
2. Compute futures did not list on 10/5; the CFTC extended its review to 11/9 → DOCKET L250 (VULCAN/WATT/DEWEY) premise has slid.
3. Petroline: the helper's "could fire" is withdrawn by PROME; BG-02 LAPSED 9/25 (see § 2).
4. Blue Owl OTIC 39%-of-shares request (10/2 release) may be missing from the BRK-R2 tally, which records OCIC only. Owner BROCK.

## 6. Gaps (SEARCH-NOT-FOUND — search budget exhausted)
- **Macro:** Fed speaker content 10/6; US government funding status; Canadian counter-tariff status; tariff court rulings; Fifth Plenum date; ECB.
- **Credit:** student-loan/card/BNPL news; Meta off-balance-sheet bond and Stargate debt prices; new CoreWeave/Oracle CDS prints; FLG close after 10/2; the date of the NY Fed private-credit review.
- **Tech:** Mag-7 share; CoreWeave bonds; an unconfirmed ~$70B OpenAI run-rate.
- **Energy:** UKMTO numbers above 156-26; USO 10/7 quote; G7 release country shares/timing; Russian mobilisation signals.
- **Florida:** condo/milestone news; Citizens; Florida banks; migration.

## 7. Provenance
- **Helpers:** five read-only Opus subagents, 10/7 ~09:10–09:20 ET launch, ~8 min each. Ledgers held in-session (not committed); each returned a final report and wrote nothing.
- **Intake lane:** read-only clone of `williepowen-debug/research-intake` at `2e30b63` (collect 2026-10-06T19:56Z); no consumption cursor touched.
- **PROME's own pulls:**
  - `.venv/bin/python3 FORGE/tools/market-data/fetch.py price …` (10/6 closes).
  - yfinance futures 10/7 ~09:15 ET (vendor reads, not closes):
    - Risk assets: ES 7,842 (−0.41%) · NQ 31,261 (−0.71%) · VIX 15.74 · BTC 83,437 (−2.5%).
    - Energy: BZ 101.49 · CL 89.80 · HO 4.71 (+3.1%).
    - Metals: GC 4,113 (−1.8%) · SI 59.99.
    - Rates and FX: ^TNX 5.345 · USD/JPY 158.28 · DXY 102.42.
  - FRED cache-busted CSV `BAMLH0A0HYM2` / `DGS10` / `DFII10` through 10/5.
