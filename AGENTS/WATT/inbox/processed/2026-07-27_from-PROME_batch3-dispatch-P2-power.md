# PROME → WATT · Batch-3 dispatch · **P2 — power-cost asymmetry**

**State:** NEW · **From:** PROME · **Date:** 2026-07-27 · **Disposition:** ACTION (research leg, date-gated)
**Authority:** Will-approved 2026-07-24 (`6619bccf`). Authoritative on owner-map and scope; supersedes DEWEY's 7/24 stub where they differ.

> ## ⏳ START GATE — begin at your **first boot on or after Mon 2026-08-03**
> Do not start before then. If you boot earlier for grid/catalyst work, **leave this packet**. Scheduled into the Aug 3-11 lull deliberately; dispatched early only so it is written with full context.

---

## Why you're on this leg

Will's directed thesis — *"China bankrupts the USA the way the US bankrupted the USSR, via AI spending"* — was largely demolished as stated by DEWEY's framing legs (**P0**: the Reagan/SDI story is mostly myth; **P1**: private AI capex reaches the federal balance sheet via ~$0 committed federal dollars). What survives is a **misallocation-bust-transmitting-via-recession** story. **P2 tests the corrected SDI mechanism: is the US buying AI capability at a materially worse cost-to-capability ratio than China?**

**And your axis turned out to be the one that survived.** DEWEY's carve-out refuted the price premise and left power standing as the *real* asymmetry — via speed and queue.

## ⚠️ The premise you were originally handed is REFUTED. Do not rebuild on it.

The packet's original framing was *"China's cheaper electricity vs US power-constrained data centers."* **Wrong on price:**

| | US | China |
|---|---|---|
| Industrial electricity, 2025 avg | **8.62¢/kWh** (2024: 8.13¢; mid-2026 ~9¢, +8.6% YoY) | **~9.7¢/kWh**; ~11.6¢ business (Apr-2026) |
| Data-center-state retail avg (2025) | top-10 DC states **14.46¢** vs **14.39¢** all others (**≈ identical**) | sited regions (Inner Mongolia/Xinjiang) far below national avg (off-peak) |

**China is comparable-to-slightly-higher on average price.** The "top DC states pay a premium" story also fails — 14.46¢ vs 14.39¢ is noise.

**Right on capacity, speed and queue — this is the live axis:**

| | US | China |
|---|---|---|
| New generating capacity added 2025 | **~53 GW** (largest since 2002); 86 GW planned 2026 | **543 GW (~10×)**; >430 GW wind+solar; ~$500B in one year |
| Interconnection / constraint | **700 GW** of DC interconnection requests in 2025 — **more than total 2023 US consumption (477 GW)**; ERCOT 198 GW large-load Q1-2026; **PJM capacity +10×**, DCs = 63% of the 2025/26 auction rise ($9.3B); utilities sought **$29B** rate hikes H1-2025 (2× YoY) | state-directed siting + grid; no comparable market-queue constraint |

## Your leg — the questions

1. **Is "time-to-power" the real cost, and can it be priced?** The asymmetry converts to **delay + marginal/capacity-cost premiums + rate-base socialization**, not average ¢/kWh. Can you put a number on the *effective* cost-of-compute penalty a US data center pays for queue position? That number, if it exists, is the whole P2 mechanism on your axis.
2. **Does state-directed siting actually beat a market queue, or just relocate the cost?** China can site compute into ultra-cheap-power regions on a state-directed grid. Is that a genuine efficiency edge or a subsidy/misallocation that shows up elsewhere (stranded capacity, transmission losses, curtailment)? **Both readings are live — don't assume the flattering one.**
3. **Who bears the US cost?** PJM capacity +10× with DCs = 63% of the rise, and $29B of sought rate hikes, is a **socialization** question with a consumer/political tail. Note it if it's load-bearing; it may matter more to CARL/HENRY than to the P2 verdict.
4. **Is the 543-vs-53 GW comparison honest?** Capacity ≠ dispatchable energy; >430 GW of China's add is wind+solar with capacity factors well below thermal. **Check whether the ~10× survives conversion to actual generation** before anyone builds on it. If it doesn't, that is a finding and I want it flagged loudly — it is currently the single most quotable number in the whole leg.

**Out of bounds:** sovereign transmission (P1) · USSR history (P0) · trade construction (P4 → RED/HENRY/TERRY).

## Coordination

**VULCAN leads P2** (chip/export-control axis, solo — ZHAO is off P2). **HENRY** carries sterile-capex/FCF. Per root canon, **scoped overlaps are intentional — reconcile shared metrics to ONE figure, don't silo.** Your speed/queue numbers and VULCAN's cost-to-capability numbers touch; agree the figure.

## Run-time freshness

DEWEY's framing is **current-as-of-2026-07-24** and the power/capacity numbers move. **Re-verify at run time** — especially the 543/53 GW and 700 GW queue figures, which are load-bearing.

## Deliverable

- Memo → `AGENTS/WATT/outbox/` addressed to PROME.
- **⚠️ Write back to your own `STATUS.md` the same session.** 7/27 ran 3-for-3 on agents shipping a polished memo and leaving STATUS stale. The artifact plus your state is the deliverable.
- New catalyst-worthy threshold → flag it, I add a DOCKET row.

**Docket:** `PROME/DOCKET.tsv` `2026-08-01..2026-08-02`, owner PROME. **Report (canonical):** `AGENTS/DEWEY/output/2026-07-24_p2-efficiency-asymmetry-deepseek-power.md`.

— PROME
