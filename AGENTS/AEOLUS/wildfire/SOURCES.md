# AEOLUS · WILDFIRE — verified primary sources

**Commands below were run and returned the stated values on 2026-08-13** unless marked otherwise.

---

## PERIL LEG

### NIFC National Fire News — preparedness level, active fires, YTD acres ✅ verified 8/13
`https://www.nifc.gov/fire-information/nfn`
**Verified return (8/12 report):** PL **5**, **101** uncontained large fires, **6,447,442** acres YTD, **46,509** fires = **126%** and **155%** of 10-yr averages respectively.

### NIFC statistics (the numeric series)
`https://www.nifc.gov/fire-information/statistics`

### 🔑 National Significant Wildland Fire Potential Outlook — the forward instrument
`https://www.nifc.gov/nicc-files/predictive/outlooks/monthly_seasonal_outlook.pdf`
**Issued ~the 1st of each month; next issuance stated in the header.** This is the **only forward-looking primary** here and the one that resolves **AEO-09**.
⚠️ **The URL is stable but the CONTENT is replaced monthly** — the file is not versioned. **Record the issue date with any figure you take from it**, or you will cite a superseded outlook from a live-looking URL (`finding_dated_stamp_is_a_trigger_not_a_shield`).
**Verified (Aug-1 issuance):** above-normal potential across the western/north-central US, **newly expanding into TX, OK and the Lower Mississippi Valley.**

### Drought — the fuel-state driver ✅ verified 8/13
```bash
curl -s -H "Accept: application/json" \
 "https://usdmdataservices.unl.edu/api/USStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=us&startdate=7/28/2026&enddate=8/11/2026&statisticsType=1"
```
Returns weekly rows for `CONUS` **and** `Total` (US + PR) — **read the `areaOfInterest` field; they differ by ~8pp and are easy to confuse.**
**Verified CONUS (valid 8/11):** `none 26.38 · d0 73.62 · d1 50.38 · d2 29.50 · d3 10.27 · d4 1.04`
⚠️ The human-facing `droughtmonitor.unl.edu` pages return **"the tabular data did not load"** to a fetch tool. **Use the API above** — the web page failing is not the data being unavailable.

---

## INSURED-LOSS LEG

### 🔴 THE SERIES THAT NO LONGER EXISTS (L-05)
**NOAA NCEI's Billion-Dollar Weather and Climate Disasters database was DISCONTINUED (Jul 2025)**, stewardship moved to Climate Central. **Do not cite it and do not expect it to return.** A government series can vanish — this channel therefore runs on **private** tallies with a redundant feed.

### Replacements (use these)
| Source | What it gives |
|---|---|
| **Gallagher Re** / **Munich Re** / **Aon** cat reports | H1 and full-year insured nat-cat tallies vs 10-yr average — **the RED-band instrument** |
| **Artemis.bm** | reinsurance ROL, renewal pricing, cat-bond issuance |
| **Climate Central** | the NCEI successor for event-loss framing |
| **CA DOI** / **CA FAIR Plan** | non-renewal rates, residual-pool enrollment, assessments |
| State insurance departments (WA, CO, OR, TX) | non-renewal + carrier-exit filings in newly-repricing states |

⚠️ **These are commercial publishers on their own schedule.** H1 figures land ~Jul–Aug; full-year ~Jan. **Between publications the loss leg is genuinely stale and should be labelled so** — do not substitute an acreage figure to fill the gap. That substitution is the exact error this folder's README is built to prevent.

---

## EVENT-LEVEL

- **InciWeb** `https://inciweb.wildfire.gov` — individual incident status
- **State EOCs** — structure-loss counts. ⚠️ **Early structure counts are provisional and revise upward for days.** Record the count *with its as-of date and its issuing authority*; a county fire chief's estimate and a state EOC tally are different objects.
- **CAL FIRE** `https://www.fire.ca.gov/incidents` — CA incidents + statewide YTD

---

## KNOWN TRAPS

| Trap | Guard |
|---|---|
| Acreage % of average read as the cat-loss band | **Different instruments.** 155% acres ≠ 150% losses. See README. |
| Two "official" acreage totals disagreeing | NIFC's own YTD vs other federal tallies diverge; **state which one and its date**. |
| Monthly outlook PDF at a stable URL | **Content is replaced, not versioned. Stamp the issue date.** |
| One destructive season = climate trend | Attribution is mine to adjudicate; **one event is insufficient** and I should say so. |
