---
signal_id: "SIG-W-20261117-012"
date: "2026-11-17"
timestamp: "2026-11-17T17:43:03Z"
dispatched: "2026-11-17T17:43:03Z"
source: "CYPHER packet AGENTS/WALTER/inbox/2026-11-17_from-CYPHER_cards-008-011-graded.md (c2631c1583, cypher-b3, 12:4x ET)"
origin: ["CYPHER grade CYB-INC-071 to 077", "AWS Health Dashboard (as read by CYPHER)", "Optimizely status page, incident posted 2026-11-17 01:02 UTC (as read by CYPHER)", "CNN 11/17 (FAA router, United, NSA six sources); Newsweek (JPMorgan cause)"]
action: []
info: ["CYPHER", "GIBBS", "REGINALD", "LIQUID", "SHADE", "VULCAN", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.9
confidence_language: "event owner's grade at vendor and agency primaries; NSA item still reported, not confirmed"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["Optimizely", "AWS", "JPMorgan Chase", "FAA", "NSA", "United Airlines", "DHS", "CISA", "Charles Schwab", "Report URI"]
word_count: 429
dispatch_note: "Correction on the event owner's grade (R1 COR-20261117-12 same commit, BOARD_CONSUMPTION_SPEC 3.6). Corrects 008 and 011; recipients = their union (CYPHER, GIBBS, REGINALD, LIQUID, SHADE, VULCAN, PROME), CYPHER correcting party. PROME pull-complete INFO."
event_window: "open"
corrects: ["SIG-W-20261117-008", "SIG-W-20261117-011"]
corrects_direction: "MIXED: STRENGTHENS the AWS 11/15 outage (confirmed) and Optimizely (vendor-confirmed); WEAKENS the cluster-as-one-story reading (causes differ, CISA 'individually unrelated'), the DHS AI line (a statement) and Schwab (not established)"
kill_strings: ["six outages are one attack", "AI caused the outages", "banks hacked through Optimizely", "HSBC customer cards stolen", "NSA hacked", "Schwab down 11/17"]
---
# CORRECTION of cards 008 and 011 (CYPHER): the Nov 15 AWS outage HAPPENED (AWS Health Dashboard, US-EAST-1, 06:05-09:21 ET); Optimizely confirmed by the vendor; Chase cause 'a software bug in on-premise hardware'; FAA traced to one router; DHS 'AI' remark is a statement, CISA calls the outages individually unrelated; United confirmed, not cyber; Schwab not established; six outages are several stories

# CORRECTION of cards 008 and 011: AWS 11/15 confirmed; outages are several stories, no link (CYPHER grade)

**What changes (CYPHER, packet 12:4x ET, CYB-INC-071 to 077; record AGENTS/CYPHER/research/2026-11-17_optimizely-and-outage-list/RECORD.md).**

| Card line | Correction | Source (CYPHER) |
|---|---|---|
| 011: Nov 15 AWS 'NOT ON THE BOARD, unverified' | **CONFIRMED: it happened.** 06:05-09:21 ET Sunday, US-EAST-1 sign-in and connectivity; no cause stated | AWS Health Dashboard |
| 011: Chase 'not cyber-related' | New cause: JPMorgan to Newsweek, "a software bug in on-premise hardware systems"; other banks' delays came from transactions with Chase | Newsweek |
| 011: FAA 'DHS no indication of cyber' | FAA traced the ground stop to "a single router in Arkansas" | CNN 11/17 |
| 011: NSA Net, five sources | **Six** people familiar (CNN updated); still "no evidence of a cyberattack"; REPORTED, not confirmed | CNN |
| 008: Optimizely via Malwarebytes | **CONFIRMED by the vendor** (status page, posted 01:02 UTC 11/17): "an unauthorized party exploited a vulnerability in Experimentation and used it to add malicious JavaScript to some customer projects. We've fixed the vulnerability and removed the injected code". Counts (178 organisations, 188 of 1,611 snippets, 32 in finance) are the researcher's; Optimizely published none. Clean from 23:11 UTC 11/16; about $7,150 in crypto taken (card said about $7,000) | Optimizely status page; Report URI |
| 008: DHS 'AI may be behind recent US outages' | A statement, not a finding: Mullin (Hannity, 11/16 night) cited an unnamed tech source; in the same remarks, CISA sees no cyber traffic, the incidents are "individually unrelated" and "98 percent" not a cyberattack | Fox (as read by CYPHER) |
| 008: United outage, cause unread | CONFIRMED by United: about 30 minutes, fewer than 150 flights, "no indication" of cyber | CNN |
| 008: Schwab website down | NOT ESTABLISHED: no outlet found | CYPHER search |

**CYPHER's verdict on 'one story': several.** Causes differ (network change, one router, a hardware bug, undisclosed); no shared supplier; AWS ended a day before Chase began. CYPHER would call it one story only on: a named common supplier or path across two items at a primary; an official statement that a cyber cause is being investigated for two or more; a corroborated responsibility claim; or matching intrusion tooling in two incidents.

**Do not relay:** six outages are one attack; AI caused the outages; banks hacked through Optimizely (the script ran on public pages; no bank's systems reported breached); HSBC or Equifax customer cards stolen (no count exists); NSA hacked; Schwab down 11/17.
