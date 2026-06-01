# KOYOMI MEMORY

State file for the docket-steward sub-agent. Spec is in [`KOYOMI.md`](KOYOMI.md) (durable). This file holds dated state: run history, pending items, standing monitors.

**Ownership:** KOYOMI writes this file directly at end-of-run (consistent with KOYOMI's other write privileges — full-edit mode by default, busy-work-only). SAM may pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** KOYOMI reads `KOYOMI.md` first (spec), then `KOYOMI_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last synced*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KOYOMI at run start: what's moved in STATUS / THESIS / TIMELINE / CHANGELOG since the previous sync. Cleared at end-of-run.*

*(empty — first KOYOMI_MEMORY entry; next run will populate)*

---

## LAST RUN

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

- **RELEASES.md Jun 16 BOJ + Jun 17 FOMC rows** could be upgraded with official-source date verification (currently corroborated internally via STATUS/THESIS but not from the BOJ/Fed pages). Non-blocking; ~3 min next KOYOMI run with WebSearch. From Run 3 (Jun 1) escalation #3.
- **Phase 2 Watch section reframe** may be needed if MOU walks back this week (Trump-Khamenei reset → Brent collapse → Phase 2 re-engages). Pre-emptive flag from Run 3 escalation #2. SAM-domain trigger.

---

## STANDING MONITORS (surface each run)

- **BOJ pre-meeting blackout windows** (T-2 of each MPM) — currently kept as narrative in CALENDAR, not in TSV per form-consistency call from Jun 1. Revisit if SAM wants regime-boundary dates in TSV going forward (would need 1-2 other boundary rows added for consistency).
- **Recurring weekly catalysts** (CFTC release Fri/Mon) — not in TSV (handled by `cftc_jpy.py` auto-pull). Surface if cadence changes.
- **Post-meeting catalyst-window refill** — after each major catalyst resolves, the forward horizon thins; pull next-month's events from RELEASES.md cadence rules.

---

## NEXT RUN HINTS

- **Post-Jun-16 BOJ resolution:** RECENTLY RESOLVED will fill up; prune pass needed. Also TSV needs new forward window populated:
  - Jul JGB auctions (cadence: 10Y/20Y/30Y/40Y monthly — pull from MOF schedule via RELEASES.md)
  - FOMC Jul 30 (tentative — verify at fed calendar)
  - Tankan Q2 (early Jul, ~Jul 1)
  - Next BOJ MPM Jul 30-31 (tentative — verify at BOJ schedule)
  - Shunto interim data (Aug)
- **If MOU walks back:** refresh INTERVENTION WATCH + Phase 2 Watch + GEOPOLITICAL WATCH tables; trigger likely auto-detected via STATUS Brent move.
- **RELEASES.md verification upgrades** — opportunity to bring Jun 16/17 rows to ✅ CONFIRMED if WebSearching anyway.
