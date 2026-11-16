---
signal_id: "SIG-W-20261116-006"
date: "2026-11-16"
timestamp: "2026-11-16T18:48:20Z"
dispatched: "2026-11-16T18:48:20Z"
source: "Will's X bookmark 2122397406117466145 (@DailyMail 18:32Z) + WebSearch 2026-11-16T18:4xZ (TMZ, Boston 25, Brit Brief, yournews summaries; pages not opened)"
origin: ["X bookmark @DailyMail 2026-11-16T18:32:28Z, link not opened", "WebSearch summaries: TMZ 11/16, Boston 25 News, Brit Brief, yournews.com, Traders Union (Nick Sortor relay)"]
action: ["CYPHER"]
info: ["GIBBS", "REGINALD", "LIQUID", "CARL", "PROME"]
precedence: "IMMEDIATE"
signal_type: "catalyst"
confidence: 0.7
confidence_language: "outage reported by several outlets and Downdetector, Chase support acknowledges a technical issue; Wells Fargo leg thin; cause unknown; nothing read at a bank primary"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["JPMorgan Chase", "Bank of America", "Wells Fargo", "U.S. Bank", "Zelle", "Downdetector"]
word_count: 248
dispatch_note: "ROUTING_TABLE CYBER row v0.49: named-bank and payment-system outage, accidental included, routes CYPHER ACTION, IMMEDIATE on a named bank hit; never folded. Info GIBBS (Category I-III banks), REGINALD (banks), LIQUID (payments, Zelle), CARL pull-complete. Not established as cyber. CYPHER not live in ListAgents at 18:5xZ."
event_window: "open"
---
# Live US bank outage, Mon Nov 16: Chase customers locked out of app and website, Chase acknowledges a technical issue; Bank of America, U.S. Bank, Wells Fargo and Zelle users also report problems; cause unknown

**What is happening (Monday November 16, during US hours).** Daily Mail (Will's bookmark, 18:32Z): "Widespread banking outage at Chase, Bank of America and Wells Fargo as customers are locked out of their accounts." Search summaries (TMZ, Boston 25, Brit Brief, yournews; pages not opened): Chase customers cannot log in on the app or the website; Downdetector had over 2,000 Chase reports; Chase Support acknowledged technical problems and is working on them; Chase had not explained the cause as of about noon ET. Bank of America and U.S. Bank customers report account-access and mobile problems; Zelle users report issues; the Wells Fargo leg is thin (one outlet, no Wells statement). Symptoms reported: login failures, credit card balances showing zero, trouble viewing transactions or making transfers and payments.

**Limits.** Downdetector counts are user reports, a sign of scale, not a measured outage size. Nothing says cyber; nothing establishes whether the banks share a cause (a common vendor, cloud or network provider) or merely coincide. Last week's Microsoft 365 outage (CYB-INC-071, cards 20261113-004 and 20261114-002) was a network-change failure that hit banks unnamed.

**ACTION CYPHER:** log the incident; establish cause and whether the banks share a provider; say whether any escalation row fires. Per the CYBER row this is IMMEDIATE because named US banks and a payment system are reported hit. INFO GIBBS (JPMorgan, Bank of America, Wells Fargo and U.S. Bancorp are in your perimeter), REGINALD, LIQUID (payments and Zelle), CARL (consumer).

No position action follows from this card. $0.
