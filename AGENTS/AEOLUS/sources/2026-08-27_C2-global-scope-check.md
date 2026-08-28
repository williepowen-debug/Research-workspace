# C2 global-scope check — does the US-crop-condition band see the crops El Niño actually hits?

**Worker pass. Findings are PROPOSAL-ONLY — AEOLUS adjudicates.** Written per STATUS.md open item #10 ("Global-crop scope check for C2 (ABARES + FAO) — my benign read may certify US row crops only") and STATUS.md's own flag that C2 has "refused to confirm" for four straight sessions on a US-only instrument while CPC gives >90% odds of a very-strong El Niño and 69% odds of a historic event.

**As of: 2026-08-27.** All pulls run live this session; commands and raw outputs below are reproducible.

---

## 0. VERDICT UP FRONT

**HYPOTHESIS HOLDS.** C2's registered band (US corn/soy G/E %) is measuring a crop-region/season combination with a **documented weak-to-insignificant** El Niño teleconnection, while the mechanism the channel claims to track (`drought·heat·flood → crop yield ↓ → grain & softs ↑`) is firing hardest in regions the band never looks at. A "benign" US G/E read this session is not evidence of a benign global picture — it is a correctly-read instrument pointed at the wrong geography for this driver.

**Single strongest piece of evidence:** peer-reviewed and USDA-agronomic consensus states ENSO's growing-season effect on US/Canada summer row crops (corn, soybean) is **weak or insignificant** because "the strongest effects of ENSO do not occur during the [US] growing season" — while the *same* literature finds ENSO is "the most significant driver" of yield variability **globally**, with impacts detected on **every crop-producing continent** (Iizumi et al. 2014, and the multi-model ESD teleconnection study, cited below). The channel's own thermometer is in the one major basket ENSO barely touches.

**Second-strongest evidence, pulled live this session:** USDA's own August 2026 PSD Online database — the same institutional source AEOLUS already cites for the US G/E read — shows the **August-vintage 2026/27 production forecast for Australian wheat down 22.2% YoY** (28.0 vs 35.985 MMT) and **Malaysian palm oil down 3.0% YoY** (19.6 vs 20.2 MMT), while **US corn is down 5.9% YoY for reasons the WASDE narrative does not attribute to ENSO** (area/other factors) and Argentine/Brazilian soybean are both **up** (a positive El Niño signal, consistent with the literature below, not a global bear case).

---

## 1. THE TELECONNECTION MAP (established literature — label: LITERATURE)

| Region / crop | Direction | Confidence | Mechanism | Source |
|---|---|---|---|---|
| **Australian wheat** (SE Australia, Aug–Dec) | **NEGATIVE** — drier/warmer | **HIGH**, but **declining relative to IOD since the 1990s** | El Niño → below-normal spring rainfall in the Murray-Darling Basin (avg. 28% below long-term average across all El Niño years since 1900); 6 of 9 moderate+ El Niño events cut production, 4 by ≥30% below trend | Univ. of Sydney (2023); *Impacts of IOD, ENSO and ENSO Modoki on Australian Winter Wheat Yields*, *Sci. Reports* (2015); *Increasing dominance of Indian Ocean variability impacts Australian wheat yields*, *Nature Food* (2022) |
| **SE Asia palm oil** (Indonesia, Malaysia — Sabah/Sarawak, Kalimantan/Sumatra) | **NEGATIVE**, but **lagged 9–12 months** | **HIGH** on direction, **MEDIUM** on 2026 timing | Reduced rainfall → moisture stress on oil palm; historical: Malaysian CPO output fell 13.2% in 2016 (post-2015/16 Super El Niño) and 8.3% in 1998 (post-1997/98) | MPOB *OPB74* (Nadia et al.); Marex (2026); MPOC (2026) |
| **SE Asia rice** (Thailand, Vietnam, Indonesia) | **NEGATIVE** — reduced monsoon/irrigation water | **MEDIUM** | Same monsoon-suppression mechanism as India; historically ties to reduced planted area / delayed transplanting in mainland SE Asia | FAO GIEWS El Niño/La Niña Collection (2026); general ENSO-rice literature |
| **Indian monsoon (all crops: rice, pulses, coarse cereals, oilseeds, cotton — kharif)** | **NEGATIVE** — weaker SW monsoon | **HIGH** — one of the most robust ENSO teleconnections in the literature | El Niño historically associated with below-normal Indian monsoon rainfall; explicit in IMD/CPC framing | IMD; USDA FAS GAIN report *"Monsoon Recovery Fails to Boost Sluggish Crop Planting"* (Aug 2026, Mumbai post) |
| **Southern African maize** (Zambia, Zimbabwe, Malawi, South Africa) | **NEGATIVE** for the Oct–Mar growing season | **HIGH** for the mechanism; **the current print is NOT yet a test of it** (see §4) | El Niño → dry spells Oct–Mar; 2023/24 event produced the worst regional drought on record, 68M people needing food aid, 40–80% of Zambia/Zimbabwe/Malawi maize crop lost | SADC Regional Humanitarian Appeal (2024); IFPRI; WFP |
| **Argentina / southern Brazil corn & soy (Pampas)** | **POSITIVE** for the Oct–Mar growing season | **HIGH** in moderate events, **flips to flood risk in strong events** | El Niño → above-normal (120–160% of normal) spring/summer rainfall in Buenos Aires, Santa Fe, Córdoba, Entre Ríos, Paraná, Rio Grande do Sul; boosts yields in moderate El Niño, caused major flooding/waterlogging (>3M ha damaged) in the strong 2015/16 event | farmdoc daily (2020, 2024); El Niño Guide (2026) |
| **Brazil wheat** (Paraná, Rio Grande do Sul — a *winter* crop, different calendar from the corn/soy positive signal above) | **NEGATIVE this cycle** — but via a **behavioral/area** channel, not yet a realized yield hit | **MEDIUM** | Farmers reducing wheat-planted area in anticipation of El Niño-linked excess-rain/quality risk at harvest, not a rainfall deficit | USDA FAS WAP circular (Aug 2026) — CONAB cut Paraná/Rio Grande do Sul wheat area 3%/5% in July |
| **Brazil coffee (Arabica)** | **AMBIGUOUS / MIXED** — flagged, not resolved | **LOW** | El Niño reduces frost risk (positive) but raises heat-wave/uneven-flowering risk (negative); literature does not converge on net sign | The Pourover; Modern Diplomacy (Aug 2026) |
| **Brazil sugar (Center-South)** | **WEAK / AMBIGUOUS** | **LOW** | Brazil "tends to experience more limited impacts" vs. Northern Hemisphere producers; wetter Center-South could help 2027/28 cane but risks harvest disruption if excessive | Hedgepoint Global (2026); riotimesonline (2026) |
| **US corn/soybean belt (Jun–Aug growing season)** | **NEUTRAL / NO CONSISTENT SIGNAL** | **the literature explicitly calls this OUT as the weak case** | "Yields of summer annual crops such as corn and soybean tend to be less affected because the strongest effects of ENSO do not occur during the growing season"; a 1982–2014 study of 10 El Niño + 9 La Niña events found **no consistent relationship** between ENSO intensity and Corn Belt yield/NDVI | Pioneer Seeds (Corteva) agronomy summary; commodityreport.substack.com; hectar.global synthesis of the underlying academic literature |

**⚠️ Where the literature disagrees or is weak (flagged, not smoothed over):**
- **Coffee and sugar** (Brazil): genuinely mixed-sign in the sourced material — do not treat as a confirmed leg of C2's global read.
- **Australia**: the ENSO signal itself is reported as **declining in relative importance since the 1990s** vs. the Indian Ocean Dipole (*Nature Food* 2022) — a real, sourced caveat against over-crediting El Niño alone for the current ABARES cut.
- **Palm oil and Southern African maize** both carry a **lag** (9–12 months for palm oil; the next growing season for SE Africa) that the literature is explicit about — a benign *current* print in either does not falsify the mechanism, because the mechanism hasn't been tested yet this cycle (see §4).

---

## 2. THE CRITICAL COMPARISON — does the US corn/soy belt even have a summer El Niño signal?

**No — and this is not a close call in the sourced material.**

Three independent characterizations converge on the same answer:
1. **Mechanistic**: "the strongest effects of ENSO do not occur during the [US] growing season" (Pioneer/Corteva agronomy summary, citing the standard ENSO-crop literature).
2. **Statistical**: a study spanning 10 El Niño + 9 La Niña events (1982–2014) found ENSO events "are not reflected in a consistent manner in NDVI or corn yield data," and "historical research has not identified a consistent relationship between ENSO intensity and Corn Belt summer yield or weather outcomes."
3. **Comparative**: the same sources that report the weak US summer link are the ones reporting **strong, specific, mechanistically-clear** signals for Australia (spring rainfall), India (monsoon), and Argentina (spring/summer rainfall) — i.e., this is not "ENSO signals are hard to find anywhere," it is specifically "ENSO signals are hard to find **here**."

**Implication for AEOLUS:** a benign or even improving US G/E print during a very-strong/historic El Niño is **not informative** about the global C2 mechanism one way or the other — it is close to what the null hypothesis predicts. STATUS.md's own C2 read already contains the tell: drought is "concentrated OK/TX Panhandle, not the corn belt" — consistent with a channel that is watching a crop in a season where this driver has little to say, and is (correctly, on its own terms) failing to confirm because there is nothing here for it to confirm.

---

## 3. INSTRUMENTS — verified vs. not verified

### ✅ VERIFIED — pulled live this session, exact commands below

**USDA FAS PSD Online — bulk CSV downloads (no API key required).** This is the strongest find: a reproducible, no-auth, direct-download global production/supply/distribution database, refreshed to WASDE-release cadence (last-modified header confirms **2026-08-12**, the August WASDE cycle).

```bash
# Grains & pulses (wheat, corn, rice, barley, sorghum, etc.)
curl -sL -o psd_grains.zip "https://apps.fas.usda.gov/psdonline/downloads/psd_grains_pulses_csv.zip" -A "Mozilla/5.0"
unzip -o psd_grains.zip   # -> psd_grains_pulses.csv (~51 MB, flat CSV)

# Oilseeds (soybean, palm oil/palm kernel, rapeseed, sunflowerseed, etc.)
curl -sL -o psd_oil.zip "https://apps.fas.usda.gov/psdonline/downloads/psd_oilseeds_csv.zip" -A "Mozilla/5.0"
unzip -o psd_oil.zip      # -> psd_oilseeds.csv (~78 MB, flat CSV)

# Also live (not yet queried this session): psd_cotton_csv.zip, psd_sugar_csv.zip
```
CSV schema: `Commodity_Code,Commodity_Description,Country_Code,Country_Name,Market_Year,Calendar_Year,Month,Attribute_ID,Attribute_Description,Unit_ID,Unit_Description,Value`. Query pattern (Python `csv.DictReader`, filter on `Country_Name`, `Commodity_Description`, `Market_Year`, `Attribute_Description=="Production"`).

**Results pulled 2026-08-27 (all August-2026-vintage USDA estimates, `Month=08` except where noted):**

| Country | Commodity | MY2026 Production | MY2025 Production | YoY | Direction vs. El Niño literature |
|---|---|---|---|---|---|
| Australia | Wheat | **28,000** (1000 MT) | 35,985 | **−22.2%** | ✅ consistent (negative) |
| Argentina | Soybean | **50,000** | 49,500 | **+1.0%** | ✅ consistent (positive) |
| Brazil | Soybean | **186,000** | 180,500 | **+3.0%** (record) | ✅ consistent (positive) |
| Indonesia | Palm oil | **47,500** | 46,700 | **+1.7%** | ⚠️ **disagrees with MPOC's reported −2M-tonne 2026 call** (see caveat below) |
| Malaysia | Palm oil | **19,600** | 20,200 | **−3.0%** | ✅ consistent (negative), smaller than the 2016 post-event 13.2% cut — consistent with the literature's 9–12mo lag: full stress hasn't hit yet |
| India | Wheat | **121,000** | 117,945 | +2.6% | N/A — wheat is a *rabi* (winter) crop, already harvested before this monsoon; not a live test of the current El Niño |
| India | Rice, milled | **150,000** | 154,024 (Jul-vintage) | −2.6% | directionally consistent but early-season; kharif harvest not complete |
| Thailand | Rice, milled | **20,300** | 20,700 (Jun-vintage) | −1.9% | directionally consistent, early |
| South Africa | Corn | **16,500** | 18,000 (Jul-vintage) | **−8.3%** | ⚠️ **conflicts with South Africa's own CEC** (see caveat below) |
| Zambia | Corn | **4,938** | 3,865 | **+27.8%** (record) | ⚠️ **this is the OLD season, already harvested** — see §4 |
| **US** | Corn | **406,748** | 432,342 | **−5.9%** | control — WASDE narrative does not attribute this to ENSO (area/other) |

⚠️ **Two flagged disagreements, reported honestly rather than smoothed:**
- **Indonesia palm oil**: USDA's PSD figure (+1.7% YoY) **disagrees in direction** with MPOC's press-reported call of a ~2M-tonne 2026 decline. Both are dated 2026; I did not find a reconciling source. **This is a live, unresolved instrument conflict, not a synthesis error on my part** — flag for AEOLUS adjudication.
- **South Africa corn**: USDA PSD (16.5 MMT) is **~5% below** South Africa's own Crop Estimates Committee figure (17.4 MMT, reported 2026-08-27, same day as this pull) for what should be the same May–April marketing year. Possible explanations I could not resolve: MY-labeling convention mismatch between USDA and CEC, or a genuine USDA-vs-CEC estimate gap. **Do not cite either figure as authoritative without resolving this first.**

**FAO Food Price Index** — pulled live, WebFetch on `https://www.fao.org/worldfoodsituation/foodpricesindex/en/`:
- **131.1 points, July 2026** (latest available). Sub-indices: Cereals **113.8**, Vegetable oils **195.7**, Dairy **116.2**, Meat **127.7**, Sugar **95.0**. Narrative: "Increases in the price indices for cereals, sugar and vegetable oils were partially offset by declines in those for meat and dairy." This is a **global, monthly, single-number aggregate** — a plausible C2 replacement instrument (see §5).

**USDA FAS World Agricultural Production circular (WAP)** — pulled live via direct PDF download (`curl` succeeded where `WebFetch` failed):
```bash
curl -sL -o wap.pdf "https://apps.fas.usda.gov/psdonline/circulars/production.pdf" -A "Mozilla/5.0"
```
Latest issue: **WAP 08-26, August 2026**, released same-day as WASDE. Contains narrative feature articles (this month: Russia corn record, EU corn 20-year low, Zambia corn record, Kazakhstan wheat, Brazil wheat cut, EU wheat cut, Argentina sunflowerseed) — **which countries get a feature article varies month to month**; it is not a fixed watchlist. Confirmed the Brazil-wheat-area-cut-on-El-Niño-risk narrative in §1 directly from this primary.

**ABARES Australian Crop Report** — confirmed via search (WebFetch itself timed out on the page, but the June 2026 figures are corroborated independently by DTN/Grain Central/Stockjournal secondary reporting, all citing the same primary report): national wheat production forecast **26.7 million tonnes, −26% YoY**; WA −29% to 9.47 Mt, Qld −43% to 1.32 Mt; explicitly attributed to "soil moisture availability" concerns. **Next issue due 2026-09-01** — falls inside AEOLUS's normal ~30-day calendar-catalyst window.

**South Africa CEC report** — confirmed via search (direct PDF at `sagis.org.za/wp-content/uploads/2026/06/CEC_2026-06-25.pdf` not fetched this session, but the August round-up is corroborated by CNBC Africa, IOL, CAJ News): August 2026 estimate **17.4 million tonnes**, white maize 9.49 Mt / yellow maize 7.91 Mt.

**MPOB (Malaysian Palm Oil Board)** — confirmed via search-corroborated secondary reporting (direct site fetch 404'd, see below): July 2026 stocks **2.63M tonnes (+3.32% MoM)**, CPO production **1.79M tonnes (+9.41% MoM)**. **Currently rising, not yet showing drought stress** — consistent with the literature's 9–12 month lag (§1); this is *not* a falsification of the mechanism, it's a "too early to test yet" reading.

**India monsoon (via USDA FAS GAIN, corroborated by search only — see gap below):** cumulative season rainfall **~11–11.5% below the Long Period Average as of Aug 1, 2026**; kharif sowing **20% behind last year** (35M ha vs. 44.3M ha same date last year), with rice, pulses, coarse cereals, oilseeds and cotton all lagging; 111 districts flagged high-risk (prolonged deficit + <25% irrigation coverage). IMD forecasts continued below-normal (<94% LPA) rainfall through September.

### ❌ NOT VERIFIED — declared gaps, not substituted

- **IGC Grains and Oilseeds Index (GOI)**: `igc.int/en/gmr_summary.aspx` and the `marketinfo-goi.aspx` page both returned a **live ASP.NET server error** (`System.Data.OleDb.OleDbException: Unspecified error` — the site's own backend database call is failing), confirmed by direct `curl`, not just WebFetch. A press-reported secondary claims GOI "rose 3% since the July report to a two-year high, +14% YoY, wheat and soybeans each +16% YoY" — **directionally consistent with global (not US) grain stress, but I could not pull the primary number myself. Report the secondary as unverified, not as an instrument reading.**
- **India IMD rainfall statistics page** (`mausam.imd.gov.in/responsive/rainfall_statistics.php`): loaded, but the live cumulative-departure figure is on a linked sub-page I did not locate; homepage carries navigation only.
- **USDA FAS GAIN India monsoon report, direct PDF/HTML**: both the PDF link and the HTML report page returned **Access Denied (Akamai edge block, reference ID logged)** on direct `curl`. The content is only available to me via WebSearch-summarized secondary text, not a primary pull — flag accordingly.
- **FAO AMIS Market Monitor**: not attempted this session (time-boxed); a real gap, not a "checked and failed" gap — note for a follow-up pass.
- **FAO GIEWS country briefs**: home page located (`fao.org/giews/countrybrief/`) and the El Niño Collection summary was retrievable via WebSearch snippet, but I did not WebFetch/pull an individual country brief PDF this session — partial verification only.

---

## 4. THE LAG PROBLEM — a second reason C2 is reading "benign" that has nothing to do with geography

Beyond the wrong-crop-region problem (§1–2), several of the "current" reads above are **not actually tests of this El Niño cycle yet**:
- **Southern African maize** (Zambia record +27.8%, South Africa's CEC 17.4 Mt): this is the crop that was **planted and grown under the prior (non-El-Niño) season** and is now being harvested/finalized. The relevant test is the **Oct 2026 – Mar 2027 planting**, which is still ahead.
- **Malaysian/Indonesian palm oil**: currently **rising** (MPOB July +3.32% stocks, +9.41% production MoM) — this is pre-lag, not a falsification; the literature's own 9–12 month lag places the expected stress window in **late 2026 into 2027**.
- **India wheat** (+2.6%): a *rabi* crop already harvested before the current monsoon; irrelevant to grading this event.

**A single global snapshot cannot separate "the mechanism doesn't apply here" (Southern Africa maize's forward risk, palm oil) from "the mechanism applies and just hasn't fired yet."** Any re-scoped C2 instrument needs to carry this distinction explicitly, or it will misread "too early" as "benign" the same way the US band currently misreads "wrong season" as benign.

---

## 5. PROPOSED RE-SCOPE (proposal only — AEOLUS adjudicates; no levels set without a base rate)

**The core defect:** a single US-domestic physical-condition metric cannot represent a globally-transmitted mechanism. Two structurally different fixes exist, with a real tradeoff:

| Option | What it measures | Pro | Con |
|---|---|---|---|
| **A. Global price index** (FAO Food Price Index cereals/veg-oils sub-indices, and/or IGC GOI once its primary is reachable) | Aggregate market-clearing outcome across all producing/consuming regions | Single number, already aggregates the geography problem away, monthly cadence matches AEOLUS's session rhythm, **FAO FPI already verified pullable this session** | **Lagging and noisy** — prices reflect stocks, freight, currency, and demand shocks too, not just this mechanism; a price move could confirm C2 or could be a different story entirely (a "naked number" risk under the fleet's own citation discipline) |
| **B. Physical-condition basket** (ABARES wheat forecast + a palm-oil production/stocks read + IMD monsoon departure + a Southern Hemisphere maize read, each cited to its regional primary) | The actual mechanism stage (crop stress), region by region | Traceable to a specific driver in a specific place — matches AEOLUS's "channels, not weather" discipline and gives a real falsifier per leg | Four to five separate instruments to maintain instead of one; cadences don't line up (ABARES quarterly-ish, MPOB monthly, IMD daily-in-season, USDA PSD monthly) — a maintenance-cost problem, not a signal problem |
| **C. Hybrid** — keep US G/E as a labeled **"US-only, low-ENSO-relevance"** sub-line (it's still useful for the CARL/MARCO CPI bridge on its own terms), and add ONE global leg as the actual C2 driver-confirmation instrument | Separates "is the US crop fine" (a real, still-useful question) from "is the ENSO-driven global mechanism firing" (C2's actual charter) | Minimal disruption to the existing US instrument that CARL/MARCO already consume; fixes the mislabeling without discarding a working read | Still needs Option A or B picked for the new global leg |

**My read (proposal, not adjudication): Option C, with the global leg built from Option B's ABARES + IMD + MPOB/PSD-oilseeds legs rather than Option A's price index** — because C2's own stated mechanism (`crop yield ↓ → grain & softs ↑`) has the price move as the **second** stage, not the first; scoring the channel on the price already conflates stages 1 and 2, the same layering problem AEOLUS's water/regime folders were built to avoid. A price-only C2 would also duplicate what the FAO Food Price Index and IGC GOI already do generically, without adding AEOLUS's channel-specific value.

**⚠️ Levels: deferred pending base rate, as required.** I have **not** established a base rate for any of: ABARES wheat-forecast YoY-change distribution across past El Niño years, IMD cumulative-departure distributions, or MPOB stock/production percentage moves. Registering Yellow/Orange/Red bands on any of these now would repeat the exact defect class flagged elsewhere in STATUS.md (`finding_base_rate_the_threshold_before_building_it` — cited there for the Panama slot-utilization band). **This worker did not attempt that base-rate work; it is a distinct, larger task from this scope check.**

---

## 6. SOURCES (consolidated)

- Univ. of Sydney (2023), *How will El Nino impact the world's wheat and global food supply*
- *Impacts of IOD, ENSO and ENSO Modoki on the Australian Winter Wheat Yields in Recent Decades*, Scientific Reports (2015) / PMC4663488
- *Increasing dominance of Indian Ocean variability impacts Australian wheat yields*, Nature Food (2022)
- DTN/Progressive Farmer (2026-06-02), *Australian Wheat Production Expected to Drop 26%*; Grain Central, Stockjournal (ABARES June 2026 secondary coverage)
- MPOB, *OPB74* — Nadia et al., *The Impact of El Niño and La Niña on Malaysian Palm Oil*
- Marex (2026-06), *El Niño impact on Malaysian and Indonesian palm oil production*
- MPOC (2026), *Indonesia 2026 crude palm oil output to fall due to El Nino*
- USDA FAS GAIN (Aug 2026, Mumbai), *Monsoon Recovery Fails to Boost Sluggish Crop Planting* (secondary-sourced only — primary blocked, see §3)
- IMD (via secondary reporting), cumulative rainfall departure ~11–11.5% below LPA as of 2026-08-01
- SADC Regional Humanitarian Appeal (2024); IFPRI, *Southern Africa drought: Impacts on maize production*; WFP
- farmdoc daily, *The Impact of Preseason La Niña Episodes on Corn and Soybean Yields in Brazil and Argentina* (2020); farmdoc IFES South America Crop Production report (2024)
- USDA FAS, *World Agricultural Production* circular WAP 08-26 (Aug 2026) — pulled primary, `apps.fas.usda.gov/psdonline/circulars/production.pdf`
- USDA FAS PSD Online bulk CSV — `apps.fas.usda.gov/psdonline/downloads/psd_grains_pulses_csv.zip`, `psd_oilseeds_csv.zip` — pulled primary, 2026-08-27
- FAO, Food Price Index — `fao.org/worldfoodsituation/foodpricesindex/en/` — pulled primary, July 2026 release
- IGC, GOI — attempted primary pull, **server error**, secondary-only (Kpler/World Grain-style trade press)
- CNBC Africa, IOL, CAJ News Africa, africannewsagency.com (2026-08) — South Africa CEC August maize estimate, secondary corroboration of `sagis.org.za` primary (not directly fetched)
- Malay Mail, New Straits Times, palmoilmagazine.com (2026-08-10/13) — MPOB July 2026 stocks/production, secondary corroboration of MPOB primary (site fetch 404'd)
- Iizumi et al. (2014) and the multi-model ESD teleconnected-crop-yield-variability study (2020), cited via NOAA Climate.gov ENSO blog synthesis and academic secondary summaries — global ENSO-crop-yield teleconnection literature
- Pioneer Seeds (Corteva agronomy), *Impacts of the El Niño Southern Oscillation on Crop Production*; commodityreport.substack.com; hectar.global — US Corn Belt weak-signal synthesis

**Internal (AEOLUS own files, read not edited, for context only):** `STATUS.md` (C2 row, ENSO forward odds, open item #10), `regime/DOSSIER.md` §1 (ONI/RONI/OISST/weekly state), §3 (C2 per-channel sign: "ambiguous... drought geography is southern Plains, not the corn belt"), `THESIS.md` C2 section (bidirectional-flip re-spec, phenology note on corn dent stage).
