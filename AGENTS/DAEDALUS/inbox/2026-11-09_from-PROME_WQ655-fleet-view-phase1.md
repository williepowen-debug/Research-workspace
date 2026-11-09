# 2026-11-09 — From PROME to DAEDALUS: WQ-655 Phase 1 — build the generated, read-only fleet view

**ACTION:** Build one generated, read-only fleet view for PROME. Deliver a working view, its tests and a return packet. Then stop: Will reviews before anything else follows.

**Authority:** WQ-655, Will in PROME's chat 2026-11-09 14:21 ET. His full words are in `PROME/proposals/2026-11-09_wq655-fleet-view-phase1-RULED.md`; that file governs and this brief only applies it. Background: `PROME/proposals/2026-11-09_prome-state-simplification-PROPOSAL.md` §1, §5 (PROME's sketch — a starting point, not a spec; Will's ruling overrides it where they differ). $0.

## Hard bounds (Will's words, kept)
- **Read-only.** No change to authority, canonical records or boot requirements. The view writes only its own generated output file(s); it edits no ledger, no DOCKET, GATES, ORCH_LOG, ROSTER, inbox or desk file.
- **Use existing readers wherever practical.** Inspect these BEFORE writing any new reader:
  - spawn slate: `PROME/tools/spawn_list.py`, `PROME/tools/spawn_slate.py` (yours, 10/02)
  - inbox: `PROME/tools/inbox_census.py` (PROME changed it today, c49c5f261f: dotfiles and README* scaffolds skipped; PROTOCOL.md and RECEIPT.md in FERT's inbox still count, a known gap)
  - orchestration: `scripts/orch_log.py`, `PROME/tools/orch_closeout.py`, `PROME/state/ORCH_LOG.tsv`
  - activity attribution: `PROME/tools/desk_activity.py`
  - session discovery: `PROME/tools/session_presence.py`, `PROME/tools/session_bridge.py`, `PROME/tools/session_identity.py`
  - also: `PROME/ROSTER.md`, `PROME/DOCKET.tsv`, `PROME/GATES.tsv`, `PROME/tools/board_scan.py`, the desks' `NEXUS_BRIEF.md` files (31, no common header)
- **Preserve Git preflight controls.** This is not a Git-coordination redesign.
- **Not in scope:** positions and conviction; any "live now" marker maintained by hand; a trial, recurring measurement program, new checker framework or expanded audit.

## What the view must show
1. **Opening view, exception-first:** due work · unconsumed returns · blockers · coordination conflicts · consequential unknowns. A clean desk does not appear in the opening view.
2. **The full roster on demand** from the same underlying data, e.g. a flag or a second section. One collection, two renderings.
3. **Every line carries a timestamp and a source pointer** (file and line, commit, or ledger key) so PROME can verify at the artifact.
4. **Three distinctions, never merged:**
   - an **attributable commit** (a desk-prefixed commit touched the desk's paths) vs **substantive work** (it changed a STATUS, a grade, a ledger row), as far as existing readers can tell — say which basis was used;
   - an **observed session** (evidence a session existed, with its time) vs **current activity** (evidence it is running now). Scripts cannot see Claude ListAgents; show what the discovery tools can observe, with coverage stated, and UNKNOWN beyond it;
   - **missing evidence** (UNKNOWN: the source is absent, unreadable or out of coverage) vs a **clean result** (checked, nothing found).

## Today's live examples to test against (desktop, 11/9)
- Will-launched desks PROME did not spawn (WALTER, HAWK, CORAL, FALCON, OSPREY, CREED, BROCK about 10:44 ET); PROME-spawned ORACLE, SAM, VULCAN, BRENT, HENRY, ZHAO, NEXUS, BOND, CARL, FERT; ORACLE, OSPREY and CREED closed out (ORCH_LOG CLOSE rows); CORAL reopened by Will directly at 12:55 ET.
- Shared-index sweeps: WALTER 811962c856 and 6022eddfe5 committed other desks' staged renames (a coordination-conflict example).
- A due row with no citing return (GATE-NEXUS-T12S-DFII10 before NEXUS answered); an unconsumed return (`PROME/inbox/` files from CATO and DAEDALUS, 11/9).
- A scaffold-only inbox that must read as empty, not unread.

## Acceptance (write it before building, in your own record)
Neighbours to consider: ordinary · overlap (an item both committed and pending) · wrong owner · missing information · concurrent activity. Give a one-line N/A where one does not apply. Report IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED separately. An independent read is your call under your own charter; it is not required by this brief.

## Deliver
- Generator plus tests in your own paths, or under `PROME/tools/` if you judge it belongs beside the readers it reuses. Name the output path; a sensible default is `PROME/state/FLEET.md`, generated, never hand-edited.
- Run it once on the live repo and commit that output.
- Return packet to `PROME/inbox/2026-11-09_from-DAEDALUS_WQ655-fleet-view.md` with: commits, how to run it, what each section answers, which existing readers it reuses, coverage limits, and anything you chose differently from PROME's sketch and why.
- Commit path-scoped; push via `scripts/safe-push.sh`. Then stop.
