# HOMER script 2 (filing reader): read for Will

**Written 2026-11-25 21:54 ET** (Will 21:53 ET: "Can you help me with this thread"). Input: HOMER's five-item answer, pasted by Will. Read-only; nothing sent to HOMER; no scope approved.

## Checked at the file

| HOMER claim | Result |
|---|---|
| SEC access already approved (WQ-600) | CONFIRMED: `scripts/sec_contact.py` reads the one local setting; ruling in `PROME/proposals/2026-11-04_wq591-601-RULED.md` |
| Companies = listed servicers on the servicer watch | CONFIRMED in part: `registry/SERVICER_WATCH.md` names PFSI, RKT, UWMC, LDI, Onity; Rithm not found by name there. Freedom private, files no 10-Q: HOMER's claim, not checked |
| Item 4: cash, debt and MSR lines from structured filing data (XBRL) | AT RISK: SEC's structured-data service carries standard tags only. DEWEY's reader says so in its own code (`AGENTS/DEWEY/scripts/edgar_doc.py:335`: "Standard entity-level US-GAAP facts only; custom tags and segment facts need document work"). Servicer lines such as advances and hedging cash are often company-specific tags; per company, unverified by me |
| A new reader is needed | NOT SHOWN: `AGENTS/DEWEY/scripts/edgar_doc.py` (617 lines, tested by `test_edgar_xbrl_compare.py`) already does full-text search, document read, standard facts, and an evidence-preserving compare of one fact across two exact periods, which is the year-earlier comparison |

## Recommendation

1. **When:** agree with HOMER: decide after script 1's December trial. Nothing to approve tonight.
2. **Reuse, don't rebuild:** script 2 = a short list of companies and lines that calls DEWEY's `edgar_doc.py` as a command. HOMER never edits DEWEY's file; DEWEY is told it has a user.
3. **Start narrow:** two lines (servicing advances against the year-earlier quarter; MSR value and change), two companies (PennyMac plus one other, so the setup is not shaped to one filer). Add lines and companies one at a time after it works.
4. **First step of any scope:** for each line and company, find whether the figure carries a standard tag. Any line that does not goes to "print the sentence and its location", which is close to today's hand read.
5. **Honest benefit:** low on time (about six filers, four times a year). Its real value is the year-earlier comparison that went wrong this month. The stop rule should say which: time saved, or errors caught against a hand read over two quarters.

## Limits

No SEC call made; no tag looked up for any company. HOMER's line list not judged as housing analysis.
