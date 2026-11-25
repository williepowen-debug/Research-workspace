# Does AI power demand crack? WATT read, Wednesday November 25, 2026

**Commission:** PROME prome-77, class C9, 11:35 ET; from WALTER's 09:43 ET read to Will and card SIG-W-20261125-017. One bounded session. No trade, card, threshold or score change.
**Question:** is anything in the PHYSICAL or CONTRACTED record of data-centre power demand weakening, or is this week equity repricing only?

## Answer

**Equity repricing, on the record as it stands today.** Over the three chip-led down days (November 20, 24 and 25) the power and grid-equipment names fell 10 to 21%, two to three times the S&P 500 (-6.8%) and about half to nine tenths of the chip index (-23.1%), while regulated utilities were flat to up. Nothing in the contracted or physical record I could reach shows demand weakening since the last utility prints (late October): AEP added 15 GW of signed load commitments in the third quarter, Dominion's data-centre pipeline grew 13% since December, PJM's own commissioned forecast (Charles River Associates, November 2) says the binding limit is power SUPPLY, not demand, and equipment order books were still lengthening at the last prints. The one cut on the record, Exelon's high-probability pipeline 18 to 11 GW, was reported in July and held in October. I found no named US data-centre cancellation, utility load-forecast cut or queue-withdrawal wave dated November 2026 (bounded search, listed below). ⚠️ That is an absence in a bounded search, not proof of absence: the most recent hard prints are a month old, PJM's price feed is dark to this desk, and the next primary tests fall December 10 to mid-February.

## 1. Prices (root rule #4)

Source: `FORGE/tools/market-data/fetch.py price ... --history 8`, pulled 11:39:45 ET November 25 (vendor, Yahoo). November 25 is an INTRADAY bar at about 11:40 ET, not a close; the other days are closes. November 23 (Monday) was a rebound day between the down days.

| Name | Nov 19 close | Nov 20 | Nov 23 | Nov 24 | Nov 25 (intraday) | Three down days compounded | Nov 19 to now | vs SPY, 3 down days (pts) |
|---|---|---|---|---|---|---|---|---|
| GE Vernova (GEV) | $756.28 | -7.53% | +8.20% | -4.77% | -6.47% | **-17.6%** | -10.9% | -10.9 |
| Constellation (CEG) | $252.03 | -5.80% | +6.03% | -2.73% | -5.46% | -13.4% | -8.2% | -6.6 |
| Vistra (VST) | $124.15 | -7.17% | +7.48% | -2.54% | -3.75% | -12.9% | -6.4% | -6.2 |
| NRG | $93.85 | -6.45% | +11.30% | -6.98% | -3.86% | -16.3% | -6.9% | -9.6 |
| Talen (TLN) | $355.91 | -6.46% | +9.58% | -4.70% | -2.86% | -13.4% | -5.1% | -6.6 |
| Caterpillar (CAT) | $537.37 | -5.01% | +7.17% | -1.17% | -4.33% | -10.2% | -3.8% | -3.4 |
| Eaton (ETN) | $330.57 | -5.82% | +8.03% | -5.08% | -4.78% | -14.9% | -8.0% | -8.1 |
| Vertiv (VRT) | $184.89 | -10.14% | +12.10% | -6.67% | -6.21% | **-21.3%** | -11.8% | -14.6 |
| Quanta (PWR) | $587.43 | -4.83% | +8.94% | -3.18% | -7.96% | -15.2% | -7.6% | -8.4 |
| Utilities ETF (XLU) | $43.01 | -0.74% | +1.48% | +0.18% | -0.05% | -0.6% | +0.9% | +6.2 |
| NextEra (NEE) | $83.79 | -0.41% | +0.62% | +0.73% | +0.44% | +0.8% | +1.4% | +7.5 |
| Southern (SO) | $93.29 | -0.17% | -0.02% | +1.07% | +1.02% | +1.9% | +1.9% | +8.7 |
| Duke (DUK) | $128.86 | +0.71% | -0.24% | +1.15% | +0.95% | +2.9% | +2.6% | +9.6 |
| S&P 500 (SPY) | $715.87 | -3.64% | +4.71% | -0.49% | -2.78% | -6.8% | -2.4% | 0 |
| Chips (SMH) | $447.48 | -10.60% | +15.03% | -7.26% | -7.21% | **-23.1%** | -11.5% | -16.3 |

**Reading:** the market is pricing the power and equipment names as AI beta: they move with the chip index at roughly half to nine tenths of its amplitude, in both directions (the November 23 rebound was +6 to +12%). Regulated utilities, whose earnings come from rate base rather than merchant power prices or equipment orders, did not move. A share-price fall is not evidence of demand. No dated filing, cancellation or utility statement was found that coincides with any of the three down days.

## 2. The record: established, reported, not found

| Line | What | Date / basis | Grade |
|---|---|---|---|
| Contracted load (AEP) | 15 GW of new load commitments signed in Q3; incremental contracted load to 84 GW by 2031; counted only if backed by executed electric service agreements or letters of agreement; $100B five-year capital plan | AEP Q3 release October 28, 2026, read via finviz mirror | **ESTABLISHED** (issuer release) |
| Pipeline (Dominion) | Data-centre pipeline about 54.9 GW at September 30, +6.3 GW (+13%) since December 2025; about 12.2 GW under electric service agreements, 9.8 GW construction letters, 32.8 GW engineering | Dominion Q3 (early November) via Zacks and Baxtel summaries; PJM LAS 9/29 Dominion deck says about 54 GW | **REPORTED** (secondaries agree; issuer deck not read). The firm figure is the 12.2 GW, not 54.9 |
| Pipeline (Exelon) | High-probability data-centre load 11 GW at Q3, unchanged from Q2; it was cut from 18 GW at Q2 (late July), broad pipeline 43 to 25 GW; 4 GW backed by signed transmission security agreements and $1B collateral | Q3 October 30 via 247wallst and Webull; Q2 cut via Bloomberg Law | **REPORTED**. The one real cut on the record is July's, tied to local opposition and stricter vetting, not to a demand fall this month |
| PJM forecast review | Charles River Associates for PJM: data-centre demand 30 GW by 2030, 82 GW by 2047 (soft supply constraint); with supply as the hard limit, about 11.5 GW of that demand cannot be served at 1-in-10 reliability by 2030; low AI adoption cuts 2047 demand 19 GW, constrained supply cuts it 29 GW; the pipeline is tiered for moratorium and permitting risk | PJM Load Analysis Subcommittee November 2, 2026, item 03, PDF read by text extraction | **ESTABLISHED** (PJM-posted consultant review, a forecast, not PJM's adopted 2027 forecast) |
| PJM 2027 forecast | Final large-load adjustments due November to December, forecast published January 2027; LAS next meets December 18, no materials posted | PJM LAS page read 11:5x ET | **PENDING**, not found |
| Prior PJM forecast | PJM's 2026 forecast was below 2025's through 2032 on stricter vetting of large-load requests (duplicates) | Utility Dive, PJM January 2026 | **REPORTED**, already in the record (KB165 counterevidence class) |
| IMM delay/cancel tally | 4,016.9 MW of data-centre projects cancelled or delayed as of September 21 | KB165 (carried) | carried, not new |
| Equipment: turbines | GE Vernova gas backlog plus slots 116 to 122 GW, converted 13 GW in July to September; Siemens converted 0 GW, reservations 26 to 39 GW | KB208 (November 11, issuer releases) | carried; next print late January |
| Equipment: transformers | Large power transformers about 128 weeks, step-up units over 160 weeks | VULCAN KB-284 (October 23) | carried, not re-read |
| Equipment: US orders | Electrical equipment new orders October 19,074 ($M) vs 19,003, +0.4% | ISHM 11/25 packet (Census advance) | **ESTABLISHED** at ISHM's read |
| Equipment investment | BEA Q3 information-processing equipment +41.7% annualised (revised up); Fed G.17 business-equipment OUTPUT since 2022 cut to +4.5% | ISHM 11/25 packet | weighed below |
| Contracts (PPA) | No new November hyperscaler PPA found in a bounded search; Constellation raised guidance November 9 (Q3) | search; Webull 11/10 | **NOT FOUND** for November |
| Financing | ING's about $500M data-centre loan sale closed short of bids, moving to single sales (Bloomberg 11/20, summary); lenders cutting GPU-loan advance rates 80% to 50-60% (title) | cards 20261123-008, 20261124-018 | **REPORTED**. Financing friction, not a load cancellation; it bears on the neocloud tail, not on hyperscaler ESAs |
| Cancellation claims | Alibaba 'may cut' 20 GW plan (one X account, no report found); SoftBank $2.9B power-equipment write-off, load direction not established (KB209) | card 20261120-009; KB209 | **UNVERIFIED** / carried |
| Policy, demand-positive | Texas TCEQ resumes data-centre permits (11/20 titles); Trump threat of a ban or tax on US firms' overseas data centres (11/20 titles, no order) | cards 20261120-006, 20261121-003 | titles only; if anything they push load onshore |
| Auction | 2029/30 BRA still scheduled December; the Market Monitor and state advocates asked for delay (its Q3 report, KB214); PJM's November 3 and 9 filings assume it proceeds | PJM filings EL27-11, ER27-454 (titles and summaries) | no postponement found (bounded); WATT-14/15 clock unchanged |
| Named November cancellations, utility forecast cuts, queue-withdrawal wave | none found | searches 11:45 to 11:55 ET: cancellations/deferrals November 2026; utility load-forecast cuts; hyperscaler lease walk-aways; PJM 2027 adjustments; ERCOT queue update (newest total 474.7 GW as of June) | **SEARCH-NOT-FOUND** |

**ISHM's two figures, weighed:** BEA's +41.7% says money spent on information-processing equipment is still accelerating in Q3; the Fed's revision says US factories made much less business equipment than thought. Together (ISHM's inference): spending is real and much of it is imported or price. For power this is a demand-side positive (servers get bought, and servers draw power once energized) and a supply-side caution (domestic equipment capacity is thinner than the old data said, which fits the long transformer and turbine waits). Neither figure says demand is cracking.

## 3. Proposed Section 301 tariffs and data-centre build cost and timing

**Status (VULCAN KB-VULCAN-477, ZHAO packet 11/25):** PROPOSED, not in force; comments by January 5, 2027, hearing from January 25, no effective date. Taiwan and Korea up to 15% (alternative 25%), Malaysia up to 18%, China up to 20% net of the forced-labor 301 layer (alternative 40%). Servers, chips and server power supplies (8504.40) are exempt everywhere except China; large transformers (8504.21 to .23), switchgear (8537) and insulated cable (8544) were NOT found on the exempt list in the Taiwan, Malaysia and Korea notices (VULCAN, PROVISIONAL, scope column not read row by row); China's annex charges up to 10% on all of it.

**What I can size (ASSUMPTION grade: industry rules of thumb, not sourced today):**

| Step | Figure |
|---|---|
| Non-IT data-centre build cost | about $10-14M per MW of IT load |
| Of which electrical systems | about 40-50%, $4-6M/MW |
| Of which the tariffed items (power and distribution transformers, switchgear, cable) | about half, $2-3M/MW |
| Imported share from the named economies | UNKNOWN; tested at 30-60% |
| Tariff on that share | up to 15-20% |
| **Added cost** | **about $0.1-0.3M per MW**, 1-3% of non-IT build cost, about 0.2-0.6% of all-in cost including servers ($40-55M/MW) |
| Against the power bill | one MW at 80% load factor, at PJM's January-September 2026 load-weighted real-time price $74.98/MWh (Market Monitor, KB214): about $0.53M a year of energy alone, so the tariff is about two to six months of a site's wholesale energy bill, once |

**So, cost:** small for the data-centre owner, too small on its own to change a site decision. **Timing is the bigger lever and I cannot size it:** transformers already wait about 128 weeks and makers have been passing tariff costs straight through in a sellers' market (Korean press, 2025, secondary). A final tariff could push buyers toward domestic and Mexican lines that are already full, lengthening waits, or it could change nothing if suppliers simply pass the price through. **Where it lands in WATT's channels:** most large transformers sit on the utility side of the meter (substations, transmission), so the cost goes into utility rate base and from there to ratepayers or to large-load tariffs: the WATT-08 door A/B question (who pays) and CARL's bill channel, not the data-centre's own capex. **Cannot size:** import shares by HTS line and country, stacking with Section 232 steel-derivative duties (one secondary says 25% already applies to most power transformers, unverified), the final rates, and any lead-time effect.

## 4. What this desk cannot see (PJM Data Miner 2 refuses the key, HTTP 401 since 14:12 ET November 16; WILL_QUEUE 695)

- The PJM 5-minute and hourly price tape from November 14 11:00 EPT to now (boot `tape_scan.py` 11:37 ET: UNKNOWN span, one failed call), including the November 17-19 and 24-25 cold mornings. P1 over those eleven days is UNKNOWN, not quiet. EIA-930 shows the demand half met this morning (107,114 MW at 14Z = 100% of the trailing window peak; 105,688 at 16Z), which after KB222 is not a stress reading.
- WATT-13's resolver (DM2 `gen_outages_by_type`), due first boot on or after December 2: it cannot be graded while the key is refused.
- WATT-16's resolver (verified 5-minute tape) for December 18.
- The same-vintage spark spread. The EIA ICE proxy (PJM West peak, delivery November 25, $80.21/MWh, Henry Hub $3.662) gives +$54.58/MWh at heat rate 7, a different product.
- None of these is a demand measure: the key gap blinds the price and outage channels (P1, P4), not the contracted-demand record above.

## 5. Forward view (outlooks, not registered, unscored)

**Expectation:** no physical or contracted crack shows in primary data before year-end; the equity names keep trading as AI beta until a hard print arrives. **Alternative that matters:** the crack, if it comes, shows first at the financing tail (neoclouds, standalone developers, GPU-backed loans) as stalled or withdrawn large-load requests, not at the hyperscalers' signed ESAs; that would hit pipeline totals (Dominion's engineering-stage 32.8 GW, ERCOT's 474.7 GW of requests) long before firm load.

| What would show demand actually cracking | Where and when | My odds |
|---|---|---|
| A hyperscaler or named developer cancels or defers a US site of 1 GW or more, by name, on the record | any day; check at the Q4 prints late January to early February | about 30% by January 31, 2027 |
| A utility cuts SIGNED load (ESA/LOA-backed: AEP 84 GW, Dominion 12.2 GW, Exelon 4 GW TSA), not pipeline | Q4 prints mid-to-late February 2027 | about 15% by February 28, 2027 |
| PJM's final 2027 large-load adjustments come in below the 2026 forecast's data-centre adder for 2030 | LAS December 18; forecast January 2027 | about 40% (vetting has cut each round; a cut from vetting is not a demand crack, so read the reason) |
| ERCOT Batch Zero (December 10) excludes or loses a large share of the 6.5 GW first batch | December 10, PUCT December 17 | about 20% for a withdrawal-led shortfall |
| GE Vernova gas backlog plus slot reservations FALL below 122 GW, or reservations are cancelled | Q4 print late January 2027 | about 10% |
| 2029/30 BRA clears below the cap (WATT-14 at 88% YES) | results December 22 | 12% (registered) |

What would change my mind toward cracking: two of the first three rows in the same quarter, or any signed-load cut. A single developer failure or a financing stall alone is the tail, not demand. Horizon: December 10 to February 28, 2027.

## 6. Limits

All searches bounded (WebSearch summaries, a few pages read); Dominion and Exelon figures from secondaries; AEP from an issuer-release mirror; CRA from the PJM PDF. Cost-sizing figures are ASSUMPTION grade. November 25 prices intraday. No PJM price data after November 14 11:00 EPT.
