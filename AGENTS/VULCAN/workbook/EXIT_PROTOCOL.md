# VULCAN — Exit Protocol & Falsification Rail

**Kill rail re-derived: 2026-08-13** *(first authored — VULCAN carried no kill tree, no EXIT_PROTOCOL and no dated falsification surface across its 16-file inventory from build 2026-07-10 until today. Flagged by DAEDALUS at the 8/7 Production Review as the one genuine F5 gap in the fleet; Market-L3 requires one, blueprint §4 ★. Reference shape: FALCON `workbook/EXIT_PROTOCOL.md` 7/30.)*

**This file holds kill/exit conditions and nothing else.** `STATUS.md` is canonical for scores and live reads; `workbook/PREDICTIONS.tsv` is canonical for registered prediction text. **Where a kill condition is also a registered prediction, this file REFERENCES it by ID and does NOT restate it** — a condition written in two places drifts in one of them.

> ### Why the distinction this file turns on
> **CHANNEL-KILL ≠ THESIS-KILL.** A strong memory quarter kills S2's live bearish read; it does not touch the concentration thesis, which migrates to S1/S3. §1 is the thesis. §2 is per-channel. Never report a channel death as a thesis death, and never let a surviving thesis excuse a dead channel from being re-scored.

---

## 1. THESIS KILL — the specified form

**The thesis:** *the AI-capex buildout is the largest systemic vector in the tape — it concentrates index risk into a handful of megacaps, its FCF math gates HENRY's HEN-36, its compute demand collides with a supply-constrained grid, and its supply chain funnels through Taiwan.*

⚠️ **The prior sentence (STATUS:133) was unusable and this replaces it.** It read: *"Thesis dies only if AI-capex re-accelerates AND concentration unwinds cleanly AND memory stays healthy — multi-quarter, testable at each earnings stack."* Three legs, **no levels, no windows, no instruments, no session counts, no from-state** — the PAT-072 shape that fails silently because it can never be evaluated. Each leg below now carries a number, an instrument, a window and the state it is measured FROM.

| # | Leg | From-state (2026-08-13) | Kill condition | Instrument | Window | Met? |
|---|---|---|---|---|---|:---:|
| **1** | **AI-capex re-accelerates** | FY26 aggregate 4-name guide **~$735-760B economic** (VULCAN-01 HIT 7/31), vs 2025's ~$410B | FY27 aggregate guide implies **≥ +40% YoY** off the FY26 base (i.e. **≥ ~$1.03T**), against a consensus that expects decel to ~+25% | **Governed by `VULCAN-10`'s registered text — read it in `PREDICTIONS.tsv`, do not restate here.** Jan-2027 company guides, not analyst estimates | resolves **2027-02-15** | ❌ |
| **2** | **Concentration unwinds cleanly** | **Mag-7 32.98% of S&P 500 [SPY fund weight, 2026-08-20, issuer-primary]** — ⚠️ *from-state MEASURED 8/21, was an aggregator's ~32.5% until then* | Mag-7 share falls to **≤28%** and holds **3+ consecutive months**, with **no VIX print >30** and **no SPX drawdown >15%** anywhere in that window — "cleanly" means the risk leaves without the repricing | **`tools/mag7.py` → `workbook/MAG7_SERIES.tsv`** — SSGA's daily SPY holdings file (issuer-primary), append-only, content-vintage, fail-loud, validated each run with zero free parameters. ⚠️ **A FUND weight, not an S&P DJI INDEX weight** (the committee publishes no free constituent weights) — quote the basis. ⚠️ **Alphabet has TWO classes in the index (GOOGL + GOOG) and both count; dropping one understates by ~2.4pp.** *(Was aggregator-cited and flagged 'the weakest instrument on the rail' from 7/12 until 2026-08-21 — that gap is now closed.)* VIX/drawdown are **VIOLET's numbers; the owner's value governs** | continuous; re-read every closeout | ❌ |
| **3** | **Memory stays healthy** | DRAM contract **rising** (3Q26 fcst +13-18% QoQ); spot **rising** (DDR5 **$52.70**, DDR4 **$87.72**, 8/13); MU FQ3 GM **84.6%** | DRAM contract price growth stays **≥ 0% QoQ for 4 consecutive quarters** (3Q26, 4Q26, 1Q27, 2Q27) — i.e. no roll through mid-2027 | TrendForce contract series + MU FQ4/FQ1 prints (SEC-primary) | through **2027-06-30** | ⚠️ **CURRENTLY TRUE** |

### 🔴 THESIS-KILL STATUS 2026-08-21 (re-evaluated at closeout): **1 of 3 legs currently satisfied — UNCHANGED, and re-checked rather than restated.**

**Leg 1 (capex re-accelerates ≥+40% YoY):** NOT met, not yet observable — resolves at the Jan-2027 guides (`VULCAN-10`). **Leg 2 (Mag-7 ≤28%, 3+ months, no VIX>30, no SPX drawdown >15%):** NOT met — **Mag-7 32.98%** [SPY holdings, 8/20, own pull], nowhere near; **the instrument is no longer the weak point — it was pulled at an issuer primary on 8/21 and is now retained by `tools/mag7.py` → `workbook/MAG7_SERIES.tsv`.** ⚠️ Basis is a **FUND** weight, not an S&P DJI **index** weight (the committee publishes no free constituent weights; spglobal 403s) — quote it as such. ⚠️ **And the number is closer to a band than the old figure implied: 32.98% sits 0.019pp under the 33% yellow line, which is inside the basis noise — treat it as AT the line.** *(That is a threshold-proximity note about S1's banded rule, not about this kill leg, which needs ≤28% and is nowhere near.)* **Leg 3 (memory stays healthy, DRAM contract ≥0% QoQ for 4 straight quarters through 2027-06-30):** **STILL MET at the only observation available** — spot rose again this session (DDR5 **$54.10 +0.62%** · DDR4 **$91.07 +0.54%**, 8/21), the 3Q26 contract forecast is still positive, and the −25% roll rule is *further* from firing than on 8/3. **Only 1 of the leg's 4 quarters has been observed; 3 remain.** ⚠️ **Nothing this session moved the count, and the count moving is not the test of whether it was checked** — it was checked leg by leg against current instruments, which is the point of the closeout re-evaluation.

### 🔴 THESIS-KILL RE-EVALUATION 2026-08-21 **EVENING** (pass 9 closeout) — **STILL 1 of 3, and this time the rail was actually RE-READ rather than the count restated.**

⚠️ **Why this entry exists at all:** across passes 7-8 I wrote *"thesis-kill still 1 of 3"* into three commit messages and a NEXUS brief **without opening this file.** The count was correct — but a **restated** count is not a **re-evaluated** one, and the distinction is the entire point of step 3. `finding_record_of_an_action_is_not_the_action`, caught on myself at the last step of the day.

**Leg-by-leg, against today's evidence:**

| Leg | Kill condition | Today | Met? |
|---|---|---|:---:|
| **1** AI-capex re-accelerates | FY27 aggregate ≥ +40% YoY (≈ ≥$1.03T) | **Not yet observable** — no FY27 aggregate guide exists; resolves at the Jan-2027 guides (`VULCAN-10`). ⚠️ The NVDA 8-K does **not** touch this: leg 1 grades the **four hyperscalers**, and NVDA is not one of them | **NO** |
| **2** Concentration unwinds cleanly | Mag-7 ≤28%, 3+ months, no VIX>30, no SPX drawdown >15% | **Mag-7 32.98%** [SPY fund weight, 8/20, unchanged today] — **4.98pp above the kill level.** ⚠️ Breadth **broadening** (+5.18pp, 97.6th pctile) is *directionally* toward an unwind but the leg grades the **SHARE**, and the share has not moved | **NO** |
| **3** Memory stays healthy | DRAM contract ≥0% QoQ for 4 consecutive quarters | Spot **still rising 8/21** (DDR5 **$54.10** +0.62%, DDR4 **$91.07** +0.54%); contract still rising, still decelerating | **YES** |

**⇒ 1 of 3. Unchanged, and the unchanged-ness is now evidenced rather than asserted.**

### 🆕 Does the 8/17 NVDA 8-K move any kill condition? **No — and one channel moved AWAY from death.**

- **Thesis legs:** none. It is not a hyperscaler capex guide (leg 1), not an index-share move (leg 2), not a memory price (leg 3).
- **S3 channel-kill** — *"grid constraint stops binding: interconnection clears faster than load is added for 2 consecutive planning cycles"* — the 8-K **adds ~4.25 GW of IT load in PJM territory** (+~3.8 GW optional). That pushes **directly against** S3's death condition. ⇒ **S3 is more alive, not less.** ⚠️ Do not convert that into a queue number without WATT: *IT load* is a third quantity, and the site may already sit inside the 55 GW.
- **S5 channel-kill:** unaffected on the letter — this is a **private contract**, not the regulator-mandated collateral or priced new issue S5's bands grade. **Evidence strengthened, no kill condition approached, score held at 3.**

**Dated rewrite trigger: NOT DUE.** Fires on the FIRST of {MU FQ4 ~9/29 · the 9/30 resolutions · 2026-11-15}; earliest is ~39 days out and is a registered `docket/CATALYSTS.tsv` row, so it will surface at boot rather than depending on memory.

⚠️ **From-states deliberately NOT refreshed.** Leg 3's from-state still reads the **8/13** spot prices even though 8/21 prices exist and are higher. **That is correct: a from-state is a FROZEN reference.** Moving it because newer data exists would silently re-baseline the test and destroy the comparison the leg is built on. *(Leg 2's from-state WAS changed on 8/21 — that was a **correction** of an aggregator error, not a re-baseline. The two look identical in a diff and are not the same act.)*

---

### 🔴 THESIS-KILL RE-EVALUATION 2026-08-27 **PM** (second closeout, Will-directed reconcile session) — **STILL 1 of 3, re-read leg by leg, and the session produced NO market datum that touches any leg.**

**Leg 1 (capex re-accelerates ≥+40% YoY):** unmet, not yet observable — resolves at the Jan-2027 guides (`VULCAN-10`). Unchanged.
**Leg 2 (Mag-7 ≤28%, 3+ months, no VIX>30, no SPX DD>15%):** unmet. Current reading refreshed to **32.9085%** [holdings as-of 8/26] from 32.87% [8/21] — **+0.04pp, and ~4.9pp from the ≤28% bar.** ⚠️ **The from-state stays 32.98% [8/20] — a market move never moves a from-state** (fourth consecutive session stating this; the 8/21 change was a *correction*, which is a different act that looks identical in a diff).
**Leg 3 (memory stays healthy):** **still MET.** No new datum this session — the morning's two opposite-signed 8/27 points ($279B procurement vs the DDR5 −0.12% turn) are already recorded above and neither is this leg's instrument (DRAM **contract**, −25% QoQ).

**⇒ STILL 1 of 3.** All three required; legs 1 and 2 unmet.

🆕 **A NEW INSTRUMENT NOW BEARS ON LEG 2, recorded because a kill leg gaining an instrument is worth more than a reading:** the sector-within-index decomposition (`workbook/LAYER_SERIES.tsv`, built today) says that over **63 trading days the index rose +2.34pp while the AI-hardware layer SUBTRACTED −0.35pp** and the hyperscalers −0.09pp. **That is directionally what leg 2 describes — concentration unwinding — measured for the first time as a CONTRIBUTION rather than a weight level.** ⚠️ **It does NOT move the leg:** leg 2's bar is a **weight ≤28% sustained 3+ months**, and a 63-day contribution drag is neither that metric nor that duration. **Logged as a second, independent way to watch leg 2 approach — not as evidence it has.**

**Dated rewrite trigger: NOT DUE — but it moved.** Fires on the FIRST of {MU FQ4 **~9/22, window opens 9/17** · the 9/30 resolutions · 2026-11-15}. **The earliest leg is now ~21-26 days out, a week nearer than the ~9/29 this file carried this morning** — see §7.

### 🔴 THESIS-KILL RE-EVALUATION 2026-08-27 (closeout step 3, after the NVDA print + 10-Q) — **STILL 1 of 3. And the counterintuitive result is that the session's BIGGEST datum pushed on the leg that is ALREADY MET — i.e. toward the thesis dying, not away from it.**

**Re-read leg by leg against today's material, not restated.**

| Leg | Today's material | Moves it? |
|---|---|:---:|
| **1 — AI-capex re-accelerates** (FY27 4-name guide ≥ +40% YoY ⇒ ≥ ~$1.03T) | NVDA guided **its own** Q3 revenue to **$108.0B ±2%**. ⚠️ **That is not the instrument.** Leg 1's instrument is the **Jan-2027 hyperscaler company guides** (VULCAN-10) — NVDA's print is a READ-THROUGH under this desk's standing S1 semantics. 📌 Noted without moving the leg: NVDA's **own** forward procurement ladder (**rem-FY27 $92B / FY28 $87B / FY29 $88B**) is supplier-side evidence that the buildout persists at scale — *relevant to the leg's eventual direction, not admissible as its measurement.* | **❌ NO — not yet observable** |
| **2 — Concentration unwinds cleanly** (Mag-7 ≤28% held 3+ months, no VIX>30, no SPX DD>15%) | **No new Mag-7 reading taken today.** Series content-vintage **2026-08-21 holdings, 32.87%** — gap to kill **4.87pp**. ⚠️ **`mag7.py` is deliberately being run POST-CLOSE alongside `semi_watch.py`** so both of today's readings share one basis and neither is an intraday sample taken after seeing the event. | **❌ NO — unchanged** |
| **3 — Memory stays healthy** (DRAM contract ≥0% QoQ, 4 consecutive quarters through 2027-06-30) | 🔴 **REINFORCED, AND THIS IS THE FINDING.** NVDA's supply-and-capacity commitments went **$119B → $279B in one quarter, *"primarily related to the procurement of memory"*** [KB-118]; the consumer leg shows memory is expensive enough to be **named as a drag on PC volume** by a supplier [KB-119]. Both say *memory is healthy*, which is **exactly what this leg requires.** 🔵 **RE-VERIFIED AND QUALIFIED 2026-09-06.** The CFO quote is REAL — re-verified at the primary myself (8-K acc `0001045810-26-000073` **Ex-99.2**, 1 hit, VULCAN own EDGAR pull) after WALTER's `SIG-W-20260904-001` ruled it existed in no primary. **It does; KB-118 stands.** 🔴 **BUT the 10-Q filed the SAME DAY describes the SAME commitments differently:** *"data center infrastructure systems, primarily memory **AND MANUFACTURING FACILITIES**"* (acc `0001045810-26-000075`, Note 10). **Neither document discloses the memory SHARE.** ⚠️ **And the hierarchy matters:** the 8-K states on its face that the CFO Commentary is **"furnished and shall not be deemed filed"** (§18), so the NARROW attribution is in a FURNISHED exhibit while the BROADER wording is in the FILED 10-Q. **Prefer the filed wording; quote the CFO line AS CFO commentary, never as the filing's operative words.** ⇒ **The $279B figure HOLDS. The memory-only reconciliation is NOT COMPUTABLE** — foundry/CoWoS/packaging sit inside the same undisclosed total. `FL-VULCAN-12` downgraded **LIVE → CANDIDATE**: direction intact, **cannot be SIZED**. **No score moves** — this weakens a supporting clause, not the −25% QoQ contract rule the channel grades on. [KB-147] 🔑 **THE LEG'S STATE DOES NOT MOVE AND THE REASON IS THE IMPORTANT PART: leg 3 grades on `DRAM contract ≥0% QoQ, 4 consecutive quarters`, NOT on NVDA's commitments.** The $279B was cited as *reinforcing evidence*, and it is that evidence which weakens — the leg's own criterion is untouched. **A weakened supporting argument is not a changed verdict**, and saying so explicitly is the difference between re-reading the rail and restating it. | **✅ STILL MET — but see the same-day counter-datum, and see the 9/6 qualification of the reinforcing evidence** |

> 🔴 **AMENDED LATER THE SAME DAY (2026-08-27), AND THE AMENDMENT IS THE HONEST PART.** The leg-3 row above was written in the morning off the $279B commitment alone. That afternoon the **physical spot leg turned: DDR5 −0.12%, the first decline in the retained series** (52.70 → 54.10 → 54.17 → **53.93**), with both legs now below VULCAN-16's frozen 8/24 pre-state. ⇒ **TWO 8/27 DATA POINTS, OPPOSITE DIRECTIONS, ON THE SAME LEG:** the $279B multi-year memory procurement says *memory is healthy* (leg 3 **more** satisfied — the L-24 inversion below still stands); the spot turn says *the physical market is softening* (leg 3 **less** satisfied). **VERDICT UNCHANGED — STILL MET, and the reason is that NEITHER datum is the leg's instrument:** leg 3 grades **DRAM CONTRACT ≥0% QoQ across four consecutive quarters**, and contract is still rising. Spot is not contract, and one session is not a quarter. ⚠️ **Recorded rather than quietly reconciled, because a leg I called 'REINFORCED' in the morning acquired a counter-datum by the afternoon and the row would otherwise read as one-sided.** 🔑 **The generalisable bit: a same-day amendment is the cheapest correction there is, and the only thing that makes it expensive is having already published the morning's version as settled.** ⚠️ **Leg 3's from-state (8/13 spot) is STILL not moved — and a turn in the data is precisely when that temptation is strongest.**


**⇒ STILL 1 of 3.** Legs 1 and 2 both unmet; the thesis requires **all three**.

### 🔑 THE INVERSION, WRITTEN DOWN BECAUSE IT IS EASY TO MISS WHEN A BIG DATUM ARRIVES

**Today's single most impressive number — NVDA committing $160B of incremental memory procurement in one quarter — is, ON THIS RAIL, evidence FOR the thesis dying.** Leg 3 is *"memory stays healthy,"* it is the one leg **already satisfied**, and today made it *more* satisfied.

⚠️ **This inverts the intuition the S2 channel work creates.** In the channel, a strong memory datum reads as *"S2 is rich with evidence."* On the kill rail, the same datum reads as *"one of the three conditions for my thesis being wrong is more firmly true."* **Both readings are correct and they point opposite ways — because the channel measures whether the mechanism is LIVE and the rail measures whether the thesis is DEAD, and a healthy memory market is evidence for the first *and* for the second.**

⇒ ***When a datum strengthens a channel, check whether it also strengthens a kill leg. A rail that only ever moves on bad news is a rail nobody is reading against their own position.*** [pairs with the 8/24 note that a −19% five-session move moved ZERO legs — the rail is insensitive to price action **by design**, and correspondingly sensitive to exactly this kind of structural datum.]

### 🆕 CHANNEL-KILL SWEEP 2026-08-27 — **none died; TWO moved further from death, and one is unevaluated by design**

- **S5 — ALIVE, and today argues hard against its death.** Kill needs *new issues clearing at/inside talk for 2 consecutive quarters* **AND** *no second jurisdiction*. **No AI-infra new issue priced today** — the **$500B is MOUs**, which is not a cleared issue in either direction. And NVDA now states in a filed document that its customers *"lack the ability to secure… investment-grade financing capacity."* **A channel whose death condition is "financing is easy" does not die on the day the biggest name says financing is the constraint.**
- **S3 — ALIVE and moved FURTHER from death, second consecutive session.** Kill needs interconnection clearing **faster than load is added** for 2 planning cycles; the 10-Q **adds ~4.25 GW of committed PJM IT load with a nine-phase schedule** (+~3.8 GW optional). **Load added, on a filed timetable.**
- **S4 — ALIVE.** Kill needs export controls **net loosening both directions** for 2 quarters AND TSMC YoY ≥+20%. Today's China datum is a **realised tightening** (NVDA DC-China <1% of revenue, guide assumes zero), not a loosening. TSMC cum **+37.0%** clears the second conjunct, but the first is unmet.
- **S1 — ALIVE.** Capex net RAISED; no two consecutive flat-or-down stacks.
- **S2 — NOT EVALUATED TODAY, AND SAID SO RATHER THAN ASSUMED.** Its kill is a **conjunction**: DRAM contract ≥0% QoQ 4 straight quarters **AND memory equity outperforming QQQ**. The first conjunct is trending true; **the second requires an equity cross-section I have deliberately not pulled until post-close.** ⚠️ **An unevaluated conjunct is not a satisfied one — the status stays ALIVE on the 8/24 evaluation, and this line exists so the gap is visible rather than papered over.**

**From-states NOT refreshed — third consecutive session.** Leg 2's stays **32.98% [8/20]**, leg 3's stays the **8/13** spot prices. ⚠️ **Today's temptation was specifically leg 3:** the $279B commitment is a *better* piece of evidence than the 8/13 spot print sitting in the from-state cell. **A from-state is a FROZEN reference and better evidence is not a reason to move it** — the new datum belongs in the *current-state* column and in KB, which is where it went.

**Dated rewrite trigger: NOT DUE.** Fires on the FIRST of {MU FQ4 ~9/29 · the 9/30 resolutions · 2026-11-15}; earliest **~33 days** out and registered in `docket/CATALYSTS.tsv`, so it surfaces at boot.

---

### 🔴 THESIS-KILL RE-EVALUATION 2026-09-06 (closeout step 3) — **STILL 1 of 3, re-read leg by leg, and NO market datum arrived this session that touches any leg.**

**Session type: a correction/consumption pass, not a measurement pass.** No new price, guide or filing was observed; three corrections were adjudicated and one instrument was encoded. **Saying that first matters, because a session with a lot of writing in it can read as a session with a lot of evidence in it.**

- **Leg 1 — FY27 aggregate capex guide ≥ +40% YoY.** **UNMET.** No hyperscaler guided this session; the 7/31 cluster remains the last observation. **From-state unchanged.**
- **Leg 2 — Mag-7 ≤ 28% held 3+ months.** **UNMET, and the gap is at its widest in the retained series.** Mag-7 **33.5528%** [holdings 2026-09-01] — the level moved *away* from the kill threshold on 9/2 and nothing has re-measured it since. ⚠️ **The series is 5 days old and the next reading is not scheduled** — `mag7.py` has no pre-committed cadence, unlike `semi_watch.py`. **Named as a gap, not papered over.**
- **Leg 3 — memory stays healthy** (DRAM contract ≥0% QoQ, 4 consecutive quarters). **STILL MET.** 🔵 **The reinforcing EVIDENCE was qualified today** — the NVDA `$119B → $279B` attribution is real at the primary but the memory *share* is undisclosed (see the leg-3 row above, KB-147). 🔑 **The leg's own criterion is the DRAM contract series, not NVDA's commitments, so the state does not move. A weakened supporting argument is not a changed verdict.**
  ⚠️ **Counter-pressure that also did NOT move it:** HBM3E spot at ~4–5× LTA with capacity reportedly locked (KB-148) is *consistent with* memory being healthy, but it is a **spot** read on a thin residual float and the leg grades on **contract**. **Not counted in either direction.**

**⇒ STILL 1 of 3. All three are required; legs 1 and 2 are unmet and leg 2 moved further from meeting.**

⚠️ **THE HONEST NOTE ON THIS RE-READ:** the count has now read `1 of 3` for **six consecutive evaluations** (8/13 → 8/21 → 8/24 → 8/27 ×2 → 9/2 → 9/6). *"A count that never moves is a count nobody is checking"* is this file's own warning, so: **it was re-read leg by leg today, and the reason it does not move is legible — leg 3 is the only satisfied leg and it grades on a contract series that has not turned, while legs 1 and 2 need a capex cut and a ~5.5pp concentration collapse respectively.** Both are large, dated, and instrumented. **The count is stable because the world is, not because the rail is unread.**

**Dated rewrite trigger: NOT DUE — 24 calendar / 17 trading days out.** Fires on the FIRST of {MU FQ4 · the 9/30 resolutions · 2026-11-15}. **MU FQ4 is CONFIRMED 2026-09-30 16:30 ET**, so the first two legs COINCIDE and the trigger date is **2026-09-30**. ⚠️ **The print lands AFTER the close on that date**, so the rewrite — like the four prediction grades — is realistically a **2026-10-01** action. Registered in `docket/CATALYSTS.tsv`.

---

### 🔴 THESIS-KILL RE-EVALUATION 2026-08-24 (PROME-spawned session, closeout step 3) — **STILL 1 of 3. And the headline is that the fastest semi de-rate in this desk's record moved NOTHING on this rail — which is the rail working, not the rail failing.**

| Leg | Kill condition | Today (2026-08-24, own live pulls) | Met? |
|---|---|---|:---:|
| **1** AI-capex re-accelerates | FY27 aggregate ≥ +40% YoY (≈ ≥$1.03T) | **Not yet observable** — no FY27 aggregate guide exists; resolves at the Jan-2027 guides (`VULCAN-10`). ⚠️ **NVDA's 8/26 print does NOT touch this either:** leg 1 grades the **four hyperscalers**, and NVDA is not one of them — its print is a read-through, not a trigger | **NO** |
| **2** Concentration unwinds cleanly | Mag-7 ≤28%, 3+ months, no VIX>30, no SPX drawdown >15% | **Mag-7 32.8683%** [SSGA SPY holdings as-of 8/21, own fetch 8/24] — **4.87pp above the kill level** (was 4.98pp on 8/21). ⚠️ **The 0.11pp move is a genuine MARKET move toward the kill, and it is noise against a 4.87pp gap.** Breadth **+5.17pp, 97.6th pctile** — still *directionally* toward an unwind, but the leg grades the **SHARE** | **NO** |
| **3** Memory stays healthy | DRAM contract ≥0% QoQ for 4 consecutive quarters | Spot **rose again 8/24** (DDR5 **$54.17** +0.12%, DDR4 **$91.32** +0.27%) — series highs; contract still rising, still decelerating. **Still only 1 of the leg's 4 quarters observed; 3 remain** | **YES** |

**⇒ 1 of 3. Unchanged — and re-read, not restated** (the failure mode this step exists to catch, caught on myself 8/21).

### 🔑 Why a −19% five-session move in WDC moves ZERO kill legs, stated because it looks like it should

**The three legs grade a capex GUIDE, an index SHARE, and a CONTRACT price. None of them is an equity drawdown.** A violent de-rate in memory/semicap equities is **not an input to any of them** — it is the *repricing*, and this rail deliberately grades the *mechanism*. **A rail that moved on this tape would be a rail keyed to price action, which is the thing it was built not to be.** ⚠️ **The inverse caution is equally live: "no leg moved" must never be reported as "nothing happened."** Something large happened; §1 of today's memo says what, and it belongs to the channel reads, not to the kill rail.

### 🆕 Does today's de-rate move any CHANNEL-kill? **Yes — and in the direction nobody would guess: S2 moved FURTHER FROM death.**

- **S2's channel-kill is a CONJUNCTION:** *DRAM contract ≥0% QoQ for 4 straight quarters* **AND** *memory equity outperforms QQQ over the same span.* The first conjunct is currently true; **the second is now emphatically false** — memory **−5.05%** vs QQQ **+3.45%** on the rolling month, a **8.5pp** underperformance. ⇒ **S2's death condition is further from firing than it was on 8/21.** *(Same shape as the 8/17 8-K pushing S3 away from ITS death, logged 8/21.)*
- ⚠️ **AND THE DISTINCTION THAT MATTERS, because collapsing it would be a real error: S2's LEADING INDICATOR is disarmed while S2's CHANNEL is more alive than ever.** Those are two different objects — the indicator is a *timing* instrument, the channel-kill is an *existence* test. **A disarmed indicator is not a dying channel, and today is the cleanest example this desk has produced of the two moving in opposite directions at once.**
- **S1 channel-kill** (two consecutive stacks guiding capex flat-or-down with no index repricing): untouched — no capex guide landed. **S3/S4/S5:** untouched today.

**From-states deliberately NOT refreshed, again, and the reason is sharper today.** Leg 2's from-state still reads **32.98% [8/20]** and leg 3's still reads the **8/13** spot prices. **Today's 32.87% is the CURRENT reading, not a new from-state.** ⚠️ **This is exactly the case the 8/21 note warned about and it is easy to get wrong right now:** leg 2's from-state *was* legitimately changed on 8/21 — because it was **correcting an aggregator error**. Today's −0.11pp is a **market move**. **A correction may move a from-state; a market move never may** — and in a diff the two edits are indistinguishable.

**Dated rewrite trigger: NOT DUE.** Fires on the FIRST of {MU FQ4 ~9/29 · the 9/30 resolutions · 2026-11-15}; earliest ~36 days out and registered in `docket/CATALYSTS.tsv`, so it surfaces at boot.

---

### (2026-08-13 record — retained) THESIS-KILL STATUS: **1 of 3 legs currently satisfied.**

**Leg 3 is met right now and my files have never said so.** Memory *is* healthy — every price leg is rising, the last two prints were records, Micron says 2027 will be tighter than 2026, and the −25% QoQ roll rule is nowhere near firing. Writing the rail is what surfaced it. This is not a reason to soften the leg: a conjunctive kill with one leg standing is the honest state, and the correct response is to say so, not to re-word the leg until the count reads 0.

**What this does NOT mean:** one leg of a three-way conjunction is not a third of a kill. Legs 1 and 2 are the load-bearing ones — the thesis is about capex and concentration, and memory is the channel most likely to resolve benignly on its own without touching either.

---

## 2. CHANNEL KILL — per-channel, with the migration path

**A channel death must name where its evidence goes.** A channel that dies into nothing was never a channel.

| Ch | Channel-kill condition | Migration path on death | Status |
|---|---|---|:---:|
| **S1** | Two consecutive quarterly stacks (≥2 of 4 names each) guide capex **flat-or-down YoY** with **no** index-level repricing — the buildout ends without the unwind | Thesis leg 1 fires; concentration mechanism migrates to **VIOLET** as a pure vol call and VULCAN's seat loses its core | **ALIVE** — capex net RAISED 7/31, agg ~$735-760B |
| **S2** | DRAM contract **≥0% QoQ for 4 straight quarters** AND memory equity outperforms QQQ over the same span — the cycle neither rolls nor is repriced | Cost-push evidence migrates to **S1** (capex-cost line) and **CARL** (goods); the cycle-roll read dies, the concentration thesis does not | **ALIVE, and this is the channel under active pressure** — see §3 |
| **S3** | Grid constraint stops binding: PJM/ERCOT interconnection clears faster than load is added for **2 consecutive planning cycles** | Migrates to **WATT** entirely; VULCAN retains only the capex→MW conversion | **ALIVE** — ERCOT queue frozen under audit (KB-085) |
| **S4** | Export controls **net loosen** in both directions for **2 consecutive quarters** AND TSMC monthly revenue YoY stays ≥+20% | Dies to a watch-line; kinetic risk stays **HAWK's** | **ALIVE** — genuinely two-sided; the cleanest independent root |
| **S5** | AI-infra new issues clear **at or inside talk** for **2 consecutive quarters** AND no second jurisdiction writes an IG threshold into a utility tariff | Financing evidence migrates to **LIQUID** (spread tells) and **BROCK** (private credit); VULCAN keeps only the obligations mechanism | **ALIVE** — DDTL 5.5 cleared **+100bp** wide of the prior identical facility (KB-075) |

---

## 3. ⚠️ THE CHANNEL UNDER ACTIVE PRESSURE — S2, stated against myself

The 8/3 S2 upgrade 2 → 3 rested on **two** stated legs. **One of them has failed.**

- **Leg A — contract-price second derivative:** 3Q26 forecast **+13-18% DRAM / +10-15% NAND** vs 2Q26's +58-63% / +70-75%. ⚠️ *general* vs *server* DRAM — the deceleration survives the perimeter mismatch, the magnitude does not. **INTACT, untouched.**
- **Leg B — the equity de-rate as a LEADING indicator:** ~~❌ **FAILED.** It retraced in 10 days and the decoupling flipped sign (KB-071). A leading indicator that round-trips inside two weeks was a drawdown.~~ ⚠️ **REVISED 2026-08-21 — "FAILED" WAS WRONG, AND SO WAS THE EVIDENCE FOR IT.** The 8/3→8/13 "retrace" was measured over a window **starting at the drawdown's own lowest close** (MU $829.50, 8/3). Extremum-anchored windows manufacture the move they measure; that window cannot carry the verdict. **Corrected status: UNRESOLVED, not failed.** Three bases, reported together because they disagree and **the disagreement is the finding**: **(a)** rolling-1mo, the only window fixed *before* the data — spread **+19.02 → +13.14 → +4.54pp**, narrowing; **(b)** peak-to-current — **KLAC −38.6% · MU −19.1%** vs **QQQ −4.6%**, de-rate large and intact; **(c)** YTD — the complex is **+45% to +483%**, so a 30% drawdown off a parabolic June top is arithmetic, not a roll. **The indicator STAYS DISARMED, on a better reason: it has no specified basis**, and one that fires / un-fires / re-fires across three consecutive readings is measuring my window choice, not the market. ⚠️ **Deliberately NOT re-armed on the 8/18-19 re-fire, which agreed with my prior.** **Pre-specified re-arm rule, registered now and grading at 9/30: rolling-1mo spread ≥ +10pp for 3+ consecutive readings AND further contract deceleration.** [KB-089/091/092 · **L-17**]

**Two known perimeter defects now sit under S2's standing −25% QoQ rule, and they point in opposite directions:**
1. **DRAM/NAND split** (KB-057): 2027 DRAM supply stays tight while NAND eases. A NAND roll with a DRAM hold resolves VULCAN-02 ambiguously.
2. **Consumer/datacentre split** (KB-081, new): the deceleration is a **consumer** story (affordability limits) while the **datacentre** leg *tightens* (customers price-insensitive). The rule is measured on a blend that is bifurcating.

⇒ **The rule is now known to be measured on a blend of two blends.** Registered here rather than fixed: **do not rewrite VULCAN-02's gate** (own L-11 rule (b)); grade it on the DRAM leg per KB-057 and record a SPLIT as a spec failure against me, not a HIT.

---

## 4. LIVE BIDIRECTIONAL FLIP — re-registered 2026-08-13

⚠️ **The previous flip (STATUS:135) named the 7/22-7/29 earnings stack and EXPIRED with it on 7/31.** No successor existed for 13 days. A rail whose only flip has expired is a rail that cannot fire.

**Next resolver: MU FQ4 FY26 — 🔴 CONFIRMED 2026-09-30, 2:30 p.m. Mountain (16:30 ET), AFTER THE CLOSE.** *(Micron press release 2026-08-26 16:01 ET; `date_class: confirmed`.)*

> ~~*Superseded: "**~2026-09-22** (window opens 09-17; re-dated 2026-08-27 from ~9/29 — derived from MU's own filing history, `fiscalYearEnd=0903` is a NOMINAL EDGAR marker not a period end. Still MODELED)*"*~~ · ~~*"Headroom to the 9/30 resolve date is now ~6-13 days, not ~1."*~~
> 🔴 **BOTH SENTENCES WERE WRONG AND THE SECOND WAS THE DANGEROUS ONE — corrected 2026-09-02, struck not deleted.** The re-derivation assumed a **52-week** fiscal year; MU runs **52/53-week** years and FY2026 is a **53-week** year ending **2026-09-03** — so `fiscalYearEnd=0903` was **RIGHT**, and the counter-example (FY2020 10-K `period_end` **2020-09-03**) was sitting in this desk's own `workbook/EDGAR_SEEN.tsv` the whole time. **Micron had already announced 9/30 on 8/26, the day BEFORE I re-derived it.**
> ⚠️ **REAL HEADROOM IS ~0 HOURS, NOT 6-13 DAYS.** VULCAN-02/-11/-12/-14 all resolve **2026-09-30** and the print lands **after that day's close** ⇒ **any grade needing the FQ4 print is a 2026-10-01 action** (registered in `docket/CATALYSTS.tsv`). The 8/27 note said the change *"moved in my favour, which is exactly when to be most careful about touching anything else"* — and then banked it. [KB-135]

| Direction | What must be observed at MU FQ4 | Consequence |
|---|---|---|
| **Confirms the bearish read** | GM expansion **stalls** (≤84.6% GAAP) or FQ1 guide below FQ4 on the same basis | The LTA/presold ceiling is real and measured; the memory maker does not capture the rent; S2's cost-push into S1 and CARL is the live transmission |
| **Falsifies it** | GM expands **≥+2.0pp** (≥86.6%) **and** FQ1 guided at-or-above | "Presold" is a moat, not a ceiling; **retract KB-055's framing and correct WALTER, CARL and HENRY**, all of whom got the ceiling version from me |

**Governed by `VULCAN-12`'s registered text — read it in `PREDICTIONS.tsv`.** Explicit NO-VERDICT band and the GAAP-vs-non-GAAP basis discipline live there.

---

## 5. STANDING COUNTER-EVIDENCE — the steelman, kept verbatim

**Held here because a rail without the strongest case against its own thesis is an advocacy document.** These do **not** kill S1's mechanism (mechanism-vs-thermometer, L-02) — they attack its **repricing leg**, and S1's value depends on the unwind being *un*-priced:

- **SIG-W-20260521-013** — NVDA's 5/20 print **absorbed clean**: post-print IV crushed *below* 20d realized, **no tail bid**; the vol surface "decisively faded the catalyst" (conf 0.85).
- **SIG-W-20260622-009** — **record SOXL outflow / record SOXS inflow**: semi bearishness is **already crowded** (conf 0.75).
- **SIG-W-20260702-016** — GS Prime Book: hedge funds de-grossed US tech at a **~−4σ record** (wk ending 6/25) with **NO cascade** (conf 0.75) — the unwind may be **partly pre-positioned**.
- **Added 2026-08-13 — the market kept funding it, twice.** MSFT **+8.88%** and AMZN **+7%** AH both *rewarded* capex RAISES (VULCAN-09 MISS-DOWNGRADE), and CoreWeave raised FY26 capex to **$35-39B against $12.4-13.2B of revenue** — ~3× revenue at a ~10.4% marginal cost of debt — and the equity paid it **+16-18%**.

---

## 6. CROSS-AGENT THRESHOLDS — I do not own these numbers

| Threshold | Owner | My use |
|---|---|---|
| Mag-7 weight, vol/dispersion expression, Path-B | **VIOLET** | I own the *mechanism*; VIOLET owns the repricing. Reconcile to ONE figure |
| AI-credit **spread tells** (HY/IG, CDS, the GS/JPM basket) | **LIQUID** | I own capex/fundamentals + obligations. **Do NOT maintain a parallel spread series** — KB-075's DDTL ladder is routed to LIQUID, not kept as a rival index |
| PJM/ERCOT power price, firm-vs-forecast GW | **WATT** | Adopt verbatim *(wording corrected 2026-09-06)*: **~55 GW = aggregate utility-reported forecast (self-reported, non-coincident, contains duplication) · ~32 GW = firm coincident-peak (PJM-vetted). Never net, never average. Neither is an interconnection-queue nameplate figure — the ~250 GW generation queue is a third population** (KB-087 + KB-146) |
| China capacity timeline (CXMT, bit output) | **ZHAO** | The number that would move S2's shortage premise; unsized, requested |
| Taiwan kinetic | **HAWK** | S4's tail; I own only the semiconductor consequence |

---

## 7. TIME-BASED REVIEW + DATED REWRITE TRIGGER

> 🔴 **TRIGGER DATE RE-DERIVED 2026-09-02: it is now 2026-09-30.** The trigger fires on the FIRST of {MU FQ4 · the 9/30 resolutions · 2026-11-15}. With MU FQ4 **confirmed 2026-09-30**, the first two legs **COINCIDE**. It had been riding at **~9/22** on my own wrong derivation.
> 🔑 **A "whichever is FIRST" trigger inherits EVERY leg's date, so re-dating one leg silently re-dates the trigger — and this is the SECOND time that has bitten this rail in seven days, in opposite directions.** On 8/27 the trigger moved EARLIER (~9/29 → ~9/22) and nothing said so; on 9/2 it moved LATER (~9/22 → 9/30) for the same structural reason. **The defect is not the direction, it is that a derived leg feeds a trigger with no publisher.** *(`[[finding_retired_threshold_has_no_publisher]]`.)*

- **Re-read this file at every closeout falsification check.** Boot↔closeout symmetry: what you read at boot, you write back.
- **Thesis-kill leg count: re-evaluate every closeout.** It is `1 of 3` today; a count that never moves is a count nobody is checking.
- **⚠️ DATED REWRITE TRIGGER** *(per `[[finding_banner_is_a_warning_not_a_fix]]` — a banner without a date is a deferral)*: **rewrite this rail when MU FQ4 prints (🔴 **CONFIRMED 2026-09-30 16:30 ET**, issuer press release 2026-08-26 — ~~*was ~2026-09-22 on my own wrong 52-week derivation; corrected 2026-09-02, see §4*~~), OR when VULCAN-02/-11/-12 resolve (2026-09-30), OR by 2026-11-15 — whichever is FIRST.** 🔴 **THE EARLIEST LEG MOVED A WEEK EARLIER ON 2026-08-27 AND THIS LINE DID NOT FOLLOW IT UNTIL THE PM CLOSEOUT.** The MU re-date was propagated to `CATALYSTS.tsv`, `PREDICTIONS.tsv`, `STATUS.md` and the NEXUS brief the same morning — **and not to the trigger that DEPENDS on it.** ⚠️ **A 'whichever is FIRST' trigger inherits every one of its legs' dates, so re-dating any leg silently re-dates the trigger; nothing announces it** [`finding_dated_carry_item_has_no_expiry_check`]. **This is a FORWARD COMMITMENT, not a from-state — moving it is required, and it is NOT the act the from-state rule forbids.** Three of five channel-kill rows and the entire §4 flip resolve inside that window, so a rail read after it without a rewrite is describing a phase that has passed.
- **If a future reader finds this file asserting a live condition that has already resolved, that is the failure this rail exists to prevent** — and the §3 self-indictment is the model for how to record it.
