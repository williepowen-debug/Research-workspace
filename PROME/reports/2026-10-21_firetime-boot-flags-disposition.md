# Fire-time boot flags — disposition (boot 2026-10-21, session af287aee)

**Source:** `/tmp/prome-boot-af287aee/checks/04-firetime-owner-routed-flags-persist-.txt` (boot gate run 08:1x ET; `scripts/firetime_check.py --window 7`). The gate line said "47 flags". That count is **26 date warnings across 15 artifacts + 19 dead pointers across 12 artifacts + 2 unreadable references.** It is not 47 wrong dates. (Correction to PROME's own 08:2x ET boot report, which called them "47 date-mismatch flags in desk files"; Will relayed the correction at 08:47 ET.)

**Method:** for each date warning, PROME printed the flagged token in its line of the artifact and read what the date refers to (the logic re-read BOOT step 5 requires). For each pointer, PROME searched the repo for the path and the basename. No artifact was edited.

## A. Date warnings — 26 flags / 15 artifacts → 0 wrong dates

The checker reads short `M/D` and `MM/YY` tokens as dates in the next 45 days, then reports them as "near" unrelated DOCKET rows (Colorado River backstop 12/31, the OZK sub-notes call-notice window, the Makhijani trial date). Every flag below is one of four classes.

| Class | Flags | Artifact (token) | What the token is |
|---|---|---|---|
| Fraction / score / ratio | 8 | WAL STATUS L57 (`1/5`); WAL Q2_10Q_READ L66/L303 (`1/5`); REGINALD VLY_CRE_transmission L58 (`1/6`); CREED VLY_property_comparable L14/L46 (`1/16`, `1/6`); NEXUS brief_health L9 (`1/17`); LABOR STATUS L50 + PROME/inbox/processed LABOR 10/15 packet L31 (`12/24`) | a V-score, a share of a book, a gap rate, a hit rate. Not dates. |
| Historical period label (MM/YY) | 9 | REGINALD nano-banc-forensics L28/29/87/98 (`12/23`, `12/24`, `12/25`); REGINALD VLY_CRE_transmission L45/L72 (`12/23`, `12/24`, `12/25`); OZK CRE_LOSS_TRANSMISSION L30 + Q2_WORKOUT_CHECK L22/L30 (`Dec-25`); BROCK catchups/2026-10-09 L63 (`12/24`) | quarter-end labels (Dec 2023/2024/2025) on Call Report and 10-Q series. Not future dates. |
| Historical full date | 4 | DEWEY nano-banc-primary-documents L47/L125 (`1/18/2022`), L377 (`01/01/2025`), L381 (`1/13/2023`); FLG WQ312_Q2_workout_rows L23 (`1/19/26`) | past events written with their year; the checker dropped the year. |
| Real forward date, owner-internal | 5 | CORAL STATUS L106 (`2027-01-04`, Fannie LL-2026-03 effective date, sourced); LABOR STATUS L121 (`2027-01-15` fold-by, `2027-01-01` CA SB 951 effective, INFERRED by LABOR); PROME/reports/2026-10-09_L624 read 3 L33/L82 (`2026-12-29`, `2027-01-07` — test-case run dates inside a review record) | correct as written. None is a DOCKET obligation: the first three are desk-calendar dates kept by their owners; the last two are test fixtures. |

*(8 + 9 + 4 + 5 = 26 flags.)*

**Disposition:** no artifact edit is owed, so no owner packet is sent for class A. The defect is the checker's: it parses fractions and MM/YY period labels as dates. This is recorded as a DOCKET row for the check's owner. PROME did not add allowlist rows, because that would be a fourth process change this session (ceiling 3) and would hide the class instead of fixing it.

## B. Dead pointers — 19 flags / 12 artifacts

| Class | Flags | Artifact → pointer | Finding |
|---|---|---|---|
| Resolves inside another desk (citation lacks the owner prefix) | 12 | PROME proposals/2026-09-05_spawn-driver → `BLUEPRINTS/meta-agent.md`, `profiles/FERT.md` (both in AGENTS/DAEDALUS); CREED nano-banc-collateral → `reports/…/dossier_EGBN.md` (REGINALD); DEWEY nano-banc-primary-documents → `reports/…nano-banc-failure-forensics.md` (REGINALD), `research/…stupin-recovery.md` (WAL); OZK CRE_LOSS_TRANSMISSION and Q2_WORKOUT_CHECK → `reports/…q2_OZK.md` ×2, `reports/…loss_bridge.md` (REGINALD); PROME ROSTER → `registry/FALSIFICATION_TRIGGERS.tsv` (RED), `scripts/flng_watch.py` (OZK), `workbook/CATALYSTS.tsv` (generic per-desk pattern); PROME reports/2026-10-12_SHADE-freshness → `sources/…/ACCESS_RESULT.json` (SHADE) | every target exists. These are unqualified relative paths (`finding_unqualified_identifier_is_a_defect_waiting_for_a_reader`). Low consequence; fixed by each owner as touched. Not chased. |
| Not a path (prose / template / guard text) | 3 | PROME/CLAUDE.md "PROME docs/handoffs" (prose), `memory/YYYY-MM-DD.md` (template); NEXUS CLAUDE.md `AGENTS/PROME` (the warning that it must NOT exist) | checker false positives. |
| Session-ephemeral, correctly gone | 2 | PROME proposals/2026-09-25_wq299 → `scratchpad/wq299result.md`; PROME reports/2026-10-09_L624 read 3 → `harness/cx2.py` | scratch paths of past reads; the findings are recorded in the citing files. |
| **Real** | 2 | PROME/inbox/processed/2026-10-15_from-LABOR_crash-recovery-claims-graded.md → `AGENTS/LABOR/docket/GRADING_CARD_20261015_claims.md` (MOVED: now `AGENTS/LABOR/docket/graded/`); same packet → `AGENTS/REGINALD/inbox/2026-10-14_from-LABOR_jolts-openings-band-decision.md` (**never committed**: `git log --all` returns nothing for the inbox or processed path; no file of that name anywhere) | The move is benign (processed packet = history). The missing packet is a **lost LABOR → REGINALD packet** from the 10/14–15 crash window. Packet sent to LABOR (owner), 2026-10-21. |

## C. Unreadable — 2 flags

`778ef6a38:PROME/inbox/2026-10-12_from-MIDAS_news-sweep.md` and `55ee66731:AGENTS/MIDAS/analysis/2026-10-12_MIDAS-news-sweep.md` are `commit:path` git object references. Both resolve (`git cat-file -e` rc 0). The checker reads them as filesystem paths, so this is a checker false positive.

## Outcome

Of 47 flags, 1 needs owner action (the lost LABOR → REGINALD packet). 12 are low-consequence unqualified cross-desk citations. The rest are checker false positives in three classes (fraction/period-label dates, prose/template pointers, `commit:path` references), recorded for the check's owner. No date was wrong.

## Evening boot addendum — 2026-10-21 20:2x ET (session prome-56 / a77d2266)

One NEW flag against the morning baseline: `PROME/ROSTER.md` DEAD POINTER `WILL/private`. Disposition: **done — benign by design on this box.** ROSTER line 168 names VIRGIL's home `WILL/private/fellowship/` and line 174 states it is DESKTOP-ONLY and gitignored (`.gitignore` line 76 `WILL/private/`); this boot ran on the laptop (`hostname` = `WilliePOwen`, `PROME/MACHINE_LOCAL.md` laptop column), where the directory does not exist and is not expected to. Not a lost directory: re-verify on the desktop at the next switch (`ls WILL/private`); if absent THERE, that is a real loss and a Will item. Same class as the three ROSTER cross-desk dead pointers in § B. Baseline accepted with this record as pointer.

## Evening closeout addendum — 2026-10-21 21:3x ET (prome-56)

Two NEW flags at the closeout run (`scripts/firetime_check.py --window 7`), three baseline rows no longer reported (pruned):
- `PROME/WILL_QUEUE.md` DEAD POINTER `tools/phone_scan.py` — **done:** the WQ-204 DONE row quoted WALTER's desk-relative path; qualified to `AGENTS/WALTER/tools/phone_scan.py` (the file exists there; WALTER retires its boot step under WQ-204 DECLINE).
- `AGENTS/HENRY/domain/ECON_CALENDAR.md` DATE DRIFT ("Dec 23", 2026-12-23) — **routed to HENRY** by message 21:3x ET (henry-2b, live): HENRY rebuilt the calendar tonight (2e59e4d8a) from the agency schedules; the owner verifies whether 12/23 is a real BEA/BLS date or a drift. Owner artifact, PROME never edits it. **Outcome (HENRY 21:40 ET, f4c107744): REAL — BEA GDP third estimate + November PCE, Wed 12/23 08:30, now verified at BEA; not a drift.**
