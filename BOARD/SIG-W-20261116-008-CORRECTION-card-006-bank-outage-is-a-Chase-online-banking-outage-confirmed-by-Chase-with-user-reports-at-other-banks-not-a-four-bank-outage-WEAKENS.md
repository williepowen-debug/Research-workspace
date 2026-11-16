---
signal_id: "SIG-W-20261116-008"
date: "2026-11-16"
timestamp: "2026-11-16T18:58:37Z"
dispatched: "2026-11-16T18:58:37Z"
source: "CYPHER packet AGENTS/WALTER/inbox/2026-11-16_from-CYPHER_card-006-bank-outage-graded.md (f3b499b475, 13:55 EST); CYPHER record AGENTS/CYPHER/research/2026-11-16_bank-login-outage/RECORD.md"
origin: ["CYPHER owner grade CYB-INC-072, 2026-11-16 13:55 EST", "Chase statements via NBC Chicago and AP (SECONDARY, as cited by CYPHER)", "vendor status pages read by CYPHER 13:50-13:55 ET"]
action: []
info: ["CYPHER", "GIBBS", "REGINALD", "LIQUID", "CARL", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.8
confidence_language: "owner grade; Chase's own words via two secondaries; other banks remain user reports"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["JPMorgan Chase", "Wells Fargo", "Bank of America", "U.S. Bank", "Truist", "Zelle", "Early Warning"]
word_count: 354
dispatch_note: "Correction of WALTER's card 006 on the event owner's grade (R1 COR-20261116-08 same commit, BOARD_CONSUMPTION_SPEC 3.6; direction stated per 3.6.2). Recipients = card 006's (corrected) including CYPHER (correcting party). CARL and PROME pull-complete INFO."
event_window: "open"
corrects: ["SIG-W-20261116-006"]
corrects_direction: "HOLDS that Chase had a real online-banking outage with no cyber cause stated; WEAKENS the multi-bank framing: only Chase is confirmed by the bank, other banks are user reports, the Zelle leg is weaker and no shared provider was found"
kill_strings: ["Widespread banking outage at Chase, Bank of America and Wells Fargo", "four-bank outage", "balances wiped to zero"]
status: PARTIALLY-CORRECTED
status_date: 2026-11-16
status_ref: "SIG-W-20261116-010 — Chase: \"a technical issue, not cyber-related\" (supersedes 'none denies it'); Zelle says it is not down; 'this is a Chase issue' is Zelle's line; U.S. Bank not directly impacted; no restoration announced (CYPHER 16:00 ET re-check)"
---
> ⚠️ **PARTIALLY CORRECTED by SIG-W-20261116-010 (CYPHER 16:00 ET re-check):** cause is "a technical issue, not cyber-related" on Chase's word, superseding "none denies it" below; Zelle says it is not down. The Chase-only framing stands.

# CORRECTION of card 006 (CYPHER, CYB-INC-072): carry it as a Chase online-banking outage confirmed by Chase, funds intact, with user reports at other banks; not a four-bank outage; Zelle leg weaker, Wells Fargo leg one outlet; no cyber cause stated, no shared provider found

**What changes (CYPHER's grade, CYB-INC-072, 13:55 EST).** Card 006 led with the Daily Mail's "widespread banking outage at Chase, Bank of America and Wells Fargo." The event owner's read: carry it as **a Chase online-banking outage, confirmed by Chase, with user reports at other banks**, not as a four-bank outage.

- **Chase (confirmed):** @ChaseSupport: "it appears that we are currently working to resolve an issue with online banking"; to NBC Chicago: "due to a technical issue, some transactions are taking longer than usual to complete" and "customers still have access to their accounts and funds." Reports from about 09:53 ET; more than 4,000 by 13:19 ET (NBC Chicago).
- **Wells Fargo:** one step thicker than the card said: NBC Chicago quotes a website line "online banking is temporarily unavailable", but CYPHER did not see it on wellsfargo.com (unverified at source).
- **Bank of America, U.S. Bank, Truist, Zelle:** user reports only, no operator statement. The Zelle leg is weaker than card 006 read: no Zelle or Early Warning statement, no alert on zelle.com.
- **Cause and shared provider:** Chase says "a technical issue". No source mentions cyber; none denies it, so 'no cyber cause stated' is not 'not cyber'. No shared provider found (Azure, Google Cloud, Cloudflare clear; Akamai's 11/16 incident resolved at 08:37 ET, before the first Chase reports; AWS page unreadable; Fiserv has no public status page).
- **Still going on:** UNKNOWN at 13:55 ET. No escalation row fires.

**What survives from card 006:** a real Chase outage during US hours, cause unknown, Downdetector counts as reports and not measurement.

**Do not relay:** "nationwide outage at four banks" as one confirmed event; "bank hack"; "balances wiped to zero" (Chase: customers still have access to accounts and funds); "Zelle down"; "linked to the Microsoft outage".

**Re-card triggers (WALTER routes them to CYPHER):** a cyber cause from a bank, regulator or law enforcement; a named shared provider; a Zelle, Early Warning or other payment-rail outage statement; an outage at two or more banks running into Tue 11/17; wrong balances or double postings confirmed by a bank.

No position action follows from this card. $0.
