---
signal_id: "SIG-W-20261121-003"
date: "2026-11-21"
timestamp: "2026-11-21T23:10:01Z"
dispatched: "2026-11-21T23:10:01Z"
source: "RESEARCH-INTAKE data/2026-11-20/news.json (fingerprint 15d0680e3dd0), data/2026-11-21/news.json@c136640ac0c9 (lane commit 9175bac) and data/2026-11-21/news.json (aec572697298), titles; intake_scan GPU_FINANCE_REVIEW list"
origin: ["RESEARCH-INTAKE scan and title skim (7e(d), 7e(g), 7e(h)), WALTER return 11/21"]
action: ["VULCAN", "CYPHER", "OSPREY", "HANS", "CORAL"]
info: ["WATT", "ZHAO", "BROCK", "YURI", "SHADE", "CREED", "MIDAS", "SAM", "LIQUID", "PROME"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.6
confidence_language: "titles only except where marked; aggregator items low grade"
resources: 1
safety_net: "clear"
cluster: "MISC"
domain: "AI_CAPEX"
entities: ["Trump", "TSMC", "Samsung", "TrendForce", "SanDisk", "SpaceX", "CoreWeave", "FBI", "N-able", "Citizens Property Insurance"]
word_count: 886
dispatch_note: "Small-items card (step 10.6). ACTION: VULCAN (items 1 to 5), CYPHER (6, 7), OSPREY (8), HANS (9), CORAL (10). INFO the other line owners; PROME by BOARD diff. One combo:none subject (Paraguay) carried to PROME at closeout."
event_window: "open"
---
# Small items, RESEARCH-INTAKE Nov 20 22:17Z and Nov 21 runs: Trump threatens ban or tax on US firms' overseas AI data centres; TSMC and Samsung reportedly pause China consumer chip shipments; TrendForce bearish 2027 NAND, SanDisk -14%; GPU financing items; FBI criminal database hack; Russia-bound ship attacked in Gulf of Finland; EU gas +40% title; Citizens Property CEO to step down

# Small items, RESEARCH-INTAKE batches data/2026-11-20/news.json (rewritten by the 22:17Z run), data/2026-11-21/news.json (12:46Z and 20:56Z versions)

Titles only unless marked. Logging is not scoring: nothing here moves a score, band or trigger on WALTER's read. Each line names its owner theme for combination (WQ-622).

| # | Item (source, date) | Owner | combo |
|---|---|---|---|
| 1 | 'Trump threatens ban on US firms building AI data centres overseas' (BBC 11/20); 'Donald Trump threatens tremendous tax on data centres built outside US' (FT 11/20). Threat, no order or text found. | VULCAN, WATT | combo:VULCAN/datacenter-siting-policy |
| 2 | '[News] TSMC, Samsung reportedly pause China consumer chip shipments under new U.S. rules; 16nm orders affected' (TrendForce 11/20). Reported, not company-confirmed. The 11/19 chip rule is already on VULCAN's S4 row. | VULCAN, ZHAO | combo:VULCAN/export-controls |
| 3 | 'SanDisk tumbles as TrendForce turns bearish on 2027 NAND prices; Micron -5%, SK Hynix -4%' (Yahoo 11/20) and four repeats; 'NAND price to fall' (Electronics Weekly 11/20); against 'Samsung's memory capacity booked through 2029 as customers sign long-term deals through 2031' (BigGo 11/21). Card 20261120-006 item 14 carried the 11/19 NAND titles. | VULCAN | combo:VULCAN/memory-cycle |
| 4 | GPU_FINANCE_REVIEW (12): 'SpaceX $44B GPU financing priced Nov 20 (Vera Rubin)' (explainx); 'SpaceX falls 4% on $32 billion AI chip debt at yields topping 8%' (TIKR); 'Project Saturn: 5 lenders seek SpaceX chip launch ban' (shattered.io); '9fin Excess Spread: the vastness of SpaceX'; 'GPU rental prices climb 24% as AI trade cools, Silicon Data' (Crypto Briefing); 'CRWV, IREN, NBIS extend neocloud selloff' (TradingView) and 'Neoclouds shed up to 76% from peaks' (BigGo); 'Little room for error: a debt-laden cloud computing company' (Guardian 11/21); 'Applied Digital's financing costs dwarf its rent as Nvidia tightens neocloud funding' (11/20); 'Nvidia's $228 billion data center bet' (BloombergNEF); 'The Bank of Nvidia is closed' (Seeking Alpha); 'Fed AI exposure: $1T bank links in FSR 2026' and 'AI data center debt insurance' (low-grade aggregators). SpaceX dollar figures conflict across titles ($44B vs $32B); none read. 'CoreWeave owes $47 billion' (11/21) and 'Nebius lifts 2026 capex view to $27B' (11/19) likewise. | VULCAN, BROCK | combo:VULCAN/gpu-financing |
| 5 | 'Amazon closes in on $7.5bn deal to buy AI start-up Decart' (FT 11/21). | VULCAN | combo:VULCAN/ai-m-and-a |
| 6 | 'FBI reportedly investigating apparent hack of its criminal database' (11/21, lane ALERT). Not read. | CYPHER | combo:CYPHER/federal-cyber-posture |
| 7 | N-able: 'security breach led to major service outage' (BleepingComputer 11/20), 'cyberattack knocked email controls offline' (Digg). Same incident as SIG-W-20261119-009 and 20261120-006 item 7; new wording only (outage now attributed to the breach). | CYPHER | combo:CYPHER/msp-supply-chain |
| 8 | 'Russia-bound ship attacked in Gulf of Finland' (FT 11/21). Not read: attacker, flag and cargo unknown. 'Zelensky says Crimean Bridge strikes fair response' (11/21; bridge strike on card 20261120-006 item 5). 'Russia and Ukraine's drone war sends optical fibre prices soaring' (FT 11/21). 'Denmark accuses Russia of plotting to assassinate US-Ukrainian rapper' (11/20). | OSPREY, YURI | combo:OSPREY/baltic-and-crimea |
| 9 | 'European gas prices soar more than 40% on LNG supply fears' (DD News 11/20; level, contract and window not stated, not read); 'NW Europe CFR prices firm as TTF natgas rises again' (Quantum 11/20). HANS's TTF row was NOT read by WALTER this weekend. 'ECB needs December rate hike into restrictive zone, Nagel says' (Bloomberg 11/20; inflation 4% per BigGo). | HANS | combo:HANS/ttf-and-ecb |
| 10 | 'Citizens Property Insurance CEO Tim Cerio to step down in January' (Florida's Voice, Tampa Bay Times 11/20); policies 'fall to 215,000' (Beinsure). 'Florida condo prices tumble in Treasure Coast county' (TCPalm 11/21). | CORAL, SHADE | combo:CORAL/fl-insurance-and-condo |
| 11 | 'Commercial real estate lending loses momentum' (CoStar 11/20). Crain's 'extend and pretend' already folded (20261120-006 item 17). | CREED | combo:CREED/cre-credit |
| 12 | 'Private equity-backed companies face a $300 billion debt wall; looking at your retirement account for an exit' (Fortune 11/21); 'Barings BDC showed weakness (downgrade)' (Seeking Alpha 11/21); 'CVC claims accounting manipulation in 3bn euro Advent pastry ingredients deal' (FT 11/21). | BROCK | combo:BROCK/pe-exits-and-bdc |
| 13 | 'Copper price sinks into bear market, worst week of the year' (Mining.com 11/20); 'Traders start to move US copper to China as Trump tariff fears ease' (FT 11/21). | MIDAS | combo:MIDAS/copper |
| 14 | 'FX Daily: Carry trade unwind in full swing' (ING 11/20); 'USD/JPY weekly outlook: yen carry unwind risks flash red' (FOREX.com 11/21); USD/JPY 'lower 158' (BigGo 11/20). | SAM | combo:SAM/carry-unwind |
| 15 | 'Paraguay's new president inherits a crisis deeper than a bank failure' (AzerNews 11/21, lane ALERT). Same story as SIG-W-20261119-005 and -018. | HANS, LIQUID | combo:none |

**Killed as date traps (kill_log):** Reuters 'Saudi Arabia restarts East-West oil pipeline' dated 2026-09-22; Reuters 'Explainer: US diesel exports ban' dated 2026-09-23; Cato 'diesel export ban' 2026-09-22; Reuters 'Houthis say they attacked Riyadh and Aramco facilities in Yanbu' dated 2026-09-24; Kpler Bab el-Mandeb explainer dated 2026-07-27. The lane's BRENT and FALCON watch hits on the first two are these vintage items.

**Folded elsewhere:** 'Nvidia interim CEO urges progress in first all-hands since Huang's exit' (11/19, HENRY watch hit) is old news (20261120-006 item 15); Nvidia accounting and tape titles go to SIG-W-20261121-001; Iran and Gulf titles to SIG-W-20261121-002.
