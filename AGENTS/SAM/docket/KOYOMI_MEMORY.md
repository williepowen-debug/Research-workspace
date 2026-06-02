# KOYOMI MEMORY

State file for the docket-steward sub-agent. Spec is in [`KOYOMI.md`](KOYOMI.md) (durable). This file holds dated state: run history, pending items, standing monitors.

**Ownership:** KOYOMI writes this file directly at end-of-run (consistent with KOYOMI's other write privileges — full-edit mode by default, busy-work-only). SAM may pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** KOYOMI reads `KOYOMI.md` first (spec), then `KOYOMI_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last synced*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KOYOMI at run start: what's moved in STATUS / THESIS / TIMELINE / CHANGELOG since the previous sync. Cleared at end-of-run.*

*(cleared at end of Run 4 — see LAST RUN below)*

---

## LAST RUN

### Run 4 — 2026-06-02 (post-Jun-2-auction sync; gap fix + Jul forward seed; Opus 4.7)
- **Jun 2 10Y auction backfilled to CALENDAR RECENTLY RESOLVED.** Workbook had captured result (BTC 3.530x, tail 0.7bp, WA 2.649%, ✅ orderly; mild soften vs May 12 same issue) but it had never been a forward catalyst — gap fix.
- **CATALYSTS.tsv gap investigation (per spec):** Pulled MOF Jun calendar (`auction/calendar/2606e.htm`). Discovered the gap was NOT isolated — **Jun 23 5Y** and **Jun 30 2Y** were also missing from the TSV. Pattern: prior runs had cherry-picked super-long auctions (30Y/20Y/40Y, J-ICS-relevant) and dropped belly/front (2Y/5Y). Filled both. Going forward: TSV should reflect the full MOF schedule; SAM can decide priority per row but absence = a real gap.
- **TSV adds:** Jun 23 5Y (🟡), Jun 30 2Y (🟡), Jul 1 Tankan Q2 (🟠), Jul 2 10Y (🟡), Jul 7 30Y (🟠), Jul 9 5Y (🟡), Jul 14 20Y (🟡), Jul 22 40Y (🟠), Jul 30 2Y (🟡), Jul 31 BOJ MPM (🔴). FOMC Jul 28-29 deferred (non-SEP, not a dot-plot meeting; SAM can elevate later).
- **CALENDAR adds:** "EARLY JULY — POST-MEETING FOLLOW-ON WINDOW" section seeded; Jun 23 / Jun 30 inserted into EARLY-MID JUNE table.
- **Pruning (>1wk rule):** Removed Tue May 26 Big 3 ESR rows (7 days old, at the edge — eligible). May 28 / May 29 / May 30 / May 31 retained (within 1 week). Added pruning note pointer to TIMELINE.
- **RELEASES.md "Confirmed dates" upgrades:** 13 new rows verified at source — Jun 10 30Y / Jun 16 BOJ / Jun 17 FOMC / Jun 23 5Y / Jun 25 20Y / Jun 30 2Y / Jul 2/7/9/14/22 JGB / Jul 28-29 FOMC / Jul 30 2Y / Jul 30-31 BOJ MPM (Day 2 = Jul 31, Outlook Report meeting). Clears PENDING item #1 from Run 3.
- **Date corrections caught at source:** NEXT RUN HINTS from Run 3 had said "FOMC Jul 30" — actual is **Jul 28-29** (decision day Jul 29). BOJ Jul "tentative" → confirmed **Jul 30-31** (decision day Jul 31). Both corrected.
- **Header refresh:** CALENDAR "Last Updated" line + INTERVENTION WATCH section header retained from Run 3 (no MOU walk-back / Phase 2 trigger to update).
- **Runway:** 59 days to furthest event (BOJ Jul 31); 11 events in next 14d (BOJ + FOMC week packed).
- **Runtime:** ~9 min. catalyst_countdown.py runs clean post-edits.

### Run 3 — 2026-06-01 (post-MOU-break sync; Opus 4.8)
- **CALENDAR ↔ CATALYSTS sync verified:** 11 forward catalysts in agreement (Jun 8 GDP, Jun 10 US CPI / JGB 30Y, Jun 16 BOJ / Sato / QT, Jun 17 FOMC, Jun 18 May TB, Jun 19 National CPI, Jun 25 JGB 20Y, Jun 26 Tokyo CPI).
- **TRUTH MODEL cleanup:** 4 cells stripped of live spot values that duplicated STATUS feed (USDJPY 159.64, Brent $94.78 x3, +4.02%). Replaced with structural-threshold framing + "(Live in STATUS)" pointers.
- **Stale header fix:** INTERVENTION WATCH section header updated from "#3 zone dormant on Brent collapse" → "#3 zone REACTIVATED Jun 1 on Iran MOU break" (had been left out-of-sync with its own table rows).
- **RECENTLY RESOLVED:** nothing prunable (all entries within 1-week retention window; oldest = May 26 Big 3 ESR = 6 days, edge of rule).
- **Jun 13 BOJ pre-meeting blackout:** declined to add to TSV (form-consistency — TSV holds discrete release/policy dates, not regime-boundary overlays). Kept as narrative in CALENDAR INTERVENTION WATCH.
- **Runway:** 25 days to furthest event (Tokyo Jun CPI, Jun 26); 3 events in next 14d.

### Run 2 — 2026-05-31 (synced to BOJ-hike repricing mark-up)
- TSV Jun 16 row updated to SAM-21 70% / mkt ~88% (was stale 55-65%).
- Pruned >1wk resolved rows; stripped live levels per TRUTH MODEL.
- Confirmed Jun 8 Q1-GDP 2nd-prelim at ESRI = 8:50 AM JST → fixed ESRI source URL in RELEASES.md.

### Run 1 — pre-2026-05-31 (initial docket structure)
- Established CALENDAR.md / CATALYSTS.tsv / RELEASES.md as the docket triad.
- See SAM's MAINTENANCE.md for structural-change history of the docket itself.

---

## PENDING (escalations SAM hasn't yet resolved)

- **Phase 2 Watch section reframe** may be needed if MOU walks back this week (Trump-Khamenei reset → Brent collapse → Phase 2 re-engages). Pre-emptive flag from Run 3 escalation #2. SAM-domain trigger. *(Still pending Jun 2; no MOU walk-back observed today; Brent live in STATUS.)*
- **CATALYSTS.tsv coverage policy (NEW):** Run 4 discovered that prior runs cherry-picked super-long JGB auctions and dropped 2Y/5Y. KOYOMI now defaults to **full MOF schedule** (all tenors). If SAM wants to suppress non-stress-relevant tenors (e.g., 2Y/5Y when carry-thesis-irrelevant), set explicit policy. Otherwise: comprehensive = the default going forward.
- **Jul Tankan Q2 date (Jul 1)** — used cadence rule (1st business day of July; March Tankan released Apr 1 2026); could not find an explicit BOJ Tankan release-schedule page that confirms the date forward. Surface to SAM in case a closer-to-date check finds a different date. Non-blocking — directionally correct.
- **FOMC Jul 28-29** added to RELEASES.md as confirmed but NOT to CATALYSTS.tsv (non-SEP meeting, no dot plot). SAM call whether to promote.

---

## STANDING MONITORS (surface each run)

- **BOJ pre-meeting blackout windows** (T-2 of each MPM) — currently kept as narrative in CALENDAR, not in TSV per form-consistency call from Jun 1. Revisit if SAM wants regime-boundary dates in TSV going forward (would need 1-2 other boundary rows added for consistency).
- **Recurring weekly catalysts** (CFTC release Fri/Mon) — not in TSV (handled by `cftc_jpy.py` auto-pull). Surface if cadence changes.
- **Post-meeting catalyst-window refill** — after each major catalyst resolves, the forward horizon thins; pull next-month's events from RELEASES.md cadence rules.
- **MOF auction calendar alteration page** — `auction/calendar/26MMae.htm` (e.g., 2606ae.htm) records mid-month tenor-band changes. Check at month boundary; current Jun 2026 alteration was a liquidity-enhancement tenor-band tweak (15.5-39 vs 11-39, then back), no date moves.
- **MOF schedule full-coverage default** — KOYOMI now mirrors the full MOF auction schedule (all tenors) in TSV unless SAM sets a suppress policy. See PENDING.

---

## NEXT RUN HINTS

- **Post-Jun-10 30Y auction:** backfill result to CALENDAR RECENTLY RESOLVED (workbook auto-fetches via `jgb_auctions.py`). Critical row — direct SAM-26 mechanism test.
- **Post-Jun-16 BOJ + Jun-17 FOMC resolution:** RECENTLY RESOLVED will fill heavily; prune pass + TIMELINE cross-check. Also expect TSV `Sato joins BOJ board` + `BOJ interim QT assessment` rows to resolve same day; mark and prune per >1wk rule.
- **Pull Aug auctions from MOF Aug calendar (auction/calendar/2608e.htm)** post-Jul-MPM to keep runway >30d. Also Shunto interim data (Aug, no firm date yet — RENGO cadence).
- **Pull MOF Aug alteration page** (`2608ae.htm` if it exists) to catch any post-budget tenor-band shifts.
- **Verify Tankan Q2 Jul 1 date** at BOJ Tankan release page once schedule posts (currently using cadence rule + March-2026 precedent).
- **If MOU walks back:** refresh INTERVENTION WATCH + Phase 2 Watch + GEOPOLITICAL WATCH tables; trigger likely auto-detected via STATUS Brent move.
- **PENDING coverage-policy decision:** if SAM has not weighed in on the "full MOF schedule vs cherry-pick" question, default to full schedule for Aug onwards (Run 4 set this default).
- **National May CPI Jun 19 (post-BOJ)** — high-information row; once resolved, weight National vs Tokyo in the prune note.
