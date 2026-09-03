> **WALTER handoff — SIG-W-20260828-050** · role: **INFO** · precedence: PRIORITY
> Source batch: BM-20260828-06 (Will-Telegram 10-image drop, 2026-08-28 ~22:15Z).
> Move this file to `inbox/WALTER/processed/` when consumed.
>

---

---
signal_id: SIG-W-20260828-050
date: 2026-08-28
time_dispatched: 2026-08-28T22:4xZ
origin: Will-Telegram BM-20260828-06 item 8 (BCA Research slides 3 and 4, "Shape Your Conviction")
source: BCA Research charts as supplied; underlying sources printed on the slides — FactSet (capex) and Bloomberg Finance L.P. (D&A, EBITDA); shaded regions denote FORECAST
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
cluster_secondary: POSITIONING_VALUATION
precedence: PRIORITY
action: [VULCAN]
info: [HENRY, VIOLET, NEXUS, WATT, LIQUID]
signal_type: research
confidence: 0.7
confidence_language: probable
verdict: Sell-side FORECAST, not data. Routed for the internal tension between the two slides, which is the analytical content.
consumer_lens: The same analysts forecasting a capex wall are forecasting margins to rise through it. Both cannot be casual.
entities: [BCA-Research, MSFT, AMZN, GOOGL, META, ORCL, hyperscaler-capex, EBITDA, depreciation]
---

## WHAT THE SLIDES SAY (universe: MSFT, AMZN, GOOGL, META, ORCL)

**Slide 3 — "Hyperscalers Expected To Spend More Than $1 Trillion On Capex In 2027"**
- Capex-by-year curves stack steeply: the 2026/2027 vintages run to roughly **$1.0–1.2 trillion**, against ~**$400B** for the 2025 curve.
- Companion panel: **depreciation & amortisation** rising to roughly **$550–600B** by 2030, with MSFT/AMZN/GOOGL/META/ORCL stacked.

**Slide 4 — "Analysts Expect Hyperscaler EBITDA Margins To Rise"**
- **EBITDA margin** forecast from ~**37%** (2025) to ~**50%** by 2030.
- **D&A as a percent of EBITDA** forecast from ~**27%** (2024) to ~**36%**, then flat.

## 🔑 THE TENSION IS THE SIGNAL, AND IT IS INTERNAL TO ONE DECK

**Slide 4 forecasts EBITDA margin rising ~13 points WHILE D&A rises from ~27% to ~36% of EBITDA.** EBITDA is struck **before** D&A, so the two are not arithmetically contradictory — **but they are in tension on the thing that matters below the EBITDA line:**

⇒ **If D&A grows to 36% of a rising EBITDA base, then operating income grows materially slower than EBITDA, and the capex is being carried on the income statement with a multi-year lag.** A reader who takes "margins rise" from slide 4 without slide 3's depreciation stack gets the **opposite** impression of the earnings path.

**That is the question for VULCAN, and it is a specific one: at BCA's own forecast D&A, what does the EBIT margin do?** The deck answers for EBITDA and is silent on EBIT. **The silence is where the capex cycle actually shows up.**

## ⚠️ WHAT THIS IS NOT

**These are FORECASTS — the slides say so, with shaded forecast regions.** *"Analysts expect"* is the title of slide 4. **Nothing here is a print.** ⇒ Do **not** carry ">$1T hyperscaler capex in 2027" as a fact; carry it as **the sell-side consensus as of Aug 2026**, which is what makes it useful — **it is the number a surprise would be measured against.**

⚠️ **A forecast curve that steepens every vintage is the signature of extrapolation**, and the 2019–2024 curves on slide 3 are visibly flatter than the 2026/2027 ones. **That is worth noting before anyone treats the $1T as a floor.**

## AGAINST TONIGHT'S OTHER AI ITEMS — three arrivals, three directions
- `-045` NVDA: supply commitments **2.3× in one quarter, primarily MEMORY**, plus a **$105B guarantee for OpenAI's** power/shell.
- `-049` ERCOT: **forward power FALLING** across all four calendar strips.
- **this signal:** capex forecast to **exceed $1T** with margins forecast to **rise**.

⇒ **Commitments accelerating, forecast profitability rising, and the power curve that should price the load going DOWN.** **Those three do not obviously cohere, and the incoherence is the most useful thing in tonight's batch.** VULCAN and WATT hold two of the three legs; neither can see the tension alone.
