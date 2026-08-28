[1] enumerating NPORT-P filings holding Athene Global Funding ...
    123 filings | enumeration STOPPED EARLY | pages lost to failure: 0
    20/120 filings, 138 holdings
    40/120 filings, 251 holdings
    60/120 filings, 398 holdings
    80/120 filings, 476 holdings
    100/120 filings, 585 holdings
    120/120 filings, 717 holdings
[2] 717 raw holdings, 0 fetch failures
[3] 527 priced holdings after dedup/sanity
[4] 53 matched funds (hold Athene AND >=1 peer); 492 holdings
[5] period 2026-05-31 | curve as-of 2026-05-29 (BACKFILLED 2d) | tenors [2, 3, 5, 7, 10, 20, 30] | OK: {2: 3.98, 3: 4.06, 5: 4.13, 7: 4.27, 10: 4.45, 20: 4.98, 30: 4.99}
[5] period 2026-06-30 | curve as-of 2026-06-30 (exact) | tenors [2, 3, 5, 7, 10, 20, 30] | OK: {2: 4.14, 3: 4.15, 5: 4.19, 7: 4.3, 10: 4.44, 20: 4.93, 30: 4.91}

==============================================================================
FABN PEER-RELATIVE SPREAD — NPORT-P holder marks, matched funds only
periods: ['2026-05-31', '2026-06-30'] | matched funds: 53 | holdings: 449
==============================================================================

--- 0-3y ---
   GLOBALATL   n=39   median T+  70.2bp   (min  -15.3 / max  118.3)
   ATHENE      n=106  median T+  68.9bp   (min  -42.7 / max  184.6)
   COREBRIDGE  n=60   median T+  63.9bp   (min   27.1 / max  155.2)
   PRICOA      n=9    median T+  47.0bp   (min   21.0 / max   92.0)
   METTOWER    n=15   median T+  44.0bp   (min    5.6 / max   54.9)
   NYLIFE      n=50   median T+  32.3bp   (min  -27.4 / max   75.1)
   MASSMUTUAL  n=22   median T+  26.2bp   (min  -21.1 / max   50.8)
   >>> ATHENE PEER PENALTY: +18.5bp  (peer median T+50.4, n=195)

--- 3-6y ---
   ATHENE      n=46   median T+ 112.0bp   (min   93.3 / max  126.8)
   GLOBALATL   n=43   median T+  86.8bp   (min   71.8 / max  144.8)
   COREBRIDGE  n=15   median T+  73.3bp   (min   65.8 / max   80.5)
   METTOWER    n=2    median T+  59.4bp   (min   55.8 / max   63.1)
   PRICOA      n=8    median T+  57.6bp   (min   52.4 / max   64.8)
   MASSMUTUAL  n=10   median T+  57.0bp   (min   50.8 / max   72.5)
   NYLIFE      n=6    median T+  50.3bp   (min   39.9 / max   59.5)
   >>> ATHENE PEER PENALTY: +37.8bp  (peer median T+74.2, n=84)

--- 6-11y ---
   ATHENE      n=9    median T+ 136.4bp   (min  132.0 / max  136.9)
   GLOBALATL   n=2    median T+  93.3bp   (min   93.1 / max   93.4)
   COREBRIDGE  n=3    median T+  89.5bp   (min   86.6 / max   89.5)
   NYLIFE      n=4    median T+  69.5bp   (min   64.9 / max   80.1)
   >>> ATHENE PEER PENALTY: +49.7bp  (peer median T+86.6, n=9)

wrote /home/willi/Research-workspace/AGENTS/SHADE/research/FABN_PEER_SPREAD_NPORT_2026-07-27.json
