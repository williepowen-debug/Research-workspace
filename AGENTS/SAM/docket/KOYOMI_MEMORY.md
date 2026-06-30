# KOYOMI MEMORY

State file for the docket-steward sub-agent. Spec is in [`KOYOMI.md`](KOYOMI.md) (durable). This file holds dated state: run history, pending items, standing monitors.

**Ownership:** KOYOMI writes this file directly at end-of-run (consistent with KOYOMI's other write privileges — full-edit mode by default, busy-work-only). SAM may pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** KOYOMI reads `KOYOMI.md` first (spec), then `KOYOMI_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last synced*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KOYOMI at run start: what's moved in STATUS / THESIS / TIMELINE / CHANGELOG since the previous sync. Cleared at end-of-run.*

*(Run 9 Jun 22 → Run 10 Jun 30 — 8 calendar days)*

- **THESIS v1.6.1 executed (Jun 29 session):** JGB long-end DEMAND-VACUUM thesis now live — BOJ conditional-let-run / supply forward-amplifier / demand structural-vacuum (3 legs). New prediction **SAM-32** (lifer non-re-entry, mechanism-based). New **30Y JGB 4.5% disorderly** carry-tail trigger. `research/outputs/JGB_SUPPLY_DEMAND_THESIS.md` created. SIGNAL-ONLY (BOND/LIQUID/HENRY). Jul 7 30Y + Jul 22 40Y = elevated demand-vacuum tests. Jul 31 BOJ MPM + FY2027 purchase-plan = JGB-supply read.
- **Position reconciled FLAT (Will-confirmed Jun 29):** prior 6-sh FXY stub moot. Carry-convexity-tail is now WATCH-FOR-ENTRY on a flat book.
- **BOJ SoO Jun 24:** hawkish-of-priced (~90% hike-by-Dec; neutral-2% urging faster; taper-halt Apr-2027). Confirmatory, no re-mark.
- **Tokyo June CPI Jun 26:** core-core 1.9% sticky (+30bp vs May 1.6). Mild hawkish tick; within-band.
- **CFTC Jun-23:** −146,104 / 81.2% — FIRST cover off the 83.4% top (+4,028 WoW). Amplifier +5pp ON. SAM-29 leg-1 (~32K room) / SAM-30 reclaim (3.8pp away). Next print Fri Jul 3 (Jun-30 data).
- **USDJPY:** 161.34 (Run 9 close) → 162.40 (Jun 30 boot) — fresh 40-yr high/1986-weakest; MOF silent 14d at 160+; market re-anchored intervention line 160→162 (ING).
- **Brent:** ~$77.7 (Run 9) → ~$74.25 (Jun 30) — oil-in-yen deeper dormant (~−23% cum).
- **TODAY (Jun 30):** Sato Ayano takes Nakagawa's BOJ seat (reflationist) + JGB 2Y auction (first post-Jun-16-MPM front-end read). Both resolving today.

---

## LAST RUN

### Run 10 — 2026-06-30 (post-JGB-demand-vacuum execution; Jun-17-22 >7d prune; Jun-23-26 cluster migration; Jun-30 events resolved; EARLY JULY framing refresh; claude-sonnet-4-6)

**Triggering context (CHANGES SINCE Run 9 Jun 22 → Jun 30):** THESIS v1.6.1 executed (JGB demand-vacuum, 3 legs, SAM-32 + 30Y-4.5%-disorderly trigger). Position flat (Will-confirmed Jun 29). BOJ SoO Jun-24 hawkish-of-priced. Tokyo Jun CPI core-core 1.9% sticky. CFTC Jun-23 −146,104/81.2% (first cover off the 83.4% top). USDJPY 162.40 (fresh 40-yr low; MOF silent 14d). Brent ~$74.25 (oil-in-yen dormant). TODAY Jun 30: Sato takes Nakagawa's seat + JGB 2Y auction (both resolving today).

**Pruned (>7d rule, RECENTLY RESOLVED cluster):** Wed Jun-17 FOMC (13d) + Iran-deal (13d) + May-TB (13d), Fri Jun-19 National-CPI (11d), Mon Jun-22 CFTC EV-gate (8d) — all narrative in STATUS/CHANGELOG/TIMELINE.md.

**Resolved-row migration (spec §1):**
- **CATALYSTS.tsv:** removed both Jun-30 rows (Sato + JGB 2Y) — dates pass EOD today. Forward TSV now leads with Jul-1 Tankan.
- **CALENDAR.md LATE JUNE table:** removed Jun-22 CFTC resolved row (>7d, prune entirely) and Jun-23-26 cluster row (migrated to RECENTLY RESOLVED). Marked Jun-30 JGB 2Y ✅ result-pending.
- **CALENDAR.md MID-JUNE table:** marked Sato Jun-30 row ✅ resolved.
- **RECENTLY RESOLVED:** added Jun-23-26 cluster + Jun-30 Sato + Jun-30 JGB 2Y (result pending). Pruned Jun-17-19 entries (all >7d). Updated prune note.

**Framing refresh (task 3 — match STATUS/THESIS v1.6.1 view):**
- **CALENDAR Jul-7 30Y:** "J-ICS lifer long-end abandonment continuation test (SAM-26 mechanism re-test)" → **"JGB-demand-vacuum test (SAM-32 / THESIS v1.6.1): lifer structural non-re-entry mechanism. Watch BTC/tail vs Jun-10 30Y (BTC 2.936x, tail 2.8bp). SAM-26 FAILED; SAM-32 = mechanism test."**
- **CALENDAR Jul-22 40Y:** "Ultra-long demand; J-ICS abandonment most acute at 40Y" → **"JGB-demand-vacuum test (SAM-32 / THESIS v1.6.1): most stressed tenor for lifer non-re-entry. Watch BTC/tail vs May-27 BTC 2.702; Jul-7 30Y sets the intermediate read."**
- **CALENDAR Jul-31 BOJ:** added **"FY2027 purchase-plan decision = JGB-supply read (SAM-32 / THESIS v1.6.1)"** to What to Check + Threshold.
- **CALENDAR Jul-29 FOMC:** "Powell presser" → **"Warsh presser"** (Warsh in seat since May 22; stale reference corrected per [[finding_boot_sweep_macro_regime_context]]).
- **CATALYSTS.tsv:** identical framing updates propagated to threshold_signal + notes for Jul-7/22/31 rows; Jul-29 what_to_check fixed Warsh.
- **No live-spot violations found** in forward rows (INTERVENTION WATCH, PHASE 2 WATCH, STRUCTURAL CHANNEL 1, RETAIL/NISA all threshold-only — TRUTH MODEL clean).

**Sync verification (CALENDAR ↔ CATALYSTS):** 9 forward events in TSV (Jul 1 → Jul 31); CALENDAR carries the same set across EARLY JULY + MID-JUNE ✅ BOJ tables. catalyst_countdown.py runs clean post-edits; no sam-internal rows in TSV (last was Jun-22 CFTC EV-gate, now resolved).

**Baseline audit:** No trigger fired this run (not the first run of July; no SAM post-miss flag). Note "no audit trigger this run." **MONTHLY TRIGGER FIRES ON NEXT RUN** (first run of July — same day as Tankan Q2). Block ~10-12 min context for MOF Jul+Aug calendars / BOJ Aug / Stats Bureau Jul / BLS Jul / ESRI Q2 GDP audit.

**Runway:** 31 days to furthest event (BOJ Jul 31). 3 events in next 7d (Jul 1 Tankan, Jul 2 JGB 10Y, Jul 7 JGB 30Y). Healthy.

**Runtime:** ~8 min. RELEASES.md no additions (no source-fetched dates this run; all forward dates previously confirmed Runs 4/6/8). Did NOT commit/push — left for SAM.

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

- **Phase 2 Watch section reframe** may be needed if MOU walks back (Trump-Khamenei reset → Brent collapse → Phase 2 re-engages). Pre-emptive flag from Run 3. SAM-domain trigger. *(No MOU walk-back through Run 10; Brent ~$74 deeply dormant. Watch.)*
- **MOF quarterly per-op intervention release date verification (Run 5):** Apr-Jun 2026 ops breakdown ~early August. Fetch `mof.go.jp/english/policy/international_policy/reference/feio/quarterly/`, confirm convention, add as 🟡 TSV row. Non-urgent.
- **Sato verification provenance (Run 6, INFORMATIONAL):** All 5 claims primary-source verified Jun 4. RELEASES.md schema question (board-composition section?) still open for SAM.
- **✅ RESOLVED by SAM (Run-8/9) — CATALYSTS.tsv schema regression + CFTC EV-gate row + resolved-event TSV migration.** *SAM may clear these items.*
- **TIMELINE.md stale (Run 9 + Run 10 flag — still open):** TIMELINE last entry is Jun 16 BOJ hike. Does NOT carry discrete entries for Jun-17 FOMC / Jun-17 Iran-US deal / Jun-17 May-TB / Jun-19 National-CPI / Jun-20 Hormuz re-closure / Jun-22 CFTC EV-gate shrug / **Jun-24 BOJ SoO / Jun-26 Tokyo CPI**. Per [[finding_doc_routing_data_drops]] resolved-event narrative belongs in TIMELINE. **SAM-owned — flagged Runs 9 + 10, not acted.**
- **GEOPOLITICAL WATCH >7d rows (Run 9 flag — escalating: now 16-20d):** Jun 10-11 kinetic (**20d**), Jun 12 14-pt draft (**18d**), Jun 14 Brent sub-$90 (**16d**) — all far past the >7d rule. KOYOMI did NOT prune (SAM's analytical watch surface). **Flagged again — SAM should prune or explicitly retain-for-context.**
- **Jun 10 US CPI primary-source verification (Run 7 backlog):** BLS schedule page returned 403 in June. Append RETROSPECTIVE-CONFIRMED to RELEASES.md when BLS page accessible. Low-priority.
- **NEW (Run 10) — JGB 2Y Jun 30 auction result pending:** KOYOMI marked ✅ result-pending in CALENDAR. **SAM action:** run jgb_auctions.py / fetch `mof.go.jp/english/policy/jgbs/auction/calendar/eresul/eresul20260630.htm` for BTC ratio + tail + WA yield; compare vs May 2Y WA 1.369%. Not in KOYOMI write-set.

---

## STANDING MONITORS (surface each run)

- **BOJ pre-meeting blackout windows** (T-2 of each MPM) — kept as narrative in CALENDAR, not in TSV per form-consistency call from Jun 1. *Jun-16 MPM resolved (hiked 1.00%). Next blackout = **~Jul 29 (T-2 of the Jul 30-31 MPM)**.* Revisit if SAM wants regime-boundary dates in TSV.
- **Recurring weekly catalysts** (CFTC release Fri/Mon) — not in TSV (handled by `cftc_jpy.py` auto-pull) EXCEPT when a specific release is a pre-registered SAM-internal EV-gate (then it gets a `type=sam-internal` row). **Jun-22 CFTC EV-gate fully resolved (−150,132/83.4% → HOLD-band; v1.6 finalized).** Current state: CFTC Jun-23 = −146,104/81.2% (first cover off the top; amplifier +5pp ON). **Next print: Fri Jul 3 (Jun-30 data)** — routine auto-pull, no pre-registered EV-gate. Surface if a future CFTC print qualifies as a new sam-internal decision gate.
- **Post-meeting catalyst-window refill** — after each major catalyst resolves, the forward horizon thins; pull next-month's events from RELEASES.md cadence rules.
- **MOF auction calendar alteration page** — `auction/calendar/26MMae.htm` (e.g., 2606ae.htm) records mid-month tenor-band changes. Check at month boundary; current Jun 2026 alteration was a liquidity-enhancement tenor-band tweak (15.5-39 vs 11-39, then back), no date moves.
- **SAM-internal review triggers (Run 5; scope precedent in KOYOMI.md):** TSV-scope extended to admit SAM-internal mechanical decision gates (`type=sam-internal`). **Zero sam-internal rows in forward TSV (Jun-6 CFTC + Jun-9 SAM-21 resolved Run 7; Jun-22 CFTC EV-gate resolved/cleared).** Watch for new candidates as THESIS v1.6.1 / SAM-32 pre-registers mechanical gates (must meet DATE-SPECIFIC + ACTION-FORCING). Likely next: if SAM pre-registers a dated Jul-7 30Y or Jul-22 40Y demand-vacuum decision gate (pass/fail with a pre-defined response).
- **BOJ board composition transitions (Run 6):** Sato Jun-30 **RESOLVED** (took seat today). Next composition event: TBD (other Policy Board terms expire 2026-2030 — baseline against BOJ page needed). RELEASES.md schema still doesn't cover board-composition events; flag for SAM if/when the next transition approaches.

---

## NEXT RUN HINTS

- **🚨 NEXT RUN = first run of July → MONTHLY BASELINE AUDIT FIRES** (per spec § 2a; last fired Run 4 Jun 2; Run 10 is the last June run). Audit: MOF Jul + **Aug** calendars (`auction/calendar/2607e.htm` + `2608e.htm` + `2608ae.htm` alteration), BOJ Aug MPM schedule, Stats Bureau Jul releases (National Jul CPI ~Aug 21, Tokyo Jul CPI ~Jul 31), BLS Jul CPI (~Jul 15), ESRI Q2 GDP 1st prelim (~mid-Aug). Read CALIBRATION "Declined release classes" first (none currently). Block ~10-12 min. Pull Aug auctions to keep runway >30d past Jul-31 BOJ.
- **Imminent-catalyst results to backfill to RECENTLY RESOLVED:** Tankan Q2 (Jul 1) + JGB 10Y (Jul 2). Auto-fetch via jgb_auctions.py for 10Y; Tankan result from STATUS/news.
- **Jul-7 30Y prune cadence:** after Jul 7 fires, move to RECENTLY RESOLVED (result → STATUS/workbook). Compare BTC/tail vs Jun-10 (BTC 2.936x, tail 2.8bp) — SAM-32 mechanism test read. If BTC <2.5x or tail >5bp → SAM-32 preliminary confirmation; surface to SAM.
- **JGB 2Y Jun 30 result (see PENDING):** SAM should fetch eresul20260630 and update STATUS/workbook. KOYOMI notes it here for next-run prune tracking. Once result is logged in STATUS, the RECENTLY RESOLVED entry is complete.
- **RECENTLY RESOLVED prune cadence (next run):** Jun 23-26 cluster turns >7d on Jul 1 → prune eligible first run of July. Jun 30 Sato + Jun 30 JGB 2Y turn >7d on Jul 7 → eligible at the Jul-7 30Y run.
- **Flagged for SAM (see PENDING — repeated flags):** (a) TIMELINE stale — backfill Jun 17-20 + Jun 24/26 events; (b) GEOPOLITICAL WATCH Jun 10-14 rows now 16-20d old — prune or retain.
- **CFTC Jul 3 print (Jun-30 data):** routine auto-pull. cftc_jpy.py auto-fetches. Not a TSV row (excluded class); STATUS owns the live read. Watch: SAM-29 leg-1 (cover <−108K) / SAM-30 reclaim (build through −153K/85%).
- **BOJ pre-meeting blackout ~Jul 29 (T-2 of Jul 30-31 MPM):** add as CALENDAR narrative note when closer; not a TSV row (form-consistency call from Jun 1 still stands).
- **If SAM pre-registers a dated mechanical gate (e.g., "Jul-7 30Y BTC <2.5x → SAM-32 confirmation action"):** apply TSV-SCOPE PRECEDENT inclusion bar without re-escalating (DATE-SPECIFIC + ACTION-FORCING). The `type` column is in place (8-field header confirmed Run 9).
- **MOF feio/quarterly source check:** Apr-Jun 2026 per-op breakdown ~early August. Non-urgent; verify date at source, add 🟡 TSV row when date pinned. Still in PENDING.
- **Trade-stat date pinning reminder:** Japan TB dates come from MOF Customs (`customs.go.jp/toukei/calendar/calend_e.htm`), NOT mof.go.jp/jgbs. Jun TB = Jul 22 (already in boot.py auto-pull). Not a TSV row (boot.py handles it).
