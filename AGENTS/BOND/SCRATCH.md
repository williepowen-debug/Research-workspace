# BOND SCRATCH — 2026-08-20 (Thu, 08:4x → ~11:3x ET). Boot → SAM packet → BND-17 → Will-requested core-file sweep → two checkers → fix-verification audit → THESIS v1.1.5.

**Purpose:** ephemeral session handoff. Read at boot, rewritten at closeout.

> ## 🔴 FIRST THING NEXT SESSION — `BND-17` IS OPEN AND ITS EVENT HAS PASSED
> **The 8/20 1PM 30Y TIPS reopening (`912810US5`, $8B) was NOT graded — this session closed before 1PM ET.**
> **Bars are FROZEN and committed** (`grade_auction.py`, trailing-7 SAME-TIPS, 2023-02-16→2026-02-19, **n=7**): indirect median **76.17%** · BTC median **2.48** · dealer median **6.89%** · failure test indirect **<70.44 AND** dealer **>9.87** · cover marker BTC **<2.38**.
> **Run `python3 monitors/grade_auction.py --cusip 912810US5`; grade `BND-17`** — TRUE if indirect ≥76.17, FALSE if below, **VOID-UNSCOREABLE** if TreasuryDirect has not published competitive-accepted components within 24h of the auction. **STATE THE MARGIN IN pp.** Commit the artifact, doorbell PROME.
> ⚠️ **Will-directed CALIBRATION row — nothing rides on it.** No gate, no capital, no composition claim; the 8/18 no-composition-gate-at-this-tenor ruling is untouched.

## CHANGES SINCE 8/19

1. **SAM's 4wk-rolling bar RULED** (`KB-BND-144`). Centred on the **median +¥0.723T**, σ 1.851T. **SELL WATCH ≤ −¥2.054T** (2.76% de-clustered, ~1.4/yr) · **ESCALATE ≤ −¥2.979T** (1.33%). Buy side context-only. **±1.0σ rejected** — the overlap bias is *worst at the loosest bar* (3.22×), so on the raw obs-rate I would have taken it. ⛔ **Frequency-calibrated ONLY: separation vs UST outcomes has NEVER been tested. It escalates attention and corroborates; it fires nothing alone.**
2. **`BND-17` pre-registered pre-print** (Will-directed via PROME). The registration caught a live defect: STATUS carried a hand-derived **n=3** benchmark (indirect median 77.48) while the tool returns **n=7** (76.17) — a *method* difference, not a data one. Registering off STATUS would have used a **1.31pp harder bar that nobody chose on purpose.** Reconciled on STATUS ×2, CATALYSTS, AUCTION_HEALTH.
3. **🔴 THE DM CROSS-SECTION WAS REBUILT TWICE AND THE SECOND ANSWER INVERTS THE FIRST** (`KB-BND-145` → **CORRECTED**, `-148`, `-151`; **THESIS v1.1.5**).
   - Built because the Will-ruled 8/10 scope claimed BOND ran it and **it did not exist.** UK leg added same day (BoE IADB — the blocker was an HTTP 302 returning 0 bytes).
   - **First estimator (rank of cumulative Δ over a window) FAILED:** 7 one-week windows → **7 distinct orderings**, and the *horizon flipped the conclusion.* Retracted same session.
   - **Second (factor decomposition on daily Δ, n=239; DM factor = US/EA/UK with Japan EXCLUDED so it is not circular) is stable and has no window free parameter:** R² **US 66.6 · EA 77.8 · UK 78.6 · JP 6.8%**; JP–US daily corr **0.11** vs EA–UK **0.74**. Episode 7/13→8/18: Japan's **+14.8bp** = drift **+13.3** / **common factor only +1.6** / idiosyncratic ~0.
   - ⇒ **A global common factor explains ~1.6bp of Japan's move — H3 explains almost none of it, the OPPOSITE of what I sent SAM in the morning.**
   - Non-synchronous-trading artifact **hypothesised and REFUTED** (lagging JP makes correlations *worse*). My own first decomposition was **wrong** — drift folded into the factor term; caught only because it disagreed with the R².
4. **Core-file sweep (Will-requested): 17 stale/false claims across 6 files.** Worst: **`TRADE.md` described the only live add-gate as "6bp and closing" when DFII10 had backed off to 9bp and was WIDENING**, and asserted *"PREDICTIONS.tsv IS EMPTY"* with two rows OPEN. Marks **stripped and pointed at STATUS**, not re-stamped.
5. **Fix-verification audit: 5 defects had NOT been fixed** — I had treated flagging as fixing. Includes a **VIOLET ask orphaned 76 days** (written, committed, never delivered) and **`outbox/delivered/` never existing**, so "sent" and "orphaned" were indistinguishable for every packet this desk ever wrote. Both fixed.
6. **THESIS v1.1.5** — channel **6(a)** measured for the first time (above); and the **v1.1.4 held-spec blocker was itself stale** (corpus is 390 rows through 8/13 and structurally intact, refreshed 8/18). **Base-rating unblocked since 8/18 — nothing adopted; that work is still owed.**
7. **WALTER `-003 ADDENDUM 4b`** independently corroborates the retraction and states it symmetrically — *"both get weaker, not one"* (`KB-BND-149`). Third independent route to one conclusion in a day.

## NEXT SESSION (dated, future-verifiable)

1. **🔴 GRADE `BND-17`** — see the box at the top. Highest priority; the event has passed.
2. **🔴 8/25 decide-by → 8/29 hard close: the T6 FIX, and it needs LIQUID.** All four defects sit in **one clause** (the HOLD/EXTEND OR-leg) plus the trigger; the primary `≥5.10` leg is clean, which is why T6 grades at all. **Proposal: (a) DELETE the OR-leg** — kills the `^TYX`-intraday provenance dated to a *Sunday*, the ungradeable *"keeps falling"*, and the new `>5.28`-vs-fresh-high divergence in one change; **(b) name the trigger rule as "BOTH platforms print <25% on the same trading day."** **Legitimate mid-flight because the trigger has NOT fired (the test has not started), (a) only narrows BOND's OWN path to winning, and (b) is chosen while both platforms sit above the line so it cannot flatter either side.** ⚠️ **Co-owned — frozen text NOT to be edited unilaterally. Will was asked whether to send the proposal with an 8/25 decide-by; escalate if LIQUID is silent.**
3. **🟠 Base-rate (a)/(b)/(c) + the VX-01 revert-rule — NOW UNBLOCKED.** Corpus current to 8/13, intact, 390 rows. Measure hit rate + separation, then adopt or reject. *"Don't build it" is a real answer.*
4. **🟠 9/3 — cross-section for SAM's CH-016.** ⚠️ **Spec question to settle FIRST:** the factor decomposition is now the *stronger* instrument and the frozen four-horizon rank table the weaker. **Proposal: send the factor read as primary and keep the horizon table as a robustness check — flag the change to SAM, do NOT swap silently.** Coverage: US/EA/UK to ~9/2, **AU only to ~8/26–28** (weekly file cadence), quoted at its own end-date, never silently squared.
5. **🟡 8/24 (Mon) — Will's HELD US sovereign-CDS sub-item.** Establish existence + pullability **before** proposing any threshold.
6. **🟡 8/27 — content-check the 5 unverified outbox packets** (HENRY 5/19, LIQUID 5/19, SAM 7/1, TERRY 7/10, TERRY 7/16). **Verify by CONTENT at the recipient's KB, not by filename** — a filename scan over-counted (HENRY demonstrably had the 7/23 packet, filed under another convention). **Do not redeliver stale text.**
7. **🟡 Separation test for the SAM bar** — does a −1.5σ episode coincide with weak UST auction composition? Until it runs, the bar corroborates and fires nothing. **Currently undated — give it a date.**
8. **🟡 9/20 — VIOLET HYG put-skew re-test.** If silent, **RETIRE** the "OR VIOLET skew-vs-flat-cash" clause from the CDX vector rather than leave it unfireable a second time.
9. **🟡 LIQUID still owes:** T6 platform-naming + 3 spec defects (packet 8/18) · the 7/01→7/15 repo refuse-or-confirm (since 7/28).
10. **🟡 8/29 — T6 hard close + HEN-42.** C-36 decline expires with HEN-42; **if it NO-VERDICTs, BOND rules within one session — cannot roll.**

## OPEN THREADS / KNOWN GAPS

- **`assertion_check` catches the vocabulary it knows, never the class.** The retracted *"my FRED series starts 2021-08"* would **not** fire — and the THESIS corpus blocker (*"stale to 2026-05-28"*) didn't, which is that gap observed live within an hour of shipping.
- **Neither checker can judge whether ANALYSIS is still true.** A clean pass means "nothing of these shapes fired," never "the files are true."
- **Today's recurring failure was not bad analysis:** fixing *by line list instead of by pattern* (4×) and *treating a flag as a fix* (5×). Both now partly mechanised, neither fully covered.

## POSITION

**TLT puts HOLD, no add — unchanged all session.** Will's 7/16 NO-ADD stands. **DFII10 2.41 [8/18], 9bp from the only live add-gate and it moved AWAY.** Composite **12/35 unchanged** — no vector moved, nothing crossed a pre-registered line. **OPEN predictions: `BND-15`, `BND-17`.**

## MAIL

**Inbox 0 / WALTER lane 0 — fully drained.** Out: 2 packets to SAM (bar ruling + the retraction), 1 to VIOLET (re-sent orphan). Doorbelled SAM ×3, PROME ×3. ⚠️ **PROME's clock ran ~2.5h fast this morning** — they owned it and corrected four ruling packets; **stamp from `date`, never narrative time.**

## CLOSEOUT

STATUS ✅ (248 lines, under cap; THESIS pointer corrected v1.1.3→v1.1.5) · THESIS ✅ **v1.1.5** + CHANGELOG ✅ · PREDICTIONS ✅ (`BND-17` added) · CATALYSTS ✅ · KB ✅ (+11 rows, 141–151, all 13-field, whole-file verified) · FLOW ✅ (`FL-BND-11` — closes the newly-adopted ledger nudge) · RECEIPT ✅ · auto-memory ✅ (`finding_overlapping_window_inflates_the_base_rate`, index verified, hook trimmed) · **`closeout_check.py` rc=0** · consumer_check cross-agent = 60 candidates / **zero certified-stale**, no packets sent · claim_check weekday clean · zero KB rows past `Stale_By` · orphan_check clean.
