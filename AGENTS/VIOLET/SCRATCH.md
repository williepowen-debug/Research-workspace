# VIOLET SCRATCH — September 6, 2026 (Sun ~11:3x ET — **boot session; Will directed the `VX_DAILY` backfill and the `CLAUDE.md` re-key. Both done. The backfill turned out to be the bigger of the two by a wide margin.**)

> **Scope as given (Will):** *"boot up"* → then *"do the backfill, and yes re-point those CLAUDE.md lines."* No thesis bump, no proposal, no edits outside `AGENTS/VIOLET/` (plus the `PROME/inbox/` memo, carve-out ①).
> **🔑 The session's shape: I went to fill four missing rows and found the ledger under my highest-profile live claim had been sourced from a mirror for its entire life, while the publisher of record sat imported at the top of the same script.**

---

## CHANGES SINCE (what moved while I was offline)

| | 9/2 | **9/4 settle** | |
|---|---|---|---|
| `^SKEW` | 144.12 | **151.58** | **2nd consecutive ≥150, new leg high** |
| VIX | 15.20 | **14.53** | |
| VIX9D | 12.57 | **11.97** | 9-day vol, 4 days from CPI |
| VIX3M/VIX | 1.1664 | **1.2120** | cash curve **steepened** |
| VVIX | 86.25 | **84.42** | |
| MOVE | 79.71 | **73.10** | **−6.61 in two sessions; +0.69 from F1** |
| M1:M2 | +11.07% | **+11.51%** | eased from +12.16% [9/3] |

- **`RED-FT-10` advanced to 2 of 4** — WALTER `SIG-W-20260905-001` (consumed). **I verified it myself** rather than take the relay: own CBOE pull, `09/04/2026,151.580000`, matches to the hundredth.
- **Convergence 29 → 28/50.** One vector moved: **MOVE 3 → 2.** Everything else held.
- **COT unchanged** — 9/1 is the newest report that exists; next release **Fri 9/11**.

## WHAT I DID

1. **Booted clean** — 14/14 stages, `ledger_staleness` rc=0, `corrections_boot_check` rc=0. Both inbox lanes drained (WALTER ×2, top-level ×1) and `git mv`'d to `processed/`.
2. **Backfilled `VX_DAILY.tsv` — and then found the real problem.** 4 missing sessions (8/28 · 8/31 · 9/1 · 9/3) restored; **then a full-ledger reconcile against CBOE found 9 WRONG cells and 467 blanks**, including **226 of 416 `vix3m`/`vix6m`** — VIOLET's own core owned metric, 54% missing.
3. **Generalized the fix into code.** `backfill.py`'s CBOE path existed **for VIX9D only**; now it covers all six spot columns, runs **second and wins** (fills *and* corrects, printing every correction), and stamps `basis=SETTLE` for completed sessions. **Verified against the real artifact with the real defects: it reported exactly the 9 cells my independent script found, to the cent. Re-run corrects 0 — idempotent.**
4. **Built `scripts/vx_daily_gapcheck.py`** — boot-warns, **closeout-BLOCKS** (8th contract). Falsified **both** branches (injected a missing 9/3 bar → rc=1 naming it; injected a phantom holiday row → rc=1 naming it), ledger restored and md5-verified.
5. **Executed the `COMPLETION_SPEC` re-key on Will's word.** `CLAUDE.md` L52 + FILES row re-pointed to the dated `PROME/inbox/` memo; `LAST_COMPLETION.md` frozen with a banner; `README.md` map row fixed. **Then swept for the class and found two BLOCKING guards that track that file** — re-pointed both, verified live.
6. **Made `canary_staleness.py` cadence-aware** — the blanket `>4d` current-cell line was the twin of the retired COT `>9d` defect. Falsified both ways.
7. **KB-VIO-246→251 filed** (schema clean, 251 rows). STATUS rewritten and **SHRANK 30,145 → 27,5xx B** under PROME's read-cap note. MEMORY's phantom-print attribution corrected.

---

## NEXT SESSION (priority-ordered)

1. 🔴 **THE 9/8 BAR — the fork.** Pull CBOE `SKEW_History.csv` at/after the 9/8 close. **≥150 ⇒ 3 of 4. Anything <150 ⇒ RESET TO 0.** Run `skew_integrity.py` at the moment of use and **paste its verdict beside the count** (PROME `DOCKET L275`). Then **9/9 is the earliest possible fire**, published 9/10.
2. 🔴 **Read the thesis against its trail — 38 rows / 3 retractions since v4.0.** Now *well* over threshold and it is the only open item that is a judgement rather than a build. **The tail/front-end divergence now has enough bars that the v4.0 headline may be behind the tape.**
3. 🔴 **Call `skew_integrity.py` from `cheap_tail.py` at the `^SKEW` pull.** Weaker than it was — the ledger is CBOE-sourced now — but **not closed**: `cheap_tail.py` still reads `^SKEW` at run time, and the at-the-moment-of-use check is the only cover for that read.
4. 📅 **Grade `VIO-FOMC-0916`** — legs 1·4·5 + first read of leg 3 at the **9/16** close · leg 3 second read **9/18** · leg 2 **9/23** (MU confound withdrawn). Frozen letter: `research/2026-09-16_FOMC_VIXEXPIRY_PREREG_LETTER.md` §7.
5. 🟠 **The DAEDALUS 🟠 register** (D#8 prediction registry · D#10 `TRADE.md` close row · D#12 three silent-rot ledgers · D#14 wire `test_daily_log.py` · D#9/16/17/18) — unchanged, in STATUS § RESEARCH QUEUE with per-row dispositions.

---

## CARRY-FORWARD

- **🔑 A WORKAROUND BUILT FOR ONE COLUMN IS EVIDENCE ABOUT THE SOURCE, NOT ABOUT THAT COLUMN.** `backfill.py` imported CBOE *specifically because yfinance serves no `^VIX9D` daily history* — and that fact was sitting there as a comment while five other columns kept pulling from the mirror, two of them (`^VIX3M`/`^VIX6M`) **equally unserved**, which is why 226 cells were blank. **When you write a workaround for one field, immediately ask what else the better source covers.** Same shape as KB-VIO-158, which nearly bought a data subscription. → KB-VIO-246
- **🔑 AN IMPOSSIBILITY CLAIM INHERITS THE SCOPE OF THE METHOD THAT PRODUCED IT.** I carried RED's *"can BOUND, never CLEAR"* for two days as a property of the **problem**. It was a property of the **instrument** — a bar-count check over yfinance. Against the publisher of record it clears in one pass, and the answer was *one* bad cell in 20 months: **the one RED already named.** ⇒ **Before banking a "cannot be done," ask what a DIFFERENT instrument would see.** → KB-VIO-248
- **⚠️ A WRONG NUMBER IS BOUNDED; A WRONG NUMBER ON A TRIGGER LINE IS A FALSE BROADCAST.** 2026-02-06 held `vix == vix3m == 20.37` ⇒ ratio **exactly 1.0000**, a manufactured flat curve in my **🔴 peak-marker** zone (true ratio 1.147). **I scanned the class, not the row** — the other 28 near-inversion rows reconcile exactly, so the March-2026 cluster is genuine. Had I fixed only the named row, the state of the other 28 would still be unknown. → KB-VIO-249
- **⚠️ THE FLAG'S SCOPE WAS NOT THE DEFECT'S SCOPE, AND OBEYING IT EXACTLY WOULD HAVE INVERTED TWO CONTROLS.** PROME named 2 lines; a sweep found 5 consumers, two of them **BLOCKING closeout guards that track `LAST_COMPLETION.md`**. Freezing the file without re-pointing them doesn't remove a control — it makes one **red at every future closeout**, and a guard that is always red gets silenced, which deletes the real coverage too. **Retiring a surface is an INTERFACE change: grep for what READS it, and count scripts as first-class consumers.** → KB-VIO-250
- **⚠️ WHEN YOU RETIRE A BAD THRESHOLD, GREP FOR ITS SIBLINGS.** The COT `>9d` line was retired for false-DARKing a current ledger every Friday. The **same assumption survived in `canary_staleness.py`'s `>4d` current-cell check** and fired today on `Current [9/1 report]` when 9/1 *is* the newest report. **A class fixed in one instrument survives in every other one that encoded it — and those are exactly the ones nobody was looking at.** → KB-VIO-251
- **⚠️ THE PHANTOM-HOLIDAY PRINT IS CBOE'S, NOT YFINANCE'S — AND THE MISATTRIBUTION WAS OPERATIONALLY LOAD-BEARING.** It made the defect look like a mirror problem curable by switching sources, **and I switched sources today.** A naive "every CBOE date must be in the ledger" gap check would have demanded 13 holiday rows forever. The companion rule is correct **at the publisher**. → KB-VIO-247
- **✅ FALSIFICATION PAID AGAIN, AND ONE TEST FAILURE WAS MINE.** Every guard was run against the real artifact with a real defect injected. My phantom-row test initially returned rc=2 — **my harness had `sort`ed the header out of line 1**, not a tool bug; the tool **failed closed** on a corrupted ledger, which is the right direction, but the branch was untested until I redid it. **A test that errors is not a test that passed.**
- **⚠️ I ALSO SHIPPED A NONSENSE NUMBER AND CAUGHT IT ON SIGHT:** the re-pointed ordering check printed a MISSING surface as *"29,809,428 min behind"* — epoch arithmetic wearing the shape of a measurement. Now reads `never written`.
- **⚠️ MARKET JUDGEMENT ADDED TODAY IS THIN AND I AM SAYING SO.** The only genuinely new *market* facts are the 9/4 settles (which the 9/4 sessions could not see, being pre-open) and the second FT-10 bar. **No new mechanism work, no thesis movement.** The divergence read is the same one, with one more confirming session.

---

## OPEN HYPOTHESES *(flagged, not actionable — none tested this session)*

- **H1 — The far-tail bid and the front-end cheapening may be ONE trade, not two.** **Strengthened again, still untested.** A second ≥150 bar with VIX9D at **11.97** and VIX3M/VIX at **1.2120** is exactly the signature of selling the front to fund October convexity, and October 30/35/60 call OI is still +106–313%. **The dealer-positioning leg exists** (HENRY 9/2: NEGATIVE gamma, flip 7,689–7,699, ≈−$16B/1%, dealers AMPLIFY). ⛔ **Still a flow claim I have not measured** — GEX is a positioning state, not a funding flow. **What would test it:** whether front-end supply and October call OI move together across 9/8–9/11.
- **H2 — RETIRED 9/4.** MOVE's decline as a pre-NFP unwind is superseded; the tail bid rose **into** a relief rally.
- **H3 — If FT-10's chain survives 9/8, the fourth bar lands 9/9** — two sessions before CPI, six before the FOMC. **A sustain fire arriving inside the run-up to both catalysts is a different object from one in quiet tape. No base rate exists for this; do not improvise one.**
