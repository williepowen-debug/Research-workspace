---
signal_id: "SIG-W-20261127-002"
date: "2026-11-27"
timestamp: "2026-11-27T17:45:51Z"
dispatched: "2026-11-27T17:45:51Z"
source: "fred.stlouisfed.org fredgraph csv BAMLH0A0HYM2, BAMLH0A3HYC, VIXCLS (read 2026-11-27 after 17:44Z); Research-Intake data/2026-11-27/news.json (collect 17:43Z) and its earlier same-day version; FORGE fetch.py and yfinance 30-minute bars 17:30Z; search summaries (Meduza 2026-06-01, globaltradealert Decree 646; Axios 2026-10-30 France flash)"
origin: ["Research-Intake collect 2026-11-27T17:43Z", "FRED read after the 17:44Z scan", "web search summaries"]
action: ["LIQUID", "YURI", "BRENT", "FALCON"]
info: ["REGINALD", "OSPREY", "HAWK", "HANS", "MIDAS", "SHADE", "BROCK", "AEOLUS", "WATT", "HENRY", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "indicator"
confidence: 0.75
confidence_language: "reports: item 1 read at FRED; others titles"
resources: 1
safety_net: "clear"
cluster: "MISC"
domain: "FUNDING_LIQUIDITY"
entities: ["HY OAS", "Russia", "jet fuel", "OPEC", "Iraq", "Venezuela", "IRGC", "Kuwait", "Guggenheim", "Kirkland & Ellis"]
word_count: 553
dispatch_note: "PRIORITY: item 1 is an owner-due cell (LIQUID GATE-LIQ-069, TERRY D:L1278; TERRY live, told by message). Iran items are claims; IRAN_WAR_GUARDS read 11/26. RED, PROME by BOARD diff."
event_window: "open"
---
# Nov 27 lane: FRED HY OAS 11/25 first-published 377 bp (372, 363 before), CCC 1,417; Russia extends its jet fuel export ban to March 31, 2027 (reported by about a dozen outlets, decree not read); US lobbied Iraq and Venezuela to exit OPEC (Middle East Eye) before Sunday's OPEC+ meeting; IRGC claims warning shots turned back a US F-16 near Hengam; EU calls for pressure on Iran over the Kuwait deaths

# Friday 11/27 lane (collector run 17:43Z) and the 11/25 credit cells

| # | Item | Read | Owner |
|---|---|---|---|
| 1 | **HY OAS (BAMLH0A0HYM2) 11/25 = 377 bp**, first published (11/24 372, 11/23 363); **CCC 1,417** (11/24 1,405). REG-T-03/-04 and RED-FT-02 fired states continue; FT-02 exit (<300 s3) not near. VIXCLS 11/25 28.29; a VIXCLS bar dated 11/26 (26.80) is a NYSE-holiday NON-SESSION bar under RED's rule. Vendor 12:30 ET: ^VIX 24.79 (-7.5%; range since Wed 24.30 to 28.89), ^GSPC 7,280.89 (+1.37%; low since Wed 7,151.78): no WALTER row crossed | FRED csv, read directly | LIQUID (GATE-LIQ-069 review 11/27), REGINALD; TERRY told by message (live) |
| 2 | **Russia extends the jet fuel export ban to March 31, 2027** (the June ban, Decree 646, ran to 11/30); 'amid Ukrainian attacks on refineries' (Breakingthenews 06:34Z, Bloomberg-style titles, about a dozen outlets 11/27; one says April) | titles only; decree not read; search found no government page yet | YURI (export instrument), OSPREY; BRENT informed |
| 3 | **'US lobbied Iraq and Venezuela to exit Opec, sparking Saudi intervention'** (Middle East Eye, 17:15Z); 'Iraq boosts oil exports to 3.6 mb/d' (title). OPEC+ meets Sun 11/29 | titles only; single outlet on the lobbying claim | BRENT |
| 4 | **IRGC claims warning shots forced a US F-16 to retreat near Hengam Island** (NewsCord compilation of 7 outlets, 11:22Z); 'Iran accused of deadly drone attack in Kuwait that sparks EU call to step up pressure on Tehran' (CBS 10:07Z; follow-up to card 20261126-004); 'After heavy strikes by Iran, US naval base in Bahrain faces uncertain future' (analysis title) | titles; IRGC claim only, no CENTCOM statement found | FALCON, HAWK |
| 5 | Gold: 'COMEX gold surges 4% to $3,708, silver +10%' (India Infoline 10:33Z) | title; vendor not re-read | MIDAS |
| 6 | 'French economy shrinks 0.2% in third quarter' (FT 11:38Z); the 10/30 flash was -0.1% (search), so this reads as INSEE's second estimate, not read | title | HANS (T-10 open) |
| 7 | Novorossiysk drone attack injures three (mayor, 11/27); insurers hike Black Sea war-risk premiums (11/26) | titles | OSPREY |
| 8 | Delaware insurance regulator 'intentionally misled' over Walter insurers' affiliates (tracker 11/27; card 20261123-007 carried 'misclassified'); 'Mark Walter controls 36% of Guggenheim parent' (11/24); lawsuit on a Guggenheim fund's dividend (11/26) | titles | SHADE |
| 9 | Kirkland & Ellis under fire from PE backers over sell-to-yourself deals (FT 05:00Z) | title | BROCK |
| 10 | 'Hundreds of thousands still without power after storms hit US on Thanksgiving' (BBC 10:26Z) | title | AEOLUS, WATT |

- **Repeats, not carded:** Anthropic 'rises 17% on debut' is the 11/19 IPO close ($97.17 vs $83); Nvidia interim CEO items are 11/10 to 11/13; NYC rent freeze (20261125-043); Bank of Korea, ECB accounts, BoE FSR (20261126-005); Huawei HBM (20261126-005 area); CoreWeave $4.5B loan (20261125-031).
- **Lane health:** treasury_auctions feed status ok after PROME's repair (40 auctions, none weak by the feed's rule; 10/23 to 10/27 unchecked by the feed).
- **So what:** the 11/25 credit cell widened again (+5 bp) inside the fired states; Russia keeps jet fuel off export markets through winter; the OPEC lobbying claim lands two days before OPEC+ sets 2027 policy.
