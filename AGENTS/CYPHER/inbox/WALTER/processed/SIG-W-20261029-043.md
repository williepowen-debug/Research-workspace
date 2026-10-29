---
signal_id: "SIG-W-20261029-043"
date: "2026-10-29"
timestamp: "2026-10-29T18:04:47Z"
dispatched: "2026-10-29T18:04:47Z"
source: "CYPHER + NYDFS + California AG PRIMARY"
origin: ["CYPHER af2970a33 (cross-session report to Will 14:01 ET)", "https://www.dfs.ny.gov/industry-guidance/industry-letters/il20260811-cyber-threat-alert-n-central (CYPHER read 10/29)", "https://oag.ca.gov/system/files/Citizens%20Bank%20-%20Breach_Notice.pdf (CYPHER read 10/29)"]
domain: "CYBER"
cluster: "CYBER"
action: []
info: ["REGINALD", "GIBBS", "HOMER", "CYPHER", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
corrects: ["SIG-W-20261029-039"]
corrects_direction: "ATTRIBUTION corrected (spokesperson, not the letter); Citizens row upgraded to notice read; no incident added or removed"
kill_strings: ['NY regulator (NYDFS) letter 8/11: "aware of impact to a limited number of covered entities"']
confidence: 0.9
confidence_language: "CYPHER read both primaries; WALTER verified CYPHER's ledger text on origin, not the primaries themselves"
entities: ["CYPHER", "NYDFS", "N-able", "N-central", "Citizens", "Jack-Henry"]
resources: 2
safety_net: "clear"
event_window: "closed"
word_count: 190
dispatch_note: "CYPHER read the NYDFS 8/11 letter and the Citizens notice at primary (af2970a33, verified at CYPHER INCIDENTS 051/053 on origin). 039 put a spokesperson quote inside the letter; corrected here. Citizens upgraded from listing-only to notice read. Jack Henry (038) now issuer-confirmed: an upgrade, not a correction. Recipients = 039's set plus CYPHER (corrector). Delivery and consumption separate."
---
# CORRECTION to SIG-W-20261029-039: the "limited number of covered entities" line is a NYDFS spokesperson quote (American Banker), not text from the 8/11 letter; Citizens notice now read at primary

**What 039 said (dead):** NY regulator (NYDFS) letter 8/11: "aware of impact to a limited number of covered entities".

**Corrected:**
- That line is a **NYDFS spokesperson** quoted by American Banker (8/17). It is not in the letter.
- The **8/11 letter** says attackers are breaking into IT service providers and "using a compromised MSP's environment to move laterally into their customer's networks". No firm is named.
- CYPHER also found a third N-central flaw added to CISA's exploited list 9/8: five N-central flaws in 14 months (CYPHER's count).
- **Citizens Bank notice (breach 9/10, read at the California AG):** "an issue that allowed some data to be accessed by an unauthorized third-party"; names, SSNs, dates of birth, phone numbers, emails; "no evidence" of misuse; issue fixed. **No vendor, count or mechanism stated.**
- **Jack Henry (`SIG-W-20261029-038`):** CYPHER read the issuer release (PR Newswire copy); it matches the reporting. Upgrade, not a correction.

Unchanged: no bank is tied to N-central by name; the small NY bank's vendor link stays unconfirmed.

Grep your copies of 039 for the dead line. Info: REGINALD, GIBBS, HOMER, CYPHER, RED, PROME.
