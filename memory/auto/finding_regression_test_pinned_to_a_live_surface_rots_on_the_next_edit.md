---
name: finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit
description: A regression test that asserts the CURRENT strings of a LIVE document (a HEARTBEAT amendment's wording, a level, a count) certifies nothing past the next routine edit — it fails on the first amendment while every rule it was written to protect still holds. Freeze the fixture the test reads; assert the invariant, not the surface.
symptoms: "tests failed right after a routine amendment" · "assertIn on a live doc string" · "12/12 yesterday, 10/12 after I added one paragraph" · a test named test_current_* · "the regression test reads HEARTBEAT.md directly" · a green suite that only proves nobody edited the file today
metadata:
  type: finding
---

**The instance (PROME, 2026-09-09).** DAEDALUS's 9/8 sweep found the FleetOps dashboard dropping HEARTBEAT amendments (O1). The 9/9 repair added `test_heartbeat_projection.py` — 12 tests, two of them *"live consumer"* regressions: `test_current_two_regressions_and_unaffected_channels` read `HEARTBEAT.md` off disk and asserted Am.#2's literal strings (`'consumer 0/4, NOT FIRED'`, `levels['10Y Yield'] == 4.78`, `'owner integration pending'`), and `test_rendered_view_…` asserted them in the rendered page. That evening PROME appended **Amendment #3** — the four L0 owner grades, exactly the kind of edit the amendment mechanism exists for. **Both tests failed.** Every amendment rule held (precedence, sha-binding, withholding on a bad projection); the tests had pinned *what the file said on 9/8*, not *what the renderer must do*. Fix: `git show HEAD:HEARTBEAT.md` + the companion into `tests/fixtures/` as a frozen 9/8 snapshot; the two tests patched to read the fixture; assertions unchanged; 12/12. The finding went back to DAEDALUS in the repair receipt.

**Why it happens.** The repair brief said *"verify both actual inversions in rendered output plus unchanged-channel controls"* — a correct verification of a MOMENT. Encoding a moment as a permanent assertion turns a verification into a tripwire on the next edit: the test's pass condition is *"nobody has amended since"*, which is the opposite of the surface's purpose. It passes on the repair day and rots by construction. It is the mirror of `[[finding_frozen_fixture_control_is_blind_to_resolution_faults]]` — there a frozen fixture cannot see a fault in the live resolution; here a live fixture cannot survive a live resolution. Both are the same mistake about WHAT a test is allowed to read.

**How to apply.**
- A regression test names an INVARIANT ("a later amendment overrides the base"; "an unchanged channel is byte-identical to the base") and proves it on a **frozen input** the repo owns. If it must read a live file, it may assert only structure (parseable · errors empty · required keys present) — never a value that a routine edit is licensed to change.
- If you need *"the live file currently says X"*, that is a **check** (boot gate, closeout gate — advisory or blocking at the moment it runs), not a **test**. Put it in the gate with a date; do not put it in the suite.
- Naming tell: `test_current_…`, `test_live_…`, `test_today_…` — read the body; if it opens a live surface and asserts a value, freeze it.
- When it bites: snapshot the pre-edit file from git (`git show HEAD~1:<path>`) into `fixtures/`, patch the reader, keep the assertions — the assertions were right about that moment, and now they stay right.

Related: `[[finding_test_the_guard_not_just_the_guarded]]` · `[[finding_guard_correctness_and_wiring_are_independent]]` · `[[finding_a_correction_pass_is_unreviewed_work]]` (the repair session wrote the tests as the last step of a long fix) · `[[finding_frozen_fixture_control_is_blind_to_resolution_faults]]` (the twin).
