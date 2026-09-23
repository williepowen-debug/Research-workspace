# L446 repair — the DESK CADENCE section broke two ROSTER consumers (acceptance conditions first)

**Author:** PROME `prome-68` · 2026-09-23 11:1x ET · **Class:** WQ-229 consequential (a shared contract, `PROME/ROSTER.md`; the defect class RECURRED: the CATO heading did the same on 9/15). Found by the independent L446 reader (Opus, ledger in the session scratchpad `l446_ledger.md`: **NOT VERIFIED**, ❌ F1/F2/F4).

## Defects, verified by PROME at the artifact before any edit
- **F1:** `AGENTS/DAEDALUS/scripts/render_directory.py --check` → rc=1 `UNRECOGNISED ROSTER section 'DESK CADENCE …'`. `FLEET_DIRECTORY.md` is frozen at its 9/18 render, so YURI's 9/19 seat is missing from a boot-read surface.
- **F2:** `fleet_dashboard.parse_roster()` reports **38** ACTIVE (should be **34**). It reads everything between `## ACTIVE` and `## TIER-2`, and the section sat inside that span, so its token table (DAILY/WEEKLY/MONTHLY/UNDECLARED) parsed as four agents.

## Acceptance conditions (the test list)
- **AC1:** `render_directory.py --check` passes. PROME does NOT regenerate or commit `FLEET_DIRECTORY.md`, which is DAEDALUS's generated file; DAEDALUS is packeted.
- **AC2:** `fleet_dashboard.parse_roster()` ACTIVE = 34, TIER-2 = 4, DORMANT = 2.
- **AC3:** `spawn_list.py --as-of 2026-09-23` output byte-identical before and after, including rc. The cadence reader still finds the section: it splits on the substring `## DESK CADENCE`, which `### DESK CADENCE` contains.
- **AC4:** every other ROSTER consumer (`reads_check`, `read_cap_check --agent PROME`, `lane_coverage_check`, `sweeps_due`, `maturity_scan`, `agent_freshness`) gives byte-identical output and rc. The rc=2 on `reads_check`/`sweeps_due` is PRE-EXISTING and unrelated: undeclared desks, and a profile-clock check.
- **AC5:** no text anywhere BEFORE the new heading contains the substring `## DESK CADENCE`, because spawn_list takes the FIRST occurrence.

## Neighbours (WQ-229)
- **Ordinary:** AC1–AC4.
- **Overlap:** the section content moves verbatim, so no rule text changes. Only the heading level and position change, plus one placement note.
- **Wrong owner:** `render_directory.py` and `FLEET_DIRECTORY.md` are DAEDALUS's; the renderer is not edited, and the "add it to a list" alternative is DAEDALUS's call. The packet names both routes.
- **Missing information:** spawn_list's no-section path already exists, so a missing section reads CANNOT-EVALUATE, never a crash (the reader verified this).
- **Concurrent activity:** no live desk session (ListAgents empty at 11:0x); ROSTER is PROME-owned.

## Fix
Move the section verbatim to the end of the file, below `## Transmission chain`, a known non-agent section the renderer skips. Demote its heading to `###` and add one placement note. **Not fixed here (residue, carried):** F5 (the token table parses as desks, so the printed cause reads "absent" instead of "UNDECLARED") · F6/F7 (duplicate-with-bad-token; bold/lowercase names dropped) · F8 label · F11 stale docstring · F12 timezone. All are spawn_list code; the two-correction discipline and a separate reader apply. F13: desks have no legal route to declare (ROSTER is PROME's) — a design question for DAEDALUS.

## Result (PROME's own tests. State: IMPLEMENTED · TESTED, NOT yet independently verified)
- **AC2 ✅:** `parse_roster()` → ACTIVE 34 · TIER-2 4 · DORMANT 2 (was 38/4/2).
- **AC3 ✅:** `spawn_list.py --as-of 2026-09-23` is byte-identical, rc included.
- **AC4 ✅:** `agent_freshness`, `lane_coverage_check` and `maturity_scan` are byte-identical. `reads_check` and `read_cap_check` differ ONLY in `FLEET_DIRECTORY.md`'s byte count (see the surprise below). `sweeps_due` drops its `DIRECTORY-STALE` line for the same reason. rc unchanged everywhere.
- **AC1 ✅ on the section; a new finding surfaced:** the `UNRECOGNISED ROSTER section` failure is gone. The renderer now runs to its end and exits rc=1 on a DIFFERENT, previously masked guard: `REVERSE-GUARD: 1 ACTIVE/TIER-2 agent(s) have NO FLEET_MAP row: ['YURI']`. That is a real DAEDALUS finding (YURI was seated 9/19), not caused by this edit. The F1 failure had been hiding it.
- **AC5 ✅:** the only `DESK CADENCE` string is the new `###` heading.
- ⚠️ **Surprise, recorded:** `render_directory.py --check` is NOT a dry run. The run REWROTE `AGENTS/DAEDALUS/FLEET_DIRECTORY.md`: 10,822 → 11,286 B, a correct render that now includes YURI. The file is DAEDALUS's, so PROME restored it to HEAD with `git checkout --` (the tree was clean before the run, so the change was PROME's alone). DAEDALUS is packeted to regenerate it itself.
