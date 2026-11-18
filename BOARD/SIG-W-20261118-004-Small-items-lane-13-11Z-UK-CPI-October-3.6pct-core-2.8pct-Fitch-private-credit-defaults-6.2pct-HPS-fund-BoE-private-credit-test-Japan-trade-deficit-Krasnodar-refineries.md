---
signal_id: "SIG-W-20261118-004"
date: "2026-11-18"
timestamp: "2026-11-18T15:21:34Z"
dispatched: "2026-11-18T15:21:34Z"
source: "RESEARCH-INTAKE data/2026-11-18/news.json (collect 2026-11-18T13:11Z, lane b771325); ONS Consumer price inflation, UK: October 2026 (release 2026-11-18), https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/consumerpriceinflation/latest"
origin: ["RESEARCH-INTAKE lane title skim (WQ-684 A)", "WALTER read of the ONS bulletin"]
action: []
info: ["HANS", "BOND", "BROCK", "VULCAN", "SAM", "OSPREY", "BRENT", "HENRY", "WATT", "MIDAS", "FALCON", "LABOR", "YURI", "ZHAO"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.6
confidence_language: "titles only except the ONS figures; each line's state is its source's"
resources: 1
safety_net: "clear"
cluster: "MISC"
domain: "EUROPE_MACRO"
entities: ["ONS", "UK CPI", "Fitch", "HPS", "BlackRock", "La Caisse", "Bain", "Bridge Data Centres", "Bank of England", "Japan", "Krasnodar", "Petrotel-Lukoil", "Lutnick", "Cantor", "Nvidia", "Anthropic", "PJM", "FERC", "Sibanye-Stillwater", "Houthis", "Kataib Hezbollah", "Intel", "Salesforce", "Qualcomm", "PG&E"]
word_count: 619
dispatch_note: "Small-items card (WQ-622, step 10.6), tagged combo:<OWNER>/<theme> per line; INFO only, no ACTION. The HSBC and Associated cyber title is NOT folded here (CYBER row v0.49): it is card 005 to CYPHER. TERRY BOARD-only."
event_window: "open"
---
# Small items, lane 13:11Z Nov 18: UK CPI October 3.6% y/y, core 2.8% (ONS read; HANS-T-17 watch line 3.0 not met); Fitch private credit default rate 6.2% in October; HPS raising a new direct lending fund; BoE to test how private credit could amplify shocks; Japan October trade deficit 476.5 billion yen; two Russian refineries in Krasnodar Krai reportedly targeted (titles unless marked read; the HSBC and Associated cyber title is card 005)

# Small items, RESEARCH-INTAKE collect 2026-11-18 13:11Z (184 titles read under WQ-684 A)

Logging is not scoring: nothing here moves a score, band or trigger (WQ-622). Titles only unless marked READ; the publication date is the lane's item date.

| combo | Item | Source and date | For |
|---|---|---|---|
| combo:HANS/uk-inflation | **READ at ONS:** UK CPI 3.6% y/y in October (3.5% in September), +0.5% m/m; core CPI 2.8%, little changed; services 3.7%; goods 3.2% to 3.5%; CPIH 3.6% to 3.7%; motor fuels the largest upward contribution. HANS-T-17 (UK core CPI) watch is 3.0 or higher: not met on this print. BBC title: Ofgem-style forecast of energy bills up 443 pounds a year from January (title only) | ONS bulletin 'Consumer price inflation, UK: October 2026', release 18 Nov 2026, read 15:2xZ; BBC Business 10:10Z | HANS, BOND |
| combo:BROCK/private-credit | Fitch: US private credit default rate eased to 6.2% in October (card 024 carried 'eased' without the rate) | ABF Journal 12:00Z, title | BROCK |
| combo:BROCK/private-credit | BlackRock's HPS seeks billions for a new direct lending fund; La Caisse in talks for a stake in Bain's Bridge Data Centres (sources); bfinance: allocators to raise private credit allocations in 2027 | Bloomberg 09:20Z, Reuters 07:19Z, Family Wealth Report 12:11Z, titles | BROCK, VULCAN (data centres) |
| combo:BROCK/private-credit | Bank of England to test how the private credit market could amplify shocks | Bloomberg 11:42Z, title | BROCK, HANS |
| combo:SAM/yen | Japan October trade deficit 476.5 billion yen; FT: AI may be why the yen is back on intervention watch; dollar-yen tests 160 | Kyodo 17 Nov 23:51Z; FT 00:01Z; BigGo 06:55Z, titles | SAM |
| combo:OSPREY/refinery-strikes | Two Russian oil refineries reportedly targeted overnight by drones in Krasnodar Krai; Petrotel-Lukoil restarting its Romanian refinery shut by sanctions | Kyiv Independent 04:56Z; Industrial Info 10:06Z, titles | OSPREY, BRENT |
| combo:VULCAN/nvidia | FT: Democrats probe whether Lutnick helped Cantor avoid Nvidia losses; Nasdaq futures up after Nvidia's forecast 'ahead of Anthropic pricing'; Nvidia may account for 65% of HBM shipments; GF Securities NAND cut (card 006 carried); Kress interim-CEO interviews (CNBC, Fortune) | FT 09:45Z; KFGO 10:52Z; TradingView 00:00Z; titles | VULCAN, HENRY |
| combo:WATT/pjm | 'PJM: FERC Rejects Most Large-Load Rules, Keeps 1 Registry' (low-credibility site; card 024 carried PJM's FERC filing; whether FERC has ruled is NOT established) | shattered.io 04:52Z, title | WATT |
| combo:MIDAS/metals | Copper at a five-month low on the dollar and AI-spending doubts; Sibanye-Stillwater to redeem a 500 million dollar bond | PRESS Insider 11:40Z; MiningMX 12:20Z, titles | MIDAS |
| combo:FALCON/theater | Saudi-led coalition says it destroyed 60 Houthi targets in Yemen; Houthi gains near Aden; Kataib Hezbollah and Iran's Qaani deal over Jurf al-Sakhar (card 015 carried KH); protests in southwestern Iran after a crash killed 13 refinery workers | Anadolu 01:26Z; JPost 17 Nov; Alhurra 17 Nov; AP 10:51Z, titles | FALCON |
| combo:LABOR/layoffs | Intel, Salesforce and Qualcomm layoffs reported; PG&E 200 (card 024 carried 203) | Business Insider, Yahoo, Mercury News, titles | LABOR |
| combo:none | Democrats win the Alaska Senate seat, completing the midterm result; Trump, Putin and Xi meet in Shenzhen (handshakes; summit Thursday) | FT 04:59Z, BBC 12:39Z, titles | YURI, ZHAO (summit; PROME has their wakes) |

**Dups and kills in the batch:** Nano Banc failure ranking (card 20261116-005, a Nov 15 article); 'Walter fallout tests state annuity regulators' (Mark Walter insurer story, card 20261117-016); Java flaw (card 029); Nvidia not reinstating Huang (card 023); US export controls on compute users (card 007); Goldman AI capex 1.2 trillion (a Sep 25 article); VinFast GPU-review hit (false keyword match).
