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

## Will's word (2026-11-25 22:02 ET)

"no trials lets just do it". Read by DAEDALUS as: build script 2 now, without waiting for script 1's December trial, at HOMER's full scope (six servicers, six lines). Recommendations 2 and 4 above (reuse DEWEY's tool; check tags first) carried into the paste block for HOMER; 3 (start narrow) and 5 (two-quarter trial) dropped per Will. Builder: HOMER. Relayed by Will pasting into HOMER's window, not by peer message.

## Build read (2026-11-25 22:45 ET; HOMER f93dc17539, `AGENTS/HOMER/tools/filing_reader.py`, 373 lines)

| Claim | Result |
|---|---|
| `--selftest` | REPRODUCED: 5 malformed refused, 6 behaviour checks pass; no file written |
| `check`: 5 of 5 hand readings match | REPRODUCED by DAEDALUS run (rc 0; PFSI advances, liquidity, hedge; LDI 60+ DQ, equity). Network via DEWEY's reader and `sec_contact` (WQ-600); nothing written |
| DEWEY's file not edited; DEWEY told | CONFIRMED: last edit to `edgar_doc.py` is DEWEY's 26596405af; packet `AGENTS/DEWEY/inbox/2026-11-25_from-HOMER_depends-on-edgar_doc.md` |
| Writes one draft only | CONFIRMED in code: one file under `reports/filing_drafts/`; charter change is the tools-table row only |

Notes, none blocking:
1. "Untagged" means none of the one to four standard names tried (`CANDIDATES`), not that no tag exists. PennyMac and UWM MSRs show untagged; likely company labels.
2. The three stress lines (advances, liquidity cushion, 60+ delinquency) are untagged at all six. For those the draft is a locator; the check proves the text rows only at PennyMac and loanDepot, and loanDepot already shows wrong-row matches.
3. Re-running an old period after a later filing carries the same balance-sheet date (for example period 2026-12-31 after the Q1-2027 10-Q) makes the filing finder refuse: a loud failure, not a wrong figure. February first use is unaffected.
4. A change to DEWEY's `doc` layout shows as "not found", caught only by running `check`; HOMER runs it first.

## Ideas to make it more useful (Will 22:47 ET asked; ideas only, none begun, nothing sent)

1. Read the filing's statement pages (the R*.htm tables EDGAR renders in each filing folder) instead of searching the whole 10-Q: one clean table per statement, company labels included, year-earlier column alongside. Cash flow lines (advances, hedge cash) are on the face statements, so tagged in the filing itself under company labels that SEC's standard-tag service drops. `edgar_doc.py exhibits` already lists them and `doc --doc` may read them: unverified; `choose_doc` excludes them today.
2. Remember the right row: once a quarter is hand-confirmed, store each company-and-line label that was correct; next quarter look for that label first, search only as fallback. Removes the loanDepot wrong-row class.
3. Show the change against last quarter's draft beside each figure. Print only; no threshold, flag or grade.
4. Optional: run on the earnings-release 8-K (two to four weeks before the 10-Q; text only, no tags). Earlier, less exact.
5. Optional, checker-like (Will prefers fewer): print sentences with covenant-waiver, facility-draw or going-concern wording, which map to servicer-watch classes B and C. Prints only; never an alarm.
Not recommended: more companies, or any threshold or alert.
