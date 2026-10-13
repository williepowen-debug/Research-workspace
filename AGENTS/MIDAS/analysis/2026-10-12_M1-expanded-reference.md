# MIDAS — expanded M1 conditional reference

October12,2026 · Will-approved maintenance · design `041cfdfb5` committed before calculation23:28:43UTC. The sample start, same October8 endpoint,120-pair regression,20-new-pair horizon,−0.08 flip and original grid phase were fixed in the approved plan. No alternate grid or horizon was tried.

There are **4186 paired ending dates, January5,2010–October8,2026**. The old690 pairs reproduce to floating-point precision (max return difference4.45e−14, yield-change difference0). Original four2024+ grid episodes are preserved. Expanded anchors are the original phase plus integer multiples of141, backwards and forwards, with full raw-level supports disjoint.

| Reference | Eligible below-flip starts | Persistence A | Endpoint flip B | B frequency |
|---|---:|---:|---:|---:|
| All overlapping horizons | 1578 | 1334 | 244 | 15.46% |
| Fixed nested disjoint-input grid | 9 | 7 | 2 | 22.22% |

The complete reference has4047 overlapping anchors and28 grid episodes. The19 grid episodes starting at/above the flip include16 ending at/above. **All nine eligible grid starts occur in2012–2021; none occurs after2022.** More raw data closes the old zero-eligible-sample gap, while leaving the relevant current-regime comparison thin. Nine disjoint inputs do not prove nine independent macro regimes. Rolling120/20 retains100 observations, so apparatus persistence remains a separate influence.

ALFRED's single whole-window attempt exceeded its2000-vintage cap. The three predeclared blocks supplied first-published records:4194 of4195 used yield-level dates have numeric first values, all equal to the latest snapshot. **2020-08-19's first record is nonnumeric**, released2020-08-21 and ending2020-08-24. This is an access/completeness exception, not a claim of zero yield or an imputed value. First-per-observation vintages do not recreate the latest-carried120-row snapshots at every historic resolving date; GLD is one later Yahoo capture.

**Disposition:** reference calculation DONE; draft probability UNASSIGNED and live registration withheld. The grid result is a historical frequency, not a22.22% forward forecast. Review regime comparability and resolving-vintage evidence onOctober19. Do not shift the phase or reanchor a future ineligible start. No held-position beta was refreshed; no score, frozen forecast, capital action or persistent monitor follows from this calculation.

Recompute from `sources/2026-10-12_m1-expanded/`: raw inputs/capture hashes, pairs, every anchor, disjoint episodes, `reference.json` and the static one-off `calculation.md`. Original `ad1c2f443` design and `c6512626c` result remain historical evidence. [FRED DFII10](https://fred.stlouisfed.org/series/DFII10) supplies the yield; Yahoo GLD raw Close supplies the fund return.
