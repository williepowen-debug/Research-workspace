# CORAL — STATUS evidence detail (dashboard · pillars · FL bank exposure)

**SPLIT OUT OF `STATUS.md` 2026-09-02 ~22:2x ET** under the fleet READ-CAP remedy (`AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`, rule 4b — hot/cold split). `STATUS.md` keeps the **hot** one-line-per-channel dashboard and every owed action; this file keeps the **full evidence rows**: every source tag, vintage, basis caveat, publisher-framing warning and reconcile note behind those lines.

**Content = `STATUS.md` lines 102–159 as they stood at commit-time 2026-09-02, VERBATIM and CONTIGUOUS** (SIGNAL DASHBOARD · WHOLE-FLORIDA PILLARS · FL BANK EXPOSURE). Nothing edited, reordered, summarised or dropped.

**Receipt (recomputed at write time over the extracted slice — not copied from a banner, READ_CAP rule 11):** **23,566 B · crc32 `43f1a95a`**

## How to read this file
- **`STATUS.md` is canonical for STATE** (the colour, the current level, what is owed). **This file is canonical for EVIDENCE** (why that level, on what basis, from which vintage). On any disagreement the hot file wins on state; this file wins on provenance — and a disagreement is a defect to fix, not a choice to make.
- **On-demand / sectional read — NOT a boot read whole.** Grep or read the one channel you are working (`grep -n "Citizens" STATUS_DETAIL.md`). It is deliberately outside the boot budget; reading it whole at boot would re-create the breach this split fixed.
- ⚠️ **Rows carry their own dates and several are STALE-marked in place** (Palm Beach condo inventory still Apr; SE-FL vintage $/sf 6/16–7/13; condo-blacklist count vintage Apr-2025). **A row's date is part of the row** — never lift a figure out of here without it.

⚠️ **DATED RE-TRIGGER (READ_CAP rule 7 — this is not a leanness claim):** **re-measure this file and `STATUS.md` at ANY append, or on 2026-10-02, whichever comes first** — `python3 scripts/read_cap_check.py --agent CORAL`. A split that runs once and boasts disarms the next check; the header does not become false by being wrong, it becomes false by being left.

---

## SIGNAL DASHBOARD (rows individually dated; **housing / Citizens / hurricane rows refreshed 2026-08-23**, remainder ≤7/21 EVE)

| Channel | Latest reading | Source / date | Status |
|---------|----------------|---------------|--------|
| FL foreclosure rate (H1-2026, CUMULATIVE) | ⚠️ **RANK-vs-LEVEL QUALIFIER ADDED 8/3 (HOMER publisher-side correction, ACCEPTED):** "#1" is a **RANK** claim, NOT a level claim. **FL's 2025 rate 0.435% is ~31% BELOW its own 2019 level (0.63%); FL ranked #8 as recently as 2023; FY2026 projects ~0.58%, still short of the 0.63–0.72% pre-COVID normal band.** FL is #1 because every other state fell further and stayed lower. Even Lakeland (worst US metro 2025, 0.69%) is below its own 2019 (0.81%). **What is genuinely anomalous is SPEED, not level:** timelines **563d = lowest since 2013** (−13% YoY), REO **+33% H1**. ⚠️ **Four non-convertible bases circulate** (ATTOM annual / H1-cumulative / quarterly / monthly + MBA-style *% of LOANS in foreclosure inventory*) — a FL figure near **3–4% is the loans basis**, never set it against these. **#1 of 50 states, 0.27% (1 in 373 HU), 27,494 properties** (+0.01pp over SC #2; +32.7% YoY filings). **Rate-RANK rose #3(Q1)→#1(H1)** = relative deterioration. **Trajectory (reconciled w/ HOMER, pipeline owner): FL is a LEVEL leader (#1), NOT among fastest-YoY-risers; national flow-GROWTH is DECELERATING (Q1 +26%→H1 +21%; Q2 filings 115,714 < Q1 118,727) while CONVERSION ACCELERATES (avg timeline 563d = lowest since 2013, −13% YoY; REO +33% H1).** High plateau, not a fresh spike. FL metros: **Punta Gorda 0.50% #1-US, Lakeland 0.48% #2-US**, Cape Coral 0.35%, Jax 0.31% NEW, Ocala 0.31% NEW (5 of top-10 US metros). Grid → `GRID_PER_METRO.md`; primary → `sources/ATTOM_H1_2026_foreclosure.md` | ATTOM Mid-Year 2026 (pulled 7/17) | 🔴 (FL's hardest-confirmed distress leg; ATTOM frames NAT'L aggregate as "gradual normalization" off suppressed lows) |
| FL foreclosure rate (May, MONTHLY — window ref) | #1 nationally, 1 in 2,110 HU; starts 2nd-highest. *Monthly ≠ the H1 cumulative above; ~0.047%/mo consistent, no step-change.* | ATTOM May 2026 (pub Jun 11) | 🔴 |
| FL REO completions | H1-2026 national REO 27,983 (+33% YoY); FL Q1 2026 1,014, +108% YoY (was 487) | ATTOM Q1 + Mid-Year 2026 | 🟠 |
| Condo/TH **median SALE PRICE** (statewide, BLENDED — ⚠️ **MIX STATISTIC**) | ⚠️ **THE FLIP DID NOT HOLD. July: median $295K, 0.0% YoY** (June was $305K/+1.7%, the "first flip"; Apr −6.1%, May −1%). Closed sales **8,194, +11% YoY**; new pending +3.8%; **11th straight month of statewide YoY sales gains**. ⚠️ **BASIS LABEL ADOPTED 8/23 (HOMER):** this is a **median SALE PRICE — a mix statistic**, the midpoint of *what transacted*, NOT a price-level trend. **ZHVI (mix-controlled) has all six FL top-50 counties NEGATIVE for June**, and statewide Q2 condo/TH **$1M+ sales ran +29.5%** against total closings of +9.3%. ⭐ **A median that rises because the vintage/assessment-hit low end stops clearing IS the Coral Bleaching mechanism seen through a mix statistic** — same phenomenon as the vintage row below, from the other angle. ⚠️ FL Realtors' own warning: *"June 2025 was a particularly weak sales month."* | FL Realtors July 2026 (pub 8/17, PRIMARY) | 🟠 |
| SE FL vintage (30+yr) condo pending $/sf | **$313, −9%** (was $342 Apr 28) — re-confirmed 7/21, no fresher SE-FL-wide read; NEW Broward cut: vintage asking $246/sf vs **transaction $216/sf** (Jul 13) | Zalewski/Condo Vultures, Jun 16 + Jul 13 2026 | 🟠 |
| Condo inventory (statewide) | ⭐ **7.8 mo (July)** — **FOURTH straight tightening** (Apr 8.9 → May 8.6 → Jun 8.1 → **Jul 7.8**); condo/TH inventory down ~13% YoY. MARCO MAR-08 (>9.0 = distress re-engage) decisively NOT met. ⚠️ **But read it with the price row above and the metro row below: sales +11%, inventory −13%, months-supply falling, price flat-to-down = the market is CLEARING BY CUTTING PRICE**, which is the 🔴 supply-side leg showing up in statewide data. ⭐ **CORAL-canonical — supersedes the 8.1mo June figure HOMER cites; refresh routed to HOMER 8/23.** | FL Realtors July 2026 (pub 8/17, PRIMARY) | 🟡 |
| Condo inventory (Miami-Dade / Broward / PB) | ⭐ **Miami-Dade 12.0 mo, 86 median DOM (July 2026)** — MIAMI REALTORS via HOMER 8/23. ⚠️ **THREE DIFFERENT COMPILERS, LEVELS ONLY — NEVER A DELTA ACROSS THEM** (HOMER 8/23): 12.0 = MIAMI REALTORS · CORAL's prior 12.3 (7/23) · HOMER's earlier 12.9 = Steadily/RESF. **Do not read 12.9→12.3→12.0 as a trend; it is three instruments.** Broward **10.1 mo (June)**, PB **8.2 mo still Apr — STALE-marked**. ⭐⭐ **THE COMPOSITION POINT (HOMER 8/23, accepted): the FL condo story is a METRO story that the statewide figure averages away. Statewide 7.8mo TIGHTENING while Miami-Dade sits at 12.0mo and is the #1 buyer's market in the nation — not in tension, and it locates where FL stress actually is.** | MIAMI Realtors July 2026 via HOMER; Broward/PB June-Apr | 🟠 |
| DOM (Miami-Dade / Broward condos) | **Miami-Dade 85 / Broward 71 days (June 2026)** — REFRESHED 7/23 to a dated primary (supersedes the stale-ish untagged Labros 95/102 ~spring-26). ⚠️ source/measure differs from Labros — do not read the 95→85 / 102→71 gap as a clean MoM decline; treat as a source change to the county-board primary. MARCO May Miami-Dade days-to-sale 106 = different measure, do not merge | MIAMI Realtors June 2026 (pulled 7/23) | 🟠 |
| Special assessments (reserve mandate) | **$25K–$100K/unit typical; up to $400K**; ~40% of owners w/in 3 yrs. **✅ Timing texture STATUTE-VERIFIED 7/23 (primary: FL Stat. 718.112(2)(g) + 553.899):** SIRS default deadline **12/31/25**, BUT §718.112(2)(g) expressly lets an association *required to complete a milestone inspection on or before 12/31/26* complete the SIRS **simultaneously with the milestone** — hard cap "in no event after **December 31, 2026**." PLUS a **2-consecutive-budget reserve-funding PAUSE/reduction to fund milestone repairs, effective through 12/31/28.** → the carried "≤12/31/26 rolling wave into 2027 budgets" read is **CONFIRMED and HARDENED** (pause extends the tail toward 2028), not moved. Reinforces the winter-26/27 composite window (KB ML-CORAL-043/-046). | Zalewski/LongYield 2026 + **FL Statutes 718.112(2)(g) & 553.899 (primary, leg.state.fl.us, pulled 7/23)** | 🔴 (mandate live 1/1/26; compliance tail ≤12/31/26; funding-pause tail ≤12/31/28) |
| Fannie/Freddie condo blacklist + **project-review regime (LIVE TODAY 8/3)** | ⭐ **THE FINANCING CHANNEL IS THE MECHANISM, NOT THE COUNT (reframed 8/3).** **Effective for applications dated on/after 2026-08-03: Limited/Streamlined Review ELIMINATED**; projects **>10 units** → mandatory **Full Review** regardless of down payment, and Full Review interrogates precisely **reserves, deferred maintenance, open special assessments, litigation and master insurance**. **NEW second gate 2027-01-04: required reserve funding 10% → 15%** of budgeted assessment income. ⭐ **Load-bearing arithmetic:** unfunded repairs **>$10,000/unit due within 12 months** flag a project non-warrantable — CORAL's tracked assessments are **$25K–$100K/unit typical, to $400K** = **2.5–40× that threshold**, so the post-Surfside SIRS cohort is non-warrantable **by construction**. Non-warrantable ≠ unfinanceable (Non-QM/portfolio/DSCR survive at higher rate/down-payment) → a **buyer-pool and price effect**. Testable instrument (HOMER, adopted): **widening warrantable-vs-non-warrantable spread in DOM / cash-share / price from Aug onward**, not a uniform statewide move. ⚠️ **SOURCE TIER: PRESS-TIER, primary NOT retrieved** — attributed to Fannie/Freddie **LL-2026-03 (2026-03-18)**, consistent across many independent outlets + HOMER's independent packet, but `singlefamily.fanniemae.com` Cloudflare-403'd (curl + WebFetch) and Selling Guide **B4-2.2-01 still shows pre-change text dated 04/02/2025**. **Open verification item — do not cite as primary.** ⚠️ **Also unverified and cutting the OTHER way:** a search summary of **SEL-2026-05** indicates Fannie *expanded* the project-review **waiver** to ≤10-unit projects, **retired the Florida-specific PERS submission requirement** for new attached projects, and retired the 50% investor-concentration limit — **if true this is partial FL-specific LOOSENING** and the "screw only tightens" framing is wrong. **Effective dates unknown; flagged OPEN, not adopted.** Count leg (unchanged): **~1,438 FL assoc. / 696 tri-county — no precise fresher public count exists (re-searched 7/23; list is non-public by construction).** Aug-2025 data corroborates "more than 1,400 FL developments" (~700 South FL) = stable, not a fresh spike. Policy tightens: **"limited review" ELIMINATED for most condo loans eff Aug 3 2026** (all full review); Mar-2026 GSE transparency/standards update also in train — both widen blacklist-cascade intake without a headcount jump | MPA/Kelley Grant (Apr-2025 count) + Aug-2025 corroboration, re-searched 7/23 [count vintage Apr-2025, STALE-marked; no more-precise figure public] | 🟠 (tightening) |
| Termination / receivership test | *Biscayne 21*: **100%-consent ruling STANDS (FL Sup Ct denied cert 10/14/25 — appellate path exhausted)**; Jan-26: ~$61M restoration order vs Two Roads; late-Jan: NEW **"economic waste" equitable-termination suit** = potential new exit avenue, unresolved. No other FL buildings found in termination/receivership (re-confirmed 7/21) | Bisnow/NBC Miami, pulled 7/21 | 🟡 watch (new suit = live variable) |
| FL property-cat reinsurance | 6/1: **−15-20% risk-adjusted** (Guy Carpenter, confirmed 7/21); 7/1: global property-cat ROL **−16% YTD** (Artemis); **Citizens own placement: net ROL 8.46% vs 11.95% 2025 = −29.2% YoY** | GC Jun 2026 + Artemis/Citizens 6/23 release, pulled 7/21 | 🟢 EASING (soft-market asymmetry per AEOLUS) |
| Citizens policies in force (CANONICAL, scope-resolved 7/21; **REFRESHED 8/23**) | ⭐ **MONTH-END SERIES: 278,196 as of Jul 31 2026** (citizensfla.com primary, pulled 8/23) — personal **273,822** / commercial **4,374** (sums exactly). ⭐ **Separate CURRENT-SNAPSHOT series: 277,902 as of Aug 14 2026** — a DIFFERENT basis, do not mix. Trajectory: 392,689 (1/31) → 278,246 (6/30) → 278,196 (7/31) → 277,902 (8/14) = **−29% in five months, then SIX WEEKS FLAT (−344, −0.12%)**. ⭐ **The flat total conceals a SIGN SPLIT: personal +138 (+0.05%, it GREW) while commercial −188 (−4.1%). Personal-lines depopulation has STOPPED.** ⚠️ 8/18 assumption round #2 **not yet observable in any published series** — the 8/14 snapshot predates it and the 8/31 month-end is unpublished; next observable ≈ early Sep. | citizensfla.com (PRIMARY) 8/23 | 🟠 |
| Citizens commercial / condo-assoc layer | **Commercial Lines +10.4% capped, eff on/after 7/1/26** (⚠️ +18.8% uncapped indication remains un-re-confirmed — lean on capped only). **NEW 7/21 (press-tier):** 91% of FL associations report unexpected 2026 expense increases; master-policy premiums $15-50K/yr small-inland → **$300K-$2M+/yr large-coastal**; insurance = 25-35% of association operating budgets; no clean YoY % found, directionally UP. Carried threads: $1.6B Damac construction-insurance availability block; flood-uninsured tail (FL ~18% of NFIP, $375B *modeled*, landfall-gated); **NFIP authorized through 9/30/26 = next cliff** | Citizens/OIR filings (primary) + association-market press, pulled 7/21 | 🟠 COST AMPLIFIER (diverging worse vs personal) |
| Recent-vintage negative equity | **~18-20% of 2024-vintage financed FL buyers underwater**; 84%+ of underwater loans originated in last ~3.5 yrs; Cape Coral #1 nationally, **10.1%→11.1%** (ICE thru May-26, 2nd source vs Parcl); **2024-vintage cohort 35.4% underwater**; Lakeland 10.8% (2nd major >10%) | Parcl/Lewris + Cotality via SIG-002 (Jun 19); ICE refresh via SIG-702-006 (Jul 2); DEWEY inflection-read via SIG-628-002 (Jun 28) | 🟠 UPSTREAM COLLATERAL |
| Bankruptcy filings | **M.D. Fla #2 / S.D. Fla #6 by volume** (12mo ended 3/31/26), true but population-weighted; FL ~190/100k vs national ~168-173; **+22.2% YoY acceleration**, consumer-led | AOUSC F-2 packet via WALTER SIG-008, Jun 19 2026 | 🟠 CONSUMER CANARY |
| 2026 hurricane season — LIVE (**REFRESHED 8/23**) | ⚠️ **NOT "empty" any more, and the season count moved: 3 named / ZERO hurricanes.** NHC TWO 2:00PM EDT 8/23: **no active Atlantic named storm**; AL95 (400mi SE of Bermuda) 40%/48h+7d tracking **N/NNE well NE of Bermuda, no FL threat**; E-Atlantic wave off Africa **0%/48h, 50%/7d** moving W 15-20mph — *formation ≠ track; at 15-20mph it is still mid-Atlantic at day 7.* **TS CRISTOBAL (AL032026) formed 8/12 while CORAL was dark** — 36.7N 43.0W, 880mi W of the Azores, moving **EAST at 25mph away from the US**, dissipated 8/13; **both first and final advisories: "HAZARDS AFFECTING LAND: None."** Zero FL relevance. **CSU 8/5 held the forecast EXACTLY at 7/8: 9 NS / 4 H / 1 MH / ACE 50 / ACE-W60 25 / NTC 60%** (~40% of the 1991-2020 average; analogs 1965/82/87/97/2009/2015). **NOAA 8/6: 7-13 / 2-6 / 0-2, 75% below-normal.** **CSU 8/19 two-week (Aug 19–Sep 1): below-normal 70% / near 28% / above 2%.** ⭐ **NEW — CSU remainder-of-season MAJOR-hurricane landfall probability: US East Coast incl. FLORIDA PENINSULA 7% (climo 21%) · Gulf Coast FL panhandle→Brownsville 9% (climo 27%) · entire US coastline 16% (climo 43%).** ⇒ **AEOLUS soft-market asymmetry unchanged in kind, now quantified in degree — a 7-9% FL tail onto a −15/−30%-priced market; the PRICING makes it expensive, not the frequency.** | NHC / CSU / NOAA (all PRIMARY) 8/23 | 🟡 |
| Sargassum (SE FL Atlantic) — *2nd-order overlay* | **~38M MT July outlook — CROSSES the >37.5M record-tier bar** (Jun 33.6M → Jul ~38M; carried May 28.9M); ≥2nd-largest belt year on record; USF: SE FL beaching "will continue and likely increase" through July. NOAA SIR SE-FL band not retrievable 7/21 (last: "high," Jun 16). $2.7B/yr *modeled*; NOT an insurance peril, NOT a bank signal. → MARCO owns tourism-$ side | USF Optical Oceanography July outlook (via NOAA NCCOS), pulled 7/21 | 🟠 (record band) |

---

## WHOLE-FLORIDA PILLARS (built 6/19; **pillar 2/3 rows refreshed 8/23**, remainder 7/21 — full detail in `COVERAGE.md` + `research/SWEEP_2026-06-19.md`)

The dashboard above is pillars 1/3/5/10 (condo, insurance, climate). The rest of the state:

| Pillar | Read (as of 2026-06-19) | Signal |
|--------|--------------------------|--------|
| **Migration (7)** | Net domestic **+22,517 (−93% from peak, now #8, 2025 annual Census, STALE — canonical per MARCO commit `a95631b7`)**; intl **+178,674 (2025 annual Census vintage — Census Vintage 2025 state population estimates, components of change; stamped 2026-09-13 per DAEDALUS 9/5 reconcile)**, ~~**−57% YoY** off MARCO-canonical **+411K (2024)** — the two desks CORROBORATE: 178,674/411,000 = −56.5%~~ ⛔ **CORRECTED 2026-09-28 (MARCO packet 9/24, re-verified by CORAL at `NST-EST2025-ALLDATA.csv`): that was a CROSS-VINTAGE comparison — 411K is Vintage 2024's estimate; Vintage 2025 revises 2024 to +283,664 ⇒ same-vintage change = 178,674/283,664 = −37.0%.** V2025 series: 2022 +287,845 · 2023 +333,449 · 2024 +283,664 · 2025 +178,674. The 9/13 'corroboration' checked a baseline against itself (both desks inherited MARCO's cross-vintage base) (−75% projected); **natural change negative**; out-migration ~510K → GA/TX/NC, driven by insurance/assessments/cost. **⚠️ 7/9 documented divergence:** BofA-internal Q1'26 claims Miami(4th)/Orlando(6th)/Tampa(>Chicago) net-negative — different vintage/basis, directionally corroborating but NOT merged into the canonical count (see 7/9 EVENING block #7). *Demand engine failing.* | 🔴 |
| **Tourism/snowbird (8)** | 2025 record 143.3M but Q1'26 **−1.0%**; **Canadian −12.1%** + airline capacity deleted (worst SW-FL); overseas **+8.5% record** offsets. **Orlando leg ELECTRIC (7/21 refresh): TDT June ~$34M record-June +10% YoY, May $32.8M +9.3%, 14-month YoY streak, Mar $42.9M all-time record — Epic Universe driver.** VISIT FLORIDA Q2 not yet published (Q1 stands); no fresh Canadian read. Note 7/21: FL leisure/hosp *added* jobs in June — mildly counter to tourism-collapse, reconcile sent → MARCO | 🟠 (bifurcated: Orlando strong / Canadian-SW-FL weak) |
| **Single-family (2)** | ⚠️ **Median SALE PRICE $425K, +3.7% YoY (July, FL Realtors — DECELERATING from June $432K/+4.9%)**, **4.5mo supply**, closed 23,870 **+5.1%**, new pending **+2.4% (12th straight)**. ⚠️ **BASIS LABEL (HOMER 8/23): a MIX statistic, not a price-level trend** — ZHVI mix-controlled has all six FL top-50 counties negative for June (PB −1.3 / Miami-Dade −1.6 / Duval −1.7 / Orange −2.2 / Hillsborough −2.6 / Broward −3.6), with the luxury tier at +29-38% against total closings +9.3%. ⭐ **🟠 Parcl MSI supply-side leg — FIRED 7/23 (Will-ratified), STOOD DOWN 🔴→🟠 on 2026-09-13** when the 8/23 condition was met on readings #5 (9/2, 3-of-5) and #6 (9/13, 4-of-5), 11 days apart. **9/13 levels: Tampa 7.15 · Punta Gorda 6.59 · North Port 6.27 · Cape Coral 5.91 · Lakeland 6.01.** ⛔ **This leg ONLY — bank rail and overall state untouched, both directions.** ⚠️ **The stand-down fired on a strengthening series (3 of 5 rose; Tampa a series high); breadth failed on Cape Coral alone, 0.09 under.** ⚠️ **Price-cut share 46-51% is an 8/23 figure and is NO LONGER RETRIEVABLE** (Parcl moved it client-side) — do not carry it as current. **Canonical letter → `STATUS.md` OQ §A; full grading record → § "2026-09-13 session evidence" above.** Gulf-Coast-concentrated correction. Builder cross-check: **LGI Q2 FL ASP −6.5% YoY on +14.7% closings** (SEC 8-K primary, via HOMER). | 🟠 |
| **CRE non-condo (4)** | **Condo/residential-specific, not commercial-wide:** Miami office 12.5% (tightest in US); retail/industrial mostly healthy. **New (7/9):** Blackstone $115M JPM refi on FLL W Hotel = trophy-hospitality window open (top-tier only); **MF rent concessions 16.9%** (highest since 2014) bifurcating within-state — Jax/Tampa oversupply-driven rises vs Miami tightening. | 🟢 |
| **Labor (econ)** | **June 4.7% SA (−0.1pp MoM, FIRST decline since 2024; +0.9pp YoY vs Jun-25 3.8%)** — the ~7-straight-rise streak REVERSED (BLS LAUS June 2026, 7/21); still US +0.5pp. FL **+11,100 jobs MoM** (leisure/hosp, health care, transport/warehousing). Construction in ICE labor squeeze (immigrants 37.9% of FL constr.; national construction-hiring rate series-record-low 3.5%, WALTER SIG-704-006); permits −6.1% (Lennar −53%). **Labor leg mildly softened this print — see 7/21 pre-reg block (UNGRADED texture, not a rail move).** | 🟠→🟡-leaning (one-month; 525K unemployed +107K YoY) |
| **State fiscal (9)** | **🔴 Property-tax Amendment 3/HJR 1F CERTIFIED for Nov-3-2026 ballot** (verified primary, DEWEY 7/9 — see EVENING block #1): homestead $50K→$150K(2027)→$250K(2028), ~$8.4B is the FY28-29 terminal figure; non-homestead cap 10%→5% (CRE/rental easing); 5yr new-resident gate (anti-migration by design); **NEW: CRE/MF/business burden-shift headwind** (levy reallocated off homesteaders onto commercial/apartments); muni-fiscal tail (protection fund stripped, S&P warning); **polling now FRAMING-DEPENDENT (UNF 7/20, n=848, ±3.8): 61/32 neutral = passes; 45/47 with budget-impact disclosure = FAILS** (supersedes Sachs 64% as latest); **ballot-language lawsuit escalated to 3 consolidated challenges, hearing 7/29** (rewrite risk, not removal). Budget deficits FY28-29 −$8.1B; condo HB913 relief valves (loans/2yr pause) soften the assessment cascade; DBPR 2026 reserve-study threshold $25,675; no 2026-session SIRS rollback (re-confirmed 7/21). | 🟠 |

**Convergence flags:** (a) SW-FL Gulf Coast = snowbird loss + SF correction + migration drop + recent-vintage negative equity stacking on the *same* metros; (b) household cost-stack (commercial/condo insurance + assessment + HOA + property tax) is both the out-migration *driver* and what the property-tax vote would *partially relieve*; (c) **USCB** is the cleanest condo→bank wire (direct condo-association lender). **Per-metro convergence grid → `GRID_PER_METRO.md` (BUILT 7/17 off the ATTOM H1 print — core SW/Central Gulf Coast hardened, FC channel broadened to NE-FL [Jax/Ocala] but no new multi-channel metro).**

---

## FL BANK EXPOSURE (Q2 WINDOW **CLOSED 7-of-7 BENIGN**, final sync 0-of-≥2; leading-bucket 10-Q detail **closed by REGINALD 8/10, 4-of-4 REVERT**; → REGINALD; expanded watchlist → `FL_BANK_WATCHLIST.md`)

**Headline (8/3 — WINDOW COMPLETE): none of the FL-exposed banks is breaking on credit. Q1 clean, and ALL SEVEN Q2 prints are BENIGN anti-data (CCBG 7/21, BKU 7/22, VLY 7/23-BMO, USCB + AMTB 7/23-AMC, SSB graded 7/24, SBCF graded 8/3). Final synchronization count 0-of-≥2 — empirically closed, not merely mathematically closed. ⭐ The sharpest pre-registered tell (SBCF nonaccrual 3rd rise >$95M) is FALSIFIED: nonaccrual REVERSED to $86.5M with the entire aging ladder falling together. CRE stress remains rate-shock reclassification with high collateral cushions, not loss content — and criticized buckets are accumulating WITHOUT converting across the cohort. USCB condo-assoc wire clean (Garrido 1st print). Zero HOA/condo/association/SIRS disclosure in any of the 7 releases = the wire is structurally unobservable. Rail NOT met, NOT armed; next re-test Q3 ~late Oct, nearer observable = three ~Aug 10-Qs. Prices below = 7/23 ~4:15PM ET EXCEPT the 8/3 live pulls marked as such (detail → `FL_BANK_WATCHLIST.md` rows 4-7).**

| Bank | Px (date) | CET1 | NCO | NPL/NPA | CRE / FL note | Q1 read |
|------|-----------|------|-----|---------|---------------|---------|
| **SSB** (SouthState) | **$100.52 (7/23 intraday, −1.63%)** | — | **9 bps** ($10M) | NPA **0.66%** | Investor CRE 37%/$18.3B; classified $2.5B/3.6% assets, **88% accruing, problem-loan LTV 56% / 98% current** ("little/no loss content"); FL & SC ~$640M production each; watchlist = consumer + SBA, **not FL CRE** | EPS **$2.28 beat**; NIM 3.79%; loan growth 7.5%; PT $115, Buy. **Short thesis broken.** |
| **SBCF** (Seacoast) — **Q2 GRADED 8/3** | **$35.20 (8/3 close, +4.6% off the 7/28 print)** | — | **10 bps** ($3.199M, vs 11bps Q1) | **NPL 0.66%** ($86.5M, **−8.9% QoQ from $95.0M**); NPA/assets 0.42% (was 0.47%); **30-89d $28.2M→$20.1M** | 100% FL; **CRE 230% / C&D 40% of bank-level RBC (UP from 224%/35% — exposure growing under improving credit)**; ACL 1.38% (−1bp); **criticized/classified 2.82%→2.88% (+6bps = accumulating without converting)**; loans +16% ann. organic | **Q2 (7/28): BENIGN 0-of-4 — and the sharpest pre-registered tell FALSIFIED (nonaccrual reversed, whole ladder down). Strictest reading 2-of-4, bar ≥3.** See 8/3 block |
| **BKU** (BankUnited) | **$46.05 (7/23 intraday, +0.24%)** (7/22 close $45.94 post-print −4.43%) | **12.3%** | **11bps ann. Q2** (vs 61bps Q1) | NPA **0.66%** (was 0.79%) | Criticized/classified CRE **−14% QoQ**; ACL 0.91% (+4bps); ACL/NPL 97.1% | **Q2 (7/22): EPS $0.97 miss (cons ~$1.00–1.03) but credit BENIGN — graded 1-of-4 axes, anti-datum.** Tape −4.43% = earnings line, not credit |
| **VLY** (Valley Natl) | **$14.19 (7/23 intraday, −2.31%)** — post-print (graded benign, EPS-miss reaction) | **11.37% (Q2, ↑ from 10.91%)** | **~17 bps Q2** ($22.0M vs $17.5M Q1) | non-accrual **0.88%** ($462.6M, +3bps); NPA $467.8M | **criticized/classified 8.1%→7.3% (DOWN, mgmt-guided)**; 3 collateral-dependent CRE loans →non-accrual ($49.6M, no allocated reserves); ACL 1.16% (−2bps); MF 2.6%; **no FL cut disclosed**; CRE/RBC 329% is Q1 (10-Q pending) | **Q2 (7/23-BMO): BENIGN/does-not-count — 1-of-4 axes, no FL attribution. Adj EPS $0.30 vs $0.31 cons.** See 7/23 block |
| KRE (ETF ref) | **$74.45 (7/23 intraday, −1.52%)** | — | — | — | Above REGINALD's $60 stress line | 🟢 |

*SSB/SBCF/VLY all reported the same pattern: CRE criticized/classified rose on the 2024-era 3%-rate-shock underwriting vs higher rates, but LTVs and payment performance remain intact → reclass, not realized loss. This is the crux of why the bank leg hasn't transmitted.*

---


---

# 2026-09-13 FL enrollment verification (SIG-W-20260911-002 — the primary-source record)

**Ask:** WALTER routed *"Orange County FL schools −7,600 students YoY on ~191,000; district names housing affordability + immigration law."* CORAL↔MARCO must reconcile FL migration figures to ONE number, so the figure had to be established at a primary before publication.

## Sources reached 2026-09-13

| URL | HTTP | Figure? |
|---|---|---|
| `files.smartsites.parentsquare.com/8070/enrollment_summary_09_15_25.pdf` | 200 | ✅ District Total **201,652** (Trad 180,282 + Charter 18,686 + ESE/Alt-Ed 2,684 — ⛔ the third term was missing until MARCO's 9/17 correction; Trad+Charter alone = 198,968); footer verbatim `Monday, September 15, 2025` |
| `files.smartsites.parentsquare.com/6888/enrollment_summary_05_15_26.pdf` | 200 | ✅ District Total **199,368** (Trad 178,409 + Charter 18,000); footer `Friday, May 15, 2026` |
| `files.smartsites.parentsquare.com/6888/fy27_adopted_budget_summary.pdf` | 200 | ✅ Table 1 *Full Time Equivalent Pupil Enrollment FY18–FY27*: **2026-27 = 228,198**, `Annual Increase 1,864`, `% Annual Increase 0.82%`; 2025-26 = 226,335. Board-adopted **2026-09-08** |
| `ocps.net/enrollment-summary` | 200 | index of 182 PDFs, no inline figures |

## Clean negatives (SEARCH-BLOCKED / absent — recorded, not passed over)

- **No 2026-27 enrollment summary exists.** Series ends 5/15/2026. Probed `08_24_26`, `08_25_26`, `08_31_26`, `09_01_26`, `09_02_26`, `09_08_26`, `09_15_26` against both folder ids (`6888`, `8070`) — **all 403**, which is that store's response for an absent file. ⇒ **re-check after mid-Sep for `09_15_26`; that is the first primary on the new year.**
- **FLDOE fully blocked**, curl AND WebFetch: `fldoe.org/` **403** · `…/students.stml` **403** · `2526MembBySchool.xlsx` / `2627MembBySchool.xlsx` **403** · `edstats.fldoe.org` **connection failed (000)**. **No FL Survey 2 figure obtained.**
- **BoardDocs gated:** `ocps.net/134073_2` → 302 → `go.boarddocs.com/fla/orcpsfl/Board.nsf/Public` **403**; tenant guesses `fl/ocps`, `fl/ocpsfl`, `fl/ocpsb`, `fl/orangefl` all 404. **Sept-8 hearing agenda backup not reached.**
- `ocps.net/departments/*` is a **JS-only SPA shell** — `/student_enrollment` and `/budget` returned **byte-identical** bodies (md5 `1c04017d…`, both 374,245 B). ⚠️ **A byte-identical body across two different paths is the tell that a scrape is reading a shell, not content.**

## ⛔ Why the routed figures cannot be published as fact

| Check | Result |
|---|---|
| `201,652 − 7,672` | **= 193,980**, not ~191,000 |
| Is 191,000 a plausible traditional-only base? | **No — it EXCEEDS the traditional-only 180,282** |
| Is FTE differenceable against headcount? | **No — 228,198 FTE > 201,652 headcount** ⇒ different/weighted population (charter + dual-enrollment weighting) |
| Is `−7,672` in any district document? | **No.** Press-attributed to Supt. Maria Vazquez's **10-day count** report to the board (~late Aug 2026); **primary not yet published** |
| Is the causal quote in a district document? | **No.** Press-only. No hit for `hiring freeze`, `8.5 million`, `7,672` in the FY27 budget summary |

⚠️ **Do NOT quote `193,248` or `191,383` from the FY27 budget PDF as enrollment — they are DOLLAR AMOUNTS in financial tables.** A number of the right magnitude in the right document is exactly how a wrong figure gets sourced convincingly.

⭐ **Three distinct instruments, none sharing a basis — the 10-day count, the 9/15 headcount series, and budget FTE.** The routed *"−7,600 on ~191,000 ≈ −3.8%"* divides one instrument's delta by another's base.

⭐ **The fiscal tell that is more interesting than the enrollment number: the FY27 budget was ADOPTED 2026-09-08 — AFTER the late-August 10-day count — and still carries `+1,864 (+0.82%)`.** A budget book projecting growth against an actual count below it is exactly the shape of *"lost more than projected ⇒ $8.5M extra cuts."* **The narrative is coherent; the numbers are not comparable.**

## Inference audit (step 13a) — why pillar 7 does not move

1. **RIVAL MECHANISM, same direction, named by the district itself:** *"expansion of taxpayer-funded vouchers."* A voucher-driven shift from public to private schooling produces a **public-school enrollment decline with ZERO net out-migration.** **Declining birth rates** do the same. ⇒ **the statistic cannot separate migration from substitution, so it is not evidence for the migration pillar.**
2. **What would REFUTE a migration reading:** private/voucher enrollment rising by a comparable magnitude in the same county-year, or FLDOE Survey 2 showing the decline concentrated in grades inconsistent with household relocation.
3. **Confounds by SIGN:** the voucher and birth-rate confounds both cut **against** a migration reading; the immigration-enforcement confound cuts **toward** it. Both directions named rather than stopping at the flattering one.
4. **Unweighted causes:** the district listed four causes and assigned **no share to any**. Assigning one is the reader's inference, not the district's claim.

⇒ **Published as a press-tier claim with a named resolution path (OQ T), NOT as a CORAL finding. Pillar 7 UNCHANGED.**

---

# 2026-09-13 session evidence (GATE-CORAL-MSI-01 reading #6 — the grading record)

**Why here:** `STATUS.md` keeps the 9/13 *grade and obligations*; this is the *evidence* — the raw stamps, the verification legs, the full series and the instrument-integrity finding.

## The pull

| | |
|---|---|
| **Pulled** | 2026-09-13 ~12:0x ET (Sun), direct `curl` + browser UA |
| **URLs** | `https://www.parcllabs.com/research/markets/fl/{tampa,punta-gorda,north-port,cape-coral,lakeland}/metro` |
| **HTTP** | **200 on all five** (44,127 / 44,258 / 44,241 / 44,241 / 44,189 B) |
| **Page self-stamp** | **`Updated: 9/13/2026`** — identical verbatim string on **all five** pages |
| **Prior stamp (reading #5)** | `Updated: 9/3/2026` ⇒ **the vintage CHANGED; this is a new observation, not a re-read of the same one** |

⚠️ **Stamp-extraction gotcha, recorded because it fails silently:** the rendered DOM is `Updated: <!-- -->9/13/2026`. A naive `grep -o 'Updated:[^<]*'` stops at the intervening HTML comment and returns **an empty stamp** — a false negative that would read as "the page carries no date." The date must be read across the comment node.

## Per-metro readings and verification

| Metro | MSI 9/13 | `<title>` | `og:description` | JSON `"value"` | 3-way agree | vs 9/2 |
|---|---:|---:|---:|---:|:--:|---:|
| Tampa | **7.15** | 7.15 | 7.15 | 7.15 | ✅ | +0.14 |
| Punta Gorda | **6.59** | 6.59 | 6.59 | 6.59 | ✅ | +0.07 |
| North Port | **6.27** | 6.27 | 6.27 | 6.27 | ✅ | −0.02 |
| Cape Coral | **5.91** | 5.91 | 5.91 | 5.91 | ✅ | −0.04 |
| Lakeland | **6.01** | 6.01 | 6.01 | 6.01 | ✅ | +0.04 |

**Every value read three independent ways from the fetched HTML; all agree to the hundredth on all five metros.**

## Full series — 7/8 → 9/13 (six readings)

| Metro | 7/8 | 7/23 | 8/3 | 8/23 | 9/2 | **9/13** |
|---|---:|---:|---:|---:|---:|---:|
| Tampa | 6.90 | 6.96 | 6.99 | 7.05 | 7.01 | **7.15** ⭐ series high |
| Punta Gorda | 6.90 | 6.82 | 6.75 | 6.58 | 6.52 | **6.59** |
| North Port | 6.45 | 6.45 | 6.43 | 6.39 | 6.29 | **6.27** |
| Cape Coral | 6.12 | 6.20 | 6.07 | 6.02 | 5.95 | **5.91** |
| Lakeland | 6.09 | 6.09 | 6.04 | 6.03 | 5.97 | **6.01** ⭐ re-crossed above |
| **Breadth >6.0** | 5/5 | 5/5 | 5/5 | 5/5 | **3/5** | **4/5** |

## The grade, leg by leg against the frozen 8/23 letter

| Leg of the letter | Required | Observed 9/13 | ✅ |
|---|---|---|:--:|
| Breadth, reading 1 | <5-of-5 | 9/2 = **3-of-5** | ✅ |
| Breadth, reading 2 | <5-of-5 | 9/13 = **4-of-5** | ✅ |
| Spacing | **≥10 days** after reading 1 | **11d** observed (9/2→9/13); **10d** by page vintage (9/3→9/13) — ≥10 on **both** clocks | ✅ |
| Consecutive | no countable reading between | none taken or logged: KB ends **ML-CORAL-074** (9/2); no CORAL commit between `53dc298b6` and this session | ✅ |

**⇒ ALL FOUR LEGS MET ⇒ 🔴→🟠, SUPPLY-SIDE PRICE-DISCOVERY LEG ONLY.**

## ⚠️ Instrument integrity — the listings field (ML-CORAL-079)

| | 9/2 | **9/13** |
|---|---|---|
| Active-listing count in server HTML | **absent** (SEARCH-NOT-FOUND) | **present, renders `Total Active Listings · 0`** on all five |
| Backing numeric field in payload | none | **none** — zero matches for any `*listing*` numeric key |
| Truth | unknown | **still unknown.** Tampa had **26,801** on 8/23; a true 0 is impossible |

⇒ **A hydration placeholder, not a measurement.** ⛔ **Never carry "0 listings."** The absence got **worse by becoming present**: a field that was honestly missing is now dishonestly filled, so a downstream presence/completeness check **passes** while the value is fabrication. Price-cut share likewise absent (prose only, no number). **This is the discriminator the MSI inference audit needs** — see OQ L.

---

# 2026-09-02 session evidence (moved here from `STATUS.md` at write time, VERBATIM — read-cap rule 4b)

**Why here:** `STATUS.md` keeps the 9/2 *findings and obligations*; this is the *evidence* behind them — the MSI per-metro series, the Freddie methodology quote, the four-perimeter table and the instrument-integrity limits. **Receipt: 9,146 B at extraction.**

## 9/2 (Wed) — MSI BREADTH BREAKS (reading 1 of 2) · THE STATEWIDE SIGN QUESTION DISSOLVES · PEAK SEASON WITH ZERO HURRICANES — READ FIRST

**1. 🔴 GATE-CORAL-MSI-01 — reading #5, and breadth BREAKS for the first time since the leg fired.** Parcl metro pages pulled direct 2026-09-02 ~22:0x ET; **all five pages self-stamp `"Updated: 9/3/2026"`** (recorded verbatim — the stamp is one day AHEAD of the ET pull date, consistent with the site stamping in UTC; 22:0x ET = 02:0x UTC 9/3).

| Metro | MSI 9/2 | vs 8/23 | >6.0? |
|---|---:|---:|:--:|
| Tampa | **7.01** | 7.05 → −0.04 | ✅ |
| Punta Gorda | **6.52** | 6.58 → −0.06 | ✅ |
| North Port | **6.29** | 6.39 → −0.10 | ✅ |
| **Cape Coral** | **5.95** | 6.02 → **−0.07** | ❌ |
| **Lakeland** | **5.97** | 6.03 → **−0.06** | ❌ |

**⇒ 3-of-5 >6.0. Breadth condition NOT met.** Full series (7/8 → 7/23 → 8/3 → 8/23 → 9/2): Tampa 6.9 → 6.96 → 6.99 → 7.05 → **7.01** (rolls over after 4 straight rises) · Punta Gorda 6.9 → 6.82 → 6.75 → 6.58 → **6.52** (−0.38 cumulative) · North Port 6.45 → 6.45 → 6.43 → 6.39 → **6.29** · Cape Coral 6.12 → 6.2 → 6.07 → 6.02 → **5.95** · Lakeland 6.09 → 6.09 → 6.04 → 6.03 → **5.97**. **ALL FIVE now fall together — the first reading with no riser.**

⛔ **GRADED ON THE FROZEN LETTER, NOT RE-FITTED: this is sub-threshold reading ONE of the two the rule requires. The leg stays 🔴. The clock starts. Nothing else changes in either direction.** The 8/23 rule anticipated exactly this and the anti-noise leg is doing exactly its job — Cape Coral and Lakeland went sub-threshold by **0.05 and 0.03**, which is the rounding-error de-fire the spacing leg exists to refuse. **Second reading must be ≥10 days after this one ⇒ earliest 2026-09-13** (taken off the **9/3** page vintage, not the 9/2 pull, per the rule's own symmetry note that spacing moves toward MORE, never less).

⚠️ **Instrument-integrity note, stated as a limit rather than passed over:** the per-metro **active-listing counts and price-cut shares were NOT retrievable this reading** — Parcl now renders them client-side (server HTML shows `Total Active Listings · 0` and `Loading…`), so prior readings' companion figures (e.g. 8/23 Tampa 26,801 listings / 51% cutting) have **no 9/2 counterpart**. **SEARCH-NOT-FOUND, not zero.** The MSI values themselves are **VERIFIED twice independently** — the rendered page and the raw `<title>` element of the curl'd HTML agree to the hundredth on all five metros. ⭐ **The graded quantity is intact; only its context is missing.** Do not carry "0 listings" anywhere.

**2. ⭐⭐ THE THREE-STATEWIDE-SIGN QUESTION IS RESOLVED — and the answer is that there was never a sign conflict, because one instrument cannot see condos at all.** PROME routed HOMER's FMHPI FL +1.68% SA (July) on 8/31 as *"a THIRD statewide sign"* against ZHVI-negative and CORAL's median. **Checked at the Freddie primary, methodology verbatim:**

> *"Data are limited to single-family detached and townhome properties that are financed by first-lien conventional and conforming loans. The FMHPI further excludes planned unit developments (PUDs), condominium, and cooperative properties."*

⇒ **FMHPI is blind to the Florida condominium stock by construction.** It cannot corroborate, contradict, or bear on CORAL's core subject. **Composition before contradiction — and here composition dissolves the contradiction entirely.** Naming the three perimeters side by side:

| Instrument | Basis | Geography | Property types | Vintage | Reading |
|---|---|---|---|---|---|
| **FMHPI FL** | Repeat-sales, **constant-quality**, SA | **Statewide** | SF-detached + townhome; **condo/co-op/PUD EXCLUDED**; conforming conventional only | **Jul 2026** | **+1.68% YoY** |
| FL Realtors SF median | **Mix statistic** (midpoint of what transacted) | Statewide | Single-family, all financing | Jul 2026 | **+3.7% YoY** |
| FL Realtors condo/TH median | **Mix statistic** | Statewide | Condo/townhouse, all financing | Jul 2026 | **0.0% YoY** |
| ZHVI, FL counties in the US top-50 | Mix-controlled, **full stock** (transacted or not) | **County subset — NOT statewide** | All types | **Jun 2026** | every one **negative YoY** |

⭐ **Once the perimeters are named there is no three-way disagreement.** On **single-family** both statewide instruments point the **same way** (+1.68% constant-quality, +3.7% mix) — the gap between them is the mix premium, not a sign conflict. The **condo** leg (0.0%) has **no constant-quality counterpart in hand at all**. The **ZHVI** leg is a **county subset on a different month** and was never a statewide sign — it belongs with the metro cut, not in this comparison.

⛔ **VINTAGE CORRECTION owed back to PROME/HOMER:** the routed packet set FMHPI July against *"your median +4.9%"*. **+4.9% is the JUNE single-family figure.** CORAL's July SF median is **+3.7%** (FL Realtors July, pub 8/17, PRIMARY). The comparison as routed was July-vs-June; corrected like-for-like the gap narrows from 3.2pp to **2.0pp**.

⭐ **THE ONE FIGURE THE DESK PUBLISHES** *(the one-figure rule binds per METRIC; "FL house prices" and "FL condo prices" are two metrics, and collapsing them to one number would be the error, not the fix)*:
> **FL statewide single-family, constant-quality: `+1.68% YoY SA, July 2026` (FMHPI FL, Freddie issuer master file).** Cite the perimeter with it — **excludes condo/co-op/PUD, conforming conventional only.**
> **FL statewide condo/townhouse: `$295,000 median, 0.0% YoY, July 2026` (FL Realtors, PRIMARY), published EXPLICITLY as a mix statistic** — because **no constant-quality statewide FL condo index is in hand.** That absence is now a named gap with a resolution path (below), not a silence.

⚠️ **And the caveat that matters most for this desk, because it cuts at CORAL's own mechanism:** FMHPI covers **only conforming conventional financed** transactions. FL cash share was **51.0% in July** (FL Realtors) — so **FMHPI sees under half the FL market by count, and the half it cannot see is precisely the cash channel CORAL identified as the price-discovery mechanism** (ML-CORAL-049: cash end-user capitulation-clearing marks collateral DOWN via appraisal comps). **A rising FMHPI is therefore not evidence against the capitulation-clearing read — the instrument is structurally blind to it.** `[[finding_instrument_measures_a_superset_of_the_thesis_subject]]` in its mirror form: here the instrument measures a **subset**, and the excluded part is the thesis.
⛔ **Nothing in this reconcile changes a colour, a gate, a band or the thesis.** It settles which number the desk publishes and on what basis. **No threshold set or moved.**

**3. Hurricane — peak season, and the tail keeps NOT arriving.** NHC Tropical Weather Outlook **8:00 PM EDT Wed Sep 2 2026** (PRIMARY): *"Tropical cyclone formation is not expected during the next 7 days."* One system in the basin — **TD Edouard, inland over eastern Texas**, final NHC advisory issued, handed to WPC as a flood threat. **Season = 5 named / ZERO hurricanes** (NHC 2026 archive: Arthur · Bertha · Cristobal · Dolly · Edouard — **all five archived as Tropical Storm**). Two formed while dark: **Dolly** (~8/28, degenerated to an open wave near the Leewards) and **Edouard** (TX landfall). ⇒ **NO FL LANDFALL. The 🔴 insurance flip did NOT fire — graded on its own letter, which is landfall-gated; no advisory names Florida.** ⭐ **A 7-day no-formation outlook at the ~9/10 climatological peak, with zero hurricanes through five named storms, HARDENS the AEOLUS soft-market asymmetry** — CSU's remainder-of-season **7% FL-Peninsula / 9% FL-panhandle-Gulf** major-landfall probabilities are being run down by the calendar onto a market priced −15/−30%. **The pricing makes the tail expensive, not the frequency.**

**4. Mail DRAINED 7-of-7** (CREED · RED · DAEDALUS ×2 · PROME ×3) — dispositions in `board_log.tsv`, files in `inbox/processed/`. Substantive outcomes: **pillar 4 stays 🟡 and its REASON is rewritten** on CREED's evidence (the feed is structurally thin, not stale — CREED's monthly PDF class has **no geographic layer at all**, so "FL-metro CMBS delinquencies" is **permanently undeliverable** from it; a 🟢 there would have re-created the exact defect the 🟡 was raised for) · **RED's two rows CONFIRMED** on CORAL's word · **DAEDALUS mtime flag ENCODED** · **WQ-86 join rule wired** into the fire procedure.

**5. READ-CAP remedy EXECUTED** (DAEDALUS P1, Will-ruled 8/28). STATUS was **95,195 B = 292% of the 32,550 B budget / 175% of the 54,250 B cap** — over the cap, a boot Read returns a **partial file with no error**, and what vanishes is whatever sits LAST: **this desk's Will-facing BOTTOM LINE**. Remedy = **hot/cold split + rotation**, verbatim, crc-verified by recomputation. **Obligation audit run before and after: 34 owed actions/watches in, 34 out** — audited by OBLIGATION, not by byte, because a byte check passes while an owed action silently disappears.

---


---

# OPEN QUESTIONS — full text as at 2026-09-02 (elaboration; the OWED TABLE in `STATUS.md` is canonical for WHAT IS OWED)

⚠️ **`STATUS.md` carries the canonical MSI stand-down letter and the owed-item table. This copy is the reasoning behind each item — resolution paths, prior failed routes, discriminators. On any disagreement about WHAT IS OWED, `STATUS.md` wins.** Receipt: 8,279 B at extraction.

## OPEN QUESTIONS / NEXT SESSION

**A. 🔴 [RULED 2026-08-23 — WILL, IN-SESSION, VERBATIM "accept" — CANONICAL LETTER LIVES HERE]** The 🔴 supply-side price-discovery leg fired 7/23 on a Will-ratified breadth+sustain condition with **no falsifier ever registered**. That gap is closed. **This is the canonical text; `PROME/GATES.tsv` `GATE-CORAL-MSI-01` is a POINTER — on any disagreement, this surface wins and the GATES row is the copy to fix (PAT-006).**

> ### 🔴 MSI SUPPLY-SIDE LEG — REGISTERED STAND-DOWN CONDITION (Will-ruled 2026-08-23, adopted unamended)
> **Breadth <5-of-5 FL metros with Parcl MSI >6.0, on TWO CONSECUTIVE readings ≥10 DAYS APART ⇒ 🔴→🟠.**
>
> ⛔ **BOTH LEGS BIND — neither is decorative:**
> 1. **A single sub-threshold reading does NOT stand the leg down.** One reading below 5-of-5 changes nothing; it starts a clock, it does not ring a bell.
> 2. **Two readings closer than 10 days do NOT count as two.** The second reading must be **≥10 days after** the first sub-threshold reading. A pair taken 3 days apart is ONE observation for this purpose, however many times the pages are pulled.
>
> ⭐ **The spacing is the ANTI-NOISE leg and it is the load-bearing one.**
> **Scope, unchanged in both directions: the SUPPLY-SIDE PRICE-DISCOVERY LEG ONLY.** The bank-transmission rail and CORAL's overall 🟠 state are untouched whether this fires or stands down.
> **Symmetry note (why this form):** the leg FIRED on persistence (breadth sustained ~15d), so it stands down on persistence too. Any future amendment should move the spacing **toward more**, never less.

**⏱️ CURRENT STATE UNDER THE RULE — THE CLOCK IS RUNNING (started 2026-09-02).**
- **Sub-threshold reading 1 of 2: 2026-09-02** (page vintage self-stamped `"Updated: 9/3/2026"`) — **3-of-5 >6.0**; Cape Coral 5.95, Lakeland 5.97.
- **Reading 2 of 2: NOT BEFORE 2026-09-13** (≥10 days after the 9/3 page vintage — the later of the two candidate dates, per the rule's own "toward more, never less").
- **Leg state today: 🔴 HOLDS.** ⛔ A pull before 9/13 is **the same observation** and cannot be counted, however many times the pages are fetched.
- **If reading 2 is also <5-of-5 ⇒ 🔴→🟠 on the supply-side leg ONLY.** If reading 2 is back to 5-of-5, the clock **resets** and the next sub-threshold reading starts a fresh one.
- ⚠️ **Do not re-fit at the second reading.** The rule was written before the data turned; grade it as written.

**B. [CARRIED] The Miami discriminator — needs a SUBMARKET cut before it can discriminate.** Miami for-sale loosest in the nation (154% more sellers than buyers) while rental concession share (28.6%) is among the tightest — the signature of an **ownership-specific** cost shock rather than demand loss. **But a supply-composition reading is at least as good** (concessions concentrating in Brickell/Downtown/Edgewater new-build while ~7% MF vacancy means older stock is not discounting), and **HOMER weakened its own hypothesis.** ⇒ **A QUESTION with a named resolution path: a submarket-level concession cut.** Metro levels **single-sourced**; only the *relationship* is second-sourced. Coordinate HOMER (Miami metro theirs, statewide mine).

**C. [SHARPENED 9/2 — the search is CLOSED, the question is not] The Orlando/FL hotel portfolio.** ✅ **CREED independently re-extracted the Trepp primaries (8/27) and confirmed the trace exactly** — a second independent read, so the relayed claim is upgraded to VERIFIED. ⛔ **Identity now ruled out STRUCTURALLY, not by a failed search:** every monthly Delinquency Report is 5 pages, exactly two tables, **both national, neither geographic**; the July Special Servicing report has **zero** geographic mentions. **Close "is it in Trepp's monthly?" permanently.** Only path = **CMBS deal-level remittance (Trepp/DBRS)**. **July names no FL asset ⇒ no re-default through July** *(limit: one outside the top five is invisible here)*. ⚠️ **CREED's noise caveat ADOPTED, and it cuts against over-reading this:** national lodging DQ moves **|MoM| mean 72bp, max 137bp (n=6)**, so the FL-cure month's −79bp is **1.10× typical — and Mar→Apr was ALSO −79bp with no FL asset named.** ⇒ **The portfolio is identifiable because Trepp NAMED it, not because the move was unusual; one named asset in four months is NOT evidence FL drives the national series.** Does not reopen the bank window.

**D. [CARRIED] The warrantability spread cannot be measured yet.** Earliest honest read **~Oct–Nov** (August-application loans have not closed); anything earlier is anticipation, not measurement. **Sub-question owed: how many FL associations already carry a per-unit master-policy deductible >$50,000?** — a direct, countable insurance→warrantability wire CORAL owns both ends of. **Second GSE gate dated 2027-01-04: required reserve funding 10% → 15%.** ⚠️ **SEL-2026-05 loosening (≤10-unit projects, FL PERS retirement): effective dates still UNKNOWN — flagged OPEN, not adopted.**

**E. [CARRIED — OLDEST UN-WORKED ITEM] Amendment 3 ruling — still unlocated.** Judge **David Frank, 2nd Judicial Circuit (Leon County)** heard three consolidated ballot-language challenges **7/29**, did not rule from the bench, set an August briefing deadline whose date has **never been confirmed**. ⛔ **Pre-registration ML-CORAL-042 stays UNRESOLVED — do not score any branch.** Remedy sought is a **rewrite, not removal**. ⚠️ **The news-outlet path has now failed three times (8/3, 8/23, not re-tried 9/2) — try COURT-DOCKET routes, not outlets.** Feeds falsify criterion 6 and the **Nov 3** prior.

**F. [CARRIED] Ocala June-2026 metro UR — still owed.** BLS bot-blocked, FRED 403, deptofnumbers retired; a promising article was a **June-2025 decoy**. **Next route: FloridaCommerce LMS primary** (`lmsresources.labormarketinfo.com`). ⭐ Baseline salvaged: Marion County's *normal* June shape is **+0.6pp**, so a ~+0.5-0.6pp rise is **not** signal.

**G. [CARRIED] Citizens 8/31 month-end — OWED NOW, and it is the first series that can show the 8/18 assumption round.** Base **278,196 (7/31)**. ⭐ **Watch the personal/commercial SPLIT, not the total.**

**H. [CARRIED — BUILD BEFORE 11/15] Bankruptcy tripwire instrument.** Ch.7 per capita M.D.+S.D. Fla (AOUSC quarterly), tripwire **>~230/100k**. ⛔ **Falsify criterion 5 scored UNGRADED (0) because it went untracked June→August. An unobserved criterion is a defect, not a pass** — with no instrument by 11/15 it scores 0 again for the same reason.

**I. [CARRIED] Receivership/termination count** — no FL building in active termination/receivership beyond *Biscayne 21*; NEW variable = Two Roads' "economic waste" equitable-termination suit, unresolved.

**J. [CARRIED] The condo price-band test — required before the composition claim can EVER go load-bearing.** Pull **condo unit sales by price band, sub-$300K especially — UNITS, never SHARE** (a high-end surge cuts the low end's share with zero low-end units lost, so a share test confirms the thesis whether or not it is true). Not in the monthly summary; a separate report.

**K. ⭐ [NEW 9/2] No constant-quality statewide FL CONDO price index is in hand — and that gap is now load-bearing.** FMHPI **excludes condos by construction**, so the desk's only statewide condo price signal is a **mix statistic** (FL Realtors median). Every composition argument this desk makes about condos therefore rests on an instrument that cannot control for composition. **Resolution paths to test, in order:** FHFA **expanded-data** HPI (includes condos in some series) · Case-Shiller condo indices (Miami-area, not statewide) · FL Realtors band-level cut (OQ J). **Until one lands, publish the condo median AS a mix statistic and never as a price-level trend.**

**L. ⭐ [NEW 9/2] The Parcl sub-metrics went client-side.** Active-listing counts and price-cut shares are no longer in the server HTML. The MSI grade is unaffected (title element), but **the companion context is gone** and the second reading (≥9/13) will face the same wall. **Owed: find a retrieval route for listings/price-cut share before 9/13**, or record their absence explicitly on that reading rather than silently.

---


---

# BOTTOM LINE — full text as at 2026-09-02 (pre-compaction, verbatim)

## BOTTOM LINE

Florida is repricing as the "Coral Bleaching" mechanism predicts, and the call stays **🟠 overall with the supply-side price-discovery leg 🔴** — but **the leg's own falsifier started running today**, and the honest restatement of the split is unchanged from 8/23: **VOLUME is improving, PRICE is not.**

**The single most important thing that happened: the 🔴 leg's breadth broke for the first time since it fired, and the rule held.** All five metros fell together — the first reading with no riser — and Cape Coral (5.95) and Lakeland (5.97) crossed below 6.0 by **0.05 and 0.03**. ⭐ **That is precisely the rounding-error de-fire the 8/23 anti-noise leg was written to refuse, and it refused it: the leg stays 🔴 and a second confirming reading cannot legally arrive before 9/13.** Asking Will for a pre-registered falsifier ten days before the data turned is the reason today was a mechanical grade rather than an improvisation. ⚠️ **Do not pre-judge the second reading in either direction** — three metros remain comfortably above (Tampa 7.01, Punta Gorda 6.52, North Port 6.29), and a single metro recovering 0.05 resets the clock entirely.

**The statewide price question turned out to be a perimeter question, and that dissolved it.** Of the three "statewide signs," **FMHPI excludes condominiums by construction** (verbatim at the Freddie primary) so it never had standing on CORAL's subject, and **ZHVI is a county subset on a different month** — never statewide. What remains is a single-family pair that **agrees in sign** (+1.68% constant-quality, +3.7% mix) and a condo median at 0.0% with **no constant-quality counterpart in existence at this desk** — the more useful output being that **new named gap**. ⚠️ **The sharpest caveat cuts at my own mechanism, so it is stated loudest: FMHPI covers only conforming conventional financed sales while FL cash share is 51% — it is structurally blind to the cash capitulation-clearing channel this desk says is doing the price discovery.** A rising FMHPI is not evidence against that read; it is an instrument that cannot see it.

**What did not move, and it is still the thing that matters. Bank-loss transmission remains unconfirmed** — Q2 closed **7-of-7 benign**, the sharpest pre-registered tell **falsified**, and REGINALD's leading-bucket close (4-of-4 REVERT) graded the last owed observable. Rail **NOT met, NOT armed**; next re-test **Q3 ~late Oct**. **Household and collateral stress must still not be read as banks breaking.**

**The hurricane tail keeps not arriving, and that is now a positioned fact rather than a wait.** Five named storms, **zero hurricanes**, no FL landfall, and a **7-day no-formation outlook at the climatological peak.** The residual is a low-probability landfall onto a −15/−30%-priced market — **the pricing, not the frequency, is what would make it expensive.**

⚠️ **Carried as gaps, not findings:** the **Miami discriminator** (a question until a submarket cut exists) · the **FL hotel portfolio's identity** (search now closed structurally — deal-level remittance only — and CREED's noise check says one named asset in four months is not a signal about Florida) · the **Amendment 3 ruling** (unlocated on three attempts; switch to court dockets) · the **bankruptcy instrument** (unbuilt, and criterion 5 scores 0 again on 11/15 if it stays that way).

**Next:** **≥9/13 — the MSI second reading, the one that can stand the leg down** (do not pull earlier and count it) · **Citizens 8/31 month-end, owed now — watch the personal/commercial split** · **~9/10 peak hurricane season** · **~9/17 FL Realtors August** — does the condo median go negative after 0.0%, and does supply tighten a 5th time? Read price and volume as **separate legs** · **9/8 Canadian counter-tariffs** (MARCO owns the fold) · **~Oct–Nov: first honest read on warrantability friction** · **late Oct: Q3 bank prints** · **Nov 3 Amendment 3**, still the biggest two-sided forward variable · **Sun Nov 15 — the pre-registered falsify grade** (baseline 1.5 of 6; ⛔ do not re-derive the decision rule and do not reword a criterion).

*CORAL: tracking the bleaching of Florida's condo market. Evidence detail → `STATUS_DETAIL.md` · session history → `archive/STATUS_SESSIONS_20260721-20260823.md` · prior dashboard → `workbook/STATUS_archive_20260325.md`.*

---

# 2026-09-13 STATUS hot-surface blocks — ROTATED OUT OF `STATUS.md` 2026-09-28 (read-cap rule 5 remedy)

**Why:** `STATUS.md` stood at 32,493 B = 100% of the 32,550 B budget at the 9/28 boot (DAEDALUS PR#6 ask: rotate to <22,785 B, not to the band). **Content = the five blocks below, VERBATIM from `STATUS.md` at commit `7035b2b3b`**, each headed with its source line range. Nothing edited, reordered or summarised. **The Will-ruled MSI-01 letter (STATUS OQ §A, the quoted block) was NOT rotated — it stays canonical in `STATUS.md`.**

**Receipt (recomputed over the concatenated extracted segments at write time):** **17,678 B · crc32 `5ff2d9aa`**

## [rotated] 9/13 READ-FIRST block — STATUS.md L10–L42 @ 7035b2b3b

## 9/13 (Sun) — 🟠 MSI LEG STANDS DOWN ON A RULE THAT FIRED AGAINST THE DATA'S DIRECTION — READ FIRST

⭐ **Full evidence — per-metro series, verbatim stamps, the triple-verification legs, the listings-placeholder finding → `STATUS_DETAIL.md` § "2026-09-13 session evidence".** *(The 9/2 session block that stood here is preserved VERBATIM at `STATUS_DETAIL.md` § "2026-09-02 session evidence".)*

**1. 🟠 GATE-CORAL-MSI-01 — reading #6. The stand-down condition is MET.** Parcl metro pages pulled direct 2026-09-13 ~12:0x ET, HTTP 200 on all five; **all five self-stamp `Updated: 9/13/2026`** (verbatim) — a **NEW** vintage vs the 9/3 pages of reading #5, so this is a new observation, not a re-read.

| Metro | MSI 9/2 | **MSI 9/13** | Δ | >6.0? |
|---|---:|---:|---:|:--:|
| Tampa | 7.01 | **7.15** | **+0.14** | ✅ |
| Punta Gorda | 6.52 | **6.59** | +0.07 | ✅ |
| North Port | 6.29 | **6.27** | −0.02 | ✅ |
| **Cape Coral** | 5.95 | **5.91** | −0.04 | ❌ |
| **Lakeland** | 5.97 | **6.01** | **+0.04** | ✅ |

**⇒ 4-of-5 >6.0. <5-of-5 ⇒ SUB-THRESHOLD READING 2 OF 2.**

⛔ **GRADED ON THE FROZEN 8/23 LETTER, NOT RE-FITTED.** All three legs check out independently: reading 1 (9/2) 3-of-5 **<5-of-5** ✅ · reading 2 (9/13) 4-of-5 **<5-of-5** ✅ · spacing **11 days** by observation and **10 days** by page vintage, both **≥10** ✅ · **CONSECUTIVE** — no MSI reading was taken or logged between 9/2 and 9/13 (KB ends at ML-CORAL-074; no CORAL commit between) ✅. **⇒ 🔴→🟠 ON THE SUPPLY-SIDE PRICE-DISCOVERY LEG ONLY.**

⛔⛔ **SCOPE, RESTATED BECAUSE THIS IS THE CELL SOMEONE ACTS ON: CORAL's OVERALL STATE STAYS 🟠 AND THE BANK-TRANSMISSION RAIL IS UNTOUCHED — NOT MET, NOT ARMED, in BOTH directions.** A supply-side leg standing down is **not** a Florida all-clear and is **not** evidence about bank transmission. Next bank re-test is still **Q3, ~late Oct**.

**⚠️⚠️ THE FINDING THAT MATTERS MORE THAN THE GRADE: the rule stood the leg down while its own underlying series moved the OTHER way.** Between the two readings **three of five metros ROSE**, **Lakeland re-crossed ABOVE the threshold** (5.97 → 6.01), and **Tampa printed the highest MSI in the whole series** (6.9 → 6.96 → 6.99 → 7.05 → 7.01 → **7.15**). Breadth fails on **Cape Coral alone, 0.09 under the line.** ⭐ **The 8/23 anti-noise leg guarded the TIME dimension and left the LEVEL dimension unguarded** — it was written to refuse a rounding-error de-fire and it has now produced one by a different route: a single metro a rounding-distance below 6.0 can hold the stand-down open indefinitely while the other four strengthen. **That is a rule defect, and it is Will's to rule on PROSPECTIVELY — CORAL proposes and does not self-apply, exactly as on 8/23 when the fire had no falsifier.** ⛔ **The defect does NOT change today's grade.** Re-fitting a rule at the grading table because the result is inconvenient is the precise failure the pre-registration exists to prevent, and the rule was written on 8/23 **before** the data turned.

**⛔ WHAT I AM NOT CLAIMING — inference audit (step 13a).** A rising MSI is **not** published here as "seller stress is intensifying." **RIVAL MECHANISM, same direction:** MSI can rise because the *remaining listing pool* is more distressed (composition) rather than because *more sellers* are motivated (breadth) — both push the index up, so **the index level cannot separate them.** ⭐ **The discriminator is UNIT VOLUME — active listing counts — and that is exactly what is no longer retrievable (OQ L).** So the MSI moves are published as **measured values only**, with the causal upgrade **explicitly declined**. This makes OQ L matter *more*, not less.

**2. ⚠️ INSTRUMENT INTEGRITY — the Parcl listings field got WORSE, not better, and in the way that evades review.** On 9/2 the per-metro active-listing count was **absent** from the server HTML (SEARCH-NOT-FOUND). On 9/13 it is **present and renders as a literal `0`** (`Total Active Listings · 0`) on **all five** metros — with **no backing numeric field anywhere in the payload** (verified: zero matches for any `*listing*` numeric key). **Tampa carried 26,801 active listings on 8/23; a true 0 is impossible.** ⇒ **It is a hydration placeholder, not a measurement.** ⛔ **DO NOT carry "0 listings" and do not let it satisfy a presence check** — a required field satisfied by a placeholder passes every presence audit while being pure fabrication downstream. **OQ L remains UNRESOLVED and is now higher-priority**, because it is also the discriminator the inference audit above just named. Price-cut share likewise absent (prose only, no number).

**3. Verification legs (detail → `STATUS_DETAIL.md`):** every MSI value read **three independent ways** — `<title>`, `og:description`, embedded JSON `"value"` — **all agree to the hundredth on all five metros.** Stamps read verbatim across an intervening HTML comment node (the naive grep returns an empty stamp — a silent false negative).

**4. STILL LIVE FROM 9/2, unchanged and not re-derived** *(full text → `STATUS_DETAIL.md`)*: **FMHPI excludes condominiums by construction**, so the "three statewide signs" conflict dissolved — it was a perimeter question. ⭐ **THE ONE FIGURE THE DESK PUBLISHES** *(binds per METRIC — FL house prices and FL condo prices are two metrics)*:
> **FL statewide single-family, constant-quality: `+1.68% YoY SA, July 2026` (FMHPI FL, Freddie issuer master file)** — **excludes condo/co-op/PUD; conforming conventional only.**
> **FL statewide condo/townhouse: `$295,000 median, 0.0% YoY, July 2026` (FL Realtors, PRIMARY), EXPLICITLY a mix statistic** — no constant-quality statewide FL condo index is in hand (OQ K).
> ⚠️ **The caveat that cuts at my own mechanism: FMHPI sees only conforming conventional financed sales while FL cash share was 51.0% in July** — structurally blind to the cash capitulation-clearing channel this desk says is doing the price discovery. **A rising FMHPI is not evidence against that read.**


## [rotated] OQ A resolved-state bullets — STATUS.md L105–L111 @ 7035b2b3b

**✅ RESOLVED STATE — THE CLOCK RAN AND THE CONDITION WAS MET (2026-09-02 → 2026-09-13).**
- **Sub-threshold reading 1 of 2: 2026-09-02** (page vintage `Updated: 9/3/2026`) — **3-of-5 >6.0**; Cape Coral 5.95, Lakeland 5.97.
- **Sub-threshold reading 2 of 2: 2026-09-13** (page vintage `Updated: 9/13/2026`) — **4-of-5 >6.0**; **Cape Coral 5.91 the only metro under.** Spacing **11 days** observed / **10 days** by page vintage — **≥10 on both clocks.** No reading taken in between ⇒ **CONSECUTIVE.**
- **⇒ CONDITION MET. LEG STATE: 🟠 (stood down 2026-09-13 from 🔴).** ⛔ **Supply-side price-discovery leg ONLY** — CORAL overall **🟠 unchanged**, bank-transmission rail **NOT met, NOT armed, unchanged in both directions.**
- **The leg did NOT stand down because Florida improved.** It stood down because breadth is a **count**, and one metro (Cape Coral) sits **0.09** below 6.0 while the other four are above and three of five ROSE. ⭐ **Registered as a rule defect for Will to rule on PROSPECTIVELY** — the 8/23 letter guards SPACING but not LEVEL, so a single laggard can hold a stand-down open while the signal strengthens. ⛔ **CORAL proposes; CORAL does not self-apply, and did not re-fit the rule at the grading table.** → escalated to PROME 9/13 (OQ S).
- **Re-fire:** the 8/23 letter registers a stand-down and **no re-fire condition**. ⚠️ **That is the mirror of the gap closed on 8/23 and it is now the live one** — if breadth returns to 5-of-5 there is no registered rule to take the leg back to 🔴. **Named, not self-answered** (OQ S).


## [rotated] FL ENROLLMENT (9/13 version, pre-MARCO reconcile) — STATUS.md L140–L152 @ 7035b2b3b

## FL ENROLLMENT — the one figure, for MARCO to reconcile against (SIG-W-20260911-002)

⛔ **THE ROUTED HEADLINE DOES NOT RECONCILE AT PRIMARY. CORAL DOES NOT PUBLISH IT AS A FACT.** WALTER routed *"Orange County FL schools −7,600 students YoY on ~191,000, district names housing affordability + immigration law."* **Primary verification run 9/13 at OCPS direct** (full table, URLs and clean negatives → `STATUS_DETAIL.md` § "2026-09-13 FL enrollment verification").

⭐ **THE ONE FIGURE CORAL PUBLISHES:** **OCPS district total enrollment `201,652` — headcount, vintage `2025-09-15`, source: OCPS "Enrollment Summary by School/Grade" PDF (PRIMARY).** Same series **`199,368` at 2026-05-15.** ⛔ **No 2026-27 file exists yet** (every 2026-27 filename probed returns 403 = absent), **so no comparable-basis YoY is available at all.**

⛔ **THREE INSTRUMENTS, NO SHARED BASIS — do not difference them.** (a) the **headcount** series above · (b) **FY27 Adopted Budget K-12 FTE `228,198, +0.82%`** (PRIMARY, adopted **2026-09-08**) · (c) the **−7,672** claim, off the district's **10-DAY COUNT** (~late Aug 2026), **press-tier, primary unpublished.** `201,652 − 7,672 = 193,980`, **not ~191,000**; 191,000 **exceeds** the traditional-only 180,282; **FTE ≠ headcount.**
⭐ **The sharper fiscal tell than the enrollment number: the FY27 budget was ADOPTED 2026-09-08 — AFTER the late-Aug 10-day count — and still carries a +0.82% INCREASE.** A budget projecting growth against an actual count below it is exactly what *"lost more than projected ⇒ $8.5M extra cuts"* looks like. **The narrative is coherent; the numbers are not comparable.**

⛔ **INFERENCE AUDIT — THIS DOES NOT MOVE PILLAR 7 (MIGRATION), AND THE REASON IS NOT THE SOURCING.** **Rival mechanism moving the statistic the SAME direction, named by the district itself: "expansion of taxpayer-funded vouchers."** A voucher-driven shift from public to private schooling produces a **public-school enrollment decline with ZERO net out-migration**; declining birth rates do the same. ⇒ **Public-school enrollment cannot separate migration from substitution.** Causes are published **unweighted**, and the causal quote is **in no district-published document reached — press-only.** **Pillar 7 UNCHANGED; no colour moves.**
⚠️ **Correction to WALTER:** the signal's limit says *"single local-TV outlet"* — **it is multi-outlet** (WKMG · Spectrum 13 · CF Public Media · FOX 35), all sourcing 7,672 to Supt. Vazquez's 10-day report. Still press, not primary.
**Resolution path → OQ T:** the 2026-27 OCPS headcount file (re-check after mid-Sep), or **FLDOE PK-12 Survey 2 (October membership)**, the canonical FL count. ⚠️ **FLDOE, EDStats and OCPS BoardDocs were ALL 403/unreachable 9/13 — SEARCH-BLOCKED, never absent.**


## [rotated] FEEDS TO (9/13) — STATUS.md L153–L164 @ 7035b2b3b

## FEEDS TO

- **PROME** — 🟠 **MSI reading #6 GRADED: 4-of-5 >6.0 ⇒ second consecutive sub-threshold reading ≥10d apart ⇒ GATE-CORAL-MSI-01 STANDS DOWN 🔴→🟠, supply-side price-discovery leg ONLY.** Stamps `Updated: 9/13/2026` verbatim ×5, HTTP 200 ×5, MSI triple-verified. ⛔ **CORAL overall 🟠 and the bank rail are UNTOUCHED in both directions.** 🔴 **Two governance items for Will (OQ S): (a) the rule stood the leg down while 3 of 5 metros ROSE and Tampa hit a series high — it guards spacing, not level; (b) there is NO registered RE-FIRE condition.** Both **prospective** — today was graded as written. **PROME owns GATES.tsv; CORAL edited no PROME file.**
- **HOMER** *(via PROME — HOMER dark)* — **FMHPI cannot bear on the FL condo question: the Freddie methodology excludes condominiums verbatim.** ⛔ **Vintage correction: the FMHPI-vs-median comparison used CORAL's JUNE median (+4.9%); the July figure is +3.7%** — like-for-like the gap is 2.0pp, not 3.2pp. On single-family the two statewide instruments **agree in sign**; there was never a three-way conflict.
- **REGINALD** — bank rail **UNCHANGED: NOT met, NOT armed.** Q2 closed 7-of-7 benign; your 8/10 leading-bucket close consumed as owner-read, not re-derived. ⚠️ **Upstream-of-the-bridge correction to my 9/2 send: the MSI stand-down CLOCK has now RESOLVED — the leg is 🟠, not 🔴.** ⛔ **Do not read that as FL supply stress easing** — breadth failed on one metro 0.09 under while Tampa printed a series high 7.15. **Nothing about bank transmission changed.** Next re-test Q3 ~late Oct.
- **CREED** — ✅ **§5 ask GRANTED: pillar 4 STAYS 🟡, reason rewritten to yours** — "feed live but structurally thin; no FL geographic layer; named-loan prose only, ~1 event per 2 months." **A 🟢 would have re-created the defect the flag was raised for.** Your −79bp noise caveat **adopted into OQ C**; it materially weakens what CORAL was carrying. **Send the empty months — the zeros are the cadence.**
- **RED** — ✅ **BOTH ROWS CONFIRMED, not superseded** (KB-RED-046 · KB-RED-052): the **~70/30** split and its **~winter** anchoring **STAND on summer data**, and the summer evidence pushed **toward the 70% leg**: Q2 closed 7-of-7 benign with the sharpest pre-registered tell falsified. **Re-date Stale_By to 2026-11-15** (CORAL's pre-registered falsify grade). cc DEWEY, same answer.
- **MARCO** — ✅ your 9/2 adoption of all four FL figures received, zero divergence. ⚠️ **UPDATE THE MSI CELL: you carry it as "reading 1 of a required 2, clock running, leg holds 🔴." Reading 2 landed 9/13 at 4-of-5 ⇒ the leg is now 🟠 (leg only).** ⭐ **FL enrollment (SIG-W-20260911-002) — my figure and its limits are in §"FL ENROLLMENT" below; reconcile to ONE number, and I do not assert your half.** ⛔ **Your VX-FL-02 single-family months-of-supply hole: I hold FL Realtors statewide SF 4.5 months (July 2026) — take it if the perimeter fits, it is a SUPPLY figure, not FMHPI.** Tourism/Canada fold stays yours.
- **CARL** — cost stack unchanged; **Citizens personal-lines depopulation has STOPPED** (+138 July) — the household relief that was easing has flattened. Hurricane tail still low.
- **AEOLUS** — **season 5 named / ZERO hurricanes, no FL landfall; NHC 9/2 8PM: no formation expected 7 days, at the ~9/10 peak.** Your soft-market asymmetry **hardens** — the CSU 7%/9% remainder-of-season tail is being run down by the calendar onto a −15/−30%-priced market. ENSO figure remains yours.
- **DAEDALUS** — ✅ **F-2 fix APPLIED 9/13: intl migration now stamped `+178,674 (2025 annual Census, components of change)`** with your arithmetic shown (−56.5% vs stated −57%) — **the two desks corroborate; never a conflict.** ⏳ **L4 declared-flat `TRADE.md` DEFERRED, not refused** — accepted that it is not Will-blocked.


## [rotated] BOTTOM LINE (9/13) — STATUS.md L165–L178 @ 7035b2b3b

## BOTTOM LINE

**The 🔴 supply-side price-discovery leg stood down to 🟠 today on its own pre-registered rule — and the reason it stood down is not the reason anyone would assume.** Breadth came in at **4-of-5 >6.0**, a second sub-threshold reading 11 days after the first, so the 8/23 Will-ratified condition was met and the leg went 🔴→🟠. ⛔ **The leg ONLY. CORAL stays 🟠 overall and the bank-transmission rail is untouched in both directions — NOT met, NOT armed.**

⭐ **But between the two readings the series moved the OTHER way.** Three of five metros ROSE, **Lakeland re-crossed back above 6.0**, and **Tampa printed the highest MSI in the entire series (7.15)**. Breadth failed on **Cape Coral alone, 0.09 under the line.** **A leg stood down on a strengthening signal because the rule counts metros and does not look at levels.** That is a real defect in a rule I wrote and Will ratified, and **it is registered for Will to rule on PROSPECTIVELY (OQ S) — not fixed at the grading table today.** Pre-registration is worth nothing if it is renegotiated the moment it returns an awkward answer, so today was graded exactly as written. The companion gap is sharper: **the letter registers a stand-down and NO re-fire condition** — the mirror of the exact hole closed on 8/23.

⚠️ **What I explicitly did NOT conclude.** A rising MSI is published as a **measured value, not as "seller stress is intensifying."** Composition (a more-distressed remaining listing pool) and breadth (more motivated sellers) push the index the same way, so **the index cannot separate them — the discriminator is unit volume.** And **unit volume is precisely what Parcl stopped serving**: the active-listing count now renders as a literal **`0`** with no backing field, which is a placeholder that **passes a presence audit while being fabrication downstream**. ⛔ **Never carry "0 listings."** That instrument gap (OQ L) is now load-bearing, because it blocks the causal read the grade invites.

**What did not move is still the thing that matters. Bank-loss transmission remains unconfirmed** — Q2 closed 7-of-7 benign, the sharpest pre-registered tell falsified, REGINALD's leading-bucket close 4-of-4 REVERT. **Household and collateral stress must still not be read as banks breaking**, and a supply-side leg standing down is **not** a Florida all-clear. Next bank re-test **Q3, ~late Oct**.

**Next:** **Citizens 8/31 month-end, owed NOW — watch the personal/commercial split** · **~9/17 FL Realtors August** (price and volume as separate legs) · **9/30 NFIP expiry + FIGA assessment ends + FL min wage $14→$15** · **~Oct–Nov warrantability friction** · **late Oct Q3 bank prints** · **Nov 3 Amendment 3**, still the biggest two-sided forward variable and the **oldest un-worked item** (E, unlocated on 3 attempts — switch to court dockets) · **Nov 15 pre-registered falsify grade**, with the **bankruptcy instrument (H) still unbuilt** and criterion 5 scoring 0 again if it stays that way.

*CORAL: tracking the bleaching of Florida's condo market. Evidence → `STATUS_DETAIL.md` · session history → `archive/STATUS_SESSIONS_20260721-20260823.md` · prior dashboard → `workbook/STATUS_archive_20260325.md`.*


---

# 2026-09-28 session evidence (15-day catch-up; desk dark 9/13→9/28)

**Method note:** five read-only research pulls (Opus subagents, scratchpad only) + CORAL's own primary re-checks. Every figure below carries its tier. Raw artifacts were in the session scratchpad; the bankruptcy instrument is persisted at `tools/bkcy/`.

## A. MSI reading #7 — 2026-09-28 (Parcl direct, curl+UA)
| Metro | 9/13 | **9/28** | Δ | >6.00 | Active listings | % cutting |
|---|---:|---:|---:|:--:|---:|---:|
| Tampa | 7.15 | **7.18** | +0.03 | ✅ | 26,894 | 51.7% |
| Punta Gorda | 6.59 | **6.51** | −0.08 | ✅ | 4,093 | 47.2% |
| North Port | 6.27 | **6.34** | +0.07 | ✅ | 11,919 | 46.3% |
| Cape Coral | 5.91 | **5.96** | +0.05 | ❌ | 13,133 | 44.9% |
| Lakeland | 6.01 | **6.13** | +0.12 | ✅ | 8,208 | 45.7% |
| *Jacksonville / Orlando / Miami (context)* | — | 6.40 / 6.21 / 4.79 | | | 12,220 / 19,912 / 52,296 | 48.9 / 47.8 / 38.5% |
- HTTP 200 ×8; all stamped `Updated: <!-- -->9/28/2026` (new vintage vs 9/13). MSI read via `<title>`, `og:description`, JSON-LD `"value"` (+ `__NEXT_DATA__ seo.msiValue`) — agree to the hundredth. ⚠️ All four come from one server object: consistency of extraction, not four independent measurements.
- **⇒ 4-of-5 > 6.00. No rule in the 8/23 letter applies (it has no re-fire condition). Leg stays 🟠.** Pages ~3 KB smaller than 9/13 ⇒ template changed.
- **⭐ LISTINGS FIELD (OQ L / ML-CORAL-079) — the counts ARE retrievable:** `__NEXT_DATA__` → `seo.totalCount` (active listings) and `seo.nCutting` (listings with a cut); also a JSON-LD "Active listings" value and the og text; all agree. Share = nCutting/totalCount (no numeric share field; `ppsf` null). The visible `Total Active Listings · 0` is still a placeholder. ⚠️⚠️ **The 9/13 finding "no backing numeric field anywhere" may itself be a KEYED-SEARCH ARTIFACT** — that check grepped for keys containing *listing*; `totalCount`/`nCutting` don't contain it. Unresolved whether the fields existed on 9/13 (Wayback 429). **Do NOT write "Parcl restored the field."** Route: `https://www.parcllabs.com/_next/data/<buildId>/research/markets/fl/<slug>/metro.json` (buildId read from page; `OeYHjnzxFCwhF5PUjMG5V` on 9/28).
- **Unit-volume leg (the discriminator the 9/13 inference audit named):** Tampa listings 26,801 (8/23) → 26,894 (9/28), +0.3%; cut-share ~51% → 51.7%. With the index at a series high and listings flat, the composition-vs-breadth question is **still not separable on two points** — logged, not interpreted.

## B. FL Realtors AUGUST 2026 (PRIMARY — Monthly Market Detail PDFs, pub 2026-09-16; next 10/16)
**Condo/TH, Aug-26 vs Aug-25:** closed 7,291 vs 7,424 (**−1.8%**; Jul +11.0%) · cash 3,722 (+0.6%), share 51.0% vs 49.8% · median **$298,000 +2.8%** · average $426,467 +1.8% (Jul avg $443,764 ⇒ fewer high-end sales MoM) · $ vol $3.1B 0.0% · new pending +1.2% (13th straight) · new listings +1.1% · inventory 59,697 −11.5% · **months supply 7.7** (9.3) · **pct of original list 93.3% (91.8%)** · **time to contract 69d (72d)** / to sale 109 (110).
**SF, Aug-26 vs Aug-25:** closed 21,497 −1.4% · cash −2.1%, share 26.9% (27.1%) · median **$415,000 +1.2%** · avg $607,238 +3.8% · $ vol +2.4% · new pending **−2.8% (ends 12-mo run)** · new listings −1.3% · inventory 94,610 −13.0% · **months supply 4.3** (5.3) · orig-list 96.0% (94.8%) · TTC 44d (51d).
- **Four-leg read (step 13a.4), condo:** LEVEL +2.8% (mix) · VOLUME −1.8% · REALIZATION up (93.3 vs 91.8) · VELOCITY faster (69 vs 72). **Three of four legs cut AGAINST "clearing by cutting price" statewide.** Absorption narrowed (sales turned negative YoY). Statewide release does not corroborate the Parcl seller-motivation read; it does not refute it either (Parcl ≠ statewide perimeter).
- ⚠️ **Months-supply denominator:** FL Realtors divides inventory by the 12-mo average of closed sales (YTD +7.9%), so the ratio falls on trailing sales even when the current month's sales fall. The 7.8→7.7 tick is not evidence of August demand.
- ⚠️ **CORAL COUNTING ERROR:** the condo series is Jan 9.7 → Feb 9.3 → Mar 9.1 → Apr 8.9 → May 8.6 → Jun 8.1 → Jul 7.8 → Aug 7.7 = **7 straight declines**. CORAL carried "4th straight tightening" in July (should have been 6th); the July PDF shows the same values, so it is not a revision. Corrected forward.

## C. MIAMI REALTORS August 2026 (issuer text via PR Newswire 9/16 — miamirealtors.com 403 = SEARCH-BLOCKED)
Miami-Dade: total 1,769 **−1.1% YoY** (SF 858 −3.1% · condo 911 +1.0%) · condo median $408,000 −0.49% · SF median $680,000 +3.82% · condo listings 11,495 −9.04% · **condo months supply 12.1 (14.0)** · condo TTC/TTS 66/108 (67/106) · condo cash 50.5%. **The "−47%" is vs Aug-2021 (3,299 ⇒ −46.4%)**; YoY −1.1%. Other compilers ("$420K +6%", "12.7mo") deliberately NOT mixed. **Broward condo months 9.9** (listings −14.8%) · **Palm Beach condo months 6.7** (listings −17.1%) — ⚠️ PB's April 8.2 compiler basis unverified, so 8.2→6.7 is NOT asserted as a trend. ⚠️ Issuer-release defects: Broward SF median line duplicates the condo median; PB total-sales headline duplicates Broward's (1,899) vs its own text 1,877; "days up" prose contradicts the numbers.

## D. Citizens (PRIMARY — "Detail By Product Line" PDFs 20260731 run 8/4 / 20260831 run 9/8, "Excludes Takeouts"; "2026 Stats" file data as of 9/22)
| Bucket | 6/30 | 7/31 | 8/31 | Jul Δ | Aug Δ |
|---|---:|---:|---:|---:|---:|
| Personal (PR-M+PR-W) | 273,684 | 273,822 | 262,006 | +138 | **−11,816 (−4.32%)** |
| Commercial (CR-M/W + CNR-M/W) | 4,562 | 4,374 | 4,225 | −188 | **−149 (−3.41%)** |
| **Total** | 278,246 | 278,196 | **266,231** | −50 | **−11,965 (−4.30%)** |
Exposure $78.908B → **$74.805B (−5.20%)**. MARCO's 9/24 figures reproduce exactly.
- **Mechanism:** personal takeout round **8/18 = 11,723 policies** (PR-M 10,378 · PR-W 1,345) ⇒ **ex-round personal ≈ −93 (flat).** July had no personal round (+138); June −15,273 vs a 14,486 round (≈ −787 ex-round). ⚠️ Assumes 8/18 assumptions are reflected in the 8/31 file — timing fits; no document states it. **Commercial rounds are Jan/Mar/May/Jul/Sep/Nov — none in Aug ⇒ −149 is genuine commercial attrition** (July's −188 included only 10 takeouts).
- **September rounds:** 9/15 personal **10,210** (Manatee 4,151 · Mangrove 66 · One Alliance 32 · Slide 5,961) · 9/22 commercial 40 (Slide). **No "9/18 round"** — 9/18 is the date of the snapshot **255,099** (different series; never difference against month-end). YTD assumed 131,144. Next personal rounds 10/20, 11/17.
- ⚠️ **Citizens PDF defects:** PR-M dollar "Change From Prior Month" columns = −(prior level) in both files; CR-M wind/ex-wind change columns swapped. Derive $ changes from levels.

## E. NFIP / FIGA / season
- **NFIP extended to 2026-12-11** — H.R. 6500 "Continuing Appropriations and Extensions Act, 2027", signed **2026-09-02** (White House statement P1; GovInfo enrolled text Sec. 139 → Sec. 106(3) date = Dec 11, 2026, P1); FEMA page updated 9/28 (P2). P.L. 119-103 per CRS title (S; congress.gov 403). **The 9/30 cliff carried on STATUS/CALENDAR was stale since 9/2.**
- **FIGA 1% ends 9/30/2026** — FIGA notice 2026-02-24 (P1): policies eff 10/1/26+ should not carry it. No separate OIR ending order found (levy order OIR 308776-23). **No new FL insurer insolvency/receivership/FIGA assessment Aug–Sep** (FIGA insolvent list, OIR Recent Actions, DFS receivership — newest is UPC 2023; P1).
- **Season (NHC archive, every advisory AL01–AL08, P1):** Arthur · Bertha (FL Panhandle TS watch/warning 7/19–22) · Cristobal · Dolly · Edouard · **Fay** (peak 60 kt, TD 9/28, post-tropical Tue) · **Gonzalo** (Cabo Verde) · **Hanna** (formed 9/28, 45 mph, ENE of Bermuda) ⇒ **8 named / 0 hurricanes; no FL landfall, no FL watch/warning since 9/13.** NHC 2 PM EDT 9/28: *"Tropical cyclone formation is not expected over the next 7 days."*

## F. Amendment 3 — OQ E RESOLVED (ruling 2026-08-03; found via AG letter, P1)
- *Save Our Voters From Misleading Ballot Language, Inc. v. Byrd*, Leon Co. 2026 CA 1254/1405/1381 consolidated. **Judge Frank's 18-page SJ order dated 8/3 (reported 8/4, press S):** title "Save Our Homes From Excessive Property Taxes" + summary "clearly and conclusively defective" (title a "political slogan"). AG given 10 days to rewrite. **Not removed.**
- **No appeal:** AG Uthmeier → SoS Byrd letter 8/13 (P1) cites the state's notice declining further appeals, triggering the §101.161(3)(c)2. rewrite. Plaintiff (Brandes) and FL Policy Institute called the rewrite accurate (CBS12 8/14, S).
- **Ballot (P1, Division of Elections, read 9/28): Ballot No. 3 — "INCREASED HOMESTEAD EXEMPTION; LOWER CAP ON INCREASES IN NON-HOMESTEAD PROPERTY ASSESSMENTS".** Mechanics: non-school homestead exemption $150K (2027) → $250K (2028), then CPI; local option to full value; school levies unchanged; non-homestead cap 10% → 5%; new residents (not FL-resident 12/31/26) get it from year 5; property-tax use list; eff 1/1/2027; **60% to pass**. Fiscal: ~−$4.93B FY27-28, ~−$11.83B/yr thereafter (state estimates via WPTV, S).
- **Polling (not a trend line — different wordings/populations):** St. Pete Polls for FL Politics **Sep 15–17, 913 LV ±3.2: 45 yes / 30 no / 25 undecided** · Sachs ~Aug 18, 800: 63% (new wording 65 vs old 60) · Targoz/JMI Jul 20–26: 74–76% no-tradeoff, **55%** with service-cuts framing · UNF Jul 8–17: 61% minimal, **45/47** with $11.86B cost.
- **PRE-REGISTRATION ML-CORAL-042 GRADED AS WRITTEN: BRANCH A (rewrite ordered) ⇒ pillar-9 amendment row marked "leaning FAIL"; household cost-stack relief OFF; CRE/MF burden-shift + muni-fiscal tail OFF. NOT a rail/thesis move.** ⚠️ **Honest limit:** Branch A's rationale was that a rewrite *injects fiscal language*; the rewritten summary reads as mechanics (plus a spending-use list) and the one post-rewrite poll with a clean comparison (Sachs) shows new wording ≥ old. The branch was graded on its letter (rewrite ordered), not on whether its mechanism materialised — **the mechanism is unconfirmed**. The one poll since the rewrite that is under 60% (St. Pete 45 yes) has 25% undecided. Leon Clerk 403 = order not read at primary (SEARCH-BLOCKED).

## G. Brightline Florida Ch.11 (SIG-W-20260925-014)
In re **FIHPNP LLC, No. 26-20876 (MEH), Bankr. D.N.J.** (Judge Hall), filed 9/24 23:22, 17 debtors (P: Stretto petition/RECAP). **Operator Brightline Trains Florida LLC is NOT a debtor**; prearranged (RSA), not prepack; first-day hearing 9/29 11:00 ET; Doc 55 objection unread. Interim: BTF issues $257.7M senior secured notes pari passu with existing senior (Assured consented). **Impaired: Brightline East LLC taxable notes ~$1.19B** (Redwood/Aristeia/Nut Tree; S Bond Buyer 9/25). **Unimpaired (S, company release):** 2025B commuter bonds $985M · AAF Ops 2024 $925M · AAF Ops 2024A $285.7M; the $2.2B FDFC-conduit 2024 senior tax-exempts keep principal but accept a limited interest deferral (Assured guarantees deferred interest on the ~$1.13B it wraps). $490M exit capital (Assured + Nuveen/First Eagle/Invesco/Nomura). **FL exposure:** Flagler/real-estate entities are debtors (DT Miami, New Flagler Development, Brightline Property Holdings, Brevard FGT, AAF Jacksonville Segment) — schedules not filed; top-20 unsecured includes Miami-Dade Water & Sewer $361,554 (trade); no FL bank found; FDFC is a conduit (no state credit).

## H. Bankruptcy instrument BUILT (OQ H) — see `tools/bkcy/README.md`
12 mo to 6/30/26, M.D.+S.D. all chapters **217.1/100k, +21.2% YoY**; nonbusiness 205.5; Ch.7 151.5; statewide nonbusiness 199.0 (the carried "~190" = statewide nonbusiness 189.6 @3/31/26, exact); S.D. alone 230.0. US 176.3 (+12.3%). FL/US 1.205× → **1.231×**. Tripwire >~230 not crossed on the M+S basis; reachable at 12/31/26 if Jul–Dec growth ≥12.6% (every quarter since early 2025 has cleared that). **Spec defects flagged for between-grade amendment:** (1) the "Ch.7" label vs the "~190" anchor are different bases; (2) "fades" carries no number. **Direction is basis-robust: acceleration has NOT faded on any basis.**

## I. Statewide FL enrollment sweep (2026-09-28, Will's ask; KB ML-CORAL-089) — ⭐ now a TRACKED SERIES: VX-CORAL-ENRL-01 · ledger `workbook/FL_ENROLLMENT.tsv` · full reports `sources/enrollment/`
| Measure | Value | Basis / tier |
|---|---|---|
| FLDOE Oct membership PK-12 incl. charters | 2,859,655 → **2,792,954 (−66,701, −2.33%)**, Oct-24 → Oct-25 | Survey 2, PRIMARY via Wayback (fldoe.org 403) |
| Districts down, 2025-26 | **61 of 67** (gains: Dixie, Sumter, Hendry, St. Johns, Charlotte, Walton; all <500) | same |
| 2026-27 early, same-basis YoY | **9 of 11 down** (Broward −12,343 · Miami-Dade ~−15,100 first day · Orange −7,672 · Palm Beach −7,204 · Pinellas ~−3,840 · Seminole −1,473 · Volusia −1,400 · Osceola −816 · Lake −396); St. Johns flat; Lee slightly up | district PRIMARY (Broward, PB, Osceola, St. Johns) / press others |
| District FTE (EEC) | 2,817,655 → 2,749,749 est (−67,906) → 2,722,531 fcst 26-27; 25-26 came in 55,549 below budget forecast | EDR EEC 8/11/26, PRIMARY |
| Scholarship (FES) FTE | 361,748 → **434,053 (+72,305)** → 482,528 fcst | EEC, PRIMARY — ⚠️ not all switchers (universal eligibility) |
| English-learner FTE | **−22,084 YoY** (~33% of district drop); private-school enrollment +1.5% | EEC 8/2026 |
| Kindergarten | −11,337 (−5.9%); K cohort births (2020/21) 7–9% below the 2008 graduating cohort | FLDOE; FL DOH |
⛔ District counts vs FLDOE Survey 2 disagree for the same year (Broward −10,834 vs −7,289; Lee −2,315 vs −1,167; Manatee +300 vs −324) — cite each on its own basis, never difference across. **Inference audit:** rival mechanisms (scholarship substitution, cohort size, international arrivals) all move the count the same way as domestic out-migration and are the ones the state and districts name ⇒ **not evidence of domestic out-migration; consistent with the Census intl −37%.** Pillar 7 unchanged. Next same-basis read: FLDOE Survey 2 (Oct-26).

---

# 2026-09-28 READ-FIRST table — ROTATED out of `STATUS.md` 2026-09-28 (evening, read-cap)

**Verbatim; receipt 3118 B · crc32 `fc809d76`.**

## 9/28 (Mon) — WHAT CHANGED WHILE THE DESK WAS DARK — READ FIRST

| # | Item | Level (dated, tiered) | So what |
|---|---|---|---|
| 1 | **MSI reading #7** | **2026-09-28**, stamp `Updated: 9/28/2026` ×5: Tampa **7.18** (series high) · Punta Gorda 6.51 · North Port 6.34 · **Cape Coral 5.96** · Lakeland 6.13 ⇒ **4-of-5 > 6.00** | ⛔ **No rule applies** — the 8/23 letter has no re-fire condition. Leg stays 🟠. Re-fire + level-guard proposal delivered to PROME for Will (WQ-241). |
| 2 | **Parcl listings recoverable** | `__NEXT_DATA__ seo.totalCount` / `nCutting`: Tampa **26,894** listings, **51.7%** cutting (≈ 8/23's 26,801 / 51%) | OQ L route found. ⚠️ **The 9/13 "no backing field" finding may be a keyed-search artifact** (searched for `*listing*` keys) — unresolved, do NOT say "restored". |
| 3 | **FL Realtors Aug** (PRIMARY, pub 9/16) | Condo median **$298K +2.8%** · sales **−1.8%** · orig-list **93.3% vs 91.8%** · contract **69d vs 72d** · months **7.7**; SF $415K +1.2%, 4.3 mo, pendings −2.8% | **Counter-evidence to statewide distress.** Months-supply is on a trailing-12 denominator — the tick is not demand. ⚠️ CORAL undercounted the streak: it is the **7th** straight decline, not 5th. |
| 4 | **Citizens 8/31** (PRIMARY) | **266,231 (−11,965, −4.3%)**; personal −11,816 of which **8/18 takeout round 11,723** ⇒ ex-round ≈ **−93**; commercial **−149** (no Aug round ⇒ real attrition); exposure **$74.8B** | Takeout engine working; **organic personal depopulation still stalled**. 9/15 round 10,210 more; snapshot 255,099 @9/18 (different series). |
| 5 | **Amendment 3** | Frank SJ order **8/3**: title/summary "clearly and conclusively defective"; AG rewrite 8/13; **no appeal**; **Ballot No. 3**. St. Pete Polls 9/15–17: **45 yes / 30 no / 25 undecided** (needs 60%) | ML-CORAL-042 **Branch A graded as written ⇒ "leaning FAIL"**. ⚠️ Branch A's *mechanism* (rewrite injects fiscal language) is **unconfirmed** — Sachs ~8/18 had the new wording at 65%. |
| 6 | **Bankruptcy** (AOUSC F-2 PRIMARY, 12 mo to 6/30/26) | M.D.+S.D. **217.1/100k, +21.2% YoY**; FL/US **1.205× → 1.231×**; S.D. alone 230.0 | Instrument built. Criterion 5 **NOT MET on every basis** — the basis question moves the tripwire date, not the direction. |
| 7 | **NFIP** | **Extended to 2026-12-11** (H.R. 6500, signed 9/2, P1) | No 9/30 cliff. **FIGA 1% still ends 9/30**; no new FL insurer failure Aug–Sep. |
| 8 | **Season** | **8 named / 0 hurricanes**; no FL watch/warning since 9/13; NHC 9/28 2PM: no formation 7d | Soft-market asymmetry intact; ~2 months left. |
| 9 | **Brightline FL Ch.11** (9/24, D.N.J. 26-20876) | Operator **not** a debtor; impaired = **Brightline East taxable ~$1.19B**; tax-exempt series unimpaired (senior accepts interest deferral) | **No FL bank or state-credit transmission found.** Watch: Flagler real-estate debtors' schedules (station-area parcels). ⚪ info. |
| 10 | **Miami-Dade Aug** (MIAMI REALTORS) | sales **−1.1% YoY** (the "−47%" is vs Aug-2021); condo 12.1 mo; Broward 9.9; PB 6.7 | Not a new break. |


## J. Redfin buyers-vs-sellers, August 2026 (SIG-W-20260928-014, Will's Telegram via WALTER; KB ML-CORAL-091)
**Instrument (PRIMARY, Redfin data center `top_50_metros.csv`, last updated 2026-09-03; FL extract at `sources/redfin/redfin_buyers_sellers_FL_metros_thru_2026-08.csv`):** sellers = MLS active listings; **buyers = MODELLED** (seller/buyer hazard ratio from pending sales + Redfin tour-to-close search time), seasonally adjusted. Redfin uses metro DIVISIONS: "Miami" = Miami-Dade; Fort Lauderdale all-residential suppressed ("insufficient data").

| Metro · type | Aug-24 | Aug-25 | **Aug-26** | YoY pp |
|---|---:|---:|---:|---:|
| **Miami · all** | 140.6% | 151.7% | **138.3%** (18,916 sellers / 7,939 buyers) | **−13.5** |
| Miami · condo/co-op | 235.4% | 259.0% | **231.8%** (10,214 / 3,078) | −27.2 |
| Miami · single-family | 76.5% | 82.4% | **69.0%** (6,298 / 3,728) | −13.5 |
| Miami · townhouse | 74.4% | 104.4% | 102.3% | −2.1 |
| **Orlando · all** | 64.7% | 59.7% | **121.5%** (19,868 / 8,968) | **+61.9** |
| Orlando · condo / SF / TH | 189.7 / 50.4 / 70.1 | 178.6 / 42.9 / 83.7 | **270.1 / 101.4 / 158.4** | +91.5 / +58.4 / +74.7 |
| Tampa · all (condo) | 99.6% | 94.6% | **86.4%** (172.1%) | −8.2 |
| Jacksonville · all (condo) | 88.2% | 109.2% | **66.9%** (142.8%) | −42.3 |
| West Palm Beach · all (condo) | 111.3% | 121.7% | **64.9%** (117.4%) | −56.8 |
| Fort Lauderdale · condo / SF | 206.2 / 71.0 | 243.8 / 92.1 | **166.6 / 41.2** | −77.1 / −50.8 |

**(1) Is Miami condo-led? YES.** Condos are 54% of Miami's sellers but 39% of its modelled buyers; the condo gap (232%) is 3.4× the single-family gap (69%). Independent same-month corroboration: MIAMI REALTORS Aug condo 12.1 months supply vs SF 4.9; Realtor.com Miami–FLL–WPB MSA active listings **−15.0% YoY**, pendings **+5.0%**; Parcl Miami MSI 4.79 ("stubborn" — sellers not cutting). ⇒ **A large, old, condo-concentrated overhang with sellers holding price, SHRINKING year over year** (Miami has sat at ~140–150% since at least Aug-24). "#2 nationally" is a LEVEL rank, not a new break.
**(2) Orlando: the headline deterioration is NOT corroborated.** Redfin's jump is driven by modelled buyers **−25% YoY** (12,014 → 8,968) with sellers +3.6%. Two measures of ACTUAL activity say the opposite: **ORRA (Orange+Seminole) Aug closings 2,478 vs 2,306 (+7.5% YoY), inventory 12,144 vs 13,306 (−8.7%)**; **Realtor.com Orlando–Kissimmee–Sanford MSA (Redfin's own perimeter) active listings −2.5% YoY, pending listings +11.5%**. ⇒ Treated as a probable modelled-buyer artefact until a volume measure confirms it. ⚠️ ORRA's Aug-25 median conflicts across its own pages ($403,222 vs $382,950) — median not used. Parcl Orlando MSI 6.21 (>6) is the one instrument pointing the same way as Redfin.
**(3) Statewide pattern:** every FL metro is a "buyer's market" on Redfin's ≥10% definition, the **condo gap exceeds the single-family gap in every FL metro** (117–270% vs 35–101%), and **every FL metro except Orlando narrowed YoY.**
**(4) Divergence logged for the MSI gate (not interpreted):** Tampa's Parcl MSI printed a series high 7.18 (9/28) while Redfin's Tampa gap narrowed (94.6 → 86.4) and Realtor.com Tampa listings fell 6.4% with price-reduced share down 2.0pp. Seller-motivation index up; listings-vs-demand improving.
**Inference audit:** the gap is a listings-to-modelled-demand ratio (a months-supply cousin), so it inherits the four-leg rule — here VOLUME was the discriminator, and on Orlando it cut against the headline. **Read: no colour moves; condo remains where FL excess supply sits; the trend outside Orlando is easing; bank rail untouched.**

## K. Fannie bankruptcy/receivership channel · OPPAGA 26-04 · Biscayne 21 (Will's bounded pass, 2026-09-28; KB ML-CORAL-092)
**Fannie Mae (PRIMARY, Selling Guide B4-2.1-03 v.08/05/2026, Guide pub. 9/2/2026), verbatim:** *"a project must not be the subject of a voluntary or involuntary bankruptcy, insolvency, liquidation, or receivership proceeding, or any substantially similar action under state or federal law. This includes any project that has voted or is in the process of voting on any of the actions or proceedings described above."* Also covers termination/deconversion/dissolution. **No carve-out** for a confirmed plan, a non-debtor HOA, or a litigation-only receivership; only relief = case-by-case PERS exception.
| Review path | Rule applies? |
|---|---|
| Full Review · PERS · FHA-approved (B4-2.2-03) | Yes |
| **Waiver of Project Review** (detached, 2–10 unit, PUD, Fannie-to-Fannie refi ≤80% LTV) | **Yes** — B4-2.1-02: "the project is not terminating and is not involved in insolvency proceedings" |
| High-LTV Refinance (B5-7-01) | Carve-out — ⚠️ **but Fannie's acquisitions under that program are currently PAUSED** (B5-7-01 note + product page; CATO `a0fb85230`) ⇒ no live exception |
Other: Limited Review retired (PRIMARY: no longer listed; 8/3/26 date SECONDARY) · **15% reserve from 1/4/2027 = PRIMARY, LL-2026-03 p.3 (CATO)** · reserve-study "baseline funding" may not be used to **waive the 10% test** (B4-2.2-01, PRIMARY — narrower than press's "banned") · Condo Status Finder: HOAs/managers/authorized advisors only, one of four statuses, no reason given (SECONDARY). **Freddie Mac:** near-identical text in Condo Project Advisor (PRIMARY 12/8/2025) citing Guide 5701.3(j)(2)/(p); Guide itself 401-blocked; reach into its exempt categories unverified.
⇒ **Channel:** an association filing (or a vote to file) cuts conventional GSE financing for every unit in the building — a **financing constraint on owners**, independent of any bank credit loss.

**OPPAGA Report 26-04, "Milestone Inspection Reporting Data 2024 and 2025" (July 2026, PRIMARY — a statutory data report, not an audit; data received by DBPR through 3/31/2026):**
| Figure | What it counts | Split | Page |
|---|---|---|---|
| 8,736 Phase I | completed inspections | 6,952 of 8,777 required (2024) · 1,784 of 2,880 (2025) | 2, 8 |
| 1,575 Phase II | completed | 1,301 of 1,899 · 274 of 636 | 2, 8 |
| 1,587 extensions (94% coastal) | extensions of the initial deadline | 818 · 769 | 2, 9 |
| **903 repair permits** | permit **APPLICATIONS**, not issued or completed | 671 · 232 | 2, 12 |
| **<$1K – $30M** | **estimated values on applications, not costs**; avg $337,229 (2024), $496,236 (2025), single-permit submissions only | — | 12 |
| **54 unsafe/uninhabitable** | officials' lists; statute defines neither term | 30 (2024, 6 counties, 5 vacated) · 24 (2025: 23 Miami-Dade incl. 19 Aventura, 1 Orange) | 13–15 |
⚠️ **Coverage limits on every figure:** 71% (2024) / 64% (2025) of 389 jurisdictions reported; self-reported, unverified; some non-condo buildings included; 44% of Palm Beach municipal officials did not report for 2025; Broward/Miami-Dade/Palm Beach report Phase II only when repairs are needed (Phase II not comparable across jurisdictions). Press "~2,900 never completed" is DERIVED (11,657 − 8,736 = 2,921), not stated, and includes buildings on extension. **No SIRS or special-assessment data in the report.**

**Biscayne 21 (all SECONDARY; court dockets SEARCH-BLOCKED):** settlement reached AND funded Mon 8/31/2026 (TRD 9/3; holdout counsel Glen Waldman: "closed"); court sign-off pending as of 8/31; deeds unrecorded 9/3. ~$50M = one anonymous source (Two Roads' Collins declined); "~$6.3M/owner" assumes 8 ownership units, not 10 owners. 3rd DCA (Mar-2024; revised 7/10/2025) reversed a denied temporary injunction — interlocutory; FL Supreme Court **denied the petition for review 10/14/2025** (not a merits affirmance). Economic-waste/partition suit filed ~Feb 2026; its dismissal is UNVERIFIED. Edition buyers' deposit suit (~$2.5M) still live.
