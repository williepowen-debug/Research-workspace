# Boot threshold scan — 2026-10-23 (pulls 04:37Z, markets closed)

RED scan view banner hash 32203f81 == canon FALSIFICATION_TRIGGERS.tsv (sha256 prefix 32203f81d7d4e5fe). Registries read: RED 12 rows, REGINALD 8, CREED 11, HANS 17 (CREED and HANS changed 10/22, read whole). FRED values first-published (`fetch.py fred <ID> --first-published`); FRED 10/22 bars for HY/CCC/VIXCLS not yet published at pull time.

| Row | Instrument / basis | Latest | Rule | Result |
|---|---|---|---|---|
| RED-FT-01 / FT-12 | HY OAS <280 / <260 s3 | 327 [10/21] | — | not near |
| RED-FT-02 / REG-T-03 | HY OAS >320 s3 | 331/329/333/327 [10/16–10/21] | fired 10/16; exit <300 s3 (FT-02), <=300 s5 (REG-T-03) | FIRED STATE held, exit 0 |
| REG-T-04 | HY OAS >350 s3 | 327 [10/21] | 23bp away (7.0%) | outside the 5% watch band; no new print |
| RED-FT-07 | CCC OAS >930 | 1307 [10/21] (1327 [10/20]) | firing-banked | state held |
| RED-FT-06 | VIXCLS exit >=18 s5 | 16.68 [10/21]; vendor ^VIX close 19.03 [10/22, +14.09%, not FRED] | exit run 0 after 10/20 | if VIXCLS 10/22 publishes >=18 it is exit 1-of-5 — RED owns the count |
| RED-FT-09 | T5YIFR >2.55 s5 | 2.19 [10/22] (2.34 [10/21]) | — | not near |
| RED-FT-11 | DGS30 5-session <= -10.2bp | 5.42 [10/21] | conditional classifier | RED classifies; not dispatched |
| RED-FT-05 / REG-T-05 | ICSA >250 / >300 | 194K [w/e 10/17] | next print Thu 10/29 | not near |
| RED-FT-03 / -04 | Brent front settle >130 / <75 | BZZ26.NYM 113.69 at 04:37Z (overnight, not a settle; identity UNKNOWN — name truncated) | — | not near |
| RED-FT-08 | core CPI 3-mo | fired 10/14 | next CPI Nov | no change |
| REG-T-01 / -02 | KRE <60 / WAL <78 | 72.41 / 76.67 [10/22 vendor close] | WAL cycle-2 fired state, exit >=81.90 x3 | KRE not near; WAL re-entry, exit 0 of 3 |
| REG-T-08 | SOFR−IORB >15 | 3.88−3.90 = −2bp [10/21] | — | not near |
| Boundary #8 | Brent 3:2:1, Dec legs | est. ≈ $39.75 (RBZ26 3.09, HOZ26 4.78, BZZ26 113.69; overnight, 2dp) | >50 x3 settles | not near; month switch to Jan legs Mon 11/02 |
| Boundary #3 / Cushing | EIA weekly | 27.594M [w/e 10/16] | <20M | not near; next print Wed 10/28 |
| HANS (owner grades 10/22) | per HANS registry | T-06 UK10Y 5.34 (2.9% under 5.50); T-13 UK30Y 5.73; T-10 FR–DE 174.6bp OPEN deepening; T-05 Bund 3.3311 watch open; T-07 TTF 90.30 L1/L2 open; T-08 −14.77pp orange open; T-12 UNINSTRUMENTED | — | no new WALTER read; HANS-owned |
| CREED | monthly prints | T-01a leg 1 of 2 (Sep 12.16); T-01b 16.85 vs >18 | next Trepp ~11/01 | no new print |

Safety net: no VIX >30 or +5 points (10/22 +2.35 vendor); no HY +25bp in one session (no new print). No sustained cross → no auto-fire. Not a full-registry clearance: CREED/HANS event and qualitative legs not re-swept by WALTER.
