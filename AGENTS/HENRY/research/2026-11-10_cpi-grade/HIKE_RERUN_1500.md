# HEN-63 December-hike rerun, 15:00 ET 2026-11-10 (PROME tap 15:02 ET)

**Pulled 15:02–15:03 ET** (desktop, Claude Code, Opus 5.5). Method unchanged from 9/24 and 11/6: Dec average = 100 − ZQZ26; days 1–9 at EFFR 3.88 [FRED, latest print 11/9; 11/10 publishes 11/11], days 10–31 at the post-meeting rate; post = (31 × avg − 9 × 3.88) / 22; binary P = (post − 3.88) / 0.25. Vendor last trade (yfinance ZQZ26.CBT 1-minute, prepost), **not CME settlement**; one 0.005 tick = 0.7bp = 2.8 points. cmegroup.com is blocked here, so FedWatch was not read; ORACLE owns venue odds.

## Reading

| Read | ZQZ26 | Dec average | Post-meeting | Priced | Binary probability |
|---|---:|---:|---:|---:|---:|
| 11/6 15:00 ET (registration comparison) | 95.985 | 4.015 | 4.070 | +19.0bp | 76% |
| 11/9 15:00 ET | 95.975 | 4.025 | 4.084 | +20.4bp | 82% |
| 11/10 08:25 ET, after Waller 04:00, before CPI | 95.945 | 4.055 | 4.127 | +24.7bp | 99% |
| 11/10 08:35 and 11:00 ET, after CPI | 95.920 | 4.080 | 4.162 | +28.2bp | 113% |
| **11/10 15:00 ET (last trade 14:37 ET, 50 lots; no trade 14:38–15:02)** | **95.925** | **4.075** | **4.155** | **+27.5bp** | **110%: 25bp fully priced plus about 10% of a further 25bp** |
| Range 08:30–15:02 ET (67,514 contracts) | 95.910 – 95.945 | | | +29.6bp – +24.7bp | 118% – 99% |

Session distribution of 1-minute closes since 08:30: 95.920 (100 minutes), 95.925 (47), 95.915 (20), 95.930 (1), 95.910 (1). **The afternoon sits one tick under the morning peak, inside the post-print range.**

Further out (vendor last, contract averages, no meeting split attempted): ZQF27 95.825 → 4.175% January average; ZQH27 95.620 → 4.380% March average (95.615 / 4.385% at 11:00 ET; 95.725 / 4.275% pre-print 08:25 ET). March still carries about 22bp above the December post-meeting rate, so a second hike by March stays roughly priced.

## What changed against the morning read

1. **Nothing material since 11:00 ET.** 95.920 → 95.925, one tick (0.7bp, about 3 points). Both the Waller leg (82% → 99%, 04:00 ET minute) and the CPI leg (+3.5bp at 08:30) held through the session. Nothing given back beyond that tick.
2. **The 50bp tail is still priced at about 10%** (it was about 13% at 11:00). The binary 25-or-hold model fails above 100%. The residual reads as a 50bp December probability only if one assumes no other path. That assumption is a model choice, not an observation.
3. **Stocks recovered part of the day while rates did not.** ES 7,538.5 at 14:50 ET (low 7,503.75); SPX 7,505.60 −0.59% at 15:02 ET (vendor quote); 10Y 4.99% (vendor, about +13bp on the day); VIX 19.89 (−0.15%). ZT 102.023 at 14:50 against 101.977 low: the 2Y future bounced about 1.5 ticks off its low while December fed funds did not move.

## HEN-63

**Not re-marked: 0.70 stands.** The letter carries no re-mark clause: it settles on the 12/9 statement (upper bound above 4.00% = YES). The futures comparison now sits about 30 points above the forecast on the binary scale (110% vs 70%). I record that gap as the market's read against mine. It is not a revision, and I do not claim an edge for my 0.70. The case for the shade at registration (4.5 weeks of data, the October precedent, a soft core expectation) has lost its CPI leg: core printed 0.3, not my +0.2. A re-mark, if any, is Will's or the letter's, not this session's.

Sources: yfinance ZQZ26.CBT / ZQF27.CBT / ZQH27.CBT / ZT=F / ES=F 1- and 5-minute bars (`.venv`); FRED EFFR csv; `FORGE/tools/market-data/fetch.py price ^GSPC ^TNX ^VIX` 15:02 ET; morning reads `CPI_GRADE.md`, `OVERNIGHT_HIKE_REPRICING.md`.
