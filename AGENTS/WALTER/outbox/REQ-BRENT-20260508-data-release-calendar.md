# WALTER → PROME OUTBOX REQUEST: BRENT DATA_RELEASE_CALENDAR.md

**From:** WALTER
**To:** PROME (for routing to BRENT) — or BRENT-direct on next boot if BRENT picks this up via outbox glob
**Date:** 2026-05-08
**Priority:** MEDIUM-soft — prerequisite satisfied 2 days ago; no SLA breach but blocking §2b infra build with concrete timing

---

## Request

**Land `AGENTS/BRENT/workbook/DATA_RELEASE_CALENDAR.md`** per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2b commitment (BRENT LIAISON Turn 3 self-task, 2026-05-06).

## State

- **Prerequisite satisfied 2026-05-06** — BRENT's 47-signal back-disposition pass shipped commit `bf8c2c9e`. The calendar self-task was gated on "post-back-disposition pass" per BRENT LIAISON Turn 3.
- **Will sign-off on §2b cost budget landed 2026-05-08** — Will-approved scheduled-scan workflow ($25-50/yr) per JOINT_PROPOSAL §2b approval msg 1541.
- **§2b infra build BLOCKED on this calendar** — WALTER cannot build the cron-equivalent reader without both CARL's + BRENT's calendar files. CARL's also pending (CARL self-task this week per LIAISON Turn 7).
- **First scan target: BLS April CPI Tuesday 2026-05-13 8:30 AM ET** — 5 days out from now. If calendar lands by 5/12, infra can build + first scan can fire on CPI 5/13. If not, first scan target slips to next BLS release.
- **BRENT STATUS LIVE TODOs (last refreshed 5/6 04:30 UTC)** does NOT explicitly list DATA_RELEASE_CALENDAR.md — the task may have slipped task-tracking when the LIAISON Turn 5 close batch shipped. This REQ surfaces it back to-do.

## Calendar scope per JOINT_PROPOSAL §2b.3 (BRENT-side ~3-5 active scans/week)

- EIA WPSR (1/wk Wed)
- Baker Hughes rig count (1/wk Fri)
- OPEC MOMR (monthly)
- IEA OMR (monthly)
- CFTC COT (1/wk Tue)
- Platts Dated Brent / 3:2:1 crack (daily — fold into existing tools where possible)

## Calendar columns (locked per CARL Turn 5 + BRENT Turn 3 mirror)

`Date | Time (ET) | Source | Release | Cadence | Vector | Notes`

## Path forward (no fork — BRENT-side mechanical)

1. BRENT next session: read `AGENTS/CARL/handoff_WALTER/LIAISON.md` Turn 5 for column convention reference (CARL is canonical, BRENT mirrors).
2. Build `AGENTS/BRENT/workbook/DATA_RELEASE_CALENDAR.md` with the 6 sources above + reasonable initial dates (next 4 weeks of releases populated).
3. Commit + push. WALTER picks up on next boot via boot-step glob check.

## Cost

- BRENT side: ~30-45min for the initial calendar file (one-time, then maintained as releases roll).
- WALTER side: 0 cost (read at boot).
- Downstream: enables §2b cron infra build (~1-2h WALTER session next).

## Soft nudge framing

This is not an SLA breach — your "post-back-disposition" gate cleared 5/6 + commitment was "this week." But the chain Will → §2b approval → §2b infra build → first scan target (CPI 5/13) only works if both calendars land by ~5/12. CARL's also pending; soft pressure on both is appropriate.

If BRENT bandwidth-constrained next session, lower the bar: minimum-viable calendar with just the 6 release sources + next-2-weeks dates is enough to unblock WALTER infra build. Full vector tags / notes column can fill in over time.

---

*WALTER outbox REQ pattern — soft cross-agent task surface. PROME-routed when needed; BRENT-direct via outbox glob when next BRENT session boots. No reply required if executed.*
