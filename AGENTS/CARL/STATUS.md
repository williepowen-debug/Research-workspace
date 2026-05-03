# CARL STATUS
**Updated:** 2026-05-04 ~01:30 UTC
**Overall:** 🔴🔴 CRITICAL — Convergence **53/70 (76%)**. Thesis **v2.5.1** (May 3): masking framework narrowed 6→4 issuers + K-shape Selection / Tariff Transmission sibling section + CRL-22/23 added. **v2.5** (May 1): Path C ACTIVE-RED (provisional), matrix expanded 12→14 vectors, score recalibrated 58/60 → 53/70 (~60% calibration + ~40% conviction reduction). Audit trail in `thesis/CHANGELOG.md`. Counter-evidence tracking moved to `handoff_RED/COUNTER_LOG.md`.

*Check-in archives: `archive/status/`*

---

## SIGNAL DASHBOARD

### Credit / Delinquency
| Metric | Value | As Of | Status |
|--------|-------|-------|--------|
| CC 90+ DQ | **12.70%** (92% of GFC) | Q4 2025, NY Fed | 🔴 |
| Subprime Auto 60+ DQ | **6.9% ATR** | Jan 2026, Fitch | 🔴🔴 |
| SoFi 2025-1 CNL | **2.6% TRIGGERED** (⚠️ snapshot Mar 2026 — no SEC path, private/144A. Cannot refresh via abs_monitor. See KB-CARL-078.) | Mar 2026, Eisman Ep 49 | 🔴 |
| **ABS Structural** | **EART 2024-2 Class E CE BREACHED** (CNL 13.06% > 7.6% initial CE). AMCAR Class E 0.4pp cushion (~2mo). SDART Class D 1.8pp (~7mo). Terminal CNL: EART 32.3%, SDART 17.6%, AMCAR 14.5%. Rating actions imminent on subordinate tranches. | Apr 16 CARL analysis, EDGAR 424B5 | 🔴🔴 |
| **Ally Near-Prime** | Q1 NCO 1.97% / 30+ DQ 4.6% — 5th consec qtr "improvement" headline. **Composition-masking** (S-tier 40→37%, nonprime 9.7→10.1%, CLN +43% YoY, ACL -$224M). FY2025 vintage loss window 2H 2026 / Q1 2027. Detail: KB-CARL-222-226. | Apr 17 2026 | 🟢 (headline) / 🟠 (cohort) |
| Auto 90+ DQ | **5.21%** (near 5.27% max) | Q4 2025, NY Fed | 🔴 |
| Student Loan 30+ DQ | **16.3% WORST EVER** (~25% w/payment due behind) | Q4 2025 NY Fed / Feb 2026 TCF | 🔴🔴 |
| Student Loan 90+ DQ | **~9.8%** (FICO Spring 2026; +25% vs 7.9% Apr 2025). 6.1M new DQ Feb-Apr, avg score drop **-69 pts** (25% of group -100pt+). NY Fed Q4 official: 9.6%; 18-29 cohort 21%. | FICO Spring 2026 / Q4 2025 NY Fed | 🔴🔴 |
| Student Loan Defaults | **9.2M / $180B** (+1.5M in 90 days, Dec→Mar) + **2.4M late-stage DQ** | Mar 2026, ED/FSA | 🔴🔴 |
| **Sweet v. McMahon Auto-Relief** | **~271K borrowers** in auto-relief pipeline (DOE missed both deadlines: Jan 28 + Apr 15). Full discharge + refunds + credit tradeline deletion. Notices due Jun 15. Self-executing, no stay. KB-CARL-183/216. | Apr 17 STUE | 🔴 FIRED |
| SAVE Transition | **ENDING Jul 1** — 7.5M must select; judicially dead (8th Cir Mar 10) + legislatively dead (WFTCA Jul 2025). Wave-structured notices every 2wks, 90-day selection window, non-selectors → Standard/Tiered Standard Oct 1. | ED.gov / 8th Cir | 🔴 |
| MOHELA Servicer Failure | **2.5M missed bills → 800K DQ.** AFT v. MOHELA in discovery; next status conf **May 28**; 3 concurrent class actions active. | DOE / AFT | 🔴 |
| BNPL Late Rate | **41%** (+7pp YoY) | 2025, CFPB | 🟠 |
| SYF Q1 2026 | NCO **5.42%** / FY26 guide CUT to <5.5% (was 6.0%). ⚠️ Survivor-pool: Home & Auto -3.7% YoY, active accounts -0.7%; ACL +36bps. CRL-12 77→55%. KB-CARL-243/244. | Apr 21 | 🟠 headline / 🔴 cohort |
| COF Q1 2026 | Card NCO **5.1%** clean; Auto +21% YoY originations w/ "slightly higher subprime mix" admitted; $230M ACL build. ALLY-pattern confirmed. KB-CARL-245/246. | Apr 21 | 🟠 Card / 🔴 Auto composition |
| Total Household Debt | **$18.78T record** | Q4 2025, NY Fed | 🔴 |

### Housing / Multifamily
| Metric | Value | As Of | Status |
|--------|-------|-------|--------|
| Fannie MF DQ | **0.74%** (6bps from GFC) | Feb 2026, Fannie | 🔴 |
| FHA DQ | **11.52%** vs Conv 2.89% | Q4 2025, MBA | 🔴 |
| 30-Yr Mortgage | **6.30%** PMMS Apr 30 — easing thread REVERSED (round-trip 6.30 Apr 17 → 6.23 Apr 24 → 6.30 Apr 30); MBA contract **6.37% (+2bps)** wk Apr 24, jumbo/large-balance pricing pressure. Iran-shock + UMich un-anchoring back-up. KB-CARL-272. | Apr 30, Freddie PMMS | 🟠 |
| MBA Purchase Apps | **+1.1% WoW (wk Apr 24)** — Composite -1.6% (after prior +7.9% mass-refi-pop), Refi -4.4% (refi window collapsed). Rate easing window opened-and-shut. KB-CARL-272. | Apr 24, MBA | 🟠 |
| NAHB HMI Apr | **34** (-4pts from 38 Mar, 7-mo low, 24th consec mo <50). Future Sales **42** (-7pts). Tariff cost +$10,900/home (60% builders report). | Apr 15, NAHB | 🔴 (breaches <40 threshold) |
| Rent Growth Negative | **56% of top 100 cities** | Jan 2026, Apollo/Slok | 🟠 |
| Median Homebuyer Age | **59** (was 31 in 1981) | Mar 2026, Apollo/Slok | 🔴 |
| Foreclosures Q1 2026 | **118,727 filings** (+6% QoQ, **+26% YoY**). **Q1 REO 14,020 (+45% YoY) — PIPELINE CONVERTING, not just accumulating.** Mar monthly: 45,921 filings (+18% MoM, +28% YoY); REO 5,229 (+28% MoM). | Apr 16, ATTOM | 🔴 |
| Existing Home Sales | **3.98M SAAR** (-3.6% MoM, lowest since Jun, approaching <4.0M RED) | Mar 2026, NAR | 🔴🔴 |
| **Case-Shiller National Feb** | **+0.7% YoY** (down from +0.8%); 20-City -0.1% MoM (MISS). **Real prices negative 9 consec months.** Worst: Denver -2.2%, Tampa -2.1%, Seattle -2.0%. Geographic broadening beyond Sun Belt (LA + DC newly joining). KB-CARL-261. | Apr 28 | 🔴 |
| CMBS MF DQ | **7.15% NEW ATH** (+30bps MoM; shadow rate 9.07%) | Mar 2026, Trepp | 🔴🔴 |
| FL Condo Inventory | **13.2 months** (condo prices -6.1% YoY, 92% declining) | Q1 2026 | 🔴🔴 |
| 90+/FC Pipeline | **878K** (+175K/25% in 4mo, cure -40%) | Feb 2026, MBA | 🔴🔴 |
| FL Foreclosures | **Q1 REO 1,014 (+108% YoY vs 487 Q1'25)** — GREATEST % RISE NATIONALLY. Q4'25 filings +190% YoY. Active completion wave, not pipeline. | Q1 2026, ATTOM | 🔴🔴 |
| Nat'l State Leaders Q1 | **TX 10,617 FC starts #1; FL 10,099 #2**. Top rates: IN 1/739 HU, SC 1/743, FL 1/750. | Q1 2026, ATTOM | 🔴 |
| "Help with mortgage" | **ALL-TIME HIGH** | Mar 2026, Google | 🔴🔴 |
| Lennar Gross Margin | **15.2%** (lowest since 2010) | Q1 FY2026, LEN | 🔴 |
| **DHI Q2 FY2026** | GM **20.1%** (litigation/warranty benefit + cost control, NOT pricing recovery). ASP $361,600 (-3% YoY); cancellations 16% (mortgage qualification failure); FY26 closings trimmed -500. **Tariff $10,900/home = FY27 hit (CRL-23).** | Apr 21 | 🔴 |
| **PHM Q1 2026** | GM **24.4% MISS** (-310bps YoY); incentives 10.9% (+290bps YoY); Q2 guide compression. **Mgmt names "K-shape" explicitly:** active adult +14%, first-time flat. CRL-23 anchor. | Apr 23 | 🔴 |
| Non-Bank Servicer Stress | **PennyMac FHA DQ 7.5%** (+160bps QoQ); loanDepot $107.5M loss; Lakeview 18% / Freedom 15.5% (stale). **Rithm Q1 2026 (Apr 28): "DQ will reverse" claim QUIETLY DROPPED** → "stable + FHA flatten via mod-accounting normalization." Mod-accounting cushion = optical DQ smoothing 12-24mo before underlying stress visible. PennyMac differential = next bridge test. Detail: KB-CARL-202 (→HMR-065), 257. | Apr 28 + Apr 13 | 🟠 |

### Insurance / Healthcare *(K-shape Selection transmission — POLLY tracks broader domain)*
| Metric | Value | As Of | Status |
|--------|-------|-------|--------|
| **UNH Q1 2026** | MCR **83.9%** — no MLR breach. MA membership **-965K Q1** (FY guide ~-1.3M loss). MA cost trend ~10% embedded in 2026 pricing (vs historical 3-5%). FY adj EPS guide raised >$18.25. DOJ investigation ongoing. CRL-22 anchor. | Apr 21 | 🟠 margin / 🔴 culling |
| **ELV Q1 2026** | BCR **86.8%** — no breach. Adj EPS $12.58 BEAT. $935M one-time CMS accrual (RA dispute, compliance Jul 31). Bronze-plan ACA shift = high-deductible trap activating. FY guide raised >$26.75. CRL-22 anchor. | Apr 22 | 🟠 margin / 🔴 Vector #12 transmission |
| **ALL Q1 2026** | Combined ratio **82.0** (vs 97.4 prior year). Cat losses $1.0B (-$778M YoY). Homeowners flipped -$451M loss → +$685M profit; CR 83.5; avg premium +5.7% YoY. Adj NI $2.8B / $10.65 EPS. POLLY-P05 confirmed (joins PGR 86.4 + TRV 88.6). Note: Q1 cat-light, Q3 hurricane season is true test. KB-CARL-266. | May 1 | 🟢 (Q1) ⚠️ Q3 test |
| Auto Insurance CPI | **0.8% YoY** Mar (flat MoM, down from 5.9% Feb / 19.8% Jun 2023 peak). Hard market for personal lines effectively over. KB-CARL-267. | Mar 2026 BLS | 🟢 ⚠️ |
| Tenants' & Household Insurance CPI | **7.4% YoY** Mar (+0.9% MoM) — still elevated; renter cohort cost-squeeze continues. KB-CARL-267. | Mar 2026 BLS | 🟠 |
| CA FAIR Plan | **684,388 policies** Mar 2026 (ATH, $750B exposure, 35.8% rate hike requested) — structural market failure amplifier. POLLY-P02 anchor. | Apr 17, POLLY | 🔴 |

### Macro / Energy / Stress
| Metric | Value | As Of | Status |
|--------|-------|-------|--------|
| Gas Pump | **$4.446 national** (May 3 AAA — +1.3¢ overnight, +34.7¢ WoW, +40.2% YoY). **Gap to CRL-08 $4.50 = $0.054; deceleration trio +9.2/+4.1/+1.3¢ + Brent -5% Fri = NEAR-BREACH NOT-YET.** Top: HI $5.634, CT $4.518, DC $4.484, NJ $4.417, VT $4.416. Detail: KB-CARL-259/264/268. | May 3, AAA | 🔴🔴 |
| Diesel | **$5.642 national** (May 3 AAA — +1.5¢ vs May 2 $5.627, +53.4% YoY). Diesel/gas day-on-day moves now both single-digit cents = gap compression sustaining. KB-CARL-253 freight-demand thread further weakening pending May 7 EIA. | May 3, AAA | 🔴 |
| Brent | **$108.17 May 2 close** (-$5.84 / -5.12% on Iran peace proposal; single-largest daily drop since cluster intensified). Pulled back from $107-110 May 1. Detail: KB-CARL-240/248/258/269. | May 2 close | 🔴🔴 |
| WTI | **$101.94 May 2 close** (-$3.13 / -2.98%). **Brent-WTI spread $6.23 — WIDENED from $2-4 May 1 = physical-spot tightness mechanism RELAXED.** Spread regime change is the most actionable single finding (KB-269). | May 2 close | 🔴 |
| **Qatar LNG** | **~80 MTPA OFFLINE = ~20% global LNG supply** (Iranian drone strikes Ras Laffan Mar 2/18-19; QatarEnergy FM extended). TTF EU gas +50%, JKM Asia LNG +39%. Supports diesel elevated + distillate tightness. | Apr 19 | 🔴🔴 |
| **Iran Cluster Resolution** | **STILL LIVE May 3** — bidirectional firing simultaneously: (a) Iran state media submitted new peace proposal (triggered Brent -5% Friday); (b) Trump announced US Navy Hormuz ship-escort initiative ("doubles down on blockade to choke Iran's oil exports"); WPR May-1 expired no statutory pause (admin: hostilities "terminated" Apr 7); Iran warns $140 oil; Pakistan oil imports +167% since cluster start; net supply loss est 9M bpd. Neither de-escalation nor escalation resolved. Detail: KB-CARL-240/242/248/258/269. | May 3 | 🔴🔴 |
| HY OAS | **294bps Apr 10 — STALE 23d, FRED + secondary fetches all blocked May 3.** Iran cluster + 8-session Brent streak almost certainly widened spreads beyond Apr 10 reading. Awaiting fetch path resolution. | Apr 10, FRED ⚠️STALE | 🟡 PENDING REFRESH |
| CPI Energy YoY | **+12.5%** (+11.9% MoM index jump) | Mar 2026, BLS | 🔴 |
| Savings Rate | **3.6%** Mar (↓40bps from Feb 4.0%; matches Dec 2025 trough = 2008 stress profile). Buffer-exhaustion regime. PCE +0.9% MoM nominal DESPITE Real DPI -0.1% = forced consumption funded by savings depletion. KB-CARL-270. | Mar 2026, BEA | 🔴🔴 |
| Urea cash | **$585/T May 1** (-15% MoM from Q1 peak; +24% YoY). Triangulated path: $475 pre-cluster (early Mar) → $690s late Mar (+47% AFBF) → $585 May 1 (~50% retraced). Mechanism damage already done — plantings determined, under-application locked. KB-CARL-275/276. | May 1, tradingeconomics | 🟠 (down from 🔴🔴) |
| **AFBF Fertilizer Survey Apr 14** | 5,700+ farmers Apr 3-11: **70% can't afford full fertilizer needs** (S 78%/NE 69%/W 66%/MW 48%); ~60% worsening finances; pre-booking Midwest 67% / South 19% — most volatile since Russia 2022 invasion. KB-CARL-275. | Apr 14, AFBF | 🔴🔴 |
| Russia AN | **SUSPENDED** Mar 24 (binary; news scan May 3 — sources blocked, status unverified post-Mar 24). Flag for next session. | Mar 2026 ⚠️UNVERIFIED | 🔴 |
| USDA Wheat Acres | **43.775M — LOWEST SINCE 1919** (107-year low). Locked in for 2026/27 harvest. | Mar 31, USDA | 🔴🔴 |
| USDA Corn Acres | **95.338M** (-3.45M/-3.5% YoY). Locked in for 2026/27 harvest. | Mar 31, USDA | 🟠 |
| **CBOT Wheat Futures** | **$624.50/Bu (+23.18% YTD)** May 3 — market pricing locked-in 2026/27 supply tightness 6-9mo ahead. Corn $468.25 (+6.36% YTD); Soy $1,187.75 (+15.26% YTD). KB-CARL-276. | May 3, tradingeconomics | 🔴 |
| **Food CPI Headline** | **2.7% YoY Mar 2026** (DECEL from Feb 3.1%) — supply-side stress NOT YET on grocery shelves; consistent with 1973 analog 6-12mo lag. CRL-10 timeline intact (>4% by Q4 2026, 70%). KB-CARL-277. | Mar 2026, BLS | 🟠 |
| JOLTS Ratio | **0.91 INVERTED & DEEPENING** | Feb 2026, BLS | 🔴🔴 |
| Unemployment Duration | **25.7 wks** (4-yr high) | Feb 2026, BLS | 🔴 |
| UI Exhaustion Hole | **$650M/mo** (peak $930M/mo July) | CARL est, Mar 31 | 🔴🔴 |
| Core PCE Monthly | **3.2% YoY Mar** (+0.3% MoM, +20bps from Feb 3.0% — acceleration confirmed). CRL-19 RESOLVES direction-correct / magnitude-light (predicted 3.3-3.5%, actual 3.2% = 10bps below floor). Headline PCE 3.5% YoY. KB-CARL-270. | Mar 2026, BEA | 🔴 |
| CPI Headline Mar | **+3.28% YoY, +0.86% MoM** (hot headline, gas/food pass-through) | Mar 2026, BLS | 🔴 |
| CPI Core Mar | **+2.61% YoY, +0.21% MoM** (contained — supply-side inflation, not demand) | Mar 2026, BLS | 🟠 |
| PPI Headline Mar | **+4.0% YoY, +0.5% MoM** (highest since Feb 2023; gasoline MoM +15.7% drove ~½ of monthly jump) | Mar 2026, BLS | 🔴 |
| PPI Core Mar | **+3.8% YoY** (also highest since Feb 2023) | Mar 2026, BLS | 🔴 |
| PPI Core-Core Mar | **+3.6% YoY, +0.2% MoM DECELERATING** (ex food/energy/trade — services MoM ~0%; goods+energy shock, NOT broad) | Mar 2026, BLS | 🟠 |
| UMich 1Y Inflation Exp | **4.7%** Final (vs prelim 4.8%, vs Mar 3.8% — +90bps MoM, largest one-month jump since Apr 2025) | Apr 2026 Final, UMich (Apr 24) | 🔴 |
| UMich 5-10Y Inflation Exp | **3.5%** Final (vs prelim 3.4% — un-anchoring DEEPENED on Final, highest since Oct 2025, Fed red line breached) | Apr 2026 Final, UMich (Apr 24) | 🔴🔴 |
| **ISM Manufacturing PMI Apr** | Headline **52.7** (4th mo expansion) BUT **Prices Paid 84.6 HIGHEST SINCE APR 2022** (+6.3pp), Employment 46.4 deepening contraction, Export Orders 47.9 contraction, 47% of respondents mention tariffs, sentiment 2.2:1 negative. Quotes: "impossible to absorb 15-25% China tariff" + "fuel increases coming." Stagflation in sub-component form. | May 1 ISM | 🔴 (sub-component) / 🟢 (headline mirage) |
| **GDP Q1 2026 NIPA (advance)** | Real **+2.0%** (vs 2.3% cons / 1.3% GDPNow Apr 7); PCE Price **+4.5% ann.**; Core PCE **+4.3% ann.**; GDP Price (gross dom. purch.) **+3.6%**. K-shape composition: residential + non-residential structures drag, healthcare-led PCE. Vector #12 hardened — realized > UMich 5-10Y 3.5%, Fed pure-locked. Detail: KB-CARL-254/255. | Apr 30 BEA | 🔴🔴 |
| GDP Q4 2025 | **0.5%** (revised down from 0.7% Apr 30 annual revision) | Apr 30 BEA | 🔴 |
| Tariff Burden | **~$1,500/HH annual** (eff rate 13.7%, peak impact Apr-Oct 2026) | Apr 2026, Tax Fdn | 🔴 |
| UMich Sentiment | **49.8 RECORD LOW Final** Apr (revised UP from 47.6 prelim; barely below prior ATL 50.0 Jun 2022). Current Conditions 52.5 / Expectations 48.1. KB-CARL-204/241. | Apr 24 Final | 🔴🔴 |
| CB Expectations | **72.2 Apr** (+1.2 from 70.9 Mar — STILL <80 RECESSION WARNING, 4 consec months). Headline 92.8 (+0.6); Present Situation 123.8 (-0.3). UMich/CB divergence: bottom-cohort sentiment collapsing (UMich 49.8), top-cohort merely soft. KB-CARL-273. | Apr 2026, CB | 🟠 |
| Retail Sales MoM | **+1.7% Mar** (vs cons +1.4%) — strongest since Mar 2025; gas station receipts **+15.5% record** = Iran-shock pump pass-through; tax refund pull-forward broad-based. KB-CARL-271. | Mar 2026, Census | 🟢 ⚠️ |
| Real Consumer Spending | **+0.2% Mar** (Real PCE — barely positive despite +0.9% nominal). Savings-funded forced consumption. KB-CARL-270. | Mar 2026, BEA | 🔴 |
| Real DPI | **-0.1% Mar** (4th NEGATIVE month sustaining; nominal DPI +0.6% but PCE deflator +0.7% MoM = real income shrinking). KB-CARL-270. | Mar 2026, BEA | 🔴🔴 |
| Retail Control Group | **+0.7% Mar** (vs cons +0.2% — beat by 50bps); 15.5% gas station distortion explains majority of headline beat. KB-CARL-271. | Mar 2026, Census | 🟢 ⚠️ |
| **NFP Mar** | **+178K** (cons +57K) — Scenario 1 headline / Scenario 2 internals | Apr 3, BLS | 🟢 ⚠️ |
| Feb NFP Revision | **-133K** (revised down from -92K, -41K revision) | Apr 3, BLS | 🔴 |
| 3-Mo NFP Avg | **~68K/mo** (well below 150K breakeven) | Apr 3, CARL calc | 🔴 |
| Unemployment Rate | **4.3%** (from 4.4% — BUT LFPR fell to 61.9%, lowest since Nov 2021) | Mar 2026, BLS | 🟠 ⚠️ |
| LFPR | **61.9%** (labor force shrank ~396K — discouraged workers exiting) | Mar 2026, BLS | 🔴 |
| AHE YoY | **3.5%** (lowest since May 2021, barely above PCE 3.1%) | Mar 2026, BLS | 🟠 |
| Avg Weekly Hours | **34.2** (-0.1 — hours cut = leading layoff indicator) | Mar 2026, BLS | 🟠 |
| Part-Time Econ Reasons | **4.5M** | Mar 2026, BLS | 🟠 |
| Long-Term Unemployed | **1.8M** (25.4% of total, +322K YoY) | Mar 2026, BLS | 🔴 |

---

## CONVERGENCE MATRIX *(mirror — canonical in `thesis/THESIS.md`)*

**v2.5 score definition:** 5 = fully fired, no further upside in mechanism. 4 = firing, room to escalate. 3 = watching, elevated. 2 = mildly relevant. 1 = not active. **Currently 0 vectors at 5.**

| # | Vector | v2.4 | v2.5 | Current |
|---|--------|------|------|---------|
| 1 | CC 90+ DQ → GFC | 4 | **4** | 12.70% = 92% of GFC; 1.04pp gap. |
| 2 | Subprime Auto 60+ | 5 | **4** ⬇️ | ATR 6.9% Jan; cure collapse 3 trusts. **Strict-def fix:** EART Class E terminal but AMCAR/SDART have cushion. |
| 3 | Fannie MF DQ → GFC | 4 | **4** | 0.74% Feb (6bps from peak); March data late Apr. |
| 4 | Student Loan 90+ | 5 | **4** ⬇️ | 9.6% NY Fed / ~9.8% FICO Spring; cascade EXECUTING; room to escalate to 12-15%+. |
| 5 | Gas Price Squeeze | 5 | **4** ⬇️ | $4.446 May 3; CRL-08 92% NEAR-BREACH ($0.054 gap, deceleration trio); room to $5+. |
| 6 | UI Exhaustion Wave | 5 | **4** ⬇️ | FL Wave 1 fired. Wave 2 surface counter-thesis (initial claims declining); exhaustion mechanism unverified pending DEO continued + DOL ETA. |
| 7 | FL Triple Squeeze | 4 | **4** | Condo inv 13.2mo; FL Q1 REO +108% YoY nationally. |
| 8 | K-Shape Converging *(merged 8+9, two-step)* | 5+5 | **4** ⬇️ | Both cohorts deteriorating. Step 1: merger eliminates double-count. Step 2: magnitude-not-2008-quantified. |
| 10 | Foreclosure Acceleration | 5 | **4** ⬇️ | Q1 ATTOM REO +45% YoY; FL +108%. *2025 base partially pandemic-suppressed; 2019 absolute PENDING_VERIFY.* |
| 11 | SB Bankruptcy + Owner Income | 4 | **3** ⬇️ | SubV +67% YoY breached; SBA defaults 12-yr high; income est $73-145B. |
| 12 | Stagflation Trap / Fed Locked | 5 | **4** ⬇️ | UMich 5-10Y 3.5% un-anchored; Q1 NIPA Core PCE +4.3%; ISM Prices Paid 84.6. *TTM not yet crossed; UMich triangulation PENDING_VERIFY.* |
| 13 | **Federal Fiscal Capacity Stress** *(NEW v2.5)* | — | **3** | Watching — TGA dynamics, debt ceiling, term-premium pressure; restrained but not at crisis. |
| 14 | **Upper-Decile Wealth Stress** *(NEW v2.5)* | — | **3** | Watching — RV crash + retail-investor pullback are early signals; SPX still near highs; magnitude not 2008-quantified. |
| 16 | **Employment Structural Rot** *(NEW v2.5)* | — | **4** | JOLTS 0.91 inverted, LFPR 61.9%, 3-mo NFP avg 68K, hires 3.1%, duration 25.7wk. |

V9 merged into V8 (May 1). V15 Refi-Window dropped (RED domain).

### Score histogram

| Score | Vectors | Count | Sum |
|-------|---------|-------|-----|
| 5 | (none) | 0 | 0 |
| 4 | V1, V2, V3, V4, V5, V6, V7, V8, V10, V12, V16 | 11 | 44 |
| 3 | V11, V13, V14 | 3 | 9 |
| **Total** | **14 vectors** | **14** | **53/70** |

**Total: 53/70 (76%) → 🔴🔴 CRITICAL.** Critical vectors avg 3.9, supporting avg 3.0, spread 0.9 — score now actually discriminates. May 1 v2.5 promotion: ~60% calibration (matrix expansion + 5-def tighten + V8/V9 merge) + ~40% legitimate conviction reduction (V6/V8/V12 honest downgrades). Prior 58/60 was probably overconfident; 53/70 closer to true conviction we should have had all along. Path C ACTIVATING-RED → ACTIVE-RED (provisional). Cross-industry data masking promoted to thesis-level methodology with CRL-21 (Q3'26) + CRL-20 (Q1'27) falsification windows. Counter-Evidence section stripped, staged for RED in `handoff_RED/`.

---

## THESIS

**"Beneath the Ice" v2.5.1 — 60% structurally fragile, multi-vector cost squeeze is the mechanism.** Canonical: `thesis/THESIS.md`.
- 37% can't cover $400 | 62% paycheck-to-paycheck | JOLTS inverted (0.91, Feb 2026)
- **Mechanism:** Employment didn't break acutely — multi-vector cost squeeze (energy + food + UI exhaustion + tariff pass-through) grinding the bottom 60%. K-shape converging downward (both cohorts stressed). Subsidence, not earthquake.
- **Paths:** A (Employment→Subprime, SLOW), B (SPX→Wealth effect), **C (Housing→Banks, ACTIVE-RED provisional)**, F (AI→Prime mortgage), PC (Private credit→Middle-market)
- **Cross-industry data masking framework** (4 issuers: ALLY, COF, SYF [ACL-only caveat], RITM) — composition/securitization/accounting-driven optical clean. Falsification windows: CRL-21 Q3 2026 intermediate / CRL-20 Q1 2027 outer.
- **K-shape Selection + Tariff Transmission (sibling, v2.5.1):** UNH/ELV (membership culling + pricing-cycle risk → CRL-22), DHI/PHM (FY27 builder GM compression on tariff timing → CRL-23). Distinct from masking — these are mechanism-confirmed transmission tests, not falsifications.

---

## DANGER WINDOW: Q2-Q4 2026

| Window | Trigger | Status |
|--------|---------|--------|
| **NOW (May 3)** | Iran cluster bidirectional (peace proposal + Hormuz escort blockade — Brent $108.17 -5.12% Fri); CRL-08 gas $4.446 NEAR-BREACH NOT-YET (gap $0.054, deceleration trio + Brent pullback widens timing distribution); v2.5.1 thesis refinement complete | 🔴🔴 **OIL BREAKOUT / CONSUMER STAGFLATION** |
| **Recently fired (last 30d)** | Apr 15 Sweet v. McMahon ✅ (~271K pipeline) • Apr 21 SYF/COF/UNH/ELV/DHI/PHM ✅ (3-way K-shape WIDENING confirmed, KB-CARL-243-247) • Apr 21 Iran ceasefire ✅ (binary unresolved → oil breakout) • Apr 24 UMich Final 49.8 ✅ (5-10Y 3.5%) • Apr 26 FL UI Wave 2 🟡 PARTIAL (initial claims surface counter-thesis; exhaustion mechanism = LABOR/GIG spawn, KB-CARL-262) • Apr 28 Case-Shiller Feb ✅ + Rithm Q1 ✅ (KB-CARL-257/261) • **Apr 28-29 FOMC ✅ HELD 3.50-3.75% w/ 4 dissents most since 1992 (KB-274)** • Apr 30 BEA Mar PCE ✅ (Real DPI -0.1%, Savings 3.6%, Core PCE 3.2% YoY, KB-270) • May 1 ALL Q1 ✅ POLLY-P05 confirmed (CR 82.0, KB-266) • **May 3 CRL-19 RESOLVED MIXED** (Mar Core PCE 3.2% vs predicted 3.3-3.5%, direction-correct/magnitude-light) | — |
| **Late Apr/May** | PennyMac Q1 — FHA DQ >7.5% bridge test on Rithm mod-accounting framework | 🟠 |
| **May 5** | PayPal Q1 (new CEO Lores) — PHAN owns | ⏳ |
| **May 6-8** | Earnings cluster: Uber+DoorDash (May 6) / Dave+Lyft+Affirm (May 7) / BLS Apr NFP (May 8) | ⏳ |
| **May 13** | BLS Apr CPI — first full Iran-shock + tariff month | ⏳ |
| **May-Jun** | DQ conversion (Mar/Apr stress → May/Jun spike) + middle-market PC cuts | 🔴 UPGRADED |
| **~Mid-May** | NY Fed Q1 HHDC — CC 90+ DQ vs 12.7% / CRL-05 test | ⏳ |
| **May 28** | AFT/MOHELA status conference (discovery) + BEA Q1 GDP 2nd est (CRL-18) | 🟠 |
| **Jun 16-17** | **FOMC + SEP** — first dot-plot post-Iran-shock + un-anchoring Apr Final UMich 5-10Y 3.5%; 4-dissent April pattern carries forward (KB-274) | 🔴 |
| **Jun 24** | FL Wave 1 UI exhaustion cliff (~4,500 workers) | 🔴 |
| **Jul 1** | **SAVE → RAP transition** — 7.5M forced into new plans | 🔴 |
| **Jul** | Involuntary collections restart (AWG + Treasury Offset) — 5M+ defaulted borrowers | 🔴 |
| **Jul-Aug** | FL exhaustion peak ($7.4M/mo hole) + national peak ($800M-$930M/mo) | 🔴🔴 |
| **Q2-Q3** | Food CPI spike (triple nitrogen seizure) | 🔴🔴 |
| **Q2-Q3** | **ABS subordinate tranche rating actions** — EART Class E CE breached; AMCAR Class E ~2mo; SDART Class D ~7mo. Downgrades trigger forced selling. | 🔴 |
| **Q2-Q3** | **Non-bank servicer stress window** — Ginnie advance drain cumulative; loanDepot most vulnerable. GAO: no stagflation test. | 🟠 |
| **Q3** | **CONSUMPTION STRESS QUARTER** — UI exhaustion + gas + food CPI converge | 🔴🔴 UPGRADED |
| **Q4+** | Foreclosure acceleration | PROJECTED |

---

## CROSS-AGENT LINKS

| From | Key Signal | As Of | Status |
|------|-----------|-------|--------|
| LABOR | JOLTS 0.91 inverted, hires COVID-low 3.1%, duration 25.7wk, **NFP Mar +178K (headline) but Feb revised -133K, LFPR 61.9%, 3mo avg 68K**, DOGE 260K+ (fed govt -18K in Mar) | Apr 3 | 🔴🔴 |
| FOMC | **Hold 3.50-3.75%** Apr 28-29 (3rd consec hold). **4 DISSENTS — most since Oct 1992** (Miran -25bps + 3 others objected to forward language). Consensus hold through Q2. Fed signaling openness to **HIKES if inflation persists** = locked + hawkish-leaning, not just locked. Next: **June 16-17 (SEP)**. KB-CARL-274. | Apr 28-29 | 🔴🔴 |
| MARCO | ICE 1,100+/day, remittances -4.6%, Miami outmigration -2.0% | Mar 26 | 🔴 |

---

## PREDICTIONS

*Canonical source: `thesis/PREDICTIONS.tsv`. Changes logged in `thesis/CHANGELOG.md`. IDs below match TSV.*

**Resolved:**
| ID | Prediction | Status |
|----|-----------|--------|
| CRL-01 | Gas pump peak stress Mar 14-21 | ❌ MISSED (direction right, magnitude wrong) |
| CRL-02 | Subprime Auto 60+ DQ >7.0% | ✅ CONFIRMED* (6.9% ATR, at threshold) |
| CRL-19 | Mar Core PCE accelerates Feb 3.0% → 3.3-3.5% | ⚠️ MIXED — direction correct (3.2% confirms acceleration), magnitude light (10bps below 3.3% floor). KB-270. |

**Legacy confirmed (pre-TSV, not re-numbered):**
- CC 90+ >2019 peak ✅ | FL Foreclosures +100% YoY ✅ | Hardship 401k >5.5% ✅

**Open:**
| ID | Prediction | Conf | Timeframe | Current |
|----|-----------|------|-----------|---------|
| CRL-03 | Fannie MF DQ >0.80% (GFC) | 90% | Q2 2026 | 0.74% Feb — hovering 6bps from target |
| CRL-04 | Student 90+ DQ >10% | 95% | Q1-Q2 2026 | **~9.8% FICO Spring 2026** (up 25% from 7.9% Apr 2025). 9.2M default, 2.4M late-stage DQ. **Near-confirmed, breach likely Q2.** |
| CRL-05 | CC 90+ DQ >13.74% (GFC) | **82%** | Q2-Q3 2026 | 12.70% — 1.04pp gap. **Apr 17 (PM): 85→82%** on ALLY Q1 counter-evidence — near-prime auto headline clean 5 consec qtrs. Audit found composition-masking not fraud (KB-CARL-223). SL cascade pathway intact. |
| CRL-06 | Foreclosures >70K/qtr | 70% | Q2 2026 | 58,140 Q4 — needs +20% |
| CRL-07 | FL UI exhaustion → DQ spike | 85% | Jun-Aug 2026 | LABOR model confirms timeline |
| CRL-08 | Gas $4.50+ national avg | **92%** | May-Jun 2026 | **May 3 AAA: $4.446** (+1.3¢ overnight, +34.7¢ WoW, +40.2% YoY). Gap to threshold $0.054. **Deceleration trio May 1-3:** +9.2¢ → +4.1¢ → +1.3¢ (partial weekend effect; May 2 Sat + May 3 Sun lag). **Counter-pressure:** Brent -5.12% Fri May 2 close ($108.17) on Iran peace proposal — 3-4d transmit lag suggests pump softening Mon-Wed. Disposition NEAR-BREACH NOT-YET; held 92% (no reprice without 2-week sustainability test post-cross). 92% set May 1 on accelerated pass-through (Brent breakout transmitted in 3-4d vs 2-4wk typical). Capped below 95% by: (a) Iran peace proposal acceptance → Brent to $80-90 → pump retreat (10-15% scenario), (b) demand destruction $4.50+ behavioral breakpoint, (c) Trump WPR resolution pressure for de-escalation. |
| CRL-09 | JOLTS Mar ratio <0.88 | 75% | May release | Feb was 0.91, pre-Iran |
| CRL-10 | Food CPI YoY >4.0% | 70% | Q4 2026 | Wheat 107yr low, urea $690s |
| CRL-11 | Hires rate ≤3.2% through Q2 | 85% | Jul/Aug releases | Currently 3.1% COVID-low |
| CRL-12 | SYF FY2026 NCO >6.0% (guidance ceiling) | **55%** | FY2026 (Jan 2027) | Q1 NCO 5.42%, FY guide CUT to <5.5%. Apr 29: 77→55%. Survivor-pool not recovery (Home & Auto -3.7%, ACL +36bps). |
| CRL-13 | SAVE non-selection rate >35% | 70% | Oct 1 2026 | NEW — 2.6M+ face $0→$407/mo cliff |
| CRL-14 | MOHELA-caused defaults >500K from Jul 1 | 65% | Q3-Q4 2026 | NEW — servicer capacity near-zero for clean transition |
| CRL-18 | Q1 GDP second estimate revises advance 2.0% down 0.2-0.4pp to 1.6-1.8% | 60% | May 28 2026 | NEW May 1 — pattern basis Q4 cumulative -0.9pp |
| CRL-20 | ≥3 of {ALLY, COF, SYF, RITM} show NCO/DQ acceleration breaking "headline clean" pattern | **75%** | Q1 2027 | **NEW v2.5 — outer falsification window for cross-industry data masking framework.** Specific: ALLY consumer auto NCO ≥+30bps QoQ for 2 consecutive quarters; COF Card NCO ≥+25bps QoQ for 2 consecutive quarters; SYF NCO breaks above FY26 ceiling 5.5%. Failure → masking thesis invalidated, CONTAINMENT validated. |
| CRL-21 | NCOs at ALLY/COF/SYF visible inflection by Q3 2026 + vintage projections ≥+50bps over FY2023 baseline | **60%** | Q3 2026 | **NEW v2.5 — INTERMEDIATE falsification, addresses 12-24mo unfalsifiability tail risk.** Specific: ALLY consumer auto NCO ≥+30bps QoQ for 2 consecutive quarters OR vintage projections diverge above FY2023 ≥+50bps. **POSITION-ACTION COMMITMENT on failure:** confidence -25-30pp + trim short positions 25% + extend duration to Q2 2027+. |
| CRL-22 | Insurer MLR re-acceleration (UNH/ELV) — MA cost trend ≥10% in FY27 pricing OR MLR breach | **60%** | FY27 (early 2027) | **NEW v2.5.1 — K-shape Selection transmission test, NOT masking falsification.** UNH MA -965K Q1 culling + ELV $935M CMS accrual = pricing-cycle risk + regulatory contingency mechanism. Distinct from masking framework. |
| CRL-23 | FY27 builder gross-margin compression (DHI/PHM) — tariff $10,900/home pass-through hits FY27 GM ≥-200bps | **70%** | FY27 (early 2027) | **NEW v2.5.1 — Tariff Transmission test, NOT masking falsification.** Tariff timing = mechanical inventory cost-flow, not management choice. DHI Q2 GM 20.1%, PHM Q1 24.4% MISS already showing compression baseline. |

---

## EXIT RULES
- **Thesis kill:** Claims <220K 8+ weeks AND CC 90+ DQ declines 2 consecutive quarters
- **Time-based:** Q1 consumer earnings (April) = mandatory review → **See `EARNINGS_WATCH_Q1.md` for full calendar + watch metrics**

*Next catalysts (forward-looking only): **May 4** AAA pump weekday refresh (CRL-08 timing) | **May 5** PayPal Q1 | **May 6** Uber+DoorDash + BLS state jobs | **May 7 TRIPLE** Dave + Lyft + Affirm + EIA distillate | **May 8** BLS Apr NFP | **May 13** BLS Apr CPI (Food at Home decomposition extract) | **~May 18** Klarna Q1 | **Mid-May** NY Fed Q1 HHDC (CC 90+ DQ — CRL-05 test) | **May 28** AFT/MOHELA + GDP Q1 2nd (CRL-18) | **Jun 16-17** FOMC + SEP (V12 hawk/dove surprise) | **Jul 1** SAVE→RAP | **$4.50/gal CRL-08 breach watch** | **Q2-Q3** ABS subordinate rating actions | **Q3-Q4 2026** Food CPI loading (CRL-10) | **Q1 2027** ALLY FY2025 vintage loss window*
*Key docs: `thesis/THESIS.md` | `thesis/PREDICTIONS.tsv` | `thesis/CHANGELOG.md` | `workbook/KB.tsv` | `domain/sources/CVNA_FRAUD_WATCH.md` | `workbook/ABS_BASELINE.tsv` | `workbook/STATE_DIFFUSION.tsv`*
