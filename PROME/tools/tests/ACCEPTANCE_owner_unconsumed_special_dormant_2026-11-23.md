# Acceptance: the boot backlog line counts special and dormant desks, never names them (WQ-729 item 2)

**Authority:** Will 2026-11-23 12:03 ET, "WQ-729 item 2 (drop RAV and BARON from the boot backlog line): approved." Record `PROME/proposals/2026-11-23_wq732-follow-up-RULED.md`. Conditions written before the edit.

| # | Condition | Result |
|---|---|---|
| A1 | A SPECIAL or DORMANT desk holding aged inbox items is not named on the line | TESTED: fixture desks SLEEPY and MANUAL absent; live run 2026-11-23 names MARCO and FLG only |
| A2 | The fact does not vanish: the tail counts such desks and names the command that lists them | TESTED: "2 special or dormant desk(s) with aged items not named" in the fixture and in the live run (RAV, BARON) |
| A3 | ACTIVE and TIER-2 desks read exactly as before | TESTED: the other 13 tests unchanged and passing; live MARCO and FLG text unchanged |
| A4 | A boot whose only hits are special or dormant reads the gate line as passing | IMPLEMENTED in `prome_gate.py` (pass test uses `launchable_hits`); not exercised by a fixture |

**Neighbours considered:** ordinary (A3) · overlap N/A, a desk has one roster class · wrong owner N/A, no ownership is decided here · missing information: a desk with unknown liveness is still listed in the tail, unchanged · concurrent activity N/A, read-only.

**State:** IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED WITH NAMED RESIDUE (2026-11-23 12:53 ET). reads: 1.

## Independent read (Opus, read-only, about 12:51 ET 2026-11-23)
The reader ran the author's suite (14 tests, OK) and nine counterexamples of its own on fixtures and on the live tree. **A1 to A4 hold** (A4 on a fixture, by evaluating the gate's exact pass expression; the full boot gate was not run). Old and new code print byte-identical lines for ACTIVE-only inputs. No other reader of the removed wording exists in the repository.

**Residue, NOT fixed (no edit after the read):**
1. A SPECIAL or DORMANT desk is still NAMED, and still fails the gate line, through the tail's "undated" and "liveness UNKNOWN" lists (a dormant desk holding an undated file; a special desk with aged items and a git error). Not occurring live today. Low to medium.
2. A SPECIAL desk's ACTION count no longer appears on the line (RAV's 1 ACTION item is inside the desk count). Within the approved scope.
3. `ACCEPTANCE_owner_unconsumed_boot_line_2026-11-16.md` condition A8 ("prints tagged 'Will-driven' … 'not a PROME launch candidate'") is SUPERSEDED by this file; that file is not edited.
4. The tail points to `inbox_census.py <DESK>`, but the line no longer gives the desk names; the classes are in `PROME/ROSTER.md` (DORMANT and SPECIAL sections).
