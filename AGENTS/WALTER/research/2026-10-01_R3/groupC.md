# WQ-295 R3 WATCH_FOR live test: GROUP C (SAM, LABOR, VULCAN, ZHAO, FERT)

Run 2026-10-01 ~15:00–15:29Z by a WALTER test subagent. Read-only: nothing was committed or moved, and nothing was written to `~/Research-Intake`.

## Method

- **Tool:** `AGENTS/WALTER/tools/watch_for_harness.py`. It runs the lane's real `match_watch_for()` (`~/Research-Intake/scripts/newsweep_config.py:961`, lane HEAD `cca0ef6`, 2026-09-30 17:59 ET) in memory. Matcher rules:
  - every word longer than 3 characters that is not on the skip list must appear in the title as a case-insensitive **substring**;
  - words of 3 characters or fewer are dropped;
  - ALL-CAPS tokens of 2–5 characters bind as case-sensitive entity tokens; `BOJ` also binds through the aliases Bank of Japan, Ueda and Kuroda.
- **Lane corpus:** **10,405 unique headlines**, 71 lane days, **2026-06-29 → 2026-09-30**.
- **Live corpus:** Google News RSS (`when:Nd`), on-topic subject queries per desk, listed in each section. The window is **30d** for VULCAN, ZHAO and FERT, and **60d** for SAM and LABOR, matching the owners' pre-screens. One VULCAN hazard probe used 180d. ⚠️ RSS returns at most about 100 items per query, so samples are capped.
- **Synthetic controls:** one or more plausible real headlines per phrase, to test recall. A miss is reported as ⚠️ recall.
- **Classification (mine):**
  - **TRUE**: the headline reports the event the phrase is keyed to. Coverage of that event in the same news cycle (reaction, explainer) counts as TRUE, because duplicates are a dedup matter, not noise.
  - **FALSE**: the phrase matched a headline whose subject is not the keyed event. Examples: a time anchor ("since X"), another entity, evergreen or forecast commentary, or a substring collision.
- **Verdict rule:** ⛔ REJECTED if there are more than 0 FALSE hits on the lane or the live sample. ✅ PASS otherwise.
- **0 / 0 results:** a phrase with no hits in a corpus that **contained the subject** shows zero noise, but its recall is unproven. A 0 on a corpus that **could not contain** the event is **UNINFORMATIVE** and is marked as such.

---

## 1. SAM — 12 proposed, replacing the current list

**Current list, from `--current`:** the lane holds **5** phrases, not the 6 the packet says. `USD/JPY above 162` is already gone. The five are `BOJ rate hike announcement` · `yen intervention confirmed` · `GPIF allocation shift` · `Japan life insurer UST sale` · `carry trade unwind confirmed`.

The current list scores **0 lane / 0 live** on every phrase. The live check covered 294 headlines over 60d from five queries: `yen intervention` · `Bank of Japan rate hike` · `GPIF allocation` · `carry trade unwind` · `Japanese life insurers Treasuries`. So it is dead: it caught **none** of the 7/30 suspected intervention, the 8/3 joint operation, or the 9/18–21 rate check.

**Live queries (504 headlines, 60d):** `yen intervention` · `Japan intervention spent` · `Mimura yen` · `Katayama yen` · `rate check yen` · `Bank of Japan emergency` · `Japan bond auction demand` · `Japanese life insurers Treasuries` · `intervention`. The corpus contained the subject for every phrase: 35 Katayama headlines, 16 JGB auction headlines, 8 "Bond Sale … Demand" headlines, 9 "emergency" headlines and 1 life-insurer headline.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `suspect intervention` | 3 (3 T: 7/30) | 1 (**1 F**) | ⛔ **REJECTED** | FALSE: *"USD/JPY weekly forecast: Suspected rate check revives intervention threat - stonex.com"*. The headline's subject is a suspected **rate check** in a forecast column, not an intervention. It is desk-relevant (ladder T1) and #3 already catches it, so its marginal cost is low; overruling is PROME's call. **Tested replacement:** `surges suspect intervention` scores 3 lane (3 T) and 0 live F. ⚠️ It misses *"Yen jumps on suspected intervention"*. Every phrase misses "intervenes / intervening" forms, e.g. *"Japan suspected of intervening as yen surges 3%"*. The tested stem `Japan intervenes` is noisy: it hits *"Yen Options Suggest a Slide to 165 Level Before Japan Intervenes"* and *"UBS AM's Zhao Is Ready to Sell Yen If Japan Intervenes Again"*, both Bloomberg. Not recommended. |
| 2 | `joint intervention` | 3 (3 T) | 18 (17 T, **1 F**) | ⛔ **REJECTED** | FALSE: *"Yen falls past 160 per dollar for first time since joint intervention - Nikkei Asia"*. "Since joint intervention" is a time anchor; the event is a 160 break, which is SAM's instrument-owned trigger and not this phrase's. **SAM's three asked adjudications:** CME *"Markets react to joint U.S. and Japan yen intervention"* = TRUE (day-after coverage). VT Markets *"Mimura warns joint US-Japan currency intervention may have peaked…"* = TRUE (an official's verbal statement). Nikkei 160 = **FALSE**. The false hit points to a desk-relevant event, so an overrule is defensible, but under the letter of the rule it is rejected. |
| 3 | `rate check intervention` | 2 (2 T) | 6 (6 T) | ✅ PASS | The stonex weekly forecast is TRUE here, because its subject is the rate check. The synthetic *"Japan conducts rate check, signaling readiness for intervention"* fires. |
| 4 | `Japan spent intervention` | 0 | 8 (8 T) | ✅ PASS | All 8 are confirmations of amounts, e.g. Kyodo *"Japan spent record 6.28 tril. yen in forex intervention on April 30"*. The synthetic fires. |
| 5 | `Mimura warn` | 2 (2 T) | 6 (6 T) | ✅ PASS | The synthetic fires. |
| 6 | `Mimura intervention` | 0 | 4 (4 T) | ✅ PASS | Includes *"USD/JPY: Japan's Mimura Dismisses Intervention Funding Limit"*, classed TRUE as an official verbal statement on intervention. |
| 7 | `Katayama excessive` | 0 | 1 (1 T) | ✅ PASS | *"Japan's Fin. Min. Katayama: Excessive Yen selling may be corrected - Kyodo"*. The synthetic fires. |
| 8 | `Katayama decisive action` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The corpus had 35 Katayama headlines and none used "decisive". The synthetic fires. |
| 9 | `BOJ emergency meeting` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The synthetic fires. |
| 10 | `BOJ emergency bond buying` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The synthetic *"BOJ launches emergency bond-buying operation"* fires, because `buying` is a substring of `bond-buying`. |
| 11 | `Japan bond sale weakest demand` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The corpus held 8 Bloomberg "Bond Sale … Demand" headlines, including *"Japan Two-Year Bond Sale Sees Weak Demand"*, and all were correctly excluded. ⚠️ **Recall:** Reuters/ET-style wording uses "auction", e.g. *"Japan's 10-year bond yield climbs after weak auction"*, and that wording is missed. **Suggest adding** `Japan bond auction weakest demand`: 0 lane, 0 live, and the synthetic *"Japan's 30-year bond auction draws weakest demand since 2015"* fires. |
| 12 | `Japan insurers sell Treasuries` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The synthetic fires (`japan` is a substring of `Japanese`). ⚠️ It misses wordings like "lifers cut foreign bonds". |

**SAM tally: 10 pass, 2 rejected (#1, #2).** Both rejections are desk-relevant spillovers: a T1 rate-check column and a 160 level break. They are not off-subject noise.

---

## 2. LABOR — 9 proposed

LABOR's pre-screen was re-run, and it agrees except on #5, where live hits are now 6 rather than 1. LABOR's pre-screen is evidence; this run is the verdict.

**Live queries (469 headlines, 60d):** `jobless claims` · `initial jobless claims` · `JOLTS job openings` · `Challenger job cuts` · `WARN notice layoffs` · `Robert Half` · `jobs report shutdown delay` · `BLS data shutdown` · `Florida unemployment claims`. The lane carried subject headlines too: 7 "jobless claims", 2 JOLTS, 297 "jobs report", 298 Florida, 4 WARN, 0 Robert Half. No government shutdown occurred in the window; the 7d check found 23 "jobs report" headlines and none mentioned a delay.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `jobless claims jump` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The synthetic fires. ⚠️ It misses "surge", "rise" and "climb". `jobless claims rise` was tested and has **1 F**: *"Gold, silver rise as jobless claims temper PCE-driven Fed repricing - Kitco"*. Not recommended. |
| 2 | `jobless claims highest` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | Both synthetics fire. |
| 3 | `JOLTS openings million` | 0 | 6 (6 T) | ✅ PASS | Every hit is a release headline. Note that it pages on every monthly scheduled release. |
| 4 | `JOLTS hires` | 0 | 1 (1 T) | ✅ PASS | *"…June JOLTS Miss as Leisure Hires Hit 18-Month Low - Tech Times"*. |
| 5 | `Challenger job cuts` | 0 | 6 (6 T) | ✅ PASS | ⚠️ **Recall gap, measured:** the lane **did** carry three Challenger releases (7/01, 8/07, 9/03), all worded "Layoffs", e.g. *"Layoffs Reach Lowest August Tally Since 2022, Challenger Report Shows"*. This phrase missed all three. **Suggest adding** `Challenger layoffs`: 3 lane + 8 live, **all TRUE** (Challenger releases). A residual hazard is "Challenger" as a Dodge model, e.g. a Stellantis plant layoff; it was not observed. |
| 6 | `WARN notice layoffs` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The synthetic *"Amazon files WARN notices for 1,200 layoffs"* fires. |
| 7 | `Robert Half outlook` | 0 | 1 (1 T) | ✅ PASS | *"Robert Half Stock Hit as Hiring Outlook Darkens - TipRanks"*. The lane runs no Robert Half query, so the lane 0 is uninformative. |
| 8 | `jobs report delay` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The synthetic *"September jobs report delayed by government shutdown"* fires. ⚠️ It misses *"BLS will not release jobs report as shutdown begins"*. `jobs report shutdown` scores 0 lane and 0 live, so it is a candidate second form. "postponed" was not tested. |
| 9 | `Florida unemployment claims jump` | 1 (1 T, 7/20 Florida Politics) | 0 | ✅ PASS | ⚠️ It misses "Florida jobless claims jump" wording; that form tested 0/0. |

**LABOR tally: 9 pass, 0 rejected.** Top recall add: `Challenger layoffs`.

---

## 3. VULCAN — 9 gap replacements + 2 safety-demand phrases

**Live queries (759 headlines, 30d):** `force majeure` · `data center force majeure` · `force majeure metal` · `HBM prices` · `HBM oversupply` · `HBM glut` · `Project Jupiter Oracle` · `Oracle lease` · `data center loan default` · `AI training pause` · `AI moratorium` · `AI safety legislation frontier models` · `OpenAI Oracle compute contract` · `compute contract`.

The corpus contained the subjects: 116 force-majeure headlines (94 of them Oracle), 60 HBM, 53 Jupiter, 62 moratorium and 75 training.

**Hazard probe (493 headlines, 180d):** `Hudbay Minerals` · `Hudbay HBM shares` · `force majeure copper` · `force majeure metals` · `force majeure aluminium smelter` · `Amazon force majeure` · `Meta force majeure` · `Microsoft force majeure` · `Oracle lease` · `HBM prices`.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `HBM oversupply` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The synthetic fires. ⚠️ **Entity hazard:** `HBM` is also **Hudbay Minerals' ticker**, and the lane carries 12 Hudbay "(NYSE:HBM)" headlines, about one a week. A *"Hudbay (HBM) … copper oversupply"* headline would fire it. |
| 2 | `HBM glut` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The synthetic fires. ⚠️ It has the same Hudbay hazard ("copper glut"). |
| 3 | `HBM prices decline` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | ⚠️ **The negative control fired:** *"Hudbay Minerals (TSX:HBM) shares decline as copper prices slip"* → match. It was not observed live (0 in 180d). ⚠️ **Recall:** it misses *"HBM prices fall 10%"*, and `HBM prices drop` scored 0/0. |
| 4 | `CoreWeave force majeure` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | It correctly ignored all 94 Oracle force-majeure headlines, which is the real negative control. The synthetic fires. |
| 5 | `Microsoft force majeure` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | ⚠️ It is open to the same market-wrap structure that killed #6, e.g. "Microsoft gains as Oracle force majeure weighs"; not observed. |
| 6 | `Meta force majeure` | 0 | 1 (**1 F**, 180d) | ⛔ **REJECTED** | FALSE: *"Nasdaq Rises to 26,939.37 as Meta Rally Offsets Oracle Force Majeure Shock - BBN Times"*. This is the Oracle n=1 case again, reached through a market wrap. It also fires on the substring negative control *"Codelco declares force majeure on copper **meta**l shipments"* (`meta` ⊂ `metal`). |
| 7 | `Amazon force majeure` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | ⚠️ The negative control *"Amazon River drought forces shipper to declare force majeure"* fires it. Not observed live. |
| 8 | `Oracle lease termination` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | ⚠️ **Recall:** it misses *"Oracle terminates lease at … Project Jupiter site"*, because `termination` is not a substring of `terminates`. **Suggest the stem** `Oracle terminat lease`: 0 lane, 0 live over 180d, and it fires on both wordings. |
| 9 | `Jupiter loan default` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | Both synthetics fire (`default` ⊂ `defaults`). |
| A1 | `defers compute contract` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | Weak corpus: only 2 "compute contract" headlines. ⚠️ It misses "delays", "pauses" and "cancels contract" wordings. |
| A2 | `AI training moratorium` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The corpus held 62 moratorium headlines (school AI moratoria, data-center moratoria) and none fired. The synthetic fires. |

**VULCAN tally: 10 pass, 1 rejected (`Meta force majeure`).**

🔴 **Coverage finding, important for VULCAN:** the lane carries **0** "force majeure", **0** "Jupiter" and **0** pause-plus-training headlines in 10,405. VULCAN's lane queries are `memory-cycle`, `ai-capex`, `power-grid` and `memory-pricing`. So phrases #4–#9 and A1–A2 are **inert on the lane** until a query fetches force-majeure, Jupiter or AI-lab news; only the HBM phrases (#1–3) are lane-live, from 225 HBM headlines. Landing them is harmless, but it is not coverage.

**VULCAN's 9/02 Fortune question** (*"Anthropic pauses some AI training following rogue agent hacks"*): it **never reached the lane**. That headline, and every other pause-plus-training headline, is absent from all 10,405 lane headlines (no AI-lab or AI-safety query exists). No BOARD signal `SIG-W-20260901…09` mentions Anthropic, so it never reached a WALTER signal either. This was a lane-coverage gap, plus a WALTER manual-routing non-catch. It was **not** a VULCAN consumption miss. The 30d live corpus shows at least 8 OpenAI pause headlines, which the lane also did not carry. If the new S1 sub-read is to be lane-fed, it needs a query, e.g. `"pauses AI training" OR "AI training pause" OR "frontier model moratorium" OR "compute contract"`; that form is untested.

---

## 4. ZHAO — 9 proposed

**Live queries (512 headlines, 30d):** `BIS Affiliates Rule` · `Busan agreement trade` · `Kuala Lumpur joint arrangement` · `US China trade truce` · `rare earth export controls` · `CXMT` · `YMTC` · `Fifth Plenum` · `Hong Kong dollar peg HKMA` · `weak-side convertibility` · `gallium` · `gallium germanium export ban`.

**Alternatives probe (481 headlines, 30d):** the same subjects plus `50% rule China` · `Kuala Lumpur trade` · `Communist Party plenum` · `HKMA buys Hong Kong dollars` · `rare earth suspension`.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `Affiliates Rule` | 0 | 0 | ✅ PASS (zero noise) — ⚠️ **recall FAILED on a real event** | The actual extension headline was *"U.S. Extends 50% Rule Under China Trade Truce - WSJ"*, which has no "Affiliates", so it was missed. This phrase is **already live under VULCAN**, so the gap is VULCAN's too. **Tested add:** `Rule China truce` scores 1 live (1 T, the WSJ headline) and 0 lane, and the synthetic fires. ⚠️ `rule` also matches "rules". |
| 2 | `Busan Agreement` | 0 | 6 (6 T) | ✅ PASS | All six report the extension to January, e.g. Reuters *"US, China agree to extend 'the Busan agreement' until January, Bessent says"*. The ET explainer is TRUE as same-cycle coverage. ⚠️ Latent hazard: other "Busan … agreement" stories, such as plastics-treaty talks; not observed. |
| 3 | `Kuala Lumpur joint arrangement` | 0 | 0 | ✅ PASS (zero noise) — ⚠️ **recall FAILED on a real event** | Missed *"China, US extend Kuala Lumpur trade arrangement to Jan 10, pledge further talks - Global Times"* (no "joint"). **Tested replacement:** `Kuala Lumpur arrangement` scores 1 live (1 T) and 0 lane. |
| 4 | `rare earth export controls` | 0 | 5 (**5 F**) | ⛔ **REJECTED** | Every hit is a preview, evergreen or off-target story; none reports a change to the suspension clock. **FALSE:** <br>• *"Trump and Xi to discuss China's rare earth export controls - S&P Global"* <br>• *"FM spokesperson responds to whether Chinese, US leaders will discuss in Washington China's rare earth export controls to Japan - Global Times"* <br>• *"China US Rare Earth Export Controls After Summit 2025 - Rare Earth Exchanges"* <br>• *"China Rare Earth Export Controls Machine Learning Early Warning - Rare Earth Exchanges"* <br>• *"China Rare Earth Export Controls Loom Over Upcoming Trump Xi Summit - SuaraGarut.ID"* <br>**Tested verb-bound forms:** `reimposes rare earth` and `rare earth controls suspension` both score 0/0 and their synthetics fire; recall unproven. |
| 5 | `CXMT` | 26 (**26 F**) | 100 (**≥40 shown, all F**) | ⛔ **REJECTED** | A bare entity fires on all company news. Examples: *"Chinese chip champion CXMT soars 466% in market debut"* (lane 7/27); *"CXMT Officially Starts Mass Production of LPDDR6 Memory - TechPowerUp"*. **Tested replacement:** `CXMT Entity List` scores 0/0 and the synthetic fires. VULCAN's live `adds Entity List` / `added to Entity List` already cover the event shape. |
| 6 | `YMTC` | 5 (**5 F**) | 24 (**24 F**) | ⛔ **REJECTED** | Examples: *"[News] German Court Reportedly Finds Micron Infringed Two YMTC NAND Patents, Grants Injunctions - TrendForce"* (lane 9/23); *"China Flash Memory Giant YMTC Takes Key Step Toward Marquee IPO - Bloomberg.com"*. **Tested replacement:** `YMTC Entity List` scores 0/0. |
| 7 | `Fifth Plenum` | 0 | 1 (1 T) | ✅ PASS | *"Fifth Plenum date set; Xi's US visit confirmed… - Sinocism"*. ⚠️ **Recall:** it missed Reuters *"China's Xi chairs Politburo; Central Committee plenum set for October 26-29"* and SCMP *"Communist Party sets October plenum date…"*. Tested alternatives: `plenum October` (6 T) and `Central Committee plenum` (3 T). 🔑 **The dating headline has already arrived** (Reuters: Oct 26–29), so ZHAO should verify its CATALYSTS placeholder row against it. |
| 8 | `weak-side convertibility` | 0 | 0 | ✅ PASS (zero noise; recall unproven) | The corpus had only 2 HKMA headlines, e.g. *"HKMA flags carry-trade risks as currency weakens to one-month low"*. ⚠️ Real defence headlines usually read "HKMA buys HK$… to defend peg" or "weak end of band". The synthetic *"Hong Kong Monetary Authority buys HK dollars to defend peg"* fires **nothing**, and `HKMA buys` needs the literal token `HKMA` (there is no alias). |
| 9 | `gallium` | 1 (**1 F**) | 61 (**61 F**) | ⛔ **REJECTED** | Lane: *"Alcoa to build gallium plant at Wagerup refinery - Yahoo Finance"* (7/15). Live examples: *"Gallium Anomaly May Finally Be Explained - American Physical Society"*; *"US Department of War Pledges US$174 Million for New Gallium Plant"*. **Tested replacement:** `China gallium export` scores 0/0 and the synthetic fires. |

**ZHAO tally: 5 pass, 4 rejected** (`rare earth export controls`, `CXMT`, `YMTC`, `gallium`). Two of the passes (#1, #3) **demonstrably missed real events this month**, so their replacements are recommended over the originals.

---

## 5. FERT — 8 proposed (no lane key, no fertilizer query)

The lane has 0 fertilizer headlines (0 fertiliz, 0 potash, 0 phosphate, 0 Mosaic, 0 QAFCO). The 10 "urea" substrings in the lane are all **"B*urea*u"**. **Every lane 0 below is UNINFORMATIVE by construction.**

**Live queries:**
- **Run 1 (511 headlines, 30d):** `China urea export` · `China fertilizer export` · `China phosphate export` · `urea import tender India` · `phosphate countervailing duties` · `Mosaic phosphate` · `Mosaic curtail` · `QAFCO` · `Qatar urea` · `potash sanctions` · `Belarus potash` · `fertilizer prices` · `urea prices` · `China export Bureau` · `National Bureau of Statistics China exports`.
- **Run 2:** the candidate lane query below (99 headlines, 7d).
- **Run 3 (326 headlines, 30d):** a probe of verb-bound alternatives.
- **Run 4 (124 headlines, 60d):** a Farm Bureau hazard probe.

| # | Phrase | Lane | Live | Verdict | Recall control / note |
|---|---|---|---|---|---|
| 1 | `China urea export` | 0 (uninformative) | 9 (7 T, **2 F**) | ⛔ **REJECTED** | **FALSE:** *"Petrovietnam Ca Mau Fertilizer: Urea exports surpass domestic sales, China key - theinvestor.vn"* (Vietnamese exports; China is only the market) and *"NW China's Qinghai opens first direct rail route to Laos, driving urea exports deep into ASEAN - Global Times"* (a logistics story, not quota or floor state). TRUE hits include Reuters *"China allows fresh urea exports amid Iran war-fuelled fertiliser crisis, sources say"*, a T10/G3-relevant event that **FERT's own samples did not surface**. ⚠️ **Substring hazard:** `urea` ⊂ `Bureau`, and Google News titles carry the source suffix (e.g. "- Oklahoma Farm Bureau", "iowafarmbureau.com"). The synthetic negative *"China's exports beat forecasts…, National Bureau of Statistics data show"* **fires**. It was not observed live. **Tested replacements:** <br>• `China allows urea export`: 4 live, all T <br>• `China halts urea export`: 0/0, synthetic fires <br>• `China urea export quota`: 0/0, synthetic fires <br>• `China resumes urea export`: 0/0 <br>All share the Bureau hazard. |
| 2 | `China fertilizer export` | 0 (uninformative) | 9 (6 T, **3 F**) | ⛔ **REJECTED** | **FALSE:** <br>• Petrovietnam (above) <br>• *"DW News. . China's recent restriction on exports of sulfuric acid—a little-known chemical with a huge role in batteries, fertilizers and cri…"* (a sulfuric-acid control, not urea quota or floor) <br>• *"China Ammonium Chloride Market Turns Firmer Amid Rising Fertilizer Demand and Export Enquiries - ChemAnalyst"* <br>TRUE hits include Reuters *"China tightens border inspections for fertilizer exports, sources say"*. `China fertilizer export curbs` tested 0/0. |
| 3 | `China phosphate export` | 0 (uninformative) | 0 | ✅ PASS (zero noise; recall unproven) | The corpus had 1 phosphate-export headline (SMM phosphate ore) plus Egypt raw-phosphate curbs, and neither fired. The synthetic fires. |
| 4 | `urea import tender` | 0 (uninformative) | 4 (4 T) | ✅ PASS | Hits: ET *"Tender floated to import 1.7 mt urea…"*; *"India launches second round of global urea import tender…"*; PSU Watch *"NFL's urea import tender gets lowest bid of $445…"*; Indian Express *"Urea prices crash in latest import tender"*. The synthetic *"NFL issues tender to import urea"* fires. |
| 5 | `phosphate countervailing` | 0 (uninformative) | 0 | ✅ PASS (zero noise; recall unproven) | No CVD headlines were in the corpus. The synthetic fires. |
| 6 | `Mosaic curtail` | 0 (uninformative) | 0 | ✅ PASS (zero noise) — ⚠️ **recall FAILED on a real event** | It missed three live T12 headlines: *"ASA Statement on Mosaic Phosphate Production Cuts - Oklahoma Farm Report"*, *"ISG Raises Concerns Over Mosaic Phosphate Production Cuts"* and *"Mosaic's phosphate cuts another blow to Prairie farmers - producer.com"*. It also misses *"Mosaic idles … mine"*. **Tested add:** `Mosaic phosphate cuts` scores 3 live (3 T). |
| 7 | `QAFCO` | 0 (uninformative) | 0 | ✅ PASS (zero noise; recall unproven) | QAFCO is absent from both corpora, including the `QAFCO` and `Qatar urea` queries, so this is weak evidence. The synthetic fires. |
| 8 | `potash sanctions` | 0 (uninformative) | 4 (4 T) | ✅ PASS | All four concern Belarus sanctions status, e.g. Kyiv Post *"US Urges Ukraine to Support Easing Belarus Potash Sanctions"*. RFE *"Will The EU Soon Lift Potash Sanctions On Belarus?"* is commentary-shaped; it is TRUE for a triage-only row. |

**FERT tally: 6 pass, 2 rejected** (`China urea export`, `China fertilizer export`). Recommended swaps: `China allows urea export` plus `China urea export quota` / `China halts urea export` for #1–2, and add `Mosaic phosphate cuts`.

**Should the lane get a fertilizer query?** Yes. Without one, all eight FERT phrases are inert, and this month's two FERT-relevant events (China re-allowing urea exports; Mosaic phosphate production cuts) never reach the lane.

- **Measured form:** `"urea export" OR "urea exports" OR "urea tender" OR "urea import" OR "fertilizer exports" OR "phosphate exports" OR "DAP prices" OR "urea prices" OR "Mosaic phosphate" OR QAFCO OR "potash sanctions" OR "Belarus potash"`, plus `when:7d` (the lane's own CRUISE finding: without a recency operator the RSS returns stale items).
- **Volume:** 99 headlines per 7d, which equals the RSS cap, so true volume is higher. Most are price and market chatter (about 53 fertilizer and 58 urea titles in 99).
- **Expected noise:** query output lands as plain NEW unless a phrase matches, so noise equals phrase hits. Over this output the phrases produced 20 hits in 7d; the only FALSE hits came from the two phrases rejected above.
- **Leaner form:** dropping `"DAP prices"`, `"urea prices"` and `"Belarus potash"` returned only **7** headlines in 7d and missed both key events, so it is too thin. ⚠️ `"Belarus potash"` should still come out of the query, given FERT's potash triage-only rule (81/30d per FERT); keep `"potash sanctions"`. That exact variant is untested.
- **Shared hazard:** the `Bureau` substring (Farm Bureau sources) is the main risk to every `urea` phrase once this query is live.

This is WALTER's and PROME's call; FERT flagged it and did not request it.

---

## Desk tallies

| Desk | Pass | Rejected | Rejected phrases |
|---|---|---|---|
| SAM | 10 | 2 | `suspect intervention`, `joint intervention` (both desk-relevant spillovers) |
| LABOR | 9 | 0 | — |
| VULCAN | 10 | 1 | `Meta force majeure` |
| ZHAO | 5 | 4 | `rare earth export controls`, `CXMT`, `YMTC`, `gallium` |
| FERT | 6 | 2 | `China urea export`, `China fertilizer export` |

Harness output for each run is in the session scratchpad and was not committed. To reproduce, re-run with the queries listed in each section.
