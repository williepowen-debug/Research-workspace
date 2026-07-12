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

## S3 — AI-capex → power demand (feeds WATT) — GAP

| Stage | Mechanism | State |
|---|---|---|
| 1 | AI-capex → datacenter buildout → compute demand | confirmed (macro) |
| 2 | Compute demand → interconnection + grid MW load | needs sizing |
| 3 | Grid can't supply → power becomes the binding constraint on AI deployment | open (the WATT coupling) |

**Repricing:** hands WATT the demand driver (WATT prices the grid response); power-availability as a gate on AI-capex. **VULCAN owes** the compute→MW sizing; WATT owns the power price (reconcile to one figure).

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
