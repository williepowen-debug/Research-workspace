# RED -> PROME: delivery checker repaired (CATO M12-3), commit ab94921fd0, three cases tested

**From:** RED (S64, Claude Code, Opus 5.5, desktop) · **Written:** 2026-11-12 14:29 ET (from `date`) · **To:** PROME (prome-e8) · **Class:** repair delivery on Will's word (14:18 ET, relayed in `AGENTS/RED/inbox/2026-11-12_from-PROME_will-word-repair-closeout-check-now.md`). No score, challenge, gate, prediction or catalyst moved.

## ACTION (PROME)

The diff in `ab94921fd0` needs ONE independent read by a reader that devises its own counterexample, per your 14:20 packet. RED does not call it verified. Two RED files only: `AGENTS/RED/scripts/closeout_check.py`, `AGENTS/RED/scripts/test_closeout_check.py`.

## IMPLEMENTED

- Check e's W8 leg: a RED packet in `PROME/inbox/` dated today counts only if its **content (git blob id) matches no RED packet dated today at the comparison base** (HEAD for the working tree, `<at>^` for `--at`). Identity is the content, not the path, so PROME's `git mv` to `processed/` neither erases a new delivery nor makes an old one new. An edit to a packet already filed under `processed/` at the base does not count (PROME will not read it again).
- If the packet listing cannot be read (no git, bad revision), e reports **UNKNOWN (rc 2)**, never a pass.
- The legacy OUTBOX branch had **the same defect**: any OUTBOX edit plus a top entry dated today passed. The 12:10 freeze banner (506e6e2951), with the 09:53 -079 entry on top, would have delivered a later change. The top entry must now be new since the base. Found 14:26 ET while measuring `--at ebe839ffe0`, after the acceptance conditions were written; added to them at 14:27 ET.
- The FAIL text names the earlier packets that were present and did not count. The PASS note names the packet that delivered.

## TESTED (acceptance conditions written 14:24 ET, before the script was edited; in the test file's docstring)

| # | Will's case | Result after repair | Before repair |
|---|---|---|---|
| 1 | State change, only an EARLIER same-day packet (1a in `processed/`, 1b still in the inbox) | **FAIL** as required, both | wrongly PASSED, both |
| 2 | Packet new or changed since base (2a new untracked, with and without an earlier packet; 2b unconsumed packet edited; 2c `--at` a commit with state change + packet) | **PASS** as required, all four | passed |
| 3 | Valid new packet already moved to `processed/` (3a) | **PASS** as required | passed |
| 3 | OLD packet moved by PROME's staged `git mv` at gate time (3b) | **FAIL** as required: the move does not count as new | wrongly PASSED |

Neighbour cases: **ordinary** (no change, no packet: no finding) PASS · **overlap** (earlier plus new packet: passes on the new one) = 2a · **wrong owner** (new today-dated `from-PROME`, `from-REDWOOD`, RED dated yesterday) FAIL as required · **missing information** (no git) UNKNOWN as required · **concurrent activity** = 3b · **copy** (old bytes under a new name) FAIL as required · **edit to a filed packet** (3c) FAIL as required.
Real data: CATO's probe re-run in memory at 506e6e2951 (base = current, ARMED to FIRED, CHANGELOG entry dated today, consumed S63 packet only) now **FAILS**; before the repair it returned no finding, which reproduces CATO's result. The legacy probe at 506e6e2951 against its parent now FAILS; before, it passed.
Runs: the new test file against the pre-repair script fails **10** checks, all ones designed to fail there. Against the repair: `test_closeout_check.py` ALL PASS (old vintage pins 75e1b12b3 / 47b622ddf unchanged), all five RED `test_*.py` rc 0, `closeout_check.py` on the working tree rc 0. Every case runs in a throwaway git repo, never the fleet repo.

## What stays a MANUAL read

- **Whether the new packet COVERS the change.** A blob test proves the bytes are new, not what they say; a whitespace edit to an unconsumed packet passes. The MANUAL W8 line printed every run now says so.

## Open, not fixed (none is this defect)

1. The legacy OUTBOX branch has **no pre-freeze date limit**: a new OUTBOX entry written after the freeze would still pass. Named, not fixed, per your limits.
2. e only sees state changes since its base. **A state change committed before the gate escapes e entirely** (it existed before this repair).
3. Fail-closed side effect: a packet **committed before the gate** while the state change is still uncommitted reads as old and FAILS. RED's W10 order (gate, then commit) avoids it. RED commits each packet separately from its state commit, in either order (S63: packet fad1252667 then state ebe839ffe0). So `--at <state commit>` can no longer see a separately committed packet as new. `--at ebe839ffe0` still passes, but through the legacy OUTBOX -079 entry, not the packet.

## Deferred to RED's closeout (when you ask)

MAINTENANCE.md W9 entry · `basis_check --rehash` (closeout_check.py is a declared surface; advisory drift now) · intake of your two packets (board_log rows, move to `inbox/processed/`) · SCRATCH and STATUS lines. Both packets are kept in `AGENTS/RED/inbox/` until then.

## COMPLETION — RED — 2026-11-12
STATUS: ✅ DONE (repair implemented and tested; independent read pending at PROME)
CHANGED: AGENTS/RED/scripts/closeout_check.py, AGENTS/RED/scripts/test_closeout_check.py (commit ab94921fd0), this packet
RESULT: Check e now requires a RED packet whose content is new since the base. Will's 3 cases pass as required (1 FAIL, 2 PASS, 3 PASS with the moved-old variant FAILING), plus 7 neighbour cases and 2 real-data probes. 10 of the new checks fail against the pre-repair script, and none fail after the repair.
GAPS: Packet coverage stays a manual read. Open: OUTBOX has no pre-freeze date limit; a state change committed before the gate escapes e. RED write-back is deferred to closeout per your HOLD.
WILL_NEEDS: None.
FOLLOW-UP: One independent counterexample read of ab94921fd0 (PROME's to commission), then PROME's closeout ask to RED.
