# Plaza Continental: the court entered an order on the turnover and cash-collateral motion on November 17; its text is unread

**Date:** 2026-11-18 | **Mode:** Cold | **Request:** PROME DOCKET L517 (due today; prome-6e message 10:15 ET) | **Confidence:** High on the docket entry and its label; Medium on what the order is (inferred from the label pattern); UNKNOWN on its terms and on everything about the Nano Banc lien.

## Key finding

**One new docket entry, #128, was filed on Tue 11/17, the day of the final cash-collateral hearing. Its court label is "Turnover of Property (BNC-PDF)".** In this case the court labels its own orders with the motion type plus "(BNC-PDF)": #118 "Employ (BNC-PDF)" is the order approving the brokers, and #126 "Reject Lease or Executory Contract (BNC-PDF)" is the order granting the lease rejection. #128 is therefore very probably the court's order on the debtor's turnover and cash-collateral motion (Doc 103, whose final hearing was set for 11/17 by Doc 108). That reading is an inference from the label, not from the document. [S1, S2]

**The order's text is not free on RECAP, so the docket proves nothing new about the Nano Banc lien on this loan.** It does not show whether the motion was granted, denied or modified, any adequate-protection payment to Preferred Bank or to the FDIC as receiver for Nano Banc, a lien balance, a priority statement or a sale. Graded against WAL's pre-registered sheet (`AGENTS/WAL/research/2026-09-27_nano-banc-receivership-stupin-recovery.md` §10): **NO-VERDICT (H6 class: an order with no Nano-side fact readable).** Ontario stays at **B1** on the earlier docket evidence (Doc 100, 10/2; Doc 107 stipulation, 10/15). Nothing here moves it, and nothing here re-proves it.

## Evidence

| Check, 2026-11-18 | Result | Source |
|---|---|---|
| Court docket RSS through CourtListener, fetched 15:16 UTC | 30 newest entries, 10/09 to 11/17; **one new entry since 11/16: #128, 11/17, "Turnover of Property (BNC-PDF)"**; #127 (11/11) was the previous last entry | S1 |
| Docket-entry API, entries 127 and up (token) | #128 filed 11/17; long description blank in the mirror; RECAP document 501850401, `is_available` false, no page count | S2 |
| Minute entry for the 11/17 hearing | **None in the feed yet.** (Minute entries do appear in this feed; for example, three for 10/16.) A minute entry may lag the order | S1 |
| Label pattern, entries 108 to 127 (11/16 pull) | Orders carry "(motion type) (BNC-PDF)": #112 order on the generic motion, #113 stipulation and order, #118 order to employ, #126 order to reject the lease | S3 |
| Judge Houle's posted-calendar / tentative-ruling page | It loads, but the page needs a browser to run its scripts; a plain fetch and a form post for 11/17 both returned no day entries. **Weak evidence either way** | S4 |
| News search | Not run today (the 11/12 search found no sale, bid or price) | — |

## What the order is not

- **Not a sale, price, relief from stay or foreclosure.** Doc 103 asks to move the property from the state-court receiver to the debtor and to use cash collateral. WAL's H8 does not fire.
- **Not an ownership or priority fact about the Nano lien.** H1 to H4 need an appearance, transfer notice or succession filing by a named party. None is in the new entry. H7 (current balance), H9 (terms aimed at the Cantor V liens WAL holds) and H11 (priority statement) could sit inside the order's text, which is unread.

## Counter-evidence and limits

- **The label inference could be wrong in kind.** A "(BNC-PDF)" entry is a document sent out through the court's notice center. In this case every such entry is an order, but a turnover-related order could also be an interim order, a continuance order or a denial. Only the PDF settles it.
- CourtListener mirrors the court's feed and can lag. A minute entry or a later amended order may follow.
- **The four older documents and now #128 need PACER** (paid, Will's account, ask-first under WQ-547). PACER was not used. #128's page count is unknown; PACER charges $0.10 a page, capped at $3.00 per document.

## What this changes

| Recipient | Read |
|---|---|
| WAL | **NO-VERDICT** on H1 to H11. Ontario B1 unchanged. If #128's text is ever read, check it for H7 (adequate-protection or balance figures for the Nano lien) and H9 (any term touching the Cantor V liens). |
| PROME / L517 | The 11/17 hearing produced an order (very probably on Doc 103); the result is unreadable without PACER. Remaining observables: a sale motion with a price, a disclosure-statement hearing on Docs 119/120, or #128's text. |
| TERRY | No price, recovery, timing or ownership fact. **This supports no investment implication**, because the only new fact is that an order exists, and its contents are unknown. No card. |

## References

- **S1 PRIMARY (court docket via CourtListener RSS):** https://www.courtlistener.com/docket/73112993/feed/, fetched 2026-11-18 15:16 UTC with `scripts/recap_pull.py feed 73112993`; saved `research/2026-11-18_L517/feed.xml`, SHA-256 `3717c9f5…7933` (11/16 copy `3f163dca…84d4`).
- **S2 PRIMARY (CourtListener v4 docket-entries API):** https://www.courtlistener.com/api/rest/v4/docket-entries/?docket=73112993&entry_number__gte=127, fetched 2026-11-18; saved `research/2026-11-18_L517/de.json`, SHA-256 `897aed7d…0e58`.
- **S3 PRIMARY (RECAP documents API, 11/16 pull):** saved `research/2026-11-16_L517/rd.json`.
- **S4 PRIMARY (court site):** http://ecf-ciao.cacb.uscourts.gov/CiaoPosted/?jid=MH, fetched 2026-11-18; saved `research/2026-11-18_L517/ciao.html` and `ciao_1117.html`.
- WAL read-sheet: `AGENTS/WAL/research/2026-09-27_nano-banc-receivership-stupin-recovery.md` §10 (H1 to H11), §9b row 2.

## Process report

**Searches run:** none; three primary fetches plus one form post. **What worked:** the CourtListener token (from `~/.config/courtlistener/token`) and the docket-entry API, which gave the new entry's document ID and availability. **Frustrations:** the court's tentative-ruling page needs a browser; RECAP has no free copy of #128. **Confidence:** High on the entry, Medium on its kind, UNKNOWN on terms. **If I had more tools:** PACER for #128 (likely a few pages, at most $3.00), which is Will's call.

**Do-not-relay-as:** an approved cash-collateral order with known terms, a sale or price, lender consent, a change to WAL's Ontario branch, or any recovery signal.
