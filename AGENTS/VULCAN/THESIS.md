# VULCAN — THESIS (per-channel transmission tables)

**The one-line thesis:** the AI-capex buildout is the single largest systemic vector in the tape — it concentrates index risk into a handful of megacaps, its FCF math gates the whole AI trade, its compute demand collides with a supply-constrained grid, and its supply chain funnels through Taiwan; VULCAN owns the *mechanism* that drives all four.

*Richness lives here; STATUS.md carries the live 5-pt matrix. Each channel is `event → mechanism → repricing` with a stage table (state ∈ confirmed / open / falsified).*

---

## S1 — AI-capex concentration (the core — the reason the seat exists)

| Stage | Mechanism | State |
|---|---|---|
| 1 | Hyperscalers ramp AI-capex (MSFT/GOOGL/AMZN/META) | confirmed |
| 2 | Megacap earnings + market cap concentrate → Mag-7 dominates index weight | confirmed (VIOLET Path-B 🔴) |
| 3 | Index becomes single-factor: breadth narrows, correlation-1 risk | **open — and as of 2026-08-21 MEASURED FOR THE FIRST TIME, RUNNING AGAINST THIS STAGE.** Breadth = **RSP/SPY 63d relative return +5.17pp, 97.6th percentile** [own pull, **refreshed 2026-08-24**; was +5.18pp as-of 8/20 — **unchanged in substance across four sessions of a violent semi de-rate, which is itself the finding**]: equal-weight is strongly **OUTPERFORMING**, i.e. breadth is **BROADENING**, not narrowing. ⚠️ This stage was unmeasured until today — my S1 instrument was level-only, which also made the red band (*≥40% AND breadth collapse*) **untrippable by construction**. ⇒ **The stage is not falsified — a stage is a mechanism, and one reading is a state, not a verdict — but it is now instrumented and the instrument disagrees with it.** Collapse threshold **≤ −7.5pp** (base-rated: 5 distinct episodes in 23.3yr). Retained in `workbook/MAG7_SERIES.tsv` so this can become a trend rather than a point. [KB-103] |
| 4 | Capex ROI question OR a capex cut → concentration unwinds → index-wide repricing | open (the systemic event) |

**Repricing:** the megacap-concentration vol expression (→ VIOLET Path-B), HEN-36 FCF (→ HENRY). **Confirms/breaks:** capex guides raised + FCF holding at the 7/22–7/29 stack confirms; a capex cut YoY with Mag-7 >40% fires the unwind. This is the cleanest bidirectional flip.

### PRE-PRINT BASELINE (quantified 2026-07-12, ahead of the 7/22-7/31 cluster)

> ⚠️ **HISTORICAL RECORD — THE CLUSTER RESOLVED 2026-07-31. Retained deliberately as the pre-print baseline (it is the frozen reference VULCAN-01 was graded against); do NOT read the "Next print (the gate)" column as forward.** *(Banner added 8/21 — the table had read as forward for three weeks.)*
>
> **Outcome:** **VULCAN-01 HIT — capex net RAISED, S1 NOT-FIRED on the cut rule.** Final FY26 guides: **AMZN ~$220B** (raised from ~$200B, the biggest mover) · **GOOGL $195-205B** · **MSFT ~$190B economic** (⚠️ the **$175B headline is a lease RECLASS, not a cut** — building useful life 15→25y eff. FY27 shifts future DC leases finance→operating) · **META $130-145B**. **Aggregate ~$735-760B economic vs the $710-725B baseline below** = ~$25-40B ABOVE. Also resolved on that one catalyst — **root counted ONCE** — VULCAN-03 HIT (GOOGL 7/22) · -04 HIT (SK Hynix **7/29**) · -06 HIT (→WATT) · **-07 NOT-FIRED (0-of-4 useful-life changes, all SEC-primary)** · **-09 NOT-CONFIRMED → downgraded to a watch-line** (MSFT +8.88% and AMZN +7% both *rewarded* raises; the GOOGL 7/22 punishment did not generalize). [KB-041..046]

**Per-hyperscaler: last reported quarter (calendar Q1 2026, all reported 2026-04-29) + FY2026 capex guide**

| Co. | Q1 CY26 capex (actual) | vs consensus | FY26 capex guide (as of Q1 print) | Q1 CY26 FCF | FCF trend | Next print (the gate) |
|---|---|---|---|---|---|---|
| MSFT | $31.9B (+finance leases, +49% YoY) | **miss** ($34.9B Visible Alpha consensus) | **~$190B** (raised; ~$25B = component-price effect) | $15.8B | −22% YoY | **7/29/26** (FQ4, guided capex >$40B) |
| GOOGL | $35.67B | — (raised guide overshadowed) | **$180-190B** (raised from $175-185B) | $10.1B | margin 21%→9.2% YoY | **7/22/26 after close — first gate of the whole cluster** |
| AMZN | $43.2B (cash) / $44.2B (prop.+equip.) | **beat** ($43.6B FactSet) | **~$200B** (Jassy verbal commit, up from $123B '25/$77B '24) | TTM $1.2B | **−95% YoY** (near-zero) | **7/30/26** |
| META | $19.8B | — | **$125-145B** (raised from $115-135B; driven by component/memory costs) | $12.39B | (OCF $32.23B) | **7/29/26** (same day as MSFT) |
| **Sum** | **≈$129.8B–130.6B** (+80% YoY, industry tracker vs. VULCAN's own sum — reconciled) | — | **≈$710-725B** (4-name, +77% YoY vs $410B 2025; ~$750B incl. Oracle) | — | **universal compression, all 4 simultaneously** | — |

*Sources: MSFT/GOOGL/AMZN/META 8-Ks + Q1'26 earnings calls (all 2026-04-29); aggregate cross-check via CreditSights/industry tracker (2026-06 vintage). Full row-level sourcing → `workbook/KB.tsv` KB-VULCAN-005 through 011.*

**Concentration metrics:**
- **Mag-7 S&P 500 weight: 32.8683%** *(normalized 32.8860%)* — ⚠️ **REFRESHED 2026-08-24** [SSGA daily SPY holdings, **holdings as-of 2026-08-21**, 505 holdings, own fetch, validated 0.000% err]. ~~32.9810% [as-of 8/20]~~ **is superseded by a genuine one-day MARKET MOVE of −0.11pp — not a correction and not a basis change.** ⚠️ **Direction matters here: concentration is FALLING**, which with breadth at the 97.6th pctile is the *opposite* of this channel's red-band shape. *(Original 8/21 issuer-primary pull, retained as the record:)* **32.9810%** — ⚠️ **PULLED AT AN ISSUER PRIMARY 2026-08-21, replacing the ~32.5% aggregator figure carried since 7/12** [State Street SSGA daily holdings file for SPY, as-of **2026-08-20**, 505 holdings, own fetch]. Per name: **NVDA 7.9785** · AAPL 6.9455 · MSFT 5.4294 · AMZN 3.8681 · GOOGL 3.0346 · GOOG 2.4282 · META 1.8209 · TSLA 1.4759. **NVDA is the largest single S&P name and 24.19% of the group** — ⚠️ *not the "21%" this line carried*.
  - ⚠️ **STILL BELOW THE 33% YELLOW LINE, AND THE 8/24 REFRESH WIDENS THE GAP: 32.8683 is 0.13pp under**, which is now OUTSIDE the two-fetch basis noise quoted below — so the 8/21 *"distance smaller than the noise"* caveat **no longer binds at today's level**, though the 8/21 arithmetic below is retained as the record of how it read then. **NOT-FIRED on the letter, and moving away from the line, not toward it.**
  - *(2026-08-21 record, retained:)* ⚠️ **IT IS AT THE 33% YELLOW LINE, NOT COMFORTABLY BELOW IT.** 32.9810 is **0.019pp** under the threshold, and two fetches of the same as-of file (SSGA republished intraday) put the equity-normalized figure between **32.9821 and 32.9982** — **the distance to the line is smaller than the basis noise.** Report as **AT the line, NOT-FIRED on the letter**; do not claim above-or-below on a normalized basis. ✅ The Mag-7 total was **identical (32.9810) in both snapshots** — only the residual cash line moved, so the load-bearing number is stable even though the normalizer is not.
  - ⚠️ **PERIMETER TRAP — ALPHABET HAS TWO CLASSES IN THE INDEX (GOOGL A + GOOG C) AND BOTH COUNT.** Dropping GOOG gives **30.5528%**, understating by **2.43pp** — roughly 120× the distance to the threshold being tested. Any Mag-7 figure that omits a class is wrong by more than the number it is compared against.
  - ⚠️ **BASIS: this is a FUND weight, not an S&P DJI INDEX weight.** The committee publishes no free constituent weights (spglobal 403s), so the replicating trust's own holdings file is the best reachable primary. **Say "SPY fund weight" when quoting it.**
  - ✅ **Validated with ZERO free parameters:** anchoring the scale on NVDA alone and predicting the other seven from shares × 8/20 close reproduces every stated weight to **0.000%** error.
  - 🔑 **The 7/12 caveat on this line — *"sharpen before citing in a trade-facing context"* — sat unactioned for six weeks while this figure served as S1's banded threshold input AND THESIS-KILL leg 2's instrument. It rotted because nothing pulled it. Now instrumented: `tools/mag7.py` → `workbook/MAG7_SERIES.tsv` (append-only, content-vintage, fail-loud).** [KB-101]
- **Capex as % of FCF / FCF compression:** the load-bearing new datum. AMZN's TTM FCF has collapsed to $1.2B (−95% YoY) against ~$200B FY26 capex guide — capex now vastly exceeds FCF generation. GOOGL's FCF margin fell from 21% to 9.2% YoY in one quarter. MSFT FCF down 22% YoY despite record operating cash flow. **This is the first quarter all four hyperscalers show FCF compression simultaneously** — the MECHANISM-VS-THERMOMETER discipline's EXPECTED_SIGNAL co-appearance test, now live.
- **Market-pricing corroboration:** NDX-SPX 3m ATM IV dispersion hit 10.2 on 7/2/26 (2nd-highest ever, ATH 10.80 on 6/23/26, ~5σ vs 5.1 mean), peaking alongside VIOLET's Path-B partial-fire [VIOLET board_log SIG-W-20260702-017] — vol markets are already pricing the concentration mechanism, independent of VULCAN's fundamentals read.

**~~Registered resolver — GOOGL 7/22/26~~ — ⚠️ RESOLVED, see the box above. Retained as the registered text; the live S1 clock is now the Jan-2027 guides (VULCAN-10, 2/15/27) and there is NO near-clock S1 gate. (VULCAN-03, the first hard gate):** CONFIRMS/extends if FY26 guide is HELD ≥$180B or RAISED and Q2 capex ≥$40B (up from Q1's $35.67B). FIRES the bidirectional-flip (S1 escalation, flag VIOLET+HENRY same day) if FY26 guide is CUT below $180B or management flags capex deceleration/ROI concern. **Composite resolver — the full cluster (VULCAN-01/04, resolves 7/31):** the summed FY26 guide across MSFT/GOOGL/AMZN/META nets HOLD/RAISE vs. the $710-725B baseline pinned here — a net CUT fires S1 to 4/5 or 5/5 on the convergence matrix.

**VULCAN's read going in:** capex is still being *raised*, not cut — S1 has NOT fired by its own standing rule. But the FCF-compression breadth (universal, same quarter) and the component-cost inflation inside the guide raises (see S2 below) are new load-bearing facts that sharpen the bidirectional flip without tripping it yet.

## S2 — Memory cycle (the real-economy demand tell) — first pull done 2026-07-12

| Stage | Mechanism | State |
|---|---|---|
| 1 | AI demand pulls HBM; conventional DRAM/NAND ride the broader cycle | confirmed |
| 2 | Memory price (spot → contract) + maker capex signal the cycle position | **SPLIT READ 8/3 — physical legs UP, equity leg ROLLED.** ~~Spot rising 8/3 (DDR5 $51.33 +0.72% · DDR4 $85.71 +0.57%)~~ → **spot STILL RISING and higher, 8/24: DDR5 $54.17 +0.12% · DDR4 $91.32 +0.27%** *(8/21: $54.10 / $91.07)* ⚠️ **rate of increase is the LOWEST in the retained series — logged as a WATCH ITEM, explicitly NOT scored: "rate of increase slowed" is not "prices falling," which is the 8/13 error class inverted, and n=1 on an irregular cadence** [TrendForce spot tracker 18:10 GMT+8, own `semi_watch.py` pull]; contract rising but **decelerating** (3Q26 fcst DRAM +13-18% / NAND +10-15% QoQ). ⚠️ vs 2Q26's +58-63%/+70-75% — **general vs SERVER DRAM, not like-for-like**. **⇒ The physical legs have moved FURTHER from the −25% roll rule since 8/3, not closer** |
| 2b | **Equity/flows price the cycle position ahead of contract** *(new leg, 8/3)* | ~~**ROLLED**~~ → ⚠️ **UNRESOLVED, AND THE INDICATOR IS DISARMED (8/13, upheld 8/21 on better grounds, RE-GRADED EARLY 2026-08-24 AGAINST THE PRE-SPECIFIED RULE AND STILL DISARMED — both legs unmet).** **8/24:** spread **+19.02 → +13.14 → +4.54 → +3.31pp** (four consecutive readings narrowing, one-third of the +10pp bar, moving AWAY); leg 2 unmet, spot at series highs. ⚠️ **The 8/24 tape is the fastest de-rate in this desk's record and STILL fails this leg's defining clause — AI-compute fell HARDER than QQQ (NVDA −6.53%, AVGO −7.76% vs −2.99%), so "equity prices the cycle ahead of contract" is not what is happening; it is a bloc rotation.** [KB-115/116]  7/6→8/3 read retained as the record: SNDK −26.2, KLAC −21.7, LRCX −15.9, MU −15.8, AMAT −12.6 vs QQQ −3.2, **NVDA +5.7/AVGO +4.9**; flows agreed (Vanda 7/28: 88% of a COVID-magnitude retail sell = 4 memory names). **What happened since: the answer is BASIS-DEPENDENT and I now carry all three.** ① **rolling-1mo** (the only window fixed *before* the data, `S2_SERIES.tsv`): AI-compute−memory spread **+19.02 → +13.14 → +4.54pp**, **NARROWING**; ② **peak-to-current** (peaks all late June): **KLAC −38.6 · WDC −37.2 · AMAT −31.8 · SNDK −31.5 · MU −19.1** vs **QQQ −4.6** and **NVDA −3.7** — de-rate **large and intact**; ③ **YTD** (the steelman): the complex is **+45% to +483%**, so a 30% drawdown off a parabolic June top is **arithmetic, not a roll**. ⚠️ **The 8/13 "retrace" verdict is WITHDRAWN — it was measured from the drawdown's own trough** (8/3, MU $829.50), which manufactures a retrace by construction [KB-089, **L-17**]. **🆕 And the cohort has SPLIT for the first time:** semicap −10.01 vs memory −4.35, **MU +1.14 vs KLAC −14.54** — DRAM's bellwether is now the *strongest* leg, sorting along the DRAM-tight/NAND-eases line flagged in KB-057. **Indicator stays DISARMED — not "it failed" but "it has no specified basis"; pre-specified re-arm rule grades 9/30** (rolling-1mo spread ≥+10pp for 3+ readings AND further contract deceleration). [KB-089/091/092/093] |
| 3 | A contract-price roll = demand inflection (memory leads the cycle) | open — **NOT triggered**; both price legs still positive, −25% QoQ rule far from firing |

**Repricing:** memory makers, a broad demand-velocity read (→ HENRY), goods/tech demand (→ CARL). **Why it matters:** memory is the most cyclical semi — a contract-price roll is one of the earliest real-economy demand tells. **First pull (2026-07-12):** TrendForce 2Q26 forecast + Micron FQ3 FY26 print (reported 6/24/26, revenue $41.46B vs $32.75-34.25B guide, CEO says can fill only 50-67% of demand) both confirm a structural shortage, not a roll — no capacity relief expected before late 2027/2028. **New cross-channel link (MISSED CONNECTIONS, 2026-07-12): S2 feeds S1 directly.** MSFT and META both cite higher component/memory costs as explicit drivers of their FY26 capex-guide raises (MSFT: ~$25B of its $190B guide = pricing effect). Some fraction of the eye-catching capex $ growth is memory-cost inflation, not purely incremental compute capacity — relevant nuance for how VIOLET/HENRY read the raw capex figures. **Next resolver:** **MU FQ4, ~2026-09-29** — ⚠️ **not "~8/4"**, which was a VULCAN-authored error carried 7/12→8/3 (Micron's FY ends **09/03**; a quarter ending then cannot report 8/4 — KB-047, L-13). It lands **one day before VULCAN-02 + VULCAN-11 resolve 9/30**.

### ⚠️ 2026-08-03 RE-MARK — the S2 mechanism is the LTA / PRESOLD CEILING (WALTER's, adopted)

The 7/12 read above ("structural shortage, not a roll") is **still true on the physical legs and is no longer the whole story.** What changed is that the *repricing* leg moved while the price legs did not, and the mechanism that explains it is **not** a generic cycle peak:

- **US CSPs hold multi-year LTAs that RESTRICT suppliers from raising prices to them.** From 3Q26 the price-increase driver shifts to customers **without** LTAs, plus incremental supply sold outside them ⇒ **hyperscalers capped, everyone else absorbs** — a bifurcation *inside* the memory market.
- **A supplier that has PRESOLD cannot monetise the spike.** Micron is presold through 2027, so that volume was priced **before** the surge ⇒ **"sold out through 2027" is a CEILING, not a moat.** The structure protecting the hyperscaler's cost line also caps the supplier's upside.
- **This explains what a cycle-peak read cannot:** why memory de-rates on *record* fundamentals **while AI-compute rises**. The 7/31 closes sorted along exactly that line — LTA-protected **AMZN +15.32% · GOOGL +6.73% · META +3.28% · MSFT +3.02%** vs **AAPL −7.35%** (non-LTA buyer paying up) and **MU −5.90%** (capped seller). ⚠️ AAPL closed **−7.35%**, not the "10%" the Friday wires carried.
- **The consumer leg of the S2→S1 cost-push, which this doc previously lacked:** Cook (AAPL FQ3, 7/30) — Apple *"reluctantly raised prices"* on Macs/iPads citing a **"100-year flood on memory pricing,"** expects to pay more still, says DRAM needs >3 suppliers; 7/31 Apple published the rationale across **14 products**. That *is* TrendForce's "consumer demand weakening": consumers hit an affordability limit because the cost reached them. ⚠️ **And a QUANTITY channel carried nowhere else:** the shortage *"raised costs **and lowered production**"* — raising prices fixes only the price half.
- **⚠️ DRAM and NAND must stop being one line.** TrendForce 7/30: **2027 DRAM supply stays TIGHT while NAND supply EASES.** This doc, STATUS and VULCAN-02 all quote them paired. **VULCAN-11 is DRAM-specific and survives; VULCAN-02's paired wording is the exposed one** — a NAND roll with a DRAM hold would resolve it ambiguously. Consistent with **SNDK (NAND-heavy) leading the de-rate at −26.2%**. [KB-057]

**Provenance + caveat:** the LTA/presold mechanism is **WALTER's** (`SIG-W-20260731-002`, `-010`), adopted here with its author's own caveat intact — *"a hypothesis for you to kill or keep, not a finding"*; the 7/31 single-session move is not decomposed. Registered as **VULCAN-11** (equity-leads-contract, resolves 9/30, frozen baselines, explicit NO-VERDICT band). [KB-048/049/055/056/057]

## S3 — AI-capex → power demand (feeds WATT) — first sizing done 2026-07-12 (round 2)

| Stage | Mechanism | State |
|---|---|---|
| 1 | AI-capex → datacenter buildout → compute demand | confirmed (macro) |
| 2 | Compute demand → interconnection + grid MW load | **sized: capex-implied ~8-11 GW/yr global 4-name flow (2026) — conversion below** |
| 3 | Grid can't supply → power becomes the binding constraint on AI deployment | open (the WATT coupling) — WATT's P2 capacity leg already FIRED on its side |

**Repricing:** hands WATT the demand driver (WATT prices the grid response); power-availability as a gate on AI-capex. WATT owns the power price (reconcile to one figure).

### CAPEX → MW CONVERSION (first pass, 2026-07-12 — every step ASSUMPTION-tier unless noted)

**Inputs:** S1 baseline agg FY26 capex guide $710-725B (4-name, EMPIRICAL, KB-009) — ⚠️ **SUPERSEDED 7/31: the realised aggregate is ~$735-760B economic. This input is the FROZEN 7/12 baseline and every result below inherits it (~3-5% low). Re-derive before citing any GW figure; do not quote the band as current.** · capex intensity **$50-60B per GW** all-in AI infrastructure [Jensen Huang, ~May 2026 vintage, NVDA hardware >half of that sum — **incentive-flagged: vendor-sourced**, Barclays has publicly stress-tested the "Jensen math"; Stargate corroborates ~$50B/GW ($500B/~10GW target)] · AI-related share of hyperscaler capex **~70-75%** [industry estimate vs top-5, late-2025/early-2026 vintage; KB-017].

| Step | Calculation | Result | Tier |
|---|---|---|---|
| 1. AI-specific 2026 capex (4-name) | $710-725B × 70-75% | **$500-545B** | ASSUMPTION (share) |
| 2. Implied new AI capacity, global, 2026 flow | $500-545B ÷ $50-60B/GW | **~8.3-10.9 GW/yr** | ASSUMPTION ($/GW) |
| 3. Gross-up for non-big-4 (Oracle/Stargate/xAI/neoclouds/China; 4-name ≈ ~70% of global AI capex) | ÷ 0.7 | **~12-16 GW/yr global all-players** | ASSUMPTION |
| 4. Cumulative 2024-2030, 4-name (2024-25 ~$630B actuals + 2026 guide + FLAT-at-2026 2027-30 — the conservative branch) | ~$4.2T × ~70% ÷ $50-60B/GW | **~48-62 GW global (4-name)** | ASSUMPTION (flat-capex branch) |
| 5. All-players global, 2024-2030 | ÷ 0.7 | **~68-89 GW** | ASSUMPTION |
| 6. US share (~55-60%) → PJM share of US DC (~25-35%, VA data-center alley) | sequential | **~9.5-19 GW PJM, hyperscaler-AI only** | ASSUMPTION ×2 |
| 7. PJM total-DC (hyperscaler-AI ≈ 50-70% of PJM DC growth; rest = colo/enterprise/crypto) | ÷ 0.5-0.7 | **~14-37 GW PJM total-DC, 2024-2030** | ASSUMPTION |

**Honest-uncertainty note:** 5+ stacked assumptions — the band is wide by construction and the deliverable is *which forecast sits inside the band*, not a point estimate. Known biases: (a) GPU-refresh into existing shells inflates $ without net-new MW (overstates GW); (b) capex-year ≠ energization-year (12-24mo lag — 2026 capex powers 2027-28 load); (c) flat-capex 2027-30 is conservative — the 2026 guide is +77% YoY, and if that growth persists the band shifts materially up; (d) S2's component-cost inflation means some capex $ is price, not capacity (same nuance as the S1 read — cuts implied GW further).

### RECONCILIATION vs WATT's P3 range (read-only consume of AGENTS/WATT/, 2026-07-12)

WATT's two seam datums [WATT STATUS P3 row, KB-WATT-012..014]: **PJM-official 32 GW** total peak-load growth 2024-2030, 30 GW (94%) data-center-driven [PJM via DCD, pub 2025-08-12] vs **WoodMac/utility-self-reported 55 GW by 2030** (100 GW by 2037) [via White & Case, pub 2026-03-11] — a 23 GW / 70% unreconciled gap.

> ## 🔴 THE 7/12 VERDICT BELOW IS SUPERSEDED TWICE — READ THIS BOX FIRST (added 2026-08-21)
>
> **This section sat 18 days asserting the OPPOSITE of STATUS.** Two things resolved it and neither was written back here:
>
> **① 2026-07-31 — VULCAN-06 resolved HIT, and it UPGRADED the verdict.** The discriminator named below (the 7/22-7/31 capex cluster) fired on the **(a)** branch: all four guides RAISED (agg **~$735-760B** economic vs the $710-725B baseline) **AND** ≥2 of 4 named power/energy as a binding constraint (MSFT *"capacity constrained, demand exceeds supply"* +1GW +~$80B power-gated Azure backlog; META *"tens of gigawatts this decade"*; AMZN *"still not enough capacity"*). ⇒ **the raised capex + power-as-binding-constraint SUPPORT the WoodMac 55 GW HIGH side.** Routed to WATT 7/31. **The 7/12 "supports 32 GW, not 55" verdict is retired.**
>
> **② 2026-08-13 — the WATT seam closed, and it dissolves the either/or the verdict was built on.** **32 GW and 55 GW are not two rival forecasts of one quantity — they are two different quantities, and both are right:** **~55 GW = nameplate interconnection ceiling · ~32 GW = FIRM coincident-peak contribution.** ⚠️ **Adopt verbatim; never net, never average them.** Curtailability offset is **0 GW today** (NCBL went voluntary, not in effect). ⇒ The question *"is it 32 or 55?"* was **mis-specified** — which is also why the (c) "double-counted/speculative requests" branch below is not the artifact explanation it looked like: nameplate legitimately exceeds firm without anything being double-counted. [KB-087]
>
> ⚠️ **The arithmetic below is ALSO computed off the superseded $710-725B baseline** (actual ~$735-760B, VULCAN-01 HIT 7/31), so every step from AI-specific capex down to the ~14-37 GW band is ~3-5% low. **The band is retained as the 7/12 record, not as a current read** — re-derive before citing.

**~~VULCAN's verdict: hyperscaler-guided capex supports the LOW-to-MID (PJM-official) forecast, not the high one.~~** *(7/12 verdict — RETIRED 7/31, see box above.)* PJM's 32 GW sits inside the upper half of the capex-implied ~14-37 GW band; WoodMac's 55 GW sits ~50% ABOVE the band's top. For 55 GW to be real funded demand, at least one of: **(a)** aggregate capex keeps growing high-double-digits through 2028-30 (2026's +77% raise is a trajectory, not a step), **(b)** PJM's share of the US buildout rises above ~35%, or **(c)** the 55 GW contains double-counted/speculative utility interconnection requests (same project shopped to multiple utilities — a known inflation mechanism in self-reported pipelines; this branch resolves the gap as *artifact*, not demand). **The (a)-vs-(c) discriminator is on VULCAN's clock: the 7/22-7/31 capex-guide cluster.** Continued raises + FY27 acceleration language → (a) gains, 55 GW path stays live; capex plateau/cut → 32 GW is the funded ceiling and the WoodMac excess is likely artifact. Registered as **VULCAN-06** (resolves 7/31).

**Shared-antecedent discipline:** this couples S3's resolver to S1's catalyst — the capex root is shared (per STATUS independence note); a capex disappointment fires BOTH, count the root once. **Double-count guard for the seam:** WATT's IPP PPA datums (VST 3,800MW AWS + 2,609MW Meta; TLN 1,920MW Amazon) are the *utility-side reflection of the same hyperscaler capex* — when reconciling to one figure, PPA-MW and capex-implied-MW are two views of one demand, never additive.

## S4 — Supply-chain / geopolitics (the chokepoint) — first pull done 2026-07-12

| Stage | Mechanism | State |
|---|---|---|
| 1 | Leading-edge fab capacity concentrates at TSMC-Taiwan | confirmed (structural) |
| 2 | US/China export controls tighten the equipment + chip flow | **two-sided, not one-directional — see below** |
| 3 | Equipment ban / fab cutoff / Taiwan kinetic → supply shock across the chain | open; TSMC revenue shows no stress yet |

**Repricing:** the semi-supply consequence of ZHAO's China events + HAWK's Taiwan geopolitics. **First pull (2026-07-12):** TSMC May'26 monthly revenue +30.1% YoY (record) — no chokepoint stress on the revenue line; ~~June print delayed to 7/13/26 (typhoon), VULCAN-05 resolves there.~~ ⚠️ **RESOLVED — VULCAN-05 HIT 7/17** (June NT$442.68B, +6.2% MoM; ⚠️ cite **H1 +35.6% YoY**, NOT the +67.9% headline, which is a base effect off a June-2025 trough). **🆕 CURRENT READ, pulled 2026-08-21 — the section above is the 7/12 record, not the live number: TSMC July 2026 revenue NT$467,580M, +5.6% MoM, +44.7% YoY; Jan-Jul +37.0% YoY** (up from H1's +35.6% — a mild acceleration) [**SEC 6-K acc `0001046179-26-000471`, filed 8/10**, own EDGAR pull]. **S4 revenue line clean; NOT-FIRED. Next print ~2026-09-10 — this is a MONTHLY series and must be pulled monthly** (it sat 5 weeks stale through two sessions; the reassuring number is why nobody noticed). [KB-100] **The export-control picture is NOT simply tightening** — it is genuinely two-sided: the US *eased* (BIS approved H200 sales to China 1/13/26, ~10 buyers cleared by 5/14/26, though paired with a 25% tariff), while Taiwan is *tightening* from the other end — weighing a Foreign Trade Act amendment to criminalize unauthorized AI-chip exports to all of China (undated), with a first concrete enforcement event 7/1/26 (Keelung court detained 3 Super Micro/Albatron execs — Taiwan's first criminal AI-chip-diversion probe). No fixed-date resolver exists for the Taiwan legislative side; monitoring item. Kinetic Taiwan = HAWK cross-flag; China macro = ZHAO — **route-out: neither may have this dated 7/1 event logged from the semiconductor angle.**

### 🆕 2026-08-21 — S4 IS INSTRUMENTED, AND IT NOW HAS 20 MONTHS OF RETAINED HISTORY

*Added at closeout step 2b. ⚠️ **This is an ADDITION, not a correction** — the three 2b
questions were run against this section and it contradicted nothing: stage 3's "open; TSMC
revenue shows no stress yet" agrees with STATUS, VULCAN-05 was already struck as resolved,
and the 7/12 May'26 +30.1% first-pull figure is reproduced exactly by the new series. The
section was thin, not wrong.*

**`tools/tsmc_watch.py` → `workbook/S4_SERIES.tsv`** — TSMC monthly revenue from its own SEC
Form 6-K (issuer-primary, CIK 0001046179), 20 months backfilled Dec-2024 → Jul-2026, every
row validated by three zero-free-parameter recomputations. **S4 previously had no instrument
and no retained history at all** — which is why it was found **35 days stale on a MONTHLY
series** on 2026-08-21.

**What the history says, and it could not be said before today:**

| | 2025 | 2026 YTD |
|---|---|---|
| Cumulative YoY path | **43.5 → 31.6** — monotone decel, 8 consecutive months | **36.8 → 29.9 → 35.1 → 29.9 → 30.0 → 35.6 → 37.0** — oscillating, no run >1 |
| Shape | a genuine decelerating year | **choppy, and RE-ACCELERATING into July** |

🔑 **The read: ~~2026's cumulative +37.0% now sits ABOVE full-year 2025's +31.6%~~ ⚠️ **PERIOD-MISMATCHED — CORRECTED 2026-08-21 (evening self-check). That set a 7-MONTH YTD against a 12-MONTH FULL YEAR.** Like-for-like at July, **2026 (+37.0%) is BELOW 2025 (+37.6%)**, and 2026 sits below 2025 at **every aligned month except January**. 🔑 **What IS true, and it is the better read: 2026 re-accelerated WITHIN the year — Apr +29.9% → Jul +37.0%, +7.1pp — and has narrowed the gap to 2025's pace from −13.6pp (Apr) to −0.6pp (Jul). It has very nearly CAUGHT 2025, not overtaken it.** The S4 verdict is unchanged (NOT-FIRED; the red band is *decline* and growth is ~37%), but the SHAPE claim was overstated. [`finding_cross_entity_comparison_needs_same_perimeter`]. The
deceleration that ran through all of 2025 did not continue — it reversed.** S4's revenue line
is not merely "clean", it is **re-accelerating**, which strengthens the NOT-FIRED verdict
rather than just failing to contradict it. ⚠️ **Cite the cumulative** — monthly YoY ranges
**16.9% to 67.9%** across these 20 observations (a 51pp spread), so any single month's YoY is
close to meaningless on its own. That spread is the quantified version of the standing
"June's +67.9% was a base artifact" warning.

⚠️ **Two instrument caveats that belong with the read, not buried in the tool:**
- **The RED band (monthly YoY < 0) has occurred 0 times in 20 months.** It is *reachable*
  (proven by fixture 8/21) but **unobserved in-sample**, so it carries no base rate. Do not
  present its silence as evidence of stability.
- **The YELLOW `decel` band fires 7/20 (35%)** even after being tightened to require 2+
  consecutive months. It is honest — TSMC really did decelerate for most of 2025 — but a
  band lit a third of the time is a "look", never an "act". The actionable bands are
  **flat** and **decline**.

## S5 — AI-infra financing — **PROMOTED tier-2 → CORE 2026-08-03** (Will-approved)

| Stage | Mechanism | State |
|---|---|---|
| 1 | AI buildout is funded by debt, off-BS leases and vendor/lessor guarantees rather than operating cash | **confirmed, and larger than the headline names** — ORCL alone: **$260B** off-BS DC lease commitments (FY27-29 commencement, 15-19yr) + **$3.3B** lessor-borrowing guarantee **maturing Sept-2026**; FY26 capex $55.7B vs $32.0B OCF = **−$23.7B** structural gap [FY26 10-K Note 9] |
| 2 | The obligations sit where no leverage ratio computes them | **confirmed** — on balance sheet these look like ordinary levered tech issuers; ⚠️ the **NVDA→OpenAI ~$250B backstop is filed NOWHERE** (entire filed guarantee book **$3.5B gross / $712M escrowed**), so the headline node is the wrong one |
| 3 | Financing capacity is contractually tied to operating inputs, not just leverage | **confirmed, filed** — CRWV's $8.5B DDTL 4.0 re-marks its sizing model for **hedge/SOFR rates and POWER only** (§5.25 Power Cost Protection; §5.23 ≥95% hedging), resolving to **Projected DSCR ≥1.20x** (1.15x maint.), + a **"Negative NOI Event"** repaying **two months before** the first projected-negative month ⇒ **power price → borrowing capacity.** *(Couples S3.)* |
| **3b** | **Regulators write IG thresholds into utility tariffs ⇒ a standing liquidity demand independent of capex** | **🔑 THE INDEPENDENCE LEG. Live.** WI PSC rule (**April 2026**): any DC developer rated **below A-** posts guarantees before service — **>$100M/yr** in deposits/LCs. **NOT downgrade-triggered:** ORCL was already **BBB**, the rule predates the 7/9 cut by 3 months, and ORCL **sued 6/19**. ⇒ **rating LEVEL, not migration, is binding** |
| 4 | Price of access repricing before access is lost | **elevated** — CRWV $2.6B DDTL **cleared +100-125bp wide of talk** (S+550/OID 96-97/**YTM 10.44%**) **at full size**; NVDA 5Y CDS **40→68→~82bp record [all 7/27]**, ORCL **~210-215bp record [7/27]**; GS/JPM **shortable** basket **319bp [7/23]** (18 equal-wtd **neoclouds**) vs HY 279. ⚠️ **CDS AND THE BASKET ARE GENUINELY-UNAVAILABLE TO THIS DESK** (Markit/Bloomberg paywall) — **LIQUID, who owns the spread tell, carries the same 7/27 prints**, so this is a data-access limit on both desks, not a VULCAN collection gap. **Stamp them [7/27]; never state as current.** **🆕 WHAT IS REFRESHABLE, PULLED 8/21: HY OAS 275bp [8/20] — TIGHTER than the 281bp my files carried — and IG OAS 81bp [8/19]. The aggregate-benign leg is intact and slightly STRONGER.** ⚠️ **And the equity counter-leg DECAYED: CRWV +4.8% / ORCL +4.5% on the same 8/3 basis** (was +23.9% / +10.2% at 8/13; do NOT quote "−15.5% since 8/13" — 8/13 is effectively CRWV's peak, so that is extremum-anchored, **L-17**). [KB-104] |
| 5 | Access actually lost → project halts / default | **NOT reached** — no default, no pulled deal, aggregate IG/HY benign, ORCL contesting in court rather than failing to post |

**Repricing:** AI-infra credit spreads (→ **LIQUID**, who owns the spread tells), private-credit marks (→ BROCK), FCF/valuation (→ HENRY), project feasibility (→ WATT).

### Why it was promoted, and the one argument that carried it

The weak case is volume — S5 accreted more filed, dated material in a week than some core channels hold. **That alone would not justify promotion; it would justify a longer sub-read.**

**The argument that carried it: S5 demonstrated it can fire while S1 is NOT firing.** The Oracle collateral requirement is live *while hyperscaler capex is being raised* — it fires on the **balance sheet and the tariff**, not on capex direction. A channel that can only fire when S1 fires is not independent (that is precisely why obsolescence and the returns-case stayed **sub-reads**). S5 cleared that bar; they have not.

⚠️ **Independence is PARTIAL and must be stated every time:** the **ROI-disappointment leg** still shares S1's antecedent — an AI-capex disappointment drives S1 + S3 + S5 at once and **that root is still counted ONCE**. Only the **financing-structure/regulatory leg** is independent.

⚠️ **Scored 3, not 4, and the reason is sourcing rather than severity:** the two strongest datums are the weakest-sourced. ~~The DDTL terms have **no filing at all** — CRWV's last 8-K of any kind is 6/18, and the terms first become verifiable at its **Q2 10-Q (~Aug)** [KB-068].~~ ⚠️ **THAT NEGATIVE RESOLVED 2026-08-12 AND THIS FILE CARRIED IT AS LIVE FOR 9 DAYS.** **CRWV's Q2 10-Q printed 8/12 (acc `0001769628-26-000366`) and VULCAN read it:** the facility is **DDTL 5.5 — $2.6B at Term SOFR + 5.50%**, commitment termination Dec-2026, **matures Sept-2031, $1.2B drawn**, JPMorgan admin agent. ✅ **The S+550 margin is FILING-CONFIRMED.** ❌ The **OID 96-97 and the 10.44% YTM are NOT in the filing** and remain trade-press/PROVISIONAL — so **the sourcing objection is HALF discharged, not discharged**, and the score stays 3 on the same logic (*a better-sourced 3 is still a 3*). ⚠️ **Naming: say "DDTL 5.5", never "the $2.6B DDTL" — DDTL 3.0 was also $2.6B.** [KB-074/075] And the ORCL headline **did not survive verification**: the "$7B" is uncorroborated and its causation was backwards [KB-069]. **Do not score on numbers that verification just corrected.**

**Upgrade triggers → 4:** a cleared AI-infra new issue flexing **+150bp or pulled** · a **second jurisdiction** writing an IG threshold into a tariff · ~~CRWV's Q2 10-Q disclosing terms **worse** than trade press.~~ ⚠️ **THIS THIRD TRIGGER HAS FIRED AND ANSWERED — NO.** The 10-Q disclosed the margin **at** trade press (S+550, exactly as reported), not worse. **The trigger is spent; do not carry it as a forward condition.** ⇒ **Two live upgrade triggers remain, not three.**

> 🔑 **What replaced it as the sharpest S5 evidence (8/13):** the 10-Q handed over **a pricing TIME SERIES at one issuer**, which is strictly better than the dealer basket I had retracted as historyless — **DDTL 4.0 (Mar-26) SOFR+225 → 5.0 (May-26) +450 → 5.5 (Aug-26) +550.** ⚠️ **Do NOT quote Mar→Aug as +325bp: DDTL 4.0 is NON-RECOURSE.** The defensible like-for-like claim is **+100bp on the 5.0→5.5 leg in three months.** Routed to **LIQUID**, who owns the spread tell — not maintained here as a rival index. Also filed: recourse debt **$31.4B** (+51.5% in 6mo) at 9-15%, total liabilities **$72.0B**, **$35.5B off-BS leases not yet commenced** (2026-29) = the CRWV analogue to ORCL's $260B in the same window, **interest expense $640M > net loss $626M** (GAAP operating loss only −$49M ⇒ *the loss IS the interest bill*), 6-month funding gap **~−$10.5B** on $4.7B revenue, **RPO $103.7B** against **72% of revenue from three customers**. [KB-076..080]

---

## 🔴 THE NVDA RESIDUAL-VALUE GUARANTY — the mechanism, not the news (registered 2026-08-21)

*Filed evidence: NVDA 8-K 2026-08-17, acc `0001045810-26-000069`, Item 1.01. Facts in KB-111/112.
This section is the JUDGMENT; the ledger holds the data. Written because the first pass logged and
routed the filing without ever stating what it means — and the mechanism is the reason this seat exists.*

**What NVDA did:** wrote residual-value guaranties on ~4.25 GW of datacenter leases (+~3.8 GW at its
option) where an **OpenAI affiliate is the tenant**, at a site that hosts **NVDA's own platform**.
Obligation capped at **$105B**; NVDA pays the shortfall between a guaranteed minimum lease value and
what a re-let or sale recovers. It terminates when **OpenAI achieves a satisfactory credit rating**.

### 🔑 Why it is an S1 concentration-FRAGILITY mechanism, not a financing footnote

**The two legs of NVDA's exposure are positively correlated, and that is the whole point.**

| Leg | What triggers it |
|---|---|
| OpenAI defaults on the lease | an AI demand/monetisation disappointment |
| Re-let or sale recovers less than the guaranteed minimum | **the same** AI demand disappointment — AI-specific datacenter capacity is thin-market and purpose-built |

⇒ **NVDA has written a guarantee whose payout becomes most likely in exactly the state where its own
core business is weakest.** That is not risk *transfer* and it is not diversification — it is a
**correlated exposure that concentrates rather than spreads**. The index consequence is what makes it
S1's: NVDA is **7.98% of the S&P and 24.19% of the Mag-7**, so a contingent claim on the single largest
index name, conditional on the very scenario that would already be repricing that name, is a
**convexity the index does not see** until it fires.

⚠️ **Stated at the right strength, because the temptation is to overclaim.** This is **not** "NVDA lends
OpenAI money to buy NVDA chips." NVDA is taking **residual-value risk on real estate**, OpenAI
**indemnifies** NVDA, and the obligation is **capped** and **conditional**. The claim here is narrower and
survives that: **the guarantee's payoff is correlated with the AI-demand state, so it fails to hedge and
instead stacks.**

### Why it is S5's strongest evidence yet — and why the score still did NOT move

**Rating LEVEL is the binding variable, for the second time and in a new legal form.** Wisconsin PSC
(KB-069) binds a sub-A- developer through a **regulatory tariff**; this binds through a **private
contract**, and its termination condition is literally *"OpenAI achieving a satisfactory credit rating."*
Two independent legal channels now key on the same variable. That is the **strongest affirmative support
the S5 independence claim has** — and it landed **while capex was being RAISED**, which is precisely the
form the promotion argument predicted.

⚠️ **And the score is HELD at 3 anyway.** My S5 bands grade *regulator-mandated* collateral and *priced
new issues*; this is neither. **Evidence strengthening without a band tripping is the normal case, and
moving the score because a datum feels important is how a matrix stops meaning anything.**

### What CANNOT be concluded yet — the two numbers that decide the size

**The $105B is a CAP on NVDA's obligation, not an exposure estimate.** Actual exposure depends on:
1. **the guaranteed-minimum-value schedule** — not public;
2. **the definition of "satisfactory credit rating"** — not public, and it is the entire termination condition.

Both are said to arrive as an **exhibit to the 10-Q for the quarter ended 2026-07-26**. ⚠️ **Until then,
any exposure figure is a ceiling being quoted as a level** — do not let $105B propagate as "NVDA's
exposure." *(This is why the 8/31 tripwire survived the 8-K rather than being retired by it.)*

### Does this need its own prediction? **No — and saying so is the discipline.**

The recurrence question is **already** what VULCAN-13 tests, in a form that does not depend on this
structure repeating in exactly this shape. **A second prediction here would be the same claim registered
twice**, which inflates the book and lets one event resolve two rows. The one genuinely novel falsifiable
question — *does OpenAI obtain a rating?* — has **no bounded date**, and a prediction without a resolution
window is not a prediction. **Registered as a watch item, not a forecast.**

---

## Boundaries (reconcile-to-one-figure, don't silo)

- **VIOLET** owns the concentration-*unwind* vol expression (Path-B); **VULCAN** owns the concentration *mechanism/driver*. VULCAN gives VIOLET's channel the fundamental it's been carrying without.
- **HENRY** owns the AI-capex FCF valuation (HEN-36) + macro velocity; **VULCAN** owns the semi/memory/capex fundamentals feeding it.
- **WATT** owns wholesale power price; **VULCAN** owns the compute→power demand driver.
- **ZHAO** owns China macro; **HAWK** owns Taiwan geopolitics; **VULCAN** owns the semiconductor consequence of both.
- **BROCK** owns private credit; **VULCAN** flags AI-infra debt as a fragility channel (S5).
