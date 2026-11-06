# 11/6 close read — HENRY, pulled 17:09–17:13 ET 11/6

Basis: vendor dated daily bars (`^GSPC` and peers), Treasury Daily Par Yield Curve 11/6 (posted by 17:12 ET), Cboe chain via `gamma_flip.py --both`. FRED SP500, VIXCLS, HY and Cboe History had not posted 11/6 at the pull.

| Series | Open | High | Low | Close | Prior close | Change |
|---|---:|---:|---:|---:|---:|---:|
| SPX | 7,377.65 | 7,444.20 | 7,369.55 | 7,376.86 | 7,353.73 | +0.31% |
| NDX | 27,045.26 | 27,316.09 | 26,887.69 | 26,989.99 | 26,629.81 | +1.35% |
| QQQ | 658.35 | 664.52 | 654.00 | 656.10 | 647.05 | +1.40% |
| SMH | 473.41 | 476.25 | 456.43 | 463.96 | 447.73 | +3.62% |
| RSP | 215.24 | 217.26 | 214.75 | 216.05 | 216.87 | −0.38% |
| IWM | 271.98 | 274.55 | 270.24 | 273.67 | 270.98 | +0.99% |
| Dow | 51,078.85 | 51,662.26 | 50,992.61 | 51,285.73 | 51,523.06 | −0.46% |
| KRE | 72.15 | 72.73 | 71.82 | 72.20 | 72.31 | −0.15% |
| HYG | 77.32 | 77.36 | 77.22 | 77.23 | 77.28 | −0.06% |
| VIX (vendor, unconfirmed) | 27.68 | 27.76 | 23.47 | 25.64 | 28.18 | −9.01% |

Treasury par 11/6 against 11/5: 2Y 4.51 / 4.46 · 10Y 4.86 / 4.84 · 30Y 5.26 / 5.25. VIX9D 27.18, VIX3M 24.60, VVIX 121.94. SKEW 11/6 not published. ZQZ26 last 95.985 from 15:30 through 16:45 ET.

Own calc through 11/6: SPX 50-day 7,679.45, 100-day 7,618.70, 200-day 7,325.05; QQQ 200-day 680.89; NDX 200-day 27,983.89. SPX closes under the 50-day: 10/30, 11/2, 11/3, 11/4, 11/5, 11/6 (six; 11/4 by 4.35 points).

Gamma outputs: `gamma_spx_both.txt`, `gamma_qqq_both.txt`, `gamma_ndx_both.txt`. Open interest on four sampled QQQ Nov-20 puts matches the 09:55 ET chain exactly, so these maps carry 11/5 trading, not 11/6.
