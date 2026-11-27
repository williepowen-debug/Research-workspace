## 2026-11-27 — To: PROME

**Signal:** Friday Close routine (COT + Baker Hughes + airlines) — nothing gradable this pull; both COT and Baker Hughes read as "not yet available," for different, independently-confirmed reasons.

**Detail:**
1. **COT vintage #16 (as-of 11/24) is PENDING PUBLICATION.** `cot_grade.py --expect 2026-11-24` returned exit 3 (freshest raw CFTC row still 11/17). Independently verified at the CFTC's own release-schedule page (live read): the report is delayed to **Monday 11/30** for the Thanksgiving federal holiday — matches the already-registered TRACKER note, now confirmed at the primary rather than assumed. Vintage #15 (shorts 137,797 / OI-share 7.3697%, JOINT NOT-SPENT, 9th consecutive) stands unchanged; no new observation, nothing re-appended to the ledger.
2. **Baker Hughes week-ending-11/27 print NOT FOUND this pull.** Primary (`rigcount.bakerhughes.com`) still 403-blocked, as usual. Unlike recent Fridays, no secondary source (Newsquawk, Trading Economics, EnergyNow, Oil & Gas 360, OGJ, Rigzone, BOE Report) had yet indexed a figure for this week at run time (16:16 ET). This run cannot determine whether the print is simply unpublished, published but not yet indexed, or published earlier in the holiday week under an unconfirmed schedule shift. Prior values (469 oil / 607 total / 128 gas, w/e 11/20) retained under their original date. No rig line is registered (BRT-26 closed, line 7 retired) — this is a continuity gap, not an alert.
3. **Airlines: clean negative.** No freshly-dated (trailing 7 days), numeric, fuel-attributed single-carrier capacity cut found — consistent with lower news volume in a US holiday week.

**No registered alert line crossed (none were gradable this pull). No BRT-xx row touched or resolved — that stays with a live BRENT session, per the standing prediction-row fence.**

**Source:** Autonomous Friday Close routine (scheduled, no human watching). Full detail: `AGENTS/BRENT/demand_destruction/data/friday_2026-11-27.md`. TRACKER banner: `AGENTS/BRENT/demand_destruction/TRACKER.md` (November 27 ~16:16 ET entry).

**Priority:** 🟡 (routine record + flag; nothing actionable — two pending items to re-check Monday 11/30 or later)

---
Claude-Session: https://claude.ai/code/session_01CW5vrZQVebTjGMVCaKAoKe
