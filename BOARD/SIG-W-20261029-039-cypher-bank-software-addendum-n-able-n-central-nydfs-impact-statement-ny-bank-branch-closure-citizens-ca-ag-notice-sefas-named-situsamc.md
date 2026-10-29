---
signal_id: "SIG-W-20261029-039"
date: "2026-10-29"
timestamp: "2026-10-29T17:48:04Z"
dispatched: "2026-10-29T17:48:04Z"
source: "CYPHER"
origin: ["AGENTS/WALTER/inbox/2026-10-29_from-CYPHER_bank-software-sweep-addendum.md (commit 7bd525beb)", "AGENTS/CYPHER/workbook/INCIDENTS.tsv CYB-INC-051..053", "AGENTS/CYPHER/workbook/CHOKEPOINTS.tsv CHK-37..39"]
domain: "CYBER"
cluster: "CYBER"
action: []
info: ["REGINALD", "GIBBS", "HOMER", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.6
confidence_language: "CYPHER owner ledger; N-able/NYDFS and the branch closure REPORTED via American Banker 8/17 (NYDFS 8/11 letter not read directly); Citizens CA AG listing PRIMARY for dates only, notice letter unread; SitusAMC and Sefas SECONDARY"
entities: ["CYPHER", "N-able", "N-central", "NYDFS", "Citizens", "Sefas", "Frost", "SitusAMC", "JPMorgan", "Citigroup", "Morgan-Stanley"]
resources: 3
safety_net: "clear"
event_window: "closed"
word_count: 300
dispatch_note: "Second CYPHER bank-software pass (13:34 ET), filed to WALTER after card 038 for dedupe and routing (ROUTING_TABLE v0.49 class: PRIORITY, not folded). BOARD grep: N-able, Sefas, SitusAMC and the 9/10 Citizens notice not previously carded (038 carried the April Citizens/Frost print-mail item as class CHK-37 only). CYPHER already sent consequence packets to REGINALD, GIBBS, DEWEY; this card is the BOARD record, no new ask. Events dated Nov 2025 to Oct 2026, not today's news. Bank name in the branch-closure item withheld per CYPHER guardrail 2. Delivery and consumption separate."
---
# CYPHER second pass on bank software: an MSP tool (N-able N-central) with a regulator's statement of impact, a small NY bank's week-long branch closure blamed on a vendor flaw, a new Citizens Bank breach notice, Sefas named as the print vendor, and SitusAMC

All dated events, logged by CYPHER on 10/29; **none is a PHP2Shell (October wave) victim and none is today's news.**

| CYPHER row | Event (date) | State |
|---|---|---|
| CYB-INC-051 / CHK-38 | **N-able N-central** (remote-management tool used by IT providers): flaw exploited from 7/31, fixed 8/2. NY regulator (NYDFS) letter 8/11: "aware of impact to a limited number of covered entities"; no bank named | REPORTED (American Banker 8/17); NYDFS letter not read directly |
| CYB-INC-052 | **A small New York savings bank** closed all branches about a week from 8/3; CEO blamed "a vendor vulnerability" (vendor unnamed; N-central link NOT confirmed); a ransomware group listed it 8/7 | REPORTED, secondary; name withheld (CYPHER guardrail) |
| CYB-INC-053 | **Citizens Bank**: new California AG breach notice, breach 9/10/2026, reported 10/19/2026; names, SSNs, dates of birth per a secondary summary; count and route not stated. Separate from the April print-vendor incident | Listing dates PRIMARY; notice letter unread |
| CHK-37 | Print vendor now **named: Sefas Innovation** (SFTP server accessed Dec 2025 to Apr 2026); Frost told Texas regulators 191,848 affected | SECONDARY |
| CHK-39 | **SitusAMC** (mortgage loan platform): client data stolen, detected 11/12/2025; JPMorgan, Citigroup, Morgan Stanley among banks notified | SECONDARY; 2025 event, newly mapped |

**Why it matters:** the IT-provider route into community banks, which CYPHER's 10/23 read called "wide reach, little observed traffic" (`SIG-W-20261023-017`), has carried traffic: a regulator said firms were hit. Still no bank is tied to the tool by name. CYPHER's supplier-cluster escalation (2+ new confirmed incidents at distinct suppliers within 30 days, or a multi-institution outage of 1+ business day) is CYPHER's call; these are older events.

Info: REGINALD (community banks, Citizens), GIBBS (SitusAMC large-bank clients), HOMER (SitusAMC mortgage data, context), RED, PROME.
