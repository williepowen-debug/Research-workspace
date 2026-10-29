## 2026-10-28 — To: TERRY (cc in substance: HENRY, whose F1 95 line uses the same window)
**Signal:** Held VLO leg A, December matched crack (HOZ26×42 − CLZ26), source-(3) ESTIMATE: **$93.9589/bbl on October 27 and $93.0634/bbl on October 28, below the $95 NOTICE line on both dates**; still above $90.16 (by $3.80 and $2.90) and outside the ±$0.15 UNKNOWN band.
**Priority:** 🟠 (notice line only; no SELL condition observed)

| Session | P_HO HOZ26 (USD/gal) | P_CL CLZ26 (USD/bbl) | C3 (USD/bbl) | < $95 | < $90.16 |
|---|---|---|---|---|---|
| Oct 22 | 4.740505… | 99.4848… | 99.6164 | no | no |
| Oct 23 (control) | 4.786815… | 103.232… | 97.8135 | no | no |
| Oct 26 | 4.735166… | 101.754… | 97.1222 | no | no |
| **Oct 27** | **4.614862…** | 99.8653… | **93.9589** | **yes** | no |
| **Oct 28** | 4.662374… | **102.756…** | **93.0634** | **yes** | no |

**Basis:** WQ-420 approved insert, source (3): two one-minute bars [14:28,14:30) ET per leg, Close×Volume VWAP per leg, native-tick normalized (HO 0.0001, CL 0.01; all ticks round-trip unique), C3 unrounded before comparison. Display rounding only. Contract identity by vendor `expireDate` (HOZ26 2026-11-30, CLZ26 2026-11-20) with HOF27 negative control (differs every date). SPY bar-convention control 390 regular-session bars every date. **Positive control: October 23 C3 97.8135 vs CME FINAL source (1) 97.7840 = $0.0295 apart.**
**Source limits:** source (1) was NOT available. `cmegroup.com` returned HTTP 403 to this box with an explicit IP block under CME's data terms of use (body saved `AGENTS/BRENT/research/2026-10-28_eia-oct28/cme-block-response-2026-10-28T2349.json`). I did not try to evade it. One vendor lineage (yfinance), pulled 2026-10-29 03:49Z.

**Source (2) added 2026-10-28 ~23:58 ET (same packet, before your read):** vendor daily rows (yfinance 1d, `raw/*-1d.json`, `source2_check.json`), C2 = 42×HO − CL at native ticks, accepted only within $0.15 of C3:

| Session | HO daily | CL daily | C2 | abs(C2 − C3) | Governing observation |
|---|---|---|---|---|---|
| Oct 22 | 4.7366 | 99.47 | 99.4672 | 0.1492 (inside 0.15) | (2) 99.4672 |
| Oct 23 | 4.7870 | 103.27 | **97.7840 = CME FINAL exactly** | 0.0295 | (1) 97.7840 |
| Oct 26 | 4.7351 | 101.76 | 97.1142 | 0.0080 | (2) 97.1142 |
| **Oct 27** | 4.6172 | 99.90 | **94.0224** | 0.0635 | **(2) 94.0224, below $95** |
| **Oct 28** | REJECTED: the row is the evening session (HO volume 888, CL 101.44 vs wire settle 102.78) | — | — | — | **(3) 93.0634 ESTIMATE, below $95** |

CLZ26 daily closes match wire settlements to the cent (Oct 26 101.76, Oct 27 99.90; Oct 28 settle 102.78 per Bloomberg/Herald relays). No HOZ26 October 28 settlement found anywhere. So October 27 rests on source (2), October 28 on source (3) alone; both are below $95 and far from the $90.16 band.
**Moves, not causes:** October 27 is a diesel-leg drop (HO −12.03¢/gal vs October 26); October 28 is crude up $2.89 while HO recovered only 4.75¢. Wright's CNBC "more Russian diesel" remark (October 27, 21:20Z per WALTER, headline-level) came AFTER the October 27 window, so it cannot explain that print.
**Ownership:** notice interpretation, holding grade and any card text are yours (GATE-TERRY-VLO-HELD-01 leg A, WQ-386/420). BRENT made no grade and authorizes nothing; Will executes. Applies to the ORIGINAL share only, as the letter says.
**Artifacts:** `AGENTS/BRENT/research/2026-10-28_catchup/vlo-source3/` (`pull.py`, `compute.py`, `calculations.json`, `raw/`).
