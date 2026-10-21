# Calendar coverage check — October20 build result

IMPLEMENTED: `AGENTS/DAEDALUS/scripts/calendar_docket_coverage.py`, owned standalone read-only advisory. Commission: today's PROME calendar coverage inbox packet; Will “okay please beghin”. Acceptance file was written before code. No PROME instrument, docket, desk calendar, roster or market source edited.

TESTED:24 unit tests, including missing/ragged inputs, empty population, dates/horizon, wrong owners, history-only key terms, ambiguity, quoted TSV, escaped pipes, resolved-section boundaries, concurrent change and CLI JSON/human agreement. Production runner3/3: actual LABOR claims candidate, BOND20Y lexical absence and the BOND TIPS false range match. `production.json` pins source rows; runner reads the COMPLETE docket at that Git revision. Missing Git objects are rc2. No synthetic input is presented as original production evidence.

INDEPENDENTLY VERIFIED: Codex `/root/calendar_review`; three findings fixed and delta-read.24 tests and3 production cases independently run. Report: `runs/2026-10-20_CALENDAR_COVERAGE_REVIEW.md` (relative to DAEDALUS). Reader explicitly closed its read-only task; report was its only authored artifact. No code changes after final reader hashes.

STILL UNRESOLVED: fleet baseline rc2,27 files,5 MATCHED,81 UNMATCHED,331 UNASSESSED,34 EXCLUDED,320 OUTSIDE-WINDOW. These are parsed record counts, not distinct events or missing registrations. All locations and input SHA256s in `baseline.json`; event text lives in source files. Initial prototype baseline and subsequent development counts are not final results.

## Operation and wiring boundary

`python3 AGENTS/DAEDALUS/scripts/calendar_docket_coverage.py --as-of 2026-10-20 --json`

Default horizon today..+14 inclusive, Eastern date. Exact four discovery patterns are named in output; DAEDALUS included if a matching file exists. Explicit `--ledger AGENTS/<DESK>/...` scopes a diagnostic. CLI writes only stdout; no auto-registration. JSON carries full original rows and hash-bound input identities. Human output enumerates all paths/results, with no silent truncation. Run production acceptance with `python3 AGENTS/DAEDALUS/builds/calendar_coverage_2026-10-20/production_check.py`.

rc0 only nonempty supported rows with one candidate each and no unassessed; rc1 unmatched supported candidates; rc2 unsupported or unreadable scope, or no assessed rows. rc2 dominates rc1 while retaining all findings. A match does not establish event identity, current schedule, pending status, delivery or consumption. An unmatched row may be registered under different wording; PROME/desk verify before acting. Broad ranges, approximate and symbolic schedules do not certify point-event coverage.

PROME owns boot integration. Independent review clears standalone advisory use, NOT boot integration. Current unknown volume would make a binary boot gate permanently noisy. Any wiring must retain rc2 and the counts/perimeter, link the full output, and avoid automatic docket insertion or implicit launch. First action is bounded owner triage of unmatched and unsupported shapes; no new fleet rewrite is authorized. No files outside the declared four patterns, opaque natural language beyond recognizers, or semantic contents of history exclusions are certified.

## Completion and maintenance

L628 re-verification is a separate unchanged-patch handoff in `builds/summons_fix_2026-10-08/REVERIFICATION_2026-10-20_CODEX.md`. RED census remains queued; VULCAN's bounded update is consumed as design input, not independently rerun. L748 October21 and L470 conditional October22 remain owed. Scorecard/PR#8/profile/staleness and document rotation clocks unchanged.

REVIEW: required — new checker scope/evidence interpretation; full tool/tests/acceptance/production fixtures; independent calendar_review; APPLIED3, remaining semantic/coverage limits disclosed. No new blueprint rule or fleet token registered. Local result codes implement the commission, not a fleet vocabulary amendment.

## Closeout evidence boundary

The candidate-v2 capture was attempted with honest known dependency limits and refused rc2: C1 orphan_check reads global Git status, which the current exact-path context schema cannot bind. C8 has the corresponding previously documented global-history limitation. No reusable candidate receipt, candidate eligibility, or candidate-review clearance is claimed. Existing full closeout checks are run separately for this single handoff; their result does not repair that limitation. Artifact persistence under root Git rules is separate from candidate assurance and owner integration.

No SURFACES/PATTERNS refresh claimed: this package changes no shared ownership, adds no root scripts and yields no novel lesson beyond existing parsing/perimeter patterns; overdue registry sweeps remain due. The STATUS write records delivery, not a ledger refresh. No blueprint standard amended.
