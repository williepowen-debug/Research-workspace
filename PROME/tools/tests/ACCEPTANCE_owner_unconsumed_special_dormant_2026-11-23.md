# Acceptance: the boot backlog line counts special and dormant desks, never names them (WQ-729 item 2)

**Authority:** Will 2026-11-23 12:03 ET, "WQ-729 item 2 (drop RAV and BARON from the boot backlog line): approved." Record `PROME/proposals/2026-11-23_wq732-follow-up-RULED.md`. Conditions written before the edit.

| # | Condition | Result |
|---|---|---|
| A1 | A SPECIAL or DORMANT desk holding aged inbox items is not named on the line | TESTED: fixture desks SLEEPY and MANUAL absent; live run 2026-11-23 names MARCO and FLG only |
| A2 | The fact does not vanish: the tail counts such desks and names the command that lists them | TESTED: "2 special or dormant desk(s) with aged items not named" in the fixture and in the live run (RAV, BARON) |
| A3 | ACTIVE and TIER-2 desks read exactly as before | TESTED: the other 13 tests unchanged and passing; live MARCO and FLG text unchanged |
| A4 | A boot whose only hits are special or dormant reads the gate line as passing | IMPLEMENTED in `prome_gate.py` (pass test uses `launchable_hits`); not exercised by a fixture |

**Neighbours considered:** ordinary (A3) · overlap N/A, a desk has one roster class · wrong owner N/A, no ownership is decided here · missing information: a desk with unknown liveness is still listed in the tail, unchanged · concurrent activity N/A, read-only.

**State:** IMPLEMENTED · TESTED (author's tests) · not INDEPENDENTLY VERIFIED: no independent reader has run a counterexample. The change touches a boot-gate advisory line, so one independent read is owed before it is called fixed. reads: 0.
