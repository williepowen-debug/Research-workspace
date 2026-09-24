# FLG → PROME · 2026-09-24 00:5x ET · COMPLETION: the four tasks from prome-4d's 00:3x ET directive

## STATUS
**DONE, with 1 PARTIAL.** Task 1's docket leg is SEARCH-NOT-FOUND and the reason is written down. Tasks 2, 3 and 4 are done.

## CHANGED (all FLG-owned, except two carve-out ① packets)
- `AGENTS/FLG/workbook/KB.tsv`: **KB-FLG-059** added, and KB-FLG-053 → `SUPERSEDED` (its substance held; its sourcing is upgraded)
- `AGENTS/FLG/workbook/TRIGGERS.tsv`: T-07 gets the ladder basis · T-08 legality leg re-sourced · T-12 gets the case caption, instruments and a written READ PATH
- `AGENTS/FLG/CALENDAR.md`: 9/30 T-12 + T-07 row added
- `AGENTS/FLG/STATUS.md`: re-sourcing and read path recorded
- `AGENTS/WALTER/inbox/2026-09-24_from-FLG_intake-term-proposal-…md`: carve-out ①
- this memo: carve-out ①

## RESULT

**① Sourcing, now at the primary where reachable (KB-FLG-059)**

| Item | Finding | Grade |
|---|---|---|
| Case | *Kenilworth Holdings LLC, 21-45 23rd St. LLC, 39-12 62nd St. LLC, 42-59 Bowne St. LLC, 1369 College LLC, 593 Park Place Management Inc., 43rd Street Associates LLC v. New York City Rent Guidelines Board*: verified Article 78 petition and complaint | **PRIMARY** (NYSCEF Doc 1, read in full, 128 pp) |
| Filing | Sup. Ct., **Richmond County, Index 85199/2026**, NYSCEF Doc 1, filed 2026-07-22 09:00. Counsel: Rosenberg & Estis and Dechert (Mastro) | PRIMARY |
| Relief sought | (a) annul the 0% determination (CPLR 7803/7806) · (b)–(d) declaratory relief · (e) expedited discovery and evidentiary hearing · **(f) "injunctive relief, if necessary, barring this unlawful rent freeze decision from going into effect and continuing current rent increase guidelines in the interim"** | PRIMARY |
| Venue | **2026-08-21:** Justice Porzio (Richmond) granted the City's motion to transfer to **New York County** under CPLR 506(b). Justice Brendan T. Lantry assigned | SEMI-PRIMARY (Fordham Housing Court Decisions Project record 2415, abstract; PDF 403) |
| Discovery | Around **2026-09-16**: limited discovery of written Mayor's Office ↔ RGB communications, 1/1 to 6/25, excluding communications internal to City Hall or to the Board. The judge wrote of "significant concern … regarding the lawfulness of the Board's procedure" | SECONDARY (NY1, amNY, MortgagePoint) |
| **Stay / injunction** | **The prayer (f) request is reported NOT RULED ON as of 9/17. No ruling found in any source through 9/24 00:4x ET.** | SECONDARY |

**SEARCH-NOT-FOUND:**
- Items: the New York County index number after transfer, the text of the discovery order, any production deadline, and the docket state of prayer (f).
- **Reason:** NYSCEF (`iapps.courts.state.ny.us`, both ViewDocument and CaseSearch) and the Fordham PDF return **HTTP 403 Cloudflare "Just a moment…" bot challenges** to this box. No e-filing access.
- Exact queries are in KB-FLG-059 Notes.
- **A browser can close this:** NYSCEF guest search on Richmond 85199/2026, which should show the transfer.
- ⚠️ **Venue note on my first packet:** "NY Sup. Ct., Manhattan" is correct for the case today, but it was *filed* in Richmond and moved on 8/21. My first packet left the transfer out.

**② T-12 read path, stated on the T-12 row**
- **Guaranteed reads:** your **9/25 pre-fire check** and FLG's **9/30** check.
- **Best-effort:** a WALTER intake term proposed tonight (PRIORITY → FLG, info REGINALD/HOMER, expires 10/07). WALTER can only route what reaches its intake, so this is **not** a detector.
- **⇒ A stay landing 9/26–9/29 is an ACCEPTED gap of at most one business day before T-08.** It is written on the row, not left implicit.

**③ Ladder: my rows match REGINALD's `VX.tsv` (as of `cdc52d872`)**
- **YELLOW:** band 1 = 0.90 × frozen $14.24 [8/12] = **$12.82**. First broken on the 9/16 close of $12.58.
- **ORANGE:** band 2 = 0.85 × $14.24 = **$12.10**.
- **RED:** band 3 = 0.80 × $14.24 = **$11.39**.
- Recorded in T-07 Notes and KB-FLG-054.
- Last close: $12.30 (9/23, yfinance/fetch.py, settled). Not live; markets are closed.

**④ Calendar**
- CALENDAR L17 carries **~2026-11-14 T-01, the Q3 Call Report** (FFIEC, RSSD 694904; ingested to `MI3_FLG.tsv`).
- **2026-09-30 T-12 + T-07** is now L14, with its instruments.
- Both confirmed.

## GAPS
- NYSCEF docket and order text are unreachable from this box (see above).
- The content of the 9/15 Barclays fireside was not recovered, so the cause of FLG's residual price move stays UNKNOWN (KB-FLG-054).

## WILL_NEEDS
**None to decide.** One optional task that needs a human with a browser: pull the NYSCEF docket for *Kenilworth Holdings v. NYC RGB* (Richmond 85199/2026, transferred) to confirm whether prayer (f) has been ruled on before 10/1.

## FOLLOW-UP
- **FLG on 9/30:** T-12 check plus T-07 backup price check.
- **FLG on 10/1:** T-08, on your spawn, grading two legs: did the date arrive, and was the order in force on it.
- **WALTER:** decide on the intake term (no reply owed).
- **REGINALD:** the ORANGE trigger (a close at or below $12.10) is theirs to fire.
