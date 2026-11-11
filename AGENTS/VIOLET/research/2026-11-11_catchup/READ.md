# VIOLET catch-up read, Wednesday November 11, 2026 (Veterans Day)

Launched by PROME prome-2b on Will's 09:24 ET word ("Lets make sure we get all our agents caught up to the live data and news"). Boot 09:25 ET from `date`. Research only: no trade, card, gate, band, threshold or charter change; $0.

## 1. The 11/10 bar carried to this boot: CONFIRMED on Cboe History

| Series | 11/10 History close | 16:15:01 ET print (TICK row) | Agrees |
|---|---:|---:|---|
| VIX | 19.46 (open 19.76, high 21.61, low 19.29) | 19.46 (quote high 21.43) | yes; the quote high understated the History high by 0.18 |
| VIX9D / VIX3M / VIX6M | 18.54 / 20.64 / 21.99 | same | yes |
| VVIX | 96.63 | 96.63 | yes |
| SKEW | **151.12** | not printed at the 16:31 read | blank filled |

`backfill.py --spot-only --spot-days 15`, 09:26 ET: 2,771 agreed, 1 blank filled, 0 corrected, the 11/10 row stamped SETTLE. VIX3M/VIX 1.0606, VIX9D/VIX 0.9527. **LOW_VOL on 11/10 confirmed (0.54 under 20.00).** FRED VIXCLS had not yet posted 11/10 at 09:27 ET (frontier 11/09 = 19.92).

## 2. Live surface, 09:32 ET (Cboe values via yfinance 1-minute bars, 15-minute delayed; TICK, not a close)

| Metric | 09:32 ET | 11/10 History | Change |
|---|---:|---:|---:|
| VIX | **18.19** (overnight high 18.96) | 19.46 | −6.53% |
| VIX9D | 16.93 | 18.54 | |
| VIX3M | 19.89 | 20.64 | |
| VIX6M | 21.46 | 21.99 | |
| VVIX | 96.03 | 96.63 | |
| VIX3M/VIX | **1.0935** | 1.0606 | steeper contango |
| VIX9D/VIX | **0.9307** | 0.9527 | the front is the cheapest point |
| COR1M | 11.10 (Cboe quote 09:31 ET) | 12.35 | −10.1% |
| Adjusted VX M1:M2 | −1.98% (VX/X6 19.9067 vs VX/Z6 19.5125, **11/10 settle**) | | front future above second |

Vendor tape 09:47 ET (fetch basis, not closes): SPY 755.33 (+0.72%), QQQ 684.22 (+1.40%, off a 689.02 high), RSP 221.32 (+0.20%). Leadership is again the Nasdaq-100 over the equal-weight index; HENRY owns the read (pre-open map 18608dfb0c: S&P dealer gamma negative and shallow under a 7,622 to 7,625 flip, NDX positive).

**Regime: LOW_VOL, 1.81 under 20.00 on the tick.** Not a close; the label for 11/11 is set on History.

**The futures front, an inference to test, not a finding:** VX/X6 settles at the 11/18 AM SOQ, and that VIX prices 11/18 to about 12/18, which contains the 12/9 FOMC (HENRY's HEN-63, hike at 0.70). VX/Z6 settles 12/16, after the meeting. Under KB-VIO-367's event-window rule, X6 over Z6 is consistent with the December hike meeting and the NVIDIA 11/17 reaction both sitting in X6's window. Spot VIX9D under VIX says the next nine days are priced calm. Neither is flow evidence.

## 3. Veterans Day session rule (D:L342)

| Series | Is 11/11 a session? | Consequence |
|---|---|---|
| VIX complex, VIXCLS, SKEW, VX futures | **Yes**: NYSE and Cboe open | Counts in every VIX-based count; RED-29 says so on its letter. VX_DAILY gets a real 11/11 row; the orphan guard (KB-VIO-395) does not fire because companions publish (they did, 09:31 ET). |
| FRED HY/CCC/BB OAS (ICE) | **No**: SIFMA full close | Non-session under RED's registry NON-SESSION CLAUSE; LIQUID's 398a946b9a fix reads it. For VIOLET's 5-session "VIX +30%, credit flat" row, the credit leg's five sessions skip 11/11. The row is far from met (VIX falling). |
| MOVE (Treasury options) | **Treat as no**: cash Treasuries closed | `move.py` has no holiday rule. If investing.com prints an 11/11 bar, it is not a rates-vol observation; check at the next boot before quoting it. |

## 4. RED-29: the legs (RED grades after 10:30 ET 11/12; VIOLET states, does not grade)

Letter (AGENTS/RED/workbook/PREDICTIONS.tsv row RED-29): FRED VIXCLS ≥ 18.00 on each of 11/06, 11/09, 11/10, 11/11.

| Session | FRED VIXCLS | Cboe History | vs 18.00 |
|---|---:|---:|---|
| 11/06 | 25.64 | 25.64 | above, +7.64 |
| 11/09 | 19.92 | 19.92 | above, +1.92 |
| 11/10 | not posted at 09:27 ET | **19.46** | above, +1.46 |
| 11/11 | open session | 09:32 ET tick **18.19** | **+0.19 on a tick; the close decides** |

RED-FT-06's exit count (≥ 18 ×5) runs on the same closes; RED owns it.

## 5. WALTER cards: claims checked at the publisher (KB-VIO-397)

- VVIX one-month realized volatility: 204.3% annualized [11/10], highest since 2006; above Feb 2018 (180.3), Mar 2020 (115.3), Aug 2024 (191.1). CONFIRMED with the 2006 early-series caveat.
- "Two straight days above 27, then two closes under 20, third time": true on intraday highs only (2018-02-14, 2021-05-14, 2026-11-09); false on closes.
- "Two closes over 25, then three straight under 20, never since 1990": CONFIRMED; the 11/11 close decides whether it now happens once.

## 6. Instruments

- Yen carry: RV10 6.99%, p35.2, CALM (09:47 ET). The FXY IV leg is not usable this morning: 2.4% pre-open, 20.2% at 09:47 ET, against 11.2% to 11.8% on prior reads. The pre-open read printed a false "RV through IV"; `jpy_vol.py` now treats 09:00 to 09:29 as off-hours (MAINTENANCE 11/11).
- MOVE 92.43 [11/10], +6.45; OVX 53.10, OVX/VIX 2.73 CALM [11/10]; CFTC 11/03 lev-money −31,479 p38.5.
- Credit, owner LIQUID: HY OAS first-published **334bp [11/09]**, from 342 [11/06] and the 348 run peak [11/05]; CCC 13.11% [11/09]. Credit is now following vol down, 14bp off the peak.
- VIX options (09:26 ET boot pull, OI from the prior day): Nov 18 C/P OI 1.82, 30C OI 323,732; Dec 16 C/P OI 2.07.
