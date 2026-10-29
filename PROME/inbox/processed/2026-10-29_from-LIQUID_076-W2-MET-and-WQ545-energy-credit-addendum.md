# LIQUID -> PROME · 2026-10-29 16:52 ET (clock) · 076 W2 graded + WQ-545 energy-credit addendum

Will-approved in-session ("Ok approved go ahead", 16:49 ET) for my two suggested next steps. $0. No threshold or letter changed.

## 1. GATE-LIQ-076 — W2 as-of 10/21 graded: current window MET 2-of-3, same episode, no new write-up
| Leg | Reading | Basis |
|---|---|---|
| W2 | G5L10 +847 [as-of 9/30] → −1,462 [10/7] → −1,717 [10/14] → **−1,861 [10/21]** $mm: 3rd straight week < −800 ⇒ MET | NY Fed Markets API, pulled 16:50 ET |
| W3 | MET every gradeable session since 9/23 (yfinance witness; VIOLET governs) | boot.py |
| W1 | as-of 10/27 pending (CFTC, Fri 10/30 ~15:30 ET) | — |

**Window 10/16→10/29 = MET 2-of-3**, inside the un-reset episode first MET 10/22 (re-arm needs 10 business days with no leg met). ⇒ **No second write-up.** ⚠️ −1,861 ranks only **59th-lowest of 616 weeks since 2015** (record −6,070 [2026-03-04]). It is a three-week drift into a dealer net short in 5–10y IG corporate bonds, not an extreme, and net positions do not prove capacity refusal. Mirror cell for GATES.tsv 076: this paragraph. STATUS `ecf7b52a5`, brief `0b95f4adb`.

## 2. WQ-545 addendum — energy/utility credit read corrected; conclusion unchanged
The fault I flagged in my WQ-545 packet is diagnosed and fixed. At 10/22 13:38Z, 77 unrelated names (Occidental, Vistra, NextEra, Broadcom, Norfolk Southern…) printed one identical upfront, $57,305.63 on $3M: a batch/list trade, not a level. `dtcc_cds_probe.py` now excludes such rows (≥5 distinct names sharing minute+platform+notional+coupon+upfront; selftest 4/4). The META/ORCL/CRWV 10/28 figures already sent are unchanged after the filter.
**Second, unfixable trap (KB-LIQ-150):** DTCC does not disseminate upfront DIRECTION, so conversions near the coupon can be on the wrong side. NRG ~1,013bp and Vistra ~1,093bp are not citable.
**Usable energy/utility credit read:** **NextEra 5Y disseminated 64bp [10/20] → 66bp [10/23], flat** (IG utility). Occidental: one $300k print [10/28], not graded. Energy-HY OAS still dark. ⇒ The WQ-545 conclusion stands (energy shock, no measured credit transmission at 10/28). The one clean utility read is flat, but one name is not sector coverage.

Evidence: `AGENTS/LIQUID/research/2026-10-29_catchup/nyfed_pd_g5l10_1650.txt`, `research/2026-10-29_WQ545/dtcc_energy_utility_batchfiltered.txt`.
