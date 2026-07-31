# PRE-REGISTRATION — Floor-Controlled Channel-1 Transmission Test

**Written:** 2026-07-31, session 19, **BEFORE pulling any outcome data.**
**Author:** MARCO
**Status at write time:** thesis v2.8 — Channel 1 has HIGH quantity evidence and **NO working price/cost transmission instrument.** Both prior candidates died 2026-07-25, hours apart.

> **Why this file exists.** On 7/25 MARCO promoted a Channel-1 instrument (FL leisure-hospitality wage divergence) into THESIS, STATUS, NEXUS_BRIEF and packets to LABOR and CARL — then falsified it hours later with a panel that had been runnable off the free BLS API the whole time. The lesson recorded that day ([[finding_run_the_falsifier_before_promoting]]) was: **run the runnable falsifier BEFORE promoting.** This document fixes the specification, the thresholds, and the pre-committed consequence in writing, before any outcome is observed. Anything I discover later that is not in this file is a new hypothesis, not a confirmation of this one.

---

## 1. The question

Does the immigration labor-supply shock (Channel 1) **transmit to wages/costs**, or is it a large, well-measured upstream quantity fact with no demonstrable downstream price effect?

Quantity evidence (NOT in question, HIGH confidence, untouched by this test):
foreign-born LF −700K YoY · LFPR 61.5% (50-yr low ex-Covid) · less-than-HS LFPR 43.1% (from 49.0% Jul'25) · H-2A certifications on a ~455-465K FY26 pace (FY26-through-Q2 = 254,688 certified, +16.9% YoY, verified from OFLC primary 7/31).

## 2. Why the previous instrument failed, precisely

FL leisure & hospitality AHE ran **+8.75% YoY vs national +3.87%** — read as immigrant-supply withdrawal bidding up wages. The 4-state panel killed it:

| Jun'26 YoY gap vs national (pp) | Leisure & Hosp | Construction |
|---|---|---|
| FL | **+4.88** | +1.02 |
| TX | **−6.45** (falling outright) | −3.22 |
| CA | −1.94 | +3.96 |
| AZ | −1.05 | −0.36 |

**FL's cell is Amendment 2**: the statutory floor stepped $13 → **$14 on Sep 30 2025** (→ $15 Sep 30 2026), a **7.7% floor rise inside the June YoY window**, in the most floor-exposed sector. TX — largest immigrant workforce exposure, most aggressive enforcement, **$7.25 since 2009** — has hospitality wages *falling*.

**The confound is structural, not incidental:** statutory floors bind hardest in low-wage sectors, and immigrant-intensive sectors *are* low-wage sectors. So floor exposure and immigrant exposure are **positively correlated**, and any naive cross-state wage comparison loads the floor effect onto the immigration coefficient. A within-state sector difference does not fix this either, if the two sectors have different floor exposure.

## 3. The design — a stratum where the floor cannot bind

**Restrict the sample to federal-minimum ($7.25, no state step) states.** In those states the floor sits at $7.25 while leisure-hospitality AHE runs roughly $16–18/hr — the floor is **non-binding by a factor of ~2.3x** and did not move at all in the observation window. Any wage movement in that stratum is therefore market-determined. This removes the confound by construction rather than adjusting for it.

Within that stratum, the test is a **difference-in-differences**:

- **Sector difference (within state):** `DID_s = YoY%ΔAHE(Leisure & Hospitality)_s − YoY%ΔAHE(Retail Trade)_s`
  Retail Trade is the control sector: comparable wage level and comparable exposure to any general low-wage labor-market tightness, but **materially lower immigrant intensity** than leisure-hospitality. It absorbs general tightness, seasonality, and state-level demand shocks.
- **Exposure difference (across states):** compare mean `DID` in **high-immigrant-share** $7.25 states vs **low-immigrant-share** $7.25 states.

If Channel 1 transmits to wages, immigrant-intensive sectors must outpace floor-matched control sectors **more** where immigrant labor supply is a larger share of the workforce.

**Window:** June 2026 vs June 2025 (12-month), BLS CES State and Area Employment, AHE all employees (data type 03). Series form `SMU{fips}00000{industry}03`; L&H = `70000000`, Retail Trade = `42000000`. National reference: `CES7000000003` / `CES4200000003`.

**State strata (fixed now, before any pull):**
- **High-immigrant $7.25 states:** TX, GA, NC, UT, OK, KS
- **Low-immigrant $7.25 states:** TN, AL, MS, KY, SC, WV, IN, LA
- **Excluded (floor stepped in window, retained only as diagnostics):** FL, CA, AZ, NY, NJ, NV, WA, CO

**FL diagnostic (not part of the primary test):** if FL's `DID` ≈ 0 while FL's *raw* L&H gap was +4.88pp, that independently **confirms the Amendment 2 explanation** — i.e. it validates that the 7/25 falsification was correct rather than merely inconclusive.

## 4. Pre-committed decision rule

Scored on the **high-immigrant $7.25 stratum**. All figures in percentage points.

**CONFIRM transmission — requires ALL THREE:**
1. Mean `DID` across high-immigrant $7.25 states **≥ +1.5pp**, AND
2. `DID > 0` in **≥ 70%** of those states (not driven by one cell), AND
3. High-immigrant mean `DID` exceeds low-immigrant mean `DID` by **≥ 1.5pp**.

**NULL / FALSIFIED — any ONE of:**
1. High-immigrant mean `DID` **< +0.5pp**, OR
2. High-vs-low stratum difference **< 0.5pp** (no dose-response in exposure), OR
3. **TX `DID` ≤ 0** — TX is the maximal-exposure natural control with a frozen floor; if the single best-powered cell points the wrong way, the mechanism is not there.

**AMBIGUOUS** (between the two): treated as **NOT CONFIRMED**. No promotion. Practically identical to NULL for downstream consumers.

**Data-quality abort:** if Retail Trade AHE is unavailable for **>40%** of the high-immigrant stratum, the primary design is underpowered — say so, fall back to the secondary test in §5, and do **not** score the primary either way.

## 5. Secondary instrument (independent) — H-2A offer premium above the AEWR floor

Newly reachable: `h2a_pull.py` was repaired 2026-07-31, so OFLC disclosure microdata is available again (16,707 certified records FY26-through-Q2).

The **Adverse Effect Wage Rate (AEWR)** is the administratively-set wage floor H-2A employers must pay. **AEWR itself is NOT usable as evidence of transmission** — it is a mandated floor set by formula, so citing a rising AEWR as proof of labor scarcity would repeat the Amendment 2 error exactly. *(Sharper still: AEWR derives from the USDA NASS Farm Labor Survey, which was **canceled Aug 2025** — so its 2026 setting basis is itself in question.)*

What **is** informative is the **spread of actual offered wages above the AEWR floor**, per state: employers paying above a binding floor are revealing scarcity. Statistic: share of certified positions offering **> state AEWR**, and the mean premium, FY26 vs FY25.

**Known data hazard, logged before running:** `WAGE_OFFER` in this file has median **$15.79** but mean **$93.64** — the field carries **mixed pay units** (hourly / weekly / monthly / piece rate). It must be filtered to hourly-unit records before any aggregation. Any result computed on the raw column is invalid. *(Also flagged: `TOTAL_WORKERS_H2A_REQUESTED` summed to exactly 262,144 = 2^18, which is suspicious enough to verify rather than cite.)*

Secondary test is **corroborative only**: it cannot by itself promote an instrument, because it covers agricultural H-2A specifically rather than the broad Channel-1 cost claim.

## 6. Pre-committed consequence — binding

From `SCRATCH.md` NEXT SESSION item 1, written 2026-07-25, **before** this session:

> *"If a floor-controlled test also comes back null, downgrade Channel 1 from spine to 'well-evidenced upstream fact, unproven downstream' (MAJOR bump) rather than hunting a third instrument."*

**This is binding.** On NULL or AMBIGUOUS:
- Thesis **v2.8 → v3.0** (MAJOR — conviction-structural change).
- Channel 1 reclassified: **quantity HIGH / transmission UNDEMONSTRATED**, and downstream consumers (CARL cost, LABOR U-3, REGINALD) told plainly that Channel-1 *transmission* claims are unsupported by MARCO.
- **No third instrument hunt.** Three failed pre-registered tests is itself the finding: it is evidence about the world, not a run of bad luck with thermometers.

On CONFIRM: promote to primary Channel-1 instrument at MEDIUM (not higher — single window, two sectors), and **name the next falsifier in the same breath**, per [[finding_run_the_falsifier_before_promoting]].

---

## AMENDMENT 1 — 2026-07-31, control sector unavailable (feasibility, not outcome)

**What happened:** the first run fired the §4 **data-quality abort** — Retail Trade AHE was missing for **100%** of every stratum. Cause verified against the API, not assumed: BLS publishes state-level AHE for **supersectors only**, and Retail Trade (`42000000`) is a *sub*-sector. The API returns `"Series does not exist for Series SMU48000004200000003"`. National retail (`CES4200000003`) exists, state retail does not. So the pre-registered control sector cannot be built at all.

**⚠️ Full disclosure of what I had already seen when writing this amendment.** The Leisure & Hospitality leg *did* return for every state, so before choosing a replacement control I had already observed the L&H column, including:
- high-immigrant $7.25 stratum raw L&H YoY: TX −2.58, GA +5.70, NC +3.14, UT +1.40, OK +1.25, KS −1.04 (**mean +1.31%**)
- low-immigrant $7.25 stratum raw L&H YoY: **mean +2.23%**
- national L&H +3.87%

That is **already pointing against transmission** (the low-immigrant stratum ran *hotter*). I cannot un-see it, so I am recording it rather than pretending the amendment was blind. **The thresholds in §4 are NOT changed** — they were set before any pull and stay exactly as written. The only change is which control series the DID is built from, and that change is forced by availability.

**Replacement control (fixed now, before computing any DID):**
- **Primary control: Trade, Transportation & Utilities (`40000000`)** — the published supersector that contains retail; lower immigrant intensity than leisure-hospitality, and it absorbs state-level demand and general low-wage tightness.
- **Robustness control: Education & Health Services (`65000000`)** — independent, large, stable, lower immigrant intensity. Reported alongside; the primary verdict is scored on TTU.

**Note on what the amendment costs:** retail was chosen as a *floor-matched* control. TTU is a worse floor match (higher wage level). **This matters less than it would elsewhere, because the whole point of the $7.25 stratum is that the floor binds for neither sector and did not move** — floor-matching was belt-and-braces on top of a stratum that already removes the confound. The real cost is a weaker immigrant-intensity *contrast* between treated and control sector, which biases the test toward **understating** a true effect. Stated plainly: this amendment makes a false NULL somewhat more likely and a false CONFIRM less likely. Weigh the verdict accordingly.

**Not attempted, and why:** Construction would be the natural high-immigrant treated sector, but state-level CES bundles it as **Mining, Logging & Construction (`15000000`)**, which is contaminated by oil & gas in TX, OK, KS, LA and WV — exactly the states carrying the test. Using it would reintroduce a confound as bad as the one this design exists to remove.

---

*Nothing below this line existed when the §4 thresholds were set. Results → `research/2026-07-31_floor_controlled_channel1_RESULTS.md`.*
