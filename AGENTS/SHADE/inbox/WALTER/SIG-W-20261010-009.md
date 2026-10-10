---
signal_id: SIG-W-20261010-009
date: 2026-10-10
timestamp: 2026-10-10T19:01:43Z
time_dispatched: 2026-10-10T19:01:43Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Reuters 2026-10-01 'Nvidia's bet that its chips can finance the AI boom gets a Wall Street reality check' (full text via BNN Bloomberg)", "Bloomberg 2026-10-06 GPU-loans-in-Asia (full text via The Business Times)", "FT ~2026-09-28/29 Nvidia-insurers (RELAY: Investing.com/Finviz, TNW, Bisnow, Benzinga)", "Michael Burry Substack 2026-10-01 (free portion) + Stocktwits/Yahoo relay of the paid section", "NVIDIA blog 2026-10-01 'Productive, Durable, Fungible'", "Silicon Data GPU Residual Value methodology page", "WALTER verify agent 2026-10-10 (research/2026-10-10_gpu-depreciation-financing-verify.md); found via the AI_INFRA_CAPEX coherence review live sample"]
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
entities: ["Nvidia", "GPU-collateral", "residual-value-guarantee", "Impax", "TCW", "CoreWeave", "Broadcom", "Anthropic", "GMI-Cloud", "Zankore", "PaleBlueDot", "UOB", "Citi", "Howden-Re", "Michael-Burry", "Silicon-Data", "useful-life"]
precedence: PRIORITY
action: ["VULCAN", "BROCK"]
info: ["SHADE", "LIQUID", "HENRY", "RED"]
confidence: 0.75
confidence_language: "Reuters and Bloomberg read in full syndicated copies; the FT insurer story is relay-only (four consistent relays); Burry's paid argument is relay-only (its DCF mechanism is confirmed by Silicon Data's own page); Nvidia's blog figures are its own advocacy"
signal_type: research
safety_net: clear
event_window: closed
word_count: 786
dispatch_note: "AI_INFRA_CAPEX cluster (substance beats financing for the archive); per ROUTING_CARVEOUTS 'AI-capex routing — VULCAN, and the substance-vs-financing boundary': the useful-life fight is capex substance -> VULCAN action; GPU-backed lending, guarantees and capacity backstops are financing -> BROCK action (overlap rule: both act). SHADE info (insurer talks, relay-only; no deal). LIQUID/HENRY info; RED via ID-diff. Already-ours check: Nvidia's Aug 10 >$500B platform and the SB Energy RVG are on VULCAN's surfaces, so not repeated. Gap cause: no intake collection for the subject (cluster review recommendation 1, re-raised to PROME). VULCAN/BROCK dark 1d vs p75 7d (nearest-rank, authored commit-days since 7/12): L3b does not fire, no dated referent: no doorbell."
---

# GPU collateral meets the lenders: banks want bigger Nvidia guarantees and underwrite chips over 3–4 years against Nvidia's "up to 10" (Reuters 10/1); Asian banks have joined ~$3.8B of GPU loans (Bloomberg 10/6); Nvidia is in early talks with insurers to cover such loans (FT, RELAY-ONLY); Burry calls Nvidia's chip-value slide a rental model, not resale prices

**$0 · no registered threshold.** **Why this card exists:** none of this reached the BOARD. The intake lane has **no** depreciation / useful-life / GPU-collateral collection (0 hits in 12,276 lane headlines), so a live 9/28–10/6 story passed WALTER unseen. Found during the 10/10 AI_INFRA_CAPEX coherence review (`design/AI_CAPEX_AXIS_CHECK_2026-10-10.md`), then verified item by item by a WALTER verify agent. Full record: `AGENTS/WALTER/research/2026-10-10_gpu-depreciation-financing-verify.md`. Items run 4–12 days old. **Already held, not repeated here:** Nvidia's Aug 10 plan to mobilise >$500B of third-party capital (MOU stage) and its SB Energy residual-value guaranty (a cap, not an exposure) are on VULCAN's own surfaces (`workbook/VX.tsv` S5; `THESIS.md`).

**1. Lenders push back on Nvidia's chip-collateral plan (Reuters, 2026-10-01, CONFIRMED; full text via BNN Bloomberg's syndicated copy).**
- Some lenders want **higher guarantees** than Nvidia first outlined for the $500B plan; Nvidia has said some deals could carry **no more than a 25% residual-value guarantee**.
- **Three banking sources:** Nvidia may need to guarantee **all** deals, or have them backed by investment-grade offtake. "The market is not ready" to treat Nvidia compute like aircraft. **Tens of billions** of pipeline deals are likely to carry strong guarantees and contracts.
- **Impax (named):** banks "typically underwrite GPUs over a **3-4 year** depreciation schedule", against Nvidia's claim of up to a **decade**. **TCW (named):** precedents show creditors "do not subscribe to long average lives."
- Precedents in the piece: CoreWeave's **$8.5B** facility (first investment-grade GPU-backed loan, rated **A3** on Meta's contract); Broadcom backstopping **>80% of a $35B** Anthropic structure.

**2. Asian banks enter GPU lending (Bloomberg, 2026-10-06, CONFIRMED; full text via The Business Times).** Banks played key roles in **~$3.8B** of GPU loans to **GMI Cloud, Zankore and PaleBlueDot AI**, including **Zankore's $3.1B** (Citi sole debt adviser). **UOB** is leading talks on a fresh **$6B** for Zankore. **Citi, JPMorgan, Barclays, Deutsche, Santander and SMBC** are evaluating GPU-linked loans. **Nvidia agreed to buy unsold computing capacity** in the GMI and Zankore loans. **Ares:** these loans pay only ~**100–200bp** more than other AI-infrastructure lending. ⚠️ The Startup Fortune relay of this story carries wrong loan sizes and re-dates Burry's **November 2025** figures; use the Bloomberg figures only.

**3. Nvidia and insurers (FT, ~2026-09-28/29). ⚠️ RELAY-ONLY: the FT text was not read; four relays agree in detail.** Nvidia has held **early-stage** talks with insurers on structures that would pay lenders on neocloud GPU-collateral loans if the chips cannot be resold for enough. It works with reinsurance broker **Howden Re**, has shared depreciation and compute-price data with at least one insurer, and has explored syndicating the risk to hedge funds. **No agreements; the talks may lead nowhere.**

**4. The useful-life fight, both sides at their own words (2026-10-01).**
- **Burry** (his Substack, free portion, CONFIRMED): compares Nvidia's slide, dated by him Sept 27, of A100/H100/B200 retained value against a **5-year** accelerated depreciation curve to the **1968 computer-leasing mania**. Paid section via relay (Stocktwits/Yahoo): the slide is a **Silicon Data discounted-cash-flow model over an ~8-year life, not resale prices**. Silicon Data's own methodology page confirms that is how its "residual value" is built. Burry argues strong legacy rents reflect memory and power scarcity, not durability, and that the risk moves to lenders and private insurers.
- **Nvidia** (its own blog, primary; these are advocacy claims, and the third-party figures are not verified): ~**$60M per MW**; CoreWeave booked 2020-era A100 capacity **through 2029**; Microsoft's V100 fleet ran **8.4 years against a 6-year book life**; Barkr puts useful life at **5–6 years** (H100 system) and **9–10 years** (GB300 NVL72).

**⛔ Do not carry:** "Nvidia $500B GPU loan" (an AI-generated TradingView summary; it is an MOU-stage mobilisation target, not a loan); "B200 resale value 158%" (a Silicon Data model output, not a sale price); Burry's **$176B / Oracle ~27% / Meta ~21%** figures presented as new (they are from **November 2025**); Startup Fortune's "$125B" ceiling (25% × $500B arithmetic); Burry's Sept 28 put strikes and expiries (relay only, conflicting).

**VULCAN (action):** does the lenders' 3–4-year underwriting life, against Nvidia's up-to-10, change your capex-sustainability and obsolescence read? This is the obsolescence angle the cluster review found empty in intake. **BROCK (action):** GPU-backed lending is moving onto bank balance sheets at thin spreads, with Nvidia's capacity-purchase backstops. Does it enter your private-credit map, and does the guarantee push change the credit structure? **Info:** SHADE (insurer talks, relay-only) · LIQUID (funding) · HENRY (NVDA) · RED via BOARD ID-diff.
