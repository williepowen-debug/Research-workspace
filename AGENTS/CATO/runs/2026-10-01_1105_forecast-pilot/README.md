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

## October 1 setup completed

Rules and baseline frozen in `3b7e3ac72` before implementing the collector. Baseline `391bc5d95fa4e1fe7259aec9bbb08173b99474f4` covers **29 registered live paths** and excludes **531 already-seen desk/IDs**, inventoried across **54 live/archive TSVs** in those desks. Archive keys prevent routine rotations/imports from being mistaken for new predictions where the old record is in the checked perimeter. Unregistered historical material can still need a retrospective-import disposition; there is no claim of exhaustive historical identity recovery.

`collect.py` is implemented; ten isolated Git-fixture author tests passed ([receipt](setup_checks.json)). [Initial capture](capture.json): **0/20**, no new numeric or nonnumeric records at that pin. [Review table](reviews.tsv) and [effort log](effort.tsv) are initialized and empty, not zero-error outcome results. Preview and write were both run successfully; same-pin replay checked. The collector never grades, silently repairs a row, or contacts another agent. Dates in source prose are not heuristically parsed into deadlines: the reviewer reads the specified publication/window.

Each later session logs all pilot collection/review minutes in effort.tsv, including unsuccessful searches; the two-hour budget includes that overhead, but excludes this one-time setup. reviews.tsv stores the original claim's commit reference rather than asking a desk to retype its forecast. The source row and any referenced registration document remain available at that immutable Git revision. Eligibility checks must cite evidence, not merely copy an owner's HIT/MISS or current confidence.

Current deliverable is installed collection and a frozen review procedure. Forecast outcomes, useful feedback and demonstrated benefit are still pending. CATO can continue only when manually opened; no scheduled or continuous monitor is running, and no PROME packet was sent. This preserves CATO's manual-only roster restriction and the user's prior concern about hidden coordination. No further approval is needed for this bounded assignment's ordinary collection/review; any larger rollout remains separate.

Closeout: same-pin capture replay and frozen-config byte comparison passed; weekday check passed on the three PROME queue/registry surfaces, CATO STATUS and this report; whitespace check passed. Generic CATO read-cap check is CANNOT-EVALUATE (it assumes CLAUDE.md); direct checks of all six actual startup surfaces passed, largest 24,236 bytes, CATO CONTINUITY 13,994. No STATUS, memory or published numerical-series changes, so conditional ledger/memory/consumer checks do not apply. The initial clean-tree sync attempt met a concurrent WALTER write and aborted without pulling; no retry across foreign dirt. Orphan advisory now shows other owners' FLG/TERRY/VULCAN work; none authored here or included. Git delivery is exact-path CATO-only; receipt and any other already-committed work carried by the shared push are reported in-session.

## October 1 session closeout — Will requested stop

Setup was delivered in `5f9b9d314c6952c96c21a0e96813fbcd608dd9ab`, following the rule freeze `3b7e3ac72`. Safe-push confirmed that implementation on origin/master by fresh fetch. That shared push also carried already-committed PROME, WALTER and TERRY work; CATO did not author those changes.

Will requested that CATO's files reflect the session and close out. The bounded pilot approval survives; collection and adjudication resume at the next manually opened CATO session under the existing limits. No collection or grading was performed for this closeout. Last saved capture remains 0/20 through `a1de3280343ed33e2955614ce1cc3fb837b8d042`; it does not establish the current number of new forecasts. No outcomes, forecast skill or useful feedback have yet been demonstrated. Historical reconstruction remains deferred.

Correction to the earlier check description: CATO has no STATUS.md at closeout, so the stated weekday pass must not be read as verification of a CATO STATUS surface. The closeout weekday check covers the three existing PROME surfaces and the two changed CATO documents. This documentation-only closeout does not change collector behavior or repeat its ten author tests. No memory, ledger or published forecast figure is changed.

Closeout checks: weekday check passed on all five named existing files; scoped whitespace check passed; all six startup surfaces remain below 32,550 bytes (CONTINUITY 14,280). Orphan advisory identified only other owners' pending files; preserved without edits or staging. No new CATO-authored packets or shared files were created. Final documentation commit/push receipt is delivered in-session.
