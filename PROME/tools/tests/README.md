# PROME tool tests — the neighbour-case contract

**Origin:** external review (CODEX), 2026-09-11, after a repair to `argus_scope.py` passed its own 12 tests and
was still incomplete. **The miss was an OVERLAP case** — a path both committed and pending — and no test in the
suite addressed that shape because the suite was written against the *reported reproduction* rather than against
the defect's *neighbourhood*.

## The rule

**A fix's test list comes from its ACCEPTANCE CONDITIONS, written before editing, not from the bug report.**
Restating the symptom produces a narrow condition ("include pending files"). Stating the property produces the
real one ("every pending change in the intended closeout is visible, INCLUDING files already committed earlier;
unrelated work is excluded; the agent's own instructions request the right comparison").

## The five categories — CONSIDER every repair; justified N/A is a passing answer

| # | Category | Ask |
|---|---|---|
| 1 | **Ordinary** | the plain case works |
| 2 | 🔴 **Overlap** | an input in TWO states at once — committed *and* pending, live *and* archived, both lanes |
| 3 | **Wrong owner** | someone else's data reaching a perimeter it should not, and yours excluded from one it should reach |
| 4 | **Missing information** | the attribute you key on is ABSENT — no lineage, no header, no date. Fail LOUD; never silently claim and never silently drop |
| 5 | **Concurrent activity** | two writers, two taps, two sessions; day- or second-precision keys colliding |

Category 2 is the one that stays untested, because the reproduction is almost never an overlap.
Category 4 is the one most often "fixed" by a silent default, which converts a detectable hole into an
undetectable one.

🔢 **Counts in this table are measured, never remembered** — `grep -c 'def test_' <file>`. Three different counts for one suite appeared across three surfaces on 2026-09-11.

⚠️ **CONSIDER is the verb, not PERFORM** (external review refinement 2, 2026-09-11). Writing five tests for a
one-line repair is the paperwork reflex this contract exists to reduce. A one-line justified **N/A** — *"no
concurrency: single-writer tool"* — discharges a category. What is NOT allowed is silence: a category neither
tested nor explicitly dismissed.

## What passing this suite does and does not establish

**Does:** IMPLEMENTED, and TESTED against the author's stated conditions.
**Does NOT:** INDEPENDENTLY VERIFIED. That requires a reader who did not write the fix and who devises at least
one counterexample of their own. `finding_adoption_is_not_validation` — consumed, confident and consistent means
nobody tested it.

## Fixture rules

- **Throwaway repos only.** No assertion may read the live tree, or the test certifies nothing past the next
  edit (`finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit`).
- **Falsify the guard itself.** A test that cannot fail is decoration: induce the defect, watch it fire, restore.
  `finding_test_the_guard_not_just_the_guarded`.
- Run under `python3 -W error::ResourceWarning`.

## Current suites

| Suite | Covers | Neighbour categories |
|---|---|---|
| `test_argus_scope.py` (26) | the ARGUS scope: recorded baseline + recorded perimeter (L336) | 1 · 2 (committed+pending) · 3 (other desks' commits, pending work, shared-memory lineage) · 4 (untracked shared memory ⇒ UNATTRIBUTED) · 5 partial |
| `test_wq_ledger_L336.py` (10) | WQ ledger B1 (full-payload comparison) + B2 (consecutive-duplicate test) | 1 · 2 (A→B→A oscillation) · 4 (generated metadata absent) · 5 N/A: single-writer tool |
| `test_spawn_list_desk_commit_attribution_L455.py` (22) | desk-commit attribution in `spawn_list.py` + `desk_activity.py` (L455): convention form by subject, loose forms corroborated by PATHS | 1 (seven subject forms) · 2 (`WAL`/`WALTER` both directions) · 3 (processed-move · root doc · other desk's home · body-line mention) · 4 (empty marker attributed by subject, documented) · 5 N/A: committed history, re-run per boot |
| `test_prome_gate_citability_L417.py` (15) | the GATE-CITABILITY RULE as a boot-gate leg (L417): tokens over LIVE rows' definition_surface files + condition cells, README never scanned, unreachable ⇒ ERROR | 1 (pass-with-hit, fail-on-lead) · 2 (two homes: condition cell + file; non-LIVE ignored) · 3 (the README's own prose, cited but excluded) · 4 (unreachable path ⇒ ERROR; NONE-prose ⇒ no error) · 5 N/A: single reader over a committed ledger |
