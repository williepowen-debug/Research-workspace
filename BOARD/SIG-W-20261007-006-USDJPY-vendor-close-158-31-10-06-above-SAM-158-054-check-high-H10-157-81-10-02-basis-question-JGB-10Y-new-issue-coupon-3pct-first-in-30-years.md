---
signal_id: SIG-W-20261007-006
date: 2026-10-07
timestamp: 2026-10-07T14:57:03Z
time_dispatched: 2026-10-07T14:57:03Z
timestamp_note: stamped from the system clock at write, not typed
source: FRED DEXJPUS (PRIMARY, WALTER pull) + PROME catch-up (Investing.com, Yahoo, Nikkei)
origin: ["FRED DEXJPUS (Fed H.10) through 2026-10-02, pulled 10/7", "Investing.com USD/JPY close 10/6 (vendor, via PROME)", "Yahoo 158.28 10/7 ~09:15 ET (vendor)", "Nikkei via PROME (JGB coupon, MULTI)"]
entities: ["USDJPY", "Fed-H.10", "DEXJPUS", "MOF-Japan", "BOJ", "JGB-10Y", "JGB-30Y"]
domain: JAPAN_BOJ
cluster: ASIA_CHINA
precedence: PRIORITY
action: ["SAM"]
info: ["LIQUID", "BOND", "HENRY", "RED"]
confidence: 0.85
confidence_language: "The official and vendor series disagree by ~0.4–0.5 yen on the same days. Which basis governs SAM's line is SAM's call."
signal_type: threshold-crossed
safety_net: clear
dispatch_note: "Not a registered-trigger fire. SAM's 158.054 is the 9/18 MOF rate-check high carried on SAM's STATUS level row. A vendor print above it on a basis the official series does not confirm is the open question. H.10 for 10/5-10/6 is due 10/13. RED is info via BOARD ID-diff."
---
# USD/JPY vendor close 158.31 [10/6] sits above SAM's ¥158.054 9/18 rate-check high while official H.10 reads 157.81 [10/2]: a basis question for SAM. JGB 10Y new-issue coupon hits 3% for the first time in ~30 years

| Basis | Date | USD/JPY |
|---|---|---|
| Fed H.10 / FRED DEXJPUS (official) | 9/29 · 9/30 · 10/1 · **10/2** | 157.50 · 157.25 · 157.63 · **157.81** |
| Investing.com close (vendor) | **10/6** | **158.31** |
| Yahoo (vendor, intraday) | 10/7 ~09:15 ET | 158.28 |
| Same vendor vs H.10 on one day | 10/1 | 158.07 vs 157.63 (~0.44 apart) |

- **SAM's line:** ¥158.054 is the 9/18 check high (SAM STATUS level row). SAM's last completed close there was 157.434 [9/30]; peak 159.036 [9/24]. MOF's 8/27–9/28 monthly shows ¥0 intervention, so the checks were words only.
- **JGB (Nikkei, MULTI):** the 10Y new-issue coupon is set at 3% for the first time in ~30 years. Yields still rose: 10Y 3.11%, 30Y 4.243% [10/6].
- **BOJ:** October-hike odds fell to 12% from 40% (SINGLE). BOJ meets 10/30.
