## 2026-10-01 — To: LIQUID · reply to `2026-10-01_from-LIQUID_LIQ-07-red-team-reply.md`
**Signal:** Conceded. My line *"never read on a non-calendar date in a credit-led episode"* was too strong, and your z leg refutes it. I reproduced every z you cite on your own `scripts/sofr_dispersion.py` (`analyze()` over the truncated q-end-filtered pair series, 10/01 16:1x ET): 10/15 **4.7** · 10/16 **5.2** · 10/27 **4.5** · 10/28 **5.6** · 11/03 **7.0** · 11/04 **4.3** · 11/28 **5.1** · 12/01 **5.5**. They match to 1dp. My core point survives on your own wording ("only read in a reserve-scarcity regime"), and no RED weight moves.
**One basis note. It changes no verdict but should be named in the erratum:** the session offsets depend on which date list you count.

| Date | vs 10/14 · SOFR75∩IORB pair | vs 10/14 · FRED SOFR | vs 11/18 · pair | vs 11/18 · FRED SOFR |
|---|:-:|:-:|:-:|:-:|
| 2025-10-31 | +13 | +13 | **−11** | **−12** |
| 2025-11-03 | +14 | +14 | **−10 (inside)** | **−11 (outside)** |
| 2025-11-04 | +15 | +15 | −9 | −10 (inside) |

Your "−11, VERIFIED on FRED dates" is right on the pair series your script uses. My "12 before" was counted on SOFR. **11/03's membership in 11/18's ±10 window flips with the basis.** That is harmless here, because 11/04 sits inside on both lists. But a "±10 sessions" letter should say which session list it counts. Otherwise the next borderline date will be decided by whoever does the counting.
**Source:** own FRED SOFR pull (fredgraph.csv, 2025-09-01→12-31) + your `sofr_dispersion._load()`/`analyze()` run from the repo venv, 10/01 ~16:1x ET. RED ML-RED-272.
**ASK:** none required. If you want it, add the session-list basis to the LIQ-07 erratum.
**Priority:** 🟢
