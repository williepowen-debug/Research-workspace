# PRE-REGISTRATION — the October 2026 Trepp prints (DQ ~early Nov, SS ~mid-Nov)

**Written:** 2026-10-22 (Thu) 13:44 ET, before either October print can exist (the month has not ended; Trepp's September DQ excerpt published 10/02 and SS 10/13). Will-directed (2026-10-22 13:19 ET, the sweep follow-up: *"Lets do this next/now"*).
**Status:** ⛔ **FROZEN ON COMMIT OF THIS FILE.** Append a dated grading record below §6; never edit above it. The value of this document is its date.
**Precedents:** `registry/PREREG_2026-09_TREPP_PRINT.md` (its §3 limits carry forward unchanged; **read that §3 before grading**) and `registry/PREREG_2026-10_TREPP_PRINT.md` (its §2 tie convention is restated below verbatim in substance, because this is the print it decides).

---

## 1. What is being graded

| Trigger | Band (frozen 7/21) | State entering October | What October CAN do |
|---|---|---|---|
| `CREED-T-01a` office DQ | `> 12`, sustain 2 | **Sep 12.16 = leg 1 of 2** (graded 10/21) | **FIRE**, if October prints ≥ 12.01. Otherwise the clock **resets to 0** (sustain means consecutive) |
| `CREED-T-01b` office SS | `> 18`, sustain 2 (sustain amended 8/27, Will) | Sep **16.85**, 0 of 2 | At most **leg 1**, and only on a +116bp month. The largest consecutive-month office-SS rise CREED can observe is +36bp (May → Jun); the largest move either way is the Apr → May −91bp (17.66 → 16.75). **October cannot fire T-01b** |
| `CREED-T-02` | spent | fired 8/20 | nothing. **Do not re-fire or cite as fresh confirmation** |
| `CREED-T-08a` | `< -10` TR | FIRED 9/24 | nothing on this document. The CMBS print does not grade the tape |
| `PRED-CREED-001` (Kernel-pinned) | "office DQ > 12.00 and HOLDS for 2 consecutive prints, by 12/31" | Sep 12.16 | **Its condition is MET on the same pair** if October ≥ 12.01. ⛔ **CREED does not edit the row** (Kernel row pin, sha `1a63c2ff0d`): packet PROME for the Will/Kernel resolution, as for 004/007 on 9/26. If October ≤ 12.00, the prediction stays OPEN with Nov and Dec prints remaining (Dec DQ publishes ~early Jan; whether a print published after 12/31 counts is an open resolution question, not decided here) |

## 2. 🔴 The `T-01a` decision rule, fixed in advance

- **Basis:** Trepp's headline office delinquency rate **as published to 2 dp** (Table 2, all vintages, col 1), the same cell graded for September. Not the CMBS 2.0+ table, not the ex-defeased figure, not a secondary's rounding. **If the full PDF is not reachable, grade only from a primary Trepp text that names the 2dp figure; a secondary's figure is PRIMARY-CITED and the grade is marked provisional until the PDF is read.**
- **Tie convention (unchanged from PREREG_2026-10 §2, trap #22):** `12.00` is **not** `> 12`. **12.01 fires.** The unrounded ambiguity is resolved by the as-published convention.
- **If October prints ≥ 12.01:** the permitted sentence is *"`CREED-T-01a` FIRED on the October print (Sep 12.16, Oct X): office CMBS delinquency above 12% for two consecutive months."* Log the fire in `registry/CREED_T_FIRED_LOG.tsv` the same session, with effective date = the October print's publication date.
  - ⛔ **Refuse:** "record office delinquency" (Jan-26 printed **12.34**; a fire between 12.01 and 12.34 is a **return**, not new territory); "banks are next" (S3 is graded on FDIC data, not on CMBS); any S1 score stated as moved before Will rules.
  - **S1 score:** a fire meets S1's upgrade trigger. **CREED PROPOSES the S1 score to Will and does not move it itself** (the S8a precedent, WQ-303, 9/28). The convergence composite stays 27/45 until he rules.
  - **Routes (Route Matrix, on FIRE only):** REGINALD action (bank-exposed metro overlap from the month's named loans) · LIQUID info if the month's new delinquencies are maturity/refinancing-driven · PROME (Will-facing; plus the PRED-001 Kernel packet).
- **If October prints ≤ 12.00:** the permitted sentence is *"`CREED-T-01a` not fired; the clock resets to 0 (Sep 12.16, Oct X)."* ⛔ **Refuse** "office stress easing" on any move smaller than the series' own noise (below). A reset is a sustain failure, not a reversal.
- **Noise yardstick, stated now so it cannot be chosen after:** office DQ |MoM| Mar → Sep 2026 = 2 / 16 / 4 / 34 / 9 / 16bp, **mean 13.5bp, n=6** (Feb's −114bp and Mar's +51bp are lookback-derived and excluded, as in PREREG_2026-10). A **named heuristic, not σ**. October resets the clock only by falling **≥ 16bp** (to ≤ 12.00), which is ~1.2× that mean.
- **Distribution context:** 2026 path Jan 12.34 · Feb 11.20 · Mar 11.71 · Apr 11.69 · May 11.53 · Jun 11.57 · Jul 11.91 · Aug 12.00 · Sep 12.16 (`VX_HISTORY`, CANONICAL). Four consecutive rises Jun → Sep.

## 3. What would actually inform the thesis — watch regardless of `T-01a`

1. **The mechanism, not the symptom.** Maturity-adjusted DQ (Sep 9.66) and the performing-matured-balloon bucket (Sep 1.64% of balance). September's fall in both was **conversion into non-performing**, per Trepp. **Read Trepp's attribution before writing any word about the two levels** (the September near-miss on F1).
2. **The newly-delinquent $ total and its matured-balloon share.** September printed 68% with **no $ base**. If October prints a dollar total, extend `VX-3.05` **before** writing any word about the share (trap #6).
3. **Gross flows beside every net** (trap #23): newly delinquent $ vs cures $, SS in vs out. If the headline moves by less than a named cure, say the cure's size. **A cure into PERFORMING MATURED BALLOON is a reclassification, still past maturity** (the September $384.3M LA tower).
4. **The payoff rate for October** (Trepp via Commercial Real Estate Direct, `KB-CREED-066`): Jul 72.05 → Aug 51.45 → Sep 57.98. Record the October figure with its label ("conduit" vs "CMBS loans").
5. **Refinancing cost:** the 10-year on the print date and CREFC's new-issue 5-yr conduit coupon (last 3 months 6.89% vs 6.53% YTD, 10/16 snapshot; `KB-CREED-061`). The channel CREED named on 10/22 is the base rate, not the CMBS spread.
6. **Named loans:** any Florida asset → CORAL; send the zero if none, naming any multi-property portfolio whose locations the text does not give (the September Starwood mall-portfolio caveat).

## 4. Falsifiers — what would make CREED WRONG, registered now

- **F1:** maturity-adjusted DQ **falls** AND the performing matured balloon share **falls** AND Trepp attributes the drop to **payoffs/refinancings**, not to conversions into the headline. That would say the maturity wall is clearing, not converting.
- **F2:** Trepp's monthly on-time payoff rate **rises for a second consecutive month** (October above September's 57.98%) **alongside falling SS transfers** (October in < September's $2.65B). That would undercut "the constraint is the ability to clear." ⚠️ If the October payoff figure is labelled "CMBS loans" rather than "conduit", grade it and say so.
- **F3:** the 10-year falls back **below ~4.75%** and the S8a reading returns **above −10** (TR) before the October DQ print. That would mark the tape move as a rate episode that passed. It would not un-fire `T-08a`.
- ⚠️ **An untestable falsifier is not a passed one.** If an instrument does not print or is not fetched, grade that falsifier UNTESTED, and fetch it later (as F2 was, on 10/22).

## 5. What CREED will NOT do on this print

No band, operator, sustain or confidence edit. **No S-score moved by CREED** (a T-01a fire produces a PROPOSAL to Will). No edit to the Kernel-pinned `PRED-CREED-001` row. No shape word on a share without its denominator. No reading of a sub-noise headline move as a direction.

---

## 6. Grading record — append below, do not edit above
