---
signal_id: "SIG-W-20261029-024"
date: "2026-10-29"
timestamp: "2026-10-29T15:33:08Z"
dispatched: "2026-10-29T15:33:08Z"
source: "WALTER"
origin: ["https://www.credaily.com/briefs/cmbs-office-payoff-rate-hits-12-8-as-retail-nears-90/", "https://news.theregistrysf.com/acore-held-34-3mm-non-performing-loan-on-shuttered-172-room-former-moxy-oakland-uptown-hits-the-market/", "https://www.cushmanwakefield.com/en/united-states/insights/us-marketbeats/chicago-marketbeats/cbd-office", "https://x.com/i/status/2115435968371028266", "https://x.com/i/status/2115232722444865963", "https://x.com/i/status/2115229557574062139"]
domain: "BANK_CRE"
cluster: "BANK_COLLATERAL"
action: ["CREED"]
info: ["REGINALD", "BROCK", "RED"]
precedence: "PRIORITY"
signal_type: "pattern-match"
confidence: 0.75
confidence_language: "Trepp via CRE Daily; The Registry and CRE Direct partly paywalled; Cushman report summary"
entities: ["540-West-Madison", "Salesforce-Tower-Indianapolis", "Moxy-Oakland-Uptown", "ACORE", "Royal-Sonesta-Minneapolis", "Laxmi-Hotels", "Trepp"]
case: ["540 West Madison, Chicago IL", "Salesforce Tower, Indianapolis IN", "Moxy Oakland Uptown, Oakland CA", "Royal Sonesta Minneapolis Downtown, Minneapolis MN"]
resources: 6
safety_net: "clear"
event_window: "closed"
word_count: 302
dispatch_note: "Will's X bookmarks (BM-20261029-04). Named-case feed (ROUTING_CARVEOUTS Sep 29): four cases, none in CREED CASES.tsv per helper grep. CREED owns case entries; WALTER does not edit the ledger. Selection bias applies. Delivery and consumption separate."
---
# Four named CRE distress cases; September office CMBS payoff 12.79% (retail 89.60%)

**Trepp (via CRE Daily, 10/27):** of **$516.9M** of office CMBS maturing in September, **12.79%** paid off on time; retail **89.60%**. Two loans are 63% of the office balance:

| Case | Event | Basis |
|---|---|---|
| **540 West Madison, Chicago** | $216.5M senior loan did not pay off at September maturity; $183.5M subordinate/mezzanine behind it; 1.1M SF | Trepp via CRE Daily |
| **Salesforce Tower, Indianapolis** | $108M loan did not pay off at September maturity | Trepp via CRE Daily |
| **Moxy Oakland Uptown (172-room hotel, closed)** | ACORE-held **$34.3M non-performing loan** to a Ten-X note auction **Nov 2–4**; receivership since ~September 2025, closed January 2026 | The Registry (403 at full text); **$2.5M starting bid unconfirmed** and is a marketing floor, not a price |
| **Royal Sonesta Minneapolis Downtown (360 rooms)** | Sold to Laxmi Hotels Group for **$5M** vs $75M paid in 2018 | CRE Direct citing the MSP Business Journal (paywall); a snippet suggests an eight-property portfolio, so **$5M may be an allocated price** and the "93% discount" is unconfirmed |

Context: Chicago CBD Q3 office vacancy **27.2%** (Class A 23.3%), 12th straight quarter of negative absorption, −1.4M SF YTD (Cushman & Wakefield, 10/7). Debt wall: CNBC 10/27 credits **Trepp $733.2B due in 2027**; the circulating "$800B this year" is an earlier estimate and its "office delinquencies 12%+" is office CMBS only (Trepp 12.16%).

CREED holds the overall September payoff figure (57.98% of $1.41B, KB-CREED-066) but not the office/retail split or these four names. Unread: the Trepp report, Ten-X listing, county deed for the Sonesta sale. Patterns off named cases carry selection bias.

**CREED ACTION:** open/verify the four cases. REGINALD (bank holders unknown), BROCK (ACORE is a debt-fund lender), RED info.
