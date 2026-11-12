# Plaza Continental: no lender objection on the docket before the November 17 cash hearing

**Date:** 2026-11-12 | **Mode:** Cold | **Authority:** Will 2026-11-12 08:55 ET ("lets do the research now. start with one"), DOCKET L517 continuation, run ahead of its 11/16 check-by date. **Confidence:** High on the docket record read; UNKNOWN on case economics (documents still unavailable).

## Key finding

**No objection to the debtor's request to use the property's rents was filed by the November 3 deadline.** The court's own docket feed shows every numbered entry from 103 to 127 with no gap. None of them is an opposition, and no reply was filed by November 10. The only entry since the 11/11 read is #127 (11/11), a court mailing certificate. So the **November 17, 2:00 p.m. Pacific final cash-collateral hearing in Courtroom 6C looks set to go ahead unopposed**. That hearing is about operating money while the property is marketed. It does not deal with a sale, a price or a recovery. [S1, S2]

**Nothing in this read changes WAL's branch read or supplies economics.** The plan, the disclosure statement, the September operating report and the lease-rejection order remain unavailable on RECAP as of 2026-11-12 13:5x UTC. [S3]

## Evidence

| Item | Record | Consequence |
|---|---|---|
| Numbered docket 103–127 | Court RSS, fetched fresh 2026-11-12, 30 entries back to 10/08; numbers 103–127 complete with no gap [S1] | Every numbered filing in the window is visible by title |
| Opposition deadline Nov 3 / reply Nov 10 (Doc 108 p.2) [S2] | Entries #124 (10/31, BNC certificate) → #125 (11/9, no-hearing-requested declaration on the lease motion); no opposition entry; no reply entry | **No numbered opposition filed** by Preferred Bank, FDIC as receiver for Nano Banc, or any other party |
| #125–#126 (11/9) | Declaration that no party requested a hearing; lease-rejection order (Dapper Dine & Lounge) | Lease rejection went through unopposed; order text still unread |
| #127 (11/11) | BNC Certificate of Notice | Mailing record only |
| Doc 117 (9/30 monthly operating report), 119 (disclosure statement), 120 (liquidation plan), 126 (order), 103 (turnover motion) | `is_available=false`, no file path, checked 2026-11-12 via the recap-documents API [S3] | Cash, rents, lien balances, plan classes and priority remain **UNREAD** |
| Docs 104 (cash-collateral statement), 113 (turnover order) | Availability check throttled by CourtListener (HTTP 429), not completed | Last known state (11/11 search): unavailable |
| Free web search, 2026-11-12 (two queries) | No news since 11/11 of a bid, buyer, price or sale motion | Absence in two searches, not proof no offer exists |

## Counter-evidence and limits

- **An empty docket isn't proof of agreement.** A secured lender can still object in person at the hearing or negotiate terms beforehand. Doc 107 (the October stipulation) already had both Preferred Bank and the FDIC receiver agreeing to the turnover arrangement. No objection fits that agreement, but it may simply carry the October terms forward rather than signal any view of value.
- **Coverage:** the RSS shows titles, not documents. A late objection could be filed after 11/11, before the hearing; the 11/16 pre-check exists for exactly that.
- **No unnumbered filings:** minute entries carry no number. A paper objection that was lodged but not docketed would not appear here. Neither would an objection filed as an attachment to some other entry.
- Judge Houle's court page has a "Tentative Rulings" tab ([cacb.uscourts.gov/node/349](https://www.cacb.uscourts.gov/node/349)). Its posting schedule wasn't verified, and no tentative ruling for 11/17 was looked for today because it would be too early.

## What this changes

| Recipient | Read |
|---|---|
| WAL | No move on H1–H11. H7 (current Nano balance), H8 (sale price) and H11 (priority) remain unread. Consensual cash-collateral use is consistent with the October stipulation. |
| PROME / L517 | 11/16 check-by stays. What's left: any late objection, the judge's tentative ruling (if posted), and the 11/17 result. Plan/DS economics stay unread unless someone buys them on PACER, which is paid access and Will's call. |
| TERRY | No price, recovery or timing fact. Nothing new for a tradeability read. |

## Sources

- **S1 PRIMARY (court docket via RECAP RSS):** https://www.courtlistener.com/docket/73112993/feed/, fetched 2026-11-12. Raw saved `research/2026-11-12_L517/feed.xml`, SHA-256 `3f163dcaded90f85b01ba790dcde402d0ca6833bfdfaadbaa5f24797325f84d4`.
- **S2 PRIMARY:** Doc 108, notice of final cash-collateral hearing, filed 10/16/26, pp.1–2 (identity-verified 11/11; text `research/2026-11-11_L517/doc-108-text.txt`).
- **S3 PRIMARY metadata:** CourtListener `recap-documents` API, record ids 498401048 (117), 499226756 (119), 499226757 (120), 500834611 (126), 496891292 (103). Responses saved in `research/2026-11-12_L517/`.
- **Web (for absence only):** searches for "Plaza Continental" sale/plan news, 2026-11-12. Hits were older items, e.g. [Keen-Summit earlier Sarkis-case marketing](https://www.keen-summit.com/?p=417), [IE Business Daily, Feb 2026](https://iebusinessdaily.com/former-bankrupt-retail-project-up-for-sale/), [Bondoro filing alert](https://bondoro.com/plaza-continental-group-filing-alert/).
- Prior reads: `output/2026-11-11_plaza-continental-preread.md`, `output/2026-11-11_plaza-marketing-and-document-limits.md`, `output/2026-11-02_plaza-continental-docket-read.md`.

## Process report

**Run:** Claude Code, Opus 5.5, DESKTOP-BC6EF81. One RSS fetch; one authenticated search, which got **HTTP 502** (server side, not retried); seven document-availability calls, two of them throttled (429); three web searches. No subagents, no paid access, no outside message.
**Source frustration:** the token is exported only in interactive `~/.bashrc`. A non-login tool shell shows `auth: ANONYMOUS` until the variable is exported from `~/.config/courtlistener/token`, which was done by hand for this run.
**Self-flag:** the seven availability calls went straight through `curl`, not `recap_pull.py`. That skipped the helper's shared 5-per-minute pacing and caused the two 429s. The next pass should use the helper or pace calls 12+ seconds apart.
**Data gaps:** plan and disclosure-statement economics, the MOR, current lien balance and priority. All are PACER-only today.
**Suggestion:** a `recap_pull.py` subcommand that checks one document's availability would keep these calls inside the shared budget. It's a candidate for the BACKLOG, not a build request.

**Do-not-relay-as:** lender consent to a sale, a valuation signal, a recovery estimate, or a final hearing outcome.
