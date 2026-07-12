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
| 2 | Memory price (spot → contract) + maker capex signal the cycle position | **live: TrendForce 2Q26 DRAM +58-63% / NAND +70-75% QoQ (accelerating up, not rolling)** |
| 3 | A contract-price roll = demand inflection (memory leads the cycle) | open — NOT triggered; opposite extreme currently in effect |

**Repricing:** memory makers, a broad demand-velocity read (→ HENRY), goods/tech demand (→ CARL). **Why it matters:** memory is the most cyclical semi — a contract-price roll is one of the earliest real-economy demand tells. **First pull (2026-07-12):** TrendForce 2Q26 forecast + Micron FQ3 FY26 print (reported 6/24/26, revenue $41.46B vs $32.75-34.25B guide, CEO says can fill only 50-67% of demand) both confirm a structural shortage, not a roll — no capacity relief expected before late 2027/2028. **New cross-channel link (MISSED CONNECTIONS, 2026-07-12): S2 feeds S1 directly.** MSFT and META both cite higher component/memory costs as explicit drivers of their FY26 capex-guide raises (MSFT: ~$25B of its $190B guide = pricing effect). Some fraction of the eye-catching capex $ growth is memory-cost inflation, not purely incremental compute capacity — relevant nuance for how VIOLET/HENRY read the raw capex figures. **Next resolver:** VULCAN-04, SK Hynix Q2'26 print 7/23/26.

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

## S5 — AI-infra financing (tier-2, not yet in the live matrix)

Neocloud/datacenter debt + vendor financing → credit fragility if AI-capex ROI disappoints. Couples to BROCK (private credit) + HENRY (FCF). **Build only after S1–S4 prove out.**

---

## Boundaries (reconcile-to-one-figure, don't silo)

- **VIOLET** owns the concentration-*unwind* vol expression (Path-B); **VULCAN** owns the concentration *mechanism/driver*. VULCAN gives VIOLET's channel the fundamental it's been carrying without.
- **HENRY** owns the AI-capex FCF valuation (HEN-36) + macro velocity; **VULCAN** owns the semi/memory/capex fundamentals feeding it.
- **WATT** owns wholesale power price; **VULCAN** owns the compute→power demand driver.
- **ZHAO** owns China macro; **HAWK** owns Taiwan geopolitics; **VULCAN** owns the semiconductor consequence of both.
- **BROCK** owns private credit; **VULCAN** flags AI-infra debt as a fragility channel (S5).
