# QQQ — MEASURED FINDINGS

> ⚠️ **Every figure here is a `2026-08-04` snapshot and decays.** `scripts/v_episodes.py` is the authority; this file is its transcript. **If they disagree, the script is right.** Re-run before any of this carries a ticket.
> **Live pulls: QQQ $722.87 · VXN 25.9 · VIX 16.5 · SPX 7,743 — 8/4 ~14:00 ET.**

---

## 1. 🔴 DATA INTEGRITY — read this before any historical QQQ base rate, from any source

**QQQ launched 1999-03-10 and split 2:1 on 2000-03-20. Over 1999–2003 the QQQ and `^NDX` series disagree materially:**

| Era | mean daily \|NDX−QQQ\| | max | days >1pp apart |
|---|---|---|---|
| **1999–2003** | **0.492pp** | **6.72pp** | **137** |
| 2004–2026 | 0.065pp | 3.70pp | 8 in 23 years |

**An ETF cannot miss its index by 6.7% in a day.** One series is wrong in that window and the divergence decays monotonically as QQQ matured, which points at early QQQ.

★ **Why this dominates everything below:** 1999–2003 supplies **22 of 33** episodes under this event definition — *and those rows carry the opposite forward sign to every other era.* **The least trustworthy rows are simultaneously the most numerous and the ones driving the answer.**

⛔ **Consequence, adopted:** ex-bubble is the **honest default** for anything decision-bearing, not a robustness toggle. Any QQQ base rate quoted without its era split is not usable.

*Method note: this was found by running the episode finder on **both** series and matching the results. The correlation alone (0.980) looked fine and hid it — `finding_base_rate_the_instrument_before_its_event_table`.*

---

## 2. THE 2026-07/08 EPISODE — an ordinary drop, retraced at a top-1% pace

| | |
|---|---|
| Drawdown 6/2 → 7/29 (closes) | **−11.22%** |
| QQQ drawdowns ≥10% since 1999 | 21 — one every **1.3 years**; 14 were deeper ⇒ **33rd pctile: ORDINARY** |
| Recovery 7/29 → 8/4, 4 sessions | **+9.24%** |
| Percentile of all 6,889 four-day windows | **99.17th** |
| Retrace of the drawdown | **73.1%** |
| Drawdown from ATH now | **−3.0%** |

**★ The single most unusual feature is not the +9.2% — it is that it happened at VIX 16.5.** The lowest VIX of any prior instance in 27 years was **18.5** (2002-05-16); the median was **24.7**. **Rallying this hard in this much calm has no precedent in the series.**

---

## 3. FORWARD BEHAVIOUR — the base rate inverts across the bubble line

*`^NDX`, 1987–2026, threshold = the episode's own 4-session return (~9.3%), de-clustered at 10 sessions.*

| Cohort | n | 1m med | 1m win | 3m med | 3m win |
|---|---|---|---|---|---|
| ALL prior | 33 | +0.3% | 52% | +4.1% | 58% |
| **bubble 1999–2003** *(data-suspect)* | 22 | −1.0% | 50% | **−2.6%** | 50% |
| **EX-BUBBLE** | 11 | +2.2% | 55% | **+21.9%** | **73%** |
| NEAR-HIGHS (dd > −15%) | 8 | +1.3% | 62% | +4.4% | 62% |
| **NEAR-HIGHS EX-BUBBLE ← today's config** | **3** | +2.2% | 67% | +21.9% | 67% |

### ⚠️ The cohort that matches today is n=3. Quote the n, never the % alone.

| | 1m | 3m |
|---|---|---|
| 1991-01-21 | +15.6% | +26.6% |
| 1997-05-02 | +2.2% | +21.9% |
| **2022-03-18** | −1.5% | **−21.9%** |

**Two strong continuations and one severe trap.** 2022-03-18 looked exactly like this — sharp recovery, near the highs — and was a bear-market rally. **Any "75% win rate" on this configuration is three observations in a trenchcoat.**

---

## 4. THE PRIOR HIGH — rejection is rare, but *reaching* it is rarer

| | |
|---|---|
| Episodes with a ≥8% prior drawdown | 29 |
| **Carried back to the old high within 250 sessions** | **7 = 24%** |
| Of those, **broke through on first test** | **6 = 86%** |
| Rejected on first test | 1 = 14% |
| **Ex-bubble** | **5 / 5 broke through = 100%** |
| Median sessions from the V to first touch | **18** |

**⇒ A rejection at the prior high is NOT the modal path — it is rare. But that barely matters, because the modal path is never getting there (76%).**

⚠️ **Conditioning caveat:** most sample episodes sat 40–80% below their high, making "return to the old high" a multi-year proposition. **Today is 3% below the ATH** — and the five ex-bubble successes were all shallow-drawdown cases like this one, so 24% understates it badly for this configuration.

**In levels:** prior high **745.34 close / 748.65 intraday**; QQQ 722.87 = **+3.1% away**; median 18 sessions from the V ⇒ a first test around **mid-to-late August**.

> 🔴 **Level discrepancy, open:** PROME's question #3 refers to *"the prior-high band"* but cites **726–730**. That is **not** the prior high — it is the **78.6% retracement** (656.30 + 0.786 × 92.35 = **728.9**). Different test, different base rate. **Unresolved; do not treat the two as interchangeable.**

---

## 5. THE VOL / VOLUME REGIME — half of Will's premise checks out

| | | |
|---|---|---|
| Realized vol 10d | **31.5%** | |
| Realized vol 20d | **26.3%** | **86th pctile** (2y) |
| Implied (VXN) | 25.9% | 78th pctile |
| **RV20 − IV** | **+0.3pp** | 78th pctile |
| Avg daily range, last 10d | **1.94%** vs 1.41% 1y | **1.38×** |
| **Volume, 20d avg vs 1y avg** | **0.77×** | ⚠️ **below average** |

**✅ The movement is real** — daily range is 1.38× normal and realized vol sits at the 86th percentile.
**❌ The participation is not** — 20-day volume is **77% of the annual average.** Wide ranges on light volume *feel* like heavy volume; that is the illusion.

### Construction consequences

1. **Long premium is not expensive here.** RV ≈ IV with the spread at the 78th percentile ⇒ options are fairly-to-cheaply priced against what the index is actually doing. **Buying optionality is defensible; this is not a "vol is rich, sell it" tape.**
2. **⚠️ But you are buying after the move.** RV at the 86th percentile means the expansion has already happened. **Cheap relative to realized ≠ cheap in absolute terms.**
3. **Light volume cuts against trend-continuation reads.** A breakout on below-average participation is weaker evidence than the range implies — relevant directly to the 8/4 break through 712.
4. **⇒ The vol regime does NOT favour either direction.** It favours *defined-risk structures over naked directional ones*, which is where §2 of `PLAYBOOK.md` starts.

---

## 6. Open questions

- **Level discrepancy** (726–730 vs 745–749) — with PROME, unresolved.
- **What drove +3.2% on 8/4?** Unknown at time of writing. **A 3% single-session move with no identified cause is a reason not to size, in either direction.** Owner: VULCAN (AI-capex/concentration) or VIOLET (market structure).
- **Down-volume vs up-volume split** across the selloff and recovery — not yet measured; would test whether the recovery is accumulation or drift.
- **Sample reconciliation with PROME** — their "19 analogues / 14-of-18" and this file's 33 episodes are different selection rules for the same question and have not been reconciled.
