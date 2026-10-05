# Reviewer bundle 2, v2 — PROME assessment

Reviewed the supplied v2 patch and addendum against HEAD `95bdada1c`. Recommendation: one bounded revision before adoption. No fleet spawned, production implementation changed, hooks installed or policy activated. This continues the user-requested bundle review; it does not reopen acceptance of the earlier safeguards implementation.

## Resolved

- Fleet consumer findings are advisory; PROME no longer waits for another desk's repair to close out. Packet obligations remain a human responsibility, not a verified receipt in this gate.
- Candidate-only output is correctly reported as needing verification. The summary uses verdict-shaped lines and requires rc 0 for a clean verdict instead of counting glyphs in quoted hits.
- Leading-dot paths and single `:312` / `:L46` locators parse correctly.
- Bare CLI boot is described as non-advancing, explicitly acknowledging the local spawn-slate write. CLI tests confirm BOARD advancement requires the flag; this review did not independently repeat the reviewer's full filesystem-write enumeration.
- The cap number is no longer imposed by installation: the unset shared configuration leaves the mechanism dormant. Rule-class migration remains outside this patch.

## Remaining completion defect — own-directory candidates have no disposition path

The proposed blocking orange row cannot be cleared by the verification it asks for. `check_consumer_declared()` still accepts only OLD/NEW and always reruns a bare scan; it accepts neither per-metric context nor a verification receipt. More fundamentally, the underlying checker intentionally retains unrelated matches as candidates even with context.

Independent fixture: PROME/STATUS.md contains `Warehouse inventory: 320 crates.`; the metric being updated is HY OAS 320→321 bp. The real checker returns rc 0 with one orange candidate. Adding `--series 'HY OAS' --unit bp` still yields one candidate, now explicitly because the line lacks that context. Both outputs fail the proposed own-directory row. Human verification that crates are unrelated cannot alter the next gate result without an inappropriate content edit or an inaccurate declaration.

**Recommended bounded change:** preserve certified red own-surface findings as blocking; report orange as advisory needing verification until an evidence-bound disposition mechanism exists. Do not mark orange clean. A future blocking version must accept a scoped verification receipt and invalidate it when the relevant input changes. Merely adding context flags does not resolve unrelated candidates. The reviewer's one-line severity suggestion needs care: changing the whole own-directory row to advisory would also downgrade red; severity must depend on the verdict.

The earlier mirror-map integration limitation remains: the declaration interface cannot select that scope, although the advice mentions it. Applicable canon/threshold changes still require the separate canonical check.

## Smaller remaining issues

- The legacy no-space joiner still regresses: `PROME/DOCKET.tsv+PROME/GATES.tsv` becomes one filename. Restore split-on-plus compatibility and cover it with a parser regression case. This is a synthetic compatibility case, not a claim of a current production row using that form.
- A range locator such as `PROME/STATUS.md:99-146` also remains part of the filename. This is an additional synthetic limitation; the single-line docket cases cited by the reviewer are fixed.
- “Visible not-configured notice at all three sites” overstates the implementation. `forge_validate.docket_row_cap()` captures stdout and returns an empty message list on rc 0, so the dormant notice is swallowed at the save hook. Correct the claim or surface a non-error notice.
- DAEDALUS's existing `scripts/daedalus_gate.py` C2 callback checks rc 1 or a red glyph and otherwise reports no stale consumer. Source inspection confirms the orange blind spot and glyph-counting family of problem there. No DAEDALUS file edited or packet sent in this review.

## Validation

- `git apply --check` against the shared checkout: PASS; patch applied only to disposable export `/tmp/prome-review2-v2-shvus53q`.
- Cap tests: 19 PASS; declaration/boot tests: 14 PASS; locks tests: 14 PASS. All run with ResourceWarning treated as error.
- Independent actual-checker outputs, captured gate commands and parser cases: `/tmp/prome-review2-v2-shvus53q/v2-counterexamples.json`.
- Initial minimal checker fixture omitted a script dependency; the corrected fixture copied the scripts tree and produced the cited results. No product failure inferred from that setup error.
- Broader gate suites, aggregate parser coverage totals and clean-fixture write enumeration remain reviewer-reported, not independently recertified here.

Disposition: v2 materially improves the bundle. Hold application pending the bounded candidate-severity/disposition fix and parser compatibility correction. The numerical cap remains Will's separate choice; no value adopted.
