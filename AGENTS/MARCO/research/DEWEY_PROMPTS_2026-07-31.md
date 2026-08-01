# MARCO → DEWEY — candidate deep-research prompts
**Written:** 2026-07-31 (session 20) · **Status:** proposed, Will-gated (DEWEY is Tier-2, Will-spawned)

Ranked by what would actually move MARCO's book. Each is written as a **find-and-verify** question, per DEWEY's identity rule (*"You find data; others interpret it"*) — no prompt below asks DEWEY to judge a thesis.

> **⚠️ Standing basis warning to include in ANY MARCO prompt to DEWEY.** MARCO's most productive failure class is **basis/baseline error, not bad data** — five in one session on 2026-07-31, each of which would have shipped a confident wrong mark (wrong category filter reversed a sign; cross-month comparison manufactured 30pp; median-vs-repeat-value index; insurer-side exposure substituted for a coverage gap; an effect below its instrument's dispersion). **For every figure returned, state explicitly: the UNIT, the DENOMINATOR, the GEOGRAPHY, the VINTAGE, and whether it is per-trip / per-season / per-person / per-household.** A number without its basis is not usable by MARCO regardless of source quality.

---

## PROMPT 1 — 🔴 HIGHEST VALUE: the Canadian-Florida spending base

**Why this one first:** MARCO's single biggest forward claim — the winter 2026-27 FL Canadian-$ hole, routed to REGINALD as a bank/CRE collateral input and dated in the thesis TIMELINE — rests on `~$6B annually (3.4M visitors × $1,800 avg)` with **no source or vintage on either factor**, and a 10–20% haircut that is asserted rather than computed. It is also **scope-mismatched**: derived for three counties, cited as all of Florida.

> **Question:** How much do Canadian visitors actually spend in Florida per year, and what is the defensible current figure with its basis fully stated?
>
> Find and verify, each with unit / denominator / geography / vintage:
> 1. **Canadian visitor volume to Florida** — annual, most recent available. Distinguish **overnight visitors** from **same-day/land-crossing** trips, and **seasonal residents (snowbirds, multi-week/multi-month stays)** from short-stay tourists. Visit Florida, StatCan, NTTO, and county tourist-development councils are the likely primaries.
> 2. **Average spend per Canadian visitor in Florida** — and critically, **on what basis**: per trip, per night, per party, or per season. A snowbird staying 3 months and a day-tripper cannot be averaged into one figure; if published sources do that, say so explicitly.
> 3. **County-level concentration** — how much of Canadian FL spend sits in **Broward, Palm Beach, and Lee** versus statewide. This is the specific reconciliation MARCO needs.
> 4. **Canadian-owned FL residential property** — counts and/or assessed value, ideally Broward/PB/Lee/Sarasota/Charlotte. Non-homestead and seasonal-resident property rolls are the likely route. Snowbird *owners* spend without any hotel or STR trace, so they are invisible to lodging-tax data.
> 5. **Any published estimate of Canadian-boycott $ impact on Florida specifically**, 2025–2026, with its own method stated.
>
> **Explicitly report negatives.** If per-visitor spend is not published on a defensible basis, say so — "no reliable figure exists" is a usable finding here and MARCO will retract rather than carry it.

---

## PROMPT 2 — 🟠 The realized-snowbird measurement gap

**Why:** MARCO measures Canadian travel three ways — **intent** (Google Trends), **capacity** (airline schedules), and **national return trips** (StatCan). All three are upstream proxies. MARCO has **no realized, Florida-specific, snowbird-specific measure at all**, yet the winter 2026-27 window is its most dated forward claim. This is a source-discovery question, which is DEWEY's strongest mode.

> **Question:** What data sources exist that measure the *realized presence* of Canadian seasonal residents in Florida — as opposed to travel intent, airline capacity, or national border-crossing counts?
>
> Search for and evaluate, reporting availability, cadence, lag, cost, and geographic resolution for each:
> - **Provincial out-of-country health insurance** — Ontario OHIP / Quebec RAMQ / BC MSP out-of-province absence reporting, snowbird residency-requirement filings, or travel-insurance industry data (Canadian snowbird travel-medical policy counts).
> - **Canada Revenue Agency / IRS** — Canadian filers claiming US days present; **IRS Form 8840** (Closer Connection Exception) filing counts, which is close to a direct snowbird census if published in aggregate.
> - **Florida county property rolls** — seasonal/non-homestead parcels with Canadian mailing addresses; whether any county appraiser publishes owner-address country.
> - **County tourist-development tax (TDT)** monthly series for **Broward, Palm Beach, Lee, Charlotte, Sarasota** — availability and lag.
> - **Snowbird associations and surveys** — Canadian Snowbird Association membership//survey data, Kanata/Snowbird Advisor surveys.
> - **Cross-border vehicle data** — CBP land-crossing counts by port with vehicle/passenger split, seasonal pattern.
>
> **Deliverable:** a ranked table of candidate instruments by *usability* (free vs paid, cadence, lag, FL-specific vs national). MARCO needs to know what it *could* measure, not an interpretation of the boycott.

---

## PROMPT 3 — 🟠 Channel-1 reopening: can labor scarcity be seen outside payroll surveys?

**Why:** MARCO closed Channel-1 transmission after three pre-registered nulls, concluding the **payroll-survey instrument class** is structurally unable to observe a substantially off-payroll population. That conclusion is deliberately falsifiable, and MARCO named the reopening conditions. This prompt tests one of them without MARCO re-specifying a fourth wage panel itself.

> **Question:** What published data measures **time-to-fill / vacancy duration / unfilled-position counts** in immigrant-intensive US occupations (agriculture, meatpacking, construction trades, hospitality back-of-house, home care) at monthly-or-better frequency, 2024–2026?
>
> Find and verify:
> 1. Sources for **vacancy duration by occupation** — Indeed Hiring Lab, Lightcast/Burning Glass, LinkUp, ZipRecruiter, state workforce agencies. Note which are free and what geography/occupation resolution each offers.
> 2. Any published **firm-level or industry-level labor-cost disclosure** for these sectors — earnings-call commentary, USDA cost-of-production surveys, industry association wage surveys.
> 3. **H-2A/H-2B program stress indicators other than certification counts** — processing times, denial rates, employer withdrawal, litigation.
> 4. Whether **any credible study 2025–2026** has measured immigration-enforcement wage/cost effects using data that observes undocumented or off-payroll workers directly — and what it found, including studies finding **no effect**.
>
> **⚠️ Do NOT return the Adverse Effect Wage Rate (AEWR) as evidence of scarcity.** It is an administratively-set floor, and its USDA NASS Farm Labor Survey basis was canceled in Aug 2025. Only the *spread of offered wages above* the floor is informative. **Counter-evidence is as valuable as confirming evidence here** — MARCO has publicly concluded this cannot be measured and would rather be shown wrong than agreed with.

---

## PROMPT 4 — 🟡 American emigration (VX-MARCO-EMG-01, never researched)

**Why:** A named MARCO vector that has sat WATCH/PENDING without ever being worked. It is the one population-movement direction MARCO tracks in principle and has zero evidence on.

> **Question:** Is there measurable evidence of increased US citizen emigration in 2025–2026, and what are the best available instruments?
>
> Find and verify: foreign **residency-permit issuance to US citizens** (Portugal, Spain, Mexico, Costa Rica, Canada, Ireland, Italy); **renunciation-of-citizenship** counts (Federal Register quarterly); **overseas voter registration** (FVAP); State Department passport issuance and overseas-citizen estimates; **Canadian and Mexican immigration statistics for US-origin arrivals**; moving-company and relocation-industry data. Report base rates and pre-2024 trend for each — the question is whether any *change* is distinguishable from a long-running level.

---

## PROMPT 5 — 🟡 Channel-4 fiscal terminus (the honest rebuild test)

**Why:** MARCO downgraded Channel 4 to MED-LOW on **absent** evidence, not contrary evidence — with rebuild conditions named so it can move either way. Running this is the intellectually honest follow-through.

> **Question:** What is the current fiscal condition of US border municipalities dependent on cross-border Mexican retail — specifically El Paso, Laredo, McAllen, Pharr (TX) and Nogales, Douglas (AZ)?
>
> Find and verify: **EMMA/MSRB** continuing-disclosure filings and any **rating actions** (Moody's/S&P/Fitch) 2025–2026; **Texas Comptroller** sales-tax allocations by city and **Arizona DOR** TPT collections, monthly, YoY; municipal budget deficits/surpluses as adopted vs actual; pension funded ratios where disclosed; **CBP northbound crossing counts** by port. Report each city separately — MARCO's prior frozen figures (Laredo shopper share 51%→13%, El Paso $55–62M deficit, Pharr S&P negative) are Feb-2026 vintage and **must not be used as the baseline**; re-derive from primaries.

---

## Sequencing note

**Prompt 1 is the one to run first** and is worth running alone. It is the only one attached to a live fleet-facing number that other agents consume, and it can *retract* rather than merely add — which is the higher-value outcome. Prompts 2 and 3 are instrument-discovery and can run in either order. Prompts 4 and 5 are genuine gaps but neither is load-bearing for a current claim.
