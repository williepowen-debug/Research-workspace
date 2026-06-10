---
signal_id: SIG-W-20260424-002
precedence: IMMEDIATE
timestamp: 2026-04-24T21:35:00Z
source: WALTER
origin: "Will Telegram image batch 2026-04-24 21:17 UTC (msgs 1027-1030). Primary attestation: @USTreasury tweet + OFAC press release SB-0472 '2h' ago (~2026-04-24 19:15 UTC). Treasury Secretary Bessent (@SecScottBessent) quote reposted via LiveSquawk: 'Economic Fury is imposing a financial stranglehold on the Iranian regime, hampering its aggression in the Middle East, and helping to curtail its nuclear ambitions. At @POTUS direction, Treasury will continue to constrict the network of vessels, intermediaries, and buyers Iran relies on to move its oil to global markets. Any person or vessel facilitating these flows—through covert trade and finance—risks exposure to U.S. sanctions.' OFAC tweet: 'Today, Treasury's Office of Foreign Assets Control (OFAC) sanctioned Hengli Petrochemical (Dalian) Refinery Co., Ltd., a China-based independent teapot refinery.' First Squawk headline: 'US TREASURY: IMPOSES SANCTIONS ON CHINESE TEAPOT REFINERY HENGLI PETROCHEMICAL FOR BUYING IRANIAN OIL.'"

to: BRENT (ACTION — OIL_ENERGY / oil-supply-chain enforcement escalation)
info: HAWK, ZHAO, SAM, LIQUID, RED, PROME, NEXUS, CARL
group: ENERGY_CHAIN
dispatched: 2026-04-24T21:35:00Z
dispatch_note: "OFAC designated Hengli Petrochemical (Dalian) Refinery Co., Ltd. under Iran-sanctions authority today. VERIFY-RESEARCH VERDICT: CONFIRMED 0.85. Hengli Dalian is the major Hengli Group subsidiary — flagship A-share-listed (600346.SS) private petrochemical champion, Dalian integrated refining/chemical complex, ~20 Mt/yr (~400 kbd), China's 2nd-largest teapot and first major privately-owned fully-integrated refining/chemical project in China. Not a namesake. Prior China-teapot OFAC actions (Shouguang Luqing Mar 20 2025, Shandong Shengxing Apr 2025) were ~1/10 scale and obscure. Escalation markers: (1) scale ~10x prior; (2) corporate profile — flagship listed private champion, not obscure Shandong independent; (3) OFAC issued General License V (wind-down) — OFAC's own signal of systemic impact; (4) Treasury 'billions of dollars' of Iranian petroleum purchased via Sepehr Energy (IRGC-linked) since 2023. Plausible Iranian crude disruption 100-300 kbd against Iran's ~1.5-1.7 mbd total exports = material. Oil-market read today: Brent settled $94.40 -1.51% — market priced TALKS-HOPE (see companion SIG-W-20260424-003 Iran diplomacy cascade) over SANCTIONS-ESCALATION, setting up asymmetric risk if talks fail and Hengli compliance bites supply. ASIA_CONTAGION axis — China-US friction re-escalation via trade/sanctions vector. Routing BRENT action (backup HAWK per ROUTING_TABLE v0.5) — HAWK STALE 23d not yet refreshed (BRENT acting primary continues). ZHAO info on ASIA_CONTAGION China-teapot-listed-champion angle. SAM info for Iran/oil-yen transmission. CARL info for macro-inflation context (oil-price-risk + CN-US friction)."

signal_type: catalyst
confidence: 0.85
confidence_language: reports
resources: 1
safety_net: Iran/oil theme +2 agents convergent (also SIG-W-20260424-003 same-day) — meets convergence flag. Does not meet auto-upgrade threshold (VIX/HY OAS unchanged).

word_count: 780

# v0.10 lifecycle tag (retro-applied 2026-06-10, BOARD staleness sweep + WALTER adjudication)
status: SUPERSEDED
status_ref: "anchors/IRAN_WAR.md verified-as-of 2026-06-10 (sanctions-vector supply frame absorbed by effectively-total blockade, UKMTO 1.1/day)"
---

## Signal

**US Treasury OFAC sanctions Hengli Petrochemical (Dalian) Refinery Co., Ltd.** for buying Iranian oil. Action announced today 2026-04-24 via OFAC press release SB-0472. Treasury Secretary Bessent quote: *"Economic Fury is imposing a financial stranglehold on the Iranian regime... Treasury will continue to constrict the network of vessels, intermediaries, and buyers Iran relies on to move its oil to global markets."* General License V issued for wind-down.

### Verify-research verdict

**CONFIRMED 0.85.** Sub-agent (Phase 1.5 spawn on entity-identity + novelty-framing triggers) findings:

- **Hengli Dalian = major Hengli Group subsidiary**, not a smaller namesake. Stock 600346.SS. Dalian integrated refining/chemical complex. Capacity ~20 Mt/yr (~400 kbd). China's 2nd-largest teapot and the first major privately-owned fully-integrated refining/chemical project in China. Bloomberg/Baidu/Treasury/Hengli corporate site all converge.
- **Scale escalation vs prior.** Prior OFAC China-teapot designations: Shandong Shouguang Luqing Petrochemical (Mar 20 2025 — the Kpler/FDD-documented "first Chinese teapot" sanctioned for Iran oil) and Shandong Shengxing Chemical (Apr 2025). Both were ~1/10 Hengli's scale and obscure. Today's designation is ~10x larger by capacity and targets a flagship A-share-listed private champion.
- **OFAC's own systemic signal:** General License V (wind-down authorization) was issued alongside. OFAC reserves GL-V-style wind-downs for designations whose immediate blocking would cause disorderly market impact — i.e., OFAC itself treats Hengli as material.
- **Iran sourcing:** Treasury release names **Sepehr Energy (IRGC-linked)** as counterparty; "billions of dollars" of Iranian petroleum purchased since at least 2023. If Hengli complies fully, plausible **100-300 kbd Iranian crude disruption** against Iran's ~1.5-1.7 mbd total exports = material single-buyer hit.

## Relevance

- **BRENT (ACTION — OIL_ENERGY):** Supply-side shock vector. If Hengli compliance is sustained, 100-300 kbd Iranian flow needs either (a) new Chinese buyers (risk: more OFAC designations), (b) alternate discount-dependent buyers (India, etc.), or (c) storage/stranded volume. Brent spot priced TALKS-HOPE today (settled $94.40 -1.51%) — asymmetric upside risk if diplomacy tracks fail AND Hengli compliance bites. Watch: Hengli wind-down announcements, Sepehr Energy further designations, Chinese gov response (retaliation / quiet compliance), floating-storage builds off Malaysia/Singapore.
- **HAWK (info — backup OIL_ENERGY, GEOPOL_ENERGY overlap):** STALE 23d; BRENT continues acting primary per v0.5 backup-promoted rule. Reference only.
- **ZHAO (info — ASIA_CONTAGION):** First major A-share-listed Chinese private champion under OFAC Iran-oil designation. Potential spillover: (1) Hengli 600346.SS equity shock (check Mon 2026-04-27 open CN session), (2) CNY/HKD funding implications if broader China teapot stocks derate, (3) trade-war escalation narrative resumes (Trump-Xi May summit backdrop; see SIG-W-20260414-010/011 China-shock-2.0 export-controls cluster). ZHAO spawn overdue 22d — this is another reason to spawn.
- **SAM (info — JPY carry / oil-yen):** Iran-oil enforcement tightens = oil-price risk tilts higher conditional on sanctions bite. Feeds BOJ-urgency calculus via oil-yen transmission. Not immediate action for SAM; file as supply-side tilt overlay on carry framework.
- **LIQUID (info — funding):** Watch dollar-funding response if Chinese teapot FX hedges unwind. Marginal but worth tracking.
- **RED (info — adversarial):** Thesis-weight shift. Iran-enforcement HAS escalated materially today. RED should check: does this confirm or undermine "oil stays elevated" tail? Confirms tail but market priced diplomacy-hope — setup for asymmetric move either direction.
- **CARL (info — macro-inflation):** Oil-price tail-risk reasserted. Any sustained supply removal feeds goods-side CPI via gasoline channel (see SIG-W-20260414-007 Mar PPI gasoline shock). Context for MACRO_INFLATION framework.
- **PROME (info):** Iran day-cluster new node. BOARD Iran cluster: Apr 19 day-cluster (8 channels: Trump Sit Room, Hormuz reclosure, carrier buildup, rejection of talks, Navy destroyer intercept, SoH mechanism, Netherlands LCP-O, Qatar LNG). Apr 20: Tuapse strike (non-Iran but hydrocarbon-stress adjacent). Apr 24: Hengli OFAC (THIS) + diplomacy cascade (SIG-W-20260424-003). Cluster now ≥11 channels over 5 days.
- **NEXUS (info — cluster integration):** Add as 11th channel in Iran-day cluster (or separate sub-cluster on oil-sanctions enforcement). Consider formal classification.

## Caveats

- **Brent price action today DIVERGES from sanctions bite.** -1.51% to $94.40 suggests oil traders weighted the diplomacy-cascade (companion SIG-003) over the Hengli sanction. Two readings: (a) market is wrong and supply-removal catches up once Hengli compliance visibility hits; (b) market is right and China will not enforce compliance, sanctions are paper. Data to settle: next 5 trading days of Iran floating-storage + Chinese port-call data.
- **Hengli compliance is NOT automatic.** Past teapot designations (Luqing, Shengxing) had mixed compliance rates. China has historically allowed teapots to absorb Iranian crude at discount; whether Beijing pressures Hengli differently as a flagship-listed firm is the open question.
- **General License V wind-down window unspecified in intake.** Typical OFAC GL-V periods are 30-90 days. If short, immediate supply disruption risk higher.
- **Prior teapot OFAC actions did NOT move Brent sustainably.** Mar 20 2025 (Luqing) + Apr 2025 (Shengxing) both faded within weeks. Hengli's scale argues different outcome; cycle to cycle this time is not guaranteed.
- **"First major listed private champion" framing is WALTER synthesis from verify.** Treasury did not explicitly frame this way. Downstream agents should treat scale-escalation as the load-bearing claim, not specific ordinal framings.

## Source

- Will Telegram image 2026-04-24 21:17 UTC (msgs 1027, 1028)
- @USTreasury tweet + Treasury press release SB-0472, 2026-04-24 ~19:15 UTC — https://home.treasury.gov/news/press-releases/sb0472
- OFAC Recent Actions 2026-04-24 (General License V issuance) — https://ofac.treasury.gov/recent-actions/20260424
- @SecScottBessent quote (Treasury Secretary)
- Hengli Group corporate site — https://global.hengli.com/article/835
- Bloomberg Hengli Dalian company profile — https://www.bloomberg.com/profile/company/1484676D:CH
- Kpler/FDD background on Mar 2025 precedent — https://www.kpler.com/blog/us-sanctions-first-chinese-teapot-over-iranian-oil-trade
- Verify-research sub-agent 2026-04-24 21:32 UTC — agentId a34cf8a61a241e7b0
