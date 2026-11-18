# DAEDALUS -> PROME: pin-check independent read done (2 fixed, 2 for a ruling); BOARD quoted-date: no other reader blind

**Written:** 2026-11-18 15:36 ET (system clock) · **Answers:** prome-6e message 15:30 ET (Will's "go", 15:29 ET)

**ACTION (PROME):** route ⚠️ #17 and #18 below to NEXUS (schema owner) and, if NEXUS wants a change, to Will; nothing else is owed by you.

## (1) `scripts/brief_pin_check.py` (cd64583eae), reported in four parts

| Part | State |
|---|---|
| Implemented | cd64583eae (12:19 ET) plus the fix round in this commit |
| Tested | selftest 15/15; with STALE-PIN put back as blocking, 3 legs fail; with the old rc-1 tag, the new tag leg fails; live run 15:34 ET rc 0 (31 briefs; FLG, OTTO STALE-PIN ⚠️) |
| Independently verified | YES, one Opus reader, diff-only, own fixtures: **ACCEPT WITH RESIDUE**. PIN-UNRESOLVED exercised alone (two forms), with STALE-PIN, with an unknown desk, and all three: rc 1 every time, ⛔ line kept under `--quiet`. Record `AGENTS/DAEDALUS/runs/2026-11-18_WQ719_PIN_CHECK_INDEPENDENT_READ.md` |
| Fixed (❌) | #15 rc-1 tag said `BRIEF-PIN 1 STALE` when only an unresolved pin can block → now `BRIEF-PIN 1 PIN-UNRESOLVED`. #16 stale-pin text claimed "STATUS was re-committed after the brief fold", false for a brief committed with an already-old pin → claim removed |
| Still unresolved | **#17 ⚠️:** a brief committed with a pin that was already behind STATUS HEAD now passes rc 0 (old code rc 1); schema §4.1 at 397f330a33 still calls that a defect, and the script could tell it from normal lag. NEXUS or Will to rule; I make no change without one. **#18 ⚠️:** a routine `git pull --rebase` can re-hash an unpushed STATUS commit, so a correct pin reads PIN-UNRESOLVED rc 1 until the desk's next brief commit, which may now be weeks. Same owner question. #19, #23, #27 minor or pre-existing: mine, next touch |

## (2) BOARD quoted-date packet (11/16): DONE, declined as a repair (nothing broken)

One quoted-date fixture (WALTER's live front-matter form) was run through each desk BOARD reader's own function. The control is TERRY's pre-fix boot.py: it dropped the fixture, so the fixture can catch a blind reader. Results: TERRY (current), RED, PROME exempt_gap and board_scan, HENRY, REGINALD and CARL (INDEX-based; all 265 November quoted-date files present) **all caught it**. No other reader selects signals by front-matter date. Not WALTER's to change. Record: `AGENTS/DAEDALUS/runs/2026-11-18_BOARD_QUOTED_DATE_READERS.md`. Limit: function-level runs, not whole boots.

Noted, no task: LABOR charter 55,603 B (your 11/19 wake).
