# CRUISE catch-up, 2026-11-11 (Veterans Day: bond market closed, stocks open)

Wake: PROME prome-2b on Will's 09:24 ET word, "Lets make sure we get all our agents caught up to the live data and news." Last CRUISE session 2026-11-06. Figures below come from `calc.py` → `calculations.json` in this folder unless a filing is named.

## What changed since 11/6, in plain words

1. **Carnival's stock has recovered past the −10% line.** It closed $30.81 on 11/9 and $30.74 on 11/10, 9.36% and 9.56% below the fixed $33.99 February reference. The −10% line is $30.591. On the band's evident meaning that is GREEN, but the GREEN cell is one of the two cells PROME's 10/28 answer called ambiguous (SF13), and no worked GREEN trigger was ever recorded (searched VX.tsv, CADENCE.md, STATUS.md and the WQ-435 ruling for 30.59: none). PROME's 10/28 instruction: a clarification that moves a grade is not mine to make. **`VX-CRU-01` stays YELLOW(2) on the letter; the GREEN reading is an ask to PROME.** If read GREEN, the desk total goes 9/20 → 8/20. The move was mostly the market: 11/9 CCL +4.16% with SPY +2.37% and XLY +2.92%.
2. **A hiking Fed barely touches cruise credit through interest costs.** Floating-rate debt is 12% of Norwegian's, 6% of Royal Caribbean's and 15% of Carnival's (two-thirds of that euro-based). Norwegian's own 10-Q puts a 1-point SOFR rise at **$18.2M a year**; one 25bp December hike is about **$4.6M**, 0.17% of trailing Adj EBITDA, and less after October's $376.3M revolver paydown moved debt from floating to fixed. Leverage in `VX-CRU-05` is net debt over EBITDA, so interest cost does not enter it at all.
3. **This week's rate rise has not yet made Norwegian's refinancing dearer than when it last borrowed.** On 10/15, when it priced the $950M 8.750% 2031 notes, the 5-year Treasury was 4.899% and the 10-year 5.089%. At the 11/10 close they were 4.807% and 4.983%, still about 10bp lower, even after 11/10's jump (+15bp 5-year, +12bp 10-year). The high-yield spread leg was not measured here.
4. **The refinancing calendar is where rates would matter, and it is back-loaded.** Norwegian owes $238.6M for the rest of 2026, $1,105.7M in 2027, $1,346.1M in 2028, $1,370.0M in 2029 and **$4,134.3M in 2030**. Each 1 point higher on the rate at which the 2027 maturities are refinanced costs about $11M a year. Replacing the $216.2M 2027 exchangeable notes (1.64% and 3.06% effective) at an 8.75% coupon would cost about $12–15M a year on its own, a coupon reset that happens whatever the Fed does.
5. **No new filing moves anything.** EDGAR, read 11/11 10:2x ET for filing dates 11/6 to 11/11: no 8-K from any of the three. Insider filings only (row 6). Issuer IR press pages were not checked, so the no-news claim is CONDITIONAL on them.
6. **CRU-11 is near zero.** NCLH minus RCL, cumulative adjusted total return from 10/2: **−0.10pp at the 11/10 close** (NCLH +22.26%, RCL +22.36%). CONFIRMED needs ≤ −5pp at the 11/13 close (11/14 is a Saturday).

## Row detail

| Row | Item | Reading | Basis / source | Limit |
|---|---|---|---|---|
| 1 | Closes 11/10 | CCL $30.74 (−0.23%), RCL $339.85 (+0.85%), NCLH $18.51 (+0.43%); SPY $749.92 (−0.37%), XLY $121.05 (+0.03%) | yfinance auto_adjust=False raw Close, retrieved 11/11 10:13 ET; FORGE fetch.py same vendor | 11/11 bars are intraday, not used |
| 2 | Closes 11/9 | CCL $30.81 (+4.16%), RCL $336.98 (+3.00%), NCLH $18.43 (+2.85%); SPY +2.37%, XLY +2.92% | same | Trade press tied 11/9 to falling oil (Schaeffer's 11/9, headline only); oil is BRENT's |
| 3 | `VX-CRU-01` | −9.36% (11/9), −9.56% (11/10) vs raw $33.99; −10% line $30.591, −20% line $27.192, RED $22.0935 | fixed raw reference, WQ-435 D1 | GREEN cell ambiguous (SF13); held YELLOW(2), asked |
| 4 | CRU-11 interim | +0.57pp (11/6), +0.40pp (11/9), **−0.10pp (11/10)** | pinned adjusted series, base 10/2 adj NCLH $15.14, RCL $277.74 | interim, not a grade |
| 5 | Treasuries | 3-month 4.000 → 4.115 (11/6 → 11/10); 5Y 4.648 → 4.807; 10Y 4.859 → 4.983; 30Y 5.260 → 5.350; 10/15: 5Y 4.899, 10Y 5.089 | CBOE yield indices via yfinance (^IRX ^FVX ^TNX ^TYX) | Bond market closed 11/11; PROME's 11/10 Treasury-close figures (10Y 4.98, 30Y 5.35) agree; 2Y not pulled |
| 6 | Insider filings | RCL: A. Wilhelmsen AS Form 144 for 500,000 shares (~$170.5M at filing, 11/9) after Form 4 sales 11/4 and 11/6 at ~$319–327, indirect holding ~16.07M after 11/6. CCL: CFO and CAO David Bernstein sold 26,681 at $31.2606 on 11/4 | EDGAR acc 0000103623-26-000048, 0001317345-26-000020, -000018, 0000815097-26-000111 | Founding-holder sale ≈3% of its stake; no read on the business |
| 7 | NCLH rate exposure | 88% fixed / 12% variable at 9/30 (90/10 at 12/31/25); +1pp SOFR = +$18.2M/yr ex capitalized interest; implied variable ≈ $1.82B; Q3 interest expense, net $170.5M | 10-Q acc 0001104659-26-120217, Item 3 and income statement | Post-10/15 variable ≈ $1.44B is INFERRED (assumes the repaid revolver was SOFR-based and no other draws) |
| 8 | NCLH maturities | rest-2026 $238.6M · 2027 $1,105.7M · 2028 $1,346.1M · 2029 $1,370.0M · 2030 $4,134.3M · 2031 $1,875.1M · later $5,428.2M · total $15,498.0M | same 10-Q, Note 7 | at 9/30, before the 10/15 notes and paydown |
| 9 | RCL rate exposure | variable $1,412M of $22,872M (6.17%): USD term loan $1,216M at 5.44%, euro $196M; +1pp on the USD piece ≈ $12.2M (INFERRED, before any swaps); maturities rest-2026 $579M · 2027 $2,371M · 2028 $3,211M | 10-Q acc 0000884887-26-000044, Note 6 | RCL's sensitivity figure is in its 10-K, not read |
| 10 | CCL rate exposure | fixed 52%, EUR fixed 33%, floating 5%, EUR floating 10% of $24,559M at 8/31; USD floating ≈ $1.23B, +1pp ≈ $12M (INFERRED); maturities rest-2026 $301M · 2027 $2,517M · 2028 $3,961M; revolver $4.5B available | 10-Q acc 0000815097-26-000107, Item 3 and debt note | 8/31 vintage; euro floating moves with the ECB, not the Fed |
| 11 | News | RCL Legend of the Seas naming 11/11, Fort Lauderdale (capacity); Carnival moved departure times on 70 Pride and Adventure sailings (operations). No NCLH operating news found | WebSearch 11/11, trade press headlines | headlines only, C3 |

## Grade on the desk's own letters

| Vector / row | Before | After | Why |
|---|---|---|---|
| `VX-CRU-01` | YELLOW(2) | **YELLOW(2) held; GREEN reading asked** | Close above $30.591 on two sessions; GREEN cell literal "<-10%" is ambiguous and no worked GREEN trigger exists |
| `VX-CRU-05` | ORANGE(3) | ORANGE(3) | Cannot move between prints; rates do not enter either leg |
| `VX-CRU-03` | YELLOW(2) | YELLOW(2) | No booking-pace datum, no guide-down |
| `VX-CRU-04` | YELLOW(2) | YELLOW(2) | No new Big-3 cancellation found (headline search only) |
| `VX-CRU-02` | observation | observation | Oil fell 11/9 per trade press; BRENT owns the price |
| Convergence | 9/20 | 9/20 (8/20 if GREEN is ruled) | |

## What a hiking Fed does to the cruise-credit read

Through coupons: very little. One 25bp hike is about $4.6M a year for Norwegian (about $3.6M after October), about $3M each for Royal Caribbean's and Carnival's dollar floating debt. None of the three has a floating share large enough for the Fed path to change leverage, liquidity or the 11/17 test. The 11/17 Free Liquidity test counts cash and drawable revolver, not interest.

Through refinancing: modest and slow. Norwegian's next big wall is 2030 ($4.13B). Its 2027–2029 maturities ($3.8B together) would reprice at whatever high-yield rate prevails; the biggest single cost step is the coupon reset on cheap exchangeables, not the Fed. Treasury yields are still a little below where Norwegian last borrowed.

Through demand: the channel that could matter, and not this desk's to measure. A Fed hiking into 5% long yields pressures mass-market household budgets, which is CARL's read; this desk sees it only through bookings and ticket price per day at the Q4 prints. Nothing in this week's data measures it.

Bottom line: the rate move changes no letter on this desk. Norwegian's credit read still turns on earnings per capacity day and deposits, and the Q4 print, not the Fed, is the next test.
