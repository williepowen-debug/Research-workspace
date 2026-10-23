# Idea #2: is energized power capacity the scarce asset?

**Desk:** VULCAN (S3 power, with S5 finance) · **Written:** 2026-10-23, research 16:04–16:30 ET · **Mode:** research only. This is not a trade card: TERRY builds cards and Will approves them (root rule #5).
**Tiers:** T1 = primary source read here (SEC filing, company release, ERCOT deck, own tool output). T2 = named outlet read directly. T3 = search-engine summary or relay. Prices come from `fetch.py` at 16:04–16:05 ET on 10/23, the 10/23 close. Valuation fields come from yfinance at 16:06 ET; these are vendor estimates (T3).

## Bottom line

1. **Power scarcity is real and measurable.**
   - A new US grid connection now takes a median of about 5 years.
   - GE Vernova has gas-turbine contracts and reservations equal to about 5.8 years of its own production.
   - PJM's capacity auctions keep clearing at the price cap and still fall short of target.
   - ERCOT has about 205 GW of large loads eligible for its first study batch alone.
2. **The bond market already prices the right variable, and it is the tenant, not the power.** From 10/13 to 10/22, HYG's vendor prices show:
   - Site bonds backed by Google or AWS leases moved +9 to +26bp.
   - Site bonds leased to CoreWeave moved +74 to +122bp.
   - CoreWeave's own notes moved +82 to +215bp.
3. **The share prices do not separate the two groups.** Over the last 21 sessions every ex-miner fell 23–56%, against −40% for CRWV and −0.9% for SPY. That includes the miners with only investment-grade tenants. The equity trades as one AI-financing basket.
4. **Hidden tenant risk is concentrated.** Applied Digital, Core Scientific and Galaxy have about 1,516 MW contracted to CoreWeave. All of their AI capacity energized today (about 810 MW) is CoreWeave capacity.
5. **Equipment makers have scarcity in their order books but trade at 18–32x forward earnings.** They fell 15–21% in a month. GE Vernova and Vertiv both report on **10/28**, the same morning as the Microsoft and Alphabet capex prints.

## 1. How tight is the constraint now?

| Metric | Latest figure | Date / basis | Source (tier) |
|---|---|---|---|
| US interconnection wait, request → commercial operation | **Median 61 months** for projects built in 2025 (36 months in 2015, 22 in 2008); only 13% of 2000–2020 requested capacity was built | LBNL *Queued Up 2026* (data to end-2025, published Jun-2026) | [LBNL](https://emp.lbl.gov/publications/queued-2026-edition-characteristics) (T3 summary) |
| PJM capacity price, 2027/28 auction | **$333.44/MW-day, at the cap.** Uncapped price would have been $529.80. Short of the reliability requirement by 6,623 MW. 5,100 of the 5,250 MW peak-load increase is data centers | Auction 12/17/2025 | [PJM release](https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2025-releases/20251217-pjm-auction-procures-134479-mw-of-generation-resources.pdf) (T3 summary) |
| PJM, 2028/29 auction (newer) | **$325/MW-day = 100% of own cap; 6,831 MW short** | 7/14/2026 | WATT STATUS P2 (WATT is canonical) |
| PJM, next auction (2029/30) | December 2026; exact day unverified | — | WATT STATUS |
| PJM stress | EEA-1 + demand response 10/13–14. FERC rejected the curtail-large-loads-first plan 10/9. Backup-generation authority unused 10/13–14 | Oct-2026 | KB-220/255; WATT |
| ERCOT large-load queue | **~205 GW eligible for Batch Zero** (data as of 7/28/2026). Chart labels: 274 GW had no qualifying study; 20 GW had no dynamic model (my reading of the chart labels, total ≈498 GW). The final transmission plan for the batch is expected fall 2027 | ERCOT panel deck 8/19/2026 | [ERCOT PDF](https://www.ercot.com/files/docs/2026/08/19/ERCOTPanel1DataCenters.pdf) (T1, text extracted) |
| ERCOT queue, headline | ~474 GW tracked, ~90% data centers | ERCOT Senate deck 7/29/2026 | [ERCOT](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf) (T3) |
| Large power transformer lead time | **128 weeks** (standard units); generator step-up **>160 weeks by 1Q26** (144 in 2025); ~30% US supply deficit (2025) | WoodMac surveys | [AJOT](https://www.ajot.com/news/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies), [pv-mag 5/11/26](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/) (T3) |
| Gas turbines, GE Vernova | Backlog + slot reservations **116 GW** (from 100 GW in 1Q). Output is 20 GW/yr from 3Q26 and 24 GW in 2028. **116/20 ≈ 5.8 years of output** (VULCAN arithmetic). Target ≥125 GW by end-2026 | Q2 release 7/22/2026 | [GEV 8-K](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm) (T1) |
| Gas turbines, slot dates | A new large order now delivers in about 2031; Siemens Energy says lead times are ">3 years"; MHI orders placed Mar–Jun 2026 deliver 2028–30 | Q2 2026 calls | [Power Eng.](https://www.power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova-power-equipment-orders-as-turbine-slots-tighten-through-2030/) (T3) |
| Chip-side constraint, for comparison | Lam: supply-constrained December quarter; CY2027 WFE ">$200B" vs 2026 "$140B+" | 10/21 | KB-272 (8-K T1; WFE figure from the call, T3) |

**Power is the binding constraint where projects are physically delayed (a WATT read):** IMM counts 4,016.9 MW of PJM data-center growth cancelled OR delayed, ~42% of 9,481 MW forecast growth (KB-255). That is evidence of delay, not lost demand, and should not be read as a glut.

## 2. Energized vs contracted: the ex-miner landlords

| Company | AI capacity energized (critical IT) | Contracted (critical IT) | Named tenants | Site-level financing | Source (tier) |
|---|---|---|---|---|---|
| **APLD** | **250 MW** at Polaris Forge 1, live 10/1/2026. 300 MW expected end-2026 | **~1.41 GW**, ~$36B base-term revenue | PF1 400 MW = **CoreWeave** (~$11B). PF2 = IG hyperscaler (Oracle per Motley Fool, UNVERIFIED). Delta Forge 1/2 + PF3 = "tier-one IG hyperscaler" (unnamed) | ComputeCo 9.25% 2030 ($2.35B); ComputeCo 3 7.00% 2031 ($1.59B, funds PF1 building 3 = CoreWeave); ComputeCo 2 6.75% 2031 (campus UNVERIFIED) | [8-K Ex99.1 10/7/2026](https://www.sec.gov/Archives/edgar/data/1144879/000114487926000057/) (T1) |
| **CORZ** | **>430 MW billing** (mid-July); 395 MW at 6/30 | **~1.1 GW**, >$24B | **CoreWeave ~590 MW** (~$10B+, 12-yr take-or-pay; last ~150 MW early 2027). AMD/neocloud ~530 MW | $3.3B senior secured 2031; **CoreWeave rent paid into the lockbox for those notes** | [Q2 deck 7/28/2026](https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001839341-26-000012/q2fy26earningsdeck728am.htm) (T1) |
| **GLXY** | **133 MW** (Helios Phase I, July 2026) | **526 MW** (800 MW gross); Phase II 260 MW 2Q27, Phase III 133 MW 2028 | **100% CoreWeave**, 15-yr | Helios II $3.5B senior secured 2031 (9.875%) | Q2 8-K 8/5/2026 (T1) |
| **WULF** | **102 MW** at Lake Mariner (July 2026) | 438 MW Lake Mariner by 1H27 + 401 MW Justified (KY) | Fluidstack (**Google credit support $600M effective**), Core42 60 MW, **Anthropic 401 MW** (~$19B, 20-yr, delivery 2H27–1H28) | WULF Compute 7.75% 2030 | [Q2 release 8/5/2026](https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000162/a_wulfearningsreleaseq22026.htm) (T1) |
| **CIFR** | Black Pearl first capacity delivered Aug-2026 (MW not stated). Barber Lake data halls 4Q26–1Q27 | 700 MW gross HPC, $16.6B, 17.3-yr WALT (9/30) | Black Pearl = **AWS** ("IG hyperscale tenant"). Barber Lake amended to a **direct lease with a "leading AI lab"** (unnamed), $9.1B, 20 yrs | Cipher Compute 7.125% 2030 (amortizes with the Google backstop); Black Pearl Compute 6.125% 2031; $850M 0% convert priced 10/13 (conv. $15.31) | [Project Compass deck 10/13/2026](https://www.sec.gov/Archives/edgar/data/1819989/000119312526419743/) (T1) |
| **HUT** | **0 MW AI** (first data halls 2Q27 / 3Q27) | **949 MW**, ~$26.6B | River Bend 245 MW Fluidstack/Anthropic, **Google-backstopped**. Beacon Point 2 leases (incl. 352 MW) with an unnamed "high-IG tenant". Hut 8 says all 949 MW is "IG leased or backstopped" | $7.5B IG non-recourse project notes; $1.07B revolver (9/28) | Q2 8-K 8/4/2026; 8-K 9/28/2026 (T1) |
| **IREN** | Horizon 1 (50 MW IT) accepted by Microsoft Aug-2026; Horizons 2–4 4Q26 | ~200 MW Microsoft, ~$9.7B, 5-yr; $4B contracted ARR for 2026 capacity | **Microsoft** + a "frontier AI lab". **IREN is a GPU-cloud operator, not a landlord: it carries GPU capex and pricing risk** | Convertibles; customer prepayments 45–55% of GPU capex | [FY26 8-K 8/27/2026](https://www.sec.gov/Archives/edgar/data/1878848/000187884826000051/) (T1) |

**A construction-risk tell:** Cipher's Barber Lake estimate-at-completion rose from **$2,157M to $2,941–2,966M (+~37%)**. Half of the costs above $359M are recovered as extra rent, and the company says equipment is "fully secured" (10/13 deck, T1). Holding power rights does not remove build risk.

## 3. Market tape: bonds separate tenants, equities do not

**Site-level secured notes vs CoreWeave, HYG vendor evaluations 10/13 → 10/22.** Computed by VULCAN from DEWEY's committed HYG files. These are vendor marks, not TRACE trades.

| Bond | Tenant behind it | Price 10/13 → 10/22 | YTW change |
|---|---|---|---|
| WULF Compute 7.75% 2030 | Fluidstack + Google backstop | 102.54 → 102.28 | **+9bp** |
| Flash Compute 7.25% 2030 | UNVERIFIED | 99.41 → 98.97 | +13bp |
| Cipher Compute 7.125% 2030 | Fluidstack/AI lab + Google backstop | 99.89 → 99.47 | **+23bp** |
| Black Pearl Compute 6.125% 2031 | AWS | 98.71 → 97.75 | **+26bp** |
| APLD ComputeCo 2 6.75% 2031 | UNVERIFIED (likely PF2, IG) | 96.38 → 95.26 | +36bp |
| Core Scientific Finance 7.75% 2031 | **CoreWeave lockbox** | 95.63 → 93.03 | **+74bp** |
| APLD ComputeCo 3 7.00% 2031 | **CoreWeave** (PF1 building 3) | 94.56 → 92.05 | **+75bp** |
| APLD ComputeCo 9.25% 2030 | **CoreWeave** (PF1) | 104.72 → 102.50 | **+98bp** |
| Galaxy Helios II 9.875% 2031 | **CoreWeave** | 94.64 → 90.55 | **+122bp** |
| Edged Compute 7.5% 2031 | UNVERIFIED | 90.89 → 85.33 | +354bp |
| CoreWeave unsecured (4 notes) | — | −0.8 to −5.3 pts | +26 to +215bp |

A caveat on the CoreWeave 9.625% 2032: it moved only +26bp in these files, while LIQUID recorded 10/16 at 79.21 / 15.15% (KB-270). The 10/13 vendor mark may be stale. The other three CoreWeave notes moved +82 to +215bp. DEWEY's exchange-quote G-spread for CoreWeave is +137bp over 10/13→10/22 (DEWEY §2b). The "+300bp" framing in the brief does not match those windows.

**Equities, `fetch.py` closes 10/23 vs 9/24 (21 sessions) and 9/14 (30 sessions):**

| Ticker | Close 10/23 | 21 sessions | 30 sessions | Main tenant | Fwd P/E · EV/EBITDA (yfinance) |
|---|---|---|---|---|---|
| CRWV | $54.24 | **−39.8%** | −34.6% | (tenant itself) | n/m |
| APLD | $18.25 | −32.6% | −25.8% | CoreWeave (all live MW) | n/m |
| CORZ | $13.10 | −27.7% | −22.8% | CoreWeave (~54% of contracted) | 80x · n/m |
| GLXY | $14.68 | −41.7% | −39.2% | CoreWeave 100% | n/m |
| WULF | $11.32 ⚠️ | −30.5% | −26.8% | Google-backstopped / Anthropic | n/m |
| CIFR | $7.94 | **−56.1%** | −49.2% | AWS / AI lab | 35x |
| IREN | $24.91 | −46.0% | −42.3% | Microsoft | n/m |
| HUT | $61.23 | −39.7% | −32.8% | IG / Google-backstopped | n/m |
| GEV | $814.57 | −14.7% | −6.9% | — | 32.3x · 54.1x |
| ETN | $366.04 | −16.8% | −6.9% | — | 22.5x · 24.7x |
| VRT | $194.30 | −20.8% | −18.2% | — | 21.1x (yfinance); **29.0x on its own 2026 adj-EPS guide midpoint $6.70** · 28.2x |
| ENR.DE (Siemens Energy) | €118.68 | −16.5% | −10.5% | — | 19.0x · 20.9x |
| SU.PA (Schneider) | €231.40 | −20.2% | −14.9% | — | 18.4x · 17.5x |
| 6501.T (Hitachi) | ¥5,562 | +1.2% | +7.8% | — | 31.2x · 13.9x |
| NXT.AX (NextDC) | A$5.61 | −50.8% | −52.1% | — | — |
| SPY | $759.96 | −0.9% | +0.1% | — | — |
| SOXX | $478.20 | −15.5% | −3.8% | — | — |

⚠️ WULF printed $11.32 on both 10/22 and 10/23, on different volume (50.2M vs 35.9M). That is probably a real unchanged close, but a stale bar is possible. Re-check before citing the day change. Hitachi's history is missing 4 Tokyo sessions (holidays). Short interest as a share of float (yfinance) is 17–28% across the miners, including 28% for WULF.

**What the tape says:**
- Credit discriminates by tenant. The Google- and AWS-backed bonds barely moved; the CoreWeave-leased site bonds moved 3–8 times as much.
- Equity does not discriminate. CIFR, IREN and HUT have zero CoreWeave exposure, yet fell as much as or more than APLD, CORZ and GLXY.
- So if the thesis is right, the equity mispricing is in the **IG-tenant names**: the market sells them as CoreWeave proxies. This is an observation, not a recommendation.
- Competing explanations for the IG-tenant names' falls: convert dilution (CIFR's convert priced at $11.34 on 10/13; the stock is now $7.94), development and capex risk, and high short interest.

## 4. Who wins, who is already priced, who carries hidden tenant risk

| Bucket | Names | Why |
|---|---|---|
| **Scarcity owner with an IG or Google-backed tenant** | WULF (Lake Mariner), CIFR (Black Pearl, AWS), HUT (all IG/backstopped, but **0 MW energized until 2Q27**), IREN (Microsoft, but GPU-owner risk) | Bonds already agree that the leases are good (+9 to +26bp). Equity has been sold with the basket. HUT is a contracted-not-energized story, which is the opposite of the scarcity thesis until 2027 |
| **Hidden CoreWeave risk** | **GLXY (100%)**, **CORZ (~54% contracted; ~all billing)**, **APLD (28% contracted, 100% of live MW)** | ~1,516 MW contracted to CoreWeave, ~810 MW of it energized (250 + >430 + 133). CoreWeave's own credit marks: unsecured YTW ~15.2–15.7% (HYG 10/22), 5Y CDS ~1,112bp (KB-278), $10.6B principal due 7/2026–2027 vs $5.5B June cash (KB-249). If CoreWeave stressed, these landlords would hold energized buildings with take-or-pay contracts against a high-yield tenant. The power has re-lease value, but that value cannot be measured here |
| **Scarcity loser (no power yet)** | NextDC; any developer whose grid feed is not built | NextDC: Jemena suspended 66kV works, no restart before Feb-2027, A$140M of FY27 revenue removed, liquidity A$8,675M (KB-261). It is short of electricity, not money |
| **Equipment makers: order books full, multiples full** | GEV (32x fwd, 54x EV/EBITDA), VRT (~29x 2026 guide), ETN 22x, Siemens Energy 19x, Schneider 18x, Hitachi 31x | GEV backlog $176B; Electrification book-to-bill ~1.7; 2026 FCF guide raised to $11.5–12.5B (T1). Siemens Energy FQ3: orders €17.9B, backlog €162B, book-to-bill 1.57 (T3). Schneider Q3 revenue €11.46B, +16.9% organic, guide raised (10/16, T3). Vertiv **stopped disclosing backlog** in the Q2 release (none in Ex-99.1; last disclosed $15.0B at Q4-25, T3) and cited "temporary supply chain congestion". Scarcity is in their numbers. The −15 to −21% month says the multiple, not the order book, is what is moving |

## 5. Falsifiers and dated catalysts

| Falsifier | What would show it | Current state |
|---|---|---|
| Hyperscaler capex **cut** | MSFT/GOOGL 10/28, AMZN (date not announced) cut 2026/27 guides | Opposite so far: META raised its low end to $135–145B (KB-248); TrendForce 9-CSP $957B 2026, >$1.5T 2027 (KB-219). Tesla cut its own capex to ~$20B (KB-263; not a hyperscaler) |
| CoreWeave credit event | Missed rent, a DDTL breach, or lease renegotiation at APLD/CORZ/GLXY | Not observed; CoreWeave Q3 date not announced (modeled ~11/9–11/10, T3) |
| Efficiency lowers MW per unit of compute | Guidance on lower power per token or rack, or lease downsizing | **UNTESTED in this report**; no evidence read either way |
| Glut of announced-but-unenergized capacity | Lease-up of unleased capacity slows (Galaxy 830 MW unleased; Cipher 3.4 GW pipeline; ERCOT ~205 GW Batch Zero); vacancy at energized sites | No energized vacancy observed. IMM 4.0 GW cancelled OR delayed in PJM (delay ≠ glut) |
| Large-load policy | PJM refile after the FERC 10/9 rejection; EL26-67 responses 11/16; ERCOT Batch Zero classification; state orders (e.g. Kentucky EO 2026-494) | A refile that makes new large loads curtailable first would *raise* the value of already-energized sites. A cost-allocation rule that charges existing sites would lower it |
| Community/siting refusal spreads | Loudoun–Amazon (10/20), Jemena–NextDC | This strengthens scarcity for energized sites and hurts developers with unbuilt power |

**Dated catalysts (owner-confirmed unless marked):**

| Date | Event |
|---|---|
| **10/28 pre-market** | GE Vernova Q3 (7:30 ET call; [release 10/13](https://www.gevernova.com/news/press-releases/ge-vernova-announce-third-quarter-2026-financial-results-october-28)) and Vertiv Q3 (11:00 ET call; [10/14](https://investors.vertiv.com/news/news-details/2026/Vertiv-Announces-Date-of-Third-Quarter-2026-Earnings-Release-and-Conference-Call/)). Watch the GW count under contract vs ≥125 GW, Vertiv orders/backlog, any lead-time changes |
| **10/28** | MSFT, GOOGL capex guides (KB-226) |
| 11/3 (T3, unconfirmed) | Eaton Q3 |
| ~11/9–11/10 (modeled) | CoreWeave Q3 (backlog, delay discounts, landlord delivery acceptance) |
| 11/11 (T3, unconfirmed) | Siemens Energy FQ4 |
| 11/16 | EL26-67 responses due (PJM large-load complaint) |
| 11/20 | NextDC AGM; capex review outcome |
| 4Q26 | Cipher Barber Lake data halls 1–4; IREN Horizons 2–4 to Microsoft; WULF CB-4 rent; APLD PF2 first ops (300 MW total) |
| Dec-2026 | PJM 2029/30 auction (WATT; exact day unverified) |

## 6. What we could not reach

- **Secured-note TRACE prints.** All bond figures above are HYG vendor evaluations, which iShares says "may not necessarily be as of the date shown". Tenants behind Flash Compute, Edged Compute and APLD ComputeCo 2 are UNVERIFIED.
- **Q3 2026 releases for APLD and CORZ** are not out. APLD's 10/7 release covers to 8/31 plus later events; CORZ's latest MW figures are mid-July. Galaxy's energized MW is from July.
- **Cipher Barber Lake:** whether Google's backstop survives the direct lease with the "leading AI lab", and which lab it is. Hut 8 Beacon Point's tenant name.
- **Lease economics per MW** (rent $/kW-month) for most landlords. Only CORZ (~$850M a year on ~590 MW) and IREN (>$20M revenue per MW over 3 years, GPU basis) give comparable figures.
- **Current PJM total active queue** (WATT: UNKNOWN). The ERCOT total is my reading of the chart labels.
- **A fresh 2026 WoodMac transformer survey.** The 128-week figure is from 2Q25. Grid-equipment lead times are not in GEV's release.
- **Hitachi and Siemens Energy guidance:** read only through search summaries. Hitachi's Q2 FY26 date is not checked.
- **The MW-per-GPU efficiency falsifier:** not researched.
