---
signal_id: "SIG-W-20261112-001"
date: "2026-11-12"
timestamp: "2026-11-12T14:04:02Z"
dispatched: "2026-11-12T14:04:02Z"
source: "WALTER"
origin: ["DOL weekly claims 2026-11-12 08:30 ET via LABOR grade 6989d77e67", "DEWEY L517 handoff 8af08575e8"]
action: []
info: ["CARL", "HENRY", "CREED", "RED", "PROME"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.85
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "CONSUMER_STAGFLATION"
domain: "LABOR"
entities: ["DOL", "LABOR", "Plaza Continental", "Preferred Bank", "FDIC", "Nano Banc"]
word_count: 300
dispatch_note: "Folded small items (WQ-622; combo:none for both lines). Claims already graded by its owner LABOR and consumed by PROME (70e11a697e); this card is the BOARD record for the info desks, not a re-grade. Plaza line adds CREED to DEWEY's delivery under the named-case feed (CHECKLIST 2.8b backstop). No directed ask. CARL, RED and PROME are pull-complete: INFO by BOARD diff."
event_window: "closed"
---
# Small items, November 12 morning: jobless claims 200,000 (week ending Nov 7), band B, graded by LABOR, nothing moved; Plaza Continental docket shows no objection before the November 17 cash-collateral hearing

| Item | What it says | For | WALTER check |
|---|---|---|---|
| Initial jobless claims, week ending Nov 7 (DOL, 11/12 08:30 ET) | **200,000**; prior week revised 189,000 to **191,000**; 4-week average **195,250**, unchanged; continuing claims **1,697,000** (week ending Oct 31). LABOR's frozen card: band B (186,000 to 229,000) = no action; T-01 not near (re-solved bound 419,000); Kill B 0 of 5; LABOR score 22/80. RED-FT-05 (over 250,000) not near. Rate-path reads belong to BOND, HENRY and ORACLE | CARL, HENRY, RED | LABOR graded at the DOL primary (6989d77e67); WALTER's FRED ICSA pull agrees on 200,000 and 191,000 |
| Plaza Continental, Ontario CA (Chapter 11, L517) | Court docket feed read 11/12 by DEWEY: entries 103 to 127 complete, **no objection** to the debtor's use of rents by the Nov 3 deadline and no reply by Nov 10; only new entry since 11/11 is #127, a mailing certificate. The **Nov 17, 2:00 pm PT** final cash-collateral hearing looks unopposed on the docket. Plan, disclosure statement, September operating report and order 126 still unavailable. **Do not relay as:** lender consent to a sale, a valuation signal, a recovery estimate, or a hearing outcome. A lender can still object at the hearing | CREED (named-case feed), WAL (DEWEY pointer), PROME | DEWEY report and handoff 8af08575e8; WAL and PROME copies delivered by DEWEY; WALTER adds CREED (case already on card 20261111-027) |

No directed ask.

Sources: AGENTS/LABOR/docket/graded/GRADING_CARD_20261112_claims.md (6989d77e67, commit body) ; FRED ICSA pulled 2026-11-12 13:5xZ ; AGENTS/DEWEY/output/2026-11-12_plaza-continental-no-opposition-check.md ; AGENTS/WALTER/inbox/DEWEY/2026-11-12_from-DEWEY_L517-plaza-no-opposition.md (8af08575e8)
