# MIDAS → PROME · 2026-10-01 ~12:5x ET · touch 2: the silver/PGM band draft (WQ-352) refreshed to 9/30 closes

**On Will's word 12:49 ET ("go for the six"), PROME re-ping.** $0 · ⛔ the draft stays NOT IN FORCE · no band, score or threshold moved.
**Where:** a dated **ADDENDUM 2026-10-01** at the end of `AGENTS/MIDAS/analysis/2026-09-25_silver-pgm-bands-DRAFT.md`. The 9/25 text is untouched. The stats script was re-run unchanged on closes through 9/30 (it dropped the partial 10/1 bar itself).

## 1. Refreshed headline figures (no-roll ETFs, 9/24 → 9/30)

| Metal | Off the 1-year high | vs 200-day average |
|---|---|---|
| Silver (SLV) | −45.4% → **−48.4%** | −12.6% → **−17.3%** |
| Platinum (PPLT) | −37.0% → **−38.9%** | −10.1% → **−12.9%** |
| Palladium (PALL) | −38.1% → **−41.3%** | −14.9% → **−19.0%** |

**Would the newer data change a proposed line? No.** No new episode starts at any drafted line. Six fire-rate cells moved by 0.01/yr, which is a longer denominator and not a different history.

## 2. Scores under the draft, and the composite effect

| Metal | Score 9/24 | **Score 9/30** | Next level |
|---|---|---|---|
| Silver | 3 🟠 | **3 🟠** | 2.7 pts to 🔴 |
| Platinum | 2 🟡 | **2 🟡** | 2.1 pts to 🟠 |
| Palladium | 2 🟡 | **2 🟡** | ⚠️ **1.0 pt to 🟠** |

**Composite effect of approval: still 8/20 → 10/20 (M2 1 → 3), all of it from the rule change.** Every crash-leg (event) reading has decayed: silver's last new crossing was −40% on 3/20, platinum's −30% on 3/20, palladium's −40% on 6/8. If palladium closes below −20% vs its 200-day average after approval, I2 goes 2 → 3 and the composite to 11.

## 3. My strongest objection to my own draft (in the addendum as A4)

The bands arrive after the damage, and the fast part is already off. Approve today and the alarm says "silver is in a decline" about a metal already 48% off its high. Its trend line first fired on 6/24, about five months after the top. The crash leg, which did catch January within days, has stepped down to nothing by now, so the jump to 10/20 announces what Will already knows. It also rests on lines drawn on history that includes the collapse. **Amendment I would accept first:** adopt the bands but leave them unscored for one month, so the first score move comes from a line crossed on data that arrives after approval, not from an accounting change.

## 4. COT 9/29

**Not published.** `cot_gold.py --expect 2026-09-29` returns WAIT and is still serving 9/22. CFTC releases it Fri 10/2 15:30 ET. §4 positioning stays as-of 9/15 (context only).

```
STATUS: ✅ DONE
CHANGED: AGENTS/MIDAS/analysis/2026-09-25_silver-pgm-bands-DRAFT.md (dated ADDENDUM appended), AGENTS/MIDAS/OPEN_ITEMS.md, AGENTS/MIDAS/STATUS.md, PROME/inbox/this memo
RESULT: Band draft refreshed to 9/30 closes: SLV −48.4% off high / −17.3% vs 200d, PPLT −38.9 / −12.9, PALL −41.3 / −19.0. No drafted line changes (6 rate cells drift 0.01/yr, no new episodes). Scores unchanged 3/2/2, so approval still moves the composite 8 → 10. Palladium is 1.0 pt from orange. My strongest objection, with an amendment (adopt but unscored for one month), is written for Will.
GAPS: COT 9/29 not yet published (CFTC Fri 10/2 15:30 ET), so positioning context stays as-of 9/15. Fire rates remain in-sample (unchanged limit).
WILL_NEEDS: Will rules on WQ-352: adopt the silver/platinum/palladium bands as drafted, adopt them unscored for a month, amend, or decline.
FOLLOW-UP: MIDAS consumes the 9/29 COT at its next boot (on/after 10/2 15:30 ET); on Will's word MIDAS encodes the ruled bands in its charter THRESHOLDS and re-scores.
```
