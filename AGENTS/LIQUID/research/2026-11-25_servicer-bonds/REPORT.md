# Nonbank mortgage servicer bonds, 11/24 against 10/21 (D:L1290 Part A)

**LIQUID, 2026-11-25, started 16:12 ET. Claude Code / Opus 5.5. Research only: no gate, score, count or card moved.**

## Answer

1. **Freedom's new note:** 10.00% due January 15, 2032 is in HYG at a 99.69 mark [11/24, vendor price, not a trade], accrual date December 4, 2026, so it had not settled. The file shows yield 10.00%; 99.69 gives 10.07% by my arithmetic (the two do not agree; the 10.00 fits a par reoffer). **The reoffer price and price talk were NOT FOUND** in any source I could read. "Priced at or near par" is INFERRED.
2. **Wide for BB-, ordinary for Freedom.** 10.00% is 302 bp over the ICE BB effective yield (6.98%) and 122 bp over single-B (8.78%) [FRED, 11/24], and above 84% of the 1,325 HYG bonds. But it is 4 to 16 bp over Freedom's own 8.00% February 2032 (9.84%) and 8.375% April 2032 (9.96%). BB- is one agency: KBRA has BB+ (HOMER), and a search summary of a deal page gave B2/B/BB- for the July note (not verified), so single-B is the closer yardstick.
3. **It is Freedom, not the servicers.** Freedom widened 83 to 115 bp in the month, the 75th to 86th percentile of HYG bonds that started at similar spread and duration. PennyMac +20 to +58, about the median of its control. Rocket +3 to +35, less than its control. UWM, CrossCountry and Rithm are between flat and +48.

## Spread to Treasuries, October 21 to November 24 (bp)

| Issuer | Bonds | Median yield 11/24 | Median spread 11/24 | Median change | Control median change (p25 to p75, n) |
|---|---:|---:|---:|---:|---|
| Freedom | 6 | 9.85% | 517 | **+95** | +26 (−6 to +88, 112) |
| PennyMac | 7 | 9.27% | 459 | +39 | +32 (−8 to +98, 108) |
| UWM | 2 | 10.91% | 624 | +26 | +151 (+29 to +382, 30; a distressed tail, weak control) |
| Rithm | 3 | 8.87% | 420 | +12 | not run |
| Rocket (incl. Rocket Mortgage) | 9 | 6.40% | 173 | +13 | +27 (+17 to +42, 329) |
| CrossCountry | 3 | 8.63% | 395 | 0 | not run |
| All HYG bonds in both files | 1,224 | 7.05% | — | +27 | p90 +104 |
| ICE HY / B / BB OAS (FRED, the same two dates) | — | — | 372 / 405 / 225 | +45 / +73 / +27 | — |

Named bonds (price 10/21 to 11/24, spread change): Freedom 9.25% February 2029 101.56 to 100.37, +115; 6.875% May 2031 92.65 to 90.25, +97; 9.125% May 2031 99.87 to 97.38, +93; 8.00% February 2032 94.83 to 92.62, +83; 8.375% April 2032 96.41 to 93.54, +98; 7.875% April 2033 93.09 to 90.39, +89. PennyMac 4.25% February 2029 +20; 7.875% December 2029 +39; 7.125% November 2030 +32; 5.75% September 2031 +39; 6.875% May 2032 +54; 6.875% February 2033 +58; 6.75% February 2034 +33. UWM 6.625% February 2030 88.65 to 89.35, +3; 6.25% March 2031 83.97 to 83.49, +48. Rocket 6.125% August 2030 +18; 6.125% August 2031 +3; 6.375% August 2033 +11; 6.50% August 2029 +35; 6.50% June 2034 +9; 7.125% February 2032 +24; Rocket Mortgage 3.625% March 2029 +13, 3.875% March 2031 +16, 4.00% October 2033 +13. All rows: `servicer_read_output.txt`.

**Why 10% and not 8%:** Freedom sold an 8.00% February 2032 note in July (July 21 per a search summary of a deal page, par; accrual July 24 in HYG). Treasury at the same duration is up about 34 bp since then (4.34 to 4.68, par curve) and single-B OAS about 119 bp (286 to 405). That covers roughly 150 of the 200 bp; about 50 bp is left for Freedom itself. Rough, because coupon and index OAS are not the same object.

## Limits

- **Evaluated prices, not TRACE.** TRACE is not reachable from this box. HYG's own note says the vendor price may predate the date shown. These marks cannot show the 11/25 sell-off.
- **Two dates only.** The server ignores a past-date request, so I cannot say whether Freedom moved before or after Fitch's November 16 action. Cause not established.
- Spread = yield to worst less the Treasury par curve at the file's modified duration; not OAS. Control = bonds in both files, duration 2 to 5, yield under 25%, so it drops names that defaulted, were called or left the fund.
- Planet, loanDepot and Provident have no HYG line: UNMEASURED.
- Freedom 6.625% January 2027: $540M (Fitch via HOMER), not $1.19B; not in HYG, unread. The refinancing link to the $500M is INFERRED.
- cbonds refused (403); fitchratings.com is closed to this search client; neither worked around. CreditFlow's issuer page had no line from August on.

## Read and forward view

One new data point outside AI financing, and it points to **one issuer paying up, not a closed or spreading market**: the note was sold, and the peers did not follow. For HENRY's question it does NOT support broadening through servicers. Expect Freedom to keep trading near 10% until the rate-hedge cash drain eases. Meaningful alternative: Freedom is the first of the group and PennyMac (Fitch Negative) follows. Horizon: to the December 4 settlement and year-end. I would change my mind on PennyMac widening past its control's p75 (about +98 on this window), a note that fails to settle or breaks more than 2 points, or a warehouse or MSR line cut in a filing.

**Investment implication (WQ-696):** none I can see. Freedom is private with no listed equity; PennyMac, Rocket and UWM bonds do not show the stress a listed-equity short would need. Invalidated by the same three events. Unknown: reoffer price, talk, book size, TRACE volumes, anything on 11/25.
