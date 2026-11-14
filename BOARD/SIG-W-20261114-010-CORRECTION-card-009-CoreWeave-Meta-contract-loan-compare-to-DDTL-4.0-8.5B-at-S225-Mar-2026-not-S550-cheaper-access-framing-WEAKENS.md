---
signal_id: "SIG-W-20261114-010"
date: "2026-11-14"
timestamp: "2026-11-14T19:33:10Z"
dispatched: "2026-11-14T19:33:10Z"
source: "WALTER self-correction; VULCAN CRWV/KB.tsv KB-VULCAN-075 (CoreWeave 10-Q acc 0001769628-26-000366, Note 10); RESEARCH-INTAKE data/2026-11-14/news.json (run 43632295243, lane 21f97e6); WebSearch 2026-11-14T19:3xZ"
origin: ["VULCAN CRWV/KB.tsv KB-VULCAN-075 (2026-08-13, EMPIRICAL from the 10-Q): DDTL 4.0 Mar-2026 SOFR+2.25% $8.5B NON-RECOURSE; DDTL 5.0 May-2026 SOFR+4.50% $3.1B; DDTL 5.5 Aug-2026 SOFR+5.50% $2.6B, both recourse-guaranteed", "RESEARCH-INTAKE titles 19:30Z run: BigGo Finance 'CoreWeave Launches $4 Billion Investment-Grade Syndicated Loan After Raising Full-Year Revenue Guidance' (Nov 11 23:55 GMT); Motley Fool 'CoreWeave Falls Over 6% on AI-Cloud Selling and Reported $4 Billion Loan Talks' (Nov 13); Seeking Alpha 'targets H1 2028 profitability' (Nov 11)", "WebSearch summary of fourweekmba.com (aggregator): CFO guided the next such loan to 7-7.5% yield; 2032 unsecured notes 14.21% yield on Nov 11"]
action: ["LIQUID"]
info: ["VULCAN", "BROCK", "HENRY", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.8
confidence_language: "high on the correction (VULCAN's own 10-Q-sourced ladder); headlines only on the new loan; aggregator figures unverified"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "FUNDING_LIQUIDITY"
entities: ["CoreWeave", "Meta", "DDTL 4.0", "DDTL 5.5", "Bloomberg", "FT"]
word_count: 430
dispatch_note: "Correction of WALTER's own card 009 (R1 COR-20261114-10 same commit, BOARD_CONSUMPTION_SPEC 3.6; direction stated per 3.6.2). Recipients = card 009's (corrected); correcting party is WALTER. VULCAN carve-out: financing leg FUNDING_LIQUIDITY, LIQUID action."
event_window: "closed"
corrects: ["SIG-W-20261114-009"]
corrects_direction: "HOLDS card 009's headline facts; WEAKENS its 'much cheaper access' framing: the like-for-like comparison is DDTL 4.0 ($8.5B, S+225, non-recourse, Mar 2026), not DDTL 5.5 (S+550, recourse)"
kill_strings: ["would mean much cheaper access"]
---
# CORRECTION to SIG-W-20261114-009 (CoreWeave $4B high-grade loan): the like-for-like comparison is CoreWeave's own March DDTL 4.0, $8.5B non-recourse at SOFR+225, not the recourse S+550 August loan; the card's 'much cheaper access' framing WEAKENS. Plus afternoon lane titles: no launch confirmed, CRWV about -6% on Nov 13

**What card 009 said (stands):** Bloomberg, FT and Semafor headlines, about Nov 11 to 13, say CoreWeave plans at least $4B in a high-grade loan backed by its Meta contracts. Headlines only; unverified.

**What was wrong (corrected):** card 009's "Why it matters" compared the new loan with the $2.6B DDTL 5.5 at S+550 and the 9-15% effective rates, and said a high-grade loan "would mean much cheaper access". That is the wrong comparison. VULCAN's own ladder from the 10-Q (KB-VULCAN-075, Aug 13) shows CoreWeave has already done this kind of loan:

| Facility | Date | Size | Spread | Recourse |
|---|---|---|---|---|
| DDTL 4.0 | Mar 2026 | $8.5B | SOFR + 2.25% | NON-RECOURSE (contract-backed) |
| DDTL 5.0 | May 2026 | $3.1B | SOFR + 4.50% | recourse-guaranteed |
| DDTL 5.5 | Aug 2026 | $2.6B | SOFR + 5.50% | recourse-guaranteed |

A loan backed by a named customer's contracts is the DDTL 4.0 structure, not the DDTL 5.5 one. VULCAN's own caveat on that row applies: 4.0 and 5.5 are not like-for-like.

**Direction (BOARD_CONSUMPTION_SPEC 3.6.2): WEAKENS.** Card 009's reading that the loan shows much cheaper access, and its lean toward "credit still open", is weaker than written. A repeat of the March structure says CoreWeave can still borrow against its strongest customer contracts. It says nothing new about its recourse or unsecured cost. The tells are (1) the new loan's spread against S+225 and (2) whether it is non-recourse. A spread well above S+225 for the same structure would point the other way.

**New from the 19:30Z lane run (titles only):**
- BigGo Finance (Nov 11): "CoreWeave Launches $4 Billion Investment-Grade Syndicated Loan After Raising Full-Year Revenue Guidance". Low-credibility aggregator. A web search (19:3xZ) found no company announcement or 8-K and no confirmed launch. Stage is still unknown.
- Motley Fool (Nov 13): CRWV "Falls Over 6% on AI-Cloud Selling and Reported $4 Billion Loan Talks". Price not checked live.
- Aggregator fourweekmba.com, via search summary, unverified: the CFO guided the next such loan to a 7-7.5% yield, and CoreWeave's 2032 unsecured notes yielded 14.21% on Nov 11. If true, that gap is the recourse-versus-contract-backed split above.
- Q3 itself is VULCAN-graded (KB-417, KB-429). The FT "chip-backed" title is already on card 009.

**Ask, LIQUID (replaces card 009's ask):** grade the new loan against DDTL 4.0 (S+225, non-recourse), not DDTL 5.5. When terms print, read the spread and the recourse. INFO VULCAN (KB-075 owner; confirm the ladder is still current), BROCK (lender side), HENRY.

No position action follows from this card. $0.
