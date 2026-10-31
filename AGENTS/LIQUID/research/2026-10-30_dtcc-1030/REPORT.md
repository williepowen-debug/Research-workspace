# DTCC SEC cumulative credits, 10/30 — ORCL / CRWV (and Meta) 5Y read

**Wake:** PROME prome-34 Tier-1 follow-up, spawned ~20:09 ET Fri 2026-10-30. File `https://pddata.dtcc.com/ppd/api/report/cumulative/sec/SEC_CUMULATIVE_CREDITS_2026_10_30.zip`: HTTP 404 at 20:09 ET, **HTTP 200 (114,826 B) at 20:15:33 ET**; 1,563 SEC credit rows. Read 20:15 ET with `scripts/dtcc_cds_probe.py` (batch filter on: 0 BATCH rows for each name) and `scripts/crwv_cds_grade.py` (ISDA-approximation, clean/dirty). No CORR/MODI/EROR/TERM row names ORCL or CRWV in the file. Raw outputs: `dtcc_cds_1030.txt`, `crwv_grade_1029_1030.txt` (this directory). Zips not committed (re-fetchable at the URL).

**Basis for every bp figure below:** MODEL-DERIVED par spread from the OBSERVED UPFRONT (DTCC field "Other payment amount", UFRO, unsigned, buyer-pays assumed), flat-hazard r=4% R=40% — not ISDA, good to tens of bp — unless marked "disseminated" (DTCC spread field, observed). "5Y" = standard 2031-12-20 maturity; 2030-12-20 = 4Y.

## ORCL (BBB−, coupon 100bp)

| Cell | 10/29 (carried) | 10/30 |
|---|---|---|
| 5Y converted, 10/30-executed prints (n=9 upfront prints, 13:40Z–20:28Z) | 270–276bp (7.14–7.37pt) | **280–294bp** (7.53–8.06pt); late-day cluster 290 (7.91pt ×3) |
| 5Y disseminated | none (3Y 208bp) | **293bp ×2 (19:51Z)** |
| Other tenors in file | — | 4.5Y (2031-06-20) 258 [10/29 21:00Z late report] → 279 [10/30 17:26Z]; 4Y (2030-12-20) 245 [10/29 21:00Z late]; 3.6Y 270 [10/20 late] |

⇒ **ORCL 5Y +~10–18bp d/d** (converted 270–276 → 280–294; disseminated 276–280 [10/28] → 293 [10/30]); conversion and disseminated agree within ~3bp at the 19:28–20:28Z cluster (KB-LIQ-150 cross-check satisfied: level ~190bp from the coupon). ORCL equity raw close $130.67 −6.37% [10/30, `fetch.py`]. Still below the ~315 [10/21] read.

## CRWV (coupon 500bp)

| Cell | 10/29 (carried) | 10/30 |
|---|---|---|
| **5Y (2031-12-20)** | 989–1,004bp probe (978–992 clean / 998–1,012 dirty, grader) | **NOT PRINTED** — zero 5Y CoreWeave NEWT rows in the 10/30 file |
| 4Y (2030-12-20) | 934bp probe / 926 clean / 948 dirty (12.21pt, executed 10/29 18:47Z, reported in the 10/30 file) | **980–986bp probe / 972–977 clean / 995–1,000 dirty** (13.32pt 12:59Z; 13.44pt 13:02Z flagged NONSTD) |

⇒ **No 10/30 5Y CRWV cell.** The 4Y moved ~+46bp (12.21 → 13.32pt, one unflagged print each side, 18h apart) — a different tenor from the L2 instrument, context only; the 4Y→5Y relation (5Y − 4Y ≈ +50–65bp clean on 10/29) cannot be assumed to carry. Both 10/30 4Y prints are at 13:0x Z (09:0x ET), BEFORE most of the session's equity fall (CRWV raw close $54.87 −9.66% [10/30, `fetch.py`]; intraday worst −11.76% 15:40 ET per PROME).

## Grades (letter only; no re-count)

- **GATE-LIQ-069 L2** (KB-LIQ-069 letter of 10/02: DTCC standard 5Y, ISDA lines A >697 / B >737 positive-sign, A >520 / B >649 negative-sign): **no 10/30 standard 5Y print ⇒ 10/30 UNOBSERVED on the L2 instrument.** Last 5Y 978–1,012 [10/29] clears all four lines on both sign readings (upfront 15pt, far from par). L2 stays **FIRED [9/26]**, measured, no re-count; gate 2-of-2 FIRED unchanged. The 4Y prints (972–1,000) would also clear every line but are not the instrument and are not graded.
- **GATE-LIQ-069 L4 equity half:** CRWV raw close −9.66% > −15% ⇒ CRWV alone does not meet; IREN/APLD/NBIS closes and the HY 10/30 cell (FRED Monday 11/2) not read ⇒ **L4 10/30 UNGRADEABLE-PENDING-PUBLICATION**, unchanged.
- **GATE-LIQ-072 event legs (file-borne only):** ORCL 5Y 280–294 / disseminated 293 is the same issuer already scored (not a "3rd/4th issuer" instance) ⇒ no new instance. **Meta 5Y 2031-12-20: 0.95–0.99pt upfront on 100 cpn (3 prints) ⇒ buyer-pays reading 121–122bp vs 108–115 [10/28] and the 121–127 record [10/23]; |upfront| < 1.5pt ⇒ SIGN UNKNOWABLE (KB-LIQ-150 / L510 limit 4) — not a citable level, not graded;** no disseminated Meta spread in the file. Meta is AA, not an IG issuer at BB-like spreads, in any case. 072 stays QUIET / NOT FIRED; price legs (IG >94, basis <180) wait for the 10/30 FRED cells (11/2).
- **Not graded tonight:** FRED ICE 10/30 cells (HY >320 run 2-of-3, 069 L1/L4, 072 price legs) — publish Monday 11/2; owed row re-dated there (10/31 is a Saturday).

## Judgment (one session, n=1)

The AI-capex → credit chain's named "next discriminating observation" printed **directionally wider, modest in size**: ORCL 5Y +10–18bp on a −6.4% equity day; CRWV 4Y +~46bp on a −9.7% equity day, with the CRWV prints taken in the first half-hour. Wider on both names on the day the equity broke, but inside a range the CRWV curve has already visited (5Y 1,110 on a 10/16 late print) — **credit is following equity, not leading it, and a one-day d/d this size does not establish restriction.** Mainly repricing stays the call. The CRWV 5Y has no 10/30 print; the next file (Mon 11/2, ~20:15 ET) is the first chance.
