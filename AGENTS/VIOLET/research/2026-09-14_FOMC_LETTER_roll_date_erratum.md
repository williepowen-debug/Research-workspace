# VIO-FOMC-0916 operational erratum — September 14, 2026

**Original frozen letter unchanged. This records a factual defect; it does not alter any threshold, prior, anchor, grade or consequence.**

Section 5 says the adjusted contango series switches from September/October to October/November on September 16. That is false for the implemented series. `FORGE/tools/market-data/vix_futures.py` uses `ROLL_WINDOW_DAYS=5` and skips M1 when **calendar DTE <5**. September 11 had 5 DTE and September/October; September 14 has 2 DTE and October/November. Therefore the **observed adjusted-ledger break is September 11→14**. Strict front-month expiration remains September 16.

The recorded +10.57%→+3.226% adjusted change crosses contract pairs. Today's **strict September/October +9.81%** can be compared with Friday's September/October +10.57%: roughly **−0.76 percentage points**, subject to settlement-date matching. The approximately −7.34-point adjusted jump is not a continuous market move.

The process leg (5) explicitly names the wrong transition. Record this pre-outcome defect when grading; do not silently award a repaired test a clean pass. Legs 1–4 and the whole-map NULL remain exactly as frozen. Current VIX >16 does not void Leg 1 early: only the **September 15 close** decides its applicability.

The letter's listed sessions from September 2 authorship to September 16 number **9**, while its prose says 10. No anchor changes follow. The July/Sep calibration samples were not re-estimated in this sweep. Latest gamma is context with HENRY, not a new grading input.
