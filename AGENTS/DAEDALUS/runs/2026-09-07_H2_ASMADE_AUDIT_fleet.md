# H2 — AS-MADE CONFIDENCE AUDIT, fleet run · 2026-09-07 ~19:5x ET · DAEDALUS (harvest batch, Will-ruled 2026-09-07 "Go ahead with the batch")

**Tool:** `scripts/asmade_audit.py --all-seeded` (built tonight; positive control = LABOR's ledger at `1d17dacfa^` fires on every row LABOR's own audit found; clean-side limits stated in the docstring). **What a MISMATCH means:** the earliest STATUS blob carrying the ID shows a different confidence from the ledger's as-made — a CANDIDATE the owner verifies at the named blob. **Two named limits:** (1) cell-only percentages, else first % after the ID on a prose line; (2) an ID can post-date the registration (a row born as prose and numbered later) — if the ledger `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (LABOR's 9/7 method). **What this is for:** the 2026-03-04 rollout (`91c301279`) stamped placeholder `Date_Made` on 55 rows across 11 desks; LABOR found 4 of 12 scored rows mis-scored this way (Brier 0.299 → 0.342). Every seeded desk has the same exposure; this is the per-desk candidate list. Packets sent per desk (carve-out ①).

| Desk | rows | SAME | MISMATCH | NOT-FOUND | NO-CONF |
|---|---|---|---|---|---|
| CARL | 29 | 8 | 18 | 2 | 1 |
| HANS | 9 | 4 | 1 | 4 | 0 |
| HAWK | 21 | 3 | 4 | 14 | 0 |
| HENRY | 40 | 0 | 0 | 0 | 40 |
| LABOR | 19 | 12 | 6 | 1 | 0 |
| LIQUID | 6 | 2 | 3 | 1 | 0 |
| MARCO | 16 | 1 | 8 | 7 | 0 |
| OTTO | 20 | 4 | 6 | 10 | 0 |
| REGINALD | 20 | 3 | 5 | 12 | 0 |
| SAM | 34 | 8 | 15 | 11 | 0 |
| ZHAO | 17 | 8 | 9 | 0 | 0 |

**HENRY: NO Confidence column at all** — 40 rows, none calibratable; a Brier cannot be computed for the desk. Separate finding (packet).

## Raw output
```
[CARL] ledger AGENTS/CARL/thesis/PREDICTIONS.tsv · 29 rows · Confidence col: yes
   MISMATCH   CRL-01   ledger as-made  75% (Date_Made 2026-03-03) vs STATUS earliest  28% @7e7e419b8 2026-07-10 :: **Updated:** 2026-07-10 (inbox-processing session — HAWK Russia-diesel/CRL-01 + CREED CMBS-MF + energy live-refresh integrated; **no score c
   NOT-FOUND  CRL-02   ledger as-made  70% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   CRL-04   ledger as-made  98% (Date_Made 2026-03-10) vs STATUS earliest   6% @4e8c98359 2026-03-09 :: | CRL-04 | Hardship 401k >5.5% | 6% | — | — | — | ✅ CONFIRMED |
   MISMATCH   CRL-05   ledger as-made  20% (Date_Made 2026-03-10) vs STATUS earliest  90% @4e8c98359 2026-03-09 :: | CRL-05 | Fannie MF DQ >0.80% | 0.74% | 6bps | Q2 2026 | 90% | ⚠️ IMMINENT |
   MISMATCH   CRL-06   ledger as-made  78% (Date_Made 2026-03-10) vs STATUS earliest  88% @4e8c98359 2026-03-09 :: | CRL-06 | Student 90+ >10% | 9.6% | 0.4pp | Q1 2026 | 88% | ⚠️ IMMINENT |
   MISMATCH   CRL-07   ledger as-made  40% (Date_Made 2026-03-10) vs STATUS earliest  75% @4e8c98359 2026-03-09 :: | CRL-07 | CC 90+ >13.74% (GFC) | 12.70% | 1.04pp | Q2 2026 | 75% | TRACKING |
   MISMATCH   CRL-08   ledger as-made  45% (Date_Made 2026-03-10) vs STATUS earliest  70% @4e8c98359 2026-03-09 :: | CRL-08 | Foreclosures >70K/qtr | 58,140 | 12K | Q2 2026 | 70% | TRACKING |
   NOT-FOUND  CRL-09   ledger as-made  73% (Date_Made 2026-03-31) — ID never appears with a % in STATUS history
   MISMATCH   CRL-10   ledger as-made  62% (Date_Made 2026-03-31) vs STATUS earliest  70% @ba402e60f 2026-05-03 :: | CRL-10 | Food CPI YoY >4.0% | 70% | Q4 2026 | Wheat 107yr low, urea $690s |
   MISMATCH   CRL-11   ledger as-made  83% (Date_Made 2026-03-31) vs STATUS earliest  85% @3427660fc 2026-06-05 :: | CRL-11 | Hires rate ≤3.2% through Q2 | 85% | Jul/Aug releases | Currently 3.1% COVID-low |
   MISMATCH   CRL-12   ledger as-made  20% (Date_Made 2026-04-02) vs STATUS earliest  77% @3e4b234ba 2026-04-02 :: | CRL-12 | SYF FY2026 NCO >6.0% (guidance ceiling) | 77% | FY2026 (Jan 2027) | Feb 5.8%, near ceiling in month 2 |
   MISMATCH   CRL-13   ledger as-made  75% (Date_Made 2026-04-06) vs STATUS earliest  70% @c876257f0 2026-04-07 :: | CRL-13 | SAVE non-selection rate >35% | 70% | Oct 1 2026 | NEW — 2.6M+ face $0→$407/mo cliff |
   MISMATCH   CRL-14   ledger as-made  55% (Date_Made 2026-04-06) vs STATUS earliest  65% @c876257f0 2026-04-07 :: | CRL-14 | MOHELA-caused defaults >500K from Jul 1 | 65% | Q3-Q4 2026 | NEW — servicer capacity near-zero for clean transition |
   MISMATCH   CRL-15   ledger as-made  35% (Date_Made 2026-04-09) vs STATUS earliest  65% @d619854c2 2026-06-06 :: | CRL-15 | SBA 7(a) default rate >6.5% by end-2026 | 65% | Q4 2026 | *(POP domain)* Currently 3.7% (12-yr high); Crestmont projects 6.5-7.5%
   MISMATCH   CRL-16   ledger as-made  35% (Date_Made 2026-04-09) vs STATUS earliest  60% @d619854c2 2026-06-06 :: | CRL-16 | Regional-bank Q2'26 SB-related provisions +25% YoY | 60% | Jul-Aug 2026 | *(POP domain)* Tariff cash-flow stress → 30DPD (3-5mo) 
   MISMATCH   CRL-17   ledger as-made  25% (Date_Made 2026-04-09) vs STATUS earliest  55% @d619854c2 2026-06-06 :: | CRL-17 | SB owner income destruction >$100B annualized | 55% | Q3 2026 | *(POP domain)* Base $73-145B pre-tariff → $83-165B post-Apr tarif
   MISMATCH   CRL-20   ledger as-made  35% (Date_Made 2026-05-01) vs STATUS earliest  75% @656c41795 2026-05-01 :: | CRL-20 | ≥3 of {ALLY, COF, SYF, RITM} show NCO/DQ acceleration breaking "headline clean" pattern | **75%** | Q1 2027 | **NEW v2.5 — outer 
   MISMATCH   CRL-21   ledger as-made  25% (Date_Made 2026-05-01) vs STATUS earliest  60% @656c41795 2026-05-01 :: | CRL-21 | NCOs at ALLY/COF/SYF visible inflection by Q3 2026 + vintage projections ≥+50bps over FY2023 baseline | **60%** | Q3 2026 | **NEW
   MISMATCH   CRL-23   ledger as-made  45% (Date_Made 2026-05-03) vs STATUS earliest  70% @e7177e56e 2026-05-03 :: | CRL-23 | FY27 builder gross-margin compression (DHI/PHM) — tariff $10,900/home pass-through hits FY27 GM ≥-200bps | **70%** | FY27 (early 
   MISMATCH   CRL-26   ledger as-made  70% (Date_Made 2026-07-16) vs STATUS earliest  28% @e6bd71c6f 2026-07-18 :: **Updated:** 2026-07-18 (Sat — Fable-orchestration session, Will co-piloting, 4-agent Opus wave. **Gas $3.992 = $0.008 from the $4.00 line; 
   perimeter: 29 rows read · SAME 8 · MISMATCH 18 · NOT-FOUND 2 · NO-CONF 1
[HANS] ledger AGENTS/HANS/workbook/PREDICTIONS.tsv · 9 rows · Confidence col: yes
   NOT-FOUND  HNS-01   ledger as-made  12% (Date_Made 2026-03-04) — ID never appears with a % in STATUS history
   NOT-FOUND  HNS-02   ledger as-made  60% (Date_Made 2026-07-16) — ID never appears with a % in STATUS history
   NOT-FOUND  HNS-03   ledger as-made  55% (Date_Made 2026-07-16) — ID never appears with a % in STATUS history
   NOT-FOUND  HNS-04   ledger as-made  70% (Date_Made 2026-07-16) — ID never appears with a % in STATUS history
   MISMATCH   HNS-05   ledger as-made  88% (Date_Made 2026-08-28) vs STATUS earliest  75% @b33d305ee 2026-08-28 :: | **HNS-05** | **ECB HIKES 25bp to 2.50% deposit on Sept 10 2026** | **75%** | 2026-09-10 | ECB press release `ecb.europa.eu/press/pr` 13:45
   perimeter: 9 rows read · SAME 4 · MISMATCH 1 · NOT-FOUND 4 · NO-CONF 0
[HAWK] ledger AGENTS/HAWK/thesis/PREDICTIONS.tsv · 21 rows · Confidence col: yes
   NOT-FOUND  HAW-01   ledger as-made  25% (Date_Made 2026-02-18) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-02   ledger as-made  60% (Date_Made 2026-02-18) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-03   ledger as-made  95% (Date_Made 2026-02-18) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-04   ledger as-made  55% (Date_Made 2026-03-01) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-05   ledger as-made  65% (Date_Made 2026-03-01) — ID never appears with a % in STATUS history
   MISMATCH   HAW-06   ledger as-made  70% (Date_Made 2026-04-20) vs STATUS earliest  35% @132abbd04 2026-06-08 :: **Calibration anchor:** HAW-06 just FAILED because I called clean ceasefire lapse Apr 21 when reality delivered Trump-deferral-on-Munir-requ
   NOT-FOUND  HAW-07   ledger as-made  65% (Date_Made 2026-04-20) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-08   ledger as-made  55% (Date_Made 2026-04-20) — ID never appears with a % in STATUS history
   MISMATCH   HAW-09   ledger as-made  35% (Date_Made 2026-06-08) vs STATUS earliest  12% @132abbd04 2026-06-08 :: 4. **Iran walkback by Jun 15** (HAW-09) — Iran returns to mediated talks OR Khamenei walk-back of nuclear "fantasy" line. Promotes B from 12
   NOT-FOUND  HAW-10   ledger as-made  25% (Date_Made 2026-06-08) — ID never appears with a % in STATUS history
   MISMATCH   HAW-11   ledger as-made  20% (Date_Made 2026-06-08) vs STATUS earliest  90% @f21e2db68 2026-06-12 :: **Framework gap (registered Jun 12):** prediction set covers Iranian leakage onto *Gulf* energy infra (HAW-11) but not US strikes on *Irania
   NOT-FOUND  HAW-12   ledger as-made  55% (Date_Made 2026-06-19) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-13   ledger as-made  45% (Date_Made 2026-06-19) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-14   ledger as-made  70% (Date_Made 2026-06-19) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-15   ledger as-made  65% (Date_Made 2026-06-19) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-16   ledger as-made  70% (Date_Made 2026-07-12) — ID never appears with a % in STATUS history
   NOT-FOUND  HAW-17   ledger as-made  60% (Date_Made 2026-07-12) — ID never appears with a % in STATUS history
   MISMATCH   HAW-18   ledger as-made  55% (Date_Made 2026-07-25) vs STATUS earliest  60% @a552c04be 2026-07-25 :: **🆕 HAW-18 registered 7/25 (60%, → Sep 1) — first HAWK-native prediction post-split.** *Through Sep 1, NEITHER theater produces a production
   perimeter: 21 rows read · SAME 3 · MISMATCH 4 · NOT-FOUND 14 · NO-CONF 0
[HENRY] ledger AGENTS/HENRY/workbook/PREDICTIONS.tsv · 40 rows · Confidence col: NO
   perimeter: 40 rows read · SAME 0 · MISMATCH 0 · NOT-FOUND 0 · NO-CONF 40
[LABOR] ledger AGENTS/LABOR/workbook/PREDICTIONS.tsv · 19 rows · Confidence col: yes
   MISMATCH   LAB-02   ledger as-made  70% (Date_Made 2026-02-18) vs STATUS earliest  72% @cc0d0ab9e 2026-03-06 :: | LAB-02 | U-3 reaches 4.7%+ | Q2 2026 | **72%** ↑ | U-3 now 4.4% (up from 4.3%). NFP -92K = accelerant. 0.3pp gap to trigger. |
   MISMATCH   LAB-03   ledger as-made   7% (Date_Made 2026-02-18) vs STATUS earliest  65% @cc0d0ab9e 2026-03-06 :: | LAB-03 | Claims breach 250K | Q2-Q3 | 65% | Shadow payroll gap verdict Mar-Apr |
   MISMATCH   LAB-05   ledger as-made  70% (Date_Made 2026-02-18) vs STATUS earliest  55% @cc0d0ab9e 2026-03-06 :: | LAB-05 | KFRC earnings miss | Q1 2026 | 55% | ⬇️ from 70% — sequential growth counter |
   MISMATCH   LAB-07   ledger as-made  60% (Date_Made 2026-02-18) vs STATUS earliest  65% @cc0d0ab9e 2026-03-06 :: | LAB-07 | DOGE separations >400K | Q3 2026 | 65% | 327K already, Schedule Policy/Career Mar 6 |
   NOT-FOUND  LAB-09   ledger as-made  60% (Date_Made 2026-02-18) — ID never appears with a % in STATUS history
   MISMATCH   LAB-10   ledger as-made  75% (Date_Made 2026-02-18) vs STATUS earliest  70% @cc0d0ab9e 2026-03-06 :: | LAB-10 | 70%+ layoff cohort shows revenue decel | Q3 2026 | 75% | Framework base rate |
   MISMATCH   LAB-11   ledger as-made  50% (Date_Made 2026-02-18) vs STATUS earliest  55% @cc0d0ab9e 2026-03-06 :: | LAB-11 | AI narrative shield breaks | Q3-Q4 | 55% | Second post-layoff earnings cycle |
   perimeter: 19 rows read · SAME 12 · MISMATCH 6 · NOT-FOUND 1 · NO-CONF 0
[LIQUID] ledger AGENTS/LIQUID/workbook/PREDICTIONS.tsv · 6 rows · Confidence col: yes
   MISMATCH   LIQ-01   ledger as-made  70% (Date_Made 2026-02-26) vs STATUS earliest  11% @94c546c06 2026-03-11 :: **One-liner:** HY OAS 319bps [CONF Mar 9] — 1bp from LIQ-01 trigger. Mar 10 FRED release today. DIFC targeted by Iran (new vector). VIX 24.9
   NOT-FOUND  LIQ-02   ledger as-made  55% (Date_Made 2026-02-26) — ID never appears with a % in STATUS history
   MISMATCH   LIQ-03   ledger as-made  50% (Date_Made 2026-02-26) vs STATUS earliest  25% @0fe650ca0 2026-07-01 :: - **LIQ-03 RESOLVED ACHIEVED-at-letter, TAIL-FORM (7/1):** PC/MM CLO senior AAA repriced through 160 in the Mar-Apr stress (Diameter S+170/1
   MISMATCH   LIQ-05   ledger as-made  55% (Date_Made 2026-07-08) vs STATUS earliest  60% @9333a2a3b 2026-07-11 :: - **075** — LIQ-05 VOID (premise-mismatch, Will Option A 7/11: BRENT's DENY mechanism sat outside both scripted branches) + successor LIQ-06
   perimeter: 6 rows read · SAME 2 · MISMATCH 3 · NOT-FOUND 1 · NO-CONF 0
[MARCO] ledger AGENTS/MARCO/thesis/PREDICTIONS.tsv · 16 rows · Confidence col: yes
   NOT-FOUND  MAR-10   ledger as-made  80% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  MAR-15   ledger as-made  75% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   MAR-18   ledger as-made  75% (Date_Made 2026-02-23) vs STATUS earliest  10% @2927ea419 2026-07-02 :: 5. **Q2 predictions resolved (window closed 6/30):** MAR-18 (Cdn air capacity −10%+) **CONFIRMED**; MAR-01 (Nogales residential −50/−60% flo
   NOT-FOUND  MAR-19   ledger as-made  80% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   MAR-01   ledger as-made  65% (Date_Made 2026-02-23) vs STATUS earliest  60% @2927ea419 2026-07-02 :: 5. **Q2 predictions resolved (window closed 6/30):** MAR-18 (Cdn air capacity −10%+) **CONFIRMED**; MAR-01 (Nogales residential −50/−60% flo
   NOT-FOUND  MAR-08   ledger as-made  75% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   MAR-17   ledger as-made  60% (Date_Made 2026-02-23) vs STATUS earliest  43% @db537f001 2026-07-02 :: 6. **STALENESS HUNT + LIVE-RESEARCH corrections (later 7/2 rounds):** **🔴 FL Citizens — MAR-17 (>$750B) INVALIDATED:** "$678.8B" was 2024/ba
   MISMATCH   MAR-11   ledger as-made  72% (Date_Made 2026-02-23) vs STATUS earliest  88% @db537f001 2026-07-02 :: 6. **STALENESS HUNT + LIVE-RESEARCH corrections (later 7/2 rounds):** **🔴 FL Citizens — MAR-17 (>$750B) INVALIDATED:** "$678.8B" was 2024/ba
   MISMATCH   MAR-12   ledger as-made  35% (Date_Made 2026-02-23) vs STATUS earliest  60% @2f40e3be9 2026-07-25 :: 7. **Predictions marked:** MAR-14 **74%→45%** (also reconciled a 74-vs-55 STATUS/TSV drift to one number), MAR-12 **60%→35%**, MAR-24 **45%→
   MISMATCH   MAR-14   ledger as-made  20% (Date_Made 2026-02-23) vs STATUS earliest  74% @2f40e3be9 2026-07-25 :: 7. **Predictions marked:** MAR-14 **74%→45%** (also reconciled a 74-vs-55 STATUS/TSV drift to one number), MAR-12 **60%→35%**, MAR-24 **45%→
   NOT-FOUND  MAR-25   ledger as-made  95% (Date_Made 2026-02-27) — ID never appears with a % in STATUS history
   MISMATCH   MAR-26   ledger as-made  74% (Date_Made 2026-03-23) vs STATUS earliest  17% @2927ea419 2026-07-02 :: 5. **Q2 predictions resolved (window closed 6/30):** MAR-18 (Cdn air capacity −10%+) **CONFIRMED**; MAR-01 (Nogales residential −50/−60% flo
   NOT-FOUND  MAR-27   ledger as-made  90% (Date_Made 2026-03-26) — ID never appears with a % in STATUS history
   NOT-FOUND  MAR-21   ledger as-made  55% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   MAR-24   ledger as-made  55% (Date_Made 2026-02-23) vs STATUS earliest  45% @2f40e3be9 2026-07-25 :: 3. **🟠 FLL May −10.7% is a SUPPLY shock, not FL demand — do not route it as tourism deterioration.** Broward PDF (primary): total 2,255,277 
   perimeter: 16 rows read · SAME 1 · MISMATCH 8 · NOT-FOUND 7 · NO-CONF 0
[OTTO] ledger AGENTS/OTTO/thesis/PREDICTIONS.tsv · 20 rows · Confidence col: yes
   NOT-FOUND  OTTO-01  ledger as-made  75% (Date_Made ?) — ID never appears with a % in STATUS history
   MISMATCH   OTTO-04  ledger as-made  62% (Date_Made ?) vs STATUS earliest  68% @7d12bf40f 2026-07-04 :: > - **OTTO-04 nudged 75→68%** — spring tax-refund bounce softened the monthly Fitch series (recovery up to 37.48%); makes the ~24.3-24.5% Se
   NOT-FOUND  OTTO-06  ledger as-made  70% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-07  ledger as-made  15% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-08  ledger as-made  50% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-09  ledger as-made  65% (Date_Made ?) — ID never appears with a % in STATUS history
   MISMATCH   OTTO-10  ledger as-made  20% (Date_Made ?) vs STATUS earliest  14% @07ac94344 2026-08-14 :: > - **⚠️ A PREDICTION WAS NEARLY GRADED OFF THE WRONG SERIES.** The NY Fed **<620 DOLLAR share is 16.13% and rising** against OTTO-10's inva
   NOT-FOUND  OTTO-11  ledger as-made  60% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-12  ledger as-made  55% (Date_Made ?) — ID never appears with a % in STATUS history
   MISMATCH   OTTO-27  ledger as-made  50% (Date_Made ?) vs STATUS earliest 108% @9416b0f94 2026-04-15 :: - OTTO-27 (FSK coverage <1.0x): **FALSIFIED** — Q4 2025 coverage 108%, dividend maintained
   NOT-FOUND  OTTO-28  ledger as-made  50% (Date_Made ?) — ID never appears with a % in STATUS history
   NOT-FOUND  OTTO-29  ledger as-made  80% (Date_Made ?) — ID never appears with a % in STATUS history
   MISMATCH   OTTO-30  ledger as-made  12% (Date_Made ?) vs STATUS earliest  65% @3c880fbb1 2026-05-22 :: - **OTTO-30 confidence drop 65% → 45%** — Q1 surface swept clean for *new* disclosure; only Q2 2026 earnings (Jul-Aug) and any M&T dollar-am
   MISMATCH   OTTO-31  ledger as-made  12% (Date_Made ?) vs STATUS earliest  60% @c66cec278 2026-05-22 :: - **OTTO-31 confidence dropped 60% → 30%.** Plaintiff allegation looks like litigation rhetoric, not franchise exit. The Tricolor-specific r
   MISMATCH   OTTO-32  ledger as-made  97% (Date_Made ?) vs STATUS earliest  85% @c66cec278 2026-05-22 :: - **OTTO-32 unchanged at 85%** — no early read on May 20 hearing, but no disconfirming signal either; structural picture (PMG plan + UST mot
   NOT-FOUND  OTTO-34  ledger as-made  50% (Date_Made ?) — ID never appears with a % in STATUS history
   perimeter: 20 rows read · SAME 4 · MISMATCH 6 · NOT-FOUND 10 · NO-CONF 0
[REGINALD] ledger AGENTS/REGINALD/workbook/PREDICTIONS.tsv · 20 rows · Confidence col: yes
   MISMATCH   REG-02   ledger as-made  65% (Date_Made 2026-02-23) vs STATUS earliest  60% @cc0d0ab9e 2026-03-06 :: | REG-02 | FHLB advances spike >$600B | Q2-Q3 2026 | 60% |
   MISMATCH   REG-03   ledger as-made  70% (Date_Made 2026-02-23) vs STATUS earliest  50% @cc0d0ab9e 2026-03-06 :: | REG-03 | At least one Tier 1 bank capital raise | H2 2026 | 50% |
   MISMATCH   REG-04   ledger as-made  60% (Date_Made 2026-02-23) vs STATUS earliest  65% @cc0d0ab9e 2026-03-06 :: | REG-04 | Chicago pattern replicates in Phoenix | H1 2026 | 65% |
   NOT-FOUND  REG-05   ledger as-made  40% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-06   ledger as-made  10% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-07   ledger as-made  68% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-08   ledger as-made  45% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   REG-09   ledger as-made  50% (Date_Made 2026-02-23) vs STATUS earliest  20% @f69ff2963 2026-08-13 :: **🟠 8/13 THU 3RD PASS — WILL-RULED SLATE EXECUTED, 5 items. ★ THE UP-CAP HYPOTHESIS I OPENED THIS MORNING IS RETIRED, NOT SUPPORTED — 0 of 1
   NOT-FOUND  REG-10   ledger as-made  65% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-11   ledger as-made  55% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-12   ledger as-made  60% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-13   ledger as-made  72% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-14   ledger as-made  50% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-15   ledger as-made  60% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   MISMATCH   REG-17   ledger as-made  50% (Date_Made 2026-02-23) vs STATUS earliest  20% @f69ff2963 2026-08-13 :: **🟠 8/13 THU 3RD PASS — WILL-RULED SLATE EXECUTED, 5 items. ★ THE UP-CAP HYPOTHESIS I OPENED THIS MORNING IS RETIRED, NOT SUPPORTED — 0 of 1
   NOT-FOUND  REG-18   ledger as-made  45% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   NOT-FOUND  REG-19   ledger as-made  70% (Date_Made 2026-02-23) — ID never appears with a % in STATUS history
   perimeter: 20 rows read · SAME 3 · MISMATCH 5 · NOT-FOUND 12 · NO-CONF 0
[SAM] ledger AGENTS/SAM/thesis/PREDICTIONS.tsv · 34 rows · Confidence col: yes
   MISMATCH   SAM-28   ledger as-made  40% (Date_Made 2026-06-22) vs STATUS earliest   2% @cf2b9479c 2026-07-02 :: **(3) NFP June +57K vs 113K consensus** (revisions **−74K**; U-3 4.2% = participation artifact, 61.5%; AHE +3.5% YoY; Challenger 45.8K cooli
   MISMATCH   SAM-29   ledger as-made  65% (Date_Made 2026-06-22) vs STATUS earliest  85% @a0ce790b1 2026-06-29 :: - **CFTC −146,104 / 81.2% (Jun-23): FIRST COVER off the 83.4% top** (+4,028 WoW; longs −3,677, shorts −7,705; OI 520,825→431,030). Still dee
   MISMATCH   SAM-30   ledger as-made  30% (Date_Made 2026-06-22) vs STATUS earliest  85% @a0ce790b1 2026-06-29 :: - **CFTC −146,104 / 81.2% (Jun-23): FIRST COVER off the 83.4% top** (+4,028 WoW; longs −3,677, shorts −7,705; OI 520,825→431,030). Still dee
   MISMATCH   SAM-31   ledger as-made  35% (Date_Made 2026-06-22) vs STATUS earliest   2% @cf2b9479c 2026-07-02 :: **(3) NFP June +57K vs 113K consensus** (revisions **−74K**; U-3 4.2% = participation artifact, 61.5%; AHE +3.5% YoY; Challenger 45.8K cooli
   MISMATCH   SAM-38   ledger as-made  55% (Date_Made 2026-07-29) vs STATUS earliest  85% @f27fc1961 2026-07-31 :: **BRANCH C FIRED (the ~55% modal call) — SAM-38 RESOLVED CONFIRMED; SAM-34 RESOLVED CONFIRMED (hold @85%).** Primary sources: statement `k26
   MISMATCH   SAM-24   ledger as-made  85% (Date_Made 2026-05-12) vs STATUS earliest  72% @ee4479afb 2026-06-16 :: **Predictions resolved (see PREDICTIONS.tsv):** SAM-21 (June hike) ✅ **CONFIRMED** · SAM-24 (25bp not 50bp) ✅ **CONFIRMED** · SAM-23 (MOF in
   MISMATCH   SAM-26   ledger as-made  70% (Date_Made 2026-05-21) vs STATUS earliest   4% @3b493ea00 2026-05-26 :: 3. **JGB 30Y back below 4.0% (3.931%, -7bp).** Driver: oil collapse + dovish CPI, NOT BOJ super-long operation or insurer return. **SAM-26 (
   MISMATCH   SAM-25   ledger as-made  40% (Date_Made 2026-05-21) vs STATUS earliest 200% @3851059ee 2026-05-26 :: **SAM-25 (any Big 3 <200% @40%) — TECHNICALLY TRUE on Nippon 195% but FAILED IN SPIRIT.** Exact threshold-vs-mechanism trap logged in MEMORY
   MISMATCH   SAM-32   ledger as-made  72% (Date_Made 2026-06-30) vs STATUS earliest  85% @27ab67130 2026-07-01 :: **Forward catalysts** (full docket → `docket/CALENDAR.md`): Thu Jul 2 JGB 10Y auction · Fri Jul 3 CFTC (Jun-30 data) · **Jul 7 JGB 30Y / Jul
   MISMATCH   SAM-08   ledger as-made  85% (Date_Made 2026-02-15) vs STATUS earliest  70% @bc7bdb1f1 2026-05-31 :: - **Why 70%, not 88%:** earned discount — failed TWICE being too-hawkish on the Takaichi 0.75% ceiling (SAM-08, SAM-20), which remains live;
   NOT-FOUND  SAM-14   ledger as-made  60% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-15   ledger as-made  80% (Date_Made 2026-03-20) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-17   ledger as-made  65% (Date_Made 2026-04-13) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-18   ledger as-made  55% (Date_Made 2026-04-13) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-19   ledger as-made  75% (Date_Made 2026-04-13) — ID never appears with a % in STATUS history
   MISMATCH   SAM-20   ledger as-made  60% (Date_Made 2026-04-13) vs STATUS earliest  70% @bc7bdb1f1 2026-05-31 :: - **Why 70%, not 88%:** earned discount — failed TWICE being too-hawkish on the Takaichi 0.75% ceiling (SAM-08, SAM-20), which remains live;
   MISMATCH   SAM-22   ledger as-made  65% (Date_Made 2026-04-24) vs STATUS earliest  25% @2d8659eb5 2026-08-07 :: **Calibration note:** this is the third member of the over-confidence cluster (SAM-08 @90%, SAM-20 @60%) — **but in the opposite direction**
   NOT-FOUND  SAM-04   ledger as-made  60% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-05   ledger as-made  70% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-06   ledger as-made  75% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-07   ledger as-made  48% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-13   ledger as-made  55% (Date_Made 2026-02-15) — ID never appears with a % in STATUS history
   NOT-FOUND  SAM-16   ledger as-made  70% (Date_Made 2026-04-13) — ID never appears with a % in STATUS history
   MISMATCH   SAM-27   ledger as-made  75% (Date_Made 2026-05-21) vs STATUS earliest  74% @3b493ea00 2026-05-26 :: 1. **April CPI DOVISH MISS (May 22).** Core 1.4% vs 1.7% consensus / 1.8% prior — 30bp undershoot, 3rd month below 2% target. Core-core 1.9%
   MISMATCH   SAM-36   ledger as-made  50% (Date_Made 2026-07-10) vs STATUS earliest  85% @a749cb999 2026-07-11 :: **Live anchor state (trued-up Sat 7/11; newest print = Jul-7 data [rel Fri 7/10 3:30 PM ET]):** CFTC **−123,778 = 68.8% of cycle peak** (COV
   MISMATCH   SAM-37   ledger as-made  55% (Date_Made 2026-07-17) vs STATUS earliest  85% @e16b5466f 2026-07-17 :: **Pre-registered SAM-37 verdict map** (graded mechanically at Phase 2 vs the frozen lines): base −123,778/68.8%; **RE-FIRE ≤−153K/85% [SAM-3
   perimeter: 34 rows read · SAME 8 · MISMATCH 15 · NOT-FOUND 11 · NO-CONF 0
[ZHAO] ledger AGENTS/ZHAO/workbook/PREDICTIONS.tsv · 17 rows · Confidence col: yes
   MISMATCH   ZHA-01   ledger as-made  18% (Date_Made 2026-03-03) vs STATUS earliest  70% @0d0ead00a 2026-03-09 :: | ZHA-01 | USD/CNY breaks 7.30 | 70% → **55%** ↓ | ~~2-4 weeks~~ 6-10 weeks | OPEN | DXY <100 sustained 10 sessions + PBOC stops gold buys |
   MISMATCH   ZHA-03   ledger as-made  25% (Date_Made 2026-03-06) vs STATUS earliest  65% @0d0ead00a 2026-03-09 :: | ZHA-03 | Belgium TIC >$500B | 65% | Q1-Q2 2026 | OPEN | Growth decelerates <15% YoY for 2 prints |
   MISMATCH   ZHA-04   ledger as-made  42% (Date_Made 2026-03-06) vs STATUS earliest  65% @0d0ead00a 2026-03-09 :: | ZHA-04 | China official <$650B | 65% | Q2-Q3 2026 | OPEN | NFP relief → may slip to Q3. Watch DXY. |
   MISMATCH   ZHA-06   ledger as-made  72% (Date_Made 2026-03-06) vs STATUS earliest  60% @0d0ead00a 2026-03-09 :: | ZHA-06 | >250 small banks consolidated in 2026 | 60% | 2026 | OPEN | Policy reversal on mergers |
   MISMATCH   ZHA-10   ledger as-made  40% (Date_Made 2026-03-09) vs STATUS earliest  45% @77f56870c 2026-03-22 :: | ZHA-10 | Yuan oil settlement via Hormuz >$5B cumulative | 45% | Q3 2026 | OPEN | Ceasefire reopens Hormuz to all traffic → yuan channel co
   MISMATCH   ZHA-11   ledger as-made  68% (Date_Made 2026-07-09) vs STATUS earliest  65% @c4c0bc33a 2026-07-09 :: | ZHA-11 | China NOT the 30Y 7/9 indirect-bid (77.74%) driver | 65% | OPEN — pre-registered 7/9, indirect test only (TIC has no maturity bre
   MISMATCH   ZHA-12   ledger as-made  80% (Date_Made 2026-07-16) vs STATUS earliest   4% @adeac0f72 2026-07-16 :: **(a) BoK branch — DECISION ALREADY PRINTED, this is now integration + a forward falsifiable consequence (ZHA-12, KB-ZHAO-093/094).** BoK hi
   MISMATCH   ZHA-15   ledger as-made  18% (Date_Made 2026-07-16) vs STATUS earliest  55% @9283ddbe0 2026-07-16 :: | ZHA-15 | Politburo late-Jul meeting signals STIMULUS branch (concrete new fiscal measure) | 55% | OPEN — pre-registered, date TBC |
   MISMATCH   ZHA-16   ledger as-made  45% (Date_Made 2026-09-02) vs STATUS earliest  35% @d757fb63b 2026-09-02 :: | 🆕 **ZHA-16** | **Xi–Trump summit (9/24) produces branch A — an official output extending the reciprocal-tariff suspension beyond 2026-11-1
   perimeter: 17 rows read · SAME 8 · MISMATCH 9 · NOT-FOUND 0 · NO-CONF 0
ASMADE-AUDIT 1: >=1 MISMATCH candidate — candidates, owner verifies at the named blob
```
