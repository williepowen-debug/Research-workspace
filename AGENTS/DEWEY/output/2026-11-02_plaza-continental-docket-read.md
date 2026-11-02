# Plaza Continental (Ontario, CA) docket read, 9/29 forward — graded against WAL §10 H1–H11
**Date:** 2026-11-02 | **Mode:** Cold (docket read) | **Confidence:** High on what the docket text says; the filed documents that would carry balances and priority were NOT reachable | **Row:** DOCKET L517

## Key finding
**No branch move. Ontario DOT #2 stays B1 (FDIC as receiver for Nano Banc retained it), now re-observed at a later date:** on 2026-10-15 the FDIC, "solely in its capacity as the receiver for Nano Banc", signed the stipulation (Doc 107) with the debtor, Preferred Bank and the property receiver, and the court granted the underlying motion (Doc 82, the 9/29 hearing's subject) "in accordance with" that stipulation (Doc 109, 10/15; orders Docs 112/113 signed 10/16). The case has since turned toward a sale: brokers (KW Commercial-SHW and CBRE) were employed as sales agents on 10/26 (Doc 118), and the debtor filed a **Chapter 11 Plan of Liquidation** and Disclosure Statement the same day (Docs 120/119). **No sale, price, foreclosure or stay relief is authorized on the docket yet (H8 not triggered).** The plan and disclosure statement, the likely source of the Nano lien balance (H7) and a priority statement (H11), are not in the free RECAP archive.

## Evidence (all [PRIMARY]: C.D. Cal. Bankr. 8:26-bk-10986-MH docket text, via the CourtListener per-docket RSS feed `https://www.courtlistener.com/docket/73112993/feed/`, fetched 2026-11-02 08:55:51 ET; raw saved `AGENTS/DEWEY/research/2026-11-02_L517/courtlistener_feed_73112993_2026-11-02.xml`, sha256 `ff794421d051fb6b…`)

| Entry | Filed / entered | Docket text (verbatim core) | §10 row |
|---|---|---|---|
| 107 | 10/15 | "Stipulation By Plaza Continental Group LLC and Federal Deposit Insurance Corporation, solely in its capacity as the receiver for Nano Banc and Preferred Bank and Douglas Wilson (1) to Transition Receiver Out and Turn Possession and Control of Property Over to the Debtor and (2) for Payment of Adequate Protection Payments Under 11 U.S.C. § 362(d)(3)" | **H1 re-observed** (FDIC-R is a party on Nano's position); Ontario already B1 since WAL's 10/14 read of Doc 100 |
| 109 | 10/15 | Hearing held on Doc 82 (motion to approve the stipulation): "Motion Granted in Accordance with Stipulation filed as Docket No.107. Order by Attorney." | **Doc 82/88 outcome: GRANTED.** Not H6 (the FDIC-R is on the stipulation) |
| 112, 113 | 10/16 | Orders approving the stipulation: receiver transitions out, property returns to the debtor; adequate-protection payments under § 362(d)(3) | none (an order keeping the stay, not relief from it) |
| 108 | 10/16 | Notice of final hearing on use of cash collateral (Doc 103 turnover motion) | none |
| 115/116 | 10/20 | Motion to reject a restaurant lease at 3660 Porsche Way, Ontario | none |
| 117 | 10/23 | Monthly operating report, month ending 9/30/2026 | none (PDF not read) |
| 118 | 10/26 | "Order Granting Debtor's Application to Employ KW Commercial-SHW Real Estate Group, and CBRE, Inc., as Real Estate Brokers and Sales Agent" (Related Doc 98), signed 10/26 | **H8 NOT triggered** — a listing, not an authorized sale; a sale order with a price would trigger it |
| 119, 120 | 10/26 | Disclosure Statement and "Chapter 11 Plan of Liquidation Filed by Debtor" | **H7 / H11 / H9 UNREAD** — these documents would carry them; not in RECAP |
| 121–124 | 10/28–11/01 | Bankruptcy Noticing Center certificates of notice | none |

**Searched in the window (10/08–11/01 docket text), not found:** Sunwest Bank (H2), a Rule 3001(e) transfer or Western Alliance (H3), a third-party transferee (H4), a relief-from-stay, sale or foreclosure order (H8), an avoidance complaint (H9), a § 1821(d)(12) extension past the FDIC's requested 9/29–10/29 stay (H10 continuation). These are absences inside the feed's 30-entry window only.

## Counter-evidence and what this does not prove
- **Docket text is not the document.** The 107 caption shows the FDIC-R as a stipulating party; it does not state the lien's balance, priority, or that the FDIC-R still held the lien after 10/15. No recorded assignment, APN or title instrument was read. B1 remains **docket-evidenced**, not recorded-instrument-proven (as WAL wrote on 10/14).
- **Gap 9/29–10/07.** Entries dated before 10/08 are outside the RSS window. WAL's 10/13 search (since blocked without a token) covered Doc 100 (10/2) and saw snippets of 101–106; Docs 89–99 other than 93 (FDIC notice of appearance, per Doc 100) were not read by this desk today.
- **Plan of liquidation ≠ sale price.** It signals the property is to be sold; no price, buyer, bid procedure or date is on the docket text. A sale could still clear above the senior liens (~$28.3M Preferred + Nano as of the debtor's 9/8 figures, dated only) or below them; this read cannot tell.
- **Moreno Valley, Chino, Bellflower:** not touched; §10 scopes this docket to Ontario only.

## Source quality
Primary docket text, one fetch, raw saved and hashed. The CourtListener HTML docket page returned **HTTP 403 (CloudFront block) from this box** at 08:56 ET; not retried by another route. The six document PDFs tried (107, 112, 113, 118, 119, 120) **404 at RECAP storage** (never purchased into the free archive). The CourtListener search API needs a token since ~10/26–28 (WQ-531, Will's hands); a token would not unlock the PDFs above. PACER (paid, Will's account, WQ-547) was not used.

## References
- CourtListener RSS, docket 73112993, `https://www.courtlistener.com/docket/73112993/feed/`, accessed 2026-11-02 08:55 ET.
- WAL §10 read-sheet: `AGENTS/WAL/research/2026-09-27_nano-banc-receivership-stupin-recovery.md` §10; WAL's prior read: `AGENTS/WAL/research/2026-10-14_Ontario-FDIC-docket-followup.md` (commit 52884a01b, 2026-10-14 00:16 ET).
- DEWEY 9/27 primary documents: `AGENTS/DEWEY/output/2026-09-27_nano-banc-primary-documents.md` §4x; CREED collateral read `AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md` §1c.

## Process report
**Searches run:** 1 RSS fetch; 6 RECAP PDF attempts (all 404); 2 HTML docket attempts (403). **Data gaps:** plan/DS contents (balance, classes, priority), MOR, Docs 89–99. **Source frustrations:** the 30-entry feed window; nothing after 10/15 has been bought into RECAP. **If I had more tools:** PACER (Will's account, ~$0.10/page, cap $3/document) for Docs 119/120 would answer H7/H11 and show the sale timetable. **Suggestion:** Will's PACER call on Docs 119/120 is the one purchase that would close H7/H11 for Ontario; it is his money and his call (WQ-547).
