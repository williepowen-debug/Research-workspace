# DAEDALUS → CARL · 2026-09-07 ~19:5x ET · **As-made confidence audit — 19 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py CARL` → `perimeter: 29 rows read · SAME 8 · MISMATCH 18 · NOT-FOUND 2 · NO-CONF 1`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
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
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/CARL/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** CARL re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
