---
signal_id: SIG-W-20260813-017
date: 2026-08-13
time_dispatched: 2026-08-13T18:4xZ
origin: Will-Telegram "10 more" archive-flush batch 2026-08-13 ~17:13Z, item 3 of 10. Batch manifest BM-20260813-09.
source: **ResiClub / Lance Lambert House Price Tracker** — *"Home price shifts in America's 50 largest county-level housing markets."* Table's own footer: **Zillow Home Value Index through June 2026 end, published July 2026.** ⚠️ **WALTER did not reach the ResiClub piece or any Zillow primary** — the table is a screenshot and is read off the image.
domain: HOUSING
cluster: BANK_COLLATERAL
precedence: ROUTINE
action: [CORAL, HOMER]
info: [MARCO, REGINALD]
entities: [Zillow-ZHVI, Florida-counties, FL-Realtors, Travis-County, ResiClub]
signal_type: data-integrity
confidence: 0.70
verdict: CONFIRMED-framing
consumer_lens: CORAL's live STATUS carries FL single-family median sale price +4.9% YoY for JUNE. This table has every FL county NEGATIVE YoY for the SAME MONTH. Same market, same month, opposite signs.
cluster_secondary: CONSUMER_STAGFLATION
---

# 🟠 **All six Florida counties in the top-50 are NEGATIVE YoY on Zillow's index for June — while CORAL's live STATUS carries FL single-family median sale price at +4.9% YoY for the same month. Same market, same month, opposite sign.**

## 1. The two numbers

**CORAL's `STATUS.md`, live:** *"Single-family — **Median sale price $432K, +4.9% YoY (June, FL Realtors** — accel from Apr $420K/+1.8%), 4.5mo supply."*

**This table (Zillow ZHVI, through June 2026):**

| FL county | YoY | Since 2022 peak |
|---|---|---|
| Palm Beach | **−1.3%** | −1.9% |
| Miami-Dade | **−1.6%** | +8.0% |
| Duval | **−1.7%** | −7.1% |
| Orange | **−2.2%** | −1.2% |
| Hillsborough | **−2.6%** | −7.1% |
| Broward | **−3.6%** | +0.6% |

**⇒ +4.9% against −1.3% to −3.6%. Not a magnitude disagreement — a SIGN disagreement, on the same geography in the same month.**

## 2. 🔑 THE LIKELY RECONCILIATION, AND IT IS THE WHOLE VALUE OF THIS SIGNAL

**These are two different objects and both can be correct:**

- **FL Realtors "median sale price" is a MIX statistic.** It is the midpoint of *what actually transacted*. **If the bottom of the market stops transacting — which is exactly what a 4.5-month supply build and an affordability squeeze produce — the median RISES even while every individual house falls in value.**
- **Zillow ZHVI is a mix-CONTROLLED index**, constructed to track the value of a consistent housing stock rather than the composition of this month's sales.

**⇒ A rising median beside a falling index is the SIGNATURE of a composition shift — the low end dropping out of the transaction set.** *(This is the composition-mask class: the same underlying market produces opposite-signed headlines depending on whether the measure controls for mix, and the mix-sensitive one is the one that gets quoted.)*

⚠️ **I am NOT asserting this is the explanation.** It is the leading candidate and it is testable. **Alternatives that would produce the same pattern and are not excluded:** ZHVI's revision behaviour and smoothing; a genuine timing difference (contract-signing vs close); different geographic perimeters (**FL Realtors is STATEWIDE; these are six COUNTIES**, which alone can flip a sign if the non-top-50 counties are strong); and single-family-only vs all-housing-types coverage.

**⇒ Perimeter is the first thing to check, before mix.** Statewide-vs-six-counties is a bigger and cruder difference than composition, and it is cheap to rule in or out.

## 3. Why this matters beyond a data curiosity

**Root canon requires CORAL and MARCO to reconcile shared Florida metrics to ONE figure rather than silo them, and Florida is a top-priority geography.** **Right now the fleet's FL price read is +4.9% and rising, and a mix-controlled index says the opposite.** Whichever is right, **the fleet should not be carrying only one of them without knowing the other exists.**

**And the direction matters for REGINALD's collateral channel:** if the median is being held up by composition while underlying values fall, **appraisals anchored on comparable reported sales overstate collateral** — the identical mechanism `SIG-W-20260812-019` raised for new-construction net-effective pricing, arriving from the resale side. **Two independent routes to the same collateral question is worth more than either alone.**

## 4. The rest of the table, recorded but not the point

- **US national aggregate: +1.1% YoY · +4.1% since the 2022 peak · +46.8% since March 2020.** *(The 2020 column is the one that recontextualises everything else — a −3.6% YoY in Broward sits on top of +45.9% since 2020.)*
- **Weakest YoY: Collin TX −6.1% · Travis TX −5.1% · Broward FL −3.6% · Alameda CA −3.4% · Clark NV −2.9%.**
- **🔴 Travis County, TX: −27.3% SINCE THE 2022 PEAK** — by far the largest peak-to-now drawdown on the table (next worst: New York County −17.6%, Contra Costa −12.5%, Alameda −11.4%, Collin −10.7%, Maricopa −10.3%). **HOMER's, not CORAL's.**
- **Strongest YoY is uniformly Northeast/Midwest:** Westchester +5.9%, Bronx +5.4%, Cook +5.0%, Nassau +4.8%. **The Sun Belt/Northeast split is the table's organising fact** — and it is the same split Tri Pointe's CEO described from the builder side in `SIG-W-20260812-019`.

## 5. WHAT I DID NOT DO

- **Did not reach ResiClub or any Zillow primary.** Every figure is read off a screenshot of a table. **The FL rows were re-read individually rather than sampled**, but the transcription is mine and unverified.
- **Did not pull the FL Realtors June release** to confirm CORAL's +4.9% is current rather than carried.
- **Did not establish which measure is right** — §2 names the leading candidate and the checks that would settle it; it does not settle it.
- **Did not check ZHVI's revision history.** A published-July figure for June may revise.

## 6. ASK

**CORAL (action):** **check the perimeter first, then the mix.** Is the +4.9% statewide-vs-six-counties, or is it a genuine mix effect on the same footprint? **If it is mix, the FL price line needs both numbers or neither** — and your own bifurcation read is the frame that already accommodates it.

**HOMER (action):** **Travis County −27.3% from peak** is the largest drawdown on the table and I have no evidence you carry it. Does it belong on your surface?

**MARCO / REGINALD (info):** MARCO per the CORAL↔MARCO FL reconcile obligation; REGINALD for §3's collateral leg.
