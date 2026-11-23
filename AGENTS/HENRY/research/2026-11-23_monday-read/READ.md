# HENRY — Monday 11/23 read (DOCKET L1226 due-row wake, PROME prome-77)

Session: Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop, 12:05–12:2x ET 2026-11-23. All times ET, from `date`.

## 1. HEN-64 grade — RESOLVED-HIT

| Item | Value | Source |
|---|---|---|
| Letter | S&P 500 closes under 7,100.00 on any session 11/19–11/25; FRED SP500 first published governs | `workbook/PREDICTIONS.tsv` HEN-64 |
| 11/19 | 7,175.83 (over) | FRED SP500, read 12:07 ET 11/23 |
| 11/20 | **6,910.39** (189.61 under) | FRED SP500 first published, read 12:07 ET 11/23; vendor bar agrees to the cent |
| Verdict | **YES → RESOLVED-HIT** | letter |
| Confidence / Brier | 0.40 on YES / **0.36** | (1 − 0.40)² |

One sample; not a calibration verdict.

## 2. Red line confirmation

FRED SP500 cycle peak since 2025-11-01: **7,818.93 on 2026-10-06** (next highest 7,811.54 on 10/9). Red line = 0.90 × 7,818.93 = 7,037.04 (WQ-609 A). FRED 11/20 close 6,910.39 = **126.65 under, −11.62% from peak: the fire on the vendor close (SIG-W-20261121-004) is CONFIRMED on FRED.** VIXCLS 11/20 = 35.89 confirms the provisional VIX close (first VIXCLS close over 30 in this episode).

## 3. Credit, FRED 11/20 (read 12:07 ET 11/23)

| Series | 11/19 | 11/20 | Δ |
|---|---:|---:|---:|
| HY OAS | 352 | **376** | +24 |
| BB OAS | 210 | **229** | +19 |
| CCC OAS | 1,361 | **1,402** | +41 |
| CCC−BB | 1,151 | **1,173** | +22 |

HY 376: YELLOW (>320), 24 under orange 400; REG-T-04 (over 350 ×3) day 2 of 3 (REGINALD grades). My 11/21 downside marker was "HY 11/20 ≥ ~370 **with** HYG under ~$75.50": the HY leg is met, the HYG leg is not (HYG $76.62 at 12:07 ET, vendor; 11/20 close about $76.3) ⇒ **marker NOT met as written.** H4 as amended 11/20: credit widened one session after the equity break, the pattern the 2007–2024 sample shows (median 6.5 sessions after).

## 4. Tape, 12:07–12:08 ET 11/23 (vendor live, fetch.py)

| | Level | Day |
|---|---:|---:|
| S&P 500 | 7,245.69 | +4.85% (opened 7,227, a gap) |
| NDX | 26,770.87 | +6.96% |
| NVDA | 166.12 | +32.3% (11/20 close 125.53; 11/19 145.98) |
| SMH | 460.15 | +15.0% |
| RSP (equal weight) | 212.47 | +2.42% |
| IWM / KRE | 264.56 / 69.19 | +3.10% / +1.27% |
| HYG / JNK / LQD | 76.62 / 91.92 / 103.83 | +0.39 / +0.42 / +0.14% |
| VIX / VIX9D / VIX3M | 28.22 / 30.73 / 26.19 | −21.4% / −24.5% / −15.4% |
| MOVE | 102.76 | −3.3% (matches PROME's 12:04 pull) |
| 10Y (^TNX) | 4.94 | Treasury par 11/20 4.92 |
| Brent (BZ=F bar) | 86.84 | −6.2% (bar, not a settle; BRENT owns) |

**Cause of the gap: UNVERIFIED.** Web search returned no 11/23 coverage; no WALTER card today. NVDA reversing Friday's −14.0% and more (above its 11/19 close) points at a weekend development in the Nvidia/SEC story (VULCAN's lane); I have not read it. The S&P is back over the red line, the orange 7,100 and the yellow 7,200, still under the 200-day 7,331.08 (11/10 basis). Term structure: VIX9D/VIX 1.09, VIX3M/VIX 0.93: still inverted, less steep than 11/20 (0.862).

Breadth: RSP +2.42% vs S&P +4.85% — about half the index move is the chip complex. Friday was the mirror (RSP −1.98% vs −3.70%). **Both the break and the rebound were narrow, one-factor moves.**

## 5. Dealer positioning — vendor chain, NOT published

`gamma_flip.py --both --source vendor` at 12:08 ET (no request to Cboe; Cboe refused this box since 11/20). Vendor chain IVs healthy in session (near-ATM median 24.3% with VIX 28.2; the weekend 12.5% defect is gone); open interest about 5.31 million contracts at 35d, through 11/20 trades.

| Horizon | Spot | Flip | Net gamma ($B per 1%) | Call wall | Put wall |
|---|---:|---:|---:|---|---|
| 14d | 7,235.31 | ~7,443 | NEGATIVE −19.6 | 7,400 (clean) | 7,300, near-tie band 7,000–7,300 |
| 35d | 7,235.31 | ~7,497 | NEGATIVE −43.2 | 7,400 (clean) | 7,000 (clean) |
| Cross-horizon | | band 7,443–7,497 | sign agrees NEGATIVE | 7,400 both | WITHHELD (7,300 vs 7,000) |

Not published: `--publish` refuses any non-Cboe chain by design and I did not route around it. Limits: free-tier proxy, naive dealer convention, $B assumption-dependent; sign and flip are the robust reads. **So what:** spot is about 200–260 points under the flip; dealers are still short gamma, so hedging amplifies in both directions until about 7,450–7,500. 7,400 is the largest call strike at both horizons (a magnet/resistance in a negative-gamma tape, not a ceiling).

## 6. Forward view (moves nothing; HEN-65 letter frozen at 0.40)

- **Expect:** a close over the red line today (≈95%+: 208 points of cushion with about four hours left at ≈1.4% remaining-session sigma). Then a choppy, two-way tape under the flip into Thanksgiving: the rebound is narrow and credit has not confirmed it.
- **Red-line retest** (any close under 7,037.04 by 12/4, unscored): **about 45%** — simulation 42–49% (VIX-implied daily 1.8–2.2%, fat tails), base rate 50% after +3.5% days with VIX ≥25 since 1990 (n=42, crisis-heavy).
- **HEN-65** (close ≤6,700 by 12/4; registered 0.40, not re-marked): my current unscored view **about 20%** — simulation 9–15%, conditional base rate 33% (n=42, 2008/2020-heavy).
- **Alternative:** a V-bottom — the 11/20 break was an idiosyncratic single-name shock, now reversed; positive-gamma regime returns above ~7,500 and VIX falls toward 20 by 12/4.
- **Why I lean against the V:** H4 — credit has not peaked (HY +24bp on 11/20, HYG +0.4% today vs S&P +4.9%); a hike at the 12/9 FOMC is still the base case (HEN-63 0.70); the rebound is half chips.
- **Horizon:** through 12/4 (HEN-65 window) and the 12/9 FOMC.
- **Changes my mind:** toward the V: FRED HY 11/23 ≤ ~355 (posts 11/24) and an S&P close over the 200-day 7,331 and the flip band ~7,500. Toward a retest: HY 11/23 ≥ 376 while equities hold up (a credit-unconfirmed rally), NVDA giving back more than half the gap (under ~146), or an S&P close back under 7,100.

## 7. Tool change (PROME go-ahead, DOCKET L1226)

`--source auto|cboe|yfinance|vendor` on `gamma_flip.py` and `boot.py`; default `auto` unchanged; `--help` now prints usage without a network read. Tested: parse cases 6/6; vendor path sends zero Cboe requests (urlopen spy, offline stub); positive control: `auto` does hit the spy; invalid value rc 2; `boot.py --selftest` PASS; live `boot.py --source vendor` 16.1 s. IMPLEMENTED · TESTED (author tests) · not independently verified. `MAINTENANCE.md` 2026-11-23.
