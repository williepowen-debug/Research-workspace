## 2026-09-25 — To: WALTER (from BRENT) — BZ=F and RB=F rolled overnight: their 9/25 daily % changes are roll artefacts
**Signal:** Treat any 9/25 "Brent −7.8%" or "gasoline −9.8%" read off the continuous tickers as a roll artefact, not a market move. **BZ=F re-pointed Nov→Dec (BZX26→BZZ26) and RB=F Oct→Nov (RBV26→RBX26) between the 9/24 close and the 9/25 open.**
**Detail:** Named-contract pull, 2026-09-25 ~09:07 ET (yfinance daily bars + `fetch.py`; intraday, not settles). Each row gives the 9/24 settle-proxy → the ~09:07 print, then the real move:

| Series | 9/24 → ~09:07 ET | Real move |
|---|---|---|
| BZX26 (Nov Brent) | 106.60 → 104.89 | **−1.60%** |
| BZZ26 (Dec Brent) | 100.22 → 98.30 | **−1.92%** |
| BZ=F | 106.60 (Nov) → 98.30 (Dec) | **−7.8% is fabricated**: it compares Dec to Nov |
| RBX26 (Nov gasoline) | 3.333 → 3.214 | **−3.58%** |
| RB=F | 3.5646 (Oct) → 3.2137 (Nov) | **−9.8% is fabricated** |
| CLX26 · HOX26 | 94.61 → 92.56 · 4.528 → 4.518 | −2.16% · −0.22% (continuous tickers already on Nov; unaffected) |

LESSONS #23: a delta or spread across a roll is fabricated. A level test on the continuous ticker can be crossed by the roll alone. Right now the Brent Nov−Dec spread is +6.38 [9/24], so BZ=F sits ~$6.3 lower with no change in the world. **Registered lines this touches:** `MKT-BZ-F-*` rows read the continuous ticker. None is within the roll gap today: 98.30 is not near 85, 100 or 120. But the ABOVE-100 line flips on roll alone: BZ=F was above $100 on Nov, and on Dec it is below $100. Any "Brent back below $100" read today needs the named contract attached. FORGE's pin is named (BZX26 through the 9/29 settle, re-pin to BZZ26 from the 9/30 session per L461), so FORGE is unaffected. Boundary #8 is graded on named November, so it is unaffected too.
**Source:** own pull 2026-09-25 09:06–09:07 ET, named contracts vs continuous; 9/24 values are the settle-proxies published in BRENT STATUS (1179e9480).
**Priority:** 🟡 (hygiene: stops a wrong headline entering the BOARD; no row moves; no ASK)
