# LIQ-07 forecast and historical count clarification — October 14, 2026

Will authorized implementation of CATO's LQR-1–4 direction in the existing LIQUID session. This is a dated documentation clarification. The September25 letter, including its October1 erratum, is preserved verbatim below its new notice and in `archive/before/reports/2026-09-25_Q2_first-observation-of-spreading.md`. No registered threshold, branch, probability, window, invalidation, calendar choice or consequence is changed.

## Forecast outcome versus remaining verdict

The September25 forecast assigned **P(S1 or S2)=15%, P(S1)=5%, P(S3)=15% and P(S4)=70%**. The credit trigger occurred on **September30**, confirmed from the three September28–30 observations as first published in the October1 grade. The low-probability credit-trigger outcome therefore materialized and eliminated S3/S4. This is a forecast surprise. A useful detector firing does not validate its assigned probability; one realization cannot establish general miscalibration.

**Only the funding branch remains pending.** October16 completes its required publication frontier. The prediction ledger stays OPEN until adjudicable; the original November10 Resolve_By and all probabilities remain unchanged. Report both ICE and SOFR lists, with missing observations pending. A branch difference is AMBIGUOUS-BY-SESSION-LIST and goes to PROME. S2 establishes **no reserve-channel loop observed**; redemption pressure, collateral calls, term-credit restrictions and offshore constraints remain separate context.

## Counts with explicit units

The original paragraph mixes observation windows and grouped episodes. Its statements must not be reused interchangeably.

| Quantity | Numerator | Denominator / convention | Permitted interpretation |
|---|---:|---|---|
| Strict funding accompaniment among the original enumerated trigger dates | **2** | **7 listed trigger windows**: August6,2024; March10/April7/October14/November18,2025; February12/March16,2026. One window per listed trigger, ±10 published dates on each named list | October14 and November18,2025 both qualify on the non-quarter-end z leg. This is two qualifying windows, with correlated exposure to the same period |
| Strict accompaniment under an explicit run-reset diagnostic | **2** | **8 reconstructed trigger windows**: the seven dates above plus March28,2025. One trigger at the third consecutive qualifying observation; any failed observation resets the run to zero | Reproduces RED's extra March28 date on the saved latest-revised data. This is a diagnostic count, not a replacement ex-ante calibration |
| Grouped historical periods, matching RED's descriptive grouping | **1** | **4 named groups**: August2024; March–April2025; October–November2025; February–March2026. Count a group once if any contained trigger window qualifies | Only October–November2025 qualifies. These are explicitly named descriptive groups, not statistically established independent episodes or a newly registered clustering rule |
| Original loose “around 3 of 7” | **UNDEFINED** | Seven listed dates, but no recoverable rule for what counts as loose accompaniment, its horizon or its reset | **Do not reuse as a strict S1 rate.** February2026's $30.5B SRF use is below the registered $50B leg; October31,2025 is outside the adjacent ±10 windows |
| Ledger's historical “funding legs met 1/7” | Mixed units | One qualifying grouped period divided by seven trigger dates | **Withdrawn from quantitative reuse.** Use the explicitly named window or group count above |

The original seven-date enumeration's reset/deduplication convention was not recovered. It cannot be retroactively declared equivalent to the explicit eight-trigger diagnostic. Likewise, one grouped period cannot be divided by seven windows and called an episode rate.

## Bounded replay evidence

`historical-count-recount.py` has no network calls. It reads the previously saved October14 `evidence-full.json.gz`, forms integer-bp B/CCC changes using the frozen +28/0 conditions, and calls the unchanged dispersion instrument's pure `analyze()` on trailing, quarter-end-filtered observations. Full dated window bounds, z witnesses, maxima and input hash are in `historical-counts.json`.

| Original trigger | Eligible z ≥4 in ICE and SOFR windows | Largest SRF $B | Largest unfiltered SOFR99−IORB bp | Strict funding result |
|---|---|---:|---:|---|
| 2024-08-06 | None | 0.101 | 11 | Absent |
| 2025-03-10 | None | 0.100 | 9 | Absent |
| 2025-04-07 | None | 0.100 | 18 | Absent |
| 2025-10-14 | October15/16/27/28; z4.721/5.171/4.497/5.621 | 8.400 | 27 | Present on z |
| 2025-11-18 | November4/28 and December1 on both lists; z4.272/5.059/5.492 | 26.000 | 33 | Present on z |
| 2026-02-12 | None | 30.500 | 24 | Absent |
| 2026-03-16 | None | 9.000 | 17 | Absent |

The extra March28,2025 window has no qualifying funding leg. November3,2025 z6.970 is additionally inside the SOFR list used in this replay; it is outside ICE. RED's October1 comparison used a different SOFR date list and found November3 outside that list but inside the SOFR75∩IORB pair list. **This new capture's SOFR list differs from that earlier date inventory.** It is not silently substituted into the original erratum: November4 qualifies on all the compared lists, so the two positive windows survive. Publication-history/session-list differences remain a basis dependency.

No historical GATE079 ARM is replayed outside its current exclusion-list perimeter. Both positive windows qualify independently on z. For every negative window, even the unfiltered SOFR99−IORB maximum is below the necessary +30bp line and SRF is below $50B; hence ARM cannot change those negative classifications on these inputs.

**Vintage limits:** this is October14 latest-revised saved history, not a recovered September25 vintage. The rolling ICE history now begins October16,2023 versus October2 in the original reference sample; earliest lost observations are not reconstructed. No claim is made that the original 12%, 29.6%, broadening frequencies or probability estimates have been revalidated. A general recalibration remains outside this bounded documentation repair.

Sources: original LIQ-07 letter §3; October1 trigger grade; RED's October1 critique and z/basis concession; saved October14 raw evidence. These have distinct vintages and counting bases.
