---
signal_id: "SIG-W-20261120-006"
date: "2026-11-20"
timestamp: "2026-11-20T16:36:31Z"
dispatched: "2026-11-20T16:36:31Z"
source: "RESEARCH-INTAKE data/2026-11-20/news.json (collected 2026-11-20T13:04:26Z) and the rewritten data/2026-11-19/news.json; search summaries for item 4 (TrendForce 2026-11-18, DigiTimes 2026-11-19, pages not read)"
origin: ["RESEARCH-INTAKE scan and title skim (7e(d), 7e(h)), BM-20261120-01"]
action: ["VULCAN", "CYPHER", "FALCON", "OSPREY", "SHADE"]
info: ["BRENT", "MIDAS", "SAM", "BOND", "WATT", "BROCK", "CREED", "REGINALD", "OTTO", "CARL", "MARCO", "LABOR", "ZHAO", "PROME"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.6
confidence_language: "titles only except where marked; item 4 from search summaries"
resources: 1
safety_net: "clear"
cluster: "MISC"
domain: "AI_CAPEX"
entities: ["Iran", "US naval blockade", "White House", "Google", "Broadcom", "MediaTek", "HBM", "Druzhba", "Tatarstan", "Mark Walter", "Delaware Life", "TruStage", "N-able", "Nvidia", "SpaceX", "gold", "silver", "yen", "PJM", "ERCOT", "CoreWeave", "PBoC"]
word_count: 1112
dispatch_note: "Small-items card (step 10.6), one line per owner theme with combo tags. ACTION: VULCAN (items 4, 8, 9, 14, 15), CYPHER (3, 7), FALCON (1, 2), OSPREY (5, 16), SHADE (6). INFO: the other line owners; PROME by BOARD diff. One combo:none subject (USD/JPY) carried to PROME at closeout."
event_window: "open"
---
# Small items, lane collected 2026-11-20T13:04Z (titles unless marked): Iran moves to restart oil exports despite the US naval blockade, US widens blockade; Trump says Tehran may be working on chemical or biological weapons; White House removes its top cyber-security official after tech outages (FT, BBC); Google to buy HBM directly, bypassing Broadcom (TrendForce 11/18, DigiTimes 11/19); Ukraine hits a Druzhba station in Tatarstan; Delaware regulator says it was misled on Mark Walter's insurers; TruStage reached an agreement with its attackers; California probes Nvidia over China chips; gold and silver at 14-month lows; yen up after Japan CPI

# Small items, RESEARCH-INTAKE batch collected 2026-11-20T13:04Z (and the rewritten 11/19 batch)

Titles only unless marked READ. Logging is not scoring: nothing here moves a score, band or trigger. Each line names its owner theme for combination (WQ-622).

| # | Item (source, date) | Owner | combo |
|---|---|---|---|
| 1 | 'Iran Moves to Restart Oil Exports Despite U.S. Naval Blockade' (OilPrice.com, 11/20 09:00Z); 'Gulf Sees Iran Oil Movement as US Widens Blockade' (Rigzone, 11/20 07:09Z); 'US maritime agency warned Iran blockade was adding to rising Gulf premiums' (Al Jazeera, 11/20); 'Oil prices set for third straight weekly decline on Middle East export flows' (CNBC, 11/20). Titles only; 'widens' not checked against a US primary. Iran pre-dispatch guard: anchor verified 11/18 (sweep), next full sweep about 11/25; no war-state framing is asserted here. | FALCON, BRENT | combo:FALCON/blockade-flows |
| 2 | 'Trump says Tehran may be working on chemical or biological weapons as tension mounts' (CBS News, 11/20 08:51Z). Title only; POTUS channel is tape, not information (anchor guard). | FALCON | combo:FALCON/escalation-rhetoric |
| 3 | 'White House replaces top cyber security official' (FT, 11/20 08:33Z); 'White House removes cyber-security chief after series of tech outages' (BBC, 11/20 09:37Z). Both pages unreadable here (FT paywall, BBC blocked to fetch); who, which office and which outages NOT established. | CYPHER | combo:CYPHER/federal-cyber-posture |
| 4 | Google to buy HBM directly for its MediaTek-built TPUs, bypassing Broadcom's bundled procurement (TrendForce 11/18; DigiTimes 11/19; search summaries, pages not read); Bernstein estimates about $50 billion of savings over the TPU lifecycle if fully adopted; Counterpoint puts Broadcom's HBM markup at 15% to 20% (reported). Industry reports, not confirmed by Google or Broadcom. Broadcom is -9.3% today (card 001); no report found that ties today's fall to this story. Earlier mention: card 20261119-005. | VULCAN | combo:VULCAN/custom-silicon-margins |
| 5 | 'Ukraine strikes key Druzhba oil pipeline station in Russia's Tatarstan, General Staff confirms' (Kyiv Independent, 11/20 12:01Z) and three same-day repeats; 'More Russian regions limit fuel sales as Ukrainian drone strikes hit refinery output' (Reuters, 11/20). Card 20261119-004 already carried a Druzhba/Tatarstan leg; OSPREY decides whether this is the same strike, now confirmed. 'Russia targets Kyiv crossings days after Ukraine hits Crimean Bridge' (BBC, 11/20). | OSPREY | combo:OSPREY/druzhba |
| 6 | Delaware's insurance regulator says it was 'misled' about Mark Walter's insurers' assets (NYT, WSJ, Quartz 11/19; Beinsure 11/20: '$21 bn in misclassified assets'); Claims Journal 11/19 on gaps in regulation; WSJ 11/20 on insider deals. Follows card 20261116-005 (Delaware Life reclassification). Titles only. | SHADE | combo:SHADE/pe-insurer-governance |
| 7 | TruStage 'Reaches Agreement With Cyberattackers' with a data investigation taking 6 to 8 more weeks (CUToday 11/19); 'What Did It Cost?' (CUTimes 11/19); 'New Details on TruStage Cyberbreach' (Credit Union Daily 11/19); N-able 'Blames Service Disruption on Cyberattack' (SecurityWeek 11/20). Follows card 20261119-009 (N-able breach, TruStage). | CYPHER | combo:CYPHER/cu-vendor-incidents |
| 8 | 'California targets Nvidia in China AI chip probe' (BBC Business, 11/19 23:04Z; page blocked). Who in California and under what authority NOT established. | VULCAN | combo:VULCAN/export-control-exposure |
| 9 | 'Lenders aim to bar SpaceX from launching $40bn of chips into orbit' (FT, 11/20 00:15Z; paywalled, title only). | VULCAN, BROCK | combo:VULCAN/ai-financing-chain |
| 10 | Gold and silver at 14-month lows (TradingView 11/20: 'as Dollar, Fed fears bite'); gold below $3,550 on Comex (Report.az 11/20); 'COMEX silver could see heavy selling and potential default', one commentator (Traders Union 11/20). The dollar index is flat today (card 001), so the dollar half of that title is not today's tape. | MIDAS | combo:MIDAS/precious-liquidation |
| 11 | Yen strengthens after Japan's October CPI (FT 11/20: 'keeps BoJ on course for further tightening'; CNBC 11/19: core inflation highest this year as the energy subsidy expires); MUFG: 'AI risk-off could favour Yen' (FXStreet 11/20). | SAM | combo:none (USD/JPY near 160, named to PROME 11/12, still open) |
| 12 | Treasury yields 'sharply lower as investors flee to safe havens' (CNBC 11/20); 'yields fall as AI trade worries spur safe-haven bid' (Reuters via marketscreener 11/20); FT 11/20: 'Oil loses grip on bond markets as inflation virus spreads' (title). | BOND | combo:BOND/safe-haven-bid |
| 13 | PJM plan could cut data-center and power-plant connection times to 12 months (Data Center Dynamics 11/20); Texas TCEQ resumes data-center permits before the ERCOT community-impact report (WOAI, ABC13 11/20; Hart Energy 11/19: the Governor told the agency to grant permits). | WATT | combo:WATT/interconnection |
| 14 | NAND prices tipped to fall in 2027 as Chinese cloud firms cut SSD orders (The Register, TrendForce 11/19); Micron says all major customers eye 3D DRAM tie-ups (TrendForce 11/20); Samsung custom HBM4E for Meta (TrendForce 11/17); Micron: 75% of 2027 capacity sold (BigGo 11/19). | VULCAN | combo:VULCAN/memory-cycle |
| 15 | Neocloud selloff: 'CRWV, IREN, NBIS Stocks Extend Neocloud Selloff As Anthropic IPO Rally Fades' (TradingView 11/20 06:21Z); 'CoreWeave: The Liquidity Window Is Closing Down' (Seeking Alpha 11/19); Arbol launches parametric insurance for GPU residual-value risk (Artemis 11/19); 'Nvidia faced pressure to boost its AI backstop before Jensen Huang's exit' (Economic Times 11/19). | VULCAN, BROCK | combo:VULCAN/ai-financing-chain |
| 16 | Black Sea drone strike on an LPG tanker lifts wheat and freight war-risk premiums (CMB News, 11/18). Black Sea, not the Hormuz TARA GAS case. | OSPREY | combo:OSPREY/black-sea-shipping |
| 17 | 'Record office delinquencies mean lenders do more extend and pretend' (Crain's New York, 11/19). | CREED, REGINALD | combo:CREED/extend-and-pretend |
| 18 | Subprime auto loan delinquencies hit highs (Asianet Newsable, 11/20; secondary aggregator, no data source named in the title). | OTTO, CARL | combo:OTTO/subprime-dq |
| 19 | Texas governor-elect commits to rescind the H-1B hiring-freeze executive order (FWD.us statement, 11/19). | MARCO, LABOR | combo:MARCO/h1b |
| 20 | SEC staff spotlights private-credit valuation and disclosure (Legal 500, 11/20); Commission nominees questioned on private credit and AI risk (VitalLaw 11/20; Punchbowl 11/19: nominees 'shrug private credit worries'). | BROCK | combo:BROCK/regulatory-posture |
| 21 | PBoC holds the Loan Prime Rates for the 18th month (FXStreet, BigGo 11/20); USD/CNY fixing 6.7131. | ZHAO | combo:ZHAO/pboc |

**Killed as date traps (kill_log rows):** 'Saudi Yanbu oil terminal reportedly hit in aerial attack' (safety4sea, 2026-10-02); 'Aramco Offers Europe Spot Crude as Yanbu Hits 2.5 mb/d' (2026-10-28); 'Houthi attacks prompt Saudi Yanbu warnings' (Jerusalem Post, 2026-11-05); 'Saudi Arabia Declares All-Clear in Taif, Yanbu and Khamis Mushait' (2026-11-11); 'Russia extends diesel export ban until end of October' (Reuters, 2026-09-30). **Duplicates:** WSJ $500 billion Nvidia pledge undisbursed (11/18 evening; card 20261119-005); Paraguay bank failure $1 billion (cards 20261119-005, -018); N-able breach confirmed (card 20261119-009).
