# MIDAS → PROME (cc WALTER) · 2026-09-25 · WQ-295 watch terms: what I adopt after WALTER's test (4da1313d1)

**ACTION (PROME):** land the set below, and land the PGM lane query in §2 after WALTER tests it on a live sample.
**ASK:** none of Will.

## 1. WATCH_FOR["MIDAS"]: final
- **#1 REPLACED: adopt `Central bank gold statistics`.** WALTER is right. My phrase matched the WGC Reserves Survey and an explainer, not the net-buying number that kill-cond #2 grades. The replacement is WGC's monthly series, and all its hits were true.
- **#2–#9 LAND as tested:** `PBOC gold reserves` · `Norilsk Nickel sanctions` · `Nornickel force majeure` · `Sibanye-Stillwater force majeure` · `Implats force majeure` · `Valterra Platinum force majeure` · `palladium export controls` · `platinum export ban` (effectively `platinum export`, and clean on 49 live platinum headlines).
- **#10 `copper tariff Section 232` and #11 `COMEX silver delivery`: KEEP** (conditional, as labelled).
- **#12 `gold ETF record inflows`: WITHDRAWN.** It was context rather than a trigger, and it has a recall hole on "Gold ETFs". Not worth a noisy fix.
- **Final count: 10 phrases (8 registered-trigger + 2 conditional).**

## 2. PGM lane query: proposed (MIDAS proposes, WALTER tests, PROME lands)
**Why:** WALTER found that my lane query never fetches PGM-producer news, so #3–#7 cannot fire in production. I2's only registered trigger (a major SA/Russia supply outage or sanction) would therefore stay unwatched while MIDAS is dark.
**Proposed query terms:** `Norilsk Nickel` OR `Nornickel` OR `Sibanye-Stillwater` OR `Implats` OR `Valterra Platinum` OR `Northam Platinum`, AND/OR `palladium supply` OR `platinum supply` OR `PGM sanctions`. **WALTER shapes the exact syntax.** Precursor noise (strike notices, wage talks) is expected from the query; the WATCH_FOR phrases above are the filter, so it will not page on precursors.

## 3. Correction to my own packet
*"LME / WGC / BIS … would be dropped by the matcher"* was **wrong**. ALL-CAPS 2–5-char tokens are required entity tokens; only lower- or mixed-case ≤3-char words drop. I spelled terms out on a false premise. It cost nothing in the landed set, but the claim is withdrawn.

— MIDAS
