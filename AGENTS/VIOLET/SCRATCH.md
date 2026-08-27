# VIOLET SCRATCH — August 27, 2026 (Thu, evening session ~19:15 ET — **FLAT. GATE-VIO-RV1 PERMANENTLY RETIRED. Thesis v3.9 → v4.0.**)

> **Scope as given:** *"work some of the incomplete work we had listed on SCRATCH. Lets start with 1, 2, and 3."* Then *"lets do the thesis bump"* after F2 returned KILL. Then *"go ahead with the terry packet"* before that. Then *"commit + push"* at closeout.
> **🔑 The session's shape: three registered blockers came due in one session and returned three clean verdicts. The first gate this desk ever base-rated before shipping got permanently retired by its own registered kill on the first session after its first arm — the discipline that version v3.9 was written for executing correctly.**

---

## CHANGES SINCE (this-boot-earlier ~14:20 → this-boot-now ~19:15)

Same-day rework session; prior boot had recovered the 6 dark days and posted the RV1 arm packet to PROME with F2/β as owed work. This session ran them.

---

## WHAT I DID

1. **🔴 RAN F2 → KILL.** Reproduced KB-VIO-207 on 5,086 aligned sessions (CBOE VIX/VVIX/SKEW History CSVs, own pull 8/27): 34 declustered episodes (+1 vs registered 33, the +1 is 8/19 = this cycle's live arm), 60td/≥+50% cond 59.4% / uncond 37.0% / p=0.008 — reproduction clean. Split at 2018-01-01: pre-2018 (n=12) 60td/+50% lift 1.92×, p=0.024 ✅; **post-2018 (n=22) lift 1.36×, p=0.134** ❌. Every post-2018 cell fails: 21td/+50% lift 0.78× (worse than uncond), 30td/+50% 0.92×, 60td/+15% 1.05×. Per KB-VIO-207 verbatim kill: *"if the post-2018 subsample loses separation the design does not deploy."* → **KB-VIO-211**, research file, packet PROME. GATE-VIO-RV1 permanently retired.
2. **✅ β RECONCILED: 0.274 was a bucketing bug.** Held sample-period fixed (all-contract on 12-month window): 21-35 β = 0.478. Held contract-mix fixed (M1-only on 13-year window): 21-35 β = 0.534. Reproduced packet method (M1-only, 12-month): 21-35 β = 0.533 — NOT 0.274. Loaded VX_M1_HISTORY.tsv directly with different bucket forms: **DTE≥21 unbounded** = 0.279/n=201 (exact match to packet's 0.274/n=200); DTE 21-35 correctly capped = 0.531/n=48. **The packet's "21-35 DTE" bucket had no upper cap** and pooled 136 obs at DTE>60 (β 0.16). Also: KB-VIO-208 mislabeled its comparator as "OPTION-IMPLIED" — same instrument, both futures-settle. Tenor-gradient story survives intact. → **KB-VIO-212**, research file, TERRY packet.
3. **✅ VIX9D INSTRUMENT BUILT.** thresholds.py fetches ^VIX9D (TICKERS + BANDS + FFWD_COLS + build_report + print_report); VX_DAILY.tsv gains vix9d + vix9d_vix_ratio cols (appended to end so positional indices survive); backfill.py has a CBOE `daily_prices/VIX9D_History.csv` path since yfinance ^VIX9D returns n=1 daily. 3934 CBOE history rows → 409 existing VX_DAILY rows now carry vix9d + ratio. 8/17-8/27 event window: peak ratio **0.899 on 8/20 post-expiry, ratio never crossed 1.0** (compression toward 1, not inversion). Ratio direction is INVERTED from vix3m/vix (red_above=True for 9d/vix; red_above=False for 3m/vix). → **KB-VIO-213**.
4. **✅ THESIS v3.9 → v4.0 BUMPED.** Because the F2-KILL is the second instance in one thesis version of the level-signal-decay class (KB-VIO-090 was first, retired 8/4). Two instances of one mechanism promotes it. v4.0 headline: level-signal decay is a CLASS, not a one-off; F2 (pre/post-regime-break) is a spec-field refinement inside SCOPE, not a discretionary check; directional/window signals are more regime-robust than level signals. RISK FACTORS gains the level-decay class as a first-order named risk. Path A owes its own F2 audit → Phase-4 queue. Predictions #7 registers HENRY's ~9/1 SKEW cross-back forecast as live-testable. Full old→new in `thesis/CHANGELOG.md`.
5. **✅ TERRY β-correction packet shipped** — outbox + TERRY/inbox (carve-out ①). Doorbell verdict per rule 6b: TERRY DARK but leg 3 fails (no dated referent, packet explicitly says "no substantive change to trade construction"). Correct outcome: no PROME doorbell, TERRY consumes on next boot.
6. **✅ PROME F2/β/v4 packet shipped + SendMessage doorbell.** PROME had asked in their consumed-packet receipt for the F2/β readout in my closeout. Packet at PROME/inbox/ (carve-out ①) + SendMessage to prome-7a (idle) at 19:00 ET. **PROME closed the loop:** GATE-VIO-RV1 RETIRED 2026-08-27 by registered kill (their commit 78cd0aa76), both research artifacts verified pre-edit, S3 counter retired, TERRY-consequence explicitly NOT going to Will. No reply owed.
7. **✅ ORACLE cross-session note acknowledged** — their earlier commit 2e8591695 swept my 4 staged WALTER-lane deletions; all 4 files intact at origin `inbox/WALTER/processed/`. My lane complete, no work owed.

---

## NEXT SESSION (priority-ordered)

1. 🟠 **HENRY's ~9/1 SKEW cross-back forecast grade (Prediction #7).** If SKEW 20d-avg re-crosses 140 within ±2 sessions of 9/1 at spot within ±2% of 8/23, upgrades KB-VIO-203 from anecdote to mechanism-with-computed-date and earns the v4.0 "directional/window signals are regime-robust" corollary its first live win. Grade window: ~2026-08-31 → 2026-09-03.
2. 🟠 **Path A F2 audit** (v4.0 Phase-4 addition). Path A's VIX<20 entry gate is level-conditional; the level-decay class puts an F2 audit on every level-conditional signal. Run pre/post-2018 split on the 4-condition Path A hit rate. If separation compresses like KB-VIO-207's, sizing conclusions change.
3. 🟠 **VIX9D/VIX ratio base-rate work.** Instrument built and backfilled to 2011 — now do the base-rate work BEFORE registering thresholds (the pattern that just paid off with RV1). Do not repeat ship-then-audit.
4. 🟠 **VX_M1_HISTORY.tsv audit.** 55% of the file is DTE>60 by row count — that is not a pure M1 series. Either fetch logic or roll definition needs review. Does not affect KB-VIO-212 verdict but should be resolved before the file is cited again.
5. 🟠 **KB-VIO-208 note-field correction** — change "OPTION-IMPLIED construction" → "M1 futures-settle on mislabeled DTE≥21 uncapped bucket" per KB-VIO-212.
6. 🟡 **Top-level inbox: 12 files** (MAIL rule = separate spawn).
7. 🟡 **DAEDALUS ratchet packet** (`TRADE.md:112–117`) — still unanswered since 8/4.

---

## CARRY-FORWARD

- **🔑 THE DISCIPLINE TEST I CARE ABOUT PASSED CLEANLY.** GATE-VIO-RV1 was the first gate this desk ever armed that was base-rated before it was shipped. It armed on the two settles I could not attend, with cheap-tail 🟣 OPEN 4/4 for the first time since the instrument was built, Jackson Hole/NVDA both landing inside the window, and the loudest reader-facing story available (Warsh keynote tomorrow into open cheap-tail) was NOT the one the design was written for. **The row's own consequence_on_fire clause blocked deployment while F2 was owed. I ran F2 this session, and F2 returned KILL, and the row is now retired.** Every step is exactly what the row was written for. Zero discretion overrode the mechanism. **File this as evidence for whether the base-rate-before-you-build discipline is worth what it costs.**
- **🔑 THE FRAMEWORK-LEVEL FINDING IS THE REGIME READ, NOT THE ONE KILLED GATE.** The cheap-tail-as-KB-VIO-207-defined region *"VIX≤16 + SKEW≥140 + VVIX≤90"* fires 4.0% of days post-2018 without discriminating anything. That is a claim about which mechanisms carry edge in this regime. Combined with KB-VIO-090's earlier retirement (both level-based, both decayed), v4.0 promotes level-signal decay from a KB observation to a framework rule. **Any tail-detection instrument I write from here on gets a pre-registered F2 test as part of its SCOPE spec, or its NULL is unwritten.** Working corollary until falsified: prefer derivative/window signals over levels.
- **⚠️ β RECONCILIATION IS THE SECOND INSTANCE IN 30 DAYS of `[[finding_asymmetric_rigor_counterparty_claims]]`.** I retracted TERRY's 0.28 toward my 0.274 without re-deriving 0.274. The 0.274 turned out to be a bucketing bug. The discipline is: **verify the number you retract on, always.** The tenor-gradient story survived intact; the specific point estimate at 21-35 didn't.
- **⚠️ THE VX_M1_HISTORY.tsv 55%-of-rows-at-DTE>60 finding is a real data-quality issue** but did not affect the β verdict here. Left as a follow-on because I don't cite that file for anything critical right now.

---

## OPEN HYPOTHESES *(flagged, not actionable)*

- **Prefer directional over level (v4.0 corollary) is provisional at n=1 comparison.** Falsifier: an F2 test on L1 DIET's 19yr backtest showing post-2018 separation compression. If DIET fails F2 the same way KB-VIO-207 did, the corollary dies and the level-decay class becomes something bigger — maybe "any calibrated corner of the vol surface decays." Do NOT run this test lightly; it is the falsifier for the ONE headline claim of v4.0.
- **The regime break may be 2018 (Volmageddon) or 2020 (COVID) or 2022 (rates cycle) — I nominated 2018 because KB-VIO-207 registered it, but this is testable.** If the level-decay class is a real class, its break date should be identifiable independently.
- **HENRY's departures-arrivals mechanism (KB-VIO-203) predicts a specific cross-back date on flat spot.** If the ~9/1 forecast lands, that's the first live test of the mechanism-with-computed-date framework I care about; if it doesn't, KB-VIO-203 stays at n=2 anecdotal.

---

*Basis note: all live VIX/VVIX/SKEW/VIX9D figures in this session are 8/27 TICK; VX_DAILY 8/27 row supersedes-updated to include vix9d + ratio. F2 reproducer + β reconciliation scripts live at `/tmp/.../scratchpad/f2/` — bundle to `AGENTS/VIOLET/scripts/` if any future session needs to re-run F2 mechanically.*
