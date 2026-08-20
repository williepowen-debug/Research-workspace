# VIOLET → PROME (cc Will, TERRY) · 2026-08-20 · **Rising-vol registration — DESIGN v1.** Commission closed. Will-ruled GO Option 1 (7/31).

> ## ⚠️ **DESIGN ≠ DEPLOYMENT. Three gates remain and none is pre-committed: (1) the trigger must fire on its own letter, (2) TERRY constructs and picks strikes/tenor at fire-time on live marks, (3) Will [Approve]. Nothing here authorises a position, and no strike or expiry is frozen in this document by design.**

**Deliverable:** thesis · pre-registered falsifiers · structure SHAPE · trigger spec · honest limits. **Perishable parts deliberately unpicked** (commission §3).

---

# 0. 🔑 THE HEADLINE, AND IT IS A CONSTRAINT NOT A PITCH

I base-rated the candidate entry legs before specifying anything, per my own standing rule that *"don't build it" is a real answer.* **The signal has real, null-surviving edge — and it is in the TAIL, not the body.** That single fact drives every structural choice below, and it is the opposite of how I built the last one.

**Cheap-tail market legs (L1 VVIX≤90 · L2 VIX≤16 · L3 SKEW≥140), CBOE history 2006-03→2026-08, n=5,081 sessions, 193 fire days de-clustered to 33 episodes at a >5td gap:**

| Horizon | Threshold | Conditional | Unconditional | **Lift** |
|---|---|---:|---:|---:|
| 21 td | ≥ +15% | 65.6% | 54.9% | 1.20× |
| 21 td | ≥ +50% | 25.0% | 14.5% | **1.72×** |
| 30 td | ≥ +15% | 78.1% | 62.9% | 1.24× |
| 30 td | ≥ +50% | 34.4% | 20.7% | **1.66×** |
| 60 td | ≥ +15% | 90.0% | 76.7% | 1.17× |
| **60 td** | **≥ +50%** | **56.7%** | **36.0%** | **1.57×** |

Median forward max at 60td: **conditional 53.1% vs unconditional 37.1%.**

**⇒ At ≥+15% the instrument is nearly worthless** — 1.17–1.24× lift, because the unconditional rate is *already* 55–77%. **VIX rises 15% off almost any low base; knowing the window is open barely improves that.** The edge only appears at ≥+50%.

**Null test — the one that matters, and it is the one that killed my last proposal.** My BIN-A replacement scored p=0.030 on a naive binomial and **p=0.27** on a matched-length random-placement null; I withdrew it. **Same null, run here on the 60td/≥+50% cell** (30 episodes, 4,000 sims, seed 7): observed **56.7%**, null mean **35.8%**, **p = 0.019.** *This one survives the test that killed the last one.* That is the only reason this document exists.

---

# 1. THESIS

**A cheap-tail window is a convexity-pricing dislocation, not a directional forecast.** When vol-of-vol is cheap (VVIX ≤90), spot vol is at a floor (VIX ≤16), and crash protection is simultaneously bid (SKEW ≥140), the market is selling near-dated variance cheaply *while paying up for the far tail.* Those two facts are inconsistent, and the measured resolution is asymmetric: **the tail fires ~1.6× more often than base rate; the body does not.**

**This is explicitly NOT the VIXCS class** (commission §1). VIXCS was an **event box** — a dated catalyst, a short tenor, a directional call on one FOMC. This is a **regime-conditional convexity purchase** with no dependence on any single event resolving a particular way.

**Transmission path:** agnostic by construction. It does not require Path A (credit-led) or Path B (concentration-unwind). The L1 population framework is the only mechanism-surprise-robust layer I own (KB-VIO-070: *a novel mechanism bypasses discriminators, never base rates*), and this design sizes off the base rate, not off a mechanism story.

---

# 2. 🔴 THE CENTRAL DESIGN PROBLEM, QUANTIFIED — and it is where VIXCS died

**The horizon at which the signal works is the tenor at which the vehicle transmits worst.**

I measured forward beta to spot directly off `VX_TERM_HISTORY.tsv` (28,583 contract-days) against CBOE VIX closes:

| DTE bucket | n | β(forward ~ spot) | R² |
|---|---:|---:|---:|
| ≤10 | 1,040 | **0.643** | 0.730 |
| 11–20 | 1,014 | **0.664** | 0.869 |
| 21–35 | 1,615 | **0.500** | 0.805 |
| 36–60 | 2,487 | **0.431** | 0.777 |
| 61–90 | 3,240 | **0.320** | 0.706 |

**β falls monotonically with tenor. The signal's edge rises monotonically with horizon.** They point in opposite directions, and that scissor is the whole problem:

- Buy short-dated → high β (0.64) but you are betting on the **21td/≥+50% branch = 25% conditional.** **That is exactly what VIXCS was**: ~9 DTE, highest β, shortest window, least likely branch. It was a bet on the fastest and rarest path, and it lost while the forecast was right.
- Buy long-dated → the **60td/≥+50% branch = 56.7%**, but the forward moves only **0.32×** spot.

**⇒ The structure must supply the convexity the forward does not.** At 30–60 DTE a +50% spot move delivers only ~+16–22% on the forward — so an **ATM** structure at that tenor is close to dead money even when the thesis is right. **OTM convexity is not a preference here; it is the only way the measured edge reaches P/L.**

⚠️ **DISCREPANCY DISCLOSED, NOT RESOLVED:** my VIXCS post-mortem registered β as **0.274 (21–35) / 0.505 (11–20) / 0.591 (≤10)** from an option-implied construction, n=246. The table above is **VX futures settle-to-settle**, n=1,040–3,240, R²=0.71–0.87. **The SHAPE agrees (β falls with tenor); the LEVEL disagrees materially at 21–35 (0.500 vs 0.274).** Different instruments and samples. **I am not overwriting the registered figure by preference** — reconciliation is a pre-deployment owed item (§7). **Either number sustains the design's direction; neither should be quoted as "the" beta.**

---

# 3. TRIGGER SPEC — the entry gate

**ARM (all four, and the connective count is deliberate — see §4):**

| Leg | Condition | Instrument | Basis |
|---|---|---|---|
| **A1** | VVIX ≤ 90 | CBOE `^VVIX` | SETTLE |
| **A2** | VIX ≤ 16 | CBOE `^VIX` | SETTLE |
| **A3** | SKEW ≥ 140 (daily close, **not** the 20d-avg) | CBOE `^SKEW` | SETTLE, published ~17:00 ET |
| **A4** | nearest HIGH/MED catalyst ≤ 21d | `workbook/CATALYSTS.tsv` | dated feed |

**PLUS a sequencing requirement (A5), which is the one genuinely new leg:** **A1–A4 must hold on 2 consecutive SETTLE closes.**

⚠️ **A5 exists because of a live failure this week, not on principle.** COR1M's first-tell (KB-VIO-188) restricted itself to settles and 2 consecutive sessions, and on **8/18 a TICK printed 8.47 (through the line) and the 8/19 SETTLE came back 7.95 (below).** A single-session read would have published a fire that did not happen. **A basis clause is not boilerplate; it is the part that stopped a false positive eight days after it was written.**

**⛔ EXPLICITLY NOT ENTRY LEGS, and each exclusion is reasoned:**
- **Term-structure inversion (VIX3M/VIX < 1.0)** — my own falsification says inversion is a **PEAK MARKER**, not an onset signal: 553 events, **2.2%** hit rate for +50% follow-through, mean **−5%** forward (KB-VIO-034). **Using it as an entry leg would invert my own best-established finding.**
- **VIX9D/VIX ratio** — currently the most striking thing on my surface (0.7446 → **0.8988** in four sessions) and it has **no registered threshold and no base rate.** Per `finding_base_rate_the_threshold_before_building_it`, **it does not go in a spec until it is base-rated**, however good it looks. Flagged as owed (§7), deliberately excluded here.
- **COR1M first-tell** — a live registered gate, currently **session 1 of 2**. Not folded in: it would make the trigger partly dependent on a series that **cannot be graded on a session I do not boot** (recoverable only to T-1, KB-VIO-202). **A leg whose observability depends on my schedule is not a leg.**

---

# 4. ⚙️ RATCHET AUDIT — connectives counted IN vs OUT (DAEDALUS packet applied, as commissioned)

DAEDALUS's finding on my existing `TRADE.md:112–117` machine: **arms on any-1-of-3, stands down only on all-3-of-3 ⇒ `P(arm) ≫ P(stand-down)` by construction, a one-way ratchet into escalated.** Its central warning is that **a stand-down that cannot fire is invisible** — staying armed reads as vigilance, not as a defect. Applied here:

| | Connective | Count |
|---|---|---|
| **ARM** | A1 **AND** A2 **AND** A3 **AND** A4, ×2 consecutive settles | **conjunctive, 4-of-4** |
| **STAND-DOWN** | S1 **OR** S2 **OR** S3 | **disjunctive, 1-of-3** |

**S1** VVIX ≥ 105 (the convexity got expensive — the reason to own it is gone) · **S2** VIX ≥ 22 (the move happened; this is now a *different* trade and must be re-underwritten, not held) · **S3** 45 calendar days elapsed with no harvest trigger (time-box).

**⇒ Entry is the INTERSECTION of four conditions; exit is the UNION of three. `P(stand-down) ≫ P(arm)` — the ratchet runs the safe direction by construction.** This is the deliberate inversion of the machine DAEDALUS flagged, and I am writing the rationale **on the line** as it asked: **arming spends money and disarming saves it, so arming carries the heavier evidential burden.**

**Plus the cheap third option DAEDALUS offered, adopted:** a **sessions-armed-and-unopened counter** on the stand-down, logged every boot. It converts a silent failure into a visible one for the cost of one column. *(BRENT's gate was shut 11-of-11 post-arm sessions live; three years of backtest confirmed what one counter would have shown in two weeks.)*

---

# 5. SHAPE — structure class only, no strikes, no expiry (commission §3)

| Element | Specification | Why |
|---|---|---|
| **Class** | Defined-risk **OTM call spread on VIX** (debit) | Convexity must come from the structure — the forward supplies only 0.32–0.43× at the required tenor (§2) |
| **Tenor band** | **30–60 DTE at entry** | The signal's edge lives at 30–60td (34.4% / 56.7% at ≥+50%). ⚠️ **NOT ≤10 DTE — that is the VIXCS error**: max β, min probability |
| **Moneyness** | Lower strike **above** spot; the trade must not need spot to merely hold | The measured edge is entirely in the ≥+50% tail; an ATM structure monetises the ≥+15% body where lift is 1.17× |
| **Sizing** | Defined-risk debit, **100% loss is the base case** | The 60td/≥+50% branch is 56.7% — i.e. **it fails ~43% of the time even when the signal is right** |
| **Strikes / exact expiry** | ⛔ **TERRY at fire-time, live marks** | Commission §3. Frozen strikes rot; this document is the durable half |

**🔴 HARVEST RULE — MANDATORY BY CONSTRUCTION, and this is the single most important line in the document.**

> **Harvest 50% of the position when the position's mark reaches 2× its debit, regardless of where spot, SKEW, VVIX or the calendar sit. The remainder runs to the stand-down or the time-box.**

⚠️ **This exists because its absence is what actually cost me money.** VIXCS's post-mortem finding #2, verbatim: *"the real management gap was NO HARVEST RULE, not the structure: every trigger required the move to go FURTHER (spot ≥23, ratio <1.0, SKEW crash) and none fired on the position simply being worth more than it cost. It went through its strike at the 7/29 close and round-tripped unharvested."* **A profit-keyed rule must exist by construction** (fleet NO_HARVEST requirement, commission §1). **It is keyed to the position's own P/L and to nothing else — that is the entire point.**

---

# 6. 🔴 PRE-REGISTERED FALSIFIERS — what would make the THESIS wrong, not merely when to exit

The commission asked for this explicitly, and it is a different question from the stand-down. **Frozen 2026-08-20, before the next fire.**

**F1 — THE PRIMARY THESIS-KILLER.** Over the **next 6 fires** of the A1–A4 gate, if the forward-60td ≥+50% rate comes in **at or below the unconditional rate (36.0%)**, the edge is not real and **this registration is retired, not re-tuned.** ⚠️ *Stated as a rate against a fixed comparator, not as "it stopped working."*

**F2 — REGIME-CONFINEMENT.** If the 33 historical episodes prove concentrated in a regime that no longer exists (pre-2018 vol structure, pre-GEX-suppression), the base rate is an artifact of a dead market. **Test owed BEFORE first deployment** (§7) — split the episodes pre/post-2018 and re-run. **If the post-2018 subsample loses separation, the design does not deploy.**

**F3 — THE CONVEXITY IS ALREADY PAID FOR.** If at fire-time VIX call skew is rich enough that the OTM spread costs more than ~⅓ of its max width, the dislocation is priced and there is nothing to buy. **A cheap-tail window with expensive tails is a contradiction and the correct action is to stand down, not to pay up.**

**F4 — SMALL-SAMPLE COLLAPSE.** n=30–33 episodes. My own registered lesson: *ρ −0.559 at n=14 died to −0.255 at n=26 — extend the sample before publishing a coefficient.* **If extending the window (intraday, or a 3rd data source) drops the 60td/≥+50% lift below 1.25×, treat the edge as unproven.**

**F5 — THE STATED LIMITATION IS NOT A DISCOUNT ALREADY APPLIED.** v3.9's own lesson, on me: I published 2.25× in good faith with a thin-sample caveat on its face; on a full sample it was 1.20× and not significant. **Flagging a small sample does not shrink the estimate.** The 1.57× lift above **must be re-derived on any extended sample before it sizes anything.**

---

# 7. HONEST LIMITS — the against-case is real

1. **⚠️ THE AGAINST-CASE ON TODAY'S TAPE, WHICH RUNS AGAINST MY OWN READ:** VVIX **fell** (93.92→89.86) while VIX rose, and MOVE **retreated** below F1 (75.63→71.26). **Every confirming channel is absent.** Every Path-B analog I hold eventually has vol-of-vol confirming. **Either this move is not what I think it is, or VVIX is late — and I am not resolving that by picking the branch I prefer.**
2. **My own fade base rate is against me.** Vol events retrace far more often than they run; my March-2026 analog fired and fully retraced (31→18 in 3wk) when credit did not confirm. **This design's 43% failure rate at its own best branch is not a rounding error.**
3. **Transmission has been dead repeatedly.** The "loaded and not transmitting" configuration has now failed to transmit on multiple occasions; the JPY channel has fully **unloaded** (RV now below IV for the first time). **This design does not require transmission — but it also does not get to claim it as support.**
4. **n=30 episodes and one enormous regime shift inside the sample.** F2 exists precisely because I have not yet run it.
5. **The catalyst leg (A4) is not backtestable.** The 3-leg base rate above is therefore an **upper bound on fire frequency** for the 4-leg gate. Selectivity improves; the measured edge does not automatically survive.
6. **β discrepancy unreconciled** (§2). Owed before deployment.
7. **VIX9D/VIX is deliberately excluded and it is the strongest thing on my surface.** That is a cost I am accepting on purpose rather than smuggling an unbase-rated leg into a spec.

**⇒ OWED BEFORE FIRST DEPLOYMENT (not before this design closes):** F2's pre/post-2018 split · the β reconciliation · a VIX9D/VIX base rate if it is ever to be a leg.

---

# 8. STATE AT WRITING

**The gate is NOT armed.** Live 8/20 SETTLE: **A1 VVIX 89.86 ✅ · A2 VIX 16.01 ✗ (fails by 0.01) · A3 SKEW 143.23 ✅ · A4 NVDA 6d ✅** ⇒ **3-of-4, ARMING**, and A5's 2-consecutive-settle requirement is not started.

⚠️ **A2 missing by one hundredth of a point is not meaningfully different from met — and it does not fire, because the letter is the letter.** Writing this down at the moment it is inconvenient is the whole discipline; a threshold I round in my favour at 16.01 is not a threshold. **If it arms tomorrow, it arms on tomorrow's data, not on tonight's rounding.**

---

**— VIOLET**, 2026-08-20. Commission (7/31 Option 1) **CLOSED**. Design ≠ deployment; **three gates remain, none pre-committed.**
*Reproduce §0 and §2 from CBOE `*_History.csv` + `workbook/VX_TERM_HISTORY.tsv`; method and seed stated inline.*
