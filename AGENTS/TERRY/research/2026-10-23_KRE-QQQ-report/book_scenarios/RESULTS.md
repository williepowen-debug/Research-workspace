# See-saw book under scenarios — MODEL (quotes pulled 2026-10-23 13:38 ET)

Black-Scholes European puts, r 4.0%, no dividends, today's vendor implied vol per contract scaled by the stated multiplier. Changes are model value at the horizon minus model value now (same model both ends, so the vendor-mid vs model gap cancels). Single names move by 1-year two-factor betas. Not fills; not broker marks.

## Lines and current screening marks

| Leg | Acct | Line | Qty | Spot | Bid / Ask | IV | Value at mid |
|---|---|---|---:|---:|---|---:|---:|
| bank | Fidelity | KRE 2026-11-20 66P | 3 | 72.62 | 0.4 / 0.45 | 32% | +$128 |
| bank | Fidelity | KRE 2026-11-27 70P | 2 | 72.62 | no vendor quote | 30% ASSUMED | +$288 |
| bank | Fidelity | KRE 2026-11-27 67P | 4 | 72.62 | 0.51 / 0.77 | 31% | +$256 |
| bank | Fidelity | KRE 2026-12-18 60P | 5 | 72.62 | 0.27 / 0.37 | 36% | +$160 |
| bank | Fidelity | KRE 2026-12-31 65P | 2 | 72.62 | 0.81 / 0.97 | 30% | +$178 |
| bank | Fidelity | APO 2026-12-18 95P | 1 | 112.33 | 1.25 / 1.65 | 45% | +$145 |
| bank | Fidelity | OZK 2026-11-20 40P | 4 | 50.79 | 0.05 / 0.45 | 59% | +$100 |
| bank | Fidelity | WAL 2026-12-18 70P | 2 | 76.58 | 1.55 / 1.7 | 36% | +$325 |
| bank | Fidelity | WAL 2026-12-18 65P | 4 | 76.58 | 0.7 / 0.85 | 40% | +$310 |
| bank | Fidelity | ZION 2026-11-20 62.5P | 2 | 66.42 | 0.6 / 1.2 | 38% | +$180 |
| bank | Robinhood (unverified) | WAL 2026-12-18 70P | 1 | 76.58 | 1.55 / 1.7 | 36% | +$162 |
| bank | Robinhood (unverified) | KRE 2027-01-15 25P | 1 | 72.62 | 0.0 / 0.13 | 95% | +$6 |
| nasdaq | Fidelity | QQQ 2026-10-26 710P | 1 | 705.34 | 7.71 / 7.74 | 17% | +$772 |
| nasdaq | Fidelity | QQQ 2026-10-26 705P | 2 | 705.34 | 5.22 / 5.24 | 18% | +$1,046 |
| nasdaq | Fidelity | QQQ 2026-11-20 690P | 2 | 705.34 | 13.32 / 13.38 | 26% | +$2,670 |
| nasdaq | Fidelity | QQQ 2026-11-20 670P | -2 | 705.34 | 8.68 / 8.7 | 28% | −$1,738 |

**Value at mid now: bank/credit +$2,239 · Nasdaq +$2,751 · total +$4,989.**

## Betas used (1 year of daily returns; two-factor on KRE and QQQ)

| Name | to KRE | to QQQ | R² |
|---|---:|---:|---:|
| APO | 0.65 | 0.42 | 0.22 |
| OZK | 0.96 | -0.04 | 0.67 |
| WAL | 1.31 | 0.21 | 0.73 |
| ZION | 1.09 | 0.03 | 0.81 |

## By Monday 10/26 close (whole book; the Oct-26 QQQ puts expire that day)

| Scenario | KRE | QQQ | Vol (bank / QQQ) | Bank/credit puts | Nasdaq downside | **Book** |
|---|---:|---:|---|---:|---:|---:|
| Flat | +0% | +0% | ×1.00 / ×1.00 | −$205 | −$1,150 | **−$1,355** |
| See-saw continues | +2% | -2% | ×1.00 / ×1.05 | −$740 | +$3,398 | **+$2,658** |
| Snap-back | -2% | +2% | ×1.00 / ×0.95 | +$499 | −$1,943 | **−$1,444** |
| Both fall | -3% | -3% | ×1.15 / ×1.15 | +$2,210 | +$5,703 | **+$7,913** |
| Both rally | +2% | +2% | ×0.90 / ×0.90 | −$1,249 | −$1,973 | **−$3,223** |

## By Friday 11/13 close (put-wall time stop; Oct-26 lines excluded — decided Monday)

| Scenario | KRE | QQQ | Vol (bank / QQQ) | Bank/credit puts | Nasdaq downside | **Book** |
|---|---:|---:|---|---:|---:|---:|
| Flat | +0% | +0% | ×1.00 / ×1.00 | −$1,363 | −$330 | **−$1,693** |
| See-saw continues | +5% | -5% | ×1.00 / ×1.10 | −$1,929 | +$1,463 | **−$466** |
| Snap-back | -5% | +5% | ×1.05 / ×0.85 | +$453 | −$868 | **−$415** |
| Both fall (Aug-2024 shape) | -10% | -8% | ×1.35 / ×1.35 | +$6,853 | +$2,224 | **+$9,077** |
| Both fall hard | -15% | -12% | ×1.60 / ×1.60 | +$14,887 | +$2,755 | **+$17,642** |
| Both rally | +5% | +5% | ×0.85 / ×0.80 | −$2,160 | −$872 | **−$3,032** |

## Grid at 11/13, vol unchanged (book excluding Oct-26 lines): change in value

| KRE \ QQQ | -12% | -8% | -4% | +0% | +4% | +8% |
|---|---:|---:|---:|---:|---:|---:|
| -15% | +$14,886 | +$13,997 | +$12,164 | +$10,402 | +$9,609 | +$9,263 |
| -10% | +$8,212 | +$7,404 | +$5,653 | +$3,973 | +$3,260 | +$2,993 |
| -5% | +$4,003 | +$3,299 | +$1,646 | +$60 | −$563 | −$746 |
| +0% | +$2,002 | +$1,388 | −$183 | −$1,693 | −$2,248 | −$2,369 |
| +5% | +$1,233 | +$677 | −$843 | −$2,309 | −$2,825 | −$2,912 |
