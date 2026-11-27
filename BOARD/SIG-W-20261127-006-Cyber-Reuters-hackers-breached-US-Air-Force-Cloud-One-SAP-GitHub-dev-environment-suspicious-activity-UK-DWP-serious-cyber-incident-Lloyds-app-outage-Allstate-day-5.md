---
signal_id: "SIG-W-20261127-006"
date: "2026-11-27"
timestamp: "2026-11-27T22:12:55Z"
dispatched: "2026-11-27T22:12:55Z"
source: "Reuters exclusive 2026-11-27 via US News, CNBC, Military Times; ComputerBase, Handelsblatt, All About Security 11/26 to 27; ITV 2026-11-27; The Register 2026-11-27; TechCrunch 2026-11-25, CBS; Fortune 2026-11-16; Cyprus Mail 2026-11-18 (read); all others search summaries"
origin: ["X bookmarks @unusual_whales, @MTSlive, @HormuzLetter, @Polymarket, @BBCBreaking, @TheInsiderPaper, @Kalshi, @BillEvanina (11/27)", "Rule 9 helper verify (search summaries; Cyprus Mail read)"]
action: ["CYPHER"]
info: ["GIBBS", "REGINALD", "SHADE", "HANS", "LIQUID", "VULCAN", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.75
confidence_language: "reports: tier-1 press via search summaries; no victim's own page read"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["US Air Force", "Cloud One", "Leidos", "SAP", "GitHub", "DWP", "NCSC", "Lloyds Banking Group", "Bank of Scotland", "Halifax", "Allstate", "JPMorgan Chase", "Wells Fargo"]
word_count: 511
dispatch_note: "PRIORITY under CYBER v0.49 bank-class minimum (Lloyds, Allstate). ACTION CYPHER. Info GIBBS (US large banks), REGINALD, SHADE (Allstate), HANS (UK), LIQUID (payments), VULCAN (SAP). RED, PROME by BOARD diff."
event_window: "open"
---
# Cyber and outages, Nov 23 to 27: Reuters exclusive, hackers breached the US Air Force's Cloud One platform (found in the past month, Air Force declines comment; 'control plane' and NORAD details not corroborated); SAP confirms 'suspicious activity' in its GitHub development environment (Spiegel; AI use and code alteration unconfirmed; no customer data access reported); UK DWP takes public services offline after a 'serious cyber incident' (payments unaffected); Lloyds, Bank of Scotland, Halifax apps down on payday (cause not stated); Allstate outage day 5

# Cyber and outage items from Will's bookmarks

| # | Victim | Claim / event | Read | Verdict | Channel |
|---|---|---|---|---|---|
| 1 | US Air Force Cloud One (Leidos-run) | Reuters exclusive Nov 27 (3 people): intrusion found 'in the past month or so' during an upgrade; app updates blocked, some admin rights revoked, migration paused; actor, scope, data theft unknown. NBC: a US official confirmed. Air Force: no comment on specific networks | Reuters via US News, CNBC, Military Times summaries | CONFIRMED core; 'control plane', NORAD radar, munitions tracking at 200+ sites NOT corroborated | government IT; pay apps reportedly hosted, no payment impact reported |
| 2 | SAP | Spiegel Nov 26 to 27: suspected attack on SAP's GitHub development environment, employee auth tokens stolen, code reportedly altered and copied; SAP confirms 'suspicious activity' and countermeasures ('Project Granite'), no indication of customer business-data access | ComputerBase, Handelsblatt, All About Security summaries; Spiegel not read | CORRECTED-FRAMING: a development-environment compromise; 'AI altered SAP's source code' unconfirmed | software supply chain (ERP used by banks, insurers) |
| 3 | UK Department for Work and Pensions | Pat McFadden: 'a serious cyber incident'; nearly all public-facing services down (Universal Credit portals, Pension Credit, Tell Us Once); NCSC investigating unusual activity from Thu Nov 26; benefit and pension payments unaffected | ITV, Yahoo summaries; BBC page not found | CONFIRMED; nature unconfirmed | government payment system touched, payments unaffected |
| 4 | Lloyds, Bank of Scotland, Halifax (Lloyds Banking Group) | apps and online banking failed from about 10:00 UTC Fri Nov 27 (payday), over 4,000 Downdetector reports; Lloyds: 'aware some customers are having difficulty accessing the app'; no cause or ETA by about 13:00. City AM alone links it to DWP | The Register summary | CONFIRMED outage; cyber NOT established; 'major UK banks' (Kalshi) beyond LBG not found | UK bank |
| 5 | Allstate | outage since Mon Nov 23 (login, policy, bill pay, claims submission, app roadside); claims by phone, no lapse or late fees; cause not stated | TechCrunch 11/25, CBS summaries | CORRECTED-FRAMING: day 5, still ongoing | US insurer |
| 6 | 'Past two weeks' outage list (@BillEvanina) | JPMorgan Chase and Wells Fargo outages were Nov 16 (with BofA, U.S. Bank, Capital One, Zelle); a source told NBC JPM's was a software bug, 'no evidence cyber'; FAA 11/14 router, Apple 11/17 'not a cyberattack', NSA 11/17 | Fortune, CBS, Cyprus Mail (read) | Mixed; officials see no coordinated attack | banks |

- **Per the v0.49 bank-supplier rule:** none of these is a named US core-banking or payment vendor; item 4 is a single UK banking group, one day. PRIORITY, not IMMEDIATE. Never list affected credit unions by name.
- **So what:** a dense cluster with no stated common cause: US banks Nov 16, Allstate from Nov 23, DWP Nov 26, Lloyds Nov 27, plus two confirmed intrusions (Air Force, SAP dev environment). The SAP item is the supply-chain one to watch for customer impact.
