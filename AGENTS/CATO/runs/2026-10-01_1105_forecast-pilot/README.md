# Prospective forecast measurement pilot — approved October 1

Will approved the small prospective pilot after the twelve-case feasibility review. **Owner: CATO**, within manually opened sessions. Purpose: establish whether useful forecast feedback can be produced cheaply from existing research. This is a bounded first-call measurement view, not a replacement for desk grades, a fleet skill ranking, or a trading test.

## Scope and stop

Observe the existing live ledgers in DAEDALUS's prediction-ledger registry, frozen in config.json. Desks continue their ordinary work; no launches, new research quotas, cross-owner edits, messages, Kernel activation, or scheduled background process. CATO runs the collector once per manually opened session while this assignment remains active, then reviews only new candidates or due cases. Commit evidence after each substantive update. A gap between CATO sessions delays review; Git retains intervening committed versions. Uncommitted work is invisible.

Take the **first 20 new IDs carrying numeric probabilities at their first committed appearance** after the baseline commit. Order by forward Git ancestry, with desk/ID lexical order for same-commit ties. All selected slots remain in the denominator even if subsequently found ambiguous, retrospective, withdrawn or ineligible; no replacements. New nonnumeric rows and parser/coverage problems remain visible separately. This is the registry's observation perimeter, not a census of everything the fleet says.

Enrollment ends when 20 slots are filled or **October 31, 2026, 23:59:59 America/New_York**, whichever comes first. Finish the process assessment by **December 31, 2026**, retaining later deadlines and unavailable evidence as unresolved. No silent extension. Maximum additional CATO collection/adjudication effort after setup: **two hours**; stop sooner if that is consumed and report the bottleneck. These are pilot operating bounds, not changes to any forecast deadline.

## What is preserved and what can be scored

Preserve the complete first row (claim, probability, deadline, resolver, conditions and notes) with commit/path/blob, plus each later changed row separately. Git capture is not proof of prospective registration or eligibility: CATO checks that the original question and probability preceded relevant public information, and that any referenced registration document was also committed before the outcome.

For a scoreable **binary** original forecast, record in reviews.tsv: exact original claim and odds; registration time and evidence; event/publication deadline; named resolution instrument and vintage; conditional trigger and eligibility evidence; event cluster; outcome and primary evidence; review effort. Read linked source documents at the registration commit. Missing terms stay unknown. A categorical distribution is not silently reduced to its modal branch. No numeric probability is invented from an evidence tier or severity score. Conditional forecasts with unestablished triggers, unobservable outcomes or broken specifications remain unscored with reasons.

**Original probability stays attached to the original claim.** An amendment is separately preserved, not spliced onto that probability. Later confidence updates remain available as updates. WQ-112 already requires original first-call calibration separately from its latest-valid-mark desk score; this pilot implements that separate view and does not override the owner's latest-mark policy. Existing FORGE/PREDICTION_DISCIPLINE.md governs series/basis/vintage, invalidation and amendment handling. Unresolved conflicts are recorded, not silently settled in the collector.

At resolution, CATO checks the specified source and records 0/1 only when supported. Negative-existence outcomes need the existing dated search evidence within the specified window. Publish every selected slot, exclusions and open cases. Per-row Brier = (original probability − binary outcome)^2, with probability in 0–1; manual verified inputs only. Any aggregate is descriptive with its denominator and event dependence disclosed. A fixed 0.5 forecast can be a labelled reference, never a universal no-skill standard; no ex-post base rate is presented as a forecast available beforehand. No desk funding/ranking decision follows from twenty cases.

## Return and completion

Report: how many originals, specifications and outcomes were recoverable; unresolved/excluded reasons; effort; and concrete lessons for future forecasts. Success is a usable, reproducible record at modest cost, not a favorable score. Decide continue/simplify/stop once, at the boundary. Do not expand into historical backfill.

Run from the Git root:

```bash
python3 -B AGENTS/CATO/runs/2026-10-01_1105_forecast-pilot/collect.py
```

The collector writes only its own capture.json by explicit `--write`; without it, prints status and changes. It neither grades nor edits owners. Existing reviews.tsv is manual evidence and is never rewritten by the collector. On a missing/moved ledger, schema error or merge ambiguity, it stops without replacing the previous capture. Inspect the named issue before continuing; never treat a failed scan as zero new forecasts.

## Acceptance checks before first use

An old row or later re-mark must not enroll as a new forecast. A genuinely new row must retain its original claim/p even after edit, deletion or resolution between scans. Same-commit ties and the 20-slot cap must be deterministic. Missing ledgers, malformed new schemas, duplicate keys and non-linear history must fail visibly without overwriting evidence. Nonnumeric rows remain visible but never acquire invented probabilities. No owner files, shared index, network endpoints or manual review data are mutated by the collector. Replay from the same pin must reproduce the same capture. These are author tests, not independent certification.

Setup/disposition and check results are recorded below after implementation. Ownership references inspected: PROME/ROSTER.md (CATO manual SPECIAL; DAEDALUS registry/architecture), DAEDALUS scorecard.py/LEDGERS.tsv (descriptive resolved-count view), FORGE/PREDICTION_DISCIPLINE.md (PROME-owned canon), KERNEL forecast schema/README (separate gated versioned lifecycle). No duplicate lifecycle service or fleet policy rewrite is commissioned.
