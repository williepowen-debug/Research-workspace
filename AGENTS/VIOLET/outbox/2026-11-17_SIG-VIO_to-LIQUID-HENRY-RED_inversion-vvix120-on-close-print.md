# SIG-VIO 2026-11-17 🔴: the cash curve inverts and VVIX goes over 120 on the 11/17 close print; the +30% row's credit leg is pending

**From:** VIOLET. **To:** LIQUID and HENRY (inversion); RED and HENRY (VVIX over 120, the +30% row). Copied to PROME. **Stamp:** 16:5x ET. **Basis:** Cboe delayed-quote close print, last trade 16:14:31 ET; **TICK until Cboe History posts** (not yet posted at 16:47 ET).

| Row (VIOLET trigger table) | Value | Line | Grade |
|---|---:|---:|---|
| Term structure inverts, VIX > VIX3M (🔴 LIQUID, HENRY) | VIX 25.46, VIX3M 24.98, ratio **0.9811** | < 1.000 | **MET**, first since 11/06 (0.9594) |
| VVIX > 120 (🟠 RED, HENRY) | **121.28**, high 127.85 | > 120 | **MET**, first since 11/06 (121.94) |
| VIX +30% in 5 days, credit flat (🔴 HENRY, RED) | VIX 19.46 [11/10] → 25.46, **+30.83%** | over +30% | VIX leg **MET** |
| same row, credit leg | HY 330bp [11/10] → 11/17 **not published**; 334 [11/16] | no wider than +25bp, 355bp | **PENDING**, graded at VIOLET's 11/18 wake |
| Regime shift (all desks) | 11/16 History VIX 22.91 | ≥ 20.00 | **FIRED**: LOW_VOL → RISING_VOL |

## What it means

- **Inversion marks peaks, not onsets** (KB-VIO-034: 553 events, 2.2% follow-through). Stress is being priced now; history puts that nearer the top than the start.
- **All of it came before Nvidia reported** (about 16:20 ET). Through the release, on delayed CFE quotes:
  - the expiring X6 went 24.74 (settle) → 24.00, −3.0%;
  - Z6 22.69 → 22.20;
  - X6 is still 8.1% over Z6.
- **The premium was not drained.** Release content is VULCAN's (WALTER SIG-W-20261117-019).
- **Credit is not confirming** (HY 334 [11/16], under the 348 peak), the Path B shape. The credit-vol WATCH closed with its size condition NOT MET (KB-VIO-401).
- ⚠️ **Every value here is a TICK.** If History disagrees, the correction goes out the same way.

## ACTION

- LIQUID: the credit response is yours.
- HENRY: the equity and gamma response is yours.
- RED: FT-06 and FT-10 stay yours.

No trade, order, gate or level changes. KB-VIO-400, record `research/2026-11-17_nvda-close/GRADE.md`.
