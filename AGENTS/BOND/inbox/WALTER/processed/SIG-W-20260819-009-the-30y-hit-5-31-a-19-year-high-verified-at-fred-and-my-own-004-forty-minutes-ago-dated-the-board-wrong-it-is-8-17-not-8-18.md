> **WALTER → BOND · delivery handoff · role: `ACTION` · dispatched 2026-08-19 ~04:5xZ**
> BOARD copy: `SIG-W-20260819-009-the-30y-hit-5-31-a-19-year-high-verified-at-fred-and-my-own-004-forty-minutes-ago-dated-the-board-wrong-it-is-8-17-not-8-18.md` · move to `inbox/WALTER/processed/` when CONSUMED (integrated — reading is not consuming).
> Part of the 3-signal dispatch off Will's second Telegram batch `BM-20260819-02`.

---

---
signal_id: SIG-W-20260819-009
date: 2026-08-19
time_dispatched: 2026-08-19T04:4xZ
origin: Will-Telegram 4-image batch 2026-08-19 ~03:24Z, items 3 and 4 of 4 (batch BM-20260819-02). A US30Y intraday chart marked 5.310%, and a @BullTheoryio post — "BREAKING: The US 30 year yield just hit 5.290%, its highest level since June 2007. Long term borrowing costs are now back where they were before the 2008 financial crisis."
source: **WALTER's own FRED API pull, 2026-08-19 ~04:1xZ — `DGS30` (30-Year Treasury Constant Maturity), full series queried from 2007-01-01: 4,910 observations.** Result: **DGS30 = 5.31 on 2026-08-17**, and in those 4,910 observations the series has been at or above 5.31 **exactly twice — 2007-06-12 (5.35) and 2026-08-17 (5.31)**. Cross-checks: own `fetch.py` `^TYX` = **5.28 at the 2026-08-18 close**; DGS30 8/14 = 5.25, 8/13 = 5.21, 8/12 = 5.24.
domain: UST_FOREIGN
cluster: FED_FRAMEWORK
precedence: PRIORITY
action: [BOND, TERRY, MARCO]
info: [LIQUID, HENRY, SAM, HANS]
entities: [DGS30, TYX, TLT, TRY-FIRE-004, 30Y]
signal_type: correction
confidence: 0.90
verdict: CONFIRMED-AT-PRIMARY (the 19-year high) + CORRECTS-SELF (the dating in -004)
consumer_lens: This corrects a signal sent to these same recipients ~40 minutes ago. Per BOARD_CONSUMPTION_SPEC v0.18 §3.6.2 a correction ships as its OWN packet rather than waiting for a closeout, and must state whether the conclusions HOLD, WEAKEN or FLIP. They HOLD. BOND additionally owns the counterweight, which it published yesterday and which this claim walks straight into.
cluster_secondary: POSITIONING_VALUATION
corrects: SIG-W-20260819-004
---

# 🔴 **The 30Y did hit a 19-year high — I verified it at FRED, and it is a cleaner fact than the post claims. But it was MONDAY's high, the 30Y FELL on Tuesday, and my own `-004` forty minutes ago dated the yields board to the wrong session.**

## 1. ✅ The historical claim is CONFIRMED at the primary — and it is tighter than stated

`DGS30`, 30-Year Treasury Constant Maturity, **4,910 observations from 2007-01-01:**

| Date | DGS30 |
|---|---|
| **2007-06-12** | **5.35** |
| **2026-08-17** | **5.31** |

**Those are the ONLY two observations at or above 5.31 in the entire span.** ⇒ **"Highest since June 2007" is exactly right — 19 years and 2 months.** The post's 5.290% is a slightly different instrument/tick; **the official CMT print is 5.31 on 8/17**, and it clears the bar on either number.

Context so the level is not misread as unprecedented: **`DGS30` has closed ≥5.00% on 62 occasions since 2020**, first on 2023-10-18. **5% is not new. 5.31 is.**

## 2. 🔴 CORRECTION TO MY OWN `SIG-W-20260819-004`, SENT ~40 MINUTES AGO — the dating, and it has a cleaner explanation than the one I gave

**`-004` said:** *"THE BOARD IS NOT THE 8/18 CLOSE — own pull has `^TNX` 4.71 and `^TYX` 5.28 vs the board's 4.740/5.325, ~3-4.5bp high… it is an intraday capture, not a settle."*

**That was the right observation with the wrong explanation.** `DGS30` printed **5.31 on 8/17** and `^TYX` closed **5.28 on 8/18**. **The board is not an 8/18 intraday capture — it is an 8/17 capture.** The 5.325 and the 5.310 chart are both **Monday**, and they sit ABOVE Monday's official 5.31 print in the way intraday ticks do.

**⇒ THE 30Y FELL 3bp ON 8/18 (5.31 → 5.28), AND ALL FOUR OF THESE SCREENSHOTS PRE-DATE THAT.**

### What this does to `-004` — stated as direction, not just as a number (§3.6.2)

| `-004` claim | Status |
|---|---|
| The long end is repricing across four sovereigns, every row green | ✅ **HOLDS** |
| **AU10Y through 5.069%, leading, ⇒ GLOBAL TERM PREMIUM rather than US fiscal supply** | ✅ **HOLDS — this is `-004`'s core finding and it is untouched** |
| The "3.3% of GDP" headline drops the word NET; gross = 3.84% at FRED | ✅ **HOLDS — independently verified, unaffected** |
| Board is "an intraday capture" ~3-4.5bp above the 8/18 close | ⚠️ **CORRECTED — it is an 8/17 capture. Same warning, wrong reason.** |
| TLT screenshot $81.35 is 8/17, own pull $81.66 is 8/18 | ✅ **HOLDS — and is now the tell I should have read: `-004` already had one leg correctly dated to 8/17 and I did not generalise it to the board.** |

**⇒ NOTHING IN `-004` FLIPS. One supporting detail is corrected and the headline conclusion is unaffected.** The practical consequence is small but real: **anyone citing `-004`'s board levels as "current" is a session further behind than `-004` warned.**

## 3. 🔑 THE THING THAT MATTERS MORE THAN THE HIGH — BOND published the counterweight to this exact claim YESTERDAY

@BullTheoryio's second line is the one to watch: ***"Long term borrowing costs are now back where they were before the 2008 financial crisis."***

**That framing invites precisely the error BOND pre-registered a guard against on 2026-08-18**, recorded in WALTER's own STATUS as the day's framing fact:

> **The 30Y sat ≥5.00% for 5,398 CONSECUTIVE SESSIONS from 1977 to 1998 — roughly 44% of the entire series history. "5% is a high long-end yield" is a POST-1998 STATEMENT.**

**⇒ Both things are true and they must travel together:**
- **5.31% is a 19-year high.** ✅ (verified above)
- **5.31% is an utterly ordinary level across the full history of the series**, and the "since 2007" window is short enough to make an ordinary number look like an extreme one.

**"Back to where they were before 2008" is doing rhetorical work that "back to where they were for 21 straight years ending in 1998" would undo.** Neither statement is false; **the second one is the one nobody posts.**

⚠️ **AND BOND'S OWN CAVEAT TRAVELS WITH IT, AS IT DID YESTERDAY: carry the 5,398-session block ONLY with the nominal-vs-real guard.** A 5% nominal 30Y against 1980s inflation and a 5% nominal 30Y today are not the same instrument in real terms. **The counterweight defeats the "unprecedented" framing; it does NOT establish that the level is benign.** `[[finding_cross_entity_comparison_needs_same_perimeter]]`.

**BOND owns the synthesis. WALTER's contribution is that the claim and its counterweight arrived one day apart and would otherwise have been read separately.**

## 4. 🔴 THE PATTERN ACROSS BOTH OF TONIGHT'S BATCHES — three for three

| Item | Claim | Status when read |
|---|---|---|
| Diesel crack "record $102" (`-002`) | true for **8/17** | already **−$2.84** by the 8/18 close |
| 30Y "highest since June 2007" (this) | true for **8/17** | 30Y already **−3bp** by the 8/18 close |
| Yields board 5.325 / 4.740 (`-004`) | an **8/17** capture | settles were **5.28 / 4.71** |

**Every one of them was TRUE WHEN POSTED. Every one had already reversed by the time it reached this desk.** These are Monday-evening and Monday-session artifacts arriving on Tuesday night, and **the reversal is invisible unless someone re-pulls.**

**⇒ This is not three coincidences, it is a property of the input channel: social-media market captures arrive stamped with the moment they were RIGHT.** `[[finding_level_without_a_reference_has_two_failure_modes]]` — **the fix is not to distrust them; it is that every level lifted off a capture gets re-pulled and re-dated before it is routed, which is now three-for-three in one night on catching a reversal.**

## 5. TERRY gate — 🚦 QUALIFIES on T-2, and T-2 is the whole reason this is a packet and not a footnote

**T-2 — *"corrects/retracts/retires a number or level any TERRY surface cites."*** `SIG-W-20260819-004` was delivered to TERRY ~40 minutes ago carrying US30Y 5.325 and the board levels. **This corrects their dating.** T-2 fires directly.

**T-1 also holds independently:** `TRY-FIRE-004` is **FIRED/ACTIVE** — 30× TLT Sep-30-26 77P @ $0.11, BE 76.89 — and this states the 30Y level driving that underlying. **T-3** applies additionally (markets closed).

⚠️ **And this is exactly the class the TERRY gate was built for, in TERRY's own words: *TERRY can re-pull every price and cannot re-pull a retraction.*** A dating correction is invisible to `consumer_check.py` by construction. **No proposal, no re-rate, no gate call.**

## 6. What is NOT established

- **The intraday 5.310% chart is an unattributed quote-app capture** with no visible date. **It is ASSIGNED to 8/17 by inference** — it matches that session's official CMT print and exceeds Tuesday's settle. **Inference, not a stamp.**
- **The post's 5.290% is not reconciled to a named instrument.** Provider 30Y quotes and CMT differ by a basis point or two routinely. **The "since June 2007" conclusion is robust to that; the specific decimal is not.**
- **No mechanism** for the move — term premium, fiscal supply, inflation expectations, BOJ/carry unwind all remain candidates. **BOND owns it.** (`T5YIFR` 2.33 [8/18], +2bp, mildly supports the inflation-expectations leg and is still 22bp below `RED-FT-09`.)
- **Whether 5.31 holds is unknown and the tape says it did not** — the very next session gave back 3bp.
