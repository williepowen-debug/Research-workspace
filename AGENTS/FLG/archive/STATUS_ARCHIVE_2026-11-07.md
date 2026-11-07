# FLG STATUS ARCHIVE — rotated 2026-11-07

Verbatim blocks (sessions 2026-11-02 and 2026-11-01) rotated out of `STATUS.md` on 2026-11-07 (FLG, PROME prome-bf spawn) to make room for the Q3 10-Q session block. History, never current. crc32 of the block (UTF-8 bytes, exactly as between the fences): `1961fa7e`.

```
## SESSION 2026-11-02 — bounded freshness audit and corrections

The SEC feed checked at **11:11 ET** showed no new 8-K/10-Q after the 10/23 earnings filing; the 10/27 BlackRock 13G/A and 10/28 director Form 4 were already logged. Q3 Call Report was consumed 11/01 and WALTER card 026 was the latest FLG handoff. Corrected current-state figures in `THESIS.md` v1.0.4 and `workbook/EXIT_PROTOCOL.md`; re-dated the sole stale ACTIVE KB row (KB-FLG-032) without adding data. **Full Q3 flow/FDM/maturity review, prediction grading and kill-rail re-derivation remain assigned to the 10-Q session.**

## 🟠 SESSION 2026-11-01 — T-01: the Q3 Call Report, ingested at the primary 13 days early (PROME C9 spawn on WALTER card 026)

**No prediction, threshold, kill cell or score moved.** The Q3 Call Report was filed (CDR last-update 10/30); FLG pulled it itself (`scripts/ffiec_pull.py`, `sources/ffiec_2026-11-01/`), ingested it (`MI3_FLG.tsv` 9/30 row, PRIMARY) and re-dated T-01 to the Q4 report (2027-02-14). All figures bank level = issuer (one entity since 2025Q4).

| Read | 6/30 → 9/30 | KB |
|---|---|---|
| **SR 07-1** (F158+F159+1460+F161 / total RBC RCFA3792) | 327.52% → **322.11%** ($31.58B / $9.80B); numerator −3.61%, denominator −1.99% — the buyback lifted the ratio ~+6.6pp, the CRE run-off more than offset it | 099 |
| **Non-accrual rate** | Call Report basis (RC-N 1403 / loans 2122) 4.88% → **4.81%**; matched-to-issuer basis (ex GNMA $167.6M, ex HFS $4.2M) 4.59% → **4.55%** = $2,817M | 099 |
| **Coverage** | Call Report basis 29.09% → **29.07%**; matched basis 31.03% → **30.84%** — FLG-02 PREVIEW consistent with HIT, graded only at the 10-Q | 099 |
| **WALTER card 026 FLG figures** | **8 of 8 AGREE** at the primary (equity −$496.183M, RI-A bridge closes to $0, CET1 13.16%→12.38%, income $34.5M→$12.1M, NCO $99.4M→$74.1M, loan provision $14.4M→$74.1M (+$2.0M off-balance = release's +$58M), M3 +54.12%, NDFI +30.48%) | 100 |
| **M3 / NDFI step** | NDFI = new **private-equity-fund (+$599M) and business-credit-intermediary (+$470M)** lending — the issuer's Funds/Lender Finance verticals. M3 total exposure (funded + unfunded RC-L 1.c.(2)) **+12.1%**, not +54%; no reclassification signature. **Which line holds the +$238M M3 step is UNRESOLVED → T-02 10-Q ask** | 101 |
| **K-1 leg 1 context** | Multifamily RCON1460 $26,922M → **$25,965M (−3.56%)**, every observed quarter down; K-1 NOT firing | 102 |
| **Pipeline** | MF 30–89 days past due **$233M → $392M (+68%)** (Q1 $676M — n=3, not a trend); MF 90+ accruing $38M → $50M; modified MF in compliance $199M → $264M; loans repricing ≤12 months +$5.84B (the 2027 wall entering the window, INFERRED) | 102 |

**Routing fired (charter counter-thesis row, literal):** total loans QoQ positive two quarters (+0.88%, +1.50%) — a C&I/NDFI mix shift, multifamily still shrinking. Packets REGINALD (with the M3/NDFI adjudication inputs) + RED, this session. The pre-8/28 total-loans K-1 would have FIRED here; the multifamily re-cut is what kept it from killing the thesis on C&I growth.

**Inbox drained (2):** WALTER SIG-W-20261031-026 → ACTED (KB-100/101, board_log) · PROME FFIEC-token packet → INTEGRATED (T-01 note; KB-103: new expiry 2027-01-31 is 14 days before the Q4 print). `TRADE.md` re-stated: FLG Mar-19-2027 $10P ×1 now in the mirror.

```
