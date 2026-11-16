# Plaza Continental: docket unchanged since November 11, the day before the cash-collateral hearing

**Date:** 2026-11-16 | **Mode:** Cold | **Request:** PROME DOCKET L517 pre-check (check-by date today) | **Confidence:** High on the docket titles read; UNKNOWN on case economics (documents still unavailable without PACER).

## Key finding

**Nothing new has been filed in the bankruptcy case since November 11, so no lender objection to the November 17 cash hearing is on the docket.** The case is Plaza Continental Group's single-asset Chapter 11 (8:26-bk-10986-MH, the Ontario, California office property). The court's docket feed, fetched fresh today at 15:13 UTC, still ends at entry #127 (11/11, a mailing certificate). The saved feed file is byte-identical to the November 12 copy. The final cash-collateral hearing, Tuesday November 17 at 2:00 p.m. Pacific, still looks set to go ahead unopposed. It concerns operating money while the property is marketed. It is not a sale, price or recovery event. [S1]

**Nothing here moves WAL's read.** The plan, disclosure statement, September operating report and lease-rejection order (Docs 120, 119, 117, 126) are still not free on RECAP. Lien balances, plan classes, priority and any price remain unread. [S2]

## Evidence

| Check, 2026-11-16 | Result | Source |
|---|---|---|
| Court docket RSS via CourtListener (token accepted) | 30 newest entries, 10/08 to 11/11; entries 103 to 127 complete; nothing after #127; SHA-256 `3f163dca…84d4`, same as the 11/12 feed | S1 |
| RECAP document availability, entries 108 to 127 | Free: 108 (hearing notice), 116 (lease-motion notice). Not free: 109 to 115, 117 to 127, including 117, 119, 120 and 126 | S2 |
| Judge Houle's posted-calendar / tentative-ruling page | The calendar page loads; 11/17 shows no posted marker at about 10:15 ET. The page is built by script, so a static read is weak evidence; tentative rulings may still post later today | S3 |

## Counter-evidence and limits

- An empty docket is not agreement. A lender can still object in person at the hearing or settle terms beforehand. The October stipulation (Doc 107) already had Preferred Bank and the FDIC as receiver for Nano Banc on terms, which fits a quiet docket. It says nothing about value.
- CourtListener mirrors the court's feed and can lag. An unnumbered minute entry or a paper filing not yet docketed would not show here.
- **PACER is required to read Docs 117, 119, 120 and 126.** It is paid, Will's account and ask-first (WQ-547), and this brief does not authorize it. It was not used.
- No news search was run today; the 11/12 search found no sale, bid or price.

## What this changes

| Recipient | Read |
|---|---|
| WAL | No move on H1 to H11. H7 (current Nano balance), H8 (sale price) and H11 (priority) remain unread. |
| PROME / L517 | The 11/16 pre-check is done with no change. The next observable is the 11/17 hearing result, its minute entry or order, or a tentative ruling if one posts. |
| TERRY | No price, recovery or timing fact. Nothing for a tradeability read. |

## References

- **S1 PRIMARY (court docket via RECAP RSS):** https://www.courtlistener.com/docket/73112993/feed/, fetched 2026-11-16 15:13 UTC; saved `research/2026-11-16_L517/feed.xml`.
- **S2 PRIMARY (RECAP API):** https://www.courtlistener.com/api/rest/v4/recap-documents/?docket_entry__docket__id=73112993&docket_entry__entry_number__gte=103, fetched 2026-11-16; saved `research/2026-11-16_L517/rd.json`, SHA-256 `95ac9d02…a384`.
- **S3 PRIMARY (court site):** http://ecf-ciao.cacb.uscourts.gov/CiaoPosted/?jid=MH, linked from https://www.cacb.uscourts.gov/node/349, fetched 2026-11-16; saved `research/2026-11-16_L517/ciao.html`.

## Process report

**Searches run:** none; three primary fetches. **Frustrations:** the tentative-ruling page needs a browser to show posted items; a static fetch cannot confirm an empty day. **Confidence:** High on the docket titles; UNKNOWN on economics. **If I had more tools:** PACER for the four documents (Will's call).

**Do-not-relay-as:** an approved hearing outcome, lender consent to any sale, a recovery or price signal, or a change to WAL's branch read.
