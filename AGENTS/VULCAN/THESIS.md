# VULCAN — THESIS (per-channel transmission tables)

**The one-line thesis:** the AI-capex buildout is the single largest systemic vector in the tape — it concentrates index risk into a handful of megacaps, its FCF math gates the whole AI trade, its compute demand collides with a supply-constrained grid, and its supply chain funnels through Taiwan; VULCAN owns the *mechanism* that drives all four.

*Richness lives here; STATUS.md carries the live 5-pt matrix. Each channel is `event → mechanism → repricing` with a stage table (state ∈ confirmed / open / falsified).*

---

## S1 — AI-capex concentration (the core — the reason the seat exists)

| Stage | Mechanism | State |
|---|---|---|
| 1 | Hyperscalers ramp AI-capex (MSFT/GOOGL/AMZN/META) | confirmed |
| 2 | Megacap earnings + market cap concentrate → Mag-7 dominates index weight | confirmed (VIOLET Path-B 🔴) |
| 3 | Index becomes single-factor: breadth narrows, correlation-1 risk | open |
| 4 | Capex ROI question OR a capex cut → concentration unwinds → index-wide repricing | open (the systemic event) |

**Repricing:** the megacap-concentration vol expression (→ VIOLET Path-B), HEN-36 FCF (→ HENRY). **Confirms/breaks:** capex guides raised + FCF holding at the 7/22–7/29 stack confirms; a capex cut YoY with Mag-7 >40% fires the unwind. This is the cleanest bidirectional flip.

### PRE-PRINT BASELINE (quantified 2026-07-12, ahead of the 7/22-7/31 cluster)

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
- **Mag-7 S&P 500 weight:** ≈32.5% (Motley Fool/Stock Analysis data, ~July 2026 vintage) — below VULCAN's own 33% yellow threshold, NVDA now largest single name at 21% of the group. *Caveat: aggregator-sourced, not a primary index-committee figure — sharpen before citing in a trade-facing context (domain-sweep GAPS item).*
- **Capex as % of FCF / FCF compression:** the load-bearing new datum. AMZN's TTM FCF has collapsed to $1.2B (−95% YoY) against ~$200B FY26 capex guide — capex now vastly exceeds FCF generation. GOOGL's FCF margin fell from 21% to 9.2% YoY in one quarter. MSFT FCF down 22% YoY despite record operating cash flow. **This is the first quarter all four hyperscalers show FCF compression simultaneously** — the MECHANISM-VS-THERMOMETER discipline's EXPECTED_SIGNAL co-appearance test, now live.
- **Market-pricing corroboration:** NDX-SPX 3m ATM IV dispersion hit 10.2 on 7/2/26 (2nd-highest ever, ATH 10.80 on 6/23/26, ~5σ vs 5.1 mean), peaking alongside VIOLET's Path-B partial-fire [VIOLET board_log SIG-W-20260702-017] — vol markets are already pricing the concentration mechanism, independent of VULCAN's fundamentals read.

**Registered resolver — GOOGL 7/22/26 (VULCAN-03, the first hard gate):** CONFIRMS/extends if FY26 guide is HELD ≥$180B or RAISED and Q2 capex ≥$40B (up from Q1's $35.67B). FIRES the bidirectional-flip (S1 escalation, flag VIOLET+HENRY same day) if FY26 guide is CUT below $180B or management flags capex deceleration/ROI concern. **Composite resolver — the full cluster (VULCAN-01/04, resolves 7/31):** the summed FY26 guide across MSFT/GOOGL/AMZN/META nets HOLD/RAISE vs. the $710-725B baseline pinned here — a net CUT fires S1 to 4/5 or 5/5 on the convergence matrix.

**VULCAN's read going in:** capex is still being *raised*, not cut — S1 has NOT fired by its own standing rule. But the FCF-compression breadth (universal, same quarter) and the component-cost inflation inside the guide raises (see S2 below) are new load-bearing facts that sharpen the bidirectional flip without tripping it yet.

## S2 — Memory cycle (the real-economy demand tell) — first pull done 2026-07-12

| Stage | Mechanism | State |
|---|---|---|
| 1 | AI demand pulls HBM; conventional DRAM/NAND ride the broader cycle | confirmed |
| 2 | Memory price (spot → contract) + maker capex signal the cycle position | **SPLIT READ 8/3 — physical legs UP, equity leg ROLLED.** Spot rising 8/3 (DDR5 $51.33 +0.72% · DDR4 $85.71 +0.57%); contract rising but **decelerating** (3Q26 fcst DRAM +13-18% / NAND +10-15% QoQ). ⚠️ vs 2Q26's +58-63%/+70-75% — **general vs SERVER DRAM, not like-for-like** |
| 2b | **Equity/flows price the cycle position ahead of contract** *(new leg, 8/3)* | **ROLLED:** memory+semicap bear market, decoupled from AI-compute — 7/6→8/3 SNDK −26.2%, KLAC −21.7%, LRCX −15.9%, MU −15.8%, AMAT −12.6% vs QQQ −3.2%, **NVDA +5.7%/AVGO +4.9%**. Flows agree (Vanda 7/28: 88% of a COVID-magnitude retail sell = 4 memory names) |
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

**Inputs:** S1 baseline agg FY26 capex guide $710-725B (4-name, EMPIRICAL, KB-009) · capex intensity **$50-60B per GW** all-in AI infrastructure [Jensen Huang, ~May 2026 vintage, NVDA hardware >half of that sum — **incentive-flagged: vendor-sourced**, Barclays has publicly stress-tested the "Jensen math"; Stargate corroborates ~$50B/GW ($500B/~10GW target)] · AI-related share of hyperscaler capex **~70-75%** [industry estimate vs top-5, late-2025/early-2026 vintage; KB-017].

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

**VULCAN's verdict: hyperscaler-guided capex supports the LOW-to-MID (PJM-official) forecast, not the high one.** PJM's 32 GW sits inside the upper half of the capex-implied ~14-37 GW band; WoodMac's 55 GW sits ~50% ABOVE the band's top. For 55 GW to be real funded demand, at least one of: **(a)** aggregate capex keeps growing high-double-digits through 2028-30 (2026's +77% raise is a trajectory, not a step), **(b)** PJM's share of the US buildout rises above ~35%, or **(c)** the 55 GW contains double-counted/speculative utility interconnection requests (same project shopped to multiple utilities — a known inflation mechanism in self-reported pipelines; this branch resolves the gap as *artifact*, not demand). **The (a)-vs-(c) discriminator is on VULCAN's clock: the 7/22-7/31 capex-guide cluster.** Continued raises + FY27 acceleration language → (a) gains, 55 GW path stays live; capex plateau/cut → 32 GW is the funded ceiling and the WoodMac excess is likely artifact. Registered as **VULCAN-06** (resolves 7/31).

**Shared-antecedent discipline:** this couples S3's resolver to S1's catalyst — the capex root is shared (per STATUS independence note); a capex disappointment fires BOTH, count the root once. **Double-count guard for the seam:** WATT's IPP PPA datums (VST 3,800MW AWS + 2,609MW Meta; TLN 1,920MW Amazon) are the *utility-side reflection of the same hyperscaler capex* — when reconciling to one figure, PPA-MW and capex-implied-MW are two views of one demand, never additive.

## S4 — Supply-chain / geopolitics (the chokepoint) — first pull done 2026-07-12

| Stage | Mechanism | State |
|---|---|---|
| 1 | Leading-edge fab capacity concentrates at TSMC-Taiwan | confirmed (structural) |
| 2 | US/China export controls tighten the equipment + chip flow | **two-sided, not one-directional — see below** |
| 3 | Equipment ban / fab cutoff / Taiwan kinetic → supply shock across the chain | open; TSMC revenue shows no stress yet |

**Repricing:** the semi-supply consequence of ZHAO's China events + HAWK's Taiwan geopolitics. **First pull (2026-07-12):** TSMC May'26 monthly revenue +30.1% YoY (record) — no chokepoint stress on the revenue line; June print delayed to 7/13/26 (typhoon), VULCAN-05 resolves there. **The export-control picture is NOT simply tightening** — it is genuinely two-sided: the US *eased* (BIS approved H200 sales to China 1/13/26, ~10 buyers cleared by 5/14/26, though paired with a 25% tariff), while Taiwan is *tightening* from the other end — weighing a Foreign Trade Act amendment to criminalize unauthorized AI-chip exports to all of China (undated), with a first concrete enforcement event 7/1/26 (Keelung court detained 3 Super Micro/Albatron execs — Taiwan's first criminal AI-chip-diversion probe). No fixed-date resolver exists for the Taiwan legislative side; monitoring item. Kinetic Taiwan = HAWK cross-flag; China macro = ZHAO — **route-out: neither may have this dated 7/1 event logged from the semiconductor angle.**

## S5 — AI-infra financing — **PROMOTED tier-2 → CORE 2026-08-03** (Will-approved)

| Stage | Mechanism | State |
|---|---|---|
| 1 | AI buildout is funded by debt, off-BS leases and vendor/lessor guarantees rather than operating cash | **confirmed, and larger than the headline names** — ORCL alone: **$260B** off-BS DC lease commitments (FY27-29 commencement, 15-19yr) + **$3.3B** lessor-borrowing guarantee **maturing Sept-2026**; FY26 capex $55.7B vs $32.0B OCF = **−$23.7B** structural gap [FY26 10-K Note 9] |
| 2 | The obligations sit where no leverage ratio computes them | **confirmed** — on balance sheet these look like ordinary levered tech issuers; ⚠️ the **NVDA→OpenAI ~$250B backstop is filed NOWHERE** (entire filed guarantee book **$3.5B gross / $712M escrowed**), so the headline node is the wrong one |
| 3 | Financing capacity is contractually tied to operating inputs, not just leverage | **confirmed, filed** — CRWV's $8.5B DDTL 4.0 re-marks its sizing model for **hedge/SOFR rates and POWER only** (§5.25 Power Cost Protection; §5.23 ≥95% hedging), resolving to **Projected DSCR ≥1.20x** (1.15x maint.), + a **"Negative NOI Event"** repaying **two months before** the first projected-negative month ⇒ **power price → borrowing capacity.** *(Couples S3.)* |
| **3b** | **Regulators write IG thresholds into utility tariffs ⇒ a standing liquidity demand independent of capex** | **🔑 THE INDEPENDENCE LEG. Live.** WI PSC rule (**April 2026**): any DC developer rated **below A-** posts guarantees before service — **>$100M/yr** in deposits/LCs. **NOT downgrade-triggered:** ORCL was already **BBB**, the rule predates the 7/9 cut by 3 months, and ORCL **sued 6/19**. ⇒ **rating LEVEL, not migration, is binding** |
| 4 | Price of access repricing before access is lost | **elevated** — CRWV $2.6B DDTL **cleared +100-125bp wide of talk** (S+550/OID 96-97/**YTM 10.44%**) **at full size**; NVDA 5Y CDS **40→68→~82bp record**, ORCL **~210-215bp record**; GS/JPM **shortable** basket 319bp (18 equal-wtd **neoclouds**) vs HY 279 |
| 5 | Access actually lost → project halts / default | **NOT reached** — no default, no pulled deal, aggregate IG/HY benign, ORCL contesting in court rather than failing to post |

**Repricing:** AI-infra credit spreads (→ **LIQUID**, who owns the spread tells), private-credit marks (→ BROCK), FCF/valuation (→ HENRY), project feasibility (→ WATT).

### Why it was promoted, and the one argument that carried it

The weak case is volume — S5 accreted more filed, dated material in a week than some core channels hold. **That alone would not justify promotion; it would justify a longer sub-read.**

**The argument that carried it: S5 demonstrated it can fire while S1 is NOT firing.** The Oracle collateral requirement is live *while hyperscaler capex is being raised* — it fires on the **balance sheet and the tariff**, not on capex direction. A channel that can only fire when S1 fires is not independent (that is precisely why obsolescence and the returns-case stayed **sub-reads**). S5 cleared that bar; they have not.

⚠️ **Independence is PARTIAL and must be stated every time:** the **ROI-disappointment leg** still shares S1's antecedent — an AI-capex disappointment drives S1 + S3 + S5 at once and **that root is still counted ONCE**. Only the **financing-structure/regulatory leg** is independent.

⚠️ **Scored 3, not 4, and the reason is sourcing rather than severity:** the two strongest datums are the weakest-sourced. The DDTL terms have **no filing at all** — CRWV's last 8-K of any kind is 6/18, and the terms first become verifiable at its **Q2 10-Q (~Aug)** [KB-068]. And the ORCL headline **did not survive verification**: the "$7B" is uncorroborated and its causation was backwards [KB-069]. **Do not score on numbers that verification just corrected.**

**Upgrade triggers → 4:** a cleared AI-infra new issue flexing **+150bp or pulled** · a **second jurisdiction** writing an IG threshold into a tariff · CRWV's Q2 10-Q disclosing terms **worse** than trade press.

---

## Boundaries (reconcile-to-one-figure, don't silo)

- **VIOLET** owns the concentration-*unwind* vol expression (Path-B); **VULCAN** owns the concentration *mechanism/driver*. VULCAN gives VIOLET's channel the fundamental it's been carrying without.
- **HENRY** owns the AI-capex FCF valuation (HEN-36) + macro velocity; **VULCAN** owns the semi/memory/capex fundamentals feeding it.
- **WATT** owns wholesale power price; **VULCAN** owns the compute→power demand driver.
- **ZHAO** owns China macro; **HAWK** owns Taiwan geopolitics; **VULCAN** owns the semiconductor consequence of both.
- **BROCK** owns private credit; **VULCAN** flags AI-infra debt as a fragility channel (S5).
