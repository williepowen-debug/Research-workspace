# WATT → PROME · Batch-3 P2, power axis: **time-to-power is the cost, and it is 2–15× the price of the power itself**

**From:** WATT · **Date:** 2026-08-04 · **Leg:** PROME Batch-3 dispatch, P2 power-cost asymmetry (Will-approved 2026-07-24, `6619bccf`)
**Start gate:** honoured — began at first boot on/after Mon 8/3. **Deliverable:** this memo + same-session STATUS write-back (done).
**Scope kept:** sovereign transmission (P0/P1), USSR history, and trade construction all left alone.

---

## BOTTOM LINE (four answers, in the order you asked)

1. **YES — time-to-power prices, and the number is large.** A year of delay on a 1 GW AI data center costs **$201–1,283/MWh** depending on how much of the stack is sunk. **US industrial power costs $87.1/MWh.** The delay is **2.3× to 14.7× the commodity.** Time-to-power is not a modifier on the power price — it dwarfs it.
2. **State-directed siting genuinely wins, but NOT because it's efficient — it relocates the cost into a far cheaper currency.** China wastes **electrons** (curtailment rising, utilization hours falling); the US wastes **years**. On my numbers wasting electrons is **roughly an order of magnitude cheaper** than wasting time.
3. **Who bears it is genuinely undecided and I now own the docket** — with the near-term resolver **just having slipped ~90 days** (below).
4. **⚠️ THE 543-vs-53 GW NUMBER SURVIVES — but everyone quoting it is right by accident.** The ~10× holds on capacity (**10.2×**) *and* on annualized energy (**9.4×**). It does **not** appear in realized 2025 output (**4.1×**). And it survives only because **two composition errors cancel**. Details in §4 — this is the loud flag you asked for, and it doesn't say what you expected.

---

## 1. Can "time-to-power" be priced? — **Yes. Here is the number.**

### The delay clock (PJM, verified)
- **Average interconnection wait: 40 months.** Candidate sites average **3.4 years** as of June 2026.
- Projects in **data-center load-growth zones: 36–48 months**.
- Worse end-to-end: **>3 years to an interconnection service agreement, then ~4 more years to come online.**
- Even post-reform, 2026-cycle projects may not reach commercial operation until the **early 2030s**.

### The cost of that clock, per 1 GW
Inputs: **$38B capex per GW** ($38M/MW, Epoch AI May-2026); shell + electrical ≈ **$15B**, equipment ≈ **$23B**. Output at an 85% load factor = **7,446,000 MWh/yr**. WACC 10%.

| What is sunk while waiting | Cost of ONE year of delay | Per MWh of eventual output |
|---|---:|---:|
| Shell + electrical only | **$1.50B/GW** | **$201/MWh** |
| Full stack, cost of capital only | **$3.80B/GW** | **$510/MWh** |
| Full stack + GPU depreciation @25%/yr | **$9.55B/GW** | **$1,283/MWh** |
| *Benchmark — PJM wholesale on-peak* | | *~$48/MWh* |
| *Benchmark — US industrial retail (May-26)* | | *$87.1/MWh* |

**Levelized answer to your exact question** — *"the effective cost-of-compute penalty a US data center pays for queue position"*: carrying the shell through PJM's **3.4-year** average wait costs **$5.10B/GW**, which spread over a 10-year facility life is **$68/MWh — 79% of the entire US industrial power bill.**

> **⇒ Queue position costs a US data center roughly the equivalent of a SECOND power bill.** That is the P2 mechanism on my axis, and it is a bigger number than any ¢/kWh gap anyone has been arguing about.

### The revealed-preference cross-check — and the gap that is itself the finding
PJM's approved reliability backstop caps the large-load charge at **$555/MW-day = $202,575/MW-year = $27.2/MWh** at an 85% load factor. That is the administratively-set price of *skipping the queue*.

**It is 7×–47× below the economic cost of the delay it relieves.** Three consequences, and I'd weight them in this order:

1. **The backstop will be structurally oversubscribed.** At $27/MWh to avoid a $201–1,283/MWh problem, every eligible large load wants it. The binding constraint stays **administrative rationing, not price.**
2. **It explains behind-the-meter and co-location economics completely.** If delay costs $201+/MWh, paying an enormous premium for on-site gas turbines or a co-located nuclear PPA is *trivially* rational. Co-location isn't a tax dodge — it is the market routing around a price cap.
3. **A market-clearing queue-skip price would be far higher than $555/MW-day**, which tells you the cap is doing real distributive work — i.e. it is already a partial answer to your Q3.

**Assumptions I'd want challenged:** the 10% WACC (CoreWeave-class borrowers pay more, hyperscalers less), the 25% GPU depreciation, and the 85% load factor. All three are stated so you can re-run them; none change the sign or the order of magnitude.

---

## 2. Does state-directed siting beat a market queue, or relocate the cost? — **Both, and they are not symmetric**

You asked me not to assume the flattering reading. I didn't, and the unflattering-to-China evidence is real:

**China's system converts capacity into energy WORSE, and getting worse:**
- Curtailment is **climbing** — early-2026 reported rates **9.2% solar / 8.5% wind**, levels not seen for years.
- **China Electricity Council: average solar utilization fell 12%** vs the 2020–23 average — *a much larger drop than the reported curtailment rate implies*, so the headline understates it.
- Gansu-type provinces now exceed **30% VRE share** with serious integration strain.
- Ember: utility-scale storage **"could have shifted 23 TWh more clean power in 2025"** — i.e. measurable waste.
- Structurally: wind+solar are **47.0% of installed capacity (1,840 GW)** but only **~22% of generation.** The capacity is doing progressively less work per GW.

**⚠️ Terminology trap you will hit if you read Chinese sources directly:** China reports a **"utilization rate"** of **94.0% wind / 94.7% solar**. That is **(1 − curtailment)** — an anti-waste metric. It is **NOT a capacity factor.** China's actual solar capacity factor is **~15%** (derived below). Anyone importing "94.7% utilization" into a capacity-factor slot produces nonsense.

**But the asymmetry that matters:** China's failure mode is *throwing away electrons*. The US failure mode is *waiting years*. Curtailing a MWh costs its foregone value — on the order of **$30–60/MWh**. Waiting costs **$201–1,283/MWh** (§1).

> **⇒ China has not built a more efficient system. It has chosen a much cheaper way to be wasteful.** For a compute buildout — where the asset depreciates fast and the revenue window is the whole thesis — **wasting energy is roughly an order of magnitude cheaper than wasting time.** That is the corrected SDI mechanism on my axis: not cost-per-kWh, but **cost-per-year-of-delay.**

---

## 3. Who bears the US cost? — undecided, dockets moving, and I own it

- **PJM capacity prices +10×**, data centers **63%** of the 2025/26 auction rise (**$9.3B**); utilities sought **$29B** of rate increases in H1-2025, 2× YoY.
- Structural confirmation on my own tape: **three consecutive at-cap BRA clears** (26/27 $329.17, 27/28 $333.44, 28/29 $325), the last **6,831 MW short** of the reliability requirement, **$16.4B**.
- **DOOR A — ratepayers** ⇒ prices rise across PJM (~65M people, 13 states + DC) = CPI/consumer squeeze → CARL, HENRY. ⚠️ **Not yet a CPI datum; do not carry it as an inflation input.**
- **DOOR B — data centers** ⇒ hyperscaler opex rises, AI-capex ROI degrades → VULCAN S1, HENRY HEN-36.
- **My call: Door B, ~65%**, registered as **WATT-08** (re-dated 2027-06-30 — see below). §1's cap-vs-cost gap is corroborating: capping the large-load charge at 1/7th–1/47th of the delay cost is already a decision to *not* charge large loads what the scarcity is worth.

> ### ⚠️ CATALYST-WORTHY, and it moved THIS WEEK — you may want a DOCKET row
> **PJM and the Indicated PJM Transmission Owners each moved on 7/28 to hold the show cause in abeyance for 90 days** [Federal Register 91 FR 49426, FR Doc 2026-15779 — FERC Secretary's notice dated 7/30, published 8/4]. They asked for a 5-day answer window; **FERC declined**, setting answers for **5:00 p.m. ET Fri 8/7**. FERC **has not ruled**. **If granted, PJM's substantive filing moves from 8/17 to ~mid-November.**
> ⚠️ **Two corrections to my own prior record, now propagated:** the proceeding is **EL26-67-000**, *not* EL25-49 (that is the earlier **co-location** track); and the PJM order carries a **four**-item directive list that **omits co-location** — FERC limited it to large loads **not** co-located with generation.
> **Tracking:** WATT-07 HIT (abeyance branch) · **WATT-09** = the substantive filing · **WATT-08** = the door itself.

---

## 4. ⚠️ Is the 543-vs-53 GW comparison honest? — **YES on capacity AND on energy. And that is not the good news it sounds like.**

You asked me to flag loudly if the ~10× fails conversion to generation. **It doesn't fail. But it survives for a reason nobody quoting it knows**, and it means something different from what it's used to mean.

### Re-verified at run time (your instruction)

| | Figure | Source |
|---|---|---|
| China total 2025 additions | **~540 GW** (implied: 3,891 GW cumulative, **+16.1% YoY**) | NEA, released 2026-01-28 |
| China wind + solar 2025 | **434.4 GW** (**315.07** solar AC + **119.33** wind), +22% YoY, record | NEA |
| US total 2025 additions | **53 GW** — largest since 2002 | EIA |
| **CAPACITY RATIO** | **10.2×** | — |

**DEWEY's ">430 GW wind+solar" and the ~543 GW headline both verify.** Good numbers.

### The conversion test

| Step | China | US | Ratio |
|---|---:|---:|---:|
| Capacity added 2025 | 540 GW | 53 GW | **10.2×** |
| **Annualized energy from that capacity** | **~862 TWh/yr** | **~91 TWh/yr** | **9.4×** |
| **Realized 2025 output growth** | **+494 TWh** (consumption, 10,368.2 TWh @ +5%) | **+120.9 TWh** (generation, 4,429.5 vs 4,308.6 TWh) | **4.1×** |

*Energy conversion uses each country's own capacity factors — China solar **14.3%** (derived: 1,175 TWh total solar generation ÷ ~858 GW average capacity ⇒ **15.6%**, used conservatively), China wind 22%, US solar 23.5%, US wind 34%, thermal/nuclear/hydro 45%, **storage 0**.*

### 🔑 Why it survives — two composition errors that happen to cancel

1. **28% of the US 53 GW is battery storage (15 GW), which produces ZERO net energy.** It is a shifting device with round-trip losses. The US number is *overstated* as an energy-addition figure.
2. **China's capacity factors are roughly HALF the US's** (solar 14–16% vs 23.5%; wind 22% vs 34%). China's number is *overstated* as an energy figure too.

These are large errors pointing in opposite directions, and they very nearly offset. **The ~10× is right, but for none of the reasons it is cited.** Anyone who "corrects" only one side — the usual move is sneering at Chinese capacity factors — will land on a *wrong* answer of ~5×.

### 🔑 And the honest caveat that matters more than the ratio

**The 10× does not appear in realized 2025 output — that ratio is 4.1×.** Two reasons, and they cut opposite ways:
- **Partial-year effect (temporary, favours China).** Capacity installed *during* 2025 generates for only part of 2025. The annualized ~9.4× lands in **2026 and after**. This is a timing artefact, not a debunk.
- **Rising curtailment (permanent, cuts against China).** §2's evidence — curtailment up to 9.2%/8.5%, utilization hours down 12% vs 2020–23 — means a *growing* share of Chinese nameplate never reaches a wire. **The gap between installed and delivered is widening**, so the realized ratio will land below 9.4× even once the timing artefact clears.

> **⇒ Recommended language for anyone quoting this:** *"China added ~10× the US's generating capacity in 2025 and roughly 9× the annualized energy — though only ~4× showed up in 2025 output, and China's own curtailment is rising fast enough that the delivered gap will be smaller than the nameplate gap."*
> **Do NOT say** *"China added 10× the electricity."* **Do NOT quote China's 94.7% "utilization rate" as a capacity factor.**

### One more units problem in the inherited framing
The packet carried *"700 GW of DC interconnection requests in 2025 — more than total 2023 US consumption of 477 GW."* **Consumption is energy (TWh), not power (GW).** 477 GW is the *average power* implied by 2023 generation (4,183 TWh ÷ 8,760 h = 477 GW) — coherent but sloppily stated, and it invites a peak-vs-average error. The **700 GW** itself is a national aggregate across all ISOs and is widely believed to contain duplicate submissions; PJM's own new-process first cycle is **220 GW**, ERCOT's large-load queue **198 GW**. **I would not put weight on 700 GW as a net figure.**

---

## 5. What this does to the corrected SDI thesis

The premise I was handed — *"China's cheaper electricity"* — is dead on price, and I re-verified my own side: **US industrial retail is 8.71¢/kWh (May-2026, +0.6% MoM)**, which is *my canonical figure* and supersedes the "~9¢" in DEWEY's stub. China is comparable-to-higher. **There is no ¢/kWh asymmetry to build on.**

**What replaces it:** the asymmetry is **time**, and time is expensive in a way ¢/kWh never was. A US data center pays a queue penalty equivalent to **~79% of a second power bill** (levelized), or **$201–1,283/MWh** at the margin of delay — against a Chinese system that connects fast and pays for it by discarding ~9% of its variable output.

**For the misallocation-bust-transmitting-via-recession story that survived P0/P1:** this axis supports it, but reframes the mechanism. The US is not overpaying for electricity. **The US is paying an enormous, largely invisible carrying cost on capital that is built but cannot be energized** — and that cost lands as *deferred revenue and idle depreciating assets*, which is exactly the shape that turns an investment boom into a write-down cycle. **The bust channel is stranded time, not expensive power.**

**Reconciled to one figure with VULCAN** (per canon, and agreed with them today): `~55 GW aggregate utility-reported large-load forecast to 2030 / ~32 GW PJM vetted system-coincident peak growth`. Not two estimates of one quantity — two different quantities.

---

## 6. Confidence, and what would change my mind

| Claim | Tier | What would falsify it |
|---|---|---|
| Time-to-power costs $201–1,283/MWh-equivalent | **PROVISIONAL** | A hyperscaler disclosing that shell capex is *not* sunk ahead of energization (i.e. they sequence to avoid carrying cost), which would collapse the low end |
| 10× survives to ~9.4× annualized energy | **EMPIRICAL** | Revised NEA/EIA capacity data; materially different Chinese capacity factors |
| Realized ratio is 4.1× and will rise then settle below 9.4× | **PROVISIONAL** | 2026 Chinese output growth landing near +850 TWh (would confirm), or below +550 TWh (would mean curtailment is eating more than I've assumed) |
| Door B ~65% | **PROVISIONAL** | WATT-08 / WATT-09 |

**Out-of-scope items I did not touch:** sovereign transmission, USSR history, trade construction. **Not attempted:** a single audited China data-center tariff — DEWEY flagged it as the soft spot and it remains one; regional Chinese siting (Inner Mongolia/Xinjiang) is cheap off-peak but I found nothing auditable, and **§1 makes it largely moot — the asymmetry is time, not tariff.**

**Sources:** NEA 2025 statistics (2026-01-28) · EIA (US generation, capacity additions, retail prices — API pulls this session) · Ember (China solar 1,175 TWh; storage 23 TWh) · China Electricity Council (utilization hours) · Epoch AI (May-2026, $38M/MW) · Carbon Direct / PJM interconnection-reform fact sheet (queue timelines) · Federal Register 91 FR 49426 · PJM BRA results.

— WATT
