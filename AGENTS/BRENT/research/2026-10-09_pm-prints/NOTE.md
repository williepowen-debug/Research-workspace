# BRENT PM prints — Friday 2026-10-09 (PROME DOCKET L659 hand-back, taken at prome-75's request 12:43 ET)

Context: Will closed the AM session at 11:15 ET. PROME then asked BRENT to take its own three registered items when the prints landed. This is measurement only, with no trade or gate authority.

## ② MMA / BSEE Isaias shut-in — 10/9

[CONF BSEE/MMA primary] `…/mma-monitors-gulf-response-isaias3`, "Friday, October 9, 2026". Page was live at 12:43 ET; saved here as `mma_isaias3.html`. Figures are operator reports as of **11:00 a.m. CDT 10/9**, 12 companies.

| Item | 10/9 | 10/8 (isaias2) | Change |
|---|---:|---:|---:|
| Oil shut-in | **1,458,814 b/d = 71.51%** | 1,282,879 = 62.89% | **+175,935 b/d** |
| Gas shut-in | 1,259.2 MMcf/d = 58.84% | 57.35% | +1.49 pp |
| Platforms evacuated | 129 of 371 (34.77%) | 121 | +8 |
| Non-DP rigs evacuated | 8 of 11 (72.73%) | 5 | +3 |
| DP rigs moved off | 2 of 17 (11.76%) | 4 | −2 |

- **Implied Gulf base:** 1,458,814 ÷ 0.7151 ≈ **2.04 mb/d**, consistent with the 10/8 implied base.
- **[EST] WPSR week ending 10/9:** shut-in days 10/7, 10/8 and 10/9 at 0.51, 1.28 and 1.46 mb/d, plus a partial 10/6, give ≈ **3.3–3.6M bbl** lost in the week. That supersedes the 10/8 estimate of 3.1–3.5. It prints **Thu 10/15 12:00 ET**, and carries the shut-in only if EIA's production estimate does.
- **Interpretation:** this is the pre-landfall peak trajectory. The barrels return in days if there is no damage; damage is the tail risk.
- Refineries were NOT re-checked at this read; the AM status stands (no cut found; Chevron's "operational" statement is Thursday's).

## ③ Settle-window matched diesel crack — 10/9 (ESTIMATE; TERRY grades WQ-386 leg A)

[EST single vendor] yfinance 1-min bars 14:28–14:30 ET, typical-price VWAP (same method as `../2026-10-08_isaias-hormuz/PM_NOTE.md`); all 3 window bars present on all 4 legs. `crack_pull.py` run at 14:44:46 EDT (`evidence.json`). The first run at 14:33:17 returned **NOT MEASURABLE**: the vendor feed lagged ~10 min (last bar 14:23), so the window was not yet published. Kept as `evidence_1433_lagged.json`; it is a feed-latency artefact, not a missing-leg verdict.

| Leg | Window VWAP (typ) | Window vol |
|---|---:|---:|
| HOX26 | $4.73874/gal | 3,659 |
| CLX26 | $91.86774 | 7,556 |
| HOZ26 | $4.58826/gal | 2,970 |
| CLZ26 | $91.01829 | 6,383 |

| Crack | 10/9 typ VWAP | close-convention | 10/8 typ | Change |
|---|---:|---:|---:|---:|
| **Nov `HOX26×42−CLX26`** | **$107.15941** | $107.21518 | $113.57914 | **−$6.42** |
| **Dec `HOZ26×42−CLZ26`** | **$101.68866** | $101.75503 | $107.32876 | −$5.64 |

- Nov (governs leg A through the 10/14 settle) is **$17.00 above $90.16** (sell line) and **$12.16 above $95** (notice line); not within ±$0.15 of either ⇒ no UNKNOWN band. Dec is diagnostic until 10/15.
- The 10/8 distillate jump (+$7.79) has mostly retraced: crude is flat-to-up (CLX26 ~$91.87 vs 10/8 settle relay $91.49), heating oil is down. This is consistent with China's reduced export resumption and/or Isaias tracking east of the Louisiana/Texas refining belt. It does not discriminate between them (no refinery cut announced as of the AM read).
- Daily vendor rows NOT used (L05: today's bar is still forming). No official CME settle is available to BRENT.
