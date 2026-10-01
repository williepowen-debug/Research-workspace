# EXIT_PROTOCOL — dated log archive (moved 2026-10-01)

⛔ **History. Never cite an entry here as a current kill state.** The live rail is `workbook/EXIT_PROTOCOL.md`; its §1 table, §2 table, §4b flip and §7 trigger are canonical. Every block below was moved **verbatim** (byte-for-byte lines) on 2026-10-01 by the PROME-spawned VULCAN session (DOCKET L547), because the live file was over the 54,250 B physical read cap and is re-read at every closeout. Archived by ENTRY, read first for forward commitments: the only ones found were the 9/30 rewrite trigger (FIRED, its successor written live in §7) and the owed items in §C (discharged or re-dated live, see §8 of the live file).

Integrity line: see the README-free footer at the end of this file (crc32 of each block, computed by the command at write time).

---

## §A — from live §1: dated thesis-kill re-evaluations 2026-08-21 → 2026-08-27 + the 2026-08-13 from-state record (live lines 26–153 as of commit HEAD before 2026-10-01)

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

## §C — from live §7: the 9/30 trigger's derivation history (live lines 238–239 and 243–244) + §8's owed-line

> 🔴 **TRIGGER DATE RE-DERIVED 2026-09-02: it is now 2026-09-30.** The trigger fires on the FIRST of {MU FQ4 · the 9/30 resolutions · 2026-11-15}. With MU FQ4 **confirmed 2026-09-30**, the first two legs **COINCIDE**. It had been riding at **~9/22** on my own wrong derivation.
> 🔑 **A "whichever is FIRST" trigger inherits EVERY leg's date, so re-dating one leg silently re-dates the trigger — and this is the SECOND time that has bitten this rail in seven days, in opposite directions.** On 8/27 the trigger moved EARLIER (~9/29 → ~9/22) and nothing said so; on 9/2 it moved LATER (~9/22 → 9/30) for the same structural reason. **The defect is not the direction, it is that a derived leg feeds a trigger with no publisher.** *(`[[finding_retired_threshold_has_no_publisher]]`.)*

- **⚠️ DATED REWRITE TRIGGER** *(per `[[finding_banner_is_a_warning_not_a_fix]]` — a banner without a date is a deferral)*: **rewrite this rail when MU FQ4 prints (🔴 **CONFIRMED 2026-09-30 16:30 ET**, issuer press release 2026-08-26 — ~~*was ~2026-09-22 on my own wrong 52-week derivation; corrected 2026-09-02, see §4*~~), OR when VULCAN-02/-11/-12 resolve (2026-09-30), OR by 2026-11-15 — whichever is FIRST.** 🔴 **THE EARLIEST LEG MOVED A WEEK EARLIER ON 2026-08-27 AND THIS LINE DID NOT FOLLOW IT UNTIL THE PM CLOSEOUT.** The MU re-date was propagated to `CATALYSTS.tsv`, `PREDICTIONS.tsv`, `STATUS.md` and the NEXUS brief the same morning — **and not to the trigger that DEPENDS on it.** ⚠️ **A 'whichever is FIRST' trigger inherits every one of its legs' dates, so re-dating any leg silently re-dates the trigger; nothing announces it** [`finding_dated_carry_item_has_no_expiry_check`]. **This is a FORWARD COMMITMENT, not a from-state — moving it is required, and it is NOT the act the from-state rule forbids.** Three of five channel-kill rows and the entire §4 flip resolve inside that window, so a rail read after it without a rewrite is describing a phase that has passed.
- 🆕 **2026-09-29: the rewrite was SPLIT, deliberately.** The half that does NOT depend on Micron was done **before** the print (§8): kill conditions are only honest when written before the event that could test them. **The Micron-dependent half — §4, and the S1/S2/S5 channel-kill rows in §2 that resolve inside the window — is still owed on 2026-10-01**, AFTER grading from `workbook/MU_FQ4_RESOLVER.md` and never rewritten before it. PROME's disinflationary-productivity falsifier (open since 8/21) is also still owed then.

**Still owed 2026-10-01 (Micron-dependent, NOT touched today):** grade §4 from the resolver sheet; rewrite the §2 channel-kill rows that resolve in the window; retire §4 into history and make §4b live; PROME's disinflationary-productivity falsifier. ⚠️ **This file is 50.9 KB and is re-read in full at every closeout.** The 10/01 pass should move the dated re-evaluation log (most of the bytes) to `archive/`, verbatim, and keep §1–§8 live.

---

## §B — from live §7: re-evaluations 2026-09-06 PM → 2026-09-25 (live lines 249–287)

### 🔴 THESIS-KILL RE-EVALUATED 2026-09-06 PM (closeout step 3): **1 of 3 — UNCHANGED, and re-checked leg by leg rather than restated.**
- **Leg 1 — FY27 aggregate capex guide ≥ +40% YoY: NOT satisfied.** Guides were RAISED, not cut (agg ~$735-760B econ vs the $710-725B baseline), but nothing this session tested the +40% bar. No new capex datum was observed.
- **Leg 2 — Mag-7 ≤28% held 3+ months: NOT satisfied, and the gap is WIDE.** Mag-7 **33.5528%** [SSGA holdings 2026-09-01], i.e. moving AWAY from the kill level. ⚠️ **Not re-measured this session — the reading is 9/1 vintage.** The instrument now has a pre-committed Friday cadence from **9/11**, which is what makes the *"3+ months"* duration test gradeable at all.
- **Leg 3 — memory stays healthy: STILL TRUE.** No memory datum arrived since the 8/27 spot read; the single DDR5 **−0.12%** tick is one observation of rounding scale and does not unmake it.
- **Nothing this session bore on any leg — no price, guide or filing was observed.** The day's seven findings were all in instruments and instructions. **A session that produces no market datum cannot move a kill count, and saying so is the re-evaluation.**
- **Dated rewrite trigger: NOT DUE — 2026-09-30, 24 calendar / 17 trading days out**, on the FIRST of {MU FQ4 (CONFIRMED 9/30 16:30 ET) · the 9/30 resolutions · 2026-11-15}; the first two legs COINCIDE. ⚠️ **The print lands AFTER the close, so the rewrite is realistically a 2026-10-01 action**, registered in `docket/CATALYSTS.tsv`.


### 🔴 THESIS-KILL RE-EVALUATION 2026-09-11 (PROME-spawned session, DOCKET L323; closeout step 3): **STILL 1 of 3 — re-read leg by leg. Two market data arrived (TSMC August, ORCL Q1) and neither touches a leg; one INSTRUMENT was added to the rail's evidence base.**
- **Leg 1 — FY27 aggregate hyperscaler capex guide ≥ +40% YoY:** UNCHANGED, not met. No hyperscaler guided this session; ORCL's Q1 FY27 capex of **$28.5B in one quarter** (vs $8.5B YoY) [KB-156] is a *print*, not a guide, and ORCL is not in the aggregate this leg is defined on. **NOT MET.**
- **Leg 2 — Mag-7 ≤28% held 3+ months:** UNCHANGED, not met. Last reading 33.5528% [holdings 9/1]; the 9/11 post-close `mag7.py` slot was NOT taken by this pre-close session (flagged to PROME). **NOT MET — and further from met than any prior read.**
- **Leg 3 — memory stays healthy:** **STILL TRUE.** TSMC August cumulative +39.3% (re-accelerating) [KB-157]; DRAM Q2 industry revenue +59.5% QoQ (a REVENUE figure, not price — KB-161); Kioxia's CEO resisting NAND hikes is a *stance*, not a print. Nothing here is a memory roll. **MET (1 of 3).**
- 🆕 **What was ADDED to the rail, not to the count:** `VULCAN-17` registers NVDA's guarantee-COMMITMENT level as an instrument with a pre-committed reading rule (KB-153/154). On the Lucent/Nortel base rate the commitment level was the only thing that led, and NVDA's is going vertical ⇒ **build phase, not break phase** — which is the same direction as leg 3 and does not move leg 1 or 2. A **(iv) withdrawal** reading at the ~11/19 10-Q would be the first instrument on this desk pointing the other way; it is registered so it cannot be read as prudence when it arrives.
- **Dated rewrite trigger: NOT DUE — 2026-09-30, 19 calendar / 13 trading days out** (boot leg 6, holiday-correct). MU FQ4 prints after the close that day ⇒ the rewrite is a **2026-10-01** action. Unchanged.

---

### 🔴 THESIS-KILL RE-EVALUATION 2026-09-13 (PROME-spawned session, DOCKET L330; closeout step 3): **STILL 1 of 3 — re-read leg by leg, and the honest headline is that NO market datum reached this desk at all.**

Markets have been shut since the Friday 2026-09-11 close and **this session took no instrument reading** (all three instruments are on a pre-committed cadence whose next slot is 09-18 post-close). So the legs are re-read against the same evidence the 9/11 pass used, and the re-read is recorded rather than the count restated.

- **Leg 1 — AI-capex re-accelerates (FY27 aggregate ≥ +40% YoY):** **NO.** Not yet observable; no FY27 aggregate guide exists. Resolves at the Jan-2027 guides (`VULCAN-10`). Untouched.
- **Leg 2 — Mag-7 ≤28% held 3+ months:** **NO**, and the distance is large: last read **33.5528%** (holdings as-of 2026-09-01). ⚠️ **The instrument did NOT read this week — `mag7.py` slot 1 (9/11 post-close) is MISSED**, the first miss on a cadence registered only days earlier. **A duration leg on a series with a hole in it is the defect this cadence was created to prevent, so the miss is recorded here and not only in STATUS.** Next slot 09-18.
- **Leg 3 — Memory stays healthy (DRAM contract ≥0% QoQ, 4 consecutive quarters):** **✅ STILL MET.** Nothing arrived that touches the leg's own instrument, which is **contract**, not spot. ⚠️ The spot series has now missed **four** pre-committed readings (8/27 post-close · 8/28 · 09-04 · 09-11) and its last row is 2026-08-24 — **20 days stale**. That does not move the leg; it narrows the evidence the 9/30 grade will rest on.

🔑 **The one thing that DID change on this rail is an instrument, not a leg** — and it changed by acquiring a **limit**: `GPU-PANEL-01` was frozen, and the freeze established that **the GPU on-demand-minus-contract spread cannot be computed from public sources** (no vendor publishes a 12-month H100 price). **A kill rail gaining a known blind spot is worth recording at the same weight as a kill rail gaining an instrument** — this one is neither a leg nor evidence for one, but it bounds what future evidence can look like.

- **Dated rewrite trigger: NOT DUE — 2026-09-30, 17 calendar / 13 trading days out** (boot leg 6, holiday-correct). Fires on the FIRST of {MU FQ4 (CONFIRMED 2026-09-30 16:30 ET) · the 9/30 resolutions · 2026-11-15}; the first two legs COINCIDE. MU prints AFTER the close that day ⇒ the rewrite is realistically a **2026-10-01** action. Unchanged.

### 🔴 THESIS-KILL RE-EVALUATION 2026-09-25 (Will-launched boot after a 12-day dark period; closeout step 3): **STILL 1 of 3 — re-read leg by leg. A lot of market data arrived; none of it touches a leg. The week's stress sits in FINANCING STRUCTURE, which no thesis-kill leg measures.**
- **Leg 1 — FY27 aggregate capex guide ≥ +40% YoY: NOT satisfied.** No hyperscaler guided in the window. The 9/12–14 "pace the frontier" shock (Amodei essay; Altman IPO "not 2026") moved PRICES: SOX −5.9% on 9/14, memory fully retraced by 9/23. It moved no budget: 0 capex, contract or DC-plan changes found [KB-166]. Next test is the late-October cluster.
- **Leg 2 — Mag-7 ≤28% held 3+ months: NO.** Last read **33.5528%** (holdings 2026-09-01). ⚠️ **Not re-measured since:** `mag7.py` slots 1 (9/11) and 2 (9/18) were MISSED to dark periods. The distance is too large for a 5pp move to be plausible in the gap, but the instrument is **24 days stale**, and the leg is a DURATION test that an irregular series cannot grade.
- **Leg 3 — memory stays healthy: TRUE.** TrendForce **lifted** its 4Q26 contract outlook; the sell-side sees DRAM ASP +16.5% QoQ in 3Q → +5.4% in 4Q (a decelerating RISE); MU **$1,089.56** (9/25 10:13 ET) ahead of 9/30 [KB-172].

🔑 **What changed on the rail is a GAP it does not cover, recorded at the same weight as a leg moving:** ORCL's off-BS DC leases went **$260B → $288B** in a quarter; ORCL invoked **force majeure** on a 2.45 GW site to defer rent against power delay; ORCL 5Y CDS hit a record (single-source 221.78bp); and **SB Energy — the party behind NVDA's $105B guaranty — postponed its IPO** [KB-167/168/173/174]. **None of the three kill legs can see any of it:** they test SCALE (capex growth), CONCENTRATION (Mag-7 weight) and PRICE (memory). This is the same mis-fit STATUS has flagged on S5's bands since 9/11: **the stress is arriving as structure, and the rail measures levels.** ⇒ **Carry into the 10/01 rewrite as a named requirement:** the rewritten rail needs at least one **structure** leg, or it must say in writing why the thesis cannot be killed on that axis (the same honest-unfalsifiable option already owed to PROME for the disinflationary path).

- **S2 channel note:** the pre-specified 9/30 re-arm rule is **UNGRADEABLE by construction** (6 of 8 slots missed). This is not a channel kill and not a channel revival; S2's standing −25% QoQ rule is unaffected and far from firing.
- **Dated rewrite trigger: NOT DUE — 2026-09-30, 5 calendar / 3 trading days out** (boot leg 6). MU prints AFTER that close ⇒ the rewrite is a **2026-10-01** action. Unchanged.

---

**Footer (computed at write time):** §A 128 lines crc32 `0x17de3eb9` · §C 5 lines crc32 `0x1a695073` · §B 39 lines crc32 `0x6a43ed45`. Live file before the move: 311 lines, 56347 B.
