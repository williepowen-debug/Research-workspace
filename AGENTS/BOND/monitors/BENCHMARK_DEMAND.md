# BENCHMARK DEMAND — mandated-holder index reweightings
**Vector:** `VX-BND-20` (Benchmark-Driven Structural UST Demand) · **Channel:** `FL-BND-14` (LATENT) · **MBS leg:** `VX-BND-17`
**Opened:** 2026-09-04 at Will's direction. **Owner:** BOND. **Last real data refresh: 2026-09-04**

> ## ⚠️ WHY THIS SURFACE EXISTS — read before using it
> **On 2026-09-04 BOND told Will the pension-UST-divestment topic was a stale January story, and added *"if you see it again this week, it's recycled."* NBIM's submission was dated 1 September and hit the wires that morning.** The desk had no vector for announced **benchmark** demand changes, so the largest such event on record arrived and was nearly filed as old news.
> **The failure was not the miss, it was that nothing would have caught it.** `VX-BND-17` (MBS) was **DORMANT**; `VX-BND-13` scores realized *auction* indirect%, which this object will not touch before 2027. **A dormant vector plus an observable-shaped vector equals no coverage of an announced, mechanical, multi-year object.**
> **Method error to keep naming:** three searches keyed on *"Swedish pension"* returned January and that was read as *"the topic is January."* **A search shaped like one instance says nothing about the others.** `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`

---

## 1. What this vector tracks — and what it deliberately does not

**TRACKS:** formal, announced changes to the **benchmark index** of a large mandated holder (sovereign wealth fund, national pension, reserve manager) that alter **government-bond / UST weight**. Index-driven mandates are **mechanical and price-insensitive once adopted** — the manager sells and buys to track, regardless of level or conviction.

**DOES NOT TRACK (scope fence, so this cannot drift):**

| Object | Owner |
|---|---|
| Realized foreign flows, TIC, reserve-manager behaviour, **any holdings level** | **ZHAO** — BOND keeps no foreign-holdings series |
| The JGB leg of any reweighting | **SAM** |
| Realized auction indirect% | `VX-BND-13` / `VX-BND-08` (BOND, but a different instrument) |
| Discretionary sales driven by conviction rather than a benchmark | logged for scale only (§3), not scored here |

**The distinction that justifies a separate vector:** a benchmark change is **announced, mechanical, and multi-year**; auction indirect% is **realized, discretionary, and same-day**. Putting one on the other's row either contaminates a clean observable or gets ignored because the evidence field is the wrong shape. `[[finding_hypothesis_needs_an_instrument_for_its_defining_mechanism]]`

---

## 2. LIVE OBJECT — Norway GPFG (NBIM → Ministry of Finance, 2026-09-01)

**Primary:** `nbim.no/en/news-and-insights/submissions-to-ministry/2026/the-government-pension-fund-global--analyses-and-assessments-of-the-investment-strategy-for-bonds`, read at source **2026-09-04**. Responds to the Ministry's letter of **25 February 2026**. Wire pickup 9/4 (CNBC, Bloomberg, BNN).

| Index component | From | To | Δ | **≈ $ [EST]** |
|---|---:|---:|---:|---:|
| **Government subindex** | **70%** | **50%** | −20pp | — |
| **Non-government** (corp + govt-related + MBS) | 30% | **50%** | +20pp | **+$126B** |
| — of which **MBS** (~13% of new index) | ~0 | **~13%** | — | **+$82B** |
| **US government** | 34.1% | **21.9%** | −12.2pp | **−$77B** |
| Euro-area government | 16.8% | 14.1% | −2.7pp | −$17B |
| **JGB** | 4.6% | **7.4%** | +2.8pp | **+$18B** → SAM |
| **USD currency share** | **"just over 50%"** | **"just over 50%"** | ⚠️ **0** | — |

**Published anchor:** ~**$80B** off ~**$215B** of USTs held at end-June. **Stated rationale:** liquidity sufficiency (*"a comfortable margin to the estimated upper limit for the liquidity needs"*) + market-representativeness vs the **Bloomberg Global Aggregate** — **explicitly not a credit or political judgement on the US.**

### 2.1 🔴 The finding — and it is the opposite of the coverage
> **The USD currency weight does not move. ~$80B leaving Treasuries is almost exactly offset by ~$82B going INTO US MBS. This is a Treasury→spread-product rotation INSIDE the dollar bloc, not de-dollarization.**

**Derivation, shown so it is checkable rather than asserted:** $215B ÷ 34.1% ⇒ **bond index ≈ $630B**, cross-checked independently against GPFG's strategic **28% fixed income** on a ~$2.0–2.3T fund. The −12.2pp US-government leg then yields **≈ −$77B**, which reconciles with the published *"nearly $80B."*
⚠️ **The WEIGHTS are [CONF NBIM primary]. Every dollar figure is [EST] from ONE anchor. Re-derive if NBIM publishes the fixed-income sleeve size — DO NOT harden the estimate by repetition.** `[[finding_loadbearing_number_must_be_reproducible]]`

### 2.2 Why nothing moves — the timeline the coverage buries
Ministry of Finance must take a position → **expert group reports 2027-01-25** → NBIM supplies mandate language + implementation plan → *"the adjustment … should be made gradually out of consideration for market impact and transaction costs"* (one-time transition cost ≈ **NOK 750M**).
⇒ **ZERO effect on the 9/8–9/10 refunding. No vector re-scored, no trigger fired, frozen `I'` bars and the kill spec untouched.** **A benchmark proposal with a 2027 decision point is not an auction-demand event.**

---

## 3. Scale reference — the discretionary cluster, for contrast only *(NOT scored here)*

| Fund | Move | Date | Note |
|---|---:|---|---|
| Alecta 🇸🇪 | ~$7.7–8.8B of ~$11B | staged from early 2025; reported 2026-01-21/22 | |
| ABP 🇳🇱 | >€10B US govt (of €18B US bonds) | 2025 | IPE: **rebalancing**, not a sentiment shift |
| Lærernes Pension 🇩🇰 | ~$560M → Bunds | Dec 2025 | **post-hedge yield pickup; fund says expected return unchanged** |
| AkademikerPension 🇩🇰 | ~$100M (entire book) | 2026-01-20 | **rotated into USD short-duration — stayed in dollars** |
| Japanese life insurers 🇯🇵 | not sized | through 2026 | hedge cost > UST pickup — **SAM/ZHAO** |
| GPIF 🇯🇵 | **none** | — | ⛔ **SPECULATION ONLY — do not carry as a decision** |

**Cluster ≈ $21B over ~18 months, against a $125B single quarterly refunding. Only Norway is size — and Norway is not leaving the dollar.**
🔴 **At least three are explicitly NOT anti-US trades by the funds' own words.** The common factor across the field is **hedged relative value and the price of duration, not credit fear** — which is this desk's own *"expensive, not broken"* thesis rather than evidence against it.

---

## 4. Reconciliation against the measurements that govern

- **ZHAO `KB-ZHAO-122` (June 2026 TIC):** foreign **OFFICIAL** sold **$45.4B**; foreign **NON-OFFICIAL bought $23.2B**. **Every fund in §3 is non-official — they sit in the bucket that was net buying.**
- **BOND's own instrument:** foreign step-away at size would appear in **auction composition**. It has not — **18 consecutive benign resolutions since 7/9**, no composition failure at any tenor on either live definition.

---

## 5. Thresholds *(EVENT-based by design — there is no price series for "benchmark demand", so a level threshold would be untrippable)*

| | Condition | Meaning |
|---|---|---|
| 🟡 **Upgrade to 3** | A **SECOND** mandated holder (>$250B AUM) formally **proposes** a government-subindex or UST-weight reduction | It is a **class**, not one fund |
| 🔴 **Upgrade to 4** | An **ADOPTED MANDATE** (not a proposal) at a holder with a **>$150B UST book**, implementing **inside 12 months** | Announced intent becomes a dated, mechanical supply-absorption problem |
| ⬇ **Downgrade to 1** | The Norwegian Ministry **rejects or materially dilutes** the government-subindex cut | The only live object dies |

⛔ **NO PREDICTION IS REGISTERED ON THIS VECTOR, AND THAT IS THE RULE RATHER THAN AN OVERSIGHT.** There is **no base rate** for sovereign benchmark-reweighting announcements and this desk **refuses a gate below n=6**. Inventing a prior to look rigorous is the failure mode. **A base rate is OWED before any `BND-` row keys on this vector.**

---

## 6. Open items — dated, so they are closable

| Owed | By | Why it matters |
|---|---|---|
| Is the ~13% MBS **agency-only or inclusive of non-agency**? | **2026-10-06** | **Decides whether the ~$82B bid is BOND's lane (`VX-BND-17`) or credit's.** Currently unchecked. |
| GPFG **fixed-income sleeve size** at the primary | opportunistic | Every $ figure here is [EST] off one anchor; publication ⇒ re-derive |
| ZHAO objection / scope confirmation | routed **2026-09-04** | If ZHAO claims the vector, BOND keeps only the MBS leg |
| Ministry of Finance response | unscheduled — **watch** | First point at which "proposal" could become "mandate" |
| **Expert group report** | **2027-01-25** | Hard checkpoint; on `docket/CATALYSTS.tsv` |
| Base rate for the vector class | before any prediction | See §5 |

**Review checkpoint: 2026-10-06.** Refresh this surface at the Ministry response, at any second-holder announcement, and at the 2027-01-25 report.
