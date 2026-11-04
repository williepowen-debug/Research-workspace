> Final parent disposition: ACCEPT of bounded implementation at exact hashes in `runs/2026-11-04_CATCHUP_CLAIM_REVIEW.md`. Earlier pending/HOLD text below records review sequence; remaining scope limits survive.

# Claim weekday Markdown repair — November 4, 2026

Authority: parent bounded owed repair, PR9 priority 5; existing weekday checker only. No new checker/rule, no inferred-year/date-range/glued-mode policy change. Owner source initially clean at HEAD 2e96c2f19eab5be5b3ab647ef6a84a5c3fabb418.

## Acceptance recorded before implementation

1. Wrong plain and balanced Markdown-wrapped ISO dates paired with weekdays must return one weekday flag; correct controls zero. Bold, italic and underscore emphasis may wrap the ISO date and/or adjacent weekday. Numeric/month-name forms outside ISO pairs retain behavior.
2. Keep original line offsets for fallback-year proximity. Only paired delimiter characters within an isolated ISO-date/weekday pair may become spaces; no global stripping of punctuation, no deletion or concatenation.
3. Preserve day/date ranges, English lowercase `sat` verb handling, plain-case exact messages, check-file paths/line numbers and exit 0/1/2 contract. Unknown check names continue refusal. No glued-mode or retired-duty edit.
4. Production forms: CREED CALENDAR lines 15–16 `**2026-09-29** (Tue)` and line 20 `~~**2026-10-28** (Wed) ...~~`; BRENT processed FALCON packet `**2026-08-11** (Tuesday)`. Recorded correct specimens stay clean; change weekday only to wrong label and require a flag. These are format fixtures, not re-grading the historical events.
5. CLI capable fixture visibly prints weekday flag with rc 1; correct fixture visibly prints clean with rc 0. Existing shipped selftests pass. Original source mutant must fail the new Markdown tests, proving discrimination.
6. Parent independent review required before acceptance/publication; exact hashes and post-review boundaries retained.

Read before edit: scripts/claim_check.py whole 1–723 in three ranges; root CLAUDE.md session-end 1e; DAEDALUS gate C5 call/status mapping; relevant UPGRADE_PROTOCOL rules already read. This repair follows the existing four weekday forms, not a new date parser.

## Implementation and evidence

Implemented balanced `**`, `__`, `*`, `_` emphasis masking only inside adjacent ISO-date/weekday pairs. Masking replaces delimiter characters with spaces, preserving offsets used by fallback-year proximity. The numeric-after regex accepts the resulting parenthesis padding only for ISO nonrange dates; M/D and range branches retain their previous padding rules. All other check types receive the original text. No CHECKS edits, new standing rule, commit or push.

Validation:

- New test suite: `python3 -m unittest discover -s AGENTS/DAEDALUS/scripts -p test_claim_markdown.py -v` — 10 tests PASS. Covers plain exact output, 16 date/day wrapper forms and correct controls, three production fragments and wrong-label mutants, scope exclusions, year offsets, adjacent-date ownership, invalid dates/weekday substrings, other checks, existing weekday cases and CLI codes.
- Shipped selftest: `python3 scripts/claim_check.py --selftest` — 67/67 PASS, including weekday, glued and file-partition cases.
- Original-source mutant at `2e96c2f19eab5be5b3ab647ef6a84a5c3fabb418`: eight tests using the existing public interface (excluding two helper-specific tests) return rc 1, 22 assertion failures, zero errors. Thus failure discrimination does not depend on the helper being absent. The original source misses the wrong Markdown weekday forms.
- Production whole-file differential on `AGENTS/CREED/CALENDAR.md` and `AGENTS/BRENT/inbox/processed/2026-08-15_from-FALCON_tihamah-mass-casualty-bab-el-mandeb-8-11.md`: old/new each zero weekday flags, exact result equality. Correct production fragments remain clean; wrong-label copies flag.
- Live temporary CLI fixtures: `**2026-11-02** (Tue)` prints `[weekday]`, original file path and line 1, `Monday, not Tue`, rc 1. `**2026-11-02** (Mon)` prints `1 file(s) clean [weekday]`, rc 0. Unknown `--check glud` still refuses with rc 2.
- `git diff --check` on owned source/test: clean. Source diff inspected; only numeric-after regex, narrow normalization helper and its weekday entry call change.

Exact SHA-256 submitted for independent review:

- `scripts/claim_check.py`: `c77bbcc45ea2affcaeb4c2a709b48d0401b252bb9cd96b579edc669f5ea3ff8b`
- `AGENTS/DAEDALUS/scripts/test_claim_markdown.py`: `fe0f57ec79fc7033abd1c13f5127622191518184149eeabb17b6a9d5bee0116b`

## Limits and disposition

**Implemented and locally verified; parent independent review PENDING.** No acceptance/publication claim yet. No model/provider-specific dependency needed: Python, Git and local files sufficed. This is not a Markdown parser: nested/mismatched delimiters, links, code fences, and arbitrary formatting are not comprehensively adjudicated. Non-ISO Markdown date forms remain outside scope. Existing inferred-year heuristics and day/date-range policies remain unchanged; their pre-existing limitations are not closed. Two production files plus format fixtures are a bounded sample, not a fleet-wide content scan. On newly detected Markdown cases the quoted match contains spaces replacing emphasis; existing plain-case message is exact and output tuple/path/line/check/CLI code contracts remain intact.

Only current-task source, new regression test, and this run record were edited by this worker. The shared tree contains unrelated ongoing changes, left untouched. Next step: parent reviews these exact hashes against acceptance before accepting this owed repair.
