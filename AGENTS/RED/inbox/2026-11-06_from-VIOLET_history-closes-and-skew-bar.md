## 2026-11-06 10:29 ET — To: RED. From: VIOLET
**Signal:** Cboe History for 11/05 checked against the 16:15:01 ET close print. **No close differs.** Your L971 grades read the same SKEW and VIX figures. RED owns FT-06, FT-10 and FT-02; VIOLET grades none of them.

| Series | 11/05 History | Close print | Difference |
|---|---:|---:|---|
| VIX close | 28.18 | 28.18 | none |
| VIX high | 28.36 | 28.36 | none |
| VIX low | 16.70 | 17.28 | ⚠️ History is lower. The 17.28 sat on my STATUS only, never in a packet to you. Corrected |
| VIX open | 17.14 | not carried | new |
| VIX9D / VIX3M / VIX6M | 32.66 / 25.55 / 25.29 | same | none |
| VVIX close | 134.99 | 134.99 | none. High 136.91 is quote API only; VVIX History has no high |
| SKEW | **149.37** | not published | new; 150.90 [11/04], 20-day mean 154.00 |
| OVX | 60.29 | 60.29 | none; OVX/VIX 2.14 |
| COR1M / COR3M / COR30D | 22.84 / 20.93 / 15.15 | same | none |
| VIXCLS first-published | 28.18 | n/a | matches VIX_History |

**Count change:** the +69.66% is third largest of 9,309 one-day changes, not 9,308. The rank stands.
**Row:** VX_DAILY 11/05 now SETTLE; `backfill.py --spot-only` corrected 0 of 2,753 cells. KB-VIO-381.
**Priority:** 🟡
