# Calendar → DOCKET coverage check — acceptance before code

Authority: PROME inbox `2026-10-20_from-PROME_desk-calendar-to-docket-coverage-check.md`, relaying Will October20 13:45 “Yes I want all of these fixed”; Will in this session “okay please beghin”. DAEDALUS builds in its own tree. PROME owns integration; no live docket writes.

Prior art: searched calendar/transport/unregistered in `memory/auto/MEMORY.md`, `memory/auto/INDEX_COLD.md`, PATTERNS_HOT and memory bodies. Root MEMORY.md is absent; actual index is memory/auto/MEMORY.md. Relevant: `finding_scan_keyed_on_naming_reads_local_form_as_absence`, `finding_parse_failure_folded_into_a_benign_bucket`, PAT-155/158/173. Body reads scoped to mechanism paragraphs, not whole historical accumulations. Existing `scripts/docket_view.py` owns docket parsing; reuse it. VULCAN's October20 transport census proves date correspondence only; no event-identity or delivery inference.

## Contract

Read-only advisory. Default window today through today+14 calendar days inclusive, Eastern date; `--as-of` and `--days` injectable. Discover exactly `AGENTS/*/CALENDAR.md`, `AGENTS/*/docket/CATALYSTS.tsv`, `AGENTS/*/data/CATALYSTS.tsv`, `AGENTS/*/workbook/CATALYSTS.tsv`. Own desk IN if matching files exist. Print enumerated paths, row locations, counts and unsupported cases. No files matching is UNKNOWN, never clean. No archive recursion or market-source fetch.

Support TSV headers Date/Event (case-insensitive) with exact field widths and quoted cells; Markdown tables with Date/When and Event/What/Catalyst headers. Extract only an exact ISO point date, with Markdown emphasis and optional weekday/time suffix. No year inferred from today. Nonpoint/relative/approximate/invalid dates UNASSESSED even if a human could interpret them. Unknown headers, malformed rows and dated prose outside supported tables UNASSESSED. Explicit FROZEN first-line banners excluded with reason; resolved/history sections and explicit terminal Status cells excluded with counts. A mention of “resolved” elsewhere in prose does not exclude a row.

Compare date + exact desk identity in docket owners (parenthetical prose excluded) + shared event key term. Key terms exclude generic calendar/process words, standalone numbers, years and desk name. Read the docket's event column only for terms, never state/history/notes. A multi-day docket range is an UNASSESSED candidate: date containment cannot locate the event within a long carrier. Exact same-day topic match is a candidate record, not semantic proof. Multiple matches UNASSESSED; conflicting quarter qualifiers UNASSESSED. A corresponding symbolic/approximate docket row is UNASSESSED, not declared absent. All docket states count as record presence; pending execution is not measured.

rc0: nonempty assessed population, every in-window row has exactly one candidate match, no UNASSESSED. rc1: supported in-window row has no candidate docket match; owner reviews for registration or alternate wording. rc2: any UNASSESSED, unreadable/ragged input, zero files, zero assessed in-window rows. rc2 dominates rc1 but retains findings. No auto-registration or threshold actions.

## Acceptance cases

| ID | Case | Expected |
|---|---|---|
| A1 | Same date, desk, discriminating term | MATCHED with docket line + terms; rc0 for complete fixture |
| A2 | Supported event absent; today and +14 included, +15 excluded | UNMATCHED, rc1; all window counters shown |
| A3 | Wrong desk; desk appears only in notes or owner's explanatory parentheses | No coverage match |
| A4 | Same desk/date, unrelated event sharing only earnings/review/2026 | No match |
| A5 | Key term present only in docket state/history | No match |
| A6 | Two possible docket rows; conflicting Q2/Q3 qualifiers | UNASSESSED, rc2 |
| A7 | Invalid date, relative date, unknown shape, ragged or unreadable input | UNASSESSED, rc2; retain other findings |
| A8 | Empty glob; empty file; zero eligible rows; zero docket data | rc2, no clean assertion |
| A9 | Quoted TSV with embedded tab; escaped Markdown pipe; repeated tables | Correct cells/locations or explicit UNASSESSED; no silent swallow |
| A10 | FROZEN banner, terminal Status, resolved section versus live prose mentioning history | Only explicit scopes excluded, reasons/counters retained |
| A11 | Canonical date range; approximate date; symbolic schedule | All nonpoint/symbolic forms remain UNASSESSED candidates |
| A12 | Cwd elsewhere; all four patterns; DAEDALUS file included | Same result and declared perimeter |
| A13 | JSON output and human output | Same rc/counts; full rows retained without display truncation |
| A14 | Concurrent input change during read | Inputs hashed; detected change produces rc2; snapshot limit disclosed |

Author counterexample: two same-day earnings events for one desk share “Q3 earnings”, but one is META and one is MSFT. Generic words and Q3 cannot certify identity. Another counterexample: a docket notes cell mentions META as old history while the event is MSFT; notes must not be a key-term source.

Production acceptance: freeze real positive/negative rows and docket bytes at the build revision under `builds/calendar_coverage_2026-10-20/`; document hand-checked matches and misses with source paths/lines. Run full discovered population before proposing wiring; record unassessed and unmatched counts. Wiring stays PROME's, with baseline and noise limits visible.

REVIEW: required — new checker scope and evidence interpretation. Independent reader must inspect this contract, tool, tests and production fixtures and devise its own counterexample. Implementation and review receipts will be in the build record; no review claimed by this acceptance file.

## Amendment after first independent review — October20

POST-REVIEW author fixes, sent for delta review: dated Markdown headings and explicit relative scheduling prose now emit UNASSESSED; weekday names/abbreviations cannot be event keys. Header aliases Date / Window and Existing event are supported. The original A11 range-match rule is tightened to UNASSESSED after BOND TIPS matched a broad nominal-buyback carrier whose body excluded TIPS. Same-day candidate matches still do not establish semantics. Unknown natural-language forms beyond explicit date/relative patterns, mixed-purpose history headings, and negated/historical mentions inside same-day event text remain limits. Full baseline is rc2, not wiring clearance.

Production fixtures preserve source excerpts with a pinned Git revision; production_check.py retrieves and validates the complete docket from that revision. Missing Git objects return rc2. No second canonical docket copy is created.
