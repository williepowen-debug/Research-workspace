---
signal_id: "SIG-W-20261118-005"
date: "2026-11-18"
timestamp: "2026-11-18T15:21:34Z"
dispatched: "2026-11-18T15:21:34Z"
source: "RESEARCH-INTAKE data/2026-11-18/news.json item 154 (American Banker, 2026-11-17 21:54Z, title only); BBC World 2026-11-18 04:57Z (title); web search 2026-11-18 15:2xZ found no second source"
origin: ["RESEARCH-INTAKE lane, bank-vendor-incidents-core query, collect 2026-11-18T13:11Z"]
action: ["CYPHER"]
info: ["GIBBS", "REGINALD", "LIQUID"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.4
confidence_language: "one trade-press title, page unread, no second source; may repeat a carded event"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["HSBC", "Associated Banc-Corp", "American Banker", "Optimizely", "Rubio"]
word_count: 162
dispatch_note: "CYBER row: every cyber item routes to CYPHER; v0.49 forbids folding a bank or bank-vendor incident into the ROUTINE card, so this is its own card. Precedence PRIORITY, not the row's IMMEDIATE for a named bank hit, because the only evidence is an unread title that may repeat card 008's already-carded event; CYPHER may escalate. Info: GIBBS (HSBC, large bank), REGINALD (Associated, regional bank), LIQUID (bank sites/payments). TERRY BOARD-only."
event_window: "open"
---
# American Banker title (Nov 17 21:54Z): 'HSBC, Associated sites briefly affected by cyberattack'; page not read and no second source found; HSBC was named in card 008's Optimizely supply-chain compromise (Nov 16), so this may be the same event: NOT established; Rubio says the US is 'not under systemic attack' after the series of tech outages (BBC title)

# HSBC and Associated bank sites, cyberattack title (CYPHER to grade)

**What WALTER has:** one RESEARCH-INTAKE title, American Banker, dated 2026-11-17 21:54Z: 'HSBC, Associated sites briefly affected by cyberattack' (query bank-vendor-incidents-core). **The page was not read** (American Banker is paywalled to this desk) and a web search found no second report of a November 2026 event at Associated Banc-Corp or HSBC; the search returned only HSBC's October 2025 credential-stuffing incident and an older DDoS (date traps).

**Possible overlap, not established:** card SIG-W-20261117-008 carried the Optimizely supply-chain compromise of Nov 16 (malicious JavaScript on 178 organizations, 32 in banking and finance, HSBC named; CYPHER: confirmed by the vendor, card 012). 'Associated' is presumably Associated Banc-Corp (Green Bay, Wisconsin), a regional bank; that identification is WALTER's inference from the title.

**Context title:** BBC World 2026-11-18 04:57Z, 'Rubio says US not under systemic attack after series of tech outages'.

**Ask:** CYPHER, say whether this is card 008's event or a new incident, and grade it.
