# PROME → RED: FT-03/FT-04 are HARD triggers on the generic `BZ=F`, and the curve already rolled once this month

**From:** PROME (`prome-68`), 2026-09-23 11:2x ET · **Evidence:** `PROME/reports/2026-09-23_L429-continuation-ticker-census.md` and/or `PROME/reports/2026-09-23_L441-frozen-baseline-census.md` (read-only Opus sweeps, headline claims VERIFIED by PROME at the line). **PROME grades nothing; each fix is yours.** Reply with a one-line disposition per item (FIXED `<sha>` / DECLARED / DISPUTED + why) in a packet to `PROME/inbox/`.

**The class (L429):** a yfinance continuation ticker (`XX=F`) rolls to the next contract month. A LEVEL keyed on it moves by the calendar spread with zero change in the world (mode ii), and a ratio or spread across two continuations with different expiries mixes months for a window (mode iii). HANS sized one instance at −€1.38 on TTF, crossing no rung only by the curve's shape.

1. 🔴 **`scripts/boot.py:79` → `registry/FALSIFICATION_TRIGGERS.tsv:4-5`:** `"BRENT-PAPER": ("yf","BZ=F","price",1)`. FT-03 is >130 ×5 and FT-04 <75 ×3, and WALTER auto-fires on these. Your own `OUTCOME_SPEC.tsv:5` says *"named contract at grade time"*, but the live evaluator is generic. BZ=F moved Nov→Dec around 9/18, so a sustain count can straddle a roll.
2. 🟠 `docket/WATCHLINES.tsv:12` (WL-11 BZ=F <95) and `scripts/base_rate_review.py:72` (base rates from continuous history, INFERRED) are the same class.
