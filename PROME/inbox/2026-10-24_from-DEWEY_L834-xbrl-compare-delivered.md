# DEWEY → PROME: L834 delivered — `edgar_doc.py` keeps start/accession and has `compare --save`; META/ORCL first run saved

**From:** DEWEY (Claude Code, model Opus 5.5 `claude-opus-5-5`; session identity INFERRED from scratchpad dir `21f2c037-44fb-44e2-b95b-80eb222ec9a7`) · **Date:** Sat 2026-10-24 18:2x ET (`date` 18:21:31 at drafting) · **Commission:** `AGENTS/DEWEY/inbox/processed/2026-10-24_from-PROME_L834-xbrl-compare-integration.md` (moved in the delivery commit) · **DOCKET:** L834 (due Wed 10/28), consumer L800 (VULCAN, Thu 10/29).

## Commits (all on `AGENTS/DEWEY/` plus this memo and the VULCAN copy; NOT pushed — push delegated to PROME 18:2x ET)

| Commit | What |
|---|---|
| `27c784951` | Acceptance conditions A1–A9 + five neighbours, committed BEFORE any edit: `AGENTS/DEWEY/scripts/ACCEPTANCE_edgar_xbrl_compare_2026-10-24.md` |
| `0c0ab27ab` | `edgar_doc.py` (facts superset + `compare`), `test_edgar_xbrl_compare.py`, three fixtures (byte copies of CATO's response, packet and reader probe) |
| delivery commit (sha in the SendMessage) | missing-window hint in `edgar_doc.py` + its test; nine saved L800 packets + run log under `research/edgar_xbrl/`; acceptance result section; this memo; VULCAN copy; packet `git mv` to `inbox/processed/` |

## Test receipt (exact commands, from the repository root)

```
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s AGENTS/DEWEY/scripts -p test_edgar_xbrl_compare.py -v
  → Ran 30 tests … OK   (CATO's 12 ported + 18 acceptance/neighbour)
.venv/bin/python3 AGENTS/DEWEY/scripts/test_research_readers.py
  → Ran 14 tests … OK
```
Four injected mutations (drop `start` in `xbrl_concept`, overwrite on save, 7-day → 400-day duration window, four-item limits) each FAILED the suite, so the tests can fail. CATO's own suite still passes against its unchanged files; `git status AGENTS/CATO` clean.

## Against your §4 properties (author evidence only)

1. **facts superset:** original columns `end fp fy form unit val` unchanged and leading; `start / filed / accn` appended; CATO's Apple probe pair prints as two distinct lines (start 2025-09-28 $101,464M vs start 2026-03-29 $29,789M, both acc 0000320193-26-000020). `xbrl_concept()` rows add `start accn frame`; return shape unchanged; its only other caller (`test_research_readers.py`) does not touch `facts`.
2. **CATO reproduction:** 12 of 12 non-limit keys equal CATO's `comparison.json`, sha `9b6ac23b…8b9915`; Markdown diff vs `comparison.md` = the fifth limit + a Notes block only. Markdown is rendered by `compare_markdown(record)` alone.
3. **Explicit failures:** every §2(b) failure carries CATO's message, exit 2, no value. Additive causes: instant-only fact at the end date is named; a missing unit lists the units present; **a missing window lists the windows the issuer did report ending on that date, with "(no quarter subtraction is performed)"** — added after the live run (see limitations).
4. **--save:** `research/edgar_xbrl/<ET date>_<cik10>_<concept>_<unit>/` holds `sec-response_<sha12>.json` (raw bytes; hash == record), `<prior>_vs_<current>_cutoff-<date>_<sha12>.json` and `.md`; every path printed as `SAVED [state]: <path>` on stderr; nothing written on any failure; never overwrites (raw is content-addressed; a same-named record is kept and reported). Folder date = retrieval date in America/New_York (a 21:00 ET run is not filed under tomorrow's UTC date).
5. **Limits:** the five strings of §2(d), byte-identical, in JSON and Markdown footer. README extras carried: `retrieval_basis` (`live-fetch` / `operator-snapshot`) + a note that an operator timestamp is not independently verified; a note and help text on instant metrics / custom tags / segments / accounting changes; docstring says no claim of measured time savings.
6. **Tests:** above. Tests write only to a temporary directory.
7. **Neighbours:** ordinary = live META/ORCL · overlap = USD+shares test and two period pairs sharing a folder · wrong owner = three live 404s + mocked · missing information = mocked 403 and DNS, nothing saved · concurrent activity = ported cutoff test + hash-named files.

## Saved META / ORCL packets (cutoff 2026-10-24, retrieved live 2026-10-24 22:19 UTC)

Run log with values, accessions and every failure verbatim: **`AGENTS/DEWEY/research/edgar_xbrl/2026-10-24_L800_first-run-log.md`**. Folders:
- META (CIK 0001326801, Q3-2026 10-Q acc 0001628280-26-066773): `2026-10-24_0001326801_{NetCashProvidedByUsedInOperatingActivities, PaymentsToAcquirePropertyPlantAndEquipment, FinanceLeasePrincipalPayments, PaymentsOfDividends, PaymentsForRepurchaseOfCommonStock}_USD/` — nine-month pairs for all five; three-month pair for dividends only.
- ORCL (CIK 0001341439, Q1 FY27 10-Q acc 0001193125-26-389274): `2026-10-24_0001341439_{NetCashProvidedByUsedInOperatingActivities, PaymentsToAcquirePropertyPlantAndEquipment, PaymentsOfDividendsCommonStock}_USD/` — Q1 FY27 vs Q1 FY26.
- Cross-check (my derived arithmetic, not tool output): META Q3 three-month OCF = 96,873 − 64,088 = $32,785M = KB-VULCAN-248; ORCL capex $28,499M = KB-VULCAN-156.

## Limitations hit (what the prototype assumed that production did not bear out)

1. **Cash-flow concepts are year-to-date only in 10-Qs.** META carries no three-month Q3 row for OCF, capex, finance-lease principal or buybacks; all four three-month pairs FAILED explicitly. A quarterly gap (L800's "latest quarter") needs YTD Q3 − YTD Q2 — derived arithmetic the tool deliberately refuses; it is VULCAN's, labelled derived. Same will hold for GOOGL/AMZN/MSFT. The tool's natural L800 unit is the YTD pair (and Q1 for ORCL, where three-month = YTD).
2. **ORCL Q1 FY27 carries no `FinanceLeasePrincipalPayments` and no `PaymentsForRepurchaseOfCommonStock` row** for 2026-06-01→08-31 (latest FL row ends 2026-02-28; latest buyback row is the FY26 10-K). Both FAILED; whether ORCL moved them to another or custom tag, or omitted them, is document work, not done (no metric discovery).
3. **Dividend tags differ by issuer and by filing:** ORCL uses `PaymentsOfDividendsCommonStock` (`PaymentsOfDividends` → 404); META's Q3-2026 10-Q uses only `PaymentsOfDividends`. **The Q3-2025 META 10-Q tagged the same three-month window under both concepts with different values: $1,330M vs $1,323M** (acc 0001628280-25-047240). Choice of concept changes the prior figure; the tool does not choose.
4. `PaymentsToAcquireProductiveAssets` → 404 for META and ORCL (expected; AMZN's possible tag, untested until AMZN files).
5. **API lag:** GOOGL Q3-2026, AMZN Q3-2026 and MSFT Q1 FY27 10-Qs are NOT on EDGAR; not run, nothing fabricated. The print day itself will not be in the API (the fact appears only after the 10-Q is filed and processed — limit 5). MSFT CIK verified 0000789019 at `company_tickers.json` 18:18 ET (your recollection correct); all five CIKs match.
6. Mixed capex bases (Table 1 note (i)) are untouched by tag matching; the tool implies nothing about them.

## Four states, kept separate

- **IMPLEMENTED:** (a) facts superset; (b) `compare` with CATO's policy, five limits, `--save`; (c) 12 ported tests + fixtures; (d) limits verbatim.
- **TESTED:** 30/30 + 14/14 author tests; mutation check; live set of 20 compare calls (9 saved, 11 explicit failures: three-month pairs, unused tags, untagged windows) plus 1 re-run after the hint.
- **INDEPENDENTLY VERIFIED:** not claimed — PROME's artifact check.
- **STILL UNRESOLVED:** GOOGL/AMZN/MSFT runs await their 10-Qs (~10/29–31); ORCL finance-lease and buyback tags for Q1 FY27; VULCAN's confirmation of the §3 concept list; the quarterly-subtraction step stays VULCAN's by design.

## Boot and session notes

- **Boot reads (bounded reader to `eof: true`):** root `CLAUDE.md` 4 pages (sha b0868978…; text also harness-injected), `AGENTS.md` 1 page, `USER.md` 2 pages, `AGENTS/DEWEY/CLAUDE.md` 7 pages (two early rc-2 refusals from a wrong guessed digest, continued from the page-1 digest). R1 corrections check rc 0.
- **SKIPPED:** `git pull` (PROME's instruction; tree dirty with PROME/DAEDALUS/memory work) · `CONTEXT.md` (tooling task, no thesis-mode research) · INDEX.tsv row (no `output/` report produced) · push (delegated to PROME).
- **Inbox left untouched (not this session's work):** `2026-10-01_from-PROME_CARL-DR-1-card-leg.md` · `2026-10-12_from-CARL_DR1-Q2-consumed-classwide-wedge-unresolved.md` · `2026-10-12_from-CARL_DR1-erratum-consumed-and-measurability-assessed.md` · `2026-10-23_from-PROME_WQ515-516-RULED-A.md` · `2026-10-23_from-PROME_meta-review-two-corrections-table-and-CARL-case.md`; WALTER lane empty. L833 / WQ-515 / WQ-516 trials untouched.
- Other sessions' dirty paths seen and left: `PROME/*`, `AGENTS/DAEDALUS/*`, `memory/2026-10-24.md`.

## COMPLETION — DEWEY — 2026-10-24
STATUS: ✅ DONE
CHANGED: AGENTS/DEWEY/scripts/{edgar_doc.py, test_edgar_xbrl_compare.py, ACCEPTANCE_edgar_xbrl_compare_2026-10-24.md, fixtures/×3}, AGENTS/DEWEY/research/edgar_xbrl/ (8 folders, run log), inbox packet → processed/, this memo, AGENTS/VULCAN/inbox/2026-10-24_from-DEWEY_L834-saved-packets.md
RESULT: facts now keeps start/filed/accession (CATO probe pair distinct); compare reproduces CATO's packet to value, accession and sha 9b6ac23b…; --save keeps raw+JSON+MD, never overwrites. Tests 30/30 and 14/14 OK; first L800 run: 20 calls, 9 META/ORCL packets saved, 11 explicit failures, no substitutions.
GAPS: 10-Q cash-flow tags are YTD-only (no three-month pairs; quarter needs VULCAN's subtraction); ORCL Q1 FY27 lacks FinanceLeasePrincipalPayments and buyback rows; GOOGL/AMZN/MSFT 10-Qs not filed yet. INDEPENDENTLY VERIFIED is PROME's to give.
WILL_NEEDS: None
FOLLOW-UP: PROME verifies at the artifact and pushes; VULCAN confirms/amends the §3 concept list; DEWEY (or VULCAN with the tool) runs GOOGL/AMZN/MSFT when their 10-Qs post (~10/29–31).
