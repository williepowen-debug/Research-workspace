# 11/10 close read: rates set, Treasury par (HEN-62), equity and vol close (PROME tap 16:21 ET)

**Pulled 16:21–16:23 ET 2026-11-10** (desktop, Claude Code, Opus 5.5). Vendor = yfinance via `.venv` (1-minute last trades for futures; dated daily bars for cash indexes and stocks). FRED SP500 and VIXCLS for 11/10 not posted; Cboe History not read; CME settlement not read (cmegroup.com blocked).

## Rates set against the 15:00 ET read

| Instrument | Close read | Source, observation time | 15:00 ET read | Change |
|---|---:|---|---:|---|
| **ZQZ26 (December fed funds)** | **95.920 = +28.2bp, 113%** | vendor last trade 16:01 ET | 95.925 = +27.5bp, 110% | one tick firmer (+0.7bp). In the 14:55–15:05 ET window around CME's 14:00 CT settlement it traded only 95.925 (117 lots); settlement price itself unread |
| ZQF27 (January) | 95.825 = 4.175% | vendor last 16:06 ET | 95.830 | one tick firmer |
| ZQH27 (March 2027) | 95.620 = 4.380% | vendor last 15:52 ET | 95.620 | unchanged; about 22bp over the December post-meeting rate |
| ZT (2Y note future, Dec) | 102.008 | vendor last 16:09 ET | 102.023 (14:50) | slightly lower |
| ZN (10Y note future, Dec) | 106.203 | vendor last 16:10 ET | — | — |
| ^TNX (Cboe 10Y index) | 4.983% | vendor, last 14:59 ET (index stops at 15:00) | 4.99% | flat |
| DXY | 102.262 (+0.60%, 11/9 101.65) | vendor 16:11 ET | — | dollar up on the day |
| USD/JPY | 158.72 | vendor 16:21 ET (daily bar mis-dated, not used) | 158.74 (11:09) | flat; SAM's ≥2% velocity rule NOT FIRED |
| Brent January | 91.85 | vendor futures bar 16:09 ET, **not a settle; BRENT owns** | ~90.6 (11:09) | — |

**December pricing at the close: +28.2bp on the last trade, +27.5bp at the settlement window, against +27.5bp at 15:00 ET.** Nothing changed after 15:00 beyond one tick. The day's whole move is 82% (11/9 15:00) → 110–113%, and it held through the close.

## Treasury par yield curve, 11/10 (HEN-62)

Source: `home.treasury.gov` daily par yield curve CSV (2026, all), read 16:21 ET, **first published for 11/10**. Treasury's curve uses indicative bid-side quotes taken near 15:30 ET, not the 16:00 close.

| Tenor | 11/6 | 11/9 | **11/10** | Change on 11/9 |
|---|---:|---:|---:|---:|
| 3 Mo | 4.19 | 4.24 | 4.30 | +6bp |
| 6 Mo | 4.23 | 4.26 | 4.38 | +12bp |
| 1 Yr | 4.33 | 4.38 | 4.56 | +18bp |
| **2 Yr** | 4.51 | 4.56 | **4.73** | **+17bp** |
| 5 Yr | 4.64 | 4.67 | 4.81 | +14bp |
| 10 Yr | 4.86 | 4.88 | 4.98 | +10bp |
| 30 Yr | 5.26 | 5.26 | 5.35 | +9bp |

2s10s 25bp (32bp on 11/9): **bear flattening, led by 1Y and 2Y**. That matches a hike being pulled into December and a second move by March.

**HEN-62 RESOLVED YES.** The letter: Treasury Daily Par Yield Curve, 2 Yr column, first published, two decimals, above 4.60 on any published date 11/9–11/30; YES on the first such print. 11/9 printed 4.56 (not above). **11/10 printed 4.73.** Forecast 0.60 → **HIT** (Brier 0.16). It resolved on the second date of a 16-session window, on the CPI and Waller day.

Threshold states on par 11/10: **2Y 4.73 RED** (>4.60; was ORANGE at 4.56). 10Y 4.98 ORANGE, 2bp under red (>5.0). 30Y 5.35 ORANGE (>5.25; red >5.50). Thresholds unchanged.

## Equity and vol close (vendor dated daily bars, read 16:22 ET)

| | 11/9 | 11/10 close | Day |
|---|---:|---:|---:|
| SPX | 7,549.94 | **7,520.93** | −0.38% (intraday low 7,482.52, −0.89%) |
| NDX | 27,907.63 | 27,740.80 | −0.60% |
| QQQ | 679.35 | 674.76 | −0.68% |
| RSP (equal weight) | 220.95 | 220.88 | **−0.03%** |
| IWM | 282.51 | 280.56 | −0.69% |
| KRE | 73.45 | 73.09 | −0.49% |
| NVDA | 178.67 | 168.89 | **−5.47%** |
| SMH | 487.41 | 483.63 | −0.78% |
| APO | 122.20 | 122.74 | +0.44% |
| VIX | 19.92 | **19.46** | −2.31% (bar read after the 16:15 index close; Cboe/FRED not read) |
| VIX9D / VIX3M / VVIX | 19.88 / 20.85 / 98.43 | 18.54 / 20.65 / 96.30 | contango, VIX3M/VIX 1.061 |

**Read:** rates repriced and held; stocks absorbed it. SPX took back more than half its intraday fall to close −0.38%. Equal weight finished flat, VIX fell, and the term structure steepened in contango. Cap weight lagged equal weight by about 0.35pp on a day Nvidia fell 5.47% on its own story (point attribution not run). KRE fell 0.49% with yields up and moved with IWM: a rate day, not a credit read (HY 11/10 publishes on FRED 11/11).

**Against the map (11/10 ~11:1x ET, not re-run on the close; the chain carries 11/9 trading until tomorrow):** SPX closed 7,520.93, above the 7,500 gamma concentration and about 1.5% under the flip ~7,635, still in negative gamma. The negative-gamma amplification did not show up in size today. Walls remain WITHHELD.

**Levels (own calc, 11/10 bar):** 200-day 7,331.08 (SPX +2.59% above it; **HEN-60 not triggered**); 50-day 7,672.91 (still under it: short-term CTA condition still met); −3.81% from the 7,818.93 peak (HEN-61 not triggered); red 7,037.04.

Cascade conditions on the close: vol-control (VIX >23–24) NOT met at 19.46; short-term CTA (under the 50-day) met. Standing Will rule joint count 0 (VIX 19.46 > 15; HY 334 [FRED 11/9] > 260).

Sources: Treasury par CSV; yfinance (futures 1-minute last, cash and stocks daily bars); own SMA calc from vendor closes.
