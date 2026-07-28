---
signal_id: SIG-W-20260728-003
date: 2026-07-28
time_dispatched: 2026-07-28T14:4xZ
origin: Will-Telegram 10-image batch 2026-07-28 (@MorePerfectUS relaying NBC4 Washington, 770K views) — verified and MECHANISM-CORRECTED by WALTER at intake
source: US News/AP 7/22; DataCenterDynamics 7/22; NBC4 Washington; PJM Interconnection + Dominion Energy statements as reported; TechCrunch 7/25
domain: POWER_GRID
cluster: AI_INFRA_CAPEX
cluster_secondary: MISC
precedence: PRIORITY
signal_role: primary_substance
signal_type: event
action: [WATT, VULCAN]
info: [HENRY, CARL, AEOLUS, NEXUS, RED, PROME]
confidence: 0.85
verify_verdict: CORRECTED-FRAMING — the EVENT is confirmed and larger than posted; the posted CAUSAL MECHANISM is INVERTED
verify_method: WebSearch multi-source cross-check against AP/US News, DataCenterDynamics and the NBC4 original, 2026-07-28
---

# ⚡ **3 GIGAWATTS OF DATA-CENTRE LOAD DROPPED OFF PJM IN ONE EVENT AND TOOK ~10 MINUTES TO STABILISE — BUT THE VIRAL FRAMING HAS THE MECHANISM EXACTLY BACKWARDS, AND THE REAL MECHANISM IS THE MORE DANGEROUS ONE.**

**The event is real, confirmed, and BIGGER than the post claims. The CAUSE in the post is wrong — and correcting it changes this from a capacity story into a CORRELATED-AUTOMATION story.**

---

## 1. WHAT HAPPENED (confirmed)

**Wednesday 2026-07-22.** An area transmission line went out of service in **northern Virginia** — Ashburn, *"Data Center Alley,"* the largest concentration of data centres in the world.

- **>3 GIGAWATTS of demand went offline** — **~3% of PJM's total electric demand at that moment.**
- **PJM** serves **67 million people**, Washington DC to Chicago.
- The voltage disturbance was **felt from Washington DC to Chicago**.
- **Grid disturbances normally correct in MILLISECONDS. This one took ~10 MINUTES to stabilise.**
- Customers in northern Virginia reported **flickering lights and noises from air conditioners and refrigerators**.

## 2. 🔑 THE MECHANISM CORRECTION — AND IT INVERTS THE STORY

**The post says:** *"a concentration of data centers **straining the grid**"* caused the flicker.

**Dominion Energy's actual account:** when the transmission line went out of service, **the data centres' OWN CONTROL SYSTEMS UNPLUGGED THEM FROM THE GRID and transferred them to backup power.**

**⇒ THE DATA CENTRES DID NOT OVERLOAD THE GRID. THEY ABANDONED IT — SIMULTANEOUSLY, AUTOMATICALLY, AND FASTER THAN ANY OPERATOR COULD RESPOND.** The disturbance came from the sudden **ABSENCE** of 3 GW of load, not from excess draw.

**Why the correction matters more than the event:**

| Posted framing | Actual mechanism |
|---|---|
| Data centres consume too much → grid strains | Data centres **self-protect** → 3 GW of load vanishes in sub-second time |
| Fix = build more generation / transmission | Fix = **change the protective settings**; generation is irrelevant to this failure |
| Risk scales with **demand growth** | Risk scales with **CONCENTRATION + IDENTICAL AUTOMATION** |
| A capacity problem | **A CORRELATED-CONTROL problem** |

**🔴 THE REASON THIS IS THE MORE DANGEROUS VERSION: every hyperscale facility runs the same protective logic for the same commercial reason — an operator whose uptime SLA is the product will always drop the grid rather than risk the load.** So the disconnection is **not a diversified population of independent decisions; it is one decision executed simultaneously by everybody.** **A grid can plan for load growth. It cannot easily plan for 3 GW of its largest customers leaving at the same instant, by design, in response to a fault that did not threaten them.**

*(TechCrunch framed it 7/25 as *"one fallen power line exposed a growing AI data center problem"* — the correct emphasis.)*

## 3. ⚠️ A GEOGRAPHIC OVERSTATEMENT IN THE POST — do not propagate

The post says the flicker ran ***"from Chicago to Boston to Miami."*** **Reporting describes the footprint as Washington DC to Chicago — which is PJM's territory.** **Boston is ISO-NE and Miami is FRCC — different interconnection regions, neither in PJM.** NBC4's own headline says *"across half the U.S."*

**Carry: "felt across PJM, DC to Chicago." Do NOT carry "Boston to Miami."** *(The event is impressive enough at its true size; the inflated version is the one that gets refuted and takes the real datum with it.)*

## 4. 🔑🔑 THE JOIN THAT MAKES THIS URGENT — READ WITH TODAY'S `SIG-W-20260728-002`

**Today's FLASH reports Nvidia in talks to guarantee ~$250B so OpenAI can lease a 10-GIGAWATT campus in southern Ohio. OHIO IS IN PJM.**

**⇒ 3 GW leaving PJM simultaneously destabilised the largest US grid for ten minutes on 7/22. The campus being financed this week is more than THREE TIMES that size, on the same interconnection.**

**And it lands on the cost question already routed:** `SIG-W-20260727-026` framed PJM's **$555/MW-day** backstop procurement as a **switch** routing AI power cost to **ratepayers** or to the **data centres**. **This event adds a second, separate question to that fight: not just who PAYS for capacity, but WHO IS RESPONSIBLE FOR STABILITY when the largest loads are also the fastest to disconnect.** A capacity payment does not buy ride-through behaviour.

⚠️ **STATED AS A READ-ACROSS, NOT A PREDICTION: phase 1 of the Ohio campus is ~800 MW and is scheduled for 2028, the guarantee is unsigned, and nothing says the new campus would use the same protective settings. What is established is that the ONE observed instance of this failure mode came from ~3 GW, and PJM is being asked to host a multiple of that.** **WATT owns the adjudication.**

## 5. WHAT THE ACTION OWNERS OWE

- **WATT** — (a) is the corrected mechanism (correlated automatic disconnection) already in your grid-stress frame, or has that frame been built around **demand growth**? (b) Does the 7/17 ratepayer-advocate FERC filing on data-centre **transmission** costs touch ride-through/protective settings, or only cost allocation? (c) **Is there a registered threshold that this should be attached to?** — there is currently nothing in the 15-trigger array that would fire on a grid-stability event.
- **VULCAN** — this is a cost/feasibility input to AI-capex that is **not** a chip or a power price: if hyperscale interconnection starts carrying ride-through obligations or stability penalties, **that is a new cost line on the same balance sheets `-002` is about.**

---

**Verdict: the event CONFIRMED and understated in size; the causal mechanism CORRECTED (inverted); one geographic claim REFUSED.** *(Will-Telegram batch 7/28; WALTER-verified at intake, no sub-agent.)*
