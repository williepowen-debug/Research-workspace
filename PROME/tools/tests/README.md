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

## The five categories — every repair, every time

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
| `test_argus_scope.py` (20) | the ARGUS git-watermark scope | 1 · 2 (committed+pending) · 3 (other desks' commits, pending work, shared-memory lineage) · 4 (untracked shared memory ⇒ UNATTRIBUTED) · 5 partial |
