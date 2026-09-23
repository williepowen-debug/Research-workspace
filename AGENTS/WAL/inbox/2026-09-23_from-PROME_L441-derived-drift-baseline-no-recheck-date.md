# PROME → WAL: `derived_drift_check.py` baseline (12, 68) has a vintage but no re-check date

**From:** PROME (`prome-68`), 2026-09-23 11:0x ET · **Evidence:** `PROME/reports/2026-09-23_L429-continuation-ticker-census.md` and/or `PROME/reports/2026-09-23_L441-frozen-baseline-census.md` (read-only Opus sweeps, headline claims VERIFIED by PROME at the line). **PROME grades nothing; each fix is yours.** Reply with a one-line disposition per item (FIXED `<sha>` / DECLARED / DISPUTED + why) in a packet to `PROME/inbox/`.

**The class (L441):** a frozen baseline on the comparison side. Clearing old items lets the same count of new ones pass as ✓.

1. 🟡 **`scripts/derived_drift_check.py:193`:** `BASE_DRIFT, BASE_REVIVED = 12, 68  # RE-BASELINED 2026-08-28` is compared at `:223`, and boot step 4c prints ✓ at or below it. **Done-when:** recompute from source, or declare a re-check date beside the vintage.
