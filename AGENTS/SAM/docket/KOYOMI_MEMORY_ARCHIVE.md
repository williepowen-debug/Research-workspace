# KOYOMI_MEMORY — ARCHIVE

> **Reference only. NOT read at boot.** Terminal run-history rolled out of `KOYOMI_MEMORY.md` so the live file stays a working set rather than a ledger.
> **Nothing here was deleted — every block is verbatim.** A block reaches this file only when it carries an explicit closure marker; unmarked blocks stay live by rule, because silence is never read as closure.
> Rolled by `scripts/subagent_memory_roll.py`.

---

### Run 11 — 2026-07-02 (first run of July → 🔍 MONTHLY BASELINE AUDIT fired; Jul-1/2 resolved-row migration; mid/late-June forward-table cleanup; ambush-regime framing refresh; Fable 5)

**Triggering context:** see CHANGES SINCE above (v1.6.3 / SAM-32 FALSE / NO-STRIKE adjudication / NFP miss / CFTC re-date — SAM's same-day inline docket edits treated as current-and-correct inputs, per spawn instruction).

**Resolved-row migration (spec §1):**
- **CATALYSTS.tsv:** removed Jul-1 Tankan + Jul-2 JGB 10Y rows (resolved; results logged in RECENTLY RESOLVED/STATUS/TIMELINE). Forward TSV now leads with Jul-6 CFTC (sam-internal). 9 forward events, 8 fields each; countdown + 🔧 rendering verified clean; jgb_auctions.py token filter intact.
- **CALENDAR.md:** removed the two ✅ rows from EARLY JULY (both duplicated verbatim in RECENTLY RESOLVED). **Also removed the stale mid/late-June resolved forward tables** — LATE JUNE (Jun-30 2Y ✅, duplicated in RECENTLY RESOLVED) + MID-JUNE (Jun-16 BOJ 16d / Jun-17 FOMC 15d / Jun-16-17 QT passed / Jun-30 Sato duplicated). Narrative verified preserved: STATUS § BOJ/§ FOMC pointers + TIMELINE Jun-16 / Jun-17-20 / Jun-22-Jul-2 blocks; FY2027 purchase-plan thread carries on the Jul-31 BOJ row. Left a one-line pruned-note pointer above the EARLY JULY table.

**Pruned (>7d rule, RECENTLY RESOLVED):** Jun 23-26 cluster (6-9d; prune pre-authorized by Run-10 NEXT RUN HINTS). Retained: Jun-30 Sato + 2Y (2d; eligible Jul 7), Jul-1 Tankan, Jul-2 10Y + NFP/MOF-verify rows. Prune note updated.

**Framing refresh (task 3 — matched to STATUS 7/2 view):**
- **INTERVENTION WATCH:** header + row 1 → 7/2 ambush-regime framing (MOF silent 16d / NO-STRIKE adjudication / line re-anchored 160→162 / rate-check-absence-uninformative per playbook S1-A; dropped the stale "SAM-23 ~30%" mark — SAM-23 resolved FALSE — in favor of "MOF #3 DECAYING ~15-20%/30d"). Brent row: dropped stale "Hormuz physically closed Day 105" → reopening-begun/dormant. Jun-17 deal row compressed to a pointer (full narrative duplicated in GEOPOLITICAL WATCH + TIMELINE). Bessent/Katayama row: stale "blackout ACTIVE" (Jun-16 vintage) → next blackout ~Jul 29; refreshed to the 7/1-7/2 jawbone tier.
- **PHASE 2 WATCH:** header stale "v1.6 relabel pending" → v1.6-finalized/dormant/decoupling-SHRUG. CFTC row: stale "next print Fri Jun 26" → **Mon Jul 6**; stale "No cover" → Jun-23 first-cover-off-the-top (still HOLD band); resolved EV-gate detail compressed. Brent + MOU rows: Jun-22 decoupling test marked resolved SHRUG; stale Day-105/Day-110 claims dropped.
- **Header housekeeping (ESCALATION-LOG, low-stakes structural default):** compressed the pre-Jun-30 "Last Updated" history tail (Jun-14→Jun-22 passes) to a one-line pointer (git history + these run logs). Veto-able.
- **TSV true-up:** Jul-31 BOJ threshold_signal "(if delivered)" → "(delivered, as-priced)" + SAM-34 hold@85% framing (matches CALENDAR).

**SAM-edit reconciliation (spawn task):** Jul-6 CFTC + ~Jul-31 MOF monthly rows verified present + consistent in BOTH files (dates/priority/who_cares/type=sam-internal); Jul-7/Jul-22 bid-real re-frames + BOND in who_cares consistent in both; Jul-2 10Y resolution consistent. **Zero residual mismatches found** beyond the stale "(if delivered)" fixed above.

**🔍 BASELINE AUDIT (monthly trigger — first run of July; last fired Run 4 Jun-2):** CALIBRATION declined-classes checked first (section absent → none declined). Sources fetched: MOF Jul (2607e.htm — **all 5 remaining July auctions verify exactly** vs TSV) + Aug (2608e.htm) calendars; alteration pages 2607ae/2608ae **404 = none exist**; BOJ MPM schedule (**no August MPM** — next Sep 17-18, decision Sep 18, no Outlook; SoO for Jul MPM shown "Aug 8" by fetch — ⚠️ that's a Saturday, suspect summarization, verify before use; SoO not in audit universe anyway); Fed calendar (**no August FOMC** — next Sep 15-16, SEP); Stats Bureau 1582.html (full table parsed raw — National Jun CPI Jul-24 / Tokyo Jul CPI Jul-31 / **National Jul CPI Aug-21 = FIRST 2025-base release** / Tokyo Aug CPI Aug-28); BLS CPI schedule (curl + User-Agent beats the 403: Jul-14 + Aug-12; Jun-10 retro-confirmed → Run-7 backlog cleared); ESRI (Q2 GDP 1st prelim **Mon Aug-17** 8:50 JST; 2nd prelim Sep-8); Japan Customs calendar (Jun TB provisional **Jul-22**; Jul TB **Aug-20**). **DELTA: 14 proposed rows (4 July + 10 August) — written to ## PENDING below, propose-only, NOT added to TSV.** Out-of-universe observations: Aug-12 10Y JGBi + Aug-24 Climate Transition Bond auctions (not in the 2Y/5Y/10Y/20Y/30Y/40Y universe — flag only); no 40Y auction in August. All 14 proposal dates + the Sep pre-confirms appended to RELEASES.md Confirmed dates (20 rows) per audit step 6.

**Runway:** 29d to furthest TSV event (Jul-31 BOJ + MOF monthly). 3 events next 7d (Jul-6 CFTC, Jul-7 30Y, Jul-9 5Y). Healthy now, but the TSV goes DARK after Jul-31 — applying the August delta extends runway to Aug-28.

**Runtime:** ~14 min (audit-heavy). Did NOT commit/push — left for SAM.

### Run 9 — 2026-06-22 (post-BOJ/FOMC/Iran-deal-signed cleanup sync; >7d cluster prune + resolved-row migration + PHASE 2 CFTC live-strip; Opus 4.8)

**Triggering context (CHANGES SINCE Run 8 Jun 19 → Jun 22):** Run-8 SAM-apply landed — CATALYSTS.tsv schema fix (7→8 fields, `type` column restored, 18 rows backfilled `external`); Sat Jun 20 CFTC EV-gate row added (then **date-corrected Sat Jun 20 → Mon Jun 22**: Fri Jun 19 Juneteenth holiday delays the COT release). Two market events since: (1) **Sat Jun 20 Iran RE-DECLARED Hormuz CLOSED + Lebanon re-heat** (declaratory; CENTCOM-disputed; cross-agent BRENT v4.1 / HAWK B34/C44/D22) → logged to GEOPOLITICAL + PHASE 2 watch by SAM, **NO SAM re-mark** (declaratory ≠ physical); (2) **Mon Jun 22 Brent decoupling test RESOLVED = SHRUG** — declaratory re-closure produced NO Brent spike (Brent $77.84, −2.5% day, ~−20% cum) → oil-in-yen channel stays dormant, thesis holds. **Jun-24 BOJ Summary of Opinions** added to docket by SAM Jun-21 (verified at BOJ source). National May CPI resolved Jun 19 (headline 1.5 / core 1.4 / core-core 1.8, soft underlying). v1.6 still pending the Mon Jun 22 3:30 PM ET CFTC Jun-16 print + RED pass. USDJPY 161.54 (MOF silent 6 days at 160+, no 3rd strike; ~0.4y below 161.96 record).

**Pruned (>7d rule, RECENTLY RESOLVED cluster — lead-vetted prune-eligible):** Thu Jun 12 14-pt draft (10d), Sun Jun 14 6-input re-mark (8d), Sun Jun 14 Brent sub-$90 breach (8d). Cross-checked: BOJ/kinetic/CPI narrative in TIMELINE; Jun-14 re-mark + Brent breach narrative preserved in STATUS (CARRY UNWIND / INTERVENTION STATUS sections) + CHANGELOG.
**🔒 RETAINED past >7d by SAM directive:** Fri Jun 12 CFTC −145,818 — the pre-catalyst peak-fuel read load-bearing for the pending v1.6 EV-table. SAM clears after v1.6 finalize. (<7d, retained normally: Jun 17 FOMC / Iran-deal / May-TB.)

**Resolved-row migration (spec §1 — forward views shed passed events):**
- **CATALYSTS.tsv:** removed resolved Jun-19 National May CPI row (Jun 19 < today). Forward feed now leads with Jun-22 CFTC. (Run-8's rows 2-5 Jun-16/17 already migrated by SAM.)
- **CALENDAR.md:** removed resolved **Jun-17 May-TB** + **Jun-19 National-CPI** rows from the forward "EARLY-MID JUNE" table; renamed that section header **EARLY-MID JUNE → LATE JUNE — POST-BOJ INTERVENING DATA** (remaining rows now Jun 22-30). Added **Jun-19 National May CPI** to RECENTLY RESOLVED (resolved, <7d, retain). Jun-17 May-TB was already in RECENTLY RESOLVED — just dropped the forward duplicate.

**Live-spot strip + framing refresh (TRUTH MODEL / task 3):** PHASE 2 WATCH CFTC row — stripped the stale pre-Jun-16 live level (**−145,818 / 81% / "7,182 shy of −153K"**) → kept thresholds only (−75K / −108K / −153K), pointed live net → STATUS, and refreshed the stale "fuel maximally loaded into Tue Jun 16 binary" framing → post-event view ("BOJ Jun-16 binary resolved as-priced; the Jun-16 CFTC data releasing 3:30 PM ET Mon Jun 22 is the v1.6 EV-gate observable"). No other live spot found in forward rows (SAM's Jun 18-20 sweeps left forward framing current — post-hike 1.00% / post-FOMC-Warsh / Iran-deal-signed / oil-in-yen-dormant all present).

**Sync verification (CALENDAR ↔ CATALYSTS):** 16 forward catalysts in TSV (Jun 22 → Jul 31); CALENDAR carries the same set across LATE JUNE + the BOJ-RESOLVED table (Sato Jun 30) + EARLY JULY tables. Full July JGB string present + consistent (Jul 2 10Y / Jul 7 30Y / Jul 9 5Y / Jul 14 20Y / Jul 22 40Y / Jul 30 2Y), BOJ Jul 31, Tankan Jul 1, FOMC Jul 29, Jun-24 SoO, Jun 23 5Y, Jun 25 20Y, Jun 26 Tokyo CPI, Jun 30 Sato+2Y — all present in both. catalyst_countdown.py runs clean post-edits; 🔧 prefix renders on the CFTC sam-internal row (schema fix intact).

**Baseline audit:** No trigger fired this run (not the first run of July; no SAM post-miss flag). "no audit trigger this run." **Monthly trigger fires first run of July (next sync) — block ~10-12 min for the MOF Jul+Aug / BOJ Aug / Stats-Bureau Jul / BLS Jul / ESRI Q2-GDP audit.** This is the last KOYOMI run before that.

**Runway:** 39 days to furthest event (BOJ Jul 31). ~9 events in next 14d (Jun 22 CFTC + Jun 23/24/25/26 + Jun 30 ×2 + Jul 1/2). Healthy.

**Runtime:** ~7 min. RELEASES.md ✏️ no additions (no source-fetched dates this run — all forward dates previously confirmed Runs 4/6/8). Did NOT commit/push — left for SAM.

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

**Pre-fire-week cadence-derived date verification (per [[finding_subagent_prefire_date_verification]]):**
- ✅ **Jun 10 JGB 30Y auction** — RELEASES.md "Confirmed dates" CONFIRMED at MOF Jun calendar Jun 2 2026. No change.
- ✅ **Jun 16 BOJ MPM** — RELEASES.md CONFIRMED at BOJ schedule Jun 2 2026. No change.
- ⚠️ **Jun 10 US CPI** — NOT in RELEASES.md "Confirmed dates" table. Cadence rule says monthly mid-month BLS; STATUS treats Jun 10 as consensus. WebFetch BLS schedule page returned 403 Forbidden — primary-source verification not achievable this run. Date directionally consistent with cadence (mid-month Wed BLS) + universally-cited in financial press. **No change applied. Logged to NEXT RUN HINTS for manual BLS verify.**
- ✅ **Sat Jun 13 CFTC** — weekly Friday cadence; CFTC standing monitor. No TSV row (excluded class per spec); STATUS/CALENDAR PHASE 2 WATCH carries narrative.

**Baseline audit:** No trigger fired this run. Monthly trigger fired Run 4 (Jun 2, first run of June); next monthly fire = first run of July (~Jul 1). Post-miss: none flagged.

**RELEASES.md ✏️ no additions** — no source-fetched dates this run (Jun 10 US CPI WebFetch blocked; rows would have been added had it returned). Schema didn't need extension (Sato Jun 30 board-composition addition flagged in Run 6 PENDING remains SAM-judgment).

**Runway:** 52 days to furthest event (BOJ Jul 31). 11 events in next 14d (Jun 10 US CPI + JGB 30Y → Jun 16 BOJ + QT → Jun 17 FOMC → Jun 18 May TB → Jun 19 National CPI → Jun 23 JGB 5Y → Jun 25 JGB 20Y → Jun 26 Tokyo CPI → Jun 30 Sato + JGB 2Y). High-traffic 7-9d window.

**Runtime:** ~5 min. catalyst_countdown.py runs clean post-edits.


### Run 16 — 2026-08-17 (verify SAM's same-day inline boot sync + repair 3 sibling misses + delete a stale restated BOJ% + >7d prune + closed the long-open MOF feio/quarterly date-pin PENDING item; no baseline-audit trigger)

**Triggering context:** see CHANGES SINCE above. SAM ran its own inline docket sync earlier today (commit `b41406264`); this run's job was explicitly to verify that pass and finish what it did not cover, not redo it.

**1 — Sibling misses found + repaired (spec §1/§3, the run's main find):**
- **Aug-6 BOJ current-account `jd20260804.xlsx` row: CALENDAR's forward-table copy had been rewritten correctly (RESOLVED 2026-08-14, retraction of the "dead archive" claim, all 3 ladder legs FINAL) but the `CATALYSTS.tsv` mirror row still carried the ORIGINAL stale notes** — "STILL 404... ARCHIVE PATH ITSELF APPEARS DEAD... OWED = proper path DISCOVERY." SAM's inline edit touched CALENDAR only. Removed the row from both files (event date Aug-6 = 11d old, already past the >7d bar, so it went straight to a pruned-note rather than lingering a run in RECENTLY RESOLVED) — full FINAL ACTUALS (Aug-3 −¥8.03T / Aug-4 −¥11.27T anomaly-survives / Aug-5 −¥3.29T ordinary) preserved in the note.
- **Fri Aug-14 CFTC (Aug-11 data) was already GRADED in STATUS** (§ live block + workbook table, verified against `workbook/CFTC_JPY.tsv` Aug-11 row: net −42,085/OI 391,874/long 134,188/short 176,273) — B0 NO-VERDICT on net (deep inside the deadband) but **OI −27,519 = 2.53× the bar ⇒ LIQUIDATION**, and **TFF KILL SPEC #3 FIRED** (asset-mgr/other-reportable opposite-signed, both over bar) — meaning some of the 8/7 "one crowd forced out together" story is a composition effect, not a pure crowd event. This outcome was sitting in STATUS but neither docket file had migrated the row out of its forward-looking framing ("FIRST FULLY POST-REVERSAL READ"). Migrated to CALENDAR RECENTLY RESOLVED with the full grade; removed from CATALYSTS.tsv forward feed.
- **Fri Aug-14 FRBNY Q2-2026 FX Operations quarterly row** already had its outcome written in-line (✅ resolved, Q2 predates 7/30-31, confirms the 8/10 ESF/SOMA-halves retraction) but was still sitting in the AUGUST-REMAINING forward table in both files instead of RECENTLY RESOLVED. Relocated; content otherwise correct, condensed on the move.
- **Stale restated BOJ percentage found and deleted (correction ③ from the spawn packet, "doubly so"):** the Sep-18 SAM-28/SAM-39 grading row's `notes` field in `CATALYSTS.tsv` still carried **"BAND of ~40-54% unpriced (repriced 2026-08-06)"** — a restated OIS figure that predates SAM's 8/17 flag that the instrument itself is now suspect (Sep reads 51.0%, +0.0pp across 2 as-of dates, against a JGB 2Y sell-off to a series high). CALENDAR's own copy of this row was already clean (SAM must have caught it there on an earlier pass); the TSV mirror was the miss. **Deleted the figure per the standing fix — did not refresh it** — replaced with a pointer to `workbook/BOJ_OIS.tsv` only.

**2 — Verified: Sep-18 date never described as a live retire-check gate.** Both files correctly frame all 3 Sep-18 rows (National CPI / BOJ decision / SAM-28+SAM-39 grading) — the grading row explicitly says "SUPERSEDED 2026-08-13... can no longer FIRE... GRADING, not deciding," consistent on both surfaces. No regression found.

**3 — CALENDAR ↔ CATALYSTS row-for-row agreement, verified by count:** CALENDAR carries 22 distinct forward events across AUGUST-REMAINING (6 rows / 8 events: the Aug-20 20Y+TB pair and Aug-28 2Y+Tokyo-CPI pair each merge two events into one row) + SEPTEMBER (9 rows / 12 events: Sep-16 FOMC+TB pair, Sep-18 triple-stack) + BEYOND-6-WEEK-HORIZON (2 rows / 2 events). CATALYSTS.tsv: **22 data rows**, exact match.

**4 — MOF `feio/quarterly` per-op release date-pin — CLOSED (open since Run-5, 2026-06-03).** Fetched `mof.go.jp/english/policy/international_policy/reference/feio/quarter/` at primary: **the Q2 2026 (Apr-Jun) report already PUBLISHED Aug-7, 2026** — `2026_2Qe.html` lists 3 ops by date (Apr-30 ¥6,278.7B / May-4 ¥780.2B / May-6 ¥4,675.9B), total **¥11,734.9B**, matching STATUS's already-known MOF-monthly-sourced aggregate exactly (own-verified, not new content — closes the long-standing "per-op breakdown awaits MOF quarterly release" note from Run-5). Also pulled Q1 (`2026_1Qe.html`, published May-12, ¥0) to derive a 2-point cadence: +42d (Q1) / +38d (Q2) after quarter-end. Applied to the Sep-30 quarter-end ⇒ **Q3 (Jul-Sep, the window containing the 7/30-31 ops) estimated ~Nov-9, 2026** — added as a new 🟠 row to CALENDAR's BEYOND-6-WEEK-HORIZON table and a matching CATALYSTS.tsv row, explicitly flagged as the **JAPANESE-side counterpart** to the already-tracked FRBNY Nov-13 row (US-side). Both rows now converge on the same ~1-week window for the same operation from independent primaries. Both dates appended to RELEASES.md Confirmed dates (Q1/Q2 retrospective + Q3 estimate-methodology).

**5 — >7d prune (today = Aug 17):** Fri Aug-7 CFTC (10d) · Thu Aug-6 JGB 30Y + MOF weekly (11d) · Tue Aug-4 JGB 10Y + BOJ c/a no-3rd-op (13d) · Sun Aug-2/Tue Aug-4 candidate-op-resolved (13-15d) — 6 rows pruned from RECENTLY RESOLVED, narrative preserved in the prune-note (all already fully narrated in STATUS/TIMELINE/workbook TSVs). Post-prune, RECENTLY RESOLVED holds exactly the <7d set: Aug-17 GDP (0d), Aug-14 CFTC + FRBNY (3d, both newly migrated this run), Aug-12 CPI (5d).

**6 — October boundary + MOF alteration page — verified still correctly flagged, no action due yet.** Tokyo September CPI Oct-2 (not in September) is carried in both CALENDAR's SEPTEMBER header note and RELEASES.md Confirmed dates — confirmed still present, no regression. MOF `2609ae` alteration-page re-check is due "early September," not yet — confirmed still flagged in STANDING MONITORS below, no fetch performed this run (not due).

**Verification:** `awk -F'\t'` column count = **8 on all 23 lines** (22 data rows), no drift. File date-sorted (`sort -c` on the date column: clean). `jgb_auctions.py` token filter: **8** JGB auction rows (down from 9 pre-run — the Aug-18 row is the earliest surviving one, none of the removed rows were JGB-auction-tagged so this reflects no change from the removals, just the ongoing monthly cycle). `sam-internal` rows: **2** (Aug-31 MOF monthly, Sep-18 grading) — both correctly render 🔧. `catalyst_countdown.py` rc=0, clean, no parse errors, 45-day horizon shows imminent+upcoming through Sep-30 as expected; the two Nov rows correctly do not render (tool horizon, not a gap).

**Runway:** **84d** to the furthest TSV event (Nov-13 FRBNY Q3 quarterly) — up sharply from Run-15's 53d, driven by the new Nov-9 MOF row (the furthest event before this run's add was already Nov-13; the runway number itself is unchanged in kind but the horizon now carries 2 independent Nov primaries instead of 1). Within the 45-day countdown window: 5 events in the next 7 days (Aug-18 5Y, Aug-20 20Y+TB, Aug-21 CPI+CFTC).

**Baseline audit:** **no trigger fired** — not the first run of a new calendar month, no SAM post-miss flag. **Next monthly audit = first run of October** (unchanged).

**Runtime:** ~35 min (2 sibling-miss diffs against STATUS/workbook primaries, live MOF `feio/quarter` primary fetch ×2 for the cadence derivation, full TSV rewrite + CALENDAR multi-section edit, RELEASES.md addition, verification suite). Did NOT commit/push — left for SAM.

#### CLOSEOUT ADDENDUM — 2026-08-17, same day (post-ruling reconciliation, commit `ce30639af` already applied)

Run 16 above was written **before** SAM ruled on its escalations; this addendum reconciles the state file to what actually landed, per SAM's closeout request. Summary of the reconciliation (not a new sync — no re-run, no re-verification of already-graded events):

1. **Escalation 1 (MOF Q3 row 🟠→🔴) — RULED DENIED, 🟠 stands.** Reasoning preserved in full at the top of `## PENDING`. Propagated the ruling into the row itself: `CATALYSTS.tsv`'s Nov-9 row `notes` field had been left asking "SAM to decide if this should be elevated to 🔴" — a stale open-question artifact of exactly the class SAM's closeout flagged (a ruling that landed in KOYOMI_MEMORY.md but not in the row that asked the question). Fixed; CALENDAR's copy of the same row never asked the question, so it needed no edit.
2. **Escalation 2 (verification):** no action needed — SAM independently re-confirmed the same numbers (22×8, sorted, rc=0, zero stale %) and specifically validated the "no bare COLD" claim (3 hits, all legitimate transition arrows). Noted in NEXT RUN HINTS as a worked example of a precise-vs-loose claim.
3. **Escalation 3:** no action needed — already closed correctly.
4. **CPI row (Aug-21) — SAM's separate same-day fix, verified not redone.** Confirmed at the artifacts (not re-derived): `ESTAT_APPID` retraction + the two real rebasing parameters (`statsDataId`, Tokyo `cdArea`) are correctly reflected in both CALENDAR and CATALYSTS, and neither implies a clean 8/21 cutover (parallel-basis-to-Dec-2026 fact is intact in both rows). Added a STANDING MONITOR so a future sync doesn't accidentally introduce a cutover claim.
5. **Header/state-line drift check (the cross-fleet defect SAM flagged — 3 other files hit today):** `docket/` clean except the one row noted in (1). `CALENDAR.md`'s own "Last Updated" header is current (this run). No `KOYOMI_MEMORY.md`-level "Last run:" quick-reference field exists in this file's structure (unlike METSUKE/KURA's memory files) — the `## CHANGES SINCE LAST RUN` section serves that role and was already current as of Run 16's own write.
6. `## PENDING`, `## STANDING MONITORS`, `## NEXT RUN HINTS` rewritten against current (post-ruling) state — old pre-ruling hints struck, not left to mislead a future run. `## CALIBRATION` untouched (SAM-owned). Only `docket/` files touched. Did not commit/push.

