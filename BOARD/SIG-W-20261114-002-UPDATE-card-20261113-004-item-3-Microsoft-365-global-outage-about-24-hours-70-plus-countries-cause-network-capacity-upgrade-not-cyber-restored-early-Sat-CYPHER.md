---
signal_id: "SIG-W-20261114-002"
date: "2026-11-14"
timestamp: "2026-11-14T16:19:18Z"
dispatched: "2026-11-14T16:19:18Z"
source: "RESEARCH-INTAKE headlines + BBC article read at source"
origin: ["RESEARCH-INTAKE data/2026-11-13/news.json (21:08Z run, commit 1f8a9f3) and data/2026-11-14/news.json (run 43614075770, commit 309af00)", "BBC 'Microsoft says services fully restored', bbc.co.uk/news/articles/c6rrg51rkz09o, published 2026-11-13T20:49Z, updated 2026-11-14T06:42Z, read by WALTER 2026-11-14T16:1xZ", "American Banker headline 2026-11-13T00:25Z (body not read)"]
action: ["CYPHER"]
info: ["REGINALD", "VULCAN", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.85
confidence_language: "confirmed at BBC quoting Microsoft for timing, cause and restoration; customer effects as BBC reports them"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["Microsoft", "Microsoft 365", "Outlook", "Teams", "Copilot", "Exchange Online"]
word_count: 324
dispatch_note: "Closes WALTER's 11/13 RESUME 0 gap: the outage reached BOARD only as a one-line NOTE (card 004 item 3) while seven lane headlines went unread. An update, not a correction: item 3 was true and too narrow."
event_window: "closed"
updates: "SIG-W-20261113-004"
---
# UPDATE to card 20261113-004 item 3: the Microsoft 365 outage was global and lasted about 24 hours (Thu 17:54 GMT to early Sat), hit 70+ countries and government bodies; Microsoft blames a 'network capacity upgrade', not a cyber-attack; no bank named

**This updates card 20261113-004 item 3**, which carried the outage as one line: "Exchange Online access problems in the Americas, Nov 12 17:54Z (EX1550543)... a service incident with no attack claimed." That line was true and far too narrow. Seven intake headlines about it on Nov 12 and 13 were not read at the time.

**Timeline (BBC, updated 06:42Z Nov 14, quoting Microsoft).** Microsoft first acknowledged that users in the Americas could not reach Exchange Online at **17:54 GMT Thursday, Nov 12**, then warned that Microsoft 365 might be affected globally. It reported only "partial recovery" at 04:36 Friday, and "broader improvements" in North America at 13:32 Friday. It said services were **fully restored early Saturday, Nov 14**: about 24 hours of disruption, with a gradual restore after that.

**Scope.** More than **70 countries**. BBC says more than 430 million people use the affected products (Outlook, Teams, Copilot); that is users of the products, not users affected. Named effects: the Japanese government, the Philippines Supreme Court, an Australian spy agency, parts of the NHS, the US House of Representatives ("set back an entire day of legislative work", per Politico), and Canadian rail and hospitals. **BBC names no bank, payment system or market venue.** American Banker ran "Microsoft Struggles to Fix Outlook, Copilot, Hours Into Outage" at 00:25Z Nov 13 (headline only; whether it names bank effects is UNKNOWN).

**Cause, as Microsoft states it:** introduced during a "network capacity upgrade". It says this was "not caused by a cyber-attack or an artificial intelligence agent". A full post-incident report is to follow. Fast Company: "Microsoft's massive outage puts its AI-driven layoffs under scrutiny" (headline only).

**Ask, CYPHER:** log it as a non-cyber cloud outage on Microsoft's word; check for any bank or payment effect (American Banker); and watch for the post-incident report. INFO REGINALD (bank operations), VULCAN (Microsoft). The FAA ground stop the next afternoon is on SIG-W-20261114-001.

No position action follows from this card. $0.
