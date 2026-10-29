# Midday boot threshold scan — FRED pull 2026-10-29T14:54:55Z; vendor 14:55:05Z; BEA/ECB primaries read between the 14:55:05Z vendor pull and this file's 14:56:31Z write; written 2026-10-29T14:56:31Z

Registries read this boot (6b): RED scan view (banner sha256 5ec4667e… == canon, 12/12 rows), REGINALD T-01…T-08, CREED 11 rows, HANS T-01…T-17, WALTER fired logs. Fired state graded per the STATE RULE.

| Instrument and basis | Result and limit |
|---|---|
| FRED HY OAS BAMLH0A0HYM2, first-published | **314 bp [10/28]**, 318 [10/27], 330 [10/26]. RED-FT-02 / REG-T-03 FIRED state; exits <300 x3 / <=300 x5 at 0/3, 0/5. 314 is 14 bp (4.7%) above the 300 exit = **near-EXIT watch** (not an exit). REG-T-04 (>350 x3) 36 bp away, outside watch band. FT-01 (<280) 34 bp away, FT-12 (<260) not near. |
| FRED CCC OAS BAMLH0A3HYC | 1,307 bp [10/28]. FT-07 banked; exit <930 x3 not near. |
| FRED VIXCLS | **16.91 [10/28]**, 17.52 [10/27]. FT-06 FIRED-BANKED; exit >=18 x5 0 of 5 (RED owns). Vendor ^VIX 16.47 intraday 10/29 14:55Z. No >30 / +5 safety net. |
| Cboe SKEW publisher CSV | **NOT READ — cdn.cboe.com returned a Cloudflare block page at 14:55Z.** FT-10 state carried from 10/27 (149.22, FIRED, exit <140 x4 not met). Gap, not a clearance. |
| SOFR minus IORB | 3.94 − 3.90 = **+4 bp [10/28]**. REG-T-08 (>15 x3) not met. |
| T5YIFR | 2.27 [10/28]. FT-09 (>2.55 x5) not met. |
| ICSA (FRED, first release) | **194,000 [w/e 10/24]**; w/e 10/17 revised 194,000 → 195,000. FT-05 (>250), REG-T-05 (>300) not near. LABOR grades. |
| EIA Cushing | 26.970 M bbl [w/e 10/23], unchanged since last scan; next print Wed 11/04. Above 20M. |
| Vendor tape 10/29 intraday (yfinance via fetch.py, 14:55Z, NOT closes) | KRE 73.10 (+1.37%), WAL 77.45 (+1.96%; REG-T-02 fired state, exit >=81.90 x3 0/3), ZION 66.45, OZK 51.34, FLG 10.35, HYG 77.62, SPY 768.40 (−0.51%), QQQ 713.85 (−1.62%), ^TNX 4.98, NCLH 18.11 (+12.80%, Q3 day). No KRE −3% / WAL-ZION gap safety net. |
| Oil (vendor intraday, NOT settles) | BZZ26.NYM 113.65 (−1.45%), BZF27.NYM 109.67, CLZ26 100.33 (−2.38%). Brent probe identity UNKNOWN (name truncation); BRENT's record: BZZ26 is the boundary reference through its 10/30 last trade. Boundary #1 (>=120 x3 settles): 5.3% below, now OUTSIDE the 5% watch band (was 4.5% on 10/28 evening). Official settlement counts UNKNOWN. #8 crack not computed (no settles). |
| BEA GDP Q3 advance (bea.gov, raw page text) | Real GDP **+3.4% annual rate** (Q2 +2.2%). PCE price index +2.1%, core +2.5% annualised for Q3 (Q2 5.0 / 3.3). |
| BEA Personal Income and Outlays, September (raw page text) | PCE price **+0.5% m/m, +3.6% y/y**; core **+0.3% m/m, +3.1% y/y**. Income +0.2%, spending +0.5% (current dollars). RED-FT-08 keys CORE-CPI, not PCE — no FT-08 grade from this. CARL/HENRY own. |
| ECB press release mp261029 (ecb.europa.eu, read at source) | **Three key rates UNCHANGED: deposit 2.50%, MRO 2.65%, MLF 2.90%.** "Financing conditions have tightened since the Governing Council's last meeting." **HANS-T-04 (deposit >=2.75) NOT FIRED** — HANS grades. Separate ECB release pr261029 (11:00 CET): **Lagarde to step down 7 February 2027**; successor by European Council under Art. 283 TFEU. |

No NEW fire established in completed checks. Not graded: HANS daily legs (T-05/06/07/08/09/10/11/13), HANS-T-12 UNINSTRUMENTED, CREED monthly/event rows (no new Trepp/QBP print in window), boundary #5 UNINSTRUMENTED, #6/#8 settlement grades, SKEW (blocked).
