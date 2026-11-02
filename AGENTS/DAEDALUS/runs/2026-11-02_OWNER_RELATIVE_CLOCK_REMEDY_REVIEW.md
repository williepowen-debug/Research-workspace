# Owner-relative profile clock — pre-implementation remedy review

**Disposition: ACCEPT (bounded plan, not a result certification).** Reader `/root/prome_spine_read`, OpenAI Codex; exact model variant unavailable. Scope: `design/2026-11-02_OWNER_RELATIVE_CLOCK_ACCEPTANCE.md` whole; `scripts/profile_clock_check.py` whole (167 lines); `scripts/tests/test_profile_clock_check.py` whole (103 lines); UPGRADE_PROTOCOL clock clarification and rules 4/4a/4b; current HENRY/OSPREY profile metadata and owner STATUS headers; `scripts/sweeps_due.py:299–321` plus DAEDALUS gate B1/C0 mappings. No code, owner files or frozen fixtures changed; only this report written. No commits.

## Why the remedy is within scope

The registered predicate is owner-STATUS date minus last whole-profile body vintage, strictly greater than the declared day count. The current tool already detects that declaration and refuses it; it does not evaluate it. Enabling the declared comparison adds a dependency read, not a new refresh policy. HENRY's metadata says STATUS as-of stamp leads body by >21d; OSPREY says STATUS stamp leads vintage >21d. Both body vintages remain August 7. Current HENRY STATUS begins `Last owner update: 2026-11-02`; OSPREY begins `Last Updated: 2026-11-02`, before their first content headings. The observed lead is 87 calendar days, so a successful repaired run must ALERT/FIRED, not OK or refreshed. These are content dates, not tool execution times.

UPGRADE_PROTOCOL says receipts/deltas cannot reset the body clock and owner-relative predicates require the named owner-stamp comparison. The proposed anchored-header parsing, chronology refusal, disposable `--owners-root`, immutable production fixture evidence and no wall-clock fallback satisfy that contract.

## Consumer/return contract

- `sweeps_due.py` runs this child `--quiet`, prints its result, maps rc2 to cannot-certify and rc1 to due. It does not parse the exact owner-detail message.
- DAEDALUS boot B1 and closeout C0 map sweeps rc0/1/2 to CLEAN/DUE/UNKNOWN. Therefore current two profiles moving from rc2 UNKNOWN to rc1 DUE is the intended correction; it must not turn them clean.
- The pipeline-rc wrappers only name the executable/return-code class; no new rc code is needed.
- Preserve aggregate behavior: an unresolved malformed/missing owner anywhere keeps overall rc2 while independently supported alerts remain printed. The header read does not certify event/content triggers or that a whole-profile refresh was actually performed.

## Reader's independent counterexamples (required result-read cases)

1. **Wall-clock false alert:** profile body August 7, owner header August 28 (21-day lead), as-of November 2 (87-day wall age). Expected relative day-clock result CLEAN, despite wall age; changing owner only to August 29 must ALERT (22-day lead). A wall-age implementation fails the first case. A hard floor October 31 in the same profile must still ALERT as-of November 2; this tests the two clocks independently.
2. **Invalid header must not disappear:** pre-section owner header `Last Updated: 2026-11-99` followed by another valid pre-section `As of: 2026-11-02`. Expected CANNOT-EVALUATE, not success from the valid line after silently ignoring the malformed declaration. The plan's absent/malformed/conflicting clause already requires this.
3. **Do not read quoted history:** valid initial `Last owner update: 2026-08-28`, then `## Historical records` and `Last Updated: 2026-11-02` in that section. Expected 21-day lead/clean; the later historical line must not override the initial owner header. Repeated identical header dates may collapse to one distinct date; two different valid header dates must refuse.
4. **Mixed relative predicates:** a future profile says `STATUS stamp leads body >21d; OR no owner update for >7d`. Current `clock_of` reduces all day counts to the minimum and sets one global relative bool. Applying that minimum to owner-minus-body would implement a third, undeclared predicate. For this bounded repair, ambiguous/multiple distinct day clauses on an owner-relative field must refuse unless implementation explicitly parses their separate referents. This is a scope boundary, not a request to build a general prose-expression parser.

## Minimal implementation clarifications

No blocking change to the actual HENRY/OSPREY remedy is needed. Keep the plan's fail-closed ambiguity requirement explicit at the implementation boundary: **one supported owner-relative day predicate; mixed/ambiguous day referents remain CANNOT-EVALUATE**. The existing generic footer currently says owner STATUS-relative clocks are never certified. When the new branch is implemented, update that footer narrowly to distinguish evaluated supported relative clocks from unsupported/ambiguous ones; retain the content/event and truth-of-refresh disclaimers. Otherwise the successful output would contradict its own new perimeter claim.

These two clarifications do not authorize new trigger forms, owner-header fallback to body/history, a profile vintage reset, wall-clock substitution or direct owner edits. They are acceptance details to check in the final code/tests counterexample read.

## Pre-repair observation

An independent disposable test passed the current checker a `TEST.md` with explicit body August 7 and `Staleness: when STATUS stamp leads body >21d`, as-of November 2. Current main returned rc2 and printed `STATUS-stamp-relative >21d trigger needs owner-stamp comparison; wall-clock age is NOT that trigger`; zero dated clocks evaluated. No live owner files were read or written by that fixture. This demonstrates the unsupported pre-repair branch; it does not test the proposed implementation.

**REVIEW:** required — existing checker gains a new dependency/read boundary for an already-declared trigger; scope and consumer rc contracts above; reader `/root/prome_spine_read`; disposition ACCEPT plan, final implementation/tests independent result review OWED. Parent author fixes after any result read must remain labelled POST-REVIEW under UPGRADE_PROTOCOL 4b.

Observed review time: 2026-11-02T10:05:43-05:00
