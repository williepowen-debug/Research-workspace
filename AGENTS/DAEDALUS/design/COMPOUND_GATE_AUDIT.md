# COMPOUND-GATE JOINT-SATISFIABILITY — AUDIT DESIGN + FIRST SCREEN

**Author:** DAEDALUS · **Date:** 2026-07-30 · **Origin:** PROME packet `inbox/2026-07-30_from-PROME_sweep-candidate-compound-gate-joint-satisfiability-audit.md`, off BRENT's `setups/2026-07-30_LESSONS21a-cooldown-gate-respec-PROPOSAL.md` (Will-approved Option A same day)
**Status:** design ruled + screen run. **Semantic screen = mine and DONE. Joint base-rating = owners' (domain data).** No cross-agent file touched.

---

## 1. THE DEFECT, STATED PRECISELY

PROME's packet framed it as *"base-rate the legs jointly."* That is necessary and not sufficient — it under-describes what BRENT found, and the missing half is where the fleet's remaining exposure lives.

BRENT's gate `{OVX <44.2 AND ratio <2.89}` was:

| Measure | Value | Reads as |
|---|---|---|
| Marginal base rate, each leg | healthy | ✅ |
| **Joint**, unconditional, 1y | **50.4%** of sessions (127/252) | ✅ **still healthy** |
| Joint, unconditional, 3y | 74.5% | ✅ |
| **Joint, CONDITIONAL on the arm's trigger state** (Brent +15%/20d) | **0 of 38 days = 0.0%** | 🔴 |

**An unconditional joint base rate would have passed this gate.** 50.4% is not a number that prompts anyone to look further. The defect is only visible **conditional on the state in which the gate is asked to open** — and the cause is stated in one line by BRENT: `corr(OVX, 20-day crude move) = +0.483`. *The same event that arms the trade is the event that shuts the gate.*

⇒ **The test is not "is the conjunction satisfiable." It is "is the conjunction satisfiable IN THE TRIGGER STATE."** A gate is a conditional object; base-rating it unconditionally answers a question nobody asked.

### 1b. Three distinct defects, not one

| # | Defect | Test | Detectable without data? |
|---|---|---|---|
| **D1** | **Trigger-conditional unsatisfiability** — legs anti-correlated with the arming state | `P(all legs open \| trigger fired)` over the trigger's own history | Partly — see §2 |
| **D2** | **Joint improbability** — legs near-independent, each rare, conjunction required in one window | product of marginals × window | Yes, by arithmetic |
| **D3** | **Non-discriminating veto** — a leg that fires identically in the true and false worlds | `P(leg \| thesis true)` vs `P(leg \| thesis false)`; equal ⇒ decoration | Yes, by reading |
| **D4** | **Asymmetric arm/disarm** — disjunctive entry, conjunctive exit ⇒ a ratchet | **count the connectives in vs out**; `P(enter) ≫ P(exit)` for any legs | **Yes — pure arithmetic, no domain knowledge** |

D1 is BRENT's cooldown gate. D2 is BRENT's own 7/29 diesel falsifier (`distillate ≥+2.0M AND crack −>$5, same week` ⇒ **0.6%** joint). D3 is BRENT's Stage-A tanker veto (flagged OPEN to Will). **All three came out of one agent in one session, which is why this is a class and not an incident.** **D4 is mine, found in this screen** (VIOLET) — see §4b; it is the cheapest of the four and the only one invisible to leg-level base-rating, because the defect lives in the *relationship between two gates*, not inside either.

---

## 2. THE CHEAP SCREEN — semantic anti-correlation, no backtest required

BRENT's §3 contains the generalization, and it is worth more than the backtest that produced it:

> *"Any metric measuring 'the move hasn't happened yet' is 0% on days the move is happening."*

This makes D1 **readable**. You do not need the data to flag a candidate; you need the two semantic contents side by side:

**SCREEN:** write the trigger's semantic in one clause and each leg's semantic in one clause. **If any leg's clause is the negation, the precondition, or the calm-state form of the trigger's clause, the gate is a D1 candidate** and must be base-rated conditionally before it is trusted.

Worked: trigger = *"escalation is happening."* Leg = *"vol is low"* = *"escalation is not happening."* Flagged in one line, months before anyone ran 753 sessions.

**This screen is a structural read, so it is mine.** The conditional base rate needs each agent's own series and regime definition, so it is **theirs** — the same detection/disposition split the Falsification Sweep already runs on.

---

## 3. ⚠️ THE DIRECTION NOBODY LOOKED AT — kill-side gates fail SILENTLY

BRENT found the defect in a **deploy** gate. A broken deploy gate is loud in a specific way: capital sits, the operator eventually asks why nothing fired, and BRENT did exactly that (wrongly diagnosed at first, then tested).

**The same defect in a KILL, STAND-DOWN, or RETIRE gate produces no such question.** A kill that cannot fire looks *identical* to a thesis that is still true. Nobody files a complaint about an alert that never stands down; it reads as ongoing vigilance. **A conjunctive kill gate is the same bug with the observability removed** — and it is strictly worse, because the failure mode is *carrying a dead thesis as live*, which is the failure this fleet exists to avoid.

Severity ordering for the audit:

| Gate direction | Failure | Observability |
|---|---|---|
| Deploy / entry | capital never deploys | **loud** — operator notices the non-event |
| Exit / harvest | position never harvests | medium — P/L eventually says it |
| **Kill / stand-down / retire** | **dead thesis stays live; alert never clears** | 🔴 **silent — indistinguishable from "still true"** |

This is the extension beyond BRENT's finding, and it re-ranks the screen below.

---

## 4. FIRST SCREEN — run 2026-07-30, semantic only

Scope: BRENT's named set (RED, TERRY, FALCON, OSPREY, VIOLET) + BRENT. Method: grep for numeric AND-joined conditions in gate/kill/trigger/deploy/veto context, excluding inbox/archive/lessons; then read each candidate's semantics against §2. **This is a screen, not a verdict — every row below needs its owner's conditional base rate.**

| # | Owner | Gate | Legs | Class | Dir | Screen verdict |
|---|---|---|---|---|---|---|
| 1 | BRENT | cooldown deploy gate | OVX <44.2 **AND** ratio <2.89 | D1 | deploy | ✅ **CONFIRMED + FIXED** 7/30 (sequenced, Will-approved) |
| 2 | BRENT | diesel falsifier | distillate ≥+2.0M **AND** crack −>$5, same wk | D2 | falsifier | ✅ **CONFIRMED by owner** (0.6% joint) — self-found |
| 3 | BRENT | Stage-A tanker veto | — | D3 | veto | ⚠️ **OPEN to Will** — owner-flagged non-discriminating |
| 4 | **VIOLET** | `TRADE.md:112` **arm** vs `:117` **STAND-DOWN** | arms on **ANY ONE** of 3 gates · stands down only on **ALL THREE** benign | **D4 (new)** | 🔴 **stand-down** | 🔴 **STRONGEST — and it is not a correlation finding at all.** The arm is **disjunctive (1-of-3)** and the disarm is **conjunctive (3-of-3)**. `P(arm) ≫ P(disarm)` **by construction, for any legs whatsoever, correlated or not** — a one-way ratchet into the escalated state. No base rate is needed to see it; it is arithmetic. Add that the three benign legs must hold *simultaneously* in a state entered under stress and it is D1 as well. **§3's silent class exactly:** VIOLET stays escalated and nothing complains. |
| 5 | **OSPREY** | `CLAUDE.md:153` full-theater retirement | ceasefire **in force** **AND** 3 channels quiet **60+d** **AND** terminals at pre-war status | D2 | 🔴 retire | 🟡 **REAL BUT BOUNDED — downgraded on a full read.** ~5 effective legs incl. a 60d joint quiet across three channels whose own kills are 30/30/21d. **But it is not exit-less:** `:154` (settlement / 60d zero deep-strike) and `:155` (model-falsification) are genuine independent routes. Ask is narrow — has any 60d window ever satisfied the *sub*-conjunction — not "this thesis can't die." |
| 6 | **OSPREY** | `CLAUDE.md:147/148` Channel-1 / Channel-2 kills | no strike-class row **30+d** **AND** aggregate-recovery threshold | — | kill | 🟢 **CLEARED on a full read — my grep-level call was wrong.** `:145` states the rationale: *"a strike-pause alone is see-saw noise… a recovery alone just means repair outpaced a still-live campaign."* The legs are **input (strikes) and output (capacity), positively correlated with a lag** — not the same measure twice. Deliberate, reasoned, satisfiable. **No ask.** |
| 7 | **TERRY** | `PAPER_BOOK_DESIGN.md:34` scoring gate | N ≥10 closed/lane **AND** ≥5 distinct antecedents/lane | — | scoring | 🟢 **DESIGN CORRECT — downgraded; the ask changes shape.** §5b/:35 does not merely imply the anti-correlation, it **states it and accepts it deliberately**: *"this desk fires rarely and concentrates… row-count is the easy number to reach and the misleading one."* Opening on a one-trade book is the worse error, so the binding leg is binding **on purpose.** 🟡 **Residual is instrumentation, not specification:** the gate has no expiry, no counter and no escalation — if `≥5 antecedents` is never reached, the book reads *"still gathering data"* forever. That is §5b's counter, not a re-spec. |
| 8 | RED | `SCRATCH.md:44` CARL rationalization test | HHDC benign-or-better **AND** V2 not 4→3, ~8/15 | D2 | scored test | 🟢 low — dated single-shot, both legs plausible in the same state, no anti-correlation with the test's own premise. |
| 9 | FALCON | FAL-03 | — | — | falsifier | ➖ **out of scope** — its failure was **scope mismatch** (instrument couldn't see LNG), not joint satisfiability. Owner-banked; see the separate FALCON packet + PAT-072's sibling. |

**Screen yield: 2 live asks (rows 4, 5) + 1 instrumentation note (row 7), both asks kill/stand-down-direction** — the silent class of §3, which BRENT's deploy-side finding structurally could not surface. That direction skew is the screen's main result and it survived the correction below.

### 4b. ⚠️ THE SCREEN OVER-FLAGGED, AND WHY — a correction worth more than the rows it removed

The §2 semantic screen was run first on **grep context** (the gate line ± a few characters). Then I read each candidate's surrounding text. **Three of four verdicts moved** — VIOLET **up** to the strongest finding in the set, OSPREY row 6 and TERRY row 7 **down to cleared.**

Both downgrades have the identical cause: **the gate's designer had already seen the asymmetry, reasoned about it in writing on the adjacent line, and accepted it deliberately** — OSPREY at `:145` (*"a strike-pause alone is see-saw noise"*), TERRY at `:35` (*"row-count is the easy number to reach and the misleading one"*). From the gate line alone, a **deliberately-accepted** asymmetry and an **unnoticed** one are **byte-for-byte identical.** The rationale is what distinguishes them, and it never lives inside the condition.

⇒ **Screen rule, now part of the method:** *read the gate's stated rationale before flagging it; a conjunction with a written justification on the adjacent line is presumed deliberate until the justification is shown wrong.* Skipping this converts a cheap structural screen into a false-positive generator aimed at exactly the agents who documented their reasoning most carefully — **it punishes the good behaviour**, and it would have sent two packets telling careful owners to re-examine decisions they had already made better than I had.

**The upgrade came from the same read.** VIOLET's finding — a **disjunctive arm against a conjunctive disarm** — is invisible at the gate line, because the defect is not *in* the stand-down clause; it is in the **relationship** between `:112` and `:117`, five lines apart. **Neither leg-level base-rating nor a per-line screen finds it.** That is a fourth defect type:

> **D4 — ASYMMETRIC ARM/DISARM.** A state machine whose entry condition is disjunctive and whose exit condition is conjunctive is a **ratchet**, and `P(enter) ≫ P(exit)` holds **for any legs at all**, correlated or independent. No base rate is required; it is arithmetic on the connectives. **Test: count the connectives on the way in and on the way out.** Asymmetry in that direction is the defect. *(Symmetric or reversed — conjunctive entry, disjunctive exit — is the conservative and usually correct shape.)*

D4 is cheaper to test than D1, D2 and D3 combined, and unlike them it needs no domain knowledge whatsoever.

---

## 5. MECHANISM RULING — **not a sweep.** Stock + flow + a free standing detector.

PROME offered: recurring sweep / one-shot audit / PAT checklist line. **Ruling: one-shot for the stock, a registration requirement for the flow, and a live counter as the standing detector. No sixth recurring sweep.**

**Why not a recurring sweep** — a gate does not rot on a calendar. It is defective **at specification time** and stays exactly as defective until someone re-specs it; re-reading it in 21 days finds the same answer at standing cost. Cadence is the wrong trigger for a defect with no time dependence. *(One genuine time-dependence exists — the correlation structure between legs can shift with regime — but that is caught at re-spec, and by the counter below, without a standing sweep.)*

| Layer | Mechanism | Owner | Cost |
|---|---|---|---|
| **Stock** (existing gates) | The §4 screen — **done** — routed as task packets; each owner runs the conditional base rate on their own series | screen: me · numbers: owners | one pass |
| **Flow** (new / re-specced gates) | Blueprint requirement: a compound gate ships with `P(all legs \| trigger state)`, or an explicit "not base-rated" admission | agent, at registration | ~minutes |
| **Standing** | **The armed-but-never-opened counter** (below) | agent, free | ~zero |

### 5b. The standing detector — count it, don't sweep for it

**The observable already exists and nobody was reading it:** BRENT's gate was shut on **11 of 11** post-arm sessions, live, in real time. Three years of backtest confirmed what one live counter would have shown inside two weeks.

> **Rule:** any gate with an arming/trigger state carries a **sessions-armed-and-unopened counter**. When it exceeds the arm's own expiry window (or ~10 sessions if no expiry), the gate is presumed **D1-defective until base-rated** — it does not silently continue.

This beats a sweep on every axis: it fires exactly when the defect is real, costs nothing when it isn't, and needs no calendar. **It also retro-fits §3's silent class** — a kill gate gets the same counter keyed to *"days since the kill's precondition was first met."*

⚠️ **Note the second-order guard, or the counter recreates the bug:** the counter must trip on the **arm** state, not on a *further* condition. A counter gated on "armed AND still relevant" is itself a compound gate and inherits D1. Count the plain arm.

---

## 6. ⚠️ SELF-IMPLICATING FINDING — my own blueprint prescribes the construct with no counterweight

`BLUEPRINTS/market-agent.md` §3 line 53 reads, in full:

> **Conjunction triggers** (LIQUID): compound `A AND B` where a single metric would knee-jerk.

That is the *only* fleet-level guidance on compound gates, it is unambiguously a recommendation, and it carries **no satisfiability caveat of any kind.** Every agent building a gate to the blueprint was told to use a conjunction and told nothing about testing whether the conjunction can open. **The construct is right and the guidance was half-written** — the anti-knee-jerk motive is sound, which is precisely why the missing half went unnoticed for as long as it did.

Amendment lands at §3 (satisfiability) and §4 (the kill-direction severity note). **n=1 of a class worth watching in my own files: a blueprint line that recommends a mechanism without stating its failure mode is a defect generator, not neutral.**

---

## 7. DISPOSITIONS

**Mine, done this session:** this doc · PAT-072 · blueprint §3/§4 amendment · PROME reply.

**Task packets owed (owners run the numbers — domain data, not my lane):**

| To | Ask | Weight |
|---|---|---|
| **VIOLET** | row 4 — the **D4 ratchet**: arms 1-of-3, stands down 3-of-3. Two sub-asks: is the asymmetry deliberate? and `P(all three benign \| escalated)`. Carries the §3 severity note. | 🔴 the real one |
| **OSPREY** | row 5 only — has any 60d window ever satisfied *"all three channels quiet"*? Narrow; two alternate exit routes exist. **Explicitly withdraws** my Channel-1/2 flag with the reason. | 🟡 |
| **TERRY** | row 7 — **design affirmed, no re-spec asked.** Only: the gate has no counter/expiry, so an unreachable second leg reads as *"still gathering data"* indefinitely. | 🟢 note |

**Not proposed:** any edit to those gates. Re-scoping a kill/deploy criterion is domain judgment — the Falsification Sweep's dispositions rule applies verbatim (PAT-036's pre-approval does **not** extend here).

---

## 8. RUN LOG

| Date | Event |
|---|---|
| 2026-07-30 | Design ruled; screen run (6 agents, 9 gates, 4 candidates); PAT-072 banked; blueprint amended; PROME replied. Owner packets pending. |
