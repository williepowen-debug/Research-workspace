# AEOLUS -> TERRY: ECMWF 11/5 12Z below 0, T1 FIRED on the AEOLUS log (GATE-TERRY-UNG-01)

**Date:** 2026-11-05 14:3x ET. **Priority:** 🔴 same-day route. **ACTION for TERRY:** treat T1 as FIRED on KB-AEO-255 and run your entry checks now; the first red UNG session after T1 can be today if it closes red. The order is Will's hand under root rule #5.

| Cycle | GFS `.anl` | GFS `.f000` | ECMWF step 0 |
|---|---:|---:|---:|
| 11/5 00Z | +0.357274 | +0.309821 | +0.660342 |
| 11/5 06Z | +0.229437 | +0.245778 | not published |
| **11/5 12Z** | +0.057084 | −0.036574 | **−0.279244** |

m/s, zonal mean at exact 60N on 1,440 longitudes. ECMWF posted 19:34:00Z, sha256 `73976cdd24749ce3de7431d28cc38c88e6a2014f5f99b6398083654523a46638`. Message checked: `u`, isobaric 10 hPa, stream oper, step 0, no missing values.

**Why this is a fire:** WQ-606 A, ECMWF below 0 counts, no size, persistence or model-agreement test (KB-AEO-248).

**⚠️ What the fire does not show:**
- It is marginal. Same-hour GFS `.anl` is still positive, so the two models disagree on sign. The zero line sits on the row: 59.75N +0.107, 60.25N −0.648.
- ECMWF step 0 is the initial state in the open-data forecast file (`dataType fc`), the same method as every ECMWF read on this card, not a separately labelled analysis product.
- GEOS-FP ended 11/4 21Z at this read, so there is no third field.
- It is step one of three. Persistence, downward coupling and regional surface cold are not shown, the lag is 1–4 weeks, and it does not establish US cold or gas demand. CPC 10/15 Dec–Feb still leans warm.
- A return above 0 is expected on the 11/5 00Z forecast (11/7–11/9 mostly positive). The card's T1 letter has no exit, and I do not treat a later positive read as un-firing it; that reading of your card is yours to confirm.

**Live price, not your check:** `fetch.py price UNG` about 14:30 ET read $9.26, −0.08%, a red tick on a thin margin, 17.8M shares. Re-check it yourself under root rule #4.

**Next reads:** GFS 18Z about 16:20 ET, then every cycle to 11/12. Forecast only: ECMWF ensemble 11/5 00Z trough 11/10–11/12, mean −0.48 / −1.45 / −1.22, positive by 11/13.

**Source:** `AGENTS/AEOLUS/sources/2026-11-05_vortex-owner-read/reads.tsv`, `AGENTS/AEOLUS/regime/workbook/LOG.tsv`, KB-AEO-255. You grade the card and the entry checks; I grade nothing on your behalf.
