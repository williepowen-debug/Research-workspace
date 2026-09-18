# BRENT — News catch-up, Friday 2026-09-18 (live session, boot ~10:58 ET)

**Scope:** what moved since the 9/17 crash-recovery closeout. Tape is INTRADAY (10:59 ET pull, `FORGE/tools/market-data/fetch.py`, named NYMEX contracts, legs rounded to $0.01 by the tool). Nothing here grades a close-specified gate (LESSONS #5). No position changed. Owners: FALCON/HAWK own hull and theater evidence; this note carries the barrel, the tape and the curve.

## 1. Tape — 10:59 ET, all [CONF Yahoo via fetch.py, intraday]

| Contract | Price | Δ day | Note |
|---|---|---|---|
| Brent Nov `BZX26` (NYMEX Last-Day-Financial) | **$104.47** | −0.33% | 9/17 settle $104.82 [CONF CNBC via WALTER SIG-007]; overnight low ~$102.4 (Trading Economics/Investing.com 02:48 ET, financefeeds) then recovered |
| Brent Dec `BZZ26` | $99.71 | −0.22% | |
| Brent Jan `BZF27` | $96.11 | −0.04% | |
| WTI Oct `CLV26` (expires ~9/22, front by tenure) | $102.57 | +0.65% | 9/17 settle $101.91 [CONF CNBC via WALTER] |
| WTI Nov `CLX26` (front by volume, OI 175k) | **$97.23** | +0.00% | |
| WTI Dec `CLZ26` | $92.65 | +0.04% | |
| ULSD Nov `HOX26` | $4.90/gal | +0.28% | |
| RBOB Nov `RBX26` | $3.23/gal | −0.60% | |
| USO | $155.96 | +0.42% | |
| XLE | $64.55 | +0.11% | |
| STNG (tracked, never owned) | $88.07 | +0.25% | |

**Derived (same capture minute, rounded legs ⇒ ±$0.4) [EST]:** Brent Nov−Dec **+$4.76** · Brent Nov−Jan **+$8.36** (vs +$6.55 at 08:38 ET 9/17 and +$10.56 on 9/14 — backwardation re-widened off the post-FOMC dip, still below the 9/14 peak) · WTI Nov−Dec +$4.58 · WTI−Brent like-for-like Nov **−$7.24** (>$5-premium line untouched). Cracks on Nov legs: diesel `HOX26−CLX26` **≈$108.6/bbl** · gasoline `RBX26−CLX26` **≈$38.4/bbl** · 3-2-1 **≈$61.8/bbl**. Physical: Dated Brent reported **>$130** [CONF Saxo/Ole Hansen 9/16; Rigzone 9/17 — vendor assessment, not FRED `DCOILBRENTEU` which lags]; North Sea grade premiums **up to $20 over Dated** [CONF Kpler blog 9/17]; US and EU diesel **>$220/bbl**, US retail diesel record **$6.27/gal** [CONF Saxo 9/16, week of 9/14].

**Registered lines:** none crossed on this read. WTI >$100 (`MKT-CL-F-ABOVE-100`) fired 9/14 on `CLV26`; note `CLV26` is still >$100 while `CLX26` is $97 — the line's contract basis matters next week when Oct expires ~9/22 (roll desync, LESSONS #23/#27). Brent $120 line distance ~$15.5.

## 2. Saudi — Petroline day 8, and the Red Sea leg is now a two-front problem

**Petroline (East-West) status [CONF ENR 9/17 compiling Bloomberg/Reuters/CNBC/Saudi MoE]:** Pump Stations 8 and 9 damaged (Reuters, three oil/security sources); MoE says attacks struck the line in Riyadh and Madinah regions, drones from **Iraq**; MoE gives **no restart timeline**. Aramco objective (Bloomberg): **≥half capacity "within several days," full in ~six weeks**; Reuters sources: repairs **five to six weeks**, partial pumping possibly sooner; US Energy Sec. Wright (CNBC 9/15): flow "within days." ⚠️ All restart figures are OBJECTIVES or third-party estimates — no operator statement of resumed pumping exists as of this note. Pre-shut throughput 4–5 mb/d (Reuters); nameplate 7 mb/d.

**Yanbu [CONF Kpler blog 9/17, vendor primary, single tracker]:** no crude loaded since **9/11**; terminal stock **3–5 days of loadings / ~9 days of refinery runs**; **~4.5 mb/d of crude exports halted** (Kpler's estimate of the Yanbu export base); bypass could restore ~half of Yanbu throughput (**~2–2.5 mb/d of exports**) "within about a month"; full repair 4–6 weeks; YASREF diesel ~200 kb/d flagged at risk; Saudi production **<6 mb/d, multi-decade low** (Kpler estimate). Kpler's only "force majeure" is Indonesian coal — **no Saudi crude FM** (kill-on-sight stands, WALTER ADD#25; FALCON FAL-05 route (a) UNFIRED 9/17).

**The Gulf-side offset [CONF Reuters 9/16 via WALTER SIG-007, unnamed Asian term buyers/trade sources; OilPrice 9/18 citing Reuters]:** Aramco offering Arab Light/Medium/Heavy to Asian term buyers via **STS off Sohar**; Ras Tanura + Juaymah daily loadings **doubled to ~4 mb/d (two VLCCs)**; **~60M bbl sold from Ras Tanura for Sep/Oct loading** (OilPrice 9/18, Reuters trade sources) — the earlier "~20M bbl" figure is the same programme at an earlier vintage. Gulf-of-Oman STS "2.7 mb/d vs 1.5 in August" is quoted by Al Jazeera 9/17 as Kpler data (FXStreet gave no source 9/17) — carry as Kpler-attributed, not verified at Kpler. ⛔ **This is a HAND-OFF, not a route: the shuttles still transit Hormuz.** Hormuz 7-day average flow "almost 12 mb/d by Sunday 9/13" [CONF Saxo 9/16 / Rigzone 9/17, source unnamed] — a FLOOR-class figure, not a level (WALTER ADD#13 class). Saudi total loadings ~2.1 mb/d in H1 September vs 7.5 mb/d Jan–Feb [CONF Al Jazeera 9/17, LSEG/Gibson/Rystad analysts] — that is BEFORE the Gulf-side ramp; net lost Saudi barrels remain **UNKNOWN**, unchanged from 9/16.

**Saudi–Houthi front [CONF AP via Rappler/Al-Monitor/Detroit News 9/17; ABC 9/18; KSAT/AP 9/18]:** Thursday 9/17 Saudi airstrikes in Hajjah (near the Red Sea coast) and around Taiz; Houthis claim an F-15 downed (unverified); first Saudi-announced death (debris from a drone intercepted over **Taif**, western KSA); >80 wounded to date; drone intercepted near Mecca 9/16. Houthis hold Mokha and Perim/Mayyun (WALTER anchor 9/11–13, CONTESTED-dated). Bab el-Mandeb transits: 35/day → 25 after the advance → **45 on Sunday 9/13** [CONF ABC 9/18, vendor unnamed — single-source, do not make a denominator]. Red Sea: **no new ship attacks since 8/24**, traffic ~90% below pre-war [CONF AP 9/18]. ⇒ **For the barrel: the Red Sea leg is a RISK to the Yanbu restart's value, not a current flow loss** — HAWK's 9/17 read (Red Sea transits recovering, Yanbu northbound via Suez/SUMED never touches Bab) stands; Taif is ~150 km from Yanbu and the drone reach now demonstrably covers the Hijaz coast. Restart ⇒ resumed loadings ⇒ Houthi-declared Saudi-ship ban becomes operative again on the southbound leg. Ban is stated by a spokesman only; no enforcement event since 8/24.

## 3. Hormuz — tanker struck today, Iran claims it [FALCON/HAWK own; barrel relevance only]

IRGC says it struck the **Togo-flagged tanker `Trend`** for an "illegal attempt" to pass, and that it was detained after a fire [CONF AFP via Korea Times/FMT 9/18]. UKMTO: incident **16 nm NE of Khasab**, fire extinguished, crew safe, no pollution; UKMTO did not name the vessel, so IRGC-claim ≠ UKMTO-incident is **not established** as one event. A second tanker was hit by an "unknown projectile" **Wednesday 9/16** exiting the strait [CONF AP 9/18]. **Laden/unladen and cargo UNKNOWN** — the BG-02 frame-breaker carve-out (WQ-189: confirmed loss of cargo or Gulf export/transit throughput) is **not met on the facts available**; not graded. Iran rally in Tehran (largest since 2/28); South Korea rules out troops, may expand Gulf of Aden ops.

## 4. Russia — Yaroslavl hit 9/17; no energy truce

Ukrainian drones hit the **Yaroslavl** refinery (~300 kb/d, Rosneft/Gazprom Neft JV, supplies Moscow region) 9/17; fire extinguished [CONF Bloomberg 9/17 via Cyprus Mail/News-Tribune]. Trump's 9/14 energy-truce claim confirmed by neither side; Russia fired 157 drones + missiles at Kyiv/Zaporizhzhia/Odesa 9/17. Syzran (CDU-6, ≥1 month) and Saratov halts already at OSPREY. ⇒ **Products leg strengthens again** (third large refinery this week); crude-export counter-signal (3.54 mb/d 4-wk to 9/13, HAWK) unchanged. Logged to INCIDENTS.tsv only after a primary (LESSONS #1) — Bloomberg is a wire; facility-damage row deferred to OSPREY's confirmation.

## 5. OPEC+ — nothing new; audit clock

Seven-country group held October targets 9/6; next monthly meeting **10/4** (docket row exists). Secretariat capacity audit for 2027 baselines due end-September, ministers late November [CONF OGJ/WorldOil 9/6]. Actual output below quotas on Hormuz/Russia/Kazakhstan constraints — consistent with LESSONS #10. ORACLE 9/17: Polymarket "another country exits OPEC 2026" **24.5%** (Δ7d −12.5) — noted, relevance ruling deferred.

## 6. JWC — boot finding resolved

**JWLA-035, 16 Sep 2026** [CONF LMA PDF, read locally via pdfminer]: **"Amended: Europe — 2) Black Sea excluding territorial waters of adjoining countries other than Russia and Ukraine."** Listed Areas still include **Persian/Arabian Gulf, Gulf of Oman, Indian Ocean, Gulf of Aden and Southern Red Sea** (NW boundary Red Sea south of 25.5°N — Yanbu at ~24°N is INSIDE the listed water), **Saudi Arabia, Yemen, Oman, Iran, Iraq, Kuwait, Qatar, UAE, Bahrain**. ⇒ `KILL-LEG2-JWC-LISTING` **NOT FIRED**; probe baseline re-stamped to JWLA-035; **BRT-30's frozen prediction baseline stays JWLA-034** (resolves on the 10/26 date).

## 7. Still owed today (Friday prints)

- **Baker Hughes rig count ~13:00 ET** — BRT-26 print 1 of 2 remaining vs the frozen **457** oil-rig line (last 450, +1, 9/11). Two independent pulls.
- **CFTC COT ~15:30 ET, as-of 9/15** — `cot_grade.py --expect 2026-09-15`; exit 3 = wait. Vintage #6; base 122,904.5 / bars FROZEN. Cross-check raw `f_disagg.txt`.
- Both grade SEPARATELY (SCRATCH item 3). EIA next 9/23 (BRT-29 weeks 9/18, 9/25 remain).

## Sources
CNBC 9/18 (403; figures via UPI/search snippet) · [UPI 9/18](https://www.upi.com/Top_News/World-News/2026/09/18/saudi-arabia-yemen-crude-oil/2891789703256/) · [Fortune 9/18](https://fortune.com/article/price-of-oil-09-18-2026/) · [financefeeds 9/18 02:48 ET](https://financefeeds.com/brent-crude-oil-price-102-saudi-east-west-pipeline-restart/) · [ENR 9/17](https://www.enr.com/articles/63668-saudi-aramco-works-to-bypass-damage-on-critical-east-west-oil-pipeline) · [Kpler blog 9/17](https://www.kpler.com/blog/yanbu-pipeline-attack-ripples-across-crude-freight-and-gas-markets) · [Al Jazeera 9/17](https://www.aljazeera.com/news/2026/9/17/from-yanbu-to-sohar-tracking-saudi-arabias-alternative-oil-routes) · [OilPrice 9/18](https://oilprice.com/Latest-Energy-News/World-News/Saudi-Oil-Exports-Rebound-at-Hormuz-While-East-West-Pipeline-Remains-Offline.html) · [Rigzone 9/17](https://www.rigzone.com/news/saudi_pipeline_outage_exposes_limits_of_supply_optionality-17-sep-2026-184640-article/) · [Saxo 9/16](https://www.home.saxo/en-mena/content/articles/commodities/saudi-pipeline-outage-sends-physical-crude-and-diesel-into-scarcity-pricing-16092026) · [KSAT/AP 9/18](https://www.ksat.com/news/world/2026/09/18/iran-says-it-strikes-an-oil-tanker-and-other-mideast-developments/) · [Korea Times/AFP 9/18](https://www.koreatimes.co.kr/world/20260918/iran-says-struck-oil-tanker-in-strait-of-hormuz) · [ABC 9/18](https://www.abc.net.au/news/2026-09-18/houthi-attacks-saudi-oil-world-markets/107168508) · [Rappler/AP 9/17](https://www.rappler.com/world/middle-east/saudis-houthis-exchange-strikes-yemenis-flee-middle-east-war-spreads-september-17-2026/) · [Cyprus Mail/Bloomberg 9/17](https://cyprus-mail.com/2026/09/17/russia-strikes-ukraine-as-kyiv-hits-russian-oil-refinery) · [OGJ 9/6](https://www.ogj.com/general-interest/economics-markets/news/55403398/opec-holds-october-production-targets-steady-as-focus-shifts-to-2027-quotas) · [JWLA-035 PDF](https://lmalloyds.com/wp-content/uploads/2026/09/JWLA-035-Black-Sea.pdf) · WALTER SIG-W-20260917-001/006/007 · ORACLE 9/17 packet · FALCON STATUS 9/17 · HAWK NEXUS_BRIEF 9/17.

## 8. Japan replacement barrels — answer to SAM's routed question (added ~12:3x ET)

**Trigger:** SAM correction packet 9/18 (`aaa9a9f54`): Japan's Middle-East share of crude imports fell from 91–95% (2025-04→2026-03) to **62.6% in Aug-2026** (customs *sokuho*). Verified at SAM's report. **No live BRENT surface carried the ~90% premise** — it sits only in FROZEN `FLOW-BRT-03` / `FLOW-BRT-19` / `KB-BRT-021` (March vintage, read-only by rule). SAM's +22% implied-premium flag is NOT inherited.

**Primary [CONF METI Preliminary Report on Petroleum Statistics, "Import of Crude Oil by Source", newest month Jul-2026, fetched 9/18 with browser UA after a 403 on the default fetcher; basis = crude entering refineries/stockpiling bases/terminals, NOT customs clearance — so it is a different measurement lineage from SAM's 62.6%/59.3%, and it agrees: ME share 58.9% vs customs 59.3% for July].** Six area totals sum exactly to the 11,719,259 kl headline (flat-PDF alignment check passed). METI conversion 1 kl = 6.29 bbl; 31 days.

| Source, Jul-2026 | kl | share | vs Jul-2025 (R.S.) | ≈ mb/d |
|---|---|---|---|---|
| **Total** | 11,719,259 | 100.0% | 117.0% | 2.38 |
| Middle East | 6,897,089 | **58.9%** | 78.6% | 1.40 |
| — Saudi Arabia (Arab-L 3,157,464 · Arab-S-L 47,416) | 3,204,880 | 27.3% | 92.6% | 0.65 |
| — UAE (Murban 2,230,243 · DAS 960,043 · U-Zakum 318,043) | 3,508,329 | 29.9% | 81.6% | 0.71 |
| — Oman | 183,880 | 1.6% | — | 0.04 |
| — **Kuwait** | **0** | 0 | (Jul-25: 784,310, 7.8%) | 0 |
| — **Qatar** | **0** | 0 | (Jul-25: 230,752, 2.3%) | 0 |
| **United States** (WTI-Midland 2,825,294 · Mars 918,512 · WTL 433,515 · T-Horse 159,036) | **4,336,357** | **37.0%** | **460.6%** (Jul-25: 941,425, 9.4%) | **0.88** |
| C&S America (Mexico Isthmus 165,473 · Ecuador Napo 205,436) | 370,909 | 3.2% | 215.8% | 0.08 |
| SE Asia (Viet Nam Bach Ho) | 47,620 | 0.4% | 54.0% | 0.01 |
| Africa (South Sudan) | 46,484 | 0.4% | — | 0.01 |
| Oceania (Australia Pyrenees) | 20,800 | 0.2% | 50.3% | 0.00 |
| Russia (Sakhalin) | 0 | 0 | 0 | 0 |

**Findings.**
1. **The replacement barrels are US crude, and it is one origin, not a basket:** USA 37.0% of July receipts (0.88 mb/d), **4.6× July 2025**, up from 32.3% in June (3,244,831 kl). Everything else non-ME sums to 4.2%. WTI-Midland alone is 24% of Japan's crude intake.
2. **The Hormuz tell inside the ME number:** Kuwait and Qatar are **zero** in July (7.8% and 2.3% a year earlier). The surviving ME barrels are grades with non-Hormuz outlets — Murban/DAS (ADNOC, Fujairah via the ADCOP line) and Arab Light (Yanbu-capable) — plus Oman. ⚠️ Grade ≠ route: Arab Light can load at Ras Tanura too; METI does not carry the load port. But a Japan intake with Kuwait/Qatar at zero is what a Hormuz-routed loss looks like, and **Saudi barrels to Japan are therefore exposed to the Petroline shut** to whatever extent they were Yanbu-loaded — unquantifiable from this table.
3. **Durability — SAM's actual question — is NOT answered by this table.** METI shows origin and grade, not contract form. What can be said: (a) the shift is three months deep (Jun 32.3% → Jul 37.0% US share) and WTI-Midland-led, which is the barrel US Gulf exporters sell on term as well as spot; (b) US crude is a long-haul, freight-heavy substitute, consistent with SAM's implied unit-cost flag rather than refuting it; (c) the reversal test is mechanical: **when Hormuz normalises, the first barrels back are Kuwait/Qatar (zero → non-zero) and the first to go are the marginal US spot cargoes.** ⇒ 62.6% is a **waypoint under a Hormuz constraint**, with the durable floor unknown; carry as SAM states it — a measured current value, not a constant.
4. **Cross-desk:** HAWK (Hormuz-routed grade census — Kuwait/Qatar zero is a clean, primary, monthly instrument for "Hormuz-dependent barrels reaching Asia"), SAM (origin answer + basis caveat), FALCON (Fujairah/ADCOP leg carries Japan's largest surviving ME stream). **August METI table due ~late September/early October** — successor read registered as a dated item; not on the docket as a catalyst (no threshold).

**Sources:** [METI index](https://www.meti.go.jp/english/statistics/tyo/sekiyuso/index.html) → `sekiyuso/pdf/h2j581011e.pdf` (Jul-2026 preliminary), parsed locally with pdfminer; SAM `AGENTS/SAM/reports/2026-09-18_me-crude-substitution.md`.
