# OZK → PROME: inbox drain and four examination items (prome-6f assignment, Will 13:45 ET)

**Date:** 2026-11-16 ~14:30 ET · **Desk session:** OZK, Opus 5.5 (claude-opus-5-5), Claude Code, desktop checkout; session id not exposed · **Desk commit:** `0f69a577ba` (OZK files only) · **Git:** no pull and no push, per your instruction; worked on the checkout as found (HEAD 3b7bd2660a at boot; 2 PROME state files dirty, not touched).

**Boot:** read root `CLAUDE.md`, `AGENTS.md`, `USER.md`, `AGENTS/OZK/CLAUDE.md` (no local `AGENTS.md` exists), STATUS, LESSONS, CALENDAR, MEMORY. boot.py rc 0. Corrections check rc 0 (0 named outstanding). Tools: web search and SendMessage available; Quartr not called (no subscription, standing rule); pdf-viewer and Prisma MCP servers failed to connect (not needed).

## 1. Inbox drained (4 packets, all moved to `inbox/processed/`)

| Packet | Disposition | What it changed |
|---|---|---|
| DEWEY 003R full-population refresh (11/11) | Information. OZK is not one of the six banks; the full Q3 $10–100B band trigger is OFF quarter to quarter, ON year over year | **Nothing.** OZK cites no 003R figure anywhere (grep 11/16). Relay rule recorded in STATUS: any DEWEY smaller-bank figure travels with the United Fidelity caveat and the leave-one-out comparison |
| DEWEY 003R placement continuation (11/11) | Information; comparator-date rule noted | Nothing |
| DEWEY 003R six-bank partial (11/11) | Retained as information, as the packet asks | Nothing |
| DAEDALUS WQ-678 harness lines (11/12) | **A1 applied** (non-ff → root session-end step 3). **Optional trims C24–C32: all applied**, none declined (pull per root; collapsed the duplicate local Git section to a pointer; dropped the conviction parenthetical, the "#1 rule"/"file > verbal" duplicates, the duplicate read list, the cd-wrapper explanation, two history clauses, dated scope lines). Also cut a stale "OZK-09 45%" inside the MI3 line to "OZK-09" (removal only) | `AGENTS/OZK/CLAUDE.md` 22,832 → 21,193 B. No authority, route or threshold moved (class C4) |

## 2. Own open rows, graded by my own rule

| Row | Due? | Grade |
|---|---|---|
| DOCKET L588 sub-notes call-notice window, 11/2 → 12/22 | Open, not due until 12/22 | Not pre-graded. Today's read is item 5 |
| DOCKET L810 charter hot/cold split | OZK leg DONE 10/28 (8e3d7ce23); charter now 21,193 B = 65% of budget | Nothing owed by OZK |
| CALENDAR: Boston land maturity (Dec), Q4 print (~1/19/27), short interest 11/13 settlement (~11/24), OZK-11/12 (RESOLVE_BY 2027-03-01) | None due today | Not pre-graded |

No row naming OZK is due on 11/16 by my rule.

## 3. Who is paying to extend: logging only; moves no score, band, gate or trigger

**The lines live at `AGENTS/OZK/research/threads/2026-11-16_WHO_PAYS_TO_EXTEND.md`** (pointer in STATUS Open Items 2b and Recent Developments). Sources: Q3 Management Comments Fig 23, Fig 25 and p.28 (FDIC FLNG 12022), 8-K FLNG 12019, the Q3 10-Q and Call Report.

- **RaDD (San Diego, IQHQ; $579.1M funded):** sponsor and mezz lender ($100M fresh 10/9; about $1.23B invested), plus up to $121.3M of lender re-advance and a $28.6M sponsor-supplied reserve. **Maturity December 2029.** The loan rate is undisclosed, so months of carry are UNKNOWN. ⚠️ An illustration on an ASSUMED 7% rate puts the reserve at about 8 to 9 months and the reserve plus full re-advance at about 3.7 years.
- **Boston land ($105.9M substandard accrual, current on payments):** payer UNKNOWN; $0.5M unfunded. **Matures December 2026.**
- **Baltimore land ($40.0M nonaccrual, 303 days past due):** nobody pays; the bank forbears until its note sale closes, expected Q4-26 or Q1-27, or else takes title.
- **Lake Tahoe ($23.6M substandard accrual since 2019):** the lender, with $19.6M of advances left to finish construction. Maturity UNKNOWN in my record.
- **Special-mention pair ($209.9M, condo and office, unnamed):** UNKNOWN / UNKNOWN.
- **Foreclosed RESG properties ($416.0M, 7 assets):** the bank itself, with $9.8M of holding cost in Q3, for as long as it chooses.
- **345 N Morgan, Chicago:** a takeout lender (DekaBank $79M, reported; ⚠️ one source chain, payoff primary unread).
- **Book-wide:** sponsors put in $956M of reserve deposits and $581M of paydowns over 711 modifications in 17 quarters (50 in Q3). $6,049.4M of construction loans sit on interest reserves, with $87.1M capitalized in Q3.

**Read across:** the bank, not a sponsor, now funds the delay on about $480M. Boston land's December maturity is the nearest date at which a payer must show itself.

## 4. Read cap

`read_cap_check.py --agent OZK` at boot: rc 0; STATUS 23,843 B = 73% of budget, 569 B under the 75% trigger. I was about to add to STATUS, so I **rotated it by my hot/cold rule**: 7 Recent Developments rows (10/6 – 10/12) moved **verbatim** to `AGENTS/OZK/archive/STATUS_HISTORY_2026-11-16.md` (all 7 rows checked byte-identical against HEAD). STATUS is now 21,279 B = 65%, under the 70% stop line. The charter is 65% after the WQ-678 trims. The re-run after the edits returned rc 0 with rotation_due=0. MEMORY is 55%, CALENDAR 27%, LESSONS 47%: nothing owed.

## 5. Sub-notes call-notice window (DOCKET L588)

**Seen so far (11/2, 11/11, 11/16): no call notice.** FDIC FLNG returned 185 filings with none after 12040 (boot, ~14:03 ET 11/16); two press searches found nothing. ⚠️ A holder notice need not be public, so silence is not proof. The next press check is mid-December.

## Trade read

**No material finding, no direction.** Item 3 re-files Q3 disclosures already on the record; it adds no new evidence and fires no trigger. Nothing goes to TERRY from this session. Live price: OZK $50.46, −0.59% (fetch.py ~14:03 ET 11/16), in line with KRE −1.1%. No band is near: <$45 is $5.46 below.

## Not done / flags

- Orphan check shows WAL workbook files dirty (`KB.tsv`, `KB_INDEX.md`, `PREDICTIONS.tsv`) that belong to WAL, not to me. Flagged, not touched.
- Holding open as instructed; not closing out until PROME asks.
