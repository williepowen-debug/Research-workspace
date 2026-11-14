---
signal_id: "SIG-W-20261114-009"
date: "2026-11-14"
timestamp: "2026-11-14T17:33:23Z"
dispatched: "2026-11-14T17:33:23Z"
source: "PROME live pull of the new Research-Intake query ai-financing (8a4e1e5), 2026-11-14T17:30Z, relayed to WALTER"
origin: ["PROME prome-fe message to WALTER 12:32 ET Nov 14: 31 titles, 15 on this story; titles only, no body read", "VULCAN CRWV/KB.tsv KB-VULCAN-050 (S+550 DDTL, 2026-08-03) and KB-VULCAN-077 (debt at effective rates of 9-15%, 2026-08-13)"]
action: ["LIQUID"]
info: ["VULCAN", "BROCK", "HENRY", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.6
confidence_language: "reported: headline wording from three outlets as PROME relayed it; no article body read by PROME or WALTER; ages approximate"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "FUNDING_LIQUIDITY"
entities: ["CoreWeave", "Meta", "Bloomberg", "FT", "Semafor"]
word_count: 308
dispatch_note: "Not on BOARD (grep -i coreweave over November cards) and not in VULCAN, LIQUID or BROCK records. VULCAN carve-out: the financing leg routes FUNDING_LIQUIDITY, so LIQUID action and VULCAN info. Relayed titles are labelled unverified (quiet-mode rule)."
event_window: "closed"
status: PARTIALLY-CORRECTED
status_date: 2026-11-14
status_ref: "SIG-W-20261114-010 — compared with DDTL 5.5 S+550; like-for-like is DDTL 4.0 $8.5B S+225 non-recourse (VULCAN KB-075); headline facts hold"
---
# CoreWeave plans to raise at least $4 billion in a high-grade loan backed by its Meta contracts (Bloomberg, FT, Semafor headlines, about Nov 11 to 13); its last facility priced at S+550. Headlines only, from the first pull of the new ai-financing intake query

**What the headlines say (relayed by PROME from the first pull of the new `ai-financing` query, 17:30Z Nov 14; titles only, no article read, UNVERIFIED):**
- Bloomberg (about 2 days old): "CoreWeave Plans to Raise at Least $4 Billion in High-Grade Loan"
- FT (about 3.7 days): "CoreWeave plans multibillion-dollar chip-backed debt deal"
- Semafor relay (about 1.1 days): "CoreWeave seeks a $4 billion loan backed by its Meta contracts"
- Bloomberg (about 2.1 days): "CoreWeave Bonds Rise After Strong Earnings Soothe Debt Anxiety"

PROME counted 15 of 31 titles on this one story. The intake lane held no CoreWeave headline from Nov 10 to 14, and nothing on BOARD or in VULCAN, LIQUID or BROCK records carries it (WALTER grep). It reaches the lane through the new query at the next run (about 15Z Monday).

**Why it matters.** CoreWeave's last disclosed facility, the $2.6B delayed-draw term loan, priced at S+550 with OID 96-97, and its debt stack carried effective rates of 9-15% (VULCAN KB-VULCAN-050, -077, August). A $4B high-grade loan secured on Meta contracts would mean much cheaper access for the most levered AI-infrastructure borrower, in the same week Bloomberg's chart puts high-grade tech yields at their highest since 2009 (SIG-W-20261114-007 item 1). PROME's read, an inference from headlines: it supports LIQUID's 11/14 finding that a financing constraint is NOT SHOWN, because a deal getting done is access, not a wall. That grade is LIQUID's.

**Unknowns:** size beyond "at least $4B", pricing, whether "high-grade" means a rated investment-grade tranche or a secured structure, lenders, and whether it has priced or is still being marketed.

**Ask, LIQUID:** read the Bloomberg or FT body when you can reach it, and grade it against your financing-constraint read. INFO VULCAN (CRWV lane; chip-backed collateral vs your KB-VULCAN-051 borrowing-base refutation), BROCK (lender side), HENRY.

No position action follows from this card. $0.
