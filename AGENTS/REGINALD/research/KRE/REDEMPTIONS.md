# KRE creations and redemptions — mechanics, evidence and interpretation

**Prepared:** 2026-11-03  
**Official evidence through:** 2026-11-02  
**Full calculations:** [rolling and 2026 monthly report](reports/2026-11-03_redemption-history/REPORT.md) · [2025 monthly and annual comparison](reports/2026-11-03_redemption-history/2025_MONTHLY.md)

## Bottom line

KRE's ETF wrapper has contracted substantially since the end of 2024, but regional-bank prices have risen. That combination does not support a simple story of investors abandoning regional banks. The defensible reading is a smaller KRE wrapper with volatile two-way flows, not an acute redemption crisis or a bank-credit signal.

## What a redemption means

A normal investor selling KRE on an exchange transfers those shares to another market participant; the number of ETF shares does not change. A redemption is a separate primary-market transaction: an authorized participant (a large broker-dealer or market-making firm with an agreement with the ETF issuer) returns KRE shares to the fund and receives underlying bank stocks or equivalent assets. The returned ETF shares cease to exist.

The underlying banks' shares do not cease to exist, and the banks do not lose deposits or capital. The AP can hold, sell or hedge the underlying stocks; the data does not identify the AP, its clients or their motive. A falling share count is therefore not a pure measure of directional investor conviction.

For remaining KRE holders, redemption does not mechanically dilute value. The fund has fewer shares and fewer assets, while NAV per share still represents the underlying basket. It is not a corporate share buyback.

## Core numbers

| Period | Shares outstanding | NAV | Total net assets |
|---|---:|---:|---:|
| Full-year 2025 | −29.45% | +7.41% | −24.22% |
| 2026 through 11/02 | −10.39% | +13.66% | +1.84% |
| Three months through 11/02 | −7.45% | −3.17% | −10.38% |
| Two months through 11/02 | −0.56% | −0.67% | −1.22% |
| One month through 11/02 | +5.01% | +4.13% | +9.34% |

From 2024-12-31 through 2026-11-02, shares outstanding fell from 84.55M to 53.45M (approximately −37%), while NAV rose from $60.36 to $73.69 (approximately +22%). Total fund assets fell from approximately $5.10B to $3.94B (approximately −23%).

### 2026 rolling detail

| Window through 2026-11-02 | Net share change | Creation days | Redemption days | Gross created | Gross redeemed |
|---|---:|---:|---:|---:|---:|
| Three months | −4.30M (−7.45%) | 30 | 35 | 54.00M | 58.30M |
| Two months | −0.30M (−0.56%) | 18 | 24 | 40.80M | 41.10M |
| One month | +2.55M (+5.01%) | 9 | 12 | 22.70M | 20.15M |

The latest completed official decline, 2026-11-02, was **2.15M shares (−3.87%)**, approximately **$158M** at that day's NAV. It ranked ninth-largest among 65 three-month daily changes and sixth-largest among 42 two-month changes. It was meaningful but not unprecedented.

## Monthly patterns

- **2025:** five share-positive months and seven negative. February (−15.24%) and October (−15.25%) were the largest monthly contractions; August (+10.15%) and December (+8.75%) were strong creation months.
- **2026 through 11/02:** four positive months and seven negative. June (+16.02%) was the largest expansion and July (−8.84%) the largest contraction. October increased 3.54% before November opened with one negative observation.
- **Aligned declines are more informative than divergence:** February–April and October 2025 had falling shares and NAV, a stronger risk-off pattern. In both full-year 2025 and year-to-date 2026, however, shares fell while NAV rose. Redemption alone did not forecast price direction.

Exact monthly tables are preserved in [2025_MONTHLY.md](reports/2026-11-03_redemption-history/2025_MONTHLY.md) and [REPORT.md](reports/2026-11-03_redemption-history/REPORT.md#calendar-month-detail--2026).

## Interpretation

1. **KRE-specific exposure has contracted.** This may reflect migration to direct stocks, other funds, hedging structures or AP inventory management. The data cannot distinguish them.
2. **There is no steady one-way exit.** Large creations repeatedly offset redemptions, and the recent one-month count is positive.
3. **Share contraction is not a price forecast.** NAV rose in both annual comparisons. A more consequential bearish pattern would require sustained share contraction together with price underperformance, falling assets, comparable-fund outflows and bank-credit deterioration.
4. **No bank-credit inference follows.** These flows measure the ETF wrapper, not banks' loan losses, deposits or capital.
5. **Use rolling net changes, not one daily alert.** The 2026-11-03 boot monitor's vendor-derived 2.2% decline used Yahoo `totalAssets / NAV`; State Street's official completed series ends 11/02 and differs in level and daily change. That vendor observation is unconfirmed, not an official 11/03 redemption.

This research changes no bank score, prediction, probability, position or trade instruction.

## Preserved package

- [Rolling and 2026 monthly report](reports/2026-11-03_redemption-history/REPORT.md)
- [2025 monthly report and annual comparison](reports/2026-11-03_redemption-history/2025_MONTHLY.md)
- [Official State Street source workbook](reports/2026-11-03_redemption-history/data/kre_navhist.xlsx), retrieved 2026-11-03, SHA-256 `d9113ec7823fff4dd35625e0e2ad22031a2c6d22ae9cfd11f58e23e4baf2fefe`
- [2025 exact monthly CSV](reports/2026-11-03_redemption-history/data/kre_monthly_2025.csv)
- [2026 exact monthly CSV](reports/2026-11-03_redemption-history/data/kre_monthly_2026_through_2026-11-02.csv)
- [Three-month daily CSV](reports/2026-11-03_redemption-history/data/kre_shares_2026-07-31_to_2026-11-02.csv)
- [Two-month daily CSV](reports/2026-11-03_redemption-history/data/kre_shares_2026-09-02_to_2026-11-02.csv)

Primary source: State Street Global Advisors, `https://www.ssga.com/library-content/products/fund-data/etfs/us/navhist-us-en-kre.xlsx`. Gross figures are sums of daily share changes, not issuer-reported dollar flows.
