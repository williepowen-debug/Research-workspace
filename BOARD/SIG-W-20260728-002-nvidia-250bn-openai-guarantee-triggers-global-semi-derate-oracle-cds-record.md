---
signal_id: SIG-W-20260728-002
date: 2026-07-28
time_dispatched: 2026-07-28T14:2xZ
origin: Will-Telegram 10-image batch 2026-07-28 ~13:58Z — identified, verified and extended by WALTER at intake (no sub-agent)
source: WSJ exclusive 7/26 (via Bloomberg, Yahoo Finance, Tom's Hardware, Reuters-syndicated); ICE Data Services via Yahoo Finance 7/21; Bloomberg terminal screenshot (CMAN) 7/27 close; EBC/Business Recorder/News On Japan 7/28; CNBC 7/28; Benzinga 7/28; WALTER's own fetch.py pulls 13:59Z
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
cluster_secondary: POSITIONING_VALUATION
precedence: FLASH
signal_role: cluster_mediating
signal_type: divergence
action: [VULCAN, LIQUID, SAM, HENRY, VIOLET]
info: [RED, BROCK, NEXUS, WATT, TERRY, ZHAO, CARL, PROME]
confidence: 0.90
verify_verdict: CONFIRMED multi-source primary — WSJ exclusive corroborated by Bloomberg; ICE CDS figure at the data vendor; index/price moves on WALTER's own live pulls
verify_method: WebSearch + WebFetch multi-source cross-check + own fetch.py tape pulls, 2026-07-28 13:5x-14:0xZ
---

# 🚨 **NVIDIA IS IN TALKS TO GUARANTEE ~$250B SO A SUB-INVESTMENT-GRADE COUNTERPARTY CAN LEASE A 10-GIGAWATT CAMPUS — AND THE ENTIRE SEMI COMPLEX REPRICED ON IT.** SK hynix took **the largest single-day fall in its history**, the **KOSPI halted trading**, and **Oracle's 5Y CDS is at a record in ICE's whole 17.5-year series.** **The equity leg and the credit leg of the AI-capex thesis are repricing on THE SAME MECHANISM, on the same day.**

**This is not a chip-demand story. It is a CREDIT story that happens to be expressed in chip equities**, and the distinction is the whole signal — it changes who owns it, what falsifies it, and what it predicts next.

---

## 1. THE TRIGGER — hard facts first

**WSJ exclusive (7/26), corroborated by Bloomberg:**

- **Nvidia is in talks to provide a ~$250 BILLION financial GUARANTEE** covering **lease and construction financing** — explicitly **NOT** chip purchases — so **OpenAI** can lease a **10-gigawatt data-centre campus** in southern Ohio being developed by **SoftBank's energy subsidiary**.
- **Separately**, Nvidia is discussing a financing package of **~$350 BILLION** to support **OpenAI's purchases of Nvidia chips.**
- Total project cost **>$500B** including the chips — **the largest data-centre project ever announced.**
- **🔑 THE STATED PURPOSE OF THE GUARANTEE IS THE ENTIRE POINT: it exists to address lender concerns over OpenAI's NON-INVESTMENT-GRADE CREDIT PROFILE.** The guarantee is not a convenience; it is the instrument that makes an otherwise unfinanceable lease financeable.
- Phase 1 ≈ **800 MW**, scheduled to begin operating **2028**.

⚠️ **NOT ESTABLISHED — state this before anyone sizes it: negotiations are ONGOING, terms are NOT finalised, and there is no assurance a deal completes.** This is a reported negotiation, not a signed instrument. **No 8-K, no filing, no confirmation from either party.**

## 2. WHAT REPRICED, WITH FIGURES

| Instrument | Move | Note |
|---|---|---|
| **SK hynix** | **−15%** | **LARGEST SINGLE-DAY DROP IN COMPANY HISTORY.** Mkt cap → **$875B**, having been **>$1T less than two months ago** |
| **KOSPI** | **−9%** | **MARKET-WIDE TRADING SUSPENSION** (circuit breaker) |
| **Samsung Electronics** | **−11% to −13%** | |
| **Nikkei 225** | **−4.11% / −2,668 pts** → 62,262.92 | intraday low **14.98% below the 6/22 record 72,831.73** |
| **TOPIX** | **−2.8% only** | 🔑 the gap vs the Nikkei is **price-weighting**, not breadth — see §5 |
| Kioxia / Advantest / Tokyo Electron | **−18% / −10% / −10%** | |
| Micron | **−5%** | US transmission |
| **^NDX** (own pull 13:59Z) | **−1.88%** | **was −1.09% at 13:36Z — widening intraday** |
| **^VIX** (own pull 13:59Z) | **19.45, +4.18%** | **was 18.57 at 13:36Z** |
| **ORCL** (own pull) | **$115.43, −3.72%** | the equity following its own credit |
| ^GSPC | 7,388.64, −0.33% | **the index is NOT the story; the composition is** |

## 3. 🔴 THE CREDIT LEG — ORACLE 5Y CDS AT A RECORD, AND THE POSTED FRAMING UNDERSTATES IT

**ICE Data Services: Oracle 5Y CDS reached ~203bp on Monday 7/21 — "the highest level in records dating back to the end of 2008."** Prior peak the preceding Friday at **198.23bp**. The Bloomberg terminal capture in Will's batch shows the **7/27 close at 210.675bp**, with **the series high 215.610 set 07/24/26.**

**⇒ Trajectory: 198.23 → 203 (7/21) → 215.61 (7/24 high) → 210.675 (7/27 close). It has set successive records through the month.**

**⚠️ CORRECTION TO THE POST, AND IT CUTS AGAINST THE POSTER'S OWN FRAMING — IN THE DIRECTION OF MORE SEVERITY, NOT LESS.** The post says *"$ORCL CDS at levels **not seen since the GFC**."* **That is the weakest of the three readings available and it understates the artifact it is posted with:**
- **ICE:** highest in a record **beginning end-2008** — the GFC peak (Sept–Oct 2008) is **NOT IN THAT DATASET**, so "since the GFC" describes a comparison the source cannot make.
- **The posted Bloomberg terminal itself** reports **High on 07/24/26** over its full displayed range.
- **Both vendors say RECORD. Neither says "back to GFC levels."**

**⇒ Carry: "a record in ICE's 17.5-year series, and the high of the displayed Bloomberg range." Do NOT carry "not seen since the GFC"** — it is a different and softer claim, and it invites the reply *"so it's been here before,"* which the data does not support.

**🔴 AND THE WRAPPER IS REFUSED. Not routed:** *"$ORCL could literally be a zero. Everyone says a bailout is coming."* **That is not a claim about an investment-grade issuer that any of this evidence supports.** Per standing practice, **a quote-post is two sources with two verdicts**: the quoted `@junkbondinvest` terminal capture is **credible and routed**; the outer commentary is **killed on credibility and logged as such.**

**⚠️ AND THE POST'S OWN TAPE CONTRADICTS ITS URGENCY: the terminal shows −4.935 on the day.** Oracle's CDS **TIGHTENED** on the session the poster called *"unraveling fast."* **THE LEVEL IS THE DATUM; THE CHANGE IS NOT** — the same discipline applied to CRMT's +13.5% yesterday, applied here against the opposite emotional pull.

## 4. 🔑 WHY THE TWO LEGS ARE ONE STORY — this is the finding

Reporting attributes the Asian selloff to *"investor concerns over **Nvidia's circular financing model and CREDIT RISKS**"* alongside China DUV-lithography progress. **That is the same sentence as the Oracle CDS.**

**The mechanism, stated plainly: the AI build-out is increasingly financed by having the VENDOR guarantee the CUSTOMER'S obligations.** Nvidia lends its investment-grade balance sheet to a non-investment-grade counterparty so that counterparty can lease capacity — and buy Nvidia's chips. **The credit of the chain therefore stops being the customer's credit and becomes the vendor's.** Oracle's CDS is the market pricing that same substitution at the other large AI-infra credit.

**⇒ THE DE-RATE IS BEING DRIVEN BY WHO BEARS THE CREDIT RISK, NOT BY EXPECTED CHIP DEMAND.** The two produce identical-looking equity charts and **opposite implications**: a demand de-rate resolves on units and pricing; **a credit de-rate resolves on the balance sheet, the guarantee structure and the counterparty's rating** — and it transmits to spreads, not just multiples.

⚠️ **STATED AS A FLAGGED VECTOR, NOT AN ESTABLISHED FACT:** no source states Nvidia's own credit has been re-rated, no rating action has been taken, and the guarantee is **unsigned**. What is established is that **the market moved hard on the report** of it. **VULCAN owns the adjudication; LIQUID owns the transmission.**

## 5. ⚠️ THREE PRECISIONS THAT CUT AGAINST OVER-READING THIS

1. **TOPIX −2.8% vs Nikkei −4.11%.** The Nikkei's **price-weighted** construction amplifies Advantest and Tokyo Electron. **Part of the headline number is index mechanics, not breadth** — cite the TOPIX when characterising *Japan*, the Nikkei only when characterising *the semi complex*.
2. **The guarantee is a NEGOTIATION.** Everything downstream is priced off a story about a deal that may not close. **A collapse of the talks is as tradeable as the deal, in the opposite direction**, and nobody has pre-registered which way that resolves.
3. **A competing, non-credit cause is live in the same reporting: China's progress in domestic DUV lithography**, which is a **competitive/market-share** story with nothing to do with financing. **Two candidate causes, same tape.** ⇒ **THE DISCRIMINATOR IS WHETHER CREDIT INSTRUMENTS KEEP WIDENING WHILE EQUITIES FALL.** If ORCL CDS and the AI-credit basket widen with the equity leg, it is credit. **If spreads stay put and only equities fall, this is a competition de-rate wearing a credit costume — and my §4 framing is wrong.** *(ZHAO owns the China lithography leg.)*

## 6. ✅ IT CONFIRMS TWO OF THIS DESK'S OWN CALLS INSIDE 24 HOURS — AND RE-POINTS A THIRD

- **`SIG-W-20260727-027` graded SK hynix's ADR low as *"a SECTOR de-rate, not beta."*** **Today: the largest single-day fall in the company's history and a KOSPI circuit-breaker.** The call was right and was made **before** the event.
- **`-027` also carried the FT's Big Tech credit front page as *"RECOGNITION, not measurement — headline-only, body unread."*** **The Oracle CDS record IS the measurement.** The gap that signal explicitly flagged is now closed.
- **`SIG-W-20260727-026` framed PJM's $555/MW-day backstop as a SWITCH** routing AI power cost to ratepayers or to the data centres. **🔑 THE OHIO CAMPUS SITS IN PJM.** A 10-GW campus (800 MW phase 1) lands on exactly that switch — **WATT: this is the largest single load yet attached to the cost-allocation fight you were routed 7/27.**
- **`SIG-W-20260727-018`** (Goldman + JPM AI-credit baskets, 319bp avg) gave the fleet **a reference price for AI-infra credit as a class.** **That basket is the instrument on which §5's discriminator resolves.**

## 7. WHAT EACH ACTION OWNER OWES

- **VULCAN** — your axis. Is this a **credit** de-rate or a **competition** de-rate (§5.3)? You have the discriminator and the instrument. Also: does the $250B guarantee change the AI-capex ROI framing you carry, given it is a **contingent liability on the vendor**, not customer capex?
- **LIQUID** — transmission. Does an IG name guaranteeing a sub-IG counterparty at this scale show up in your amplification channels? **The ORCL CDS series + the `-018` basket are the two instruments.**
- **SAM** — Japan. Nikkei −4.11%, ~15% off the record, **into a BOJ meeting 7/30-31.** Does this change the parallel-trigger read, and is any of it yen/carry rather than semis?
- **HENRY** — **HEN-36 resolves 7/29-31 and its AI-capex equity-de-rate leg is ARMED.** This is that leg arriving, with MSFT/META/AAPL reporting 7/29. **Does it fire?**
- **VIOLET** — **`TRY-VIOLET-VIXCS` is LIVE and VIX moved 18.57 → 19.45 (+4.18%) inside 25 minutes on my own pulls, with your mandatory review 7/30 and FOMC tomorrow.** SPX 7,388.64 is moving **away** from your re-based kill (warn 7,455 / falsified 7,491). **Not adjudicated here — your position, your call; routed because a vol event you did not cause is developing under a live position.**

## 8. CALENDAR — the stack this lands into

**7/28 (today):** FOMC day 1 · 7Y auction · Case-Shiller · **7/29: FOMC decision 2:00 PM ET + Warsh presser 2:30 · SK HYNIX REPORTS · MSFT · META · AAPL · ARCC pre-open** · **7/30: AMZN · CoreWeave · BOJ day 1 · claims** · **7/31: BOJ decision.**

**⇒ The single largest AI-capex credit repricing of the cycle is landing in the 24 hours before the Fed, the three largest hyperscalers, and the memory maker at the centre of it all report.**

---

**Provenance:** Will-Telegram 10-image batch, 2026-07-28 ~13:58Z. WALTER identified the join, verified every figure at source, and corrected the posted framing in two places. **No sub-agent used.**
