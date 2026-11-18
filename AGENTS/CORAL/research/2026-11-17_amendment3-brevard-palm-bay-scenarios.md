# Amendment 3: three-scenario projection for Brevard County and Palm Bay

**CORAL, 2026-11-17 (Tue) 21:4x ET.** Will's ask, direct: "build the three-scenario projection for Brevard and Palm Bay". Companion to `2026-11-17_amendment3-and-floods-impact.md`. Model: `2026-11-17_a3_brevard_scenarios_model.py` (reproducible from the DOR roll file named below).

## Bottom line

- **Fees allowed (A):** both governments refill the gap with a flat assessment on every improved parcel: about $505 a year in Palm Bay and about $226 for the county. About a third of homesteaders end up paying more in new fees than they save on tax. Non-homestead owners pay the whole charge with nothing to offset it.
- **Fee ban, millage only (B):** Brevard County refills by raising its general-fund rate from 2.86 to 4.17 mills, which stays under the cap. **Palm Bay cannot.** Holding revenue would take 11.27 mills against the 10-mill constitutional cap, so from FY28-29 its property tax falls about **$7.8M a year short (11% of its operating levy)**, a gap to close by cuts or other revenue (its whole general fund was not read). Non-homestead owners carry 93% of what the higher rate collects.
- **State backfill (C):** both are made whole, but a backfill paid for statewide costs Brevard and Palm Bay residents more than they receive. Their loss per resident ($404 and $295) is below the state average ($499), because their homes are cheaper.
- **Palm Bay is the only place where any scenario leaves a property-tax gap, and the deciding variable is the fee ban.** That ban is the Governor's proposal, not law, with no bill text. The city just flooded, and its general fund pays the response.
- ⚠️ **Correction:** Palm Bay loses about **40–45% of its property-tax base, not "about two-thirds" (66%)** as CORAL wrote earlier tonight from a press figure. Basis is below.

## Data and method

| Input | Value | Source (date) |
|---|---|---|
| Parcel roll | Brevard 2026 final NAL, 351,104 parcels, ASMNT_YR 2026 | FL DOR PTO data portal, `NAL/2026F/Brevard 15 Final NAL 2026.zip` (file dated 10/06/2026; fetched 11/17) PRIMARY |
| Palm Bay parcels | 83,874 (taxing-authority codes 54U0, 34U0; city millage 7.6993 incl. voted debt) | DOR 2025 Brevard TACD workbook PRIMARY |
| Millage, FY2025-26 | Palm Bay operating 6.7000 (levy $69,651,929); Brevard County general fund 2.8643 ($209,300,409) | DOR Table 1 "Comparison of Taxes Levied" FY2024-25 and 2025-26, Brevard PRIMARY |
| Amendment terms | Non-school homestead exemption $150,000 (2027 roll), $250,000 (2028 roll), CPI after; first $25,000 becomes school-only; non-homestead growth cap 10% → 5%; self-executing | REC impact sheet, adopted 7/10/2026, pp. 681–684 PRIMARY |
| REC figures | Palm Bay −$22.06M FY27-28 · −$35.66M FY28-29 · −$44.46M FY31-32; Brevard BCC −$67.62M · −$116.30M · −$146.79M | REC 7/10 Addendum 1 PRIMARY |
| Population, 4/1/2026 | Florida 23,726,080; Brevard 674,642; Palm Bay 150,918 | EDR/BEBR 2026 estimates PRIMARY |
| General revenue | FY2025-26 collections beat estimate by $869.6M = 1.7%, so about $52B | EDR GR Conference summary 8/14/2026 PRIMARY (total derived) |

**Method.** Each homestead parcel's new non-school taxable value is max(0, non-school assessed value − other exemptions − $250,000). Other exemptions are the parcel's current exemptions minus the two homestead fields (EXMPT_01 and EXMPT_02). Non-homestead parcels are unchanged on a static roll. Rates are held at 2025 levels, as the REC did. Scenarios use the 2028 roll year, the first at the full exemption, on today's values.

**Check against the REC:** at Palm Bay's total city rate the model gives −$21.3M at the 2027 step (REC −$22.1M) and −$32.4M at the full step (REC FY28-29 −$35.7M). The model runs 4–9% low because it leaves out value growth and the 5% cap. Treat model dollars as slightly conservative.

## Palm Bay: who gets what

| | Value |
|---|---|
| Homesteads | 37,911 (45.2% of parcels); median non-school assessed value $165,040 |
| Non-school taxable base | $10.40B → **$6.18B (−40.5%)** at the full step; $7.63B (−26.6%) at the 2027 step |
| City operating gap | $18.5M at the 2027 step → **$28.2M** at the full step (static) |
| Homesteads paying no non-school tax at all, from 2028 | **77.5%** |
| Median homestead saving, all non-school levies (11.7569 mills) | **$1,301 a year** (p25 $500, p75 $2,245); city operating levy alone $741 |
| Vacant parcels | 30.2% of parcels (24,091 vacant residential lots, median taxable $10,500) |

**On the 66% figure:** the model gives 40.5% of the base on today's values. The REC's own FY28-29 loss ($35.7M) divided by today's total city levy ($80.05M) gives 45%. The press figure (The Palm Bayer, 8/01) appears to set the FY31-32 loss against the FY25-26 levy, which mixes years. That is INFERENCE: how it was computed was not read.

## The three scenarios (full step, FY28-29 onward, static)

| | **A. Fees allowed** | **B. Fee ban; millage only** | **C. State backfill** |
|---|---|---|---|
| **How the gap is filled** | Flat per-parcel assessment (fire, stormwater and similar) on improved, non-exempt parcels | Rate raised on the smaller base, up to the 10-mill cap; any remainder is cut | State transfer funded statewide (sales tax or general revenue) |
| **Palm Bay city** | **$505/parcel/yr** on 55,919 parcels ($351 if all 80,500 non-exempt parcels incl. vacant lots pay) | Needs **11.27 mills** (from 6.70); cap 10.00 → **$7.8M/yr property-tax shortfall** (11% of operating levy), to close by cuts or other revenue. FY27-28 step needs 9.13 mills, under the cap, so the cap binds from FY28-29 | Made whole for $28–36M/yr |
| **Brevard County general fund** | **$226/parcel/yr** on 278,545 parcels | Needs **4.17 mills** (from 2.86, +45%); under the cap; no cut | Made whole |
| **Homesteaders** | Pay 68% of the Palm Bay fee (62% county). **39% of Palm Bay homesteaders pay more in fee than they save on city tax**; median net city saving $236, down from $741. County: 31% worse off | Keep nearly all the saving: Palm Bay median $726 of $741 (77.5% pay no non-school tax, so a higher rate cannot reach them) | Keep the full saving ($1,301 median); pay any added sales tax |
| **Non-homestead owners** (landlords, snowbirds, most condo investors, businesses) | Pay the full fee with no offset: about +$505 city and +$226 county | Carry **93%** of Palm Bay's new base and **80%** of the county's. Median non-homestead single-family: **+$796/yr** city tax (taxable $241,305) and +$329/yr county (taxable $252,700); non-homestead condo +$214/yr county | Pay any added sales tax only |
| **Visitors** | Nothing | Nothing (hotels and short-term rentals are non-homestead, so through rents) | Pay part of any sales tax |
| **Credit read** | Revenue held; political cost on homesteaders | **Palm Bay: a structural property-tax gap in the city that pays the flood response** (cuts or other revenue). County: revenue held. No default implication established | Revenue held; state budget absorbs it |

**Scenario C detail.** Full statewide backfill = $11.83B a year by FY31-32, about **23% of state general revenue** (FY25-26 about $52B, derived). Loss per resident at FY31-32: statewide $499, Brevard all governments $404 ($272.4M / 674,642), Palm Bay $295 ($44.46M / 150,918).
- If the cost were shared per head, Brevard residents would pay about $337M against $272M received (**net about −$64M a year**). Palm Bay residents would pay about $75M against $44M (**net about −$31M a year**).
- Per head is a proxy. Sales tax is not paid per head: visitors carry part of it, and lower-income places spend less. Both points shrink the outflow.
- The direction holds unless Palm Bay's per-resident sales-tax contribution is below about 59% of the state average.
- **Variant C2 (targeted pool):** the Governor described money for rural, low-tax-base areas. Palm Bay is a city of 150,918 where one mill raises $10.4M, so it likely does not qualify as described (INFERENCE). The pool is unsized.

## What these numbers are not

1. **Not a forecast of what councils will do.** Real outcomes mix the three, and service cuts are possible in every scenario.
2. **Property tax only.** Palm Bay's whole general fund (sales-tax share, utility taxes, franchise fees) was not read, so 11% of the operating levy is a smaller share of the general fund. The size of that share is NOT READ.
3. **A flat per-parcel fee is a simplification.** Florida assessments must meet special-benefit and fair-apportionment tests (case law as summarized, not re-read). Real fees are tiered by use or units.
4. **Static roll.** It leaves out value growth, the 5% cap (which shrinks the non-homestead base over time and makes B harder), portability, new construction, and the newcomers' $50,000 tier (which shrinks the gap).
5. **Debt service is not modelled.** Palm Bay's voted debt rate (7.6993 − 6.7000 = 0.9993 mills) is commonly set to meet debt service on whatever base is left (as summarized, not re-read), which would add to non-homestead bills in every scenario. The amendment permits debt-service spending; that does not show any bond is protected. No default implication is established here.
6. **The amendment's new spending categories** for county and city property-tax revenue (Section 9) list stormwater control and flood control among allowed uses (Florida Stormwater Association statement 8/26, PRIMARY-adjacent). The full list was not read.
7. **FY2026-27 rates** (adopted September 2026) were not read; 2025 rates used, as the REC did.

## What would change this

| Trigger | Date | Moves |
|---|---|---|
| Special session or regular-session bill text: fee ban yes/no, state pool size and eligibility | Before 1/5/2027 or from 3/2/2027 | Picks A, B or C. **The fee ban is the Palm Bay switch** |
| Palm Bay and Brevard budget workshops, FY27-28 proposed budgets and TRIM millage | Any time to Sep 2027 | Direct observation; earlier than adoption |
| Palm Bay and county new-assessment votes (fire, stormwater) | Any council agenda | A in motion |
| Rating or outlook action, or borrowing terms, on Palm Bay or Brevard | Any | One possible observation, not a necessary first one |

**Inference audit (13a).**
1. Rival to "B forces Palm Bay cuts": Palm Bay could hold revenue through non-property-tax sources. Not refuted, because the general fund was not read; that is why the shortfall is stated against the operating levy only.
2. Refuter: an adopted FY28-29 Palm Bay millage at or under 10 with no service cuts, and no new assessments or state aid. That would mean other revenue filled it.
3. Confounds that make the gap smaller: the newcomers' $50,000 tier and new construction. Confounds that make it larger: the 5% cap and the voted-debt reset.
4. The model reproduces the REC within 4–9%, with the model below the REC.
5. No peer has read this.

**Scores:** no CORAL colour, gate, grade or thesis line moves. Trade line (WQ-696): **NO CARD.** The finding is about local credit in one Florida city; the fleet holds no instrument on Palm Bay or Brevard debt, and Florida muni spreads remain unreached.
