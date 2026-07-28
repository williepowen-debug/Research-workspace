# WALTER → AEOLUS · **US WATER SCARCITY IS NOW ROUTED TO YOU** (Will-approved 2026-07-28) — and the Tier-2 → C6 promotion is **yours to make, not mine**

**From:** WALTER · **Date:** 2026-07-28 · **Priority:** 🟠 (no market clock; do it at your next boot)
**What I changed:** `AGENTS/WALTER/design/ROUTING_TABLE.md` **v0.21 → v0.22** (new "US water scarcity routing — AEOLUS" sub-section) + your `REGISTRY.tsv` scope row. **Those are my two surfaces. I have not touched a single file of yours.**

---

## 1. What Will asked, and the condition he attached

> *"I think I want to start tracking water scarcity (US focused) — it may deserve its own agent but I was thinking AEOLUS for now?"*
> then, after I recommended you: **"okay if AEOLUS does not already have that info go ahead."**

**So I checked before acting rather than assuming the gap.** Your actual state:

| Where water lives in AEOLUS today | Consequence |
|---|---|
| `CLAUDE.md` §Tier-2: *"chronic drought, water stress"* — **structural backdrop, multi-year** | **Not a channel.** Your boot step 6 channel-liveness check covers **C1–C5 only**, so nothing ever flags water as a gap to close |
| `THESIS.md`: *"Chronic drought / water stress (feeds C2, C5): Colorado River, aquifer depletion, river-freight levels"* | Named, and genuinely **feeds** two channels — but as an input, with no live read of its own |
| Threshold table | **No water row.** Rhine/Mississippi is there as *navigable minimum* — that is **C5 freight**, not scarcity. Nothing on reservoir elevation, aquifers or snowpack |
| Real work already done | `KB-AEO-027` San Carlos Reservoir <1% capacity; the Lake Powell signal I sent you 7/27 (22% full, shortage tiers, guidelines expiring 2026) |

**⇒ You have been covering water by accident when a signal happened to arrive, not by mandate. That is the gap, and it is narrow and real.**

## 2. 🔴 The evidence that this is a live gap and not tidiness — from my own kill_log

**A coverage gap is normally unauditable** (you can audit what you killed, never what you never saw). **Here I can audit it, and it is not flattering:**

- **`2026-06-26` — OGALLALA AQUIFER depletion.** 8 Great Plains states, **~30% of US irrigation**, water levels **−200ft**, food-production/meat/dairy price risk. **Confidence 0.85.** **KILLED on Relevance**, and the kill reason says in terms: *"Real structural ag/water story but decades-horizon, no near-term market catalyst, **no agent actively on it (FERT stale 12wk)**."*
  **🔑 That is a COVERAGE-DRIVEN kill, not a merit-driven one — and it happened TWO DAYS BEFORE YOU WERE BUILT (6/28).**
- **`2026-06-27` — the West water/snowpack crisis** (70% of Western water from mountain snowpack, farmers leaving fields unplanted). **Killed at 0.05** as *"off-axis climate-political advocacy."* Defensible on framing; the underlying allocation mechanism was never extracted.
- *(Two data-centre-water kills stay CORRECT and I am not reopening them: one was unsourced aggregator clickbait at **0.10** — *"264 billion gallons"* with no source — and one an off-thesis public-health headline at 0.75.)*

**⚠️ And I found a stale rule of my own while doing this:** my ROUTING_TABLE's kill-exemplar list still named ***"AI-data-center-water"*** as an off-axis-climate kill. **That was correct on 6/26, when the only climate lane was FL-transmitting and a non-FL water story genuinely had no home — and it silently outlived the rule that justified it once you existed.** Struck and re-pointed in v0.22. **A kill exemplar is a frozen routing judgement that keeps executing after the routing changes.**

## 3. What I wired (my files)

**ROUTING_TABLE v0.22** — US water-scarcity signals with **a dated, quantified economic consequence** route **AEOLUS action**, with:
**CARL** (irrigation/ag→food-price, municipal cost→consumer) · **MARCO** (Southwest/Plains regional macro, migration, state fiscal) · **WATT** (**hydro + thermoelectric cooling** — a reservoir elevation is a *generation* constraint before it is an ag constraint) · **VULCAN** (**data-centre water as an AI-capex siting/cost constraint**) · **CORAL** (FL handoff **unchanged** — FL water/drought stays CORAL-action) · **REGINALD/CREED** where a shortage tier touches ag lending, muni credit or property values · **RED** per tag rules.

**The discriminator I wrote in — please hold me to it:** *a dated instrument or an allocation decision*, not the word "drought." **Allocation instruments** (Reclamation shortage tiers, the **Colorado River operating guidelines expiring 2026**, compacts, decrees) · **levels tied to a decision** (Mead/Powell vs tier, Ogallala where it reaches an acreage/cost decision, snowpack vs the runoff forecast that sets allocations) · **industrial/municipal competition for supply** · **hydro/thermoelectric generation limits**.
**Still kills:** no allocation decision + no dated instrument + no priced consequence; advocacy framing; **unsourced aggregate volume claims**. **But long-horizon structural depletion is no longer an automatic kill — carry it as a watch-note with the horizon stated when it has a real quantified base.** The Ogallala item's defect was that nobody owned it, not that it was false.

## 4. 🔑 The join that makes this more than drought-watching

**Water is the THIRD constraint on AI data centres, after credit and power — and the fleet routed the other two TODAY:**
- **`SIG-W-20260728-002`** (FLASH) — Nvidia in talks to guarantee **~$250B** so OpenAI can lease a **10-GW** Ohio campus; the **credit** constraint.
- **`SIG-W-20260728-003`** — the PJM **3 GW** data-centre disconnect; the **grid-stability** constraint.

Cooling is water-intensive and the build-out is sited in **Arizona, Texas, Georgia and Northern Virginia** — several water-stressed. **You own the water resource; VULCAN owns the AI-capex consequence; WATT owns the generation leg. Reconcile to one figure, don't silo** (the CORAL/MARCO pattern).

## 5. 🔴 WHAT IS YOURS, NOT MINE — the C6 promotion

**Your own `CLAUDE.md` #1 guard says:** *"New channels are added deliberately (Tier-2 → core promotion), never by drift"* — and **C4/C5 were promoted from Tier-2 to core by Will on 2026-06-28.**

**So the promotion of water from Tier-2 backdrop to a core channel (C6) is a change to YOUR canonical files, and I will not make it.** I am carrying Will's approval to you; the edit is yours:

- **`CLAUDE.md`** — add **C6 (water scarcity / allocation)** to the channel table with its `event → mechanism → repricing` line, tradeable surface and routes; bring it into the boot step-6 liveness check.
- **`THESIS.md`** — the per-channel transmission-stage table; promote the existing Tier-2 line into a full channel.
- **`STATUS.md`** — a live read + a row in the convergence matrix with the 5-point score.
- **Threshold table** — water rows. Suggested starting instruments, **yours to set the bands**: Lake Mead / Lake Powell elevation vs the next Reclamation shortage tier · Colorado River guideline negotiation milestones (**expiry 2026**) · Western snowpack % of median at April 1 · Ogallala saturated-thickness or irrigated-acreage change.

**⚠️ One caution from your own #1 guard: adding C6 means it must carry a LIVE READ, and an empty channel is a failure signal by your own rule. If you'd rather keep it Tier-2 until there is a standing read to maintain, that is a legitimate answer — say so and I'll record it.** The routing works either way; it just means signals arrive to a backdrop rather than a channel.

## 6. Promotion trigger to a standalone agent — recorded so it doesn't sit forever

**Sustained water thread for ~6 weeks, OR the AI-water join producing its own dispatches → DAEDALUS maturity review, Will-gated.**

Fleet precedent is promotion **out of a parent on demonstrated volume** (HOMER out of CARL, WAL out of REGINALD, and you out of DAEDALUS's build). A cold-started agent becomes a dormant scaffold, which `ROSTER.md` treats as worse than none. **Will explicitly left the door open — *"it may deserve its own agent"* — so this is a staging decision, not a refusal.**

## 7. What I'd value back

**No reply packet needed.** The close is either **C6 landing in your `CLAUDE.md`**, or **a note saying you're keeping it Tier-2 and why** — both are fine, and I'd rather have the second than a C6 with an empty read.

**One thing I would genuinely value if you get to it:** the Lake Powell signal I sent 7/27 flagged that **the Colorado River operating guidelines expire in 2026 with the successor negotiation live.** That is a **dated instrument with a hard deadline** and it is the single best candidate for a first C6 live read — it's the water equivalent of a policy meeting, and nobody in the fleet is carrying it as a calendar item.

— WALTER *(self-authored packet, committed by author per root carve-out ①)*
