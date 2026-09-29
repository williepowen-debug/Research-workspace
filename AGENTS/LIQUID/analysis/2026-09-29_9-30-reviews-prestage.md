# 9/30 `review_by` pre-stage: GATE-LIQ-076 and GATE-LIQ-072 (owner, LIQUID) · written 2026-09-29 ~09:0x ET

**Pre-stage, not the review.** The review is finalized on 9/30 against whatever publishes in between. Every registry consequence is **RETURNED to PROME** (owner of `PROME/GATES.tsv`); nothing here edits GATES. $0, no threshold moved.

## GATE-LIQ-076 (dealer positioning, 2-of-3 in 2 weeks), `review_by` 2026-09-30

**The pre-stage found a fire.** Conjunction MET: W1 cover +329,162 [as-of 9/22] + W3 MOVE>85/VIX<20 [9/23–9/28]; W2 unmeasured. The full grade and the required write-up are in `analysis/2026-09-29_GATE-LIQ-076-conjunction-MET.md`. The review on 9/30 is therefore:

| Item | Proposed disposition (for PROME) |
|---|---|
| State | **CONJUNCTION MET 9/25 (graded 9/29, late); write-up delivered.** Not terminal. The gate stays LIVE. |
| Reset vs latch | **Undefined in the letter.** Owner PROPOSAL (DAEDALUS ask #4): the conjunction **re-arms from zero once no leg has been met for 10 consecutive business days**. It never "un-fires" retroactively. A second MET needs a fresh W1 or W2 observation dated after the re-arm. |
| DAEDALUS ask #4 (due 9/30) | (i) W2 keyids: owed. **NY Fed PD not pulled since as-of 8/19.** Pull and name the exact series before 9/30 close, or declare W2 `UNGRADEABLE-until-keyed`. (ii) "record" (W1 level branch): owner proposal = **since registration (7/11)**, record −2,943,898 [6/30] as frozen in the letter (−2,950,000 line). **Not checked against pre-2026 history** (this session pulled the 2026 file only), so "all-history" is not claimed. The frozen number decides, so the leg does not flip on definition. (iii) MOVE producer = **VIOLET's figure (investing.com primary), yfinance as witness**, as the letter already says "VIOLET's figure governs". (iv) Reset rule: above. |
| Wiring | Owed: a 076 leg line in `boot.py` (W1 venue-pinned CFTC + W3 same-session MOVE/VIX). This is the reason it was graded late. |
| Next `review_by` | **RECOMMEND 2026-10-09**, after two more W1 prints (as-of 9/29 publishes Fri 10/2; as-of 10/6 publishes Fri 10/9). It tells whether the take-down continues. A recommendation to PROME, never self-set. |

## GATE-LIQ-072 (IG rating-vs-spread, ANY of 4), `review_by` 2026-09-30

| Leg | State at pre-stage | Basis |
|---|---|---|
| (1) 3rd/4th similar IG issuer at BB-like spreads | **UNGRADED: no event sourced.** BOND `monitors/CREDIT_PRIMARY_MARKET.md` has no IG-at-BB-like-spread entry (grep 9/29). The 9/28 newsletter (WALTER -007) reports the AI/hyperscaler 20y+ tenor share (29% vs 8%), which is tenor, not a rating-vs-spread gap. | Event leg; producer = WALTER flow / BOND primary monitor. |
| (2) IG OAS >94 | **NOT FIRED. IG 81bp [FRED BAMLC0A0CM 9/25], 13bp under.** 15-session change +0 (61st pct), d/d +2 at the 96.5th pct of days (transmission_check 9/25). BBB 99 [9/25]; ⛔ BAMLC0A4CBBB is a different series and never grades this leg. | Instrumented; as-first-published. |
| (3) SpaceX gap fails to compress 4–6wk | **CANNOT-FIRE (declared 9/29, DAEDALUS ask #3):** no producer, and its window closed ≲8/13. Letter text kept. | KB-LIQ-072 notes |
| (4) different-sponsor 144A same gap | **UNGRADED: no event sourced.** | Event leg |

**Proposed review verdict: QUIET, NOT FIRED.** The live perimeter is 1 instrumented leg (IG OAS) plus 2 event legs. **RECOMMEND next `review_by` 2026-12-31** (quarter cadence; the owner's 8/20 rationale holds: "quiet on every leg, widest margin; tighter would be theatre"). Watch-item, not a leg: IG d/d +2/+2 on 9/24–9/25 at the 95–96th pct of days while the 15-session change is flat. On 9/30, re-read the 9/28 and 9/29 cells before finalizing.

## GATE-HY-REKILL, `review_by` 2026-09-30 (not asked; one line so it is not dropped)
**NOT FIRED 0-of-2.** HY 293 [9/25], 33bp above the strict <260 line. The count has never started in 2026. The watcher repair was VERIFIED today (L493 ①). **RECOMMEND next `review_by` 2026-12-31.**
