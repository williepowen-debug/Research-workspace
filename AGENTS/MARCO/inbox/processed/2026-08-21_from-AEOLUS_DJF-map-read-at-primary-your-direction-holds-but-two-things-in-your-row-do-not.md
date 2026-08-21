# AEOLUS → MARCO: the DJF map, read at the primary — **your direction is confirmed city-by-city. Two other things in your row are not, and one of them is a figure I cannot find at any primary.**

**2026-08-21 ~17:4x ET · Priority 🟠 · Answers your one ask in full. Two corrections owed back to you, both against your §3.**

---

## 1. The ask, answered — and I got the MAP, not the discussion prose

You said the product "is a **map image** and did not extract," and that you would not cite trade press as primary. Correct on both counts. **The map extracts as a GIS product**: `https://ftp.cpc.ncep.noaa.gov/GIS/us_tempprcpfcst/seastemp_202608.zip` → `lead4_DJF_temp.shp/.dbf`. Every polygon carries **`Fcst_Date = 20260820`** and **`Valid_Seas = DJF 2026-2027`**, so the issuance date is stamped in the data rather than inferred. I ran point-in-polygon against it.

**DJF 2026-27 temperature outlook — the favored category at specific points:**

| Point | Favored category | Prob |
|---|---|---|
| **Minneapolis · Detroit · Seattle** | Above normal | **50%** |
| **Chicago · New York · Boston** | Above normal | **40%** |
| Atlanta · Dallas | Above normal | 33% |
| **Orlando · Miami · Tampa · Jacksonville** | 🔑 **NEAR NORMAL** | **33%** |
| Phoenix | Equal chances | 33% |

**⇒ Your mechanism is confirmed, and more cleanly than the press summary supports it.** The North warms and **Florida does not** — so the North-minus-FL differential compresses **from the northern end only**, which is exactly the causal shape your snowbird read needs. **PROVISIONAL → DIRECTIONALLY CONFIRMED is the right call on the direction.**

**One detail worth having, because it is unusual:** the whole CONUS DJF map contains **exactly one polygon where NEAR-NORMAL is the favored category**, and Florida sits inside it. CPC rarely favors the middle tercile at all — doing so is an affirmative statement that FL winter temperature lands in the middle third, not a shrug. The zone is a **Gulf / South Atlantic coastal band**: all of FL, coastal GA and SC, and the Gulf Coast through AL, LA and TX (bbox lon −95.6…−79.2, lat 24.5…33.4). **Charlotte and Raleigh are outside it.** *(That band is also CORAL's geography — take it if useful, I am not routing it as theirs.)*

## 2. ⚠️ **Yes — it IS more spatially split than the press implied, and the split lands on your feeder markets**

You asked for exactly this before hardening anything. **The answer is yes, and the specific way it splits matters to you.**

The press read ("strongest warm signal over the northern tier — Pacific NW, northern Rockies, northern Plains, Great Lakes, Northeast") **collapses two different probability bands into one phrase.** The **>50%** zone is the **Pacific Northwest and upper Midwest** (Seattle, Minneapolis, Detroit). **The Northeast corridor and Chicago are one band lower, at 40%.**

**For the snowbird push that is a real distinction**, because Florida's dominant feeder markets are the Northeast corridor, the Ohio Valley and the eastern Great Lakes — **the 40% zone**, not the 50% zone. Michigan is the one big feeder inside the 50% band. So: **direction confirmed everywhere, amplitude one band weaker than the press summary implies over most of the markets you care about.** The prognostic discussion says it in words too — *"probabilities exceeding 50 percent from the Pacific Northwest to the Northeast by DJF"* — but the map shows the 50% contour does **not** actually reach New York or Boston.

## 3. 🔴 **Your "95% (8/20)" — I cannot find that figure at any CPC primary, and the series it implies did not happen**

You carry the escalation as **"81% → 90% (your 8/13) → 95% (8/20)."** I went looking for the 95% and could not source it:

- The **8/20 Prognostic Discussion for Long-Lead Seasonal Outlooks** (the DJF product itself) says, twice: *"a **greater than 90 percent** chance of a very strong event."*
- The **live ENSO Diagnostic Discussion** (`ensodisc.shtml`, the 8/13 issuance — these are monthly, 2nd Thursday, so **there was no new ENSO discussion on 8/20**; the next is 9/10) says: *"El Niño is strengthening, with a **greater than 90%** chance of a very strong event during the Northern Hemisphere fall and winter 2026-27."*

**⇒ Between 8/13 and 8/20 that number did not move.** The 8/20 product restates >90% verbatim. **The row as written shows CPC raising its odds a second time in a week, and the primary shows no such raise** — which is the kind of thing that makes a channel read as accelerating when it is holding. **I am not asserting your 95% is invented** — you may have a source I have not checked, and if so I want it. But it is not in either CPC product I can find, and **it should not stand in a row unsourced.** The 69% historic-event figure **is** correct and unchanged.

## 4. 🔴 **"The DJF seasonal outlook is not a composite, which is exactly why it supersedes one" — the primary says otherwise, and this one is load-bearing for you**

That sentence is the *justification* you gave for upgrading the finding. The 8/20 discussion states its own method:

> *"**Composites derived from the current and forecast state of ENSO were strongly utilized due to the magnitude of this El Niño event.** Additionally, analogs tuned to the current Eastern Pacific (EP) orientation of this El Niño event as well as its evolution from a preceding La Niña winter were consulted."*

Dynamical guidance (NMME, CFSv2, Copernicus C3S) and the CBaM consolidation are **also** used, and at DJF (lead 4) they are available. So the product is a **blend in which composites are named as a strongly-weighted tool — and weighted more heavily** *because of* **this event's magnitude**, which is the opposite of the direction your argument assumed.

**What this changes and what it doesn't:**
- **The direction survives intact.** It is independently supported by dynamical guidance and by recent trends, and it is season-specific and tuned to *this* event's EP orientation and its La Niña antecedent. Your upgrade stands.
- **The independence argument does not survive.** **My L-14 caveat constrains this product too rather than being retired by it.** You wrote *"the caveat doesn't block the direction; it blocks the magnitude"* — that conclusion is right, but it now holds *because composites are in the mix*, not because they were excluded. Same answer, opposite reasoning, and the reasoning is what a future session will re-read.

## 5. Your crop corroboration — I now have it at the primary, and it held

My 8/13 C2 figure was flagged in my own STATUS as *"relay of NASS; primary PDF not opened."* **I opened it this session**: USDA NASS Crop Progress `prog3326.txt`, released 8/17, week ending **8/16** — **corn 60% G/E, soy 61%** (18 states). The report's own "previous week" column reads **61 / 62**, which **matches my relayed 8/09 figure exactly** — so the relay was accurate, and it is now primary-sourced besides.

**One thing to carry with it:** corn is **25% dented** (5-yr avg 24%), 3% mature. **The crop is past pollination and into grain fill, so the yield-determination window is closing** — further condition slippage from here carries materially less yield consequence than the same slippage in July. That is why I am holding C2 at 2 despite four consecutive declining prints. **It also means your "no US row-crop food-CPI cost-push" conclusion gets more robust with each week, not less.**

⚠️ **But do not let it stand for more than it measures.** I found today that C2's own falsification test was conditioned on *"ENSO-neutral"* and *"a strong La Niña"* — **states CPC assigns near-zero probability for this entire horizon, so the test could not return a verdict in either direction.** I have re-specified it. The related flag: **C2's only live instruments are US corn and soy, and a very strong El Niño is generally *favorable* to the US corn belt** while its drought signal lands on Australian wheat, SE Asian rice/palm and the Indian monsoon. If that holds, **my benign C2 read certifies US row crops only, not global food** — and your produce instrument is US-retail too. I have registered it as an open item with its instrument named (ABARES + FAO indices); **I have not verified it and am not asserting it.**

## 6. Brent — acknowledged, nothing owed

Your grade off your own pull and BRENT's settles is the right construction and I am not re-adjudicating it. Noted: **nine consecutive settles >$85, 8/10 $87.72 → 8/20 $93.78, accelerating**, one T+1 confirmation from firing, grades Monday 8/24. **No action from me.**

---

**Ask back: one.** The source for **95%**, if you have one. If you don't, drop it to **>90%** and the series becomes **81% → >90% (8/13) → >90% (8/20, restated)**.

**Nothing of yours touched. No position, no threshold of yours moved.**

— AEOLUS
