# DESK cadence reader specification — WQ-184 / L292

**DAEDALUS design deliverable, 2026-09-08. Implementation proposal for the September 12 tooling sitting; PROME adoption and reader implementation remain open, graded September 19.** Commission: `PROME/proposals/2026-09-05_spawn-driver-RULED.md` leg ⑥. The five canonical tokens already exist in STATE_VOCABULARY Class 8; this document fills in the reader contract. It does not create a second triage tool or change live spawn authority.

What: add one owner-declared `Cadence` column to PROME/ROSTER.md and consume it in the existing `PROME/tools/spawn_list.py`. Why: distinguish planned quiet from elapsed-time lapse without mistaking a commit for completed work. Effort: one column migration plus one reader adaptation and fixtures. Expected value: a cadence-aware liveness hint alongside explicit due obligations. First step: PROME reviews the edge cases and applies the column to eligible rows; DAEDALUS does not assign desk cadences by inference.

## Proposed semantics

| Token | Clock comparison proposal | Meaning and limits |
|---|---|---|
| DAILY | More than one calendar day since last qualifying owner commit | Review hint, not evidence that a particular daily release was missed |
| WEEKLY | More than seven calendar days | Exact seven-day boundary is within cadence |
| MONTHLY | Later than the corresponding day of the next calendar month; clamp to that month's last day | Calendar month, not an arbitrary 30-day constant |
| EVENT-DRIVEN | No elapsed-time classification | Registered event/due-row governs; absent a dated event, cannot infer overdue work |
| ON-DEMAND | No elapsed-time classification | Operator/registered work governs; never overdue by age alone |

Thresholds above are proposed implementation choices, not previously ruled constants. Use America/New_York calendar dates from commit timestamps for comparison, with the supplied `--as-of` date printed. The file-level cadence declarations and their data/attention clocks remain independent.

## Reader integration and authority

1. `spawn_list.py` joins each desk's existing identity with ROSTER.Cadence. ROSTER remains the single source; no second hand-authored map in code.
2. Retain the existing subject-based owner-commit filter. A commit touching the owner's directory is insufficient evidence of owner activity. Print the qualifying commit and its date, plus the fact that commit activity is a proxy.
3. Calculate a separate cadence annotation. Keep registered due obligations visible even when the owner is within cadence. A recent commit or a cadence token never proves a named grade was completed.
4. Keep PROME's artifact-read step for an apparently active owner. A live session is handled under the existing live-owner preflight; this specification neither spawns nor messages anyone.
5. Missing/unknown cadence, missing commit evidence, invalid dates, duplicate roster identities or parse errors produce a named CANNOT-EVALUATE result. Do not silently classify the owner as active or suppress its due row. Preserve the reader's existing exit-code contract; enumerate any proposed change before implementation.
6. Explicit dated rows and Will/PROME ownership retain the current WQ-184 exclusions and routing. The proposed cadence annotation does not reclassify a Tier-2 request or trade/spend consequence as authorized Tier 1.

The earlier `fleet_triage.py` name in Class 8 was a planned instrument. Prefer integration into the existing spawn reader; PROME and DAEDALUS update that pointer together when adoption is verified. Until then the old planned name is not evidence of a running instrument.

## Acceptance cases for PROME's implementation

| Case | Required observation |
|---|---|
| WEEKLY owner at exactly seven / at eight days | Within cadence / review hint; due-row output survives both |
| MONTHLY January 31 into February | Month-end clamp is explicit; no invalid date or silent 30-day substitution |
| EVENT-DRIVEN and ON-DEMAND with no due row | No clock-overdue claim |
| EVENT-DRIVEN with overdue registered row | Row remains visible despite no age clock |
| Recent unrelated owner commit plus unresolved dated grade | Artifact-read obligation remains; no completion inferred |
| Peer-only commit touching owner files | Does not advance owner activity |
| Malformed / missing / duplicate cadence data | Named cannot-evaluate result; no false clean |
| Historical --as-of date | Same classification on repeated runs; no accidental comparison to today's wall clock |
| Owner live in session | Existing live-owner preflight still governs; no duplicate spawn |

The implementation review must watch the failure and clean paths and compare the full output before/after on the same frozen input. This document is not a fixture-run receipt.

## M2 offer

Do not add M2 to scorecard render 3. The ratio is optional and the proposed owner-grade date/tombstone-commit date pair needs an event identity and a rule for corrections and multi-owner rows. PROME's offered manual September 19 calculation is the current path; report missing dates separately. No scoring threshold or automated receipt-lag claim is introduced here.
