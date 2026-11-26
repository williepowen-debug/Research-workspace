# Plaza Continental: cash collateral approved only on an interim basis to December 7; final and status hearings set for that day; an objection filed November 23 is unread
**Date:** 2026-11-26 (work 12:49 to 12:51 ET, times from `date`) | **Mode:** Cold | **Request:** PROME DOCKET L517 ("re-keyed to DEWEY's next session": re-check the free docket for a minute entry, a sale motion with a price, or a disclosure-statement hearing on Docs 119/120), run on Will's "yes" in DEWEY's window | **Confidence:** High on the docket text read; UNKNOWN on the objection's filer, target and content, and on all case economics

## Key finding

The November 17 final hearing on cash collateral did not end the question. The court continued it to **Monday 2026-12-07 at 1:30 pm PT** and approved the debtor's use of cash collateral **on an interim basis through 12/7** (entry #130). A case status hearing is set for the same time, with the debtor's **status report due 2026-12-01** (#129). Entry #128, signed 11/17, is now titled "Order **Granting in Part** Motion to Approve Turnover of Property ... Payment of the Adequate Protection Payments Contemplated by 11 U.S.C. § 362(d)(3), and Use of Cash Collateral". That settles the 11/18 report's inference about which order it was, though the order's text remains unread. **New since 11/18: an Objection (#132) and a Notice (#133), both filed 11/23.** The free feed carries only those one-word titles, so who objected, and to what, is UNKNOWN. **No sale motion, no price, and no disclosure-statement hearing appears in the free feed.**

## Evidence

| Entry | Date | Text (free feed) | Reads as |
|---|---|---|---|
| #128 | 11/17 | Order Granting in Part Motion to Approve Turnover of Property from the Receiver to the Debtor, Amendment to Scheduling Order, Payment of the Adequate Protection Payments Contemplated by 11 U.S.C. § 362(d)(3), and Use of Cash Collateral; "A Final Hearing will be Heard on November 17, 2026 at 2:00 PM"; related Doc 103; signed 11/17 | The order on Doc 103, granted in part; terms unread |
| #129 | 11/17, entered 11/19 | Status hearing continued to 12/7/2026 1:30 PM, Crtrm 6C, Santa Ana; Judge Mark D. Houle; **Status Report due 12/1/26** | Next case-level filing date |
| #130 | 11/17, entered 11/19 | Final hearing on the use of cash collateral (Doc 103) continued to 12/7/2026 1:30 PM; **"Granted on an Interim Basis through 12/7/26. Order by Attorney."** | Interim approval only; the final decision moved |
| minute entries | 11/19 | Two "Hearing Rescheduled/Continued" (Motion; Other) | Match #129 and #130 |
| #131 | 11/19 | BNC certificate of notice for #128 | Mailing only |
| **#132** | **11/23** | "Objection" (no further text in the free feed) | **Filer and target UNKNOWN** |
| **#133** | **11/23** | "Notice" (no further text) | **Subject UNKNOWN** |

Source: CourtListener's public docket feed for 8:26-bk-10986 (C.D. Cal.), fetched 2026-11-26 17:49 UTC with `scripts/recap_pull.py feed 73112993` [PRIMARY: court docket text, as mirrored]. Saved `research/2026-11-26_L517/feed.xml` (SHA-256 `a5b6acebd1381207...`) and `feed_pull.txt`. The feed holds the 30 newest entries (oldest 10/15).

## What this changes, and what it does not

- **For WAL's sheet (H1 to H11):** NO-VERDICT again. Nothing readable says anything about the Nano Banc lien, its holder, its priority or its balance. Ontario stays where WAL has it.
- **The next observables are dated:** the debtor's status report (due 12/1) and the 12/7 hearings. A final cash-collateral order, a sale motion with a price, or a disclosure-statement hearing date would be the first economic evidence.
- **#132 could matter, or not.** An objection filed six days after a contested cash-collateral hearing could come from a secured lender (Preferred Bank, or the FDIC as Nano's receiver), from the U.S. Trustee, or concern a claim or a fee. The free record does not say, and DEWEY does not guess.

## Counter-evidence and limits

- CourtListener mirrors the court and can lag or omit text; the blank #132 and #133 descriptions may be a mirror gap, not the court's entry.
- "Granted in part" and "interim basis" are docket-text labels; the order's terms (amounts, adequate-protection payments, conditions) are in the unread PDF.

## Source Quality Assessment

One primary source, the court's docket text through CourtListener's free feed, read whole for entries 127 to 133. Strong on dates and titles; silent on the content of #128, #132 and #133. Three routes to that content were not used. CourtListener's docket web page returned HTTP 403 to the honest client name `research-bot/1.0`, and was not retried under another name (WQ-735). The docket API needs the CourtListener token, which is not on this laptop (WQ-687, Will's hands). PACER costs money (Will's account, ask-first; DEWEY does not recommend a pull before the 12/1 status report is filed).

## References

- https://www.courtlistener.com/docket/73112993/feed/ (fetched 2026-11-26 17:49 UTC)
- https://www.courtlistener.com/docket/73112993/plaza-continental-group-llc/ (HTTP 403 to `research-bot/1.0`, 2026-11-26 about 17:50 UTC; not used)
- Prior reads: `output/2026-11-18_plaza-continental-hearing-result.md`, `output/2026-11-16_plaza-continental-precheck.md`

## Process report

**Searches run:** none; one feed fetch (worked without a token) and one docket-page fetch (403, stopped). **Frustrations:** the docket page now refuses the honest client name; the feed gives one-word titles for new filings. **Fix made:** `scripts/fetch_url.py`'s 403 message told the user to retry under the other client name, which WQ-735 now forbids; it now says to stop, mark the reading unavailable and tell PROME. **Confidence:** High on the dates and titles; UNKNOWN on terms and on #132 and #133. **If I had more tools:** the CourtListener token on this laptop would show #132's filer and target (the API gives the full description). **Missed at boot:** this row was due at DEWEY's next session; the 11/26 boot scan missed it until Will asked what was outstanding.
