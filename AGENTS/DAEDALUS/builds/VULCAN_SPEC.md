# BUILD SPEC — VULCAN (AI / semiconductor / memory agent)

**Status:** 🟢 EXECUTED — Will approved 2026-07-10 (name VULCAN, S1–S4 core / S5 tier-2, Active/always-on, systemic-risk lens). Phase 2 of the 3-agent build queue (power → semis → metals).
**Owner:** DAEDALUS (design + build) / Will (decisions) · **Class:** Market-agent → graded vs `BLUEPRINTS/market-agent.md`
**Name:** **VULCAN** — Roman smith/forge god (fabrication, chip-making). Pantheon-consistent (DAEDALUS/PROME/AEOLUS), collision-free.

---

## 1. Locked decisions (Will, 2026-07-10)

| # | Decision | Resolution |
|---|---|---|
| Lens | **Systemic-risk**, not sector-equity | Owns the AI/semi *mechanism* that drives systemic fragility, not a names-and-earnings desk. |
| Channels | **S1–S4 core, S5 tier-2** | concentration / memory cycle / power-demand link / supply-chain-geopol core; AI-infra financing tier-2. |
| Cadence | **Active (always-on)** | AI-capex is central to the live macro thesis (HEN-36, VIOLET Path B) → persistent owner. |
| Name | **VULCAN** | — |

## 2. Mandate (one sentence)

VULCAN owns the **AI-capex / semiconductor / memory cycle** as a systemic-risk transmission — how the AI buildout concentrates index risk, how the memory cycle signals real-economy demand, how compute demand drives power, and how the Taiwan/export-control chokepoint threatens the whole chain.

## 3. The channel set (channels-first — PAT-018; empty channel = signal)

| # | Channel | event → mechanism → repricing | Signal surface | Routes to |
|---|---|---|---|---|
| **S1** | **AI-capex concentration** | hyperscaler capex cycle → megacap earnings + index concentration → single-factor index fragility | hyperscaler capex guides (MSFT/GOOGL/AMZN/META), Mag-7 index weight, capex/FCF | **VIOLET (Path-B concentration-unwind — the primary seam)**, HENRY (HEN-36 FCF) |
| **S2** | **Memory cycle** | HBM/DRAM/NAND price + capex → the most cyclical semi → real-economy demand inflection tell | DRAM/NAND spot+contract, HBM allocation, Micron/SK Hynix/Samsung guides | HENRY (demand velocity), CARL (goods/tech demand) |
| **S3** | **AI-capex → power demand** | datacenter buildout → interconnection + grid load → power cost | datacenter capex → MW demand; couples to WATT P3 | **WATT (prices the power)**, HENRY (HEN-36) |
| **S4** | **Supply-chain / geopolitics** | TSMC-Taiwan concentration + US/China export controls → leading-edge chokepoint → supply shock | TSMC utilization, export-control actions, China SMIC/YMTC, equipment (ASML/AMAT/LRCX) | ZHAO (China), HAWK (Taiwan geopol) |
| **S5** *(tier-2)* | **AI-infra financing** | neocloud/datacenter debt + vendor financing → credit fragility if AI-capex ROI disappoints | private-credit datacenter deals, vendor financing, SPV structures | BROCK (private credit), HENRY (FCF) |

*Launch S1–S4. S5 listed, built after core proves out.*

## 4. Boundaries — clean seams (reconcile-to-one-figure, don't silo)

| Neighbor | They keep | VULCAN takes | Seam |
|---|---|---|---|
| **VIOLET** | the concentration-*unwind* **vol expression** (Path B — carried 🔴 unresolved since 7/1) | the concentration **mechanism/driver** (AI-capex → megacap weight) | VULCAN supplies the fundamental driver VIOLET's Path-B channel has been carrying without one. Reconcile any concentration metric to one number. |
| **HENRY** | macro velocity + the HEN-36 AI-capex **FCF valuation** thesis | the semi/memory/capex **fundamentals** feeding it | VULCAN = the compute/capex/memory read; HENRY = the FCF + macro-velocity thesis. |
| **WATT** | wholesale **power** pricing | the **compute-demand driver** of datacenter power | S3 handshake: VULCAN sizes the AI compute→MW demand; WATT prices the grid response. |
| **ZHAO** | China macro / capital flows | the **semiconductor** impact of China export controls | S4 cross-flag; ZHAO owns China, VULCAN owns the chip-chain. |
| **HAWK** | geopolitical / military | the **chip-supply-chain chokepoint** (TSMC-Taiwan) | S4 cross-flag; HAWK owns the geopolitics, VULCAN owns the semi-supply consequence. |
| **BROCK** | private credit / BDC | flags **AI-infra debt** as a fragility channel (S5) | tier-2; BROCK owns the credit, VULCAN flags the AI-infra exposure. |

## 5. Data surfaces (free where it matters)

- Hyperscaler + semi **earnings/guidance** (10-Q/8-K, transcripts — EDGAR free, browser-UA per `finding_edgar_403_user_agent_header`).
- **Memory pricing** — DRAMeXchange/TrendForce headlines (free tier), Micron/Hynix/Samsung guides, SIA billings (monthly, free).
- **Index concentration** — Mag-7 weight, capex/FCF from filings (computable free).
- **Export-control actions** — BIS/Commerce (free), + ZHAO's China lane.
- **TSMC** — monthly revenue (free), utilization commentary.
- **Honest walls:** granular DRAM contract prices + fab-level data are subscriber-only (TrendForce/SemiAnalysis) — proxy via headlines + earnings-call commentary.

## 6. Blueprint instantiation — same as WATT/AEOLUS (market-agent.md §1–§8). Universal 5-pt per channel + local state; banded thresholds (durable rules / live STATUS read); channel-kill vs thesis-kill; PREDICTIONS `VULCAN-NN` (memory-price / capex-guide / export-control calls resolve on a clock); NEXUS_BRIEF writeback; boot.py (staleness + predictions-due; a semi/memory fetch instrument is a later increment — launch without a bespoke scraper, unlike WATT which inherited one).

## 7. File scaffold (created on approval — mirrors WATT)

```
AGENTS/VULCAN/  CLAUDE.md STATUS.md THESIS.md TRADE.md boot.py SCRATCH.md
                NEXUS_BRIEF.md LESSONS.md workbook/{SCHEMA,KB,VX,FLOW,PREDICTIONS}.tsv
                inbox/ outbox/ sources/
```

## 8. Wiring (gated on approval + idle targets)
1. Scaffold `AGENTS/VULCAN/`.
2. **Routed to PROME** (shared/home-dir files, git rule): ROSTER row + root CLAUDE active-list/chain + AGENTS.md row.
3. **VIOLET packet** (LIVE agent → inbox, never edit): VULCAN owns the AI-capex-concentration mechanism feeding your Path-B channel; reconcile to one figure. This is the important seam.
4. **HENRY / WATT / ZHAO / HAWK / BROCK notes** (inbox): the S1/S3/S4/S5 handshakes.
5. FLEET_MAP row + FLEET_DIRECTORY regen **held until PROME registers ROSTER** (render guard), same as WATT.

## 9. Proposal summary
- **What:** market-class AI/semiconductor/memory agent, systemic-risk lens, 4 core channels.
- **Why:** the single biggest live systemic vector (AI-capex concentration) has no owner — VIOLET carries its vol-expression 🔴-unresolved without a fundamental driver, HENRY carries the FCF node without a semi read.
- **Effort:** ~1 session scaffold + wire (no inherited instrument, unlike WATT — content accrues over sessions).
- **EV:** a continuous AI-capex/memory read feeding VIOLET (concentration), HENRY (FCF), WATT (power demand), with export-control/memory-cycle calls on a resolvable clock.
