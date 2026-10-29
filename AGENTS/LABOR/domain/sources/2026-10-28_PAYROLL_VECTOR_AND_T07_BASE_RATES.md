# Payroll vector (BD-26) and WARN trigger T-07 (BD-36): base rates and sources, 2026-10-28

⚠️ **NOT PRE-REGISTERED.** Candidates were chosen in the same session the numbers were computed. Any letter adopted from this file is post-hoc.

## Part 1: BD-26, should the monthly payroll number carry a score?

**Data:** FRED PAYEMS (current vintage, revised) + USREC, pulled 2026-10-28, 1950-01 … 2026-09.
**Scaling:** each K threshold is expressed as a share of the 2026-09 level (159,044K), so 50K = 0.031% a month in every decade.
**Eligible months:** expansion months, excluding the 12 months after any recession month. Weak payrolls right after a recession are recovery, not warning; including them drove every lift below 1 in the first, unscaled pass.
**Outcome:** a recession month occurs within the next 6 or 12 months.

Raw output (verbatim):
```
PAYEMS 1950-01.. 2026-09 | scaled to the 2026-09 level 159044.0 K | expansion months excl. 12 mo after any recession month

== horizon 6 mo | eligible months 670 | base P(recession within 6) = 0.090
3-mo avg < 0K-equivalent (0.000%/mo): fires 26/670 = 0.039 | recession within 6 3/26 = 0.115 lift 1.29 | episodes 11, first-month hit 1/11 | since 2015: ['2025-08', '2025-10', '2026-02']
3-mo avg < 50K-equivalent (0.031%/mo): fires 40/670 = 0.060 | recession within 6 8/40 = 0.200 lift 2.23 | episodes 17, first-month hit 5/17 | since 2015: ['2025-03', '2025-06', '2026-02']
3-mo avg < 100K-equivalent (0.063%/mo): fires 64/670 = 0.096 | recession within 6 14/64 = 0.219 lift 2.44 | episodes 23, first-month hit 7/23 | since 2015: ['2024-06', '2025-02']
two negative months running: fires 11/670 = 0.016 | recession within 6 2/11 = 0.182 lift 2.03 | episodes 8, first-month hit 2/8 | since 2015: []

== horizon 12 mo | eligible months 664 | base P(recession within 12) = 0.181
3-mo avg < 0K-equivalent (0.000%/mo): fires 22/664 = 0.033 | recession within 12 6/22 = 0.273 lift 1.51 | episodes 9, first-month hit 2/9 | since 2015: ['2025-08']
3-mo avg < 50K-equivalent (0.031%/mo): fires 36/664 = 0.054 | recession within 12 12/36 = 0.333 lift 1.84 | episodes 16, first-month hit 7/16 | since 2015: ['2025-03', '2025-06']
3-mo avg < 100K-equivalent (0.063%/mo): fires 58/664 = 0.087 | recession within 12 19/58 = 0.328 lift 1.81 | episodes 23, first-month hit 10/23 | since 2015: ['2024-06', '2025-02']
two negative months running: fires 11/664 = 0.017 | recession within 12 2/11 = 0.182 lift 1.01 | episodes 8, first-month hit 2/8 | since 2015: []
```

**Read:**
- **Best candidate: 3-mo avg < 50K-equivalent.** It fires in `36/664 = 5.4%` of eligible months. A recession followed within 12 months `12/36 = 33.3%` of the time, vs base `18.1%`, lift `0.333/0.181 = 1.84`; 7 of its 16 episodes hit in the first month.
- **Negative months are a weaker signal than slow months.** "Two negative months running" has a 12-month lift of 1.01, because negative payrolls mostly happen inside recessions, not before them.
- **Recent false alarms:** it fired 2025-03, 2025-06 and 2026-02 (3-mo avg below 50K-equivalent on the revised data) with no recession so far.
- **Where we are now:** revised 3-mo avg Jul–Sep 2026 `(−10 + 133 + 29)/3 = 50.7K`, right at the line.
- **Caveats:** revised vintage, which is hindsight (first prints run about −66K below current on average, so real time is noisier); 11–12 post-1950 recessions, so the sample is small.

**Design options for Will:**
- (a) Add **v17 Payroll momentum**: revised 3-mo avg ≥100K ⇒ 1 · 50–100K ⇒ 2 · <50K ⇒ 3. Re-graded at each NFP on the revised 3 months. On today's data it scores **2** (50.7K), the total becomes 27/80, and the denominator moves 75 → 80.
- (b) No vector. Payrolls stay inside Kill A, T-06 and freeze-thaw LEG A only.

## Part 2: BD-36, T-07 WARN trigger, is there a monthly source?

**Finding:** YES, and the 9/29 "unmeasurable" verdict (KB-LAB-196) was an **instrument miss**. That session read LayoffAlert.org's page TEXT through fetch-tool summaries. The monthly series is in the page's embedded chart JSON ("Mass Layoffs by State – Last 24 Months", employees affected per month, 46 jurisdictions), which a text summary never sees. Extracted 2026-10-28 → `2026-10-28_layoffalert_monthly_by_state.tsv` (page "Updated October 26, 2026").

**Basis:** keyed by layoff EFFECTIVE date (labels run to 2028), not notice date. Recent and future months fill in as notices arrive. **[2ND]**: a secondary aggregator of state WARN notices, not a primary.

Monthly totals, employees affected (TOTAL column of the TSV):
```
Oct '24 5282
Nov '24 16832
Dec '24 31597
Jan '25 25265
Feb '25 18873
Mar '25 29227
Apr '25 23420
May '25 20033
Jun '25 32722
Jul '25 19877
Aug '25 24419
Sep '25 25253
Oct '25 24836
Nov '25 27071
Dec '25 30895
Jan '26 31299
Feb '26 28346
Mar '26 27839
Apr '26 49538
May '26 35420
Jun '26 36665
Jul '26 30086
Aug '26 22158
Sep '26 23189
Oct '26 19163
Nov '26 25794
Dec '26 10812
```
- Over the 24 completed months Oct '24 – Sep '26, **>50K/mo was never reached** (peak Apr '26 49,538). T-07 "accel >50K/mo" would fire in `0/24` months, a rare trigger in a no-recession sample.
- The old STATUS figure "~17K/mo [STALE 2026-07-02]" was on an unknown basis and is not comparable. Retire it either way.

**Options for Will:**
- (a) Revive T-07 on this series, tagged [2ND]: a COMPLETED month (graded the following month, once late notices land) with employees affected >50K ⇒ T-07 fires (→ CARL, REGINALD). Add a fetch step.
- (b) Retire T-07 as unmeasurable on a primary.
