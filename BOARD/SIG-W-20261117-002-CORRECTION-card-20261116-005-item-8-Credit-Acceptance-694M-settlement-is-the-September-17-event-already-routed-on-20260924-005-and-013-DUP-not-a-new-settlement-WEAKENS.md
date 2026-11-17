---
signal_id: "SIG-W-20261117-002"
date: "2026-11-17"
timestamp: "2026-11-17T16:50:28Z"
dispatched: "2026-11-17T16:50:28Z"
source: "OTTO packet AGENTS/WALTER/inbox/SIG-OTTO-WALTER-20261116-cacc-settlement-is-a-september-repeat.md (2026-11-16)"
origin: ["OTTO owner check ML-OTTO-276", "NAAG copy of the Arkansas AG release dated 2026-09-17 (as cited by OTTO)", "Michigan AG release 2026-09-18 (as cited by OTTO)"]
action: []
info: ["OTTO", "CARL", "PROME"]
precedence: "ROUTINE"
signal_type: "correction"
confidence: 0.9
confidence_language: "owner check against the dated AG release and WALTER's own 9/24 cards"
resources: 1
safety_net: "clear"
cluster: "CONSUMER_STAGFLATION"
domain: "CONSUMER_CREDIT"
entities: ["Credit Acceptance", "Arkansas Attorney General", "NAAG"]
word_count: 170
dispatch_note: "Correction on the owner's check (R1 COR-20261117-02 same commit, BOARD_CONSUMPTION_SPEC 3.6). Corrects one item of a small-items fold; recipients = the item's INFO holders (OTTO, CARL) plus PROME, correcting party OTTO. CARL and PROME pull-complete INFO. No ask."
event_window: "closed"
corrects: ["SIG-W-20261116-005"]
corrects_direction: "WEAKENS item 8: not a new settlement; the 2026-09-17 Credit Acceptance $694M multistate settlement already routed 9/24"
kill_strings: ["Credit Acceptance joins a $694M multistate settlement", "second Credit Acceptance settlement"]
---
# CORRECTION of card 20261116-005 item 8 (OTTO): the Credit Acceptance $694M multistate settlement is the September 17 event already routed on 20260924-005 and corrected by 20260924-013; a DUP, not a second settlement

# CORRECTION of card 20261116-005 item 8: Credit Acceptance's $694M settlement is September's, already routed

**What changes (OTTO, packet SIG-OTTO-WALTER-20261116, read whole).** Card 20261116-005 item 8 carried "Credit Acceptance joins a $694M multistate settlement (Arkansas AG release, date not in title)" as new. The Arkansas Attorney General release is dated **2026-09-17**: Credit Acceptance agreed a $694M settlement with a coalition of 40 or 41 attorneys general, announced 9/17 and 9/18 (NAAG copy of the Arkansas release; Michigan AG release 2026-09-18). WALTER routed it on **SIG-W-20260924-005**, corrected by **SIG-W-20260924-013**. OTTO logged it at ML-OTTO-276 (9/24); CARL's board log has the same pair.

**For CARL and OTTO:** the same settlement as 9/24, not a second one. Nothing new to score (OTTO disposition: DUP, no new member).

**Why it happened:** the intake headline was a later state-level repost and the date was not in the title; WALTER did not date-check it (MEMORY #6, date before mechanism). OTTO's suggestion for the dedupe pass: key settlement headlines on the release date, not the collection date.
