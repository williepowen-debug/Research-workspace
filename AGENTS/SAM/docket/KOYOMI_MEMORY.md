# KOYOMI MEMORY

State file for the docket-steward sub-agent. Spec is in [`KOYOMI.md`](KOYOMI.md) (durable). This file holds dated state: run history, pending items, standing monitors.

**Ownership:** KOYOMI writes this file directly at end-of-run (consistent with KOYOMI's other write privileges — full-edit mode by default, busy-work-only). SAM may pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** KOYOMI reads `KOYOMI.md` first (spec), then `KOYOMI_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last synced*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KOYOMI at run start: what's moved in STATUS / THESIS / TIMELINE / CHANGELOG since the previous sync. Cleared at end-of-run.*

*(cleared at end of Run 5 — see LAST RUN below)*

---

## LAST RUN

### Run 5 — 2026-06-03 (light-touch narrative refresh + 3-candidate triage → SAM apply pass extended scope; Opus 4.7)

**SAM-APPLIED post-Run-5 (commits coming together as bundle):**
- **TSV-scope decision (Will): option (a) — extend TSV scope to admit SAM-internal mechanical triggers.** Schema change: added `type` column (`external` default / `sam-internal` explicit) to CATALYSTS.tsv header. Backfilled 2 qualifying rows (Sat Jun 6 CFTC residual-gate re-check; Tue Jun 9 SAM-21 Polymarket re-check). Inclusion bar (both required): DATE-SPECIFIC + ACTION-FORCING decision gate. Ongoing monitors + standing/conditional triggers stay in MEMORY/STATUS, NEVER in TSV. Precedent logged in `KOYOMI.md` § TSV-SCOPE PRECEDENT — future internal-trigger questions self-resolve without re-escalating to Will.
- **catalyst_countdown.py updated:** SAM-internal rows render with 🔧 prefix (imminent + upcoming sections). Empty `type` treated as `external` for back-compat. Tested Jun 3 — Jun 6 CFTC + Jun 9 SAM-21 both surfacing labeled.
- **jgb_auctions.py filter verified:** existing `"jgb" + "auction" in event` filter naturally excludes SAM-internal rows (0 matches as expected). No code change needed.
- **CALENDAR PHASE 2 WATCH refresh (Escalation #3):** Brent escalating not collapsing — header reframed to "REFRAMED Jun 3" with "Brent escalating not walking back — Phase 1 oil pressure compounding" framing. Brent row updated with multi-day +ve sequence ($97.70, 4th up day). MOU framework row updated with deepening narrative (no walk-back overnight, fresh US-Iran clashes).
- **CALENDAR forward-events table:** Sat Jun 6 + Tue Jun 9 SAM-internal rows added with 🔧 prefix, full what-to-check + signal columns.

**Pre-apply triage (as KOYOMI originally returned — kept for audit):**
- **State-of-truth movement since Run 4 (Jun 2 PM, `127ae123`):** 5 commits today on SAM. Polymarket BOJ Jun 16 87.6% → 94.8% (SAM-21 held 70% with Jun-9 mechanical trigger pre-registered). USDJPY 159.92 → 160.03 (first hard-trigger break this cycle, no docket impact). Brent $95.67 → $97.70 (4th straight up day). MOF intervention REFERENCE DATA refreshed — authoritative ¥11.73T aggregate replaces ~¥10T two-op estimate (per-op breakdown awaits MOF quarterly release).
- **SAM-provided candidates triaged (3):**
  - **Item 1 (🔴 Jun 9 Polymarket re-check):** SAM-internal mechanical trigger. NOT auto-added — fails TSV universe gate (TSV is for public dated releases/policy; SAM-internal review triggers are a new precedent class). Escalated to SAM for scope decision (see ESCALATIONS in summary + PENDING).
  - **Item 2 (🟡 MOF quarterly per-op intervention release, ~early August):** Discrete dated catalyst once date verified at MOF source. Cadence imprecise ("~early August") — needs source check at `mof.go.jp/english/policy/international_policy/reference/feio/quarterly/` to pin actual date. Logged to PENDING for next-run source verification, not added to TSV yet.
  - **Item 3 (🟡 Jun 6 CFTC weekly — new METHOD framing):** Routine narrative refresh, within owned write-set. **Applied to CALENDAR.md PHASE 2 WATCH CFTC row** — added `-108K = 60% cycle-peak amplifier line` to threshold col + "first scheduled amplifier/residual gate under THESIS § CARRY-UNWIND PROBABILITY METHOD" to notes. CFTC stays out of TSV per spec (boot.py auto-pulls; excluded class).
- **Pruning (>1wk rule):** No prunes this run. May 28 (6d), May 29 (5d), May 30 (4d), May 31 (3d), Jun 2 (1d) all within retention. Nothing eligible until Jun 4 (May 28 turns 7d).
- **Baseline audit:** No trigger fired this run. Monthly trigger fired Run 4 (Jun 2, first run of June). Per METSUKE Run 2 [[finding_subagent_baseline_audit]]: next monthly fire = first run of July. No post-miss trigger.
- **Header refresh:** CALENDAR "Last Updated" → 2026-06-03 (Run 5 narrative).
- **Runway:** 58 days to furthest event (BOJ Jul 31). 5 events in next 14d (GDP-2nd, US CPI, JGB 30Y, BOJ MPM, FOMC). High-traffic window in 13-14 days.
- **Runtime:** ~5 min. catalyst_countdown.py runs clean post-edits. No TSV edits this run.

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

- **Phase 2 Watch section reframe** may be needed if MOU walks back this week (Trump-Khamenei reset → Brent collapse → Phase 2 re-engages). Pre-emptive flag from Run 3 escalation #2. SAM-domain trigger. *(Still pending Jun 3; no MOU walk-back observed; Brent up to $97.70 — moving the OTHER direction.)*
- **Jul Tankan Q2 date (Jul 1)** — used cadence rule (1st business day of July; March Tankan released Apr 1 2026); could not find an explicit BOJ Tankan release-schedule page that confirms the date forward. Surface to SAM in case a closer-to-date check finds a different date. Non-blocking — directionally correct.
- **NEW (Run 5) — SAM-internal mechanical-trigger TSV-scope precedent decision:** SAM-21 pre-registered a Jun-9 Polymarket re-check trigger ("if ≥90% AND no Takaichi pushback → mechanical +5pp to 75%"). This is date-driven and operationally critical (next-session boot must surface it Jun 9), but it's NOT a public release/policy event — it's a SAM-internal review trigger. **KOYOMI declined to auto-add to CATALYSTS.tsv** (would set new precedent: TSV currently holds only public dated catalysts). **SAM decision needed:** (a) add to TSV as new "internal-trigger" category (precedent — would need 1-2 sibling rows for form-consistency, e.g. SAM-26 mechanism re-checks); (b) keep in STATUS only, accept boot-surface risk; (c) add to CALENDAR narrative only (no TSV row, but human-readable surface). If (a), KOYOMI will retroactively pull other SAM-internal triggers from THESIS/STATUS to populate. *Default if undecided by next run: option (c) — KOYOMI adds a CALENDAR narrative row but not a TSV row.*
- **NEW (Run 5) — MOF quarterly per-op intervention release date verification:** Per SAM PM session, MOF publishes per-op intervention breakdown quarterly at `mof.go.jp/english/policy/international_policy/reference/feio/quarterly/`. Apr-Jun 2026 ops breakdown should land ~early August (resolves ~¥1.95T residual classification — 70/30 slippage-vs-late-May-op prior). **Action next run:** fetch MOF feio/quarterly/ page, confirm convention (typical release day of month), add to TSV as 🟡 row with verified date. Watch-only — not urgent.

---

## STANDING MONITORS (surface each run)

- **BOJ pre-meeting blackout windows** (T-2 of each MPM) — currently kept as narrative in CALENDAR, not in TSV per form-consistency call from Jun 1. Revisit if SAM wants regime-boundary dates in TSV going forward (would need 1-2 other boundary rows added for consistency). *Jun-MPM blackout starts ~Jun 14 (T-2 of Jun 16).*
- **Recurring weekly catalysts** (CFTC release Fri/Mon) — not in TSV (handled by `cftc_jpy.py` auto-pull). Surface if cadence changes. **Jun 6 release: first scheduled amplifier/residual gate under new METHOD framing** — CALENDAR PHASE 2 WATCH note updated Run 5; SAM should watch the gate-test outcome.
- **Post-meeting catalyst-window refill** — after each major catalyst resolves, the forward horizon thins; pull next-month's events from RELEASES.md cadence rules.
- **MOF auction calendar alteration page** — `auction/calendar/26MMae.htm` (e.g., 2606ae.htm) records mid-month tenor-band changes. Check at month boundary; current Jun 2026 alteration was a liquidity-enhancement tenor-band tweak (15.5-39 vs 11-39, then back), no date moves.
- **SAM-internal review triggers (NEW Run 5):** SAM is increasingly pre-registering mechanical re-check triggers (Jun 9 Polymarket; SAM-26 mechanism re-test windows). Currently NONE in TSV; STATUS-only surface. Pending PENDING-item resolution on whether TSV scope extends to this class.

---

## NEXT RUN HINTS

- **Jun 4 onward:** May 28 Tokyo-CPI row turns 7d (eligible for prune Jun 4). May 29-31 rows roll into eligibility Jun 5-7. Sequence the prune pass cleanly.
- **Post-Jun-6 CFTC release:** first amplifier/residual gate-test under new METHOD framing. If CFTC prints stay shorter than -108K → 60% cycle-peak amplifier; if covers materially → residual gate. Update CALENDAR PHASE 2 WATCH outcome (narrative only — CFTC stays out of TSV).
- **Jun 9 SAM-21 Polymarket mechanical re-check (next session SAM should surface):** if SAM has decided on TSV-scope precedent for internal-trigger rows (see PENDING), apply on this run. Otherwise add CALENDAR narrative note (default-(c) from PENDING) so the trigger has a docket surface.
- **MOF feio/quarterly/ source check** — verify per-op intervention release date convention (target Apr-Jun 2026 ops breakdown, ~early August). Add as 🟡 TSV row once date pinned. URL: `mof.go.jp/english/policy/international_policy/reference/feio/quarterly/`.
- **Post-Jun-10 30Y auction:** backfill result to CALENDAR RECENTLY RESOLVED (workbook auto-fetches via `jgb_auctions.py`). Critical row — direct SAM-26 mechanism test.
- **Post-Jun-16 BOJ + Jun-17 FOMC resolution:** RECENTLY RESOLVED will fill heavily; prune pass + TIMELINE cross-check. Also expect TSV `Sato joins BOJ board` + `BOJ interim QT assessment` rows to resolve same day; mark and prune per >1wk rule.
- **Pull Aug auctions from MOF Aug calendar (auction/calendar/2608e.htm)** post-Jul-MPM to keep runway >30d. Also Shunto interim data (Aug, no firm date yet — RENGO cadence).
- **Pull MOF Aug alteration page** (`2608ae.htm` if it exists) to catch any post-budget tenor-band shifts.
- **Verify Tankan Q2 Jul 1 date** at BOJ Tankan release page once schedule posts (currently using cadence rule + March-2026 precedent).
- **If MOU walks back:** refresh INTERVENTION WATCH + Phase 2 Watch + GEOPOLITICAL WATCH tables; trigger likely auto-detected via STATUS Brent move. *(Brent now $97.70 — moving toward $100 trigger, not collapsing; MOU walk-back direction is opposite of expected.)*
- **PENDING coverage-policy decision:** if SAM has not weighed in on the "full MOF schedule vs cherry-pick" question, default to full schedule for Aug onwards (Run 4 set this default).
- **National May CPI Jun 19 (post-BOJ)** — high-information row; once resolved, weight National vs Tokyo in the prune note.
- **Baseline audit (BASELINE AUDIT in spec § 2a):** No fire this run (monthly trigger fired Run 4 Jun 2; next fire = first run of July).
