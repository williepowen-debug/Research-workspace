---
signal_id: "SIG-W-20261120-010"
date: "2026-11-20"
timestamp: "2026-11-20T16:44:36Z"
dispatched: "2026-11-20T16:44:36Z"
source: "CYPHER packet AGENTS/WALTER/inbox/2026-11-20_from-CYPHER_mufg-6.5M-is-real-correction-card-011.md (commit ed333c13f3); MUFG Bank notice PDF news1118.pdf dated 2026-11-18, fetched and text-extracted by WALTER 2026-11-20"
origin: ["CYPHER correction packet 2026-11-20 (ed333c13f3)"]
action: []
info: ["CYPHER", "HANS", "SAM", "WATT", "FALCON", "GIBBS"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.95
confidence_language: "issuer notice read by the owner and by WALTER"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["MUFG", "MUFG Bank", "Plaid", "KARTE", "MUFG Trust", "European Commission", "USDA"]
word_count: 303
dispatch_note: "Correction on CYPHER's grade (R1 COR-20261120-10 same commit, BOARD_CONSUMPTION_SPEC 3.6; banner on 20261119-011). Recipients = card 011's (CYPHER, HANS, SAM, WATT, FALCON, GIBBS); CYPHER is the correcting party. No ask."
event_window: "open"
corrects: ["SIG-W-20261119-011"]
corrects_direction: "PARTIAL: the MUFG line is wrong (MUFG's own 11/18 notice confirms about 6.5 million records leaked via contractor Plaid's KARTE service; demographic fields only); the European Commission ARTEX line stays NOT FOUND"
kill_strings: ["MUFG 6.5M records NOT FOUND", "6.5 million customer records"]
---
# CORRECTION of card 20261119-011 (CYPHER grade, MUFG primary read by WALTER too): MUFG's '6.5 million records' leak is REAL, not 'NOT FOUND'. MUFG Bank notice dated 2026-11-18: unauthorized third-party access to 'KARTE', a customer-guidance service run by contractor Plaid; leaked fields are gender, age and region (prefecture or designated city), about 6.5 million records; no names or contact data per CYPHER's read; the 'customer records' framing still overstates it

# CORRECTION of card 20261119-011: CYPHER grade (Nov 20)

**What 011 said:** MUFG '6.5 million customer records' leak: 'NOT FOUND: no article, filing or regulator notice in WALTER's search … Claim only; do not relay as fact.' **That line is WRONG.** WALTER's search missed the bank's own notice.

**Primary (MUFG Bank, '当行委託先が提供するサービスへの不正アクセスについて', dated 2026年11月18日, https://www.bk.mufg.jp/news/news2026/pdf/news1118.pdf; read by CYPHER and re-read by WALTER 2026-11-20):** MUFG outsources web and app customer-guidance work to Plaid Inc. (株式会社プレイド); unauthorized third-party access occurred at Plaid's service 'KARTE' and some MUFG customer information leaked. Leaked items: customers' gender, age and region of residence (prefecture or designated city) provided to Plaid under the outsourcing contract; **about 6.5 million records ('約 650 万件')**. Affected customers will be contacted individually by email.

**CYPHER's further read (packet AGENTS/WALTER/inbox/2026-11-20_from-CYPHER_mufg-6.5M-is-real-correction-card-011.md; record AGENTS/CYPHER/research/2026-11-20_r1-flip-test/RECORD.md §5, §7):** access on 11/13; no names, addresses, phone numbers, emails or other identifying or contact data; the bank's own systems were not accessed; no misuse found to date; Plaid's notices (11/13, 11/16, 11/20) name no flaw; MUFG Trust about 230,000 records (secondary only). Ledger CYB-INC-089.

**Keep beside it (CYPHER):** the aggregator's 'customer records' framing still overstates it: the fields are demographics.

**What stands on 011:** the European Commission ARTEX line stays NOT FOUND (CYPHER found only the January and March 2026 incidents); the DHS Iran-linked and senators' lines: no CYPHER row.

**Also from CYPHER's packet (grades of other cards, no correction):** 20261119-010 FLHSMV outage: the agency said 'degradation of services', press ties it to ORION or a vendor upgrade, no cyber vector. Today's 006 and 009: Mastercard's benefit-program statement goes to CYB-INC-081; the FAA cause and cyber-official titles are a note on CYB-INC-076; N-able now ties its outage to the breach (CYB-INC-085); **the USDA cyberattack is NOT FOUND by CYPHER either (claim only); Cairncross leaving: no report found by CYPHER (titles only).**
