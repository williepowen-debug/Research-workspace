# ACCEPTANCE — L688 broker as-of: UNKNOWN renders UNKNOWN, never the receipt date — 2026-10-15

**Written BEFORE the edit** (PROME prome-06, post-close sitting; `date` at write time in the commit body). Step 2 of
`PROME/plans/2026-10-15_last-mile-wiring-PLAN.md`; DOCKET L688. This sitting's ONE process change (WQ-299 R1; WQ-445
unruled at write time).

## Defect, in its own terms
`will_brief.parse_money` reads the FORGE mirror header's `**Updated:**` date (the RECEIPT date) as `vintage`, and when the
header states no `marks = YYYY-MM-DD` it FALLS BACK to that same receipt date for `marks` — so the Helm's book line reads
"Broker export 2026-10-15 · marks 2026-10-15" on a day the mirror itself says "marks = UNKNOWN clock, 10/15 intraday".
`desk_attention.holdings` labels every holding "<receipt date> broker positions", the same substitution in words. A receipt
date presented as a broker observation is the class `finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly`:
the number is right by coincidence on same-day captures and wrong without a tell on any other day.

## Acceptance conditions (properties, not the symptom)
| # | Category | Condition |
|---|---|---|
| A1 | **Missing information** | A header whose marks clause reads `marks = UNKNOWN…`, or has no marks clause at all, renders marks as-of **UNKNOWN** — quoting the header's own words when it has them — never the receipt date and never today's date, in will_brief's HTML book line, in the `--book-line` text, and in desk_attention's observation label. |
| A2 | **Ordinary** | A header stating `marks = [Weekday ]YYYY-MM-DD[ CLOSE\|intraday…]` renders that date with its qualifier as the marks as-of; the receipt date renders separately, labelled "received". |
| A3 | 🔴 **Overlap** | Receipt date and marks date both present and DIFFERENT (e.g. received 2026-09-27, marks Fri 2026-09-25 CLOSE): both render, each under its own label; neither replaces the other. The stale class keys on receipt age OR an unknown marks clock — unknown ⇒ stale (fails toward caution, never toward fresh). |
| A4 | **Wrong owner** | A date anywhere else in the header (a "Vs the 10/14 mirror" phrase, a cell tag like `[10/15 rcv]`, a receipt clock "10:10 ET") is never captured as the marks date; only the `marks = ` clause is read for it. |
| A5 | **Concurrent activity** | N/A — one reader of one file per build; the helper writes nothing. |
| A6 | **Shape** | A header without `**Updated:**` still fails LOUD in will_brief (existing `fail`) and reads receipt `UNKNOWN` in desk_attention (existing); unchanged by this repair. |
| A7 | **Wiring (WIRED/OBSERVED)** | BOOT step 8 names `python3 PROME/tools/will_brief.py --book-line` as the book line pasted whole into Will-facing messages (WIRED). OBSERVED = a later boot report carries that line verbatim; not claimable at this sitting. |

## Shape of the change (one home for the parser)
- `desk_attention.forge_vintage(text) -> (receipt_date, marks_label, marks_known)` — the single parser of the mirror
  header's two clocks; `holdings()` uses it for the observation label.
- `will_brief.parse_money(head=None)` calls it; money carries `vintage` (receipt), `marks` (label), `marks_known`, `age`
  (days since receipt). `book_vintage_line(money)` is the one text home for the two clocks (will_brief's HTML line, the Helm's
  line and `--book-line` all render it); `book_line` prefixes it with the account and cash for `--book-line`.
- `PROME/BOOT.md` step 8: one clause naming the pasted book line.

## Tests
`PROME/tools/tests/test_broker_asof_L688.py` — inline header fixtures (today's header shape, the 10/13 `marks = UNKNOWN` shape,
the 9/27 `marks = Fri 2026-09-25 CLOSE` shape, the 9/3 no-clause shape, and a counterexample header carrying other dates).
Count measured at the result: `grep -c 'def test_' PROME/tools/tests/test_broker_asof_L688.py`.

## Read 1 (independent Opus reader, 17:02–17:05 ET; ledger scratchpad `l688_read1.md`, 22 claims, 12 reader counterexamples CX1–CX12) — HOLD, 2 ❌
- ❌1 FIXED at the source: the marks clause is now anchored to the `**Updated:**` line (a banner "marks =" above it can no longer win — the 9/30 header shape, commit 33bc8c293, and CX1 are fixtures: `test_A4_only_the_updated_lines_marks_clause_is_read_never_a_banner`).
- ❌2 FIXED at the source: the UNKNOWN test runs over the whole clause up to the next ` · ` (parenthetical and cell tag included), the label keeps the clause's own words (`… (clock UNKNOWN)`); CX2/CX11 are fixtures inside `test_A1_dated_clause_that_declares_an_unknown_clock_stays_unknown`.
- ⚠️5 FIXED (qualifier `[A-Za-z-]+`: "post-close" no longer truncates) · ⚠️6 FIXED (`--book-line` exits 1 on PARSE-FAILED; test A7 asserts it) · ⚠️7 FIXED (both boot-runner copies name the command; `diff -q` identical).
- Declared residue (not fixed): ⚠️3 two `**Updated:**` lines → first wins (never seen in 60 headers) · ⚠️4 full-weekday / date-less forms read UNKNOWN (safe direction) · ⚠️8 the Robinhood observation label is hard-coded Sept-3/Sept-9 text (pre-existing, outside this diff) → DOCKET row registered 17:23 ET · ⚠️9 with every header since 10/07 marks-unknown, the book line is permanently `stale`-styled (A3's intent; the class no longer separates 0d from 30d) · ⚠️10 no render-level assertion in the suite (the reader verified by builds) · ⚠️12 `test_desk_attention.py` writes the live `dashboard_build.json` (L737 ③; restored to HEAD after each run this sitting). Reader hygiene: it left `st_b.txt` one level above the scratchpad (removed); it observed PROME's own concurrent DOCKET/inbox edits (not a defect).
- Re-run after the fixes: L688 suite 11/11 · frozen desk_attention suite 10/10 · queue-parser selftest 26/26 · `--book-line` rc 0, one line.

## Read 2 (second independent Opus reader, 17:23–17:26 ET; ledger scratchpad `l688_read2.md`, 20 claims, 12 reader counterexamples R1–R12) — HOLD, 3 ❌
- ❌1 FIXED: will_brief kept a SECOND receipt reader (`vint`) beside `forge_vintage`, and a banner naming the token or a date on the next line made `parse_money` raise instead of `fail()` — now the ONE parser supplies the receipt and `parse_money` fails loud when it reads UNKNOWN; `forge_vintage` takes the first `**Updated:**` token FOLLOWED by a date (R1/R2 fixtures: `test_read2_one_receipt_reader_fails_loud_never_raises`).
- ❌2 FIXED: the clause scope now ends only at a ` · ` at paren/bracket depth 0 (`_top_level_scope`), so an UNKNOWN after a separator inside a parenthetical still counts (R3 fixture: `test_read2_separator_inside_parenthetical_does_not_end_the_clause`).
- ❌3 FIXED: the label cap (70 chars on the clause's words) is applied BEFORE the ` (clock UNKNOWN)` marker, so a label with marks_known False always carries UNKNOWN (R5 fixture: `test_read2_label_cap_never_strips_the_unknown_marker`).
- ⚠️4 FIXED (two marks clauses on the Updated line read UNKNOWN, never the first) · ⚠️5 FIXED (`\bmarks = `; "remarks =" is not a clause) · ⚠️7 FIXED (`book_vintage_line()` is the one text home — will_brief's HTML line, the Helm's line and `--book-line` all render it; asserted at the source) · ⚠️8 FIXED (BOOT step 8 + both runner copies: rc≠0 ⇒ the book reads UNAVAILABLE).
- Declared residue (not fixed): ⚠️6 the unknown-clock test keys on the literal word UNKNOWN (a clause saying "capture time not shown" reads known — keyword-scoped; the mirror's own convention is the word UNKNOWN) · ⚠️9 read 1's ⚠️3/4/8/9/10 stand as declared (a wrapped marks clause on the next `>` line reads UNKNOWN — safe) · ⚠️10 the frozen suite's live write of `dashboard_build.json` (L737 ③; restored to HEAD after each run).
- Re-run after the fixes: L688 suite 16/16 · frozen desk_attention suite 10/10 · queue-parser selftest 26/26 · `--book-line` rc 0 · Helm test build rc 0 with the one-home line.

## Read 3 (third and last independent Opus reader, 17:36–17:38 ET; ledger scratchpad `l688_read3.md`, 18 claims, 15 reader counterexamples Q1–Q15 + a cap sweep) — RELEASE, 0 ❌
- All five prior ❌ CLOSED at the artifact (read 1 ❌1/❌2; read 2 ❌1/❌2/❌3), each with the reader's own evidence (the 60-header sweep: 9 marks_known=True results, every date literally stated after `marks = ` on that header's Updated line; 0 raises; the cap sweep keeps UNKNOWN in every known-False label).
- Declared residue (new in read 3; each fails toward FRESH or loses words only under a header shape absent from all 60 headers): ⚠️1 an UNKNOWN in a SIBLING top-level clause (`… intraday · clock UNKNOWN`) escapes the test · ⚠️2 unbalanced brackets clamp the depth counter · ⚠️3 an invalid receipt date (2026-13-45) raises in `parse_money` as before the repair (loud; BOOT says rc≠0 ⇒ UNAVAILABLE) · ⚠️4 a marks date is not calendar-validated and a stated clock after it is dropped from the label · ⚠️5 = read-2 ⚠️6 (keyword-scoped on the word UNKNOWN) · ⚠️6 the Shape sentence above — FIXED here (one-word class) · ⚠️7 the frozen suite's live write of `dashboard_build.json` (L737 ③; restored to HEAD after the run).

## Completion states (filled at the end, never merged)
IMPLEMENTED: 2026-10-15 17:43 ET (prome-06) · TESTED: 16 tests, author's suites green (16/16 · 10/10 · 26/26) · INDEPENDENTLY VERIFIED: 2026-10-15 17:38 ET — read 3 RELEASE after read 1 HOLD (2 ❌) and read 2 HOLD (3 ❌), all five fixed at the source and confirmed CLOSED by a reader who did not fix them; the Shape one-word fix after read 3 is unreviewed · STILL UNRESOLVED (declared residue, none a property violation): read-1 ⚠️3/4/8 (DOCKET L742)/9/10 · read-2 ⚠️6/10 (L737) · read-3 ⚠️1–5/7
PRIOR LINE (superseded): IMPLEMENTED: 2026-10-15 17:35 ET (prome-06; two correction passes — the two-correction stop is TRIPPED for desk_attention.py / will_brief.py this session) · TESTED: 16 tests (`grep -c 'def test_'`), author's suites green · INDEPENDENTLY VERIFIED: PENDING read 3 — the episode's LAST read (ceiling 3; read 1 HOLD 2 ❌, read 2 HOLD 3 ❌, all five fixed; a ❌ surviving read 3 is dispositioned, never fixed-and-shipped) · STILL UNRESOLVED: read-1 ⚠️3 · ⚠️4 · ⚠️8 (DOCKET L742) · ⚠️9 · ⚠️10 and read-2 ⚠️6 · ⚠️10 (L737) as declared residue
