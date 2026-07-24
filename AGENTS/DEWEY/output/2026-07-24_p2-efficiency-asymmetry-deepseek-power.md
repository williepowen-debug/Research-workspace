# China-strategic-exhaustion P2 (DEWEY carve-out): efficiency asymmetry — DeepSeek real TCO + US/China power-cost primaries

**Date:** 2026-07-24 | **Mode:** Thesis | **Confidence:** High (both viral framings refuted against primaries; SemiAnalysis TCO + EIA/NBS/SAFE power data) / Med (sited-region China data-center power rates — regional, not a single national figure)

**Scope note — DEWEY primary-pull carve-out of P2, NOT the P2 judgment.** Per the Will-approved Batch-3 packet, DEWEY owns *only* two named primary pulls: (1) the **real DeepSeek total-cost-of-ownership** (vs the viral $5.6M), and (2) **US-vs-China electricity/power-cost** primaries. The efficiency-asymmetry adjudication (is the US spending *inefficiently* vs a cheaper China?) is **VULCAN/WATT/ZHAO/HENRY's** — I supply the cited spine and correct two load-bearing viral numbers.

---

## Key Finding

**Both headline framings the P2 mechanism rests on are wrong as stated — and each hides a real signal.** (1) DeepSeek's "$5.576M" is real but measures only the *marginal* GPU pre-training run; the **total cost of ownership is ~$1.3–1.6B** (SemiAnalysis: ~$1.6B server capex + ~$944M cluster opex, ~50,000 Hopper GPUs) — **~250–290× the headline.** DeepSeek demonstrates a *genuine marginal-efficiency edge* (MoE/MLA/FP8, ~2k-GPU main run) *on top of a ~$1.6B infrastructure base* — not a $5.6M frontier model. (2) "China's electricity is half the US" is **refuted at the industrial average**: US industrial ~**8.62¢/kWh** (2025) vs China ~**9.7¢** — China is comparable-to-slightly-higher. The real power asymmetry is **not price but buildout speed and queue**: China added **543 GW** of capacity in 2025 vs the US's **~53 GW (~10×)**, and US data-center power is constrained by an interconnection queue (**700 GW of 2025 requests — more than total 2023 US consumption of 477 GW**) that shows up as *time-to-power* and marginal/capacity-cost premiums (PJM capacity +10×), not average price. **Net for the P2 mechanism: the "US overspends inefficiently vs a cheap China" story does NOT hold on raw price/training-cost; it has a live form only on (a) time-to-power / grid-buildout speed and (b) whether US capex is *sterile* (FCF-cliff — P1's domain).**

---

## Evidence

### 1. DeepSeek real total cost of ownership (leg 1)

| Measure | Figure | What it includes | Source |
|---|---|---|---|
| DeepSeek's official claim | **$5.576M** | DeepSeek-V3 "official training" / GPU **pre-training rental only**; *explicitly excludes* prior research, ablations, architecture/algorithm/data experiments (their own caveat) | [PRIMARY: DeepSeek-V3 technical report, via CNBC/Reuters Jan 2025] |
| **SemiAnalysis TCO** | **~$1.6B server capex** + **~$944M** cluster opex; hardware spend "well higher than $500M" | Full fleet ~**50,000 Hopper GPUs** (~10k H800 + ~10k H100 + H20 orders); R&D, infra, operations | [INSTITUTIONAL: SemiAnalysis, "DeepSeek Debates," Jan–Feb 2025] |
| Alternate estimate | **~$1.3B** | Total-cost reconstruction | [INSTITUTIONAL: research cited by Interesting Engineering / Bufithis, Feb 2025] |

> **The discipline point (P1 flagged $5.6M as "overstated" — this confirms *how*):** the $5.6M and the $1.6B are **both true and measure different things.** $5.6M = the marginal cost of the final pre-training run (and DeepSeek's efficiency work making that run cheap is *real*). $1.3–1.6B = the fleet + R&D + opex that had to exist first. **The viral claim fuses a real marginal number with a false total** (`finding_relabeled_number_viral_stat`). For P2: DeepSeek is evidence of a **real algorithmic-efficiency edge**, NOT evidence that frontier capability now costs ~$5M — so it does *not*, by itself, prove "the US is grossly overspending." SemiAnalysis itself noted DeepSeek's *operational* cost could fall ~5× by end-2025 on efficiency — the edge is in marginal inference/training cost, on a nine-figure base.

### 2. US-vs-China electricity / power-cost primaries (leg 2)

**Price level — averages are comparable (refutes "China is half"):**

| Metric | US | China | Source |
|---|---|---|---|
| Industrial electricity, 2025 avg | **8.62¢/kWh** (2024: 8.13¢; mid-2026 ~9¢, +8.6% YoY) | ~**9.7¢/kWh** (2025 proj.); ~11.6¢ business (Apr-2026) | [PRIMARY/INSTITUTIONAL: EIA via Statista; GlobalPetrolPrices; China-Briefing] |
| Data-center-state retail avg (2025) | top-10 DC states **14.46¢** vs **14.39¢** all others (≈ identical) | sited regions (Inner Mongolia/Xinjiang) far below national avg (off-peak) | [INSTITUTIONAL: RealClearEnergy Feb 2026; China-Briefing] |

**Capacity & speed — where the real asymmetry lives:**

| Metric | US | China | Source |
|---|---|---|---|
| **New generating capacity added, 2025** | **~53 GW** (largest since 2002); 86 GW planned 2026 | **543 GW** (~10×); >430 GW wind+solar; ~$500B in one year | [PRIMARY: EIA; INSTITUTIONAL: OilPrice/CarbonCredits/Xinhua] |
| Cumulative / mix | total generation 4.43 PWh (+2.8% YoY) | cumulative PV 1.2 TW; renewables >60% of capacity; non-fossil passed thermal | [PRIMARY: EIA; NBS/Xinhua Jan 2026] |
| **Interconnection queue / constraint** | **700 GW** of DC interconnection requests in 2025 (> total 2023 US consumption 477 GW); ERCOT 198 GW large-load Q1-2026; PJM capacity prices **+10×**, DCs = 63% of 2025/26 auction rise ($9.3B); utilities sought **$29B** rate hikes H1-2025 (2× YoY) | state-directed siting + grid; no comparable market-queue constraint | [INSTITUTIONAL: IEEFA; Ascend Analytics; EESI; Utility Dive] |

> **Corrected mechanism:** the packet's premise ("China's cheaper electricity") is **wrong on price** and **right on capacity/speed/time-to-power.** China isn't paying less per kWh on average — it is adding generation ~10× faster and can *site* compute into ultra-cheap-power regions on a state-directed grid, while US data centers hit a binding interconnection queue that converts into delay + marginal/capacity-cost premiums + rate-base socialization. **Power is a real cost-asymmetry axis — via speed and queue, not headline price.**

### 3. Out of this carve-out's scope (→ owner agents, flagged not dropped)
- **Export-control *direction* — who bears the inefficiency** (US subsidized-redundant-fabs vs China indigenization/stockpiling/yield-loss): ZHAO/VULCAN judgment leg; no primary pulled here.
- **Is US AI capex productive or sterile (depreciation / GPU-obsolescence / FCF-cliff):** already evidenced in **P1** (Oracle −$23.7B FCF, CoreWeave debt tripled/−$7.3B FCF, NVIDIA circular non-marketable-securities $22→43B). HENRY/VULCAN own the "sterile-spend" judgment; I cross-reference P1 rather than re-derive.

---

## Counter-Evidence

1. **DeepSeek's efficiency edge is real and cuts toward "US overspends."** The MoE/MLA/FP8 innovations genuinely lower marginal cost; if US labs are not adopting equivalent efficiency, some US spend *is* inefficient. The refutation is only of the *magnitude* ($5.6M ≠ frontier cost), not of the *existence* of an efficiency gap.
2. **US average-price stability may be temporary.** Top-10 DC-state retail is still ≈ national avg (14.46 vs 14.39¢), but PJM capacity +10× and 700 GW of queue suggest the marginal cost is moving ahead of the average — the price asymmetry could *emerge* even though it isn't in the 2025 average.
3. **China's speed advantage has quality caveats.** Much of the 543 GW is intermittent wind/solar (>430 GW) needing firming/storage; nameplate capacity ≠ dispatchable data-center power. The 10× is a capacity-additions number, not a firm-power-for-compute number.
4. **Cheap sited power ≠ cheap compute.** China's compute is constrained by *chips* (export controls), not power; the US is constrained by *power*, not chips. The binding constraint differs by country — which complicates any single "who spends more efficiently" verdict.

---

## Source Quality Assessment

**High** on the DeepSeek TCO (SemiAnalysis is the primary institutional teardown; DeepSeek's own report is the source of the $5.6M and its caveat) and on the capacity-additions + queue figures (EIA primary US; NBS/Xinhua China; IEEFA/Ascend on the queue). **Medium** on China's data-center-sited power rates — these are regional/off-peak and vary; I have the national industrial average (~9.7¢) and the qualitative sited-region-cheap point, not a single audited data-center tariff. The joaonevesanalytics comparative series is paywalled (used EIA/Statista/GlobalPetrolPrices instead).

---

## References (accessed 2026-07-24)

- SemiAnalysis "DeepSeek Debates": https://newsletter.semianalysis.com/p/deepseek-debates ; CNBC Jan 31 2025: https://www.cnbc.com/2025/01/31/deepseeks-hardware-spend-could-be-as-high-as-500-million-report.html ; Techstrong: https://techstrong.ai/agentic-ai/early-critic-of-deepseek-says-model-cost-was-1-6-billion-not-5-6-million/
- US industrial electricity price (EIA via Statista): https://www.statista.com/statistics/190680/us-industrial-consumer-price-estimates-for-retail-electricity-since-1970/
- China industrial power: https://www.globalpetrolprices.com/China/electricity_prices/ ; https://www.china-briefing.com/news/chinas-industrial-power-rates-category-electricity-usage-region-classification/
- DC electricity by the numbers: https://www.realclearenergy.org/articles/2026/02/12/datacenters_and_electricity_costs_by_the_numbers_1164350.html
- China 543 GW: https://oilprice.com/Latest-Energy-News/World-News/China-Added-543-Gigawatts-in-New-Power-Capacity-in-2025.html ; Xinhua renewables >60%: https://english.news.cn/20260130/0d9614228f9d4ee6aee081bb4f3b6449/c.html
- US capacity/generation records (EIA): https://www.eia.gov/todayinenergy/detail.php?id=67284 ; https://www.eia.gov/todayinenergy/detail.php?id=67205
- Interconnection queue / PJM: https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10 ; https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access
- Fortune "US grid so weak the race may already be over": https://fortune.com/2025/08/14/data-centers-china-grid-us-infrastructure/

---

## Process Report

**Searches run:** ~6 WebSearches + 2 WebFetches. DeepSeek TCO and US capacity/queue data came clean; China sited-region data-center tariffs were the one soft spot (regional, no single audited figure).
**Data gaps:** (a) a single audited China data-center power tariff (only national industrial avg + qualitative sited-region cheap); (b) firm/dispatchable-power split of China's 543 GW (much is intermittent); (c) export-control-direction + sterile-capex judgment — out of carve-out scope (owner agents; sterile-capex cross-referenced to P1).
**Source frustrations:** joaonevesanalytics comparative series paywalled; had to reconcile the "China power is half" claim (globalelectricity.org) against EIA/Statista — it does not hold at the industrial average, an important refutation.
**Confidence in findings:** High that both viral framings ($5.6M; "half-price power") are wrong-as-stated, and that the real edges are marginal-algorithmic-efficiency (on a $1.6B base) + grid-buildout-speed/queue. Medium on the exact China DC-power cost.
**If I had more time/tools:** an audited China data-center tariff (Inner Mongolia/Xinjiang) and a firm-vs-intermittent split of the 543 GW would sharpen the power axis; a SemiAnalysis subscription would confirm the $1.6B teardown line-by-line.
**Suggestions:** VULCAN/WATT should treat **time-to-power / interconnection queue** (not ¢/kWh) as the operative US disadvantage; and treat DeepSeek as an *efficiency-edge* signal, not a *cost-collapse* one — do not let "$5.6M" propagate into any cost-to-capability ratio.

---

*DEWEY carve-out feeding P2 (VULCAN lead · WATT power-axis · ZHAO export-control-direction · HENRY FCF). Companion to P0/P1/P3 (all 2026-07-24). Provenance: Will-approved Batch-3, deferred to fresh session (heavy-run ceiling), Will directed P3-then-P2. Auto-memory: `finding_relabeled_number_viral_stat`, `finding_audit_the_founding_metaphor_first`, `finding_number_carries_threshold_unit_source`.*
