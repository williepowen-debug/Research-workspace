# ACCEPTANCE — `edgar_doc.py` evidence-preserving XBRL compare (DOCKET L834)

**Written:** Sat 2026-10-24 18:15 ET (`date` at write), BEFORE any edit to `edgar_doc.py` (WQ-229 discipline). **Author:** DEWEY (Claude Code, spawned by PROME prome-06). **Commission:** `inbox/2026-10-24_from-PROME_L834-xbrl-compare-integration.md` (Will 2026-10-24 18:05 ET build greenlight). **Source prototype (read-only, CATO-owned, unchanged):** `AGENTS/CATO/runs/2026-10-24_sec-comparison/` at commit 38e1c2304.

## The defect in its own terms

1. `xbrl_concept()` drops `start` and `accn` (and `frame`), so two SEC records with the same `end`, the same `fp` and the same filing — a three-month and a nine-month row of one 10-Q — print as indistinguishable lines in `facts`. A desk reading them can take a year-to-date figure for a quarter with no tell.
2. There is no tool path that turns "compare metric M for period A vs period B" into a record carrying the exact window, unit, accession, filing date, source URL and response hash, and no path that SAVES the raw response beside the derived record. A comparison assembled by hand cites an ephemeral read (charter step 8d).

## Acceptance conditions (each a property; PROME's packet §4 is the minimum)

| # | Property | How it is shown |
|---|---|---|
| A1 | `facts` output is a SUPERSET of today's: every prior column (`end fp fy form unit val`) stays, in its prior order at the start of the line; `start`, `filed`, `accn` are added after it. `xbrl_concept()` rows additionally carry `start`, `accn`, `frame`; its return shape `(entity, label, rows)` is unchanged. | Test on CATO's reader-probe pair (Apple NetIncomeLoss, 2025-09-28→2026-06-27 and 2026-03-29→2026-06-27, both `fp Q3`, both acc 0000320193-26-000020) fed through a mocked transport: the two output lines differ, each shows its own start, and both show the accession. |
| A2 | `compare` on CATO's preserved response with CATO's README arguments reproduces CATO's `comparison.json` field for field (entity, cik, concept, unit, source_url, retrieved_at, response_sha256 `9b6ac23b…8b9915`, filing_cutoff, selection, prior, current, calculation). The ONLY differences allowed: `limits` gains PROME's fifth item (A5) and the record gains additive provenance fields (`retrieval_basis`, `notes`). | Test compares against a byte copy of CATO's `comparison.json` kept as a fixture. |
| A3 | Markdown is rendered FROM the JSON record by a function that takes only the record; it is never assembled separately. | Test: changing a value in the record changes the Markdown; the Markdown carries the sha, both windows, both filing links and every limit line. |
| A4 | Each explicit failure in packet §2(b) fails with a message naming its cause and exit code 2, never a proxy value: missing period · wrong unit · mismatched durations (>7 days) · overlap/order · conflicting latest records · no filing on/before cutoff · issuer mismatch · concept mismatch · missing filing identity/form · non-finite value · retrieval timestamp without timezone · cutoff later than retrieval date · `--snapshot` without `--retrieved-at` · `--retrieved-at` without `--snapshot` · malformed CIK/concept · transport failure (403/404/DNS). No quarter subtraction, currency conversion or tag substitution anywhere in the code path. | The twelve ported CATO tests plus neighbour tests below. |
| A5 | The `limits` list is byte-identical to packet §2(d), in order: CATO's four, then *"A fact appears in the SEC API only after the XBRL filing is processed; a press-release number is not in it."* It appears in the JSON and as the Markdown footer. | Test asserts the exact five strings. |
| A6 | `--save` writes, under `AGENTS/DEWEY/research/edgar_xbrl/<YYYY-MM-DD>_<cik10>_<concept>_<unit>/` (date = retrieval date in America/New_York): the raw response bytes (sha256 equals the record's `response_sha256`), the JSON record and the Markdown, and prints each path. Nothing is written when the comparison fails (no partial packet). An existing file is never overwritten: the raw response is content-addressed by its hash; a comparison file of the same name is kept and reported, not replaced. | Tests with a temporary save root: sha of saved raw == record sha; failure path leaves no directory; re-run keeps the first file. |
| A7 | The README limits not in the five-item list are carried: an operator-supplied retrieval timestamp is not independently verified (recorded per run as `retrieval_basis`, in a note); instant (balance-sheet) metrics, custom tags, segments and accounting changes need further source work (help text + note; an instant fact at the requested end fails with that cause named); no claim of measured time savings (help text). | Test on `retrieval_basis` for snapshot vs live; test that an instant-only record fails naming "instant". |
| A8 | Transport and contact unchanged: live retrieval goes through the existing `_get()` with the existing `HJSON` headers (declared-contact User-Agent) and the existing `CONCEPT` URL. | Test: mocked `_get` receives `CONCEPT` URL and `HJSON`. |
| A9 | Regressions: `test_research_readers.py` stays green; the new test file (12 ported + neighbours) is green; nothing the tests run writes outside a temporary directory; no file outside `AGENTS/DEWEY/` changes. | Receipt lines from both test runs; `git status` scoped check. |

## Neighbours (packet §4.7 — considered, with the test or a justified N/A)

| Category | Case | Coverage |
|---|---|---|
| Ordinary | META Q3-2026 vs Q3-2025 three-month and nine-month pairs, live, `--save` | First real run; OCF Q3 cross-checks against the 10/22 report's $32,785M (KB-VULCAN-248). |
| Overlap | A concept reported in two units (USD and shares) for the same window | Synthetic test: selection reads only the requested unit; the other unit's value never leaks. Also a path collision: two period pairs of one concept on one day share a directory, distinct file names. |
| Wrong owner | A concept the issuer does not report (custom tag / unused tag) | SEC returns 404 → explicit "Comparison unavailable: HTTP 404 … not found", exit 2, nothing saved; tested with a mocked transport, and hit live wherever the L800 list names a tag the issuer does not use. |
| Missing information | SEC 403 / DNS failure | Mocked `EdgarError` (403 and transport) → explicit unavailable, exit 2, no directory created. |
| Concurrent activity | A filing processed between two runs with different cutoffs | CATO's cutoff test (earlier cutoff excludes the later revision) ported; saved packets of two different responses never collide because the raw file and the comparison file names carry the response hash. |

## Out of scope (packet §2(e))
Metric discovery · interpretation · TTM/annualising arithmetic · scheduled collection · CATO's files · L833 Experiment A, WQ-515, WQ-516.

## Result (appended after the edit, Sat 2026-10-24 18:21 ET; author's own evidence — IMPLEMENTED + TESTED, not INDEPENDENTLY VERIFIED)

| # | State | Evidence |
|---|---|---|
| A1 | IMPLEMENTED · TESTED | `test_facts_superset_distinguishes_quarter_from_nine_months`, `test_xbrl_concept_rows_keep_start_accn_frame`, `test_facts_instant_row_marked` |
| A2 | IMPLEMENTED · TESTED | `test_reproduces_cato_packet_and_limits_verbatim` (12 of 12 CATO keys equal except `limits`; sha 9b6ac23b…8b9915); CLI Markdown diff vs CATO's `comparison.md` = only the fifth limit + Notes |
| A3 | IMPLEMENTED · TESTED | `test_markdown_rendered_from_record` |
| A4 | IMPLEMENTED · TESTED | CATO's 12 + `test_cli_failures_name_cause`, `test_instant_fact_named_as_cause`, `test_missing_window_lists_same_end_windows`; live: 9 explicit failures in the L800 run, none produced a value |
| A5 | IMPLEMENTED · TESTED | literal five-string assertion |
| A6 | IMPLEMENTED · TESTED | `test_save_*` (4); live: 9 saved records, each raw file hashes to its record |
| A7 | IMPLEMENTED · TESTED | `test_retrieval_basis_snapshot_vs_live`; help text/docstring carry the README limits |
| A8 | IMPLEMENTED · TESTED | `test_live_fetch_uses_existing_transport` |
| A9 | TESTED | `test_edgar_xbrl_compare.py` 30/30 OK; `test_research_readers.py` 14/14 OK; four injected mutations each failed the suite; CATO's own suite still OK against its unchanged files |

Neighbours: ordinary = META/ORCL live run (`research/edgar_xbrl/2026-10-24_L800_first-run-log.md`); overlap = two-unit + shared-folder tests; wrong owner = live 404s (`PaymentsToAcquireProductiveAssets` ×2, ORCL `PaymentsOfDividends`) + mocked 404; missing information = mocked 403/DNS, nothing saved; concurrent activity = ported cutoff test + hash-named files. **Addition beyond the plan (disclosed):** a missing-window failure now lists the windows the issuer DID report ending on that date — added after the live run showed META's 10-Q cash-flow tags are year-to-date only.
