# ORCL Fallen-Angel Trigger Map — GATE-LIQ-069 leg-5 sharpener

> ⚠️ **CHECKED 2026-08-24 (PAT-060 queue, 36d stale) — NO CHANGE. GATE-LIQ-069 stays ARMED 1-of-2.**
>
> **R1 (the 2nd-agency leg) has NOT fired: Moody's still rates ORCL `Baa2`, outlook NEGATIVE — affirmed, not cut.** S&P remains **BBB−** (the 7/9 cut, R0, already logged); Fitch **BBB**. **Middle rating stays BBB = solidly IG**, and a fallen angel needs **2 of 3 agencies at HY** under the index middle/average rule. **No forced-sell event is live.**
>
> 🔴 **GRADE THIS CHECK AS SECONDARY-SOURCE, NOT PRIMARY.** It is a web/mirror sweep, not an agency-primary pull, and one returned item was misdated to 2025. **This map's own discipline (KB-LIQ-082) pins agency states to primaries — so this annotation is sufficient to say *nothing appears to have fired* and is NOT sufficient to move the gate in either direction.** A primary re-verification is owed before any GATE-069 action.
> **Absence-is-data record:** 36 days elapsed, R1 did not fire, the pipeline TELL from 7/9 stands unchanged.

**Built:** 2026-07-18 (Sat-eve, PROME wave, Will-approved Rank-2) · **Owner:** LIQUID (AI-credit spread-tells; VULCAN owns capex/fundamentals mechanism — seam 7/12) · **KB:** KB-LIQ-082 · **Feeds:** GATE-LIQ-069 (AI-HY cohort re-arm), NEXUS M-08/M-09, VULCAN S1/S5, VIOLET Path-B.

**Why this file:** GATE-LIQ-069 is ARMED 1-of-2 off the single S&P cut to BBB− [7/9]. But the leg-5 wording ("ORCL cut to Baa3/BBB−, either agency") conflates two very different events: the **fallen-angel PIPELINE tell** (a single agency reaching the IG floor — already fired) versus the **actual index-ejection FORCED-SELL event** (which the major indices' middle/average rating rules make impossible on one agency). This map pins the live cross-agency state to primaries and specifies the *precise* escalation that should count as a fresh/second leg — so the next ORCL rating action is graded instantly, not scrambled.

---

## 1. Live cross-agency rating state [as-of 2026-07-18, agency primaries]

| Agency | LT rating | IG-scale notch | Outlook | Notches to HY | Last action |
|--------|-----------|----------------|---------|---------------|-------------|
| **S&P** | **BBB−** | IG floor (lowest IG) | **Stable** | **1** (→ BB+) | **CUT BBB→BBB− 7/9/2026** (AI-capex FCF deficit, OpenAI concentration; leverage >4x projected FY27-28) |
| **Moody's** | **Baa2** | 2 above floor (=BBB) | **Negative** | **2** (→ Ba1) | affirmed Baa2 + **negative outlook** on latest sr-unsecured notes assignment |
| **Fitch** | **BBB** (F2 ST) | 1 above floor | **Stable** | **2** (→ BB+) | **affirmed BBB/Stable** amid the debt plans |

**Composite read:** S&P is at the edge (1 notch, but STABLE); Moody's is 2 notches out but carries the only **NEGATIVE** outlook = the most-likely next mover; Fitch is 2 out and stable. **Middle rating = BBB** (Moody's Baa2 = BBB, Fitch BBB, S&P BBB−) — solidly IG for index purposes.

## 2. Index-migration mechanics — why one agency ≠ ejection

Major IG indices assign an issue's index rating by **combining the three agencies, not taking the lowest**:

| Index family | Rule | ORCL current index rating | To eject to HY |
|--------------|------|---------------------------|----------------|
| **Bloomberg US Corporate / Agg** | **MIDDLE** of Moody's/S&P/Fitch (if 3 rate); lower of two; the one if one | **BBB** (middle) | middle must fall to BB+/Ba1 → needs **2 agencies at HY** |
| **ICE BofA US IG (C0A0)** | **AVERAGE** of Moody's/S&P/Fitch, rounded | ~**BBB** | average below BBB− → needs **~2 agencies at HY** |

**Consequence (load-bearing):** ORCL is a fallen angel — ejected from IG indices into HY indices at month-end rebalancing — **only when TWO of the three agencies rate it HY (BB+/Ba1 or below).** The 7/9 S&P cut did NOT start the forced-sell clock; it moved S&P to the floor with a stable outlook. **A single-agency cut is the pipeline tell, not the event.** *(Caveat: exact eligibility/rebalance rules vary by index provider and mandate; a benchmark can also use its own composite. The middle/average convention holds for the two dominant families above — treat as the base case, verify the specific benchmark if a name-level forced-sell tally is needed.)*

## 3. Forced-sell sizing — the "largest fallen angel ever" claim

| Item | Figure | Source / note |
|------|--------|---------------|
| ORCL total debt | **~$160B and rising** | S&P 7/9 (leverage >4x FY27-28; +$20B equity planned CY26, tens of $B debt over 3yr) |
| Prior KB basis figure | ~$133B | STATUS/KB-066 — the IG-index-eligible bond face is a SUBSET of total debt |
| **Forced-sell universe** | **~$130-160B index-eligible bonds** (precise face = bond-by-bond tally, follow-up) | order-of-magnitude only tonight |
| Prior record fallen angels | Ford ~$36B (Mar-2020), Kraft Heinz ~$22B (Feb-2019) | Oracle at $130B+ ≈ **~4x the prior record** |

**Why the size matters:** HY index market cap is ~$1.3T; a $130B+ fallen angel is ~10% of the index dumped onto HY holders in a single rebalance — a mechanical spread-widening / forced-buyer-absent event (the KB-066 BB-floor stress) independent of any change in Oracle's fundamentals. This is the concrete forced-selling tail the spread tape (IG OAS 79 [7/15], benign) has NOT priced.

## 4. Precise GATE-LIQ-069 escalation ladder (sharpens leg-5)

| Rung | Event | State | What it means | Action |
|------|-------|-------|---------------|--------|
| **R0 — pipeline tell** | 1st agency to IG floor (S&P BBB−) | **FIRED 7/9** | fallen-angel pipeline live; 1-of-2 on GATE-069 | logged; NEXUS flagged |
| **R1 — pipeline deepens** | Moody's Baa2→**Baa3** (neg outlook = live path) OR Fitch BBB→BBB− OR S&P negative-outlook re-assignment | not fired | 2 agencies at floor = one cut from a 2-agency-HY ejection; forced-sell clock arms | **counts as a fresh GATE-069 leg → 2-of-2 → re-run AI-HY discriminator + flag NEXUS/VULCAN/VIOLET** |
| **R2 — ejection clock starts** | ANY 1st agency to HY (S&P BB+, Moody's Ba1, Fitch BB+) | not fired | with middle/avg rules, still IG-in-index but one agency HY | 🟠 escalate; size the eligible face precisely |
| **R3 — FALLEN ANGEL** | **2nd agency to HY** → middle/avg below IG | not fired | month-end index ejection → forced sell ~$130B+ | 🔴 the KB-066 BB-floor event; route ALL (VULCAN/VIOLET/NEXUS/HENRY) |

**Fastest path:** Moody's (negative outlook, 2 notches) is likelier to move next than S&P re-cutting from a stable BBB−. The realistic near-term escalation to watch = **Moody's Baa2→Baa3** (R1) — that is the single most informative next print, and it is the event that should trip GATE-069's second leg.

## 5. Route-out — proposed GATE-LIQ-069 wording refinement (PROME maintains GATES.tsv)

The current leg-5 reads: *"ORCL cut to Baa3/BBB- (either agency; shorthand fixed 7/17 per owner)."* Proposed sharpening (distinguishes the fired pipeline-tell from the second-leg escalation), suggested replacement for the leg-5 clause:

> `ORCL fallen-angel ladder (KB-LIQ-082): R0 pipeline-tell = 1st agency at IG floor [S&P BBB- 7/9 = FIRED]; the leg that counts as a SECOND GATE-069 leg (→2-of-2, discriminator re-run) = R1 = a 2nd agency to the IG floor (Moody's Baa2→Baa3 [neg outlook, likeliest] / Fitch BBB→BBB-) OR any agency to HY. Index ejection (forced-sell ~$130B+) needs 2 agencies at HY (middle/avg rule), NOT one.`

No state-flip to the gate itself (stays ARMED 1-of-2); this is a wording precision + adds the KB-082 pointer.

---

## Cross-agent + reconcile notes

- **VULCAN seam:** VULCAN owns the capex/FCF-deficit *mechanism* driving the downgrades; LIQUID owns the *spread/index* consequence (this map). Reconcile the leverage/FCF figures to VULCAN's numbers — do not fork.
- **BB-floor discriminator (KB-066):** an actual R3 ejection is the mechanical trigger for the BB>220-while-CCC-flat signature (the ~$130B forced into HY concentrates in the BB bucket). This map is the "how big / when" behind that trigger.
- **Next graded input:** any of the three agencies' next ORCL action; Moody's negative outlook = the live clock. No calendar — event-driven.
