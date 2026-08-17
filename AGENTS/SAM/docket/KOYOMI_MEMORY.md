# KOYOMI MEMORY

State file for the docket-steward sub-agent. Spec is in [`KOYOMI.md`](KOYOMI.md) (durable). This file holds dated state: run history, pending items, standing monitors.

**Ownership:** KOYOMI writes this file directly at end-of-run (consistent with KOYOMI's other write privileges — full-edit mode by default, busy-work-only). SAM may pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** KOYOMI reads `KOYOMI.md` first (spec), then `KOYOMI_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last synced*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KOYOMI at run start: what's moved in STATUS / THESIS / TIMELINE / CHANGELOG since the previous sync. Cleared at end-of-run.*

*(Run 15 Aug 7 → Run 16 Aug 17 — 10 calendar days, and SAM ran its OWN inline docket sync earlier the same day as this run, so this run's job was verify-and-complete, not first-pass sync. THESIS advanced v1.6.11 → v1.7 mid-window: leg-1 fired 8/7, carry-convexity tail RETIRED TO LOW, book stays FLAT.)*

- **Why this run was spawned:** SAM's 8/17 inline boot sync covered the Q2 GDP grade, the Aug-20 20Y promotion, the Aug-21 CPI instrument-block flag, and a new Aug-21 CFTC row — but left 3 sibling items unmigrated (see LAST RUN below) and one stale restated BOJ percentage from an earlier run.
- **CFTC frame broke 8/7** (net −45,473, through leg-1 −108K/60% by 62,527 contracts, 42d early) → convexity tail RETIRED TO LOW; **SAM-29 + SAM-40 both FAILED**; book was FLAT throughout, $0 at risk. Route 4 (FOMC dot walk-back) re-rated COLD → LIVE-but-UNFIRED same day on a weak NFP.
- **8/14 CFTC (Aug-11 data) already GRADED in STATUS** (B0 NO-VERDICT on net; OI −27,519 = LIQUIDATION; TFF KILL SPEC #3 FIRED, exposing an 8/7 composition effect) but never migrated out of either docket file's forward view — fixed this run.
- **BOJ c/a `jd` archive retraction (8/14):** the "dead archive" claim from the 8/13 sync was SAM's own missing-year-subdirectory URL bug, not a dead source. All 3 ladder legs now FINAL. CALENDAR's forward table carried the correction but the TSV mirror row still had the old stale "archive is dead" claim — fixed this run.
- **JGB long end broke through 4.00%** (MOF closes 4.002 8/13 & 8/14) and the curve flipped to a long-end-led bear steepener on the 8/17 weak Q2 GDP print (+1.1% ann. vs +2.0% exp, consumption first negative in 8 quarters) — SAM registered attribution (fiscal/supply vs BOJ-hike-pull-forward) as OPEN, deliberately not resolved on one session. This promoted the Aug-20 20Y auction to 🔴 (near-term Pillar-2 adjudicator).
- **MOF weekly wk 8/2-8/8: +¥1,629B foreign LT-debt BUYING** (largest in the tracked series; 4-wk rolling ~flat +¥572B). Per SAM's explicit instruction this stays a **datum routed to BOND, not a verdict** — the single-week BND-11 gate form is STOOD DOWN and no forward MOF-weekly TSV row was added.
- **BOJ OIS instrument flagged SUSPECT by SAM** (Sep reads 51.0%, +0.0pp across two consecutive as-of dates, while JGB 2Y cash sold off to a series high) — reinforces the standing "never restate a BOJ percentage in the docket" rule; found and deleted one surviving restated band this run (see LAST RUN).

---

## LAST RUN

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

### Run 15 — 2026-08-07 (SAM-directed PRE-PRINT sync of the 8/4→8/6 resolve window; JGB 30Y FIRM + MOF weekly NO-VERDICT migrated; BOJ c/a stays open; Sep-18 OIS band repriced + de-staled in both docket files; >7d prune; no audit trigger)

**Triggering context:** see CHANGES SINCE above. Spawned mid-session Friday ~12:4x ET, PRE-PRINT — the 3:30 PM ET CFTC print has not happened yet. Scope: sync the 8/4→8/6 resolve window; edit only `docket/`.

**1 — Resolved-row migration (spec §1), verified against named primaries, not taken on say-so:**
- **JGB 30Y auction (Thu 8/6) → FIRM, PASSED its live test.** Verified `workbook/JGB_AUCTIONS.tsv` row 21: BTC 3.864×, lowest/high yield 3.952%, avg 3.937%, tail 1.5bp — exact match to the spawn packet. Migrated CATALYSTS.tsv + CALENDAR AUGUST-REMAINING row → CALENDAR RECENTLY RESOLVED with the floor-confirmation framing (7/7 → 7/22 → 8/6 series). No live JGB yield levels pasted into any watch cell (TRUTH MODEL held) — the 10Y/30Y/40Y rally context in the spawn packet was used only to justify the significance line, not written to the docket.
- **MOF weekly ITS (wk 7/26-8/1) → NO VERDICT.** Verified `workbook/MOF_FLOWS.tsv` last row (period `2026．7．26～8．1`): LT_Debt_Net_T_yen = **0.478** (+¥478B), vs prior two weeks -0.811 and -0.724 (both SELL) — exact match. ¥500B - ¥478B = ¥22B, confirms the "misses the durable bar by ¥22B" framing exactly. Migrated to RECENTLY RESOLVED as a dead-middle outcome — explicitly NOT rounded to "buying week," explicitly flagged that the resolver rolls forward with no new terms set (escalated to PENDING, not decided by KOYOMI).
- **BOJ current-account ACTUAL (`jd20260804.xlsx`) — STILL 404, kept OPEN per spawn instruction.** Notes field updated in both CATALYSTS.tsv and CALENDAR to log the two additional failed re-pull attempts (8/6, 8/7) without marking resolved or pruning. This row does not render in `catalyst_countdown.py`'s output once its date is in the past (confirmed this run — the script silently drops past-due forward rows rather than showing negative days); that's a script-horizon fact, not a docket defect, and matches the pattern already documented for other "owed re-pull" items.
- **Fri 8/7 CFTC row — untouched**, per explicit spawn instruction (today's print, no pre-written outcome).

**2 — BOJ OIS Sep-18 band repriced + de-staled (both files):** `workbook/BOJ_OIS.tsv` verified: as-of 2026-08-06 pull, Sep 17-18 cumulative 45.60% (was 39.70% at the 8/3 pull), Oct 28 75.60%, Dec 17 88.40%. Per the spawn's explicit instruction, wrote SAM's band framing verbatim — **Sep unpriced ~40-54%, NOT a point estimate, Sep/Oct split not identified** — rather than deriving a new point figure myself (that's SAM's analytical call, not KOYOMI's). Replaced the stale figure in **two places**: CATALYSTS.tsv row `2026-09-18 BOJ MPM day 2 decision` (threshold_signal — was "~60% unpriced… NOT ~77%," itself already one repricing behind) and the same-date `Convexity-tail window-end retire-check` row (notes). **Also caught a CALENDAR-only staleness the TSV-side 8/4 correction never propagated to**: CALENDAR's SEPTEMBER table Sep-18 BOJ MPM row still read **"Sep priced ~23% (Oct ~64%)"** — the *pre*-8/4 figure, never updated when SAM fixed the TSV on 8/4. Fixed both surfaces to the same 8/6 band this run so they can't diverge again silently.

**3 — >7d prune (today = Aug 7):** Jul-29 FOMC (9d) + Jul-30 JGB 2Y (8d) pruned from RECENTLY RESOLVED — both narrative already in STATUS/`workbook/JGB_AUCTIONS.tsv`. **The four Jul-31 rows + the Jul-31 CFTC row are exactly 7 calendar days old today — NOT pruned** (rule is *strictly* >7d, and Run 14's own NEXT RUN HINTS said these "turn 7d Aug-7," i.e. eligible starting Aug-8, not on the day they turn 7d). Flagged for the next run.

**4 — Escalations (no analytical calls made):**
- **MOF weekly BND-11 resolver has no post-8/6 terms.** The original 3-week test (durable ≥+¥500B / transient) has now run its course without a clean answer. SAM needs to either set new resolver terms for a future print or explicitly stand down the gate-bearing carve-out for this class (Run-14 CALIBRATION generalization) until a new live question exists.
- **BOJ c/a `jd20260804.xlsx` 404 persistence** — now 3 sessions running (8/4 discovery, 8/6, 8/7). Worth a primary-page-structure check if it's still 404 next run; flagged, not investigated (out of KOYOMI's remit to debug the source).
- **Sep 15-16 FOMC route-4 "COLD" characterization** — today's NFP (−23K, −103K net revisions; Sep Fed hike odds 57%→43.9%) may bear on this, per the spawn packet. Left the CATALYSTS.tsv/CALENDAR "COLD" wording untouched — this is an analytical call for SAM, not a mechanical date/figure update.

**Verification:** `awk -F'\t'` column count = **8 on all 24 lines** (23 data rows), no drift. File date-sorted (`diff` against `sort`: identical). `jgb_auctions.py` token filter re-checked in-process — **8** JGB auction rows match exactly (down from 9: the Aug-6 30Y resolved off). `sam-internal` rows: **4** (BOJ c/a Aug-6, CFTC Aug-7, MOF monthly Aug-31, convexity-tail retire-check Sep-18) — down from 6 at Run-14 (the two Aug-4/5 BOJ c/a rows were already consumed by SAM's 8/4 inline edit before this run; the Aug-6 MOF weekly row resolved off this run). `catalyst_countdown.py` rc=0, clean, no parse errors; 4 sam-internal rows render 🔧. CALENDAR ↔ CATALYSTS event-set agreement: **23 TSV rows = 21 CALENDAR table rows** (9 August + 12 September; August merges the Aug-20 20Y+TB pair and the Aug-28 2Y+Tokyo-CPI pair into one row each, so 9 rows carry 11 events + 12 September rows carry 12 events = 23 events, matching the TSV row count).

**Runway:** **53d** to the furthest TSV event (Sep-30 JGB 2Y) — down slightly from Run-14's 59d (time has simply passed; no rows lost). 3 events in the next 7 days (Aug-7 CFTC today, Aug-12 US CPI, Aug-17 GDP is 10d — just outside).

**Baseline audit:** **no trigger fired** — not the first run of a new calendar month, no SAM post-miss flag. **Next monthly audit = first run of October** (unchanged from Run 14).

**Runtime:** ~20 min (2 primary-source verifications against workbook TSVs + BOJ_OIS.tsv, 2-file OIS-band propagation, prune pass). Did NOT commit/push — left for SAM.

### Run 14 — 2026-08-02 (SAM-directed FULL DOCKET SYNC — inverted-CAL-DRIFT repair; September delta APPLIED [12/12]; INTERVENTION WATCH rewritten; no audit trigger)

**Triggering context:** see CHANGES SINCE above. METSUKE Run-13 escalated an **inverted CAL-DRIFT** (trade docs fresher than the docket). SAM pre-ruled on every Run-13 PENDING item on the spawn, so this run was **apply + repair**, not propose.

**1 — Resolved-row migration + prune (spec §1):**
- **CATALYSTS.tsv:** removed the last resolved forward row, **2026-07-31 CFTC (Jul-28 data)** — the gate FIRED, so it is an outcome, not a watch. (The Jul-31 BOJ and Jul-31 MOF-monthly rows had already been migrated by SAM's own write-back; Jul-22 40Y and Jul-29 FOMC were pruned/migrated 7/31. Verified — nothing else resolved was still sitting forward.)
- **CALENDAR:** deleted the now-empty **EARLY JULY** section entirely (its single remaining row was that CFTC row). Added the fired CFTC print to **RECENTLY RESOLVED** with the full outcome + the provisional-on-8/7 caveat.
- **>7d prune (today = Aug 2):** Jul-24 CFTC gate + Jul-24 National June CPI, both **9d** ✂️. Retained (<7d): Jul-29 FOMC (4d), Jul-30 2Y (3d), the four Jul-31 entries (2d) + the new Jul-31 CFTC row.

**2 — September delta APPLIED, 12/12 (SAM ruling on the spawn; Run-13 proposed, propose-only):** all 12 rows added to CATALYSTS.tsv **and** a new CALENDAR **SEPTEMBER** section, priorities/who_cares as proposed. Notes on the three SAM called out specifically:
- **Row #9 — Sep-18 convexity-tail window-end retire-check (`type=sam-internal`) APPROVED.** Written with SAM's ruled action-language: runs at **Sep-18 close, AFTER the BOJ decision prints**, window **INCLUSIVE** of Sep-18; pre-registered disposition = no eligible trigger + ≥80% fuel → retire to LOW (SAM-28), leg-1 companion cover-below-−108K (SAM-29). Both files carry the note that **this row is the TEMPLATE for future eligibility-window checks** and that it is now *more* load-bearing than at proposal (Sep 17-18 MPM in-window, ~77% unpriced).
- **Row #4 — US CPI Sep-11: provenance caveat RETAINED** in both files. Primary re-verify **re-attempted this run: BLS still HTTP 403 with curl + browser UA** (n=2 sessions — the Jun-10 workaround is dead, not just flaky). Logged to RELEASES.
- **Sep-18 triple-stack** rendered in CALENDAR in intraday order (National CPI 8:30 JST → BOJ decision ~midday → retire-check at close), with an explicit callout above the table. **No CFTC row for September** (per the CALIBRATION ruling — no live September-specific tripwire registered).

**3 — INTERVENTION WATCH REWRITTEN (the most stale section in the file).** Killed the whole "ARMED not FIRED / MOF silent 35d / 165 = next threshold / defending a one-way slide" frame — it described a world that ended on 7/30. New table: the 7/30 op as FIRED-occurrence (size = estimate, flagged as such) · the **7/31 candidate as UNRESOLVED, explicitly "do NOT record as confirmed"** with its weak leg stated (35-min progressive slide, not ballistic; month-end + stop-cascade competing causes) · the confirmation ladder (BOJ c/a T+2 ~8/4 and ~8/5, MOF monthly ~8/31 covering both) · the unchanged actionable trigger (disorderly ≥1.5-2%/day; CH-011 disorder-not-level, now stamped twice; AMBUSH S1-A) · USD/JPY 155 now a *direction-toward* level for the first time this cycle · jawbone tier with the next blackout re-dated ~Sep 15.

**4 — Other stale-framing refreshes (task 3, matched to STATUS 8/2 wording, nothing invented):**
- **CHANNEL 1 MONITORS:** header said "v1.5 — DEFERRED STRUCTURAL BACKSTOP"; STATUS says **RETIRED**. Re-headed and re-written to the retired framing + the exact re-add condition (direct foreign-SALES print, ≥2 consecutive windows, ≥2 institutions) and the [[finding_threshold_vs_mechanism]] warning that 30Y/ESR are accelerant co-conditions, never the necessary leg. Added the 4.5%-disorderly J-GAAP impairment TAIL row.
- **PHASE 2 WATCH:** re-headed to Phase-1-unwinding; Brent row de-staled; CFTC row rewritten around the **fired** flip-condition + the 8/7 resolver; **added a yen-haven re-couple (SAM-31) row** — 7/30's yen +2.7% with VIX down hard is the cleanest counter-evidence yet and had no home in the docket.
- **GEOPOLITICAL WATCH:** replaced the deal-durability-only view with the live 8/1-8/2 picture (ordered-then-cancelled energy-site strikes, pause #3 with the 4-day base rate on pause #2, Tehran unconfirmed, GasLog Shanghai Hormuz-theater-checked, Kpler transits −77%), keeping the ~Aug-16 Oman fee-window as the residual dated item.
- **RETAIL/NISA:** stripped a stale hard figure; added that the 7/30-31 ~6-yen reversal is the first move of the cycle big enough to test the unhedged-book sensitivity row against.

**5 — TRUTH MODEL live-spot strip (spawn item 4):** removed **Brent $100.43** (2 cells — INTERVENTION WATCH + PHASE 2), the "$115 nearing" proximity claim, JGB 30Y/10Y/40Y yield levels from the CHANNEL 1 table, and the stale CFTC level string (−123,778/68.8%, −122,663/68.1%, 86.2%) from PHASE 2. Thresholds kept in every case; live values pointed at STATUS. Post-edit grep for price/yield/net-position patterns above RECENTLY RESOLVED: **clean.** (Resolved *outcomes* in RECENTLY RESOLVED keep their figures by design — that table's job is outcomes.)

**6 — Three new dated rows added (ESCALATION-LOG, applied defaults, veto-able — all `type=sam-internal`):** STATUS § WHAT TO WATCH carried three dated, action-forcing discriminators that had no docket row. Applied per the TSV-SCOPE PRECEDENT (DATE-SPECIFIC + ACTION-FORCING, self-resolving per NEXT RUN HINTS) rather than round-tripped:
- **Tue 8/4 — BOJ current-account `jd20260803.xlsx`**, T+2 semi-confirm of the 7/30 op (Tanshi-gap, playbook S1-A).
- **Wed 8/5 — BOJ current-account `jd20260804.xlsx`**, the discriminator for the 7/31 candidate. 🔴 because **a *confirmed* second op is a pre-registered EARLY-ENTRY OVERRIDE (memo §5C)** — this is the row most likely to force a position decision inside 72h.
- **Thu 8/6 — MOF weekly ITS, 3rd-week BND-11 TRANSIENT/DURABLE confirm.** ⚠️ **The scope-stretch of the three:** MOF weekly is an explicitly EXCLUDED class in the spec universe. Admitted on the *same* logic SAM used for CFTC in the Run-12 CALIBRATION amendment (routine prints out; a print carrying a live pre-registered resolver in). **If SAM disagrees, this is the one to strike** — it's one line in each file.

**Verification:** `awk -F'\t'` column count = **8 on all 28 lines**, no drift. File date-sorted (`diff` against `sort`: identical). `jgb_auctions.py` token filter re-checked in-process — matches exactly the **10** JGB auction rows, zero sam-internal rows. `catalyst_countdown.py` rc=0, **6 sam-internal rows all render 🔧**. CALENDAR ↔ CATALYSTS event-set agreement: **25 CALENDAR date-rows = 27 TSV rows** (CALENDAR merges the Aug-20 and Aug-28 pairs into one row each — 25 + 2 = 27); priorities and who_cares match row-for-row.

**RELEASES.md:** +3 cadence/weekday-verified rows (the 8/4, 8/5, 8/6 discriminators); Sep-11 US CPI row updated with the failed 8/2 primary re-verify; alteration-page note given a re-check-due date. **No source-fetch audit this run** (all 12 September dates were already source-confirmed at Run 13).

**Runway:** **59d** to the furthest TSV event (Sep-30 JGB 2Y), up from **29d** pre-run (Aug-31) — the September apply roughly doubled it. **6 events in the next 7 days** (Aug 4 ×2, Aug 5, Aug 6 ×2, Aug 7), of which **2 are 🔴**. This is the densest near-window of any KOYOMI run to date; the 45-day countdown horizon now truncates at Sep-16, so Sep-18/29/30 won't render at boot until ~Aug 4 onward.

**Baseline audit:** **no trigger fired** — the monthly trigger belongs to the *first run of a new calendar month*, and Run 13 (Jul 31) already executed the September audit that this run applied. **Next monthly audit = first run of October.** No SAM post-miss flag.

**Runtime:** ~15 min. Did NOT commit/push — left for SAM.

### Run 13 — 2026-07-31 (verify SAM's inline true-up + 🔍 MONTHLY BASELINE AUDIT fired — September delta, propose-only; spawned mid-session while the Jul-31 BOJ MPM decision is still live/pending)

**Triggering context:** see CHANGES SINCE above. Two-part spawn: (1) verify (don't re-do) SAM's own inline true-up from ~30min prior; (2) September monthly baseline audit (August fully seeded, September empty, and September carries the FOMC Sep-15/16 + BOJ Sep-17/18 + Sep-18 convexity window-end thesis-critical cluster). **Jul-31 BOJ MPM row explicitly NOT touched** — resolves later this session, SAM's own write-back.

**PART 1 — Verification of SAM's inline true-up (CALENDAR.md + CATALYSTS.tsv, 2026-07-31 header entry):**
- **CALENDAR ↔ CATALYSTS.tsv agreement:** clean. All 3 new rows (Jul-31 CFTC Jul-28-data, Aug-7 CFTC Aug-4-data, ~Aug-31 MOF monthly) present in both files with matching priority/who_cares/type. All 5 resolved-and-migrated rows (Jul-24 CFTC, Jul-24 National CPI, Jul-29 FOMC, Jul-30 2Y, Jul-31 Tokyo CPI) correctly removed from CATALYSTS.tsv forward feed and present in CALENDAR's RECENTLY RESOLVED. The >7d Jul-14→22 prune (5 rows, 9-17d old) checked against Jul-31 today — all genuinely >7d, prune is correct.
- **Schema conformance:** `awk -F'\t'` column-count check on all 16 TSV rows — **all 8 fields, no drift.** File is date-sorted (verified: 07-31×3 → 08-04 → 08-06 → 08-07 → 08-12 → 08-17 → 08-18 → 08-20×2 → 08-21 → 08-28×2 → 08-31). JGB auction rows keep "JGB"+"auction" in event name; CFTC/MOF rows correctly lack those tokens (jgb_auctions.py filter stays clean). `type` column correctly tagged (`sam-internal` on the 3 new gate/intervention rows, `external` on the JGB/CPI/GDP/TB rows).
- **Date correctness (the two items the spawn flagged for explicit check):**
  - **Aug-31 MOF monthly:** Aug-31 2026 = **Monday** (`date -d`); Aug-29 = Sat, Aug-30 = Sun → **Aug-31 IS the last business day of August 2026.** Correct.
  - **Aug-7 CFTC (Aug-4-data):** Aug-4 2026 = **Tuesday**; Aug-7 2026 = **Friday**, same calendar week. Matches the CFTC cadence rule (Friday release, prior-Tuesday data) exactly — Jul-31/Jul-28 pair verified the same way (Tue→Fri same week). Correct.
  - `catalyst_countdown.py` run clean post-verification: 45-day horizon, 2 IMMINENT sam-internal rows render 🔧, runway 32d to Aug-31, no parse errors.
  - **Zero mechanical errors found — nothing to fix.** Added the 3 inline-true-up dates to RELEASES.md Confirmed dates as cadence-derived/weekday-verified (they hadn't been recorded there; strengthens future audit trail per the RELEASES-append convention, done even though this wasn't a source-fetch audit run for these 3).

**PART 2 — 🔍 MONTHLY BASELINE AUDIT (September; monthly trigger — first run touching September, per NEXT RUN HINTS carried from Run 12):**
CALIBRATION declined-classes checked first: none declined. Sources fetched: MOF Sep calendar (`2609e.htm` — full tenor set 10Y/30Y/5Y/20Y/40Y/2Y + 2 liquidity-enhancement dates, excluded per universe rule) + alteration page `2609ae.htm` (404 = none exist yet, consistent with the Jul/Aug precedent of alterations appearing mid-month); Stats Bureau `1582.html` (raw HTML parsed directly, not the WebFetch summary — the summary garbled it on the first attempt, consistent with the known truncation issue): **National August CPI → Sep-18** (same day as the BOJ decision — see escalation below); **Tokyo September CPI (prelim) → Oct-2, NOT within September** (⚠️ see escalation — breaks the same-month/month-end pattern the audit brief assumed); Japan Customs calendar (raw HTML parsed — August whole-month provisional TB = **Sep-16**, same 3rd-date-column convention as the Jun/Jul rows already in use); US CPI (August data) — **BLS primary blocked 403 on both WebFetch and curl+UA this session** (worse than the Jun-10 precedent where curl+UA worked) → cross-checked 2 independent secondary sources (macroornoise.com, cpiinflationcalculator.com), both agreeing on **Sep-11**; FOMC Sep-16 + BOJ Sep-18 + GDP Sep-8 all reused from Run-11's pre-confirm (RELEASES.md already had them; reconfirmed no change, no re-fetch needed).

**DELTA: 12 proposed rows across 8 unique dates — written to `## PENDING` below, propose-only, NOT added to TSV.** Includes one NEW sam-internal candidate (Sep-18 convexity-tail window-end retire-check, per THESIS § Eligibility window — not previously in PENDING; flagged prominently for SAM sign-off on exact action-language before it's treated as self-resolving under the TSV-SCOPE PRECEDENT). All 12 dates + the Oct-2 Tokyo CPI out-of-window flag + the MOF alteration-page null-check appended to RELEASES.md Confirmed dates (14 rows) per audit step 6.

**Runway:** 32d to furthest TSV event (Aug-31 MOF monthly) as of pre-apply; applying the September delta would extend runway to Sep-30 (JGB 2Y). 3 events next 7d (Jul-31 BOJ+MOF+CFTC triple, if BOJ still counts as "next 7d" — it's tomorrow).

**Runtime:** ~18 min (verification pass + audit-heavy September pull, 2 blocked-source workarounds). Did NOT commit/push — left for SAM.

### Run 12 — 2026-07-21 (SAM-directed fleet freshness sweep w/ verified live snapshot; heavy early-July resolved-row prune + Jul-24 CFTC gate add + INTERVENTION-WATCH refresh; no baseline-audit trigger)

**Triggering context:** SAM directed a full docket freshness refresh (part of a fleet-wide "get all files current with live data" pass). Verified live snapshot supplied (7/21 ~22:16 ET boot.py); instructed NOT to re-fetch or guess dates. STATUS read confirmed SAM had already reconciled the June TB magnitude via its own MOF-customs pull (−¥406.9B sokuho / −¥881.9B adj, branch a) — used the STATUS-canonical figures over the boot-snapshot's "magnitude unreconciled" flag (STATUS more current than the boot brief).

**CATALYSTS.tsv (rewritten via Write for tab-safety):**
- **Pruned 8 resolved/past rows:** 2026-07-06 CFTC ✅, 07-07 30Y ✅, 07-09 5Y, 07-10 CFTC ✅, 07-14 20Y, 07-14 US CPI, 07-16 discriminator, 07-22 June TB (PRINTED 7/21). Forward feed now leads with the 07-22 40Y.
- **Added 1 sam-internal gate row:** 2026-07-24 CFTC COT (Jul-21 data), 3:30 PM ET — pre-registered tripwires (cover through −108K = SAM-29 leg-1 fires/LOW · build through −153K/85% = reclaim MED-HIGH · STALL = FLAT). Meets DATE-SPECIFIC + ACTION-FORCING (SAM-29/30 pre-registered). Added on SAM's explicit direction; the CALIBRATION "CFTC stays EXCLUDED" tension it raised was **RESOLVED same-run by SAM** (kept the row + amended CALIBRATION to admit pre-registered gate prints).
- Refreshed 40Y row (SAM-35 resolves 7/22, 40Y 3.852 [MOF 7/21]) + BOJ Jul-31 SAM-34 (~3% July-hike pricing as of 7/16, holds). catalyst_countdown.py runs CLEAN post-edit; 🔧 renders on both sam-internal rows (Jul-24 CFTC + Jul-31 MOF); jgb_auctions token filter intact (CFTC row lacks "JGB"+"auction").

**CALENDAR.md:**
- **Forward EARLY JULY table:** removed the 7 resolved rows (Jul-6/10 CFTC, Jul-9 5Y, Jul-14 US CPI + 20Y, Jul-16 discriminator) + the Jul-22 June TB (printed); added the Jul-24 CFTC gate row. Table now leads with the 40Y (tomorrow).
- **RECENTLY RESOLVED:** added Jul-14 US CPI (cool), Jul-14 JGB 20Y (pointer — no stress flagged), Jul-17 CFTC (SAM-37 STALL −122,663/68.1%), Jul-21 June TB PRINTED (−¥406.9B/−¥881.9B, branch a). Jul-16 MOF + BoK already present (kept). **Pruned the >7d Jun-30→Jul-7 cluster** (Sato, 2Y, Tankan, Jul-2 10Y + NFP, Jul-7 30Y — all 14-21d).
- **INTERVENTION WATCH:** header + row-1 refreshed 162.41/161.8 vintage → 163-through-zone / ORDERLY / ARMED-not-FIRED / MOF-silent-35d / 165 = next threshold; ambush regime S1-A unchanged; TRUTH-MODEL clean (no live spot — "through the zone" + "165 threshold" + "35d silent" are structural/state, not price cells).
- Header as-of stamp → 2026-07-21 Run-12 (prior 7/11 preserved). Pruned-note pointers added above EARLY JULY + below RECENTLY RESOLVED.

**Baseline audit:** No trigger fired (not the first run of a new calendar month — July's first run was Run-11 on 7/2; August already covered Run-11; no SAM post-miss flag). **Next monthly audit = first run of September** (Sep partially pre-confirmed Run-11: Sep-8 GDP 2nd prelim, Sep-15/16 FOMC SEP, Sep-17/18 BOJ MPM → RELEASES.md).

**Runway:** 38d to furthest event (Aug-28 2Y + Tokyo CPI). 3 events next 7d (Jul-22 40Y, Jul-24 CFTC gate + National CPI). Healthy; the Run-11 August delta (applied by SAM) carries the feed past Jul-31.

**Runtime:** ~single pass. Did NOT commit/push — left for SAM.

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

**Pre-fire-week cadence-derived date verification (per [[finding_subagent_prefire_date_verification]]):**
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

> ### ✅ SAM RULING — Run-16 escalation 1, resolved same session 2026-08-17
> **Q: elevate the new MOF `feio/quarter/` Q3 row 🟠→🔴 to match the FRBNY Nov-13 row?**
> **A: 🟠 STANDS. Do not elevate.** You were right to flag it and right not to apply it — but the two rows are **not symmetric, and the asymmetry is about which question each one FIRST answers, not which authority is more definitive.**
>
> The FRBNY Nov-13 row is 🔴 because it is the **first and only** read of the **US leg's size and participation** — and participation is the genuinely open question on that file (capacity was settled and retracted 8/10: there is no balance-sheet ceiling at the $5-10B scale; what is unresolved is whether the US leg was Treasury/ESF-only or joint ESF+SOMA, which turns on a **committee vote**, not money).
>
> The MOF quarterly is the **Japanese** leg — and I will already know the Japanese leg's size and hard confirmation from the **MOF monthly on ~Aug-31**, ten weeks earlier. The quarterly adds **per-op granularity to something already answered**. Confirmatory depth ≠ first answer. **🟠 is the correct grade for a row that refines a known quantity; 🔴 is for the row that resolves an unknown one.**
>
> ✅ **Your framing that the two now "converge on the same window" is the genuinely valuable part and I have kept it** — two independent primaries (MOF ~Nov-9, FRBNY ~Nov-13) bracketing the same op record is a real cross-check, and neither is load-bearing alone. **Closing the Run-5 date-pin PENDING (open since 2026-06-03) with an own-primary verification is exactly right.**
>
> *(Escalations 2 and 3 need no ruling: 2 was a verification report — all clean, confirmed independently at the artifacts this session; 3 correctly closed the three superseded Run-15 PENDING items per my pre-edits.)*


### ✅ CLOSED at Run 16 (2026-08-17) — all three Run-15 escalations, per SAM's pre-edit rulings + this run's own resolution

1. **MOF weekly BND-11 (#1) — CLOSED.** SAM ruled (pre-edit, seeded ahead of Run 16): the 3-week single-print test is SPENT/INCONCLUSIVE (bar = 0.49σ of the series' own dispersion — inside noise); single-week form STOOD DOWN; a 4-week rolling-sum replacement is proposed to BOND, who ratifies (BND-11 is BOND's gate). **No forward MOF-weekly TSV row added.** New datum this run (not a verdict): wk 8/2-8/8 printed **+¥1,629B BUYING**, largest in the tracked series; 4-wk rolling ~flat +¥572B — routed to BOND as a datum. The ≥¥1.5T stress line stays separate and live.
2. **BOJ current-account `jd20260804.xlsx` 404 (#2) — CLOSED.** RETRACTED 2026-08-14: the "dead archive" claim was SAM's own missing-year-subdirectory URL error (`jd/<YYYY>/`), not a dead source. All 3 ladder legs now FINAL. Row removed from both docket files this run (11d old, past the >7d bar — went straight to the pruned-note; see LAST RUN Run-16 §1).
3. **Sep 15-16 FOMC route-4 "COLD" characterization (#3) — CLOSED.** Re-rated COLD → LIVE-but-UNFIRED (~7-8%/60d) on the 8/7 NFP, propagated into both docket files' Sep-16 FOMC rows same day. Verified this run: no bare "COLD" (as a current-state claim) survives anywhere in either file — every occurrence is the transition arrow "COLD → LIVE-but-UNFIRED," which is the correct historical framing, not a regression.

*(Original Run-15 escalation text retained below for audit trail.)*

### 🆕 (Run 15, 2026-08-07) — three escalations, all CLOSED above at Run 16

1. **MOF weekly BND-11 3rd-week confirm resolved NO VERDICT — resolver has no post-8/6 terms.** The 7/26-8/1 print (+¥478B) reverses the two prior SELL weeks but misses the registered ≥+¥500B durable bar by ¥22B — a dead-middle result the original 3-week test didn't anticipate. **SAM needs to either (a) set new resolver terms for a future MOF weekly print (and if so, which one — the row would need to stay `type=sam-internal` under the Run-14 CALIBRATION gate-bearing-carve-out generalization), or (b) explicitly stand the gate down** until a new live question exists. Left as a plain RECENTLY RESOLVED entry with no forward row re-added — KOYOMI does not own that call.
2. **BOJ current-account `jd20260804.xlsx` — 404 persistence now n=3 sessions** (8/4 discovery, 8/6, 8/7). Still owed, still open, not pruned. If it's still 404 next run, worth a primary-page-structure check (is the URL pattern/filename convention still correct, or did the file simply never get produced for this settlement date) — flagged, not investigated; outside KOYOMI's remit to debug the MOF/BOJ source itself.
3. **Sep 15-16 FOMC route-4 "COLD" characterization may be stale after today's NFP.** −23K with −103K net May/June revisions; Sep Fed hike odds repriced 57% → 43.9% (per spawn packet, not independently re-verified by KOYOMI this run — no primary source named). This is an analytical judgment call (whether/how "COLD" should move) — left the CATALYSTS.tsv/CALENDAR wording exactly as-is. SAM to assess and, if warranted, edit the Sep-16 FOMC row's threshold_signal directly.

### ✅ SAM RULINGS on Run-14 escalations (2026-08-02, same session)

1. **KOYOMI.md repo path — FIXED by SAM this session** (`/home/user/` → `/home/willi/`). Good catch; a fresh spawn without the correction resolves every path against a nonexistent directory. Cleared.
2. **Thu 8/6 MOF-weekly row — RULING: KEEP, and the carve-out GENERALIZES.** You flagged the right row as the scope-stretch and asked the right question. **New CALIBRATION ruling: the gate carve-out is not CFTC-specific — it is a *gate-bearing* test.** An otherwise-EXCLUDED auto-pulled class earns a TSV row when, and only when, **that specific release is a named discriminator for a live, written-down question** (here: the 3rd-week confirm of the SELL reversal that overturned the 7/16 BND-11 durable read). Routine prints of the same class stay excluded; the row retires when the question resolves. Apply this going forward without re-escalating.
3. **MOF weekly cadence Sat–Fri vs Sun–Sat labels — ✅ RESOLVED BY SAM 2026-08-04, in your favour on the substance.** You were right that both labelings cannot be correct and that BND-11's 3rd-week confirm is read off the labels. **Adjudicated against the PRIMARY rather than by preference:** MOF's own period strings in `workbook/MOF_FLOWS.tsv` are **6-of-6 Sunday→Saturday** (7/19 Sun→7/25 Sat · 7/12→7/18 · 7/5→7/11 · 6/28→7/4 · 6/21→6/27 · 6/14→6/20). ⇒ **`docket/RELEASES.md`'s "Sat–Fri" cadence rule was the error and is corrected; STATUS/CALENDAR were right all along.** The Aug-6 label "wk 7/26-8/1" is CORRECT and the 3rd-week confirm reads as written — cleared **before** the print, not after. **Escalating instead of guessing was the right call; the cadence rule was SAM's to own.** Cleared.
4. **BLS 403 now n=2 with curl+UA — ACCEPTED as dead, not flaky.** Stop re-attempting the old workaround each run. Sep-11 caveat stands as ruled.
5. **TERRY re-mark + Oman fee-window deliberately NOT added — CONFIRMED, correct on both.** The TSV is an observable/gate feed, not a task tracker, and "~Aug 16" fails the date-specificity bar. Do not add either.
6. **SAM-39 reminder in the Aug-7 row — ACCEPTED**, good use of the boot surface. If SAM writes SAM-39 before Friday, the row's threshold_signal gets re-pointed at the prediction ID.
7. **New standing monitor on the 7/31 candidate op — ACCEPTED and explicitly endorsed.** Watching that an unresolved event does not harden into stated fact through repetition is exactly the right instinct; the load-bearing wording is deliberate. Keep it until 8/5 (BOJ current account) or ~8/31 (MOF monthly) resolves it either way.

**Run-14 quality note (SAM):** clean run. The countdown verification (8 fields × 28 rows, date-sort diff, jgb_auctions token filter, rc=0) is the standard — and correctly distinguishing the tool's 45-day horizon truncation from an actual feed gap is the kind of thing a careless run reports as a bug. 12/12 September rows applied, 3 discriminators added, 0 declined.



- **🆕 NEW (Run 14) — ⚠️ `KOYOMI.md` ORIENTATION carries a STALE working-directory path.** Line 11 says the repo root is `/home/user/Research-workspace`; the actual root is **`/home/willi/Research-workspace`**. Surfaced by SAM on this run's spawn and worked around, but the spec is what a fresh KOYOMI reads first — a sub-agent spawned without the correction would resolve every path in the brief against a directory that does not exist. **KOYOMI may not edit `KOYOMI.md` (explicitly out of the write-set) — SAM must fix the line.** One-word change.
- **🆕 NEW (Run 14) — MOF weekly ITS week-LABEL convention conflict.** `RELEASES.md` cadence rule says the reporting week runs **Sat–Fri**; STATUS/CALENDAR label weeks **Sun–Sat** ("wk 7/19-25", "wk 7/26-8/1"). The *release date* is unaffected either way (Thursday), so nothing in the docket is mis-dated — but the two conventions cannot both be right, and BND-11's 3rd-week confirm is being read off the labels. Noted in the RELEASES row; **SAM owns the cadence rules, KOYOMI does not.** Low urgency, resolve before the 8/6 print if convenient.
- **🆕 ESCALATION-LOG (Run 14) — 3 sam-internal rows APPLIED as defaults, veto-able in one line each.** All three are dated action-forcing discriminators that STATUS § WHAT TO WATCH carried with no docket row: **Tue 8/4** BOJ c/a `jd20260803` (7/30 op semi-confirm, 🟠) · **Wed 8/5** BOJ c/a `jd20260804` (7/31 candidate-op discriminator, 🔴 — feeds the memo §5C early-entry override) · **Thu 8/6** MOF weekly 3rd-week BND-11 confirm (🟠). Applied per the TSV-SCOPE PRECEDENT rather than round-tripped. ⚠️ **The 8/6 MOF-weekly row is the scope-stretch** — MOF weekly is an explicitly EXCLUDED class in the spec universe, admitted here on the same logic SAM used to admit gate-bearing CFTC prints in the Run-12 CALIBRATION amendment. **If any of the three is wrong, it is that one.** A ruling either way would be useful as precedent (does the CFTC gate-print carve-out generalize to other excluded auto-pulled classes, or is it CFTC-specific?).
- **🆕 NEW (Run 14) — two dated items deliberately NOT added to the TSV; SAM to confirm or overturn:** (a) **Mon 8/3 TERRY re-mark of TRY-FIRE-005** (Will-approved, PROME-tasked; Aug-21 tenor excludes the Sep 17-18 MPM) — date-specific and action-forcing, but it is an *assigned cross-agent task*, not an observable release or a SAM decision gate; adding it would make the TSV a task tracker. Left in STATUS. (b) **~Aug 16 Oman fee-administration / 60-day toll-free window close** — genuinely dated-ish but geopolitical and imprecise ("~"); kept as CALENDAR GEOPOLITICAL narrative per the no-prose-dates TSV rule. Say the word if either should be a row.
- **🆕 NEW (Run 14) — forward-looking, informational:** STATUS itself flags "⚠️ Consider formalizing the 8/7 resolver as **SAM-39** before the print — writing the registered §5B terms as a scored row before Friday converts a disposition into a calibration datum." **Analytical, so KOYOMI took no action** beyond ensuring the Aug-7 TSV row's `notes` field carries the reminder where the boot countdown will surface it. If SAM writes SAM-39, the Aug-7 row's threshold_signal should be re-pointed at the prediction ID.
- ✅ **APPLIED (Run 14, per SAM ruling 2026-08-02) — the Run-13 September baseline-audit delta: all 12 rows landed in CATALYSTS.tsv + a new CALENDAR SEPTEMBER section**, priorities/who_cares exactly as proposed. Row #9 (Sep-18 window-end retire-check) written with SAM's ruled action-language and marked in both files as the template for future eligibility-window checks; row #4 (US CPI Sep-11) retains the secondary-source provenance caveat (primary re-verify re-attempted 8/2 → BLS 403 again, n=2); Tokyo Sep CPI confirmed out-of-window (Oct-2) and carried to the October audit; no September CFTC row. *SAM may clear the original proposal block below.*
- **🔍 (Run 13 — ORIGINAL PROPOSAL, retained for audit) — MONTHLY BASELINE AUDIT DELTA (September), PROPOSE-ONLY — SAM to apply/decline row-by-row.** All dates source-confirmed 2026-07-31 (URLs in RELEASES.md Confirmed dates). Suggested priority/who_cares are KOYOMI defaults; SAM owns the thesis lens. **Two items below need SAM's read before the rest: the Sep-18 triple-stack and the new sam-internal candidate row (#9).**
  | # | Date | Event | Sugg. pri | Sugg. who_cares | Rationale |
  |---|------|-------|-----------|-----------------|-----------|
  | 1 | 2026-09-01 | JGB 10Y auction | 🟡 | SAM,LIQUID | MOF Sep calendar; belly continuation. |
  | 2 | 2026-09-03 | JGB 30Y auction | 🟠 | SAM,LIQUID,BOND | Demand-vacuum/bid-real series continuation, first super-long after Aug-6. |
  | 3 | 2026-09-08 | Japan Q2 GDP — 2nd preliminary (Tue 8:50 JST) | 🟡 | SAM | Revision of the Aug-17 1st prelim; ESRI-confirmed (reused Run-11 pre-confirm). |
  | 4 | 2026-09-11 | US CPI (August data), 8:30 ET | 🟡 | SAM,HENRY | Route-4 inflation leg. ⚠️ Date confirmed via 2 cross-checked secondary sources only — BLS primary 403'd on both WebFetch and curl+UA this session (worse than the Jun-10 precedent). Worth a primary re-verify next session if BLS is reachable. |
  | 5 | 2026-09-15 | JGB 20Y auction | 🟡 | SAM,LIQUID | MOF Sep calendar; strike-broadening watch continues. |
  | 6 | 2026-09-16 | FOMC decision (Sep 15-16, SEP meeting) | 🔴 | ALL | Dot-plot meeting; reused Run-11 pre-confirm; same week as the BOJ Sep MPM. |
  | 7 | 2026-09-16 | Japan trade balance, August (provisional whole-month) | 🟡 | SAM | Monthly universe class; same 3rd-date-column convention as Jun/Jul rows. |
  | 8 | 2026-09-18 | BOJ MPM day 2 decision (Sep 17-18; no Outlook Report) | 🔴 | ALL | Reused Run-11 pre-confirm. **⚠️ Lands the SAME DAY as row #9 below AND the National Aug CPI (row #10) — a triple-stack event day.** |
  | 9 | 2026-09-18 | **Convexity-tail window-end retire-check (SAM-internal, THESIS leg-2 SPF)** | 🔴 | SAM,PROME | **NEW candidate — not previously in PENDING.** Per THESIS § Eligibility window (locked Sep-18-2026): if NO eligible trigger has fired by Sep-18 close (risk-off shock / Fed-dot walk-back / oil-MOU re-escalation / MOF #3), convexity-tail RETIRES to LOW; runs AFTER the BOJ decision same day (window is INCLUSIVE of Sep-18, THESIS-clarified 7/2 — a trigger fired BY that decision counts as in-window). DATE-SPECIFIC + ACTION-FORCING (retire disposition is pre-registered) → qualifies under the TSV-SCOPE PRECEDENT, but KOYOMI is flagging rather than treating as self-resolving because this is the FIRST time the window-end check itself becomes a proposed row (distinct from the routine weekly-CFTC-gate class the precedent was built for) — wanted SAM's explicit read on the row's action-language before it becomes a template for future eligibility-window checks. |
  | 10 | 2026-09-18 | Japan National CPI, August | 🟠 | SAM | Monthly universe class. Same day as #8 and #9 — see triple-stack flag. |
  | 11 | 2026-09-29 | JGB 40Y auction | 🟠 | SAM,LIQUID,BOND | No 40Y auction in August — first since Jul-22. |
  | 12 | 2026-09-30 | JGB 2Y auction | 🟡 | SAM,LIQUID | Front-end demand. |
  Out-of-universe / flag-only (NOT proposed): MOF Sep liquidity-enhancement auctions Sep-10 + Sep-25 (excluded per universe rule, same as prior months). **⚠️ Tokyo September CPI (prelim) does NOT land in September — Stats Bureau's own schedule shows it releasing Oct-2** (breaking the same-month/near-month-end pattern every month Apr-Aug followed; the audit brief's assumption of "~end-Sep" was wrong on this one — flag for the October audit, don't let it get silently missed since it falls just outside this window). No CFTC weekly row proposed for September: per the CALIBRATION ruling, routine prints stay excluded and no live pre-registered September-specific SAM-NN tripwire currently exists (the Jul-31/Aug-7 gate rows are scoped to the 7/30 spike attribution, not an open-ended standing gate) — SAM should add one only if a new tripwire gets registered before then.
- ✅ **RESOLVED (Run 12, SAM 2026-07-21) — Jul-24 CFTC gate row KEPT + CALIBRATION amended.** SAM ruled: pre-registered CFTC decision-gate prints DO qualify for a `type=sam-internal` TSV row (see the updated CALIBRATION ruling — routine weekly prints still excluded, but a print with a live SAM-NN tripwire within striking range gets a gate row). The Jul-24 print (SAM-29 leg-1 −108K, 14.7K away) is the reference case. Future runs self-resolve — no re-escalation. *(This was an active SAM adjudication, not a rubber-stamp — logged to the guard tally below.)*
- ✅ **[SAM 2026-07-02: ALL 14 APPLIED same-session** (CATALYSTS + CALENDAR incl. new AUGUST section); TB-in-TSV conflict RULED INCLUDE (see CALIBRATION); Aug-21 carries the 2025-base discontinuity warning; Sep-18 window-end coincidence documented in THESIS + SAM-28.**]** - **🔍 NEW (Run 11) — MONTHLY BASELINE AUDIT DELTA (Jul + Aug), PROPOSE-ONLY — SAM to apply/decline row-by-row.** All dates source-confirmed 2026-07-02 (URLs in RELEASES.md Confirmed dates). Suggested priority/who_cares are KOYOMI defaults; SAM owns the thesis lens:
  | # | Date | Event | Sugg. pri | Sugg. who_cares | Rationale |
  |---|------|-------|-----------|-----------------|-----------|
  | 1 | 2026-07-14 | US CPI (June data), 8:30 ET | 🟠 | SAM,HENRY | STATUS names it explicitly: route-4 (Fed-dot walk-back) inflation leg — "labor blocker cracked, inflation leg intact; watch Jul-14 CPI." Same day as JGB 20Y (already a note on that row). Highest-value gap in the set. |
  | 2 | 2026-07-22 | Japan June trade balance (provisional) | 🟡 | SAM | TIMELINE: "the clean Phase-1-inversion test is the next TB print" = this one. Same day as 40Y auction. ⚠️ Universe table says include monthly, but Run-10 hint claimed "not a TSV row (boot.py handles it)" — conflict for SAM to adjudicate; May TB WAS a TSV row (Run-8/9). |
  | 3 | 2026-07-24 | Japan National June CPI | 🟡 | SAM | Monthly universe class; follows the sticky Tokyo June print (core-core 1.9). |
  | 4 | 2026-07-31 | Tokyo July CPI (prelim) | 🟠 | SAM | Releases the MORNING of the BOJ Jul-31 decision (JST) — same-day input to the SAM-34 hold@85% read. |
  | 5 | 2026-08-04 | JGB 10Y auction | 🟡 | SAM,LIQUID | MOF Aug calendar; follow-on to the softer Jul-2 10Y (tail ~4×). |
  | 6 | 2026-08-06 | JGB 30Y auction | 🟠 | SAM,LIQUID,BOND | Next super-long after Jul-7/Jul-22 — extends the demand-vacuum/bid-real test series past the Jul-31 FY2027 purchase-plan decision. |
  | 7 | 2026-08-12 | US CPI (July data), 8:30 ET | 🟡 | SAM,HENRY | Route-4 inflation leg, post-Jul-29-FOMC read. |
  | 8 | 2026-08-17 | Japan Q2 GDP 1st prelim (Mon 8:50 JST) | 🟠 | SAM | Quarterly universe class; wage/activity mechanism input to the next-hike path. |
  | 9 | 2026-08-18 | JGB 5Y auction | 🟡 | SAM,LIQUID | MOF Aug calendar (belly). |
  | 10 | 2026-08-20 | JGB 20Y auction | 🟡 | SAM,LIQUID | MOF Aug calendar; strike-broadening watch. |
  | 11 | 2026-08-20 | Japan July trade balance (provisional) | 🟡 | SAM | Monthly universe class (same adjudication as #2). |
  | 12 | 2026-08-21 | Japan National July CPI — ⚠️ FIRST release on the 2025 base | 🟠 | SAM | See 2025-base escalation below — a measurement discontinuity, not just a print. |
  | 13 | 2026-08-28 | JGB 2Y auction | 🟡 | SAM,LIQUID | MOF Aug calendar (front end). |
  | 14 | 2026-08-28 | Tokyo August CPI (prelim) | 🟡 | SAM | Monthly universe class. |
  Out-of-universe, flag-only (NOT proposed): Aug-12 10Y JGBi + Aug-24 Climate Transition Bond auctions (outside the 2Y/5Y/10Y/20Y/30Y/40Y tenor set — say the word if the thesis lens wants JGBi as an inflation-expectations read); no 40Y auction in August; no BOJ MPM or FOMC in August (next: BOJ Sep 17-18, FOMC Sep 15-16 SEP — both already RELEASES-confirmed).
- **⚠️ NEW (Run 11) — 2025-BASE CPI REVISION lands with the National July CPI (Aug-21).** The Stats Bureau schedule row carries "Revision to 2025-Base Consumer Price Index," and the CPI index page confirms 2025-base monthly reports begin Aug-21 (with base-revision releases Jul-10 / Aug-7). Base-year rebasings historically shift measured core (2020-base shaved core readings) — SAM's CPI-anchored levels (subsidy-wedge math, core-core stickiness reads, BOJ-mechanism framing) will need a discontinuity check at that print. Analytical — KOYOMI took no action beyond the RELEASES note.
- **⚠️ NEW (Run 11) — Sep-18 BOJ MPM decision lands EXACTLY ON the LOCKED Sep-18 convexity window-end** (and FOMC Sep 15-16 SEP is the same week). Whether the window-end evaluation should run before/after that decision day is a thesis call — flagging the coincidence only. (Both dates RELEASES-confirmed this run.)
- **NEW (Run 11) — BOJ SoO for the Jul MPM: fetch showed "Aug 8" — suspect** (Saturday; likely summarizer garble of the BOJ page). SoO is outside the audit universe; SAM added the Jun-24 SoO row manually last cycle — if wanted for Aug, verify the date at the BOJ page first.
- **Phase 2 Watch section reframe** may be needed if MOU walks back (Trump-Khamenei reset → Brent collapse → Phase 2 re-engages). Pre-emptive flag from Run 3. SAM-domain trigger. *(No MOU walk-back through Run 10; Brent ~$74 deeply dormant. Watch.)*
- **MOF quarterly per-op intervention release date verification (Run 5) — ✅ CLOSED (Run 16, 2026-08-17).** Fetched at primary (`feio/quarter/`, not `feio/quarterly/` — the path in this note was wrong): Q2 2026 (Apr-Jun) published Aug-7 with the per-op breakdown (¥11,734.9B, matching STATUS's known aggregate), Q1 published May-12. Cadence derived (+38-42d post quarter-end) and a forward Q3 row added at ~Nov-9, priority 🟠 (not 🟡 as this note originally suggested — SAM ruled 🟠 stands, see PENDING escalation-1 ruling above). *SAM may clear this line.*
- **Sato verification provenance (Run 6, INFORMATIONAL):** All 5 claims primary-source verified Jun 4. RELEASES.md schema question (board-composition section?) still open for SAM.
- **✅ RESOLVED by SAM (Run-8/9) — CATALYSTS.tsv schema regression + CFTC EV-gate row + resolved-event TSV migration.** *SAM may clear these items.*
- **TIMELINE.md stale (Runs 9-10 flag) — ✅ SATISFIED (Run-11 verified):** SAM backfilled Jun-17-20 (2026-06-22) + the Jun-22→Jul-2 cluster block (2026-06-30/07-01/07-02); TIMELINE current through Jul-2. *SAM may clear.*
- **GEOPOLITICAL WATCH >7d rows (Runs 9-10 flags — 3rd flag, now 18-22d):** Jun 10-11 kinetic (**22d**), Jun 12 14-pt draft (**20d**), Jun 14 Brent sub-$90 (**18d**) — plus Jun-17 deal-signed (15d) + Jun-20 re-closure (12d) now aging too. KOYOMI still did NOT prune (SAM's analytical watch surface). **SAM should prune to the Ongoing row + TIMELINE pointers, or explicitly retain-for-context.**
- **Jun 10 US CPI primary-source verification (Run 7 backlog) — ✅ DONE (Run 11):** BLS schedule reachable via curl + User-Agent (WebFetch alone 403s — [[finding_edgar_403_user_agent_header]]); Jun-10 = May-data release, RETROSPECTIVE-CONFIRMED appended to RELEASES.md 2026-07-02. *SAM may clear.*
- **JGB 2Y Jun 30 auction result (Run 10) — ✅ SATISFIED:** result logged by SAM (BTC 4.82x / tail 0.3bp / WA 1.407% vs May 1.369) in STATUS/CALENDAR/TIMELINE. *SAM may clear.*

---

## STANDING MONITORS (surface each run)

- **BOJ pre-meeting blackout windows** (T-2 of each MPM) — kept as narrative in CALENDAR, not in TSV per form-consistency call from Jun 1. The Jul-29 blackout passed with the MPM itself. Next blackout = **~Sep 15 (T-2 of the Sep 17-18 MPM)** — now noted on the Sep-15 20Y auction row (same date), so it surfaces without needing its own row.
- **Recurring weekly catalysts** (CFTC release Fri/Mon) — not in TSV (handled by `cftc_jpy.py` auto-pull) EXCEPT when a specific release is a pre-registered SAM-internal decision gate. **Current: ONE gate row live — Fri Aug-7 (Aug-4 data).** The Jul-31 row resolved (the −153K/85% line FIRED at −163,412/90.8%) and was migrated this run. **Aug-7 is now doing double duty: the 7/30-op attribution print AND the pre-registered ENTRY resolver** (memo §5B terms) — i.e. it is a higher-stakes row than when it was added. After it resolves the class goes dormant again unless a new tripwire is registered; **no September CFTC row exists** for exactly that reason.
- **Post-meeting catalyst-window refill** — **Live: healthy, runway 84d** (Nov-13 FRBNY Q3, now paired with the new Nov-9 MOF Q3 row — Run-16). September is fully seeded through Sep-30; the Nov cluster is the only entry past that. Next thin point is still the **Oct boundary** — the October audit (first run of October) is the scheduled refill (Tokyo Sep CPI Oct-2 already flagged so it isn't missed). The 45-day countdown horizon currently reaches through Sep-30 cleanly (all September rows render); the two Nov rows correctly do not render yet — tool horizon, not a docket gap, don't "fix" it by re-adding rows.
- **MOF auction calendar alteration page** — `auction/calendar/26MMae.htm` records mid-month tenor-band changes. 2607ae/2608ae 404 (Run 11); **2609ae 404 (Run 13)**. Not re-checked Run 14 (no audit trigger; only 2 days elapsed). **Re-check due early September**, or at the October audit — whichever comes first. Now flagged in RELEASES.md too.
- **SAM-internal review triggers (Run 5; scope precedent in KOYOMI.md):** **TWO sam-internal rows live in forward TSV as of Run-16** — ~Mon Aug-31 MOF monthly · **Fri Sep-18 convexity-tail window-end retire-check (now a grading row).** Both render 🔧 (verified this run). Down from 4 at Run-15: the Aug-6 BOJ c/a row resolved off (retracted/FINAL, this run) and the Aug-7 CFTC gate row resolved off (frame broke 8/7, migrated to RECENTLY RESOLVED by SAM's own edits pre-Run-15). **The MOF-weekly gate-bearing carve-out stays dormant** pending BOND ratification of the 4-week terms (PENDING #1, CLOSED-but-monitored). **The Sep-18 row remains the reference template for eligibility-window checks** (SAM-approved 2026-08-02), now correctly re-scoped to GRADING-only per the 8/13 correction.
- **✅ CLEARED (Run 15) — Unresolved-event hygiene monitor (Run 14):** the 7/31 candidate MOF op resolved (US Treasury, confirmed 8/2, hard-evidenced 8/4) before this run started; the monitor's job is done. No open live-and-unresolved event of that shape currently in the docket — the BOJ c/a 404 is a *missing data* open item, not an ambiguous-fact one, so it doesn't need the same "don't let it harden" framing.
- **MOF weekly BND-11 resolver — RULED (Run 16 update):** SAM ruled the single-week form STOOD DOWN (0.49σ bar = inside noise) and proposed a 4-week rolling-sum replacement to BOND for ratification. **Still no forward MOF-weekly TSV row** — correct per the ruling, do not add one absent a BOND-ratified 4-week gate. wk 8/2-8/8 printed +¥1,629B (largest in series; 4-wk rolling ~flat +¥572B), routed to BOND as a datum. Watch for BOND ratification + SAM relay of the new 4-week terms — that is the trigger for a new `type=sam-internal` row (under the Run-14 CALIBRATION carve-out), not a single strong print.
- **MOF `feio/quarter/` per-op quarterly release (new monitor, Run 16; priority RULED same day):** tracked at ~Nov-9 (Q3, Jul-Sep) alongside the pre-existing FRBNY Nov-13 row — two independent primaries (Japan MOF / US NY-Fed) converging on the same window for the 7/30-31 op record. **Priority stays 🟠 (SAM ruling 2026-08-17) — do not elevate to 🔴**; FRBNY is the first/only read of the open question (US-leg participation), MOF only refines an already-known Japanese-leg figure. Both dates are cadence ESTIMATES, not announced; re-confirm both at their respective index pages in early November (same window as the MOF alteration-page re-check below).
- **BOJ OIS instrument flagged SUSPECT by SAM (new monitor, Run 16):** Sep reads 51.0% with +0.0pp movement across two consecutive as-of dates while the JGB 2Y cash market sold off to a series high — a stale-instrument pattern (price moving, the derived probability not). **Standing docket rule reinforced:** never restate a BOJ percentage in CALENDAR/CATALYSTS; cite `workbook/BOJ_OIS.tsv` only. One surviving restated band (from the 8/6 repricing) was found and deleted from the Sep-18 grading row's TSV notes this run — if a percentage resurfaces in any docket row on a future sync, delete it again rather than refreshing it.
- **🆕 Japan CPI dual-base publication (new monitor, 2026-08-17 closeout pass):** `cpi_japan.py` fixed same-day (statsDataId + Tokyo cdArea both updated for the 2025 rebasing); the Aug-21 National CPI print is expected to resolve normally now, not as a blocked/manual row. **Both the 2020-base and 2025-base series publish in PARALLEL through Dec-2026** — watch that no future docket row (CALENDAR or CATALYSTS) implies a clean single-base switchover on 8/21 or any other date before Dec-2026; cite the base explicitly whenever a CPI reading is quoted.
- **BOJ board composition transitions (Run 6):** Sato Jun-30 RESOLVED (took seat). Next composition event: TBD (other Policy Board terms expire 2026-2030 — baseline against BOJ page needed). RELEASES.md schema still doesn't cover board-composition events; flag for SAM if/when the next transition approaches.

---

## NEXT RUN HINTS

*Rewritten 2026-08-17 post-ruling (closeout pass) — the version written at Run-16's own end described a pre-ruling
state and is superseded by this one. Do not resurrect the struck items below; they are closed.*

> ### 🔒 Standing rule, restated after Run 16 found a live violation: **never hand-carry a percentage, route
> weight, or grade forward in a hint or a docket row.** Cite the owning artifact (`workbook/BOJ_OIS.tsv`,
> `thesis/PREDICTIONS.tsv`, STATUS) and re-read it fresh every time. Run-16 found and deleted a restated
> "~40-54% unpriced" BOJ band sitting in the Sep-18 grading row's TSV notes since 8/6 — untouched for 11 days
> because nothing re-reads notes fields on a routine sync. **If a percentage resurfaces in any docket row, delete
> it, do not refresh it** — that is the standing fix (SAM, 2026-08-17). *(This closeout pass applied the rule to**
> **itself: this section cites no BOJ/route/grade figure, only pointers to owning artifacts.)*

- **Next run's first job: check whether the Aug-18 JGB 5Y, Aug-20 20Y+TB, and Aug-21 CPI/CFTC rows resolved and migrate them.** All four are inside the imminent window as of Run 16 and will likely have printed by the next sync. The Aug-20 20Y is the **near-term Pillar-2 adjudicator** (promoted 🟡→🔴 8/17) — grade it on auction internals (BTC/tail), not the yield level (SAM-26 trap), per the row's own instruction.
- **Aug-21 CPI row — instrument status CHANGED same-day, do not carry the earlier "blocked" framing forward.** SAM fixed and live-verified `cpi_japan.py` on 2026-08-17: the `ESTAT_APPID`-absent half of the original block was **RETRACTED** (the key was in the repo-root `.env` the whole time — checking one location and inferring the capability gone was the actual defect). The real fix was **two rebasing parameters**: `statsDataId 0003427113 → 0004052037` and Tokyo `cdArea 13A01 → 13100` (the latter fails as a **success-shaped empty response**, not an error, if missed — a gotcha for any future series-id migration, not just this one). **⚠️ Both 2020-base and 2025-base publish in PARALLEL through Dec-2026 — this is not a clean cutover on 8/21.** If any docket row (present or future) implies a single-base switchover, correct it; `CPI.tsv` now carries a `Base` column, `--base 2020|2025` is explicit. The Aug-21 row should now resolve as a normal print, not a blocked/manual one — check the actual pull outcome rather than assuming either the old-blocked or the new-fixed framing.
- **MOF Q3 row priority — RULED, do not re-raise.** SAM ruled 2026-08-17: the MOF `feio/quarter/` Q3 row (~Nov-9) stays 🟠, is NOT elevated to 🔴 alongside FRBNY (~Nov-13). Reasoning worth preserving as a general pattern: FRBNY's row is 🔴 because it's the first/only read of an open question (US-leg participation); MOF's row only adds granularity to a figure the MOF monthly already answers ~Aug-31 — **confirmatory depth is not a first answer**, so it doesn't earn the higher grade even though it's arguably the more "authoritative" primary. Row text updated to record the ruling — don't leave a "SAM to decide" question sitting in a row once SAM has decided.
- **BND-11 (MOF weekly) stays dormant — do not add a forward MOF-weekly TSV row on a strong single print.** The 8/2-8/8 print is a **datum for BOND**, not a re-opened gate (the single-week form is STOOD DOWN by SAM's own dispersion-based ruling). Only act if SAM relays BOND-ratified 4-week rolling-sum terms — then apply the TSV-SCOPE + Run-14 CALIBRATION gate-bearing carve-out without re-escalating the mechanics.
- **Sweep for restated BOJ percentages every run, not just when flagged.** Run-16 found one that had survived 3 syncs (8/6→8/17) because it was buried in a `notes` field nobody greps. A quick `grep -n "%" docket/CATALYSTS.tsv docket/CALENDAR.md` around any BOJ/OIS-adjacent row before closing out is cheap insurance.
- **"COLD" sweep:** verified clean at Run 16, independently re-confirmed by SAM same session (3 hits, all the legitimate "COLD → LIVE-but-UNFIRED" transition arrow, none a bare current-state claim). Keep checking every run — if a future sync ever shows bare "COLD" with no arrow, that's a regression.
- **Header/state-line drift — checked this closeout pass, none found in `docket/`.** This defect class hit 3 other files fleet-wide today (stale "Last run"/"Last Updated" lines feeding a false premise into a spawn brief). `CALENDAR.md`'s own header is current (dated 2026-08-17, this run). `CATALYSTS.tsv` had ONE instance of the same defect — a row's `notes` field still asking "SAM to decide" after SAM had already decided (the MOF Q3 priority item above) — found and fixed this pass. **Grep a docket row's own notes field for open questions before assuming a ruling propagated everywhere it's referenced**, not just in KOYOMI_MEMORY.md.
- **Gov-site fetch craft:** BLS 403s on **both** WebFetch and curl+UA — durable block, not flaky (n=2, last checked 8/2). Fall back to 2+ cross-checked secondary sources and state the gap explicitly. Stats Bureau `1582.html` is truncated by the WebFetch summarizer — always curl and parse the raw HTML table. MOF's `feio/quarter/` index page itself doesn't carry publish dates — fetch the individual `<year>_<N>Qe.html` report page directly for the dateline (learned Run 16).
- **Next MONTHLY BASELINE AUDIT = first run of October.** July/August/September are all applied and live; the Nov cluster (MOF Q3 + FRBNY Q3) is seeded past that. Head start already in RELEASES: **Tokyo September CPI = Oct-2**. Block ~10-12 min for MOF Oct+Nov (+ the alteration pages) / BOJ Nov / Stats-Bureau / BLS / ESRI. ⚠️ **Also re-check the MOF `2609ae` alteration page in early September** — still not due (last checked 7/31, 404) — September's auction set is fully seeded, so a mid-month alteration is the one thing that could silently invalidate five applied rows.
- **Flagged for SAM (open, carried forward):** (a) Tokyo September CPI lands **Oct-2**, not in September — must not be missed at the October audit boundary. *(The 2025-base CPI discontinuity item that lived here previously is now RESOLVED — see the Aug-21 CPI hint above; not carried forward as open.)* (b) the new-base `Base` column / `--base` flag in `CPI.tsv` is a schema change to a workbook file KOYOMI doesn't own — if a future docket row needs to cite a specific base's reading, say which base explicitly, per the parallel-publication note above.

---

## CALIBRATION (SAM-owned — declined release classes + scope rulings; KOYOMI reads, never writes)

### Rulings as of 2026-07-02 (post Run-11)
- **Declined release classes:** none.
- **Trade balance in TSV: INCLUDE** (spec universe wins over the Run-10 hint; May-TB precedent). Monthly TB rows are in-scope.
- **CFTC weekly prints: EXCLUDED by default, but pre-registered decision-gate prints DO qualify (SAM ruling 2026-07-21, Run-12 — supersedes the prior 'stay EXCLUDED' ruling).** Routine weekly CFTC prints stay OUT of the TSV (boot.py auto-pulls; adding every weekly row = cadence creep). BUT a specific weekly print carrying a *live pre-registered SAM-NN tripwire within striking range* (e.g. SAM-29 leg-1 −108K within ~1 week's plausible move, or an active reclaim watch) DOES get a `type=sam-internal` gate row — it's DATE-SPECIFIC + ACTION-FORCING, the same class as the Jul-6/Jul-10 gate rows. **Self-resolving rule for future runs:** add the gate row when a live tripwire is within striking range of the coming print; prune after it resolves; do NOT re-escalate. *(The prior ruling under-counted the genuine gate character; the Jul-24 print with SAM-29 14.7K away is the reference case. Routine prints with no tripwire in range still stay out.)*
- **JGBi / Climate Transition Bond auctions: stay out-of-universe** (flag-only is right); revisit JGBi only if an inflation-expectations read becomes thesis-load-bearing.
- **Run-11 audit quality note:** 14/14 proposals accepted as drafted (priorities/who_cares unmodified) — the propose-only audit with staged rationale + RELEASES-confirmed dates is exactly the right shape; keep it.

### 🛡️ STANDING RUBBER-STAMP GUARD (SAM-owned metric, instituted 2026-07-02 performance review)
Track **declines-per-10-runs** here. A long streak of 100% acceptance is ambiguous between "well-calibrated proposer" and "rubber-stamping SAM" — the declines are the evidence that adjudication is real. **If 10 consecutive runs pass with zero SAM declines/modifications, the next run's apply pass must include an explicit adversarial read of at least 2 accepted items (write the reasoning here).**
- Tally as of Run-12: **Run-12 — SAM amended the CFTC-gate CALIBRATION ruling** (kept KOYOMI's row but reversed the prior 'EXCLUDED' stance → active adjudication, not a rubber-stamp). Prior: Jul-10 CFTC gate-row DECLINED (Run-11); TB-in-TSV conflict adjudicated (Run-11); Run-9 CFTC-row retention directive. Streak clock not triggered.
- **Run-15 (2026-08-07) — recorded honestly AGAINST the guard's purpose: ZERO declines, ZERO modifications to KOYOMI's own edits.** SAM accepted the run as delivered (migrations, prune, OIS band de-staling, the CALENDAR-missed-the-8/4-correction catch) and ruled on the two escalations *on top of* it — **but ruling on an escalation is not a decline**, and counting it as one would be exactly the self-flattery this guard exists to prevent. **Streak: 1 of 10.** *(Mitigating, not exculpating: Run 15 escalated rather than decided on both analytical items, which is the behaviour the spec asks for — there was genuinely little to decline. The guard still counts it.)*

