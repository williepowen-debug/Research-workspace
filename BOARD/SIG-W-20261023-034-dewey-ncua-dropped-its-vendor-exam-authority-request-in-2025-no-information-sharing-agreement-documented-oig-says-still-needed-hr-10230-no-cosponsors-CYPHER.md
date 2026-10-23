---
signal_id: "SIG-W-20261023-034"
date: "2026-10-23"
timestamp: "2026-10-23T19:53:28Z"
dispatched: "2026-10-23T19:53:28Z"
source: "DEWEY"
origin: "Will-directed DEWEY thread 3 (no WALTER REQ), AGENTS/DEWEY/output/2026-10-23_ncua-vendor-authority-information-sharing.md (d0d5463a7)"
domain: "CYBER"
cluster: "MISC"
cluster_secondary: "BANK_COLLATERAL"
action: ["CYPHER"]
info: ["REGINALD", "RED"]
precedence: "ROUTINE"
signal_type: "research"
confidence: 0.7
confidence_language: "cited deep research; High on the documentary timeline (FSOC, NCUA OIG, testimony, congress.gov fetched and text-checked by DEWEY); Low on the mechanism (the agreements themselves are undocumented)"
resources: 1
safety_net: "clear"
word_count: 420
entities: ["NCUA", "FSOC", "NCUA-OIG", "OIG-20-07", "OIG-25-07", "Ongoing-Operations", "Hauptman", "John-Crews", "Bill-Foster", "H.R.-10230", "FFIEC", "American-Banker"]
event_window: "closed"
deep_research_ref: "SIG-W-20261023-033"
dispatch_note: "Child of the DEWEY 10/23 combined delivery (parent SIG-W-20261023-033), split on S1: different action owner (CYPHER) and independently actionable for CYPHER's MSP / vendor watch. DEWEY delivered create-only copies to CYPHER (action) and REGINALD (info) in d0d5463a7; RED is pull-complete for INFO. BOARD + route_log only. No WALTER REQ and no ledger row: Will commissioned this thread directly."
---
# DEWEY research (Will's thread 3): no document describes the "information sharing agreements" FSOC says let the credit-union regulator watch tech vendors. NCUA's 10-year request for vendor-examination authority disappeared from its inspector general's open list between March and September 2025, while the inspector general wrote in June 2025 that the authority is still needed. The only bill (H.R. 10230) has no cosponsors

**Report:** `AGENTS/DEWEY/output/2026-10-23_ncua-vendor-authority-information-sharing.md` (commit d0d5463a7).

**Why it matters:** credit unions' technology vendors sit outside any federal examiner's view. In the November 2023 ransomware attack on one vendor (Ongoing Operations), about 60 credit unions with $912M in assets and 93,000 members were affected, and bank regulators had no visibility because the vendor serves mainly credit unions (NCUA OIG-25-07). A vendor-led outage or breach at credit unions has no supervisor positioned to see it first.

| Question | DEWEY's finding | Basis |
|---|---|---|
| What changed in FSOC's wording | FSOC 2024 asked Congress for NCUA and FHFA vendor powers ("annually since 2015"); FSOC 2025 (approved 2025-12-11) names FHFA only, with a footnote that NCUA "may have sufficient authority ... through information sharing agreements" | FSOC annual reports (primary, text-checked) |
| What the agreements are | **None documented.** ncua.gov search found none; American Banker (9/21/2026): the agency "has published nothing explaining" them | primary search; news |
| When the request disappeared | OIG-20-07 open item present 3/31/2025; **absent** 9/30/2025 and 3/2026. Why it closed: UNKNOWN | NCUA OIG semiannual reports (primary) |
| Contradiction | OIG-25-07 (6/9/2025): NCUA "continues to need statutory examination and oversight authority over third-party vendors" | primary |
| Who decided | The change falls inside the one-member-board period (Hauptman; John Crews confirmed 8/7/2026, now sole member and Chairman). **Timing only; no document links the two** | NCUA press release; trade group |
| Legislation | H.R. 10230 (Foster, D-IL), referred 9/2/2026, no cosponsors; no Senate companion found (search not exhaustive) | congress.gov |

**For CYPHER:** DEWEY suggests the MSP watch row carry "NCUA vendor visibility = none documented". Free next check: the next NCUA OIG semiannual report (about late November / December 2026).

**Do not relay as:** "NCUA signed information-sharing agreements" (none documented); "NCUA abandoned oversight" (absence of a published agreement is not proof that none exists; trade groups favor an FFIEC route, and NAFCU says joint exam reports were sometimes obtained).

**UNKNOWNs:** the agreements themselves; why OIG-20-07 closed; NCUA Board minutes and budget justifications 2025–26; FFIEC annual reports (fetch failed).
