# BOND SCRATCH — 2026-08-20 (Thu, 11:34 → ~12:0x ET). Boot → false-superlative retraction swept by pattern → PROME's two oversight defects taken.

**Purpose:** ephemeral session handoff. Read at boot, rewritten at closeout.

> ## 🔴 FIRST THING NEXT SESSION — `BND-17` IS OPEN AND ITS EVENT HAS **NOW** PASSED
> ⚠️ **Correction to the prior handoff, which said the event had already passed — IT HAD NOT.** At this session's boot the clock read **11:34 ET** and the auction prices at **1PM ET**. The last handoff was written before 1PM and assumed the next boot would land after it. **This session also closed before 1PM.** *(Lesson, small but repeated: a handoff wrote a future event in the past tense. State the clock time you wrote at, not the tense you expect the reader to be in.)*
> **The 8/20 1PM 30Y TIPS reopening (`912810US5`, $8B) is NOT graded.**
> **Bars FROZEN and committed** (`grade_auction.py`, trailing-7 SAME-TIPS, 2023-02-16→2026-02-19, **n=7**): indirect median **76.17%** · BTC median **2.48** · dealer median **6.89%** · failure test indirect **<70.44 AND** dealer **>9.87** · cover marker BTC **<2.38**.
> **Run `python3 monitors/grade_auction.py --cusip 912810US5`; grade `BND-17`** — TRUE if indirect ≥76.17, FALSE if below, **VOID-UNSCOREABLE** if TreasuryDirect has not published competitive-accepted components within 24h. **STATE THE MARGIN IN pp.** Commit the artifact, doorbell PROME.
> ⚠️ **Will-directed CALIBRATION row — nothing rides on it.** No gate, no capital, no composition claim.

## CHANGES SINCE the 08:4x–11:3x session

1. 🔴 **A FALSE SUPERLATIVE WAS SHIPPED AND IS NOW RETRACTED (`KB-BND-152`).** This desk published *"CCC 1027 is a FRESH SERIES HIGH."* **False.** At the primary (`BAMLH0A3HYC`, session closes, span 2023-08-21→2026-08-19, n=787): **series max 1137 (2025-04-07)** · **2026 max 1034 (7/31)** · **18 prior obs ≥ the current 1030.** It was never a series high nor a 2026 high.
   - **Missing free parameter: WINDOW.** ⇒ **n=5 of this desk's superlative class** (after run-vs-count · `^TYX`-vs-`DGS30` basis · DFII10 "series high" window · "carry trade largely unwound" series).
   - **Again a CARRIED figure.** Re-reading could never catch it — every version of the sentence was plausible. `boot_recompute`'s paste-check caught it in one pull.
   - **Propagated to 4 live surfaces + 2 sent packets** before the catch.
   - ✅ **What survives untouched: the tail IS widening** (up 6 of 8 sessions), ratio 3.77x, `VX-BND-11` HELD at 3. **No score moved.** Only the superlative died.
2. 🔴 **SECOND FINDING, LARGER, AND I DID NOT GO LOOKING FOR IT: derived gate distances do not inherit level fixes.** *"33bp to HY 300"* and *"88bp to CCC 1100"* were computed off **8/14** levels and survived every later level correction on **every** surface (true: **27bp** / **70bp**); credit-equity's *"~71bp"* did the same (true: **65bp**). **A derived figure does not inherit a level fix — fix the pair or neither.** This is the 8/18 lesson repeating *inside the rows that logged it*.
3. **Credit refreshed 8/18 → 8/19 fleet-wide on my surfaces:** HY **273** · CCC **1030** · IG **81**. DFII10 percentile corrected **96.7/99.7 → 95.7 full (n=5,911) / 99.3 post-2010**. T10YIE date 8/18 → 8/19.
4. **PROME oversight pass — both verified defects TAKEN:**
   - **`FL-BND-11` internal contradiction:** Evidence cell still read *"FX leg ARMED: yen 162, Mimura warning 7/1"* while its own Notes said NOT ARMED. **Fixed with a live pull: USD/JPY 158.95 [8/20], ~6.1 big figures AWAY from the 165 line and strengthening.** A stale clause inside a refreshed cell — the header-edit failure mode at field level.
   - **The retracted DM-median read still sat in SAM's inbox.** **Corrective packet WRITTEN AND DELIVERED** to `AGENTS/SAM/inbox/`, copy in `outbox/delivered/`. Retracts the below-median read, ships the factor decomposition as replacement, and **discloses PROME's own caveat against it** (member R²s are partly circular; pairwise corr EA–UK 0.74 vs JP–US 0.11 is the clean stat) — sending a corrected read while withholding a known overstatement in it would repeat the same failure.
5. **`FL-BND-02/03` refreshed — they had carried HY 263, the CYCLE TROUGH, as current evidence for 61 days.** Flagged by PROME as the fix-the-named-row-and-stop pattern (I had just fixed FL-BND-11 and would have stopped). Now HY 273 [8/19] / VIX 15.75 [8/20, HENRY owns].
6. **`consumer_check`:** cross-agent **zero certified-stale** (138 🟠 candidates, all bare-number collisions — no packets owed). `--self` returned 2 non-CSV 🔴 hits, **both inspected and both correctly-dated historical records** (a frozen July pre-registration snapshot; a CDX ledger time-series row) — **left unedited; editing a dated ledger row destroys the record.**

## NEXT SESSION (dated, future-verifiable)

1. **🔴 GRADE `BND-17`** — see the box at the top. Highest priority. ⚠️ **Check `date` FIRST: this was written at ~12:0x ET and the auction prices at 1PM.** If you boot before 1PM it is still pending; do not grade a print that does not exist. *(Writing this conditionally rather than asserting "the event has passed" is the fix for the exact defect this handoff opens with.)*
2. **🔴 8/25 decide-by → 8/29 hard close: the T6 FIX, needs LIQUID.** All four defects sit in **one clause** (the HOLD/EXTEND OR-leg) plus the trigger; the primary `≥5.10` leg is clean. **Proposal: (a) DELETE the OR-leg** (kills the `^TYX`-intraday provenance dated to a *Sunday*, the ungradeable *"keeps falling"*, and the `>5.28`-vs-fresh-high divergence in one change); **(b) trigger = "BOTH platforms print <25% on the same trading day."** Legitimate mid-flight: trigger NOT fired, (a) only narrows BOND's OWN path to winning, (b) chosen while both platforms sit above the line. ⚠️ **Co-owned — frozen text NOT edited unilaterally. Escalate if LIQUID is silent.**
3. **🟠 DATED (was undated — PROME's point 6, and it is the inverse of the stale-blocker class I logged n=3 on): base-rate (a)/(b)/(c) + the VX-01 revert-rule — DELIVER BY Fri 2026-09-04**, ahead of the 9/9–10 cluster. Corpus current to 8/13, intact, 390 rows. Measure hit rate + separation, then adopt or reject. *"Don't build it" is a real answer.*
4. **🟠 9/3 — cross-section for SAM's CH-016.** Spec settled and **already communicated to SAM**: factor decomposition PRIMARY, four-horizon rank table as ROBUSTNESS CHECK, flagged not swapped. **Confirmed to SAM: the 8/13→9/3 window ships as one reported cut.** Coverage US/EA/UK to ~9/2, **AU quoted at its own end-date ~8/26–28**, never silently squared. **Still to do:** lead with pairwise correlations (or leave-one-out R²) rather than in-factor member R²; state whether α is full-sample; consider running it at the **super-long tenor Channel 6 actually names** (MOF publishes daily 20/30/40Y; the US 30Y leg exists).
5. **🟡 8/24 (Mon) — Will's HELD US sovereign-CDS sub-item.** Establish existence + pullability **before** proposing any threshold.
6. **🟡 8/27 — content-check the 5 unverified outbox packets** (HENRY 5/19, LIQUID 5/19, SAM 7/1, TERRY 7/10, TERRY 7/16). **Verify by CONTENT at the recipient's KB, not by filename.** Do not redeliver stale text.
7. **🟡 Separation test for the SAM bar — still UNDATED.** Does a −1.5σ episode coincide with weak UST auction composition? Until it runs, the bar corroborates and fires nothing. **Give it a date next session** (same class as item 3).
8. **🟡 9/20 — VIOLET HYG put-skew re-test.** If silent, **RETIRE** the "OR VIOLET skew-vs-flat-cash" clause rather than leave it unfireable a second time.
9. **🟡 LIQUID still owes:** T6 platform-naming + 3 spec defects (packet 8/18) · the 7/01→7/15 repo refuse-or-confirm (since 7/28).
10. **🟡 8/29 — T6 hard close + HEN-42.** C-36 decline expires with HEN-42; **if it NO-VERDICTs, BOND rules within one session — cannot roll.**
11. **🟡 Retirement candidate:** `BND11_REFUNDING_PREREG_2026-07.md` — July artifact, `BND-11` resolved 7/9, >60d, not boot-read. Check the referenced-by test, then `git mv` to `archive/`.

## OPEN THREADS / KNOWN GAPS

- **The superlative class is now n=5 and the discipline is still not mechanical.** Every instance was a CARRIED figure and every one read plausibly. `boot_recompute` catches these only when the figure is IN its block — a superlative *about* a series it prints is not itself printed. **Worth considering: have `boot_recompute` assert the series max/2026-max beside any level it reports, so a "high" claim has its referent on the same screen.**
- **Derived-figure lag (finding 2) has no checker at all.** `boot_recompute` compares levels; nothing recomputes a *distance to a gate* when the level under it is fixed. This is the highest-value tooling gap on the desk right now.
- **`assertion_check` catches the vocabulary it knows, never the class** — the retracted *"my FRED series starts 2021-08"* still would not fire, and neither would *"fresh series high."*
- **Neither checker can judge whether ANALYSIS is still true.** A clean pass means "nothing of these shapes fired," never "the files are true."

## POSITION

**TLT puts HOLD, no add — unchanged.** Will's 7/16 NO-ADD stands. **DFII10 2.41 [8/18], 9bp from the only live add-gate and it moved AWAY.** 30Y 5.28, run **31 consecutive sessions ≥5.00 / 47 days in 2026** [DGS30, session closes, maximal run, whole-series]. Composite **12/35 unchanged** — no vector moved, nothing crossed a pre-registered line. **OPEN predictions: `BND-15`, `BND-17`.**

## MAIL

**Inbox 0 / WALTER lane 0 at boot.** ⚠️ **AT CLOSE: 1 UNPROCESSED — `2026-08-20_from-REGINALD_your-810B-lands-at-leg-2-of-3-on-REG-T-06-plus-the-discriminator-you-handed-me.md` arrived mid-session.** Left unprocessed by design (general inbox = a SEPARATE task, not a boot sweep) — **but it is REGINALD answering on the FHLB $810.7B / VX-BND-18 thread I packeted them on, so it is substantive, not noise. Process it next session.** ⚠️ **REGINALD is LIVE today (PROME, 8/20) — check their STATUS vintage BEFORE acting on the packet's figures.** A packet is a point-in-time artifact: if the thread moved after they wrote it, the packet is the OLDER record and their STATUS is the newer one. *(Inverse of the class this session was spent on: there, a stale number sat on a live surface; here, a correct number can be stale by the time it is read.)* Out: **1 packet to SAM (the retraction), written AND delivered to their inbox, copy in `outbox/delivered/`.** PROME messaged twice with an oversight report (2 defects + 4 suggestions) — **both defects taken this session; suggestions 3/4/5 folded into the SAM packet, 6 split across NEXT-SESSION items 3, 4 and the FLOW 02/03 refresh.** Reply owed to PROME at close.

## CLOSEOUT

STATUS ✅ (248 lines, under cap — trimmed from 250) · SCRATCH ✅ · KB ✅ (`KB-BND-152` added, `-139` → SUPERSEDED with its false Fact left UNEDITED as the record) · VX ✅ (02, 11) · FLOW ✅ (02, 03, 11) · NEXUS_BRIEF ✅ (§3 corrected, header vintage refreshed) · TRADE ✅ · CREDIT_PRIMARY_MARKET ✅ · RECEIPT ✅ · `docket_check` **rc=0** · `boot_recompute` **rc=0** · `closeout_check` **rc=0** · consumer_check cross-agent **zero certified-stale** / `--self` 2 hits both dated-historical, left intact · ledger nudge: **all 3 named ledgers (VX/KB/FLOW) refreshed this session** · **THESIS untouched — no thesis-level change this session; the retraction moved no score and no channel.**
