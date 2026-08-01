# BANXICO STATE REVERSE-MAPPING — US-State Implied Remittance Senders

**Author:** MARCO (data-infra session, 2026-04-21)
**Script:** `AGENTS/MARCO/tools/banxico_reverse.py`
**Outputs:** `baselines/banxico_destination_states.tsv`, `baselines/us_state_sender_implied.tsv`
**Data through:** Q4 2025 (Banxico CE100, published quarterly; Q1 2026 not yet released)
**Confidence:** Medium — method sound; sender-ratio vintage 2018-2022 is stale, likely adds ±10-15% error on rank order, larger on magnitudes.

---

## VERDICT

**Three US states with sharpest implied sender decline 2024 → 2025:**

| Rank | State | 2024 ($M) | 2025 ($M) | Drop | % Drop |
|------|-------|-----------|-----------|------|--------|
| 1 | **Arizona** | 2,395 | 2,249 | -146 | **-6.1%** |
| 2 | **Texas** | 11,438 | 10,778 | -659 | **-5.8%** |
| 3 | **Michigan** | 973 | 919 | -54 | **-5.6%** |

The next-sharpest decliners are Colorado (-5.5%), Minnesota (-5.4%), Georgia (-5.1%), Wisconsin (-5.1%), Indiana (-5.0%). California is the *least* severe among large-volume corridors (-3.5%), making CA the laggard in signal, not the leader.

**What this means for SDL-01 geographic targeting:** MARCO's self-deportation workforce-analysis focus should prioritize:
1. **AZ** — Phoenix / Yuma / Tucson MSAs — ag + construction, heavy Sonora/Sinaloa/Chihuahua migrant base, aligning with ICE enforcement posture in the Southwest.
2. **TX** — Houston / DFW / RGV / San Antonio — northern-Mexico migrant corridor (Tamaulipas, NL, Coahuila, Chihuahua) is collapsing fastest on the Banxico side; border/construction labor withdrawal.
3. **MI / MN / WI / IN / GA** — Midwest meatpacking + poultry belt. Second-tier by volume, but the YoY decline cluster is unusually tight at ~5%, consistent with enforcement concentration at processing plants (Greeley, Postville-style) rather than random.

**Underweight vs. narrative:** California, despite hosting 36% of US Mexican migrants, shows the smallest decline (-3.5%). This is because CA's migrant mix tilts to **indigenous/southern-Mexican origins** (Oaxaca +2.2%, Guerrero +3.3%, Yucatán +1.8%, Puebla +1.7% YoY) whose remittance channels held up. The pain is concentrated in **industrial/urban-origin corridors** (Edomex -20%, CDMX -17%, Sinaloa -17%, Sonora -14%) that over-index to TX / AZ / Midwest. This is a non-obvious inversion of the simplistic "CA Central Valley = primary SDL-01 exposure" prior.

---

## TOP 10 US STATES BY IMPLIED SENDER VOLUME — 2019 BASELINE

| Rank | US State | 2019 Implied ($M) | % of US total |
|------|----------|-------------------|---------------|
| 1 | California | 13,124 | 35.2% |
| 2 | Texas | 6,732 | 18.1% |
| 3 | Illinois | 2,963 | 8.0% |
| 4 | New York | 1,809 | 4.9% |
| 5 | Arizona | 1,494 | 4.0% |
| 6 | Florida | 990 | 2.7% |
| 7 | Colorado | 955 | 2.6% |
| 8 | North Carolina | 948 | 2.5% |
| 9 | Georgia | 931 | 2.5% |
| 10 | Washington | 890 | 2.4% |

The CA + TX + IL triad was 61% of national senders in 2019. By 2025 that share compressed to 60% as TX bled fastest in % terms while CA held firmer on indigenous/southern-Mexican flow resilience.

---

## TOP 10 US STATES BY IMPLIED DECLINE — 2024 vs 2025

| Rank | US State | 2024 ($M) | 2025 ($M) | Δ% | Δ$M |
|------|----------|-----------|-----------|------|------|
| 1 | Arizona | 2,395 | 2,249 | -6.10% | -146 |
| 2 | Texas | 11,438 | 10,778 | -5.76% | -659 |
| 3 | Michigan | 973 | 919 | -5.59% | -54 |
| 4 | Colorado | 1,655 | 1,565 | -5.45% | -90 |
| 5 | Minnesota | 956 | 904 | -5.36% | -51 |
| 6 | Georgia | 1,680 | 1,595 | -5.06% | -85 |
| 7 | Wisconsin | 1,150 | 1,092 | -5.06% | -58 |
| 8 | Indiana | 1,465 | 1,392 | -4.97% | -73 |
| 9 | New Mexico | 786 | 749 | -4.74% | -37 |
| 10 | Florida | 1,920 | 1,830 | -4.72% | -91 |

**Absolute-dollar view:** CA -$797M is the largest dollar drop despite the smallest percentage drop, simply because it's the largest base. TX -$659M is the second-largest absolute drop AND second-largest % drop — the clearest structural-decline signal.

**Q1-vs-Q4 2025 trajectory check:** Comparing Q1 2025 (Ene-Mar) to Q4 2025 (Oct-Dic) quarterly runs, the pace of YoY decline is **decelerating into late 2025** (-2.4% nationally in Q4 vs deeper drops earlier). This aligns with: (a) Q1 2025 captured initial self-deportation rush, (b) the population that stayed is proportionally more structurally rooted (bank accounts, documented, digital channels), (c) the 1% remittance tax effective Jan 2026 pulled Q4 2025 flows forward, muddying the Q4 print.

---

## METHODOLOGY

**Destination data (rigorous):**
- **Source:** Banco de México, SIE table CE100 — *Ingresos por remesas, distribución por entidad federativa*, quarterly, $USD millions, January 2019 through Q4 2025 (28 quarters).
- **URL:** `banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?idCuadro=CE100` with `fechaInicio` / `fechaFin` passed as ms-epoch timestamps and `formatoXLS.x=1`.
- **Series-level IDs:** SE29670 (Aguascalientes) through SE29702 (national total), sequential with the alphabetical state listing. Preserved here for future API upgrade once a Banxico `Bmx-Token` is provisioned.

**Sender-ratio matrix (approximate):**
Per Mexican state, the fraction of its migrants residing in each tracked US state. Rows normalized to sum to 1.0. Anchors:

1. **Migration Policy Institute, "Mexican Immigrants in the United States" (2024 article, 2018-22 ACS pooled):**
   CA 36%, TX 22%, IL ~6%, AZ ~5%, FL/WA/GA/NV/NC/NY ~13% combined.
   <https://www.migrationpolicy.org/article/mexican-immigrants-united-states>
2. **Batiz-Lazo & González-Correa (2022), "The Journey of a Remittance in the US-Mexico Corridor":** confirms 95% of Mexican remittance inflows originate US, California most-concentrated destination, industrial-ag tilt.
   <https://mpra.ub.uni-muenchen.de/114233/1/MPRA_paper_114233.pdf>
3. **Hometown Associations (Wilson Center / Rivera-Salgado et al.):** Zacatecas → IL + CA cluster, Jalisco/Michoacán/Guanajuato federations concentrated in LA + Chicago, Oaxaqueño networks overwhelmingly CA-based.
4. **Origin-destination heuristics:** border-state Mexican migrants (Tamaulipas, NL, Coahuila, Chihuahua) over-index TX; Sonora and BC over-index AZ/CA; Pacific-south states (Oaxaca, Guerrero, Yucatán) CA-heavy with NY secondary for Puebla/Hidalgo.

**Reverse-map computation:**
For each quarter `t`, implied US-state sender flow:
  `implied[us_state, t] = Σ_{mx_state} remittance[mx_state, t] × ratio[mx_state, us_state]`

Mass is conserved: `Σ implied = Σ destination` for every quarter (verified to 0.00% error in sanity-check output).

**Coverage:** 19 US buckets — CA, TX, IL, AZ, FL, WA, GA, NV, NC, NY, CO, OR, NM, UT, MI, MN, IN, WI, plus "OTHER" absorbing ~6% into states not explicitly tracked (PA, NJ, MA, TN, VA, OK, KS, etc.).

---

## CROSS-REFERENCE TO MARCO THESIS

| Reported ICE enforcement concentration | Banxico reverse signal | Align? |
|-----------------------------------------|------------------------|--------|
| CA Central Valley (ag) | CA -3.5%, Oaxaca/Guerrero (CA-concentrated) flat-to-positive | **Mixed** — ag workforce persisting on remittance channel |
| TX RGV / Houston construction | TX -5.8%, Tamaulipas -4.3%, NL -12.9% | **Confirmed** — Northern-MX origin collapse maps to TX |
| AZ Phoenix ag + construction | AZ -6.1%, Sonora -14%, Sinaloa -17% | **Strongly confirmed** — top signal state |
| MN meatpacking (JBS, Hormel) | MN -5.4%, MX-state mix typical | **Confirmed** — cluster with WI/IN/MI |
| WA farms (tree fruit, dairy) | WA -4.4% | **Weak** — below national average decline; indigenous-heavy workforce matches persistence pattern |

Bottom line: the Banxico reverse signal **validates TX and AZ as primary SDL-01 geographic stress vectors**, partially validates Midwest meatpacking, and *contradicts* the naive "CA Central Valley is the epicenter" framing. The CA picture is more nuanced — absolute-dollar pain is real (-$797M) but the % decline is below national.

---

## LIMITATIONS

1. **Sender ratios are stale.** Vintage 2018-2022 ACS / ENADID 2018 estimates. Interior US states (NC, GA) have grown their Mexican-born populations faster than the frontier anchors reflect. Likely understates NC/GA/TN drops, overstates CA/TX.
2. **No direct state-to-state remittance data exists publicly.** Banxico publishes destination only; the new academic reconstruction (Springer, *Quality & Quantity* 2025, DOI 10.1007/s11135-025-02239-y) offers a more rigorous ENADID-based matrix — future work should integrate it.
3. **1% remittance tax (effective Jan 2026)** creates three signal distortions: (a) Q4 2025 pull-forward, (b) Q1 2026 pothole (when data lands), (c) informal-channel substitution that evades Banxico measurement. The tax compresses this tool's forward usefulness until ~Q3 2026 when behavior stabilizes.
4. **Digital-shift effect.** Fintechs (Remitly, Wise) route through correspondent banks that may misattribute originating US state if the sender's bank HQ differs from residence. Banxico tags by "country of origin" on the wire leg, not user residence. Residual bias unknown.
5. **Mexican-state-composition confound.** The reverse-map assumes each Mexican state's US-residence distribution is static. If migrants from Oaxaca disproportionately self-deported (hypothesis not tested), the ratio matrix itself is shifting underneath us — meaning current implied flows over-attribute to CA.
6. **BC outlier:** Baja California +22% YoY is almost certainly **northern-border return-migrant** dynamics (money moving toward, not from, the US-side economy) and/or FX/tourism. Treat as non-informative for SDL-01.
7. **Granularity:** state-level only; MSA-level reverse-mapping would need Mexican-municipality Banxico data (available in CE81 / CA79 analytics table but not integrated here).

---

## NEXT STEPS FOR MARCO

- **CARL cross-signal:** TX + AZ + MI + MN + GA consumer credit deterioration should be cross-referenced against the implied sender decline — if CARL already sees subprime auto / credit-card distress clustered here, SDL-01 is the compounding factor and should be noted in the CARL-REGINALD transmission chain.
- **REGINALD CRE signal:** small-business and multifamily CRE in **Phoenix, Houston, DFW, San Antonio, Atlanta, Twin Cities, Milwaukee** is where ICE-driven workforce withdrawal most directly compounds existing office/condo distress.
- **~~2.2M~~ self-deport figure cross-check** ⚠️ *(annotated 2026-07-31: the 2.2M target of this cross-check is **RETRACTED** — a disputed DHS claim mis-attributed to CBO, corrected fleet-wide 7/2, thesis v2.6. Accurate magnitude: **~1.0M realized foreign-born LF decline / ~1.5M population**.* 🔎 **Note what this paragraph's own arithmetic was saying:** its independently-derived **~625K fewer senders** was never consistent with 2.2M — it points squarely at the corrected ~1.0M figure and was doing so from **2026-04**, three months before the fleet correction. **The cross-check ran, disagreed with the headline figure by ~3.5x, and the disagreement was not treated as a finding.** Third instance of MARCO's own material holding the right answer while the narrative asserted the wrong one — after `VX-2.04` and the s18 `VX.tsv` case, both already in `MEMORY.md`.*)**: National remittance decline of -4.6% on a base of ~$64.7B implies ~$3B annualized shortfall. At a $400/month average per sender, this implies ~625K fewer senders. Since not every self-deportee was remitting regularly (dependents, recent arrivals), and some who stayed reduced amounts (fear, under-employment), the implied *sender-count* decline is in the 400-700K range — consistent with but **modest relative to** a 2.2M headline if the bulk of self-deportees were newer arrivals / dependents / informal-sector workers whose remittance participation was lower. Flag for NEXUS concentration work.
- **When Q1 2026 Banxico prints (May-June 2026):** rerun script; the tax-adjusted print will be the first clean post-intervention data.
