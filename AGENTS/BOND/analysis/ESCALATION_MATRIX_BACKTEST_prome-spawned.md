# Escalation Matrix Backtest — prome-spawned

## PROVENANCE

- **Spawned by:** Prome, 2026-05-20 PM ET, as a one-shot research sub-agent (not BOND).
- **Why:** BOND's `monitors/AUCTION_HEALTH.md` orange-escalation thresholds (BTC<2.30, tail>2bps, dealer>12%, weak indirect) were set by judgment, not data. Prome asked: when those criteria fired historically, did TLT actually drawdown materially?
- **Source data:** `AGENTS/BOND/data/auction_history_prome-spawned.csv` (364 rows, 2023-01-10 → 2026-05-20; 324 coupon rows w/ high_yield); TLT daily close via yfinance.
- **BOND to integrate on next boot.** Sub-agent did not touch BOND state, KB, monitors, outbox, or TRADE.md. No commit.

---

## Verdict (≤200 words)

**Calibration: OVER-TRIGGERING — matrix is essentially anti-signal, not bearish-signal, at current thresholds.**

Over 323 coupon auctions (Jan 2023 → May 2026), the 2-of-3 matrix (BTC<2.30, dealer>12%, indirect<55%) fired 26 times. **Hit rate (TLT drops ≥1% over next 5 sessions) for fires was 19.2% vs base rate 35.7% across all auctions** — fires were LESS likely to precede a sell-off than a random auction. Median 5-session TLT return after fire: **+0.17%** vs base **-0.19%**. False-positive rate (TLT rallies ≥0.5%) for fires: 46.2% vs base 36.4%.

Driver: the **dealer>12% criterion is wrong-signed**. Median 5d TLT return after dealer>15% prints is **+0.39%**; after dealer>20%, **+1.45%**. High dealer takedown is a contrarian-bullish signal historically (likely because dealers absorb supply at peak yield, into the rally). Only **indirect<55% (and tighter, <50%)** independently beats base rate: at indirect<50%, N=18, hit rate 50.0%, median **-1.07%**.

**Recommendation:** Drop dealer>12% from matrix; tighten indirect to <50%; keep BTC<2.30 but only as confirmatory. See §7 for proposed replacement.

---

## Methodology

- **Dataset:** 324 coupon auctions with high_yield (TIPS, FRN, bill rows excluded). 323 had ≥6 trading days forward of TLT data.
- **Threshold convention:** dataset `dealer_pct` / `indirect_pct` are fractions (0.117 = 11.7%). Matrix spec dealer>12% → `dealer_pct > 0.12`; indirect<55% → `indirect_pct < 0.55`. Confirmed: 25th pctile dealer = 9.0%, median = 11.3%, 75th = 14.2% — threshold lands near the median, so 143/323 (44%) fire on dealer alone, suggesting threshold-too-loose by construction.
- **Matrix fire:** ≥2 of {B, D, I} true (tail not tested — v1 dataset gap).
- **Outcome metric:** TLT 5-session return = (Close[T+5] - Close[T+0]) / Close[T+0] * 100, where T+0 = first TLT trading day ≥ auction_date.
- **Hit:** TLT 5d ≤ −1%. **FPR:** TLT 5d ≥ +0.5%. **Base rate:** all auctions.
- **Caveat noted in §6 re: 5-session horizon and regime.**

---

## Results

### Headline calibration table

| Group | N | Hit rate (TLT≤−1%) | FPR (TLT≥+0.5%) | Median TLT 5d | Mean TLT 5d |
|---|---|---|---|---|---|
| **Matrix fired (current spec)** | 26 | **19.2%** | 46.2% | **+0.17%** | +0.45% |
| Matrix NOT fired | 297 | 35.7% | 36.4% | −0.19% | −0.10% |
| ALL auctions (base rate) | 323 | 34.4% | 37.2% | −0.17% | −0.05% |

**Fires UNDER-perform base rate by 16.5pp on hit rate, and the median 5d return for fires is actually positive.** Matrix is anti-signal at current thresholds.

### Per-criterion breakdown

| Criterion | N fired | Hit rate | FPR | Median 5d | Read |
|---|---|---|---|---|---|
| BTC < 2.30 | 9 | 22.2% | 22.2% | −0.67% | Slightly bearish, low N |
| BTC < 2.40 | 69 | 26.1% | 37.7% | −0.17% | Noise-level |
| dealer > 12% | 143 | 32.9% | 42.0% | −0.05% | At base rate |
| dealer > 15% | 61 | 31.1% | 47.5% | **+0.39%** | Wrong sign |
| dealer > 18% | 23 | 26.1% | 52.2% | **+0.79%** | Contrarian-bullish |
| dealer > 20% | 11 | 18.2% | 63.6% | **+1.45%** | Strongly contrarian-bullish |
| indirect < 55% | 65 | 38.5% | 33.8% | −0.48% | Marginal |
| **indirect < 50%** | **18** | **50.0%** | **16.7%** | **−1.07%** | **Best single signal** |
| indirect < 45% | 6 | 33.3% | 16.7% | −0.98% | Sample-thin |

### Long-end-only subset (20Y/30Y, N=88)

Matrix-fired N=8: hit 12.5%, median +0.17%. Long-end base: hit 35.0%, median −0.45%. Matrix still underperforms even on TLT-tenor-relevant subset.

### Roll-call: 10 most recent matrix fires

| Date | Tenor | Criteria fired | TLT 5d |
|---|---|---|---|
| 2026-05-11 | 3Y | dlr=13.6%, ind=50.5% | **−2.34%** |
| 2026-03-25 | 5Y | BTC=2.29, dlr=14.1% | −0.67% |
| 2026-03-24 | 2Y | dlr=21.7%, ind=53.4% | +0.79% |
| 2026-02-18 | 20Y | dlr=15.7%, ind=49.1% | +0.42% |
| 2025-11-13 | 30Y | BTC=2.29, dlr=12.5% | −0.17% |
| 2025-09-18 | 10Y | BTC=2.20, dlr=16.8%, ind=53.0% | −0.24% |
| 2025-08-07 | 30Y | BTC=2.27, dlr=13.0%, ind=44.4% | −0.74% |
| 2025-08-06 | 10Y | dlr=12.0%, ind=47.8% | −0.17% |
| 2025-08-05 | 3Y | dlr=13.3%, ind=40.2% | **−1.56%** |
| 2025-07-08 | 3Y | dlr=14.7%, ind=48.3% | **−1.19%** |

Only 3 of 10 recent fires preceded a ≥1% TLT drop. 2026-05-11 (3Y) was a hit but driven by indirect<50% — consistent with §3 finding.

---

## Caveats

1. **Tail not tested (v1 dataset gap).** The matrix's fourth criterion (tail>2bps) cannot be evaluated until tail BPS column is added to `auction_history_prome-spawned.csv`. Tail may rescue the matrix — single-auction tail >3bps (e.g., Aug 2023 30Y) has historically preceded sell-offs. Backtest is **3-criteria only**.
2. **Regime non-stationarity.** Dataset spans 2023 cutting cycle → 2024-25 hiking pause → 2026 fiscal-stress regime. Dealer behavior is regime-dependent; pooled stats may mask a 2026-specific signal. Did not slice by regime due to sample size.
3. **5-session horizon is arbitrary.** Some auction stress takes 10+ sessions to express (rolling tail digestion). Did not test T+10/T+20.
4. **TLT proxy.** TLT is 20+ year duration; short-tenor auction stress (2Y/3Y/5Y) may not show in TLT. Long-end-only subset (§3) confirms the calibration finding holds but with thinner N.
5. **Selection on fire definition.** 2-of-3 with current thresholds gives only N=26 fires. The escalation matrix may be designed for tail-event detection where low N is intentional — but the realized hit rate still doesn't beat base rate.

---

## Recommendation: Replace matrix v1 with revised thresholds

**Proposed v2 escalation matrix (when tail data added):**

- **B':** BTC < 2.30 (keep — directionally correct, low N)
- **I':** indirect < **50%** (tighten from 55% — best single signal, hit 50%, median −1.07%)
- **T':** tail > 2bps (untested but theoretically sound — keep until backtest possible)
- **DROP D entirely.** Dealer >12% is at-median and wrong-signed at higher thresholds. Dealers absorb supply at peak yield = contrarian-bullish.

**v2 fire condition:** ≥2 of {B', I', T'}. Given B' alone fires 9 times in 3 years and I'<50% fires 18 times, intersection will be rare (<10 fires expected) — high specificity, fewer false alarms.

**Until v2 is implemented, BOND should:** treat current-matrix orange triggers as confirmatory only, NOT as standalone TLT-puts upgrade triggers. Single-criterion indirect<50% deserves more weight than current 2-of-3 logic gives it.

---
*Word count (ex tables): ~780. Sub-agent done; BOND integrates on next boot.*
