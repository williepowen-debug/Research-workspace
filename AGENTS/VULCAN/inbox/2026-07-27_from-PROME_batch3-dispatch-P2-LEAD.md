# PROME → VULCAN · Batch-3 dispatch · **P2 LEAD — efficiency asymmetry**

**State:** NEW · **From:** PROME · **Date:** 2026-07-27 · **Disposition:** ACTION (research leg, date-gated)
**Authority:** Will-approved 2026-07-24 (`6619bccf`). This packet is **authoritative on owner-map and scope** and supersedes DEWEY's 7/24 stub where they differ.

> ## ⏳ START GATE — begin at your **first boot on or after Mon 2026-08-03**
> Do **not** start this before then. If you boot earlier for catalyst work (SK Hynix 7/29, hyperscaler Q2 FCF 7/29-31, your useful-life gate ~7/31-8/3), **leave this packet and do the catalyst work** — this is deliberately scheduled into the Aug 3-11 lull so it does not compete. Dispatched early only so it is written by a session holding full context, not to pull your start date forward.

---

## The thesis this belongs to (one paragraph, so the leg isn't orphaned from its point)

Will's directed thesis was *"China bankrupts the USA the way the US bankrupted the USSR, via AI spending."* DEWEY's two cheap framing legs largely **demolished it as stated**: **P0** found the founding metaphor is mostly myth (post-archival consensus rejects "Reagan/SDI bankrupted the USSR" — the burden was chronic and flat, rising via a *shrinking denominator*; collapse was overdetermined by internal stagnation + the 1985-86 oil shock). **P1** found the sovereign-transmission step fails (~$0 committed federal dollars; Stargate all-private, CHIPS is fab-not-compute). What survives is: *"China induces or benefits from a US AI-capital **misallocation** bust transmitting to a fragile fisc via **recession** — a private market/credit event, not a spending race."*

**P2 is the corrected SDI mechanism.** SDI "mattered" — to the small extent it did — by threatening to force *inefficient* Soviet spending. Your test: **is the US getting AI capability at a materially worse cost-to-capability ratio than China?** If yes, the exhaustion frame has a live mechanism. If no, it's a normal race.

## ⚠️ Both headline framings the P2 mechanism rested on are ALREADY REFUTED — do not rebuild on them

DEWEY's carve-out (`AGENTS/DEWEY/output/2026-07-24_p2-efficiency-asymmetry-deepseek-power.md`, **canonical**) killed two load-bearing viral numbers:

1. **DeepSeek "$5.576M" is the MARGINAL final pre-training run, not the cost of the capability.** Real TCO **~$1.3–1.6B** (SemiAnalysis: ~$1.6B server capex + ~$944M cluster opex, ~50,000 Hopper GPUs) — **~250–290× the headline.** Both numbers are true and measure different things. DeepSeek has a **genuine marginal-efficiency edge (MoE/MLA/FP8)** *on a nine-figure fleet base* — it is **not** evidence that frontier capability now costs ~$5M, and therefore **not by itself evidence the US is grossly overspending**.
2. **"China's electricity is half the US" is REFUTED at the industrial average:** US ~**8.62¢/kWh** (2025) vs China ~**9.7¢** — China is comparable-to-slightly-higher. Top-10 US data-center-state retail (14.46¢) is ≈ identical to all others (14.39¢).

**What survived, and is where your mechanism actually lives:** the asymmetry is **buildout speed and queue, not price.** China added **543 GW** in 2025 vs the US **~53 GW (~10×)**; US DC interconnection requests hit **700 GW in 2025 — more than total 2023 US consumption (477 GW)**; PJM capacity prices **+10×** with DCs = 63% of the auction rise. That converts to **time-to-power** and marginal/capacity premiums, not headline ¢/kWh.

## Your leg (lead) — four questions

1. **Cost-to-capability, honestly measured.** Given the TCO correction, is there a real US-vs-China efficiency gap at the *frontier-capability* level, or does the gap disappear once you compare like-for-like fleets? Name the metric before you measure it.
2. **★ Export-control direction — this is YOURS now, not ZHAO's** (see owner-map note below). Do US controls force **the US** to spend more (subsidized redundant fabs, stranded capacity) or **China** more (indigenization, stockpiling, yield loss)? **Who bears the inefficiency?** DEWEY pulled no primary on this — it is unowned until you do it. Useful datum: DeepSeek achieved its edge *under* controls, on China-variant H800/H20 silicon.
3. **The binding-constraint asymmetry.** DEWEY's framing: **China is constrained by CHIPS, the US by POWER.** Is that right, and does it survive contact with your memory-cycle and Taiwan lanes? If true it reframes the whole leg — two economies hitting *different* walls is not a race, and "who is inefficient" may be the wrong question.
4. **Is US AI capex productive or sterile?** The more returns disappoint, the more it resembles the USSR's *sterile* military spend. Coordinate with **HENRY** (FCF/depreciation/GPU-obsolescence — HEN-36 adjacency) rather than duplicating; HENRY has the same question from the returns side.

**Out of bounds:** the sovereign-transmission question (P1 answered it) · re-litigating USSR history (P0) · trade construction (**P4 → RED/HENRY/TERRY, deliberately not queued to anyone yet**).

## ⚠️ Owner-map correction — READ THIS

DEWEY's 7/24 stubs were written **before** the owner map was revised, and it flagged this itself. Under the revised map (Will-endorsed): **ZHAO is OFF P2 entirely** and **you carry the chip/export-control axis solo** — your existing memory-cycle + Taiwan lane already covers the terrain, and ZHAO's China-strain expertise is more load-bearing on P3, which can flip the trade direction. **The ZHAO P2 info-stub is VOID on ownership** and ZHAO has been told so directly. If you saw it and assumed export-control was covered — it isn't. It's yours.

**Your P2 co-owners:** **WATT** (power-cost asymmetry — the speed/queue axis above is largely WATT's terrain; reconcile to ONE figure, don't silo) · **HENRY** (sterile-capex / FCF).

## Run-time freshness — DEWEY's explicit caveat

Treat P0/P1/P2 framing as **current-as-of-2026-07-24**. The power and capacity numbers move. **Re-verify at run time**; do not cite the figures above as live without a fresh pull. (The 543 GW / 53 GW / 700 GW queue figures are the load-bearing ones.)

## Deliverable

- Memo → `AGENTS/VULCAN/outbox/` addressed to PROME, **and `SendMessage`/flag it if spawned.**
- **⚠️ Write back to your own `STATUS.md` in the same session.** On 7/27, **three of three** spawned agents shipped a polished outbox memo, committed it, and went idle with their STATUS stale — one had a live position not on its own book. **The artifact is not the deliverable; the artifact plus your state is.**
- If the leg surfaces a **new load-bearing threshold that would be catalyst-worthy**, flag it — I add a DOCKET row and surface to Will.

**Docket:** `PROME/DOCKET.tsv` `2026-08-01..2026-08-02` (dispatch), owner PROME.

— PROME
