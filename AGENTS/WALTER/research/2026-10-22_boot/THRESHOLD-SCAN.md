# Boot threshold scan — 2026-10-22 (pulls 11:39–11:42Z)

RED scan view banner hash 32203f81 == canon FALSIFICATION_TRIGGERS.tsv. FRED back from maintenance. Observation dates in brackets; FRED values are first-published (`fetch.py fred --first-published`).

| Row | Instrument / basis | Latest | Rule | Result |
|---|---|---|---|---|
| RED-FT-01 | HY OAS <280 s3 | 333 [10/20] | — | not near |
| RED-FT-02 / REG-T-03 | HY OAS >320 s3 | 325/323/331/329/333 [10/14–10/20] | fired 10/16; exit <300 s3 (FT-02), <=300 s5 (REG-T-03) | FIRED STATE held, exit 0 |
| **REG-T-04** | HY OAS >350 s3 | 333 [10/20] | 17bp away (4.9%) | **NEAR-TRIGGER WATCH, not a fire** (routed in SIG-W-20261022-002 to REGINALD/LIQUID) |
| RED-FT-12 | HY OAS <260 s3 | 333 | — | not near |
| RED-FT-07 | CCC OAS >930 | 1327 [10/20] (1278 [10/15]) | fired-banked | state held, widening |
| RED-FT-06 | VIXCLS exit >=18 s5 | 19.99 [10/16], 18.44 [10/19], 17.31 [10/20]; Cboe 16.68 [10/21] | exit run broken by 10/20 | exit 0-of-5 (RED's 10/19 "2-of-5" reset; RED owns) |
| RED-FT-10 | Cboe SKEW exit <140 s4 | 150.36 [10/21] (Cboe CSV) | fired 10/14 | exit 0 |
| RED-FT-09 | T5YIFR >2.55 s5 | 2.34 [10/21] | — | not near |
| RED-FT-11 | DGS30 5-session <= -10.2bp | 5.56 [10/13] → 5.42 [10/20] = -14bp | conditional classifier, no weight | precondition window live; RED classifies (not dispatched) |
| RED-FT-05 / REG-T-05 | ICSA >250 / >300 | 199K [w/e 10/10] | next print 10/22 08:30 ET | not near |
| RED-FT-03 / -04 | Brent front settle >130 / <75 | BZZ26.NYM 111.84 overnight 11:39Z (not a settle; label truncated) | — | not near |
| RED-FT-08 | core CPI 3-mo | fired 10/14 | next CPI Nov | no change |
| REG-T-01 / -02 | KRE <60 / WAL <78 | 70.62 / 75.55 [10/21 vendor close] | WAL cycle-2 fired state, exit >=81.90 x3 | KRE not near; WAL re-entry, exit 0/3 |
| REG-T-08 | SOFR−IORB >15 | 3.88−3.90 = −2bp [10/20] | — | not near |
| Boundary #8 | Brent 3:2:1 Dec legs | est. ~$41 (RBZ26 3.10, HOZ26 4.72, BZZ26 111.84; overnight, 2dp) | >50 x3 settles | not near |
| Boundary #3 / Cushing | EIA weekly | 27.594M [w/e 10/16] | <20M | not near |
| HANS-T-06 | UK 10Y >5.50 | 5.3882 [10/21, HANS] | 2.0% away | near-trigger watch (HANS-owned, already graded) |
| HANS-T-13 | UK 30Y >6.00 | 5.7970 [10/21, HANS] | 3.4% away | near-trigger watch (HANS-owned) |
| HANS other | per HANS 10/21 grades | T-05 watch open, T-07 L1/L2 open, T-08 orange open, T-10 MET open, T-16 watch 1/2; T-12 UNINSTRUMENTED | — | no new WALTER read |
| CREED | monthly prints | T-01a 12.16 Sept = leg 1 of 2 (CREED 10/21); T-01b office SS 16.85 Sept vs >18 | next Trepp ~11/01 | no new print |

Safety net: no VIX >30 or +5; no HY +25bp in one session. No sustained cross, so no auto-fire. Not a full-registry clearance: CREED/HANS event and qualitative legs were not re-swept by WALTER.
