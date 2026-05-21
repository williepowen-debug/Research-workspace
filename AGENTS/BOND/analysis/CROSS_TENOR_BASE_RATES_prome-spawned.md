# Cross-Tenor Auction Demand Base-Rates

**PROVENANCE:** Prome-spawned research sub-agent, 2026-05-20 PM ET.
Spawned to replace BOND's vibes-based "20-25%" estimate for tomorrow's (5/21) 10Y reopening with empirical base-rates drawn from `AGENTS/BOND/data/auction_history_prome-spawned.csv` (v1, 364 rows, 7 tenors, 2023-01-10 → 2026-05-20).
BOND integrates on next boot. Read-only on dataset. Not committed.

---

## Verdict (empirical)

Across all same-week (≤5 business days) coupon-auction pairs in the dataset:

- **P(Leg2 weak | Leg1 strong) = 11.7%** (12/103) — strong demand persists; weak follow-throughs are about half the unconditional rate
- **P(Leg2 weak | Leg1 weak) = 25.9%** (28/108) — weakness mildly autocorrelates
- **P(Leg2 weak | Leg1 neither) = 23.6%** (55/233) — close to baseline
- **P(any auction weak, unconditional) = 22.6%** (67/296)

**Drill to Leg2 = 10Y specifically (N=36, mostly 3Y→10Y refunding sequence):** P(10Y weak | Leg1 strong) = **8.3%** (1/12). Sample small; treat as directionally consistent with the all-tenor result, not independently authoritative.

**Calibration on BOND's 20-25%:** that estimate is *too high*. Empirical conditional is ~12%, with the 10Y-specific N=12 subset even lower. BOND was anchoring near the unconditional base-rate; the conditional on a strong Leg 1 shifts it materially lower. Use **~12% as a base estimate**, widen to 10-18% to account for small-sample uncertainty and regime drift.

---

## Methodology

**"Weak print" definition** (BOND WATCH §3, adapted): for each auction, classify against a trailing 12-month per-tenor window:
- weak BTC: below 25th pct
- weak indirect: below 25th pct
- weak dealer: dealer_pct above 75th pct
- **weak overall:** ≥2 of 3 above

Mirrored definition for **strong** (each metric above/below opposite quartile, ≥2 of 3). All others = **neither**.

Auctions with <4 prior in-tenor 12mo observations excluded (28 early-period auctions dropped → 296 classified).

**Pair construction:** for each auction (Leg 1), find every subsequent coupon auction within 5 business days (Leg 2). Excludes TIPS, includes all coupon tenors (2/3/5/7/10/20/30Y). Same Leg 1 can pair to multiple Leg 2s in the same week (e.g., refunding weeks where 3Y→10Y→30Y all chain).

Total pairs: **444**.

---

## Results

| Condition (Leg 1) | N pairs | P(Leg 2 weak) |
|---|---:|---:|
| Strong | 103 | **11.7%** |
| Weak | 108 | 25.9% |
| Neither | 233 | 23.6% |
| (Unconditional Leg 2 weak rate) | 444 | 21.4% |

| Subset (Leg 2 = 10Y) | N | P(weak) |
|---|---:|---:|
| Leg 1 strong | 12 | 8.3% |
| Leg 1 weak | 5 | 20.0% |
| Leg 1 neither | 19 | 26.3% |
| All Leg 2 = 10Y | 36 | 19.4% |
| 10Y unconditional (all 10Y prints) | 37 | 18.9% |

Leg-1 tenor distribution when Leg 2 = 10Y: 3Y (34), 2Y (1), 7Y (1). Almost all are the standard refunding-week 3Y→10Y sequence.

---

## 20Y → 10Y specific (broadened, N too small)

Direct 20Y → 10Y same-week pairs: **N=0**. Structurally, 10Y refunding new-issues print in months 2/5/8/11 *before* the 20Y in the same month; 10Y reopenings (months 1/3/4/6/7/9/10/12) print ~10 bdays after the prior 20Y, which exceeds the 5-bday window.

**Broadened to 10 bdays:** 20Y → next 10Y, **N=2**.
- 2024-10-23 (20Y, neither) → 2024-11-05 (10Y, strong)
- 2025-07-23 (20Y, strong) → 2025-08-06 (10Y, weak) ← the only strong→? case

**N=1 of the analog case yields a 100% weak rate**, which is statistically meaningless. **Insufficient sample; the 20Y→10Y specific base-rate cannot be reliably estimated from this dataset.** Defer to the all-tenor strong→? rate (11.7%) as the best available anchor.

---

## Caveats

1. **Regime non-stationarity:** 2023-2026 spans a rate-cutting cycle, two refunding-anxiety episodes (Oct 2023, Apr-May 2025), and shifting indirect/dealer behavior post-Apr-2025 trade-war shock. The historical base-rate may understate forward weak-print probability if the dealer-pct-rising regime BOND flagged is structural.
2. **Indirect_pct denominator:** v1 uses indirect / offering_amt, not / competitive_accepted. Consistent across all rows so cross-tenor comparison is valid; absolute thresholds shift ~1-2pp lower than the v2 convention will show.
3. **2-of-3 weak threshold:** A 3-of-3 ("decisive weak") definition would be more selective. Not computed here; 2-of-3 is the BOND-WATCH operational definition.
4. **Strong-Leg-1 persistence is real but moderate:** the 11.7% vs 22.6% delta (about half) is the empirically measured "good auction begets good auction" effect — meaningful but not overwhelming. Don't over-extrapolate.
5. **What is NOT captured:** macro tape between Leg 1 and Leg 2 (CPI prints, Fed-speak, geopolitical shocks within the 5-day window). Today→tomorrow has minimal scheduled event risk, which slightly favors the strong-persistence read.

---

```
STATUS: DONE
CHANGED: AGENTS/BOND/analysis/CROSS_TENOR_BASE_RATES_prome-spawned.md
RESULT: P(Leg2 weak | Leg1 strong) = 11.7% across 103 same-week coupon-auction pairs (≤5 bdays). Leg2=10Y subset (N=12) gives 8.3% — directionally consistent, small N. BOND's 20-25% vibes estimate is too high; ~12% (range 10-18%) is the empirically supported anchor.
GAPS: Direct 20Y→10Y same-week pairs structurally absent in dataset (10Y typically prints BEFORE 20Y in refunding weeks). Broadened 20Y→next-10Y within 10bd gives N=2, insufficient.
WILL_NEEDS: None
FOLLOW-UP: BOND on next boot: (1) update WATCH §3 / TRADE.md probability assumption from "20-25%" to "~12% base, 10-18% widened"; (2) if tomorrow's 10Y prints weak, that becomes a 1-in-8 outlier — strong signal worth scaling; if normal/strong, it confirms regime continuity and the TLT-put thesis on this specific catalyst is exhausted; (3) consider re-running this analysis with v2 dataset (correct indirect denominator) and 3-of-3 weak threshold for robustness check.
```
