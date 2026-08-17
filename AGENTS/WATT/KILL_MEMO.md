# WATT — KILL_MEMO (pre-written cascade ladder)

**Created 2026-08-17.** *Mandated by `CLAUDE.md` §THRESHOLDS — *"KILL_MEMO for any cascade trigger (pre-written ladder, decoupled from STATUS rewrites)"* — and absent since this seat was built (DAEDALUS §3 invalidation inventory, 8/7: **"KILL_MEMO absent"**).*

**Why it exists, in one line:** *when the thing fires, I will be composing under time pressure and with the tape in front of me — which is exactly when a threshold gets renegotiated.* This file is written **cold**, on a quiet day, so that the ladder is a **lookup** rather than a judgment.

> ⚠️ **THIS FILE IS DECOUPLED FROM STATUS ON PURPOSE.** It must **not** be rewritten as part of a normal closeout. Change it only by a **deliberate, dated amendment** with a reason — and never while a trigger is live. **If you find yourself editing this file during an event, stop: that is the failure it was written to prevent.**
>
> **Amendment log:** *(none yet — created 8/17)*

---

## 0. What this file is NOT

- **Not a trade proposal.** WATT produces signal; **TERRY** constructs, **Will** approves (root rules #5–#8). Nothing here authorizes a position.
- **Not a replacement for the exit triad** in `STATUS.md`. The triad says *whether* a rule fired. This says *what to do in the next 60 minutes* when one does.
- **Not a forecast.** No probabilities here. Only conditionals.

---

## 1. The cascade triggers (conjunctions — a single metric knee-jerks; that is the whole point)

| # | Trigger (ALL limbs required) | Why a conjunction |
|---|---|---|
| **C1** | **EEA2+ posting live** **AND** RT LMP ≥$1,000 sustained 2+ consecutive 5-min intervals | Either alone is common enough to be noise. EEA-1 happened twice in July with no RED price; **$1,217.52 printed 8/16 with no posting at all.** The pair has never co-occurred in this seat's record |
| **C2** | **DOE §202(c) emergency order** naming PJM **AND** a named large-load / data-center curtailment | §202(c) orders issue for many reasons; the *curtailment of a data center* is the specific event the whole P1→P3 coupling predicts |
| **C3** | Demand **≥97% of trailing 24h peak** **AND** an emergency-class posting **AND** the 24h peak itself **≥158,000 MW** | The third limb stops a 97% reading on a *low* peak (an August Sunday) from masquerading as a July-grade event. **This limb was added because of 8/16** |
| **C4** | **Spark spread NEGATIVE on ONE consistent basis, sustained 3+ sessions** | Gas-fired uneconomic = supply withdrawal. ⚠️ **One basis.** A level change between the ICE OTC proxy and DM2 RT on-peak is a **basis change, not a market move** (L-17) |
| **C5** | **29/30 BRA clears materially BELOW cap** **AND** interconnection queues draining | The registered **thesis-kill**. Both limbs required — a below-cap clear with queues still full is a *supply response*, not a demand collapse |

---

## 2. THE LADDER — what to do, in order, when C1/C2/C3 fires

**Do these in sequence. Do not skip to step 4 because the tape looks urgent.**

### Step 1 — VERIFY, before telling anyone (target: 10 min)
1. **Pull the PJM emergency-procedures board directly.** Record the **message ID**, the **exact posting type**, the **region** (PJM-RTO vs a local zone — a DOM/FE-AP local warning is **not** an RTO event), and the **effective window**.
2. **Pull DM2 5-min for the day.** Record max, the stamp, and **how many consecutive intervals** cleared the bar.
3. **Pull EIA-930 demand** and compute % of trailing 24h peak **and the absolute level of that peak**.
4. **Check the DOE §202(c) index** for an order naming PJM.

> ⚠️ **Two traps, both of which have already caught someone in this seat's record:**
> - **A relayed 🔴 flag from another agent is a LEAD, not an event.** On 7/22 AEOLUS routed a 🔴 alleging a §202(c) order and a record peak; four primaries refuted it and AEOLUS retracted unconditionally. **Verify at the primary before it enters my record — including when the sender is confident.**
> - **The 5-min tape is UNVERIFIED.** The verified hourly (`rt_hrl_lmps`) **lags ~4 days** (measured 8/17, KB-WATT-081) — so during a live event **the settlement-grade number will not exist.** Say "unverified 5-min" every time. Do **not** wait for verified data to act, and do **not** later present the 5-min figure as settled.

### Step 2 — CLASSIFY (target: 5 min). Answer these three, in writing, before routing:
- **Is it RTO-wide or local?** *(Local ≠ P1.)*
- **Is it demand-driven or supply-driven?** Demand-driven = high load. Supply-driven = outage/ramp at ordinary load. **8/16 was the second, and the two have opposite implications for P3.**
- **Is the price event coincident with the posting, or decoupled?** Decoupled → this may be **FL-WATT-10 (minimum-commitment fragility)**, which is a *different mechanism* and must not be logged as a heat-episode.

### Step 3 — ROUTE (target: 20 min). Written packets, not just a brief row:
| To | What they need |
|---|---|
| **HENRY** | 🔴 The curtailment-risk read for HEN-36. Say plainly whether the **power-cost FCF input** changed (a spike that retraces has **not** changed it) |
| **AEOLUS** | Whether this confirms or refutes a live C3 weather call — **reconcile to one figure** |
| **VULCAN** | Only if a **named** data-center load was curtailed or a cost lands on operators |
| **CARL** | Only if it reaches **retail**. A wholesale spike alone does not |
| **PROME** | Always, on C1/C2. Include the classification from Step 2, not just the number |

### Step 4 — SCORE, and be willing to not move
- Update the **exit triad** with the fired limb and a **literal fired-count**.
- **Move P1's score only if the STATE changed**, not because an event occurred. **A retraced spike is not an elevated state.**
- ⚠️ **The scoring trap, stated in advance so it is harder to fall into:** the pull during an event is to score the *excitement*. On 7/16 an EEA-1 fired and the correct answer was **🟠 holds, not 🔴** — because a 1,500-hour pull showed the episode was **milder** than 7/1–7/3 on all three axes and already rolling over. **Compare the live event to the season's own worst before scoring it.**

### Step 5 — WRITE IT DOWN THE SAME SESSION
KB row · VX state · FLOW pathway if the mechanism is new · **and a prediction with a resolution date** if the event implies a recurrence claim. **An event that produces no falsifiable claim produced no signal.**

---

## 3. Standing prohibitions during a live event

1. **Never relax a limb to make a trigger fire.** If it half-fires, it did not fire. Record **FIRED-ON-LETTER / MECHANISM-REFUTED** if the letter is met but the mechanism is absent (the 8/16 precedent, L-29) — **and do not retro-read the rule.**
2. **Never bank an unpassed forecast.** An EEA-1 is **not** an EEA2+. WATT-02's bar is EEA2+; a near-miss stays OPEN.
3. **Never cite a price from a STATUS file.** Pull live (root rule #4).
4. **Never let a price event satisfy a POSTING bar,** or vice versa. WATT-06's bar was a *posting*; the 8/16 price spike could not count toward it.
5. **Never edit this file during the event.**
6. **Do not spend more than ~4 PJM API calls in the first hour.** Non-member = **6 calls/min**; looping the instrument under pressure is how the key gets throttled at the exact moment it matters.

---

## 4. If C5 fires (the thesis-kill) — a different, slower ladder

C5 is **not** an emergency; it resolves on an auction date known ~a year ahead. **Do not run the fast ladder.**
1. Verify both limbs at PJM primaries. **A below-cap clear alone is NOT C5.**
2. Write a **falsification memo**, not a STATUS edit: what died, what survives, and **which channel the weight migrates to** — the same channel-kill-vs-thesis-kill discipline that governed P1's summer death.
3. Route to **PROME, HENRY, VULCAN, CARL** together — this reverses the direction of a signal all four consume.
4. **Expect to be wrong about the magnitude, not the direction.** P2 has been the highest-conviction leg since this seat opened; a genuine reversal deserves a slower, better-sourced write-up than a firing does.
