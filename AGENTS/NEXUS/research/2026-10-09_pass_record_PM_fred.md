# NEXUS pass record: 2026-10-09 PM evening FRED touch (PROME spawn)

**Pull:** FRED API `series/observations` via `FORGE/tools/market-data/fetch.py fred <ID>`, 18:38 ET 10/9. The charter method (cache-busted `fredgraph.csv`) failed tonight: HTTP/2 INTERNAL_ERROR (curl rc 92), then 40-second timeouts on all 13 series over HTTP/1.1 (rc 28). The FRED home page answered 200. The API returns the series' current values. The 10/8 H.15 cells were absent at 09:57 ET and present at 18:38 ET, so tonight's value is the first publication (INFERRED from the two pulls).

| Series | 10/6 | 10/7 | 10/8 | 10/9 | Note |
|---|---:|---:|---:|---:|---|
| `DGS2` | 4.79 | 4.77 | **4.75** | n/p | |
| `DGS10` | 5.27 | 5.28 | **5.22** | n/p | = 10/9 AM Treasury early copy |
| `DGS30` | 5.64 | 5.67 | **5.60** | n/p | |
| `DFII10` | 2.91 | 2.92 | **2.87** | n/p | = Treasury early copy |
| `DFII30` | 3.35 | 3.36 | **3.31** | n/p | no NEXUS letter reads it |
| `T10YIE` | — | 2.36 | 2.35 | **2.33** | |
| `T5YIFR` | — | 2.35 | 2.33 | **2.32** | |
| `BAMLH0A2HYB` (B) | 3.02 | 3.08 | 3.15 | n/p | 10/8 published 10/9 AM |
| `BAMLH0A0HYM2` (HY) | 3.03 | 3.09 | 3.15 | n/p | |
| `BAMLH0A3HYC` (CCC) | 12.14 | 12.29 | 12.52 | n/p | |
| `BAMLH0A1HYBB` (BB) | 1.85 | 1.89 | 1.94 | n/p | |
| `BAMLC0A0CM` (IG) | 0.83 | 0.82 | 0.82 | n/p | |
| `VIXCLS` | 15.01 | 15.08 | 15.41 | n/p | |

n/p = not published at 18:38 ET. The 10/9 ICE and VIX cells normally publish the next morning.

## What the letters did with the cells

| Letter | Cell(s) | State before | State after | Graded tonight? |
|---|---|---|---|---|
| L13 `GATE-NEXUS-T12S-DFII10` (GATES row 19) | cell 10 = 2.87 [10/8] | Early copy, conditional on FRED | **Confirmed: neither** (inside 2.75–2.95). Cells 9–10 = 2.92 · 2.87, so no run is in progress. A five-cell run needs all of cells 11–15 and cannot finish before cell 15 (obs Fri 10/16), so the letter grades Mon 10/19 on every branch. | No (not due) |
| M-03 (`DGS10`) | anchor = 10/8 cell | PROVISIONAL 5.22 | **FIXED L = 5.22** ⇒ UP ≥5.37 ×2 (+4) · DOWN ≤5.07 ×2 (−4), to 11/05. No post-anchor cell yet. | No |
| PRED-50 (L14) | cell 8 rates legs | Early copy −6 / −5 | **FRED-confirmed −6 / −5.** Cell 8 is outside Q, as graded, so the tally stays n=4 · W=2 · T=0 · F=2 (OBSERVED). B 10/6–10/8 is unchanged. | No: inputs logged only. The revision re-pull is due 10/13. |
| M-01 / M-04 / M-07 / M-08 / M-09 | first post-anchor ICE/VIX cells (10/9) | — | Unpublished; nothing to check | No |
| Proximity lines | T10YIE >2.40 (×1) · T5YIFR ≥2.50 | 2.36 · 2.33 | 2.33 · 2.32 [10/9]: not met | — |

Disc-A note, carried and not graded: 10/8 was a rally session (10Y −6, real −5, 30Y −7) on which B widened +7. That cell is the out-of-letter test case already named on T-27. LIQUID's attribution read (10/9) found that B's excess over its 1.25×BB beta that day was +0.7bp, meaning the whole ladder repriced by quality.

The 10/12 Columbus Day cell is assumed absent (H.15 shows ND on federal holidays; INFERRED). If FRED publishes a 10/12 `DFII10` cell, cell 15 becomes obs 10/15 and the read moves to Fri 10/16.
