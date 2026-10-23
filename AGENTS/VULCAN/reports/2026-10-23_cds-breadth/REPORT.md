# Is CDS widening spreading? DTCC single-name cross-section, 9/30 → 10/22

**Written:** 2026-10-23 ~14:58 ET (from `date`) · **Asked by:** Will, direct session ("It looks like more companies CDS are widening. Can you check?") · **Owner of spread tells:** LIQUID (this is a VULCAN check for the S1/S5 mechanism, not a grade of LIQUID's gates) · **$0, no score change.**

## Answer

**Yes, but the breadth is in tech and AI, not everywhere.** Of 12 tech/AI names with a reported 5-year spread, **11 widened and none tightened** (median **+12.5%, +8bp**). Of 22 other names (banks, utilities, telecom, sovereigns, industrials), **11 widened, 1 tightened and 10 were flat** (median **+3%, +2bp**). The biggest moves are at the AI financing chain: **CoreWeave ~980–1,010 → ~1,112bp**, **Oracle 264 → 314bp**, **Nvidia 93 → 117bp** (since 10/16), **Broadcom 137 → 156**, **Meta 103 → 118.5**, **Alphabet 73 → 82.5**, **Amazon 72.5 → 80.5**. The hyperscalers are still strong investment grade at 80–120bp. The pattern fits lenders and bond buyers hedging a ~$186B funding gap (DEWEY, KB-268), not a market pricing default.

## Panel (DTCC SEC-regime public dissemination; standard Dec-2031 5Y; median of the day's disseminated spreads)

| Name | Base (date) | Latest (date) | Change |
|---|---|---|---|
| CoreWeave ⚠️ upfront-derived | ~973–1,008 (10/13) | ~1,112 (10/22) | ~+120bp |
| Oracle | 264 (10/13) | 314 (10/22) | **+50bp, +19%** |
| Nvidia | 93 (10/16) | 117 (10/22) | **+24bp, +26%** |
| Broadcom | 137 (10/13) | 156 (10/21) | +19bp, +14% |
| Meta | 103 (10/13) | 118.5 (10/22) | +15.5bp, +15% |
| AMD | 95.5 (10/13) | 110 (10/22) | +14.5bp, +15% |
| Alphabet | 73 (10/13) | 82.5 (10/22) | +9.5bp, +13% |
| Amazon | 72.5 (10/09) | 80.5 (10/20) | +8bp, +11% |
| Intel | 86.5 (9/30) | 94.5 (10/22) | +8bp, +9% |
| Cisco · IBM · Motorola · Arrow | 42–69 | 47–74 | +4.5 to +6bp |
| Avnet | 79.5 (9/30) | 78 (10/21) | −1.5bp |
| SpaceX | 216 (10/16) | 240 (10/22) | +24bp |
| **Non-tech, 22 names** | | | **median +2bp**; wider: Netflix +13, T-Mobile +12, Wells Fargo +7, D.R. Horton +6.5, Argentina +115; tighter: Paramount −23; utilities, Lockheed, Caterpillar, Pfizer, NextEra flat |

Context: HY OAS 340bp [10/22] from 327 [10/21] (FRED first-published); DEWEY attributes most HY widening to a broad September move, with the AI leg small in index terms (KB-274).

## Caveats (they travel with the answer)

- **Thin and uneven.** Only 34 names had a disseminated spread both early and late; many days have one trade per name. Base dates differ by name (9/30, 10/09, 10/13 or 10/16; the earliest available print in that window is used).
- **Sign problem excluded, not solved.** Trades reported only as an upfront payment carry no sign, so investment-grade upfront trades were dropped. CoreWeave is the exception: at a 500bp coupon with an 18-point upfront the sign is unambiguous. Its level is a flat-hazard approximation (LIQUID's probe), good to tens of bp.
- **Unit-error prints dropped:** values under 5bp (e.g. Oracle 2.1, Alphabet 0.7 on single trades) and Kohl's (12.9 → 420, unit mismatch) are excluded.
- **10/23 is not in yet:** DTCC posts each day's file ~20:15 ET.
- Vendor levels (Markit, ICE, Bloomberg) differ from DTCC prints by moment and method; LIQUID owns the reconciled level.

## What it means for VULCAN

- **S1:** the widening runs along the AI chain — supplier (Nvidia, Broadcom, AMD) to payer (Meta, Alphabet, Amazon) to levered builder (Oracle, CoreWeave). Credit protection is being bought on the funding gap. **No S1 rule is keyed to CDS; no capex cut; NOT FIRED.**
- **S5:** CDS levels are not an S5 test (the tests are a new issue +150bp or pulled, a second tariff jurisdiction, or failed collateral). **S5 4, n=2, unchanged.**
- **Nvidia is the one to watch:** +26% in four sessions for a company with a $108.5B guarantee/commitment book (KB-121, KB-153; VULCAN-17 resolves ~11/19 on the NVDA 10-Q).

Data: `dtcc_5y_spread_prints.json` (every disseminated 5Y print used, by name and day); method `build_panel.py`. Source files `https://pddata.dtcc.com/ppd/api/report/cumulative/sec/SEC_CUMULATIVE_CREDITS_YYYY_MM_DD.zip` for 2026-09-30, 10-09, 10-13, 10-16, 10-20, 10-21, 10-22 (fetched 2026-10-23 14:57 ET; 10/22 zip sha256 prefix 4f091f1972e79d51).
