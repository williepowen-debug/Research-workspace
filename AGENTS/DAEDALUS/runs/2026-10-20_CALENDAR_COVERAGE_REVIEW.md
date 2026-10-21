# Calendar coverage independent review — 2026-10-20

Reviewer: Codex subagent `/root/calendar_review`, outside reader under UPGRADE_PROTOCOL review method 4/4a/4b. Read-only implementation review; only this report written. Root explicitly resolved `/home/willi/Research-workspace`; root CLAUDE.md read. Task is bounded review, no full desk boot or Git operations. Canonical commission, acceptance, CHECK_STANDARD §§2,3,9,12,14 and actual docket parser/owner contracts read.

REVIEW: required — new checker scope/evidence interpretation; scope `scripts/calendar_docket_coverage.py` full, `scripts/test_calendar_docket_coverage.py` full, acceptance full, canonical `scripts/docket_view.py` parser/owner functions; reader DAEDALUS independent Codex subagent calendar_review; disposition FIRST-PASS RESIDUE 3, production acceptance pending. Any subsequent author edits are POST-REVIEW until explicitly reread below.

## First-pass blockers and corrections

1. **P1: dated Markdown headings disappear, allowing false rc0.** Lines112–120 continue before checking dates. Own executed counterexample: matched table `|Date|Event|` / `|---|---|` / `|2026-10-20|META|`, followed by `## 2026-10-21 AMD earnings`; docket contains only October20 META for DAEDALUS. Actual rc0, MATCHED1, UNASSESSED0; AMD heading absent from records. Expected rc2 with heading location UNASSESSED and existing match retained. Check live headings for date-like material before continue; preserve explicitly scoped history exclusions. This directly violates acceptance dated-prose coverage.

2. **P1: weekday words certify unrelated events.** Own executed counterexample: DAEDALUS ledger `2026-10-21 META earnings (Wed)` and docket same-date/desk `MSFT earnings (Wed)`. Actual rc0 MATCHED, shared terms exactly `wed`. Expected rc1 UNMATCHED. Add weekday names/abbreviations to generic-calendar stop terms, including variants Tue/Tues/Thu/Thur/Thurs; test alongside non-generic subject control. This violates acceptance generic-calendar exclusion/A4. Production matches contain weekday terms, so reachable on real inputs.

3. **P2: relative prose silently omitted.** Same matched META control followed by `- Tomorrow AMD earnings` gives rc0 and only one record. DATEISH recognizes numeric/month dates only. Acceptance says relative dates UNASSESSED without restricting that promise to table cells. Detect clearly relative scheduling prose and emit UNASSESSED, or explicitly narrow the output/acceptance claim; conservative detection is preferable to silently removing the promised scope. Test relative prose alongside matched control. Do not infer a date.

Remedy consumer verification (4a): searched PROME and DAEDALUS Python/Markdown/JSON for `calendar_docket_coverage|CALENDAR.COVERAGE`; only executable consumer found was the new test suite; no existing wiring. Recommendations preserve states, rc contract, four discovery patterns and API. No consumer mutation needed. Any future PROME wiring requires its own receipt.

## Executed evidence and limits

- `python3 scripts/test_calendar_docket_coverage.py`: 22 tests pass; watched capable UNMATCHED line printed, rc0 test runner. Tests do not cover the three counterexamples above.
- Own malformed TSV trial: matched META followed by unterminated quoted AMD row => rc2, MATCHED1 + UNASSESSED1 at line3 (CSV parse error). Fail-closed behavior works and retains existing results.
- Own history ambiguity trial `## History of AMD earnings — next 2026-10-21` followed by future AMD table: row excluded, overall rc0 with matched control. Lower-priority scope limit: prefix-based historical headings can hide live content in a mixed-purpose section. Explicit historical sections are allowed exclusions; do not claim semantic completeness of such sections.
- Real population, as-of2026-10-20 +14 inclusive: 27 files, rc2, MATCHED6 / UNMATCHED81 / UNASSESSED319 / EXCLUDED33 / OUTSIDE-WINDOW320. This is not ready for a quiet boot verdict; retain actionable locations and establish owner triage before wiring.
- Real positive candidate inspected: AEOLUS/CALENDAR.md:89 C5 long-series base-rate dated October31 matches DOCKET:426 on base-rate/c5/long-series. Real unmatched example: BOND/docket/CATALYSTS.tsv:3 October21 US20Y reopening. The latter is a lexical absence finding, not proof of missing semantic registration.
- Important known candidate limitation: BOND/docket/CATALYSTS.tsv:4 October22 US5Y TIPS matches DOCKET:406 through `tips`, but docket is a nominal-buyback range and its event text says TIPS OUT of scope. The disclosed candidate-only contract technically permits this, yet this is a real false semantic correspondence; preserve it as an adverse fixture and do not present MATCHED as confirmed event coverage. Event-column-only reading does not eliminate historical/negative mentions within the event itself.
- Production acceptance fixture directory was absent at first pass; cannot discharge CHECK_STANDARD §3(e) until supplied. Default rc2 baseline remains visible, not clean.

## Inspected SHA-256 (first pass)

| File | SHA-256 |
|---|---|
| scripts/calendar_docket_coverage.py | b4f06253e645ab13c27c6bc50557326da2137d09c7691805fbc9a2f537e07d47 |
| scripts/test_calendar_docket_coverage.py | 787e7380ff16a13fab42c5c6b2e076d109c2381b7ba445f9a0b61ef4e4584ac2 |
| design/2026-10-20_CALENDAR_COVERAGE_ACCEPTANCE.md | a184c672043221b1c401d382675c8774f7591b6e7ad3af8e97bbb16ae02a5de5 |
| BLUEPRINTS/CHECK_STANDARD.md | ee105c7fd21eaf2c4f278060a73cb9c1078ce87ed6b27b3fa07f37caf5a5d06f |
| /home/willi/Research-workspace/scripts/docket_view.py | 8c725f252bcab2318897fbe9282a96f15ed91a7c6c8bd9b4d85c3d8f1e45492a |

Counterexample to this first-pass verdict: if the exact heading/weekday fixtures produce rc2/rc1 respectively with their locations retained, the first two findings no longer apply to those reviewed bytes. Future fixes must be identified by new hashes and rerun rather than retroactively treated as reviewed.

## POST-REVIEW delta read — final supplied bytes

Author supplied bounded fixes and production artifacts; independently reread changed parsing/matching code, tests, amended acceptance, production.json and full production_check.py. Re-executed my original independent heading, relative-prose and weekday counterexamples against these bytes: heading rc2 with MATCHED1/UNASSESSED1; relative prose rc2 with MATCHED1/UNASSESSED1; weekday false friend rc1 with UNMATCHED1. All three first-pass findings resolved.

`python3 scripts/test_calendar_docket_coverage.py`: 24/24 PASS. `python3 builds/calendar_coverage_2026-10-20/production_check.py`: 3/3 PASS, runner rc0. Runner verifies byte-identical header/row extracts against Git revision f36cd5d0bcb35f6ca42a6d1abe13d2a6465a1d9d and uses the complete docket at that pin. Observed real LABOR clean candidate rc0, BOND20Y lexical absence rc1, BOND TIPS range false friend rc2. Missing pinned objects are explicitly rc2. Source-pin reads are read-only. The original acceptance range rule is explicitly amended; multi-day ranges now remain UNASSESSED. This removes the observed BOND false correspondence while keeping the candidate visible; it does not prove same-day semantic identity.

Independent repeated full population: 27 files, rc2; MATCHED5 / UNMATCHED81 / UNASSESSED331 / EXCLUDED34 / OUTSIDE-WINDOW320. Compared with first pass: matched -1, unassessed +12, excluded +1; unmatched unchanged. Existing unsupported rows plus newly visible prose/headings explain a permanent-red baseline. Advisory delivery is supportable; automatic wiring/quiet verdict is not cleared by this review. PROME owns integration and owner triage.

Remaining limits are expressly disclosed in amended acceptance: unrecognized natural-language dates, mixed-purpose history headings and same-day event-column negation/history can evade semantic classification. Also per-file hashes are not an atomic snapshot. These are limits, not new implementation blockers under the bounded candidate contract. Production runner currently checks expected row states rather than asserting expected rc separately; observed rc values agree, and the unit tests cover rc behavior. Strengthening that runner assertion is optional.

REVIEW: required — new checker scope/evidence interpretation; scope final hashes below, actual docket parser/owner contracts, three original counterexamples and pinned production fixtures; reader DAEDALUS independent Codex subagent calendar_review; disposition APPLIED 3 · RESIDUE 0 blocking findings; disclosed semantic/snapshot/noise limits remain. This disposition covers standalone advisory behavior, not PROME boot integration. No state tokens, file patterns or consumer API changed; existing code consumer remains test suite.

| Final delta file | SHA-256 |
|---|---|
| scripts/calendar_docket_coverage.py | 5458588a6facb9f5013c7d6dce01aed5198f0a05682d44e93d7111ecdbfeb223 |
| scripts/test_calendar_docket_coverage.py | ba59eae0ad36b17c5b169f4c9df55f3cc412720f7e3d61d77aa623b4906a5ee5 |
| design/2026-10-20_CALENDAR_COVERAGE_ACCEPTANCE.md | a6ec31b30b8085564ec7ad3fd94ddfe1e6984d4f584977254c19a99abb744b50 |
| builds/calendar_coverage_2026-10-20/production.json | 96616d2048cc5876a1ff0bef0dff09eaa1250a637416ecf15e6001fea7733a54 |
| builds/calendar_coverage_2026-10-20/production_check.py | 3d80db6fc975fe05b8255f0e770ed0ea8fcc6ef11fa5b3e33c29f91828f8738c |
