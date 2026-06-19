# KOYOMI MEMORY

State file for the docket-steward sub-agent. Spec is in [`KOYOMI.md`](KOYOMI.md) (durable). This file holds dated state: run history, pending items, standing monitors.

**Ownership:** KOYOMI writes this file directly at end-of-run (consistent with KOYOMI's other write privileges — full-edit mode by default, busy-work-only). SAM may pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** KOYOMI reads `KOYOMI.md` first (spec), then `KOYOMI_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last synced*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KOYOMI at run start: what's moved in STATUS / THESIS / TIMELINE / CHANGELOG since the previous sync. Cleared at end-of-run.*

*(cleared at end of Run 8 — see LAST RUN below)*

---

## LAST RUN

### Run 8 — 2026-06-19 (post-BOJ/FOMC/Iran-deal sync; sat-Jun-20 CFTC EV-gate flag + schema regression catch; Opus 4.7)

**Triggering context:** Heavy SAM session Wed Jun 17 - Thu Jun 18: FOMC RESOLVED hawkish (Warsh debut, +40bp 2026 median dot); Iran/US deal SIGNED Wed Jun 17 (electronic per Al Jazeera, NOT Geneva); Step 1.5 HAWK-reconcile pass applied across CALENDAR ~10 instances (commit `97701098`). v1.6 backbone DRAFT added CONVEXITY-TAIL SURVIVAL EV section (`f378c0e4`) — Sat Jun 20 CFTC release flagged as THE decision-grade observable. Japan May TB ✅ printed Tue Jun 17 PM ET (deficit ¥-378.7B, beat ~33%, branch-a substantively confirmed but exports doing heavy lifting).

**Sync verification (CALENDAR ↔ CATALYSTS):** 8 forward catalysts in TSV (Jun 19 → Jul 31). CALENDAR carries same set in EARLY-MID JUNE + EARLY JULY tables. Jun 17 FOMC + Jun 17 May TB present in TSV but already RESOLVED — should migrate to RECENTLY RESOLVED on next prune (they're row 4-5 of TSV, will look stale on countdown if kept). Jun 16 BOJ MPM + Jun 16 BOJ QT also resolved (rows 2-3) — same treatment.

**Overclaim residue check (Step 1.5 HAWK-reconcile):** Grep clean. "Switzerland/Geneva" — only in correction-context ("NOT a Geneva/Switzerland ceremony — sweep correction") at L51 + L104 of CALENDAR. No surviving "All 3 watch conditions met", "formally dormant", or "physically reopening." Step 1.5 sweep was thorough.

**🚨 CATALYSTS.tsv schema regression CAUGHT:** Header has 7 fields (`date event what_to_check threshold_signal priority who_cares notes`). Spec § "CATALYSTS.tsv format rules" requires **8 fields** with `type` column appended (added 2026-06-03 per Run 5). All 18 data rows are 7 fields. `catalyst_countdown.py` zips header→parts so `c.get("type", "")` always returns `""` → defaults to external rendering. **Side-effect:** sam-internal rows (when re-added) silently render without 🔧 prefix. Currently 0 sam-internal rows in forward TSV (both inaugural rows resolved Run 7), so no observable miscoloring TODAY — but the next sam-internal row added will tag without the 🔧. Likely cause: a hand-edit pass dropped the column at some point between Run 5 (Jun 3) and now. **Escalated to SAM (low-stakes structural — applied default would be to re-add the column with all rows = `external`; deferring to SAM because spec gates this).**

**🔴 Sat Jun 20 CFTC release MISSING from docket** — per v1.6 EV-table (THESIS commit `f378c0e4`), Jun 20 CFTC is THE decision-grade observable with pre-registered dispositions. Falls under TSV-SCOPE PRECEDENT (DATE-SPECIFIC + ACTION-FORCING) → qualifies as sam-internal row. Proposed rows below (under SAT JUN 20 CFTC ROW in return block).

**Pruning candidates (>1wk rule):**
- Sat Jun 6 CFTC — 13d old ✂️
- Mon Jun 8 Q1 GDP — 11d old ✂️
- Tue Jun 9 SAM-21 fire — 10d old ✂️
- Wed Jun 10 US CPI, JGB 30Y, Ueda hospitalized — 9d old ✂️
- Jun 10-11 US-Iran kinetic — 8d old ✂️
- Thu Jun 12 14-pt draft, Fri Jun 12 CFTC −145,818, Sun Jun 14 6-input re-mark + Brent breach — at 7d edge as of Jun 19 (eligible)
- Wed Jun 17 FOMC + Iran deal + Tue Jun 17 May TB — 2d old, retain (retrospective use through next week)

**Date verification for next 14d items (against THESIS/STATUS narrative — no source-fetch this run):**
- ✅ Fri Jun 19 National May CPI (today) — Stats Bureau cadence, consistent with STATUS treatment.
- ✅ Tue Jun 23 JGB 5Y — MOF Jun calendar confirmed Run 4.
- ✅ Thu Jun 25 JGB 20Y — MOF Jun calendar confirmed Run 4.
- ✅ Fri Jun 26 Tokyo June CPI — Stats Bureau cadence.
- ✅ Tue Jun 30 Sato seat-take + JGB 2Y — both BOJ + MOF confirmed Runs 4/6.
- ✅ Wed Jul 1 Tankan Q2 + Thu Jul 2 JGB 10Y — confirmed Run 4.

**Baseline audit:** No trigger fired this run. Monthly trigger fires first run of July (next sync). Post-miss: none. Note: this is the LAST KOYOMI run before the Jul baseline audit — recommend SAM allocate context for it next sync.

**Runway:** 42 days to furthest event (BOJ Jul 31). 5 events in next 14d (today's CPI + Jun 23/25/26/30 cluster). Healthy.

**Runtime:** ~6 min. (SAM-21 mechanical trigger fire-day sync + 3 resolved-row migrations + 3-row >1wk prune; Opus 4.7)

**Triggering context:** SAM-21 mechanical trigger pre-registered Jun 3 fired today (Tue Jun 9). Polymarket BOJ Jun 16 hike 98.2% (5th sequential ≥90% read; volume $403K up from $304K), no Takaichi pushback (Reuters explicitly noted), Q1 GDP revised +1.8% headline-soft / composition hike-tolerant. SAM-21 marked 70 → 75. STATUS, PREDICTIONS, TIMELINE all updated upstream. Brent breached $90 line 4th down session ($90.16 −4.34%). USDJPY 4th day above MOF #3 hard trigger (160.37).

**CHANGES SINCE LAST RUN (Jun 4 → Jun 9):** Polymarket 96.9 → 98.2 (continued grind, no retrace). USDJPY 159.92 → 160.37 (4th day above hard trigger; no MOF strike yet). Brent $96.78 → $90.16 (4th down session, −7% cum; broke $90 line). CFTC -114,667 → -129,567 (5th build week; METHOD residual-gate resolved AGAINST cover). Q1 GDP revised +1.8% from +2.1% prelim. Sato characterization expanded in TIMELINE (Apr-28 dissent bloc 3→2 framing strengthened).

> **⚠️ SAM CORRECTION (Jun 9 PM, OHLC-verified — applies to the two run-log paragraphs above; run-log preserved as written):** (1) USDJPY was NOT "4th day above hard trigger" — 2 distinct 160+ tags (Fri Jun 5 160.20 + Tue Jun 9 160.37) with a Mon dip below 160 between. (2) Brent did NOT break the $90 line on a "4th down session / −7% cum" — Tue tagged $89.59 intraday (~12 PM ET) but recovered to $92.40 by evening (no closing breach); Mon Jun 8 closed UP +1.2% ($94.25), so sessions ran Thu-Fri down / Mon up / Tue down; cum from $96.78 = −4.5%. CALENDAR stamp + Phase 2 Watch row corrected by SAM Jun 9 PM (commit `cd9f23cd`). Next KOYOMI run: treat the evening-pass STATUS/CALENDAR language as current.

**Structural housekeeping applied (low-stakes per [[finding_subagent_escalation_mode_discriminator]]):**
- **CATALYSTS.tsv:** Removed 3 resolved rows: Jun 6 CFTC residual-gate (sam-internal), Jun 8 Q1 GDP, Jun 9 SAM-21 mechanical trigger (sam-internal). Per spec § 1 — forward views shed events as date passes. catalyst_countdown.py runs clean post-edit (verified — Jun 10 US CPI now leads imminent).
- **CALENDAR.md EARLY-MID JUNE table:** Removed same 3 rows (Jun 6 / Jun 8 / Jun 9). First forward row is now Jun 10 US CPI.
- **CALENDAR.md ✅ RECENTLY RESOLVED:** Added Jun 6 CFTC outcome (gate against cover; 5th build week; amplifier+residual stay ON), Jun 8 GDP outcome (+1.8% headline-soft / composition hike-tolerant), Jun 9 SAM-21 outcome (70→75 mechanical fire; Polymarket 98.2%; no Takaichi pushback; first real-time KB-185 application).
- **CALENDAR.md prune (>1wk rule):** Removed Fri May 29 April activity data (11d), Sat May 30 CFTC -114,667 (10d), Sun May 31 market reprice (9d). All narrative lives in TIMELINE. Jun 2 retained (7d edge — keep one more run to give Jun 16 retrospective).
- **CALENDAR header:** Last Updated → 2026-06-09 Run 7 with summary.

**Pre-fire-week cadence-derived date verification (per [[finding_subagent_pre_fire_date_verification]]):**
- ✅ **Jun 10 JGB 30Y auction** — RELEASES.md "Confirmed dates" CONFIRMED at MOF Jun calendar Jun 2 2026. No change.
- ✅ **Jun 16 BOJ MPM** — RELEASES.md CONFIRMED at BOJ schedule Jun 2 2026. No change.
- ⚠️ **Jun 10 US CPI** — NOT in RELEASES.md "Confirmed dates" table. Cadence rule says monthly mid-month BLS; STATUS treats Jun 10 as consensus. WebFetch BLS schedule page returned 403 Forbidden — primary-source verification not achievable this run. Date directionally consistent with cadence (mid-month Wed BLS) + universally-cited in financial press. **No change applied. Logged to NEXT RUN HINTS for manual BLS verify.**
- ✅ **Sat Jun 13 CFTC** — weekly Friday cadence; CFTC standing monitor. No TSV row (excluded class per spec); STATUS/CALENDAR PHASE 2 WATCH carries narrative.

**Baseline audit:** No trigger fired this run. Monthly trigger fired Run 4 (Jun 2, first run of June); next monthly fire = first run of July (~Jul 1). Post-miss: none flagged.

**RELEASES.md ✏️ no additions** — no source-fetched dates this run (Jun 10 US CPI WebFetch blocked; rows would have been added had it returned). Schema didn't need extension (Sato Jun 30 board-composition addition flagged in Run 6 PENDING remains SAM-judgment).

**Runway:** 52 days to furthest event (BOJ Jul 31). 11 events in next 14d (Jun 10 US CPI + JGB 30Y → Jun 16 BOJ + QT → Jun 17 FOMC → Jun 18 May TB → Jun 19 National CPI → Jun 23 JGB 5Y → Jun 25 JGB 20Y → Jun 26 Tokyo CPI → Jun 30 Sato + JGB 2Y). High-traffic 7-9d window.

**Runtime:** ~5 min. catalyst_countdown.py runs clean post-edits.

### Run 6 — 2026-06-04 (🚨 Sato primary-source verification + TSV chronological re-sort + May 28 prune; Opus 4.7)

**Will-flagged load-bearing task: primary-source verify Sato claims propagated into docket Jun 4 AM (commit `079e46ca`) without source verification. Two-part: (1) DATE — Jun 30 vs Jun 16 (load-bearing — does Sato vote at Jun-16 MPM?); (2) CHARACTERIZATION — 4 sub-claims (name, affiliation, ideology, political alignment).**

**Verification results — ALL CLEAR, no quarantine needed:**
- ✅ **DATE — BOJ official:** Junko Nakagawa's term stated verbatim at `boj.or.jp/en/about/organization/policyboard/bm_nakagawa.htm` as "from June 30, 2021 to June 29, 2026." Successor takes seat Jun 30 2026. **Jun 30 date stands. Sato does NOT vote at Jun-16 MPM.** This is the load-bearing fact. CATALYSTS row 8 + CALENDAR L28 + STATUS BOJ-ASSESSMENT + THESIS L182/L213 all correct.
- ✅ **"Ayano Sato"** — full name confirmed in Japan Times (`japantimes.co.jp/business/2026/02/25/economy/new-boj-board-members/`), Nikkei Asia, MarketScreener, Bloomberg.
- ✅ **"Aoyama Gakuin University law professor"** — confirmed via Aoyama Gakuin official researcher profile (`raweb1.jm.aoyama.ac.jp/aguhp/KgApp/k03/resid/S000855?lang=en`): Faculty of Law, Department of Human Rights, Professor. The Feb-25 Bloomberg/Japan Times nomination piece described her as "professor at Aoyama Gakuin University" without specifying field; the law-faculty specificity is confirmed at the AGU primary source.
- ✅ **"reflationist"** — explicitly stated in Japan Times Mar 19 piece ("Lower House OKs two reflationists as BOJ policymakers"), Bloomberg ("Takaichi's reflationist picks"), Nippon.com ("2 Reflationists Tapped"). Cross-source primary tier.
- ✅ **"Takaichi appointee"** — confirmed across all sources; cabinet nomination + Diet confirmation track verified.

**Structural fixes applied (low-risk per autonomy gradient):**
- **CATALYSTS.tsv chronological re-sort:** Jun-09 SAM-21 row was at row 6 (after Jun-10 rows); Jun-30 Sato row was at row 8 (between Jun-16 BOJ MPM + Jun-16 BOJ QT). Stable sort by date column preserves intra-day pairings (BOJ MPM before BOJ QT, US CPI before JGB 30Y, Sato before JGB 2Y on Jun-30). Spec compliance: "Keep file date-sorted." Verified `catalyst_countdown.py` parses clean post-sort.
- **CALENDAR.md May 28 prune:** Thu May 28 Tokyo CPI 7d old today (Jun 4), eligible per >1wk rule. Removed from RECENTLY RESOLVED. May 29 (6d) / May 30 (5d) / May 31 (4d) / Jun 2 (2d) retained. Updated pruning note from prior Jun 2 prune to Jun 4 prune.
- **CALENDAR.md header refresh:** "Last Updated" → 2026-06-04 (Run 6 — verification + sort + prune).

**Side-effect check (Will-flagged Item D — OS.1 closure dependency):** OS.1 close in MEMORY referenced "Sato characterization strengthens v1.5.1 path-MEDIUM conviction." All 4 characterization sub-claims now primary-source verified — OS.1 closure stands without caveat. No escalation to SAM needed on this leg.

**Pruning (>1wk rule):** Pruned May 28 (7d). May 29-31 + Jun 2 retained. Next eligibility: May 29 turns 7d Jun 5.
**Baseline audit:** No trigger fired this run. Monthly trigger fired Run 4 (Jun 2); next fire = first run of July. Per [[finding_subagent_baseline_audit]].
**Runway:** 57 days to furthest event (BOJ Jul 31). 6 events in next 14d (Jun 6 CFTC, Jun 8 GDP, Jun 9 SAM-21, Jun 10 US CPI + JGB 30Y, Jun 16 BOJ + QT, Jun 17 FOMC, Jun 18 TB — high-traffic window in 12-13d).
**Runtime:** ~6 min. catalyst_countdown.py runs clean post-edits.

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

- **Phase 2 Watch section reframe** may be needed if MOU walks back this week (Trump-Khamenei reset → Brent collapse → Phase 2 re-engages). Pre-emptive flag from Run 3 escalation #2. SAM-domain trigger. *(Still pending Jun 4; no MOU walk-back observed through Run 6; per session context Brent had 2nd down session Jun 3-4 but still elevated — not collapse-direction yet. Watch.)*
- **Jul Tankan Q2 date (Jul 1)** — used cadence rule (1st business day of July; March Tankan released Apr 1 2026); could not find an explicit BOJ Tankan release-schedule page that confirms the date forward. Surface to SAM in case a closer-to-date check finds a different date. Non-blocking — directionally correct.
- **NEW (Run 5) — SAM-internal mechanical-trigger TSV-scope precedent decision:** SAM-21 pre-registered a Jun-9 Polymarket re-check trigger ("if ≥90% AND no Takaichi pushback → mechanical +5pp to 75%"). This is date-driven and operationally critical (next-session boot must surface it Jun 9), but it's NOT a public release/policy event — it's a SAM-internal review trigger. **KOYOMI declined to auto-add to CATALYSTS.tsv** (would set new precedent: TSV currently holds only public dated catalysts). **SAM decision needed:** (a) add to TSV as new "internal-trigger" category (precedent — would need 1-2 sibling rows for form-consistency, e.g. SAM-26 mechanism re-checks); (b) keep in STATUS only, accept boot-surface risk; (c) add to CALENDAR narrative only (no TSV row, but human-readable surface). If (a), KOYOMI will retroactively pull other SAM-internal triggers from THESIS/STATUS to populate. *Default if undecided by next run: option (c) — KOYOMI adds a CALENDAR narrative row but not a TSV row.*
- **NEW (Run 5) — MOF quarterly per-op intervention release date verification:** Per SAM PM session, MOF publishes per-op intervention breakdown quarterly at `mof.go.jp/english/policy/international_policy/reference/feio/quarterly/`. Apr-Jun 2026 ops breakdown should land ~early August (resolves ~¥1.95T residual classification — 70/30 slippage-vs-late-May-op prior). **Action next run:** fetch MOF feio/quarterly/ page, confirm convention (typical release day of month), add to TSV as 🟡 row with verified date. Watch-only — not urgent.
- **NEW (Run 6, INFORMATIONAL — for SAM audit / clearable on next ack) — Sato verification provenance recorded:** All 5 claims (date + 4 characterization sub-claims) primary-source verified Jun 4. Sources: BOJ official Nakagawa page (date); Aoyama Gakuin researcher profile (law professor); Japan Times Feb 25 + Mar 19, Bloomberg Feb 24/25, Nikkei Asia, Nippon.com (reflationist + Takaichi pick). RELEASES.md "Confirmed dates" table NOT extended (RELEASES is recurring-cadence; one-off board-composition events don't fit its schema — flagging for SAM in case a board-composition section would help). No quarantine flags applied. OS.1 closure dependency (Will Item D) — clear, no caveat.
- **NEW (Run 8, 🚨 LOAD-BEARING) — CATALYSTS.tsv `type` column schema regression:** Header is 7 fields, spec requires 8 with `type` appended (added 2026-06-03 per Run 5). All 18 rows are 7 fields. `catalyst_countdown.py` zips header→parts so `type` defaults to "" → external rendering. Currently 0 sam-internal rows so no observable miscoloring, but next sam-internal addition will tag WITHOUT 🔧. **SAM-DECISION needed:** restore header to 8 fields + backfill all rows with `external` (or appropriate tag). Low-stakes structural; KOYOMI declined to apply the column restoration without SAM confirmation because: (a) it's a write to an SoT file affecting parser behavior; (b) two SAM-internal rows resolved Run 7 had `type=sam-internal` per Run 5 spec — confirming whether THOSE were also missing the column historically OR whether the column was dropped post-Run-7 changes the response. Action: SAM verify, then either ack restoration or apply directly.
- **NEW (Run 8) — Sat Jun 20 CFTC release docket entry:** Per v1.6 EV-table (THESIS commit `f378c0e4`), Jun 20 CFTC is THE decision-grade observable with pre-registered dispositions. Meets TSV-SCOPE PRECEDENT (DATE-SPECIFIC + ACTION-FORCING). Proposed rows in return block under SAT JUN 20 CFTC ROW. **SAM apply.**
- **NEW (Run 8) — Resolved-event TSV migration:** Rows 2-5 of TSV (Jun 16 BOJ MPM, Jun 16 BOJ QT, Jun 17 FOMC, Jun 17 May TB) all resolved but still in forward TSV. countdown.py filters by date < today so they're not surfaced; if KOYOMI prunes per spec § 1 "forward views shed events as date passes," all 4 should be removed. Per spec: forward views = TSV; the 1-week retention is CALENDAR's RECENTLY RESOLVED. **SAM apply when applying CFTC row.**
- **NEW (Run 7) — Jun 10 US CPI primary-source verification PENDING:** Per [[finding_subagent_pre_fire_date_verification]] cadence-derived rows within 7d of fire should be source-verified. Jun 10 fire date is +1d. BLS schedule page (`bls.gov/schedule/news_release/cpi.htm`) returned HTTP 403 to WebFetch this run. Date directionally consistent with monthly mid-month BLS cadence + universally cited in financial press; high confidence but not primary-source confirmed. **Action next run:** retry BLS fetch (try with WebSearch alternative, or check BLS archive) once date is in past, append to RELEASES.md "Confirmed dates" as RETROSPECTIVE-CONFIRMED. Low risk — date almost certain — but adds a gap to verification provenance.

---

## STANDING MONITORS (surface each run)

- **BOJ pre-meeting blackout windows** (T-2 of each MPM) — currently kept as narrative in CALENDAR, not in TSV per form-consistency call from Jun 1. Revisit if SAM wants regime-boundary dates in TSV going forward (would need 1-2 other boundary rows added for consistency). *Jun-MPM blackout starts ~Jun 14 (T-2 of Jun 16).*
- **Recurring weekly catalysts** (CFTC release Fri/Mon) — not in TSV (handled by `cftc_jpy.py` auto-pull). Surface if cadence changes. **Jun 6 release resolved AGAINST cover** (5th build week, -129,567 = 72.0% cycle peak; METHOD amplifier+residual stay ON; per Run 7 RECENTLY RESOLVED). **Next release Sat Jun 13** — LAST pre-blackout CFTC read (Jun 16 BOJ T-2 blackout starts ~Jun 14). Watch for: (a) cover below -108K → amplifier OFF (low prob given 5-week trajectory); (b) build through -153K (85% line) → amplifier escalates to +8-10pp.
- **Post-meeting catalyst-window refill** — after each major catalyst resolves, the forward horizon thins; pull next-month's events from RELEASES.md cadence rules.
- **MOF auction calendar alteration page** — `auction/calendar/26MMae.htm` (e.g., 2606ae.htm) records mid-month tenor-band changes. Check at month boundary; current Jun 2026 alteration was a liquidity-enhancement tenor-band tweak (15.5-39 vs 11-39, then back), no date moves.
- **SAM-internal review triggers (Run 5; resolved Jun 3 by Will, scope precedent now in KOYOMI.md):** TSV-scope extended to admit SAM-internal mechanical decision gates (`type=sam-internal`). **Both inaugural rows resolved Run 7 (Jun 6 CFTC + Jun 9 SAM-21 Polymarket); zero sam-internal rows currently in forward TSV.** Watch for additional candidates as SAM pre-registers more triggers (must meet DATE-SPECIFIC + ACTION-FORCING gates per precedent). Likely next candidate: post-BOJ Jun 16 SAM-21/SAM-23 re-evaluation cadence, if SAM pre-registers a dated mechanical gate.
- **BOJ board composition transitions (Run 6, new):** Sato Jun 30 row is the first board-composition transition in current docket window. Future class: term-expiries of other Policy Board members + corresponding successor seat-dates. RELEASES.md schema currently doesn't cover board-composition events (only recurring-cadence releases). Flag for SAM whether to extend RELEASES.md with a "Board composition transitions" section, or keep ad-hoc-with-verification-on-each-add. Next probable composition event: TBD (other Policy Board terms expire various 2026-2030 — would need separate baseline against BOJ page).

---

## NEXT RUN HINTS

- **🆕 Run 8 outputs awaiting SAM apply:** (1) schema-regression `type` column restore + backfill; (2) Sat Jun 20 CFTC row add (CALENDAR + CATALYSTS); (3) resolved-event TSV migration (rows 2-5 → drop). If SAM applied between Run 8 → Run 9, verify state in PENDING.
- **🆕 First run of July triggers MONTHLY BASELINE AUDIT** (per spec § 2a; last fired Run 4 Jun 2). Audit MOF Jul + Aug calendars, BOJ Aug schedule, Stats Bureau Jul releases, BLS Jul CPI, ESRI Q2 GDP (Aug). Block ~10-12 min context budget.
- **🆕 Likely v1.6 will pre-register new sam-internal mechanical triggers** — if so, apply TSV-SCOPE PRECEDENT inclusion bar without re-escalating. Pre-condition: `type` column must be restored first or the 🔧 tag won't render.
- **🆕 SAM Jun 10 PM docket correction (informational — already applied, verify don't redo):** May TB provisional = **Jun 17 08:50 JST** (was docketed Jun 18; June TB = Jul 22 not "~Jul 16-17"). Pinned from **MOF Customs release calendar `customs.go.jp/toukei/calendar/calend_e.htm`** — ADD THIS to your date-pinning source list alongside the MOF auction calendar; trade-stat dates come from Customs (customs.go.jp), NOT mof.go.jp. CATALYSTS.tsv + CALENDAR rows corrected by SAM. New auto-pull: `trade_balance_japan.py` (boot-wired) consumes the TB rows; keep "trade balance" in the event name. Detailed-stage release Jun 26 — NOT a separate TSV row (stage revision, not a new catalyst); script picks it up automatically.
- **Jun 10 onward prune cadence:** Jun 2 JGB 10Y turns 7d Jun 9 (kept this run — single edge row, retrospective use for Jun 16 imminent); turns 8d Jun 10 → pruneable next run. Jun 6 CFTC turns 7d Jun 13. Jun 8 GDP turns 7d Jun 15. Jun 9 SAM-21 turns 7d Jun 16 (BOJ-day — likely batched-prune with BOJ outcome row).
- **Sat Jun 13 CFTC release** — LAST pre-blackout read. cftc_jpy.py auto-pulls Sat AM. Update CALENDAR PHASE 2 WATCH narrative outcome. NOT a TSV row (excluded class); STATUS owns the live read.
- **Wed Jun 10 US CPI primary-source verify** — retry once date is in past (BLS schedule page returned 403 this run). Append to RELEASES.md "Confirmed dates" as RETROSPECTIVE-CONFIRMED with BLS source URL once accessible.
- **Post-Jun-10 30Y auction:** backfill result to CALENDAR RECENTLY RESOLVED (workbook auto-fetches via `jgb_auctions.py`). Critical row — direct SAM-26 mechanism test.
- **Post-Jun-16 BOJ + Jun-17 FOMC resolution:** RECENTLY RESOLVED will fill heavily; prune pass + TIMELINE cross-check. Also expect Jun 16 BOJ interim QT assessment + Jun 30 Sato seat-take rows to resolve in sequence; mark and prune per >1wk rule.
- **MOF feio/quarterly/ source check** — verify per-op intervention release date convention (target Apr-Jun 2026 ops breakdown, ~early August). Add as 🟡 TSV row once date pinned. URL: `mof.go.jp/english/policy/international_policy/reference/feio/quarterly/`.
- **Pull Aug auctions from MOF Aug calendar (auction/calendar/2608e.htm)** post-Jul-MPM to keep runway >30d. Also Shunto interim data (Aug, no firm date yet — RENGO cadence).
- **Pull MOF Aug alteration page** (`2608ae.htm` if it exists) to catch any post-budget tenor-band shifts.
- **Verify Tankan Q2 Jul 1 date** at BOJ Tankan release page once schedule posts (currently using cadence rule + March-2026 precedent).
- **If MOU walks back / Brent re-rallies:** refresh INTERVENTION WATCH + Phase 2 Watch + GEOPOLITICAL WATCH tables; trigger auto-detected via STATUS Brent move. *(Corrected Jun 9 PM: Brent $92.40 — choppy down-drift, NOT a held $90 breach; tagged $89.59 intraday Tue but recovered same day; Mon was an up session. Direction easing, not collapsing; no closing breach of $90.)*
- **PENDING coverage-policy decision:** if SAM has not weighed in on the "full MOF schedule vs cherry-pick" question, default to full schedule for Aug onwards (Run 4 set this default).
- **National May CPI Jun 19 (post-BOJ)** — high-information row; once resolved, weight National vs Tokyo in the prune note.
- **Watch for new sam-internal trigger pre-registrations** — both inaugural sam-internal rows resolved Run 7. Forward TSV currently has 0 sam-internal rows. Next likely candidate: post-BOJ Jun 16 SAM-21/SAM-23 re-evaluation cadence, if SAM pre-registers a dated mechanical gate. Apply TSV-SCOPE PRECEDENT inclusion bar (DATE-SPECIFIC + ACTION-FORCING) without re-escalating.
- **Baseline audit (BASELINE AUDIT in spec § 2a):** No fire this run (monthly trigger fired Run 4 Jun 2; next fire = first run of July, ~Jul 1).
