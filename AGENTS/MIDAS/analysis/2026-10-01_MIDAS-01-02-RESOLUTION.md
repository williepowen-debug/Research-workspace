# MIDAS-01 + MIDAS-02 — RESOLVED 2026-10-01 on their FROZEN LETTERS, every basis printed

**Grader:** MIDAS (spawned by PROME `prome-0c`, WQ-184 due-row driver, DOCKET L231 + L176). **Written:** Thu 2026-10-01 ~12:2x ET.
**Governing ruling:** `PROME/proposals/2026-08-27_moving-referent-class-RULED.md`, Option A class-wide: no edit to the live rows, grade on the frozen letter, print every basis. **No threshold, anchor, band or score moved. $0. No card.**
**Data:** yfinance daily bars pulled 2026-10-01 ~12:15 ET (via `.venv`), FRED `DFII10` via `FORGE/tools/market-data/fetch.py`, LME stocks via `metals_watch.py`'s westmetall scrape. The 9/30 closes are final (the 10/1 session was in flight and is not used for any grade).

## Verdicts

| Row | Frozen letter (abridged) | Verdict | Margin |
|---|---|---|---|
| **MIDAS-01** (M1) | gold does not close >10% below **$4,113.70 [7/10]** (kill line **$3,702.33**) while DFII10 >2.0, by 9/30 | ✅ **HIT** — on every basis | lowest close on any basis was **7.8% above** the kill line |
| **MIDAS-02** (I1) | copper does NOT fall >20% from **$5.75 [4/9]** WITH LME inventory +100% (RED **479,000t**), through Q3 | ✅ **HIT** — neither leg fired, so the conjunction could not | copper **+8.2% above** its anchor at its window low; LME at **64%** of the RED bar at its window high |

Neither row needed the STUCK provision (OPEN_ITEMS 22): every leg had data.

## MIDAS-01 — gold, all bases

Window 2026-07-10 → 2026-09-30. Anchor $4,113.70 was a `GC=F` print when `GC=F` sat on `GCQ26`.

| Basis | 9/30 close | vs $4,113.70 | Window low [date] | Low vs anchor | Note |
|---|---|---|---|---|---|
| `GC=F` (continuous, the letter's ticker) | **$4,186.70** | **+1.77%** | $3,992.10 [7/16] | −2.96% | low is +7.83% above the $3,702.33 kill line |
| `GCZ26` (front at grade) | **$4,186.70** | +1.77% | $4,048.70 [7/16] | −1.58% | own-contract 7/10 → 9/30: $4,173.60 → $4,186.70 = **+0.31%** |
| `GCV26` (a deferred month, context) | $4,155.60 | +1.02% | $4,019.10 [7/16] | — | own-contract +0.32% |
| `GCQ26` (the anchor's own contract) | — | — | — | — | **UNAVAILABLE**: expired; the vendor no longer serves it |
| **GLD (no-roll arbiter)** | **$380.84** | **+1.02%** vs its 7/10 close $377.01 | $364.96 [7/16] | −3.20% | |

**DFII10 conditional:** 57 observations 7/10 → 9/29, low **2.31 [7/17]**, high **2.91 [9/29]**, **none ≤2.0**. The real-yield condition held the whole window, so this was a real test and not a vacuous one. The 9/30 observation was not yet published at read time (FRED posts it ~16:15 ET 10/1); it cannot change the verdict, because the price leg never came near the kill line.
⚠️ **What a HIT here does and does not say:** gold held its premium against real yields that rose from 2.32 to 2.91 (+59bp) over the window. That is the M1 debasement-premium claim, PROVISIONAL tier. It says nothing about the last week: gold is **−3.20% on GLD since 9/25** and **−5.84% `GC=F` / −4.21% GLD since 9/8**. The row's threshold was 10%, which is wide.

## MIDAS-02 — copper, all bases

| Basis | 9/30 | vs $5.75 [4/9] | Window low 7/10→9/30 [date] | Low vs anchor | QoQ (6/30 → 9/30) |
|---|---|---|---|---|---|
| `HG=F` (the letter's ticker) | **$6.5590** | **+14.07%** | $6.2200 [7/17] | +8.17% | +5.92% |
| `HGZ26` (front at grade) | **$6.6215** | +15.16% | $6.3555 [7/17] | +10.53% | +4.48% |
| CPER (no-roll ETF) | $39.78 | +12.98% vs its 4/9 close $35.21 | $37.92 [7/17] | +7.70% | +5.43% |

The −20% line is $4.60. No basis came within 25% of it.
⚠️ `HG=F` on 9/30 is not `HGZ26`: 9.12% of its volume, −0.91% spread. The guard passes it as OK because the share clears 5%, but it is a different contract. Both are printed; the verdict is the same on both.

**LME inventory legs (westmetall, LME data):**

| Reference | Value | LME 249,400t [30 Sep] vs it |
|---|---|---|
| Hardcoded median (frozen letter, 7/10) | 239,400t | **+4.18%** |
| Hardcoded RED leg (frozen, operative per OPEN_ITEMS 22) | **479,000t** | **52.1% of the bar**; needs **+92.1%** to reach it |
| 🔎 **AS-OF 2026-09-30 trailing-2yr median** (window 2024-09-30 → 2026-09-30, n=507) | **234,750t** | **+6.24%** |
| Floating RED (2× the as-of median) | 469,500t | 53.1% of the bar |
| Window high 7/10 → 9/30 | 306,500t [7/10] | 64.0% of 479,000t |
| Window low | 204,975t [8/14] | — |

## The gold settles owed to the fleet: `GCZ26` 9/28, 9/29, 9/30

| Session | `GCZ26` daily close (vendor) | 13:29 ET 1-min bar | Day change, close to close | GLD day change (16:00 close) |
|---|---|---|---|---|
| **Mon 9/28** | **$4,168.40** | $4,168.40 | **−3.54%** (from $4,321.20 [9/25]) | −3.94% |
| **Tue 9/29** | **$4,179.70** | $4,180.70 | **+0.27%** | +1.32% |
| **Wed 9/30** | **$4,186.70** | $4,186.90 | **+0.17%** | −0.54% |

⚠️ **GRADE OF THESE FIGURES: VENDOR (yfinance), NOT EXCHANGE SETTLEMENTS.** The CME settlements endpoint returned **HTTP 403** (CME blocks automated reads; a documented wall, not retried). usagold.com returned 403. Two web-search summaries gave settle figures that matched no source page; they are not used.
**Session test (decided by the observation's session, not the clock):** each vendor daily close matches that same date's **13:29 ET** one-minute bar to within $1.00, the COMEX gold settlement window (13:29–13:30 ET). So each figure belongs to its labelled day's settlement window. It is **not** the next session's evening trade: the last bars of each calendar day after 18:00 ET read $4,164.10 / $4,205.50 / $4,205.40, and the daily closes do not match them. ⚠️ The 9/30 row carries 9/29's volume (149,747 on both), which is the known vendor duplication shape (KB-112). It does not affect the price.
**One secondary corroborates the 9/29 figure INDIRECTLY:** Investing.com (published 9/30 17:31) says *"gold futures added 0.2% to settle at $4,189.10"*. **$4,189.10 is the 16:59 ET bar, the post-close print and not the 13:30 settle**, but +0.2% back-solves to a prior reference of ~$4,180, which is consistent with $4,179.70 as the 9/29 settle. **INFERRED, not VERIFIED.**
**Why the GLD days differ from the settle days (it is timing, not an error):** GLD closes at 16:00 ET, 2½ hours after the settle. On 9/29 gold futures rose from $4,180 at 13:30 to $4,215 by 17:00, so GLD's +1.32% took in an afternoon rally that the 9/29 settle did not, and that same rally comes out of GLD's 9/30. Over 9/25 → 9/30, GLD fell **−3.20%** and `GCZ26` fell **−3.11%**: they agree once the windows match.

## DOCKET L176 — Forum-4 WT-1 record-close (hard expiry 9/30)

**Outcome recorded: WT-1 NEVER FIRED and was never jointly evaluated. It was SUPERSEDED on 2026-08-11, before its first live print, by Will's ruling dec-2 (*"dec 2: go with you rec"*, `FORUM/2026-08-10_positioning-exhaustion/04_synthesis/07_PROME_rulings-record.md` row 60).** The basis was WT-1b: NO ASSOCIATION at n=152, so the test's premise failed rather than the claim. **Q-C has carried `STATUS: UNTESTED` since 8/11, not from 9/30.** The expiry changes nothing and is not an exit: per §8.1, *"if by then the pair has NEVER been jointly evaluable, the Q-C verdict is NOT confirmed — it is re-labelled UNTESTED"*, and that label was already applied.
⚠️ **What this close does NOT certify:** I did not re-run MIDAS's WT-1 size-knob leg on the six gold COT prints between 8/14 and 9/22. The test was superseded, so no one was obliged to. "No firing recorded" is **SEARCH-NOT-FOUND** across `FORUM/`, `PROME/` and `AGENTS/MIDAS/`. It is not a computed negative.
⚠️ **Owner of the in-place revision:** §8.1 says the FINAL *"is revised in place to say so"*. `01_SAM_joint-synthesis-FINAL.md` §0 still reads *"STATUS: UNTESTED (proposed …)"*. That file is SAM's/PROME's, so MIDAS flags it and does not edit it. WT-2 (standing retraction, no expiry) and WT-3 are not MIDAS's to close.

## Limits that travel

- Every price is a vendor close. No exchange settlement was reachable (CME 403).
- `GCQ26`, the contract MIDAS-01's anchor was printed on, can no longer be pulled. Its own-contract path cannot be printed, so the grade rests on `GC=F`, `GCZ26`, `GCV26` and GLD, which all agree.
- Both rows are PROVISIONAL tier with no stated probabilities, so they produce no Brier score. They count as a calibration record only.
